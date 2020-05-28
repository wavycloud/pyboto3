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

def accept_invitation(DetectorId=None, MasterId=None, InvitationId=None):
    """
    Accepts the invitation to be monitored by a master GuardDuty account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.accept_invitation(
        DetectorId='string',
        MasterId='string',
        InvitationId='string'
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe unique ID of the detector of the GuardDuty member account.\n

    :type MasterId: string
    :param MasterId: [REQUIRED]\nThe account ID of the master GuardDuty account whose invitation you\'re accepting.\n

    :type InvitationId: string
    :param InvitationId: [REQUIRED]\nThe value that is used to validate the master account to the member account.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def archive_findings(DetectorId=None, FindingIds=None):
    """
    Archives GuardDuty findings that are specified by the list of finding IDs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.archive_findings(
        DetectorId='string',
        FindingIds=[
            'string',
        ]
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe ID of the detector that specifies the GuardDuty service whose findings you want to archive.\n

    :type FindingIds: list
    :param FindingIds: [REQUIRED]\nThe IDs of the findings that you want to archive.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_detector(Enable=None, ClientToken=None, FindingPublishingFrequency=None, Tags=None):
    """
    Creates a single Amazon GuardDuty detector. A detector is a resource that represents the GuardDuty service. To start using GuardDuty, you must create a detector in each Region where you enable the service. You can have only one detector per account per Region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_detector(
        Enable=True|False,
        ClientToken='string',
        FindingPublishingFrequency='FIFTEEN_MINUTES'|'ONE_HOUR'|'SIX_HOURS',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type Enable: boolean
    :param Enable: [REQUIRED]\nA Boolean value that specifies whether the detector is to be enabled.\n

    :type ClientToken: string
    :param ClientToken: The idempotency token for the create request.\nThis field is autopopulated if not provided.\n

    :type FindingPublishingFrequency: string
    :param FindingPublishingFrequency: An enum value that specifies how frequently updated findings are exported.

    :type Tags: dict
    :param Tags: The tags to be added to a new detector resource.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DetectorId': 'string'
}


Response Structure

(dict) --

DetectorId (string) --
The unique ID of the created detector.







Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'DetectorId': 'string'
    }
    
    
    :returns: 
    GuardDuty.Client.exceptions.BadRequestException
    GuardDuty.Client.exceptions.InternalServerErrorException
    
    """
    pass

def create_filter(DetectorId=None, Name=None, Description=None, Action=None, Rank=None, FindingCriteria=None, ClientToken=None, Tags=None):
    """
    Creates a filter using the specified finding criteria.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_filter(
        DetectorId='string',
        Name='string',
        Description='string',
        Action='NOOP'|'ARCHIVE',
        Rank=123,
        FindingCriteria={
            'Criterion': {
                'string': {
                    'Eq': [
                        'string',
                    ],
                    'Neq': [
                        'string',
                    ],
                    'Gt': 123,
                    'Gte': 123,
                    'Lt': 123,
                    'Lte': 123,
                    'Equals': [
                        'string',
                    ],
                    'NotEquals': [
                        'string',
                    ],
                    'GreaterThan': 123,
                    'GreaterThanOrEqual': 123,
                    'LessThan': 123,
                    'LessThanOrEqual': 123
                }
            }
        },
        ClientToken='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe unique ID of the detector of the GuardDuty account that you want to create a filter for.\n

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the filter.\n

    :type Description: string
    :param Description: The description of the filter.

    :type Action: string
    :param Action: Specifies the action that is to be applied to the findings that match the filter.

    :type Rank: integer
    :param Rank: Specifies the position of the filter in the list of current filters. Also specifies the order in which this filter is applied to the findings.

    :type FindingCriteria: dict
    :param FindingCriteria: [REQUIRED]\nRepresents the criteria to be used in the filter for querying findings.\nYou can only use the following attributes to query findings:\n\naccountId\nregion\nconfidence\nid\nresource.accessKeyDetails.accessKeyId\nresource.accessKeyDetails.principalId\nresource.accessKeyDetails.userName\nresource.accessKeyDetails.userType\nresource.instanceDetails.iamInstanceProfile.id\nresource.instanceDetails.imageId\nresource.instanceDetails.instanceId\nresource.instanceDetails.outpostArn\nresource.instanceDetails.networkInterfaces.ipv6Addresses\nresource.instanceDetails.networkInterfaces.privateIpAddresses.privateIpAddress\nresource.instanceDetails.networkInterfaces.publicDnsName\nresource.instanceDetails.networkInterfaces.publicIp\nresource.instanceDetails.networkInterfaces.securityGroups.groupId\nresource.instanceDetails.networkInterfaces.securityGroups.groupName\nresource.instanceDetails.networkInterfaces.subnetId\nresource.instanceDetails.networkInterfaces.vpcId\nresource.instanceDetails.tags.key\nresource.instanceDetails.tags.value\nresource.resourceType\nservice.action.actionType\nservice.action.awsApiCallAction.api\nservice.action.awsApiCallAction.callerType\nservice.action.awsApiCallAction.remoteIpDetails.city.cityName\nservice.action.awsApiCallAction.remoteIpDetails.country.countryName\nservice.action.awsApiCallAction.remoteIpDetails.ipAddressV4\nservice.action.awsApiCallAction.remoteIpDetails.organization.asn\nservice.action.awsApiCallAction.remoteIpDetails.organization.asnOrg\nservice.action.awsApiCallAction.serviceName\nservice.action.dnsRequestAction.domain\nservice.action.networkConnectionAction.blocked\nservice.action.networkConnectionAction.connectionDirection\nservice.action.networkConnectionAction.localPortDetails.port\nservice.action.networkConnectionAction.protocol\nservice.action.networkConnectionAction.localIpDetails.ipAddressV4\nservice.action.networkConnectionAction.remoteIpDetails.city.cityName\nservice.action.networkConnectionAction.remoteIpDetails.country.countryName\nservice.action.networkConnectionAction.remoteIpDetails.ipAddressV4\nservice.action.networkConnectionAction.remoteIpDetails.organization.asn\nservice.action.networkConnectionAction.remoteIpDetails.organization.asnOrg\nservice.action.networkConnectionAction.remotePortDetails.port\nservice.additionalInfo.threatListName\nservice.archived When this attribute is set to TRUE, only archived findings are listed. When it\'s set to FALSE, only unarchived findings are listed. When this attribute is not set, all existing findings are listed.\nservice.resourceRole\nseverity\ntype\nupdatedAt Type: ISO 8601 string format: YYYY-MM-DDTHH:MM:SS.SSSZ or YYYY-MM-DDTHH:MM:SSZ depending on whether the value contains milliseconds.\n\n\nCriterion (dict) --Represents a map of finding properties that match specified conditions and values when querying findings.\n\n(string) --\n(dict) --Contains information about the condition.\n\nEq (list) --Represents the equal condition to be applied to a single field when querying for findings.\n\n(string) --\n\n\nNeq (list) --Represents the not equal condition to be applied to a single field when querying for findings.\n\n(string) --\n\n\nGt (integer) --Represents a greater than condition to be applied to a single field when querying for findings.\n\nGte (integer) --Represents a greater than or equal condition to be applied to a single field when querying for findings.\n\nLt (integer) --Represents a less than condition to be applied to a single field when querying for findings.\n\nLte (integer) --Represents a less than or equal condition to be applied to a single field when querying for findings.\n\nEquals (list) --Represents an equal condition to be applied to a single field when querying for findings.\n\n(string) --\n\n\nNotEquals (list) --Represents a not equal condition to be applied to a single field when querying for findings.\n\n(string) --\n\n\nGreaterThan (integer) --Represents a greater than condition to be applied to a single field when querying for findings.\n\nGreaterThanOrEqual (integer) --Represents a greater than or equal condition to be applied to a single field when querying for findings.\n\nLessThan (integer) --Represents a less than condition to be applied to a single field when querying for findings.\n\nLessThanOrEqual (integer) --Represents a less than or equal condition to be applied to a single field when querying for findings.\n\n\n\n\n\n\n\n\n

    :type ClientToken: string
    :param ClientToken: The idempotency token for the create request.\nThis field is autopopulated if not provided.\n

    :type Tags: dict
    :param Tags: The tags to be added to a new filter resource.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Name': 'string'
}


Response Structure

(dict) --

Name (string) --
The name of the successfully created filter.







Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'Name': 'string'
    }
    
    
    :returns: 
    GuardDuty.Client.exceptions.BadRequestException
    GuardDuty.Client.exceptions.InternalServerErrorException
    
    """
    pass

def create_ip_set(DetectorId=None, Name=None, Format=None, Location=None, Activate=None, ClientToken=None, Tags=None):
    """
    Creates a new IPSet, which is called a trusted IP list in the console user interface. An IPSet is a list of IP addresses that are trusted for secure communication with AWS infrastructure and applications. GuardDuty doesn\'t generate findings for IP addresses that are included in IPSets. Only users from the master account can use this operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_ip_set(
        DetectorId='string',
        Name='string',
        Format='TXT'|'STIX'|'OTX_CSV'|'ALIEN_VAULT'|'PROOF_POINT'|'FIRE_EYE',
        Location='string',
        Activate=True|False,
        ClientToken='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe unique ID of the detector of the GuardDuty account that you want to create an IPSet for.\n

    :type Name: string
    :param Name: [REQUIRED]\nThe user-friendly name to identify the IPSet.\nAllowed characters are alphanumerics, spaces, hyphens (-), and underscores (_).\n

    :type Format: string
    :param Format: [REQUIRED]\nThe format of the file that contains the IPSet.\n

    :type Location: string
    :param Location: [REQUIRED]\nThe URI of the file that contains the IPSet.\n

    :type Activate: boolean
    :param Activate: [REQUIRED]\nA Boolean value that indicates whether GuardDuty is to start using the uploaded IPSet.\n

    :type ClientToken: string
    :param ClientToken: The idempotency token for the create request.\nThis field is autopopulated if not provided.\n

    :type Tags: dict
    :param Tags: The tags to be added to a new IP set resource.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'IpSetId': 'string'
}


Response Structure

(dict) --

IpSetId (string) --
The ID of the IPSet resource.







Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'IpSetId': 'string'
    }
    
    
    :returns: 
    GuardDuty.Client.exceptions.BadRequestException
    GuardDuty.Client.exceptions.InternalServerErrorException
    
    """
    pass

def create_members(DetectorId=None, AccountDetails=None):
    """
    Creates member accounts of the current AWS account by specifying a list of AWS account IDs. The current AWS account can then invite these members to manage GuardDuty in their accounts.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_members(
        DetectorId='string',
        AccountDetails=[
            {
                'AccountId': 'string',
                'Email': 'string'
            },
        ]
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe unique ID of the detector of the GuardDuty account that you want to associate member accounts with.\n

    :type AccountDetails: list
    :param AccountDetails: [REQUIRED]\nA list of account ID and email address pairs of the accounts that you want to associate with the master GuardDuty account.\n\n(dict) --Contains information about the account.\n\nAccountId (string) -- [REQUIRED]The member account ID.\n\nEmail (string) -- [REQUIRED]The email address of the member account.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'UnprocessedAccounts': [
        {
            'AccountId': 'string',
            'Result': 'string'
        },
    ]
}


Response Structure

(dict) --

UnprocessedAccounts (list) --
A list of objects that include the accountIds of the unprocessed accounts and a result string that explains why each was unprocessed.

(dict) --
Contains information about the accounts that weren\'t processed.

AccountId (string) --
The AWS account ID.

Result (string) --
A reason why the account hasn\'t been processed.











Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'UnprocessedAccounts': [
            {
                'AccountId': 'string',
                'Result': 'string'
            },
        ]
    }
    
    
    :returns: 
    GuardDuty.Client.exceptions.BadRequestException
    GuardDuty.Client.exceptions.InternalServerErrorException
    
    """
    pass

def create_publishing_destination(DetectorId=None, DestinationType=None, DestinationProperties=None, ClientToken=None):
    """
    Creates a publishing destination to export findings to. The resource to export findings to must exist before you use this operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_publishing_destination(
        DetectorId='string',
        DestinationType='S3',
        DestinationProperties={
            'DestinationArn': 'string',
            'KmsKeyArn': 'string'
        },
        ClientToken='string'
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe ID of the GuardDuty detector associated with the publishing destination.\n

    :type DestinationType: string
    :param DestinationType: [REQUIRED]\nThe type of resource for the publishing destination. Currently only Amazon S3 buckets are supported.\n

    :type DestinationProperties: dict
    :param DestinationProperties: [REQUIRED]\nThe properties of the publishing destination, including the ARNs for the destination and the KMS key used for encryption.\n\nDestinationArn (string) --The ARN of the resource to publish to.\n\nKmsKeyArn (string) --The ARN of the KMS key to use for encryption.\n\n\n

    :type ClientToken: string
    :param ClientToken: The idempotency token for the request.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DestinationId': 'string'
}


Response Structure

(dict) --

DestinationId (string) --
The ID of the publishing destination that is created.







Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'DestinationId': 'string'
    }
    
    
    :returns: 
    GuardDuty.Client.exceptions.BadRequestException
    GuardDuty.Client.exceptions.InternalServerErrorException
    
    """
    pass

def create_sample_findings(DetectorId=None, FindingTypes=None):
    """
    Generates example findings of types specified by the list of finding types. If \'NULL\' is specified for findingTypes , the API generates example findings of all supported finding types.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_sample_findings(
        DetectorId='string',
        FindingTypes=[
            'string',
        ]
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe ID of the detector to create sample findings for.\n

    :type FindingTypes: list
    :param FindingTypes: The types of sample findings to generate.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def create_threat_intel_set(DetectorId=None, Name=None, Format=None, Location=None, Activate=None, ClientToken=None, Tags=None):
    """
    Creates a new ThreatIntelSet. ThreatIntelSets consist of known malicious IP addresses. GuardDuty generates findings based on ThreatIntelSets. Only users of the master account can use this operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_threat_intel_set(
        DetectorId='string',
        Name='string',
        Format='TXT'|'STIX'|'OTX_CSV'|'ALIEN_VAULT'|'PROOF_POINT'|'FIRE_EYE',
        Location='string',
        Activate=True|False,
        ClientToken='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe unique ID of the detector of the GuardDuty account that you want to create a threatIntelSet for.\n

    :type Name: string
    :param Name: [REQUIRED]\nA user-friendly ThreatIntelSet name displayed in all findings that are generated by activity that involves IP addresses included in this ThreatIntelSet.\n

    :type Format: string
    :param Format: [REQUIRED]\nThe format of the file that contains the ThreatIntelSet.\n

    :type Location: string
    :param Location: [REQUIRED]\nThe URI of the file that contains the ThreatIntelSet.\n

    :type Activate: boolean
    :param Activate: [REQUIRED]\nA Boolean value that indicates whether GuardDuty is to start using the uploaded ThreatIntelSet.\n

    :type ClientToken: string
    :param ClientToken: The idempotency token for the create request.\nThis field is autopopulated if not provided.\n

    :type Tags: dict
    :param Tags: The tags to be added to a new threat list resource.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ThreatIntelSetId': 'string'
}


Response Structure

(dict) --

ThreatIntelSetId (string) --
The ID of the ThreatIntelSet resource.







Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'ThreatIntelSetId': 'string'
    }
    
    
    :returns: 
    GuardDuty.Client.exceptions.BadRequestException
    GuardDuty.Client.exceptions.InternalServerErrorException
    
    """
    pass

def decline_invitations(AccountIds=None):
    """
    Declines invitations sent to the current member account by AWS accounts specified by their account IDs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.decline_invitations(
        AccountIds=[
            'string',
        ]
    )
    
    
    :type AccountIds: list
    :param AccountIds: [REQUIRED]\nA list of account IDs of the AWS accounts that sent invitations to the current member account that you want to decline invitations from.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'UnprocessedAccounts': [
        {
            'AccountId': 'string',
            'Result': 'string'
        },
    ]
}


