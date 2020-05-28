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

def approve_skill(SkillId=None):
    """
    Associates a skill with the organization under the customer\'s AWS account. If a skill is private, the user implicitly accepts access to this skill during enablement.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.approve_skill(
        SkillId='string'
    )
    
    
    :type SkillId: string
    :param SkillId: [REQUIRED]\nThe unique identifier of the skill.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

AlexaForBusiness.Client.exceptions.LimitExceededException
AlexaForBusiness.Client.exceptions.NotFoundException
AlexaForBusiness.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.LimitExceededException
    AlexaForBusiness.Client.exceptions.NotFoundException
    AlexaForBusiness.Client.exceptions.ConcurrentModificationException
    
    """
    pass

def associate_contact_with_address_book(ContactArn=None, AddressBookArn=None):
    """
    Associates a contact with a given address book.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_contact_with_address_book(
        ContactArn='string',
        AddressBookArn='string'
    )
    
    
    :type ContactArn: string
    :param ContactArn: [REQUIRED]\nThe ARN of the contact to associate with an address book.\n

    :type AddressBookArn: string
    :param AddressBookArn: [REQUIRED]\nThe ARN of the address book with which to associate the contact.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AlexaForBusiness.Client.exceptions.LimitExceededException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def associate_device_with_network_profile(DeviceArn=None, NetworkProfileArn=None):
    """
    Associates a device with the specified network profile.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_device_with_network_profile(
        DeviceArn='string',
        NetworkProfileArn='string'
    )
    
    
    :type DeviceArn: string
    :param DeviceArn: [REQUIRED]\nThe device ARN.\n

    :type NetworkProfileArn: string
    :param NetworkProfileArn: [REQUIRED]\nThe ARN of the network profile to associate with a device.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException
AlexaForBusiness.Client.exceptions.ConcurrentModificationException
AlexaForBusiness.Client.exceptions.DeviceNotRegisteredException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def associate_device_with_room(DeviceArn=None, RoomArn=None):
    """
    Associates a device with a given room. This applies all the settings from the room profile to the device, and all the skills in any skill groups added to that room. This operation requires the device to be online, or else a manual sync is required.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_device_with_room(
        DeviceArn='string',
        RoomArn='string'
    )
    
    
    :type DeviceArn: string
    :param DeviceArn: The ARN of the device to associate to a room. Required.

    :type RoomArn: string
    :param RoomArn: The ARN of the room with which to associate the device. Required.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AlexaForBusiness.Client.exceptions.LimitExceededException
AlexaForBusiness.Client.exceptions.ConcurrentModificationException
AlexaForBusiness.Client.exceptions.DeviceNotRegisteredException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def associate_skill_group_with_room(SkillGroupArn=None, RoomArn=None):
    """
    Associates a skill group with a given room. This enables all skills in the associated skill group on all devices in the room.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_skill_group_with_room(
        SkillGroupArn='string',
        RoomArn='string'
    )
    
    
    :type SkillGroupArn: string
    :param SkillGroupArn: The ARN of the skill group to associate with a room. Required.

    :type RoomArn: string
    :param RoomArn: The ARN of the room with which to associate the skill group. Required.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AlexaForBusiness.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def associate_skill_with_skill_group(SkillGroupArn=None, SkillId=None):
    """
    Associates a skill with a skill group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_skill_with_skill_group(
        SkillGroupArn='string',
        SkillId='string'
    )
    
    
    :type SkillGroupArn: string
    :param SkillGroupArn: The ARN of the skill group to associate the skill to. Required.

    :type SkillId: string
    :param SkillId: [REQUIRED]\nThe unique identifier of the skill.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AlexaForBusiness.Client.exceptions.ConcurrentModificationException
AlexaForBusiness.Client.exceptions.NotFoundException
AlexaForBusiness.Client.exceptions.SkillNotLinkedException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def associate_skill_with_users(SkillId=None):
    """
    Makes a private skill available for enrolled users to enable on their devices.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_skill_with_users(
        SkillId='string'
    )
    
    
    :type SkillId: string
    :param SkillId: [REQUIRED]\nThe private skill ID you want to make available to enrolled users.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

AlexaForBusiness.Client.exceptions.ConcurrentModificationException
AlexaForBusiness.Client.exceptions.NotFoundException


    :return: {}
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.ConcurrentModificationException
    AlexaForBusiness.Client.exceptions.NotFoundException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_address_book(Name=None, Description=None, ClientRequestToken=None):
    """
    Creates an address book with the specified details.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_address_book(
        Name='string',
        Description='string',
        ClientRequestToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the address book.\n

    :type Description: string
    :param Description: The description of the address book.

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique, user-specified identifier for the request that ensures idempotency.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AddressBookArn': 'string'
}


Response Structure

(dict) --

AddressBookArn (string) --
The ARN of the newly created address book.







Exceptions

AlexaForBusiness.Client.exceptions.AlreadyExistsException
AlexaForBusiness.Client.exceptions.LimitExceededException


    :return: {
        'AddressBookArn': 'string'
    }
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.AlreadyExistsException
    AlexaForBusiness.Client.exceptions.LimitExceededException
    
    """
    pass

def create_business_report_schedule(ScheduleName=None, S3BucketName=None, S3KeyPrefix=None, Format=None, ContentRange=None, Recurrence=None, ClientRequestToken=None):
    """
    Creates a recurring schedule for usage reports to deliver to the specified S3 location with a specified daily or weekly interval.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_business_report_schedule(
        ScheduleName='string',
        S3BucketName='string',
        S3KeyPrefix='string',
        Format='CSV'|'CSV_ZIP',
        ContentRange={
            'Interval': 'ONE_DAY'|'ONE_WEEK'|'THIRTY_DAYS'
        },
        Recurrence={
            'StartDate': 'string'
        },
        ClientRequestToken='string'
    )
    
    
    :type ScheduleName: string
    :param ScheduleName: The name identifier of the schedule.

    :type S3BucketName: string
    :param S3BucketName: The S3 bucket name of the output reports. If this isn\'t specified, the report can be retrieved from a download link by calling ListBusinessReportSchedule.

    :type S3KeyPrefix: string
    :param S3KeyPrefix: The S3 key where the report is delivered.

    :type Format: string
    :param Format: [REQUIRED]\nThe format of the generated report (individual CSV files or zipped files of individual files).\n

    :type ContentRange: dict
    :param ContentRange: [REQUIRED]\nThe content range of the reports.\n\nInterval (string) --The interval of the content range.\n\n\n

    :type Recurrence: dict
    :param Recurrence: The recurrence of the reports. If this isn\'t specified, the report will only be delivered one time when the API is called.\n\nStartDate (string) --The start date.\n\n\n

    :type ClientRequestToken: string
    :param ClientRequestToken: The client request token.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ScheduleArn': 'string'
}


Response Structure

(dict) --

ScheduleArn (string) --
The ARN of the business report schedule.







Exceptions

AlexaForBusiness.Client.exceptions.AlreadyExistsException


    :return: {
        'ScheduleArn': 'string'
    }
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.AlreadyExistsException
    
    """
    pass

def create_conference_provider(ConferenceProviderName=None, ConferenceProviderType=None, IPDialIn=None, PSTNDialIn=None, MeetingSetting=None, ClientRequestToken=None):
    """
    Adds a new conference provider under the user\'s AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_conference_provider(
        ConferenceProviderName='string',
        ConferenceProviderType='CHIME'|'BLUEJEANS'|'FUZE'|'GOOGLE_HANGOUTS'|'POLYCOM'|'RINGCENTRAL'|'SKYPE_FOR_BUSINESS'|'WEBEX'|'ZOOM'|'CUSTOM',
        IPDialIn={
            'Endpoint': 'string',
            'CommsProtocol': 'SIP'|'SIPS'|'H323'
        },
        PSTNDialIn={
            'CountryCode': 'string',
            'PhoneNumber': 'string',
            'OneClickIdDelay': 'string',
            'OneClickPinDelay': 'string'
        },
        MeetingSetting={
            'RequirePin': 'YES'|'NO'|'OPTIONAL'
        },
        ClientRequestToken='string'
    )
    
    
    :type ConferenceProviderName: string
    :param ConferenceProviderName: [REQUIRED]\nThe name of the conference provider.\n

    :type ConferenceProviderType: string
    :param ConferenceProviderType: [REQUIRED]\nRepresents a type within a list of predefined types.\n

    :type IPDialIn: dict
    :param IPDialIn: The IP endpoint and protocol for calling.\n\nEndpoint (string) -- [REQUIRED]The IP address.\n\nCommsProtocol (string) -- [REQUIRED]The protocol, including SIP, SIPS, and H323.\n\n\n

    :type PSTNDialIn: dict
    :param PSTNDialIn: The information for PSTN conferencing.\n\nCountryCode (string) -- [REQUIRED]The zip code.\n\nPhoneNumber (string) -- [REQUIRED]The phone number to call to join the conference.\n\nOneClickIdDelay (string) -- [REQUIRED]The delay duration before Alexa enters the conference ID with dual-tone multi-frequency (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send data over the telephone network.\n\nOneClickPinDelay (string) -- [REQUIRED]The delay duration before Alexa enters the conference pin with dual-tone multi-frequency (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send data over the telephone network.\n\n\n

    :type MeetingSetting: dict
    :param MeetingSetting: [REQUIRED]\nThe meeting settings for the conference provider.\n\nRequirePin (string) -- [REQUIRED]The values that indicate whether the pin is always required.\n\n\n

    :type ClientRequestToken: string
    :param ClientRequestToken: The request token of the client.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ConferenceProviderArn': 'string'
}


Response Structure

(dict) --

ConferenceProviderArn (string) --
The ARN of the newly-created conference provider.







Exceptions

AlexaForBusiness.Client.exceptions.AlreadyExistsException


    :return: {
        'ConferenceProviderArn': 'string'
    }
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.AlreadyExistsException
    
    """
    pass

def create_contact(DisplayName=None, FirstName=None, LastName=None, PhoneNumber=None, PhoneNumbers=None, SipAddresses=None, ClientRequestToken=None):
    """
    Creates a contact with the specified details.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_contact(
        DisplayName='string',
        FirstName='string',
        LastName='string',
        PhoneNumber='string',
        PhoneNumbers=[
            {
                'Number': 'string',
                'Type': 'MOBILE'|'WORK'|'HOME'
            },
        ],
        SipAddresses=[
            {
                'Uri': 'string',
                'Type': 'WORK'
            },
        ],
        ClientRequestToken='string'
    )
    
    
    :type DisplayName: string
    :param DisplayName: The name of the contact to display on the console.

    :type FirstName: string
    :param FirstName: [REQUIRED]\nThe first name of the contact that is used to call the contact on the device.\n

    :type LastName: string
    :param LastName: The last name of the contact that is used to call the contact on the device.

    :type PhoneNumber: string
    :param PhoneNumber: The phone number of the contact in E.164 format. The phone number type defaults to WORK. You can specify PhoneNumber or PhoneNumbers. We recommend that you use PhoneNumbers, which lets you specify the phone number type and multiple numbers.

    :type PhoneNumbers: list
    :param PhoneNumbers: The list of phone numbers for the contact.\n\n(dict) --The phone number for the contact containing the raw number and phone number type.\n\nNumber (string) -- [REQUIRED]The raw value of the phone number.\n\nType (string) -- [REQUIRED]The type of the phone number.\n\n\n\n\n

    :type SipAddresses: list
    :param SipAddresses: The list of SIP addresses for the contact.\n\n(dict) --The SIP address for the contact containing the URI and SIP address type.\n\nUri (string) -- [REQUIRED]The URI for the SIP address.\n\nType (string) -- [REQUIRED]The type of the SIP address.\n\n\n\n\n

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique, user-specified identifier for this request that ensures idempotency.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ContactArn': 'string'
}


Response Structure

(dict) --

ContactArn (string) --
The ARN of the newly created address book.







Exceptions

AlexaForBusiness.Client.exceptions.AlreadyExistsException
AlexaForBusiness.Client.exceptions.LimitExceededException


    :return: {
        'ContactArn': 'string'
    }
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.AlreadyExistsException
    AlexaForBusiness.Client.exceptions.LimitExceededException
    
    """
    pass

def create_gateway_group(Name=None, Description=None, ClientRequestToken=None):
    """
    Creates a gateway group with the specified details.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_gateway_group(
        Name='string',
        Description='string',
        ClientRequestToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the gateway group.\n

    :type Description: string
    :param Description: The description of the gateway group.

    :type ClientRequestToken: string
    :param ClientRequestToken: [REQUIRED]\nA unique, user-specified identifier for the request that ensures idempotency.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GatewayGroupArn': 'string'
}


Response Structure

(dict) --

GatewayGroupArn (string) --
The ARN of the created gateway group.







Exceptions

AlexaForBusiness.Client.exceptions.AlreadyExistsException
AlexaForBusiness.Client.exceptions.LimitExceededException


    :return: {
        'GatewayGroupArn': 'string'
    }
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.AlreadyExistsException
    AlexaForBusiness.Client.exceptions.LimitExceededException
    
    """
    pass

def create_network_profile(NetworkProfileName=None, Description=None, Ssid=None, SecurityType=None, EapMethod=None, CurrentPassword=None, NextPassword=None, CertificateAuthorityArn=None, TrustAnchors=None, ClientRequestToken=None):
    """
    Creates a network profile with the specified details.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_network_profile(
        NetworkProfileName='string',
        Description='string',
        Ssid='string',
        SecurityType='OPEN'|'WEP'|'WPA_PSK'|'WPA2_PSK'|'WPA2_ENTERPRISE',
        EapMethod='EAP_TLS',
        CurrentPassword='string',
        NextPassword='string',
        CertificateAuthorityArn='string',
        TrustAnchors=[
            'string',
        ],
        ClientRequestToken='string'
    )
    
    
    :type NetworkProfileName: string
    :param NetworkProfileName: [REQUIRED]\nThe name of the network profile associated with a device.\n

    :type Description: string
    :param Description: Detailed information about a device\'s network profile.

    :type Ssid: string
    :param Ssid: [REQUIRED]\nThe SSID of the Wi-Fi network.\n

    :type SecurityType: string
    :param SecurityType: [REQUIRED]\nThe security type of the Wi-Fi network. This can be WPA2_ENTERPRISE, WPA2_PSK, WPA_PSK, WEP, or OPEN.\n

    :type EapMethod: string
    :param EapMethod: The authentication standard that is used in the EAP framework. Currently, EAP_TLS is supported.

    :type CurrentPassword: string
    :param CurrentPassword: The current password of the Wi-Fi network.

    :type NextPassword: string
    :param NextPassword: The next, or subsequent, password of the Wi-Fi network. This password is asynchronously transmitted to the device and is used when the password of the network changes to NextPassword.

    :type CertificateAuthorityArn: string
    :param CertificateAuthorityArn: The ARN of the Private Certificate Authority (PCA) created in AWS Certificate Manager (ACM). This is used to issue certificates to the devices.

    :type TrustAnchors: list
    :param TrustAnchors: The root certificates of your authentication server that is installed on your devices and used to trust your authentication server during EAP negotiation.\n\n(string) --\n\n

    :type ClientRequestToken: string
    :param ClientRequestToken: [REQUIRED]\nA unique, user-specified identifier for the request that ensures idempotency.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'NetworkProfileArn': 'string'
}


Response Structure

(dict) --

NetworkProfileArn (string) --
The ARN of the network profile associated with a device.







Exceptions

AlexaForBusiness.Client.exceptions.AlreadyExistsException
AlexaForBusiness.Client.exceptions.LimitExceededException
AlexaForBusiness.Client.exceptions.ConcurrentModificationException
AlexaForBusiness.Client.exceptions.InvalidCertificateAuthorityException
AlexaForBusiness.Client.exceptions.InvalidServiceLinkedRoleStateException


    :return: {
        'NetworkProfileArn': 'string'
    }
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.AlreadyExistsException
    AlexaForBusiness.Client.exceptions.LimitExceededException
    AlexaForBusiness.Client.exceptions.ConcurrentModificationException
    AlexaForBusiness.Client.exceptions.InvalidCertificateAuthorityException
    AlexaForBusiness.Client.exceptions.InvalidServiceLinkedRoleStateException
    
    """
    pass

