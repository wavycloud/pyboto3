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

def create_campaign(ApplicationId=None, WriteCampaignRequest=None):
    """
    Creates or updates a campaign.
    
    
    :example: response = client.create_campaign(
        ApplicationId='string',
        WriteCampaignRequest={
            'AdditionalTreatments': [
                {
                    'MessageConfiguration': {
                        'APNSMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'DefaultMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'GCMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        }
                    },
                    'Schedule': {
                        'EndTime': 'string',
                        'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY',
                        'IsLocalTime': True|False,
                        'QuietTime': {
                            'End': 'string',
                            'Start': 'string'
                        },
                        'StartTime': 'string',
                        'Timezone': 'string'
                    },
                    'SizePercent': 123,
                    'TreatmentDescription': 'string',
                    'TreatmentName': 'string'
                },
            ],
            'Description': 'string',
            'HoldoutPercent': 123,
            'IsPaused': True|False,
            'Limits': {
                'Daily': 123,
                'Total': 123
            },
            'MessageConfiguration': {
                'APNSMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'DefaultMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'GCMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                }
            },
            'Name': 'string',
            'Schedule': {
                'EndTime': 'string',
                'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY',
                'IsLocalTime': True|False,
                'QuietTime': {
                    'End': 'string',
                    'Start': 'string'
                },
                'StartTime': 'string',
                'Timezone': 'string'
            },
            'SegmentId': 'string',
            'SegmentVersion': 123,
            'TreatmentDescription': 'string',
            'TreatmentName': 'string'
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type WriteCampaignRequest: dict
    :param WriteCampaignRequest: [REQUIRED] Used to create a campaign.
            AdditionalTreatments (list) -- Treatments that are defined in addition to the default treatment.
            (dict) -- Used to create a campaign treatment.
            MessageConfiguration (dict) -- The message configuration settings.
            APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP   Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK   Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL   The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            DefaultMessage (dict) -- The default message for all channels.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP   Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK   Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL   The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP   Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK   Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL   The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            
            Schedule (dict) -- The campaign schedule.
            EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
            Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE, HOURLY, DAILY, WEEKLY, MONTHLY
            IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
            QuietTime (dict) -- The time during which the campaign sends no messages.
            End (string) -- The default end time for quiet time in ISO 8601 format.
            Start (string) -- The default start time for quiet time in ISO 8601 format.
            StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
            Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
            SizePercent (integer) -- The allocated percentage of users for this treatment.
            TreatmentDescription (string) -- A custom description for the treatment.
            TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
            
            Description (string) -- A description of the campaign.
            HoldoutPercent (integer) -- The allocated percentage of end users who will not receive messages from this campaign.
            IsPaused (boolean) -- Indicates whether the campaign is paused. A paused campaign does not send messages unless you resume it by setting IsPaused to false.
            Limits (dict) -- The campaign limits settings.
            Daily (integer) -- The maximum number of messages that the campaign can send daily.
            Total (integer) -- The maximum total number of messages that the campaign can send.
            MessageConfiguration (dict) -- The message configuration settings.
            APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP   Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK   Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL   The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            DefaultMessage (dict) -- The default message for all channels.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP   Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK   Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL   The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP   Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK   Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL   The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            
            Name (string) -- The custom name of the campaign.
            Schedule (dict) -- The campaign schedule.
            EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
            Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE, HOURLY, DAILY, WEEKLY, MONTHLY
            IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
            QuietTime (dict) -- The time during which the campaign sends no messages.
            End (string) -- The default end time for quiet time in ISO 8601 format.
            Start (string) -- The default start time for quiet time in ISO 8601 format.
            StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
            Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
            SegmentId (string) -- The ID of the segment to which the campaign sends messages.
            SegmentVersion (integer) -- The version of the segment to which the campaign sends messages.
            TreatmentDescription (string) -- A custom description for the treatment.
            TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
            

    :rtype: dict
    :return: {
        'CampaignResponse': {
            'AdditionalTreatments': [
                {
                    'Id': 'string',
                    'MessageConfiguration': {
                        'APNSMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'DefaultMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'GCMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        }
                    },
                    'Schedule': {
                        'EndTime': 'string',
                        'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY',
                        'IsLocalTime': True|False,
                        'QuietTime': {
                            'End': 'string',
                            'Start': 'string'
                        },
                        'StartTime': 'string',
                        'Timezone': 'string'
                    },
                    'SizePercent': 123,
                    'State': {
                        'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'
                    },
                    'TreatmentDescription': 'string',
                    'TreatmentName': 'string'
                },
            ],
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'DefaultState': {
                'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'
            },
            'Description': 'string',
            'HoldoutPercent': 123,
            'Id': 'string',
            'IsPaused': True|False,
            'LastModifiedDate': 'string',
            'Limits': {
                'Daily': 123,
                'Total': 123
            },
            'MessageConfiguration': {
                'APNSMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'DefaultMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'GCMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                }
            },
            'Name': 'string',
            'Schedule': {
                'EndTime': 'string',
                'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY',
                'IsLocalTime': True|False,
                'QuietTime': {
                    'End': 'string',
                    'Start': 'string'
                },
                'StartTime': 'string',
                'Timezone': 'string'
            },
            'SegmentId': 'string',
            'SegmentVersion': 123,
            'State': {
                'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'
            },
            'TreatmentDescription': 'string',
            'TreatmentName': 'string',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) -- 201 response
    CampaignResponse (dict) -- Campaign definition
    AdditionalTreatments (list) -- Treatments that are defined in addition to the default treatment.
    (dict) -- Treatment resource
    Id (string) -- The unique treatment ID.
    MessageConfiguration (dict) -- The message configuration settings.
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    
    
    Schedule (dict) -- The campaign schedule.
    EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
    Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE, HOURLY, DAILY, WEEKLY, MONTHLY
    IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
    QuietTime (dict) -- The time during which the campaign sends no messages.
    End (string) -- The default end time for quiet time in ISO 8601 format.
    Start (string) -- The default start time for quiet time in ISO 8601 format.
    
    
    StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
    Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
    
    
    SizePercent (integer) -- The allocated percentage of users for this treatment.
    State (dict) -- The treatment status.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    TreatmentDescription (string) -- A custom description for the treatment.
    TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
    
    
    
    
    ApplicationId (string) -- The ID of the application to which the campaign applies.
    CreationDate (string) -- The date the campaign was created in ISO 8601 format.
    DefaultState (dict) -- The status of the campaign's default treatment. Only present for A/B test campaigns.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    Description (string) -- A description of the campaign.
    HoldoutPercent (integer) -- The allocated percentage of end users who will not receive messages from this campaign.
    Id (string) -- The unique campaign ID.
    IsPaused (boolean) -- Indicates whether the campaign is paused. A paused campaign does not send messages unless you resume it by setting IsPaused to false.
    LastModifiedDate (string) -- The date the campaign was last updated in ISO 8601 format.
    Limits (dict) -- The campaign limits settings.
    Daily (integer) -- The maximum number of messages that the campaign can send daily.
    Total (integer) -- The maximum total number of messages that the campaign can send.
    
    
    MessageConfiguration (dict) -- The message configuration settings.
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    
    
    Name (string) -- The custom name of the campaign.
    Schedule (dict) -- The campaign schedule.
    EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
    Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE, HOURLY, DAILY, WEEKLY, MONTHLY
    IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
    QuietTime (dict) -- The time during which the campaign sends no messages.
    End (string) -- The default end time for quiet time in ISO 8601 format.
    Start (string) -- The default start time for quiet time in ISO 8601 format.
    
    
    StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
    Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
    
    
    SegmentId (string) -- The ID of the segment to which the campaign sends messages.
    SegmentVersion (integer) -- The version of the segment to which the campaign sends messages.
    State (dict) -- The campaign status. An A/B test campaign will have a status of COMPLETED only when all treatments have a status of COMPLETED.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    TreatmentDescription (string) -- A custom description for the treatment.
    TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
    Version (integer) -- The campaign version number.
    
    
    
    
    
    """
    pass

def create_import_job(ApplicationId=None, ImportJobRequest=None):
    """
    Creates or updates an import job.
    
    
    :example: response = client.create_import_job(
        ApplicationId='string',
        ImportJobRequest={
            'DefineSegment': True|False,
            'ExternalId': 'string',
            'Format': 'CSV'|'JSON',
            'RegisterEndpoints': True|False,
            'RoleArn': 'string',
            'S3Url': 'string',
            'SegmentId': 'string',
            'SegmentName': 'string'
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type ImportJobRequest: dict
    :param ImportJobRequest: [REQUIRED]
            DefineSegment (boolean) -- Sets whether the endpoints create a segment when they are imported.
            ExternalId (string) -- A unique, custom ID assigned to the IAM role that restricts who can assume the role.
            Format (string) -- The format of the files that contain the endpoint definitions. Valid values: CSV, JSON
            RegisterEndpoints (boolean) -- Sets whether the endpoints are registered with Amazon Pinpoint when they are imported.
            RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the Amazon S3 location that contains the endpoints to import.
            S3Url (string) -- A URL that points to the location within an Amazon S3 bucket that contains the endpoints to import. The location can be a folder or a single file. The URL should follow this format: s3://bucket-name/folder-name/file-name Amazon Pinpoint will import endpoints from this location and any subfolders it contains.
            SegmentId (string) -- The ID of the segment to update if the import job is meant to update an existing segment.
            SegmentName (string) -- A custom name for the segment created by the import job. Use if DefineSegment is true.
            

    :rtype: dict
    :return: {
        'ImportJobResponse': {
            'ApplicationId': 'string',
            'CompletedPieces': 123,
            'CompletionDate': 'string',
            'CreationDate': 'string',
            'Definition': {
                'DefineSegment': True|False,
                'ExternalId': 'string',
                'Format': 'CSV'|'JSON',
                'RegisterEndpoints': True|False,
                'RoleArn': 'string',
                'S3Url': 'string',
                'SegmentId': 'string',
                'SegmentName': 'string'
            },
            'FailedPieces': 123,
            'Failures': [
                'string',
            ],
            'Id': 'string',
            'JobStatus': 'CREATED'|'INITIALIZING'|'PROCESSING'|'COMPLETING'|'COMPLETED'|'FAILING'|'FAILED',
            'TotalFailures': 123,
            'TotalPieces': 123,
            'TotalProcessed': 123,
            'Type': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- 201 response
    ImportJobResponse (dict) --
    ApplicationId (string) -- The unique ID of the application to which the import job applies.
    CompletedPieces (integer) -- The number of pieces that have successfully imported as of the time of the request.
    CompletionDate (string) -- The date the import job completed in ISO 8601 format.
    CreationDate (string) -- The date the import job was created in ISO 8601 format.
    Definition (dict) -- The import job settings.
    DefineSegment (boolean) -- Sets whether the endpoints create a segment when they are imported.
    ExternalId (string) -- A unique, custom ID assigned to the IAM role that restricts who can assume the role.
    Format (string) -- The format of the files that contain the endpoint definitions. Valid values: CSV, JSON
    RegisterEndpoints (boolean) -- Sets whether the endpoints are registered with Amazon Pinpoint when they are imported.
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the Amazon S3 location that contains the endpoints to import.
    S3Url (string) -- A URL that points to the location within an Amazon S3 bucket that contains the endpoints to import. The location can be a folder or a single file. The URL should follow this format: s3://bucket-name/folder-name/file-name Amazon Pinpoint will import endpoints from this location and any subfolders it contains.
    SegmentId (string) -- The ID of the segment to update if the import job is meant to update an existing segment.
    SegmentName (string) -- A custom name for the segment created by the import job. Use if DefineSegment is true.
    
    
    FailedPieces (integer) -- The number of pieces that have failed to import as of the time of the request.
    Failures (list) -- Provides up to 100 of the first failed entries for the job, if any exist.
    (string) --
    
    
    Id (string) -- The unique ID of the import job.
    JobStatus (string) -- The status of the import job. Valid values: CREATED, INITIALIZING, PROCESSING, COMPLETING, COMPLETED, FAILING, FAILED The job status is FAILED if one or more pieces failed to import.
    TotalFailures (integer) -- The number of endpoints that failed to import; for example, because of syntax errors.
    TotalPieces (integer) -- The total number of pieces that must be imported to finish the job. Each piece is an approximately equal portion of the endpoints to import.
    TotalProcessed (integer) -- The number of endpoints that were processed by the import job.
    Type (string) -- The job type. Will be Import.
    
    
    
    
    
    """
    pass