Response Structure

(dict) --
UnprocessedAccounts (list) --A list of objects that contain the unprocessed account and a result string that explains why it was unprocessed.

(dict) --Contains information about the accounts that weren\'t processed.

AccountId (string) --The AWS account ID.

Result (string) --A reason why the account hasn\'t been processed.










Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'UnprocessedAccounts': [
            {
                'AccountId': 'string',
                'Result': 'string'
            },
        ]
    }
    
    
    :returns: 
    GuardDuty.Client.exceptions.BadRequestException
    GuardDuty.Client.exceptions.InternalServerErrorException
    
    """
    pass

def delete_detector(DetectorId=None):
    """
    Deletes an Amazon GuardDuty detector that is specified by the detector ID.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_detector(
        DetectorId='string'
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe unique ID of the detector that you want to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {}
    
    
    :returns: 
    GuardDuty.Client.exceptions.BadRequestException
    GuardDuty.Client.exceptions.InternalServerErrorException
    
    """
    pass

def delete_filter(DetectorId=None, FilterName=None):
    """
    Deletes the filter specified by the filter name.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_filter(
        DetectorId='string',
        FilterName='string'
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe unique ID of the detector that the filter is associated with.\n

    :type FilterName: string
    :param FilterName: [REQUIRED]\nThe name of the filter that you want to delete.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_invitations(AccountIds=None):
    """
    Deletes invitations sent to the current member account by AWS accounts specified by their account IDs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_invitations(
        AccountIds=[
            'string',
        ]
    )
    
    
    :type AccountIds: list
    :param AccountIds: [REQUIRED]\nA list of account IDs of the AWS accounts that sent invitations to the current member account that you want to delete invitations from.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'UnprocessedAccounts': [
        {
            'AccountId': 'string',
            'Result': 'string'
        },
    ]
}


Response Structure

(dict) --
UnprocessedAccounts (list) --A list of objects that contain the unprocessed account and a result string that explains why it was unprocessed.

(dict) --Contains information about the accounts that weren\'t processed.

AccountId (string) --The AWS account ID.

Result (string) --A reason why the account hasn\'t been processed.










Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'UnprocessedAccounts': [
            {
                'AccountId': 'string',
                'Result': 'string'
            },
        ]
    }
    
    
    :returns: 
    GuardDuty.Client.exceptions.BadRequestException
    GuardDuty.Client.exceptions.InternalServerErrorException
    
    """
    pass

def delete_ip_set(DetectorId=None, IpSetId=None):
    """
    Deletes the IPSet specified by the ipSetId . IPSets are called trusted IP lists in the console user interface.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_ip_set(
        DetectorId='string',
        IpSetId='string'
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe unique ID of the detector associated with the IPSet.\n

    :type IpSetId: string
    :param IpSetId: [REQUIRED]\nThe unique ID of the IPSet to delete.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_members(DetectorId=None, AccountIds=None):
    """
    Deletes GuardDuty member accounts (to the current GuardDuty master account) specified by the account IDs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_members(
        DetectorId='string',
        AccountIds=[
            'string',
        ]
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe unique ID of the detector of the GuardDuty account whose members you want to delete.\n

    :type AccountIds: list
    :param AccountIds: [REQUIRED]\nA list of account IDs of the GuardDuty member accounts that you want to delete.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'UnprocessedAccounts': [
        {
            'AccountId': 'string',
            'Result': 'string'
        },
    ]
}


Response Structure

(dict) --

UnprocessedAccounts (list) --
The accounts that could not be processed.

(dict) --
Contains information about the accounts that weren\'t processed.

AccountId (string) --
The AWS account ID.

Result (string) --
A reason why the account hasn\'t been processed.











Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'UnprocessedAccounts': [
            {
                'AccountId': 'string',
                'Result': 'string'
            },
        ]
    }
    
    
    :returns: 
    GuardDuty.Client.exceptions.BadRequestException
    GuardDuty.Client.exceptions.InternalServerErrorException
    
    """
    pass

def delete_publishing_destination(DetectorId=None, DestinationId=None):
    """
    Deletes the publishing definition with the specified destinationId .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_publishing_destination(
        DetectorId='string',
        DestinationId='string'
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe unique ID of the detector associated with the publishing destination to delete.\n

    :type DestinationId: string
    :param DestinationId: [REQUIRED]\nThe ID of the publishing destination to delete.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_threat_intel_set(DetectorId=None, ThreatIntelSetId=None):
    """
    Deletes the ThreatIntelSet specified by the ThreatIntelSet ID.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_threat_intel_set(
        DetectorId='string',
        ThreatIntelSetId='string'
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe unique ID of the detector that the threatIntelSet is associated with.\n

    :type ThreatIntelSetId: string
    :param ThreatIntelSetId: [REQUIRED]\nThe unique ID of the threatIntelSet that you want to delete.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def describe_organization_configuration(DetectorId=None):
    """
    Returns information about the account selected as the delegated administrator for GuardDuty.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_organization_configuration(
        DetectorId='string'
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe ID of the detector to retrieve information about the delegated administrator from.\n

    :rtype: dict
ReturnsResponse Syntax{
    'AutoEnable': True|False,
    'MemberAccountLimitReached': True|False
}


Response Structure

(dict) --
AutoEnable (boolean) --Indicates whether GuardDuty is automatically enabled for accounts added to the organization.

MemberAccountLimitReached (boolean) --Indicates whether the maximum number of allowed member accounts are already associated with the delegated administrator master account.






Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'AutoEnable': True|False,
        'MemberAccountLimitReached': True|False
    }
    
    
    """
    pass

def describe_publishing_destination(DetectorId=None, DestinationId=None):
    """
    Returns information about the publishing destination specified by the provided destinationId .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_publishing_destination(
        DetectorId='string',
        DestinationId='string'
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe unique ID of the detector associated with the publishing destination to retrieve.\n

    :type DestinationId: string
    :param DestinationId: [REQUIRED]\nThe ID of the publishing destination to retrieve.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DestinationId': 'string',
    'DestinationType': 'S3',
    'Status': 'PENDING_VERIFICATION'|'PUBLISHING'|'UNABLE_TO_PUBLISH_FIX_DESTINATION_PROPERTY'|'STOPPED',
    'PublishingFailureStartTimestamp': 123,
    'DestinationProperties': {
        'DestinationArn': 'string',
        'KmsKeyArn': 'string'
    }
}


Response Structure

(dict) --

DestinationId (string) --
The ID of the publishing destination.

DestinationType (string) --
The type of publishing destination. Currently, only Amazon S3 buckets are supported.

Status (string) --
The status of the publishing destination.

PublishingFailureStartTimestamp (integer) --
The time, in epoch millisecond format, at which GuardDuty was first unable to publish findings to the destination.

DestinationProperties (dict) --
A DestinationProperties object that includes the DestinationArn and KmsKeyArn of the publishing destination.

DestinationArn (string) --
The ARN of the resource to publish to.

KmsKeyArn (string) --
The ARN of the KMS key to use for encryption.









Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'DestinationId': 'string',
        'DestinationType': 'S3',
        'Status': 'PENDING_VERIFICATION'|'PUBLISHING'|'UNABLE_TO_PUBLISH_FIX_DESTINATION_PROPERTY'|'STOPPED',
        'PublishingFailureStartTimestamp': 123,
        'DestinationProperties': {
            'DestinationArn': 'string',
            'KmsKeyArn': 'string'
        }
    }
    
    
    :returns: 
    GuardDuty.Client.exceptions.BadRequestException
    GuardDuty.Client.exceptions.InternalServerErrorException
    
    """
    pass

def disable_organization_admin_account(AdminAccountId=None):
    """
    Disables an AWS account within the Organization as the GuardDuty delegated administrator.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disable_organization_admin_account(
        AdminAccountId='string'
    )
    
    
    :type AdminAccountId: string
    :param AdminAccountId: [REQUIRED]\nThe AWS Account ID for the organizations account to be disabled as a GuardDuty delegated administrator.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {}
    
    
    :returns: 
    GuardDuty.Client.exceptions.BadRequestException
    GuardDuty.Client.exceptions.InternalServerErrorException
    
    """
    pass

def disassociate_from_master_account(DetectorId=None):
    """
    Disassociates the current GuardDuty member account from its master account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_from_master_account(
        DetectorId='string'
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe unique ID of the detector of the GuardDuty member account.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {}
    
    
    :returns: 
    GuardDuty.Client.exceptions.BadRequestException
    GuardDuty.Client.exceptions.InternalServerErrorException
    
    """
    pass

def disassociate_members(DetectorId=None, AccountIds=None):
    """
    Disassociates GuardDuty member accounts (to the current GuardDuty master account) specified by the account IDs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_members(
        DetectorId='string',
        AccountIds=[
            'string',
        ]
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe unique ID of the detector of the GuardDuty account whose members you want to disassociate from the master account.\n

    :type AccountIds: list
    :param AccountIds: [REQUIRED]\nA list of account IDs of the GuardDuty member accounts that you want to disassociate from the master account.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'UnprocessedAccounts': [
        {
            'AccountId': 'string',
            'Result': 'string'
        },
    ]
}


Response Structure

(dict) --

UnprocessedAccounts (list) --
A list of objects that contain the unprocessed account and a result string that explains why it was unprocessed.

(dict) --
Contains information about the accounts that weren\'t processed.

AccountId (string) --
The AWS account ID.

Result (string) --
A reason why the account hasn\'t been processed.











Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'UnprocessedAccounts': [
            {
                'AccountId': 'string',
                'Result': 'string'
            },
        ]
    }
    
    
    :returns: 
    GuardDuty.Client.exceptions.BadRequestException
    GuardDuty.Client.exceptions.InternalServerErrorException
    
    """
    pass

def enable_organization_admin_account(AdminAccountId=None):
    """
    Enables an AWS account within the organization as the GuardDuty delegated administrator.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.enable_organization_admin_account(
        AdminAccountId='string'
    )
    
    
    :type AdminAccountId: string
    :param AdminAccountId: [REQUIRED]\nThe AWS Account ID for the organization account to be enabled as a GuardDuty delegated administrator.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {}
    
    
    :returns: 
    GuardDuty.Client.exceptions.BadRequestException
    GuardDuty.Client.exceptions.InternalServerErrorException
    
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

def get_detector(DetectorId=None):
    """
    Retrieves an Amazon GuardDuty detector specified by the detectorId.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_detector(
        DetectorId='string'
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe unique ID of the detector that you want to get.\n

    :rtype: dict
ReturnsResponse Syntax{
    'CreatedAt': 'string',
    'FindingPublishingFrequency': 'FIFTEEN_MINUTES'|'ONE_HOUR'|'SIX_HOURS',
    'ServiceRole': 'string',
    'Status': 'ENABLED'|'DISABLED',
    'UpdatedAt': 'string',
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
CreatedAt (string) --The timestamp of when the detector was created.

FindingPublishingFrequency (string) --The publishing frequency of the finding.

ServiceRole (string) --The GuardDuty service role.

Status (string) --The detector status.

UpdatedAt (string) --The last-updated timestamp for the detector.

Tags (dict) --The tags of the detector resource.

(string) --
(string) --









Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'CreatedAt': 'string',
        'FindingPublishingFrequency': 'FIFTEEN_MINUTES'|'ONE_HOUR'|'SIX_HOURS',
        'ServiceRole': 'string',
        'Status': 'ENABLED'|'DISABLED',
        'UpdatedAt': 'string',
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    GuardDuty.Client.exceptions.BadRequestException
    GuardDuty.Client.exceptions.InternalServerErrorException
    
    """
    pass

def get_filter(DetectorId=None, FilterName=None):
    """
    Returns the details of the filter specified by the filter name.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_filter(
        DetectorId='string',
        FilterName='string'
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe unique ID of the detector that the filter is associated with.\n

    :type FilterName: string
    :param FilterName: [REQUIRED]\nThe name of the filter you want to get.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Name': 'string',
    'Description': 'string',
    'Action': 'NOOP'|'ARCHIVE',
    'Rank': 123,
    'FindingCriteria': {
        'Criterion': {
            'string': {
                'Eq': [
                    'string',
                ],
                'Neq': [
                    'string',
                ],
                'Gt': 123,
                'Gte': 123,
                'Lt': 123,
                'Lte': 123,
                'Equals': [
                    'string',
                ],
                'NotEquals': [
                    'string',
                ],
                'GreaterThan': 123,
                'GreaterThanOrEqual': 123,
                'LessThan': 123,
                'LessThanOrEqual': 123
            }
        }
    },
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --

Name (string) --
The name of the filter.

Description (string) --
The description of the filter.

Action (string) --
Specifies the action that is to be applied to the findings that match the filter.

Rank (integer) --
Specifies the position of the filter in the list of current filters. Also specifies the order in which this filter is applied to the findings.

FindingCriteria (dict) --
Represents the criteria to be used in the filter for querying findings.

Criterion (dict) --
Represents a map of finding properties that match specified conditions and values when querying findings.

(string) --

(dict) --
Contains information about the condition.

Eq (list) --
Represents the equal condition to be applied to a single field when querying for findings.

(string) --


Neq (list) --
Represents the not equal condition to be applied to a single field when querying for findings.

(string) --


Gt (integer) --
Represents a greater than condition to be applied to a single field when querying for findings.

Gte (integer) --
Represents a greater than or equal condition to be applied to a single field when querying for findings.

Lt (integer) --
Represents a less than condition to be applied to a single field when querying for findings.

Lte (integer) --
Represents a less than or equal condition to be applied to a single field when querying for findings.

Equals (list) --
Represents an equal  condition to be applied to a single field when querying for findings.

(string) --


NotEquals (list) --
Represents a not equal  condition to be applied to a single field when querying for findings.

(string) --


GreaterThan (integer) --
Represents a greater than condition to be applied to a single field when querying for findings.

GreaterThanOrEqual (integer) --
Represents a greater than or equal condition to be applied to a single field when querying for findings.

LessThan (integer) --
Represents a less than condition to be applied to a single field when querying for findings.

LessThanOrEqual (integer) --
Represents a less than or equal condition to be applied to a single field when querying for findings.









Tags (dict) --
The tags of the filter resource.

(string) --
(string) --










Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'Name': 'string',
        'Description': 'string',
        'Action': 'NOOP'|'ARCHIVE',
        'Rank': 123,
        'FindingCriteria': {
            'Criterion': {
                'string': {
                    'Eq': [
                        'string',
                    ],
                    'Neq': [
                        'string',
                    ],
                    'Gt': 123,
                    'Gte': 123,
                    'Lt': 123,
                    'Lte': 123,
                    'Equals': [
                        'string',
                    ],
                    'NotEquals': [
                        'string',
                    ],
                    'GreaterThan': 123,
                    'GreaterThanOrEqual': 123,
                    'LessThan': 123,
                    'LessThanOrEqual': 123
                }
            }
        },
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_findings(DetectorId=None, FindingIds=None, SortCriteria=None):
    """
    Describes Amazon GuardDuty findings specified by finding IDs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_findings(
        DetectorId='string',
        FindingIds=[
            'string',
        ],
        SortCriteria={
            'AttributeName': 'string',
            'OrderBy': 'ASC'|'DESC'
        }
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe ID of the detector that specifies the GuardDuty service whose findings you want to retrieve.\n

    :type FindingIds: list
    :param FindingIds: [REQUIRED]\nThe IDs of the findings that you want to retrieve.\n\n(string) --\n\n

    :type SortCriteria: dict
    :param SortCriteria: Represents the criteria used for sorting findings.\n\nAttributeName (string) --Represents the finding attribute (for example, accountId) to sort findings by.\n\nOrderBy (string) --The order by which the sorted findings are to be displayed.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Findings': [
        {
            'AccountId': 'string',
            'Arn': 'string',
            'Confidence': 123.0,
            'CreatedAt': 'string',
            'Description': 'string',
            'Id': 'string',
            'Partition': 'string',
            'Region': 'string',
            'Resource': {
                'AccessKeyDetails': {
                    'AccessKeyId': 'string',
                    'PrincipalId': 'string',
                    'UserName': 'string',
                    'UserType': 'string'
                },
                'InstanceDetails': {
                    'AvailabilityZone': 'string',
                    'IamInstanceProfile': {
                        'Arn': 'string',
                        'Id': 'string'
                    },
                    'ImageDescription': 'string',
                    'ImageId': 'string',
                    'InstanceId': 'string',
                    'InstanceState': 'string',
                    'InstanceType': 'string',
                    'OutpostArn': 'string',
                    'LaunchTime': 'string',
                    'NetworkInterfaces': [
                        {
                            'Ipv6Addresses': [
                                'string',
                            ],
                            'NetworkInterfaceId': 'string',
                            'PrivateDnsName': 'string',
                            'PrivateIpAddress': 'string',
                            'PrivateIpAddresses': [
                                {
                                    'PrivateDnsName': 'string',
                                    'PrivateIpAddress': 'string'
                                },
                            ],
                            'PublicDnsName': 'string',
                            'PublicIp': 'string',
                            'SecurityGroups': [
                                {
                                    'GroupId': 'string',
                                    'GroupName': 'string'
                                },
                            ],
                            'SubnetId': 'string',
                            'VpcId': 'string'
                        },
                    ],
                    'Platform': 'string',
                    'ProductCodes': [
                        {
                            'Code': 'string',
                            'ProductType': 'string'
                        },
                    ],
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ]
                },
                'ResourceType': 'string'
            },
            'SchemaVersion': 'string',
            'Service': {
                'Action': {
                    'ActionType': 'string',
                    'AwsApiCallAction': {
                        'Api': 'string',
                        'CallerType': 'string',
                        'DomainDetails': {
                            'Domain': 'string'
                        },
                        'RemoteIpDetails': {
                            'City': {
                                'CityName': 'string'
                            },
                            'Country': {
                                'CountryCode': 'string',
                                'CountryName': 'string'
                            },
                            'GeoLocation': {
                                'Lat': 123.0,
                                'Lon': 123.0
                            },
                            'IpAddressV4': 'string',
                            'Organization': {
                                'Asn': 'string',
                                'AsnOrg': 'string',
                                'Isp': 'string',
                                'Org': 'string'
                            }
                        },
                        'ServiceName': 'string'
                    },
                    'DnsRequestAction': {
                        'Domain': 'string'
                    },
                    'NetworkConnectionAction': {
                        'Blocked': True|False,
                        'ConnectionDirection': 'string',
                        'LocalPortDetails': {
                            'Port': 123,
                            'PortName': 'string'
                        },
                        'Protocol': 'string',
                        'LocalIpDetails': {
                            'IpAddressV4': 'string'
                        },
                        'RemoteIpDetails': {
                            'City': {
                                'CityName': 'string'
                            },
                            'Country': {
                                'CountryCode': 'string',
                                'CountryName': 'string'
                            },
                            'GeoLocation': {
                                'Lat': 123.0,
                                'Lon': 123.0
                            },
                            'IpAddressV4': 'string',
                            'Organization': {
                                'Asn': 'string',
                                'AsnOrg': 'string',
                                'Isp': 'string',
                                'Org': 'string'
                            }
                        },
                        'RemotePortDetails': {
                            'Port': 123,
                            'PortName': 'string'
                        }
                    },
                    'PortProbeAction': {
                        'Blocked': True|False,
                        'PortProbeDetails': [
                            {
                                'LocalPortDetails': {
                                    'Port': 123,
                                    'PortName': 'string'
                                },
                                'LocalIpDetails': {
                                    'IpAddressV4': 'string'
                                },
                                'RemoteIpDetails': {
                                    'City': {
                                        'CityName': 'string'
                                    },
                                    'Country': {
                                        'CountryCode': 'string',
                                        'CountryName': 'string'
                                    },
                                    'GeoLocation': {
                                        'Lat': 123.0,
                                        'Lon': 123.0
                                    },
                                    'IpAddressV4': 'string',
                                    'Organization': {
                                        'Asn': 'string',
                                        'AsnOrg': 'string',
                                        'Isp': 'string',
                                        'Org': 'string'
                                    }
                                }
                            },
                        ]
                    }
                },
                'Evidence': {
                    'ThreatIntelligenceDetails': [
                        {
                            'ThreatListName': 'string',
                            'ThreatNames': [
                                'string',
                            ]
                        },
                    ]
                },
                'Archived': True|False,
                'Count': 123,
                'DetectorId': 'string',
                'EventFirstSeen': 'string',
                'EventLastSeen': 'string',
                'ResourceRole': 'string',
                'ServiceName': 'string',
                'UserFeedback': 'string'
            },
            'Severity': 123.0,
            'Title': 'string',
            'Type': 'string',
            'UpdatedAt': 'string'
        },
    ]
}