def create_profile(ProfileName=None, Timezone=None, Address=None, DistanceUnit=None, TemperatureUnit=None, WakeWord=None, Locale=None, ClientRequestToken=None, SetupModeDisabled=None, MaxVolumeLimit=None, PSTNEnabled=None, MeetingRoomConfiguration=None):
    """
    Creates a new room profile with the specified details.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_profile(
        ProfileName='string',
        Timezone='string',
        Address='string',
        DistanceUnit='METRIC'|'IMPERIAL',
        TemperatureUnit='FAHRENHEIT'|'CELSIUS',
        WakeWord='ALEXA'|'AMAZON'|'ECHO'|'COMPUTER',
        Locale='string',
        ClientRequestToken='string',
        SetupModeDisabled=True|False,
        MaxVolumeLimit=123,
        PSTNEnabled=True|False,
        MeetingRoomConfiguration={
            'RoomUtilizationMetricsEnabled': True|False,
            'EndOfMeetingReminder': {
                'ReminderAtMinutes': [
                    123,
                ],
                'ReminderType': 'ANNOUNCEMENT_TIME_CHECK'|'ANNOUNCEMENT_VARIABLE_TIME_LEFT'|'CHIME'|'KNOCK',
                'Enabled': True|False
            },
            'InstantBooking': {
                'DurationInMinutes': 123,
                'Enabled': True|False
            },
            'RequireCheckIn': {
                'ReleaseAfterMinutes': 123,
                'Enabled': True|False
            }
        }
    )
    
    
    :type ProfileName: string
    :param ProfileName: [REQUIRED]\nThe name of a room profile.\n

    :type Timezone: string
    :param Timezone: [REQUIRED]\nThe time zone used by a room profile.\n

    :type Address: string
    :param Address: [REQUIRED]\nThe valid address for the room.\n

    :type DistanceUnit: string
    :param DistanceUnit: [REQUIRED]\nThe distance unit to be used by devices in the profile.\n

    :type TemperatureUnit: string
    :param TemperatureUnit: [REQUIRED]\nThe temperature unit to be used by devices in the profile.\n

    :type WakeWord: string
    :param WakeWord: [REQUIRED]\nA wake word for Alexa, Echo, Amazon, or a computer.\n

    :type Locale: string
    :param Locale: The locale of the room profile. (This is currently only available to a limited preview audience.)

    :type ClientRequestToken: string
    :param ClientRequestToken: The user-specified token that is used during the creation of a profile.\nThis field is autopopulated if not provided.\n

    :type SetupModeDisabled: boolean
    :param SetupModeDisabled: Whether room profile setup is enabled.

    :type MaxVolumeLimit: integer
    :param MaxVolumeLimit: The maximum volume limit for a room profile.

    :type PSTNEnabled: boolean
    :param PSTNEnabled: Whether PSTN calling is enabled.

    :type MeetingRoomConfiguration: dict
    :param MeetingRoomConfiguration: The meeting room settings of a room profile.\n\nRoomUtilizationMetricsEnabled (boolean) --Whether room utilization metrics are enabled or not.\n\nEndOfMeetingReminder (dict) --Creates settings for the end of meeting reminder feature that are applied to a room profile. The end of meeting reminder enables Alexa to remind users when a meeting is ending.\n\nReminderAtMinutes (list) -- [REQUIRED]A range of 3 to 15 minutes that determines when the reminder begins.\n\n(integer) --\n\n\nReminderType (string) -- [REQUIRED]The type of sound that users hear during the end of meeting reminder.\n\nEnabled (boolean) -- [REQUIRED]Whether an end of meeting reminder is enabled or not.\n\n\n\nInstantBooking (dict) --Settings to automatically book a room for a configured duration if it\'s free when joining a meeting with Alexa.\n\nDurationInMinutes (integer) -- [REQUIRED]Duration between 15 and 240 minutes at increments of 15 that determines how long to book an available room when a meeting is started with Alexa.\n\nEnabled (boolean) -- [REQUIRED]Whether instant booking is enabled or not.\n\n\n\nRequireCheckIn (dict) --Settings for requiring a check in when a room is reserved. Alexa can cancel a room reservation if it\'s not checked into to make the room available for others. Users can check in by joining the meeting with Alexa or an AVS device, or by saying \xe2\x80\x9cAlexa, check in.\xe2\x80\x9d\n\nReleaseAfterMinutes (integer) -- [REQUIRED]Duration between 5 and 20 minutes to determine when to release the room if it\'s not checked into.\n\nEnabled (boolean) -- [REQUIRED]Whether require check in is enabled or not.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ProfileArn': 'string'
}


Response Structure

(dict) --

ProfileArn (string) --
The ARN of the newly created room profile in the response.







Exceptions

AlexaForBusiness.Client.exceptions.LimitExceededException
AlexaForBusiness.Client.exceptions.AlreadyExistsException
AlexaForBusiness.Client.exceptions.ConcurrentModificationException


    :return: {
        'ProfileArn': 'string'
    }
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.LimitExceededException
    AlexaForBusiness.Client.exceptions.AlreadyExistsException
    AlexaForBusiness.Client.exceptions.ConcurrentModificationException
    
    """
    pass

def create_room(RoomName=None, Description=None, ProfileArn=None, ProviderCalendarId=None, ClientRequestToken=None, Tags=None):
    """
    Creates a room with the specified details.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_room(
        RoomName='string',
        Description='string',
        ProfileArn='string',
        ProviderCalendarId='string',
        ClientRequestToken='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type RoomName: string
    :param RoomName: [REQUIRED]\nThe name for the room.\n

    :type Description: string
    :param Description: The description for the room.

    :type ProfileArn: string
    :param ProfileArn: The profile ARN for the room.

    :type ProviderCalendarId: string
    :param ProviderCalendarId: The calendar ARN for the room.

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique, user-specified identifier for this request that ensures idempotency.\nThis field is autopopulated if not provided.\n

    :type Tags: list
    :param Tags: The tags for the room.\n\n(dict) --A key-value pair that can be associated with a resource.\n\nKey (string) -- [REQUIRED]The key of a tag. Tag keys are case-sensitive.\n\nValue (string) -- [REQUIRED]The value of a tag. Tag values are case sensitive and can be null.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'RoomArn': 'string'
}


Response Structure

(dict) --

RoomArn (string) --
The ARN of the newly created room in the response.







Exceptions

AlexaForBusiness.Client.exceptions.AlreadyExistsException
AlexaForBusiness.Client.exceptions.LimitExceededException


    :return: {
        'RoomArn': 'string'
    }
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.AlreadyExistsException
    AlexaForBusiness.Client.exceptions.LimitExceededException
    
    """
    pass

def create_skill_group(SkillGroupName=None, Description=None, ClientRequestToken=None):
    """
    Creates a skill group with a specified name and description.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_skill_group(
        SkillGroupName='string',
        Description='string',
        ClientRequestToken='string'
    )
    
    
    :type SkillGroupName: string
    :param SkillGroupName: [REQUIRED]\nThe name for the skill group.\n

    :type Description: string
    :param Description: The description for the skill group.

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique, user-specified identifier for this request that ensures idempotency.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'SkillGroupArn': 'string'
}


Response Structure

(dict) --

SkillGroupArn (string) --
The ARN of the newly created skill group in the response.







Exceptions

AlexaForBusiness.Client.exceptions.AlreadyExistsException
AlexaForBusiness.Client.exceptions.LimitExceededException
AlexaForBusiness.Client.exceptions.ConcurrentModificationException


    :return: {
        'SkillGroupArn': 'string'
    }
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.AlreadyExistsException
    AlexaForBusiness.Client.exceptions.LimitExceededException
    AlexaForBusiness.Client.exceptions.ConcurrentModificationException
    
    """
    pass

def create_user(UserId=None, FirstName=None, LastName=None, Email=None, ClientRequestToken=None, Tags=None):
    """
    Creates a user.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_user(
        UserId='string',
        FirstName='string',
        LastName='string',
        Email='string',
        ClientRequestToken='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type UserId: string
    :param UserId: [REQUIRED]\nThe ARN for the user.\n

    :type FirstName: string
    :param FirstName: The first name for the user.

    :type LastName: string
    :param LastName: The last name for the user.

    :type Email: string
    :param Email: The email address for the user.

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique, user-specified identifier for this request that ensures idempotency.\nThis field is autopopulated if not provided.\n

    :type Tags: list
    :param Tags: The tags for the user.\n\n(dict) --A key-value pair that can be associated with a resource.\n\nKey (string) -- [REQUIRED]The key of a tag. Tag keys are case-sensitive.\n\nValue (string) -- [REQUIRED]The value of a tag. Tag values are case sensitive and can be null.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'UserArn': 'string'
}


Response Structure

(dict) --

UserArn (string) --
The ARN of the newly created user in the response.







Exceptions

AlexaForBusiness.Client.exceptions.ResourceInUseException
AlexaForBusiness.Client.exceptions.LimitExceededException
AlexaForBusiness.Client.exceptions.ConcurrentModificationException


    :return: {
        'UserArn': 'string'
    }
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.ResourceInUseException
    AlexaForBusiness.Client.exceptions.LimitExceededException
    AlexaForBusiness.Client.exceptions.ConcurrentModificationException
    
    """
    pass

def delete_address_book(AddressBookArn=None):
    """
    Deletes an address book by the address book ARN.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_address_book(
        AddressBookArn='string'
    )
    
    
    :type AddressBookArn: string
    :param AddressBookArn: [REQUIRED]\nThe ARN of the address book to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException
AlexaForBusiness.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.NotFoundException
    AlexaForBusiness.Client.exceptions.ConcurrentModificationException
    
    """
    pass

def delete_business_report_schedule(ScheduleArn=None):
    """
    Deletes the recurring report delivery schedule with the specified schedule ARN.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_business_report_schedule(
        ScheduleArn='string'
    )
    
    
    :type ScheduleArn: string
    :param ScheduleArn: [REQUIRED]\nThe ARN of the business report schedule.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException
AlexaForBusiness.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.NotFoundException
    AlexaForBusiness.Client.exceptions.ConcurrentModificationException
    
    """
    pass

def delete_conference_provider(ConferenceProviderArn=None):
    """
    Deletes a conference provider.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_conference_provider(
        ConferenceProviderArn='string'
    )
    
    
    :type ConferenceProviderArn: string
    :param ConferenceProviderArn: [REQUIRED]\nThe ARN of the conference provider.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException


    :return: {}
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.NotFoundException
    
    """
    pass

def delete_contact(ContactArn=None):
    """
    Deletes a contact by the contact ARN.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_contact(
        ContactArn='string'
    )
    
    
    :type ContactArn: string
    :param ContactArn: [REQUIRED]\nThe ARN of the contact to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException
AlexaForBusiness.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.NotFoundException
    AlexaForBusiness.Client.exceptions.ConcurrentModificationException
    
    """
    pass

def delete_device(DeviceArn=None):
    """
    Removes a device from Alexa For Business.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_device(
        DeviceArn='string'
    )
    
    
    :type DeviceArn: string
    :param DeviceArn: [REQUIRED]\nThe ARN of the device for which to request details.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException
AlexaForBusiness.Client.exceptions.ConcurrentModificationException
AlexaForBusiness.Client.exceptions.InvalidCertificateAuthorityException


    :return: {}
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.NotFoundException
    AlexaForBusiness.Client.exceptions.ConcurrentModificationException
    AlexaForBusiness.Client.exceptions.InvalidCertificateAuthorityException
    
    """
    pass

def delete_device_usage_data(DeviceArn=None, DeviceUsageType=None):
    """
    When this action is called for a specified shared device, it allows authorized users to delete the device\'s entire previous history of voice input data and associated response data. This action can be called once every 24 hours for a specific shared device.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_device_usage_data(
        DeviceArn='string',
        DeviceUsageType='VOICE'
    )
    
    
    :type DeviceArn: string
    :param DeviceArn: [REQUIRED]\nThe ARN of the device.\n

    :type DeviceUsageType: string
    :param DeviceUsageType: [REQUIRED]\nThe type of usage data to delete.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException
AlexaForBusiness.Client.exceptions.DeviceNotRegisteredException
AlexaForBusiness.Client.exceptions.LimitExceededException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_gateway_group(GatewayGroupArn=None):
    """
    Deletes a gateway group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_gateway_group(
        GatewayGroupArn='string'
    )
    
    
    :type GatewayGroupArn: string
    :param GatewayGroupArn: [REQUIRED]\nThe ARN of the gateway group to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

AlexaForBusiness.Client.exceptions.ResourceAssociatedException


    :return: {}
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.ResourceAssociatedException
    
    """
    pass

def delete_network_profile(NetworkProfileArn=None):
    """
    Deletes a network profile by the network profile ARN.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_network_profile(
        NetworkProfileArn='string'
    )
    
    
    :type NetworkProfileArn: string
    :param NetworkProfileArn: [REQUIRED]\nThe ARN of the network profile associated with a device.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

AlexaForBusiness.Client.exceptions.ResourceInUseException
AlexaForBusiness.Client.exceptions.ConcurrentModificationException
AlexaForBusiness.Client.exceptions.NotFoundException


    :return: {}
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.ResourceInUseException
    AlexaForBusiness.Client.exceptions.ConcurrentModificationException
    AlexaForBusiness.Client.exceptions.NotFoundException
    
    """
    pass

def delete_profile(ProfileArn=None):
    """
    Deletes a room profile by the profile ARN.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_profile(
        ProfileArn='string'
    )
    
    
    :type ProfileArn: string
    :param ProfileArn: The ARN of the room profile to delete. Required.

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException
AlexaForBusiness.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.NotFoundException
    AlexaForBusiness.Client.exceptions.ConcurrentModificationException
    
    """
    pass

def delete_room(RoomArn=None):
    """
    Deletes a room by the room ARN.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_room(
        RoomArn='string'
    )
    
    
    :type RoomArn: string
    :param RoomArn: The ARN of the room to delete. Required.

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException
AlexaForBusiness.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.NotFoundException
    AlexaForBusiness.Client.exceptions.ConcurrentModificationException
    
    """
    pass

def delete_room_skill_parameter(RoomArn=None, SkillId=None, ParameterKey=None):
    """
    Deletes room skill parameter details by room, skill, and parameter key ID.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_room_skill_parameter(
        RoomArn='string',
        SkillId='string',
        ParameterKey='string'
    )
    
    
    :type RoomArn: string
    :param RoomArn: The ARN of the room from which to remove the room skill parameter details.

    :type SkillId: string
    :param SkillId: [REQUIRED]\nThe ID of the skill from which to remove the room skill parameter details.\n

    :type ParameterKey: string
    :param ParameterKey: [REQUIRED]\nThe room skill parameter key for which to remove details.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AlexaForBusiness.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_skill_authorization(SkillId=None, RoomArn=None):
    """
    Unlinks a third-party account from a skill.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_skill_authorization(
        SkillId='string',
        RoomArn='string'
    )
    
    
    :type SkillId: string
    :param SkillId: [REQUIRED]\nThe unique identifier of a skill.\n

    :type RoomArn: string
    :param RoomArn: The room that the skill is authorized for.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException
AlexaForBusiness.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_skill_group(SkillGroupArn=None):
    """
    Deletes a skill group by skill group ARN.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_skill_group(
        SkillGroupArn='string'
    )
    
    
    :type SkillGroupArn: string
    :param SkillGroupArn: The ARN of the skill group to delete. Required.

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException
AlexaForBusiness.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.NotFoundException
    AlexaForBusiness.Client.exceptions.ConcurrentModificationException
    
    """
    pass

def delete_user(UserArn=None, EnrollmentId=None):
    """
    Deletes a specified user by user ARN and enrollment ARN.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_user(
        UserArn='string',
        EnrollmentId='string'
    )
    
    
    :type UserArn: string
    :param UserArn: The ARN of the user to delete in the organization. Required.

    :type EnrollmentId: string
    :param EnrollmentId: [REQUIRED]\nThe ARN of the user\'s enrollment in the organization. Required.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException
AlexaForBusiness.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def disassociate_contact_from_address_book(ContactArn=None, AddressBookArn=None):
    """
    Disassociates a contact from a given address book.
    See also: AWS API Documentation
    
    
    :example: response = client.disassociate_contact_from_address_book(
        ContactArn='string',
        AddressBookArn='string'
    )
    
    
    :type ContactArn: string
    :param ContactArn: [REQUIRED]\nThe ARN of the contact to disassociate from an address book.\n

    :type AddressBookArn: string
    :param AddressBookArn: [REQUIRED]\nThe ARN of the address from which to disassociate the contact.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --





    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def disassociate_device_from_room(DeviceArn=None):
    """
    Disassociates a device from its current room. The device continues to be connected to the Wi-Fi network and is still registered to the account. The device settings and skills are removed from the room.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_device_from_room(
        DeviceArn='string'
    )
    
    
    :type DeviceArn: string
    :param DeviceArn: The ARN of the device to disassociate from a room. Required.

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

AlexaForBusiness.Client.exceptions.ConcurrentModificationException
AlexaForBusiness.Client.exceptions.DeviceNotRegisteredException


    :return: {}
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.ConcurrentModificationException
    AlexaForBusiness.Client.exceptions.DeviceNotRegisteredException
    
    """
    pass

def disassociate_skill_from_skill_group(SkillGroupArn=None, SkillId=None):
    """
    Disassociates a skill from a skill group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_skill_from_skill_group(
        SkillGroupArn='string',
        SkillId='string'
    )
    
    
    :type SkillGroupArn: string
    :param SkillGroupArn: The unique identifier of a skill. Required.

    :type SkillId: string
    :param SkillId: [REQUIRED]\nThe ARN of a skill group to associate to a skill.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AlexaForBusiness.Client.exceptions.ConcurrentModificationException