def create_segment(ApplicationId=None, WriteSegmentRequest=None):
    """
    Used to create or update a segment.
    
    
    :example: response = client.create_segment(
        ApplicationId='string',
        WriteSegmentRequest={
            'Dimensions': {
                'Attributes': {
                    'string': {
                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'Behavior': {
                    'Recency': {
                        'Duration': 'HR_24'|'DAY_7'|'DAY_14'|'DAY_30',
                        'RecencyType': 'ACTIVE'|'INACTIVE'
                    }
                },
                'Demographic': {
                    'AppVersion': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'DeviceType': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Make': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Model': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Platform': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'Location': {
                    'Country': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'UserAttributes': {
                    'string': {
                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                }
            },
            'Name': 'string'
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type WriteSegmentRequest: dict
    :param WriteSegmentRequest: [REQUIRED] Segment definition.
            Dimensions (dict) -- The segment dimensions attributes.
            Attributes (dict) -- Custom segment attributes.
            (string) --
            (dict) -- Custom attibute dimension
            AttributeType (string) -- The type of dimension: INCLUSIVE   Endpoints that match the criteria are included in the segment. EXCLUSIVE   Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            
            Behavior (dict) -- The segment behaviors attributes.
            Recency (dict) -- The recency of use.
            Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
            RecencyType (string) -- The recency dimension type: ACTIVE   Users who have used your app within the specified duration are included in the segment. INACTIVE   Users who have not used your app within the specified duration are included in the segment.
            
            Demographic (dict) -- The segment demographics attributes.
            AppVersion (dict) -- The app version criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE   Endpoints that match the criteria are included in the segment. EXCLUSIVE   Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            DeviceType (dict) -- The device type criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE   Endpoints that match the criteria are included in the segment. EXCLUSIVE   Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Make (dict) -- The device make criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE   Endpoints that match the criteria are included in the segment. EXCLUSIVE   Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Model (dict) -- The device model criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE   Endpoints that match the criteria are included in the segment. EXCLUSIVE   Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Platform (dict) -- The device platform criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE   Endpoints that match the criteria are included in the segment. EXCLUSIVE   Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Location (dict) -- The segment location attributes.
            Country (dict) -- The country filter according to ISO 3166-1 Alpha-2 codes.
            DimensionType (string) -- The type of dimension: INCLUSIVE   Endpoints that match the criteria are included in the segment. EXCLUSIVE   Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            UserAttributes (dict) -- Custom segment user attributes.
            (string) --
            (dict) -- Custom attibute dimension
            AttributeType (string) -- The type of dimension: INCLUSIVE   Endpoints that match the criteria are included in the segment. EXCLUSIVE   Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            
            Name (string) -- The name of segment
            

    :rtype: dict
    :return: {
        'SegmentResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Dimensions': {
                'Attributes': {
                    'string': {
                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'Behavior': {
                    'Recency': {
                        'Duration': 'HR_24'|'DAY_7'|'DAY_14'|'DAY_30',
                        'RecencyType': 'ACTIVE'|'INACTIVE'
                    }
                },
                'Demographic': {
                    'AppVersion': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'DeviceType': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Make': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Model': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Platform': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'Location': {
                    'Country': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'UserAttributes': {
                    'string': {
                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                }
            },
            'Id': 'string',
            'ImportDefinition': {
                'ExternalId': 'string',
                'Format': 'CSV'|'JSON',
                'RoleArn': 'string',
                'S3Url': 'string',
                'Size': 123
            },
            'LastModifiedDate': 'string',
            'Name': 'string',
            'SegmentType': 'DIMENSIONAL'|'IMPORT',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) -- 201 response
    SegmentResponse (dict) -- Segment definition.
    ApplicationId (string) -- The ID of the application to which the segment applies.
    CreationDate (string) -- The date the segment was created in ISO 8601 format.
    Dimensions (dict) -- The segment dimensions attributes.
    Attributes (dict) -- Custom segment attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    Behavior (dict) -- The segment behaviors attributes.
    Recency (dict) -- The recency of use.
    Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
    RecencyType (string) -- The recency dimension type: ACTIVE  Users who have used your app within the specified duration are included in the segment. INACTIVE  Users who have not used your app within the specified duration are included in the segment.
    
    
    
    
    Demographic (dict) -- The segment demographics attributes.
    AppVersion (dict) -- The app version criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    DeviceType (dict) -- The device type criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Make (dict) -- The device make criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Model (dict) -- The device model criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Platform (dict) -- The device platform criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    Location (dict) -- The segment location attributes.
    Country (dict) -- The country filter according to ISO 3166-1 Alpha-2 codes.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    UserAttributes (dict) -- Custom segment user attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    
    
    Id (string) -- The unique segment ID.
    ImportDefinition (dict) -- The import job settings.
    ExternalId (string) -- A unique, custom ID assigned to the IAM role that restricts who can assume the role.
    Format (string) -- The format of the endpoint files that were imported to create this segment. Valid values: CSV, JSON
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the endpoints in Amazon S3.
    S3Url (string) -- A URL that points to the Amazon S3 location from which the endpoints for this segment were imported.
    Size (integer) -- The number of endpoints that were successfully imported to create this segment.
    
    
    LastModifiedDate (string) -- The date the segment was last updated in ISO 8601 format.
    Name (string) -- The name of segment
    SegmentType (string) -- The segment type: DIMENSIONAL  A dynamic segment built from selection criteria based on endpoint data reported by your app. You create this type of segment by using the segment builder in the Amazon Pinpoint console or by making a POST request to the segments resource. IMPORT  A static segment built from an imported set of endpoint definitions. You create this type of segment by importing a segment in the Amazon Pinpoint console or by making a POST request to the jobs/import resource.
    Version (integer) -- The segment version number.
    
    
    
    
    
    """
    pass

def delete_apns_channel(ApplicationId=None):
    """
    Deletes the APNs channel for an app.
    
    
    :example: response = client.delete_apns_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :rtype: dict
    :return: {
        'APNSChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    """
    pass

def delete_campaign(ApplicationId=None, CampaignId=None):
    """
    Deletes a campaign.
    
    
    :example: response = client.delete_campaign(
        ApplicationId='string',
        CampaignId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type CampaignId: string
    :param CampaignId: [REQUIRED]

    :rtype: dict
    :return: {
        'CampaignResponse': {
            'AdditionalTreatments': [
                {
                    'Id': 'string',
                    'MessageConfiguration': {
                        'APNSMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'DefaultMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'GCMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        }
                    },
                    'Schedule': {
                        'EndTime': 'string',
                        'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY',
                        'IsLocalTime': True|False,
                        'QuietTime': {
                            'End': 'string',
                            'Start': 'string'
                        },
                        'StartTime': 'string',
                        'Timezone': 'string'
                    },
                    'SizePercent': 123,
                    'State': {
                        'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'
                    },
                    'TreatmentDescription': 'string',
                    'TreatmentName': 'string'
                },
            ],
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'DefaultState': {
                'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'
            },
            'Description': 'string',
            'HoldoutPercent': 123,
            'Id': 'string',
            'IsPaused': True|False,
            'LastModifiedDate': 'string',
            'Limits': {
                'Daily': 123,
                'Total': 123
            },
            'MessageConfiguration': {
                'APNSMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'DefaultMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'GCMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                }
            },
            'Name': 'string',
            'Schedule': {
                'EndTime': 'string',
                'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY',
                'IsLocalTime': True|False,
                'QuietTime': {
                    'End': 'string',
                    'Start': 'string'
                },
                'StartTime': 'string',
                'Timezone': 'string'
            },
            'SegmentId': 'string',
            'SegmentVersion': 123,
            'State': {
                'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'
            },
            'TreatmentDescription': 'string',
            'TreatmentName': 'string',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    CampaignResponse (dict) -- Campaign definition
    AdditionalTreatments (list) -- Treatments that are defined in addition to the default treatment.
    (dict) -- Treatment resource
    Id (string) -- The unique treatment ID.
    MessageConfiguration (dict) -- The message configuration settings.
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    
    
    Schedule (dict) -- The campaign schedule.
    EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
    Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE, HOURLY, DAILY, WEEKLY, MONTHLY
    IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
    QuietTime (dict) -- The time during which the campaign sends no messages.
    End (string) -- The default end time for quiet time in ISO 8601 format.
    Start (string) -- The default start time for quiet time in ISO 8601 format.
    
    
    StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
    Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
    
    
    SizePercent (integer) -- The allocated percentage of users for this treatment.
    State (dict) -- The treatment status.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    TreatmentDescription (string) -- A custom description for the treatment.
    TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
    
    
    
    
    ApplicationId (string) -- The ID of the application to which the campaign applies.
    CreationDate (string) -- The date the campaign was created in ISO 8601 format.
    DefaultState (dict) -- The status of the campaign's default treatment. Only present for A/B test campaigns.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    Description (string) -- A description of the campaign.
    HoldoutPercent (integer) -- The allocated percentage of end users who will not receive messages from this campaign.
    Id (string) -- The unique campaign ID.
    IsPaused (boolean) -- Indicates whether the campaign is paused. A paused campaign does not send messages unless you resume it by setting IsPaused to false.
    LastModifiedDate (string) -- The date the campaign was last updated in ISO 8601 format.
    Limits (dict) -- The campaign limits settings.
    Daily (integer) -- The maximum number of messages that the campaign can send daily.
    Total (integer) -- The maximum total number of messages that the campaign can send.
    
    
    MessageConfiguration (dict) -- The message configuration settings.
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    
    
    Name (string) -- The custom name of the campaign.
    Schedule (dict) -- The campaign schedule.
    EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
    Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE, HOURLY, DAILY, WEEKLY, MONTHLY
    IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
    QuietTime (dict) -- The time during which the campaign sends no messages.
    End (string) -- The default end time for quiet time in ISO 8601 format.
    Start (string) -- The default start time for quiet time in ISO 8601 format.
    
    
    StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
    Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
    
    
    SegmentId (string) -- The ID of the segment to which the campaign sends messages.
    SegmentVersion (integer) -- The version of the segment to which the campaign sends messages.
    State (dict) -- The campaign status. An A/B test campaign will have a status of COMPLETED only when all treatments have a status of COMPLETED.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    TreatmentDescription (string) -- A custom description for the treatment.
    TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
    Version (integer) -- The campaign version number.
    
    
    
    
    
    """
    pass

def delete_event_stream(ApplicationId=None):
    """
    Deletes the event stream for an app.
    
    
    :example: response = client.delete_event_stream(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] ApplicationId

    :rtype: dict
    :return: {
        'EventStream': {
            'ApplicationId': 'string',
            'DestinationStreamArn': 'string',
            'ExternalId': 'string',
            'LastModifiedDate': 'string',
            'LastUpdatedBy': 'string',
            'RoleArn': 'string'
        }
    }
    
    
    """
    pass

def delete_gcm_channel(ApplicationId=None):
    """
    Deletes the GCM channel for an app.
    
    
    :example: response = client.delete_gcm_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :rtype: dict
    :return: {
        'GCMChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Credential': 'string',
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    """
    pass