Response Structure

(dict) --

Findings (list) --
A list of findings.

(dict) --
Contains information about the finding, which is generated when abnormal or suspicious activity is detected.

AccountId (string) --
The ID of the account in which the finding was generated.

Arn (string) --
The ARN of the finding.

Confidence (float) --
The confidence score for the finding.

CreatedAt (string) --
The time and date when the finding was created.

Description (string) --
The description of the finding.

Id (string) --
The ID of the finding.

Partition (string) --
The partition associated with the finding.

Region (string) --
The Region where the finding was generated.

Resource (dict) --
Contains information about the AWS resource associated with the activity that prompted GuardDuty to generate a finding.

AccessKeyDetails (dict) --
The IAM access key details (IAM user information) of a user that engaged in the activity that prompted GuardDuty to generate a finding.

AccessKeyId (string) --
The access key ID of the user.

PrincipalId (string) --
The principal ID of the user.

UserName (string) --
The name of the user.

UserType (string) --
The type of the user.



InstanceDetails (dict) --
The information about the EC2 instance associated with the activity that prompted GuardDuty to generate a finding.

AvailabilityZone (string) --
The Availability Zone of the EC2 instance.

IamInstanceProfile (dict) --
The profile information of the EC2 instance.

Arn (string) --
The profile ARN of the EC2 instance.