AlexaForBusiness.Client.exceptions.NotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def disassociate_skill_from_users(SkillId=None):
    """
    Makes a private skill unavailable for enrolled users and prevents them from enabling it on their devices.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_skill_from_users(
        SkillId='string'
    )
    
    
    :type SkillId: string
    :param SkillId: [REQUIRED]\nThe private skill ID you want to make unavailable for enrolled users.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

AlexaForBusiness.Client.exceptions.ConcurrentModificationException
AlexaForBusiness.Client.exceptions.NotFoundException


    :return: {}
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.ConcurrentModificationException
    AlexaForBusiness.Client.exceptions.NotFoundException
    
    """
    pass

def disassociate_skill_group_from_room(SkillGroupArn=None, RoomArn=None):
    """
    Disassociates a skill group from a specified room. This disables all skills in the skill group on all devices in the room.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_skill_group_from_room(
        SkillGroupArn='string',
        RoomArn='string'
    )
    
    
    :type SkillGroupArn: string
    :param SkillGroupArn: The ARN of the skill group to disassociate from a room. Required.

    :type RoomArn: string
    :param RoomArn: The ARN of the room from which the skill group is to be disassociated. Required.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AlexaForBusiness.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def forget_smart_home_appliances(RoomArn=None):
    """
    Forgets smart home appliances associated to a room.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.forget_smart_home_appliances(
        RoomArn='string'
    )
    
    
    :type RoomArn: string
    :param RoomArn: [REQUIRED]\nThe room that the appliances are associated with.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException


    :return: {}
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.NotFoundException
    
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

def get_address_book(AddressBookArn=None):
    """
    Gets address the book details by the address book ARN.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_address_book(
        AddressBookArn='string'
    )
    
    
    :type AddressBookArn: string
    :param AddressBookArn: [REQUIRED]\nThe ARN of the address book for which to request details.\n

    :rtype: dict
ReturnsResponse Syntax{
    'AddressBook': {
        'AddressBookArn': 'string',
        'Name': 'string',
        'Description': 'string'
    }
}


Response Structure

(dict) --
AddressBook (dict) --The details of the requested address book.

AddressBookArn (string) --The ARN of the address book.

Name (string) --The name of the address book.

Description (string) --The description of the address book.








Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException


    :return: {
        'AddressBook': {
            'AddressBookArn': 'string',
            'Name': 'string',
            'Description': 'string'
        }
    }
    
    
    """
    pass

def get_conference_preference():
    """
    Retrieves the existing conference preferences.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_conference_preference()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'Preference': {
        'DefaultConferenceProviderArn': 'string'
    }
}


Response Structure

(dict) --
Preference (dict) --The conference preference.

DefaultConferenceProviderArn (string) --The ARN of the default conference provider.








Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException


    :return: {
        'Preference': {
            'DefaultConferenceProviderArn': 'string'
        }
    }
    
    
    """
    pass

def get_conference_provider(ConferenceProviderArn=None):
    """
    Gets details about a specific conference provider.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_conference_provider(
        ConferenceProviderArn='string'
    )
    
    
    :type ConferenceProviderArn: string
    :param ConferenceProviderArn: [REQUIRED]\nThe ARN of the newly created conference provider.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ConferenceProvider': {
        'Arn': 'string',
        'Name': 'string',
        'Type': 'CHIME'|'BLUEJEANS'|'FUZE'|'GOOGLE_HANGOUTS'|'POLYCOM'|'RINGCENTRAL'|'SKYPE_FOR_BUSINESS'|'WEBEX'|'ZOOM'|'CUSTOM',
        'IPDialIn': {
            'Endpoint': 'string',
            'CommsProtocol': 'SIP'|'SIPS'|'H323'
        },
        'PSTNDialIn': {
            'CountryCode': 'string',
            'PhoneNumber': 'string',
            'OneClickIdDelay': 'string',
            'OneClickPinDelay': 'string'
        },
        'MeetingSetting': {
            'RequirePin': 'YES'|'NO'|'OPTIONAL'
        }
    }
}


Response Structure

(dict) --
ConferenceProvider (dict) --The conference provider.

Arn (string) --The ARN of the newly created conference provider.

Name (string) --The name of the conference provider.

Type (string) --The type of conference providers.

IPDialIn (dict) --The IP endpoint and protocol for calling.

Endpoint (string) --The IP address.

CommsProtocol (string) --The protocol, including SIP, SIPS, and H323.



PSTNDialIn (dict) --The information for PSTN conferencing.

CountryCode (string) --The zip code.

PhoneNumber (string) --The phone number to call to join the conference.

OneClickIdDelay (string) --The delay duration before Alexa enters the conference ID with dual-tone multi-frequency (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send data over the telephone network.

OneClickPinDelay (string) --The delay duration before Alexa enters the conference pin with dual-tone multi-frequency (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send data over the telephone network.



MeetingSetting (dict) --The meeting settings for the conference provider.

RequirePin (string) --The values that indicate whether the pin is always required.










Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException


    :return: {
        'ConferenceProvider': {
            'Arn': 'string',
            'Name': 'string',
            'Type': 'CHIME'|'BLUEJEANS'|'FUZE'|'GOOGLE_HANGOUTS'|'POLYCOM'|'RINGCENTRAL'|'SKYPE_FOR_BUSINESS'|'WEBEX'|'ZOOM'|'CUSTOM',
            'IPDialIn': {
                'Endpoint': 'string',
                'CommsProtocol': 'SIP'|'SIPS'|'H323'
            },
            'PSTNDialIn': {
                'CountryCode': 'string',
                'PhoneNumber': 'string',
                'OneClickIdDelay': 'string',
                'OneClickPinDelay': 'string'
            },
            'MeetingSetting': {
                'RequirePin': 'YES'|'NO'|'OPTIONAL'
            }
        }
    }
    
    
    """
    pass

def get_contact(ContactArn=None):
    """
    Gets the contact details by the contact ARN.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_contact(
        ContactArn='string'
    )
    
    
    :type ContactArn: string
    :param ContactArn: [REQUIRED]\nThe ARN of the contact for which to request details.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Contact': {
        'ContactArn': 'string',
        'DisplayName': 'string',
        'FirstName': 'string',
        'LastName': 'string',
        'PhoneNumber': 'string',
        'PhoneNumbers': [
            {
                'Number': 'string',
                'Type': 'MOBILE'|'WORK'|'HOME'
            },
        ],
        'SipAddresses': [
            {
                'Uri': 'string',
                'Type': 'WORK'
            },
        ]
    }
}


Response Structure

(dict) --
Contact (dict) --The details of the requested contact.

ContactArn (string) --The ARN of the contact.

DisplayName (string) --The name of the contact to display on the console.

FirstName (string) --The first name of the contact, used to call the contact on the device.

LastName (string) --The last name of the contact, used to call the contact on the device.

PhoneNumber (string) --The phone number of the contact. The phone number type defaults to WORK. You can either specify PhoneNumber or PhoneNumbers. We recommend that you use PhoneNumbers, which lets you specify the phone number type and multiple numbers.

PhoneNumbers (list) --The list of phone numbers for the contact.

(dict) --The phone number for the contact containing the raw number and phone number type.

Number (string) --The raw value of the phone number.

Type (string) --The type of the phone number.





SipAddresses (list) --The list of SIP addresses for the contact.

(dict) --The SIP address for the contact containing the URI and SIP address type.

Uri (string) --The URI for the SIP address.

Type (string) --The type of the SIP address.












Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException


    :return: {
        'Contact': {
            'ContactArn': 'string',
            'DisplayName': 'string',
            'FirstName': 'string',
            'LastName': 'string',
            'PhoneNumber': 'string',
            'PhoneNumbers': [
                {
                    'Number': 'string',
                    'Type': 'MOBILE'|'WORK'|'HOME'
                },
            ],
            'SipAddresses': [
                {
                    'Uri': 'string',
                    'Type': 'WORK'
                },
            ]
        }
    }
    
    
    """
    pass

def get_device(DeviceArn=None):
    """
    Gets the details of a device by device ARN.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_device(
        DeviceArn='string'
    )
    
    
    :type DeviceArn: string
    :param DeviceArn: The ARN of the device for which to request details. Required.

    :rtype: dict
ReturnsResponse Syntax{
    'Device': {
        'DeviceArn': 'string',
        'DeviceSerialNumber': 'string',
        'DeviceType': 'string',
        'DeviceName': 'string',
        'SoftwareVersion': 'string',
        'MacAddress': 'string',
        'RoomArn': 'string',
        'DeviceStatus': 'READY'|'PENDING'|'WAS_OFFLINE'|'DEREGISTERED'|'FAILED',
        'DeviceStatusInfo': {
            'DeviceStatusDetails': [
                {
                    'Feature': 'BLUETOOTH'|'VOLUME'|'NOTIFICATIONS'|'LISTS'|'SKILLS'|'NETWORK_PROFILE'|'SETTINGS'|'ALL',
                    'Code': 'DEVICE_SOFTWARE_UPDATE_NEEDED'|'DEVICE_WAS_OFFLINE'|'CREDENTIALS_ACCESS_FAILURE'|'TLS_VERSION_MISMATCH'|'ASSOCIATION_REJECTION'|'AUTHENTICATION_FAILURE'|'DHCP_FAILURE'|'INTERNET_UNAVAILABLE'|'DNS_FAILURE'|'UNKNOWN_FAILURE'|'CERTIFICATE_ISSUING_LIMIT_EXCEEDED'|'INVALID_CERTIFICATE_AUTHORITY'|'NETWORK_PROFILE_NOT_FOUND'|'INVALID_PASSWORD_STATE'|'PASSWORD_NOT_FOUND'
                },
            ],
            'ConnectionStatus': 'ONLINE'|'OFFLINE',
            'ConnectionStatusUpdatedTime': datetime(2015, 1, 1)
        },
        'NetworkProfileInfo': {
            'NetworkProfileArn': 'string',
            'CertificateArn': 'string',
            'CertificateExpirationTime': datetime(2015, 1, 1)
        }
    }
}


Response Structure

(dict) --
Device (dict) --The details of the device requested. Required.

DeviceArn (string) --The ARN of a device.

DeviceSerialNumber (string) --The serial number of a device.

DeviceType (string) --The type of a device.

DeviceName (string) --The name of a device.

SoftwareVersion (string) --The software version of a device.

MacAddress (string) --The MAC address of a device.

RoomArn (string) --The room ARN of a device.

DeviceStatus (string) --The status of a device. If the status is not READY, check the DeviceStatusInfo value for details.

DeviceStatusInfo (dict) --Detailed information about a device\'s status.

DeviceStatusDetails (list) --One or more device status detail descriptions.

(dict) --Details of a device\xe2\x80\x99s status.

Feature (string) --The list of available features on the device.

Code (string) --The device status detail code.





ConnectionStatus (string) --The latest available information about the connection status of a device.

ConnectionStatusUpdatedTime (datetime) --The time (in epoch) when the device connection status changed.



NetworkProfileInfo (dict) --Detailed information about a device\'s network profile.

NetworkProfileArn (string) --The ARN of the network profile associated with a device.

CertificateArn (string) --The ARN of the certificate associated with a device.

CertificateExpirationTime (datetime) --The time (in epoch) when the certificate expires.










Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException


    :return: {
        'Device': {
            'DeviceArn': 'string',
            'DeviceSerialNumber': 'string',
            'DeviceType': 'string',
            'DeviceName': 'string',
            'SoftwareVersion': 'string',
            'MacAddress': 'string',
            'RoomArn': 'string',
            'DeviceStatus': 'READY'|'PENDING'|'WAS_OFFLINE'|'DEREGISTERED'|'FAILED',
            'DeviceStatusInfo': {
                'DeviceStatusDetails': [
                    {
                        'Feature': 'BLUETOOTH'|'VOLUME'|'NOTIFICATIONS'|'LISTS'|'SKILLS'|'NETWORK_PROFILE'|'SETTINGS'|'ALL',
                        'Code': 'DEVICE_SOFTWARE_UPDATE_NEEDED'|'DEVICE_WAS_OFFLINE'|'CREDENTIALS_ACCESS_FAILURE'|'TLS_VERSION_MISMATCH'|'ASSOCIATION_REJECTION'|'AUTHENTICATION_FAILURE'|'DHCP_FAILURE'|'INTERNET_UNAVAILABLE'|'DNS_FAILURE'|'UNKNOWN_FAILURE'|'CERTIFICATE_ISSUING_LIMIT_EXCEEDED'|'INVALID_CERTIFICATE_AUTHORITY'|'NETWORK_PROFILE_NOT_FOUND'|'INVALID_PASSWORD_STATE'|'PASSWORD_NOT_FOUND'
                    },
                ],
                'ConnectionStatus': 'ONLINE'|'OFFLINE',
                'ConnectionStatusUpdatedTime': datetime(2015, 1, 1)
            },
            'NetworkProfileInfo': {
                'NetworkProfileArn': 'string',
                'CertificateArn': 'string',
                'CertificateExpirationTime': datetime(2015, 1, 1)
            }
        }
    }
    
    
    """
    pass

def get_gateway(GatewayArn=None):
    """
    Retrieves the details of a gateway.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_gateway(
        GatewayArn='string'
    )
    
    
    :type GatewayArn: string
    :param GatewayArn: [REQUIRED]\nThe ARN of the gateway to get.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Gateway': {
        'Arn': 'string',
        'Name': 'string',
        'Description': 'string',
        'GatewayGroupArn': 'string',
        'SoftwareVersion': 'string'
    }
}


Response Structure

(dict) --
Gateway (dict) --The details of the gateway.

Arn (string) --The ARN of the gateway.

Name (string) --The name of the gateway.

Description (string) --The description of the gateway.

GatewayGroupArn (string) --The ARN of the gateway group that the gateway is associated to.

SoftwareVersion (string) --The software version of the gateway. The gateway automatically updates its software version during normal operation.








Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException


    :return: {
        'Gateway': {
            'Arn': 'string',
            'Name': 'string',
            'Description': 'string',
            'GatewayGroupArn': 'string',
            'SoftwareVersion': 'string'
        }
    }
    
    
    """
    pass

def get_gateway_group(GatewayGroupArn=None):
    """
    Retrieves the details of a gateway group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_gateway_group(
        GatewayGroupArn='string'
    )
    
    
    :type GatewayGroupArn: string
    :param GatewayGroupArn: [REQUIRED]\nThe ARN of the gateway group to get.\n

    :rtype: dict
ReturnsResponse Syntax{
    'GatewayGroup': {
        'Arn': 'string',
        'Name': 'string',
        'Description': 'string'
    }
}


Response Structure

(dict) --
GatewayGroup (dict) --The details of the gateway group.

Arn (string) --The ARN of the gateway group.

Name (string) --The name of the gateway group.

Description (string) --The description of the gateway group.








Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException


    :return: {
        'GatewayGroup': {
            'Arn': 'string',
            'Name': 'string',
            'Description': 'string'
        }
    }
    
    
    """
    pass

def get_invitation_configuration():
    """
    Retrieves the configured values for the user enrollment invitation email template.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_invitation_configuration()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'OrganizationName': 'string',
    'ContactEmail': 'string',
    'PrivateSkillIds': [
        'string',
    ]
}


Response Structure

(dict) --
OrganizationName (string) --The name of the organization sending the enrollment invite to a user.

ContactEmail (string) --The email ID of the organization or individual contact that the enrolled user can use.

PrivateSkillIds (list) --The list of private skill IDs that you want to recommend to the user to enable in the invitation.

(string) --







Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException


    :return: {
        'OrganizationName': 'string',
        'ContactEmail': 'string',
        'PrivateSkillIds': [
            'string',
        ]
    }
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.NotFoundException
    
    """
    pass

