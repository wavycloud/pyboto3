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

def create_app(CreateApplicationRequest=None):
    """
    Creates or updates an app.
    See also: AWS API Documentation
    
    
    :example: response = client.create_app(
        CreateApplicationRequest={
            'Name': 'string'
        }
    )
    
    
    :type CreateApplicationRequest: dict
    :param CreateApplicationRequest: [REQUIRED] Application Request.
            Name (string) -- The display name of the application. Used in the Amazon Pinpoint console.
            

    :rtype: dict
    :return: {
        'ApplicationResponse': {
            'Id': 'string',
            'Name': 'string'
        }
    }
    
    
    :returns: 
    (dict) --
    ApplicationResponse (dict) -- Application Response.
    Id (string) -- The unique application ID.
    Name (string) -- The display name of the application.
    
    
    
    
    
    """
    pass

def create_campaign(ApplicationId=None, WriteCampaignRequest=None):
    """
    Creates or updates a campaign.
    See also: AWS API Documentation
    
    
    :example: response = client.create_campaign(
        ApplicationId='string',
        WriteCampaignRequest={
            'AdditionalTreatments': [
                {
                    'MessageConfiguration': {
                        'ADMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'APNSMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'BaiduMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'DefaultMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'EmailMessage': {
                            'Body': 'string',
                            'FromAddress': 'string',
                            'HtmlBody': 'string',
                            'Title': 'string'
                        },
                        'GCMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'SMSMessage': {
                            'Body': 'string',
                            'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                            'SenderId': 'string'
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
            'Hook': {
                'LambdaFunctionName': 'string',
                'Mode': 'DELIVERY'|'FILTER',
                'WebUrl': 'string'
            },
            'IsPaused': True|False,
            'Limits': {
                'Daily': 123,
                'MaximumDuration': 123,
                'MessagesPerSecond': 123,
                'Total': 123
            },
            'MessageConfiguration': {
                'ADMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'APNSMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'BaiduMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'DefaultMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'EmailMessage': {
                    'Body': 'string',
                    'FromAddress': 'string',
                    'HtmlBody': 'string',
                    'Title': 'string'
                },
                'GCMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'SMSMessage': {
                    'Body': 'string',
                    'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                    'SenderId': 'string'
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
            ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            DefaultMessage (dict) -- The default message for all channels.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            EmailMessage (dict) -- The email message configuration.
            Body (string) -- The email text body.
            FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
            HtmlBody (string) -- The email html body.
            Title (string) -- The email title (Or subject).
            GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            SMSMessage (dict) -- The SMS message configuration.
            Body (string) -- The SMS text body.
            MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
            SenderId (string) -- Sender ID of sent message.
            
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
            Hook (dict) -- Campaign hook information.
            LambdaFunctionName (string) -- Lambda function name or arn to be called for delivery
            Mode (string) -- What mode Lambda should be invoked in.
            WebUrl (string) -- Web URL to call for hook. If the URL has authentication specified it will be added as authentication to the request
            IsPaused (boolean) -- Indicates whether the campaign is paused. A paused campaign does not send messages unless you resume it by setting IsPaused to false.
            Limits (dict) -- The campaign limits settings.
            Daily (integer) -- The maximum number of messages that the campaign can send daily.
            MaximumDuration (integer) -- The length of time (in seconds) that the campaign can run before it ends and message deliveries stop. This duration begins at the scheduled start time for the campaign. The minimum value is 60.
            MessagesPerSecond (integer) -- The number of messages that the campaign can send per second. The minimum value is 50, and the maximum is 20000.
            Total (integer) -- The maximum total number of messages that the campaign can send.
            MessageConfiguration (dict) -- The message configuration settings.
            ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            DefaultMessage (dict) -- The default message for all channels.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            EmailMessage (dict) -- The email message configuration.
            Body (string) -- The email text body.
            FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
            HtmlBody (string) -- The email html body.
            Title (string) -- The email title (Or subject).
            GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            SMSMessage (dict) -- The SMS message configuration.
            Body (string) -- The SMS text body.
            MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
            SenderId (string) -- Sender ID of sent message.
            
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
                        'ADMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'APNSMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'BaiduMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'DefaultMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'EmailMessage': {
                            'Body': 'string',
                            'FromAddress': 'string',
                            'HtmlBody': 'string',
                            'Title': 'string'
                        },
                        'GCMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'SMSMessage': {
                            'Body': 'string',
                            'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                            'SenderId': 'string'
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
            'Hook': {
                'LambdaFunctionName': 'string',
                'Mode': 'DELIVERY'|'FILTER',
                'WebUrl': 'string'
            },
            'Id': 'string',
            'IsPaused': True|False,
            'LastModifiedDate': 'string',
            'Limits': {
                'Daily': 123,
                'MaximumDuration': 123,
                'MessagesPerSecond': 123,
                'Total': 123
            },
            'MessageConfiguration': {
                'ADMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'APNSMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'BaiduMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'DefaultMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'EmailMessage': {
                    'Body': 'string',
                    'FromAddress': 'string',
                    'HtmlBody': 'string',
                    'Title': 'string'
                },
                'GCMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'SMSMessage': {
                    'Body': 'string',
                    'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                    'SenderId': 'string'
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
    (dict) --
    CampaignResponse (dict) -- Campaign definition
    AdditionalTreatments (list) -- Treatments that are defined in addition to the default treatment.
    (dict) -- Treatment resource
    Id (string) -- The unique treatment ID.
    MessageConfiguration (dict) -- The message configuration settings.
    ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    EmailMessage (dict) -- The email message configuration.
    Body (string) -- The email text body.
    FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
    HtmlBody (string) -- The email html body.
    Title (string) -- The email title (Or subject).
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    SMSMessage (dict) -- The SMS message configuration.
    Body (string) -- The SMS text body.
    MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
    SenderId (string) -- Sender ID of sent message.
    
    
    
    
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
    Hook (dict) -- Campaign hook information.
    LambdaFunctionName (string) -- Lambda function name or arn to be called for delivery
    Mode (string) -- What mode Lambda should be invoked in.
    WebUrl (string) -- Web URL to call for hook. If the URL has authentication specified it will be added as authentication to the request
    
    
    Id (string) -- The unique campaign ID.
    IsPaused (boolean) -- Indicates whether the campaign is paused. A paused campaign does not send messages unless you resume it by setting IsPaused to false.
    LastModifiedDate (string) -- The date the campaign was last updated in ISO 8601 format.
    Limits (dict) -- The campaign limits settings.
    Daily (integer) -- The maximum number of messages that the campaign can send daily.
    MaximumDuration (integer) -- The length of time (in seconds) that the campaign can run before it ends and message deliveries stop. This duration begins at the scheduled start time for the campaign. The minimum value is 60.
    MessagesPerSecond (integer) -- The number of messages that the campaign can send per second. The minimum value is 50, and the maximum is 20000.
    Total (integer) -- The maximum total number of messages that the campaign can send.
    
    
    MessageConfiguration (dict) -- The message configuration settings.
    ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    EmailMessage (dict) -- The email message configuration.
    Body (string) -- The email text body.
    FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
    HtmlBody (string) -- The email html body.
    Title (string) -- The email title (Or subject).
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    SMSMessage (dict) -- The SMS message configuration.
    Body (string) -- The SMS text body.
    MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
    SenderId (string) -- Sender ID of sent message.
    
    
    
    
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

def create_export_job(ApplicationId=None, ExportJobRequest=None):
    """
    Creates an export job.
    See also: AWS API Documentation
    
    
    :example: response = client.create_export_job(
        ApplicationId='string',
        ExportJobRequest={
            'RoleArn': 'string',
            'S3UrlPrefix': 'string',
            'SegmentId': 'string'
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type ExportJobRequest: dict
    :param ExportJobRequest: [REQUIRED]
            RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the Amazon S3 location that endpoints will be exported to.
            S3UrlPrefix (string) -- A URL that points to the location within an Amazon S3 bucket that will receive the export. The location is typically a folder with multiple files. The URL should follow this format: s3://bucket-name/folder-name/ Amazon Pinpoint will export endpoints to this location.
            SegmentId (string) -- The ID of the segment to export endpoints from. If not present all endpoints will be exported.
            

    :rtype: dict
    :return: {
        'ExportJobResponse': {
            'ApplicationId': 'string',
            'CompletedPieces': 123,
            'CompletionDate': 'string',
            'CreationDate': 'string',
            'Definition': {
                'RoleArn': 'string',
                'S3UrlPrefix': 'string',
                'SegmentId': 'string'
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
    (dict) --
    ExportJobResponse (dict) --
    ApplicationId (string) -- The unique ID of the application to which the job applies.
    CompletedPieces (integer) -- The number of pieces that have successfully completed as of the time of the request.
    CompletionDate (string) -- The date the job completed in ISO 8601 format.
    CreationDate (string) -- The date the job was created in ISO 8601 format.
    Definition (dict) -- The export job settings.
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the Amazon S3 location that endpoints will be exported to.
    S3UrlPrefix (string) -- A URL that points to the location within an Amazon S3 bucket that will receive the export. The location is typically a folder with multiple files. The URL should follow this format: s3://bucket-name/folder-name/ Amazon Pinpoint will export endpoints to this location.
    SegmentId (string) -- The ID of the segment to export endpoints from. If not present, all endpoints are exported.
    
    
    FailedPieces (integer) -- The number of pieces that failed to be processed as of the time of the request.
    Failures (list) -- Provides up to 100 of the first failed entries for the job, if any exist.
    (string) --
    
    
    Id (string) -- The unique ID of the job.
    JobStatus (string) -- The status of the job. Valid values: CREATED, INITIALIZING, PROCESSING, COMPLETING, COMPLETED, FAILING, FAILED The job status is FAILED if one or more pieces failed.
    TotalFailures (integer) -- The number of endpoints that were not processed; for example, because of syntax errors.
    TotalPieces (integer) -- The total number of pieces that must be processed to finish the job. Each piece is an approximately equal portion of the endpoints.
    TotalProcessed (integer) -- The number of endpoints that were processed by the job.
    Type (string) -- The job type. Will be 'EXPORT'.
    
    
    
    
    
    """
    pass

def create_import_job(ApplicationId=None, ImportJobRequest=None):
    """
    Creates or updates an import job.
    See also: AWS API Documentation
    
    
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
            ExternalId (string) -- DEPRECATED. Your AWS account ID, which you assigned to the ExternalID key in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This requirement is removed, and external IDs are not recommended for IAM roles assumed by Amazon Pinpoint.
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
    (dict) --
    ImportJobResponse (dict) --
    ApplicationId (string) -- The unique ID of the application to which the import job applies.
    CompletedPieces (integer) -- The number of pieces that have successfully imported as of the time of the request.
    CompletionDate (string) -- The date the import job completed in ISO 8601 format.
    CreationDate (string) -- The date the import job was created in ISO 8601 format.
    Definition (dict) -- The import job settings.
    DefineSegment (boolean) -- Sets whether the endpoints create a segment when they are imported.
    ExternalId (string) -- DEPRECATED. Your AWS account ID, which you assigned to the ExternalID key in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This requirement is removed, and external IDs are not recommended for IAM roles assumed by Amazon Pinpoint.
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
    See also: AWS API Documentation
    
    
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
                    'Channel': {
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
            AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            
            Behavior (dict) -- The segment behaviors attributes.
            Recency (dict) -- The recency of use.
            Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
            RecencyType (string) -- The recency dimension type: ACTIVE - Users who have used your app within the specified duration are included in the segment. INACTIVE - Users who have not used your app within the specified duration are included in the segment.
            
            Demographic (dict) -- The segment demographics attributes.
            AppVersion (dict) -- The app version criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Channel (dict) -- The channel criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            DeviceType (dict) -- The device type criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Make (dict) -- The device make criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Model (dict) -- The device model criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Platform (dict) -- The device platform criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Location (dict) -- The segment location attributes.
            Country (dict) -- The country filter according to ISO 3166-1 Alpha-2 codes.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            UserAttributes (dict) -- Custom segment user attributes.
            (string) --
            (dict) -- Custom attibute dimension
            AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
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
                    'Channel': {
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
                'ChannelCounts': {
                    'string': 123
                },
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
    (dict) --
    SegmentResponse (dict) -- Segment definition.
    ApplicationId (string) -- The ID of the application to which the segment applies.
    CreationDate (string) -- The date the segment was created in ISO 8601 format.
    Dimensions (dict) -- The segment dimensions attributes.
    Attributes (dict) -- Custom segment attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    Behavior (dict) -- The segment behaviors attributes.
    Recency (dict) -- The recency of use.
    Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
    RecencyType (string) -- The recency dimension type: ACTIVE - Users who have used your app within the specified duration are included in the segment. INACTIVE - Users who have not used your app within the specified duration are included in the segment.
    
    
    
    
    Demographic (dict) -- The segment demographics attributes.
    AppVersion (dict) -- The app version criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Channel (dict) -- The channel criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    DeviceType (dict) -- The device type criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Make (dict) -- The device make criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Model (dict) -- The device model criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Platform (dict) -- The device platform criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    Location (dict) -- The segment location attributes.
    Country (dict) -- The country filter according to ISO 3166-1 Alpha-2 codes.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    UserAttributes (dict) -- Custom segment user attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    
    
    Id (string) -- The unique segment ID.
    ImportDefinition (dict) -- The import job settings.
    ChannelCounts (dict) -- Channel type counts
    (string) --
    (integer) --
    
    
    
    
    ExternalId (string) -- DEPRECATED. Your AWS account ID, which you assigned to the ExternalID key in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This requirement is removed, and external IDs are not recommended for IAM roles assumed by Amazon Pinpoint.
    Format (string) -- The format of the endpoint files that were imported to create this segment. Valid values: CSV, JSON
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the endpoints in Amazon S3.
    S3Url (string) -- A URL that points to the Amazon S3 location from which the endpoints for this segment were imported.
    Size (integer) -- The number of endpoints that were successfully imported to create this segment.
    
    
    LastModifiedDate (string) -- The date the segment was last updated in ISO 8601 format.
    Name (string) -- The name of segment
    SegmentType (string) -- The segment type: DIMENSIONAL - A dynamic segment built from selection criteria based on endpoint data reported by your app. You create this type of segment by using the segment builder in the Amazon Pinpoint console or by making a POST request to the segments resource. IMPORT - A static segment built from an imported set of endpoint definitions. You create this type of segment by importing a segment in the Amazon Pinpoint console or by making a POST request to the jobs/import resource.
    Version (integer) -- The segment version number.
    
    
    
    
    
    """
    pass

def delete_adm_channel(ApplicationId=None):
    """
    Delete an ADM channel
    See also: AWS API Documentation
    
    
    :example: response = client.delete_adm_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :rtype: dict
    :return: {
        'ADMChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
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

def delete_apns_channel(ApplicationId=None):
    """
    Deletes the APNs channel for an app.
    See also: AWS API Documentation
    
    
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
            'DefaultAuthenticationMethod': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'HasTokenKey': True|False,
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

def delete_apns_sandbox_channel(ApplicationId=None):
    """
    Delete an APNS sandbox channel
    See also: AWS API Documentation
    
    
    :example: response = client.delete_apns_sandbox_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :rtype: dict
    :return: {
        'APNSSandboxChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'DefaultAuthenticationMethod': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'HasTokenKey': True|False,
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

def delete_apns_voip_channel(ApplicationId=None):
    """
    Delete an APNS VoIP channel
    See also: AWS API Documentation
    
    
    :example: response = client.delete_apns_voip_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :rtype: dict
    :return: {
        'APNSVoipChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'DefaultAuthenticationMethod': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'HasTokenKey': True|False,
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

def delete_apns_voip_sandbox_channel(ApplicationId=None):
    """
    Delete an APNS VoIP sandbox channel
    See also: AWS API Documentation
    
    
    :example: response = client.delete_apns_voip_sandbox_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :rtype: dict
    :return: {
        'APNSVoipSandboxChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'DefaultAuthenticationMethod': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'HasTokenKey': True|False,
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

def delete_app(ApplicationId=None):
    """
    Deletes an app.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_app(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :rtype: dict
    :return: {
        'ApplicationResponse': {
            'Id': 'string',
            'Name': 'string'
        }
    }
    
    
    """
    pass

def delete_baidu_channel(ApplicationId=None):
    """
    Delete a BAIDU GCM channel
    See also: AWS API Documentation
    
    
    :example: response = client.delete_baidu_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :rtype: dict
    :return: {
        'BaiduChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Credential': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
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
    See also: AWS API Documentation
    
    
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
                        'ADMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'APNSMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'BaiduMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'DefaultMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'EmailMessage': {
                            'Body': 'string',
                            'FromAddress': 'string',
                            'HtmlBody': 'string',
                            'Title': 'string'
                        },
                        'GCMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'SMSMessage': {
                            'Body': 'string',
                            'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                            'SenderId': 'string'
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
            'Hook': {
                'LambdaFunctionName': 'string',
                'Mode': 'DELIVERY'|'FILTER',
                'WebUrl': 'string'
            },
            'Id': 'string',
            'IsPaused': True|False,
            'LastModifiedDate': 'string',
            'Limits': {
                'Daily': 123,
                'MaximumDuration': 123,
                'MessagesPerSecond': 123,
                'Total': 123
            },
            'MessageConfiguration': {
                'ADMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'APNSMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'BaiduMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'DefaultMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'EmailMessage': {
                    'Body': 'string',
                    'FromAddress': 'string',
                    'HtmlBody': 'string',
                    'Title': 'string'
                },
                'GCMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'SMSMessage': {
                    'Body': 'string',
                    'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                    'SenderId': 'string'
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
    (dict) --
    CampaignResponse (dict) -- Campaign definition
    AdditionalTreatments (list) -- Treatments that are defined in addition to the default treatment.
    (dict) -- Treatment resource
    Id (string) -- The unique treatment ID.
    MessageConfiguration (dict) -- The message configuration settings.
    ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    EmailMessage (dict) -- The email message configuration.
    Body (string) -- The email text body.
    FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
    HtmlBody (string) -- The email html body.
    Title (string) -- The email title (Or subject).
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    SMSMessage (dict) -- The SMS message configuration.
    Body (string) -- The SMS text body.
    MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
    SenderId (string) -- Sender ID of sent message.
    
    
    
    
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
    Hook (dict) -- Campaign hook information.
    LambdaFunctionName (string) -- Lambda function name or arn to be called for delivery
    Mode (string) -- What mode Lambda should be invoked in.
    WebUrl (string) -- Web URL to call for hook. If the URL has authentication specified it will be added as authentication to the request
    
    
    Id (string) -- The unique campaign ID.
    IsPaused (boolean) -- Indicates whether the campaign is paused. A paused campaign does not send messages unless you resume it by setting IsPaused to false.
    LastModifiedDate (string) -- The date the campaign was last updated in ISO 8601 format.
    Limits (dict) -- The campaign limits settings.
    Daily (integer) -- The maximum number of messages that the campaign can send daily.
    MaximumDuration (integer) -- The length of time (in seconds) that the campaign can run before it ends and message deliveries stop. This duration begins at the scheduled start time for the campaign. The minimum value is 60.
    MessagesPerSecond (integer) -- The number of messages that the campaign can send per second. The minimum value is 50, and the maximum is 20000.
    Total (integer) -- The maximum total number of messages that the campaign can send.
    
    
    MessageConfiguration (dict) -- The message configuration settings.
    ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    EmailMessage (dict) -- The email message configuration.
    Body (string) -- The email text body.
    FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
    HtmlBody (string) -- The email html body.
    Title (string) -- The email title (Or subject).
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    SMSMessage (dict) -- The SMS message configuration.
    Body (string) -- The SMS text body.
    MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
    SenderId (string) -- Sender ID of sent message.
    
    
    
    
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

def delete_email_channel(ApplicationId=None):
    """
    Delete an email channel
    See also: AWS API Documentation
    
    
    :example: response = client.delete_email_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :rtype: dict
    :return: {
        'EmailChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Enabled': True|False,
            'FromAddress': 'string',
            'HasCredential': True|False,
            'Id': 'string',
            'Identity': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'RoleArn': 'string',
            'Version': 123
        }
    }
    
    
    """
    pass

def delete_endpoint(ApplicationId=None, EndpointId=None):
    """
    Deletes an endpoint.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_endpoint(
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
            'ChannelType': 'GCM'|'APNS'|'APNS_SANDBOX'|'APNS_VOIP'|'APNS_VOIP_SANDBOX'|'ADM'|'SMS'|'EMAIL'|'BAIDU'|'CUSTOM',
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
            }
        }
    }
    
    
    :returns: 
    (dict) -- 202 response
    EndpointResponse (dict) -- Endpoint response
    Address (string) -- The address or token of the endpoint as provided by your push provider (e.g. DeviceToken or RegistrationId).
    ApplicationId (string) -- The ID of the application associated with the endpoint.
    Attributes (dict) -- Custom attributes that describe the endpoint by associating a name with an array of values. For example, an attribute named "interests" might have the values ["science", "politics", "travel"]. You can use these attributes as selection criteria when you create a segment of users to engage with a messaging campaign. The following characters are not recommended in attribute names: # : ? /. The Amazon Pinpoint console does not display attributes that include these characters in the name. This limitation does not apply to attribute values.
    (string) --
    (list) --
    (string) --
    
    
    
    
    
    
    ChannelType (string) -- The channel type. Valid values: GCM | APNS | APNS_SANDBOX | APNS_VOIP | APNS_VOIP_SANDBOX | ADM | SMS | EMAIL | BAIDU
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
    
    
    
    
    OptOut (string) -- Indicates whether a user has opted out of receiving messages with one of the following values: ALL - User has opted out of all messages. NONE - Users has not opted out and receives all messages.
    RequestId (string) -- The unique ID for the most recent request to update the endpoint.
    User (dict) -- Custom user-specific attributes that your app reports to Amazon Pinpoint.
    UserAttributes (dict) -- Custom attributes that describe an end user by associating a name with an array of values. For example, an attribute named "interests" might have the values ["science", "politics", "travel"]. You can use these attributes as selection criteria when you create a segment of users to engage with a messaging campaign. The following characters are not recommended in attribute names: # : ? /. The Amazon Pinpoint console does not display attributes that include these characters in the name. This limitation does not apply to attribute values.
    (string) --
    (list) --
    (string) --
    
    
    
    
    
    
    UserId (string) -- The unique ID of the user.
    
    
    
    
    
    
    
    """
    pass

def delete_event_stream(ApplicationId=None):
    """
    Deletes the event stream for an app.
    See also: AWS API Documentation
    
    
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
    See also: AWS API Documentation
    
    
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
            'Enabled': True|False,
            'HasCredential': True|False,
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
    See also: AWS API Documentation
    
    
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
                    'Channel': {
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
                'ChannelCounts': {
                    'string': 123
                },
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
    (dict) --
    SegmentResponse (dict) -- Segment definition.
    ApplicationId (string) -- The ID of the application to which the segment applies.
    CreationDate (string) -- The date the segment was created in ISO 8601 format.
    Dimensions (dict) -- The segment dimensions attributes.
    Attributes (dict) -- Custom segment attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    Behavior (dict) -- The segment behaviors attributes.
    Recency (dict) -- The recency of use.
    Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
    RecencyType (string) -- The recency dimension type: ACTIVE - Users who have used your app within the specified duration are included in the segment. INACTIVE - Users who have not used your app within the specified duration are included in the segment.
    
    
    
    
    Demographic (dict) -- The segment demographics attributes.
    AppVersion (dict) -- The app version criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Channel (dict) -- The channel criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    DeviceType (dict) -- The device type criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Make (dict) -- The device make criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Model (dict) -- The device model criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Platform (dict) -- The device platform criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    Location (dict) -- The segment location attributes.
    Country (dict) -- The country filter according to ISO 3166-1 Alpha-2 codes.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    UserAttributes (dict) -- Custom segment user attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    
    
    Id (string) -- The unique segment ID.
    ImportDefinition (dict) -- The import job settings.
    ChannelCounts (dict) -- Channel type counts
    (string) --
    (integer) --
    
    
    
    
    ExternalId (string) -- DEPRECATED. Your AWS account ID, which you assigned to the ExternalID key in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This requirement is removed, and external IDs are not recommended for IAM roles assumed by Amazon Pinpoint.
    Format (string) -- The format of the endpoint files that were imported to create this segment. Valid values: CSV, JSON
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the endpoints in Amazon S3.
    S3Url (string) -- A URL that points to the Amazon S3 location from which the endpoints for this segment were imported.
    Size (integer) -- The number of endpoints that were successfully imported to create this segment.
    
    
    LastModifiedDate (string) -- The date the segment was last updated in ISO 8601 format.
    Name (string) -- The name of segment
    SegmentType (string) -- The segment type: DIMENSIONAL - A dynamic segment built from selection criteria based on endpoint data reported by your app. You create this type of segment by using the segment builder in the Amazon Pinpoint console or by making a POST request to the segments resource. IMPORT - A static segment built from an imported set of endpoint definitions. You create this type of segment by importing a segment in the Amazon Pinpoint console or by making a POST request to the jobs/import resource.
    Version (integer) -- The segment version number.
    
    
    
    
    
    """
    pass

def delete_sms_channel(ApplicationId=None):
    """
    Delete an SMS channel
    See also: AWS API Documentation
    
    
    :example: response = client.delete_sms_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :rtype: dict
    :return: {
        'SMSChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'SenderId': 'string',
            'ShortCode': 'string',
            'Version': 123
        }
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

def get_adm_channel(ApplicationId=None):
    """
    Get an ADM channel
    See also: AWS API Documentation
    
    
    :example: response = client.get_adm_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :rtype: dict
    :return: {
        'ADMChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
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

def get_apns_channel(ApplicationId=None):
    """
    Returns information about the APNs channel for an app.
    See also: AWS API Documentation
    
    
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
            'DefaultAuthenticationMethod': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'HasTokenKey': True|False,
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

def get_apns_sandbox_channel(ApplicationId=None):
    """
    Get an APNS sandbox channel
    See also: AWS API Documentation
    
    
    :example: response = client.get_apns_sandbox_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :rtype: dict
    :return: {
        'APNSSandboxChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'DefaultAuthenticationMethod': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'HasTokenKey': True|False,
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

def get_apns_voip_channel(ApplicationId=None):
    """
    Get an APNS VoIP channel
    See also: AWS API Documentation
    
    
    :example: response = client.get_apns_voip_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :rtype: dict
    :return: {
        'APNSVoipChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'DefaultAuthenticationMethod': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'HasTokenKey': True|False,
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

def get_apns_voip_sandbox_channel(ApplicationId=None):
    """
    Get an APNS VoIPSandbox channel
    See also: AWS API Documentation
    
    
    :example: response = client.get_apns_voip_sandbox_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :rtype: dict
    :return: {
        'APNSVoipSandboxChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'DefaultAuthenticationMethod': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'HasTokenKey': True|False,
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

def get_app(ApplicationId=None):
    """
    Returns information about an app.
    See also: AWS API Documentation
    
    
    :example: response = client.get_app(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :rtype: dict
    :return: {
        'ApplicationResponse': {
            'Id': 'string',
            'Name': 'string'
        }
    }
    
    
    """
    pass

def get_application_settings(ApplicationId=None):
    """
    Used to request the settings for an app.
    See also: AWS API Documentation
    
    
    :example: response = client.get_application_settings(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :rtype: dict
    :return: {
        'ApplicationSettingsResource': {
            'ApplicationId': 'string',
            'CampaignHook': {
                'LambdaFunctionName': 'string',
                'Mode': 'DELIVERY'|'FILTER',
                'WebUrl': 'string'
            },
            'LastModifiedDate': 'string',
            'Limits': {
                'Daily': 123,
                'MaximumDuration': 123,
                'MessagesPerSecond': 123,
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

def get_apps(PageSize=None, Token=None):
    """
    Returns information about your apps.
    See also: AWS API Documentation
    
    
    :example: response = client.get_apps(
        PageSize='string',
        Token='string'
    )
    
    
    :type PageSize: string
    :param PageSize: 

    :type Token: string
    :param Token: 

    :rtype: dict
    :return: {
        'ApplicationsResponse': {
            'Item': [
                {
                    'Id': 'string',
                    'Name': 'string'
                },
            ],
            'NextToken': 'string'
        }
    }
    
    
    :returns: 
    (dict) --
    ApplicationsResponse (dict) -- Get Applications Result.
    Item (list) -- List of applications returned in this page.
    (dict) -- Application Response.
    Id (string) -- The unique application ID.
    Name (string) -- The display name of the application.
    
    
    
    
    NextToken (string) -- The string that you use in a subsequent request to get the next page of results in a paginated response.
    
    
    
    
    
    """
    pass

def get_baidu_channel(ApplicationId=None):
    """
    Get a BAIDU GCM channel
    See also: AWS API Documentation
    
    
    :example: response = client.get_baidu_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :rtype: dict
    :return: {
        'BaiduChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Credential': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
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

def get_campaign(ApplicationId=None, CampaignId=None):
    """
    Returns information about a campaign.
    See also: AWS API Documentation
    
    
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
                        'ADMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'APNSMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'BaiduMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'DefaultMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'EmailMessage': {
                            'Body': 'string',
                            'FromAddress': 'string',
                            'HtmlBody': 'string',
                            'Title': 'string'
                        },
                        'GCMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'SMSMessage': {
                            'Body': 'string',
                            'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                            'SenderId': 'string'
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
            'Hook': {
                'LambdaFunctionName': 'string',
                'Mode': 'DELIVERY'|'FILTER',
                'WebUrl': 'string'
            },
            'Id': 'string',
            'IsPaused': True|False,
            'LastModifiedDate': 'string',
            'Limits': {
                'Daily': 123,
                'MaximumDuration': 123,
                'MessagesPerSecond': 123,
                'Total': 123
            },
            'MessageConfiguration': {
                'ADMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'APNSMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'BaiduMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'DefaultMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'EmailMessage': {
                    'Body': 'string',
                    'FromAddress': 'string',
                    'HtmlBody': 'string',
                    'Title': 'string'
                },
                'GCMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'SMSMessage': {
                    'Body': 'string',
                    'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                    'SenderId': 'string'
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
    (dict) --
    CampaignResponse (dict) -- Campaign definition
    AdditionalTreatments (list) -- Treatments that are defined in addition to the default treatment.
    (dict) -- Treatment resource
    Id (string) -- The unique treatment ID.
    MessageConfiguration (dict) -- The message configuration settings.
    ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    EmailMessage (dict) -- The email message configuration.
    Body (string) -- The email text body.
    FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
    HtmlBody (string) -- The email html body.
    Title (string) -- The email title (Or subject).
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    SMSMessage (dict) -- The SMS message configuration.
    Body (string) -- The SMS text body.
    MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
    SenderId (string) -- Sender ID of sent message.
    
    
    
    
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
    Hook (dict) -- Campaign hook information.
    LambdaFunctionName (string) -- Lambda function name or arn to be called for delivery
    Mode (string) -- What mode Lambda should be invoked in.
    WebUrl (string) -- Web URL to call for hook. If the URL has authentication specified it will be added as authentication to the request
    
    
    Id (string) -- The unique campaign ID.
    IsPaused (boolean) -- Indicates whether the campaign is paused. A paused campaign does not send messages unless you resume it by setting IsPaused to false.
    LastModifiedDate (string) -- The date the campaign was last updated in ISO 8601 format.
    Limits (dict) -- The campaign limits settings.
    Daily (integer) -- The maximum number of messages that the campaign can send daily.
    MaximumDuration (integer) -- The length of time (in seconds) that the campaign can run before it ends and message deliveries stop. This duration begins at the scheduled start time for the campaign. The minimum value is 60.
    MessagesPerSecond (integer) -- The number of messages that the campaign can send per second. The minimum value is 50, and the maximum is 20000.
    Total (integer) -- The maximum total number of messages that the campaign can send.
    
    
    MessageConfiguration (dict) -- The message configuration settings.
    ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    EmailMessage (dict) -- The email message configuration.
    Body (string) -- The email text body.
    FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
    HtmlBody (string) -- The email html body.
    Title (string) -- The email title (Or subject).
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    SMSMessage (dict) -- The SMS message configuration.
    Body (string) -- The SMS text body.
    MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
    SenderId (string) -- Sender ID of sent message.
    
    
    
    
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
    See also: AWS API Documentation
    
    
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
    :param PageSize: The number of entries you want on each page in the response.

    :type Token: string
    :param Token: The NextToken string returned on a previous page that you use to get the next page of results in a paginated response.

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
    (dict) --
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
    See also: AWS API Documentation
    
    
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
                        'ADMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'APNSMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'BaiduMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'DefaultMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'EmailMessage': {
                            'Body': 'string',
                            'FromAddress': 'string',
                            'HtmlBody': 'string',
                            'Title': 'string'
                        },
                        'GCMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'SMSMessage': {
                            'Body': 'string',
                            'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                            'SenderId': 'string'
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
            'Hook': {
                'LambdaFunctionName': 'string',
                'Mode': 'DELIVERY'|'FILTER',
                'WebUrl': 'string'
            },
            'Id': 'string',
            'IsPaused': True|False,
            'LastModifiedDate': 'string',
            'Limits': {
                'Daily': 123,
                'MaximumDuration': 123,
                'MessagesPerSecond': 123,
                'Total': 123
            },
            'MessageConfiguration': {
                'ADMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'APNSMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'BaiduMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'DefaultMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'EmailMessage': {
                    'Body': 'string',
                    'FromAddress': 'string',
                    'HtmlBody': 'string',
                    'Title': 'string'
                },
                'GCMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'SMSMessage': {
                    'Body': 'string',
                    'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                    'SenderId': 'string'
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
    (dict) --
    CampaignResponse (dict) -- Campaign definition
    AdditionalTreatments (list) -- Treatments that are defined in addition to the default treatment.
    (dict) -- Treatment resource
    Id (string) -- The unique treatment ID.
    MessageConfiguration (dict) -- The message configuration settings.
    ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    EmailMessage (dict) -- The email message configuration.
    Body (string) -- The email text body.
    FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
    HtmlBody (string) -- The email html body.
    Title (string) -- The email title (Or subject).
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    SMSMessage (dict) -- The SMS message configuration.
    Body (string) -- The SMS text body.
    MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
    SenderId (string) -- Sender ID of sent message.
    
    
    
    
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
    Hook (dict) -- Campaign hook information.
    LambdaFunctionName (string) -- Lambda function name or arn to be called for delivery
    Mode (string) -- What mode Lambda should be invoked in.
    WebUrl (string) -- Web URL to call for hook. If the URL has authentication specified it will be added as authentication to the request
    
    
    Id (string) -- The unique campaign ID.
    IsPaused (boolean) -- Indicates whether the campaign is paused. A paused campaign does not send messages unless you resume it by setting IsPaused to false.
    LastModifiedDate (string) -- The date the campaign was last updated in ISO 8601 format.
    Limits (dict) -- The campaign limits settings.
    Daily (integer) -- The maximum number of messages that the campaign can send daily.
    MaximumDuration (integer) -- The length of time (in seconds) that the campaign can run before it ends and message deliveries stop. This duration begins at the scheduled start time for the campaign. The minimum value is 60.
    MessagesPerSecond (integer) -- The number of messages that the campaign can send per second. The minimum value is 50, and the maximum is 20000.
    Total (integer) -- The maximum total number of messages that the campaign can send.
    
    
    MessageConfiguration (dict) -- The message configuration settings.
    ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    EmailMessage (dict) -- The email message configuration.
    Body (string) -- The email text body.
    FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
    HtmlBody (string) -- The email html body.
    Title (string) -- The email title (Or subject).
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    SMSMessage (dict) -- The SMS message configuration.
    Body (string) -- The SMS text body.
    MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
    SenderId (string) -- Sender ID of sent message.
    
    
    
    
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
    See also: AWS API Documentation
    
    
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
    :param PageSize: The number of entries you want on each page in the response.

    :type Token: string
    :param Token: The NextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict
    :return: {
        'CampaignsResponse': {
            'Item': [
                {
                    'AdditionalTreatments': [
                        {
                            'Id': 'string',
                            'MessageConfiguration': {
                                'ADMMessage': {
                                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                                    'Body': 'string',
                                    'ImageIconUrl': 'string',
                                    'ImageSmallIconUrl': 'string',
                                    'ImageUrl': 'string',
                                    'JsonBody': 'string',
                                    'MediaUrl': 'string',
                                    'RawContent': 'string',
                                    'SilentPush': True|False,
                                    'Title': 'string',
                                    'Url': 'string'
                                },
                                'APNSMessage': {
                                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                                    'Body': 'string',
                                    'ImageIconUrl': 'string',
                                    'ImageSmallIconUrl': 'string',
                                    'ImageUrl': 'string',
                                    'JsonBody': 'string',
                                    'MediaUrl': 'string',
                                    'RawContent': 'string',
                                    'SilentPush': True|False,
                                    'Title': 'string',
                                    'Url': 'string'
                                },
                                'BaiduMessage': {
                                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                                    'Body': 'string',
                                    'ImageIconUrl': 'string',
                                    'ImageSmallIconUrl': 'string',
                                    'ImageUrl': 'string',
                                    'JsonBody': 'string',
                                    'MediaUrl': 'string',
                                    'RawContent': 'string',
                                    'SilentPush': True|False,
                                    'Title': 'string',
                                    'Url': 'string'
                                },
                                'DefaultMessage': {
                                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                                    'Body': 'string',
                                    'ImageIconUrl': 'string',
                                    'ImageSmallIconUrl': 'string',
                                    'ImageUrl': 'string',
                                    'JsonBody': 'string',
                                    'MediaUrl': 'string',
                                    'RawContent': 'string',
                                    'SilentPush': True|False,
                                    'Title': 'string',
                                    'Url': 'string'
                                },
                                'EmailMessage': {
                                    'Body': 'string',
                                    'FromAddress': 'string',
                                    'HtmlBody': 'string',
                                    'Title': 'string'
                                },
                                'GCMMessage': {
                                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                                    'Body': 'string',
                                    'ImageIconUrl': 'string',
                                    'ImageSmallIconUrl': 'string',
                                    'ImageUrl': 'string',
                                    'JsonBody': 'string',
                                    'MediaUrl': 'string',
                                    'RawContent': 'string',
                                    'SilentPush': True|False,
                                    'Title': 'string',
                                    'Url': 'string'
                                },
                                'SMSMessage': {
                                    'Body': 'string',
                                    'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                                    'SenderId': 'string'
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
                    'Hook': {
                        'LambdaFunctionName': 'string',
                        'Mode': 'DELIVERY'|'FILTER',
                        'WebUrl': 'string'
                    },
                    'Id': 'string',
                    'IsPaused': True|False,
                    'LastModifiedDate': 'string',
                    'Limits': {
                        'Daily': 123,
                        'MaximumDuration': 123,
                        'MessagesPerSecond': 123,
                        'Total': 123
                    },
                    'MessageConfiguration': {
                        'ADMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'APNSMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'BaiduMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'DefaultMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'EmailMessage': {
                            'Body': 'string',
                            'FromAddress': 'string',
                            'HtmlBody': 'string',
                            'Title': 'string'
                        },
                        'GCMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'SMSMessage': {
                            'Body': 'string',
                            'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                            'SenderId': 'string'
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
    (dict) --
    CampaignsResponse (dict) -- List of available campaigns.
    Item (list) -- A list of campaigns.
    (dict) -- Campaign definition
    AdditionalTreatments (list) -- Treatments that are defined in addition to the default treatment.
    (dict) -- Treatment resource
    Id (string) -- The unique treatment ID.
    MessageConfiguration (dict) -- The message configuration settings.
    ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    EmailMessage (dict) -- The email message configuration.
    Body (string) -- The email text body.
    FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
    HtmlBody (string) -- The email html body.
    Title (string) -- The email title (Or subject).
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    SMSMessage (dict) -- The SMS message configuration.
    Body (string) -- The SMS text body.
    MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
    SenderId (string) -- Sender ID of sent message.
    
    
    
    
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
    Hook (dict) -- Campaign hook information.
    LambdaFunctionName (string) -- Lambda function name or arn to be called for delivery
    Mode (string) -- What mode Lambda should be invoked in.
    WebUrl (string) -- Web URL to call for hook. If the URL has authentication specified it will be added as authentication to the request
    
    
    Id (string) -- The unique campaign ID.
    IsPaused (boolean) -- Indicates whether the campaign is paused. A paused campaign does not send messages unless you resume it by setting IsPaused to false.
    LastModifiedDate (string) -- The date the campaign was last updated in ISO 8601 format.
    Limits (dict) -- The campaign limits settings.
    Daily (integer) -- The maximum number of messages that the campaign can send daily.
    MaximumDuration (integer) -- The length of time (in seconds) that the campaign can run before it ends and message deliveries stop. This duration begins at the scheduled start time for the campaign. The minimum value is 60.
    MessagesPerSecond (integer) -- The number of messages that the campaign can send per second. The minimum value is 50, and the maximum is 20000.
    Total (integer) -- The maximum total number of messages that the campaign can send.
    
    
    MessageConfiguration (dict) -- The message configuration settings.
    ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    EmailMessage (dict) -- The email message configuration.
    Body (string) -- The email text body.
    FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
    HtmlBody (string) -- The email html body.
    Title (string) -- The email title (Or subject).
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    SMSMessage (dict) -- The SMS message configuration.
    Body (string) -- The SMS text body.
    MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
    SenderId (string) -- Sender ID of sent message.
    
    
    
    
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
    See also: AWS API Documentation
    
    
    :example: response = client.get_campaigns(
        ApplicationId='string',
        PageSize='string',
        Token='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type PageSize: string
    :param PageSize: The number of entries you want on each page in the response.

    :type Token: string
    :param Token: The NextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict
    :return: {
        'CampaignsResponse': {
            'Item': [
                {
                    'AdditionalTreatments': [
                        {
                            'Id': 'string',
                            'MessageConfiguration': {
                                'ADMMessage': {
                                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                                    'Body': 'string',
                                    'ImageIconUrl': 'string',
                                    'ImageSmallIconUrl': 'string',
                                    'ImageUrl': 'string',
                                    'JsonBody': 'string',
                                    'MediaUrl': 'string',
                                    'RawContent': 'string',
                                    'SilentPush': True|False,
                                    'Title': 'string',
                                    'Url': 'string'
                                },
                                'APNSMessage': {
                                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                                    'Body': 'string',
                                    'ImageIconUrl': 'string',
                                    'ImageSmallIconUrl': 'string',
                                    'ImageUrl': 'string',
                                    'JsonBody': 'string',
                                    'MediaUrl': 'string',
                                    'RawContent': 'string',
                                    'SilentPush': True|False,
                                    'Title': 'string',
                                    'Url': 'string'
                                },
                                'BaiduMessage': {
                                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                                    'Body': 'string',
                                    'ImageIconUrl': 'string',
                                    'ImageSmallIconUrl': 'string',
                                    'ImageUrl': 'string',
                                    'JsonBody': 'string',
                                    'MediaUrl': 'string',
                                    'RawContent': 'string',
                                    'SilentPush': True|False,
                                    'Title': 'string',
                                    'Url': 'string'
                                },
                                'DefaultMessage': {
                                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                                    'Body': 'string',
                                    'ImageIconUrl': 'string',
                                    'ImageSmallIconUrl': 'string',
                                    'ImageUrl': 'string',
                                    'JsonBody': 'string',
                                    'MediaUrl': 'string',
                                    'RawContent': 'string',
                                    'SilentPush': True|False,
                                    'Title': 'string',
                                    'Url': 'string'
                                },
                                'EmailMessage': {
                                    'Body': 'string',
                                    'FromAddress': 'string',
                                    'HtmlBody': 'string',
                                    'Title': 'string'
                                },
                                'GCMMessage': {
                                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                                    'Body': 'string',
                                    'ImageIconUrl': 'string',
                                    'ImageSmallIconUrl': 'string',
                                    'ImageUrl': 'string',
                                    'JsonBody': 'string',
                                    'MediaUrl': 'string',
                                    'RawContent': 'string',
                                    'SilentPush': True|False,
                                    'Title': 'string',
                                    'Url': 'string'
                                },
                                'SMSMessage': {
                                    'Body': 'string',
                                    'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                                    'SenderId': 'string'
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
                    'Hook': {
                        'LambdaFunctionName': 'string',
                        'Mode': 'DELIVERY'|'FILTER',
                        'WebUrl': 'string'
                    },
                    'Id': 'string',
                    'IsPaused': True|False,
                    'LastModifiedDate': 'string',
                    'Limits': {
                        'Daily': 123,
                        'MaximumDuration': 123,
                        'MessagesPerSecond': 123,
                        'Total': 123
                    },
                    'MessageConfiguration': {
                        'ADMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'APNSMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'BaiduMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'DefaultMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'EmailMessage': {
                            'Body': 'string',
                            'FromAddress': 'string',
                            'HtmlBody': 'string',
                            'Title': 'string'
                        },
                        'GCMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'SMSMessage': {
                            'Body': 'string',
                            'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                            'SenderId': 'string'
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
    (dict) --
    CampaignsResponse (dict) -- List of available campaigns.
    Item (list) -- A list of campaigns.
    (dict) -- Campaign definition
    AdditionalTreatments (list) -- Treatments that are defined in addition to the default treatment.
    (dict) -- Treatment resource
    Id (string) -- The unique treatment ID.
    MessageConfiguration (dict) -- The message configuration settings.
    ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    EmailMessage (dict) -- The email message configuration.
    Body (string) -- The email text body.
    FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
    HtmlBody (string) -- The email html body.
    Title (string) -- The email title (Or subject).
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    SMSMessage (dict) -- The SMS message configuration.
    Body (string) -- The SMS text body.
    MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
    SenderId (string) -- Sender ID of sent message.
    
    
    
    
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
    Hook (dict) -- Campaign hook information.
    LambdaFunctionName (string) -- Lambda function name or arn to be called for delivery
    Mode (string) -- What mode Lambda should be invoked in.
    WebUrl (string) -- Web URL to call for hook. If the URL has authentication specified it will be added as authentication to the request
    
    
    Id (string) -- The unique campaign ID.
    IsPaused (boolean) -- Indicates whether the campaign is paused. A paused campaign does not send messages unless you resume it by setting IsPaused to false.
    LastModifiedDate (string) -- The date the campaign was last updated in ISO 8601 format.
    Limits (dict) -- The campaign limits settings.
    Daily (integer) -- The maximum number of messages that the campaign can send daily.
    MaximumDuration (integer) -- The length of time (in seconds) that the campaign can run before it ends and message deliveries stop. This duration begins at the scheduled start time for the campaign. The minimum value is 60.
    MessagesPerSecond (integer) -- The number of messages that the campaign can send per second. The minimum value is 50, and the maximum is 20000.
    Total (integer) -- The maximum total number of messages that the campaign can send.
    
    
    MessageConfiguration (dict) -- The message configuration settings.
    ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    EmailMessage (dict) -- The email message configuration.
    Body (string) -- The email text body.
    FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
    HtmlBody (string) -- The email html body.
    Title (string) -- The email title (Or subject).
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    SMSMessage (dict) -- The SMS message configuration.
    Body (string) -- The SMS text body.
    MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
    SenderId (string) -- Sender ID of sent message.
    
    
    
    
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

def get_email_channel(ApplicationId=None):
    """
    Get an email channel
    See also: AWS API Documentation
    
    
    :example: response = client.get_email_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :rtype: dict
    :return: {
        'EmailChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Enabled': True|False,
            'FromAddress': 'string',
            'HasCredential': True|False,
            'Id': 'string',
            'Identity': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'RoleArn': 'string',
            'Version': 123
        }
    }
    
    
    """
    pass

def get_endpoint(ApplicationId=None, EndpointId=None):
    """
    Returns information about an endpoint.
    See also: AWS API Documentation
    
    
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
            'ChannelType': 'GCM'|'APNS'|'APNS_SANDBOX'|'APNS_VOIP'|'APNS_VOIP_SANDBOX'|'ADM'|'SMS'|'EMAIL'|'BAIDU'|'CUSTOM',
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
            }
        }
    }
    
    
    :returns: 
    (dict) --
    EndpointResponse (dict) -- Endpoint response
    Address (string) -- The address or token of the endpoint as provided by your push provider (e.g. DeviceToken or RegistrationId).
    ApplicationId (string) -- The ID of the application associated with the endpoint.
    Attributes (dict) -- Custom attributes that describe the endpoint by associating a name with an array of values. For example, an attribute named "interests" might have the values ["science", "politics", "travel"]. You can use these attributes as selection criteria when you create a segment of users to engage with a messaging campaign. The following characters are not recommended in attribute names: # : ? /. The Amazon Pinpoint console does not display attributes that include these characters in the name. This limitation does not apply to attribute values.
    (string) --
    (list) --
    (string) --
    
    
    
    
    
    
    ChannelType (string) -- The channel type. Valid values: GCM | APNS | APNS_SANDBOX | APNS_VOIP | APNS_VOIP_SANDBOX | ADM | SMS | EMAIL | BAIDU
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
    
    
    
    
    OptOut (string) -- Indicates whether a user has opted out of receiving messages with one of the following values: ALL - User has opted out of all messages. NONE - Users has not opted out and receives all messages.
    RequestId (string) -- The unique ID for the most recent request to update the endpoint.
    User (dict) -- Custom user-specific attributes that your app reports to Amazon Pinpoint.
    UserAttributes (dict) -- Custom attributes that describe an end user by associating a name with an array of values. For example, an attribute named "interests" might have the values ["science", "politics", "travel"]. You can use these attributes as selection criteria when you create a segment of users to engage with a messaging campaign. The following characters are not recommended in attribute names: # : ? /. The Amazon Pinpoint console does not display attributes that include these characters in the name. This limitation does not apply to attribute values.
    (string) --
    (list) --
    (string) --
    
    
    
    
    
    
    UserId (string) -- The unique ID of the user.
    
    
    
    
    
    
    
    """
    pass

def get_event_stream(ApplicationId=None):
    """
    Returns the event stream for an app.
    See also: AWS API Documentation
    
    
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

def get_export_job(ApplicationId=None, JobId=None):
    """
    Returns information about an export job.
    See also: AWS API Documentation
    
    
    :example: response = client.get_export_job(
        ApplicationId='string',
        JobId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type JobId: string
    :param JobId: [REQUIRED]

    :rtype: dict
    :return: {
        'ExportJobResponse': {
            'ApplicationId': 'string',
            'CompletedPieces': 123,
            'CompletionDate': 'string',
            'CreationDate': 'string',
            'Definition': {
                'RoleArn': 'string',
                'S3UrlPrefix': 'string',
                'SegmentId': 'string'
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
    (dict) --
    ExportJobResponse (dict) --
    ApplicationId (string) -- The unique ID of the application to which the job applies.
    CompletedPieces (integer) -- The number of pieces that have successfully completed as of the time of the request.
    CompletionDate (string) -- The date the job completed in ISO 8601 format.
    CreationDate (string) -- The date the job was created in ISO 8601 format.
    Definition (dict) -- The export job settings.
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the Amazon S3 location that endpoints will be exported to.
    S3UrlPrefix (string) -- A URL that points to the location within an Amazon S3 bucket that will receive the export. The location is typically a folder with multiple files. The URL should follow this format: s3://bucket-name/folder-name/ Amazon Pinpoint will export endpoints to this location.
    SegmentId (string) -- The ID of the segment to export endpoints from. If not present, all endpoints are exported.
    
    
    FailedPieces (integer) -- The number of pieces that failed to be processed as of the time of the request.
    Failures (list) -- Provides up to 100 of the first failed entries for the job, if any exist.
    (string) --
    
    
    Id (string) -- The unique ID of the job.
    JobStatus (string) -- The status of the job. Valid values: CREATED, INITIALIZING, PROCESSING, COMPLETING, COMPLETED, FAILING, FAILED The job status is FAILED if one or more pieces failed.
    TotalFailures (integer) -- The number of endpoints that were not processed; for example, because of syntax errors.
    TotalPieces (integer) -- The total number of pieces that must be processed to finish the job. Each piece is an approximately equal portion of the endpoints.
    TotalProcessed (integer) -- The number of endpoints that were processed by the job.
    Type (string) -- The job type. Will be 'EXPORT'.
    
    
    
    
    
    """
    pass

def get_export_jobs(ApplicationId=None, PageSize=None, Token=None):
    """
    Returns information about your export jobs.
    See also: AWS API Documentation
    
    
    :example: response = client.get_export_jobs(
        ApplicationId='string',
        PageSize='string',
        Token='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type PageSize: string
    :param PageSize: The number of entries you want on each page in the response.

    :type Token: string
    :param Token: The NextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict
    :return: {
        'ExportJobsResponse': {
            'Item': [
                {
                    'ApplicationId': 'string',
                    'CompletedPieces': 123,
                    'CompletionDate': 'string',
                    'CreationDate': 'string',
                    'Definition': {
                        'RoleArn': 'string',
                        'S3UrlPrefix': 'string',
                        'SegmentId': 'string'
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
    (dict) --
    ExportJobsResponse (dict) -- Export job list.
    Item (list) -- A list of export jobs for the application.
    (dict) --
    ApplicationId (string) -- The unique ID of the application to which the job applies.
    CompletedPieces (integer) -- The number of pieces that have successfully completed as of the time of the request.
    CompletionDate (string) -- The date the job completed in ISO 8601 format.
    CreationDate (string) -- The date the job was created in ISO 8601 format.
    Definition (dict) -- The export job settings.
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the Amazon S3 location that endpoints will be exported to.
    S3UrlPrefix (string) -- A URL that points to the location within an Amazon S3 bucket that will receive the export. The location is typically a folder with multiple files. The URL should follow this format: s3://bucket-name/folder-name/ Amazon Pinpoint will export endpoints to this location.
    SegmentId (string) -- The ID of the segment to export endpoints from. If not present, all endpoints are exported.
    
    
    FailedPieces (integer) -- The number of pieces that failed to be processed as of the time of the request.
    Failures (list) -- Provides up to 100 of the first failed entries for the job, if any exist.
    (string) --
    
    
    Id (string) -- The unique ID of the job.
    JobStatus (string) -- The status of the job. Valid values: CREATED, INITIALIZING, PROCESSING, COMPLETING, COMPLETED, FAILING, FAILED The job status is FAILED if one or more pieces failed.
    TotalFailures (integer) -- The number of endpoints that were not processed; for example, because of syntax errors.
    TotalPieces (integer) -- The total number of pieces that must be processed to finish the job. Each piece is an approximately equal portion of the endpoints.
    TotalProcessed (integer) -- The number of endpoints that were processed by the job.
    Type (string) -- The job type. Will be 'EXPORT'.
    
    
    
    
    NextToken (string) -- The string that you use in a subsequent request to get the next page of results in a paginated response.
    
    
    
    
    
    """
    pass

def get_gcm_channel(ApplicationId=None):
    """
    Returns information about the GCM channel for an app.
    See also: AWS API Documentation
    
    
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
            'Enabled': True|False,
            'HasCredential': True|False,
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
    See also: AWS API Documentation
    
    
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
    (dict) --
    ImportJobResponse (dict) --
    ApplicationId (string) -- The unique ID of the application to which the import job applies.
    CompletedPieces (integer) -- The number of pieces that have successfully imported as of the time of the request.
    CompletionDate (string) -- The date the import job completed in ISO 8601 format.
    CreationDate (string) -- The date the import job was created in ISO 8601 format.
    Definition (dict) -- The import job settings.
    DefineSegment (boolean) -- Sets whether the endpoints create a segment when they are imported.
    ExternalId (string) -- DEPRECATED. Your AWS account ID, which you assigned to the ExternalID key in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This requirement is removed, and external IDs are not recommended for IAM roles assumed by Amazon Pinpoint.
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
    See also: AWS API Documentation
    
    
    :example: response = client.get_import_jobs(
        ApplicationId='string',
        PageSize='string',
        Token='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type PageSize: string
    :param PageSize: The number of entries you want on each page in the response.

    :type Token: string
    :param Token: The NextToken string returned on a previous page that you use to get the next page of results in a paginated response.

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
    (dict) --
    ImportJobsResponse (dict) -- Import job list.
    Item (list) -- A list of import jobs for the application.
    (dict) --
    ApplicationId (string) -- The unique ID of the application to which the import job applies.
    CompletedPieces (integer) -- The number of pieces that have successfully imported as of the time of the request.
    CompletionDate (string) -- The date the import job completed in ISO 8601 format.
    CreationDate (string) -- The date the import job was created in ISO 8601 format.
    Definition (dict) -- The import job settings.
    DefineSegment (boolean) -- Sets whether the endpoints create a segment when they are imported.
    ExternalId (string) -- DEPRECATED. Your AWS account ID, which you assigned to the ExternalID key in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This requirement is removed, and external IDs are not recommended for IAM roles assumed by Amazon Pinpoint.
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
    See also: AWS API Documentation
    
    
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
                    'Channel': {
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
                'ChannelCounts': {
                    'string': 123
                },
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
    (dict) --
    SegmentResponse (dict) -- Segment definition.
    ApplicationId (string) -- The ID of the application to which the segment applies.
    CreationDate (string) -- The date the segment was created in ISO 8601 format.
    Dimensions (dict) -- The segment dimensions attributes.
    Attributes (dict) -- Custom segment attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    Behavior (dict) -- The segment behaviors attributes.
    Recency (dict) -- The recency of use.
    Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
    RecencyType (string) -- The recency dimension type: ACTIVE - Users who have used your app within the specified duration are included in the segment. INACTIVE - Users who have not used your app within the specified duration are included in the segment.
    
    
    
    
    Demographic (dict) -- The segment demographics attributes.
    AppVersion (dict) -- The app version criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Channel (dict) -- The channel criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    DeviceType (dict) -- The device type criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Make (dict) -- The device make criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Model (dict) -- The device model criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Platform (dict) -- The device platform criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    Location (dict) -- The segment location attributes.
    Country (dict) -- The country filter according to ISO 3166-1 Alpha-2 codes.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    UserAttributes (dict) -- Custom segment user attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    
    
    Id (string) -- The unique segment ID.
    ImportDefinition (dict) -- The import job settings.
    ChannelCounts (dict) -- Channel type counts
    (string) --
    (integer) --
    
    
    
    
    ExternalId (string) -- DEPRECATED. Your AWS account ID, which you assigned to the ExternalID key in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This requirement is removed, and external IDs are not recommended for IAM roles assumed by Amazon Pinpoint.
    Format (string) -- The format of the endpoint files that were imported to create this segment. Valid values: CSV, JSON
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the endpoints in Amazon S3.
    S3Url (string) -- A URL that points to the Amazon S3 location from which the endpoints for this segment were imported.
    Size (integer) -- The number of endpoints that were successfully imported to create this segment.
    
    
    LastModifiedDate (string) -- The date the segment was last updated in ISO 8601 format.
    Name (string) -- The name of segment
    SegmentType (string) -- The segment type: DIMENSIONAL - A dynamic segment built from selection criteria based on endpoint data reported by your app. You create this type of segment by using the segment builder in the Amazon Pinpoint console or by making a POST request to the segments resource. IMPORT - A static segment built from an imported set of endpoint definitions. You create this type of segment by importing a segment in the Amazon Pinpoint console or by making a POST request to the jobs/import resource.
    Version (integer) -- The segment version number.
    
    
    
    
    
    """
    pass

def get_segment_export_jobs(ApplicationId=None, PageSize=None, SegmentId=None, Token=None):
    """
    Returns a list of export jobs for a specific segment.
    See also: AWS API Documentation
    
    
    :example: response = client.get_segment_export_jobs(
        ApplicationId='string',
        PageSize='string',
        SegmentId='string',
        Token='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type PageSize: string
    :param PageSize: The number of entries you want on each page in the response.

    :type SegmentId: string
    :param SegmentId: [REQUIRED]

    :type Token: string
    :param Token: The NextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict
    :return: {
        'ExportJobsResponse': {
            'Item': [
                {
                    'ApplicationId': 'string',
                    'CompletedPieces': 123,
                    'CompletionDate': 'string',
                    'CreationDate': 'string',
                    'Definition': {
                        'RoleArn': 'string',
                        'S3UrlPrefix': 'string',
                        'SegmentId': 'string'
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
    (dict) --
    ExportJobsResponse (dict) -- Export job list.
    Item (list) -- A list of export jobs for the application.
    (dict) --
    ApplicationId (string) -- The unique ID of the application to which the job applies.
    CompletedPieces (integer) -- The number of pieces that have successfully completed as of the time of the request.
    CompletionDate (string) -- The date the job completed in ISO 8601 format.
    CreationDate (string) -- The date the job was created in ISO 8601 format.
    Definition (dict) -- The export job settings.
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the Amazon S3 location that endpoints will be exported to.
    S3UrlPrefix (string) -- A URL that points to the location within an Amazon S3 bucket that will receive the export. The location is typically a folder with multiple files. The URL should follow this format: s3://bucket-name/folder-name/ Amazon Pinpoint will export endpoints to this location.
    SegmentId (string) -- The ID of the segment to export endpoints from. If not present, all endpoints are exported.
    
    
    FailedPieces (integer) -- The number of pieces that failed to be processed as of the time of the request.
    Failures (list) -- Provides up to 100 of the first failed entries for the job, if any exist.
    (string) --
    
    
    Id (string) -- The unique ID of the job.
    JobStatus (string) -- The status of the job. Valid values: CREATED, INITIALIZING, PROCESSING, COMPLETING, COMPLETED, FAILING, FAILED The job status is FAILED if one or more pieces failed.
    TotalFailures (integer) -- The number of endpoints that were not processed; for example, because of syntax errors.
    TotalPieces (integer) -- The total number of pieces that must be processed to finish the job. Each piece is an approximately equal portion of the endpoints.
    TotalProcessed (integer) -- The number of endpoints that were processed by the job.
    Type (string) -- The job type. Will be 'EXPORT'.
    
    
    
    
    NextToken (string) -- The string that you use in a subsequent request to get the next page of results in a paginated response.
    
    
    
    
    
    """
    pass

def get_segment_import_jobs(ApplicationId=None, PageSize=None, SegmentId=None, Token=None):
    """
    Returns a list of import jobs for a specific segment.
    See also: AWS API Documentation
    
    
    :example: response = client.get_segment_import_jobs(
        ApplicationId='string',
        PageSize='string',
        SegmentId='string',
        Token='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type PageSize: string
    :param PageSize: The number of entries you want on each page in the response.

    :type SegmentId: string
    :param SegmentId: [REQUIRED]

    :type Token: string
    :param Token: The NextToken string returned on a previous page that you use to get the next page of results in a paginated response.

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
    (dict) --
    ImportJobsResponse (dict) -- Import job list.
    Item (list) -- A list of import jobs for the application.
    (dict) --
    ApplicationId (string) -- The unique ID of the application to which the import job applies.
    CompletedPieces (integer) -- The number of pieces that have successfully imported as of the time of the request.
    CompletionDate (string) -- The date the import job completed in ISO 8601 format.
    CreationDate (string) -- The date the import job was created in ISO 8601 format.
    Definition (dict) -- The import job settings.
    DefineSegment (boolean) -- Sets whether the endpoints create a segment when they are imported.
    ExternalId (string) -- DEPRECATED. Your AWS account ID, which you assigned to the ExternalID key in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This requirement is removed, and external IDs are not recommended for IAM roles assumed by Amazon Pinpoint.
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
    See also: AWS API Documentation
    
    
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
                    'Channel': {
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
                'ChannelCounts': {
                    'string': 123
                },
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
    (dict) --
    SegmentResponse (dict) -- Segment definition.
    ApplicationId (string) -- The ID of the application to which the segment applies.
    CreationDate (string) -- The date the segment was created in ISO 8601 format.
    Dimensions (dict) -- The segment dimensions attributes.
    Attributes (dict) -- Custom segment attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    Behavior (dict) -- The segment behaviors attributes.
    Recency (dict) -- The recency of use.
    Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
    RecencyType (string) -- The recency dimension type: ACTIVE - Users who have used your app within the specified duration are included in the segment. INACTIVE - Users who have not used your app within the specified duration are included in the segment.
    
    
    
    
    Demographic (dict) -- The segment demographics attributes.
    AppVersion (dict) -- The app version criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Channel (dict) -- The channel criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    DeviceType (dict) -- The device type criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Make (dict) -- The device make criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Model (dict) -- The device model criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Platform (dict) -- The device platform criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    Location (dict) -- The segment location attributes.
    Country (dict) -- The country filter according to ISO 3166-1 Alpha-2 codes.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    UserAttributes (dict) -- Custom segment user attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    
    
    Id (string) -- The unique segment ID.
    ImportDefinition (dict) -- The import job settings.
    ChannelCounts (dict) -- Channel type counts
    (string) --
    (integer) --
    
    
    
    
    ExternalId (string) -- DEPRECATED. Your AWS account ID, which you assigned to the ExternalID key in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This requirement is removed, and external IDs are not recommended for IAM roles assumed by Amazon Pinpoint.
    Format (string) -- The format of the endpoint files that were imported to create this segment. Valid values: CSV, JSON
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the endpoints in Amazon S3.
    S3Url (string) -- A URL that points to the Amazon S3 location from which the endpoints for this segment were imported.
    Size (integer) -- The number of endpoints that were successfully imported to create this segment.
    
    
    LastModifiedDate (string) -- The date the segment was last updated in ISO 8601 format.
    Name (string) -- The name of segment
    SegmentType (string) -- The segment type: DIMENSIONAL - A dynamic segment built from selection criteria based on endpoint data reported by your app. You create this type of segment by using the segment builder in the Amazon Pinpoint console or by making a POST request to the segments resource. IMPORT - A static segment built from an imported set of endpoint definitions. You create this type of segment by importing a segment in the Amazon Pinpoint console or by making a POST request to the jobs/import resource.
    Version (integer) -- The segment version number.
    
    
    
    
    
    """
    pass

def get_segment_versions(ApplicationId=None, PageSize=None, SegmentId=None, Token=None):
    """
    Returns information about your segment versions.
    See also: AWS API Documentation
    
    
    :example: response = client.get_segment_versions(
        ApplicationId='string',
        PageSize='string',
        SegmentId='string',
        Token='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type PageSize: string
    :param PageSize: The number of entries you want on each page in the response.

    :type SegmentId: string
    :param SegmentId: [REQUIRED]

    :type Token: string
    :param Token: The NextToken string returned on a previous page that you use to get the next page of results in a paginated response.

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
                            'Channel': {
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
                        'ChannelCounts': {
                            'string': 123
                        },
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
    (dict) --
    SegmentsResponse (dict) -- Segments in your account.
    Item (list) -- The list of segments.
    (dict) -- Segment definition.
    ApplicationId (string) -- The ID of the application to which the segment applies.
    CreationDate (string) -- The date the segment was created in ISO 8601 format.
    Dimensions (dict) -- The segment dimensions attributes.
    Attributes (dict) -- Custom segment attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    Behavior (dict) -- The segment behaviors attributes.
    Recency (dict) -- The recency of use.
    Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
    RecencyType (string) -- The recency dimension type: ACTIVE - Users who have used your app within the specified duration are included in the segment. INACTIVE - Users who have not used your app within the specified duration are included in the segment.
    
    
    
    
    Demographic (dict) -- The segment demographics attributes.
    AppVersion (dict) -- The app version criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Channel (dict) -- The channel criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    DeviceType (dict) -- The device type criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Make (dict) -- The device make criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Model (dict) -- The device model criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Platform (dict) -- The device platform criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    Location (dict) -- The segment location attributes.
    Country (dict) -- The country filter according to ISO 3166-1 Alpha-2 codes.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    UserAttributes (dict) -- Custom segment user attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    
    
    Id (string) -- The unique segment ID.
    ImportDefinition (dict) -- The import job settings.
    ChannelCounts (dict) -- Channel type counts
    (string) --
    (integer) --
    
    
    
    
    ExternalId (string) -- DEPRECATED. Your AWS account ID, which you assigned to the ExternalID key in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This requirement is removed, and external IDs are not recommended for IAM roles assumed by Amazon Pinpoint.
    Format (string) -- The format of the endpoint files that were imported to create this segment. Valid values: CSV, JSON
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the endpoints in Amazon S3.
    S3Url (string) -- A URL that points to the Amazon S3 location from which the endpoints for this segment were imported.
    Size (integer) -- The number of endpoints that were successfully imported to create this segment.
    
    
    LastModifiedDate (string) -- The date the segment was last updated in ISO 8601 format.
    Name (string) -- The name of segment
    SegmentType (string) -- The segment type: DIMENSIONAL - A dynamic segment built from selection criteria based on endpoint data reported by your app. You create this type of segment by using the segment builder in the Amazon Pinpoint console or by making a POST request to the segments resource. IMPORT - A static segment built from an imported set of endpoint definitions. You create this type of segment by importing a segment in the Amazon Pinpoint console or by making a POST request to the jobs/import resource.
    Version (integer) -- The segment version number.
    
    
    
    
    NextToken (string) -- An identifier used to retrieve the next page of results. The token is null if no additional pages exist.
    
    
    
    
    
    """
    pass

def get_segments(ApplicationId=None, PageSize=None, Token=None):
    """
    Used to get information about your segments.
    See also: AWS API Documentation
    
    
    :example: response = client.get_segments(
        ApplicationId='string',
        PageSize='string',
        Token='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type PageSize: string
    :param PageSize: The number of entries you want on each page in the response.

    :type Token: string
    :param Token: The NextToken string returned on a previous page that you use to get the next page of results in a paginated response.

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
                            'Channel': {
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
                        'ChannelCounts': {
                            'string': 123
                        },
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
    (dict) --
    SegmentsResponse (dict) -- Segments in your account.
    Item (list) -- The list of segments.
    (dict) -- Segment definition.
    ApplicationId (string) -- The ID of the application to which the segment applies.
    CreationDate (string) -- The date the segment was created in ISO 8601 format.
    Dimensions (dict) -- The segment dimensions attributes.
    Attributes (dict) -- Custom segment attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    Behavior (dict) -- The segment behaviors attributes.
    Recency (dict) -- The recency of use.
    Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
    RecencyType (string) -- The recency dimension type: ACTIVE - Users who have used your app within the specified duration are included in the segment. INACTIVE - Users who have not used your app within the specified duration are included in the segment.
    
    
    
    
    Demographic (dict) -- The segment demographics attributes.
    AppVersion (dict) -- The app version criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Channel (dict) -- The channel criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    DeviceType (dict) -- The device type criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Make (dict) -- The device make criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Model (dict) -- The device model criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Platform (dict) -- The device platform criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    Location (dict) -- The segment location attributes.
    Country (dict) -- The country filter according to ISO 3166-1 Alpha-2 codes.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    UserAttributes (dict) -- Custom segment user attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    
    
    Id (string) -- The unique segment ID.
    ImportDefinition (dict) -- The import job settings.
    ChannelCounts (dict) -- Channel type counts
    (string) --
    (integer) --
    
    
    
    
    ExternalId (string) -- DEPRECATED. Your AWS account ID, which you assigned to the ExternalID key in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This requirement is removed, and external IDs are not recommended for IAM roles assumed by Amazon Pinpoint.
    Format (string) -- The format of the endpoint files that were imported to create this segment. Valid values: CSV, JSON
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the endpoints in Amazon S3.
    S3Url (string) -- A URL that points to the Amazon S3 location from which the endpoints for this segment were imported.
    Size (integer) -- The number of endpoints that were successfully imported to create this segment.
    
    
    LastModifiedDate (string) -- The date the segment was last updated in ISO 8601 format.
    Name (string) -- The name of segment
    SegmentType (string) -- The segment type: DIMENSIONAL - A dynamic segment built from selection criteria based on endpoint data reported by your app. You create this type of segment by using the segment builder in the Amazon Pinpoint console or by making a POST request to the segments resource. IMPORT - A static segment built from an imported set of endpoint definitions. You create this type of segment by importing a segment in the Amazon Pinpoint console or by making a POST request to the jobs/import resource.
    Version (integer) -- The segment version number.
    
    
    
    
    NextToken (string) -- An identifier used to retrieve the next page of results. The token is null if no additional pages exist.
    
    
    
    
    
    """
    pass

def get_sms_channel(ApplicationId=None):
    """
    Get an SMS channel
    See also: AWS API Documentation
    
    
    :example: response = client.get_sms_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :rtype: dict
    :return: {
        'SMSChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'SenderId': 'string',
            'ShortCode': 'string',
            'Version': 123
        }
    }
    
    
    """
    pass

def get_waiter(waiter_name=None):
    """
    
    :type waiter_name: 
    :param waiter_name: 

    """
    pass

def put_event_stream(ApplicationId=None, WriteEventStream=None):
    """
    Use to create or update the event stream for an app.
    See also: AWS API Documentation
    
    
    :example: response = client.put_event_stream(
        ApplicationId='string',
        WriteEventStream={
            'DestinationStreamArn': 'string',
            'RoleArn': 'string'
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] ApplicationId

    :type WriteEventStream: dict
    :param WriteEventStream: [REQUIRED] EventStream to write.
            DestinationStreamArn (string) -- The Amazon Resource Name (ARN) of the Amazon Kinesis stream or Firehose delivery stream to which you want to publish events. Firehose ARN: arn:aws:firehose:REGION:ACCOUNT_ID:deliverystream/STREAM_NAME Kinesis ARN: arn:aws:kinesis:REGION:ACCOUNT_ID:stream/STREAM_NAME
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
    (dict) --
    EventStream (dict) -- Model for an event publishing subscription export.
    ApplicationId (string) -- The ID of the application from which events should be published.
    DestinationStreamArn (string) -- The Amazon Resource Name (ARN) of the Amazon Kinesis stream or Firehose delivery stream to which you want to publish events. Firehose ARN: arn:aws:firehose:REGION:ACCOUNT_ID:deliverystream/STREAM_NAME Kinesis ARN: arn:aws:kinesis:REGION:ACCOUNT_ID:stream/STREAM_NAME
    ExternalId (string) -- DEPRECATED. Your AWS account ID, which you assigned to the ExternalID key in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This requirement is removed, and external IDs are not recommended for IAM roles assumed by Amazon Pinpoint.
    LastModifiedDate (string) -- The date the event stream was last updated in ISO 8601 format.
    LastUpdatedBy (string) -- The IAM user who last modified the event stream.
    RoleArn (string) -- The IAM role that authorizes Amazon Pinpoint to publish events to the stream in your account.
    
    
    
    
    
    """
    pass

def send_messages(ApplicationId=None, MessageRequest=None):
    """
    Send a batch of messages
    See also: AWS API Documentation
    
    
    :example: response = client.send_messages(
        ApplicationId='string',
        MessageRequest={
            'Addresses': {
                'string': {
                    'BodyOverride': 'string',
                    'ChannelType': 'GCM'|'APNS'|'APNS_SANDBOX'|'APNS_VOIP'|'APNS_VOIP_SANDBOX'|'ADM'|'SMS'|'EMAIL'|'BAIDU'|'CUSTOM',
                    'Context': {
                        'string': 'string'
                    },
                    'RawContent': 'string',
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    },
                    'TitleOverride': 'string'
                }
            },
            'Context': {
                'string': 'string'
            },
            'Endpoints': {
                'string': {
                    'BodyOverride': 'string',
                    'Context': {
                        'string': 'string'
                    },
                    'RawContent': 'string',
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    },
                    'TitleOverride': 'string'
                }
            },
            'MessageConfiguration': {
                'ADMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ConsolidationKey': 'string',
                    'Data': {
                        'string': 'string'
                    },
                    'ExpiresAfter': 'string',
                    'IconReference': 'string',
                    'ImageIconUrl': 'string',
                    'ImageUrl': 'string',
                    'MD5': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'SmallImageIconUrl': 'string',
                    'Sound': 'string',
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    },
                    'Title': 'string',
                    'Url': 'string'
                },
                'APNSMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Badge': 123,
                    'Body': 'string',
                    'Category': 'string',
                    'CollapseId': 'string',
                    'Data': {
                        'string': 'string'
                    },
                    'MediaUrl': 'string',
                    'PreferredAuthenticationMethod': 'string',
                    'Priority': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Sound': 'string',
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    },
                    'ThreadId': 'string',
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'BaiduMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'Data': {
                        'string': 'string'
                    },
                    'IconReference': 'string',
                    'ImageIconUrl': 'string',
                    'ImageUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'SmallImageIconUrl': 'string',
                    'Sound': 'string',
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    },
                    'Title': 'string',
                    'Url': 'string'
                },
                'DefaultMessage': {
                    'Body': 'string',
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    }
                },
                'DefaultPushNotificationMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'Data': {
                        'string': 'string'
                    },
                    'SilentPush': True|False,
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    },
                    'Title': 'string',
                    'Url': 'string'
                },
                'GCMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'CollapseKey': 'string',
                    'Data': {
                        'string': 'string'
                    },
                    'IconReference': 'string',
                    'ImageIconUrl': 'string',
                    'ImageUrl': 'string',
                    'Priority': 'string',
                    'RawContent': 'string',
                    'RestrictedPackageName': 'string',
                    'SilentPush': True|False,
                    'SmallImageIconUrl': 'string',
                    'Sound': 'string',
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    },
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'SMSMessage': {
                    'Body': 'string',
                    'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                    'OriginationNumber': 'string',
                    'SenderId': 'string',
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    }
                }
            }
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type MessageRequest: dict
    :param MessageRequest: [REQUIRED] Send message request.
            Addresses (dict) -- A map of destination addresses, with the address as the key(Email address, phone number or push token) and the Address Configuration as the value.
            (string) --
            (dict) -- Address configuration.
            BodyOverride (string) -- Body override. If specified will override default body.
            ChannelType (string) -- The channel type. Valid values: GCM | APNS | APNS_SANDBOX | APNS_VOIP | APNS_VOIP_SANDBOX | ADM | SMS | EMAIL | BAIDU
            Context (dict) -- A map of custom attributes to attributes to be attached to the message for this address. This payload is added to the push notification's 'data.pinpoint' object or added to the email/sms delivery receipt event attributes.
            (string) --
            (string) --
            
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            Substitutions (dict) -- A map of substitution values for the message to be merged with the DefaultMessage's substitutions. Substitutions on this map take precedence over the all other substitutions.
            (string) --
            (list) --
            (string) --
            
            TitleOverride (string) -- Title override. If specified will override default title if applicable.
            
            Context (dict) -- A map of custom attributes to attributes to be attached to the message. This payload is added to the push notification's 'data.pinpoint' object or added to the email/sms delivery receipt event attributes.
            (string) --
            (string) --
            
            Endpoints (dict) -- A map of destination addresses, with the address as the key(Email address, phone number or push token) and the Address Configuration as the value.
            (string) --
            (dict) -- Endpoint send configuration.
            BodyOverride (string) -- Body override. If specified will override default body.
            Context (dict) -- A map of custom attributes to attributes to be attached to the message for this address. This payload is added to the push notification's 'data.pinpoint' object or added to the email/sms delivery receipt event attributes.
            (string) --
            (string) --
            
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            Substitutions (dict) -- A map of substitution values for the message to be merged with the DefaultMessage's substitutions. Substitutions on this map take precedence over the all other substitutions.
            (string) --
            (list) --
            (string) --
            
            TitleOverride (string) -- Title override. If specified will override default title if applicable.
            
            MessageConfiguration (dict) -- Message configuration.
            ADMMessage (dict) -- The message to ADM channels. Overrides the default push notification message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify. Possible values include: OPEN_APP | DEEP_LINK | URL
            Body (string) -- The message body of the notification, the email body or the text message.
            ConsolidationKey (string) -- Optional. Arbitrary string used to indicate multiple messages are logically the same and that ADM is allowed to drop previously enqueued messages in favor of this one.
            Data (dict) -- The data payload used for a silent push. This payload is added to the notifications' data.pinpoint.jsonBody' object
            (string) --
            (string) --
            
            ExpiresAfter (string) -- Optional. Number of seconds ADM should retain the message if the device is offline
            IconReference (string) -- The icon image name of the asset saved in your application.
            ImageIconUrl (string) -- The URL that points to an image used as the large icon to the notification content view.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            MD5 (string) -- Optional. Base-64-encoded MD5 checksum of the data parameter. Used to verify data integrity
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            SmallImageIconUrl (string) -- The URL that points to an image used as the small icon for the notification which will be used to represent the notification in the status bar and content view
            Sound (string) -- Indicates a sound to play when the device receives the notification. Supports default, or the filename of a sound resource bundled in the app. Android sound files must reside in /res/raw/
            Substitutions (dict) -- Default message substitutions. Can be overridden by individual address substitutions.
            (string) --
            (list) --
            (string) --
            
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            APNSMessage (dict) -- The message to APNS channels. Overrides the default push notification message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify. Possible values include: OPEN_APP | DEEP_LINK | URL
            Badge (integer) -- Include this key when you want the system to modify the badge of your app icon. If this key is not included in the dictionary, the badge is not changed. To remove the badge, set the value of this key to 0.
            Body (string) -- The message body of the notification, the email body or the text message.
            Category (string) -- Provide this key with a string value that represents the notification's type. This value corresponds to the value in the identifier property of one of your app's registered categories.
            CollapseId (string) -- An ID that, if assigned to multiple messages, causes APNs to coalesce the messages into a single push notification instead of delivering each message individually. The value must not exceed 64 bytes. Amazon Pinpoint uses this value to set the apns-collapse-id request header when it sends the message to APNs.
            Data (dict) -- The data payload used for a silent push. This payload is added to the notifications' data.pinpoint.jsonBody' object
            (string) --
            (string) --
            
            MediaUrl (string) -- The URL that points to a video used in the push notification.
            PreferredAuthenticationMethod (string) -- The preferred authentication method, either 'CERTIFICATE' or 'TOKEN'
            Priority (string) -- The message priority. Amazon Pinpoint uses this value to set the apns-priority request header when it sends the message to APNs. Accepts the following values: '5' - Low priority. Messages might be delayed, delivered in groups, and throttled. '10' - High priority. Messages are sent immediately. High priority messages must cause an alert, sound, or badge on the receiving device. The default value is '10'. The equivalent values for FCM or GCM messages are 'normal' and 'high'. Amazon Pinpoint accepts these values for APNs messages and converts them. For more information about the apns-priority parameter, see Communicating with APNs in the APNs Local and Remote Notification Programming Guide.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Sound (string) -- Include this key when you want the system to play a sound. The value of this key is the name of a sound file in your app's main bundle or in the Library/Sounds folder of your app's data container. If the sound file cannot be found, or if you specify defaultfor the value, the system plays the default alert sound.
            Substitutions (dict) -- Default message substitutions. Can be overridden by individual address substitutions.
            (string) --
            (list) --
            (string) --
            
            ThreadId (string) -- Provide this key with a string value that represents the app-specific identifier for grouping notifications. If you provide a Notification Content app extension, you can use this value to group your notifications together.
            TimeToLive (integer) -- The length of time (in seconds) that APNs stores and attempts to deliver the message. If the value is 0, APNs does not store the message or attempt to deliver it more than once. Amazon Pinpoint uses this value to set the apns-expiration request header when it sends the message to APNs.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            BaiduMessage (dict) -- The message to Baidu GCM channels. Overrides the default push notification message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify. Possible values include: OPEN_APP | DEEP_LINK | URL
            Body (string) -- The message body of the notification, the email body or the text message.
            Data (dict) -- The data payload used for a silent push. This payload is added to the notifications' data.pinpoint.jsonBody' object
            (string) --
            (string) --
            
            IconReference (string) -- The icon image name of the asset saved in your application.
            ImageIconUrl (string) -- The URL that points to an image used as the large icon to the notification content view.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            SmallImageIconUrl (string) -- The URL that points to an image used as the small icon for the notification which will be used to represent the notification in the status bar and content view
            Sound (string) -- Indicates a sound to play when the device receives the notification. Supports default, or the filename of a sound resource bundled in the app. Android sound files must reside in /res/raw/
            Substitutions (dict) -- Default message substitutions. Can be overridden by individual address substitutions.
            (string) --
            (list) --
            (string) --
            
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            DefaultMessage (dict) -- The default message for all channels.
            Body (string) -- The message body of the notification, the email body or the text message.
            Substitutions (dict) -- Default message substitutions. Can be overridden by individual address substitutions.
            (string) --
            (list) --
            (string) --
            
            
            DefaultPushNotificationMessage (dict) -- The default push notification message for all push channels.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify. Possible values include: OPEN_APP | DEEP_LINK | URL
            Body (string) -- The message body of the notification, the email body or the text message.
            Data (dict) -- The data payload used for a silent push. This payload is added to the notifications' data.pinpoint.jsonBody' object
            (string) --
            (string) --
            
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Substitutions (dict) -- Default message substitutions. Can be overridden by individual address substitutions.
            (string) --
            (list) --
            (string) --
            
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            GCMMessage (dict) -- The message to GCM channels. Overrides the default push notification message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify. Possible values include: OPEN_APP | DEEP_LINK | URL
            Body (string) -- The message body of the notification, the email body or the text message.
            CollapseKey (string) -- This parameter identifies a group of messages (e.g., with collapse_key: 'Updates Available') that can be collapsed, so that only the last message gets sent when delivery can be resumed. This is intended to avoid sending too many of the same messages when the device comes back online or becomes active.
            Data (dict) -- The data payload used for a silent push. This payload is added to the notifications' data.pinpoint.jsonBody' object
            (string) --
            (string) --
            
            IconReference (string) -- The icon image name of the asset saved in your application.
            ImageIconUrl (string) -- The URL that points to an image used as the large icon to the notification content view.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            Priority (string) -- The message priority. Amazon Pinpoint uses this value to set the FCM or GCM priority parameter when it sends the message. Accepts the following values: 'Normal' - Messages might be delayed. Delivery is optimized for battery usage on the receiving device. Use normal priority unless immediate delivery is required. 'High' - Messages are sent immediately and might wake a sleeping device. The equivalent values for APNs messages are '5' and '10'. Amazon Pinpoint accepts these values here and converts them. For more information, see About FCM Messages in the Firebase documentation.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            RestrictedPackageName (string) -- This parameter specifies the package name of the application where the registration tokens must match in order to receive the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            SmallImageIconUrl (string) -- The URL that points to an image used as the small icon for the notification which will be used to represent the notification in the status bar and content view
            Sound (string) -- Indicates a sound to play when the device receives the notification. Supports default, or the filename of a sound resource bundled in the app. Android sound files must reside in /res/raw/
            Substitutions (dict) -- Default message substitutions. Can be overridden by individual address substitutions.
            (string) --
            (list) --
            (string) --
            
            TimeToLive (integer) -- The length of time (in seconds) that FCM or GCM stores and attempts to deliver the message. If unspecified, the value defaults to the maximum, which is 2,419,200 seconds (28 days). Amazon Pinpoint uses this value to set the FCM or GCM time_to_live parameter.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            SMSMessage (dict) -- The message to SMS channels. Overrides the default message.
            Body (string) -- The message body of the notification, the email body or the text message.
            MessageType (string) -- Is this a transaction priority message or lower priority.
            OriginationNumber (string) -- The phone number that the SMS message originates from. Specify one of the dedicated long codes or short codes that you requested from AWS Support and that is assigned to your account. If this attribute is not specified, Amazon Pinpoint randomly assigns a long code.
            SenderId (string) -- The sender ID that is shown as the message sender on the recipient's device. Support for sender IDs varies by country or region.
            Substitutions (dict) -- Default message substitutions. Can be overridden by individual address substitutions.
            (string) --
            (list) --
            (string) --
            
            
            

    :rtype: dict
    :return: {
        'MessageResponse': {
            'ApplicationId': 'string',
            'EndpointResult': {
                'string': {
                    'Address': 'string',
                    'DeliveryStatus': 'SUCCESSFUL'|'THROTTLED'|'TEMPORARY_FAILURE'|'PERMANENT_FAILURE'|'UNKNOWN_FAILURE'|'OPT_OUT'|'DUPLICATE',
                    'StatusCode': 123,
                    'StatusMessage': 'string',
                    'UpdatedToken': 'string'
                }
            },
            'RequestId': 'string',
            'Result': {
                'string': {
                    'DeliveryStatus': 'SUCCESSFUL'|'THROTTLED'|'TEMPORARY_FAILURE'|'PERMANENT_FAILURE'|'UNKNOWN_FAILURE'|'OPT_OUT'|'DUPLICATE',
                    'StatusCode': 123,
                    'StatusMessage': 'string',
                    'UpdatedToken': 'string'
                }
            }
        }
    }
    
    
    :returns: 
    (dict) --
    MessageResponse (dict) -- Send message response.
    ApplicationId (string) -- Application id of the message.
    EndpointResult (dict) -- A map containing a multi part response for each address, with the endpointId as the key and the result as the value.
    (string) --
    (dict) -- The result from sending a message to an endpoint.
    Address (string) -- Address that endpoint message was delivered to.
    DeliveryStatus (string) -- Delivery status of message.
    StatusCode (integer) -- Downstream service status code.
    StatusMessage (string) -- Status message for message delivery.
    UpdatedToken (string) -- If token was updated as part of delivery. (This is GCM Specific)
    
    
    
    
    
    
    RequestId (string) -- Original request Id for which this message was delivered.
    Result (dict) -- A map containing a multi part response for each address, with the address as the key(Email address, phone number or push token) and the result as the value.
    (string) --
    (dict) -- The result from sending a message to an address.
    DeliveryStatus (string) -- Delivery status of message.
    StatusCode (integer) -- Downstream service status code.
    StatusMessage (string) -- Status message for message delivery.
    UpdatedToken (string) -- If token was updated as part of delivery. (This is GCM Specific)
    
    
    
    
    
    
    
    
    
    
    
    """
    pass

def send_users_messages(ApplicationId=None, SendUsersMessageRequest=None):
    """
    Send a batch of messages to users
    See also: AWS API Documentation
    
    
    :example: response = client.send_users_messages(
        ApplicationId='string',
        SendUsersMessageRequest={
            'Context': {
                'string': 'string'
            },
            'MessageConfiguration': {
                'ADMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ConsolidationKey': 'string',
                    'Data': {
                        'string': 'string'
                    },
                    'ExpiresAfter': 'string',
                    'IconReference': 'string',
                    'ImageIconUrl': 'string',
                    'ImageUrl': 'string',
                    'MD5': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'SmallImageIconUrl': 'string',
                    'Sound': 'string',
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    },
                    'Title': 'string',
                    'Url': 'string'
                },
                'APNSMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Badge': 123,
                    'Body': 'string',
                    'Category': 'string',
                    'CollapseId': 'string',
                    'Data': {
                        'string': 'string'
                    },
                    'MediaUrl': 'string',
                    'PreferredAuthenticationMethod': 'string',
                    'Priority': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Sound': 'string',
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    },
                    'ThreadId': 'string',
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'BaiduMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'Data': {
                        'string': 'string'
                    },
                    'IconReference': 'string',
                    'ImageIconUrl': 'string',
                    'ImageUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'SmallImageIconUrl': 'string',
                    'Sound': 'string',
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    },
                    'Title': 'string',
                    'Url': 'string'
                },
                'DefaultMessage': {
                    'Body': 'string',
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    }
                },
                'DefaultPushNotificationMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'Data': {
                        'string': 'string'
                    },
                    'SilentPush': True|False,
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    },
                    'Title': 'string',
                    'Url': 'string'
                },
                'GCMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'CollapseKey': 'string',
                    'Data': {
                        'string': 'string'
                    },
                    'IconReference': 'string',
                    'ImageIconUrl': 'string',
                    'ImageUrl': 'string',
                    'Priority': 'string',
                    'RawContent': 'string',
                    'RestrictedPackageName': 'string',
                    'SilentPush': True|False,
                    'SmallImageIconUrl': 'string',
                    'Sound': 'string',
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    },
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'SMSMessage': {
                    'Body': 'string',
                    'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                    'OriginationNumber': 'string',
                    'SenderId': 'string',
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    }
                }
            },
            'Users': {
                'string': {
                    'BodyOverride': 'string',
                    'Context': {
                        'string': 'string'
                    },
                    'RawContent': 'string',
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    },
                    'TitleOverride': 'string'
                }
            }
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type SendUsersMessageRequest: dict
    :param SendUsersMessageRequest: [REQUIRED] Send message request.
            Context (dict) -- A map of custom attributes to attributes to be attached to the message. This payload is added to the push notification's 'data.pinpoint' object or added to the email/sms delivery receipt event attributes.
            (string) --
            (string) --
            
            MessageConfiguration (dict) -- Message configuration.
            ADMMessage (dict) -- The message to ADM channels. Overrides the default push notification message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify. Possible values include: OPEN_APP | DEEP_LINK | URL
            Body (string) -- The message body of the notification, the email body or the text message.
            ConsolidationKey (string) -- Optional. Arbitrary string used to indicate multiple messages are logically the same and that ADM is allowed to drop previously enqueued messages in favor of this one.
            Data (dict) -- The data payload used for a silent push. This payload is added to the notifications' data.pinpoint.jsonBody' object
            (string) --
            (string) --
            
            ExpiresAfter (string) -- Optional. Number of seconds ADM should retain the message if the device is offline
            IconReference (string) -- The icon image name of the asset saved in your application.
            ImageIconUrl (string) -- The URL that points to an image used as the large icon to the notification content view.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            MD5 (string) -- Optional. Base-64-encoded MD5 checksum of the data parameter. Used to verify data integrity
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            SmallImageIconUrl (string) -- The URL that points to an image used as the small icon for the notification which will be used to represent the notification in the status bar and content view
            Sound (string) -- Indicates a sound to play when the device receives the notification. Supports default, or the filename of a sound resource bundled in the app. Android sound files must reside in /res/raw/
            Substitutions (dict) -- Default message substitutions. Can be overridden by individual address substitutions.
            (string) --
            (list) --
            (string) --
            
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            APNSMessage (dict) -- The message to APNS channels. Overrides the default push notification message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify. Possible values include: OPEN_APP | DEEP_LINK | URL
            Badge (integer) -- Include this key when you want the system to modify the badge of your app icon. If this key is not included in the dictionary, the badge is not changed. To remove the badge, set the value of this key to 0.
            Body (string) -- The message body of the notification, the email body or the text message.
            Category (string) -- Provide this key with a string value that represents the notification's type. This value corresponds to the value in the identifier property of one of your app's registered categories.
            CollapseId (string) -- An ID that, if assigned to multiple messages, causes APNs to coalesce the messages into a single push notification instead of delivering each message individually. The value must not exceed 64 bytes. Amazon Pinpoint uses this value to set the apns-collapse-id request header when it sends the message to APNs.
            Data (dict) -- The data payload used for a silent push. This payload is added to the notifications' data.pinpoint.jsonBody' object
            (string) --
            (string) --
            
            MediaUrl (string) -- The URL that points to a video used in the push notification.
            PreferredAuthenticationMethod (string) -- The preferred authentication method, either 'CERTIFICATE' or 'TOKEN'
            Priority (string) -- The message priority. Amazon Pinpoint uses this value to set the apns-priority request header when it sends the message to APNs. Accepts the following values: '5' - Low priority. Messages might be delayed, delivered in groups, and throttled. '10' - High priority. Messages are sent immediately. High priority messages must cause an alert, sound, or badge on the receiving device. The default value is '10'. The equivalent values for FCM or GCM messages are 'normal' and 'high'. Amazon Pinpoint accepts these values for APNs messages and converts them. For more information about the apns-priority parameter, see Communicating with APNs in the APNs Local and Remote Notification Programming Guide.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Sound (string) -- Include this key when you want the system to play a sound. The value of this key is the name of a sound file in your app's main bundle or in the Library/Sounds folder of your app's data container. If the sound file cannot be found, or if you specify defaultfor the value, the system plays the default alert sound.
            Substitutions (dict) -- Default message substitutions. Can be overridden by individual address substitutions.
            (string) --
            (list) --
            (string) --
            
            ThreadId (string) -- Provide this key with a string value that represents the app-specific identifier for grouping notifications. If you provide a Notification Content app extension, you can use this value to group your notifications together.
            TimeToLive (integer) -- The length of time (in seconds) that APNs stores and attempts to deliver the message. If the value is 0, APNs does not store the message or attempt to deliver it more than once. Amazon Pinpoint uses this value to set the apns-expiration request header when it sends the message to APNs.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            BaiduMessage (dict) -- The message to Baidu GCM channels. Overrides the default push notification message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify. Possible values include: OPEN_APP | DEEP_LINK | URL
            Body (string) -- The message body of the notification, the email body or the text message.
            Data (dict) -- The data payload used for a silent push. This payload is added to the notifications' data.pinpoint.jsonBody' object
            (string) --
            (string) --
            
            IconReference (string) -- The icon image name of the asset saved in your application.
            ImageIconUrl (string) -- The URL that points to an image used as the large icon to the notification content view.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            SmallImageIconUrl (string) -- The URL that points to an image used as the small icon for the notification which will be used to represent the notification in the status bar and content view
            Sound (string) -- Indicates a sound to play when the device receives the notification. Supports default, or the filename of a sound resource bundled in the app. Android sound files must reside in /res/raw/
            Substitutions (dict) -- Default message substitutions. Can be overridden by individual address substitutions.
            (string) --
            (list) --
            (string) --
            
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            DefaultMessage (dict) -- The default message for all channels.
            Body (string) -- The message body of the notification, the email body or the text message.
            Substitutions (dict) -- Default message substitutions. Can be overridden by individual address substitutions.
            (string) --
            (list) --
            (string) --
            
            
            DefaultPushNotificationMessage (dict) -- The default push notification message for all push channels.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify. Possible values include: OPEN_APP | DEEP_LINK | URL
            Body (string) -- The message body of the notification, the email body or the text message.
            Data (dict) -- The data payload used for a silent push. This payload is added to the notifications' data.pinpoint.jsonBody' object
            (string) --
            (string) --
            
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Substitutions (dict) -- Default message substitutions. Can be overridden by individual address substitutions.
            (string) --
            (list) --
            (string) --
            
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            GCMMessage (dict) -- The message to GCM channels. Overrides the default push notification message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify. Possible values include: OPEN_APP | DEEP_LINK | URL
            Body (string) -- The message body of the notification, the email body or the text message.
            CollapseKey (string) -- This parameter identifies a group of messages (e.g., with collapse_key: 'Updates Available') that can be collapsed, so that only the last message gets sent when delivery can be resumed. This is intended to avoid sending too many of the same messages when the device comes back online or becomes active.
            Data (dict) -- The data payload used for a silent push. This payload is added to the notifications' data.pinpoint.jsonBody' object
            (string) --
            (string) --
            
            IconReference (string) -- The icon image name of the asset saved in your application.
            ImageIconUrl (string) -- The URL that points to an image used as the large icon to the notification content view.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            Priority (string) -- The message priority. Amazon Pinpoint uses this value to set the FCM or GCM priority parameter when it sends the message. Accepts the following values: 'Normal' - Messages might be delayed. Delivery is optimized for battery usage on the receiving device. Use normal priority unless immediate delivery is required. 'High' - Messages are sent immediately and might wake a sleeping device. The equivalent values for APNs messages are '5' and '10'. Amazon Pinpoint accepts these values here and converts them. For more information, see About FCM Messages in the Firebase documentation.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            RestrictedPackageName (string) -- This parameter specifies the package name of the application where the registration tokens must match in order to receive the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            SmallImageIconUrl (string) -- The URL that points to an image used as the small icon for the notification which will be used to represent the notification in the status bar and content view
            Sound (string) -- Indicates a sound to play when the device receives the notification. Supports default, or the filename of a sound resource bundled in the app. Android sound files must reside in /res/raw/
            Substitutions (dict) -- Default message substitutions. Can be overridden by individual address substitutions.
            (string) --
            (list) --
            (string) --
            
            TimeToLive (integer) -- The length of time (in seconds) that FCM or GCM stores and attempts to deliver the message. If unspecified, the value defaults to the maximum, which is 2,419,200 seconds (28 days). Amazon Pinpoint uses this value to set the FCM or GCM time_to_live parameter.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            SMSMessage (dict) -- The message to SMS channels. Overrides the default message.
            Body (string) -- The message body of the notification, the email body or the text message.
            MessageType (string) -- Is this a transaction priority message or lower priority.
            OriginationNumber (string) -- The phone number that the SMS message originates from. Specify one of the dedicated long codes or short codes that you requested from AWS Support and that is assigned to your account. If this attribute is not specified, Amazon Pinpoint randomly assigns a long code.
            SenderId (string) -- The sender ID that is shown as the message sender on the recipient's device. Support for sender IDs varies by country or region.
            Substitutions (dict) -- Default message substitutions. Can be overridden by individual address substitutions.
            (string) --
            (list) --
            (string) --
            
            
            Users (dict) -- A map of destination endpoints, with the EndpointId as the key Endpoint Message Configuration as the value.
            (string) --
            (dict) -- Endpoint send configuration.
            BodyOverride (string) -- Body override. If specified will override default body.
            Context (dict) -- A map of custom attributes to attributes to be attached to the message for this address. This payload is added to the push notification's 'data.pinpoint' object or added to the email/sms delivery receipt event attributes.
            (string) --
            (string) --
            
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            Substitutions (dict) -- A map of substitution values for the message to be merged with the DefaultMessage's substitutions. Substitutions on this map take precedence over the all other substitutions.
            (string) --
            (list) --
            (string) --
            
            TitleOverride (string) -- Title override. If specified will override default title if applicable.
            
            

    :rtype: dict
    :return: {
        'SendUsersMessageResponse': {
            'ApplicationId': 'string',
            'RequestId': 'string',
            'Result': {
                'string': {
                    'string': {
                        'Address': 'string',
                        'DeliveryStatus': 'SUCCESSFUL'|'THROTTLED'|'TEMPORARY_FAILURE'|'PERMANENT_FAILURE'|'UNKNOWN_FAILURE'|'OPT_OUT'|'DUPLICATE',
                        'StatusCode': 123,
                        'StatusMessage': 'string',
                        'UpdatedToken': 'string'
                    }
                }
            }
        }
    }
    
    
    :returns: 
    (dict) --
    SendUsersMessageResponse (dict) -- User send message response.
    ApplicationId (string) -- Application id of the message.
    RequestId (string) -- Original request Id for which this message was delivered.
    Result (dict) -- A map containing of UserId to Map of EndpointId to Endpoint Message Result.
    (string) --
    (dict) --
    (string) --
    (dict) -- The result from sending a message to an endpoint.
    Address (string) -- Address that endpoint message was delivered to.
    DeliveryStatus (string) -- Delivery status of message.
    StatusCode (integer) -- Downstream service status code.
    StatusMessage (string) -- Status message for message delivery.
    UpdatedToken (string) -- If token was updated as part of delivery. (This is GCM Specific)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """
    pass

def update_adm_channel(ADMChannelRequest=None, ApplicationId=None):
    """
    Update an ADM channel
    See also: AWS API Documentation
    
    
    :example: response = client.update_adm_channel(
        ADMChannelRequest={
            'ClientId': 'string',
            'ClientSecret': 'string',
            'Enabled': True|False
        },
        ApplicationId='string'
    )
    
    
    :type ADMChannelRequest: dict
    :param ADMChannelRequest: [REQUIRED] Amazon Device Messaging channel definition.
            ClientId (string) -- Client ID as gotten from Amazon
            ClientSecret (string) -- Client secret as gotten from Amazon
            Enabled (boolean) -- If the channel is enabled for sending messages.
            

    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :rtype: dict
    :return: {
        'ADMChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) --
    ADMChannelResponse (dict) -- Amazon Device Messaging channel definition.
    ApplicationId (string) -- The ID of the application to which the channel applies.
    CreationDate (string) -- When was this segment created
    Enabled (boolean) -- If the channel is enabled for sending messages.
    HasCredential (boolean) -- Indicates whether the channel is configured with ADM credentials. Amazon Pinpoint uses your credentials to authenticate push notifications with ADM. Provide your credentials by setting the ClientId and ClientSecret attributes.
    Id (string) -- Channel ID. Not used, only for backwards compatibility.
    IsArchived (boolean) -- Is this channel archived
    LastModifiedBy (string) -- Who last updated this entry
    LastModifiedDate (string) -- Last date this was updated
    Platform (string) -- Platform type. Will be "ADM"
    Version (integer) -- Version of channel
    
    
    
    
    
    """
    pass

def update_apns_channel(APNSChannelRequest=None, ApplicationId=None):
    """
    Use to update the APNs channel for an app.
    See also: AWS API Documentation
    
    
    :example: response = client.update_apns_channel(
        APNSChannelRequest={
            'BundleId': 'string',
            'Certificate': 'string',
            'DefaultAuthenticationMethod': 'string',
            'Enabled': True|False,
            'PrivateKey': 'string',
            'TeamId': 'string',
            'TokenKey': 'string',
            'TokenKeyId': 'string'
        },
        ApplicationId='string'
    )
    
    
    :type APNSChannelRequest: dict
    :param APNSChannelRequest: [REQUIRED] Apple Push Notification Service channel definition.
            BundleId (string) -- The bundle id used for APNs Tokens.
            Certificate (string) -- The distribution certificate from Apple.
            DefaultAuthenticationMethod (string) -- The default authentication method used for APNs.
            Enabled (boolean) -- If the channel is enabled for sending messages.
            PrivateKey (string) -- The certificate private key.
            TeamId (string) -- The team id used for APNs Tokens.
            TokenKey (string) -- The token key used for APNs Tokens.
            TokenKeyId (string) -- The token key used for APNs Tokens.
            

    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :rtype: dict
    :return: {
        'APNSChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'DefaultAuthenticationMethod': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'HasTokenKey': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) --
    APNSChannelResponse (dict) -- Apple Distribution Push Notification Service channel definition.
    ApplicationId (string) -- The ID of the application to which the channel applies.
    CreationDate (string) -- When was this segment created
    DefaultAuthenticationMethod (string) -- The default authentication method used for APNs.
    Enabled (boolean) -- If the channel is enabled for sending messages.
    HasCredential (boolean) -- Indicates whether the channel is configured with APNs credentials. Amazon Pinpoint uses your credentials to authenticate push notifications with APNs. To use APNs token authentication, set the BundleId, TeamId, TokenKey, and TokenKeyId attributes. To use certificate authentication, set the Certificate and PrivateKey attributes.
    HasTokenKey (boolean) -- Indicates whether the channel is configured with a key for APNs token authentication. Provide a token key by setting the TokenKey attribute.
    Id (string) -- Channel ID. Not used. Present only for backwards compatibility.
    IsArchived (boolean) -- Is this channel archived
    LastModifiedBy (string) -- Who last updated this entry
    LastModifiedDate (string) -- Last date this was updated
    Platform (string) -- The platform type. Will be APNS.
    Version (integer) -- Version of channel
    
    
    
    
    
    """
    pass

def update_apns_sandbox_channel(APNSSandboxChannelRequest=None, ApplicationId=None):
    """
    Update an APNS sandbox channel
    See also: AWS API Documentation
    
    
    :example: response = client.update_apns_sandbox_channel(
        APNSSandboxChannelRequest={
            'BundleId': 'string',
            'Certificate': 'string',
            'DefaultAuthenticationMethod': 'string',
            'Enabled': True|False,
            'PrivateKey': 'string',
            'TeamId': 'string',
            'TokenKey': 'string',
            'TokenKeyId': 'string'
        },
        ApplicationId='string'
    )
    
    
    :type APNSSandboxChannelRequest: dict
    :param APNSSandboxChannelRequest: [REQUIRED] Apple Development Push Notification Service channel definition.
            BundleId (string) -- The bundle id used for APNs Tokens.
            Certificate (string) -- The distribution certificate from Apple.
            DefaultAuthenticationMethod (string) -- The default authentication method used for APNs.
            Enabled (boolean) -- If the channel is enabled for sending messages.
            PrivateKey (string) -- The certificate private key.
            TeamId (string) -- The team id used for APNs Tokens.
            TokenKey (string) -- The token key used for APNs Tokens.
            TokenKeyId (string) -- The token key used for APNs Tokens.
            

    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :rtype: dict
    :return: {
        'APNSSandboxChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'DefaultAuthenticationMethod': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'HasTokenKey': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) --
    APNSSandboxChannelResponse (dict) -- Apple Development Push Notification Service channel definition.
    ApplicationId (string) -- The ID of the application to which the channel applies.
    CreationDate (string) -- When was this segment created
    DefaultAuthenticationMethod (string) -- The default authentication method used for APNs.
    Enabled (boolean) -- If the channel is enabled for sending messages.
    HasCredential (boolean) -- Indicates whether the channel is configured with APNs credentials. Amazon Pinpoint uses your credentials to authenticate push notifications with APNs. To use APNs token authentication, set the BundleId, TeamId, TokenKey, and TokenKeyId attributes. To use certificate authentication, set the Certificate and PrivateKey attributes.
    HasTokenKey (boolean) -- Indicates whether the channel is configured with a key for APNs token authentication. Provide a token key by setting the TokenKey attribute.
    Id (string) -- Channel ID. Not used, only for backwards compatibility.
    IsArchived (boolean) -- Is this channel archived
    LastModifiedBy (string) -- Who last updated this entry
    LastModifiedDate (string) -- Last date this was updated
    Platform (string) -- The platform type. Will be APNS_SANDBOX.
    Version (integer) -- Version of channel
    
    
    
    
    
    """
    pass

def update_apns_voip_channel(APNSVoipChannelRequest=None, ApplicationId=None):
    """
    Update an APNS VoIP channel
    See also: AWS API Documentation
    
    
    :example: response = client.update_apns_voip_channel(
        APNSVoipChannelRequest={
            'BundleId': 'string',
            'Certificate': 'string',
            'DefaultAuthenticationMethod': 'string',
            'Enabled': True|False,
            'PrivateKey': 'string',
            'TeamId': 'string',
            'TokenKey': 'string',
            'TokenKeyId': 'string'
        },
        ApplicationId='string'
    )
    
    
    :type APNSVoipChannelRequest: dict
    :param APNSVoipChannelRequest: [REQUIRED] Apple VoIP Push Notification Service channel definition.
            BundleId (string) -- The bundle id used for APNs Tokens.
            Certificate (string) -- The distribution certificate from Apple.
            DefaultAuthenticationMethod (string) -- The default authentication method used for APNs.
            Enabled (boolean) -- If the channel is enabled for sending messages.
            PrivateKey (string) -- The certificate private key.
            TeamId (string) -- The team id used for APNs Tokens.
            TokenKey (string) -- The token key used for APNs Tokens.
            TokenKeyId (string) -- The token key used for APNs Tokens.
            

    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :rtype: dict
    :return: {
        'APNSVoipChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'DefaultAuthenticationMethod': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'HasTokenKey': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) --
    APNSVoipChannelResponse (dict) -- Apple VoIP Push Notification Service channel definition.
    ApplicationId (string) -- Application id
    CreationDate (string) -- When was this segment created
    DefaultAuthenticationMethod (string) -- The default authentication method used for APNs.
    Enabled (boolean) -- If the channel is enabled for sending messages.
    HasCredential (boolean) -- If the channel is registered with a credential for authentication.
    HasTokenKey (boolean) -- If the channel is registered with a token key for authentication.
    Id (string) -- Channel ID. Not used, only for backwards compatibility.
    IsArchived (boolean) -- Is this channel archived
    LastModifiedBy (string) -- Who made the last change
    LastModifiedDate (string) -- Last date this was updated
    Platform (string) -- The platform type. Will be APNS.
    Version (integer) -- Version of channel
    
    
    
    
    
    """
    pass

def update_apns_voip_sandbox_channel(APNSVoipSandboxChannelRequest=None, ApplicationId=None):
    """
    Update an APNS VoIP sandbox channel
    See also: AWS API Documentation
    
    
    :example: response = client.update_apns_voip_sandbox_channel(
        APNSVoipSandboxChannelRequest={
            'BundleId': 'string',
            'Certificate': 'string',
            'DefaultAuthenticationMethod': 'string',
            'Enabled': True|False,
            'PrivateKey': 'string',
            'TeamId': 'string',
            'TokenKey': 'string',
            'TokenKeyId': 'string'
        },
        ApplicationId='string'
    )
    
    
    :type APNSVoipSandboxChannelRequest: dict
    :param APNSVoipSandboxChannelRequest: [REQUIRED] Apple VoIP Developer Push Notification Service channel definition.
            BundleId (string) -- The bundle id used for APNs Tokens.
            Certificate (string) -- The distribution certificate from Apple.
            DefaultAuthenticationMethod (string) -- The default authentication method used for APNs.
            Enabled (boolean) -- If the channel is enabled for sending messages.
            PrivateKey (string) -- The certificate private key.
            TeamId (string) -- The team id used for APNs Tokens.
            TokenKey (string) -- The token key used for APNs Tokens.
            TokenKeyId (string) -- The token key used for APNs Tokens.
            

    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :rtype: dict
    :return: {
        'APNSVoipSandboxChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'DefaultAuthenticationMethod': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'HasTokenKey': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) --
    APNSVoipSandboxChannelResponse (dict) -- Apple VoIP Developer Push Notification Service channel definition.
    ApplicationId (string) -- Application id
    CreationDate (string) -- When was this segment created
    DefaultAuthenticationMethod (string) -- The default authentication method used for APNs.
    Enabled (boolean) -- If the channel is enabled for sending messages.
    HasCredential (boolean) -- If the channel is registered with a credential for authentication.
    HasTokenKey (boolean) -- If the channel is registered with a token key for authentication.
    Id (string) -- Channel ID. Not used, only for backwards compatibility.
    IsArchived (boolean) -- Is this channel archived
    LastModifiedBy (string) -- Who made the last change
    LastModifiedDate (string) -- Last date this was updated
    Platform (string) -- The platform type. Will be APNS.
    Version (integer) -- Version of channel
    
    
    
    
    
    """
    pass

def update_application_settings(ApplicationId=None, WriteApplicationSettingsRequest=None):
    """
    Used to update the settings for an app.
    See also: AWS API Documentation
    
    
    :example: response = client.update_application_settings(
        ApplicationId='string',
        WriteApplicationSettingsRequest={
            'CampaignHook': {
                'LambdaFunctionName': 'string',
                'Mode': 'DELIVERY'|'FILTER',
                'WebUrl': 'string'
            },
            'Limits': {
                'Daily': 123,
                'MaximumDuration': 123,
                'MessagesPerSecond': 123,
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
            CampaignHook (dict) -- Default campaign hook information.
            LambdaFunctionName (string) -- Lambda function name or arn to be called for delivery
            Mode (string) -- What mode Lambda should be invoked in.
            WebUrl (string) -- Web URL to call for hook. If the URL has authentication specified it will be added as authentication to the request
            Limits (dict) -- The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own.
            Daily (integer) -- The maximum number of messages that the campaign can send daily.
            MaximumDuration (integer) -- The length of time (in seconds) that the campaign can run before it ends and message deliveries stop. This duration begins at the scheduled start time for the campaign. The minimum value is 60.
            MessagesPerSecond (integer) -- The number of messages that the campaign can send per second. The minimum value is 50, and the maximum is 20000.
            Total (integer) -- The maximum total number of messages that the campaign can send.
            QuietTime (dict) -- The default quiet time for the app. Each campaign for this app sends no messages during this time unless the campaign overrides the default with a quiet time of its own.
            End (string) -- The default end time for quiet time in ISO 8601 format.
            Start (string) -- The default start time for quiet time in ISO 8601 format.
            

    :rtype: dict
    :return: {
        'ApplicationSettingsResource': {
            'ApplicationId': 'string',
            'CampaignHook': {
                'LambdaFunctionName': 'string',
                'Mode': 'DELIVERY'|'FILTER',
                'WebUrl': 'string'
            },
            'LastModifiedDate': 'string',
            'Limits': {
                'Daily': 123,
                'MaximumDuration': 123,
                'MessagesPerSecond': 123,
                'Total': 123
            },
            'QuietTime': {
                'End': 'string',
                'Start': 'string'
            }
        }
    }
    
    
    :returns: 
    (dict) --
    ApplicationSettingsResource (dict) -- Application settings.
    ApplicationId (string) -- The unique ID for the application.
    CampaignHook (dict) -- Default campaign hook.
    LambdaFunctionName (string) -- Lambda function name or arn to be called for delivery
    Mode (string) -- What mode Lambda should be invoked in.
    WebUrl (string) -- Web URL to call for hook. If the URL has authentication specified it will be added as authentication to the request
    
    
    LastModifiedDate (string) -- The date that the settings were last updated in ISO 8601 format.
    Limits (dict) -- The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own.
    Daily (integer) -- The maximum number of messages that the campaign can send daily.
    MaximumDuration (integer) -- The length of time (in seconds) that the campaign can run before it ends and message deliveries stop. This duration begins at the scheduled start time for the campaign. The minimum value is 60.
    MessagesPerSecond (integer) -- The number of messages that the campaign can send per second. The minimum value is 50, and the maximum is 20000.
    Total (integer) -- The maximum total number of messages that the campaign can send.
    
    
    QuietTime (dict) -- The default quiet time for the app. Each campaign for this app sends no messages during this time unless the campaign overrides the default with a quiet time of its own.
    End (string) -- The default end time for quiet time in ISO 8601 format.
    Start (string) -- The default start time for quiet time in ISO 8601 format.
    
    
    
    
    
    
    
    """
    pass

def update_baidu_channel(ApplicationId=None, BaiduChannelRequest=None):
    """
    Update a BAIDU GCM channel
    See also: AWS API Documentation
    
    
    :example: response = client.update_baidu_channel(
        ApplicationId='string',
        BaiduChannelRequest={
            'ApiKey': 'string',
            'Enabled': True|False,
            'SecretKey': 'string'
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type BaiduChannelRequest: dict
    :param BaiduChannelRequest: [REQUIRED] Baidu Cloud Push credentials
            ApiKey (string) -- Platform credential API key from Baidu.
            Enabled (boolean) -- If the channel is enabled for sending messages.
            SecretKey (string) -- Platform credential Secret key from Baidu.
            

    :rtype: dict
    :return: {
        'BaiduChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Credential': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) --
    BaiduChannelResponse (dict) -- Baidu Cloud Messaging channel definition
    ApplicationId (string) -- Application id
    CreationDate (string) -- When was this segment created
    Credential (string) -- The Baidu API key from Baidu.
    Enabled (boolean) -- If the channel is enabled for sending messages.
    HasCredential (boolean) -- Indicates whether the channel is configured with Baidu Cloud Push credentials. Amazon Pinpoint uses your credentials to authenticate push notifications with Baidu Cloud Push. Provide your credentials by setting the ApiKey and SecretKey attributes.
    Id (string) -- Channel ID. Not used, only for backwards compatibility.
    IsArchived (boolean) -- Is this channel archived
    LastModifiedBy (string) -- Who made the last change
    LastModifiedDate (string) -- Last date this was updated
    Platform (string) -- The platform type. Will be BAIDU
    Version (integer) -- Version of channel
    
    
    
    
    
    """
    pass

def update_campaign(ApplicationId=None, CampaignId=None, WriteCampaignRequest=None):
    """
    Use to update a campaign.
    See also: AWS API Documentation
    
    
    :example: response = client.update_campaign(
        ApplicationId='string',
        CampaignId='string',
        WriteCampaignRequest={
            'AdditionalTreatments': [
                {
                    'MessageConfiguration': {
                        'ADMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'APNSMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'BaiduMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'DefaultMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'EmailMessage': {
                            'Body': 'string',
                            'FromAddress': 'string',
                            'HtmlBody': 'string',
                            'Title': 'string'
                        },
                        'GCMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'SMSMessage': {
                            'Body': 'string',
                            'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                            'SenderId': 'string'
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
            'Hook': {
                'LambdaFunctionName': 'string',
                'Mode': 'DELIVERY'|'FILTER',
                'WebUrl': 'string'
            },
            'IsPaused': True|False,
            'Limits': {
                'Daily': 123,
                'MaximumDuration': 123,
                'MessagesPerSecond': 123,
                'Total': 123
            },
            'MessageConfiguration': {
                'ADMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'APNSMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'BaiduMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'DefaultMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'EmailMessage': {
                    'Body': 'string',
                    'FromAddress': 'string',
                    'HtmlBody': 'string',
                    'Title': 'string'
                },
                'GCMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'SMSMessage': {
                    'Body': 'string',
                    'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                    'SenderId': 'string'
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
            ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            DefaultMessage (dict) -- The default message for all channels.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            EmailMessage (dict) -- The email message configuration.
            Body (string) -- The email text body.
            FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
            HtmlBody (string) -- The email html body.
            Title (string) -- The email title (Or subject).
            GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            SMSMessage (dict) -- The SMS message configuration.
            Body (string) -- The SMS text body.
            MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
            SenderId (string) -- Sender ID of sent message.
            
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
            Hook (dict) -- Campaign hook information.
            LambdaFunctionName (string) -- Lambda function name or arn to be called for delivery
            Mode (string) -- What mode Lambda should be invoked in.
            WebUrl (string) -- Web URL to call for hook. If the URL has authentication specified it will be added as authentication to the request
            IsPaused (boolean) -- Indicates whether the campaign is paused. A paused campaign does not send messages unless you resume it by setting IsPaused to false.
            Limits (dict) -- The campaign limits settings.
            Daily (integer) -- The maximum number of messages that the campaign can send daily.
            MaximumDuration (integer) -- The length of time (in seconds) that the campaign can run before it ends and message deliveries stop. This duration begins at the scheduled start time for the campaign. The minimum value is 60.
            MessagesPerSecond (integer) -- The number of messages that the campaign can send per second. The minimum value is 50, and the maximum is 20000.
            Total (integer) -- The maximum total number of messages that the campaign can send.
            MessageConfiguration (dict) -- The message configuration settings.
            ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            DefaultMessage (dict) -- The default message for all channels.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            EmailMessage (dict) -- The email message configuration.
            Body (string) -- The email text body.
            FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
            HtmlBody (string) -- The email html body.
            Title (string) -- The email title (Or subject).
            GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            SMSMessage (dict) -- The SMS message configuration.
            Body (string) -- The SMS text body.
            MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
            SenderId (string) -- Sender ID of sent message.
            
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
                        'ADMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'APNSMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'BaiduMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'DefaultMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'EmailMessage': {
                            'Body': 'string',
                            'FromAddress': 'string',
                            'HtmlBody': 'string',
                            'Title': 'string'
                        },
                        'GCMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'SMSMessage': {
                            'Body': 'string',
                            'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                            'SenderId': 'string'
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
            'Hook': {
                'LambdaFunctionName': 'string',
                'Mode': 'DELIVERY'|'FILTER',
                'WebUrl': 'string'
            },
            'Id': 'string',
            'IsPaused': True|False,
            'LastModifiedDate': 'string',
            'Limits': {
                'Daily': 123,
                'MaximumDuration': 123,
                'MessagesPerSecond': 123,
                'Total': 123
            },
            'MessageConfiguration': {
                'ADMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'APNSMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'BaiduMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'DefaultMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'EmailMessage': {
                    'Body': 'string',
                    'FromAddress': 'string',
                    'HtmlBody': 'string',
                    'Title': 'string'
                },
                'GCMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Title': 'string',
                    'Url': 'string'
                },
                'SMSMessage': {
                    'Body': 'string',
                    'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                    'SenderId': 'string'
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
    (dict) --
    CampaignResponse (dict) -- Campaign definition
    AdditionalTreatments (list) -- Treatments that are defined in addition to the default treatment.
    (dict) -- Treatment resource
    Id (string) -- The unique treatment ID.
    MessageConfiguration (dict) -- The message configuration settings.
    ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    EmailMessage (dict) -- The email message configuration.
    Body (string) -- The email text body.
    FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
    HtmlBody (string) -- The email html body.
    Title (string) -- The email title (Or subject).
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    SMSMessage (dict) -- The SMS message configuration.
    Body (string) -- The SMS text body.
    MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
    SenderId (string) -- Sender ID of sent message.
    
    
    
    
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
    Hook (dict) -- Campaign hook information.
    LambdaFunctionName (string) -- Lambda function name or arn to be called for delivery
    Mode (string) -- What mode Lambda should be invoked in.
    WebUrl (string) -- Web URL to call for hook. If the URL has authentication specified it will be added as authentication to the request
    
    
    Id (string) -- The unique campaign ID.
    IsPaused (boolean) -- Indicates whether the campaign is paused. A paused campaign does not send messages unless you resume it by setting IsPaused to false.
    LastModifiedDate (string) -- The date the campaign was last updated in ISO 8601 format.
    Limits (dict) -- The campaign limits settings.
    Daily (integer) -- The maximum number of messages that the campaign can send daily.
    MaximumDuration (integer) -- The length of time (in seconds) that the campaign can run before it ends and message deliveries stop. This duration begins at the scheduled start time for the campaign. The minimum value is 60.
    MessagesPerSecond (integer) -- The number of messages that the campaign can send per second. The minimum value is 50, and the maximum is 20000.
    Total (integer) -- The maximum total number of messages that the campaign can send.
    
    
    MessageConfiguration (dict) -- The message configuration settings.
    ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    EmailMessage (dict) -- The email message configuration.
    Body (string) -- The email text body.
    FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
    HtmlBody (string) -- The email html body.
    Title (string) -- The email title (Or subject).
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- The URL that points to the media resource, for example a .mp4 or .gif file.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    SMSMessage (dict) -- The SMS message configuration.
    Body (string) -- The SMS text body.
    MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
    SenderId (string) -- Sender ID of sent message.
    
    
    
    
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

def update_email_channel(ApplicationId=None, EmailChannelRequest=None):
    """
    Update an email channel
    See also: AWS API Documentation
    
    
    :example: response = client.update_email_channel(
        ApplicationId='string',
        EmailChannelRequest={
            'Enabled': True|False,
            'FromAddress': 'string',
            'Identity': 'string',
            'RoleArn': 'string'
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type EmailChannelRequest: dict
    :param EmailChannelRequest: [REQUIRED] Email Channel Request
            Enabled (boolean) -- If the channel is enabled for sending messages.
            FromAddress (string) -- The email address used to send emails from.
            Identity (string) -- The ARN of an identity verified with SES.
            RoleArn (string) -- The ARN of an IAM Role used to submit events to Mobile Analytics' event ingestion service
            

    :rtype: dict
    :return: {
        'EmailChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Enabled': True|False,
            'FromAddress': 'string',
            'HasCredential': True|False,
            'Id': 'string',
            'Identity': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'RoleArn': 'string',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) --
    EmailChannelResponse (dict) -- Email Channel Response.
    ApplicationId (string) -- The unique ID of the application to which the email channel belongs.
    CreationDate (string) -- The date that the settings were last updated in ISO 8601 format.
    Enabled (boolean) -- If the channel is enabled for sending messages.
    FromAddress (string) -- The email address used to send emails from.
    HasCredential (boolean) -- If the channel is registered with a credential for authentication.
    Id (string) -- Channel ID. Not used, only for backwards compatibility.
    Identity (string) -- The ARN of an identity verified with SES.
    IsArchived (boolean) -- Is this channel archived
    LastModifiedBy (string) -- Who last updated this entry
    LastModifiedDate (string) -- Last date this was updated
    Platform (string) -- Platform type. Will be "EMAIL"
    RoleArn (string) -- The ARN of an IAM Role used to submit events to Mobile Analytics' event ingestion service
    Version (integer) -- Version of channel
    
    
    
    
    
    """
    pass

def update_endpoint(ApplicationId=None, EndpointId=None, EndpointRequest=None):
    """
    Use to update an endpoint.
    See also: AWS API Documentation
    
    
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
            'ChannelType': 'GCM'|'APNS'|'APNS_SANDBOX'|'APNS_VOIP'|'APNS_VOIP_SANDBOX'|'ADM'|'SMS'|'EMAIL'|'BAIDU'|'CUSTOM',
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
            Attributes (dict) -- Custom attributes that describe the endpoint by associating a name with an array of values. For example, an attribute named 'interests' might have the values ['science', 'politics', 'travel']. You can use these attributes as selection criteria when you create a segment of users to engage with a messaging campaign. The following characters are not recommended in attribute names: # : ? /. The Amazon Pinpoint console does not display attributes that include these characters in the name. This limitation does not apply to attribute values.
            (string) --
            (list) --
            (string) --
            
            ChannelType (string) -- The channel type. Valid values: GCM | APNS | APNS_SANDBOX | APNS_VOIP | APNS_VOIP_SANDBOX | ADM | SMS | EMAIL | BAIDU
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
            
            OptOut (string) -- Indicates whether a user has opted out of receiving messages with one of the following values: ALL - User has opted out of all messages. NONE - Users has not opted out and receives all messages.
            RequestId (string) -- The unique ID for the most recent request to update the endpoint.
            User (dict) -- Custom user-specific attributes that your app reports to Amazon Pinpoint.
            UserAttributes (dict) -- Custom attributes that describe an end user by associating a name with an array of values. For example, an attribute named 'interests' might have the values ['science', 'politics', 'travel']. You can use these attributes as selection criteria when you create a segment of users to engage with a messaging campaign. The following characters are not recommended in attribute names: # : ? /. The Amazon Pinpoint console does not display attributes that include these characters in the name. This limitation does not apply to attribute values.
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
    (dict) --
    MessageBody (dict) -- Simple message object.
    Message (string) -- The error message returned from the API.
    RequestID (string) -- The unique message body ID.
    
    
    
    
    
    """
    pass

def update_endpoints_batch(ApplicationId=None, EndpointBatchRequest=None):
    """
    Use to update a batch of endpoints.
    See also: AWS API Documentation
    
    
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
                    'ChannelType': 'GCM'|'APNS'|'APNS_SANDBOX'|'APNS_VOIP'|'APNS_VOIP_SANDBOX'|'ADM'|'SMS'|'EMAIL'|'BAIDU'|'CUSTOM',
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
            Attributes (dict) -- Custom attributes that describe the endpoint by associating a name with an array of values. For example, an attribute named 'interests' might have the values ['science', 'politics', 'travel']. You can use these attributes as selection criteria when you create a segment of users to engage with a messaging campaign. The following characters are not recommended in attribute names: # : ? /. The Amazon Pinpoint console does not display attributes that include these characters in the name. This limitation does not apply to attribute values.
            (string) --
            (list) --
            (string) --
            
            ChannelType (string) -- The channel type. Valid values: GCM | APNS | APNS_SANDBOX | APNS_VOIP | APNS_VOIP_SANDBOX | ADM | SMS | EMAIL | BAIDU
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
            
            OptOut (string) -- Indicates whether a user has opted out of receiving messages with one of the following values: ALL - User has opted out of all messages. NONE - Users has not opted out and receives all messages.
            RequestId (string) -- The unique ID for the most recent request to update the endpoint.
            User (dict) -- Custom user-specific attributes that your app reports to Amazon Pinpoint.
            UserAttributes (dict) -- Custom attributes that describe an end user by associating a name with an array of values. For example, an attribute named 'interests' might have the values ['science', 'politics', 'travel']. You can use these attributes as selection criteria when you create a segment of users to engage with a messaging campaign. The following characters are not recommended in attribute names: # : ? /. The Amazon Pinpoint console does not display attributes that include these characters in the name. This limitation does not apply to attribute values.
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
    (dict) --
    MessageBody (dict) -- Simple message object.
    Message (string) -- The error message returned from the API.
    RequestID (string) -- The unique message body ID.
    
    
    
    
    
    """
    pass

def update_gcm_channel(ApplicationId=None, GCMChannelRequest=None):
    """
    Use to update the GCM channel for an app.
    See also: AWS API Documentation
    
    
    :example: response = client.update_gcm_channel(
        ApplicationId='string',
        GCMChannelRequest={
            'ApiKey': 'string',
            'Enabled': True|False
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type GCMChannelRequest: dict
    :param GCMChannelRequest: [REQUIRED] Google Cloud Messaging credentials
            ApiKey (string) -- Platform credential API key from Google.
            Enabled (boolean) -- If the channel is enabled for sending messages.
            

    :rtype: dict
    :return: {
        'GCMChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Credential': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) --
    GCMChannelResponse (dict) -- Google Cloud Messaging channel definition
    ApplicationId (string) -- The ID of the application to which the channel applies.
    CreationDate (string) -- When was this segment created
    Credential (string) -- The GCM API key from Google.
    Enabled (boolean) -- If the channel is enabled for sending messages.
    HasCredential (boolean) -- Indicates whether the channel is configured with FCM or GCM credentials. Amazon Pinpoint uses your credentials to authenticate push notifications with FCM or GCM. Provide your credentials by setting the ApiKey attribute.
    Id (string) -- Channel ID. Not used. Present only for backwards compatibility.
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
    See also: AWS API Documentation
    
    
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
                    'Channel': {
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
            AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            
            Behavior (dict) -- The segment behaviors attributes.
            Recency (dict) -- The recency of use.
            Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
            RecencyType (string) -- The recency dimension type: ACTIVE - Users who have used your app within the specified duration are included in the segment. INACTIVE - Users who have not used your app within the specified duration are included in the segment.
            
            Demographic (dict) -- The segment demographics attributes.
            AppVersion (dict) -- The app version criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Channel (dict) -- The channel criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            DeviceType (dict) -- The device type criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Make (dict) -- The device make criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Model (dict) -- The device model criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Platform (dict) -- The device platform criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Location (dict) -- The segment location attributes.
            Country (dict) -- The country filter according to ISO 3166-1 Alpha-2 codes.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            UserAttributes (dict) -- Custom segment user attributes.
            (string) --
            (dict) -- Custom attibute dimension
            AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
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
                    'Channel': {
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
                'ChannelCounts': {
                    'string': 123
                },
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
    (dict) --
    SegmentResponse (dict) -- Segment definition.
    ApplicationId (string) -- The ID of the application to which the segment applies.
    CreationDate (string) -- The date the segment was created in ISO 8601 format.
    Dimensions (dict) -- The segment dimensions attributes.
    Attributes (dict) -- Custom segment attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    Behavior (dict) -- The segment behaviors attributes.
    Recency (dict) -- The recency of use.
    Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
    RecencyType (string) -- The recency dimension type: ACTIVE - Users who have used your app within the specified duration are included in the segment. INACTIVE - Users who have not used your app within the specified duration are included in the segment.
    
    
    
    
    Demographic (dict) -- The segment demographics attributes.
    AppVersion (dict) -- The app version criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Channel (dict) -- The channel criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    DeviceType (dict) -- The device type criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Make (dict) -- The device make criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Model (dict) -- The device model criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Platform (dict) -- The device platform criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    Location (dict) -- The segment location attributes.
    Country (dict) -- The country filter according to ISO 3166-1 Alpha-2 codes.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    UserAttributes (dict) -- Custom segment user attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    
    
    Id (string) -- The unique segment ID.
    ImportDefinition (dict) -- The import job settings.
    ChannelCounts (dict) -- Channel type counts
    (string) --
    (integer) --
    
    
    
    
    ExternalId (string) -- DEPRECATED. Your AWS account ID, which you assigned to the ExternalID key in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This requirement is removed, and external IDs are not recommended for IAM roles assumed by Amazon Pinpoint.
    Format (string) -- The format of the endpoint files that were imported to create this segment. Valid values: CSV, JSON
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the endpoints in Amazon S3.
    S3Url (string) -- A URL that points to the Amazon S3 location from which the endpoints for this segment were imported.
    Size (integer) -- The number of endpoints that were successfully imported to create this segment.
    
    
    LastModifiedDate (string) -- The date the segment was last updated in ISO 8601 format.
    Name (string) -- The name of segment
    SegmentType (string) -- The segment type: DIMENSIONAL - A dynamic segment built from selection criteria based on endpoint data reported by your app. You create this type of segment by using the segment builder in the Amazon Pinpoint console or by making a POST request to the segments resource. IMPORT - A static segment built from an imported set of endpoint definitions. You create this type of segment by importing a segment in the Amazon Pinpoint console or by making a POST request to the jobs/import resource.
    Version (integer) -- The segment version number.
    
    
    
    
    
    """
    pass

def update_sms_channel(ApplicationId=None, SMSChannelRequest=None):
    """
    Update an SMS channel
    See also: AWS API Documentation
    
    
    :example: response = client.update_sms_channel(
        ApplicationId='string',
        SMSChannelRequest={
            'Enabled': True|False,
            'SenderId': 'string',
            'ShortCode': 'string'
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]

    :type SMSChannelRequest: dict
    :param SMSChannelRequest: [REQUIRED] SMS Channel Request
            Enabled (boolean) -- If the channel is enabled for sending messages.
            SenderId (string) -- Sender identifier of your messages.
            ShortCode (string) -- ShortCode registered with phone provider.
            

    :rtype: dict
    :return: {
        'SMSChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'SenderId': 'string',
            'ShortCode': 'string',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) --
    SMSChannelResponse (dict) -- SMS Channel Response.
    ApplicationId (string) -- The unique ID of the application to which the SMS channel belongs.
    CreationDate (string) -- The date that the settings were last updated in ISO 8601 format.
    Enabled (boolean) -- If the channel is enabled for sending messages.
    HasCredential (boolean) -- If the channel is registered with a credential for authentication.
    Id (string) -- Channel ID. Not used, only for backwards compatibility.
    IsArchived (boolean) -- Is this channel archived
    LastModifiedBy (string) -- Who last updated this entry
    LastModifiedDate (string) -- Last date this was updated
    Platform (string) -- Platform type. Will be "SMS"
    SenderId (string) -- Sender identifier of your messages.
    ShortCode (string) -- The short code registered with the phone provider.
    Version (integer) -- Version of channel
    
    
    
    
    
    """
    pass