Id (string) --
The profile ID of the EC2 instance.



ImageDescription (string) --
The image description of the EC2 instance.

ImageId (string) --
The image ID of the EC2 instance.

InstanceId (string) --
The ID of the EC2 instance.

InstanceState (string) --
The state of the EC2 instance.

InstanceType (string) --
The type of the EC2 instance.

OutpostArn (string) --
The Amazon Resource Name (ARN) of the AWS Outpost. Only applicable to AWS Outposts instances.

LaunchTime (string) --
The launch time of the EC2 instance.

NetworkInterfaces (list) --
The elastic network interface information of the EC2 instance.

(dict) --
Contains information about the elastic network interface of the EC2 instance.

Ipv6Addresses (list) --
A list of IPv6 addresses for the EC2 instance.

(string) --


NetworkInterfaceId (string) --
The ID of the network interface.

PrivateDnsName (string) --
The private DNS name of the EC2 instance.

PrivateIpAddress (string) --
The private IP address of the EC2 instance.

PrivateIpAddresses (list) --
Other private IP address information of the EC2 instance.

(dict) --
Contains other private IP address information of the EC2 instance.

PrivateDnsName (string) --
The private DNS name of the EC2 instance.

PrivateIpAddress (string) --
The private IP address of the EC2 instance.





PublicDnsName (string) --
The public DNS name of the EC2 instance.

PublicIp (string) --
The public IP address of the EC2 instance.

SecurityGroups (list) --
The security groups associated with the EC2 instance.

(dict) --
Contains information about the security groups associated with the EC2 instance.

GroupId (string) --
The security group ID of the EC2 instance.

GroupName (string) --
The security group name of the EC2 instance.





SubnetId (string) --
The subnet ID of the EC2 instance.

VpcId (string) --
The VPC ID of the EC2 instance.





Platform (string) --
The platform of the EC2 instance.

ProductCodes (list) --
The product code of the EC2 instance.

(dict) --
Contains information about the product code for the EC2 instance.

Code (string) --
The product code information.

ProductType (string) --
The product code type.





Tags (list) --
The tags of the EC2 instance.

(dict) --
Contains information about a tag associated with the EC2 instance.

Key (string) --
The EC2 instance tag key.

Value (string) --
The EC2 instance tag value.







ResourceType (string) --
The type of AWS resource.



SchemaVersion (string) --
The version of the schema used for the finding.

Service (dict) --
Contains additional information about the generated finding.

Action (dict) --
Information about the activity that is described in a finding.

ActionType (string) --
The GuardDuty finding activity type.

AwsApiCallAction (dict) --
Information about the AWS_API_CALL action described in this finding.

Api (string) --
The AWS API name.

CallerType (string) --
The AWS API caller type.

DomainDetails (dict) --
The domain information for the AWS API call.

Domain (string) --
The domain information for the AWS API call.



RemoteIpDetails (dict) --
The remote IP information of the connection.

City (dict) --
The city information of the remote IP address.

CityName (string) --
The city name of the remote IP address.



Country (dict) --
The country code of the remote IP address.

CountryCode (string) --
The country code of the remote IP address.

CountryName (string) --
The country name of the remote IP address.



GeoLocation (dict) --
The location information of the remote IP address.

Lat (float) --
The latitude information of the remote IP address.

Lon (float) --
The longitude information of the remote IP address.



IpAddressV4 (string) --
The IPv4 remote address of the connection.

Organization (dict) --
The ISP organization information of the remote IP address.

Asn (string) --
The Autonomous System Number (ASN) of the internet provider of the remote IP address.

AsnOrg (string) --
The organization that registered this ASN.

Isp (string) --
The ISP information for the internet provider.

Org (string) --
The name of the internet provider.





ServiceName (string) --
The AWS service name whose API was invoked.



DnsRequestAction (dict) --
Information about the DNS_REQUEST action described in this finding.

Domain (string) --
The domain information for the API request.



NetworkConnectionAction (dict) --
Information about the NETWORK_CONNECTION action described in this finding.

Blocked (boolean) --
Indicates whether EC2 blocked the network connection to your instance.

ConnectionDirection (string) --
The network connection direction.

LocalPortDetails (dict) --
The local port information of the connection.

Port (integer) --
The port number of the local connection.

PortName (string) --
The port name of the local connection.



Protocol (string) --
The network connection protocol.

LocalIpDetails (dict) --
The local IP information of the connection.

IpAddressV4 (string) --
The IPv4 local address of the connection.



RemoteIpDetails (dict) --
The remote IP information of the connection.

City (dict) --
The city information of the remote IP address.

CityName (string) --
The city name of the remote IP address.



Country (dict) --
The country code of the remote IP address.

CountryCode (string) --
The country code of the remote IP address.

CountryName (string) --
The country name of the remote IP address.



GeoLocation (dict) --
The location information of the remote IP address.

Lat (float) --
The latitude information of the remote IP address.

Lon (float) --
The longitude information of the remote IP address.



IpAddressV4 (string) --
The IPv4 remote address of the connection.

Organization (dict) --
The ISP organization information of the remote IP address.

Asn (string) --
The Autonomous System Number (ASN) of the internet provider of the remote IP address.

AsnOrg (string) --
The organization that registered this ASN.

Isp (string) --
The ISP information for the internet provider.

Org (string) --
The name of the internet provider.





RemotePortDetails (dict) --
The remote port information of the connection.

Port (integer) --
The port number of the remote connection.

PortName (string) --
The port name of the remote connection.





PortProbeAction (dict) --
Information about the PORT_PROBE action described in this finding.

Blocked (boolean) --
Indicates whether EC2 blocked the port probe to the instance, such as with an ACL.

PortProbeDetails (list) --
A list of objects related to port probe details.

(dict) --
Contains information about the port probe details.

LocalPortDetails (dict) --
The local port information of the connection.

Port (integer) --
The port number of the local connection.

PortName (string) --
The port name of the local connection.



LocalIpDetails (dict) --
The local IP information of the connection.

IpAddressV4 (string) --
The IPv4 local address of the connection.



RemoteIpDetails (dict) --
The remote IP information of the connection.

City (dict) --
The city information of the remote IP address.

CityName (string) --
The city name of the remote IP address.



Country (dict) --
The country code of the remote IP address.

CountryCode (string) --
The country code of the remote IP address.