def get_network_profile(NetworkProfileArn=None):
    """
    Gets the network profile details by the network profile ARN.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_network_profile(
        NetworkProfileArn='string'
    )
    
    
    :type NetworkProfileArn: string
    :param NetworkProfileArn: [REQUIRED]\nThe ARN of the network profile associated with a device.\n

    :rtype: dict
ReturnsResponse Syntax{
    'NetworkProfile': {
        'NetworkProfileArn': 'string',
        'NetworkProfileName': 'string',
        'Description': 'string',
        'Ssid': 'string',
        'SecurityType': 'OPEN'|'WEP'|'WPA_PSK'|'WPA2_PSK'|'WPA2_ENTERPRISE',
        'EapMethod': 'EAP_TLS',
        'CurrentPassword': 'string',
        'NextPassword': 'string',
        'CertificateAuthorityArn': 'string',
        'TrustAnchors': [
            'string',
        ]
    }
}


Response Structure

(dict) --
NetworkProfile (dict) --The network profile associated with a device.

NetworkProfileArn (string) --The ARN of the network profile associated with a device.

NetworkProfileName (string) --The name of the network profile associated with a device.

Description (string) --Detailed information about a device\'s network profile.

Ssid (string) --The SSID of the Wi-Fi network.

SecurityType (string) --The security type of the Wi-Fi network. This can be WPA2_ENTERPRISE, WPA2_PSK, WPA_PSK, WEP, or OPEN.

EapMethod (string) --The authentication standard that is used in the EAP framework. Currently, EAP_TLS is supported.

CurrentPassword (string) --The current password of the Wi-Fi network.

NextPassword (string) --The next, or subsequent, password of the Wi-Fi network. This password is asynchronously transmitted to the device and is used when the password of the network changes to NextPassword.

CertificateAuthorityArn (string) --The ARN of the Private Certificate Authority (PCA) created in AWS Certificate Manager (ACM). This is used to issue certificates to the devices.

TrustAnchors (list) --The root certificates of your authentication server, which is installed on your devices and used to trust your authentication server during EAP negotiation.

(string) --









Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException
AlexaForBusiness.Client.exceptions.InvalidSecretsManagerResourceException


    :return: {
        'NetworkProfile': {
            'NetworkProfileArn': 'string',
            'NetworkProfileName': 'string',
            'Description': 'string',
            'Ssid': 'string',
            'SecurityType': 'OPEN'|'WEP'|'WPA_PSK'|'WPA2_PSK'|'WPA2_ENTERPRISE',
            'EapMethod': 'EAP_TLS',
            'CurrentPassword': 'string',
            'NextPassword': 'string',
            'CertificateAuthorityArn': 'string',
            'TrustAnchors': [
                'string',
            ]
        }
    }
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.NotFoundException
    AlexaForBusiness.Client.exceptions.InvalidSecretsManagerResourceException
    
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

def get_profile(ProfileArn=None):
    """
    Gets the details of a room profile by profile ARN.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_profile(
        ProfileArn='string'
    )
    
    
    :type ProfileArn: string
    :param ProfileArn: The ARN of the room profile for which to request details. Required.

    :rtype: dict
ReturnsResponse Syntax{
    'Profile': {
        'ProfileArn': 'string',
        'ProfileName': 'string',
        'IsDefault': True|False,
        'Address': 'string',
        'Timezone': 'string',
        'DistanceUnit': 'METRIC'|'IMPERIAL',
        'TemperatureUnit': 'FAHRENHEIT'|'CELSIUS',
        'WakeWord': 'ALEXA'|'AMAZON'|'ECHO'|'COMPUTER',
        'Locale': 'string',
        'SetupModeDisabled': True|False,
        'MaxVolumeLimit': 123,
        'PSTNEnabled': True|False,
        'AddressBookArn': 'string',
        'MeetingRoomConfiguration': {
            'RoomUtilizationMetricsEnabled': True|False,
            'EndOfMeetingReminder': {
                'ReminderAtMinutes': [
                    123,
                ],
                'ReminderType': 'ANNOUNCEMENT_TIME_CHECK'|'ANNOUNCEMENT_VARIABLE_TIME_LEFT'|'CHIME'|'KNOCK',
                'Enabled': True|False
            },
            'InstantBooking': {
                'DurationInMinutes': 123,
                'Enabled': True|False
            },
            'RequireCheckIn': {
                'ReleaseAfterMinutes': 123,
                'Enabled': True|False
            }
        }
    }
}


Response Structure

(dict) --
Profile (dict) --The details of the room profile requested. Required.

ProfileArn (string) --The ARN of a room profile.

ProfileName (string) --The name of a room profile.

IsDefault (boolean) --Retrieves if the profile is default or not.

Address (string) --The address of a room profile.

Timezone (string) --The time zone of a room profile.

DistanceUnit (string) --The distance unit of a room profile.

TemperatureUnit (string) --The temperature unit of a room profile.

WakeWord (string) --The wake word of a room profile.

Locale (string) --The locale of a room profile. (This is currently available only to a limited preview audience.)

SetupModeDisabled (boolean) --The setup mode of a room profile.

MaxVolumeLimit (integer) --The max volume limit of a room profile.

PSTNEnabled (boolean) --The PSTN setting of a room profile.

AddressBookArn (string) --The ARN of the address book.

MeetingRoomConfiguration (dict) --Meeting room settings of a room profile.

RoomUtilizationMetricsEnabled (boolean) --Whether room utilization metrics are enabled or not.

EndOfMeetingReminder (dict) --Settings for the end of meeting reminder feature that are applied to a room profile. The end of meeting reminder enables Alexa to remind users when a meeting is ending.

ReminderAtMinutes (list) --A range of 3 to 15 minutes that determines when the reminder begins.

(integer) --


ReminderType (string) --The type of sound that users hear during the end of meeting reminder.

Enabled (boolean) --Whether an end of meeting reminder is enabled or not.



InstantBooking (dict) --Settings to automatically book the room if available for a configured duration when joining a meeting with Alexa.

DurationInMinutes (integer) --Duration between 15 and 240 minutes at increments of 15 that determines how long to book an available room when a meeting is started with Alexa.

Enabled (boolean) --Whether instant booking is enabled or not.



RequireCheckIn (dict) --Settings for requiring a check in when a room is reserved. Alexa can cancel a room reservation if it\'s not checked into. This makes the room available for others. Users can check in by joining the meeting with Alexa or an AVS device, or by saying \xe2\x80\x9cAlexa, check in.\xe2\x80\x9d

ReleaseAfterMinutes (integer) --Duration between 5 and 20 minutes to determine when to release the room if it\'s not checked into.

Enabled (boolean) --Whether require check in is enabled or not.












Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException


    :return: {
        'Profile': {
            'ProfileArn': 'string',
            'ProfileName': 'string',
            'IsDefault': True|False,
            'Address': 'string',
            'Timezone': 'string',
            'DistanceUnit': 'METRIC'|'IMPERIAL',
            'TemperatureUnit': 'FAHRENHEIT'|'CELSIUS',
            'WakeWord': 'ALEXA'|'AMAZON'|'ECHO'|'COMPUTER',
            'Locale': 'string',
            'SetupModeDisabled': True|False,
            'MaxVolumeLimit': 123,
            'PSTNEnabled': True|False,
            'AddressBookArn': 'string',
            'MeetingRoomConfiguration': {
                'RoomUtilizationMetricsEnabled': True|False,
                'EndOfMeetingReminder': {
                    'ReminderAtMinutes': [
                        123,
                    ],
                    'ReminderType': 'ANNOUNCEMENT_TIME_CHECK'|'ANNOUNCEMENT_VARIABLE_TIME_LEFT'|'CHIME'|'KNOCK',
                    'Enabled': True|False
                },
                'InstantBooking': {
                    'DurationInMinutes': 123,
                    'Enabled': True|False
                },
                'RequireCheckIn': {
                    'ReleaseAfterMinutes': 123,
                    'Enabled': True|False
                }
            }
        }
    }
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.NotFoundException
    
    """
    pass

def get_room(RoomArn=None):
    """
    Gets room details by room ARN.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_room(
        RoomArn='string'
    )
    
    
    :type RoomArn: string
    :param RoomArn: The ARN of the room for which to request details. Required.

    :rtype: dict
ReturnsResponse Syntax{
    'Room': {
        'RoomArn': 'string',
        'RoomName': 'string',
        'Description': 'string',
        'ProviderCalendarId': 'string',
        'ProfileArn': 'string'
    }
}


Response Structure

(dict) --
Room (dict) --The details of the room requested.

RoomArn (string) --The ARN of a room.

RoomName (string) --The name of a room.

Description (string) --The description of a room.

ProviderCalendarId (string) --The provider calendar ARN of a room.

ProfileArn (string) --The profile ARN of a room.








Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException


    :return: {
        'Room': {
            'RoomArn': 'string',
            'RoomName': 'string',
            'Description': 'string',
            'ProviderCalendarId': 'string',
            'ProfileArn': 'string'
        }
    }
    
    
    """
    pass

def get_room_skill_parameter(RoomArn=None, SkillId=None, ParameterKey=None):
    """
    Gets room skill parameter details by room, skill, and parameter key ARN.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_room_skill_parameter(
        RoomArn='string',
        SkillId='string',
        ParameterKey='string'
    )
    
    
    :type RoomArn: string
    :param RoomArn: The ARN of the room from which to get the room skill parameter details.

    :type SkillId: string
    :param SkillId: [REQUIRED]\nThe ARN of the skill from which to get the room skill parameter details. Required.\n

    :type ParameterKey: string
    :param ParameterKey: [REQUIRED]\nThe room skill parameter key for which to get details. Required.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'RoomSkillParameter': {
        'ParameterKey': 'string',
        'ParameterValue': 'string'
    }
}


Response Structure

(dict) --

RoomSkillParameter (dict) --
The details of the room skill parameter requested. Required.

ParameterKey (string) --
The parameter key of a room skill parameter. ParameterKey is an enumerated type that only takes \xe2\x80\x9cDEFAULT\xe2\x80\x9d or \xe2\x80\x9cSCOPE\xe2\x80\x9d as valid values.

ParameterValue (string) --
The parameter value of a room skill parameter.









Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException


    :return: {
        'RoomSkillParameter': {
            'ParameterKey': 'string',
            'ParameterValue': 'string'
        }
    }
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.NotFoundException
    
    """
    pass

def get_skill_group(SkillGroupArn=None):
    """
    Gets skill group details by skill group ARN.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_skill_group(
        SkillGroupArn='string'
    )
    
    
    :type SkillGroupArn: string
    :param SkillGroupArn: The ARN of the skill group for which to get details. Required.

    :rtype: dict
ReturnsResponse Syntax{
    'SkillGroup': {
        'SkillGroupArn': 'string',
        'SkillGroupName': 'string',
        'Description': 'string'
    }
}


Response Structure

(dict) --
SkillGroup (dict) --The details of the skill group requested. Required.

SkillGroupArn (string) --The ARN of a skill group.

SkillGroupName (string) --The name of a skill group.

Description (string) --The description of a skill group.








Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException


    :return: {
        'SkillGroup': {
            'SkillGroupArn': 'string',
            'SkillGroupName': 'string',
            'Description': 'string'
        }
    }
    
    
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