def delete_segment(ApplicationId=None, SegmentId=None):
    """
    Deletes a segment.
    
    
    :example: response = client.delete_segment(
        ApplicationId='string',
        SegmentId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type SegmentId: string
    :param SegmentId: [REQUIRED]

    :rtype: dict
    :return: {
        'SegmentResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Dimensions': {
                'Attributes': {
                    'string': {
                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'Behavior': {
                    'Recency': {
                        'Duration': 'HR_24'|'DAY_7'|'DAY_14'|'DAY_30',
                        'RecencyType': 'ACTIVE'|'INACTIVE'
                    }
                },
                'Demographic': {
                    'AppVersion': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'DeviceType': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Make': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Model': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Platform': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'Location': {
                    'Country': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'UserAttributes': {
                    'string': {
                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                }
            },
            'Id': 'string',
            'ImportDefinition': {
                'ExternalId': 'string',
                'Format': 'CSV'|'JSON',
                'RoleArn': 'string',
                'S3Url': 'string',
                'Size': 123
            },
            'LastModifiedDate': 'string',
            'Name': 'string',
            'SegmentType': 'DIMENSIONAL'|'IMPORT',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    SegmentResponse (dict) -- Segment definition.
    ApplicationId (string) -- The ID of the application to which the segment applies.
    CreationDate (string) -- The date the segment was created in ISO 8601 format.
    Dimensions (dict) -- The segment dimensions attributes.
    Attributes (dict) -- Custom segment attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    Behavior (dict) -- The segment behaviors attributes.
    Recency (dict) -- The recency of use.
    Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
    RecencyType (string) -- The recency dimension type: ACTIVE  Users who have used your app within the specified duration are included in the segment. INACTIVE  Users who have not used your app within the specified duration are included in the segment.
    
    
    
    
    Demographic (dict) -- The segment demographics attributes.
    AppVersion (dict) -- The app version criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    DeviceType (dict) -- The device type criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Make (dict) -- The device make criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Model (dict) -- The device model criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Platform (dict) -- The device platform criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    Location (dict) -- The segment location attributes.
    Country (dict) -- The country filter according to ISO 3166-1 Alpha-2 codes.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    UserAttributes (dict) -- Custom segment user attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    
    
    Id (string) -- The unique segment ID.
    ImportDefinition (dict) -- The import job settings.
    ExternalId (string) -- A unique, custom ID assigned to the IAM role that restricts who can assume the role.
    Format (string) -- The format of the endpoint files that were imported to create this segment. Valid values: CSV, JSON
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the endpoints in Amazon S3.
    S3Url (string) -- A URL that points to the Amazon S3 location from which the endpoints for this segment were imported.
    Size (integer) -- The number of endpoints that were successfully imported to create this segment.
    
    
    LastModifiedDate (string) -- The date the segment was last updated in ISO 8601 format.
    Name (string) -- The name of segment
    SegmentType (string) -- The segment type: DIMENSIONAL  A dynamic segment built from selection criteria based on endpoint data reported by your app. You create this type of segment by using the segment builder in the Amazon Pinpoint console or by making a POST request to the segments resource. IMPORT  A static segment built from an imported set of endpoint definitions. You create this type of segment by importing a segment in the Amazon Pinpoint console or by making a POST request to the jobs/import resource.
    Version (integer) -- The segment version number.
    
    
    
    
    
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

def get_apns_channel(ApplicationId=None):
    """
    Returns information about the APNs channel for an app.
    
    
    :example: response = client.get_apns_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :rtype: dict
    :return: {
        'APNSChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    """
    pass

def get_application_settings(ApplicationId=None):
    """
    Used to request the settings for an app.
    
    
    :example: response = client.get_application_settings(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :rtype: dict
    :return: {
        'ApplicationSettingsResource': {
            'ApplicationId': 'string',
            'LastModifiedDate': 'string',
            'Limits': {
                'Daily': 123,
                'Total': 123
            },
            'QuietTime': {
                'End': 'string',
                'Start': 'string'
            }
        }
    }
    
    
    """
    pass

def get_campaign(ApplicationId=None, CampaignId=None):
    """
    Returns information about a campaign.
    
    
    :example: response = client.get_campaign(
        ApplicationId='string',
        CampaignId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type CampaignId: string
    :param CampaignId: [REQUIRED]

    :rtype: dict
    :return: {
        'CampaignResponse': {
            'AdditionalTreatments': [
                {
                    'Id': 'string',
                    'MessageConfiguration': {
                        'APNSMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'DefaultMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'GCMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        }
                    },
                    'Schedule': {
                        'EndTime': 'string',
                        'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY',
                        'IsLocalTime': True|False,
                        'QuietTime': {
                            'End': 'string',
                            'Start': 'string'
                        },
                        'StartTime': 'string',
                        'Timezone': 'string'
                    },
                    'SizePercent': 123,
                    'State': {
                        'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'
                    },
                    'TreatmentDescription': 'string',
                    'TreatmentName': 'string'
                },
            ],
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'DefaultState': {
                'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'
            },
            'Description': 'string',
            'HoldoutPercent': 123,
            'Id': 'string',
            'IsPaused': True|False,
            'LastModifiedDate': 'string',
            'Limits': {
                'Daily': 123,
                'Total': 123
            },
            'MessageConfiguration': {
                'APNSMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'DefaultMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'GCMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                }
            },
            'Name': 'string',
            'Schedule': {
                'EndTime': 'string',
                'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY',
                'IsLocalTime': True|False,
                'QuietTime': {
                    'End': 'string',
                    'Start': 'string'
                },
                'StartTime': 'string',
                'Timezone': 'string'
            },
            'SegmentId': 'string',
            'SegmentVersion': 123,
            'State': {
                'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'
            },
            'TreatmentDescription': 'string',
            'TreatmentName': 'string',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    CampaignResponse (dict) -- Campaign definition
    AdditionalTreatments (list) -- Treatments that are defined in addition to the default treatment.
    (dict) -- Treatment resource
    Id (string) -- The unique treatment ID.
    MessageConfiguration (dict) -- The message configuration settings.
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    
    
    Schedule (dict) -- The campaign schedule.
    EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
    Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE, HOURLY, DAILY, WEEKLY, MONTHLY
    IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
    QuietTime (dict) -- The time during which the campaign sends no messages.
    End (string) -- The default end time for quiet time in ISO 8601 format.
    Start (string) -- The default start time for quiet time in ISO 8601 format.
    
    
    StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
    Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
    
    
    SizePercent (integer) -- The allocated percentage of users for this treatment.
    State (dict) -- The treatment status.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    TreatmentDescription (string) -- A custom description for the treatment.
    TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
    
    
    
    
    ApplicationId (string) -- The ID of the application to which the campaign applies.
    CreationDate (string) -- The date the campaign was created in ISO 8601 format.
    DefaultState (dict) -- The status of the campaign's default treatment. Only present for A/B test campaigns.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    Description (string) -- A description of the campaign.
    HoldoutPercent (integer) -- The allocated percentage of end users who will not receive messages from this campaign.
    Id (string) -- The unique campaign ID.
    IsPaused (boolean) -- Indicates whether the campaign is paused. A paused campaign does not send messages unless you resume it by setting IsPaused to false.
    LastModifiedDate (string) -- The date the campaign was last updated in ISO 8601 format.
    Limits (dict) -- The campaign limits settings.
    Daily (integer) -- The maximum number of messages that the campaign can send daily.
    Total (integer) -- The maximum total number of messages that the campaign can send.
    
    
    MessageConfiguration (dict) -- The message configuration settings.
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    
    
    Name (string) -- The custom name of the campaign.
    Schedule (dict) -- The campaign schedule.
    EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
    Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE, HOURLY, DAILY, WEEKLY, MONTHLY
    IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
    QuietTime (dict) -- The time during which the campaign sends no messages.
    End (string) -- The default end time for quiet time in ISO 8601 format.
    Start (string) -- The default start time for quiet time in ISO 8601 format.
    
    
    StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
    Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
    
    
    SegmentId (string) -- The ID of the segment to which the campaign sends messages.
    SegmentVersion (integer) -- The version of the segment to which the campaign sends messages.
    State (dict) -- The campaign status. An A/B test campaign will have a status of COMPLETED only when all treatments have a status of COMPLETED.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    TreatmentDescription (string) -- A custom description for the treatment.
    TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
    Version (integer) -- The campaign version number.
    
    
    
    
    
    """
    pass

def get_campaign_activities(ApplicationId=None, CampaignId=None, PageSize=None, Token=None):
    """
    Returns information about the activity performed by a campaign.
    
    
    :example: response = client.get_campaign_activities(
        ApplicationId='string',
        CampaignId='string',
        PageSize='string',
        Token='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type CampaignId: string
    :param CampaignId: [REQUIRED]

    :type PageSize: string
    :param PageSize: 

    :type Token: string
    :param Token: 

    :rtype: dict
    :return: {
        'ActivitiesResponse': {
            'Item': [
                {
                    'ApplicationId': 'string',
                    'CampaignId': 'string',
                    'End': 'string',
                    'Id': 'string',
                    'Result': 'string',
                    'ScheduledStart': 'string',
                    'Start': 'string',
                    'State': 'string',
                    'SuccessfulEndpointCount': 123,
                    'TimezonesCompletedCount': 123,
                    'TimezonesTotalCount': 123,
                    'TotalEndpointCount': 123,
                    'TreatmentId': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    ActivitiesResponse (dict) -- Activities for campaign.
    Item (list) -- List of campaign activities
    (dict) -- Activity definition
    ApplicationId (string) -- The ID of the application to which the campaign applies.
    CampaignId (string) -- The ID of the campaign to which the activity applies.
    End (string) -- The actual time the activity was marked CANCELLED or COMPLETED. Provided in ISO 8601 format.
    Id (string) -- The unique activity ID.
    Result (string) -- Indicates whether the activity succeeded. Valid values: SUCCESS, FAIL
    ScheduledStart (string) -- The scheduled start time for the activity in ISO 8601 format.
    Start (string) -- The actual start time of the activity in ISO 8601 format.
    State (string) -- The state of the activity. Valid values: PENDING, INITIALIZING, RUNNING, PAUSED, CANCELLED, COMPLETED
    SuccessfulEndpointCount (integer) -- The total number of endpoints to which the campaign successfully delivered messages.
    TimezonesCompletedCount (integer) -- The total number of timezones completed.
    TimezonesTotalCount (integer) -- The total number of unique timezones present in the segment.
    TotalEndpointCount (integer) -- The total number of endpoints to which the campaign attempts to deliver messages.
    TreatmentId (string) -- The ID of a variation of the campaign used for A/B testing.
    
    
    
    
    
    
    
    
    
    """
    pass

def get_campaign_version(ApplicationId=None, CampaignId=None, Version=None):
    """
    Returns information about a specific version of a campaign.
    
    
    :example: response = client.get_campaign_version(
        ApplicationId='string',
        CampaignId='string',
        Version='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type CampaignId: string
    :param CampaignId: [REQUIRED]

    :type Version: string
    :param Version: [REQUIRED]

    :rtype: dict
    :return: {
        'CampaignResponse': {
            'AdditionalTreatments': [
                {
                    'Id': 'string',
                    'MessageConfiguration': {
                        'APNSMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'DefaultMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'GCMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        }
                    },
                    'Schedule': {
                        'EndTime': 'string',
                        'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY',
                        'IsLocalTime': True|False,
                        'QuietTime': {
                            'End': 'string',
                            'Start': 'string'
                        },
                        'StartTime': 'string',
                        'Timezone': 'string'
                    },
                    'SizePercent': 123,
                    'State': {
                        'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'
                    },
                    'TreatmentDescription': 'string',
                    'TreatmentName': 'string'
                },
            ],
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'DefaultState': {
                'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'
            },
            'Description': 'string',
            'HoldoutPercent': 123,
            'Id': 'string',
            'IsPaused': True|False,
            'LastModifiedDate': 'string',
            'Limits': {
                'Daily': 123,
                'Total': 123
            },
            'MessageConfiguration': {
                'APNSMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'DefaultMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'GCMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                }
            },
            'Name': 'string',
            'Schedule': {
                'EndTime': 'string',
                'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY',
                'IsLocalTime': True|False,
                'QuietTime': {
                    'End': 'string',
                    'Start': 'string'
                },
                'StartTime': 'string',
                'Timezone': 'string'
            },
            'SegmentId': 'string',
            'SegmentVersion': 123,
            'State': {
                'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'
            },
            'TreatmentDescription': 'string',
            'TreatmentName': 'string',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    CampaignResponse (dict) -- Campaign definition
    AdditionalTreatments (list) -- Treatments that are defined in addition to the default treatment.
    (dict) -- Treatment resource
    Id (string) -- The unique treatment ID.
    MessageConfiguration (dict) -- The message configuration settings.
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    
    
    Schedule (dict) -- The campaign schedule.
    EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
    Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE, HOURLY, DAILY, WEEKLY, MONTHLY
    IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
    QuietTime (dict) -- The time during which the campaign sends no messages.
    End (string) -- The default end time for quiet time in ISO 8601 format.
    Start (string) -- The default start time for quiet time in ISO 8601 format.
    
    
    StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
    Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
    
    
    SizePercent (integer) -- The allocated percentage of users for this treatment.
    State (dict) -- The treatment status.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    TreatmentDescription (string) -- A custom description for the treatment.
    TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
    
    
    
    
    ApplicationId (string) -- The ID of the application to which the campaign applies.
    CreationDate (string) -- The date the campaign was created in ISO 8601 format.
    DefaultState (dict) -- The status of the campaign's default treatment. Only present for A/B test campaigns.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    Description (string) -- A description of the campaign.
    HoldoutPercent (integer) -- The allocated percentage of end users who will not receive messages from this campaign.
    Id (string) -- The unique campaign ID.
    IsPaused (boolean) -- Indicates whether the campaign is paused. A paused campaign does not send messages unless you resume it by setting IsPaused to false.
    LastModifiedDate (string) -- The date the campaign was last updated in ISO 8601 format.
    Limits (dict) -- The campaign limits settings.
    Daily (integer) -- The maximum number of messages that the campaign can send daily.
    Total (integer) -- The maximum total number of messages that the campaign can send.
    
    
    MessageConfiguration (dict) -- The message configuration settings.
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    
    
    Name (string) -- The custom name of the campaign.
    Schedule (dict) -- The campaign schedule.
    EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
    Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE, HOURLY, DAILY, WEEKLY, MONTHLY
    IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
    QuietTime (dict) -- The time during which the campaign sends no messages.
    End (string) -- The default end time for quiet time in ISO 8601 format.
    Start (string) -- The default start time for quiet time in ISO 8601 format.
    
    
    StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
    Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
    
    
    SegmentId (string) -- The ID of the segment to which the campaign sends messages.
    SegmentVersion (integer) -- The version of the segment to which the campaign sends messages.
    State (dict) -- The campaign status. An A/B test campaign will have a status of COMPLETED only when all treatments have a status of COMPLETED.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    TreatmentDescription (string) -- A custom description for the treatment.
    TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
    Version (integer) -- The campaign version number.
    
    
    
    
    
    """
    pass

def get_campaign_versions(ApplicationId=None, CampaignId=None, PageSize=None, Token=None):
    """
    Returns information about your campaign versions.
    
    
    :example: response = client.get_campaign_versions(
        ApplicationId='string',
        CampaignId='string',
        PageSize='string',
        Token='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type CampaignId: string
    :param CampaignId: [REQUIRED]

    :type PageSize: string
    :param PageSize: 

    :type Token: string
    :param Token: 

    :rtype: dict
    :return: {
        'CampaignsResponse': {
            'Item': [
                {
                    'AdditionalTreatments': [
                        {
                            'Id': 'string',
                            'MessageConfiguration': {
                                'APNSMessage': {
                                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                                    'Body': 'string',
                                    'ImageIconUrl': 'string',
                                    'ImageUrl': 'string',
                                    'JsonBody': 'string',
                                    'MediaUrl': 'string',
                                    'SilentPush': True|False,
                                    'Title': 'string',
                                    'Url': 'string'
                                },
                                'DefaultMessage': {
                                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                                    'Body': 'string',
                                    'ImageIconUrl': 'string',
                                    'ImageUrl': 'string',
                                    'JsonBody': 'string',
                                    'MediaUrl': 'string',
                                    'SilentPush': True|False,
                                    'Title': 'string',
                                    'Url': 'string'
                                },
                                'GCMMessage': {
                                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                                    'Body': 'string',
                                    'ImageIconUrl': 'string',
                                    'ImageUrl': 'string',
                                    'JsonBody': 'string',
                                    'MediaUrl': 'string',
                                    'SilentPush': True|False,
                                    'Title': 'string',
                                    'Url': 'string'
                                }
                            },
                            'Schedule': {
                                'EndTime': 'string',
                                'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY',
                                'IsLocalTime': True|False,
                                'QuietTime': {
                                    'End': 'string',
                                    'Start': 'string'
                                },
                                'StartTime': 'string',
                                'Timezone': 'string'
                            },
                            'SizePercent': 123,
                            'State': {
                                'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'
                            },
                            'TreatmentDescription': 'string',
                            'TreatmentName': 'string'
                        },
                    ],
                    'ApplicationId': 'string',
                    'CreationDate': 'string',
                    'DefaultState': {
                        'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'
                    },
                    'Description': 'string',
                    'HoldoutPercent': 123,
                    'Id': 'string',
                    'IsPaused': True|False,
                    'LastModifiedDate': 'string',
                    'Limits': {
                        'Daily': 123,
                        'Total': 123
                    },
                    'MessageConfiguration': {
                        'APNSMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'DefaultMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'GCMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        }
                    },
                    'Name': 'string',
                    'Schedule': {
                        'EndTime': 'string',
                        'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY',
                        'IsLocalTime': True|False,
                        'QuietTime': {
                            'End': 'string',
                            'Start': 'string'
                        },
                        'StartTime': 'string',
                        'Timezone': 'string'
                    },
                    'SegmentId': 'string',
                    'SegmentVersion': 123,
                    'State': {
                        'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'
                    },
                    'TreatmentDescription': 'string',
                    'TreatmentName': 'string',
                    'Version': 123
                },
            ],
            'NextToken': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    CampaignsResponse (dict) -- List of available campaigns.
    Item (list) -- A list of campaigns.
    (dict) -- Campaign definition
    AdditionalTreatments (list) -- Treatments that are defined in addition to the default treatment.
    (dict) -- Treatment resource
    Id (string) -- The unique treatment ID.
    MessageConfiguration (dict) -- The message configuration settings.
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    
    
    Schedule (dict) -- The campaign schedule.
    EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
    Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE, HOURLY, DAILY, WEEKLY, MONTHLY
    IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
    QuietTime (dict) -- The time during which the campaign sends no messages.
    End (string) -- The default end time for quiet time in ISO 8601 format.
    Start (string) -- The default start time for quiet time in ISO 8601 format.
    
    
    StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
    Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
    
    
    SizePercent (integer) -- The allocated percentage of users for this treatment.
    State (dict) -- The treatment status.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    TreatmentDescription (string) -- A custom description for the treatment.
    TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
    
    
    
    
    ApplicationId (string) -- The ID of the application to which the campaign applies.
    CreationDate (string) -- The date the campaign was created in ISO 8601 format.
    DefaultState (dict) -- The status of the campaign's default treatment. Only present for A/B test campaigns.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    Description (string) -- A description of the campaign.
    HoldoutPercent (integer) -- The allocated percentage of end users who will not receive messages from this campaign.
    Id (string) -- The unique campaign ID.
    IsPaused (boolean) -- Indicates whether the campaign is paused. A paused campaign does not send messages unless you resume it by setting IsPaused to false.
    LastModifiedDate (string) -- The date the campaign was last updated in ISO 8601 format.
    Limits (dict) -- The campaign limits settings.
    Daily (integer) -- The maximum number of messages that the campaign can send daily.
    Total (integer) -- The maximum total number of messages that the campaign can send.
    
    
    MessageConfiguration (dict) -- The message configuration settings.
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    
    
    Name (string) -- The custom name of the campaign.
    Schedule (dict) -- The campaign schedule.
    EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
    Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE, HOURLY, DAILY, WEEKLY, MONTHLY
    IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
    QuietTime (dict) -- The time during which the campaign sends no messages.
    End (string) -- The default end time for quiet time in ISO 8601 format.
    Start (string) -- The default start time for quiet time in ISO 8601 format.
    
    
    StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
    Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
    
    
    SegmentId (string) -- The ID of the segment to which the campaign sends messages.
    SegmentVersion (integer) -- The version of the segment to which the campaign sends messages.
    State (dict) -- The campaign status. An A/B test campaign will have a status of COMPLETED only when all treatments have a status of COMPLETED.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    TreatmentDescription (string) -- A custom description for the treatment.
    TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
    Version (integer) -- The campaign version number.
    
    
    
    
    NextToken (string) -- The string that you use in a subsequent request to get the next page of results in a paginated response.
    
    
    
    
    
    """
    pass

def get_campaigns(ApplicationId=None, PageSize=None, Token=None):
    """
    Returns information about your campaigns.
    
    
    :example: response = client.get_campaigns(
        ApplicationId='string',
        PageSize='string',
        Token='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type PageSize: string
    :param PageSize: 

    :type Token: string
    :param Token: 

    :rtype: dict
    :return: {
        'CampaignsResponse': {
            'Item': [
                {
                    'AdditionalTreatments': [
                        {
                            'Id': 'string',
                            'MessageConfiguration': {
                                'APNSMessage': {
                                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                                    'Body': 'string',
                                    'ImageIconUrl': 'string',
                                    'ImageUrl': 'string',
                                    'JsonBody': 'string',
                                    'MediaUrl': 'string',
                                    'SilentPush': True|False,
                                    'Title': 'string',
                                    'Url': 'string'
                                },
                                'DefaultMessage': {
                                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                                    'Body': 'string',
                                    'ImageIconUrl': 'string',
                                    'ImageUrl': 'string',
                                    'JsonBody': 'string',
                                    'MediaUrl': 'string',
                                    'SilentPush': True|False,
                                    'Title': 'string',
                                    'Url': 'string'
                                },
                                'GCMMessage': {
                                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                                    'Body': 'string',
                                    'ImageIconUrl': 'string',
                                    'ImageUrl': 'string',
                                    'JsonBody': 'string',
                                    'MediaUrl': 'string',
                                    'SilentPush': True|False,
                                    'Title': 'string',
                                    'Url': 'string'
                                }
                            },
                            'Schedule': {
                                'EndTime': 'string',
                                'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY',
                                'IsLocalTime': True|False,
                                'QuietTime': {
                                    'End': 'string',
                                    'Start': 'string'
                                },
                                'StartTime': 'string',
                                'Timezone': 'string'
                            },
                            'SizePercent': 123,
                            'State': {
                                'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'
                            },
                            'TreatmentDescription': 'string',
                            'TreatmentName': 'string'
                        },
                    ],
                    'ApplicationId': 'string',
                    'CreationDate': 'string',
                    'DefaultState': {
                        'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'
                    },
                    'Description': 'string',
                    'HoldoutPercent': 123,
                    'Id': 'string',
                    'IsPaused': True|False,
                    'LastModifiedDate': 'string',
                    'Limits': {
                        'Daily': 123,
                        'Total': 123
                    },
                    'MessageConfiguration': {
                        'APNSMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'DefaultMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'GCMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        }
                    },
                    'Name': 'string',
                    'Schedule': {
                        'EndTime': 'string',
                        'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY',
                        'IsLocalTime': True|False,
                        'QuietTime': {
                            'End': 'string',
                            'Start': 'string'
                        },
                        'StartTime': 'string',
                        'Timezone': 'string'
                    },
                    'SegmentId': 'string',
                    'SegmentVersion': 123,
                    'State': {
                        'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'
                    },
                    'TreatmentDescription': 'string',
                    'TreatmentName': 'string',
                    'Version': 123
                },
            ],
            'NextToken': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    CampaignsResponse (dict) -- List of available campaigns.
    Item (list) -- A list of campaigns.
    (dict) -- Campaign definition
    AdditionalTreatments (list) -- Treatments that are defined in addition to the default treatment.
    (dict) -- Treatment resource
    Id (string) -- The unique treatment ID.
    MessageConfiguration (dict) -- The message configuration settings.
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    
    
    Schedule (dict) -- The campaign schedule.
    EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
    Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE, HOURLY, DAILY, WEEKLY, MONTHLY
    IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
    QuietTime (dict) -- The time during which the campaign sends no messages.
    End (string) -- The default end time for quiet time in ISO 8601 format.
    Start (string) -- The default start time for quiet time in ISO 8601 format.
    
    
    StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
    Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
    
    
    SizePercent (integer) -- The allocated percentage of users for this treatment.
    State (dict) -- The treatment status.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    TreatmentDescription (string) -- A custom description for the treatment.
    TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
    
    
    
    
    ApplicationId (string) -- The ID of the application to which the campaign applies.
    CreationDate (string) -- The date the campaign was created in ISO 8601 format.
    DefaultState (dict) -- The status of the campaign's default treatment. Only present for A/B test campaigns.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    Description (string) -- A description of the campaign.
    HoldoutPercent (integer) -- The allocated percentage of end users who will not receive messages from this campaign.
    Id (string) -- The unique campaign ID.
    IsPaused (boolean) -- Indicates whether the campaign is paused. A paused campaign does not send messages unless you resume it by setting IsPaused to false.
    LastModifiedDate (string) -- The date the campaign was last updated in ISO 8601 format.
    Limits (dict) -- The campaign limits settings.
    Daily (integer) -- The maximum number of messages that the campaign can send daily.
    Total (integer) -- The maximum total number of messages that the campaign can send.
    
    
    MessageConfiguration (dict) -- The message configuration settings.
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    
    
    Name (string) -- The custom name of the campaign.
    Schedule (dict) -- The campaign schedule.
    EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
    Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE, HOURLY, DAILY, WEEKLY, MONTHLY
    IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
    QuietTime (dict) -- The time during which the campaign sends no messages.
    End (string) -- The default end time for quiet time in ISO 8601 format.
    Start (string) -- The default start time for quiet time in ISO 8601 format.
    
    
    StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
    Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
    
    
    SegmentId (string) -- The ID of the segment to which the campaign sends messages.
    SegmentVersion (integer) -- The version of the segment to which the campaign sends messages.
    State (dict) -- The campaign status. An A/B test campaign will have a status of COMPLETED only when all treatments have a status of COMPLETED.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    TreatmentDescription (string) -- A custom description for the treatment.
    TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
    Version (integer) -- The campaign version number.
    
    
    
    
    NextToken (string) -- The string that you use in a subsequent request to get the next page of results in a paginated response.
    
    
    
    
    
    """
    pass

def get_endpoint(ApplicationId=None, EndpointId=None):
    """
    Returns information about an endpoint.
    
    
    :example: response = client.get_endpoint(
        ApplicationId='string',
        EndpointId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type EndpointId: string
    :param EndpointId: [REQUIRED]

    :rtype: dict
    :return: {
        'EndpointResponse': {
            'Address': 'string',
            'ApplicationId': 'string',
            'Attributes': {
                'string': [
                    'string',
                ]
            },
            'ChannelType': 'APNS'|'GCM',
            'CohortId': 'string',
            'CreationDate': 'string',
            'Demographic': {
                'AppVersion': 'string',
                'Locale': 'string',
                'Make': 'string',
                'Model': 'string',
                'ModelVersion': 'string',
                'Platform': 'string',
                'PlatformVersion': 'string',
                'Timezone': 'string'
            },
            'EffectiveDate': 'string',
            'EndpointStatus': 'string',
            'Id': 'string',
            'Location': {
                'City': 'string',
                'Country': 'string',
                'Latitude': 123.0,
                'Longitude': 123.0,
                'PostalCode': 'string',
                'Region': 'string'
            },
            'Metrics': {
                'string': 123.0
            },
            'OptOut': 'string',
            'RequestId': 'string',
            'User': {
                'UserAttributes': {
                    'string': [
                        'string',
                    ]
                },
                'UserId': 'string'
            },
            'ShardId': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    EndpointResponse (dict) -- Endpoint response
    Address (string) -- The address or token of the endpoint as provided by your push provider (e.g. DeviceToken or RegistrationId).
    ApplicationId (string) -- The ID of the application associated with the endpoint.
    Attributes (dict) -- Custom attributes that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create a segment.
    (string) --
    (list) --
    (string) --
    
    
    
    
    
    
    ChannelType (string) -- The channel type. Valid values: APNS, GCM
    CohortId (string) -- A number from 0 - 99 that represents the cohort the endpoint is assigned to. Endpoints are grouped into cohorts randomly, and each cohort contains approximately 1 percent of the endpoints for an app. Amazon Pinpoint assigns cohorts to the holdout or treatment allocations for a campaign.
    CreationDate (string) -- The last time the endpoint was created. Provided in ISO 8601 format.
    Demographic (dict) -- The endpoint demographic attributes.
    AppVersion (string) -- The version of the application associated with the endpoint.
    Locale (string) -- The endpoint locale in the following format: The ISO 639-1 alpha-2 code, followed by an underscore, followed by an ISO 3166-1 alpha-2 value.
    Make (string) -- The endpoint make, such as such as Apple or Samsung.
    Model (string) -- The endpoint model, such as iPhone.
    ModelVersion (string) -- The endpoint model version.
    Platform (string) -- The endpoint platform, such as ios or android.
    PlatformVersion (string) -- The endpoint platform version.
    Timezone (string) -- The timezone of the endpoint. Specified as a tz database value, such as Americas/Los_Angeles.
    
    
    EffectiveDate (string) -- The last time the endpoint was updated. Provided in ISO 8601 format.
    EndpointStatus (string) -- The endpoint status. Can be either ACTIVE or INACTIVE. Will be set to INACTIVE if a delivery fails. Will be set to ACTIVE if the address is updated.
    Id (string) -- The unique ID that you assigned to the endpoint. The ID should be a globally unique identifier (GUID) to ensure that it is unique compared to all other endpoints for the application.
    Location (dict) -- The endpoint location attributes.
    City (string) -- The city where the endpoint is located.
    Country (string) -- Country according to ISO 3166-1 Alpha-2 codes. For example, US.
    Latitude (float) -- The latitude of the endpoint location. Rounded to one decimal (Roughly corresponding to a mile).
    Longitude (float) -- The longitude of the endpoint location. Rounded to one decimal (Roughly corresponding to a mile).
    PostalCode (string) -- The postal code or zip code of the endpoint.
    Region (string) -- The region of the endpoint location. For example, corresponds to a state in US.
    
    
    Metrics (dict) -- Custom metrics that your app reports to Amazon Pinpoint.
    (string) --
    (float) --
    
    
    
    
    OptOut (string) -- Indicates whether a user has opted out of receiving messages with one of the following values: ALL  User receives all messages. NONE  User receives no messages.
    RequestId (string) -- The unique ID for the most recent request to update the endpoint.
    User (dict) -- Custom user-specific attributes that your app reports to Amazon Pinpoint.
    UserAttributes (dict) -- Custom attributes specific to the user.
    (string) --
    (list) --
    (string) --
    
    
    
    
    
    
    UserId (string) -- The unique ID of the user.
    
    
    ShardId (string) -- The ShardId of endpoint
    
    
    
    
    
    """
    pass

def get_event_stream(ApplicationId=None):
    """
    Returns the event stream for an app.
    
    
    :example: response = client.get_event_stream(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] ApplicationId

    :rtype: dict
    :return: {
        'EventStream': {
            'ApplicationId': 'string',
            'DestinationStreamArn': 'string',
            'ExternalId': 'string',
            'LastModifiedDate': 'string',
            'LastUpdatedBy': 'string',
            'RoleArn': 'string'
        }
    }
    
    
    """
    pass

def get_gcm_channel(ApplicationId=None):
    """
    Returns information about the GCM channel for an app.
    
    
    :example: response = client.get_gcm_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :rtype: dict
    :return: {
        'GCMChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Credential': 'string',
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    """
    pass

def get_import_job(ApplicationId=None, JobId=None):
    """
    Returns information about an import job.
    
    
    :example: response = client.get_import_job(
        ApplicationId='string',
        JobId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type JobId: string
    :param JobId: [REQUIRED]

    :rtype: dict
    :return: {
        'ImportJobResponse': {
            'ApplicationId': 'string',
            'CompletedPieces': 123,
            'CompletionDate': 'string',
            'CreationDate': 'string',
            'Definition': {
                'DefineSegment': True|False,
                'ExternalId': 'string',
                'Format': 'CSV'|'JSON',
                'RegisterEndpoints': True|False,
                'RoleArn': 'string',
                'S3Url': 'string',
                'SegmentId': 'string',
                'SegmentName': 'string'
            },
            'FailedPieces': 123,
            'Failures': [
                'string',
            ],
            'Id': 'string',
            'JobStatus': 'CREATED'|'INITIALIZING'|'PROCESSING'|'COMPLETING'|'COMPLETED'|'FAILING'|'FAILED',
            'TotalFailures': 123,
            'TotalPieces': 123,
            'TotalProcessed': 123,
            'Type': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    ImportJobResponse (dict) --
    ApplicationId (string) -- The unique ID of the application to which the import job applies.
    CompletedPieces (integer) -- The number of pieces that have successfully imported as of the time of the request.
    CompletionDate (string) -- The date the import job completed in ISO 8601 format.
    CreationDate (string) -- The date the import job was created in ISO 8601 format.
    Definition (dict) -- The import job settings.
    DefineSegment (boolean) -- Sets whether the endpoints create a segment when they are imported.
    ExternalId (string) -- A unique, custom ID assigned to the IAM role that restricts who can assume the role.
    Format (string) -- The format of the files that contain the endpoint definitions. Valid values: CSV, JSON
    RegisterEndpoints (boolean) -- Sets whether the endpoints are registered with Amazon Pinpoint when they are imported.
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the Amazon S3 location that contains the endpoints to import.
    S3Url (string) -- A URL that points to the location within an Amazon S3 bucket that contains the endpoints to import. The location can be a folder or a single file. The URL should follow this format: s3://bucket-name/folder-name/file-name Amazon Pinpoint will import endpoints from this location and any subfolders it contains.
    SegmentId (string) -- The ID of the segment to update if the import job is meant to update an existing segment.
    SegmentName (string) -- A custom name for the segment created by the import job. Use if DefineSegment is true.
    
    
    FailedPieces (integer) -- The number of pieces that have failed to import as of the time of the request.
    Failures (list) -- Provides up to 100 of the first failed entries for the job, if any exist.
    (string) --
    
    
    Id (string) -- The unique ID of the import job.
    JobStatus (string) -- The status of the import job. Valid values: CREATED, INITIALIZING, PROCESSING, COMPLETING, COMPLETED, FAILING, FAILED The job status is FAILED if one or more pieces failed to import.
    TotalFailures (integer) -- The number of endpoints that failed to import; for example, because of syntax errors.
    TotalPieces (integer) -- The total number of pieces that must be imported to finish the job. Each piece is an approximately equal portion of the endpoints to import.
    TotalProcessed (integer) -- The number of endpoints that were processed by the import job.
    Type (string) -- The job type. Will be Import.
    
    
    
    
    
    """
    pass

def get_import_jobs(ApplicationId=None, PageSize=None, Token=None):
    """
    Returns information about your import jobs.
    
    
    :example: response = client.get_import_jobs(
        ApplicationId='string',
        PageSize='string',
        Token='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type PageSize: string
    :param PageSize: 

    :type Token: string
    :param Token: 

    :rtype: dict
    :return: {
        'ImportJobsResponse': {
            'Item': [
                {
                    'ApplicationId': 'string',
                    'CompletedPieces': 123,
                    'CompletionDate': 'string',
                    'CreationDate': 'string',
                    'Definition': {
                        'DefineSegment': True|False,
                        'ExternalId': 'string',
                        'Format': 'CSV'|'JSON',
                        'RegisterEndpoints': True|False,
                        'RoleArn': 'string',
                        'S3Url': 'string',
                        'SegmentId': 'string',
                        'SegmentName': 'string'
                    },
                    'FailedPieces': 123,
                    'Failures': [
                        'string',
                    ],
                    'Id': 'string',
                    'JobStatus': 'CREATED'|'INITIALIZING'|'PROCESSING'|'COMPLETING'|'COMPLETED'|'FAILING'|'FAILED',
                    'TotalFailures': 123,
                    'TotalPieces': 123,
                    'TotalProcessed': 123,
                    'Type': 'string'
                },
            ],
            'NextToken': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    ImportJobsResponse (dict) -- Import job list.
    Item (list) -- A list of import jobs for the application.
    (dict) --
    ApplicationId (string) -- The unique ID of the application to which the import job applies.
    CompletedPieces (integer) -- The number of pieces that have successfully imported as of the time of the request.
    CompletionDate (string) -- The date the import job completed in ISO 8601 format.
    CreationDate (string) -- The date the import job was created in ISO 8601 format.
    Definition (dict) -- The import job settings.
    DefineSegment (boolean) -- Sets whether the endpoints create a segment when they are imported.
    ExternalId (string) -- A unique, custom ID assigned to the IAM role that restricts who can assume the role.
    Format (string) -- The format of the files that contain the endpoint definitions. Valid values: CSV, JSON
    RegisterEndpoints (boolean) -- Sets whether the endpoints are registered with Amazon Pinpoint when they are imported.
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the Amazon S3 location that contains the endpoints to import.
    S3Url (string) -- A URL that points to the location within an Amazon S3 bucket that contains the endpoints to import. The location can be a folder or a single file. The URL should follow this format: s3://bucket-name/folder-name/file-name Amazon Pinpoint will import endpoints from this location and any subfolders it contains.
    SegmentId (string) -- The ID of the segment to update if the import job is meant to update an existing segment.
    SegmentName (string) -- A custom name for the segment created by the import job. Use if DefineSegment is true.
    
    
    FailedPieces (integer) -- The number of pieces that have failed to import as of the time of the request.
    Failures (list) -- Provides up to 100 of the first failed entries for the job, if any exist.
    (string) --
    
    
    Id (string) -- The unique ID of the import job.
    JobStatus (string) -- The status of the import job. Valid values: CREATED, INITIALIZING, PROCESSING, COMPLETING, COMPLETED, FAILING, FAILED The job status is FAILED if one or more pieces failed to import.
    TotalFailures (integer) -- The number of endpoints that failed to import; for example, because of syntax errors.
    TotalPieces (integer) -- The total number of pieces that must be imported to finish the job. Each piece is an approximately equal portion of the endpoints to import.
    TotalProcessed (integer) -- The number of endpoints that were processed by the import job.
    Type (string) -- The job type. Will be Import.
    
    
    
    
    NextToken (string) -- The string that you use in a subsequent request to get the next page of results in a paginated response.
    
    
    
    
    
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

def get_segment(ApplicationId=None, SegmentId=None):
    """
    Returns information about a segment.
    
    
    :example: response = client.get_segment(
        ApplicationId='string',
        SegmentId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type SegmentId: string
    :param SegmentId: [REQUIRED]

    :rtype: dict
    :return: {
        'SegmentResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Dimensions': {
                'Attributes': {
                    'string': {
                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'Behavior': {
                    'Recency': {
                        'Duration': 'HR_24'|'DAY_7'|'DAY_14'|'DAY_30',
                        'RecencyType': 'ACTIVE'|'INACTIVE'
                    }
                },
                'Demographic': {
                    'AppVersion': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'DeviceType': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Make': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Model': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Platform': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'Location': {
                    'Country': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'UserAttributes': {
                    'string': {
                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                }
            },
            'Id': 'string',
            'ImportDefinition': {
                'ExternalId': 'string',
                'Format': 'CSV'|'JSON',
                'RoleArn': 'string',
                'S3Url': 'string',
                'Size': 123
            },
            'LastModifiedDate': 'string',
            'Name': 'string',
            'SegmentType': 'DIMENSIONAL'|'IMPORT',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    SegmentResponse (dict) -- Segment definition.
    ApplicationId (string) -- The ID of the application to which the segment applies.
    CreationDate (string) -- The date the segment was created in ISO 8601 format.
    Dimensions (dict) -- The segment dimensions attributes.
    Attributes (dict) -- Custom segment attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    Behavior (dict) -- The segment behaviors attributes.
    Recency (dict) -- The recency of use.
    Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
    RecencyType (string) -- The recency dimension type: ACTIVE  Users who have used your app within the specified duration are included in the segment. INACTIVE  Users who have not used your app within the specified duration are included in the segment.
    
    
    
    
    Demographic (dict) -- The segment demographics attributes.
    AppVersion (dict) -- The app version criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    DeviceType (dict) -- The device type criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Make (dict) -- The device make criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Model (dict) -- The device model criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Platform (dict) -- The device platform criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    Location (dict) -- The segment location attributes.
    Country (dict) -- The country filter according to ISO 3166-1 Alpha-2 codes.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    UserAttributes (dict) -- Custom segment user attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    
    
    Id (string) -- The unique segment ID.
    ImportDefinition (dict) -- The import job settings.
    ExternalId (string) -- A unique, custom ID assigned to the IAM role that restricts who can assume the role.
    Format (string) -- The format of the endpoint files that were imported to create this segment. Valid values: CSV, JSON
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the endpoints in Amazon S3.
    S3Url (string) -- A URL that points to the Amazon S3 location from which the endpoints for this segment were imported.
    Size (integer) -- The number of endpoints that were successfully imported to create this segment.
    
    
    LastModifiedDate (string) -- The date the segment was last updated in ISO 8601 format.
    Name (string) -- The name of segment
    SegmentType (string) -- The segment type: DIMENSIONAL  A dynamic segment built from selection criteria based on endpoint data reported by your app. You create this type of segment by using the segment builder in the Amazon Pinpoint console or by making a POST request to the segments resource. IMPORT  A static segment built from an imported set of endpoint definitions. You create this type of segment by importing a segment in the Amazon Pinpoint console or by making a POST request to the jobs/import resource.
    Version (integer) -- The segment version number.
    
    
    
    
    
    """
    pass

def get_segment_import_jobs(ApplicationId=None, PageSize=None, SegmentId=None, Token=None):
    """
    Returns a list of import jobs for a specific segment.
    
    
    :example: response = client.get_segment_import_jobs(
        ApplicationId='string',
        PageSize='string',
        SegmentId='string',
        Token='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type PageSize: string
    :param PageSize: 

    :type SegmentId: string
    :param SegmentId: [REQUIRED]

    :type Token: string
    :param Token: 

    :rtype: dict
    :return: {
        'ImportJobsResponse': {
            'Item': [
                {
                    'ApplicationId': 'string',
                    'CompletedPieces': 123,
                    'CompletionDate': 'string',
                    'CreationDate': 'string',
                    'Definition': {
                        'DefineSegment': True|False,
                        'ExternalId': 'string',
                        'Format': 'CSV'|'JSON',
                        'RegisterEndpoints': True|False,
                        'RoleArn': 'string',
                        'S3Url': 'string',
                        'SegmentId': 'string',
                        'SegmentName': 'string'
                    },
                    'FailedPieces': 123,
                    'Failures': [
                        'string',
                    ],
                    'Id': 'string',
                    'JobStatus': 'CREATED'|'INITIALIZING'|'PROCESSING'|'COMPLETING'|'COMPLETED'|'FAILING'|'FAILED',
                    'TotalFailures': 123,
                    'TotalPieces': 123,
                    'TotalProcessed': 123,
                    'Type': 'string'
                },
            ],
            'NextToken': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    ImportJobsResponse (dict) -- Import job list.
    Item (list) -- A list of import jobs for the application.
    (dict) --
    ApplicationId (string) -- The unique ID of the application to which the import job applies.
    CompletedPieces (integer) -- The number of pieces that have successfully imported as of the time of the request.
    CompletionDate (string) -- The date the import job completed in ISO 8601 format.
    CreationDate (string) -- The date the import job was created in ISO 8601 format.
    Definition (dict) -- The import job settings.
    DefineSegment (boolean) -- Sets whether the endpoints create a segment when they are imported.
    ExternalId (string) -- A unique, custom ID assigned to the IAM role that restricts who can assume the role.
    Format (string) -- The format of the files that contain the endpoint definitions. Valid values: CSV, JSON
    RegisterEndpoints (boolean) -- Sets whether the endpoints are registered with Amazon Pinpoint when they are imported.
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the Amazon S3 location that contains the endpoints to import.
    S3Url (string) -- A URL that points to the location within an Amazon S3 bucket that contains the endpoints to import. The location can be a folder or a single file. The URL should follow this format: s3://bucket-name/folder-name/file-name Amazon Pinpoint will import endpoints from this location and any subfolders it contains.
    SegmentId (string) -- The ID of the segment to update if the import job is meant to update an existing segment.
    SegmentName (string) -- A custom name for the segment created by the import job. Use if DefineSegment is true.
    
    
    FailedPieces (integer) -- The number of pieces that have failed to import as of the time of the request.
    Failures (list) -- Provides up to 100 of the first failed entries for the job, if any exist.
    (string) --
    
    
    Id (string) -- The unique ID of the import job.
    JobStatus (string) -- The status of the import job. Valid values: CREATED, INITIALIZING, PROCESSING, COMPLETING, COMPLETED, FAILING, FAILED The job status is FAILED if one or more pieces failed to import.
    TotalFailures (integer) -- The number of endpoints that failed to import; for example, because of syntax errors.
    TotalPieces (integer) -- The total number of pieces that must be imported to finish the job. Each piece is an approximately equal portion of the endpoints to import.
    TotalProcessed (integer) -- The number of endpoints that were processed by the import job.
    Type (string) -- The job type. Will be Import.
    
    
    
    
    NextToken (string) -- The string that you use in a subsequent request to get the next page of results in a paginated response.
    
    
    
    
    
    """
    pass

def get_segment_version(ApplicationId=None, SegmentId=None, Version=None):
    """
    Returns information about a segment version.
    
    
    :example: response = client.get_segment_version(
        ApplicationId='string',
        SegmentId='string',
        Version='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type SegmentId: string
    :param SegmentId: [REQUIRED]

    :type Version: string
    :param Version: [REQUIRED]

    :rtype: dict
    :return: {
        'SegmentResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Dimensions': {
                'Attributes': {
                    'string': {
                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'Behavior': {
                    'Recency': {
                        'Duration': 'HR_24'|'DAY_7'|'DAY_14'|'DAY_30',
                        'RecencyType': 'ACTIVE'|'INACTIVE'
                    }
                },
                'Demographic': {
                    'AppVersion': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'DeviceType': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Make': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Model': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Platform': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'Location': {
                    'Country': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'UserAttributes': {
                    'string': {
                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                }
            },
            'Id': 'string',
            'ImportDefinition': {
                'ExternalId': 'string',
                'Format': 'CSV'|'JSON',
                'RoleArn': 'string',
                'S3Url': 'string',
                'Size': 123
            },
            'LastModifiedDate': 'string',
            'Name': 'string',
            'SegmentType': 'DIMENSIONAL'|'IMPORT',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    SegmentResponse (dict) -- Segment definition.
    ApplicationId (string) -- The ID of the application to which the segment applies.
    CreationDate (string) -- The date the segment was created in ISO 8601 format.
    Dimensions (dict) -- The segment dimensions attributes.
    Attributes (dict) -- Custom segment attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    Behavior (dict) -- The segment behaviors attributes.
    Recency (dict) -- The recency of use.
    Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
    RecencyType (string) -- The recency dimension type: ACTIVE  Users who have used your app within the specified duration are included in the segment. INACTIVE  Users who have not used your app within the specified duration are included in the segment.
    
    
    
    
    Demographic (dict) -- The segment demographics attributes.
    AppVersion (dict) -- The app version criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    DeviceType (dict) -- The device type criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Make (dict) -- The device make criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Model (dict) -- The device model criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Platform (dict) -- The device platform criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    Location (dict) -- The segment location attributes.
    Country (dict) -- The country filter according to ISO 3166-1 Alpha-2 codes.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    UserAttributes (dict) -- Custom segment user attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    
    
    Id (string) -- The unique segment ID.
    ImportDefinition (dict) -- The import job settings.
    ExternalId (string) -- A unique, custom ID assigned to the IAM role that restricts who can assume the role.
    Format (string) -- The format of the endpoint files that were imported to create this segment. Valid values: CSV, JSON
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the endpoints in Amazon S3.
    S3Url (string) -- A URL that points to the Amazon S3 location from which the endpoints for this segment were imported.
    Size (integer) -- The number of endpoints that were successfully imported to create this segment.
    
    
    LastModifiedDate (string) -- The date the segment was last updated in ISO 8601 format.
    Name (string) -- The name of segment
    SegmentType (string) -- The segment type: DIMENSIONAL  A dynamic segment built from selection criteria based on endpoint data reported by your app. You create this type of segment by using the segment builder in the Amazon Pinpoint console or by making a POST request to the segments resource. IMPORT  A static segment built from an imported set of endpoint definitions. You create this type of segment by importing a segment in the Amazon Pinpoint console or by making a POST request to the jobs/import resource.
    Version (integer) -- The segment version number.
    
    
    
    
    
    """
    pass

def get_segment_versions(ApplicationId=None, PageSize=None, SegmentId=None, Token=None):
    """
    Returns information about your segment versions.
    
    
    :example: response = client.get_segment_versions(
        ApplicationId='string',
        PageSize='string',
        SegmentId='string',
        Token='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type PageSize: string
    :param PageSize: 

    :type SegmentId: string
    :param SegmentId: [REQUIRED]

    :type Token: string
    :param Token: 

    :rtype: dict
    :return: {
        'SegmentsResponse': {
            'Item': [
                {
                    'ApplicationId': 'string',
                    'CreationDate': 'string',
                    'Dimensions': {
                        'Attributes': {
                            'string': {
                                'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            }
                        },
                        'Behavior': {
                            'Recency': {
                                'Duration': 'HR_24'|'DAY_7'|'DAY_14'|'DAY_30',
                                'RecencyType': 'ACTIVE'|'INACTIVE'
                            }
                        },
                        'Demographic': {
                            'AppVersion': {
                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            },
                            'DeviceType': {
                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            },
                            'Make': {
                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            },
                            'Model': {
                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            },
                            'Platform': {
                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            }
                        },
                        'Location': {
                            'Country': {
                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            }
                        },
                        'UserAttributes': {
                            'string': {
                                'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            }
                        }
                    },
                    'Id': 'string',
                    'ImportDefinition': {
                        'ExternalId': 'string',
                        'Format': 'CSV'|'JSON',
                        'RoleArn': 'string',
                        'S3Url': 'string',
                        'Size': 123
                    },
                    'LastModifiedDate': 'string',
                    'Name': 'string',
                    'SegmentType': 'DIMENSIONAL'|'IMPORT',
                    'Version': 123
                },
            ],
            'NextToken': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    SegmentsResponse (dict) -- Segments in your account.
    Item (list) -- The list of segments.
    (dict) -- Segment definition.
    ApplicationId (string) -- The ID of the application to which the segment applies.
    CreationDate (string) -- The date the segment was created in ISO 8601 format.
    Dimensions (dict) -- The segment dimensions attributes.
    Attributes (dict) -- Custom segment attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    Behavior (dict) -- The segment behaviors attributes.
    Recency (dict) -- The recency of use.
    Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
    RecencyType (string) -- The recency dimension type: ACTIVE  Users who have used your app within the specified duration are included in the segment. INACTIVE  Users who have not used your app within the specified duration are included in the segment.
    
    
    
    
    Demographic (dict) -- The segment demographics attributes.
    AppVersion (dict) -- The app version criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    DeviceType (dict) -- The device type criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Make (dict) -- The device make criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Model (dict) -- The device model criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Platform (dict) -- The device platform criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    Location (dict) -- The segment location attributes.
    Country (dict) -- The country filter according to ISO 3166-1 Alpha-2 codes.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    UserAttributes (dict) -- Custom segment user attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    
    
    Id (string) -- The unique segment ID.
    ImportDefinition (dict) -- The import job settings.
    ExternalId (string) -- A unique, custom ID assigned to the IAM role that restricts who can assume the role.
    Format (string) -- The format of the endpoint files that were imported to create this segment. Valid values: CSV, JSON
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the endpoints in Amazon S3.
    S3Url (string) -- A URL that points to the Amazon S3 location from which the endpoints for this segment were imported.
    Size (integer) -- The number of endpoints that were successfully imported to create this segment.
    
    
    LastModifiedDate (string) -- The date the segment was last updated in ISO 8601 format.
    Name (string) -- The name of segment
    SegmentType (string) -- The segment type: DIMENSIONAL  A dynamic segment built from selection criteria based on endpoint data reported by your app. You create this type of segment by using the segment builder in the Amazon Pinpoint console or by making a POST request to the segments resource. IMPORT  A static segment built from an imported set of endpoint definitions. You create this type of segment by importing a segment in the Amazon Pinpoint console or by making a POST request to the jobs/import resource.
    Version (integer) -- The segment version number.
    
    
    
    
    NextToken (string) -- An identifier used to retrieve the next page of results. The token is null if no additional pages exist.
    
    
    
    
    
    """
    pass

def get_segments(ApplicationId=None, PageSize=None, Token=None):
    """
    Used to get information about your segments.
    
    
    :example: response = client.get_segments(
        ApplicationId='string',
        PageSize='string',
        Token='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type PageSize: string
    :param PageSize: 

    :type Token: string
    :param Token: 

    :rtype: dict
    :return: {
        'SegmentsResponse': {
            'Item': [
                {
                    'ApplicationId': 'string',
                    'CreationDate': 'string',
                    'Dimensions': {
                        'Attributes': {
                            'string': {
                                'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            }
                        },
                        'Behavior': {
                            'Recency': {
                                'Duration': 'HR_24'|'DAY_7'|'DAY_14'|'DAY_30',
                                'RecencyType': 'ACTIVE'|'INACTIVE'
                            }
                        },
                        'Demographic': {
                            'AppVersion': {
                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            },
                            'DeviceType': {
                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            },
                            'Make': {
                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            },
                            'Model': {
                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            },
                            'Platform': {
                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            }
                        },
                        'Location': {
                            'Country': {
                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            }
                        },
                        'UserAttributes': {
                            'string': {
                                'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            }
                        }
                    },
                    'Id': 'string',
                    'ImportDefinition': {
                        'ExternalId': 'string',
                        'Format': 'CSV'|'JSON',
                        'RoleArn': 'string',
                        'S3Url': 'string',
                        'Size': 123
                    },
                    'LastModifiedDate': 'string',
                    'Name': 'string',
                    'SegmentType': 'DIMENSIONAL'|'IMPORT',
                    'Version': 123
                },
            ],
            'NextToken': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    SegmentsResponse (dict) -- Segments in your account.
    Item (list) -- The list of segments.
    (dict) -- Segment definition.
    ApplicationId (string) -- The ID of the application to which the segment applies.
    CreationDate (string) -- The date the segment was created in ISO 8601 format.
    Dimensions (dict) -- The segment dimensions attributes.
    Attributes (dict) -- Custom segment attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    Behavior (dict) -- The segment behaviors attributes.
    Recency (dict) -- The recency of use.
    Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
    RecencyType (string) -- The recency dimension type: ACTIVE  Users who have used your app within the specified duration are included in the segment. INACTIVE  Users who have not used your app within the specified duration are included in the segment.
    
    
    
    
    Demographic (dict) -- The segment demographics attributes.
    AppVersion (dict) -- The app version criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    DeviceType (dict) -- The device type criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Make (dict) -- The device make criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Model (dict) -- The device model criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Platform (dict) -- The device platform criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    Location (dict) -- The segment location attributes.
    Country (dict) -- The country filter according to ISO 3166-1 Alpha-2 codes.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    UserAttributes (dict) -- Custom segment user attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    
    
    Id (string) -- The unique segment ID.
    ImportDefinition (dict) -- The import job settings.
    ExternalId (string) -- A unique, custom ID assigned to the IAM role that restricts who can assume the role.
    Format (string) -- The format of the endpoint files that were imported to create this segment. Valid values: CSV, JSON
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the endpoints in Amazon S3.
    S3Url (string) -- A URL that points to the Amazon S3 location from which the endpoints for this segment were imported.
    Size (integer) -- The number of endpoints that were successfully imported to create this segment.
    
    
    LastModifiedDate (string) -- The date the segment was last updated in ISO 8601 format.
    Name (string) -- The name of segment
    SegmentType (string) -- The segment type: DIMENSIONAL  A dynamic segment built from selection criteria based on endpoint data reported by your app. You create this type of segment by using the segment builder in the Amazon Pinpoint console or by making a POST request to the segments resource. IMPORT  A static segment built from an imported set of endpoint definitions. You create this type of segment by importing a segment in the Amazon Pinpoint console or by making a POST request to the jobs/import resource.
    Version (integer) -- The segment version number.
    
    
    
    
    NextToken (string) -- An identifier used to retrieve the next page of results. The token is null if no additional pages exist.
    
    
    
    
    
    """
    pass

def get_waiter():
    """
    
    """
    pass

def put_event_stream(ApplicationId=None, WriteEventStream=None):
    """
    Use to create or update the event stream for an app.
    
    
    :example: response = client.put_event_stream(
        ApplicationId='string',
        WriteEventStream={
            'DestinationStreamArn': 'string',
            'ExternalId': 'string',
            'RoleArn': 'string'
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] ApplicationId

    :type WriteEventStream: dict
    :param WriteEventStream: [REQUIRED] EventStream to write.
            DestinationStreamArn (string) -- The Amazon Resource Name (ARN) of the Amazon Kinesis stream or Firehose delivery stream to which you want to publish events. Firehose ARN: arn:aws:firehose:REGION:ACCOUNT_ID:deliverystream/STREAM_NAME Kinesis ARN: arn:aws:kinesis:REGION:ACCOUNT_ID:stream/STREAM_NAME
            ExternalId (string) -- The external ID assigned the IAM role that authorizes Amazon Pinpoint to publish to the stream.
            RoleArn (string) -- The IAM role that authorizes Amazon Pinpoint to publish events to the stream in your account.
            

    :rtype: dict
    :return: {
        'EventStream': {
            'ApplicationId': 'string',
            'DestinationStreamArn': 'string',
            'ExternalId': 'string',
            'LastModifiedDate': 'string',
            'LastUpdatedBy': 'string',
            'RoleArn': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- PutEventStream Response
    EventStream (dict) -- Model for an event publishing subscription export.
    ApplicationId (string) -- The ID of the application from which events should be published.
    DestinationStreamArn (string) -- The Amazon Resource Name (ARN) of the Amazon Kinesis stream or Firehose delivery stream to which you want to publish events. Firehose ARN: arn:aws:firehose:REGION:ACCOUNT_ID:deliverystream/STREAM_NAME Kinesis ARN: arn:aws:kinesis:REGION:ACCOUNT_ID:stream/STREAM_NAME
    ExternalId (string) -- The external ID assigned the IAM role that authorizes Amazon Pinpoint to publish to the stream.
    LastModifiedDate (string) -- The date the event stream was last updated in ISO 8601 format.
    LastUpdatedBy (string) -- The IAM user who last modified the event stream.
    RoleArn (string) -- The IAM role that authorizes Amazon Pinpoint to publish events to the stream in your account.
    
    
    
    
    
    """
    pass

def update_apns_channel(APNSChannelRequest=None, ApplicationId=None):
    """
    Use to update the APNs channel for an app.
    
    
    :example: response = client.update_apns_channel(
        APNSChannelRequest={
            'Certificate': 'string',
            'PrivateKey': 'string'
        },
        ApplicationId='string'
    )
    
    
    :type APNSChannelRequest: dict
    :param APNSChannelRequest: [REQUIRED] Apple Push Notification Service channel definition.
            Certificate (string) -- The distribution certificate from Apple.
            PrivateKey (string) -- The certificate private key.
            

    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :rtype: dict
    :return: {
        'APNSChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    APNSChannelResponse (dict) -- Apple Distribution Push Notification Service channel definition.
    ApplicationId (string) -- The ID of the application to which the channel applies.
    CreationDate (string) -- When was this segment created
    Id (string) -- The unique channel ID.
    IsArchived (boolean) -- Is this channel archived
    LastModifiedBy (string) -- Who last updated this entry
    LastModifiedDate (string) -- Last date this was updated
    Platform (string) -- The platform type. Will be APNS.
    Version (integer) -- Version of channel
    
    
    
    
    
    """
    pass

def update_application_settings(ApplicationId=None, WriteApplicationSettingsRequest=None):
    """
    Used to update the settings for an app.
    
    
    :example: response = client.update_application_settings(
        ApplicationId='string',
        WriteApplicationSettingsRequest={
            'Limits': {
                'Daily': 123,
                'Total': 123
            },
            'QuietTime': {
                'End': 'string',
                'Start': 'string'
            }
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type WriteApplicationSettingsRequest: dict
    :param WriteApplicationSettingsRequest: [REQUIRED] Creating application setting request
            Limits (dict) -- The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own.
            Daily (integer) -- The maximum number of messages that the campaign can send daily.
            Total (integer) -- The maximum total number of messages that the campaign can send.
            QuietTime (dict) -- The default quiet time for the app. Each campaign for this app sends no messages during this time unless the campaign overrides the default with a quiet time of its own.
            End (string) -- The default end time for quiet time in ISO 8601 format.
            Start (string) -- The default start time for quiet time in ISO 8601 format.
            

    :rtype: dict
    :return: {
        'ApplicationSettingsResource': {
            'ApplicationId': 'string',
            'LastModifiedDate': 'string',
            'Limits': {
                'Daily': 123,
                'Total': 123
            },
            'QuietTime': {
                'End': 'string',
                'Start': 'string'
            }
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    ApplicationSettingsResource (dict) -- Application settings.
    ApplicationId (string) -- The unique ID for the application.
    LastModifiedDate (string) -- The date that the settings were last updated in ISO 8601 format.
    Limits (dict) -- The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own.
    Daily (integer) -- The maximum number of messages that the campaign can send daily.
    Total (integer) -- The maximum total number of messages that the campaign can send.
    
    
    QuietTime (dict) -- The default quiet time for the app. Each campaign for this app sends no messages during this time unless the campaign overrides the default with a quiet time of its own.
    End (string) -- The default end time for quiet time in ISO 8601 format.
    Start (string) -- The default start time for quiet time in ISO 8601 format.
    
    
    
    
    
    
    
    """
    pass

def update_campaign(ApplicationId=None, CampaignId=None, WriteCampaignRequest=None):
    """
    Use to update a campaign.
    
    
    :example: response = client.update_campaign(
        ApplicationId='string',
        CampaignId='string',
        WriteCampaignRequest={
            'AdditionalTreatments': [
                {
                    'MessageConfiguration': {
                        'APNSMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'DefaultMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'GCMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        }
                    },
                    'Schedule': {
                        'EndTime': 'string',
                        'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY',
                        'IsLocalTime': True|False,
                        'QuietTime': {
                            'End': 'string',
                            'Start': 'string'
                        },
                        'StartTime': 'string',
                        'Timezone': 'string'
                    },
                    'SizePercent': 123,
                    'TreatmentDescription': 'string',
                    'TreatmentName': 'string'
                },
            ],
            'Description': 'string',
            'HoldoutPercent': 123,
            'IsPaused': True|False,
            'Limits': {
                'Daily': 123,
                'Total': 123
            },
            'MessageConfiguration': {
                'APNSMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'DefaultMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'GCMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                }
            },
            'Name': 'string',
            'Schedule': {
                'EndTime': 'string',
                'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY',
                'IsLocalTime': True|False,
                'QuietTime': {
                    'End': 'string',
                    'Start': 'string'
                },
                'StartTime': 'string',
                'Timezone': 'string'
            },
            'SegmentId': 'string',
            'SegmentVersion': 123,
            'TreatmentDescription': 'string',
            'TreatmentName': 'string'
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type CampaignId: string
    :param CampaignId: [REQUIRED]

    :type WriteCampaignRequest: dict
    :param WriteCampaignRequest: [REQUIRED] Used to create a campaign.
            AdditionalTreatments (list) -- Treatments that are defined in addition to the default treatment.
            (dict) -- Used to create a campaign treatment.
            MessageConfiguration (dict) -- The message configuration settings.
            APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP   Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK   Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL   The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            DefaultMessage (dict) -- The default message for all channels.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP   Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK   Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL   The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP   Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK   Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL   The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            
            Schedule (dict) -- The campaign schedule.
            EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
            Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE, HOURLY, DAILY, WEEKLY, MONTHLY
            IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
            QuietTime (dict) -- The time during which the campaign sends no messages.
            End (string) -- The default end time for quiet time in ISO 8601 format.
            Start (string) -- The default start time for quiet time in ISO 8601 format.
            StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
            Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
            SizePercent (integer) -- The allocated percentage of users for this treatment.
            TreatmentDescription (string) -- A custom description for the treatment.
            TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
            
            Description (string) -- A description of the campaign.
            HoldoutPercent (integer) -- The allocated percentage of end users who will not receive messages from this campaign.
            IsPaused (boolean) -- Indicates whether the campaign is paused. A paused campaign does not send messages unless you resume it by setting IsPaused to false.
            Limits (dict) -- The campaign limits settings.
            Daily (integer) -- The maximum number of messages that the campaign can send daily.
            Total (integer) -- The maximum total number of messages that the campaign can send.
            MessageConfiguration (dict) -- The message configuration settings.
            APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP   Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK   Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL   The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            DefaultMessage (dict) -- The default message for all channels.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP   Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK   Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL   The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP   Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK   Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL   The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            
            Name (string) -- The custom name of the campaign.
            Schedule (dict) -- The campaign schedule.
            EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
            Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE, HOURLY, DAILY, WEEKLY, MONTHLY
            IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
            QuietTime (dict) -- The time during which the campaign sends no messages.
            End (string) -- The default end time for quiet time in ISO 8601 format.
            Start (string) -- The default start time for quiet time in ISO 8601 format.
            StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
            Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
            SegmentId (string) -- The ID of the segment to which the campaign sends messages.
            SegmentVersion (integer) -- The version of the segment to which the campaign sends messages.
            TreatmentDescription (string) -- A custom description for the treatment.
            TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
            

    :rtype: dict
    :return: {
        'CampaignResponse': {
            'AdditionalTreatments': [
                {
                    'Id': 'string',
                    'MessageConfiguration': {
                        'APNSMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'DefaultMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'GCMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        }
                    },
                    'Schedule': {
                        'EndTime': 'string',
                        'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY',
                        'IsLocalTime': True|False,
                        'QuietTime': {
                            'End': 'string',
                            'Start': 'string'
                        },
                        'StartTime': 'string',
                        'Timezone': 'string'
                    },
                    'SizePercent': 123,
                    'State': {
                        'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'
                    },
                    'TreatmentDescription': 'string',
                    'TreatmentName': 'string'
                },
            ],
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'DefaultState': {
                'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'
            },
            'Description': 'string',
            'HoldoutPercent': 123,
            'Id': 'string',
            'IsPaused': True|False,
            'LastModifiedDate': 'string',
            'Limits': {
                'Daily': 123,
                'Total': 123
            },
            'MessageConfiguration': {
                'APNSMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'DefaultMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'GCMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                }
            },
            'Name': 'string',
            'Schedule': {
                'EndTime': 'string',
                'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY',
                'IsLocalTime': True|False,
                'QuietTime': {
                    'End': 'string',
                    'Start': 'string'
                },
                'StartTime': 'string',
                'Timezone': 'string'
            },
            'SegmentId': 'string',
            'SegmentVersion': 123,
            'State': {
                'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'
            },
            'TreatmentDescription': 'string',
            'TreatmentName': 'string',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    CampaignResponse (dict) -- Campaign definition
    AdditionalTreatments (list) -- Treatments that are defined in addition to the default treatment.
    (dict) -- Treatment resource
    Id (string) -- The unique treatment ID.
    MessageConfiguration (dict) -- The message configuration settings.
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    
    
    Schedule (dict) -- The campaign schedule.
    EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
    Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE, HOURLY, DAILY, WEEKLY, MONTHLY
    IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
    QuietTime (dict) -- The time during which the campaign sends no messages.
    End (string) -- The default end time for quiet time in ISO 8601 format.
    Start (string) -- The default start time for quiet time in ISO 8601 format.
    
    
    StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
    Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
    
    
    SizePercent (integer) -- The allocated percentage of users for this treatment.
    State (dict) -- The treatment status.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    TreatmentDescription (string) -- A custom description for the treatment.
    TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
    
    
    
    
    ApplicationId (string) -- The ID of the application to which the campaign applies.
    CreationDate (string) -- The date the campaign was created in ISO 8601 format.
    DefaultState (dict) -- The status of the campaign's default treatment. Only present for A/B test campaigns.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    Description (string) -- A description of the campaign.
    HoldoutPercent (integer) -- The allocated percentage of end users who will not receive messages from this campaign.
    Id (string) -- The unique campaign ID.
    IsPaused (boolean) -- Indicates whether the campaign is paused. A paused campaign does not send messages unless you resume it by setting IsPaused to false.
    LastModifiedDate (string) -- The date the campaign was last updated in ISO 8601 format.
    Limits (dict) -- The campaign limits settings.
    Daily (integer) -- The maximum number of messages that the campaign can send daily.
    Total (integer) -- The maximum total number of messages that the campaign can send.
    
    
    MessageConfiguration (dict) -- The message configuration settings.
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP  Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK  Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL  The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    
    
    Name (string) -- The custom name of the campaign.
    Schedule (dict) -- The campaign schedule.
    EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
    Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE, HOURLY, DAILY, WEEKLY, MONTHLY
    IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
    QuietTime (dict) -- The time during which the campaign sends no messages.
    End (string) -- The default end time for quiet time in ISO 8601 format.
    Start (string) -- The default start time for quiet time in ISO 8601 format.
    
    
    StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
    Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
    
    
    SegmentId (string) -- The ID of the segment to which the campaign sends messages.
    SegmentVersion (integer) -- The version of the segment to which the campaign sends messages.
    State (dict) -- The campaign status. An A/B test campaign will have a status of COMPLETED only when all treatments have a status of COMPLETED.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    TreatmentDescription (string) -- A custom description for the treatment.
    TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
    Version (integer) -- The campaign version number.
    
    
    
    
    
    """
    pass

def update_endpoint(ApplicationId=None, EndpointId=None, EndpointRequest=None):
    """
    Use to update an endpoint.
    
    
    :example: response = client.update_endpoint(
        ApplicationId='string',
        EndpointId='string',
        EndpointRequest={
            'Address': 'string',
            'Attributes': {
                'string': [
                    'string',
                ]
            },
            'ChannelType': 'APNS'|'GCM',
            'Demographic': {
                'AppVersion': 'string',
                'Locale': 'string',
                'Make': 'string',
                'Model': 'string',
                'ModelVersion': 'string',
                'Platform': 'string',
                'PlatformVersion': 'string',
                'Timezone': 'string'
            },
            'EffectiveDate': 'string',
            'EndpointStatus': 'string',
            'Location': {
                'City': 'string',
                'Country': 'string',
                'Latitude': 123.0,
                'Longitude': 123.0,
                'PostalCode': 'string',
                'Region': 'string'
            },
            'Metrics': {
                'string': 123.0
            },
            'OptOut': 'string',
            'RequestId': 'string',
            'User': {
                'UserAttributes': {
                    'string': [
                        'string',
                    ]
                },
                'UserId': 'string'
            }
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type EndpointId: string
    :param EndpointId: [REQUIRED]

    :type EndpointRequest: dict
    :param EndpointRequest: [REQUIRED] Endpoint update request
            Address (string) -- The address or token of the endpoint as provided by your push provider (e.g. DeviceToken or RegistrationId).
            Attributes (dict) -- Custom attributes that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create a segment.
            (string) --
            (list) --
            (string) --
            
            ChannelType (string) -- The channel type. Valid values: APNS, GCM
            Demographic (dict) -- The endpoint demographic attributes.
            AppVersion (string) -- The version of the application associated with the endpoint.
            Locale (string) -- The endpoint locale in the following format: The ISO 639-1 alpha-2 code, followed by an underscore, followed by an ISO 3166-1 alpha-2 value.
            Make (string) -- The endpoint make, such as such as Apple or Samsung.
            Model (string) -- The endpoint model, such as iPhone.
            ModelVersion (string) -- The endpoint model version.
            Platform (string) -- The endpoint platform, such as ios or android.
            PlatformVersion (string) -- The endpoint platform version.
            Timezone (string) -- The timezone of the endpoint. Specified as a tz database value, such as Americas/Los_Angeles.
            EffectiveDate (string) -- The last time the endpoint was updated. Provided in ISO 8601 format.
            EndpointStatus (string) -- The endpoint status. Can be either ACTIVE or INACTIVE. Will be set to INACTIVE if a delivery fails. Will be set to ACTIVE if the address is updated.
            Location (dict) -- The endpoint location attributes.
            City (string) -- The city where the endpoint is located.
            Country (string) -- Country according to ISO 3166-1 Alpha-2 codes. For example, US.
            Latitude (float) -- The latitude of the endpoint location. Rounded to one decimal (Roughly corresponding to a mile).
            Longitude (float) -- The longitude of the endpoint location. Rounded to one decimal (Roughly corresponding to a mile).
            PostalCode (string) -- The postal code or zip code of the endpoint.
            Region (string) -- The region of the endpoint location. For example, corresponds to a state in US.
            Metrics (dict) -- Custom metrics that your app reports to Amazon Pinpoint.
            (string) --
            (float) --
            
            OptOut (string) -- Indicates whether a user has opted out of receiving messages with one of the following values: ALL   User receives all messages. NONE   User receives no messages.
            RequestId (string) -- The unique ID for the most recent request to update the endpoint.
            User (dict) -- Custom user-specific attributes that your app reports to Amazon Pinpoint.
            UserAttributes (dict) -- Custom attributes specific to the user.
            (string) --
            (list) --
            (string) --
            
            UserId (string) -- The unique ID of the user.
            

    :rtype: dict
    :return: {
        'MessageBody': {
            'Message': 'string',
            'RequestID': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- 202 response
    MessageBody (dict) -- Simple message object.
    Message (string) -- The error message returned from the API.
    RequestID (string) -- The unique message body ID.
    
    
    
    
    
    """
    pass

def update_endpoints_batch(ApplicationId=None, EndpointBatchRequest=None):
    """
    Use to update a batch of endpoints.
    
    
    :example: response = client.update_endpoints_batch(
        ApplicationId='string',
        EndpointBatchRequest={
            'Item': [
                {
                    'Address': 'string',
                    'Attributes': {
                        'string': [
                            'string',
                        ]
                    },
                    'ChannelType': 'APNS'|'GCM',
                    'Demographic': {
                        'AppVersion': 'string',
                        'Locale': 'string',
                        'Make': 'string',
                        'Model': 'string',
                        'ModelVersion': 'string',
                        'Platform': 'string',
                        'PlatformVersion': 'string',
                        'Timezone': 'string'
                    },
                    'EffectiveDate': 'string',
                    'EndpointStatus': 'string',
                    'Id': 'string',
                    'Location': {
                        'City': 'string',
                        'Country': 'string',
                        'Latitude': 123.0,
                        'Longitude': 123.0,
                        'PostalCode': 'string',
                        'Region': 'string'
                    },
                    'Metrics': {
                        'string': 123.0
                    },
                    'OptOut': 'string',
                    'RequestId': 'string',
                    'User': {
                        'UserAttributes': {
                            'string': [
                                'string',
                            ]
                        },
                        'UserId': 'string'
                    }
                },
            ]
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type EndpointBatchRequest: dict
    :param EndpointBatchRequest: [REQUIRED] Endpoint batch update request.
            Item (list) -- List of items to update. Maximum 100 items
            (dict) -- Endpoint update request
            Address (string) -- The address or token of the endpoint as provided by your push provider (e.g. DeviceToken or RegistrationId).
            Attributes (dict) -- Custom attributes that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create a segment.
            (string) --
            (list) --
            (string) --
            
            ChannelType (string) -- The channel type. Valid values: APNS, GCM
            Demographic (dict) -- The endpoint demographic attributes.
            AppVersion (string) -- The version of the application associated with the endpoint.
            Locale (string) -- The endpoint locale in the following format: The ISO 639-1 alpha-2 code, followed by an underscore, followed by an ISO 3166-1 alpha-2 value.
            Make (string) -- The endpoint make, such as such as Apple or Samsung.
            Model (string) -- The endpoint model, such as iPhone.
            ModelVersion (string) -- The endpoint model version.
            Platform (string) -- The endpoint platform, such as ios or android.
            PlatformVersion (string) -- The endpoint platform version.
            Timezone (string) -- The timezone of the endpoint. Specified as a tz database value, such as Americas/Los_Angeles.
            EffectiveDate (string) -- The last time the endpoint was updated. Provided in ISO 8601 format.
            EndpointStatus (string) -- The endpoint status. Can be either ACTIVE or INACTIVE. Will be set to INACTIVE if a delivery fails. Will be set to ACTIVE if the address is updated.
            Id (string) -- The unique Id for the Endpoint in the batch.
            Location (dict) -- The endpoint location attributes.
            City (string) -- The city where the endpoint is located.
            Country (string) -- Country according to ISO 3166-1 Alpha-2 codes. For example, US.
            Latitude (float) -- The latitude of the endpoint location. Rounded to one decimal (Roughly corresponding to a mile).
            Longitude (float) -- The longitude of the endpoint location. Rounded to one decimal (Roughly corresponding to a mile).
            PostalCode (string) -- The postal code or zip code of the endpoint.
            Region (string) -- The region of the endpoint location. For example, corresponds to a state in US.
            Metrics (dict) -- Custom metrics that your app reports to Amazon Pinpoint.
            (string) --
            (float) --
            
            OptOut (string) -- Indicates whether a user has opted out of receiving messages with one of the following values: ALL   User receives all messages. NONE   User receives no messages.
            RequestId (string) -- The unique ID for the most recent request to update the endpoint.
            User (dict) -- Custom user-specific attributes that your app reports to Amazon Pinpoint.
            UserAttributes (dict) -- Custom attributes specific to the user.
            (string) --
            (list) --
            (string) --
            
            UserId (string) -- The unique ID of the user.
            
            

    :rtype: dict
    :return: {
        'MessageBody': {
            'Message': 'string',
            'RequestID': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- 202 response
    MessageBody (dict) -- Simple message object.
    Message (string) -- The error message returned from the API.
    RequestID (string) -- The unique message body ID.
    
    
    
    
    
    """
    pass

def update_gcm_channel(ApplicationId=None, GCMChannelRequest=None):
    """
    Use to update the GCM channel for an app.
    
    
    :example: response = client.update_gcm_channel(
        ApplicationId='string',
        GCMChannelRequest={
            'ApiKey': 'string'
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type GCMChannelRequest: dict
    :param GCMChannelRequest: [REQUIRED] Google Cloud Messaging credentials
            ApiKey (string) -- Platform credential API key from Google.
            

    :rtype: dict
    :return: {
        'GCMChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Credential': 'string',
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    GCMChannelResponse (dict) -- Google Cloud Messaging channel definition
    ApplicationId (string) -- The ID of the application to which the channel applies.
    CreationDate (string) -- When was this segment created
    Credential (string) -- The GCM API key from Google.
    Id (string) -- The unique channel ID.
    IsArchived (boolean) -- Is this channel archived
    LastModifiedBy (string) -- Who last updated this entry
    LastModifiedDate (string) -- Last date this was updated
    Platform (string) -- The platform type. Will be GCM
    Version (integer) -- Version of channel
    
    
    
    
    
    """
    pass

def update_segment(ApplicationId=None, SegmentId=None, WriteSegmentRequest=None):
    """
    Use to update a segment.
    
    
    :example: response = client.update_segment(
        ApplicationId='string',
        SegmentId='string',
        WriteSegmentRequest={
            'Dimensions': {
                'Attributes': {
                    'string': {
                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'Behavior': {
                    'Recency': {
                        'Duration': 'HR_24'|'DAY_7'|'DAY_14'|'DAY_30',
                        'RecencyType': 'ACTIVE'|'INACTIVE'
                    }
                },
                'Demographic': {
                    'AppVersion': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'DeviceType': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Make': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Model': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Platform': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'Location': {
                    'Country': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'UserAttributes': {
                    'string': {
                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                }
            },
            'Name': 'string'
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type SegmentId: string
    :param SegmentId: [REQUIRED]

    :type WriteSegmentRequest: dict
    :param WriteSegmentRequest: [REQUIRED] Segment definition.
            Dimensions (dict) -- The segment dimensions attributes.
            Attributes (dict) -- Custom segment attributes.
            (string) --
            (dict) -- Custom attibute dimension
            AttributeType (string) -- The type of dimension: INCLUSIVE   Endpoints that match the criteria are included in the segment. EXCLUSIVE   Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            
            Behavior (dict) -- The segment behaviors attributes.
            Recency (dict) -- The recency of use.
            Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
            RecencyType (string) -- The recency dimension type: ACTIVE   Users who have used your app within the specified duration are included in the segment. INACTIVE   Users who have not used your app within the specified duration are included in the segment.
            
            Demographic (dict) -- The segment demographics attributes.
            AppVersion (dict) -- The app version criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE   Endpoints that match the criteria are included in the segment. EXCLUSIVE   Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            DeviceType (dict) -- The device type criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE   Endpoints that match the criteria are included in the segment. EXCLUSIVE   Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Make (dict) -- The device make criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE   Endpoints that match the criteria are included in the segment. EXCLUSIVE   Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Model (dict) -- The device model criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE   Endpoints that match the criteria are included in the segment. EXCLUSIVE   Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Platform (dict) -- The device platform criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE   Endpoints that match the criteria are included in the segment. EXCLUSIVE   Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Location (dict) -- The segment location attributes.
            Country (dict) -- The country filter according to ISO 3166-1 Alpha-2 codes.
            DimensionType (string) -- The type of dimension: INCLUSIVE   Endpoints that match the criteria are included in the segment. EXCLUSIVE   Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            UserAttributes (dict) -- Custom segment user attributes.
            (string) --
            (dict) -- Custom attibute dimension
            AttributeType (string) -- The type of dimension: INCLUSIVE   Endpoints that match the criteria are included in the segment. EXCLUSIVE   Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            
            Name (string) -- The name of segment
            

    :rtype: dict
    :return: {
        'SegmentResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Dimensions': {
                'Attributes': {
                    'string': {
                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'Behavior': {
                    'Recency': {
                        'Duration': 'HR_24'|'DAY_7'|'DAY_14'|'DAY_30',
                        'RecencyType': 'ACTIVE'|'INACTIVE'
                    }
                },
                'Demographic': {
                    'AppVersion': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'DeviceType': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Make': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Model': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Platform': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'Location': {
                    'Country': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'UserAttributes': {
                    'string': {
                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                }
            },
            'Id': 'string',
            'ImportDefinition': {
                'ExternalId': 'string',
                'Format': 'CSV'|'JSON',
                'RoleArn': 'string',
                'S3Url': 'string',
                'Size': 123
            },
            'LastModifiedDate': 'string',
            'Name': 'string',
            'SegmentType': 'DIMENSIONAL'|'IMPORT',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    SegmentResponse (dict) -- Segment definition.
    ApplicationId (string) -- The ID of the application to which the segment applies.
    CreationDate (string) -- The date the segment was created in ISO 8601 format.
    Dimensions (dict) -- The segment dimensions attributes.
    Attributes (dict) -- Custom segment attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    Behavior (dict) -- The segment behaviors attributes.
    Recency (dict) -- The recency of use.
    Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
    RecencyType (string) -- The recency dimension type: ACTIVE  Users who have used your app within the specified duration are included in the segment. INACTIVE  Users who have not used your app within the specified duration are included in the segment.
    
    
    
    
    Demographic (dict) -- The segment demographics attributes.
    AppVersion (dict) -- The app version criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    DeviceType (dict) -- The device type criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Make (dict) -- The device make criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Model (dict) -- The device model criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Platform (dict) -- The device platform criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    Location (dict) -- The segment location attributes.
    Country (dict) -- The country filter according to ISO 3166-1 Alpha-2 codes.
    DimensionType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    UserAttributes (dict) -- Custom segment user attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE  Endpoints that match the criteria are included in the segment. EXCLUSIVE  Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    
    
    Id (string) -- The unique segment ID.
    ImportDefinition (dict) -- The import job settings.
    ExternalId (string) -- A unique, custom ID assigned to the IAM role that restricts who can assume the role.
    Format (string) -- The format of the endpoint files that were imported to create this segment. Valid values: CSV, JSON
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the endpoints in Amazon S3.
    S3Url (string) -- A URL that points to the Amazon S3 location from which the endpoints for this segment were imported.
    Size (integer) -- The number of endpoints that were successfully imported to create this segment.
    
    
    LastModifiedDate (string) -- The date the segment was last updated in ISO 8601 format.
    Name (string) -- The name of segment
    SegmentType (string) -- The segment type: DIMENSIONAL  A dynamic segment built from selection criteria based on endpoint data reported by your app. You create this type of segment by using the segment builder in the Amazon Pinpoint console or by making a POST request to the segments resource. IMPORT  A static segment built from an imported set of endpoint definitions. You create this type of segment by importing a segment in the Amazon Pinpoint console or by making a POST request to the jobs/import resource.
    Version (integer) -- The segment version number.
    
    
    
    
    
    """
    pass