CountryName (string) --
The country name of the remote IP address.



GeoLocation (dict) --
The location information of the remote IP address.

Lat (float) --
The latitude information of the remote IP address.

Lon (float) --
The longitude information of the remote IP address.



IpAddressV4 (string) --
The IPv4 remote address of the connection.

Organization (dict) --
The ISP organization information of the remote IP address.

Asn (string) --
The Autonomous System Number (ASN) of the internet provider of the remote IP address.

AsnOrg (string) --
The organization that registered this ASN.

Isp (string) --
The ISP information for the internet provider.

Org (string) --
The name of the internet provider.













Evidence (dict) --
An evidence object associated with the service.

ThreatIntelligenceDetails (list) --
A list of threat intelligence details related to the evidence.

(dict) --
An instance of a threat intelligence detail that constitutes evidence for the finding.

ThreatListName (string) --
The name of the threat intelligence list that triggered the finding.

ThreatNames (list) --
A list of names of the threats in the threat intelligence list that triggered the finding.

(string) --








Archived (boolean) --
Indicates whether this finding is archived.

Count (integer) --
The total count of the occurrences of this finding type.

DetectorId (string) --
The detector ID for the GuardDuty service.

EventFirstSeen (string) --
The first-seen timestamp of the activity that prompted GuardDuty to generate this finding.

EventLastSeen (string) --
The last-seen timestamp of the activity that prompted GuardDuty to generate this finding.

ResourceRole (string) --
The resource role information for this finding.

ServiceName (string) --
The name of the AWS service (GuardDuty) that generated a finding.

UserFeedback (string) --
Feedback that was submitted about the finding.



Severity (float) --
The severity of the finding.

Title (string) --
The title of the finding.

Type (string) --
The type of finding.

UpdatedAt (string) --
The time and date when the finding was last updated.











Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'Findings': [
            {
                'AccountId': 'string',
                'Arn': 'string',
                'Confidence': 123.0,
                'CreatedAt': 'string',
                'Description': 'string',
                'Id': 'string',
                'Partition': 'string',
                'Region': 'string',
                'Resource': {
                    'AccessKeyDetails': {
                        'AccessKeyId': 'string',
                        'PrincipalId': 'string',
                        'UserName': 'string',
                        'UserType': 'string'
                    },
                    'InstanceDetails': {
                        'AvailabilityZone': 'string',
                        'IamInstanceProfile': {
                            'Arn': 'string',
                            'Id': 'string'
                        },
                        'ImageDescription': 'string',
                        'ImageId': 'string',
                        'InstanceId': 'string',
                        'InstanceState': 'string',
                        'InstanceType': 'string',
                        'OutpostArn': 'string',
                        'LaunchTime': 'string',
                        'NetworkInterfaces': [
                            {
                                'Ipv6Addresses': [
                                    'string',
                                ],
                                'NetworkInterfaceId': 'string',
                                'PrivateDnsName': 'string',
                                'PrivateIpAddress': 'string',
                                'PrivateIpAddresses': [
                                    {
                                        'PrivateDnsName': 'string',
                                        'PrivateIpAddress': 'string'
                                    },
                                ],
                                'PublicDnsName': 'string',
                                'PublicIp': 'string',
                                'SecurityGroups': [
                                    {
                                        'GroupId': 'string',
                                        'GroupName': 'string'
                                    },
                                ],
                                'SubnetId': 'string',
                                'VpcId': 'string'
                            },
                        ],
                        'Platform': 'string',
                        'ProductCodes': [
                            {
                                'Code': 'string',
                                'ProductType': 'string'
                            },
                        ],
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                    'ResourceType': 'string'
                },
                'SchemaVersion': 'string',
                'Service': {
                    'Action': {
                        'ActionType': 'string',
                        'AwsApiCallAction': {
                            'Api': 'string',
                            'CallerType': 'string',
                            'DomainDetails': {
                                'Domain': 'string'
                            },
                            'RemoteIpDetails': {
                                'City': {
                                    'CityName': 'string'
                                },
                                'Country': {
                                    'CountryCode': 'string',
                                    'CountryName': 'string'
                                },
                                'GeoLocation': {
                                    'Lat': 123.0,
                                    'Lon': 123.0
                                },
                                'IpAddressV4': 'string',
                                'Organization': {
                                    'Asn': 'string',
                                    'AsnOrg': 'string',
                                    'Isp': 'string',
                                    'Org': 'string'
                                }
                            },
                            'ServiceName': 'string'
                        },
                        'DnsRequestAction': {
                            'Domain': 'string'
                        },
                        'NetworkConnectionAction': {
                            'Blocked': True|False,
                            'ConnectionDirection': 'string',
                            'LocalPortDetails': {
                                'Port': 123,
                                'PortName': 'string'
                            },
                            'Protocol': 'string',
                            'LocalIpDetails': {
                                'IpAddressV4': 'string'
                            },
                            'RemoteIpDetails': {
                                'City': {
                                    'CityName': 'string'
                                },
                                'Country': {
                                    'CountryCode': 'string',
                                    'CountryName': 'string'
                                },
                                'GeoLocation': {
                                    'Lat': 123.0,
                                    'Lon': 123.0
                                },
                                'IpAddressV4': 'string',
                                'Organization': {
                                    'Asn': 'string',
                                    'AsnOrg': 'string',
                                    'Isp': 'string',
                                    'Org': 'string'
                                }
                            },
                            'RemotePortDetails': {
                                'Port': 123,
                                'PortName': 'string'
                            }
                        },
                        'PortProbeAction': {
                            'Blocked': True|False,
                            'PortProbeDetails': [
                                {
                                    'LocalPortDetails': {
                                        'Port': 123,
                                        'PortName': 'string'
                                    },
                                    'LocalIpDetails': {
                                        'IpAddressV4': 'string'
                                    },
                                    'RemoteIpDetails': {
                                        'City': {
                                            'CityName': 'string'
                                        },
                                        'Country': {
                                            'CountryCode': 'string',
                                            'CountryName': 'string'
                                        },
                                        'GeoLocation': {
                                            'Lat': 123.0,
                                            'Lon': 123.0
                                        },
                                        'IpAddressV4': 'string',
                                        'Organization': {
                                            'Asn': 'string',
                                            'AsnOrg': 'string',
                                            'Isp': 'string',
                                            'Org': 'string'
                                        }
                                    }
                                },
                            ]
                        }
                    },
                    'Evidence': {
                        'ThreatIntelligenceDetails': [
                            {
                                'ThreatListName': 'string',
                                'ThreatNames': [
                                    'string',
                                ]
                            },
                        ]
                    },
                    'Archived': True|False,
                    'Count': 123,
                    'DetectorId': 'string',
                    'EventFirstSeen': 'string',
                    'EventLastSeen': 'string',
                    'ResourceRole': 'string',
                    'ServiceName': 'string',
                    'UserFeedback': 'string'
                },
                'Severity': 123.0,
                'Title': 'string',
                'Type': 'string',
                'UpdatedAt': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_findings_statistics(DetectorId=None, FindingStatisticTypes=None, FindingCriteria=None):
    """
    Lists Amazon GuardDuty findings statistics for the specified detector ID.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_findings_statistics(
        DetectorId='string',
        FindingStatisticTypes=[
            'COUNT_BY_SEVERITY',
        ],
        FindingCriteria={
            'Criterion': {
                'string': {
                    'Eq': [
                        'string',
                    ],
                    'Neq': [
                        'string',
                    ],
                    'Gt': 123,
                    'Gte': 123,
                    'Lt': 123,
                    'Lte': 123,
                    'Equals': [
                        'string',
                    ],
                    'NotEquals': [
                        'string',
                    ],
                    'GreaterThan': 123,
                    'GreaterThanOrEqual': 123,
                    'LessThan': 123,
                    'LessThanOrEqual': 123
                }
            }
        }
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe ID of the detector that specifies the GuardDuty service whose findings\' statistics you want to retrieve.\n

    :type FindingStatisticTypes: list
    :param FindingStatisticTypes: [REQUIRED]\nThe types of finding statistics to retrieve.\n\n(string) --\n\n

    :type FindingCriteria: dict
    :param FindingCriteria: Represents the criteria that is used for querying findings.\n\nCriterion (dict) --Represents a map of finding properties that match specified conditions and values when querying findings.\n\n(string) --\n(dict) --Contains information about the condition.\n\nEq (list) --Represents the equal condition to be applied to a single field when querying for findings.\n\n(string) --\n\n\nNeq (list) --Represents the not equal condition to be applied to a single field when querying for findings.\n\n(string) --\n\n\nGt (integer) --Represents a greater than condition to be applied to a single field when querying for findings.\n\nGte (integer) --Represents a greater than or equal condition to be applied to a single field when querying for findings.\n\nLt (integer) --Represents a less than condition to be applied to a single field when querying for findings.\n\nLte (integer) --Represents a less than or equal condition to be applied to a single field when querying for findings.\n\nEquals (list) --Represents an equal condition to be applied to a single field when querying for findings.\n\n(string) --\n\n\nNotEquals (list) --Represents a not equal condition to be applied to a single field when querying for findings.\n\n(string) --\n\n\nGreaterThan (integer) --Represents a greater than condition to be applied to a single field when querying for findings.\n\nGreaterThanOrEqual (integer) --Represents a greater than or equal condition to be applied to a single field when querying for findings.\n\nLessThan (integer) --Represents a less than condition to be applied to a single field when querying for findings.\n\nLessThanOrEqual (integer) --Represents a less than or equal condition to be applied to a single field when querying for findings.\n\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'FindingStatistics': {
        'CountBySeverity': {
            'string': 123
        }
    }
}


Response Structure

(dict) --

FindingStatistics (dict) --
The finding statistics object.

CountBySeverity (dict) --
Represents a map of severity to count statistics for a set of findings.

(string) --
(integer) --












Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'FindingStatistics': {
            'CountBySeverity': {
                'string': 123
            }
        }
    }
    
    
    :returns: 
    (string) --
    (integer) --
    
    
    
    """
    pass

def get_invitations_count():
    """
    Returns the count of all GuardDuty membership invitations that were sent to the current member account except the currently accepted invitation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_invitations_count()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'InvitationsCount': 123
}


Response Structure

(dict) --
InvitationsCount (integer) --The number of received invitations.






Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'InvitationsCount': 123
    }
    
    
    """
    pass

def get_ip_set(DetectorId=None, IpSetId=None):
    """
    Retrieves the IPSet specified by the ipSetId .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_ip_set(
        DetectorId='string',
        IpSetId='string'
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe unique ID of the detector that the IPSet is associated with.\n

    :type IpSetId: string
    :param IpSetId: [REQUIRED]\nThe unique ID of the IPSet to retrieve.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Name': 'string',
    'Format': 'TXT'|'STIX'|'OTX_CSV'|'ALIEN_VAULT'|'PROOF_POINT'|'FIRE_EYE',
    'Location': 'string',
    'Status': 'INACTIVE'|'ACTIVATING'|'ACTIVE'|'DEACTIVATING'|'ERROR'|'DELETE_PENDING'|'DELETED',
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --

Name (string) --
The user-friendly name for the IPSet.

Format (string) --
The format of the file that contains the IPSet.

Location (string) --
The URI of the file that contains the IPSet.

Status (string) --
The status of IPSet file that was uploaded.

Tags (dict) --
The tags of the IPSet resource.

(string) --
(string) --










Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'Name': 'string',
        'Format': 'TXT'|'STIX'|'OTX_CSV'|'ALIEN_VAULT'|'PROOF_POINT'|'FIRE_EYE',
        'Location': 'string',
        'Status': 'INACTIVE'|'ACTIVATING'|'ACTIVE'|'DEACTIVATING'|'ERROR'|'DELETE_PENDING'|'DELETED',
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_master_account(DetectorId=None):
    """
    Provides the details for the GuardDuty master account associated with the current GuardDuty member account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_master_account(
        DetectorId='string'
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe unique ID of the detector of the GuardDuty member account.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Master': {
        'AccountId': 'string',
        'InvitationId': 'string',
        'RelationshipStatus': 'string',
        'InvitedAt': 'string'
    }
}


Response Structure

(dict) --
Master (dict) --The master account details.

AccountId (string) --The ID of the account used as the master account.

InvitationId (string) --The value used to validate the master account to the member account.

RelationshipStatus (string) --The status of the relationship between the master and member accounts.

InvitedAt (string) --The timestamp when the invitation was sent.








Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'Master': {
            'AccountId': 'string',
            'InvitationId': 'string',
            'RelationshipStatus': 'string',
            'InvitedAt': 'string'
        }
    }
    
    
    """
    pass

def get_members(DetectorId=None, AccountIds=None):
    """
    Retrieves GuardDuty member accounts (to the current GuardDuty master account) specified by the account IDs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_members(
        DetectorId='string',
        AccountIds=[
            'string',
        ]
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe unique ID of the detector of the GuardDuty account whose members you want to retrieve.\n

    :type AccountIds: list
    :param AccountIds: [REQUIRED]\nA list of account IDs of the GuardDuty member accounts that you want to describe.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Members': [
        {
            'AccountId': 'string',
            'DetectorId': 'string',
            'MasterId': 'string',
            'Email': 'string',
            'RelationshipStatus': 'string',
            'InvitedAt': 'string',
            'UpdatedAt': 'string'
        },
    ],
    'UnprocessedAccounts': [
        {
            'AccountId': 'string',
            'Result': 'string'
        },
    ]
}