def list_business_report_schedules(NextToken=None, MaxResults=None):
    """
    Lists the details of the schedules that a user configured. A download URL of the report associated with each schedule is returned every time this action is called. A new download URL is returned each time, and is valid for 24 hours.
    See also: AWS API Documentation
    
    
    :example: response = client.list_business_report_schedules(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: The token used to list the remaining schedules from the previous API call.

    :type MaxResults: integer
    :param MaxResults: The maximum number of schedules listed in the call.

    :rtype: dict

ReturnsResponse Syntax
{
    'BusinessReportSchedules': [
        {
            'ScheduleArn': 'string',
            'ScheduleName': 'string',
            'S3BucketName': 'string',
            'S3KeyPrefix': 'string',
            'Format': 'CSV'|'CSV_ZIP',
            'ContentRange': {
                'Interval': 'ONE_DAY'|'ONE_WEEK'|'THIRTY_DAYS'
            },
            'Recurrence': {
                'StartDate': 'string'
            },
            'LastBusinessReport': {
                'Status': 'RUNNING'|'SUCCEEDED'|'FAILED',
                'FailureCode': 'ACCESS_DENIED'|'NO_SUCH_BUCKET'|'INTERNAL_FAILURE',
                'S3Location': {
                    'Path': 'string',
                    'BucketName': 'string'
                },
                'DeliveryTime': datetime(2015, 1, 1),
                'DownloadUrl': 'string'
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

BusinessReportSchedules (list) --
The schedule of the reports.

(dict) --
The schedule of the usage report.

ScheduleArn (string) --
The ARN of the business report schedule.

ScheduleName (string) --
The name identifier of the schedule.

S3BucketName (string) --
The S3 bucket name of the output reports.

S3KeyPrefix (string) --
The S3 key where the report is delivered.

Format (string) --
The format of the generated report (individual CSV files or zipped files of individual files).

ContentRange (dict) --
The content range of the reports.

Interval (string) --
The interval of the content range.



Recurrence (dict) --
The recurrence of the reports.

StartDate (string) --
The start date.



LastBusinessReport (dict) --
The details of the last business report delivery for a specified time interval.

Status (string) --
The status of the report generation execution (RUNNING, SUCCEEDED, or FAILED).

FailureCode (string) --
The failure code.

S3Location (dict) --
The S3 location of the output reports.

Path (string) --
The path of the business report.

BucketName (string) --
The S3 bucket name of the output reports.



DeliveryTime (datetime) --
The time of report delivery.

DownloadUrl (string) --
The download link where a user can download the report.







NextToken (string) --
The token used to list the remaining schedules from the previous API call.








    :return: {
        'BusinessReportSchedules': [
            {
                'ScheduleArn': 'string',
                'ScheduleName': 'string',
                'S3BucketName': 'string',
                'S3KeyPrefix': 'string',
                'Format': 'CSV'|'CSV_ZIP',
                'ContentRange': {
                    'Interval': 'ONE_DAY'|'ONE_WEEK'|'THIRTY_DAYS'
                },
                'Recurrence': {
                    'StartDate': 'string'
                },
                'LastBusinessReport': {
                    'Status': 'RUNNING'|'SUCCEEDED'|'FAILED',
                    'FailureCode': 'ACCESS_DENIED'|'NO_SUCH_BUCKET'|'INTERNAL_FAILURE',
                    'S3Location': {
                        'Path': 'string',
                        'BucketName': 'string'
                    },
                    'DeliveryTime': datetime(2015, 1, 1),
                    'DownloadUrl': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_conference_providers(NextToken=None, MaxResults=None):
    """
    Lists conference providers under a specific AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_conference_providers(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: The tokens used for pagination.

    :type MaxResults: integer
    :param MaxResults: The maximum number of conference providers to be returned, per paginated calls.

    :rtype: dict

ReturnsResponse Syntax
{
    'ConferenceProviders': [
        {
            'Arn': 'string',
            'Name': 'string',
            'Type': 'CHIME'|'BLUEJEANS'|'FUZE'|'GOOGLE_HANGOUTS'|'POLYCOM'|'RINGCENTRAL'|'SKYPE_FOR_BUSINESS'|'WEBEX'|'ZOOM'|'CUSTOM',
            'IPDialIn': {
                'Endpoint': 'string',
                'CommsProtocol': 'SIP'|'SIPS'|'H323'
            },
            'PSTNDialIn': {
                'CountryCode': 'string',
                'PhoneNumber': 'string',
                'OneClickIdDelay': 'string',
                'OneClickPinDelay': 'string'
            },
            'MeetingSetting': {
                'RequirePin': 'YES'|'NO'|'OPTIONAL'
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ConferenceProviders (list) --
The conference providers.

(dict) --
An entity that provides a conferencing solution. Alexa for Business acts as the voice interface and mediator that connects users to their preferred conference provider. Examples of conference providers include Amazon Chime, Zoom, Cisco, and Polycom.

Arn (string) --
The ARN of the newly created conference provider.

Name (string) --
The name of the conference provider.

Type (string) --
The type of conference providers.

IPDialIn (dict) --
The IP endpoint and protocol for calling.

Endpoint (string) --
The IP address.

CommsProtocol (string) --
The protocol, including SIP, SIPS, and H323.



PSTNDialIn (dict) --
The information for PSTN conferencing.

CountryCode (string) --
The zip code.

PhoneNumber (string) --
The phone number to call to join the conference.

OneClickIdDelay (string) --
The delay duration before Alexa enters the conference ID with dual-tone multi-frequency (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send data over the telephone network.

OneClickPinDelay (string) --
The delay duration before Alexa enters the conference pin with dual-tone multi-frequency (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send data over the telephone network.



MeetingSetting (dict) --
The meeting settings for the conference provider.

RequirePin (string) --
The values that indicate whether the pin is always required.







NextToken (string) --
The tokens used for pagination.








    :return: {
        'ConferenceProviders': [
            {
                'Arn': 'string',
                'Name': 'string',
                'Type': 'CHIME'|'BLUEJEANS'|'FUZE'|'GOOGLE_HANGOUTS'|'POLYCOM'|'RINGCENTRAL'|'SKYPE_FOR_BUSINESS'|'WEBEX'|'ZOOM'|'CUSTOM',
                'IPDialIn': {
                    'Endpoint': 'string',
                    'CommsProtocol': 'SIP'|'SIPS'|'H323'
                },
                'PSTNDialIn': {
                    'CountryCode': 'string',
                    'PhoneNumber': 'string',
                    'OneClickIdDelay': 'string',
                    'OneClickPinDelay': 'string'
                },
                'MeetingSetting': {
                    'RequirePin': 'YES'|'NO'|'OPTIONAL'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_device_events(DeviceArn=None, EventType=None, NextToken=None, MaxResults=None):
    """
    Lists the device event history, including device connection status, for up to 30 days.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_device_events(
        DeviceArn='string',
        EventType='CONNECTION_STATUS'|'DEVICE_STATUS',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type DeviceArn: string
    :param DeviceArn: [REQUIRED]\nThe ARN of a device.\n

    :type EventType: string
    :param EventType: The event type to filter device events. If EventType isn\'t specified, this returns a list of all device events in reverse chronological order. If EventType is specified, this returns a list of device events for that EventType in reverse chronological order.

    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response only includes results beyond the token, up to the value specified by MaxResults. When the end of results is reached, the response has a value of null.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to include in the response. The default value is 50. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.

    :rtype: dict

ReturnsResponse Syntax
{
    'DeviceEvents': [
        {
            'Type': 'CONNECTION_STATUS'|'DEVICE_STATUS',
            'Value': 'string',
            'Timestamp': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

DeviceEvents (list) --
The device events requested for the device ARN.

(dict) --
The list of device events.

Type (string) --
The type of device event.

Value (string) --
The value of the event.

Timestamp (datetime) --
The time (in epoch) when the event occurred.





NextToken (string) --
The token returned to indicate that there is more data available.







Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException


    :return: {
        'DeviceEvents': [
            {
                'Type': 'CONNECTION_STATUS'|'DEVICE_STATUS',
                'Value': 'string',
                'Timestamp': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.NotFoundException
    
    """
    pass

def list_gateway_groups(NextToken=None, MaxResults=None):
    """
    Retrieves a list of gateway group summaries. Use GetGatewayGroup to retrieve details of a specific gateway group.
    See also: AWS API Documentation
    
    
    :example: response = client.list_gateway_groups(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: The token used to paginate though multiple pages of gateway group summaries.

    :type MaxResults: integer
    :param MaxResults: The maximum number of gateway group summaries to return. The default is 50.

    :rtype: dict

ReturnsResponse Syntax
{
    'GatewayGroups': [
        {
            'Arn': 'string',
            'Name': 'string',
            'Description': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

GatewayGroups (list) --
The gateway groups in the list.

(dict) --
The summary of a gateway group.

Arn (string) --
The ARN of the gateway group.

Name (string) --
The name of the gateway group.

Description (string) --
The description of the gateway group.





NextToken (string) --
The token used to paginate though multiple pages of gateway group summaries.








    :return: {
        'GatewayGroups': [
            {
                'Arn': 'string',
                'Name': 'string',
                'Description': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_gateways(GatewayGroupArn=None, NextToken=None, MaxResults=None):
    """
    Retrieves a list of gateway summaries. Use GetGateway to retrieve details of a specific gateway. An optional gateway group ARN can be provided to only retrieve gateway summaries of gateways that are associated with that gateway group ARN.
    See also: AWS API Documentation
    
    
    :example: response = client.list_gateways(
        GatewayGroupArn='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type GatewayGroupArn: string
    :param GatewayGroupArn: The gateway group ARN for which to list gateways.

    :type NextToken: string
    :param NextToken: The token used to paginate though multiple pages of gateway summaries.

    :type MaxResults: integer
    :param MaxResults: The maximum number of gateway summaries to return. The default is 50.

    :rtype: dict

ReturnsResponse Syntax
{
    'Gateways': [
        {
            'Arn': 'string',
            'Name': 'string',
            'Description': 'string',
            'GatewayGroupArn': 'string',
            'SoftwareVersion': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Gateways (list) --
The gateways in the list.

(dict) --
The summary of a gateway.

Arn (string) --
The ARN of the gateway.

Name (string) --
The name of the gateway.

Description (string) --
The description of the gateway.

GatewayGroupArn (string) --
The ARN of the gateway group that the gateway is associated to.

SoftwareVersion (string) --
The software version of the gateway. The gateway automatically updates its software version during normal operation.





NextToken (string) --
The token used to paginate though multiple pages of gateway summaries.








    :return: {
        'Gateways': [
            {
                'Arn': 'string',
                'Name': 'string',
                'Description': 'string',
                'GatewayGroupArn': 'string',
                'SoftwareVersion': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_skills(SkillGroupArn=None, EnablementType=None, SkillType=None, NextToken=None, MaxResults=None):
    """
    Lists all enabled skills in a specific skill group.
    See also: AWS API Documentation
    
    
    :example: response = client.list_skills(
        SkillGroupArn='string',
        EnablementType='ENABLED'|'PENDING',
        SkillType='PUBLIC'|'PRIVATE'|'ALL',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type SkillGroupArn: string
    :param SkillGroupArn: The ARN of the skill group for which to list enabled skills.

    :type EnablementType: string
    :param EnablementType: Whether the skill is enabled under the user\'s account.

    :type SkillType: string
    :param SkillType: Whether the skill is publicly available or is a private skill.

    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults .

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.

    :rtype: dict

ReturnsResponse Syntax
{
    'SkillSummaries': [
        {
            'SkillId': 'string',
            'SkillName': 'string',
            'SupportsLinking': True|False,
            'EnablementType': 'ENABLED'|'PENDING',
            'SkillType': 'PUBLIC'|'PRIVATE'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

SkillSummaries (list) --
The list of enabled skills requested. Required.

(dict) --
The summary of skills.

SkillId (string) --
The ARN of the skill summary.

SkillName (string) --
The name of the skill.

SupportsLinking (boolean) --
Linking support for a skill.

EnablementType (string) --
Whether the skill is enabled under the user\'s account, or if it requires linking to be used.

SkillType (string) --
Whether the skill is publicly available or is a private skill.





NextToken (string) --
The token returned to indicate that there is more data available.








    :return: {
        'SkillSummaries': [
            {
                'SkillId': 'string',
                'SkillName': 'string',
                'SupportsLinking': True|False,
                'EnablementType': 'ENABLED'|'PENDING',
                'SkillType': 'PUBLIC'|'PRIVATE'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_skills_store_categories(NextToken=None, MaxResults=None):
    """
    Lists all categories in the Alexa skill store.
    See also: AWS API Documentation
    
    
    :example: response = client.list_skills_store_categories(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: The tokens used for pagination.

    :type MaxResults: integer
    :param MaxResults: The maximum number of categories returned, per paginated calls.

    :rtype: dict

ReturnsResponse Syntax
{
    'CategoryList': [
        {
            'CategoryId': 123,
            'CategoryName': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

CategoryList (list) --
The list of categories.

(dict) --
The skill store category that is shown. Alexa skills are assigned a specific skill category during creation, such as News, Social, and Sports.

CategoryId (integer) --
The ID of the skill store category.

CategoryName (string) --
The name of the skill store category.





NextToken (string) --
The tokens used for pagination.








    :return: {
        'CategoryList': [
            {
                'CategoryId': 123,
                'CategoryName': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_skills_store_skills_by_category(CategoryId=None, NextToken=None, MaxResults=None):
    """
    Lists all skills in the Alexa skill store by category.
    See also: AWS API Documentation
    
    
    :example: response = client.list_skills_store_skills_by_category(
        CategoryId=123,
        NextToken='string',
        MaxResults=123
    )
    
    
    :type CategoryId: integer
    :param CategoryId: [REQUIRED]\nThe category ID for which the skills are being retrieved from the skill store.\n

    :type NextToken: string
    :param NextToken: The tokens used for pagination.

    :type MaxResults: integer
    :param MaxResults: The maximum number of skills returned per paginated calls.

    :rtype: dict

ReturnsResponse Syntax
{
    'SkillsStoreSkills': [
        {
            'SkillId': 'string',
            'SkillName': 'string',
            'ShortDescription': 'string',
            'IconUrl': 'string',
            'SampleUtterances': [
                'string',
            ],
            'SkillDetails': {
                'ProductDescription': 'string',
                'InvocationPhrase': 'string',
                'ReleaseDate': 'string',
                'EndUserLicenseAgreement': 'string',
                'GenericKeywords': [
                    'string',
                ],
                'BulletPoints': [
                    'string',
                ],
                'NewInThisVersionBulletPoints': [
                    'string',
                ],
                'SkillTypes': [
                    'string',
                ],
                'Reviews': {
                    'string': 'string'
                },
                'DeveloperInfo': {
                    'DeveloperName': 'string',
                    'PrivacyPolicy': 'string',
                    'Email': 'string',
                    'Url': 'string'
                }
            },
            'SupportsLinking': True|False
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

SkillsStoreSkills (list) --
The skill store skills.

(dict) --
The detailed information about an Alexa skill.

SkillId (string) --
The ARN of the skill.

SkillName (string) --
The name of the skill.

ShortDescription (string) --
Short description about the skill.

IconUrl (string) --
The URL where the skill icon resides.

SampleUtterances (list) --
Sample utterances that interact with the skill.

(string) --


SkillDetails (dict) --
Information about the skill.

ProductDescription (string) --
The description of the product.

InvocationPhrase (string) --
The phrase used to trigger the skill.

ReleaseDate (string) --
The date when the skill was released.

EndUserLicenseAgreement (string) --
The URL of the end user license agreement.

GenericKeywords (list) --
The generic keywords associated with the skill that can be used to find a skill.

(string) --


BulletPoints (list) --
The details about what the skill supports organized as bullet points.

(string) --


NewInThisVersionBulletPoints (list) --
The updates added in bullet points.

(string) --


SkillTypes (list) --
The types of skills.

(string) --


Reviews (dict) --
The list of reviews for the skill, including Key and Value pair.

(string) --
(string) --




DeveloperInfo (dict) --
The details about the developer that published the skill.

DeveloperName (string) --
The name of the developer.

PrivacyPolicy (string) --
The URL of the privacy policy.

Email (string) --
The email of the developer.

Url (string) --
The website of the developer.





SupportsLinking (boolean) --
Linking support for a skill.





NextToken (string) --
The tokens used for pagination.








    :return: {
        'SkillsStoreSkills': [
            {
                'SkillId': 'string',
                'SkillName': 'string',
                'ShortDescription': 'string',
                'IconUrl': 'string',
                'SampleUtterances': [
                    'string',
                ],
                'SkillDetails': {
                    'ProductDescription': 'string',
                    'InvocationPhrase': 'string',
                    'ReleaseDate': 'string',
                    'EndUserLicenseAgreement': 'string',
                    'GenericKeywords': [
                        'string',
                    ],
                    'BulletPoints': [
                        'string',
                    ],
                    'NewInThisVersionBulletPoints': [
                        'string',
                    ],
                    'SkillTypes': [
                        'string',
                    ],
                    'Reviews': {
                        'string': 'string'
                    },
                    'DeveloperInfo': {
                        'DeveloperName': 'string',
                        'PrivacyPolicy': 'string',
                        'Email': 'string',
                        'Url': 'string'
                    }
                },
                'SupportsLinking': True|False
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_smart_home_appliances(RoomArn=None, MaxResults=None, NextToken=None):
    """
    Lists all of the smart home appliances associated with a room.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_smart_home_appliances(
        RoomArn='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type RoomArn: string
    :param RoomArn: [REQUIRED]\nThe room that the appliances are associated with.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of appliances to be returned, per paginated calls.

    :type NextToken: string
    :param NextToken: The tokens used for pagination.

    :rtype: dict

ReturnsResponse Syntax
{
    'SmartHomeAppliances': [
        {
            'FriendlyName': 'string',
            'Description': 'string',
            'ManufacturerName': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

SmartHomeAppliances (list) --
The smart home appliances.

(dict) --
A smart home appliance that can connect to a central system. Any domestic device can be a smart appliance.

FriendlyName (string) --
The friendly name of the smart home appliance.

Description (string) --
The description of the smart home appliance.

ManufacturerName (string) --
The name of the manufacturer of the smart home appliance.





NextToken (string) --
The tokens used for pagination.







Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException


    :return: {
        'SmartHomeAppliances': [
            {
                'FriendlyName': 'string',
                'Description': 'string',
                'ManufacturerName': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.NotFoundException
    
    """
    pass

def list_tags(Arn=None, NextToken=None, MaxResults=None):
    """
    Lists all tags for the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags(
        Arn='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Arn: string
    :param Arn: [REQUIRED]\nThe ARN of the specified resource for which to list tags.\n

    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults .

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.

    :rtype: dict

ReturnsResponse Syntax
{
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Tags (list) --
The tags requested for the specified resource.

(dict) --
A key-value pair that can be associated with a resource.

Key (string) --
The key of a tag. Tag keys are case-sensitive.

Value (string) --
The value of a tag. Tag values are case sensitive and can be null.





NextToken (string) --
The token returned to indicate that there is more data available.







Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException


    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.NotFoundException
    
    """
    pass

def put_conference_preference(ConferencePreference=None):
    """
    Sets the conference preferences on a specific conference provider at the account level.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_conference_preference(
        ConferencePreference={
            'DefaultConferenceProviderArn': 'string'
        }
    )
    
    
    :type ConferencePreference: dict
    :param ConferencePreference: [REQUIRED]\nThe conference preference of a specific conference provider.\n\nDefaultConferenceProviderArn (string) --The ARN of the default conference provider.\n\n\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException


    :return: {}
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.NotFoundException
    
    """
    pass

def put_invitation_configuration(OrganizationName=None, ContactEmail=None, PrivateSkillIds=None):
    """
    Configures the email template for the user enrollment invitation with the specified attributes.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_invitation_configuration(
        OrganizationName='string',
        ContactEmail='string',
        PrivateSkillIds=[
            'string',
        ]
    )
    
    
    :type OrganizationName: string
    :param OrganizationName: [REQUIRED]\nThe name of the organization sending the enrollment invite to a user.\n

    :type ContactEmail: string
    :param ContactEmail: The email ID of the organization or individual contact that the enrolled user can use.

    :type PrivateSkillIds: list
    :param PrivateSkillIds: The list of private skill IDs that you want to recommend to the user to enable in the invitation.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException
AlexaForBusiness.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def put_room_skill_parameter(RoomArn=None, SkillId=None, RoomSkillParameter=None):
    """
    Updates room skill parameter details by room, skill, and parameter key ID. Not all skills have a room skill parameter.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_room_skill_parameter(
        RoomArn='string',
        SkillId='string',
        RoomSkillParameter={
            'ParameterKey': 'string',
            'ParameterValue': 'string'
        }
    )
    
    
    :type RoomArn: string
    :param RoomArn: The ARN of the room associated with the room skill parameter. Required.

    :type SkillId: string
    :param SkillId: [REQUIRED]\nThe ARN of the skill associated with the room skill parameter. Required.\n

    :type RoomSkillParameter: dict
    :param RoomSkillParameter: [REQUIRED]\nThe updated room skill parameter. Required.\n\nParameterKey (string) -- [REQUIRED]The parameter key of a room skill parameter. ParameterKey is an enumerated type that only takes \xe2\x80\x9cDEFAULT\xe2\x80\x9d or \xe2\x80\x9cSCOPE\xe2\x80\x9d as valid values.\n\nParameterValue (string) -- [REQUIRED]The parameter value of a room skill parameter.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AlexaForBusiness.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def put_skill_authorization(AuthorizationResult=None, SkillId=None, RoomArn=None):
    """
    Links a user\'s account to a third-party skill provider. If this API operation is called by an assumed IAM role, the skill being linked must be a private skill. Also, the skill must be owned by the AWS account that assumed the IAM role.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_skill_authorization(
        AuthorizationResult={
            'string': 'string'
        },
        SkillId='string',
        RoomArn='string'
    )
    
    
    :type AuthorizationResult: dict
    :param AuthorizationResult: [REQUIRED]\nThe authorization result specific to OAUTH code grant output. 'Code\xe2\x80\x9d must be populated in the AuthorizationResult map to establish the authorization.\n\n(string) --\n(string) --\n\n\n\n

    :type SkillId: string
    :param SkillId: [REQUIRED]\nThe unique identifier of a skill.\n

    :type RoomArn: string
    :param RoomArn: The room that the skill is authorized for.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AlexaForBusiness.Client.exceptions.UnauthorizedException
AlexaForBusiness.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def register_avs_device(ClientId=None, UserCode=None, ProductId=None, DeviceSerialNumber=None, AmazonId=None):
    """
    Registers an Alexa-enabled device built by an Original Equipment Manufacturer (OEM) using Alexa Voice Service (AVS).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_avs_device(
        ClientId='string',
        UserCode='string',
        ProductId='string',
        DeviceSerialNumber='string',
        AmazonId='string'
    )
    
    
    :type ClientId: string
    :param ClientId: [REQUIRED]\nThe client ID of the OEM used for code-based linking authorization on an AVS device.\n

    :type UserCode: string
    :param UserCode: [REQUIRED]\nThe code that is obtained after your AVS device has made a POST request to LWA as a part of the Device Authorization Request component of the OAuth code-based linking specification.\n

    :type ProductId: string
    :param ProductId: [REQUIRED]\nThe product ID used to identify your AVS device during authorization.\n

    :type DeviceSerialNumber: string
    :param DeviceSerialNumber: [REQUIRED]\nThe key generated by the OEM that uniquely identifies a specified instance of your AVS device.\n

    :type AmazonId: string
    :param AmazonId: [REQUIRED]\nThe device type ID for your AVS device generated by Amazon when the OEM creates a new product on Amazon\'s Developer Console.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DeviceArn': 'string'
}


Response Structure

(dict) --

DeviceArn (string) --
The ARN of the device.







Exceptions

AlexaForBusiness.Client.exceptions.LimitExceededException
AlexaForBusiness.Client.exceptions.ConcurrentModificationException
AlexaForBusiness.Client.exceptions.InvalidDeviceException


    :return: {
        'DeviceArn': 'string'
    }
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.LimitExceededException
    AlexaForBusiness.Client.exceptions.ConcurrentModificationException
    AlexaForBusiness.Client.exceptions.InvalidDeviceException
    
    """
    pass

def reject_skill(SkillId=None):
    """
    Disassociates a skill from the organization under a user\'s AWS account. If the skill is a private skill, it moves to an AcceptStatus of PENDING. Any private or public skill that is rejected can be added later by calling the ApproveSkill API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.reject_skill(
        SkillId='string'
    )
    
    
    :type SkillId: string
    :param SkillId: [REQUIRED]\nThe unique identifier of the skill.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

AlexaForBusiness.Client.exceptions.ConcurrentModificationException
AlexaForBusiness.Client.exceptions.NotFoundException


    :return: {}
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.ConcurrentModificationException
    AlexaForBusiness.Client.exceptions.NotFoundException
    
    """
    pass

def resolve_room(UserId=None, SkillId=None):
    """
    Determines the details for the room from which a skill request was invoked. This operation is used by skill developers.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.resolve_room(
        UserId='string',
        SkillId='string'
    )
    
    
    :type UserId: string
    :param UserId: [REQUIRED]\nThe ARN of the user. Required.\n

    :type SkillId: string
    :param SkillId: [REQUIRED]\nThe ARN of the skill that was requested. Required.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'RoomArn': 'string',
    'RoomName': 'string',
    'RoomSkillParameters': [
        {
            'ParameterKey': 'string',
            'ParameterValue': 'string'
        },
    ]
}


Response Structure

(dict) --

RoomArn (string) --
The ARN of the room from which the skill request was invoked.

RoomName (string) --
The name of the room from which the skill request was invoked.

RoomSkillParameters (list) --
Response to get the room profile request. Required.

(dict) --
A skill parameter associated with a room.

ParameterKey (string) --
The parameter key of a room skill parameter. ParameterKey is an enumerated type that only takes \xe2\x80\x9cDEFAULT\xe2\x80\x9d or \xe2\x80\x9cSCOPE\xe2\x80\x9d as valid values.

ParameterValue (string) --
The parameter value of a room skill parameter.











Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException


    :return: {
        'RoomArn': 'string',
        'RoomName': 'string',
        'RoomSkillParameters': [
            {
                'ParameterKey': 'string',
                'ParameterValue': 'string'
            },
        ]
    }
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.NotFoundException
    
    """
    pass

def revoke_invitation(UserArn=None, EnrollmentId=None):
    """
    Revokes an invitation and invalidates the enrollment URL.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.revoke_invitation(
        UserArn='string',
        EnrollmentId='string'
    )
    
    
    :type UserArn: string
    :param UserArn: The ARN of the user for whom to revoke an enrollment invitation. Required.

    :type EnrollmentId: string
    :param EnrollmentId: The ARN of the enrollment invitation to revoke. Required.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException
AlexaForBusiness.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def search_address_books(Filters=None, SortCriteria=None, NextToken=None, MaxResults=None):
    """
    Searches address books and lists the ones that meet a set of filter and sort criteria.
    See also: AWS API Documentation
    
    
    :example: response = client.search_address_books(
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        SortCriteria=[
            {
                'Key': 'string',
                'Value': 'ASC'|'DESC'
            },
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filters: list
    :param Filters: The filters to use to list a specified set of address books. The supported filter key is AddressBookName.\n\n(dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria.\n\nKey (string) -- [REQUIRED]The key of a filter.\n\nValues (list) -- [REQUIRED]The values of a filter.\n\n(string) --\n\n\n\n\n\n

    :type SortCriteria: list
    :param SortCriteria: The sort order to use in listing the specified set of address books. The supported sort key is AddressBookName.\n\n(dict) --An object representing a sort criteria.\n\nKey (string) -- [REQUIRED]The sort key of a sort object.\n\nValue (string) -- [REQUIRED]The sort value of a sort object.\n\n\n\n\n

    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response only includes results beyond the token, up to the value specified by MaxResults.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.

    :rtype: dict

ReturnsResponse Syntax
{
    'AddressBooks': [
        {
            'AddressBookArn': 'string',
            'Name': 'string',
            'Description': 'string'
        },
    ],
    'NextToken': 'string',
    'TotalCount': 123
}


Response Structure

(dict) --

AddressBooks (list) --
The address books that meet the specified set of filter criteria, in sort order.

(dict) --
Information related to an address book.

AddressBookArn (string) --
The ARN of the address book.

Name (string) --
The name of the address book.

Description (string) --
The description of the address book.





NextToken (string) --
The token returned to indicate that there is more data available.

TotalCount (integer) --
The total number of address books returned.








    :return: {
        'AddressBooks': [
            {
                'AddressBookArn': 'string',
                'Name': 'string',
                'Description': 'string'
            },
        ],
        'NextToken': 'string',
        'TotalCount': 123
    }
    
    
    """
    pass

def search_contacts(Filters=None, SortCriteria=None, NextToken=None, MaxResults=None):
    """
    Searches contacts and lists the ones that meet a set of filter and sort criteria.
    See also: AWS API Documentation
    
    
    :example: response = client.search_contacts(
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        SortCriteria=[
            {
                'Key': 'string',
                'Value': 'ASC'|'DESC'
            },
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filters: list
    :param Filters: The filters to use to list a specified set of address books. The supported filter keys are DisplayName, FirstName, LastName, and AddressBookArns.\n\n(dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria.\n\nKey (string) -- [REQUIRED]The key of a filter.\n\nValues (list) -- [REQUIRED]The values of a filter.\n\n(string) --\n\n\n\n\n\n

    :type SortCriteria: list
    :param SortCriteria: The sort order to use in listing the specified set of contacts. The supported sort keys are DisplayName, FirstName, and LastName.\n\n(dict) --An object representing a sort criteria.\n\nKey (string) -- [REQUIRED]The sort key of a sort object.\n\nValue (string) -- [REQUIRED]The sort value of a sort object.\n\n\n\n\n

    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response only includes results beyond the token, up to the value specified by MaxResults.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.

    :rtype: dict

ReturnsResponse Syntax
{
    'Contacts': [
        {
            'ContactArn': 'string',
            'DisplayName': 'string',
            'FirstName': 'string',
            'LastName': 'string',
            'PhoneNumber': 'string',
            'PhoneNumbers': [
                {
                    'Number': 'string',
                    'Type': 'MOBILE'|'WORK'|'HOME'
                },
            ],
            'SipAddresses': [
                {
                    'Uri': 'string',
                    'Type': 'WORK'
                },
            ]
        },
    ],
    'NextToken': 'string',
    'TotalCount': 123
}


Response Structure

(dict) --

Contacts (list) --
The contacts that meet the specified set of filter criteria, in sort order.

(dict) --
Information related to a contact.

ContactArn (string) --
The ARN of the contact.

DisplayName (string) --
The name of the contact to display on the console.

FirstName (string) --
The first name of the contact, used to call the contact on the device.

LastName (string) --
The last name of the contact, used to call the contact on the device.

PhoneNumber (string) --
The phone number of the contact. The phone number type defaults to WORK. You can specify PhoneNumber or PhoneNumbers. We recommend that you use PhoneNumbers, which lets you specify the phone number type and multiple numbers.

PhoneNumbers (list) --
The list of phone numbers for the contact.

(dict) --
The phone number for the contact containing the raw number and phone number type.

Number (string) --
The raw value of the phone number.

Type (string) --
The type of the phone number.





SipAddresses (list) --
The list of SIP addresses for the contact.

(dict) --
The SIP address for the contact containing the URI and SIP address type.

Uri (string) --
The URI for the SIP address.

Type (string) --
The type of the SIP address.









NextToken (string) --
The token returned to indicate that there is more data available.

TotalCount (integer) --
The total number of contacts returned.








    :return: {
        'Contacts': [
            {
                'ContactArn': 'string',
                'DisplayName': 'string',
                'FirstName': 'string',
                'LastName': 'string',
                'PhoneNumber': 'string',
                'PhoneNumbers': [
                    {
                        'Number': 'string',
                        'Type': 'MOBILE'|'WORK'|'HOME'
                    },
                ],
                'SipAddresses': [
                    {
                        'Uri': 'string',
                        'Type': 'WORK'
                    },
                ]
            },
        ],
        'NextToken': 'string',
        'TotalCount': 123
    }
    
    
    """
    pass

def search_devices(NextToken=None, MaxResults=None, Filters=None, SortCriteria=None):
    """
    Searches devices and lists the ones that meet a set of filter criteria.
    See also: AWS API Documentation
    
    
    :example: response = client.search_devices(
        NextToken='string',
        MaxResults=123,
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        SortCriteria=[
            {
                'Key': 'string',
                'Value': 'ASC'|'DESC'
            },
        ]
    )
    
    
    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults .

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.

    :type Filters: list
    :param Filters: The filters to use to list a specified set of devices. Supported filter keys are DeviceName, DeviceStatus, DeviceStatusDetailCode, RoomName, DeviceType, DeviceSerialNumber, UnassociatedOnly, ConnectionStatus (ONLINE and OFFLINE), NetworkProfileName, NetworkProfileArn, Feature, and FailureCode.\n\n(dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria.\n\nKey (string) -- [REQUIRED]The key of a filter.\n\nValues (list) -- [REQUIRED]The values of a filter.\n\n(string) --\n\n\n\n\n\n

    :type SortCriteria: list
    :param SortCriteria: The sort order to use in listing the specified set of devices. Supported sort keys are DeviceName, DeviceStatus, RoomName, DeviceType, DeviceSerialNumber, ConnectionStatus, NetworkProfileName, NetworkProfileArn, Feature, and FailureCode.\n\n(dict) --An object representing a sort criteria.\n\nKey (string) -- [REQUIRED]The sort key of a sort object.\n\nValue (string) -- [REQUIRED]The sort value of a sort object.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Devices': [
        {
            'DeviceArn': 'string',
            'DeviceSerialNumber': 'string',
            'DeviceType': 'string',
            'DeviceName': 'string',
            'SoftwareVersion': 'string',
            'MacAddress': 'string',
            'DeviceStatus': 'READY'|'PENDING'|'WAS_OFFLINE'|'DEREGISTERED'|'FAILED',
            'NetworkProfileArn': 'string',
            'NetworkProfileName': 'string',
            'RoomArn': 'string',
            'RoomName': 'string',
            'DeviceStatusInfo': {
                'DeviceStatusDetails': [
                    {
                        'Feature': 'BLUETOOTH'|'VOLUME'|'NOTIFICATIONS'|'LISTS'|'SKILLS'|'NETWORK_PROFILE'|'SETTINGS'|'ALL',
                        'Code': 'DEVICE_SOFTWARE_UPDATE_NEEDED'|'DEVICE_WAS_OFFLINE'|'CREDENTIALS_ACCESS_FAILURE'|'TLS_VERSION_MISMATCH'|'ASSOCIATION_REJECTION'|'AUTHENTICATION_FAILURE'|'DHCP_FAILURE'|'INTERNET_UNAVAILABLE'|'DNS_FAILURE'|'UNKNOWN_FAILURE'|'CERTIFICATE_ISSUING_LIMIT_EXCEEDED'|'INVALID_CERTIFICATE_AUTHORITY'|'NETWORK_PROFILE_NOT_FOUND'|'INVALID_PASSWORD_STATE'|'PASSWORD_NOT_FOUND'
                    },
                ],
                'ConnectionStatus': 'ONLINE'|'OFFLINE',
                'ConnectionStatusUpdatedTime': datetime(2015, 1, 1)
            },
            'CreatedTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string',
    'TotalCount': 123
}


Response Structure

(dict) --

Devices (list) --
The devices that meet the specified set of filter criteria, in sort order.

(dict) --
Device attributes.

DeviceArn (string) --
The ARN of a device.

DeviceSerialNumber (string) --
The serial number of a device.

DeviceType (string) --
The type of a device.

DeviceName (string) --
The name of a device.

SoftwareVersion (string) --
The software version of a device.

MacAddress (string) --
The MAC address of a device.

DeviceStatus (string) --
The status of a device.

NetworkProfileArn (string) --
The ARN of the network profile associated with a device.

NetworkProfileName (string) --
The name of the network profile associated with a device.

RoomArn (string) --
The room ARN associated with a device.

RoomName (string) --
The name of the room associated with a device.

DeviceStatusInfo (dict) --
Detailed information about a device\'s status.

DeviceStatusDetails (list) --
One or more device status detail descriptions.

(dict) --
Details of a device\xe2\x80\x99s status.

Feature (string) --
The list of available features on the device.

Code (string) --
The device status detail code.





ConnectionStatus (string) --
The latest available information about the connection status of a device.

ConnectionStatusUpdatedTime (datetime) --
The time (in epoch) when the device connection status changed.



CreatedTime (datetime) --
The time (in epoch) when the device data was created.





NextToken (string) --
The token returned to indicate that there is more data available.

TotalCount (integer) --
The total number of devices returned.








    :return: {
        'Devices': [
            {
                'DeviceArn': 'string',
                'DeviceSerialNumber': 'string',
                'DeviceType': 'string',
                'DeviceName': 'string',
                'SoftwareVersion': 'string',
                'MacAddress': 'string',
                'DeviceStatus': 'READY'|'PENDING'|'WAS_OFFLINE'|'DEREGISTERED'|'FAILED',
                'NetworkProfileArn': 'string',
                'NetworkProfileName': 'string',
                'RoomArn': 'string',
                'RoomName': 'string',
                'DeviceStatusInfo': {
                    'DeviceStatusDetails': [
                        {
                            'Feature': 'BLUETOOTH'|'VOLUME'|'NOTIFICATIONS'|'LISTS'|'SKILLS'|'NETWORK_PROFILE'|'SETTINGS'|'ALL',
                            'Code': 'DEVICE_SOFTWARE_UPDATE_NEEDED'|'DEVICE_WAS_OFFLINE'|'CREDENTIALS_ACCESS_FAILURE'|'TLS_VERSION_MISMATCH'|'ASSOCIATION_REJECTION'|'AUTHENTICATION_FAILURE'|'DHCP_FAILURE'|'INTERNET_UNAVAILABLE'|'DNS_FAILURE'|'UNKNOWN_FAILURE'|'CERTIFICATE_ISSUING_LIMIT_EXCEEDED'|'INVALID_CERTIFICATE_AUTHORITY'|'NETWORK_PROFILE_NOT_FOUND'|'INVALID_PASSWORD_STATE'|'PASSWORD_NOT_FOUND'
                        },
                    ],
                    'ConnectionStatus': 'ONLINE'|'OFFLINE',
                    'ConnectionStatusUpdatedTime': datetime(2015, 1, 1)
                },
                'CreatedTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string',
        'TotalCount': 123
    }
    
    
    """
    pass

def search_network_profiles(NextToken=None, MaxResults=None, Filters=None, SortCriteria=None):
    """
    Searches network profiles and lists the ones that meet a set of filter and sort criteria.
    See also: AWS API Documentation
    
    
    :example: response = client.search_network_profiles(
        NextToken='string',
        MaxResults=123,
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        SortCriteria=[
            {
                'Key': 'string',
                'Value': 'ASC'|'DESC'
            },
        ]
    )
    
    
    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.

    :type Filters: list
    :param Filters: The filters to use to list a specified set of network profiles. Valid filters are NetworkProfileName, Ssid, and SecurityType.\n\n(dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria.\n\nKey (string) -- [REQUIRED]The key of a filter.\n\nValues (list) -- [REQUIRED]The values of a filter.\n\n(string) --\n\n\n\n\n\n

    :type SortCriteria: list
    :param SortCriteria: The sort order to use to list the specified set of network profiles. Valid sort criteria includes NetworkProfileName, Ssid, and SecurityType.\n\n(dict) --An object representing a sort criteria.\n\nKey (string) -- [REQUIRED]The sort key of a sort object.\n\nValue (string) -- [REQUIRED]The sort value of a sort object.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'NetworkProfiles': [
        {
            'NetworkProfileArn': 'string',
            'NetworkProfileName': 'string',
            'Description': 'string',
            'Ssid': 'string',
            'SecurityType': 'OPEN'|'WEP'|'WPA_PSK'|'WPA2_PSK'|'WPA2_ENTERPRISE',
            'EapMethod': 'EAP_TLS',
            'CertificateAuthorityArn': 'string'
        },
    ],
    'NextToken': 'string',
    'TotalCount': 123
}


Response Structure

(dict) --

NetworkProfiles (list) --
The network profiles that meet the specified set of filter criteria, in sort order. It is a list of NetworkProfileData objects.

(dict) --
The data associated with a network profile.

NetworkProfileArn (string) --
The ARN of the network profile associated with a device.

NetworkProfileName (string) --
The name of the network profile associated with a device.

Description (string) --
Detailed information about a device\'s network profile.

Ssid (string) --
The SSID of the Wi-Fi network.

SecurityType (string) --
The security type of the Wi-Fi network. This can be WPA2_ENTERPRISE, WPA2_PSK, WPA_PSK, WEP, or OPEN.

EapMethod (string) --
The authentication standard that is used in the EAP framework. Currently, EAP_TLS is supported.

CertificateAuthorityArn (string) --
The ARN of the Private Certificate Authority (PCA) created in AWS Certificate Manager (ACM). This is used to issue certificates to the devices.





NextToken (string) --
An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.

TotalCount (integer) --
The total number of network profiles returned.








    :return: {
        'NetworkProfiles': [
            {
                'NetworkProfileArn': 'string',
                'NetworkProfileName': 'string',
                'Description': 'string',
                'Ssid': 'string',
                'SecurityType': 'OPEN'|'WEP'|'WPA_PSK'|'WPA2_PSK'|'WPA2_ENTERPRISE',
                'EapMethod': 'EAP_TLS',
                'CertificateAuthorityArn': 'string'
            },
        ],
        'NextToken': 'string',
        'TotalCount': 123
    }
    
    
    """
    pass

def search_profiles(NextToken=None, MaxResults=None, Filters=None, SortCriteria=None):
    """
    Searches room profiles and lists the ones that meet a set of filter criteria.
    See also: AWS API Documentation
    
    
    :example: response = client.search_profiles(
        NextToken='string',
        MaxResults=123,
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        SortCriteria=[
            {
                'Key': 'string',
                'Value': 'ASC'|'DESC'
            },
        ]
    )
    
    
    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults .

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.

    :type Filters: list
    :param Filters: The filters to use to list a specified set of room profiles. Supported filter keys are ProfileName and Address. Required.\n\n(dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria.\n\nKey (string) -- [REQUIRED]The key of a filter.\n\nValues (list) -- [REQUIRED]The values of a filter.\n\n(string) --\n\n\n\n\n\n

    :type SortCriteria: list
    :param SortCriteria: The sort order to use in listing the specified set of room profiles. Supported sort keys are ProfileName and Address.\n\n(dict) --An object representing a sort criteria.\n\nKey (string) -- [REQUIRED]The sort key of a sort object.\n\nValue (string) -- [REQUIRED]The sort value of a sort object.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Profiles': [
        {
            'ProfileArn': 'string',
            'ProfileName': 'string',
            'IsDefault': True|False,
            'Address': 'string',
            'Timezone': 'string',
            'DistanceUnit': 'METRIC'|'IMPERIAL',
            'TemperatureUnit': 'FAHRENHEIT'|'CELSIUS',
            'WakeWord': 'ALEXA'|'AMAZON'|'ECHO'|'COMPUTER',
            'Locale': 'string'
        },
    ],
    'NextToken': 'string',
    'TotalCount': 123
}


Response Structure

(dict) --

Profiles (list) --
The profiles that meet the specified set of filter criteria, in sort order.

(dict) --
The data of a room profile.

ProfileArn (string) --
The ARN of a room profile.

ProfileName (string) --
The name of a room profile.

IsDefault (boolean) --
Retrieves if the profile data is default or not.

Address (string) --
The address of a room profile.

Timezone (string) --
The time zone of a room profile.

DistanceUnit (string) --
The distance unit of a room profile.

TemperatureUnit (string) --
The temperature unit of a room profile.

WakeWord (string) --
The wake word of a room profile.

Locale (string) --
The locale of a room profile. (This is currently available only to a limited preview audience.)





NextToken (string) --
The token returned to indicate that there is more data available.

TotalCount (integer) --
The total number of room profiles returned.








    :return: {
        'Profiles': [
            {
                'ProfileArn': 'string',
                'ProfileName': 'string',
                'IsDefault': True|False,
                'Address': 'string',
                'Timezone': 'string',
                'DistanceUnit': 'METRIC'|'IMPERIAL',
                'TemperatureUnit': 'FAHRENHEIT'|'CELSIUS',
                'WakeWord': 'ALEXA'|'AMAZON'|'ECHO'|'COMPUTER',
                'Locale': 'string'
            },
        ],
        'NextToken': 'string',
        'TotalCount': 123
    }
    
    
    """
    pass

def search_rooms(NextToken=None, MaxResults=None, Filters=None, SortCriteria=None):
    """
    Searches rooms and lists the ones that meet a set of filter and sort criteria.
    See also: AWS API Documentation
    
    
    :example: response = client.search_rooms(
        NextToken='string',
        MaxResults=123,
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        SortCriteria=[
            {
                'Key': 'string',
                'Value': 'ASC'|'DESC'
            },
        ]
    )
    
    
    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults .

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.

    :type Filters: list
    :param Filters: The filters to use to list a specified set of rooms. The supported filter keys are RoomName and ProfileName.\n\n(dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria.\n\nKey (string) -- [REQUIRED]The key of a filter.\n\nValues (list) -- [REQUIRED]The values of a filter.\n\n(string) --\n\n\n\n\n\n

    :type SortCriteria: list
    :param SortCriteria: The sort order to use in listing the specified set of rooms. The supported sort keys are RoomName and ProfileName.\n\n(dict) --An object representing a sort criteria.\n\nKey (string) -- [REQUIRED]The sort key of a sort object.\n\nValue (string) -- [REQUIRED]The sort value of a sort object.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Rooms': [
        {
            'RoomArn': 'string',
            'RoomName': 'string',
            'Description': 'string',
            'ProviderCalendarId': 'string',
            'ProfileArn': 'string',
            'ProfileName': 'string'
        },
    ],
    'NextToken': 'string',
    'TotalCount': 123
}


Response Structure

(dict) --

Rooms (list) --
The rooms that meet the specified set of filter criteria, in sort order.

(dict) --
The data of a room.

RoomArn (string) --
The ARN of a room.

RoomName (string) --
The name of a room.

Description (string) --
The description of a room.

ProviderCalendarId (string) --
The provider calendar ARN of a room.

ProfileArn (string) --
The profile ARN of a room.

ProfileName (string) --
The profile name of a room.





NextToken (string) --
The token returned to indicate that there is more data available.

TotalCount (integer) --
The total number of rooms returned.








    :return: {
        'Rooms': [
            {
                'RoomArn': 'string',
                'RoomName': 'string',
                'Description': 'string',
                'ProviderCalendarId': 'string',
                'ProfileArn': 'string',
                'ProfileName': 'string'
            },
        ],
        'NextToken': 'string',
        'TotalCount': 123
    }
    
    
    """
    pass

def search_skill_groups(NextToken=None, MaxResults=None, Filters=None, SortCriteria=None):
    """
    Searches skill groups and lists the ones that meet a set of filter and sort criteria.
    See also: AWS API Documentation
    
    
    :example: response = client.search_skill_groups(
        NextToken='string',
        MaxResults=123,
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        SortCriteria=[
            {
                'Key': 'string',
                'Value': 'ASC'|'DESC'
            },
        ]
    )
    
    
    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults . Required.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.

    :type Filters: list
    :param Filters: The filters to use to list a specified set of skill groups. The supported filter key is SkillGroupName.\n\n(dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria.\n\nKey (string) -- [REQUIRED]The key of a filter.\n\nValues (list) -- [REQUIRED]The values of a filter.\n\n(string) --\n\n\n\n\n\n

    :type SortCriteria: list
    :param SortCriteria: The sort order to use in listing the specified set of skill groups. The supported sort key is SkillGroupName.\n\n(dict) --An object representing a sort criteria.\n\nKey (string) -- [REQUIRED]The sort key of a sort object.\n\nValue (string) -- [REQUIRED]The sort value of a sort object.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'SkillGroups': [
        {
            'SkillGroupArn': 'string',
            'SkillGroupName': 'string',
            'Description': 'string'
        },
    ],
    'NextToken': 'string',
    'TotalCount': 123
}


Response Structure

(dict) --

SkillGroups (list) --
The skill groups that meet the filter criteria, in sort order.

(dict) --
The attributes of a skill group.

SkillGroupArn (string) --
The skill group ARN of a skill group.

SkillGroupName (string) --
The skill group name of a skill group.

Description (string) --
The description of a skill group.





NextToken (string) --
The token returned to indicate that there is more data available.

TotalCount (integer) --
The total number of skill groups returned.








    :return: {
        'SkillGroups': [
            {
                'SkillGroupArn': 'string',
                'SkillGroupName': 'string',
                'Description': 'string'
            },
        ],
        'NextToken': 'string',
        'TotalCount': 123
    }
    
    
    """
    pass

def search_users(NextToken=None, MaxResults=None, Filters=None, SortCriteria=None):
    """
    Searches users and lists the ones that meet a set of filter and sort criteria.
    See also: AWS API Documentation
    
    
    :example: response = client.search_users(
        NextToken='string',
        MaxResults=123,
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        SortCriteria=[
            {
                'Key': 'string',
                'Value': 'ASC'|'DESC'
            },
        ]
    )
    
    
    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults . Required.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved. Required.

    :type Filters: list
    :param Filters: The filters to use for listing a specific set of users. Required. Supported filter keys are UserId, FirstName, LastName, Email, and EnrollmentStatus.\n\n(dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria.\n\nKey (string) -- [REQUIRED]The key of a filter.\n\nValues (list) -- [REQUIRED]The values of a filter.\n\n(string) --\n\n\n\n\n\n

    :type SortCriteria: list
    :param SortCriteria: The sort order to use in listing the filtered set of users. Required. Supported sort keys are UserId, FirstName, LastName, Email, and EnrollmentStatus.\n\n(dict) --An object representing a sort criteria.\n\nKey (string) -- [REQUIRED]The sort key of a sort object.\n\nValue (string) -- [REQUIRED]The sort value of a sort object.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Users': [
        {
            'UserArn': 'string',
            'FirstName': 'string',
            'LastName': 'string',
            'Email': 'string',
            'EnrollmentStatus': 'INITIALIZED'|'PENDING'|'REGISTERED'|'DISASSOCIATING'|'DEREGISTERING',
            'EnrollmentId': 'string'
        },
    ],
    'NextToken': 'string',
    'TotalCount': 123
}


Response Structure

(dict) --

Users (list) --
The users that meet the specified set of filter criteria, in sort order.

(dict) --
Information related to a user.

UserArn (string) --
The ARN of a user.

FirstName (string) --
The first name of a user.

LastName (string) --
The last name of a user.

Email (string) --
The email of a user.

EnrollmentStatus (string) --
The enrollment status of a user.

EnrollmentId (string) --
The enrollment ARN of a user.





NextToken (string) --
The token returned to indicate that there is more data available.

TotalCount (integer) --
The total number of users returned.








    :return: {
        'Users': [
            {
                'UserArn': 'string',
                'FirstName': 'string',
                'LastName': 'string',
                'Email': 'string',
                'EnrollmentStatus': 'INITIALIZED'|'PENDING'|'REGISTERED'|'DISASSOCIATING'|'DEREGISTERING',
                'EnrollmentId': 'string'
            },
        ],
        'NextToken': 'string',
        'TotalCount': 123
    }
    
    
    """
    pass

def send_announcement(RoomFilters=None, Content=None, TimeToLiveInSeconds=None, ClientRequestToken=None):
    """
    Triggers an asynchronous flow to send text, SSML, or audio announcements to rooms that are identified by a search or filter.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.send_announcement(
        RoomFilters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        Content={
            'TextList': [
                {
                    'Locale': 'en-US',
                    'Value': 'string'
                },
            ],
            'SsmlList': [
                {
                    'Locale': 'en-US',
                    'Value': 'string'
                },
            ],
            'AudioList': [
                {
                    'Locale': 'en-US',
                    'Location': 'string'
                },
            ]
        },
        TimeToLiveInSeconds=123,
        ClientRequestToken='string'
    )
    
    
    :type RoomFilters: list
    :param RoomFilters: [REQUIRED]\nThe filters to use to send an announcement to a specified list of rooms. The supported filter keys are RoomName, ProfileName, RoomArn, and ProfileArn. To send to all rooms, specify an empty RoomFilters list.\n\n(dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria.\n\nKey (string) -- [REQUIRED]The key of a filter.\n\nValues (list) -- [REQUIRED]The values of a filter.\n\n(string) --\n\n\n\n\n\n

    :type Content: dict
    :param Content: [REQUIRED]\nThe announcement content. This can contain only one of the three possible announcement types (text, SSML or audio).\n\nTextList (list) --The list of text messages.\n\n(dict) --The text message.\n\nLocale (string) -- [REQUIRED]The locale of the text message. Currently, en-US is supported.\n\nValue (string) -- [REQUIRED]The value of the text message.\n\n\n\n\n\nSsmlList (list) --The list of SSML messages.\n\n(dict) --The SSML message. For more information, see SSML Reference .\n\nLocale (string) -- [REQUIRED]The locale of the SSML message. Currently, en-US is supported.\n\nValue (string) -- [REQUIRED]The value of the SSML message in the correct SSML format. The audio tag is not supported.\n\n\n\n\n\nAudioList (list) --The list of audio messages.\n\n(dict) --The audio message. There is a 1 MB limit on the audio file input and the only supported format is MP3. To convert your MP3 audio files to an Alexa-friendly,\nrequired codec version (MPEG version 2) and bit rate (48 kbps), you might use converter software. One option for this is a command-line tool, FFmpeg. For more information, see FFmpeg . The following command converts the provided <input-file> to an MP3 file that is played in the announcement:\n\nffmpeg -i <input-file> -ac 2 -codec:a libmp3lame -b:a 48k -ar 16000 <output-file.mp3>\n\nLocale (string) -- [REQUIRED]The locale of the audio message. Currently, en-US is supported.\n\nLocation (string) -- [REQUIRED]The location of the audio file. Currently, S3 URLs are supported. Only S3 locations comprised of safe characters are valid. For more information, see Safe Characters .\n\n\n\n\n\n\n

    :type TimeToLiveInSeconds: integer
    :param TimeToLiveInSeconds: The time to live for an announcement. Default is 300. If delivery doesn\'t occur within this time, the announcement is not delivered.

    :type ClientRequestToken: string
    :param ClientRequestToken: [REQUIRED]\nThe unique, user-specified identifier for the request that ensures idempotency.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AnnouncementArn': 'string'
}


Response Structure

(dict) --

AnnouncementArn (string) --
The identifier of the announcement.







Exceptions

AlexaForBusiness.Client.exceptions.LimitExceededException
AlexaForBusiness.Client.exceptions.AlreadyExistsException


    :return: {
        'AnnouncementArn': 'string'
    }
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.LimitExceededException
    AlexaForBusiness.Client.exceptions.AlreadyExistsException
    
    """
    pass

def send_invitation(UserArn=None):
    """
    Sends an enrollment invitation email with a URL to a user. The URL is valid for 30 days or until you call this operation again, whichever comes first.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.send_invitation(
        UserArn='string'
    )
    
    
    :type UserArn: string
    :param UserArn: The ARN of the user to whom to send an invitation. Required.

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException
AlexaForBusiness.Client.exceptions.InvalidUserStatusException
AlexaForBusiness.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.NotFoundException
    AlexaForBusiness.Client.exceptions.InvalidUserStatusException
    AlexaForBusiness.Client.exceptions.ConcurrentModificationException
    
    """
    pass

def start_device_sync(RoomArn=None, DeviceArn=None, Features=None):
    """
    Resets a device and its account to the known default settings. This clears all information and settings set by previous users in the following ways:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_device_sync(
        RoomArn='string',
        DeviceArn='string',
        Features=[
            'BLUETOOTH'|'VOLUME'|'NOTIFICATIONS'|'LISTS'|'SKILLS'|'NETWORK_PROFILE'|'SETTINGS'|'ALL',
        ]
    )
    
    
    :type RoomArn: string
    :param RoomArn: The ARN of the room with which the device to sync is associated. Required.

    :type DeviceArn: string
    :param DeviceArn: The ARN of the device to sync. Required.

    :type Features: list
    :param Features: [REQUIRED]\nRequest structure to start the device sync. Required.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AlexaForBusiness.Client.exceptions.DeviceNotRegisteredException


    :return: {}
    
    
    :returns: 
    RoomArn (string) -- The ARN of the room with which the device to sync is associated. Required.
    DeviceArn (string) -- The ARN of the device to sync. Required.
    Features (list) -- [REQUIRED]
    Request structure to start the device sync. Required.
    
    (string) --
    
    
    
    """
    pass

def start_smart_home_appliance_discovery(RoomArn=None):
    """
    Initiates the discovery of any smart home appliances associated with the room.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_smart_home_appliance_discovery(
        RoomArn='string'
    )
    
    
    :type RoomArn: string
    :param RoomArn: [REQUIRED]\nThe room where smart home appliance discovery was initiated.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException


    :return: {}
    
    
    :returns: 
    AlexaForBusiness.Client.exceptions.NotFoundException
    
    """
    pass

def tag_resource(Arn=None, Tags=None):
    """
    Adds metadata tags to a specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        Arn='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Arn: string
    :param Arn: [REQUIRED]\nThe ARN of the resource to which to add metadata tags. Required.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nThe tags to be added to the specified resource. Do not provide system tags. Required.\n\n(dict) --A key-value pair that can be associated with a resource.\n\nKey (string) -- [REQUIRED]The key of a tag. Tag keys are case-sensitive.\n\nValue (string) -- [REQUIRED]The value of a tag. Tag values are case sensitive and can be null.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(Arn=None, TagKeys=None):
    """
    Removes metadata tags from a specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        Arn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type Arn: string
    :param Arn: [REQUIRED]\nThe ARN of the resource from which to remove metadata tags. Required.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe tags to be removed from the specified resource. Do not provide system tags. Required.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_address_book(AddressBookArn=None, Name=None, Description=None):
    """
    Updates address book details by the address book ARN.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_address_book(
        AddressBookArn='string',
        Name='string',
        Description='string'
    )
    
    
    :type AddressBookArn: string
    :param AddressBookArn: [REQUIRED]\nThe ARN of the room to update.\n

    :type Name: string
    :param Name: The updated name of the room.

    :type Description: string
    :param Description: The updated description of the room.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException
AlexaForBusiness.Client.exceptions.NameInUseException
AlexaForBusiness.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_business_report_schedule(ScheduleArn=None, S3BucketName=None, S3KeyPrefix=None, Format=None, ScheduleName=None, Recurrence=None):
    """
    Updates the configuration of the report delivery schedule with the specified schedule ARN.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_business_report_schedule(
        ScheduleArn='string',
        S3BucketName='string',
        S3KeyPrefix='string',
        Format='CSV'|'CSV_ZIP',
        ScheduleName='string',
        Recurrence={
            'StartDate': 'string'
        }
    )
    
    
    :type ScheduleArn: string
    :param ScheduleArn: [REQUIRED]\nThe ARN of the business report schedule.\n

    :type S3BucketName: string
    :param S3BucketName: The S3 location of the output reports.

    :type S3KeyPrefix: string
    :param S3KeyPrefix: The S3 key where the report is delivered.

    :type Format: string
    :param Format: The format of the generated report (individual CSV files or zipped files of individual files).

    :type ScheduleName: string
    :param ScheduleName: The name identifier of the schedule.

    :type Recurrence: dict
    :param Recurrence: The recurrence of the reports.\n\nStartDate (string) --The start date.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException
AlexaForBusiness.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_conference_provider(ConferenceProviderArn=None, ConferenceProviderType=None, IPDialIn=None, PSTNDialIn=None, MeetingSetting=None):
    """
    Updates an existing conference provider\'s settings.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_conference_provider(
        ConferenceProviderArn='string',
        ConferenceProviderType='CHIME'|'BLUEJEANS'|'FUZE'|'GOOGLE_HANGOUTS'|'POLYCOM'|'RINGCENTRAL'|'SKYPE_FOR_BUSINESS'|'WEBEX'|'ZOOM'|'CUSTOM',
        IPDialIn={
            'Endpoint': 'string',
            'CommsProtocol': 'SIP'|'SIPS'|'H323'
        },
        PSTNDialIn={
            'CountryCode': 'string',
            'PhoneNumber': 'string',
            'OneClickIdDelay': 'string',
            'OneClickPinDelay': 'string'
        },
        MeetingSetting={
            'RequirePin': 'YES'|'NO'|'OPTIONAL'
        }
    )
    
    
    :type ConferenceProviderArn: string
    :param ConferenceProviderArn: [REQUIRED]\nThe ARN of the conference provider.\n

    :type ConferenceProviderType: string
    :param ConferenceProviderType: [REQUIRED]\nThe type of the conference provider.\n

    :type IPDialIn: dict
    :param IPDialIn: The IP endpoint and protocol for calling.\n\nEndpoint (string) -- [REQUIRED]The IP address.\n\nCommsProtocol (string) -- [REQUIRED]The protocol, including SIP, SIPS, and H323.\n\n\n

    :type PSTNDialIn: dict
    :param PSTNDialIn: The information for PSTN conferencing.\n\nCountryCode (string) -- [REQUIRED]The zip code.\n\nPhoneNumber (string) -- [REQUIRED]The phone number to call to join the conference.\n\nOneClickIdDelay (string) -- [REQUIRED]The delay duration before Alexa enters the conference ID with dual-tone multi-frequency (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send data over the telephone network.\n\nOneClickPinDelay (string) -- [REQUIRED]The delay duration before Alexa enters the conference pin with dual-tone multi-frequency (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send data over the telephone network.\n\n\n

    :type MeetingSetting: dict
    :param MeetingSetting: [REQUIRED]\nThe meeting settings for the conference provider.\n\nRequirePin (string) -- [REQUIRED]The values that indicate whether the pin is always required.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_contact(ContactArn=None, DisplayName=None, FirstName=None, LastName=None, PhoneNumber=None, PhoneNumbers=None, SipAddresses=None):
    """
    Updates the contact details by the contact ARN.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_contact(
        ContactArn='string',
        DisplayName='string',
        FirstName='string',
        LastName='string',
        PhoneNumber='string',
        PhoneNumbers=[
            {
                'Number': 'string',
                'Type': 'MOBILE'|'WORK'|'HOME'
            },
        ],
        SipAddresses=[
            {
                'Uri': 'string',
                'Type': 'WORK'
            },
        ]
    )
    
    
    :type ContactArn: string
    :param ContactArn: [REQUIRED]\nThe ARN of the contact to update.\n

    :type DisplayName: string
    :param DisplayName: The updated display name of the contact.

    :type FirstName: string
    :param FirstName: The updated first name of the contact.

    :type LastName: string
    :param LastName: The updated last name of the contact.

    :type PhoneNumber: string
    :param PhoneNumber: The updated phone number of the contact. The phone number type defaults to WORK. You can either specify PhoneNumber or PhoneNumbers. We recommend that you use PhoneNumbers, which lets you specify the phone number type and multiple numbers.

    :type PhoneNumbers: list
    :param PhoneNumbers: The list of phone numbers for the contact.\n\n(dict) --The phone number for the contact containing the raw number and phone number type.\n\nNumber (string) -- [REQUIRED]The raw value of the phone number.\n\nType (string) -- [REQUIRED]The type of the phone number.\n\n\n\n\n

    :type SipAddresses: list
    :param SipAddresses: The list of SIP addresses for the contact.\n\n(dict) --The SIP address for the contact containing the URI and SIP address type.\n\nUri (string) -- [REQUIRED]The URI for the SIP address.\n\nType (string) -- [REQUIRED]The type of the SIP address.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException
AlexaForBusiness.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_device(DeviceArn=None, DeviceName=None):
    """
    Updates the device name by device ARN.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_device(
        DeviceArn='string',
        DeviceName='string'
    )
    
    
    :type DeviceArn: string
    :param DeviceArn: The ARN of the device to update. Required.

    :type DeviceName: string
    :param DeviceName: The updated device name. Required.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException
AlexaForBusiness.Client.exceptions.ConcurrentModificationException
AlexaForBusiness.Client.exceptions.DeviceNotRegisteredException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_gateway(GatewayArn=None, Name=None, Description=None, SoftwareVersion=None):
    """
    Updates the details of a gateway. If any optional field is not provided, the existing corresponding value is left unmodified.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_gateway(
        GatewayArn='string',
        Name='string',
        Description='string',
        SoftwareVersion='string'
    )
    
    
    :type GatewayArn: string
    :param GatewayArn: [REQUIRED]\nThe ARN of the gateway to update.\n

    :type Name: string
    :param Name: The updated name of the gateway.

    :type Description: string
    :param Description: The updated description of the gateway.

    :type SoftwareVersion: string
    :param SoftwareVersion: The updated software version of the gateway. The gateway automatically updates its software version during normal operation.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException
AlexaForBusiness.Client.exceptions.NameInUseException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_gateway_group(GatewayGroupArn=None, Name=None, Description=None):
    """
    Updates the details of a gateway group. If any optional field is not provided, the existing corresponding value is left unmodified.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_gateway_group(
        GatewayGroupArn='string',
        Name='string',
        Description='string'
    )
    
    
    :type GatewayGroupArn: string
    :param GatewayGroupArn: [REQUIRED]\nThe ARN of the gateway group to update.\n

    :type Name: string
    :param Name: The updated name of the gateway group.

    :type Description: string
    :param Description: The updated description of the gateway group.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException
AlexaForBusiness.Client.exceptions.NameInUseException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_network_profile(NetworkProfileArn=None, NetworkProfileName=None, Description=None, CurrentPassword=None, NextPassword=None, CertificateAuthorityArn=None, TrustAnchors=None):
    """
    Updates a network profile by the network profile ARN.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_network_profile(
        NetworkProfileArn='string',
        NetworkProfileName='string',
        Description='string',
        CurrentPassword='string',
        NextPassword='string',
        CertificateAuthorityArn='string',
        TrustAnchors=[
            'string',
        ]
    )
    
    
    :type NetworkProfileArn: string
    :param NetworkProfileArn: [REQUIRED]\nThe ARN of the network profile associated with a device.\n

    :type NetworkProfileName: string
    :param NetworkProfileName: The name of the network profile associated with a device.

    :type Description: string
    :param Description: Detailed information about a device\'s network profile.

    :type CurrentPassword: string
    :param CurrentPassword: The current password of the Wi-Fi network.

    :type NextPassword: string
    :param NextPassword: The next, or subsequent, password of the Wi-Fi network. This password is asynchronously transmitted to the device and is used when the password of the network changes to NextPassword.

    :type CertificateAuthorityArn: string
    :param CertificateAuthorityArn: The ARN of the Private Certificate Authority (PCA) created in AWS Certificate Manager (ACM). This is used to issue certificates to the devices.

    :type TrustAnchors: list
    :param TrustAnchors: The root certificate(s) of your authentication server that will be installed on your devices and used to trust your authentication server during EAP negotiation.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException
AlexaForBusiness.Client.exceptions.NameInUseException
AlexaForBusiness.Client.exceptions.ConcurrentModificationException
AlexaForBusiness.Client.exceptions.InvalidCertificateAuthorityException
AlexaForBusiness.Client.exceptions.InvalidSecretsManagerResourceException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_profile(ProfileArn=None, ProfileName=None, IsDefault=None, Timezone=None, Address=None, DistanceUnit=None, TemperatureUnit=None, WakeWord=None, Locale=None, SetupModeDisabled=None, MaxVolumeLimit=None, PSTNEnabled=None, MeetingRoomConfiguration=None):
    """
    Updates an existing room profile by room profile ARN.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_profile(
        ProfileArn='string',
        ProfileName='string',
        IsDefault=True|False,
        Timezone='string',
        Address='string',
        DistanceUnit='METRIC'|'IMPERIAL',
        TemperatureUnit='FAHRENHEIT'|'CELSIUS',
        WakeWord='ALEXA'|'AMAZON'|'ECHO'|'COMPUTER',
        Locale='string',
        SetupModeDisabled=True|False,
        MaxVolumeLimit=123,
        PSTNEnabled=True|False,
        MeetingRoomConfiguration={
            'RoomUtilizationMetricsEnabled': True|False,
            'EndOfMeetingReminder': {
                'ReminderAtMinutes': [
                    123,
                ],
                'ReminderType': 'ANNOUNCEMENT_TIME_CHECK'|'ANNOUNCEMENT_VARIABLE_TIME_LEFT'|'CHIME'|'KNOCK',
                'Enabled': True|False
            },
            'InstantBooking': {
                'DurationInMinutes': 123,
                'Enabled': True|False
            },
            'RequireCheckIn': {
                'ReleaseAfterMinutes': 123,
                'Enabled': True|False
            }
        }
    )
    
    
    :type ProfileArn: string
    :param ProfileArn: The ARN of the room profile to update. Required.

    :type ProfileName: string
    :param ProfileName: The updated name for the room profile.

    :type IsDefault: boolean
    :param IsDefault: Sets the profile as default if selected. If this is missing, no update is done to the default status.

    :type Timezone: string
    :param Timezone: The updated timezone for the room profile.

    :type Address: string
    :param Address: The updated address for the room profile.

    :type DistanceUnit: string
    :param DistanceUnit: The updated distance unit for the room profile.

    :type TemperatureUnit: string
    :param TemperatureUnit: The updated temperature unit for the room profile.

    :type WakeWord: string
    :param WakeWord: The updated wake word for the room profile.

    :type Locale: string
    :param Locale: The updated locale for the room profile. (This is currently only available to a limited preview audience.)

    :type SetupModeDisabled: boolean
    :param SetupModeDisabled: Whether the setup mode of the profile is enabled.

    :type MaxVolumeLimit: integer
    :param MaxVolumeLimit: The updated maximum volume limit for the room profile.

    :type PSTNEnabled: boolean
    :param PSTNEnabled: Whether the PSTN setting of the room profile is enabled.

    :type MeetingRoomConfiguration: dict
    :param MeetingRoomConfiguration: The updated meeting room settings of a room profile.\n\nRoomUtilizationMetricsEnabled (boolean) --Whether room utilization metrics are enabled or not.\n\nEndOfMeetingReminder (dict) --Settings for the end of meeting reminder feature that are applied to a room profile. The end of meeting reminder enables Alexa to remind users when a meeting is ending.\n\nReminderAtMinutes (list) --Updates settings for the end of meeting reminder feature that are applied to a room profile. The end of meeting reminder enables Alexa to remind users when a meeting is ending.\n\n(integer) --\n\n\nReminderType (string) --The type of sound that users hear during the end of meeting reminder.\n\nEnabled (boolean) --Whether an end of meeting reminder is enabled or not.\n\n\n\nInstantBooking (dict) --Settings to automatically book an available room available for a configured duration when joining a meeting with Alexa.\n\nDurationInMinutes (integer) --Duration between 15 and 240 minutes at increments of 15 that determines how long to book an available room when a meeting is started with Alexa.\n\nEnabled (boolean) --Whether instant booking is enabled or not.\n\n\n\nRequireCheckIn (dict) --Settings for requiring a check in when a room is reserved. Alexa can cancel a room reservation if it\'s not checked into to make the room available for others. Users can check in by joining the meeting with Alexa or an AVS device, or by saying \xe2\x80\x9cAlexa, check in.\xe2\x80\x9d\n\nReleaseAfterMinutes (integer) --Duration between 5 and 20 minutes to determine when to release the room if it\'s not checked into.\n\nEnabled (boolean) --Whether require check in is enabled or not.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException
AlexaForBusiness.Client.exceptions.NameInUseException
AlexaForBusiness.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_room(RoomArn=None, RoomName=None, Description=None, ProviderCalendarId=None, ProfileArn=None):
    """
    Updates room details by room ARN.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_room(
        RoomArn='string',
        RoomName='string',
        Description='string',
        ProviderCalendarId='string',
        ProfileArn='string'
    )
    
    
    :type RoomArn: string
    :param RoomArn: The ARN of the room to update.

    :type RoomName: string
    :param RoomName: The updated name for the room.

    :type Description: string
    :param Description: The updated description for the room.

    :type ProviderCalendarId: string
    :param ProviderCalendarId: The updated provider calendar ARN for the room.

    :type ProfileArn: string
    :param ProfileArn: The updated profile ARN for the room.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException
AlexaForBusiness.Client.exceptions.NameInUseException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_skill_group(SkillGroupArn=None, SkillGroupName=None, Description=None):
    """
    Updates skill group details by skill group ARN.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_skill_group(
        SkillGroupArn='string',
        SkillGroupName='string',
        Description='string'
    )
    
    
    :type SkillGroupArn: string
    :param SkillGroupArn: The ARN of the skill group to update.

    :type SkillGroupName: string
    :param SkillGroupName: The updated name for the skill group.

    :type Description: string
    :param Description: The updated description for the skill group.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AlexaForBusiness.Client.exceptions.NotFoundException
AlexaForBusiness.Client.exceptions.NameInUseException
AlexaForBusiness.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