Response Structure

(dict) --

Members (list) --
A list of members.

(dict) --
Contains information about the member account.

AccountId (string) --
The ID of the member account.

DetectorId (string) --
The detector ID of the member account.

MasterId (string) --
The master account ID.

Email (string) --
The email address of the member account.

RelationshipStatus (string) --
The status of the relationship between the member and the master.

InvitedAt (string) --
The timestamp when the invitation was sent.

UpdatedAt (string) --
The last-updated timestamp of the member.





UnprocessedAccounts (list) --
A list of objects that contain the unprocessed account and a result string that explains why it was unprocessed.

(dict) --
Contains information about the accounts that weren\'t processed.

AccountId (string) --
The AWS account ID.

Result (string) --
A reason why the account hasn\'t been processed.











Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'Members': [
            {
                'AccountId': 'string',
                'DetectorId': 'string',
                'MasterId': 'string',
                'Email': 'string',
                'RelationshipStatus': 'string',
                'InvitedAt': 'string',
                'UpdatedAt': 'string'
            },
        ],
        'UnprocessedAccounts': [
            {
                'AccountId': 'string',
                'Result': 'string'
            },
        ]
    }
    
    
    :returns: 
    GuardDuty.Client.exceptions.BadRequestException
    GuardDuty.Client.exceptions.InternalServerErrorException
    
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

def get_threat_intel_set(DetectorId=None, ThreatIntelSetId=None):
    """
    Retrieves the ThreatIntelSet that is specified by the ThreatIntelSet ID.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_threat_intel_set(
        DetectorId='string',
        ThreatIntelSetId='string'
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe unique ID of the detector that the threatIntelSet is associated with.\n

    :type ThreatIntelSetId: string
    :param ThreatIntelSetId: [REQUIRED]\nThe unique ID of the threatIntelSet that you want to get.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Name': 'string',
    'Format': 'TXT'|'STIX'|'OTX_CSV'|'ALIEN_VAULT'|'PROOF_POINT'|'FIRE_EYE',
    'Location': 'string',
    'Status': 'INACTIVE'|'ACTIVATING'|'ACTIVE'|'DEACTIVATING'|'ERROR'|'DELETE_PENDING'|'DELETED',
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --

Name (string) --
A user-friendly ThreatIntelSet name displayed in all findings that are generated by activity that involves IP addresses included in this ThreatIntelSet.

Format (string) --
The format of the threatIntelSet.

Location (string) --
The URI of the file that contains the ThreatIntelSet.

Status (string) --
The status of threatIntelSet file uploaded.

Tags (dict) --
The tags of the threat list resource.

(string) --
(string) --










Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'Name': 'string',
        'Format': 'TXT'|'STIX'|'OTX_CSV'|'ALIEN_VAULT'|'PROOF_POINT'|'FIRE_EYE',
        'Location': 'string',
        'Status': 'INACTIVE'|'ACTIVATING'|'ACTIVE'|'DEACTIVATING'|'ERROR'|'DELETE_PENDING'|'DELETED',
        'Tags': {
            'string': 'string'
        }
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

def invite_members(DetectorId=None, AccountIds=None, DisableEmailNotification=None, Message=None):
    """
    Invites other AWS accounts (created as members of the current AWS account by CreateMembers) to enable GuardDuty, and allow the current AWS account to view and manage these accounts\' GuardDuty findings on their behalf as the master account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.invite_members(
        DetectorId='string',
        AccountIds=[
            'string',
        ],
        DisableEmailNotification=True|False,
        Message='string'
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe unique ID of the detector of the GuardDuty account that you want to invite members with.\n

    :type AccountIds: list
    :param AccountIds: [REQUIRED]\nA list of account IDs of the accounts that you want to invite to GuardDuty as members.\n\n(string) --\n\n

    :type DisableEmailNotification: boolean
    :param DisableEmailNotification: A Boolean value that specifies whether you want to disable email notification to the accounts that you\xe2\x80\x99re inviting to GuardDuty as members.

    :type Message: string
    :param Message: The invitation message that you want to send to the accounts that you\xe2\x80\x99re inviting to GuardDuty as members.

    :rtype: dict

ReturnsResponse Syntax
{
    'UnprocessedAccounts': [
        {
            'AccountId': 'string',
            'Result': 'string'
        },
    ]
}


Response Structure

(dict) --

UnprocessedAccounts (list) --
A list of objects that contain the unprocessed account and a result string that explains why it was unprocessed.

(dict) --
Contains information about the accounts that weren\'t processed.

AccountId (string) --
The AWS account ID.

Result (string) --
A reason why the account hasn\'t been processed.











Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'UnprocessedAccounts': [
            {
                'AccountId': 'string',
                'Result': 'string'
            },
        ]
    }
    
    
    :returns: 
    GuardDuty.Client.exceptions.BadRequestException
    GuardDuty.Client.exceptions.InternalServerErrorException
    
    """
    pass

def list_detectors(MaxResults=None, NextToken=None):
    """
    Lists detectorIds of all the existing Amazon GuardDuty detector resources.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_detectors(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 50. The maximum value is 50.

    :type NextToken: string
    :param NextToken: You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.

    :rtype: dict

ReturnsResponse Syntax
{
    'DetectorIds': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

DetectorIds (list) --
A list of detector IDs.

(string) --


NextToken (string) --
The pagination parameter to be used on the next list operation to retrieve more items.







Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'DetectorIds': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_filters(DetectorId=None, MaxResults=None, NextToken=None):
    """
    Returns a paginated list of the current filters.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_filters(
        DetectorId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe unique ID of the detector that the filter is associated with.\n

    :type MaxResults: integer
    :param MaxResults: You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 50. The maximum value is 50.

    :type NextToken: string
    :param NextToken: You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.

    :rtype: dict

ReturnsResponse Syntax
{
    'FilterNames': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

FilterNames (list) --
A list of filter names.

(string) --


NextToken (string) --
The pagination parameter to be used on the next list operation to retrieve more items.







Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'FilterNames': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_findings(DetectorId=None, FindingCriteria=None, SortCriteria=None, MaxResults=None, NextToken=None):
    """
    Lists Amazon GuardDuty findings for the specified detector ID.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_findings(
        DetectorId='string',
        FindingCriteria={
            'Criterion': {
                'string': {
                    'Eq': [
                        'string',
                    ],
                    'Neq': [
                        'string',
                    ],
                    'Gt': 123,
                    'Gte': 123,
                    'Lt': 123,
                    'Lte': 123,
                    'Equals': [
                        'string',
                    ],
                    'NotEquals': [
                        'string',
                    ],
                    'GreaterThan': 123,
                    'GreaterThanOrEqual': 123,
                    'LessThan': 123,
                    'LessThanOrEqual': 123
                }
            }
        },
        SortCriteria={
            'AttributeName': 'string',
            'OrderBy': 'ASC'|'DESC'
        },
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe ID of the detector that specifies the GuardDuty service whose findings you want to list.\n

    :type FindingCriteria: dict
    :param FindingCriteria: Represents the criteria used for querying findings. Valid values include:\n\nJSON field name\naccountId\nregion\nconfidence\nid\nresource.accessKeyDetails.accessKeyId\nresource.accessKeyDetails.principalId\nresource.accessKeyDetails.userName\nresource.accessKeyDetails.userType\nresource.instanceDetails.iamInstanceProfile.id\nresource.instanceDetails.imageId\nresource.instanceDetails.instanceId\nresource.instanceDetails.outpostArn\nresource.instanceDetails.networkInterfaces.ipv6Addresses\nresource.instanceDetails.networkInterfaces.privateIpAddresses.privateIpAddress\nresource.instanceDetails.networkInterfaces.publicDnsName\nresource.instanceDetails.networkInterfaces.publicIp\nresource.instanceDetails.networkInterfaces.securityGroups.groupId\nresource.instanceDetails.networkInterfaces.securityGroups.groupName\nresource.instanceDetails.networkInterfaces.subnetId\nresource.instanceDetails.networkInterfaces.vpcId\nresource.instanceDetails.tags.key\nresource.instanceDetails.tags.value\nresource.resourceType\nservice.action.actionType\nservice.action.awsApiCallAction.api\nservice.action.awsApiCallAction.callerType\nservice.action.awsApiCallAction.remoteIpDetails.city.cityName\nservice.action.awsApiCallAction.remoteIpDetails.country.countryName\nservice.action.awsApiCallAction.remoteIpDetails.ipAddressV4\nservice.action.awsApiCallAction.remoteIpDetails.organization.asn\nservice.action.awsApiCallAction.remoteIpDetails.organization.asnOrg\nservice.action.awsApiCallAction.serviceName\nservice.action.dnsRequestAction.domain\nservice.action.networkConnectionAction.blocked\nservice.action.networkConnectionAction.connectionDirection\nservice.action.networkConnectionAction.localPortDetails.port\nservice.action.networkConnectionAction.protocol\nservice.action.networkConnectionAction.localIpDetails.ipAddressV4\nservice.action.networkConnectionAction.remoteIpDetails.city.cityName\nservice.action.networkConnectionAction.remoteIpDetails.country.countryName\nservice.action.networkConnectionAction.remoteIpDetails.ipAddressV4\nservice.action.networkConnectionAction.remoteIpDetails.organization.asn\nservice.action.networkConnectionAction.remoteIpDetails.organization.asnOrg\nservice.action.networkConnectionAction.remotePortDetails.port\nservice.additionalInfo.threatListName\nservice.archived When this attribute is set to \'true\', only archived findings are listed. When it\'s set to \'false\', only unarchived findings are listed. When this attribute is not set, all existing findings are listed.\nservice.resourceRole\nseverity\ntype\nupdatedAt Type: Timestamp in Unix Epoch millisecond format: 1486685375000\n\n\nCriterion (dict) --Represents a map of finding properties that match specified conditions and values when querying findings.\n\n(string) --\n(dict) --Contains information about the condition.\n\nEq (list) --Represents the equal condition to be applied to a single field when querying for findings.\n\n(string) --\n\n\nNeq (list) --Represents the not equal condition to be applied to a single field when querying for findings.\n\n(string) --\n\n\nGt (integer) --Represents a greater than condition to be applied to a single field when querying for findings.\n\nGte (integer) --Represents a greater than or equal condition to be applied to a single field when querying for findings.\n\nLt (integer) --Represents a less than condition to be applied to a single field when querying for findings.\n\nLte (integer) --Represents a less than or equal condition to be applied to a single field when querying for findings.\n\nEquals (list) --Represents an equal condition to be applied to a single field when querying for findings.\n\n(string) --\n\n\nNotEquals (list) --Represents a not equal condition to be applied to a single field when querying for findings.\n\n(string) --\n\n\nGreaterThan (integer) --Represents a greater than condition to be applied to a single field when querying for findings.\n\nGreaterThanOrEqual (integer) --Represents a greater than or equal condition to be applied to a single field when querying for findings.\n\nLessThan (integer) --Represents a less than condition to be applied to a single field when querying for findings.\n\nLessThanOrEqual (integer) --Represents a less than or equal condition to be applied to a single field when querying for findings.\n\n\n\n\n\n\n\n\n

    :type SortCriteria: dict
    :param SortCriteria: Represents the criteria used for sorting findings.\n\nAttributeName (string) --Represents the finding attribute (for example, accountId) to sort findings by.\n\nOrderBy (string) --The order by which the sorted findings are to be displayed.\n\n\n

    :type MaxResults: integer
    :param MaxResults: You can use this parameter to indicate the maximum number of items you want in the response. The default value is 50. The maximum value is 50.

    :type NextToken: string
    :param NextToken: You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.

    :rtype: dict

ReturnsResponse Syntax
{
    'FindingIds': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

FindingIds (list) --
The IDs of the findings that you\'re listing.

(string) --


NextToken (string) --
The pagination parameter to be used on the next list operation to retrieve more items.







Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'FindingIds': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_invitations(MaxResults=None, NextToken=None):
    """
    Lists all GuardDuty membership invitations that were sent to the current AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_invitations(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 50. The maximum value is 50.

    :type NextToken: string
    :param NextToken: You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.

    :rtype: dict

ReturnsResponse Syntax
{
    'Invitations': [
        {
            'AccountId': 'string',
            'InvitationId': 'string',
            'RelationshipStatus': 'string',
            'InvitedAt': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Invitations (list) --
A list of invitation descriptions.

(dict) --
Contains information about the invitation to become a member account.

AccountId (string) --
The ID of the account that the invitation was sent from.

InvitationId (string) --
The ID of the invitation. This value is used to validate the inviter account to the member account.

RelationshipStatus (string) --
The status of the relationship between the inviter and invitee accounts.

InvitedAt (string) --
The timestamp when the invitation was sent.





NextToken (string) --
The pagination parameter to be used on the next list operation to retrieve more items.







Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'Invitations': [
            {
                'AccountId': 'string',
                'InvitationId': 'string',
                'RelationshipStatus': 'string',
                'InvitedAt': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    GuardDuty.Client.exceptions.BadRequestException
    GuardDuty.Client.exceptions.InternalServerErrorException
    
    """
    pass

def list_ip_sets(DetectorId=None, MaxResults=None, NextToken=None):
    """
    Lists the IPSets of the GuardDuty service specified by the detector ID. If you use this operation from a member account, the IPSets returned are the IPSets from the associated master account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_ip_sets(
        DetectorId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe unique ID of the detector that the IPSet is associated with.\n

    :type MaxResults: integer
    :param MaxResults: You can use this parameter to indicate the maximum number of items you want in the response. The default value is 50. The maximum value is 50.

    :type NextToken: string
    :param NextToken: You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.

    :rtype: dict

ReturnsResponse Syntax
{
    'IpSetIds': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

IpSetIds (list) --
The IDs of the IPSet resources.

(string) --


NextToken (string) --
The pagination parameter to be used on the next list operation to retrieve more items.







Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'IpSetIds': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_members(DetectorId=None, MaxResults=None, NextToken=None, OnlyAssociated=None):
    """
    Lists details about associated member accounts for the current GuardDuty master account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_members(
        DetectorId='string',
        MaxResults=123,
        NextToken='string',
        OnlyAssociated='string'
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe unique ID of the detector the member is associated with.\n

    :type MaxResults: integer
    :param MaxResults: You can use this parameter to indicate the maximum number of items you want in the response. The default value is 50. The maximum value is 50.

    :type NextToken: string
    :param NextToken: You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.

    :type OnlyAssociated: string
    :param OnlyAssociated: Specifies what member accounts the response includes based on their relationship status with the master account. The default value is 'true'. If set to 'false' the response includes all existing member accounts (including members who haven\'t been invited yet or have been disassociated).

    :rtype: dict

ReturnsResponse Syntax
{
    'Members': [
        {
            'AccountId': 'string',
            'DetectorId': 'string',
            'MasterId': 'string',
            'Email': 'string',
            'RelationshipStatus': 'string',
            'InvitedAt': 'string',
            'UpdatedAt': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Members (list) --
A list of members.

(dict) --
Contains information about the member account.

AccountId (string) --
The ID of the member account.

DetectorId (string) --
The detector ID of the member account.

MasterId (string) --
The master account ID.

Email (string) --
The email address of the member account.

RelationshipStatus (string) --
The status of the relationship between the member and the master.

InvitedAt (string) --
The timestamp when the invitation was sent.

UpdatedAt (string) --
The last-updated timestamp of the member.





NextToken (string) --
The pagination parameter to be used on the next list operation to retrieve more items.







Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'Members': [
            {
                'AccountId': 'string',
                'DetectorId': 'string',
                'MasterId': 'string',
                'Email': 'string',
                'RelationshipStatus': 'string',
                'InvitedAt': 'string',
                'UpdatedAt': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    GuardDuty.Client.exceptions.BadRequestException
    GuardDuty.Client.exceptions.InternalServerErrorException
    
    """
    pass

def list_organization_admin_accounts(MaxResults=None, NextToken=None):
    """
    Lists the accounts configured as GuardDuty delegated administrators.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_organization_admin_accounts(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in the response.

    :type NextToken: string
    :param NextToken: A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the NextToken value returned from the previous request to continue listing results after the first page.

    :rtype: dict

ReturnsResponse Syntax
{
    'AdminAccounts': [
        {
            'AdminAccountId': 'string',
            'AdminStatus': 'ENABLED'|'DISABLE_IN_PROGRESS'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

AdminAccounts (list) --
An AdminAccounts object that includes a list of accounts configured as GuardDuty delegated administrators.

(dict) --
The account within the organization specified as the GuardDuty delegated administrator.

AdminAccountId (string) --
The AWS account ID for the account.

AdminStatus (string) --
Indicates whether the account is enabled as the delegated administrator.





NextToken (string) --
The pagination parameter to be used on the next list operation to retrieve more items.







Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'AdminAccounts': [
            {
                'AdminAccountId': 'string',
                'AdminStatus': 'ENABLED'|'DISABLE_IN_PROGRESS'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    GuardDuty.Client.exceptions.BadRequestException
    GuardDuty.Client.exceptions.InternalServerErrorException
    
    """
    pass

def list_publishing_destinations(DetectorId=None, MaxResults=None, NextToken=None):
    """
    Returns a list of publishing destinations associated with the specified dectectorId .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_publishing_destinations(
        DetectorId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe ID of the detector to retrieve publishing destinations for.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in the response.

    :type NextToken: string
    :param NextToken: A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the NextToken value returned from the previous request to continue listing results after the first page.

    :rtype: dict

ReturnsResponse Syntax
{
    'Destinations': [
        {
            'DestinationId': 'string',
            'DestinationType': 'S3',
            'Status': 'PENDING_VERIFICATION'|'PUBLISHING'|'UNABLE_TO_PUBLISH_FIX_DESTINATION_PROPERTY'|'STOPPED'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Destinations (list) --
A Destinations object that includes information about each publishing destination returned.

(dict) --
Contains information about the publishing destination, including the ID, type, and status.

DestinationId (string) --
The unique ID of the publishing destination.

DestinationType (string) --
The type of resource used for the publishing destination. Currently, only Amazon S3 buckets are supported.

Status (string) --
The status of the publishing destination.





NextToken (string) --
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the NextToken value returned from the previous request to continue listing results after the first page.







Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'Destinations': [
            {
                'DestinationId': 'string',
                'DestinationType': 'S3',
                'Status': 'PENDING_VERIFICATION'|'PUBLISHING'|'UNABLE_TO_PUBLISH_FIX_DESTINATION_PROPERTY'|'STOPPED'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    GuardDuty.Client.exceptions.BadRequestException
    GuardDuty.Client.exceptions.InternalServerErrorException
    
    """
    pass

def list_tags_for_resource(ResourceArn=None):
    """
    Lists tags for a resource. Tagging is currently supported for detectors, finding filters, IP sets, and threat intel sets, with a limit of 50 tags per resource. When invoked, this operation returns all assigned tags for a given resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) for the given GuardDuty resource.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
Tags (dict) --The tags associated with the resource.

(string) --
(string) --









Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    GuardDuty.Client.exceptions.BadRequestException
    GuardDuty.Client.exceptions.InternalServerErrorException
    
    """
    pass

def list_threat_intel_sets(DetectorId=None, MaxResults=None, NextToken=None):
    """
    Lists the ThreatIntelSets of the GuardDuty service specified by the detector ID. If you use this operation from a member account, the ThreatIntelSets associated with the master account are returned.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_threat_intel_sets(
        DetectorId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe unique ID of the detector that the threatIntelSet is associated with.\n

    :type MaxResults: integer
    :param MaxResults: You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 50. The maximum value is 50.

    :type NextToken: string
    :param NextToken: You can use this parameter to paginate results in the response. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.

    :rtype: dict

ReturnsResponse Syntax
{
    'ThreatIntelSetIds': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ThreatIntelSetIds (list) --
The IDs of the ThreatIntelSet resources.

(string) --


NextToken (string) --
The pagination parameter to be used on the next list operation to retrieve more items.







Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'ThreatIntelSetIds': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def start_monitoring_members(DetectorId=None, AccountIds=None):
    """
    Turns on GuardDuty monitoring of the specified member accounts. Use this operation to restart monitoring of accounts that you stopped monitoring with the StopMonitoringMembers operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_monitoring_members(
        DetectorId='string',
        AccountIds=[
            'string',
        ]
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe unique ID of the detector of the GuardDuty master account associated with the member accounts to monitor.\n

    :type AccountIds: list
    :param AccountIds: [REQUIRED]\nA list of account IDs of the GuardDuty member accounts to start monitoring.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'UnprocessedAccounts': [
        {
            'AccountId': 'string',
            'Result': 'string'
        },
    ]
}


Response Structure

(dict) --

UnprocessedAccounts (list) --
A list of objects that contain the unprocessed account and a result string that explains why it was unprocessed.

(dict) --
Contains information about the accounts that weren\'t processed.

AccountId (string) --
The AWS account ID.

Result (string) --
A reason why the account hasn\'t been processed.











Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'UnprocessedAccounts': [
            {
                'AccountId': 'string',
                'Result': 'string'
            },
        ]
    }
    
    
    :returns: 
    GuardDuty.Client.exceptions.BadRequestException
    GuardDuty.Client.exceptions.InternalServerErrorException
    
    """
    pass

def stop_monitoring_members(DetectorId=None, AccountIds=None):
    """
    Stops GuardDuty monitoring for the specified member accounts. Use the StartMonitoringMembers operation to restart monitoring for those accounts.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_monitoring_members(
        DetectorId='string',
        AccountIds=[
            'string',
        ]
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe unique ID of the detector associated with the GuardDuty master account that is monitoring member accounts.\n

    :type AccountIds: list
    :param AccountIds: [REQUIRED]\nA list of account IDs for the member accounts to stop monitoring.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'UnprocessedAccounts': [
        {
            'AccountId': 'string',
            'Result': 'string'
        },
    ]
}


Response Structure

(dict) --

UnprocessedAccounts (list) --
A list of objects that contain an accountId for each account that could not be processed, and a result string that indicates why the account was not processed.

(dict) --
Contains information about the accounts that weren\'t processed.

AccountId (string) --
The AWS account ID.

Result (string) --
A reason why the account hasn\'t been processed.











Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'UnprocessedAccounts': [
            {
                'AccountId': 'string',
                'Result': 'string'
            },
        ]
    }
    
    
    :returns: 
    GuardDuty.Client.exceptions.BadRequestException
    GuardDuty.Client.exceptions.InternalServerErrorException
    
    """
    pass

def tag_resource(ResourceArn=None, Tags=None):
    """
    Adds tags to a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceArn='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) for the GuardDuty resource to apply a tag to.\n

    :type Tags: dict
    :param Tags: [REQUIRED]\nThe tags to be added to a resource.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def unarchive_findings(DetectorId=None, FindingIds=None):
    """
    Unarchives GuardDuty findings specified by the findingIds .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.unarchive_findings(
        DetectorId='string',
        FindingIds=[
            'string',
        ]
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe ID of the detector associated with the findings to unarchive.\n

    :type FindingIds: list
    :param FindingIds: [REQUIRED]\nThe IDs of the findings to unarchive.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceArn=None, TagKeys=None):
    """
    Removes tags from a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) for the resource to remove tags from.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe tag keys to remove from the resource.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_detector(DetectorId=None, Enable=None, FindingPublishingFrequency=None):
    """
    Updates the Amazon GuardDuty detector specified by the detectorId.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_detector(
        DetectorId='string',
        Enable=True|False,
        FindingPublishingFrequency='FIFTEEN_MINUTES'|'ONE_HOUR'|'SIX_HOURS'
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe unique ID of the detector to update.\n

    :type Enable: boolean
    :param Enable: Specifies whether the detector is enabled or not enabled.

    :type FindingPublishingFrequency: string
    :param FindingPublishingFrequency: An enum value that specifies how frequently findings are exported, such as to CloudWatch Events.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_filter(DetectorId=None, FilterName=None, Description=None, Action=None, Rank=None, FindingCriteria=None):
    """
    Updates the filter specified by the filter name.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_filter(
        DetectorId='string',
        FilterName='string',
        Description='string',
        Action='NOOP'|'ARCHIVE',
        Rank=123,
        FindingCriteria={
            'Criterion': {
                'string': {
                    'Eq': [
                        'string',
                    ],
                    'Neq': [
                        'string',
                    ],
                    'Gt': 123,
                    'Gte': 123,
                    'Lt': 123,
                    'Lte': 123,
                    'Equals': [
                        'string',
                    ],
                    'NotEquals': [
                        'string',
                    ],
                    'GreaterThan': 123,
                    'GreaterThanOrEqual': 123,
                    'LessThan': 123,
                    'LessThanOrEqual': 123
                }
            }
        }
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe unique ID of the detector that specifies the GuardDuty service where you want to update a filter.\n

    :type FilterName: string
    :param FilterName: [REQUIRED]\nThe name of the filter.\n

    :type Description: string
    :param Description: The description of the filter.

    :type Action: string
    :param Action: Specifies the action that is to be applied to the findings that match the filter.

    :type Rank: integer
    :param Rank: Specifies the position of the filter in the list of current filters. Also specifies the order in which this filter is applied to the findings.

    :type FindingCriteria: dict
    :param FindingCriteria: Represents the criteria to be used in the filter for querying findings.\n\nCriterion (dict) --Represents a map of finding properties that match specified conditions and values when querying findings.\n\n(string) --\n(dict) --Contains information about the condition.\n\nEq (list) --Represents the equal condition to be applied to a single field when querying for findings.\n\n(string) --\n\n\nNeq (list) --Represents the not equal condition to be applied to a single field when querying for findings.\n\n(string) --\n\n\nGt (integer) --Represents a greater than condition to be applied to a single field when querying for findings.\n\nGte (integer) --Represents a greater than or equal condition to be applied to a single field when querying for findings.\n\nLt (integer) --Represents a less than condition to be applied to a single field when querying for findings.\n\nLte (integer) --Represents a less than or equal condition to be applied to a single field when querying for findings.\n\nEquals (list) --Represents an equal condition to be applied to a single field when querying for findings.\n\n(string) --\n\n\nNotEquals (list) --Represents a not equal condition to be applied to a single field when querying for findings.\n\n(string) --\n\n\nGreaterThan (integer) --Represents a greater than condition to be applied to a single field when querying for findings.\n\nGreaterThanOrEqual (integer) --Represents a greater than or equal condition to be applied to a single field when querying for findings.\n\nLessThan (integer) --Represents a less than condition to be applied to a single field when querying for findings.\n\nLessThanOrEqual (integer) --Represents a less than or equal condition to be applied to a single field when querying for findings.\n\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Name': 'string'
}


Response Structure

(dict) --

Name (string) --
The name of the filter.







Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {
        'Name': 'string'
    }
    
    
    :returns: 
    GuardDuty.Client.exceptions.BadRequestException
    GuardDuty.Client.exceptions.InternalServerErrorException
    
    """
    pass

def update_findings_feedback(DetectorId=None, FindingIds=None, Feedback=None, Comments=None):
    """
    Marks the specified GuardDuty findings as useful or not useful.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_findings_feedback(
        DetectorId='string',
        FindingIds=[
            'string',
        ],
        Feedback='USEFUL'|'NOT_USEFUL',
        Comments='string'
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe ID of the detector associated with the findings to update feedback for.\n

    :type FindingIds: list
    :param FindingIds: [REQUIRED]\nThe IDs of the findings that you want to mark as useful or not useful.\n\n(string) --\n\n

    :type Feedback: string
    :param Feedback: [REQUIRED]\nThe feedback for the finding.\n

    :type Comments: string
    :param Comments: Additional feedback about the GuardDuty findings.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_ip_set(DetectorId=None, IpSetId=None, Name=None, Location=None, Activate=None):
    """
    Updates the IPSet specified by the IPSet ID.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_ip_set(
        DetectorId='string',
        IpSetId='string',
        Name='string',
        Location='string',
        Activate=True|False
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe detectorID that specifies the GuardDuty service whose IPSet you want to update.\n

    :type IpSetId: string
    :param IpSetId: [REQUIRED]\nThe unique ID that specifies the IPSet that you want to update.\n

    :type Name: string
    :param Name: The unique ID that specifies the IPSet that you want to update.

    :type Location: string
    :param Location: The updated URI of the file that contains the IPSet.

    :type Activate: boolean
    :param Activate: The updated Boolean value that specifies whether the IPSet is active or not.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_organization_configuration(DetectorId=None, AutoEnable=None):
    """
    Updates the delegated administrator account with the values provided.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_organization_configuration(
        DetectorId='string',
        AutoEnable=True|False
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe ID of the detector to update the delegated administrator for.\n

    :type AutoEnable: boolean
    :param AutoEnable: [REQUIRED]\nIndicates whether to automatically enable member accounts in the organization.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_publishing_destination(DetectorId=None, DestinationId=None, DestinationProperties=None):
    """
    Updates information about the publishing destination specified by the destinationId .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_publishing_destination(
        DetectorId='string',
        DestinationId='string',
        DestinationProperties={
            'DestinationArn': 'string',
            'KmsKeyArn': 'string'
        }
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe ID of the detector associated with the publishing destinations to update.\n

    :type DestinationId: string
    :param DestinationId: [REQUIRED]\nThe ID of the publishing destination to update.\n

    :type DestinationProperties: dict
    :param DestinationProperties: A DestinationProperties object that includes the DestinationArn and KmsKeyArn of the publishing destination.\n\nDestinationArn (string) --The ARN of the resource to publish to.\n\nKmsKeyArn (string) --The ARN of the KMS key to use for encryption.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_threat_intel_set(DetectorId=None, ThreatIntelSetId=None, Name=None, Location=None, Activate=None):
    """
    Updates the ThreatIntelSet specified by the ThreatIntelSet ID.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_threat_intel_set(
        DetectorId='string',
        ThreatIntelSetId='string',
        Name='string',
        Location='string',
        Activate=True|False
    )
    
    
    :type DetectorId: string
    :param DetectorId: [REQUIRED]\nThe detectorID that specifies the GuardDuty service whose ThreatIntelSet you want to update.\n

    :type ThreatIntelSetId: string
    :param ThreatIntelSetId: [REQUIRED]\nThe unique ID that specifies the ThreatIntelSet that you want to update.\n

    :type Name: string
    :param Name: The unique ID that specifies the ThreatIntelSet that you want to update.

    :type Location: string
    :param Location: The updated URI of the file that contains the ThreateIntelSet.

    :type Activate: boolean
    :param Activate: The updated Boolean value that specifies whether the ThreateIntelSet is active or not.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

GuardDuty.Client.exceptions.BadRequestException
GuardDuty.Client.exceptions.InternalServerErrorException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

