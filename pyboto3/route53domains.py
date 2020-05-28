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

def accept_domain_transfer_from_another_aws_account(DomainName=None, Password=None):
    """
    Accepts the transfer of a domain from another AWS account to the current AWS account. You initiate a transfer between AWS accounts using TransferDomainToAnotherAwsAccount .
    Use either ListOperations or GetOperationDetail to determine whether the operation succeeded. GetOperationDetail provides additional information, for example, Domain Transfer from Aws Account 111122223333 has been cancelled .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.accept_domain_transfer_from_another_aws_account(
        DomainName='string',
        Password='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe name of the domain that was specified when another AWS account submitted a TransferDomainToAnotherAwsAccount request.\n

    :type Password: string
    :param Password: [REQUIRED]\nThe password that was returned by the TransferDomainToAnotherAwsAccount request.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'OperationId': 'string'
}


Response Structure

(dict) --
The AcceptDomainTransferFromAnotherAwsAccount response includes the following element.

OperationId (string) --
Identifier for tracking the progress of the request. To query the operation status, use GetOperationDetail .







Exceptions

Route53Domains.Client.exceptions.InvalidInput
Route53Domains.Client.exceptions.OperationLimitExceeded
Route53Domains.Client.exceptions.DomainLimitExceeded


    :return: {
        'OperationId': 'string'
    }
    
    
    :returns: 
    Route53Domains.Client.exceptions.InvalidInput
    Route53Domains.Client.exceptions.OperationLimitExceeded
    Route53Domains.Client.exceptions.DomainLimitExceeded
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def cancel_domain_transfer_to_another_aws_account(DomainName=None):
    """
    Cancels the transfer of a domain from the current AWS account to another AWS account. You initiate a transfer between AWS accounts using TransferDomainToAnotherAwsAccount .
    Use either ListOperations or GetOperationDetail to determine whether the operation succeeded. GetOperationDetail provides additional information, for example, Domain Transfer from Aws Account 111122223333 has been cancelled .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.cancel_domain_transfer_to_another_aws_account(
        DomainName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe name of the domain for which you want to cancel the transfer to another AWS account.\n

    :rtype: dict
ReturnsResponse Syntax{
    'OperationId': 'string'
}


Response Structure

(dict) --The CancelDomainTransferToAnotherAwsAccount response includes the following element.

OperationId (string) --The identifier that TransferDomainToAnotherAwsAccount returned to track the progress of the request. Because the transfer request was canceled, the value is no longer valid, and you can\'t use GetOperationDetail to query the operation status.






Exceptions

Route53Domains.Client.exceptions.InvalidInput
Route53Domains.Client.exceptions.OperationLimitExceeded


    :return: {
        'OperationId': 'string'
    }
    
    
    """
    pass

def check_domain_availability(DomainName=None, IdnLangCode=None):
    """
    This operation checks the availability of one domain name. Note that if the availability status of a domain is pending, you must submit another request to determine the availability of the domain name.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.check_domain_availability(
        DomainName='string',
        IdnLangCode='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe name of the domain that you want to get availability for. The top-level domain (TLD), such as .com, must be a TLD that Route 53 supports. For a list of supported TLDs, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide .\nThe domain name can contain only the following characters:\n\nLetters a through z. Domain names are not case sensitive.\nNumbers 0 through 9.\nHyphen (-). You can\'t specify a hyphen at the beginning or end of a label.\nPeriod (.) to separate the labels in the name, such as the . in example.com .\n\nInternationalized domain names are not supported for some top-level domains. To determine whether the TLD that you want to use supports internationalized domain names, see Domains that You Can Register with Amazon Route 53 . For more information, see Formatting Internationalized Domain Names .\n

    :type IdnLangCode: string
    :param IdnLangCode: Reserved for future use.

    :rtype: dict

ReturnsResponse Syntax
{
    'Availability': 'AVAILABLE'|'AVAILABLE_RESERVED'|'AVAILABLE_PREORDER'|'UNAVAILABLE'|'UNAVAILABLE_PREMIUM'|'UNAVAILABLE_RESTRICTED'|'RESERVED'|'DONT_KNOW'
}


Response Structure

(dict) --
The CheckDomainAvailability response includes the following elements.

Availability (string) --
Whether the domain name is available for registering.

Note
You can register only domains designated as AVAILABLE .

Valid values:

AVAILABLE

The domain name is available.

AVAILABLE_RESERVED

The domain name is reserved under specific conditions.

AVAILABLE_PREORDER

The domain name is available and can be preordered.

DONT_KNOW

The TLD registry didn\'t reply with a definitive answer about whether the domain name is available. Route 53 can return this response for a variety of reasons, for example, the registry is performing maintenance. Try again later.

PENDING

The TLD registry didn\'t return a response in the expected amount of time. When the response is delayed, it usually takes just a few extra seconds. You can resubmit the request immediately.

RESERVED

The domain name has been reserved for another person or organization.

UNAVAILABLE

The domain name is not available.

UNAVAILABLE_PREMIUM

The domain name is not available.

UNAVAILABLE_RESTRICTED

The domain name is forbidden.







Exceptions

Route53Domains.Client.exceptions.InvalidInput
Route53Domains.Client.exceptions.UnsupportedTLD


    :return: {
        'Availability': 'AVAILABLE'|'AVAILABLE_RESERVED'|'AVAILABLE_PREORDER'|'UNAVAILABLE'|'UNAVAILABLE_PREMIUM'|'UNAVAILABLE_RESTRICTED'|'RESERVED'|'DONT_KNOW'
    }
    
    
    :returns: 
    Route53Domains.Client.exceptions.InvalidInput
    Route53Domains.Client.exceptions.UnsupportedTLD
    
    """
    pass

def check_domain_transferability(DomainName=None, AuthCode=None):
    """
    Checks whether a domain name can be transferred to Amazon Route 53.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.check_domain_transferability(
        DomainName='string',
        AuthCode='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe name of the domain that you want to transfer to Route 53. The top-level domain (TLD), such as .com, must be a TLD that Route 53 supports. For a list of supported TLDs, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide .\nThe domain name can contain only the following characters:\n\nLetters a through z. Domain names are not case sensitive.\nNumbers 0 through 9.\nHyphen (-). You can\'t specify a hyphen at the beginning or end of a label.\nPeriod (.) to separate the labels in the name, such as the . in example.com .\n\n

    :type AuthCode: string
    :param AuthCode: If the registrar for the top-level domain (TLD) requires an authorization code to transfer the domain, the code that you got from the current registrar for the domain.

    :rtype: dict

ReturnsResponse Syntax
{
    'Transferability': {
        'Transferable': 'TRANSFERABLE'|'UNTRANSFERABLE'|'DONT_KNOW'
    }
}


Response Structure

(dict) --
The CheckDomainTransferability response includes the following elements.

Transferability (dict) --
A complex type that contains information about whether the specified domain can be transferred to Route 53.

Transferable (string) --
Whether the domain name can be transferred to Route 53.

Note
You can transfer only domains that have a value of TRANSFERABLE for Transferable .

Valid values:

TRANSFERABLE

The domain name can be transferred to Route 53.

UNTRANSFERRABLE

The domain name can\'t be transferred to Route 53.

DONT_KNOW

Reserved for future use.









Exceptions

Route53Domains.Client.exceptions.InvalidInput
Route53Domains.Client.exceptions.UnsupportedTLD


    :return: {
        'Transferability': {
            'Transferable': 'TRANSFERABLE'|'UNTRANSFERABLE'|'DONT_KNOW'
        }
    }
    
    
    :returns: 
    Route53Domains.Client.exceptions.InvalidInput
    Route53Domains.Client.exceptions.UnsupportedTLD
    
    """
    pass

def delete_tags_for_domain(DomainName=None, TagsToDelete=None):
    """
    This operation deletes the specified tags for a domain.
    All tag operations are eventually consistent; subsequent operations might not immediately represent all issued operations.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_tags_for_domain(
        DomainName='string',
        TagsToDelete=[
            'string',
        ]
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe domain for which you want to delete one or more tags.\n

    :type TagsToDelete: list
    :param TagsToDelete: [REQUIRED]\nA list of tag keys to delete.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Route53Domains.Client.exceptions.InvalidInput
Route53Domains.Client.exceptions.OperationLimitExceeded
Route53Domains.Client.exceptions.UnsupportedTLD


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def disable_domain_auto_renew(DomainName=None):
    """
    This operation disables automatic renewal of domain registration for the specified domain.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disable_domain_auto_renew(
        DomainName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe name of the domain that you want to disable automatic renewal for.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Route53Domains.Client.exceptions.InvalidInput
Route53Domains.Client.exceptions.UnsupportedTLD


    :return: {}
    
    
    :returns: 
    Route53Domains.Client.exceptions.InvalidInput
    Route53Domains.Client.exceptions.UnsupportedTLD
    
    """
    pass

def disable_domain_transfer_lock(DomainName=None):
    """
    This operation removes the transfer lock on the domain (specifically the clientTransferProhibited status) to allow domain transfers. We recommend you refrain from performing this action unless you intend to transfer the domain to a different registrar. Successful submission returns an operation ID that you can use to track the progress and completion of the action. If the request is not completed successfully, the domain registrant will be notified by email.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disable_domain_transfer_lock(
        DomainName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe name of the domain that you want to remove the transfer lock for.\n

    :rtype: dict
ReturnsResponse Syntax{
    'OperationId': 'string'
}


Response Structure

(dict) --The DisableDomainTransferLock response includes the following element.

OperationId (string) --Identifier for tracking the progress of the request. To query the operation status, use GetOperationDetail .






Exceptions

Route53Domains.Client.exceptions.InvalidInput
Route53Domains.Client.exceptions.DuplicateRequest
Route53Domains.Client.exceptions.TLDRulesViolation
Route53Domains.Client.exceptions.OperationLimitExceeded
Route53Domains.Client.exceptions.UnsupportedTLD


    :return: {
        'OperationId': 'string'
    }
    
    
    """
    pass

def enable_domain_auto_renew(DomainName=None):
    """
    This operation configures Amazon Route 53 to automatically renew the specified domain before the domain registration expires. The cost of renewing your domain registration is billed to your AWS account.
    The period during which you can renew a domain name varies by TLD. For a list of TLDs and their renewal policies, see Domains That You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide . Route 53 requires that you renew before the end of the renewal period so we can complete processing before the deadline.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.enable_domain_auto_renew(
        DomainName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe name of the domain that you want to enable automatic renewal for.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Route53Domains.Client.exceptions.InvalidInput
Route53Domains.Client.exceptions.UnsupportedTLD
Route53Domains.Client.exceptions.TLDRulesViolation


    :return: {}
    
    
    :returns: 
    Route53Domains.Client.exceptions.InvalidInput
    Route53Domains.Client.exceptions.UnsupportedTLD
    Route53Domains.Client.exceptions.TLDRulesViolation
    
    """
    pass

def enable_domain_transfer_lock(DomainName=None):
    """
    This operation sets the transfer lock on the domain (specifically the clientTransferProhibited status) to prevent domain transfers. Successful submission returns an operation ID that you can use to track the progress and completion of the action. If the request is not completed successfully, the domain registrant will be notified by email.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.enable_domain_transfer_lock(
        DomainName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe name of the domain that you want to set the transfer lock for.\n

    :rtype: dict
ReturnsResponse Syntax{
    'OperationId': 'string'
}


Response Structure

(dict) --The EnableDomainTransferLock response includes the following elements.

OperationId (string) --Identifier for tracking the progress of the request. To use this ID to query the operation status, use GetOperationDetail.






Exceptions

Route53Domains.Client.exceptions.InvalidInput
Route53Domains.Client.exceptions.DuplicateRequest
Route53Domains.Client.exceptions.TLDRulesViolation
Route53Domains.Client.exceptions.OperationLimitExceeded
Route53Domains.Client.exceptions.UnsupportedTLD


    :return: {
        'OperationId': 'string'
    }
    
    
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

def get_contact_reachability_status(domainName=None):
    """
    For operations that require confirmation that the email address for the registrant contact is valid, such as registering a new domain, this operation returns information about whether the registrant contact has responded.
    If you want us to resend the email, use the ResendContactReachabilityEmail operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_contact_reachability_status(
        domainName='string'
    )
    
    
    :type domainName: string
    :param domainName: The name of the domain for which you want to know whether the registrant contact has confirmed that the email address is valid.

    :rtype: dict
ReturnsResponse Syntax{
    'domainName': 'string',
    'status': 'PENDING'|'DONE'|'EXPIRED'
}


Response Structure

(dict) --
domainName (string) --The domain name for which you requested the reachability status.

status (string) --Whether the registrant contact has responded. Values include the following:

PENDING
We sent the confirmation email and haven\'t received a response yet.

DONE
We sent the email and got confirmation from the registrant contact.

EXPIRED
The time limit expired before the registrant contact responded.






Exceptions

Route53Domains.Client.exceptions.InvalidInput
Route53Domains.Client.exceptions.OperationLimitExceeded
Route53Domains.Client.exceptions.UnsupportedTLD


    :return: {
        'domainName': 'string',
        'status': 'PENDING'|'DONE'|'EXPIRED'
    }
    
    
    """
    pass

def get_domain_detail(DomainName=None):
    """
    This operation returns detailed information about a specified domain that is associated with the current AWS account. Contact information for the domain is also returned as part of the output.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_domain_detail(
        DomainName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe name of the domain that you want to get detailed information about.\n

    :rtype: dict
ReturnsResponse Syntax{
    'DomainName': 'string',
    'Nameservers': [
        {
            'Name': 'string',
            'GlueIps': [
                'string',
            ]
        },
    ],
    'AutoRenew': True|False,
    'AdminContact': {
        'FirstName': 'string',
        'LastName': 'string',
        'ContactType': 'PERSON'|'COMPANY'|'ASSOCIATION'|'PUBLIC_BODY'|'RESELLER',
        'OrganizationName': 'string',
        'AddressLine1': 'string',
        'AddressLine2': 'string',
        'City': 'string',
        'State': 'string',
        'CountryCode': 'AD'|'AE'|'AF'|'AG'|'AI'|'AL'|'AM'|'AN'|'AO'|'AQ'|'AR'|'AS'|'AT'|'AU'|'AW'|'AZ'|'BA'|'BB'|'BD'|'BE'|'BF'|'BG'|'BH'|'BI'|'BJ'|'BL'|'BM'|'BN'|'BO'|'BR'|'BS'|'BT'|'BW'|'BY'|'BZ'|'CA'|'CC'|'CD'|'CF'|'CG'|'CH'|'CI'|'CK'|'CL'|'CM'|'CN'|'CO'|'CR'|'CU'|'CV'|'CX'|'CY'|'CZ'|'DE'|'DJ'|'DK'|'DM'|'DO'|'DZ'|'EC'|'EE'|'EG'|'ER'|'ES'|'ET'|'FI'|'FJ'|'FK'|'FM'|'FO'|'FR'|'GA'|'GB'|'GD'|'GE'|'GH'|'GI'|'GL'|'GM'|'GN'|'GQ'|'GR'|'GT'|'GU'|'GW'|'GY'|'HK'|'HN'|'HR'|'HT'|'HU'|'ID'|'IE'|'IL'|'IM'|'IN'|'IQ'|'IR'|'IS'|'IT'|'JM'|'JO'|'JP'|'KE'|'KG'|'KH'|'KI'|'KM'|'KN'|'KP'|'KR'|'KW'|'KY'|'KZ'|'LA'|'LB'|'LC'|'LI'|'LK'|'LR'|'LS'|'LT'|'LU'|'LV'|'LY'|'MA'|'MC'|'MD'|'ME'|'MF'|'MG'|'MH'|'MK'|'ML'|'MM'|'MN'|'MO'|'MP'|'MR'|'MS'|'MT'|'MU'|'MV'|'MW'|'MX'|'MY'|'MZ'|'NA'|'NC'|'NE'|'NG'|'NI'|'NL'|'NO'|'NP'|'NR'|'NU'|'NZ'|'OM'|'PA'|'PE'|'PF'|'PG'|'PH'|'PK'|'PL'|'PM'|'PN'|'PR'|'PT'|'PW'|'PY'|'QA'|'RO'|'RS'|'RU'|'RW'|'SA'|'SB'|'SC'|'SD'|'SE'|'SG'|'SH'|'SI'|'SK'|'SL'|'SM'|'SN'|'SO'|'SR'|'ST'|'SV'|'SY'|'SZ'|'TC'|'TD'|'TG'|'TH'|'TJ'|'TK'|'TL'|'TM'|'TN'|'TO'|'TR'|'TT'|'TV'|'TW'|'TZ'|'UA'|'UG'|'US'|'UY'|'UZ'|'VA'|'VC'|'VE'|'VG'|'VI'|'VN'|'VU'|'WF'|'WS'|'YE'|'YT'|'ZA'|'ZM'|'ZW',
        'ZipCode': 'string',
        'PhoneNumber': 'string',
        'Email': 'string',
        'Fax': 'string',
        'ExtraParams': [
            {
                'Name': 'DUNS_NUMBER'|'BRAND_NUMBER'|'BIRTH_DEPARTMENT'|'BIRTH_DATE_IN_YYYY_MM_DD'|'BIRTH_COUNTRY'|'BIRTH_CITY'|'DOCUMENT_NUMBER'|'AU_ID_NUMBER'|'AU_ID_TYPE'|'CA_LEGAL_TYPE'|'CA_BUSINESS_ENTITY_TYPE'|'CA_LEGAL_REPRESENTATIVE'|'CA_LEGAL_REPRESENTATIVE_CAPACITY'|'ES_IDENTIFICATION'|'ES_IDENTIFICATION_TYPE'|'ES_LEGAL_FORM'|'FI_BUSINESS_NUMBER'|'FI_ID_NUMBER'|'FI_NATIONALITY'|'FI_ORGANIZATION_TYPE'|'IT_NATIONALITY'|'IT_PIN'|'IT_REGISTRANT_ENTITY_TYPE'|'RU_PASSPORT_DATA'|'SE_ID_NUMBER'|'SG_ID_NUMBER'|'VAT_NUMBER'|'UK_CONTACT_TYPE'|'UK_COMPANY_NUMBER',
                'Value': 'string'
            },
        ]
    },
    'RegistrantContact': {
        'FirstName': 'string',
        'LastName': 'string',
        'ContactType': 'PERSON'|'COMPANY'|'ASSOCIATION'|'PUBLIC_BODY'|'RESELLER',
        'OrganizationName': 'string',
        'AddressLine1': 'string',
        'AddressLine2': 'string',
        'City': 'string',
        'State': 'string',
        'CountryCode': 'AD'|'AE'|'AF'|'AG'|'AI'|'AL'|'AM'|'AN'|'AO'|'AQ'|'AR'|'AS'|'AT'|'AU'|'AW'|'AZ'|'BA'|'BB'|'BD'|'BE'|'BF'|'BG'|'BH'|'BI'|'BJ'|'BL'|'BM'|'BN'|'BO'|'BR'|'BS'|'BT'|'BW'|'BY'|'BZ'|'CA'|'CC'|'CD'|'CF'|'CG'|'CH'|'CI'|'CK'|'CL'|'CM'|'CN'|'CO'|'CR'|'CU'|'CV'|'CX'|'CY'|'CZ'|'DE'|'DJ'|'DK'|'DM'|'DO'|'DZ'|'EC'|'EE'|'EG'|'ER'|'ES'|'ET'|'FI'|'FJ'|'FK'|'FM'|'FO'|'FR'|'GA'|'GB'|'GD'|'GE'|'GH'|'GI'|'GL'|'GM'|'GN'|'GQ'|'GR'|'GT'|'GU'|'GW'|'GY'|'HK'|'HN'|'HR'|'HT'|'HU'|'ID'|'IE'|'IL'|'IM'|'IN'|'IQ'|'IR'|'IS'|'IT'|'JM'|'JO'|'JP'|'KE'|'KG'|'KH'|'KI'|'KM'|'KN'|'KP'|'KR'|'KW'|'KY'|'KZ'|'LA'|'LB'|'LC'|'LI'|'LK'|'LR'|'LS'|'LT'|'LU'|'LV'|'LY'|'MA'|'MC'|'MD'|'ME'|'MF'|'MG'|'MH'|'MK'|'ML'|'MM'|'MN'|'MO'|'MP'|'MR'|'MS'|'MT'|'MU'|'MV'|'MW'|'MX'|'MY'|'MZ'|'NA'|'NC'|'NE'|'NG'|'NI'|'NL'|'NO'|'NP'|'NR'|'NU'|'NZ'|'OM'|'PA'|'PE'|'PF'|'PG'|'PH'|'PK'|'PL'|'PM'|'PN'|'PR'|'PT'|'PW'|'PY'|'QA'|'RO'|'RS'|'RU'|'RW'|'SA'|'SB'|'SC'|'SD'|'SE'|'SG'|'SH'|'SI'|'SK'|'SL'|'SM'|'SN'|'SO'|'SR'|'ST'|'SV'|'SY'|'SZ'|'TC'|'TD'|'TG'|'TH'|'TJ'|'TK'|'TL'|'TM'|'TN'|'TO'|'TR'|'TT'|'TV'|'TW'|'TZ'|'UA'|'UG'|'US'|'UY'|'UZ'|'VA'|'VC'|'VE'|'VG'|'VI'|'VN'|'VU'|'WF'|'WS'|'YE'|'YT'|'ZA'|'ZM'|'ZW',
        'ZipCode': 'string',
        'PhoneNumber': 'string',
        'Email': 'string',
        'Fax': 'string',
        'ExtraParams': [
            {
                'Name': 'DUNS_NUMBER'|'BRAND_NUMBER'|'BIRTH_DEPARTMENT'|'BIRTH_DATE_IN_YYYY_MM_DD'|'BIRTH_COUNTRY'|'BIRTH_CITY'|'DOCUMENT_NUMBER'|'AU_ID_NUMBER'|'AU_ID_TYPE'|'CA_LEGAL_TYPE'|'CA_BUSINESS_ENTITY_TYPE'|'CA_LEGAL_REPRESENTATIVE'|'CA_LEGAL_REPRESENTATIVE_CAPACITY'|'ES_IDENTIFICATION'|'ES_IDENTIFICATION_TYPE'|'ES_LEGAL_FORM'|'FI_BUSINESS_NUMBER'|'FI_ID_NUMBER'|'FI_NATIONALITY'|'FI_ORGANIZATION_TYPE'|'IT_NATIONALITY'|'IT_PIN'|'IT_REGISTRANT_ENTITY_TYPE'|'RU_PASSPORT_DATA'|'SE_ID_NUMBER'|'SG_ID_NUMBER'|'VAT_NUMBER'|'UK_CONTACT_TYPE'|'UK_COMPANY_NUMBER',
                'Value': 'string'
            },
        ]
    },
    'TechContact': {
        'FirstName': 'string',
        'LastName': 'string',
        'ContactType': 'PERSON'|'COMPANY'|'ASSOCIATION'|'PUBLIC_BODY'|'RESELLER',
        'OrganizationName': 'string',
        'AddressLine1': 'string',
        'AddressLine2': 'string',
        'City': 'string',
        'State': 'string',
        'CountryCode': 'AD'|'AE'|'AF'|'AG'|'AI'|'AL'|'AM'|'AN'|'AO'|'AQ'|'AR'|'AS'|'AT'|'AU'|'AW'|'AZ'|'BA'|'BB'|'BD'|'BE'|'BF'|'BG'|'BH'|'BI'|'BJ'|'BL'|'BM'|'BN'|'BO'|'BR'|'BS'|'BT'|'BW'|'BY'|'BZ'|'CA'|'CC'|'CD'|'CF'|'CG'|'CH'|'CI'|'CK'|'CL'|'CM'|'CN'|'CO'|'CR'|'CU'|'CV'|'CX'|'CY'|'CZ'|'DE'|'DJ'|'DK'|'DM'|'DO'|'DZ'|'EC'|'EE'|'EG'|'ER'|'ES'|'ET'|'FI'|'FJ'|'FK'|'FM'|'FO'|'FR'|'GA'|'GB'|'GD'|'GE'|'GH'|'GI'|'GL'|'GM'|'GN'|'GQ'|'GR'|'GT'|'GU'|'GW'|'GY'|'HK'|'HN'|'HR'|'HT'|'HU'|'ID'|'IE'|'IL'|'IM'|'IN'|'IQ'|'IR'|'IS'|'IT'|'JM'|'JO'|'JP'|'KE'|'KG'|'KH'|'KI'|'KM'|'KN'|'KP'|'KR'|'KW'|'KY'|'KZ'|'LA'|'LB'|'LC'|'LI'|'LK'|'LR'|'LS'|'LT'|'LU'|'LV'|'LY'|'MA'|'MC'|'MD'|'ME'|'MF'|'MG'|'MH'|'MK'|'ML'|'MM'|'MN'|'MO'|'MP'|'MR'|'MS'|'MT'|'MU'|'MV'|'MW'|'MX'|'MY'|'MZ'|'NA'|'NC'|'NE'|'NG'|'NI'|'NL'|'NO'|'NP'|'NR'|'NU'|'NZ'|'OM'|'PA'|'PE'|'PF'|'PG'|'PH'|'PK'|'PL'|'PM'|'PN'|'PR'|'PT'|'PW'|'PY'|'QA'|'RO'|'RS'|'RU'|'RW'|'SA'|'SB'|'SC'|'SD'|'SE'|'SG'|'SH'|'SI'|'SK'|'SL'|'SM'|'SN'|'SO'|'SR'|'ST'|'SV'|'SY'|'SZ'|'TC'|'TD'|'TG'|'TH'|'TJ'|'TK'|'TL'|'TM'|'TN'|'TO'|'TR'|'TT'|'TV'|'TW'|'TZ'|'UA'|'UG'|'US'|'UY'|'UZ'|'VA'|'VC'|'VE'|'VG'|'VI'|'VN'|'VU'|'WF'|'WS'|'YE'|'YT'|'ZA'|'ZM'|'ZW',
        'ZipCode': 'string',
        'PhoneNumber': 'string',
        'Email': 'string',
        'Fax': 'string',
        'ExtraParams': [
            {
                'Name': 'DUNS_NUMBER'|'BRAND_NUMBER'|'BIRTH_DEPARTMENT'|'BIRTH_DATE_IN_YYYY_MM_DD'|'BIRTH_COUNTRY'|'BIRTH_CITY'|'DOCUMENT_NUMBER'|'AU_ID_NUMBER'|'AU_ID_TYPE'|'CA_LEGAL_TYPE'|'CA_BUSINESS_ENTITY_TYPE'|'CA_LEGAL_REPRESENTATIVE'|'CA_LEGAL_REPRESENTATIVE_CAPACITY'|'ES_IDENTIFICATION'|'ES_IDENTIFICATION_TYPE'|'ES_LEGAL_FORM'|'FI_BUSINESS_NUMBER'|'FI_ID_NUMBER'|'FI_NATIONALITY'|'FI_ORGANIZATION_TYPE'|'IT_NATIONALITY'|'IT_PIN'|'IT_REGISTRANT_ENTITY_TYPE'|'RU_PASSPORT_DATA'|'SE_ID_NUMBER'|'SG_ID_NUMBER'|'VAT_NUMBER'|'UK_CONTACT_TYPE'|'UK_COMPANY_NUMBER',
                'Value': 'string'
            },
        ]
    },
    'AdminPrivacy': True|False,
    'RegistrantPrivacy': True|False,
    'TechPrivacy': True|False,
    'RegistrarName': 'string',
    'WhoIsServer': 'string',
    'RegistrarUrl': 'string',
    'AbuseContactEmail': 'string',
    'AbuseContactPhone': 'string',
    'RegistryDomainId': 'string',
    'CreationDate': datetime(2015, 1, 1),
    'UpdatedDate': datetime(2015, 1, 1),
    'ExpirationDate': datetime(2015, 1, 1),
    'Reseller': 'string',
    'DnsSec': 'string',
    'StatusList': [
        'string',
    ]
}


Response Structure

(dict) --The GetDomainDetail response includes the following elements.

DomainName (string) --The name of a domain.

Nameservers (list) --The name of the domain.

(dict) --Nameserver includes the following elements.

Name (string) --The fully qualified host name of the name server.
Constraint: Maximum 255 characters

GlueIps (list) --Glue IP address of a name server entry. Glue IP addresses are required only when the name of the name server is a subdomain of the domain. For example, if your domain is example.com and the name server for the domain is ns.example.com, you need to specify the IP address for ns.example.com.
Constraints: The list can contain only one IPv4 and one IPv6 address.

(string) --






AutoRenew (boolean) --Specifies whether the domain registration is set to renew automatically.

AdminContact (dict) --Provides details about the domain administrative contact.

FirstName (string) --First name of contact.

LastName (string) --Last name of contact.

ContactType (string) --Indicates whether the contact is a person, company, association, or public organization. Note the following:

If you specify a value other than PERSON , you must also specify a value for OrganizationName .
For some TLDs, the privacy protection available depends on the value that you specify for Contact Type . For the privacy protection settings for your TLD, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide
For .es domains, if you specify PERSON , you must specify INDIVIDUAL for the value of ES_LEGAL_FORM .


OrganizationName (string) --Name of the organization for contact types other than PERSON .

AddressLine1 (string) --First line of the contact\'s address.

AddressLine2 (string) --Second line of contact\'s address, if any.

City (string) --The city of the contact\'s address.

State (string) --The state or province of the contact\'s city.

CountryCode (string) --Code for the country of the contact\'s address.

ZipCode (string) --The zip or postal code of the contact\'s address.

PhoneNumber (string) --The phone number of the contact.
Constraints: Phone number must be specified in the format "+[country dialing code].[number including any area code>]". For example, a US phone number might appear as "+1.1234567890" .

Email (string) --Email address of the contact.

Fax (string) --Fax number of the contact.
Constraints: Phone number must be specified in the format "+[country dialing code].[number including any area code]". For example, a US phone number might appear as "+1.1234567890" .

ExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.

(dict) --ExtraParam includes the following elements.

Name (string) --The name of an additional parameter that is required by a top-level domain. Here are the top-level domains that require additional parameters and the names of the parameters that they require:

.com.au and .net.au

AU_ID_NUMBER
AU_ID_TYPE   Valid values include the following:
ABN (Australian business number)
ACN (Australian company number)
TM (Trademark number)

.ca

BRAND_NUMBER
CA_BUSINESS_ENTITY_TYPE   Valid values include the following:
BANK (Bank)
COMMERCIAL_COMPANY (Commercial company)
COMPANY (Company)
COOPERATION (Cooperation)
COOPERATIVE (Cooperative)
COOPRIX (Cooprix)
CORP (Corporation)
CREDIT_UNION (Credit union)
FOMIA (Federation of mutual insurance associations)
INC (Incorporated)
LTD (Limited)
LTEE (Limit\xc3\xa9e)
LLC (Limited liability corporation)
LLP (Limited liability partnership)
LTE (Lte.)
MBA (Mutual benefit association)
MIC (Mutual insurance company)
NFP (Not-for-profit corporation)
SA (S.A.)
SAVINGS_COMPANY (Savings company)
SAVINGS_UNION (Savings union)
SARL (Soci\xc3\xa9t\xc3\xa9 \xc3\xa0 responsabilit\xc3\xa9 limit\xc3\xa9e)
TRUST (Trust)
ULC (Unlimited liability corporation)


CA_LEGAL_TYPE   When ContactType is PERSON , valid values include the following:
ABO (Aboriginal Peoples indigenous to Canada)
CCT (Canadian citizen)
LGR (Legal Representative of a Canadian Citizen or Permanent Resident)
RES (Permanent resident of Canada)



When ContactType is a value other than PERSON , valid values include the following:


ASS (Canadian unincorporated association)
CCO (Canadian corporation)
EDU (Canadian educational institution)
GOV (Government or government entity in Canada)
HOP (Canadian Hospital)
INB (Indian Band recognized by the Indian Act of Canada)
LAM (Canadian Library, Archive, or Museum)
MAJ (Her/His Majesty the Queen/King)
OMK (Official mark registered in Canada)
PLT (Canadian Political Party)
PRT (Partnership Registered in Canada)
TDM (Trademark registered in Canada)
TRD (Canadian Trade Union)
TRS (Trust established in Canada)

.es


ES_IDENTIFICATION   Specify the applicable value:
For contacts inside Spain: Enter your passport ID.
For contacts outside of Spain: Enter the VAT identification number for the company.


Note
For .es domains, the value of ContactType must be PERSON .


ES_IDENTIFICATION_TYPE   Valid values include the following:
DNI_AND_NIF (For Spanish contacts)
NIE (For foreigners with legal residence)
OTHER (For contacts outside of Spain)


ES_LEGAL_FORM   Valid values include the following:
ASSOCIATION
CENTRAL_GOVERNMENT_BODY
CIVIL_SOCIETY
COMMUNITY_OF_OWNERS
COMMUNITY_PROPERTY
CONSULATE
COOPERATIVE
DESIGNATION_OF_ORIGIN_SUPERVISORY_COUNCIL
ECONOMIC_INTEREST_GROUP
EMBASSY
ENTITY_MANAGING_NATURAL_AREAS
FARM_PARTNERSHIP
FOUNDATION
GENERAL_AND_LIMITED_PARTNERSHIP
GENERAL_PARTNERSHIP
INDIVIDUAL
LIMITED_COMPANY
LOCAL_AUTHORITY
LOCAL_PUBLIC_ENTITY
MUTUAL_INSURANCE_COMPANY
NATIONAL_PUBLIC_ENTITY
ORDER_OR_RELIGIOUS_INSTITUTION
OTHERS (Only for contacts outside of Spain)
POLITICAL_PARTY
PROFESSIONAL_ASSOCIATION
PUBLIC_LAW_ASSOCIATION
PUBLIC_LIMITED_COMPANY
REGIONAL_GOVERNMENT_BODY
REGIONAL_PUBLIC_ENTITY
SAVINGS_BANK
SPANISH_OFFICE
SPORTS_ASSOCIATION
SPORTS_FEDERATION
SPORTS_LIMITED_COMPANY
TEMPORARY_ALLIANCE_OF_ENTERPRISES
TRADE_UNION
WORKER_OWNED_COMPANY
WORKER_OWNED_LIMITED_COMPANY

.fi

BIRTH_DATE_IN_YYYY_MM_DD
FI_BUSINESS_NUMBER
FI_ID_NUMBER
FI_NATIONALITY   Valid values include the following:
FINNISH
NOT_FINNISH


FI_ORGANIZATION_TYPE   Valid values include the following:
COMPANY
CORPORATION
GOVERNMENT
INSTITUTION
POLITICAL_PARTY
PUBLIC_COMMUNITY
TOWNSHIP

.fr

BIRTH_CITY
BIRTH_COUNTRY
BIRTH_DATE_IN_YYYY_MM_DD
BIRTH_DEPARTMENT : Specify the INSEE code that corresponds with the department where the contact was born. If the contact was born somewhere other than France or its overseas departments, specify 99 . For more information, including a list of departments and the corresponding INSEE numbers, see the Wikipedia entry Departments of France .
BRAND_NUMBER.it

IT_NATIONALITY
IT_PIN
IT_REGISTRANT_ENTITY_TYPE   Valid values include the following:
FOREIGNERS
FREELANCE_WORKERS (Freelance workers and professionals)
ITALIAN_COMPANIES (Italian companies and one-person companies)
NON_PROFIT_ORGANIZATIONS
OTHER_SUBJECTS
PUBLIC_ORGANIZATIONS

.ru

BIRTH_DATE_IN_YYYY_MM_DD
RU_PASSPORT_DATA.se

BIRTH_COUNTRY
SE_ID_NUMBER.sg

SG_ID_NUMBER.co.uk, .me.uk, and .org.uk

UK_CONTACT_TYPE   Valid values include the following:
CRC (UK Corporation by Royal Charter)
FCORP (Non-UK Corporation)
FIND (Non-UK Individual, representing self)
FOTHER (Non-UK Entity that does not fit into any other category)
GOV (UK Government Body)
IND (UK Individual (representing self))
IP (UK Industrial/Provident Registered Company)
LLP (UK Limited Liability Partnership)
LTD (UK Limited Company)
OTHER (UK Entity that does not fit into any other category)
PLC (UK Public Limited Company)
PTNR (UK Partnership)
RCHAR (UK Registered Charity)
SCH (UK School)
STAT (UK Statutory Body)
STRA (UK Sole Trader)


UK_COMPANY_NUMBER

In addition, many TLDs require a VAT_NUMBER .

Value (string) --The value that corresponds with the name of an extra parameter.







RegistrantContact (dict) --Provides details about the domain registrant.

FirstName (string) --First name of contact.

LastName (string) --Last name of contact.

ContactType (string) --Indicates whether the contact is a person, company, association, or public organization. Note the following:

If you specify a value other than PERSON , you must also specify a value for OrganizationName .
For some TLDs, the privacy protection available depends on the value that you specify for Contact Type . For the privacy protection settings for your TLD, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide
For .es domains, if you specify PERSON , you must specify INDIVIDUAL for the value of ES_LEGAL_FORM .


OrganizationName (string) --Name of the organization for contact types other than PERSON .

AddressLine1 (string) --First line of the contact\'s address.

AddressLine2 (string) --Second line of contact\'s address, if any.

City (string) --The city of the contact\'s address.

State (string) --The state or province of the contact\'s city.

CountryCode (string) --Code for the country of the contact\'s address.

ZipCode (string) --The zip or postal code of the contact\'s address.

PhoneNumber (string) --The phone number of the contact.
Constraints: Phone number must be specified in the format "+[country dialing code].[number including any area code>]". For example, a US phone number might appear as "+1.1234567890" .

Email (string) --Email address of the contact.

Fax (string) --Fax number of the contact.
Constraints: Phone number must be specified in the format "+[country dialing code].[number including any area code]". For example, a US phone number might appear as "+1.1234567890" .

ExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.

(dict) --ExtraParam includes the following elements.

Name (string) --The name of an additional parameter that is required by a top-level domain. Here are the top-level domains that require additional parameters and the names of the parameters that they require:

.com.au and .net.au

AU_ID_NUMBER
AU_ID_TYPE   Valid values include the following:
ABN (Australian business number)
ACN (Australian company number)
TM (Trademark number)

.ca

BRAND_NUMBER
CA_BUSINESS_ENTITY_TYPE   Valid values include the following:
BANK (Bank)
COMMERCIAL_COMPANY (Commercial company)
COMPANY (Company)
COOPERATION (Cooperation)
COOPERATIVE (Cooperative)
COOPRIX (Cooprix)
CORP (Corporation)
CREDIT_UNION (Credit union)
FOMIA (Federation of mutual insurance associations)
INC (Incorporated)
LTD (Limited)
LTEE (Limit\xc3\xa9e)
LLC (Limited liability corporation)
LLP (Limited liability partnership)
LTE (Lte.)
MBA (Mutual benefit association)
MIC (Mutual insurance company)
NFP (Not-for-profit corporation)
SA (S.A.)
SAVINGS_COMPANY (Savings company)
SAVINGS_UNION (Savings union)
SARL (Soci\xc3\xa9t\xc3\xa9 \xc3\xa0 responsabilit\xc3\xa9 limit\xc3\xa9e)
TRUST (Trust)
ULC (Unlimited liability corporation)


CA_LEGAL_TYPE   When ContactType is PERSON , valid values include the following:
ABO (Aboriginal Peoples indigenous to Canada)
CCT (Canadian citizen)
LGR (Legal Representative of a Canadian Citizen or Permanent Resident)
RES (Permanent resident of Canada)



When ContactType is a value other than PERSON , valid values include the following:


ASS (Canadian unincorporated association)
CCO (Canadian corporation)
EDU (Canadian educational institution)
GOV (Government or government entity in Canada)
HOP (Canadian Hospital)
INB (Indian Band recognized by the Indian Act of Canada)
LAM (Canadian Library, Archive, or Museum)
MAJ (Her/His Majesty the Queen/King)
OMK (Official mark registered in Canada)
PLT (Canadian Political Party)
PRT (Partnership Registered in Canada)
TDM (Trademark registered in Canada)
TRD (Canadian Trade Union)
TRS (Trust established in Canada)

.es


ES_IDENTIFICATION   Specify the applicable value:
For contacts inside Spain: Enter your passport ID.
For contacts outside of Spain: Enter the VAT identification number for the company.


Note
For .es domains, the value of ContactType must be PERSON .


ES_IDENTIFICATION_TYPE   Valid values include the following:
DNI_AND_NIF (For Spanish contacts)
NIE (For foreigners with legal residence)
OTHER (For contacts outside of Spain)


ES_LEGAL_FORM   Valid values include the following:
ASSOCIATION
CENTRAL_GOVERNMENT_BODY
CIVIL_SOCIETY
COMMUNITY_OF_OWNERS
COMMUNITY_PROPERTY
CONSULATE
COOPERATIVE
DESIGNATION_OF_ORIGIN_SUPERVISORY_COUNCIL
ECONOMIC_INTEREST_GROUP
EMBASSY
ENTITY_MANAGING_NATURAL_AREAS
FARM_PARTNERSHIP
FOUNDATION
GENERAL_AND_LIMITED_PARTNERSHIP
GENERAL_PARTNERSHIP
INDIVIDUAL
LIMITED_COMPANY
LOCAL_AUTHORITY
LOCAL_PUBLIC_ENTITY
MUTUAL_INSURANCE_COMPANY
NATIONAL_PUBLIC_ENTITY
ORDER_OR_RELIGIOUS_INSTITUTION
OTHERS (Only for contacts outside of Spain)
POLITICAL_PARTY
PROFESSIONAL_ASSOCIATION
PUBLIC_LAW_ASSOCIATION
PUBLIC_LIMITED_COMPANY
REGIONAL_GOVERNMENT_BODY
REGIONAL_PUBLIC_ENTITY
SAVINGS_BANK
SPANISH_OFFICE
SPORTS_ASSOCIATION
SPORTS_FEDERATION
SPORTS_LIMITED_COMPANY
TEMPORARY_ALLIANCE_OF_ENTERPRISES
TRADE_UNION
WORKER_OWNED_COMPANY
WORKER_OWNED_LIMITED_COMPANY

.fi

BIRTH_DATE_IN_YYYY_MM_DD
FI_BUSINESS_NUMBER
FI_ID_NUMBER
FI_NATIONALITY   Valid values include the following:
FINNISH
NOT_FINNISH


FI_ORGANIZATION_TYPE   Valid values include the following:
COMPANY
CORPORATION
GOVERNMENT
INSTITUTION
POLITICAL_PARTY
PUBLIC_COMMUNITY
TOWNSHIP

.fr

BIRTH_CITY
BIRTH_COUNTRY
BIRTH_DATE_IN_YYYY_MM_DD
BIRTH_DEPARTMENT : Specify the INSEE code that corresponds with the department where the contact was born. If the contact was born somewhere other than France or its overseas departments, specify 99 . For more information, including a list of departments and the corresponding INSEE numbers, see the Wikipedia entry Departments of France .
BRAND_NUMBER.it

IT_NATIONALITY
IT_PIN
IT_REGISTRANT_ENTITY_TYPE   Valid values include the following:
FOREIGNERS
FREELANCE_WORKERS (Freelance workers and professionals)
ITALIAN_COMPANIES (Italian companies and one-person companies)
NON_PROFIT_ORGANIZATIONS
OTHER_SUBJECTS
PUBLIC_ORGANIZATIONS

.ru

BIRTH_DATE_IN_YYYY_MM_DD
RU_PASSPORT_DATA.se

BIRTH_COUNTRY
SE_ID_NUMBER.sg

SG_ID_NUMBER.co.uk, .me.uk, and .org.uk

UK_CONTACT_TYPE   Valid values include the following:
CRC (UK Corporation by Royal Charter)
FCORP (Non-UK Corporation)
FIND (Non-UK Individual, representing self)
FOTHER (Non-UK Entity that does not fit into any other category)
GOV (UK Government Body)
IND (UK Individual (representing self))
IP (UK Industrial/Provident Registered Company)
LLP (UK Limited Liability Partnership)
LTD (UK Limited Company)
OTHER (UK Entity that does not fit into any other category)
PLC (UK Public Limited Company)
PTNR (UK Partnership)
RCHAR (UK Registered Charity)
SCH (UK School)
STAT (UK Statutory Body)
STRA (UK Sole Trader)


UK_COMPANY_NUMBER

In addition, many TLDs require a VAT_NUMBER .

Value (string) --The value that corresponds with the name of an extra parameter.







TechContact (dict) --Provides details about the domain technical contact.

FirstName (string) --First name of contact.

LastName (string) --Last name of contact.

ContactType (string) --Indicates whether the contact is a person, company, association, or public organization. Note the following:

If you specify a value other than PERSON , you must also specify a value for OrganizationName .
For some TLDs, the privacy protection available depends on the value that you specify for Contact Type . For the privacy protection settings for your TLD, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide
For .es domains, if you specify PERSON , you must specify INDIVIDUAL for the value of ES_LEGAL_FORM .


OrganizationName (string) --Name of the organization for contact types other than PERSON .

AddressLine1 (string) --First line of the contact\'s address.

AddressLine2 (string) --Second line of contact\'s address, if any.

City (string) --The city of the contact\'s address.

State (string) --The state or province of the contact\'s city.

CountryCode (string) --Code for the country of the contact\'s address.

ZipCode (string) --The zip or postal code of the contact\'s address.

PhoneNumber (string) --The phone number of the contact.
Constraints: Phone number must be specified in the format "+[country dialing code].[number including any area code>]". For example, a US phone number might appear as "+1.1234567890" .

Email (string) --Email address of the contact.

Fax (string) --Fax number of the contact.
Constraints: Phone number must be specified in the format "+[country dialing code].[number including any area code]". For example, a US phone number might appear as "+1.1234567890" .

ExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.

(dict) --ExtraParam includes the following elements.

Name (string) --The name of an additional parameter that is required by a top-level domain. Here are the top-level domains that require additional parameters and the names of the parameters that they require:

.com.au and .net.au

AU_ID_NUMBER
AU_ID_TYPE   Valid values include the following:
ABN (Australian business number)
ACN (Australian company number)
TM (Trademark number)

.ca

BRAND_NUMBER
CA_BUSINESS_ENTITY_TYPE   Valid values include the following:
BANK (Bank)
COMMERCIAL_COMPANY (Commercial company)
COMPANY (Company)
COOPERATION (Cooperation)
COOPERATIVE (Cooperative)
COOPRIX (Cooprix)
CORP (Corporation)
CREDIT_UNION (Credit union)
FOMIA (Federation of mutual insurance associations)
INC (Incorporated)
LTD (Limited)
LTEE (Limit\xc3\xa9e)
LLC (Limited liability corporation)
LLP (Limited liability partnership)
LTE (Lte.)
MBA (Mutual benefit association)
MIC (Mutual insurance company)
NFP (Not-for-profit corporation)
SA (S.A.)
SAVINGS_COMPANY (Savings company)
SAVINGS_UNION (Savings union)
SARL (Soci\xc3\xa9t\xc3\xa9 \xc3\xa0 responsabilit\xc3\xa9 limit\xc3\xa9e)
TRUST (Trust)
ULC (Unlimited liability corporation)


CA_LEGAL_TYPE   When ContactType is PERSON , valid values include the following:
ABO (Aboriginal Peoples indigenous to Canada)
CCT (Canadian citizen)
LGR (Legal Representative of a Canadian Citizen or Permanent Resident)
RES (Permanent resident of Canada)



When ContactType is a value other than PERSON , valid values include the following:


ASS (Canadian unincorporated association)
CCO (Canadian corporation)
EDU (Canadian educational institution)
GOV (Government or government entity in Canada)
HOP (Canadian Hospital)
INB (Indian Band recognized by the Indian Act of Canada)
LAM (Canadian Library, Archive, or Museum)
MAJ (Her/His Majesty the Queen/King)
OMK (Official mark registered in Canada)
PLT (Canadian Political Party)
PRT (Partnership Registered in Canada)
TDM (Trademark registered in Canada)
TRD (Canadian Trade Union)
TRS (Trust established in Canada)

.es


ES_IDENTIFICATION   Specify the applicable value:
For contacts inside Spain: Enter your passport ID.
For contacts outside of Spain: Enter the VAT identification number for the company.


Note
For .es domains, the value of ContactType must be PERSON .


ES_IDENTIFICATION_TYPE   Valid values include the following:
DNI_AND_NIF (For Spanish contacts)
NIE (For foreigners with legal residence)
OTHER (For contacts outside of Spain)


ES_LEGAL_FORM   Valid values include the following:
ASSOCIATION
CENTRAL_GOVERNMENT_BODY
CIVIL_SOCIETY
COMMUNITY_OF_OWNERS
COMMUNITY_PROPERTY
CONSULATE
COOPERATIVE
DESIGNATION_OF_ORIGIN_SUPERVISORY_COUNCIL
ECONOMIC_INTEREST_GROUP
EMBASSY
ENTITY_MANAGING_NATURAL_AREAS
FARM_PARTNERSHIP
FOUNDATION
GENERAL_AND_LIMITED_PARTNERSHIP
GENERAL_PARTNERSHIP
INDIVIDUAL
LIMITED_COMPANY
LOCAL_AUTHORITY
LOCAL_PUBLIC_ENTITY
MUTUAL_INSURANCE_COMPANY
NATIONAL_PUBLIC_ENTITY
ORDER_OR_RELIGIOUS_INSTITUTION
OTHERS (Only for contacts outside of Spain)
POLITICAL_PARTY
PROFESSIONAL_ASSOCIATION
PUBLIC_LAW_ASSOCIATION
PUBLIC_LIMITED_COMPANY
REGIONAL_GOVERNMENT_BODY
REGIONAL_PUBLIC_ENTITY
SAVINGS_BANK
SPANISH_OFFICE
SPORTS_ASSOCIATION
SPORTS_FEDERATION
SPORTS_LIMITED_COMPANY
TEMPORARY_ALLIANCE_OF_ENTERPRISES
TRADE_UNION
WORKER_OWNED_COMPANY
WORKER_OWNED_LIMITED_COMPANY

.fi

BIRTH_DATE_IN_YYYY_MM_DD
FI_BUSINESS_NUMBER
FI_ID_NUMBER
FI_NATIONALITY   Valid values include the following:
FINNISH
NOT_FINNISH


FI_ORGANIZATION_TYPE   Valid values include the following:
COMPANY
CORPORATION
GOVERNMENT
INSTITUTION
POLITICAL_PARTY
PUBLIC_COMMUNITY
TOWNSHIP

.fr

BIRTH_CITY
BIRTH_COUNTRY
BIRTH_DATE_IN_YYYY_MM_DD
BIRTH_DEPARTMENT : Specify the INSEE code that corresponds with the department where the contact was born. If the contact was born somewhere other than France or its overseas departments, specify 99 . For more information, including a list of departments and the corresponding INSEE numbers, see the Wikipedia entry Departments of France .
BRAND_NUMBER.it

IT_NATIONALITY
IT_PIN
IT_REGISTRANT_ENTITY_TYPE   Valid values include the following:
FOREIGNERS
FREELANCE_WORKERS (Freelance workers and professionals)
ITALIAN_COMPANIES (Italian companies and one-person companies)
NON_PROFIT_ORGANIZATIONS
OTHER_SUBJECTS
PUBLIC_ORGANIZATIONS

.ru

BIRTH_DATE_IN_YYYY_MM_DD
RU_PASSPORT_DATA.se

BIRTH_COUNTRY
SE_ID_NUMBER.sg

SG_ID_NUMBER.co.uk, .me.uk, and .org.uk

UK_CONTACT_TYPE   Valid values include the following:
CRC (UK Corporation by Royal Charter)
FCORP (Non-UK Corporation)
FIND (Non-UK Individual, representing self)
FOTHER (Non-UK Entity that does not fit into any other category)
GOV (UK Government Body)
IND (UK Individual (representing self))
IP (UK Industrial/Provident Registered Company)
LLP (UK Limited Liability Partnership)
LTD (UK Limited Company)
OTHER (UK Entity that does not fit into any other category)
PLC (UK Public Limited Company)
PTNR (UK Partnership)
RCHAR (UK Registered Charity)
SCH (UK School)
STAT (UK Statutory Body)
STRA (UK Sole Trader)


UK_COMPANY_NUMBER

In addition, many TLDs require a VAT_NUMBER .

Value (string) --The value that corresponds with the name of an extra parameter.







AdminPrivacy (boolean) --Specifies whether contact information is concealed from WHOIS queries. If the value is true , WHOIS ("who is") queries return contact information either for Amazon Registrar (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other TLDs). If the value is false , WHOIS queries return the information that you entered for the admin contact.

RegistrantPrivacy (boolean) --Specifies whether contact information is concealed from WHOIS queries. If the value is true , WHOIS ("who is") queries return contact information either for Amazon Registrar (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other TLDs). If the value is false , WHOIS queries return the information that you entered for the registrant contact (domain owner).

TechPrivacy (boolean) --Specifies whether contact information is concealed from WHOIS queries. If the value is true , WHOIS ("who is") queries return contact information either for Amazon Registrar (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other TLDs). If the value is false , WHOIS queries return the information that you entered for the technical contact.

RegistrarName (string) --Name of the registrar of the domain as identified in the registry. Domains with a .com, .net, or .org TLD are registered by Amazon Registrar. All other domains are registered by our registrar associate, Gandi. The value for domains that are registered by Gandi is "GANDI SAS" .

WhoIsServer (string) --The fully qualified name of the WHOIS server that can answer the WHOIS query for the domain.

RegistrarUrl (string) --Web address of the registrar.

AbuseContactEmail (string) --Email address to contact to report incorrect contact information for a domain, to report that the domain is being used to send spam, to report that someone is cybersquatting on a domain name, or report some other type of abuse.

AbuseContactPhone (string) --Phone number for reporting abuse.

RegistryDomainId (string) --Reserved for future use.

CreationDate (datetime) --The date when the domain was created as found in the response to a WHOIS query. The date and time is in Unix time format and Coordinated Universal time (UTC).

UpdatedDate (datetime) --The last updated date of the domain as found in the response to a WHOIS query. The date and time is in Unix time format and Coordinated Universal time (UTC).

ExpirationDate (datetime) --The date when the registration for the domain is set to expire. The date and time is in Unix time format and Coordinated Universal time (UTC).

Reseller (string) --Reseller of the domain. Domains registered or transferred using Route 53 domains will have "Amazon" as the reseller.

DnsSec (string) --Reserved for future use.

StatusList (list) --An array of domain name status codes, also known as Extensible Provisioning Protocol (EPP) status codes.
ICANN, the organization that maintains a central database of domain names, has developed a set of domain name status codes that tell you the status of a variety of operations on a domain name, for example, registering a domain name, transferring a domain name to another registrar, renewing the registration for a domain name, and so on. All registrars use this same set of status codes.
For a current list of domain name status codes and an explanation of what each code means, go to the ICANN website and search for epp status codes . (Search on the ICANN website; web searches sometimes return an old version of the document.)

(string) --







Exceptions

Route53Domains.Client.exceptions.InvalidInput
Route53Domains.Client.exceptions.UnsupportedTLD


    :return: {
        'DomainName': 'string',
        'Nameservers': [
            {
                'Name': 'string',
                'GlueIps': [
                    'string',
                ]
            },
        ],
        'AutoRenew': True|False,
        'AdminContact': {
            'FirstName': 'string',
            'LastName': 'string',
            'ContactType': 'PERSON'|'COMPANY'|'ASSOCIATION'|'PUBLIC_BODY'|'RESELLER',
            'OrganizationName': 'string',
            'AddressLine1': 'string',
            'AddressLine2': 'string',
            'City': 'string',
            'State': 'string',
            'CountryCode': 'AD'|'AE'|'AF'|'AG'|'AI'|'AL'|'AM'|'AN'|'AO'|'AQ'|'AR'|'AS'|'AT'|'AU'|'AW'|'AZ'|'BA'|'BB'|'BD'|'BE'|'BF'|'BG'|'BH'|'BI'|'BJ'|'BL'|'BM'|'BN'|'BO'|'BR'|'BS'|'BT'|'BW'|'BY'|'BZ'|'CA'|'CC'|'CD'|'CF'|'CG'|'CH'|'CI'|'CK'|'CL'|'CM'|'CN'|'CO'|'CR'|'CU'|'CV'|'CX'|'CY'|'CZ'|'DE'|'DJ'|'DK'|'DM'|'DO'|'DZ'|'EC'|'EE'|'EG'|'ER'|'ES'|'ET'|'FI'|'FJ'|'FK'|'FM'|'FO'|'FR'|'GA'|'GB'|'GD'|'GE'|'GH'|'GI'|'GL'|'GM'|'GN'|'GQ'|'GR'|'GT'|'GU'|'GW'|'GY'|'HK'|'HN'|'HR'|'HT'|'HU'|'ID'|'IE'|'IL'|'IM'|'IN'|'IQ'|'IR'|'IS'|'IT'|'JM'|'JO'|'JP'|'KE'|'KG'|'KH'|'KI'|'KM'|'KN'|'KP'|'KR'|'KW'|'KY'|'KZ'|'LA'|'LB'|'LC'|'LI'|'LK'|'LR'|'LS'|'LT'|'LU'|'LV'|'LY'|'MA'|'MC'|'MD'|'ME'|'MF'|'MG'|'MH'|'MK'|'ML'|'MM'|'MN'|'MO'|'MP'|'MR'|'MS'|'MT'|'MU'|'MV'|'MW'|'MX'|'MY'|'MZ'|'NA'|'NC'|'NE'|'NG'|'NI'|'NL'|'NO'|'NP'|'NR'|'NU'|'NZ'|'OM'|'PA'|'PE'|'PF'|'PG'|'PH'|'PK'|'PL'|'PM'|'PN'|'PR'|'PT'|'PW'|'PY'|'QA'|'RO'|'RS'|'RU'|'RW'|'SA'|'SB'|'SC'|'SD'|'SE'|'SG'|'SH'|'SI'|'SK'|'SL'|'SM'|'SN'|'SO'|'SR'|'ST'|'SV'|'SY'|'SZ'|'TC'|'TD'|'TG'|'TH'|'TJ'|'TK'|'TL'|'TM'|'TN'|'TO'|'TR'|'TT'|'TV'|'TW'|'TZ'|'UA'|'UG'|'US'|'UY'|'UZ'|'VA'|'VC'|'VE'|'VG'|'VI'|'VN'|'VU'|'WF'|'WS'|'YE'|'YT'|'ZA'|'ZM'|'ZW',
            'ZipCode': 'string',
            'PhoneNumber': 'string',
            'Email': 'string',
            'Fax': 'string',
            'ExtraParams': [
                {
                    'Name': 'DUNS_NUMBER'|'BRAND_NUMBER'|'BIRTH_DEPARTMENT'|'BIRTH_DATE_IN_YYYY_MM_DD'|'BIRTH_COUNTRY'|'BIRTH_CITY'|'DOCUMENT_NUMBER'|'AU_ID_NUMBER'|'AU_ID_TYPE'|'CA_LEGAL_TYPE'|'CA_BUSINESS_ENTITY_TYPE'|'CA_LEGAL_REPRESENTATIVE'|'CA_LEGAL_REPRESENTATIVE_CAPACITY'|'ES_IDENTIFICATION'|'ES_IDENTIFICATION_TYPE'|'ES_LEGAL_FORM'|'FI_BUSINESS_NUMBER'|'FI_ID_NUMBER'|'FI_NATIONALITY'|'FI_ORGANIZATION_TYPE'|'IT_NATIONALITY'|'IT_PIN'|'IT_REGISTRANT_ENTITY_TYPE'|'RU_PASSPORT_DATA'|'SE_ID_NUMBER'|'SG_ID_NUMBER'|'VAT_NUMBER'|'UK_CONTACT_TYPE'|'UK_COMPANY_NUMBER',
                    'Value': 'string'
                },
            ]
        },
        'RegistrantContact': {
            'FirstName': 'string',
            'LastName': 'string',
            'ContactType': 'PERSON'|'COMPANY'|'ASSOCIATION'|'PUBLIC_BODY'|'RESELLER',
            'OrganizationName': 'string',
            'AddressLine1': 'string',
            'AddressLine2': 'string',
            'City': 'string',
            'State': 'string',
            'CountryCode': 'AD'|'AE'|'AF'|'AG'|'AI'|'AL'|'AM'|'AN'|'AO'|'AQ'|'AR'|'AS'|'AT'|'AU'|'AW'|'AZ'|'BA'|'BB'|'BD'|'BE'|'BF'|'BG'|'BH'|'BI'|'BJ'|'BL'|'BM'|'BN'|'BO'|'BR'|'BS'|'BT'|'BW'|'BY'|'BZ'|'CA'|'CC'|'CD'|'CF'|'CG'|'CH'|'CI'|'CK'|'CL'|'CM'|'CN'|'CO'|'CR'|'CU'|'CV'|'CX'|'CY'|'CZ'|'DE'|'DJ'|'DK'|'DM'|'DO'|'DZ'|'EC'|'EE'|'EG'|'ER'|'ES'|'ET'|'FI'|'FJ'|'FK'|'FM'|'FO'|'FR'|'GA'|'GB'|'GD'|'GE'|'GH'|'GI'|'GL'|'GM'|'GN'|'GQ'|'GR'|'GT'|'GU'|'GW'|'GY'|'HK'|'HN'|'HR'|'HT'|'HU'|'ID'|'IE'|'IL'|'IM'|'IN'|'IQ'|'IR'|'IS'|'IT'|'JM'|'JO'|'JP'|'KE'|'KG'|'KH'|'KI'|'KM'|'KN'|'KP'|'KR'|'KW'|'KY'|'KZ'|'LA'|'LB'|'LC'|'LI'|'LK'|'LR'|'LS'|'LT'|'LU'|'LV'|'LY'|'MA'|'MC'|'MD'|'ME'|'MF'|'MG'|'MH'|'MK'|'ML'|'MM'|'MN'|'MO'|'MP'|'MR'|'MS'|'MT'|'MU'|'MV'|'MW'|'MX'|'MY'|'MZ'|'NA'|'NC'|'NE'|'NG'|'NI'|'NL'|'NO'|'NP'|'NR'|'NU'|'NZ'|'OM'|'PA'|'PE'|'PF'|'PG'|'PH'|'PK'|'PL'|'PM'|'PN'|'PR'|'PT'|'PW'|'PY'|'QA'|'RO'|'RS'|'RU'|'RW'|'SA'|'SB'|'SC'|'SD'|'SE'|'SG'|'SH'|'SI'|'SK'|'SL'|'SM'|'SN'|'SO'|'SR'|'ST'|'SV'|'SY'|'SZ'|'TC'|'TD'|'TG'|'TH'|'TJ'|'TK'|'TL'|'TM'|'TN'|'TO'|'TR'|'TT'|'TV'|'TW'|'TZ'|'UA'|'UG'|'US'|'UY'|'UZ'|'VA'|'VC'|'VE'|'VG'|'VI'|'VN'|'VU'|'WF'|'WS'|'YE'|'YT'|'ZA'|'ZM'|'ZW',
            'ZipCode': 'string',
            'PhoneNumber': 'string',
            'Email': 'string',
            'Fax': 'string',
            'ExtraParams': [
                {
                    'Name': 'DUNS_NUMBER'|'BRAND_NUMBER'|'BIRTH_DEPARTMENT'|'BIRTH_DATE_IN_YYYY_MM_DD'|'BIRTH_COUNTRY'|'BIRTH_CITY'|'DOCUMENT_NUMBER'|'AU_ID_NUMBER'|'AU_ID_TYPE'|'CA_LEGAL_TYPE'|'CA_BUSINESS_ENTITY_TYPE'|'CA_LEGAL_REPRESENTATIVE'|'CA_LEGAL_REPRESENTATIVE_CAPACITY'|'ES_IDENTIFICATION'|'ES_IDENTIFICATION_TYPE'|'ES_LEGAL_FORM'|'FI_BUSINESS_NUMBER'|'FI_ID_NUMBER'|'FI_NATIONALITY'|'FI_ORGANIZATION_TYPE'|'IT_NATIONALITY'|'IT_PIN'|'IT_REGISTRANT_ENTITY_TYPE'|'RU_PASSPORT_DATA'|'SE_ID_NUMBER'|'SG_ID_NUMBER'|'VAT_NUMBER'|'UK_CONTACT_TYPE'|'UK_COMPANY_NUMBER',
                    'Value': 'string'
                },
            ]
        },
        'TechContact': {
            'FirstName': 'string',
            'LastName': 'string',
            'ContactType': 'PERSON'|'COMPANY'|'ASSOCIATION'|'PUBLIC_BODY'|'RESELLER',
            'OrganizationName': 'string',
            'AddressLine1': 'string',
            'AddressLine2': 'string',
            'City': 'string',
            'State': 'string',
            'CountryCode': 'AD'|'AE'|'AF'|'AG'|'AI'|'AL'|'AM'|'AN'|'AO'|'AQ'|'AR'|'AS'|'AT'|'AU'|'AW'|'AZ'|'BA'|'BB'|'BD'|'BE'|'BF'|'BG'|'BH'|'BI'|'BJ'|'BL'|'BM'|'BN'|'BO'|'BR'|'BS'|'BT'|'BW'|'BY'|'BZ'|'CA'|'CC'|'CD'|'CF'|'CG'|'CH'|'CI'|'CK'|'CL'|'CM'|'CN'|'CO'|'CR'|'CU'|'CV'|'CX'|'CY'|'CZ'|'DE'|'DJ'|'DK'|'DM'|'DO'|'DZ'|'EC'|'EE'|'EG'|'ER'|'ES'|'ET'|'FI'|'FJ'|'FK'|'FM'|'FO'|'FR'|'GA'|'GB'|'GD'|'GE'|'GH'|'GI'|'GL'|'GM'|'GN'|'GQ'|'GR'|'GT'|'GU'|'GW'|'GY'|'HK'|'HN'|'HR'|'HT'|'HU'|'ID'|'IE'|'IL'|'IM'|'IN'|'IQ'|'IR'|'IS'|'IT'|'JM'|'JO'|'JP'|'KE'|'KG'|'KH'|'KI'|'KM'|'KN'|'KP'|'KR'|'KW'|'KY'|'KZ'|'LA'|'LB'|'LC'|'LI'|'LK'|'LR'|'LS'|'LT'|'LU'|'LV'|'LY'|'MA'|'MC'|'MD'|'ME'|'MF'|'MG'|'MH'|'MK'|'ML'|'MM'|'MN'|'MO'|'MP'|'MR'|'MS'|'MT'|'MU'|'MV'|'MW'|'MX'|'MY'|'MZ'|'NA'|'NC'|'NE'|'NG'|'NI'|'NL'|'NO'|'NP'|'NR'|'NU'|'NZ'|'OM'|'PA'|'PE'|'PF'|'PG'|'PH'|'PK'|'PL'|'PM'|'PN'|'PR'|'PT'|'PW'|'PY'|'QA'|'RO'|'RS'|'RU'|'RW'|'SA'|'SB'|'SC'|'SD'|'SE'|'SG'|'SH'|'SI'|'SK'|'SL'|'SM'|'SN'|'SO'|'SR'|'ST'|'SV'|'SY'|'SZ'|'TC'|'TD'|'TG'|'TH'|'TJ'|'TK'|'TL'|'TM'|'TN'|'TO'|'TR'|'TT'|'TV'|'TW'|'TZ'|'UA'|'UG'|'US'|'UY'|'UZ'|'VA'|'VC'|'VE'|'VG'|'VI'|'VN'|'VU'|'WF'|'WS'|'YE'|'YT'|'ZA'|'ZM'|'ZW',
            'ZipCode': 'string',
            'PhoneNumber': 'string',
            'Email': 'string',
            'Fax': 'string',
            'ExtraParams': [
                {
                    'Name': 'DUNS_NUMBER'|'BRAND_NUMBER'|'BIRTH_DEPARTMENT'|'BIRTH_DATE_IN_YYYY_MM_DD'|'BIRTH_COUNTRY'|'BIRTH_CITY'|'DOCUMENT_NUMBER'|'AU_ID_NUMBER'|'AU_ID_TYPE'|'CA_LEGAL_TYPE'|'CA_BUSINESS_ENTITY_TYPE'|'CA_LEGAL_REPRESENTATIVE'|'CA_LEGAL_REPRESENTATIVE_CAPACITY'|'ES_IDENTIFICATION'|'ES_IDENTIFICATION_TYPE'|'ES_LEGAL_FORM'|'FI_BUSINESS_NUMBER'|'FI_ID_NUMBER'|'FI_NATIONALITY'|'FI_ORGANIZATION_TYPE'|'IT_NATIONALITY'|'IT_PIN'|'IT_REGISTRANT_ENTITY_TYPE'|'RU_PASSPORT_DATA'|'SE_ID_NUMBER'|'SG_ID_NUMBER'|'VAT_NUMBER'|'UK_CONTACT_TYPE'|'UK_COMPANY_NUMBER',
                    'Value': 'string'
                },
            ]
        },
        'AdminPrivacy': True|False,
        'RegistrantPrivacy': True|False,
        'TechPrivacy': True|False,
        'RegistrarName': 'string',
        'WhoIsServer': 'string',
        'RegistrarUrl': 'string',
        'AbuseContactEmail': 'string',
        'AbuseContactPhone': 'string',
        'RegistryDomainId': 'string',
        'CreationDate': datetime(2015, 1, 1),
        'UpdatedDate': datetime(2015, 1, 1),
        'ExpirationDate': datetime(2015, 1, 1),
        'Reseller': 'string',
        'DnsSec': 'string',
        'StatusList': [
            'string',
        ]
    }
    
    
    :returns: 
    If you specify a value other than PERSON , you must also specify a value for OrganizationName .
    For some TLDs, the privacy protection available depends on the value that you specify for Contact Type . For the privacy protection settings for your TLD, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide
    For .es domains, if you specify PERSON , you must specify INDIVIDUAL for the value of ES_LEGAL_FORM .
    
    """
    pass

def get_domain_suggestions(DomainName=None, SuggestionCount=None, OnlyAvailable=None):
    """
    The GetDomainSuggestions operation returns a list of suggested domain names.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_domain_suggestions(
        DomainName='string',
        SuggestionCount=123,
        OnlyAvailable=True|False
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]\nA domain name that you want to use as the basis for a list of possible domain names. The top-level domain (TLD), such as .com, must be a TLD that Route 53 supports. For a list of supported TLDs, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide .\nThe domain name can contain only the following characters:\n\nLetters a through z. Domain names are not case sensitive.\nNumbers 0 through 9.\nHyphen (-). You can\'t specify a hyphen at the beginning or end of a label.\nPeriod (.) to separate the labels in the name, such as the . in example.com .\n\nInternationalized domain names are not supported for some top-level domains. To determine whether the TLD that you want to use supports internationalized domain names, see Domains that You Can Register with Amazon Route 53 .\n

    :type SuggestionCount: integer
    :param SuggestionCount: [REQUIRED]\nThe number of suggested domain names that you want Route 53 to return. Specify a value between 1 and 50.\n

    :type OnlyAvailable: boolean
    :param OnlyAvailable: [REQUIRED]\nIf OnlyAvailable is true , Route 53 returns only domain names that are available. If OnlyAvailable is false , Route 53 returns domain names without checking whether they\'re available to be registered. To determine whether the domain is available, you can call checkDomainAvailability for each suggestion.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'SuggestionsList': [
        {
            'DomainName': 'string',
            'Availability': 'string'
        },
    ]
}


Response Structure

(dict) --

SuggestionsList (list) --
A list of possible domain names. If you specified true for OnlyAvailable in the request, the list contains only domains that are available for registration.

(dict) --
Information about one suggested domain name.

DomainName (string) --
A suggested domain name.

Availability (string) --
Whether the domain name is available for registering.

Note
You can register only the domains that are designated as AVAILABLE .

Valid values:

AVAILABLE

The domain name is available.

AVAILABLE_RESERVED

The domain name is reserved under specific conditions.

AVAILABLE_PREORDER

The domain name is available and can be preordered.

DONT_KNOW

The TLD registry didn\'t reply with a definitive answer about whether the domain name is available. Route 53 can return this response for a variety of reasons, for example, the registry is performing maintenance. Try again later.

PENDING

The TLD registry didn\'t return a response in the expected amount of time. When the response is delayed, it usually takes just a few extra seconds. You can resubmit the request immediately.

RESERVED

The domain name has been reserved for another person or organization.

UNAVAILABLE

The domain name is not available.

UNAVAILABLE_PREMIUM

The domain name is not available.

UNAVAILABLE_RESTRICTED

The domain name is forbidden.











Exceptions

Route53Domains.Client.exceptions.InvalidInput
Route53Domains.Client.exceptions.UnsupportedTLD


    :return: {
        'SuggestionsList': [
            {
                'DomainName': 'string',
                'Availability': 'string'
            },
        ]
    }
    
    
    :returns: 
    Route53Domains.Client.exceptions.InvalidInput
    Route53Domains.Client.exceptions.UnsupportedTLD
    
    """
    pass

def get_operation_detail(OperationId=None):
    """
    This operation returns the current status of an operation that is not completed.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_operation_detail(
        OperationId='string'
    )
    
    
    :type OperationId: string
    :param OperationId: [REQUIRED]\nThe identifier for the operation for which you want to get the status. Route 53 returned the identifier in the response to the original request.\n

    :rtype: dict
ReturnsResponse Syntax{
    'OperationId': 'string',
    'Status': 'SUBMITTED'|'IN_PROGRESS'|'ERROR'|'SUCCESSFUL'|'FAILED',
    'Message': 'string',
    'DomainName': 'string',
    'Type': 'REGISTER_DOMAIN'|'DELETE_DOMAIN'|'TRANSFER_IN_DOMAIN'|'UPDATE_DOMAIN_CONTACT'|'UPDATE_NAMESERVER'|'CHANGE_PRIVACY_PROTECTION'|'DOMAIN_LOCK'|'ENABLE_AUTORENEW'|'DISABLE_AUTORENEW'|'ADD_DNSSEC'|'REMOVE_DNSSEC'|'EXPIRE_DOMAIN'|'TRANSFER_OUT_DOMAIN'|'CHANGE_DOMAIN_OWNER'|'RENEW_DOMAIN'|'PUSH_DOMAIN'|'INTERNAL_TRANSFER_OUT_DOMAIN'|'INTERNAL_TRANSFER_IN_DOMAIN',
    'SubmittedDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --The GetOperationDetail response includes the following elements.

OperationId (string) --The identifier for the operation.

Status (string) --The current status of the requested operation in the system.

Message (string) --Detailed information on the status including possible errors.

DomainName (string) --The name of a domain.

Type (string) --The type of operation that was requested.

SubmittedDate (datetime) --The date when the request was submitted.






Exceptions

Route53Domains.Client.exceptions.InvalidInput


    :return: {
        'OperationId': 'string',
        'Status': 'SUBMITTED'|'IN_PROGRESS'|'ERROR'|'SUCCESSFUL'|'FAILED',
        'Message': 'string',
        'DomainName': 'string',
        'Type': 'REGISTER_DOMAIN'|'DELETE_DOMAIN'|'TRANSFER_IN_DOMAIN'|'UPDATE_DOMAIN_CONTACT'|'UPDATE_NAMESERVER'|'CHANGE_PRIVACY_PROTECTION'|'DOMAIN_LOCK'|'ENABLE_AUTORENEW'|'DISABLE_AUTORENEW'|'ADD_DNSSEC'|'REMOVE_DNSSEC'|'EXPIRE_DOMAIN'|'TRANSFER_OUT_DOMAIN'|'CHANGE_DOMAIN_OWNER'|'RENEW_DOMAIN'|'PUSH_DOMAIN'|'INTERNAL_TRANSFER_OUT_DOMAIN'|'INTERNAL_TRANSFER_IN_DOMAIN',
        'SubmittedDate': datetime(2015, 1, 1)
    }
    
    
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

def list_domains(Marker=None, MaxItems=None):
    """
    This operation returns all the domain names registered with Amazon Route 53 for the current AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_domains(
        Marker='string',
        MaxItems=123
    )
    
    
    :type Marker: string
    :param Marker: For an initial request for a list of domains, omit this element. If the number of domains that are associated with the current AWS account is greater than the value that you specified for MaxItems , you can use Marker to return additional domains. Get the value of NextPageMarker from the previous response, and submit another request that includes the value of NextPageMarker in the Marker element.\nConstraints: The marker must match the value specified in the previous request.\n

    :type MaxItems: integer
    :param MaxItems: Number of domains to be returned.\nDefault: 20\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Domains': [
        {
            'DomainName': 'string',
            'AutoRenew': True|False,
            'TransferLock': True|False,
            'Expiry': datetime(2015, 1, 1)
        },
    ],
    'NextPageMarker': 'string'
}


Response Structure

(dict) --
The ListDomains response includes the following elements.

Domains (list) --
A summary of domains.

(dict) --
Summary information about one domain.

DomainName (string) --
The name of the domain that the summary information applies to.

AutoRenew (boolean) --
Indicates whether the domain is automatically renewed upon expiration.

TransferLock (boolean) --
Indicates whether a domain is locked from unauthorized transfer to another party.

Expiry (datetime) --
Expiration date of the domain in Unix time format and Coordinated Universal Time (UTC).





NextPageMarker (string) --
If there are more domains than you specified for MaxItems in the request, submit another request and include the value of NextPageMarker in the value of Marker .







Exceptions

Route53Domains.Client.exceptions.InvalidInput


    :return: {
        'Domains': [
            {
                'DomainName': 'string',
                'AutoRenew': True|False,
                'TransferLock': True|False,
                'Expiry': datetime(2015, 1, 1)
            },
        ],
        'NextPageMarker': 'string'
    }
    
    
    :returns: 
    Route53Domains.Client.exceptions.InvalidInput
    
    """
    pass

def list_operations(SubmittedSince=None, Marker=None, MaxItems=None):
    """
    Returns information about all of the operations that return an operation ID and that have ever been performed on domains that were registered by the current account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_operations(
        SubmittedSince=datetime(2015, 1, 1),
        Marker='string',
        MaxItems=123
    )
    
    
    :type SubmittedSince: datetime
    :param SubmittedSince: An optional parameter that lets you get information about all the operations that you submitted after a specified date and time. Specify the date and time in Unix time format and Coordinated Universal time (UTC).

    :type Marker: string
    :param Marker: For an initial request for a list of operations, omit this element. If the number of operations that are not yet complete is greater than the value that you specified for MaxItems , you can use Marker to return additional operations. Get the value of NextPageMarker from the previous response, and submit another request that includes the value of NextPageMarker in the Marker element.

    :type MaxItems: integer
    :param MaxItems: Number of domains to be returned.\nDefault: 20\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Operations': [
        {
            'OperationId': 'string',
            'Status': 'SUBMITTED'|'IN_PROGRESS'|'ERROR'|'SUCCESSFUL'|'FAILED',
            'Type': 'REGISTER_DOMAIN'|'DELETE_DOMAIN'|'TRANSFER_IN_DOMAIN'|'UPDATE_DOMAIN_CONTACT'|'UPDATE_NAMESERVER'|'CHANGE_PRIVACY_PROTECTION'|'DOMAIN_LOCK'|'ENABLE_AUTORENEW'|'DISABLE_AUTORENEW'|'ADD_DNSSEC'|'REMOVE_DNSSEC'|'EXPIRE_DOMAIN'|'TRANSFER_OUT_DOMAIN'|'CHANGE_DOMAIN_OWNER'|'RENEW_DOMAIN'|'PUSH_DOMAIN'|'INTERNAL_TRANSFER_OUT_DOMAIN'|'INTERNAL_TRANSFER_IN_DOMAIN',
            'SubmittedDate': datetime(2015, 1, 1)
        },
    ],
    'NextPageMarker': 'string'
}


Response Structure

(dict) --
The ListOperations response includes the following elements.

Operations (list) --
Lists summaries of the operations.

(dict) --
OperationSummary includes the following elements.

OperationId (string) --
Identifier returned to track the requested action.

Status (string) --
The current status of the requested operation in the system.

Type (string) --
Type of the action requested.

SubmittedDate (datetime) --
The date when the request was submitted.





NextPageMarker (string) --
If there are more operations than you specified for MaxItems in the request, submit another request and include the value of NextPageMarker in the value of Marker .







Exceptions

Route53Domains.Client.exceptions.InvalidInput


    :return: {
        'Operations': [
            {
                'OperationId': 'string',
                'Status': 'SUBMITTED'|'IN_PROGRESS'|'ERROR'|'SUCCESSFUL'|'FAILED',
                'Type': 'REGISTER_DOMAIN'|'DELETE_DOMAIN'|'TRANSFER_IN_DOMAIN'|'UPDATE_DOMAIN_CONTACT'|'UPDATE_NAMESERVER'|'CHANGE_PRIVACY_PROTECTION'|'DOMAIN_LOCK'|'ENABLE_AUTORENEW'|'DISABLE_AUTORENEW'|'ADD_DNSSEC'|'REMOVE_DNSSEC'|'EXPIRE_DOMAIN'|'TRANSFER_OUT_DOMAIN'|'CHANGE_DOMAIN_OWNER'|'RENEW_DOMAIN'|'PUSH_DOMAIN'|'INTERNAL_TRANSFER_OUT_DOMAIN'|'INTERNAL_TRANSFER_IN_DOMAIN',
                'SubmittedDate': datetime(2015, 1, 1)
            },
        ],
        'NextPageMarker': 'string'
    }
    
    
    :returns: 
    Route53Domains.Client.exceptions.InvalidInput
    
    """
    pass

def list_tags_for_domain(DomainName=None):
    """
    This operation returns all of the tags that are associated with the specified domain.
    All tag operations are eventually consistent; subsequent operations might not immediately represent all issued operations.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_domain(
        DomainName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe domain for which you want to get a list of tags.\n

    :rtype: dict
ReturnsResponse Syntax{
    'TagList': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --The ListTagsForDomain response includes the following elements.

TagList (list) --A list of the tags that are associated with the specified domain.

(dict) --Each tag includes the following elements.

Key (string) --The key (name) of a tag.
Valid values: A-Z, a-z, 0-9, space, ".:/=+-@"
Constraints: Each key can be 1-128 characters long.

Value (string) --The value of a tag.
Valid values: A-Z, a-z, 0-9, space, ".:/=+-@"
Constraints: Each value can be 0-256 characters long.










Exceptions

Route53Domains.Client.exceptions.InvalidInput
Route53Domains.Client.exceptions.OperationLimitExceeded
Route53Domains.Client.exceptions.UnsupportedTLD


    :return: {
        'TagList': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    """
    pass

def register_domain(DomainName=None, IdnLangCode=None, DurationInYears=None, AutoRenew=None, AdminContact=None, RegistrantContact=None, TechContact=None, PrivacyProtectAdminContact=None, PrivacyProtectRegistrantContact=None, PrivacyProtectTechContact=None):
    """
    This operation registers a domain. Domains are registered either by Amazon Registrar (for .com, .net, and .org domains) or by our registrar associate, Gandi (for all other domains). For some top-level domains (TLDs), this operation requires extra parameters.
    When you register a domain, Amazon Route 53 does the following:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_domain(
        DomainName='string',
        IdnLangCode='string',
        DurationInYears=123,
        AutoRenew=True|False,
        AdminContact={
            'FirstName': 'string',
            'LastName': 'string',
            'ContactType': 'PERSON'|'COMPANY'|'ASSOCIATION'|'PUBLIC_BODY'|'RESELLER',
            'OrganizationName': 'string',
            'AddressLine1': 'string',
            'AddressLine2': 'string',
            'City': 'string',
            'State': 'string',
            'CountryCode': 'AD'|'AE'|'AF'|'AG'|'AI'|'AL'|'AM'|'AN'|'AO'|'AQ'|'AR'|'AS'|'AT'|'AU'|'AW'|'AZ'|'BA'|'BB'|'BD'|'BE'|'BF'|'BG'|'BH'|'BI'|'BJ'|'BL'|'BM'|'BN'|'BO'|'BR'|'BS'|'BT'|'BW'|'BY'|'BZ'|'CA'|'CC'|'CD'|'CF'|'CG'|'CH'|'CI'|'CK'|'CL'|'CM'|'CN'|'CO'|'CR'|'CU'|'CV'|'CX'|'CY'|'CZ'|'DE'|'DJ'|'DK'|'DM'|'DO'|'DZ'|'EC'|'EE'|'EG'|'ER'|'ES'|'ET'|'FI'|'FJ'|'FK'|'FM'|'FO'|'FR'|'GA'|'GB'|'GD'|'GE'|'GH'|'GI'|'GL'|'GM'|'GN'|'GQ'|'GR'|'GT'|'GU'|'GW'|'GY'|'HK'|'HN'|'HR'|'HT'|'HU'|'ID'|'IE'|'IL'|'IM'|'IN'|'IQ'|'IR'|'IS'|'IT'|'JM'|'JO'|'JP'|'KE'|'KG'|'KH'|'KI'|'KM'|'KN'|'KP'|'KR'|'KW'|'KY'|'KZ'|'LA'|'LB'|'LC'|'LI'|'LK'|'LR'|'LS'|'LT'|'LU'|'LV'|'LY'|'MA'|'MC'|'MD'|'ME'|'MF'|'MG'|'MH'|'MK'|'ML'|'MM'|'MN'|'MO'|'MP'|'MR'|'MS'|'MT'|'MU'|'MV'|'MW'|'MX'|'MY'|'MZ'|'NA'|'NC'|'NE'|'NG'|'NI'|'NL'|'NO'|'NP'|'NR'|'NU'|'NZ'|'OM'|'PA'|'PE'|'PF'|'PG'|'PH'|'PK'|'PL'|'PM'|'PN'|'PR'|'PT'|'PW'|'PY'|'QA'|'RO'|'RS'|'RU'|'RW'|'SA'|'SB'|'SC'|'SD'|'SE'|'SG'|'SH'|'SI'|'SK'|'SL'|'SM'|'SN'|'SO'|'SR'|'ST'|'SV'|'SY'|'SZ'|'TC'|'TD'|'TG'|'TH'|'TJ'|'TK'|'TL'|'TM'|'TN'|'TO'|'TR'|'TT'|'TV'|'TW'|'TZ'|'UA'|'UG'|'US'|'UY'|'UZ'|'VA'|'VC'|'VE'|'VG'|'VI'|'VN'|'VU'|'WF'|'WS'|'YE'|'YT'|'ZA'|'ZM'|'ZW',
            'ZipCode': 'string',
            'PhoneNumber': 'string',
            'Email': 'string',
            'Fax': 'string',
            'ExtraParams': [
                {
                    'Name': 'DUNS_NUMBER'|'BRAND_NUMBER'|'BIRTH_DEPARTMENT'|'BIRTH_DATE_IN_YYYY_MM_DD'|'BIRTH_COUNTRY'|'BIRTH_CITY'|'DOCUMENT_NUMBER'|'AU_ID_NUMBER'|'AU_ID_TYPE'|'CA_LEGAL_TYPE'|'CA_BUSINESS_ENTITY_TYPE'|'CA_LEGAL_REPRESENTATIVE'|'CA_LEGAL_REPRESENTATIVE_CAPACITY'|'ES_IDENTIFICATION'|'ES_IDENTIFICATION_TYPE'|'ES_LEGAL_FORM'|'FI_BUSINESS_NUMBER'|'FI_ID_NUMBER'|'FI_NATIONALITY'|'FI_ORGANIZATION_TYPE'|'IT_NATIONALITY'|'IT_PIN'|'IT_REGISTRANT_ENTITY_TYPE'|'RU_PASSPORT_DATA'|'SE_ID_NUMBER'|'SG_ID_NUMBER'|'VAT_NUMBER'|'UK_CONTACT_TYPE'|'UK_COMPANY_NUMBER',
                    'Value': 'string'
                },
            ]
        },
        RegistrantContact={
            'FirstName': 'string',
            'LastName': 'string',
            'ContactType': 'PERSON'|'COMPANY'|'ASSOCIATION'|'PUBLIC_BODY'|'RESELLER',
            'OrganizationName': 'string',
            'AddressLine1': 'string',
            'AddressLine2': 'string',
            'City': 'string',
            'State': 'string',
            'CountryCode': 'AD'|'AE'|'AF'|'AG'|'AI'|'AL'|'AM'|'AN'|'AO'|'AQ'|'AR'|'AS'|'AT'|'AU'|'AW'|'AZ'|'BA'|'BB'|'BD'|'BE'|'BF'|'BG'|'BH'|'BI'|'BJ'|'BL'|'BM'|'BN'|'BO'|'BR'|'BS'|'BT'|'BW'|'BY'|'BZ'|'CA'|'CC'|'CD'|'CF'|'CG'|'CH'|'CI'|'CK'|'CL'|'CM'|'CN'|'CO'|'CR'|'CU'|'CV'|'CX'|'CY'|'CZ'|'DE'|'DJ'|'DK'|'DM'|'DO'|'DZ'|'EC'|'EE'|'EG'|'ER'|'ES'|'ET'|'FI'|'FJ'|'FK'|'FM'|'FO'|'FR'|'GA'|'GB'|'GD'|'GE'|'GH'|'GI'|'GL'|'GM'|'GN'|'GQ'|'GR'|'GT'|'GU'|'GW'|'GY'|'HK'|'HN'|'HR'|'HT'|'HU'|'ID'|'IE'|'IL'|'IM'|'IN'|'IQ'|'IR'|'IS'|'IT'|'JM'|'JO'|'JP'|'KE'|'KG'|'KH'|'KI'|'KM'|'KN'|'KP'|'KR'|'KW'|'KY'|'KZ'|'LA'|'LB'|'LC'|'LI'|'LK'|'LR'|'LS'|'LT'|'LU'|'LV'|'LY'|'MA'|'MC'|'MD'|'ME'|'MF'|'MG'|'MH'|'MK'|'ML'|'MM'|'MN'|'MO'|'MP'|'MR'|'MS'|'MT'|'MU'|'MV'|'MW'|'MX'|'MY'|'MZ'|'NA'|'NC'|'NE'|'NG'|'NI'|'NL'|'NO'|'NP'|'NR'|'NU'|'NZ'|'OM'|'PA'|'PE'|'PF'|'PG'|'PH'|'PK'|'PL'|'PM'|'PN'|'PR'|'PT'|'PW'|'PY'|'QA'|'RO'|'RS'|'RU'|'RW'|'SA'|'SB'|'SC'|'SD'|'SE'|'SG'|'SH'|'SI'|'SK'|'SL'|'SM'|'SN'|'SO'|'SR'|'ST'|'SV'|'SY'|'SZ'|'TC'|'TD'|'TG'|'TH'|'TJ'|'TK'|'TL'|'TM'|'TN'|'TO'|'TR'|'TT'|'TV'|'TW'|'TZ'|'UA'|'UG'|'US'|'UY'|'UZ'|'VA'|'VC'|'VE'|'VG'|'VI'|'VN'|'VU'|'WF'|'WS'|'YE'|'YT'|'ZA'|'ZM'|'ZW',
            'ZipCode': 'string',
            'PhoneNumber': 'string',
            'Email': 'string',
            'Fax': 'string',
            'ExtraParams': [
                {
                    'Name': 'DUNS_NUMBER'|'BRAND_NUMBER'|'BIRTH_DEPARTMENT'|'BIRTH_DATE_IN_YYYY_MM_DD'|'BIRTH_COUNTRY'|'BIRTH_CITY'|'DOCUMENT_NUMBER'|'AU_ID_NUMBER'|'AU_ID_TYPE'|'CA_LEGAL_TYPE'|'CA_BUSINESS_ENTITY_TYPE'|'CA_LEGAL_REPRESENTATIVE'|'CA_LEGAL_REPRESENTATIVE_CAPACITY'|'ES_IDENTIFICATION'|'ES_IDENTIFICATION_TYPE'|'ES_LEGAL_FORM'|'FI_BUSINESS_NUMBER'|'FI_ID_NUMBER'|'FI_NATIONALITY'|'FI_ORGANIZATION_TYPE'|'IT_NATIONALITY'|'IT_PIN'|'IT_REGISTRANT_ENTITY_TYPE'|'RU_PASSPORT_DATA'|'SE_ID_NUMBER'|'SG_ID_NUMBER'|'VAT_NUMBER'|'UK_CONTACT_TYPE'|'UK_COMPANY_NUMBER',
                    'Value': 'string'
                },
            ]
        },
        TechContact={
            'FirstName': 'string',
            'LastName': 'string',
            'ContactType': 'PERSON'|'COMPANY'|'ASSOCIATION'|'PUBLIC_BODY'|'RESELLER',
            'OrganizationName': 'string',
            'AddressLine1': 'string',
            'AddressLine2': 'string',
            'City': 'string',
            'State': 'string',
            'CountryCode': 'AD'|'AE'|'AF'|'AG'|'AI'|'AL'|'AM'|'AN'|'AO'|'AQ'|'AR'|'AS'|'AT'|'AU'|'AW'|'AZ'|'BA'|'BB'|'BD'|'BE'|'BF'|'BG'|'BH'|'BI'|'BJ'|'BL'|'BM'|'BN'|'BO'|'BR'|'BS'|'BT'|'BW'|'BY'|'BZ'|'CA'|'CC'|'CD'|'CF'|'CG'|'CH'|'CI'|'CK'|'CL'|'CM'|'CN'|'CO'|'CR'|'CU'|'CV'|'CX'|'CY'|'CZ'|'DE'|'DJ'|'DK'|'DM'|'DO'|'DZ'|'EC'|'EE'|'EG'|'ER'|'ES'|'ET'|'FI'|'FJ'|'FK'|'FM'|'FO'|'FR'|'GA'|'GB'|'GD'|'GE'|'GH'|'GI'|'GL'|'GM'|'GN'|'GQ'|'GR'|'GT'|'GU'|'GW'|'GY'|'HK'|'HN'|'HR'|'HT'|'HU'|'ID'|'IE'|'IL'|'IM'|'IN'|'IQ'|'IR'|'IS'|'IT'|'JM'|'JO'|'JP'|'KE'|'KG'|'KH'|'KI'|'KM'|'KN'|'KP'|'KR'|'KW'|'KY'|'KZ'|'LA'|'LB'|'LC'|'LI'|'LK'|'LR'|'LS'|'LT'|'LU'|'LV'|'LY'|'MA'|'MC'|'MD'|'ME'|'MF'|'MG'|'MH'|'MK'|'ML'|'MM'|'MN'|'MO'|'MP'|'MR'|'MS'|'MT'|'MU'|'MV'|'MW'|'MX'|'MY'|'MZ'|'NA'|'NC'|'NE'|'NG'|'NI'|'NL'|'NO'|'NP'|'NR'|'NU'|'NZ'|'OM'|'PA'|'PE'|'PF'|'PG'|'PH'|'PK'|'PL'|'PM'|'PN'|'PR'|'PT'|'PW'|'PY'|'QA'|'RO'|'RS'|'RU'|'RW'|'SA'|'SB'|'SC'|'SD'|'SE'|'SG'|'SH'|'SI'|'SK'|'SL'|'SM'|'SN'|'SO'|'SR'|'ST'|'SV'|'SY'|'SZ'|'TC'|'TD'|'TG'|'TH'|'TJ'|'TK'|'TL'|'TM'|'TN'|'TO'|'TR'|'TT'|'TV'|'TW'|'TZ'|'UA'|'UG'|'US'|'UY'|'UZ'|'VA'|'VC'|'VE'|'VG'|'VI'|'VN'|'VU'|'WF'|'WS'|'YE'|'YT'|'ZA'|'ZM'|'ZW',
            'ZipCode': 'string',
            'PhoneNumber': 'string',
            'Email': 'string',
            'Fax': 'string',
            'ExtraParams': [
                {
                    'Name': 'DUNS_NUMBER'|'BRAND_NUMBER'|'BIRTH_DEPARTMENT'|'BIRTH_DATE_IN_YYYY_MM_DD'|'BIRTH_COUNTRY'|'BIRTH_CITY'|'DOCUMENT_NUMBER'|'AU_ID_NUMBER'|'AU_ID_TYPE'|'CA_LEGAL_TYPE'|'CA_BUSINESS_ENTITY_TYPE'|'CA_LEGAL_REPRESENTATIVE'|'CA_LEGAL_REPRESENTATIVE_CAPACITY'|'ES_IDENTIFICATION'|'ES_IDENTIFICATION_TYPE'|'ES_LEGAL_FORM'|'FI_BUSINESS_NUMBER'|'FI_ID_NUMBER'|'FI_NATIONALITY'|'FI_ORGANIZATION_TYPE'|'IT_NATIONALITY'|'IT_PIN'|'IT_REGISTRANT_ENTITY_TYPE'|'RU_PASSPORT_DATA'|'SE_ID_NUMBER'|'SG_ID_NUMBER'|'VAT_NUMBER'|'UK_CONTACT_TYPE'|'UK_COMPANY_NUMBER',
                    'Value': 'string'
                },
            ]
        },
        PrivacyProtectAdminContact=True|False,
        PrivacyProtectRegistrantContact=True|False,
        PrivacyProtectTechContact=True|False
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe domain name that you want to register. The top-level domain (TLD), such as .com, must be a TLD that Route 53 supports. For a list of supported TLDs, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide .\nThe domain name can contain only the following characters:\n\nLetters a through z. Domain names are not case sensitive.\nNumbers 0 through 9.\nHyphen (-). You can\'t specify a hyphen at the beginning or end of a label.\nPeriod (.) to separate the labels in the name, such as the . in example.com .\n\nInternationalized domain names are not supported for some top-level domains. To determine whether the TLD that you want to use supports internationalized domain names, see Domains that You Can Register with Amazon Route 53 . For more information, see Formatting Internationalized Domain Names .\n

    :type IdnLangCode: string
    :param IdnLangCode: Reserved for future use.

    :type DurationInYears: integer
    :param DurationInYears: [REQUIRED]\nThe number of years that you want to register the domain for. Domains are registered for a minimum of one year. The maximum period depends on the top-level domain. For the range of valid values for your domain, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide .\nDefault: 1\n

    :type AutoRenew: boolean
    :param AutoRenew: Indicates whether the domain will be automatically renewed (true ) or not (false ). Autorenewal only takes effect after the account is charged.\nDefault: true\n

    :type AdminContact: dict
    :param AdminContact: [REQUIRED]\nProvides detailed contact information. For information about the values that you specify for each element, see ContactDetail .\n\nFirstName (string) --First name of contact.\n\nLastName (string) --Last name of contact.\n\nContactType (string) --Indicates whether the contact is a person, company, association, or public organization. Note the following:\n\nIf you specify a value other than PERSON , you must also specify a value for OrganizationName .\nFor some TLDs, the privacy protection available depends on the value that you specify for Contact Type . For the privacy protection settings for your TLD, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide\nFor .es domains, if you specify PERSON , you must specify INDIVIDUAL for the value of ES_LEGAL_FORM .\n\n\nOrganizationName (string) --Name of the organization for contact types other than PERSON .\n\nAddressLine1 (string) --First line of the contact\'s address.\n\nAddressLine2 (string) --Second line of contact\'s address, if any.\n\nCity (string) --The city of the contact\'s address.\n\nState (string) --The state or province of the contact\'s city.\n\nCountryCode (string) --Code for the country of the contact\'s address.\n\nZipCode (string) --The zip or postal code of the contact\'s address.\n\nPhoneNumber (string) --The phone number of the contact.\nConstraints: Phone number must be specified in the format '+[country dialing code].[number including any area code>]'. For example, a US phone number might appear as '+1.1234567890' .\n\nEmail (string) --Email address of the contact.\n\nFax (string) --Fax number of the contact.\nConstraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .\n\nExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.\n\n(dict) --ExtraParam includes the following elements.\n\nName (string) -- [REQUIRED]The name of an additional parameter that is required by a top-level domain. Here are the top-level domains that require additional parameters and the names of the parameters that they require:\n\n.com.au and .net.au\n\nAU_ID_NUMBER\nAU_ID_TYPE  Valid values include the following:\nABN (Australian business number)\nACN (Australian company number)\nTM (Trademark number)\n\n.ca\n\nBRAND_NUMBER\nCA_BUSINESS_ENTITY_TYPE  Valid values include the following:\nBANK (Bank)\nCOMMERCIAL_COMPANY (Commercial company)\nCOMPANY (Company)\nCOOPERATION (Cooperation)\nCOOPERATIVE (Cooperative)\nCOOPRIX (Cooprix)\nCORP (Corporation)\nCREDIT_UNION (Credit union)\nFOMIA (Federation of mutual insurance associations)\nINC (Incorporated)\nLTD (Limited)\nLTEE (Limit\xc3\xa9e)\nLLC (Limited liability corporation)\nLLP (Limited liability partnership)\nLTE (Lte.)\nMBA (Mutual benefit association)\nMIC (Mutual insurance company)\nNFP (Not-for-profit corporation)\nSA (S.A.)\nSAVINGS_COMPANY (Savings company)\nSAVINGS_UNION (Savings union)\nSARL (Soci\xc3\xa9t\xc3\xa9 \xc3\xa0 responsabilit\xc3\xa9 limit\xc3\xa9e)\nTRUST (Trust)\nULC (Unlimited liability corporation)\n\n\nCA_LEGAL_TYPE  When ContactType is PERSON , valid values include the following:\nABO (Aboriginal Peoples indigenous to Canada)\nCCT (Canadian citizen)\nLGR (Legal Representative of a Canadian Citizen or Permanent Resident)\nRES (Permanent resident of Canada)\n\n\n\nWhen ContactType is a value other than PERSON , valid values include the following:\n\n\nASS (Canadian unincorporated association)\nCCO (Canadian corporation)\nEDU (Canadian educational institution)\nGOV (Government or government entity in Canada)\nHOP (Canadian Hospital)\nINB (Indian Band recognized by the Indian Act of Canada)\nLAM (Canadian Library, Archive, or Museum)\nMAJ (Her/His Majesty the Queen/King)\nOMK (Official mark registered in Canada)\nPLT (Canadian Political Party)\nPRT (Partnership Registered in Canada)\nTDM (Trademark registered in Canada)\nTRD (Canadian Trade Union)\nTRS (Trust established in Canada)\n\n.es\n\n\nES_IDENTIFICATION  Specify the applicable value:\nFor contacts inside Spain: Enter your passport ID.\nFor contacts outside of Spain: Enter the VAT identification number for the company.\n\n\nNote\nFor .es domains, the value of ContactType must be PERSON .\n\n\nES_IDENTIFICATION_TYPE  Valid values include the following:\nDNI_AND_NIF (For Spanish contacts)\nNIE (For foreigners with legal residence)\nOTHER (For contacts outside of Spain)\n\n\nES_LEGAL_FORM  Valid values include the following:\nASSOCIATION\nCENTRAL_GOVERNMENT_BODY\nCIVIL_SOCIETY\nCOMMUNITY_OF_OWNERS\nCOMMUNITY_PROPERTY\nCONSULATE\nCOOPERATIVE\nDESIGNATION_OF_ORIGIN_SUPERVISORY_COUNCIL\nECONOMIC_INTEREST_GROUP\nEMBASSY\nENTITY_MANAGING_NATURAL_AREAS\nFARM_PARTNERSHIP\nFOUNDATION\nGENERAL_AND_LIMITED_PARTNERSHIP\nGENERAL_PARTNERSHIP\nINDIVIDUAL\nLIMITED_COMPANY\nLOCAL_AUTHORITY\nLOCAL_PUBLIC_ENTITY\nMUTUAL_INSURANCE_COMPANY\nNATIONAL_PUBLIC_ENTITY\nORDER_OR_RELIGIOUS_INSTITUTION\nOTHERS (Only for contacts outside of Spain)\nPOLITICAL_PARTY\nPROFESSIONAL_ASSOCIATION\nPUBLIC_LAW_ASSOCIATION\nPUBLIC_LIMITED_COMPANY\nREGIONAL_GOVERNMENT_BODY\nREGIONAL_PUBLIC_ENTITY\nSAVINGS_BANK\nSPANISH_OFFICE\nSPORTS_ASSOCIATION\nSPORTS_FEDERATION\nSPORTS_LIMITED_COMPANY\nTEMPORARY_ALLIANCE_OF_ENTERPRISES\nTRADE_UNION\nWORKER_OWNED_COMPANY\nWORKER_OWNED_LIMITED_COMPANY\n\n.fi\n\nBIRTH_DATE_IN_YYYY_MM_DD\nFI_BUSINESS_NUMBER\nFI_ID_NUMBER\nFI_NATIONALITY  Valid values include the following:\nFINNISH\nNOT_FINNISH\n\n\nFI_ORGANIZATION_TYPE  Valid values include the following:\nCOMPANY\nCORPORATION\nGOVERNMENT\nINSTITUTION\nPOLITICAL_PARTY\nPUBLIC_COMMUNITY\nTOWNSHIP\n\n.fr\n\nBIRTH_CITY\nBIRTH_COUNTRY\nBIRTH_DATE_IN_YYYY_MM_DD\nBIRTH_DEPARTMENT : Specify the INSEE code that corresponds with the department where the contact was born. If the contact was born somewhere other than France or its overseas departments, specify 99 . For more information, including a list of departments and the corresponding INSEE numbers, see the Wikipedia entry Departments of France .\nBRAND_NUMBER.it\n\nIT_NATIONALITY\nIT_PIN\nIT_REGISTRANT_ENTITY_TYPE  Valid values include the following:\nFOREIGNERS\nFREELANCE_WORKERS (Freelance workers and professionals)\nITALIAN_COMPANIES (Italian companies and one-person companies)\nNON_PROFIT_ORGANIZATIONS\nOTHER_SUBJECTS\nPUBLIC_ORGANIZATIONS\n\n.ru\n\nBIRTH_DATE_IN_YYYY_MM_DD\nRU_PASSPORT_DATA.se\n\nBIRTH_COUNTRY\nSE_ID_NUMBER.sg\n\nSG_ID_NUMBER.co.uk, .me.uk, and .org.uk\n\nUK_CONTACT_TYPE  Valid values include the following:\nCRC (UK Corporation by Royal Charter)\nFCORP (Non-UK Corporation)\nFIND (Non-UK Individual, representing self)\nFOTHER (Non-UK Entity that does not fit into any other category)\nGOV (UK Government Body)\nIND (UK Individual (representing self))\nIP (UK Industrial/Provident Registered Company)\nLLP (UK Limited Liability Partnership)\nLTD (UK Limited Company)\nOTHER (UK Entity that does not fit into any other category)\nPLC (UK Public Limited Company)\nPTNR (UK Partnership)\nRCHAR (UK Registered Charity)\nSCH (UK School)\nSTAT (UK Statutory Body)\nSTRA (UK Sole Trader)\n\n\nUK_COMPANY_NUMBER\n\nIn addition, many TLDs require a VAT_NUMBER .\n\nValue (string) -- [REQUIRED]The value that corresponds with the name of an extra parameter.\n\n\n\n\n\n\n

    :type RegistrantContact: dict
    :param RegistrantContact: [REQUIRED]\nProvides detailed contact information. For information about the values that you specify for each element, see ContactDetail .\n\nFirstName (string) --First name of contact.\n\nLastName (string) --Last name of contact.\n\nContactType (string) --Indicates whether the contact is a person, company, association, or public organization. Note the following:\n\nIf you specify a value other than PERSON , you must also specify a value for OrganizationName .\nFor some TLDs, the privacy protection available depends on the value that you specify for Contact Type . For the privacy protection settings for your TLD, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide\nFor .es domains, if you specify PERSON , you must specify INDIVIDUAL for the value of ES_LEGAL_FORM .\n\n\nOrganizationName (string) --Name of the organization for contact types other than PERSON .\n\nAddressLine1 (string) --First line of the contact\'s address.\n\nAddressLine2 (string) --Second line of contact\'s address, if any.\n\nCity (string) --The city of the contact\'s address.\n\nState (string) --The state or province of the contact\'s city.\n\nCountryCode (string) --Code for the country of the contact\'s address.\n\nZipCode (string) --The zip or postal code of the contact\'s address.\n\nPhoneNumber (string) --The phone number of the contact.\nConstraints: Phone number must be specified in the format '+[country dialing code].[number including any area code>]'. For example, a US phone number might appear as '+1.1234567890' .\n\nEmail (string) --Email address of the contact.\n\nFax (string) --Fax number of the contact.\nConstraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .\n\nExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.\n\n(dict) --ExtraParam includes the following elements.\n\nName (string) -- [REQUIRED]The name of an additional parameter that is required by a top-level domain. Here are the top-level domains that require additional parameters and the names of the parameters that they require:\n\n.com.au and .net.au\n\nAU_ID_NUMBER\nAU_ID_TYPE  Valid values include the following:\nABN (Australian business number)\nACN (Australian company number)\nTM (Trademark number)\n\n.ca\n\nBRAND_NUMBER\nCA_BUSINESS_ENTITY_TYPE  Valid values include the following:\nBANK (Bank)\nCOMMERCIAL_COMPANY (Commercial company)\nCOMPANY (Company)\nCOOPERATION (Cooperation)\nCOOPERATIVE (Cooperative)\nCOOPRIX (Cooprix)\nCORP (Corporation)\nCREDIT_UNION (Credit union)\nFOMIA (Federation of mutual insurance associations)\nINC (Incorporated)\nLTD (Limited)\nLTEE (Limit\xc3\xa9e)\nLLC (Limited liability corporation)\nLLP (Limited liability partnership)\nLTE (Lte.)\nMBA (Mutual benefit association)\nMIC (Mutual insurance company)\nNFP (Not-for-profit corporation)\nSA (S.A.)\nSAVINGS_COMPANY (Savings company)\nSAVINGS_UNION (Savings union)\nSARL (Soci\xc3\xa9t\xc3\xa9 \xc3\xa0 responsabilit\xc3\xa9 limit\xc3\xa9e)\nTRUST (Trust)\nULC (Unlimited liability corporation)\n\n\nCA_LEGAL_TYPE  When ContactType is PERSON , valid values include the following:\nABO (Aboriginal Peoples indigenous to Canada)\nCCT (Canadian citizen)\nLGR (Legal Representative of a Canadian Citizen or Permanent Resident)\nRES (Permanent resident of Canada)\n\n\n\nWhen ContactType is a value other than PERSON , valid values include the following:\n\n\nASS (Canadian unincorporated association)\nCCO (Canadian corporation)\nEDU (Canadian educational institution)\nGOV (Government or government entity in Canada)\nHOP (Canadian Hospital)\nINB (Indian Band recognized by the Indian Act of Canada)\nLAM (Canadian Library, Archive, or Museum)\nMAJ (Her/His Majesty the Queen/King)\nOMK (Official mark registered in Canada)\nPLT (Canadian Political Party)\nPRT (Partnership Registered in Canada)\nTDM (Trademark registered in Canada)\nTRD (Canadian Trade Union)\nTRS (Trust established in Canada)\n\n.es\n\n\nES_IDENTIFICATION  Specify the applicable value:\nFor contacts inside Spain: Enter your passport ID.\nFor contacts outside of Spain: Enter the VAT identification number for the company.\n\n\nNote\nFor .es domains, the value of ContactType must be PERSON .\n\n\nES_IDENTIFICATION_TYPE  Valid values include the following:\nDNI_AND_NIF (For Spanish contacts)\nNIE (For foreigners with legal residence)\nOTHER (For contacts outside of Spain)\n\n\nES_LEGAL_FORM  Valid values include the following:\nASSOCIATION\nCENTRAL_GOVERNMENT_BODY\nCIVIL_SOCIETY\nCOMMUNITY_OF_OWNERS\nCOMMUNITY_PROPERTY\nCONSULATE\nCOOPERATIVE\nDESIGNATION_OF_ORIGIN_SUPERVISORY_COUNCIL\nECONOMIC_INTEREST_GROUP\nEMBASSY\nENTITY_MANAGING_NATURAL_AREAS\nFARM_PARTNERSHIP\nFOUNDATION\nGENERAL_AND_LIMITED_PARTNERSHIP\nGENERAL_PARTNERSHIP\nINDIVIDUAL\nLIMITED_COMPANY\nLOCAL_AUTHORITY\nLOCAL_PUBLIC_ENTITY\nMUTUAL_INSURANCE_COMPANY\nNATIONAL_PUBLIC_ENTITY\nORDER_OR_RELIGIOUS_INSTITUTION\nOTHERS (Only for contacts outside of Spain)\nPOLITICAL_PARTY\nPROFESSIONAL_ASSOCIATION\nPUBLIC_LAW_ASSOCIATION\nPUBLIC_LIMITED_COMPANY\nREGIONAL_GOVERNMENT_BODY\nREGIONAL_PUBLIC_ENTITY\nSAVINGS_BANK\nSPANISH_OFFICE\nSPORTS_ASSOCIATION\nSPORTS_FEDERATION\nSPORTS_LIMITED_COMPANY\nTEMPORARY_ALLIANCE_OF_ENTERPRISES\nTRADE_UNION\nWORKER_OWNED_COMPANY\nWORKER_OWNED_LIMITED_COMPANY\n\n.fi\n\nBIRTH_DATE_IN_YYYY_MM_DD\nFI_BUSINESS_NUMBER\nFI_ID_NUMBER\nFI_NATIONALITY  Valid values include the following:\nFINNISH\nNOT_FINNISH\n\n\nFI_ORGANIZATION_TYPE  Valid values include the following:\nCOMPANY\nCORPORATION\nGOVERNMENT\nINSTITUTION\nPOLITICAL_PARTY\nPUBLIC_COMMUNITY\nTOWNSHIP\n\n.fr\n\nBIRTH_CITY\nBIRTH_COUNTRY\nBIRTH_DATE_IN_YYYY_MM_DD\nBIRTH_DEPARTMENT : Specify the INSEE code that corresponds with the department where the contact was born. If the contact was born somewhere other than France or its overseas departments, specify 99 . For more information, including a list of departments and the corresponding INSEE numbers, see the Wikipedia entry Departments of France .\nBRAND_NUMBER.it\n\nIT_NATIONALITY\nIT_PIN\nIT_REGISTRANT_ENTITY_TYPE  Valid values include the following:\nFOREIGNERS\nFREELANCE_WORKERS (Freelance workers and professionals)\nITALIAN_COMPANIES (Italian companies and one-person companies)\nNON_PROFIT_ORGANIZATIONS\nOTHER_SUBJECTS\nPUBLIC_ORGANIZATIONS\n\n.ru\n\nBIRTH_DATE_IN_YYYY_MM_DD\nRU_PASSPORT_DATA.se\n\nBIRTH_COUNTRY\nSE_ID_NUMBER.sg\n\nSG_ID_NUMBER.co.uk, .me.uk, and .org.uk\n\nUK_CONTACT_TYPE  Valid values include the following:\nCRC (UK Corporation by Royal Charter)\nFCORP (Non-UK Corporation)\nFIND (Non-UK Individual, representing self)\nFOTHER (Non-UK Entity that does not fit into any other category)\nGOV (UK Government Body)\nIND (UK Individual (representing self))\nIP (UK Industrial/Provident Registered Company)\nLLP (UK Limited Liability Partnership)\nLTD (UK Limited Company)\nOTHER (UK Entity that does not fit into any other category)\nPLC (UK Public Limited Company)\nPTNR (UK Partnership)\nRCHAR (UK Registered Charity)\nSCH (UK School)\nSTAT (UK Statutory Body)\nSTRA (UK Sole Trader)\n\n\nUK_COMPANY_NUMBER\n\nIn addition, many TLDs require a VAT_NUMBER .\n\nValue (string) -- [REQUIRED]The value that corresponds with the name of an extra parameter.\n\n\n\n\n\n\n

    :type TechContact: dict
    :param TechContact: [REQUIRED]\nProvides detailed contact information. For information about the values that you specify for each element, see ContactDetail .\n\nFirstName (string) --First name of contact.\n\nLastName (string) --Last name of contact.\n\nContactType (string) --Indicates whether the contact is a person, company, association, or public organization. Note the following:\n\nIf you specify a value other than PERSON , you must also specify a value for OrganizationName .\nFor some TLDs, the privacy protection available depends on the value that you specify for Contact Type . For the privacy protection settings for your TLD, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide\nFor .es domains, if you specify PERSON , you must specify INDIVIDUAL for the value of ES_LEGAL_FORM .\n\n\nOrganizationName (string) --Name of the organization for contact types other than PERSON .\n\nAddressLine1 (string) --First line of the contact\'s address.\n\nAddressLine2 (string) --Second line of contact\'s address, if any.\n\nCity (string) --The city of the contact\'s address.\n\nState (string) --The state or province of the contact\'s city.\n\nCountryCode (string) --Code for the country of the contact\'s address.\n\nZipCode (string) --The zip or postal code of the contact\'s address.\n\nPhoneNumber (string) --The phone number of the contact.\nConstraints: Phone number must be specified in the format '+[country dialing code].[number including any area code>]'. For example, a US phone number might appear as '+1.1234567890' .\n\nEmail (string) --Email address of the contact.\n\nFax (string) --Fax number of the contact.\nConstraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .\n\nExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.\n\n(dict) --ExtraParam includes the following elements.\n\nName (string) -- [REQUIRED]The name of an additional parameter that is required by a top-level domain. Here are the top-level domains that require additional parameters and the names of the parameters that they require:\n\n.com.au and .net.au\n\nAU_ID_NUMBER\nAU_ID_TYPE  Valid values include the following:\nABN (Australian business number)\nACN (Australian company number)\nTM (Trademark number)\n\n.ca\n\nBRAND_NUMBER\nCA_BUSINESS_ENTITY_TYPE  Valid values include the following:\nBANK (Bank)\nCOMMERCIAL_COMPANY (Commercial company)\nCOMPANY (Company)\nCOOPERATION (Cooperation)\nCOOPERATIVE (Cooperative)\nCOOPRIX (Cooprix)\nCORP (Corporation)\nCREDIT_UNION (Credit union)\nFOMIA (Federation of mutual insurance associations)\nINC (Incorporated)\nLTD (Limited)\nLTEE (Limit\xc3\xa9e)\nLLC (Limited liability corporation)\nLLP (Limited liability partnership)\nLTE (Lte.)\nMBA (Mutual benefit association)\nMIC (Mutual insurance company)\nNFP (Not-for-profit corporation)\nSA (S.A.)\nSAVINGS_COMPANY (Savings company)\nSAVINGS_UNION (Savings union)\nSARL (Soci\xc3\xa9t\xc3\xa9 \xc3\xa0 responsabilit\xc3\xa9 limit\xc3\xa9e)\nTRUST (Trust)\nULC (Unlimited liability corporation)\n\n\nCA_LEGAL_TYPE  When ContactType is PERSON , valid values include the following:\nABO (Aboriginal Peoples indigenous to Canada)\nCCT (Canadian citizen)\nLGR (Legal Representative of a Canadian Citizen or Permanent Resident)\nRES (Permanent resident of Canada)\n\n\n\nWhen ContactType is a value other than PERSON , valid values include the following:\n\n\nASS (Canadian unincorporated association)\nCCO (Canadian corporation)\nEDU (Canadian educational institution)\nGOV (Government or government entity in Canada)\nHOP (Canadian Hospital)\nINB (Indian Band recognized by the Indian Act of Canada)\nLAM (Canadian Library, Archive, or Museum)\nMAJ (Her/His Majesty the Queen/King)\nOMK (Official mark registered in Canada)\nPLT (Canadian Political Party)\nPRT (Partnership Registered in Canada)\nTDM (Trademark registered in Canada)\nTRD (Canadian Trade Union)\nTRS (Trust established in Canada)\n\n.es\n\n\nES_IDENTIFICATION  Specify the applicable value:\nFor contacts inside Spain: Enter your passport ID.\nFor contacts outside of Spain: Enter the VAT identification number for the company.\n\n\nNote\nFor .es domains, the value of ContactType must be PERSON .\n\n\nES_IDENTIFICATION_TYPE  Valid values include the following:\nDNI_AND_NIF (For Spanish contacts)\nNIE (For foreigners with legal residence)\nOTHER (For contacts outside of Spain)\n\n\nES_LEGAL_FORM  Valid values include the following:\nASSOCIATION\nCENTRAL_GOVERNMENT_BODY\nCIVIL_SOCIETY\nCOMMUNITY_OF_OWNERS\nCOMMUNITY_PROPERTY\nCONSULATE\nCOOPERATIVE\nDESIGNATION_OF_ORIGIN_SUPERVISORY_COUNCIL\nECONOMIC_INTEREST_GROUP\nEMBASSY\nENTITY_MANAGING_NATURAL_AREAS\nFARM_PARTNERSHIP\nFOUNDATION\nGENERAL_AND_LIMITED_PARTNERSHIP\nGENERAL_PARTNERSHIP\nINDIVIDUAL\nLIMITED_COMPANY\nLOCAL_AUTHORITY\nLOCAL_PUBLIC_ENTITY\nMUTUAL_INSURANCE_COMPANY\nNATIONAL_PUBLIC_ENTITY\nORDER_OR_RELIGIOUS_INSTITUTION\nOTHERS (Only for contacts outside of Spain)\nPOLITICAL_PARTY\nPROFESSIONAL_ASSOCIATION\nPUBLIC_LAW_ASSOCIATION\nPUBLIC_LIMITED_COMPANY\nREGIONAL_GOVERNMENT_BODY\nREGIONAL_PUBLIC_ENTITY\nSAVINGS_BANK\nSPANISH_OFFICE\nSPORTS_ASSOCIATION\nSPORTS_FEDERATION\nSPORTS_LIMITED_COMPANY\nTEMPORARY_ALLIANCE_OF_ENTERPRISES\nTRADE_UNION\nWORKER_OWNED_COMPANY\nWORKER_OWNED_LIMITED_COMPANY\n\n.fi\n\nBIRTH_DATE_IN_YYYY_MM_DD\nFI_BUSINESS_NUMBER\nFI_ID_NUMBER\nFI_NATIONALITY  Valid values include the following:\nFINNISH\nNOT_FINNISH\n\n\nFI_ORGANIZATION_TYPE  Valid values include the following:\nCOMPANY\nCORPORATION\nGOVERNMENT\nINSTITUTION\nPOLITICAL_PARTY\nPUBLIC_COMMUNITY\nTOWNSHIP\n\n.fr\n\nBIRTH_CITY\nBIRTH_COUNTRY\nBIRTH_DATE_IN_YYYY_MM_DD\nBIRTH_DEPARTMENT : Specify the INSEE code that corresponds with the department where the contact was born. If the contact was born somewhere other than France or its overseas departments, specify 99 . For more information, including a list of departments and the corresponding INSEE numbers, see the Wikipedia entry Departments of France .\nBRAND_NUMBER.it\n\nIT_NATIONALITY\nIT_PIN\nIT_REGISTRANT_ENTITY_TYPE  Valid values include the following:\nFOREIGNERS\nFREELANCE_WORKERS (Freelance workers and professionals)\nITALIAN_COMPANIES (Italian companies and one-person companies)\nNON_PROFIT_ORGANIZATIONS\nOTHER_SUBJECTS\nPUBLIC_ORGANIZATIONS\n\n.ru\n\nBIRTH_DATE_IN_YYYY_MM_DD\nRU_PASSPORT_DATA.se\n\nBIRTH_COUNTRY\nSE_ID_NUMBER.sg\n\nSG_ID_NUMBER.co.uk, .me.uk, and .org.uk\n\nUK_CONTACT_TYPE  Valid values include the following:\nCRC (UK Corporation by Royal Charter)\nFCORP (Non-UK Corporation)\nFIND (Non-UK Individual, representing self)\nFOTHER (Non-UK Entity that does not fit into any other category)\nGOV (UK Government Body)\nIND (UK Individual (representing self))\nIP (UK Industrial/Provident Registered Company)\nLLP (UK Limited Liability Partnership)\nLTD (UK Limited Company)\nOTHER (UK Entity that does not fit into any other category)\nPLC (UK Public Limited Company)\nPTNR (UK Partnership)\nRCHAR (UK Registered Charity)\nSCH (UK School)\nSTAT (UK Statutory Body)\nSTRA (UK Sole Trader)\n\n\nUK_COMPANY_NUMBER\n\nIn addition, many TLDs require a VAT_NUMBER .\n\nValue (string) -- [REQUIRED]The value that corresponds with the name of an extra parameter.\n\n\n\n\n\n\n

    :type PrivacyProtectAdminContact: boolean
    :param PrivacyProtectAdminContact: Whether you want to conceal contact information from WHOIS queries. If you specify true , WHOIS ('who is') queries return contact information either for Amazon Registrar (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other TLDs). If you specify false , WHOIS queries return the information that you entered for the admin contact.\nDefault: true\n

    :type PrivacyProtectRegistrantContact: boolean
    :param PrivacyProtectRegistrantContact: Whether you want to conceal contact information from WHOIS queries. If you specify true , WHOIS ('who is') queries return contact information either for Amazon Registrar (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other TLDs). If you specify false , WHOIS queries return the information that you entered for the registrant contact (the domain owner).\nDefault: true\n

    :type PrivacyProtectTechContact: boolean
    :param PrivacyProtectTechContact: Whether you want to conceal contact information from WHOIS queries. If you specify true , WHOIS ('who is') queries return contact information either for Amazon Registrar (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other TLDs). If you specify false , WHOIS queries return the information that you entered for the technical contact.\nDefault: true\n

    :rtype: dict

ReturnsResponse Syntax
{
    'OperationId': 'string'
}


Response Structure

(dict) --
The RegisterDomain response includes the following element.

OperationId (string) --
Identifier for tracking the progress of the request. To query the operation status, use GetOperationDetail .







Exceptions

Route53Domains.Client.exceptions.InvalidInput
Route53Domains.Client.exceptions.UnsupportedTLD
Route53Domains.Client.exceptions.DuplicateRequest
Route53Domains.Client.exceptions.TLDRulesViolation
Route53Domains.Client.exceptions.DomainLimitExceeded
Route53Domains.Client.exceptions.OperationLimitExceeded


    :return: {
        'OperationId': 'string'
    }
    
    
    :returns: 
    DomainName (string) -- [REQUIRED]
    The domain name that you want to register. The top-level domain (TLD), such as .com, must be a TLD that Route 53 supports. For a list of supported TLDs, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide .
    The domain name can contain only the following characters:
    
    Letters a through z. Domain names are not case sensitive.
    Numbers 0 through 9.
    Hyphen (-). You can\'t specify a hyphen at the beginning or end of a label.
    Period (.) to separate the labels in the name, such as the . in example.com .
    
    Internationalized domain names are not supported for some top-level domains. To determine whether the TLD that you want to use supports internationalized domain names, see Domains that You Can Register with Amazon Route 53 . For more information, see Formatting Internationalized Domain Names .
    
    IdnLangCode (string) -- Reserved for future use.
    DurationInYears (integer) -- [REQUIRED]
    The number of years that you want to register the domain for. Domains are registered for a minimum of one year. The maximum period depends on the top-level domain. For the range of valid values for your domain, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide .
    Default: 1
    
    AutoRenew (boolean) -- Indicates whether the domain will be automatically renewed (true ) or not (false ). Autorenewal only takes effect after the account is charged.
    Default: true
    
    AdminContact (dict) -- [REQUIRED]
    Provides detailed contact information. For information about the values that you specify for each element, see ContactDetail .
    
    FirstName (string) --First name of contact.
    
    LastName (string) --Last name of contact.
    
    ContactType (string) --Indicates whether the contact is a person, company, association, or public organization. Note the following:
    
    If you specify a value other than PERSON , you must also specify a value for OrganizationName .
    For some TLDs, the privacy protection available depends on the value that you specify for Contact Type . For the privacy protection settings for your TLD, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide
    For .es domains, if you specify PERSON , you must specify INDIVIDUAL for the value of ES_LEGAL_FORM .
    
    
    OrganizationName (string) --Name of the organization for contact types other than PERSON .
    
    AddressLine1 (string) --First line of the contact\'s address.
    
    AddressLine2 (string) --Second line of contact\'s address, if any.
    
    City (string) --The city of the contact\'s address.
    
    State (string) --The state or province of the contact\'s city.
    
    CountryCode (string) --Code for the country of the contact\'s address.
    
    ZipCode (string) --The zip or postal code of the contact\'s address.
    
    PhoneNumber (string) --The phone number of the contact.
    Constraints: Phone number must be specified in the format "+[country dialing code].[number including any area code>]". For example, a US phone number might appear as "+1.1234567890" .
    
    Email (string) --Email address of the contact.
    
    Fax (string) --Fax number of the contact.
    Constraints: Phone number must be specified in the format "+[country dialing code].[number including any area code]". For example, a US phone number might appear as "+1.1234567890" .
    
    ExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.
    
    (dict) --ExtraParam includes the following elements.
    
    Name (string) -- [REQUIRED]The name of an additional parameter that is required by a top-level domain. Here are the top-level domains that require additional parameters and the names of the parameters that they require:
    
    .com.au and .net.au
    
    AU_ID_NUMBER
    AU_ID_TYPE   Valid values include the following:
    ABN (Australian business number)
    ACN (Australian company number)
    TM (Trademark number)
    
    .ca
    
    BRAND_NUMBER
    CA_BUSINESS_ENTITY_TYPE   Valid values include the following:
    BANK (Bank)
    COMMERCIAL_COMPANY (Commercial company)
    COMPANY (Company)
    COOPERATION (Cooperation)
    COOPERATIVE (Cooperative)
    COOPRIX (Cooprix)
    CORP (Corporation)
    CREDIT_UNION (Credit union)
    FOMIA (Federation of mutual insurance associations)
    INC (Incorporated)
    LTD (Limited)
    LTEE (Limit\xc3\xa9e)
    LLC (Limited liability corporation)
    LLP (Limited liability partnership)
    LTE (Lte.)
    MBA (Mutual benefit association)
    MIC (Mutual insurance company)
    NFP (Not-for-profit corporation)
    SA (S.A.)
    SAVINGS_COMPANY (Savings company)
    SAVINGS_UNION (Savings union)
    SARL (Soci\xc3\xa9t\xc3\xa9 \xc3\xa0 responsabilit\xc3\xa9 limit\xc3\xa9e)
    TRUST (Trust)
    ULC (Unlimited liability corporation)
    
    
    CA_LEGAL_TYPE   When ContactType is PERSON , valid values include the following:
    ABO (Aboriginal Peoples indigenous to Canada)
    CCT (Canadian citizen)
    LGR (Legal Representative of a Canadian Citizen or Permanent Resident)
    RES (Permanent resident of Canada)
    
    
    
    When ContactType is a value other than PERSON , valid values include the following:
    
    
    ASS (Canadian unincorporated association)
    CCO (Canadian corporation)
    EDU (Canadian educational institution)
    GOV (Government or government entity in Canada)
    HOP (Canadian Hospital)
    INB (Indian Band recognized by the Indian Act of Canada)
    LAM (Canadian Library, Archive, or Museum)
    MAJ (Her/His Majesty the Queen/King)
    OMK (Official mark registered in Canada)
    PLT (Canadian Political Party)
    PRT (Partnership Registered in Canada)
    TDM (Trademark registered in Canada)
    TRD (Canadian Trade Union)
    TRS (Trust established in Canada)
    
    .es
    
    
    ES_IDENTIFICATION   Specify the applicable value:
    For contacts inside Spain: Enter your passport ID.
    For contacts outside of Spain: Enter the VAT identification number for the company.
    
    
    Note
    For .es domains, the value of ContactType must be PERSON .
    
    
    ES_IDENTIFICATION_TYPE   Valid values include the following:
    DNI_AND_NIF (For Spanish contacts)
    NIE (For foreigners with legal residence)
    OTHER (For contacts outside of Spain)
    
    
    ES_LEGAL_FORM   Valid values include the following:
    ASSOCIATION
    CENTRAL_GOVERNMENT_BODY
    CIVIL_SOCIETY
    COMMUNITY_OF_OWNERS
    COMMUNITY_PROPERTY
    CONSULATE
    COOPERATIVE
    DESIGNATION_OF_ORIGIN_SUPERVISORY_COUNCIL
    ECONOMIC_INTEREST_GROUP
    EMBASSY
    ENTITY_MANAGING_NATURAL_AREAS
    FARM_PARTNERSHIP
    FOUNDATION
    GENERAL_AND_LIMITED_PARTNERSHIP
    GENERAL_PARTNERSHIP
    INDIVIDUAL
    LIMITED_COMPANY
    LOCAL_AUTHORITY
    LOCAL_PUBLIC_ENTITY
    MUTUAL_INSURANCE_COMPANY
    NATIONAL_PUBLIC_ENTITY
    ORDER_OR_RELIGIOUS_INSTITUTION
    OTHERS (Only for contacts outside of Spain)
    POLITICAL_PARTY
    PROFESSIONAL_ASSOCIATION
    PUBLIC_LAW_ASSOCIATION
    PUBLIC_LIMITED_COMPANY
    REGIONAL_GOVERNMENT_BODY
    REGIONAL_PUBLIC_ENTITY
    SAVINGS_BANK
    SPANISH_OFFICE
    SPORTS_ASSOCIATION
    SPORTS_FEDERATION
    SPORTS_LIMITED_COMPANY
    TEMPORARY_ALLIANCE_OF_ENTERPRISES
    TRADE_UNION
    WORKER_OWNED_COMPANY
    WORKER_OWNED_LIMITED_COMPANY
    
    .fi
    
    BIRTH_DATE_IN_YYYY_MM_DD
    FI_BUSINESS_NUMBER
    FI_ID_NUMBER
    FI_NATIONALITY   Valid values include the following:
    FINNISH
    NOT_FINNISH
    
    
    FI_ORGANIZATION_TYPE   Valid values include the following:
    COMPANY
    CORPORATION
    GOVERNMENT
    INSTITUTION
    POLITICAL_PARTY
    PUBLIC_COMMUNITY
    TOWNSHIP
    
    .fr
    
    BIRTH_CITY
    BIRTH_COUNTRY
    BIRTH_DATE_IN_YYYY_MM_DD
    BIRTH_DEPARTMENT : Specify the INSEE code that corresponds with the department where the contact was born. If the contact was born somewhere other than France or its overseas departments, specify 99 . For more information, including a list of departments and the corresponding INSEE numbers, see the Wikipedia entry Departments of France .
    BRAND_NUMBER.it
    
    IT_NATIONALITY
    IT_PIN
    IT_REGISTRANT_ENTITY_TYPE   Valid values include the following:
    FOREIGNERS
    FREELANCE_WORKERS (Freelance workers and professionals)
    ITALIAN_COMPANIES (Italian companies and one-person companies)
    NON_PROFIT_ORGANIZATIONS
    OTHER_SUBJECTS
    PUBLIC_ORGANIZATIONS
    
    .ru
    
    BIRTH_DATE_IN_YYYY_MM_DD
    RU_PASSPORT_DATA.se
    
    BIRTH_COUNTRY
    SE_ID_NUMBER.sg
    
    SG_ID_NUMBER.co.uk, .me.uk, and .org.uk
    
    UK_CONTACT_TYPE   Valid values include the following:
    CRC (UK Corporation by Royal Charter)
    FCORP (Non-UK Corporation)
    FIND (Non-UK Individual, representing self)
    FOTHER (Non-UK Entity that does not fit into any other category)
    GOV (UK Government Body)
    IND (UK Individual (representing self))
    IP (UK Industrial/Provident Registered Company)
    LLP (UK Limited Liability Partnership)
    LTD (UK Limited Company)
    OTHER (UK Entity that does not fit into any other category)
    PLC (UK Public Limited Company)
    PTNR (UK Partnership)
    RCHAR (UK Registered Charity)
    SCH (UK School)
    STAT (UK Statutory Body)
    STRA (UK Sole Trader)
    
    
    UK_COMPANY_NUMBER
    
    In addition, many TLDs require a VAT_NUMBER .
    
    Value (string) -- [REQUIRED]The value that corresponds with the name of an extra parameter.
    
    
    
    
    
    
    
    RegistrantContact (dict) -- [REQUIRED]
    Provides detailed contact information. For information about the values that you specify for each element, see ContactDetail .
    
    FirstName (string) --First name of contact.
    
    LastName (string) --Last name of contact.
    
    ContactType (string) --Indicates whether the contact is a person, company, association, or public organization. Note the following:
    
    If you specify a value other than PERSON , you must also specify a value for OrganizationName .
    For some TLDs, the privacy protection available depends on the value that you specify for Contact Type . For the privacy protection settings for your TLD, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide
    For .es domains, if you specify PERSON , you must specify INDIVIDUAL for the value of ES_LEGAL_FORM .
    
    
    OrganizationName (string) --Name of the organization for contact types other than PERSON .
    
    AddressLine1 (string) --First line of the contact\'s address.
    
    AddressLine2 (string) --Second line of contact\'s address, if any.
    
    City (string) --The city of the contact\'s address.
    
    State (string) --The state or province of the contact\'s city.
    
    CountryCode (string) --Code for the country of the contact\'s address.
    
    ZipCode (string) --The zip or postal code of the contact\'s address.
    
    PhoneNumber (string) --The phone number of the contact.
    Constraints: Phone number must be specified in the format "+[country dialing code].[number including any area code>]". For example, a US phone number might appear as "+1.1234567890" .
    
    Email (string) --Email address of the contact.
    
    Fax (string) --Fax number of the contact.
    Constraints: Phone number must be specified in the format "+[country dialing code].[number including any area code]". For example, a US phone number might appear as "+1.1234567890" .
    
    ExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.
    
    (dict) --ExtraParam includes the following elements.
    
    Name (string) -- [REQUIRED]The name of an additional parameter that is required by a top-level domain. Here are the top-level domains that require additional parameters and the names of the parameters that they require:
    
    .com.au and .net.au
    
    AU_ID_NUMBER
    AU_ID_TYPE   Valid values include the following:
    ABN (Australian business number)
    ACN (Australian company number)
    TM (Trademark number)
    
    .ca
    
    BRAND_NUMBER
    CA_BUSINESS_ENTITY_TYPE   Valid values include the following:
    BANK (Bank)
    COMMERCIAL_COMPANY (Commercial company)
    COMPANY (Company)
    COOPERATION (Cooperation)
    COOPERATIVE (Cooperative)
    COOPRIX (Cooprix)
    CORP (Corporation)
    CREDIT_UNION (Credit union)
    FOMIA (Federation of mutual insurance associations)
    INC (Incorporated)
    LTD (Limited)
    LTEE (Limit\xc3\xa9e)
    LLC (Limited liability corporation)
    LLP (Limited liability partnership)
    LTE (Lte.)
    MBA (Mutual benefit association)
    MIC (Mutual insurance company)
    NFP (Not-for-profit corporation)
    SA (S.A.)
    SAVINGS_COMPANY (Savings company)
    SAVINGS_UNION (Savings union)
    SARL (Soci\xc3\xa9t\xc3\xa9 \xc3\xa0 responsabilit\xc3\xa9 limit\xc3\xa9e)
    TRUST (Trust)
    ULC (Unlimited liability corporation)
    
    
    CA_LEGAL_TYPE   When ContactType is PERSON , valid values include the following:
    ABO (Aboriginal Peoples indigenous to Canada)
    CCT (Canadian citizen)
    LGR (Legal Representative of a Canadian Citizen or Permanent Resident)
    RES (Permanent resident of Canada)
    
    
    
    When ContactType is a value other than PERSON , valid values include the following:
    
    
    ASS (Canadian unincorporated association)
    CCO (Canadian corporation)
    EDU (Canadian educational institution)
    GOV (Government or government entity in Canada)
    HOP (Canadian Hospital)
    INB (Indian Band recognized by the Indian Act of Canada)
    LAM (Canadian Library, Archive, or Museum)
    MAJ (Her/His Majesty the Queen/King)
    OMK (Official mark registered in Canada)
    PLT (Canadian Political Party)
    PRT (Partnership Registered in Canada)
    TDM (Trademark registered in Canada)
    TRD (Canadian Trade Union)
    TRS (Trust established in Canada)
    
    .es
    
    
    ES_IDENTIFICATION   Specify the applicable value:
    For contacts inside Spain: Enter your passport ID.
    For contacts outside of Spain: Enter the VAT identification number for the company.
    
    
    Note
    For .es domains, the value of ContactType must be PERSON .
    
    
    ES_IDENTIFICATION_TYPE   Valid values include the following:
    DNI_AND_NIF (For Spanish contacts)
    NIE (For foreigners with legal residence)
    OTHER (For contacts outside of Spain)
    
    
    ES_LEGAL_FORM   Valid values include the following:
    ASSOCIATION
    CENTRAL_GOVERNMENT_BODY
    CIVIL_SOCIETY
    COMMUNITY_OF_OWNERS
    COMMUNITY_PROPERTY
    CONSULATE
    COOPERATIVE
    DESIGNATION_OF_ORIGIN_SUPERVISORY_COUNCIL
    ECONOMIC_INTEREST_GROUP
    EMBASSY
    ENTITY_MANAGING_NATURAL_AREAS
    FARM_PARTNERSHIP
    FOUNDATION
    GENERAL_AND_LIMITED_PARTNERSHIP
    GENERAL_PARTNERSHIP
    INDIVIDUAL
    LIMITED_COMPANY
    LOCAL_AUTHORITY
    LOCAL_PUBLIC_ENTITY
    MUTUAL_INSURANCE_COMPANY
    NATIONAL_PUBLIC_ENTITY
    ORDER_OR_RELIGIOUS_INSTITUTION
    OTHERS (Only for contacts outside of Spain)
    POLITICAL_PARTY
    PROFESSIONAL_ASSOCIATION
    PUBLIC_LAW_ASSOCIATION
    PUBLIC_LIMITED_COMPANY
    REGIONAL_GOVERNMENT_BODY
    REGIONAL_PUBLIC_ENTITY
    SAVINGS_BANK
    SPANISH_OFFICE
    SPORTS_ASSOCIATION
    SPORTS_FEDERATION
    SPORTS_LIMITED_COMPANY
    TEMPORARY_ALLIANCE_OF_ENTERPRISES
    TRADE_UNION
    WORKER_OWNED_COMPANY
    WORKER_OWNED_LIMITED_COMPANY
    
    .fi
    
    BIRTH_DATE_IN_YYYY_MM_DD
    FI_BUSINESS_NUMBER
    FI_ID_NUMBER
    FI_NATIONALITY   Valid values include the following:
    FINNISH
    NOT_FINNISH
    
    
    FI_ORGANIZATION_TYPE   Valid values include the following:
    COMPANY
    CORPORATION
    GOVERNMENT
    INSTITUTION
    POLITICAL_PARTY
    PUBLIC_COMMUNITY
    TOWNSHIP
    
    .fr
    
    BIRTH_CITY
    BIRTH_COUNTRY
    BIRTH_DATE_IN_YYYY_MM_DD
    BIRTH_DEPARTMENT : Specify the INSEE code that corresponds with the department where the contact was born. If the contact was born somewhere other than France or its overseas departments, specify 99 . For more information, including a list of departments and the corresponding INSEE numbers, see the Wikipedia entry Departments of France .
    BRAND_NUMBER.it
    
    IT_NATIONALITY
    IT_PIN
    IT_REGISTRANT_ENTITY_TYPE   Valid values include the following:
    FOREIGNERS
    FREELANCE_WORKERS (Freelance workers and professionals)
    ITALIAN_COMPANIES (Italian companies and one-person companies)
    NON_PROFIT_ORGANIZATIONS
    OTHER_SUBJECTS
    PUBLIC_ORGANIZATIONS
    
    .ru
    
    BIRTH_DATE_IN_YYYY_MM_DD
    RU_PASSPORT_DATA.se
    
    BIRTH_COUNTRY
    SE_ID_NUMBER.sg
    
    SG_ID_NUMBER.co.uk, .me.uk, and .org.uk
    
    UK_CONTACT_TYPE   Valid values include the following:
    CRC (UK Corporation by Royal Charter)
    FCORP (Non-UK Corporation)
    FIND (Non-UK Individual, representing self)
    FOTHER (Non-UK Entity that does not fit into any other category)
    GOV (UK Government Body)
    IND (UK Individual (representing self))
    IP (UK Industrial/Provident Registered Company)
    LLP (UK Limited Liability Partnership)
    LTD (UK Limited Company)
    OTHER (UK Entity that does not fit into any other category)
    PLC (UK Public Limited Company)
    PTNR (UK Partnership)
    RCHAR (UK Registered Charity)
    SCH (UK School)
    STAT (UK Statutory Body)
    STRA (UK Sole Trader)
    
    
    UK_COMPANY_NUMBER
    
    In addition, many TLDs require a VAT_NUMBER .
    
    Value (string) -- [REQUIRED]The value that corresponds with the name of an extra parameter.
    
    
    
    
    
    
    
    TechContact (dict) -- [REQUIRED]
    Provides detailed contact information. For information about the values that you specify for each element, see ContactDetail .
    
    FirstName (string) --First name of contact.
    
    LastName (string) --Last name of contact.
    
    ContactType (string) --Indicates whether the contact is a person, company, association, or public organization. Note the following:
    
    If you specify a value other than PERSON , you must also specify a value for OrganizationName .
    For some TLDs, the privacy protection available depends on the value that you specify for Contact Type . For the privacy protection settings for your TLD, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide
    For .es domains, if you specify PERSON , you must specify INDIVIDUAL for the value of ES_LEGAL_FORM .
    
    
    OrganizationName (string) --Name of the organization for contact types other than PERSON .
    
    AddressLine1 (string) --First line of the contact\'s address.
    
    AddressLine2 (string) --Second line of contact\'s address, if any.
    
    City (string) --The city of the contact\'s address.
    
    State (string) --The state or province of the contact\'s city.
    
    CountryCode (string) --Code for the country of the contact\'s address.
    
    ZipCode (string) --The zip or postal code of the contact\'s address.
    
    PhoneNumber (string) --The phone number of the contact.
    Constraints: Phone number must be specified in the format "+[country dialing code].[number including any area code>]". For example, a US phone number might appear as "+1.1234567890" .
    
    Email (string) --Email address of the contact.
    
    Fax (string) --Fax number of the contact.
    Constraints: Phone number must be specified in the format "+[country dialing code].[number including any area code]". For example, a US phone number might appear as "+1.1234567890" .
    
    ExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.
    
    (dict) --ExtraParam includes the following elements.
    
    Name (string) -- [REQUIRED]The name of an additional parameter that is required by a top-level domain. Here are the top-level domains that require additional parameters and the names of the parameters that they require:
    
    .com.au and .net.au
    
    AU_ID_NUMBER
    AU_ID_TYPE   Valid values include the following:
    ABN (Australian business number)
    ACN (Australian company number)
    TM (Trademark number)
    
    .ca
    
    BRAND_NUMBER
    CA_BUSINESS_ENTITY_TYPE   Valid values include the following:
    BANK (Bank)
    COMMERCIAL_COMPANY (Commercial company)
    COMPANY (Company)
    COOPERATION (Cooperation)
    COOPERATIVE (Cooperative)
    COOPRIX (Cooprix)
    CORP (Corporation)
    CREDIT_UNION (Credit union)
    FOMIA (Federation of mutual insurance associations)
    INC (Incorporated)
    LTD (Limited)
    LTEE (Limit\xc3\xa9e)
    LLC (Limited liability corporation)
    LLP (Limited liability partnership)
    LTE (Lte.)
    MBA (Mutual benefit association)
    MIC (Mutual insurance company)
    NFP (Not-for-profit corporation)
    SA (S.A.)
    SAVINGS_COMPANY (Savings company)
    SAVINGS_UNION (Savings union)
    SARL (Soci\xc3\xa9t\xc3\xa9 \xc3\xa0 responsabilit\xc3\xa9 limit\xc3\xa9e)
    TRUST (Trust)
    ULC (Unlimited liability corporation)
    
    
    CA_LEGAL_TYPE   When ContactType is PERSON , valid values include the following:
    ABO (Aboriginal Peoples indigenous to Canada)
    CCT (Canadian citizen)
    LGR (Legal Representative of a Canadian Citizen or Permanent Resident)
    RES (Permanent resident of Canada)
    
    
    
    When ContactType is a value other than PERSON , valid values include the following:
    
    
    ASS (Canadian unincorporated association)
    CCO (Canadian corporation)
    EDU (Canadian educational institution)
    GOV (Government or government entity in Canada)
    HOP (Canadian Hospital)
    INB (Indian Band recognized by the Indian Act of Canada)
    LAM (Canadian Library, Archive, or Museum)
    MAJ (Her/His Majesty the Queen/King)
    OMK (Official mark registered in Canada)
    PLT (Canadian Political Party)
    PRT (Partnership Registered in Canada)
    TDM (Trademark registered in Canada)
    TRD (Canadian Trade Union)
    TRS (Trust established in Canada)
    
    .es
    
    
    ES_IDENTIFICATION   Specify the applicable value:
    For contacts inside Spain: Enter your passport ID.
    For contacts outside of Spain: Enter the VAT identification number for the company.
    
    
    Note
    For .es domains, the value of ContactType must be PERSON .
    
    
    ES_IDENTIFICATION_TYPE   Valid values include the following:
    DNI_AND_NIF (For Spanish contacts)
    NIE (For foreigners with legal residence)
    OTHER (For contacts outside of Spain)
    
    
    ES_LEGAL_FORM   Valid values include the following:
    ASSOCIATION
    CENTRAL_GOVERNMENT_BODY
    CIVIL_SOCIETY
    COMMUNITY_OF_OWNERS
    COMMUNITY_PROPERTY
    CONSULATE
    COOPERATIVE
    DESIGNATION_OF_ORIGIN_SUPERVISORY_COUNCIL
    ECONOMIC_INTEREST_GROUP
    EMBASSY
    ENTITY_MANAGING_NATURAL_AREAS
    FARM_PARTNERSHIP
    FOUNDATION
    GENERAL_AND_LIMITED_PARTNERSHIP
    GENERAL_PARTNERSHIP
    INDIVIDUAL
    LIMITED_COMPANY
    LOCAL_AUTHORITY
    LOCAL_PUBLIC_ENTITY
    MUTUAL_INSURANCE_COMPANY
    NATIONAL_PUBLIC_ENTITY
    ORDER_OR_RELIGIOUS_INSTITUTION
    OTHERS (Only for contacts outside of Spain)
    POLITICAL_PARTY
    PROFESSIONAL_ASSOCIATION
    PUBLIC_LAW_ASSOCIATION
    PUBLIC_LIMITED_COMPANY
    REGIONAL_GOVERNMENT_BODY
    REGIONAL_PUBLIC_ENTITY
    SAVINGS_BANK
    SPANISH_OFFICE
    SPORTS_ASSOCIATION
    SPORTS_FEDERATION
    SPORTS_LIMITED_COMPANY
    TEMPORARY_ALLIANCE_OF_ENTERPRISES
    TRADE_UNION
    WORKER_OWNED_COMPANY
    WORKER_OWNED_LIMITED_COMPANY
    
    .fi
    
    BIRTH_DATE_IN_YYYY_MM_DD
    FI_BUSINESS_NUMBER
    FI_ID_NUMBER
    FI_NATIONALITY   Valid values include the following:
    FINNISH
    NOT_FINNISH
    
    
    FI_ORGANIZATION_TYPE   Valid values include the following:
    COMPANY
    CORPORATION
    GOVERNMENT
    INSTITUTION
    POLITICAL_PARTY
    PUBLIC_COMMUNITY
    TOWNSHIP
    
    .fr
    
    BIRTH_CITY
    BIRTH_COUNTRY
    BIRTH_DATE_IN_YYYY_MM_DD
    BIRTH_DEPARTMENT : Specify the INSEE code that corresponds with the department where the contact was born. If the contact was born somewhere other than France or its overseas departments, specify 99 . For more information, including a list of departments and the corresponding INSEE numbers, see the Wikipedia entry Departments of France .
    BRAND_NUMBER.it
    
    IT_NATIONALITY
    IT_PIN
    IT_REGISTRANT_ENTITY_TYPE   Valid values include the following:
    FOREIGNERS
    FREELANCE_WORKERS (Freelance workers and professionals)
    ITALIAN_COMPANIES (Italian companies and one-person companies)
    NON_PROFIT_ORGANIZATIONS
    OTHER_SUBJECTS
    PUBLIC_ORGANIZATIONS
    
    .ru
    
    BIRTH_DATE_IN_YYYY_MM_DD
    RU_PASSPORT_DATA.se
    
    BIRTH_COUNTRY
    SE_ID_NUMBER.sg
    
    SG_ID_NUMBER.co.uk, .me.uk, and .org.uk
    
    UK_CONTACT_TYPE   Valid values include the following:
    CRC (UK Corporation by Royal Charter)
    FCORP (Non-UK Corporation)
    FIND (Non-UK Individual, representing self)
    FOTHER (Non-UK Entity that does not fit into any other category)
    GOV (UK Government Body)
    IND (UK Individual (representing self))
    IP (UK Industrial/Provident Registered Company)
    LLP (UK Limited Liability Partnership)
    LTD (UK Limited Company)
    OTHER (UK Entity that does not fit into any other category)
    PLC (UK Public Limited Company)
    PTNR (UK Partnership)
    RCHAR (UK Registered Charity)
    SCH (UK School)
    STAT (UK Statutory Body)
    STRA (UK Sole Trader)
    
    
    UK_COMPANY_NUMBER
    
    In addition, many TLDs require a VAT_NUMBER .
    
    Value (string) -- [REQUIRED]The value that corresponds with the name of an extra parameter.
    
    
    
    
    
    
    
    PrivacyProtectAdminContact (boolean) -- Whether you want to conceal contact information from WHOIS queries. If you specify true , WHOIS ("who is") queries return contact information either for Amazon Registrar (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other TLDs). If you specify false , WHOIS queries return the information that you entered for the admin contact.
    Default: true
    
    PrivacyProtectRegistrantContact (boolean) -- Whether you want to conceal contact information from WHOIS queries. If you specify true , WHOIS ("who is") queries return contact information either for Amazon Registrar (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other TLDs). If you specify false , WHOIS queries return the information that you entered for the registrant contact (the domain owner).
    Default: true
    
    PrivacyProtectTechContact (boolean) -- Whether you want to conceal contact information from WHOIS queries. If you specify true , WHOIS ("who is") queries return contact information either for Amazon Registrar (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other TLDs). If you specify false , WHOIS queries return the information that you entered for the technical contact.
    Default: true
    
    
    """
    pass

def reject_domain_transfer_from_another_aws_account(DomainName=None):
    """
    Rejects the transfer of a domain from another AWS account to the current AWS account. You initiate a transfer between AWS accounts using TransferDomainToAnotherAwsAccount .
    Use either ListOperations or GetOperationDetail to determine whether the operation succeeded. GetOperationDetail provides additional information, for example, Domain Transfer from Aws Account 111122223333 has been cancelled .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.reject_domain_transfer_from_another_aws_account(
        DomainName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe name of the domain that was specified when another AWS account submitted a TransferDomainToAnotherAwsAccount request.\n

    :rtype: dict
ReturnsResponse Syntax{
    'OperationId': 'string'
}


Response Structure

(dict) --The RejectDomainTransferFromAnotherAwsAccount response includes the following element.

OperationId (string) --The identifier that TransferDomainToAnotherAwsAccount returned to track the progress of the request. Because the transfer request was rejected, the value is no longer valid, and you can\'t use GetOperationDetail to query the operation status.






Exceptions

Route53Domains.Client.exceptions.InvalidInput
Route53Domains.Client.exceptions.OperationLimitExceeded


    :return: {
        'OperationId': 'string'
    }
    
    
    """
    pass

def renew_domain(DomainName=None, DurationInYears=None, CurrentExpiryYear=None):
    """
    This operation renews a domain for the specified number of years. The cost of renewing your domain is billed to your AWS account.
    We recommend that you renew your domain several weeks before the expiration date. Some TLD registries delete domains before the expiration date if you haven\'t renewed far enough in advance. For more information about renewing domain registration, see Renewing Registration for a Domain in the Amazon Route 53 Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.renew_domain(
        DomainName='string',
        DurationInYears=123,
        CurrentExpiryYear=123
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe name of the domain that you want to renew.\n

    :type DurationInYears: integer
    :param DurationInYears: The number of years that you want to renew the domain for. The maximum number of years depends on the top-level domain. For the range of valid values for your domain, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide .\nDefault: 1\n

    :type CurrentExpiryYear: integer
    :param CurrentExpiryYear: [REQUIRED]\nThe year when the registration for the domain is set to expire. This value must match the current expiration date for the domain.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'OperationId': 'string'
}


Response Structure

(dict) --

OperationId (string) --
Identifier for tracking the progress of the request. To query the operation status, use GetOperationDetail .







Exceptions

Route53Domains.Client.exceptions.InvalidInput
Route53Domains.Client.exceptions.UnsupportedTLD
Route53Domains.Client.exceptions.DuplicateRequest
Route53Domains.Client.exceptions.TLDRulesViolation
Route53Domains.Client.exceptions.OperationLimitExceeded


    :return: {
        'OperationId': 'string'
    }
    
    
    :returns: 
    Route53Domains.Client.exceptions.InvalidInput
    Route53Domains.Client.exceptions.UnsupportedTLD
    Route53Domains.Client.exceptions.DuplicateRequest
    Route53Domains.Client.exceptions.TLDRulesViolation
    Route53Domains.Client.exceptions.OperationLimitExceeded
    
    """
    pass

def resend_contact_reachability_email(domainName=None):
    """
    For operations that require confirmation that the email address for the registrant contact is valid, such as registering a new domain, this operation resends the confirmation email to the current email address for the registrant contact.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.resend_contact_reachability_email(
        domainName='string'
    )
    
    
    :type domainName: string
    :param domainName: The name of the domain for which you want Route 53 to resend a confirmation email to the registrant contact.

    :rtype: dict
ReturnsResponse Syntax{
    'domainName': 'string',
    'emailAddress': 'string',
    'isAlreadyVerified': True|False
}


Response Structure

(dict) --
domainName (string) --The domain name for which you requested a confirmation email.

emailAddress (string) --The email address for the registrant contact at the time that we sent the verification email.

isAlreadyVerified (boolean) --
True if the email address for the registrant contact has already been verified, and false otherwise. If the email address has already been verified, we don\'t send another confirmation email.






Exceptions

Route53Domains.Client.exceptions.InvalidInput
Route53Domains.Client.exceptions.OperationLimitExceeded
Route53Domains.Client.exceptions.UnsupportedTLD


    :return: {
        'domainName': 'string',
        'emailAddress': 'string',
        'isAlreadyVerified': True|False
    }
    
    
    """
    pass

def retrieve_domain_auth_code(DomainName=None):
    """
    This operation returns the AuthCode for the domain. To transfer a domain to another registrar, you provide this value to the new registrar.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.retrieve_domain_auth_code(
        DomainName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe name of the domain that you want to get an authorization code for.\n

    :rtype: dict
ReturnsResponse Syntax{
    'AuthCode': 'string'
}


Response Structure

(dict) --The RetrieveDomainAuthCode response includes the following element.

AuthCode (string) --The authorization code for the domain.






Exceptions

Route53Domains.Client.exceptions.InvalidInput
Route53Domains.Client.exceptions.UnsupportedTLD


    :return: {
        'AuthCode': 'string'
    }
    
    
    """
    pass

def transfer_domain(DomainName=None, IdnLangCode=None, DurationInYears=None, Nameservers=None, AuthCode=None, AutoRenew=None, AdminContact=None, RegistrantContact=None, TechContact=None, PrivacyProtectAdminContact=None, PrivacyProtectRegistrantContact=None, PrivacyProtectTechContact=None):
    """
    Transfers a domain from another registrar to Amazon Route 53. When the transfer is complete, the domain is registered either with Amazon Registrar (for .com, .net, and .org domains) or with our registrar associate, Gandi (for all other TLDs).
    For more information about transferring domains, see the following topics:
    If the registrar for your domain is also the DNS service provider for the domain, we highly recommend that you transfer your DNS service to Route 53 or to another DNS service provider before you transfer your registration. Some registrars provide free DNS service when you purchase a domain registration. When you transfer the registration, the previous registrar will not renew your domain registration and could end your DNS service at any time.
    If the transfer is successful, this method returns an operation ID that you can use to track the progress and completion of the action. If the transfer doesn\'t complete successfully, the domain registrant will be notified by email.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.transfer_domain(
        DomainName='string',
        IdnLangCode='string',
        DurationInYears=123,
        Nameservers=[
            {
                'Name': 'string',
                'GlueIps': [
                    'string',
                ]
            },
        ],
        AuthCode='string',
        AutoRenew=True|False,
        AdminContact={
            'FirstName': 'string',
            'LastName': 'string',
            'ContactType': 'PERSON'|'COMPANY'|'ASSOCIATION'|'PUBLIC_BODY'|'RESELLER',
            'OrganizationName': 'string',
            'AddressLine1': 'string',
            'AddressLine2': 'string',
            'City': 'string',
            'State': 'string',
            'CountryCode': 'AD'|'AE'|'AF'|'AG'|'AI'|'AL'|'AM'|'AN'|'AO'|'AQ'|'AR'|'AS'|'AT'|'AU'|'AW'|'AZ'|'BA'|'BB'|'BD'|'BE'|'BF'|'BG'|'BH'|'BI'|'BJ'|'BL'|'BM'|'BN'|'BO'|'BR'|'BS'|'BT'|'BW'|'BY'|'BZ'|'CA'|'CC'|'CD'|'CF'|'CG'|'CH'|'CI'|'CK'|'CL'|'CM'|'CN'|'CO'|'CR'|'CU'|'CV'|'CX'|'CY'|'CZ'|'DE'|'DJ'|'DK'|'DM'|'DO'|'DZ'|'EC'|'EE'|'EG'|'ER'|'ES'|'ET'|'FI'|'FJ'|'FK'|'FM'|'FO'|'FR'|'GA'|'GB'|'GD'|'GE'|'GH'|'GI'|'GL'|'GM'|'GN'|'GQ'|'GR'|'GT'|'GU'|'GW'|'GY'|'HK'|'HN'|'HR'|'HT'|'HU'|'ID'|'IE'|'IL'|'IM'|'IN'|'IQ'|'IR'|'IS'|'IT'|'JM'|'JO'|'JP'|'KE'|'KG'|'KH'|'KI'|'KM'|'KN'|'KP'|'KR'|'KW'|'KY'|'KZ'|'LA'|'LB'|'LC'|'LI'|'LK'|'LR'|'LS'|'LT'|'LU'|'LV'|'LY'|'MA'|'MC'|'MD'|'ME'|'MF'|'MG'|'MH'|'MK'|'ML'|'MM'|'MN'|'MO'|'MP'|'MR'|'MS'|'MT'|'MU'|'MV'|'MW'|'MX'|'MY'|'MZ'|'NA'|'NC'|'NE'|'NG'|'NI'|'NL'|'NO'|'NP'|'NR'|'NU'|'NZ'|'OM'|'PA'|'PE'|'PF'|'PG'|'PH'|'PK'|'PL'|'PM'|'PN'|'PR'|'PT'|'PW'|'PY'|'QA'|'RO'|'RS'|'RU'|'RW'|'SA'|'SB'|'SC'|'SD'|'SE'|'SG'|'SH'|'SI'|'SK'|'SL'|'SM'|'SN'|'SO'|'SR'|'ST'|'SV'|'SY'|'SZ'|'TC'|'TD'|'TG'|'TH'|'TJ'|'TK'|'TL'|'TM'|'TN'|'TO'|'TR'|'TT'|'TV'|'TW'|'TZ'|'UA'|'UG'|'US'|'UY'|'UZ'|'VA'|'VC'|'VE'|'VG'|'VI'|'VN'|'VU'|'WF'|'WS'|'YE'|'YT'|'ZA'|'ZM'|'ZW',
            'ZipCode': 'string',
            'PhoneNumber': 'string',
            'Email': 'string',
            'Fax': 'string',
            'ExtraParams': [
                {
                    'Name': 'DUNS_NUMBER'|'BRAND_NUMBER'|'BIRTH_DEPARTMENT'|'BIRTH_DATE_IN_YYYY_MM_DD'|'BIRTH_COUNTRY'|'BIRTH_CITY'|'DOCUMENT_NUMBER'|'AU_ID_NUMBER'|'AU_ID_TYPE'|'CA_LEGAL_TYPE'|'CA_BUSINESS_ENTITY_TYPE'|'CA_LEGAL_REPRESENTATIVE'|'CA_LEGAL_REPRESENTATIVE_CAPACITY'|'ES_IDENTIFICATION'|'ES_IDENTIFICATION_TYPE'|'ES_LEGAL_FORM'|'FI_BUSINESS_NUMBER'|'FI_ID_NUMBER'|'FI_NATIONALITY'|'FI_ORGANIZATION_TYPE'|'IT_NATIONALITY'|'IT_PIN'|'IT_REGISTRANT_ENTITY_TYPE'|'RU_PASSPORT_DATA'|'SE_ID_NUMBER'|'SG_ID_NUMBER'|'VAT_NUMBER'|'UK_CONTACT_TYPE'|'UK_COMPANY_NUMBER',
                    'Value': 'string'
                },
            ]
        },
        RegistrantContact={
            'FirstName': 'string',
            'LastName': 'string',
            'ContactType': 'PERSON'|'COMPANY'|'ASSOCIATION'|'PUBLIC_BODY'|'RESELLER',
            'OrganizationName': 'string',
            'AddressLine1': 'string',
            'AddressLine2': 'string',
            'City': 'string',
            'State': 'string',
            'CountryCode': 'AD'|'AE'|'AF'|'AG'|'AI'|'AL'|'AM'|'AN'|'AO'|'AQ'|'AR'|'AS'|'AT'|'AU'|'AW'|'AZ'|'BA'|'BB'|'BD'|'BE'|'BF'|'BG'|'BH'|'BI'|'BJ'|'BL'|'BM'|'BN'|'BO'|'BR'|'BS'|'BT'|'BW'|'BY'|'BZ'|'CA'|'CC'|'CD'|'CF'|'CG'|'CH'|'CI'|'CK'|'CL'|'CM'|'CN'|'CO'|'CR'|'CU'|'CV'|'CX'|'CY'|'CZ'|'DE'|'DJ'|'DK'|'DM'|'DO'|'DZ'|'EC'|'EE'|'EG'|'ER'|'ES'|'ET'|'FI'|'FJ'|'FK'|'FM'|'FO'|'FR'|'GA'|'GB'|'GD'|'GE'|'GH'|'GI'|'GL'|'GM'|'GN'|'GQ'|'GR'|'GT'|'GU'|'GW'|'GY'|'HK'|'HN'|'HR'|'HT'|'HU'|'ID'|'IE'|'IL'|'IM'|'IN'|'IQ'|'IR'|'IS'|'IT'|'JM'|'JO'|'JP'|'KE'|'KG'|'KH'|'KI'|'KM'|'KN'|'KP'|'KR'|'KW'|'KY'|'KZ'|'LA'|'LB'|'LC'|'LI'|'LK'|'LR'|'LS'|'LT'|'LU'|'LV'|'LY'|'MA'|'MC'|'MD'|'ME'|'MF'|'MG'|'MH'|'MK'|'ML'|'MM'|'MN'|'MO'|'MP'|'MR'|'MS'|'MT'|'MU'|'MV'|'MW'|'MX'|'MY'|'MZ'|'NA'|'NC'|'NE'|'NG'|'NI'|'NL'|'NO'|'NP'|'NR'|'NU'|'NZ'|'OM'|'PA'|'PE'|'PF'|'PG'|'PH'|'PK'|'PL'|'PM'|'PN'|'PR'|'PT'|'PW'|'PY'|'QA'|'RO'|'RS'|'RU'|'RW'|'SA'|'SB'|'SC'|'SD'|'SE'|'SG'|'SH'|'SI'|'SK'|'SL'|'SM'|'SN'|'SO'|'SR'|'ST'|'SV'|'SY'|'SZ'|'TC'|'TD'|'TG'|'TH'|'TJ'|'TK'|'TL'|'TM'|'TN'|'TO'|'TR'|'TT'|'TV'|'TW'|'TZ'|'UA'|'UG'|'US'|'UY'|'UZ'|'VA'|'VC'|'VE'|'VG'|'VI'|'VN'|'VU'|'WF'|'WS'|'YE'|'YT'|'ZA'|'ZM'|'ZW',
            'ZipCode': 'string',
            'PhoneNumber': 'string',
            'Email': 'string',
            'Fax': 'string',
            'ExtraParams': [
                {
                    'Name': 'DUNS_NUMBER'|'BRAND_NUMBER'|'BIRTH_DEPARTMENT'|'BIRTH_DATE_IN_YYYY_MM_DD'|'BIRTH_COUNTRY'|'BIRTH_CITY'|'DOCUMENT_NUMBER'|'AU_ID_NUMBER'|'AU_ID_TYPE'|'CA_LEGAL_TYPE'|'CA_BUSINESS_ENTITY_TYPE'|'CA_LEGAL_REPRESENTATIVE'|'CA_LEGAL_REPRESENTATIVE_CAPACITY'|'ES_IDENTIFICATION'|'ES_IDENTIFICATION_TYPE'|'ES_LEGAL_FORM'|'FI_BUSINESS_NUMBER'|'FI_ID_NUMBER'|'FI_NATIONALITY'|'FI_ORGANIZATION_TYPE'|'IT_NATIONALITY'|'IT_PIN'|'IT_REGISTRANT_ENTITY_TYPE'|'RU_PASSPORT_DATA'|'SE_ID_NUMBER'|'SG_ID_NUMBER'|'VAT_NUMBER'|'UK_CONTACT_TYPE'|'UK_COMPANY_NUMBER',
                    'Value': 'string'
                },
            ]
        },
        TechContact={
            'FirstName': 'string',
            'LastName': 'string',
            'ContactType': 'PERSON'|'COMPANY'|'ASSOCIATION'|'PUBLIC_BODY'|'RESELLER',
            'OrganizationName': 'string',
            'AddressLine1': 'string',
            'AddressLine2': 'string',
            'City': 'string',
            'State': 'string',
            'CountryCode': 'AD'|'AE'|'AF'|'AG'|'AI'|'AL'|'AM'|'AN'|'AO'|'AQ'|'AR'|'AS'|'AT'|'AU'|'AW'|'AZ'|'BA'|'BB'|'BD'|'BE'|'BF'|'BG'|'BH'|'BI'|'BJ'|'BL'|'BM'|'BN'|'BO'|'BR'|'BS'|'BT'|'BW'|'BY'|'BZ'|'CA'|'CC'|'CD'|'CF'|'CG'|'CH'|'CI'|'CK'|'CL'|'CM'|'CN'|'CO'|'CR'|'CU'|'CV'|'CX'|'CY'|'CZ'|'DE'|'DJ'|'DK'|'DM'|'DO'|'DZ'|'EC'|'EE'|'EG'|'ER'|'ES'|'ET'|'FI'|'FJ'|'FK'|'FM'|'FO'|'FR'|'GA'|'GB'|'GD'|'GE'|'GH'|'GI'|'GL'|'GM'|'GN'|'GQ'|'GR'|'GT'|'GU'|'GW'|'GY'|'HK'|'HN'|'HR'|'HT'|'HU'|'ID'|'IE'|'IL'|'IM'|'IN'|'IQ'|'IR'|'IS'|'IT'|'JM'|'JO'|'JP'|'KE'|'KG'|'KH'|'KI'|'KM'|'KN'|'KP'|'KR'|'KW'|'KY'|'KZ'|'LA'|'LB'|'LC'|'LI'|'LK'|'LR'|'LS'|'LT'|'LU'|'LV'|'LY'|'MA'|'MC'|'MD'|'ME'|'MF'|'MG'|'MH'|'MK'|'ML'|'MM'|'MN'|'MO'|'MP'|'MR'|'MS'|'MT'|'MU'|'MV'|'MW'|'MX'|'MY'|'MZ'|'NA'|'NC'|'NE'|'NG'|'NI'|'NL'|'NO'|'NP'|'NR'|'NU'|'NZ'|'OM'|'PA'|'PE'|'PF'|'PG'|'PH'|'PK'|'PL'|'PM'|'PN'|'PR'|'PT'|'PW'|'PY'|'QA'|'RO'|'RS'|'RU'|'RW'|'SA'|'SB'|'SC'|'SD'|'SE'|'SG'|'SH'|'SI'|'SK'|'SL'|'SM'|'SN'|'SO'|'SR'|'ST'|'SV'|'SY'|'SZ'|'TC'|'TD'|'TG'|'TH'|'TJ'|'TK'|'TL'|'TM'|'TN'|'TO'|'TR'|'TT'|'TV'|'TW'|'TZ'|'UA'|'UG'|'US'|'UY'|'UZ'|'VA'|'VC'|'VE'|'VG'|'VI'|'VN'|'VU'|'WF'|'WS'|'YE'|'YT'|'ZA'|'ZM'|'ZW',
            'ZipCode': 'string',
            'PhoneNumber': 'string',
            'Email': 'string',
            'Fax': 'string',
            'ExtraParams': [
                {
                    'Name': 'DUNS_NUMBER'|'BRAND_NUMBER'|'BIRTH_DEPARTMENT'|'BIRTH_DATE_IN_YYYY_MM_DD'|'BIRTH_COUNTRY'|'BIRTH_CITY'|'DOCUMENT_NUMBER'|'AU_ID_NUMBER'|'AU_ID_TYPE'|'CA_LEGAL_TYPE'|'CA_BUSINESS_ENTITY_TYPE'|'CA_LEGAL_REPRESENTATIVE'|'CA_LEGAL_REPRESENTATIVE_CAPACITY'|'ES_IDENTIFICATION'|'ES_IDENTIFICATION_TYPE'|'ES_LEGAL_FORM'|'FI_BUSINESS_NUMBER'|'FI_ID_NUMBER'|'FI_NATIONALITY'|'FI_ORGANIZATION_TYPE'|'IT_NATIONALITY'|'IT_PIN'|'IT_REGISTRANT_ENTITY_TYPE'|'RU_PASSPORT_DATA'|'SE_ID_NUMBER'|'SG_ID_NUMBER'|'VAT_NUMBER'|'UK_CONTACT_TYPE'|'UK_COMPANY_NUMBER',
                    'Value': 'string'
                },
            ]
        },
        PrivacyProtectAdminContact=True|False,
        PrivacyProtectRegistrantContact=True|False,
        PrivacyProtectTechContact=True|False
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe name of the domain that you want to transfer to Route 53. The top-level domain (TLD), such as .com, must be a TLD that Route 53 supports. For a list of supported TLDs, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide .\nThe domain name can contain only the following characters:\n\nLetters a through z. Domain names are not case sensitive.\nNumbers 0 through 9.\nHyphen (-). You can\'t specify a hyphen at the beginning or end of a label.\nPeriod (.) to separate the labels in the name, such as the . in example.com .\n\n

    :type IdnLangCode: string
    :param IdnLangCode: Reserved for future use.

    :type DurationInYears: integer
    :param DurationInYears: [REQUIRED]\nThe number of years that you want to register the domain for. Domains are registered for a minimum of one year. The maximum period depends on the top-level domain.\nDefault: 1\n

    :type Nameservers: list
    :param Nameservers: Contains details for the host and glue IP addresses.\n\n(dict) --Nameserver includes the following elements.\n\nName (string) -- [REQUIRED]The fully qualified host name of the name server.\nConstraint: Maximum 255 characters\n\nGlueIps (list) --Glue IP address of a name server entry. Glue IP addresses are required only when the name of the name server is a subdomain of the domain. For example, if your domain is example.com and the name server for the domain is ns.example.com, you need to specify the IP address for ns.example.com.\nConstraints: The list can contain only one IPv4 and one IPv6 address.\n\n(string) --\n\n\n\n\n\n

    :type AuthCode: string
    :param AuthCode: The authorization code for the domain. You get this value from the current registrar.

    :type AutoRenew: boolean
    :param AutoRenew: Indicates whether the domain will be automatically renewed (true) or not (false). Autorenewal only takes effect after the account is charged.\nDefault: true\n

    :type AdminContact: dict
    :param AdminContact: [REQUIRED]\nProvides detailed contact information.\n\nFirstName (string) --First name of contact.\n\nLastName (string) --Last name of contact.\n\nContactType (string) --Indicates whether the contact is a person, company, association, or public organization. Note the following:\n\nIf you specify a value other than PERSON , you must also specify a value for OrganizationName .\nFor some TLDs, the privacy protection available depends on the value that you specify for Contact Type . For the privacy protection settings for your TLD, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide\nFor .es domains, if you specify PERSON , you must specify INDIVIDUAL for the value of ES_LEGAL_FORM .\n\n\nOrganizationName (string) --Name of the organization for contact types other than PERSON .\n\nAddressLine1 (string) --First line of the contact\'s address.\n\nAddressLine2 (string) --Second line of contact\'s address, if any.\n\nCity (string) --The city of the contact\'s address.\n\nState (string) --The state or province of the contact\'s city.\n\nCountryCode (string) --Code for the country of the contact\'s address.\n\nZipCode (string) --The zip or postal code of the contact\'s address.\n\nPhoneNumber (string) --The phone number of the contact.\nConstraints: Phone number must be specified in the format '+[country dialing code].[number including any area code>]'. For example, a US phone number might appear as '+1.1234567890' .\n\nEmail (string) --Email address of the contact.\n\nFax (string) --Fax number of the contact.\nConstraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .\n\nExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.\n\n(dict) --ExtraParam includes the following elements.\n\nName (string) -- [REQUIRED]The name of an additional parameter that is required by a top-level domain. Here are the top-level domains that require additional parameters and the names of the parameters that they require:\n\n.com.au and .net.au\n\nAU_ID_NUMBER\nAU_ID_TYPE  Valid values include the following:\nABN (Australian business number)\nACN (Australian company number)\nTM (Trademark number)\n\n.ca\n\nBRAND_NUMBER\nCA_BUSINESS_ENTITY_TYPE  Valid values include the following:\nBANK (Bank)\nCOMMERCIAL_COMPANY (Commercial company)\nCOMPANY (Company)\nCOOPERATION (Cooperation)\nCOOPERATIVE (Cooperative)\nCOOPRIX (Cooprix)\nCORP (Corporation)\nCREDIT_UNION (Credit union)\nFOMIA (Federation of mutual insurance associations)\nINC (Incorporated)\nLTD (Limited)\nLTEE (Limit\xc3\xa9e)\nLLC (Limited liability corporation)\nLLP (Limited liability partnership)\nLTE (Lte.)\nMBA (Mutual benefit association)\nMIC (Mutual insurance company)\nNFP (Not-for-profit corporation)\nSA (S.A.)\nSAVINGS_COMPANY (Savings company)\nSAVINGS_UNION (Savings union)\nSARL (Soci\xc3\xa9t\xc3\xa9 \xc3\xa0 responsabilit\xc3\xa9 limit\xc3\xa9e)\nTRUST (Trust)\nULC (Unlimited liability corporation)\n\n\nCA_LEGAL_TYPE  When ContactType is PERSON , valid values include the following:\nABO (Aboriginal Peoples indigenous to Canada)\nCCT (Canadian citizen)\nLGR (Legal Representative of a Canadian Citizen or Permanent Resident)\nRES (Permanent resident of Canada)\n\n\n\nWhen ContactType is a value other than PERSON , valid values include the following:\n\n\nASS (Canadian unincorporated association)\nCCO (Canadian corporation)\nEDU (Canadian educational institution)\nGOV (Government or government entity in Canada)\nHOP (Canadian Hospital)\nINB (Indian Band recognized by the Indian Act of Canada)\nLAM (Canadian Library, Archive, or Museum)\nMAJ (Her/His Majesty the Queen/King)\nOMK (Official mark registered in Canada)\nPLT (Canadian Political Party)\nPRT (Partnership Registered in Canada)\nTDM (Trademark registered in Canada)\nTRD (Canadian Trade Union)\nTRS (Trust established in Canada)\n\n.es\n\n\nES_IDENTIFICATION  Specify the applicable value:\nFor contacts inside Spain: Enter your passport ID.\nFor contacts outside of Spain: Enter the VAT identification number for the company.\n\n\nNote\nFor .es domains, the value of ContactType must be PERSON .\n\n\nES_IDENTIFICATION_TYPE  Valid values include the following:\nDNI_AND_NIF (For Spanish contacts)\nNIE (For foreigners with legal residence)\nOTHER (For contacts outside of Spain)\n\n\nES_LEGAL_FORM  Valid values include the following:\nASSOCIATION\nCENTRAL_GOVERNMENT_BODY\nCIVIL_SOCIETY\nCOMMUNITY_OF_OWNERS\nCOMMUNITY_PROPERTY\nCONSULATE\nCOOPERATIVE\nDESIGNATION_OF_ORIGIN_SUPERVISORY_COUNCIL\nECONOMIC_INTEREST_GROUP\nEMBASSY\nENTITY_MANAGING_NATURAL_AREAS\nFARM_PARTNERSHIP\nFOUNDATION\nGENERAL_AND_LIMITED_PARTNERSHIP\nGENERAL_PARTNERSHIP\nINDIVIDUAL\nLIMITED_COMPANY\nLOCAL_AUTHORITY\nLOCAL_PUBLIC_ENTITY\nMUTUAL_INSURANCE_COMPANY\nNATIONAL_PUBLIC_ENTITY\nORDER_OR_RELIGIOUS_INSTITUTION\nOTHERS (Only for contacts outside of Spain)\nPOLITICAL_PARTY\nPROFESSIONAL_ASSOCIATION\nPUBLIC_LAW_ASSOCIATION\nPUBLIC_LIMITED_COMPANY\nREGIONAL_GOVERNMENT_BODY\nREGIONAL_PUBLIC_ENTITY\nSAVINGS_BANK\nSPANISH_OFFICE\nSPORTS_ASSOCIATION\nSPORTS_FEDERATION\nSPORTS_LIMITED_COMPANY\nTEMPORARY_ALLIANCE_OF_ENTERPRISES\nTRADE_UNION\nWORKER_OWNED_COMPANY\nWORKER_OWNED_LIMITED_COMPANY\n\n.fi\n\nBIRTH_DATE_IN_YYYY_MM_DD\nFI_BUSINESS_NUMBER\nFI_ID_NUMBER\nFI_NATIONALITY  Valid values include the following:\nFINNISH\nNOT_FINNISH\n\n\nFI_ORGANIZATION_TYPE  Valid values include the following:\nCOMPANY\nCORPORATION\nGOVERNMENT\nINSTITUTION\nPOLITICAL_PARTY\nPUBLIC_COMMUNITY\nTOWNSHIP\n\n.fr\n\nBIRTH_CITY\nBIRTH_COUNTRY\nBIRTH_DATE_IN_YYYY_MM_DD\nBIRTH_DEPARTMENT : Specify the INSEE code that corresponds with the department where the contact was born. If the contact was born somewhere other than France or its overseas departments, specify 99 . For more information, including a list of departments and the corresponding INSEE numbers, see the Wikipedia entry Departments of France .\nBRAND_NUMBER.it\n\nIT_NATIONALITY\nIT_PIN\nIT_REGISTRANT_ENTITY_TYPE  Valid values include the following:\nFOREIGNERS\nFREELANCE_WORKERS (Freelance workers and professionals)\nITALIAN_COMPANIES (Italian companies and one-person companies)\nNON_PROFIT_ORGANIZATIONS\nOTHER_SUBJECTS\nPUBLIC_ORGANIZATIONS\n\n.ru\n\nBIRTH_DATE_IN_YYYY_MM_DD\nRU_PASSPORT_DATA.se\n\nBIRTH_COUNTRY\nSE_ID_NUMBER.sg\n\nSG_ID_NUMBER.co.uk, .me.uk, and .org.uk\n\nUK_CONTACT_TYPE  Valid values include the following:\nCRC (UK Corporation by Royal Charter)\nFCORP (Non-UK Corporation)\nFIND (Non-UK Individual, representing self)\nFOTHER (Non-UK Entity that does not fit into any other category)\nGOV (UK Government Body)\nIND (UK Individual (representing self))\nIP (UK Industrial/Provident Registered Company)\nLLP (UK Limited Liability Partnership)\nLTD (UK Limited Company)\nOTHER (UK Entity that does not fit into any other category)\nPLC (UK Public Limited Company)\nPTNR (UK Partnership)\nRCHAR (UK Registered Charity)\nSCH (UK School)\nSTAT (UK Statutory Body)\nSTRA (UK Sole Trader)\n\n\nUK_COMPANY_NUMBER\n\nIn addition, many TLDs require a VAT_NUMBER .\n\nValue (string) -- [REQUIRED]The value that corresponds with the name of an extra parameter.\n\n\n\n\n\n\n

    :type RegistrantContact: dict
    :param RegistrantContact: [REQUIRED]\nProvides detailed contact information.\n\nFirstName (string) --First name of contact.\n\nLastName (string) --Last name of contact.\n\nContactType (string) --Indicates whether the contact is a person, company, association, or public organization. Note the following:\n\nIf you specify a value other than PERSON , you must also specify a value for OrganizationName .\nFor some TLDs, the privacy protection available depends on the value that you specify for Contact Type . For the privacy protection settings for your TLD, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide\nFor .es domains, if you specify PERSON , you must specify INDIVIDUAL for the value of ES_LEGAL_FORM .\n\n\nOrganizationName (string) --Name of the organization for contact types other than PERSON .\n\nAddressLine1 (string) --First line of the contact\'s address.\n\nAddressLine2 (string) --Second line of contact\'s address, if any.\n\nCity (string) --The city of the contact\'s address.\n\nState (string) --The state or province of the contact\'s city.\n\nCountryCode (string) --Code for the country of the contact\'s address.\n\nZipCode (string) --The zip or postal code of the contact\'s address.\n\nPhoneNumber (string) --The phone number of the contact.\nConstraints: Phone number must be specified in the format '+[country dialing code].[number including any area code>]'. For example, a US phone number might appear as '+1.1234567890' .\n\nEmail (string) --Email address of the contact.\n\nFax (string) --Fax number of the contact.\nConstraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .\n\nExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.\n\n(dict) --ExtraParam includes the following elements.\n\nName (string) -- [REQUIRED]The name of an additional parameter that is required by a top-level domain. Here are the top-level domains that require additional parameters and the names of the parameters that they require:\n\n.com.au and .net.au\n\nAU_ID_NUMBER\nAU_ID_TYPE  Valid values include the following:\nABN (Australian business number)\nACN (Australian company number)\nTM (Trademark number)\n\n.ca\n\nBRAND_NUMBER\nCA_BUSINESS_ENTITY_TYPE  Valid values include the following:\nBANK (Bank)\nCOMMERCIAL_COMPANY (Commercial company)\nCOMPANY (Company)\nCOOPERATION (Cooperation)\nCOOPERATIVE (Cooperative)\nCOOPRIX (Cooprix)\nCORP (Corporation)\nCREDIT_UNION (Credit union)\nFOMIA (Federation of mutual insurance associations)\nINC (Incorporated)\nLTD (Limited)\nLTEE (Limit\xc3\xa9e)\nLLC (Limited liability corporation)\nLLP (Limited liability partnership)\nLTE (Lte.)\nMBA (Mutual benefit association)\nMIC (Mutual insurance company)\nNFP (Not-for-profit corporation)\nSA (S.A.)\nSAVINGS_COMPANY (Savings company)\nSAVINGS_UNION (Savings union)\nSARL (Soci\xc3\xa9t\xc3\xa9 \xc3\xa0 responsabilit\xc3\xa9 limit\xc3\xa9e)\nTRUST (Trust)\nULC (Unlimited liability corporation)\n\n\nCA_LEGAL_TYPE  When ContactType is PERSON , valid values include the following:\nABO (Aboriginal Peoples indigenous to Canada)\nCCT (Canadian citizen)\nLGR (Legal Representative of a Canadian Citizen or Permanent Resident)\nRES (Permanent resident of Canada)\n\n\n\nWhen ContactType is a value other than PERSON , valid values include the following:\n\n\nASS (Canadian unincorporated association)\nCCO (Canadian corporation)\nEDU (Canadian educational institution)\nGOV (Government or government entity in Canada)\nHOP (Canadian Hospital)\nINB (Indian Band recognized by the Indian Act of Canada)\nLAM (Canadian Library, Archive, or Museum)\nMAJ (Her/His Majesty the Queen/King)\nOMK (Official mark registered in Canada)\nPLT (Canadian Political Party)\nPRT (Partnership Registered in Canada)\nTDM (Trademark registered in Canada)\nTRD (Canadian Trade Union)\nTRS (Trust established in Canada)\n\n.es\n\n\nES_IDENTIFICATION  Specify the applicable value:\nFor contacts inside Spain: Enter your passport ID.\nFor contacts outside of Spain: Enter the VAT identification number for the company.\n\n\nNote\nFor .es domains, the value of ContactType must be PERSON .\n\n\nES_IDENTIFICATION_TYPE  Valid values include the following:\nDNI_AND_NIF (For Spanish contacts)\nNIE (For foreigners with legal residence)\nOTHER (For contacts outside of Spain)\n\n\nES_LEGAL_FORM  Valid values include the following:\nASSOCIATION\nCENTRAL_GOVERNMENT_BODY\nCIVIL_SOCIETY\nCOMMUNITY_OF_OWNERS\nCOMMUNITY_PROPERTY\nCONSULATE\nCOOPERATIVE\nDESIGNATION_OF_ORIGIN_SUPERVISORY_COUNCIL\nECONOMIC_INTEREST_GROUP\nEMBASSY\nENTITY_MANAGING_NATURAL_AREAS\nFARM_PARTNERSHIP\nFOUNDATION\nGENERAL_AND_LIMITED_PARTNERSHIP\nGENERAL_PARTNERSHIP\nINDIVIDUAL\nLIMITED_COMPANY\nLOCAL_AUTHORITY\nLOCAL_PUBLIC_ENTITY\nMUTUAL_INSURANCE_COMPANY\nNATIONAL_PUBLIC_ENTITY\nORDER_OR_RELIGIOUS_INSTITUTION\nOTHERS (Only for contacts outside of Spain)\nPOLITICAL_PARTY\nPROFESSIONAL_ASSOCIATION\nPUBLIC_LAW_ASSOCIATION\nPUBLIC_LIMITED_COMPANY\nREGIONAL_GOVERNMENT_BODY\nREGIONAL_PUBLIC_ENTITY\nSAVINGS_BANK\nSPANISH_OFFICE\nSPORTS_ASSOCIATION\nSPORTS_FEDERATION\nSPORTS_LIMITED_COMPANY\nTEMPORARY_ALLIANCE_OF_ENTERPRISES\nTRADE_UNION\nWORKER_OWNED_COMPANY\nWORKER_OWNED_LIMITED_COMPANY\n\n.fi\n\nBIRTH_DATE_IN_YYYY_MM_DD\nFI_BUSINESS_NUMBER\nFI_ID_NUMBER\nFI_NATIONALITY  Valid values include the following:\nFINNISH\nNOT_FINNISH\n\n\nFI_ORGANIZATION_TYPE  Valid values include the following:\nCOMPANY\nCORPORATION\nGOVERNMENT\nINSTITUTION\nPOLITICAL_PARTY\nPUBLIC_COMMUNITY\nTOWNSHIP\n\n.fr\n\nBIRTH_CITY\nBIRTH_COUNTRY\nBIRTH_DATE_IN_YYYY_MM_DD\nBIRTH_DEPARTMENT : Specify the INSEE code that corresponds with the department where the contact was born. If the contact was born somewhere other than France or its overseas departments, specify 99 . For more information, including a list of departments and the corresponding INSEE numbers, see the Wikipedia entry Departments of France .\nBRAND_NUMBER.it\n\nIT_NATIONALITY\nIT_PIN\nIT_REGISTRANT_ENTITY_TYPE  Valid values include the following:\nFOREIGNERS\nFREELANCE_WORKERS (Freelance workers and professionals)\nITALIAN_COMPANIES (Italian companies and one-person companies)\nNON_PROFIT_ORGANIZATIONS\nOTHER_SUBJECTS\nPUBLIC_ORGANIZATIONS\n\n.ru\n\nBIRTH_DATE_IN_YYYY_MM_DD\nRU_PASSPORT_DATA.se\n\nBIRTH_COUNTRY\nSE_ID_NUMBER.sg\n\nSG_ID_NUMBER.co.uk, .me.uk, and .org.uk\n\nUK_CONTACT_TYPE  Valid values include the following:\nCRC (UK Corporation by Royal Charter)\nFCORP (Non-UK Corporation)\nFIND (Non-UK Individual, representing self)\nFOTHER (Non-UK Entity that does not fit into any other category)\nGOV (UK Government Body)\nIND (UK Individual (representing self))\nIP (UK Industrial/Provident Registered Company)\nLLP (UK Limited Liability Partnership)\nLTD (UK Limited Company)\nOTHER (UK Entity that does not fit into any other category)\nPLC (UK Public Limited Company)\nPTNR (UK Partnership)\nRCHAR (UK Registered Charity)\nSCH (UK School)\nSTAT (UK Statutory Body)\nSTRA (UK Sole Trader)\n\n\nUK_COMPANY_NUMBER\n\nIn addition, many TLDs require a VAT_NUMBER .\n\nValue (string) -- [REQUIRED]The value that corresponds with the name of an extra parameter.\n\n\n\n\n\n\n

    :type TechContact: dict
    :param TechContact: [REQUIRED]\nProvides detailed contact information.\n\nFirstName (string) --First name of contact.\n\nLastName (string) --Last name of contact.\n\nContactType (string) --Indicates whether the contact is a person, company, association, or public organization. Note the following:\n\nIf you specify a value other than PERSON , you must also specify a value for OrganizationName .\nFor some TLDs, the privacy protection available depends on the value that you specify for Contact Type . For the privacy protection settings for your TLD, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide\nFor .es domains, if you specify PERSON , you must specify INDIVIDUAL for the value of ES_LEGAL_FORM .\n\n\nOrganizationName (string) --Name of the organization for contact types other than PERSON .\n\nAddressLine1 (string) --First line of the contact\'s address.\n\nAddressLine2 (string) --Second line of contact\'s address, if any.\n\nCity (string) --The city of the contact\'s address.\n\nState (string) --The state or province of the contact\'s city.\n\nCountryCode (string) --Code for the country of the contact\'s address.\n\nZipCode (string) --The zip or postal code of the contact\'s address.\n\nPhoneNumber (string) --The phone number of the contact.\nConstraints: Phone number must be specified in the format '+[country dialing code].[number including any area code>]'. For example, a US phone number might appear as '+1.1234567890' .\n\nEmail (string) --Email address of the contact.\n\nFax (string) --Fax number of the contact.\nConstraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .\n\nExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.\n\n(dict) --ExtraParam includes the following elements.\n\nName (string) -- [REQUIRED]The name of an additional parameter that is required by a top-level domain. Here are the top-level domains that require additional parameters and the names of the parameters that they require:\n\n.com.au and .net.au\n\nAU_ID_NUMBER\nAU_ID_TYPE  Valid values include the following:\nABN (Australian business number)\nACN (Australian company number)\nTM (Trademark number)\n\n.ca\n\nBRAND_NUMBER\nCA_BUSINESS_ENTITY_TYPE  Valid values include the following:\nBANK (Bank)\nCOMMERCIAL_COMPANY (Commercial company)\nCOMPANY (Company)\nCOOPERATION (Cooperation)\nCOOPERATIVE (Cooperative)\nCOOPRIX (Cooprix)\nCORP (Corporation)\nCREDIT_UNION (Credit union)\nFOMIA (Federation of mutual insurance associations)\nINC (Incorporated)\nLTD (Limited)\nLTEE (Limit\xc3\xa9e)\nLLC (Limited liability corporation)\nLLP (Limited liability partnership)\nLTE (Lte.)\nMBA (Mutual benefit association)\nMIC (Mutual insurance company)\nNFP (Not-for-profit corporation)\nSA (S.A.)\nSAVINGS_COMPANY (Savings company)\nSAVINGS_UNION (Savings union)\nSARL (Soci\xc3\xa9t\xc3\xa9 \xc3\xa0 responsabilit\xc3\xa9 limit\xc3\xa9e)\nTRUST (Trust)\nULC (Unlimited liability corporation)\n\n\nCA_LEGAL_TYPE  When ContactType is PERSON , valid values include the following:\nABO (Aboriginal Peoples indigenous to Canada)\nCCT (Canadian citizen)\nLGR (Legal Representative of a Canadian Citizen or Permanent Resident)\nRES (Permanent resident of Canada)\n\n\n\nWhen ContactType is a value other than PERSON , valid values include the following:\n\n\nASS (Canadian unincorporated association)\nCCO (Canadian corporation)\nEDU (Canadian educational institution)\nGOV (Government or government entity in Canada)\nHOP (Canadian Hospital)\nINB (Indian Band recognized by the Indian Act of Canada)\nLAM (Canadian Library, Archive, or Museum)\nMAJ (Her/His Majesty the Queen/King)\nOMK (Official mark registered in Canada)\nPLT (Canadian Political Party)\nPRT (Partnership Registered in Canada)\nTDM (Trademark registered in Canada)\nTRD (Canadian Trade Union)\nTRS (Trust established in Canada)\n\n.es\n\n\nES_IDENTIFICATION  Specify the applicable value:\nFor contacts inside Spain: Enter your passport ID.\nFor contacts outside of Spain: Enter the VAT identification number for the company.\n\n\nNote\nFor .es domains, the value of ContactType must be PERSON .\n\n\nES_IDENTIFICATION_TYPE  Valid values include the following:\nDNI_AND_NIF (For Spanish contacts)\nNIE (For foreigners with legal residence)\nOTHER (For contacts outside of Spain)\n\n\nES_LEGAL_FORM  Valid values include the following:\nASSOCIATION\nCENTRAL_GOVERNMENT_BODY\nCIVIL_SOCIETY\nCOMMUNITY_OF_OWNERS\nCOMMUNITY_PROPERTY\nCONSULATE\nCOOPERATIVE\nDESIGNATION_OF_ORIGIN_SUPERVISORY_COUNCIL\nECONOMIC_INTEREST_GROUP\nEMBASSY\nENTITY_MANAGING_NATURAL_AREAS\nFARM_PARTNERSHIP\nFOUNDATION\nGENERAL_AND_LIMITED_PARTNERSHIP\nGENERAL_PARTNERSHIP\nINDIVIDUAL\nLIMITED_COMPANY\nLOCAL_AUTHORITY\nLOCAL_PUBLIC_ENTITY\nMUTUAL_INSURANCE_COMPANY\nNATIONAL_PUBLIC_ENTITY\nORDER_OR_RELIGIOUS_INSTITUTION\nOTHERS (Only for contacts outside of Spain)\nPOLITICAL_PARTY\nPROFESSIONAL_ASSOCIATION\nPUBLIC_LAW_ASSOCIATION\nPUBLIC_LIMITED_COMPANY\nREGIONAL_GOVERNMENT_BODY\nREGIONAL_PUBLIC_ENTITY\nSAVINGS_BANK\nSPANISH_OFFICE\nSPORTS_ASSOCIATION\nSPORTS_FEDERATION\nSPORTS_LIMITED_COMPANY\nTEMPORARY_ALLIANCE_OF_ENTERPRISES\nTRADE_UNION\nWORKER_OWNED_COMPANY\nWORKER_OWNED_LIMITED_COMPANY\n\n.fi\n\nBIRTH_DATE_IN_YYYY_MM_DD\nFI_BUSINESS_NUMBER\nFI_ID_NUMBER\nFI_NATIONALITY  Valid values include the following:\nFINNISH\nNOT_FINNISH\n\n\nFI_ORGANIZATION_TYPE  Valid values include the following:\nCOMPANY\nCORPORATION\nGOVERNMENT\nINSTITUTION\nPOLITICAL_PARTY\nPUBLIC_COMMUNITY\nTOWNSHIP\n\n.fr\n\nBIRTH_CITY\nBIRTH_COUNTRY\nBIRTH_DATE_IN_YYYY_MM_DD\nBIRTH_DEPARTMENT : Specify the INSEE code that corresponds with the department where the contact was born. If the contact was born somewhere other than France or its overseas departments, specify 99 . For more information, including a list of departments and the corresponding INSEE numbers, see the Wikipedia entry Departments of France .\nBRAND_NUMBER.it\n\nIT_NATIONALITY\nIT_PIN\nIT_REGISTRANT_ENTITY_TYPE  Valid values include the following:\nFOREIGNERS\nFREELANCE_WORKERS (Freelance workers and professionals)\nITALIAN_COMPANIES (Italian companies and one-person companies)\nNON_PROFIT_ORGANIZATIONS\nOTHER_SUBJECTS\nPUBLIC_ORGANIZATIONS\n\n.ru\n\nBIRTH_DATE_IN_YYYY_MM_DD\nRU_PASSPORT_DATA.se\n\nBIRTH_COUNTRY\nSE_ID_NUMBER.sg\n\nSG_ID_NUMBER.co.uk, .me.uk, and .org.uk\n\nUK_CONTACT_TYPE  Valid values include the following:\nCRC (UK Corporation by Royal Charter)\nFCORP (Non-UK Corporation)\nFIND (Non-UK Individual, representing self)\nFOTHER (Non-UK Entity that does not fit into any other category)\nGOV (UK Government Body)\nIND (UK Individual (representing self))\nIP (UK Industrial/Provident Registered Company)\nLLP (UK Limited Liability Partnership)\nLTD (UK Limited Company)\nOTHER (UK Entity that does not fit into any other category)\nPLC (UK Public Limited Company)\nPTNR (UK Partnership)\nRCHAR (UK Registered Charity)\nSCH (UK School)\nSTAT (UK Statutory Body)\nSTRA (UK Sole Trader)\n\n\nUK_COMPANY_NUMBER\n\nIn addition, many TLDs require a VAT_NUMBER .\n\nValue (string) -- [REQUIRED]The value that corresponds with the name of an extra parameter.\n\n\n\n\n\n\n

    :type PrivacyProtectAdminContact: boolean
    :param PrivacyProtectAdminContact: Whether you want to conceal contact information from WHOIS queries. If you specify true , WHOIS ('who is') queries return contact information either for Amazon Registrar (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other TLDs). If you specify false , WHOIS queries return the information that you entered for the admin contact.\nDefault: true\n

    :type PrivacyProtectRegistrantContact: boolean
    :param PrivacyProtectRegistrantContact: Whether you want to conceal contact information from WHOIS queries. If you specify true , WHOIS ('who is') queries return contact information either for Amazon Registrar (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other TLDs). If you specify false , WHOIS queries return the information that you entered for the registrant contact (domain owner).\nDefault: true\n

    :type PrivacyProtectTechContact: boolean
    :param PrivacyProtectTechContact: Whether you want to conceal contact information from WHOIS queries. If you specify true , WHOIS ('who is') queries return contact information either for Amazon Registrar (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other TLDs). If you specify false , WHOIS queries return the information that you entered for the technical contact.\nDefault: true\n

    :rtype: dict

ReturnsResponse Syntax
{
    'OperationId': 'string'
}


Response Structure

(dict) --
The TransferDomain response includes the following element.

OperationId (string) --
Identifier for tracking the progress of the request. To query the operation status, use GetOperationDetail .







Exceptions

Route53Domains.Client.exceptions.InvalidInput
Route53Domains.Client.exceptions.UnsupportedTLD
Route53Domains.Client.exceptions.DuplicateRequest
Route53Domains.Client.exceptions.TLDRulesViolation
Route53Domains.Client.exceptions.DomainLimitExceeded
Route53Domains.Client.exceptions.OperationLimitExceeded


    :return: {
        'OperationId': 'string'
    }
    
    
    :returns: 
    DomainName (string) -- [REQUIRED]
    The name of the domain that you want to transfer to Route 53. The top-level domain (TLD), such as .com, must be a TLD that Route 53 supports. For a list of supported TLDs, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide .
    The domain name can contain only the following characters:
    
    Letters a through z. Domain names are not case sensitive.
    Numbers 0 through 9.
    Hyphen (-). You can\'t specify a hyphen at the beginning or end of a label.
    Period (.) to separate the labels in the name, such as the . in example.com .
    
    
    IdnLangCode (string) -- Reserved for future use.
    DurationInYears (integer) -- [REQUIRED]
    The number of years that you want to register the domain for. Domains are registered for a minimum of one year. The maximum period depends on the top-level domain.
    Default: 1
    
    Nameservers (list) -- Contains details for the host and glue IP addresses.
    
    (dict) --Nameserver includes the following elements.
    
    Name (string) -- [REQUIRED]The fully qualified host name of the name server.
    Constraint: Maximum 255 characters
    
    GlueIps (list) --Glue IP address of a name server entry. Glue IP addresses are required only when the name of the name server is a subdomain of the domain. For example, if your domain is example.com and the name server for the domain is ns.example.com, you need to specify the IP address for ns.example.com.
    Constraints: The list can contain only one IPv4 and one IPv6 address.
    
    (string) --
    
    
    
    
    
    
    AuthCode (string) -- The authorization code for the domain. You get this value from the current registrar.
    AutoRenew (boolean) -- Indicates whether the domain will be automatically renewed (true) or not (false). Autorenewal only takes effect after the account is charged.
    Default: true
    
    AdminContact (dict) -- [REQUIRED]
    Provides detailed contact information.
    
    FirstName (string) --First name of contact.
    
    LastName (string) --Last name of contact.
    
    ContactType (string) --Indicates whether the contact is a person, company, association, or public organization. Note the following:
    
    If you specify a value other than PERSON , you must also specify a value for OrganizationName .
    For some TLDs, the privacy protection available depends on the value that you specify for Contact Type . For the privacy protection settings for your TLD, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide
    For .es domains, if you specify PERSON , you must specify INDIVIDUAL for the value of ES_LEGAL_FORM .
    
    
    OrganizationName (string) --Name of the organization for contact types other than PERSON .
    
    AddressLine1 (string) --First line of the contact\'s address.
    
    AddressLine2 (string) --Second line of contact\'s address, if any.
    
    City (string) --The city of the contact\'s address.
    
    State (string) --The state or province of the contact\'s city.
    
    CountryCode (string) --Code for the country of the contact\'s address.
    
    ZipCode (string) --The zip or postal code of the contact\'s address.
    
    PhoneNumber (string) --The phone number of the contact.
    Constraints: Phone number must be specified in the format "+[country dialing code].[number including any area code>]". For example, a US phone number might appear as "+1.1234567890" .
    
    Email (string) --Email address of the contact.
    
    Fax (string) --Fax number of the contact.
    Constraints: Phone number must be specified in the format "+[country dialing code].[number including any area code]". For example, a US phone number might appear as "+1.1234567890" .
    
    ExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.
    
    (dict) --ExtraParam includes the following elements.
    
    Name (string) -- [REQUIRED]The name of an additional parameter that is required by a top-level domain. Here are the top-level domains that require additional parameters and the names of the parameters that they require:
    
    .com.au and .net.au
    
    AU_ID_NUMBER
    AU_ID_TYPE   Valid values include the following:
    ABN (Australian business number)
    ACN (Australian company number)
    TM (Trademark number)
    
    .ca
    
    BRAND_NUMBER
    CA_BUSINESS_ENTITY_TYPE   Valid values include the following:
    BANK (Bank)
    COMMERCIAL_COMPANY (Commercial company)
    COMPANY (Company)
    COOPERATION (Cooperation)
    COOPERATIVE (Cooperative)
    COOPRIX (Cooprix)
    CORP (Corporation)
    CREDIT_UNION (Credit union)
    FOMIA (Federation of mutual insurance associations)
    INC (Incorporated)
    LTD (Limited)
    LTEE (Limit\xc3\xa9e)
    LLC (Limited liability corporation)
    LLP (Limited liability partnership)
    LTE (Lte.)
    MBA (Mutual benefit association)
    MIC (Mutual insurance company)
    NFP (Not-for-profit corporation)
    SA (S.A.)
    SAVINGS_COMPANY (Savings company)
    SAVINGS_UNION (Savings union)
    SARL (Soci\xc3\xa9t\xc3\xa9 \xc3\xa0 responsabilit\xc3\xa9 limit\xc3\xa9e)
    TRUST (Trust)
    ULC (Unlimited liability corporation)
    
    
    CA_LEGAL_TYPE   When ContactType is PERSON , valid values include the following:
    ABO (Aboriginal Peoples indigenous to Canada)
    CCT (Canadian citizen)
    LGR (Legal Representative of a Canadian Citizen or Permanent Resident)
    RES (Permanent resident of Canada)
    
    
    
    When ContactType is a value other than PERSON , valid values include the following:
    
    
    ASS (Canadian unincorporated association)
    CCO (Canadian corporation)
    EDU (Canadian educational institution)
    GOV (Government or government entity in Canada)
    HOP (Canadian Hospital)
    INB (Indian Band recognized by the Indian Act of Canada)
    LAM (Canadian Library, Archive, or Museum)
    MAJ (Her/His Majesty the Queen/King)
    OMK (Official mark registered in Canada)
    PLT (Canadian Political Party)
    PRT (Partnership Registered in Canada)
    TDM (Trademark registered in Canada)
    TRD (Canadian Trade Union)
    TRS (Trust established in Canada)
    
    .es
    
    
    ES_IDENTIFICATION   Specify the applicable value:
    For contacts inside Spain: Enter your passport ID.
    For contacts outside of Spain: Enter the VAT identification number for the company.
    
    
    Note
    For .es domains, the value of ContactType must be PERSON .
    
    
    ES_IDENTIFICATION_TYPE   Valid values include the following:
    DNI_AND_NIF (For Spanish contacts)
    NIE (For foreigners with legal residence)
    OTHER (For contacts outside of Spain)
    
    
    ES_LEGAL_FORM   Valid values include the following:
    ASSOCIATION
    CENTRAL_GOVERNMENT_BODY
    CIVIL_SOCIETY
    COMMUNITY_OF_OWNERS
    COMMUNITY_PROPERTY
    CONSULATE
    COOPERATIVE
    DESIGNATION_OF_ORIGIN_SUPERVISORY_COUNCIL
    ECONOMIC_INTEREST_GROUP
    EMBASSY
    ENTITY_MANAGING_NATURAL_AREAS
    FARM_PARTNERSHIP
    FOUNDATION
    GENERAL_AND_LIMITED_PARTNERSHIP
    GENERAL_PARTNERSHIP
    INDIVIDUAL
    LIMITED_COMPANY
    LOCAL_AUTHORITY
    LOCAL_PUBLIC_ENTITY
    MUTUAL_INSURANCE_COMPANY
    NATIONAL_PUBLIC_ENTITY
    ORDER_OR_RELIGIOUS_INSTITUTION
    OTHERS (Only for contacts outside of Spain)
    POLITICAL_PARTY
    PROFESSIONAL_ASSOCIATION
    PUBLIC_LAW_ASSOCIATION
    PUBLIC_LIMITED_COMPANY
    REGIONAL_GOVERNMENT_BODY
    REGIONAL_PUBLIC_ENTITY
    SAVINGS_BANK
    SPANISH_OFFICE
    SPORTS_ASSOCIATION
    SPORTS_FEDERATION
    SPORTS_LIMITED_COMPANY
    TEMPORARY_ALLIANCE_OF_ENTERPRISES
    TRADE_UNION
    WORKER_OWNED_COMPANY
    WORKER_OWNED_LIMITED_COMPANY
    
    .fi
    
    BIRTH_DATE_IN_YYYY_MM_DD
    FI_BUSINESS_NUMBER
    FI_ID_NUMBER
    FI_NATIONALITY   Valid values include the following:
    FINNISH
    NOT_FINNISH
    
    
    FI_ORGANIZATION_TYPE   Valid values include the following:
    COMPANY
    CORPORATION
    GOVERNMENT
    INSTITUTION
    POLITICAL_PARTY
    PUBLIC_COMMUNITY
    TOWNSHIP
    
    .fr
    
    BIRTH_CITY
    BIRTH_COUNTRY
    BIRTH_DATE_IN_YYYY_MM_DD
    BIRTH_DEPARTMENT : Specify the INSEE code that corresponds with the department where the contact was born. If the contact was born somewhere other than France or its overseas departments, specify 99 . For more information, including a list of departments and the corresponding INSEE numbers, see the Wikipedia entry Departments of France .
    BRAND_NUMBER.it
    
    IT_NATIONALITY
    IT_PIN
    IT_REGISTRANT_ENTITY_TYPE   Valid values include the following:
    FOREIGNERS
    FREELANCE_WORKERS (Freelance workers and professionals)
    ITALIAN_COMPANIES (Italian companies and one-person companies)
    NON_PROFIT_ORGANIZATIONS
    OTHER_SUBJECTS
    PUBLIC_ORGANIZATIONS
    
    .ru
    
    BIRTH_DATE_IN_YYYY_MM_DD
    RU_PASSPORT_DATA.se
    
    BIRTH_COUNTRY
    SE_ID_NUMBER.sg
    
    SG_ID_NUMBER.co.uk, .me.uk, and .org.uk
    
    UK_CONTACT_TYPE   Valid values include the following:
    CRC (UK Corporation by Royal Charter)
    FCORP (Non-UK Corporation)
    FIND (Non-UK Individual, representing self)
    FOTHER (Non-UK Entity that does not fit into any other category)
    GOV (UK Government Body)
    IND (UK Individual (representing self))
    IP (UK Industrial/Provident Registered Company)
    LLP (UK Limited Liability Partnership)
    LTD (UK Limited Company)
    OTHER (UK Entity that does not fit into any other category)
    PLC (UK Public Limited Company)
    PTNR (UK Partnership)
    RCHAR (UK Registered Charity)
    SCH (UK School)
    STAT (UK Statutory Body)
    STRA (UK Sole Trader)
    
    
    UK_COMPANY_NUMBER
    
    In addition, many TLDs require a VAT_NUMBER .
    
    Value (string) -- [REQUIRED]The value that corresponds with the name of an extra parameter.
    
    
    
    
    
    
    
    RegistrantContact (dict) -- [REQUIRED]
    Provides detailed contact information.
    
    FirstName (string) --First name of contact.
    
    LastName (string) --Last name of contact.
    
    ContactType (string) --Indicates whether the contact is a person, company, association, or public organization. Note the following:
    
    If you specify a value other than PERSON , you must also specify a value for OrganizationName .
    For some TLDs, the privacy protection available depends on the value that you specify for Contact Type . For the privacy protection settings for your TLD, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide
    For .es domains, if you specify PERSON , you must specify INDIVIDUAL for the value of ES_LEGAL_FORM .
    
    
    OrganizationName (string) --Name of the organization for contact types other than PERSON .
    
    AddressLine1 (string) --First line of the contact\'s address.
    
    AddressLine2 (string) --Second line of contact\'s address, if any.
    
    City (string) --The city of the contact\'s address.
    
    State (string) --The state or province of the contact\'s city.
    
    CountryCode (string) --Code for the country of the contact\'s address.
    
    ZipCode (string) --The zip or postal code of the contact\'s address.
    
    PhoneNumber (string) --The phone number of the contact.
    Constraints: Phone number must be specified in the format "+[country dialing code].[number including any area code>]". For example, a US phone number might appear as "+1.1234567890" .
    
    Email (string) --Email address of the contact.
    
    Fax (string) --Fax number of the contact.
    Constraints: Phone number must be specified in the format "+[country dialing code].[number including any area code]". For example, a US phone number might appear as "+1.1234567890" .
    
    ExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.
    
    (dict) --ExtraParam includes the following elements.
    
    Name (string) -- [REQUIRED]The name of an additional parameter that is required by a top-level domain. Here are the top-level domains that require additional parameters and the names of the parameters that they require:
    
    .com.au and .net.au
    
    AU_ID_NUMBER
    AU_ID_TYPE   Valid values include the following:
    ABN (Australian business number)
    ACN (Australian company number)
    TM (Trademark number)
    
    .ca
    
    BRAND_NUMBER
    CA_BUSINESS_ENTITY_TYPE   Valid values include the following:
    BANK (Bank)
    COMMERCIAL_COMPANY (Commercial company)
    COMPANY (Company)
    COOPERATION (Cooperation)
    COOPERATIVE (Cooperative)
    COOPRIX (Cooprix)
    CORP (Corporation)
    CREDIT_UNION (Credit union)
    FOMIA (Federation of mutual insurance associations)
    INC (Incorporated)
    LTD (Limited)
    LTEE (Limit\xc3\xa9e)
    LLC (Limited liability corporation)
    LLP (Limited liability partnership)
    LTE (Lte.)
    MBA (Mutual benefit association)
    MIC (Mutual insurance company)
    NFP (Not-for-profit corporation)
    SA (S.A.)
    SAVINGS_COMPANY (Savings company)
    SAVINGS_UNION (Savings union)
    SARL (Soci\xc3\xa9t\xc3\xa9 \xc3\xa0 responsabilit\xc3\xa9 limit\xc3\xa9e)
    TRUST (Trust)
    ULC (Unlimited liability corporation)
    
    
    CA_LEGAL_TYPE   When ContactType is PERSON , valid values include the following:
    ABO (Aboriginal Peoples indigenous to Canada)
    CCT (Canadian citizen)
    LGR (Legal Representative of a Canadian Citizen or Permanent Resident)
    RES (Permanent resident of Canada)
    
    
    
    When ContactType is a value other than PERSON , valid values include the following:
    
    
    ASS (Canadian unincorporated association)
    CCO (Canadian corporation)
    EDU (Canadian educational institution)
    GOV (Government or government entity in Canada)
    HOP (Canadian Hospital)
    INB (Indian Band recognized by the Indian Act of Canada)
    LAM (Canadian Library, Archive, or Museum)
    MAJ (Her/His Majesty the Queen/King)
    OMK (Official mark registered in Canada)
    PLT (Canadian Political Party)
    PRT (Partnership Registered in Canada)
    TDM (Trademark registered in Canada)
    TRD (Canadian Trade Union)
    TRS (Trust established in Canada)
    
    .es
    
    
    ES_IDENTIFICATION   Specify the applicable value:
    For contacts inside Spain: Enter your passport ID.
    For contacts outside of Spain: Enter the VAT identification number for the company.
    
    
    Note
    For .es domains, the value of ContactType must be PERSON .
    
    
    ES_IDENTIFICATION_TYPE   Valid values include the following:
    DNI_AND_NIF (For Spanish contacts)
    NIE (For foreigners with legal residence)
    OTHER (For contacts outside of Spain)
    
    
    ES_LEGAL_FORM   Valid values include the following:
    ASSOCIATION
    CENTRAL_GOVERNMENT_BODY
    CIVIL_SOCIETY
    COMMUNITY_OF_OWNERS
    COMMUNITY_PROPERTY
    CONSULATE
    COOPERATIVE
    DESIGNATION_OF_ORIGIN_SUPERVISORY_COUNCIL
    ECONOMIC_INTEREST_GROUP
    EMBASSY
    ENTITY_MANAGING_NATURAL_AREAS
    FARM_PARTNERSHIP
    FOUNDATION
    GENERAL_AND_LIMITED_PARTNERSHIP
    GENERAL_PARTNERSHIP
    INDIVIDUAL
    LIMITED_COMPANY
    LOCAL_AUTHORITY
    LOCAL_PUBLIC_ENTITY
    MUTUAL_INSURANCE_COMPANY
    NATIONAL_PUBLIC_ENTITY
    ORDER_OR_RELIGIOUS_INSTITUTION
    OTHERS (Only for contacts outside of Spain)
    POLITICAL_PARTY
    PROFESSIONAL_ASSOCIATION
    PUBLIC_LAW_ASSOCIATION
    PUBLIC_LIMITED_COMPANY
    REGIONAL_GOVERNMENT_BODY
    REGIONAL_PUBLIC_ENTITY
    SAVINGS_BANK
    SPANISH_OFFICE
    SPORTS_ASSOCIATION
    SPORTS_FEDERATION
    SPORTS_LIMITED_COMPANY
    TEMPORARY_ALLIANCE_OF_ENTERPRISES
    TRADE_UNION
    WORKER_OWNED_COMPANY
    WORKER_OWNED_LIMITED_COMPANY
    
    .fi
    
    BIRTH_DATE_IN_YYYY_MM_DD
    FI_BUSINESS_NUMBER
    FI_ID_NUMBER
    FI_NATIONALITY   Valid values include the following:
    FINNISH
    NOT_FINNISH
    
    
    FI_ORGANIZATION_TYPE   Valid values include the following:
    COMPANY
    CORPORATION
    GOVERNMENT
    INSTITUTION
    POLITICAL_PARTY
    PUBLIC_COMMUNITY
    TOWNSHIP
    
    .fr
    
    BIRTH_CITY
    BIRTH_COUNTRY
    BIRTH_DATE_IN_YYYY_MM_DD
    BIRTH_DEPARTMENT : Specify the INSEE code that corresponds with the department where the contact was born. If the contact was born somewhere other than France or its overseas departments, specify 99 . For more information, including a list of departments and the corresponding INSEE numbers, see the Wikipedia entry Departments of France .
    BRAND_NUMBER.it
    
    IT_NATIONALITY
    IT_PIN
    IT_REGISTRANT_ENTITY_TYPE   Valid values include the following:
    FOREIGNERS
    FREELANCE_WORKERS (Freelance workers and professionals)
    ITALIAN_COMPANIES (Italian companies and one-person companies)
    NON_PROFIT_ORGANIZATIONS
    OTHER_SUBJECTS
    PUBLIC_ORGANIZATIONS
    
    .ru
    
    BIRTH_DATE_IN_YYYY_MM_DD
    RU_PASSPORT_DATA.se
    
    BIRTH_COUNTRY
    SE_ID_NUMBER.sg
    
    SG_ID_NUMBER.co.uk, .me.uk, and .org.uk
    
    UK_CONTACT_TYPE   Valid values include the following:
    CRC (UK Corporation by Royal Charter)
    FCORP (Non-UK Corporation)
    FIND (Non-UK Individual, representing self)
    FOTHER (Non-UK Entity that does not fit into any other category)
    GOV (UK Government Body)
    IND (UK Individual (representing self))
    IP (UK Industrial/Provident Registered Company)
    LLP (UK Limited Liability Partnership)
    LTD (UK Limited Company)
    OTHER (UK Entity that does not fit into any other category)
    PLC (UK Public Limited Company)
    PTNR (UK Partnership)
    RCHAR (UK Registered Charity)
    SCH (UK School)
    STAT (UK Statutory Body)
    STRA (UK Sole Trader)
    
    
    UK_COMPANY_NUMBER
    
    In addition, many TLDs require a VAT_NUMBER .
    
    Value (string) -- [REQUIRED]The value that corresponds with the name of an extra parameter.
    
    
    
    
    
    
    
    TechContact (dict) -- [REQUIRED]
    Provides detailed contact information.
    
    FirstName (string) --First name of contact.
    
    LastName (string) --Last name of contact.
    
    ContactType (string) --Indicates whether the contact is a person, company, association, or public organization. Note the following:
    
    If you specify a value other than PERSON , you must also specify a value for OrganizationName .
    For some TLDs, the privacy protection available depends on the value that you specify for Contact Type . For the privacy protection settings for your TLD, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide
    For .es domains, if you specify PERSON , you must specify INDIVIDUAL for the value of ES_LEGAL_FORM .
    
    
    OrganizationName (string) --Name of the organization for contact types other than PERSON .
    
    AddressLine1 (string) --First line of the contact\'s address.
    
    AddressLine2 (string) --Second line of contact\'s address, if any.
    
    City (string) --The city of the contact\'s address.
    
    State (string) --The state or province of the contact\'s city.
    
    CountryCode (string) --Code for the country of the contact\'s address.
    
    ZipCode (string) --The zip or postal code of the contact\'s address.
    
    PhoneNumber (string) --The phone number of the contact.
    Constraints: Phone number must be specified in the format "+[country dialing code].[number including any area code>]". For example, a US phone number might appear as "+1.1234567890" .
    
    Email (string) --Email address of the contact.
    
    Fax (string) --Fax number of the contact.
    Constraints: Phone number must be specified in the format "+[country dialing code].[number including any area code]". For example, a US phone number might appear as "+1.1234567890" .
    
    ExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.
    
    (dict) --ExtraParam includes the following elements.
    
    Name (string) -- [REQUIRED]The name of an additional parameter that is required by a top-level domain. Here are the top-level domains that require additional parameters and the names of the parameters that they require:
    
    .com.au and .net.au
    
    AU_ID_NUMBER
    AU_ID_TYPE   Valid values include the following:
    ABN (Australian business number)
    ACN (Australian company number)
    TM (Trademark number)
    
    .ca
    
    BRAND_NUMBER
    CA_BUSINESS_ENTITY_TYPE   Valid values include the following:
    BANK (Bank)
    COMMERCIAL_COMPANY (Commercial company)
    COMPANY (Company)
    COOPERATION (Cooperation)
    COOPERATIVE (Cooperative)
    COOPRIX (Cooprix)
    CORP (Corporation)
    CREDIT_UNION (Credit union)
    FOMIA (Federation of mutual insurance associations)
    INC (Incorporated)
    LTD (Limited)
    LTEE (Limit\xc3\xa9e)
    LLC (Limited liability corporation)
    LLP (Limited liability partnership)
    LTE (Lte.)
    MBA (Mutual benefit association)
    MIC (Mutual insurance company)
    NFP (Not-for-profit corporation)
    SA (S.A.)
    SAVINGS_COMPANY (Savings company)
    SAVINGS_UNION (Savings union)
    SARL (Soci\xc3\xa9t\xc3\xa9 \xc3\xa0 responsabilit\xc3\xa9 limit\xc3\xa9e)
    TRUST (Trust)
    ULC (Unlimited liability corporation)
    
    
    CA_LEGAL_TYPE   When ContactType is PERSON , valid values include the following:
    ABO (Aboriginal Peoples indigenous to Canada)
    CCT (Canadian citizen)
    LGR (Legal Representative of a Canadian Citizen or Permanent Resident)
    RES (Permanent resident of Canada)
    
    
    
    When ContactType is a value other than PERSON , valid values include the following:
    
    
    ASS (Canadian unincorporated association)
    CCO (Canadian corporation)
    EDU (Canadian educational institution)
    GOV (Government or government entity in Canada)
    HOP (Canadian Hospital)
    INB (Indian Band recognized by the Indian Act of Canada)
    LAM (Canadian Library, Archive, or Museum)
    MAJ (Her/His Majesty the Queen/King)
    OMK (Official mark registered in Canada)
    PLT (Canadian Political Party)
    PRT (Partnership Registered in Canada)
    TDM (Trademark registered in Canada)
    TRD (Canadian Trade Union)
    TRS (Trust established in Canada)
    
    .es
    
    
    ES_IDENTIFICATION   Specify the applicable value:
    For contacts inside Spain: Enter your passport ID.
    For contacts outside of Spain: Enter the VAT identification number for the company.
    
    
    Note
    For .es domains, the value of ContactType must be PERSON .
    
    
    ES_IDENTIFICATION_TYPE   Valid values include the following:
    DNI_AND_NIF (For Spanish contacts)
    NIE (For foreigners with legal residence)
    OTHER (For contacts outside of Spain)
    
    
    ES_LEGAL_FORM   Valid values include the following:
    ASSOCIATION
    CENTRAL_GOVERNMENT_BODY
    CIVIL_SOCIETY
    COMMUNITY_OF_OWNERS
    COMMUNITY_PROPERTY
    CONSULATE
    COOPERATIVE
    DESIGNATION_OF_ORIGIN_SUPERVISORY_COUNCIL
    ECONOMIC_INTEREST_GROUP
    EMBASSY
    ENTITY_MANAGING_NATURAL_AREAS
    FARM_PARTNERSHIP
    FOUNDATION
    GENERAL_AND_LIMITED_PARTNERSHIP
    GENERAL_PARTNERSHIP
    INDIVIDUAL
    LIMITED_COMPANY
    LOCAL_AUTHORITY
    LOCAL_PUBLIC_ENTITY
    MUTUAL_INSURANCE_COMPANY
    NATIONAL_PUBLIC_ENTITY
    ORDER_OR_RELIGIOUS_INSTITUTION
    OTHERS (Only for contacts outside of Spain)
    POLITICAL_PARTY
    PROFESSIONAL_ASSOCIATION
    PUBLIC_LAW_ASSOCIATION
    PUBLIC_LIMITED_COMPANY
    REGIONAL_GOVERNMENT_BODY
    REGIONAL_PUBLIC_ENTITY
    SAVINGS_BANK
    SPANISH_OFFICE
    SPORTS_ASSOCIATION
    SPORTS_FEDERATION
    SPORTS_LIMITED_COMPANY
    TEMPORARY_ALLIANCE_OF_ENTERPRISES
    TRADE_UNION
    WORKER_OWNED_COMPANY
    WORKER_OWNED_LIMITED_COMPANY
    
    .fi
    
    BIRTH_DATE_IN_YYYY_MM_DD
    FI_BUSINESS_NUMBER
    FI_ID_NUMBER
    FI_NATIONALITY   Valid values include the following:
    FINNISH
    NOT_FINNISH
    
    
    FI_ORGANIZATION_TYPE   Valid values include the following:
    COMPANY
    CORPORATION
    GOVERNMENT
    INSTITUTION
    POLITICAL_PARTY
    PUBLIC_COMMUNITY
    TOWNSHIP
    
    .fr
    
    BIRTH_CITY
    BIRTH_COUNTRY
    BIRTH_DATE_IN_YYYY_MM_DD
    BIRTH_DEPARTMENT : Specify the INSEE code that corresponds with the department where the contact was born. If the contact was born somewhere other than France or its overseas departments, specify 99 . For more information, including a list of departments and the corresponding INSEE numbers, see the Wikipedia entry Departments of France .
    BRAND_NUMBER.it
    
    IT_NATIONALITY
    IT_PIN
    IT_REGISTRANT_ENTITY_TYPE   Valid values include the following:
    FOREIGNERS
    FREELANCE_WORKERS (Freelance workers and professionals)
    ITALIAN_COMPANIES (Italian companies and one-person companies)
    NON_PROFIT_ORGANIZATIONS
    OTHER_SUBJECTS
    PUBLIC_ORGANIZATIONS
    
    .ru
    
    BIRTH_DATE_IN_YYYY_MM_DD
    RU_PASSPORT_DATA.se
    
    BIRTH_COUNTRY
    SE_ID_NUMBER.sg
    
    SG_ID_NUMBER.co.uk, .me.uk, and .org.uk
    
    UK_CONTACT_TYPE   Valid values include the following:
    CRC (UK Corporation by Royal Charter)
    FCORP (Non-UK Corporation)
    FIND (Non-UK Individual, representing self)
    FOTHER (Non-UK Entity that does not fit into any other category)
    GOV (UK Government Body)
    IND (UK Individual (representing self))
    IP (UK Industrial/Provident Registered Company)
    LLP (UK Limited Liability Partnership)
    LTD (UK Limited Company)
    OTHER (UK Entity that does not fit into any other category)
    PLC (UK Public Limited Company)
    PTNR (UK Partnership)
    RCHAR (UK Registered Charity)
    SCH (UK School)
    STAT (UK Statutory Body)
    STRA (UK Sole Trader)
    
    
    UK_COMPANY_NUMBER
    
    In addition, many TLDs require a VAT_NUMBER .
    
    Value (string) -- [REQUIRED]The value that corresponds with the name of an extra parameter.
    
    
    
    
    
    
    
    PrivacyProtectAdminContact (boolean) -- Whether you want to conceal contact information from WHOIS queries. If you specify true , WHOIS ("who is") queries return contact information either for Amazon Registrar (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other TLDs). If you specify false , WHOIS queries return the information that you entered for the admin contact.
    Default: true
    
    PrivacyProtectRegistrantContact (boolean) -- Whether you want to conceal contact information from WHOIS queries. If you specify true , WHOIS ("who is") queries return contact information either for Amazon Registrar (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other TLDs). If you specify false , WHOIS queries return the information that you entered for the registrant contact (domain owner).
    Default: true
    
    PrivacyProtectTechContact (boolean) -- Whether you want to conceal contact information from WHOIS queries. If you specify true , WHOIS ("who is") queries return contact information either for Amazon Registrar (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other TLDs). If you specify false , WHOIS queries return the information that you entered for the technical contact.
    Default: true
    
    
    """
    pass

def transfer_domain_to_another_aws_account(DomainName=None, AccountId=None):
    """
    Transfers a domain from the current AWS account to another AWS account. Note the following:
    Use either ListOperations or GetOperationDetail to determine whether the operation succeeded. GetOperationDetail provides additional information, for example, Domain Transfer from Aws Account 111122223333 has been cancelled .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.transfer_domain_to_another_aws_account(
        DomainName='string',
        AccountId='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe name of the domain that you want to transfer from the current AWS account to another account.\n

    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe account ID of the AWS account that you want to transfer the domain to, for example, 111122223333 .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'OperationId': 'string',
    'Password': 'string'
}


Response Structure

(dict) --
The TransferDomainToAnotherAwsAccount response includes the following elements.

OperationId (string) --
Identifier for tracking the progress of the request. To query the operation status, use GetOperationDetail .

Password (string) --
To finish transferring a domain to another AWS account, the account that the domain is being transferred to must submit an AcceptDomainTransferFromAnotherAwsAccount request. The request must include the value of the Password element that was returned in the TransferDomainToAnotherAwsAccount response.







Exceptions

Route53Domains.Client.exceptions.InvalidInput
Route53Domains.Client.exceptions.OperationLimitExceeded
Route53Domains.Client.exceptions.DuplicateRequest


    :return: {
        'OperationId': 'string',
        'Password': 'string'
    }
    
    
    :returns: 
    DomainName (string) -- [REQUIRED]
    The name of the domain that you want to transfer from the current AWS account to another account.
    
    AccountId (string) -- [REQUIRED]
    The account ID of the AWS account that you want to transfer the domain to, for example, 111122223333 .
    
    
    """
    pass

def update_domain_contact(DomainName=None, AdminContact=None, RegistrantContact=None, TechContact=None):
    """
    This operation updates the contact information for a particular domain. You must specify information for at least one contact: registrant, administrator, or technical.
    If the update is successful, this method returns an operation ID that you can use to track the progress and completion of the action. If the request is not completed successfully, the domain registrant will be notified by email.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_domain_contact(
        DomainName='string',
        AdminContact={
            'FirstName': 'string',
            'LastName': 'string',
            'ContactType': 'PERSON'|'COMPANY'|'ASSOCIATION'|'PUBLIC_BODY'|'RESELLER',
            'OrganizationName': 'string',
            'AddressLine1': 'string',
            'AddressLine2': 'string',
            'City': 'string',
            'State': 'string',
            'CountryCode': 'AD'|'AE'|'AF'|'AG'|'AI'|'AL'|'AM'|'AN'|'AO'|'AQ'|'AR'|'AS'|'AT'|'AU'|'AW'|'AZ'|'BA'|'BB'|'BD'|'BE'|'BF'|'BG'|'BH'|'BI'|'BJ'|'BL'|'BM'|'BN'|'BO'|'BR'|'BS'|'BT'|'BW'|'BY'|'BZ'|'CA'|'CC'|'CD'|'CF'|'CG'|'CH'|'CI'|'CK'|'CL'|'CM'|'CN'|'CO'|'CR'|'CU'|'CV'|'CX'|'CY'|'CZ'|'DE'|'DJ'|'DK'|'DM'|'DO'|'DZ'|'EC'|'EE'|'EG'|'ER'|'ES'|'ET'|'FI'|'FJ'|'FK'|'FM'|'FO'|'FR'|'GA'|'GB'|'GD'|'GE'|'GH'|'GI'|'GL'|'GM'|'GN'|'GQ'|'GR'|'GT'|'GU'|'GW'|'GY'|'HK'|'HN'|'HR'|'HT'|'HU'|'ID'|'IE'|'IL'|'IM'|'IN'|'IQ'|'IR'|'IS'|'IT'|'JM'|'JO'|'JP'|'KE'|'KG'|'KH'|'KI'|'KM'|'KN'|'KP'|'KR'|'KW'|'KY'|'KZ'|'LA'|'LB'|'LC'|'LI'|'LK'|'LR'|'LS'|'LT'|'LU'|'LV'|'LY'|'MA'|'MC'|'MD'|'ME'|'MF'|'MG'|'MH'|'MK'|'ML'|'MM'|'MN'|'MO'|'MP'|'MR'|'MS'|'MT'|'MU'|'MV'|'MW'|'MX'|'MY'|'MZ'|'NA'|'NC'|'NE'|'NG'|'NI'|'NL'|'NO'|'NP'|'NR'|'NU'|'NZ'|'OM'|'PA'|'PE'|'PF'|'PG'|'PH'|'PK'|'PL'|'PM'|'PN'|'PR'|'PT'|'PW'|'PY'|'QA'|'RO'|'RS'|'RU'|'RW'|'SA'|'SB'|'SC'|'SD'|'SE'|'SG'|'SH'|'SI'|'SK'|'SL'|'SM'|'SN'|'SO'|'SR'|'ST'|'SV'|'SY'|'SZ'|'TC'|'TD'|'TG'|'TH'|'TJ'|'TK'|'TL'|'TM'|'TN'|'TO'|'TR'|'TT'|'TV'|'TW'|'TZ'|'UA'|'UG'|'US'|'UY'|'UZ'|'VA'|'VC'|'VE'|'VG'|'VI'|'VN'|'VU'|'WF'|'WS'|'YE'|'YT'|'ZA'|'ZM'|'ZW',
            'ZipCode': 'string',
            'PhoneNumber': 'string',
            'Email': 'string',
            'Fax': 'string',
            'ExtraParams': [
                {
                    'Name': 'DUNS_NUMBER'|'BRAND_NUMBER'|'BIRTH_DEPARTMENT'|'BIRTH_DATE_IN_YYYY_MM_DD'|'BIRTH_COUNTRY'|'BIRTH_CITY'|'DOCUMENT_NUMBER'|'AU_ID_NUMBER'|'AU_ID_TYPE'|'CA_LEGAL_TYPE'|'CA_BUSINESS_ENTITY_TYPE'|'CA_LEGAL_REPRESENTATIVE'|'CA_LEGAL_REPRESENTATIVE_CAPACITY'|'ES_IDENTIFICATION'|'ES_IDENTIFICATION_TYPE'|'ES_LEGAL_FORM'|'FI_BUSINESS_NUMBER'|'FI_ID_NUMBER'|'FI_NATIONALITY'|'FI_ORGANIZATION_TYPE'|'IT_NATIONALITY'|'IT_PIN'|'IT_REGISTRANT_ENTITY_TYPE'|'RU_PASSPORT_DATA'|'SE_ID_NUMBER'|'SG_ID_NUMBER'|'VAT_NUMBER'|'UK_CONTACT_TYPE'|'UK_COMPANY_NUMBER',
                    'Value': 'string'
                },
            ]
        },
        RegistrantContact={
            'FirstName': 'string',
            'LastName': 'string',
            'ContactType': 'PERSON'|'COMPANY'|'ASSOCIATION'|'PUBLIC_BODY'|'RESELLER',
            'OrganizationName': 'string',
            'AddressLine1': 'string',
            'AddressLine2': 'string',
            'City': 'string',
            'State': 'string',
            'CountryCode': 'AD'|'AE'|'AF'|'AG'|'AI'|'AL'|'AM'|'AN'|'AO'|'AQ'|'AR'|'AS'|'AT'|'AU'|'AW'|'AZ'|'BA'|'BB'|'BD'|'BE'|'BF'|'BG'|'BH'|'BI'|'BJ'|'BL'|'BM'|'BN'|'BO'|'BR'|'BS'|'BT'|'BW'|'BY'|'BZ'|'CA'|'CC'|'CD'|'CF'|'CG'|'CH'|'CI'|'CK'|'CL'|'CM'|'CN'|'CO'|'CR'|'CU'|'CV'|'CX'|'CY'|'CZ'|'DE'|'DJ'|'DK'|'DM'|'DO'|'DZ'|'EC'|'EE'|'EG'|'ER'|'ES'|'ET'|'FI'|'FJ'|'FK'|'FM'|'FO'|'FR'|'GA'|'GB'|'GD'|'GE'|'GH'|'GI'|'GL'|'GM'|'GN'|'GQ'|'GR'|'GT'|'GU'|'GW'|'GY'|'HK'|'HN'|'HR'|'HT'|'HU'|'ID'|'IE'|'IL'|'IM'|'IN'|'IQ'|'IR'|'IS'|'IT'|'JM'|'JO'|'JP'|'KE'|'KG'|'KH'|'KI'|'KM'|'KN'|'KP'|'KR'|'KW'|'KY'|'KZ'|'LA'|'LB'|'LC'|'LI'|'LK'|'LR'|'LS'|'LT'|'LU'|'LV'|'LY'|'MA'|'MC'|'MD'|'ME'|'MF'|'MG'|'MH'|'MK'|'ML'|'MM'|'MN'|'MO'|'MP'|'MR'|'MS'|'MT'|'MU'|'MV'|'MW'|'MX'|'MY'|'MZ'|'NA'|'NC'|'NE'|'NG'|'NI'|'NL'|'NO'|'NP'|'NR'|'NU'|'NZ'|'OM'|'PA'|'PE'|'PF'|'PG'|'PH'|'PK'|'PL'|'PM'|'PN'|'PR'|'PT'|'PW'|'PY'|'QA'|'RO'|'RS'|'RU'|'RW'|'SA'|'SB'|'SC'|'SD'|'SE'|'SG'|'SH'|'SI'|'SK'|'SL'|'SM'|'SN'|'SO'|'SR'|'ST'|'SV'|'SY'|'SZ'|'TC'|'TD'|'TG'|'TH'|'TJ'|'TK'|'TL'|'TM'|'TN'|'TO'|'TR'|'TT'|'TV'|'TW'|'TZ'|'UA'|'UG'|'US'|'UY'|'UZ'|'VA'|'VC'|'VE'|'VG'|'VI'|'VN'|'VU'|'WF'|'WS'|'YE'|'YT'|'ZA'|'ZM'|'ZW',
            'ZipCode': 'string',
            'PhoneNumber': 'string',
            'Email': 'string',
            'Fax': 'string',
            'ExtraParams': [
                {
                    'Name': 'DUNS_NUMBER'|'BRAND_NUMBER'|'BIRTH_DEPARTMENT'|'BIRTH_DATE_IN_YYYY_MM_DD'|'BIRTH_COUNTRY'|'BIRTH_CITY'|'DOCUMENT_NUMBER'|'AU_ID_NUMBER'|'AU_ID_TYPE'|'CA_LEGAL_TYPE'|'CA_BUSINESS_ENTITY_TYPE'|'CA_LEGAL_REPRESENTATIVE'|'CA_LEGAL_REPRESENTATIVE_CAPACITY'|'ES_IDENTIFICATION'|'ES_IDENTIFICATION_TYPE'|'ES_LEGAL_FORM'|'FI_BUSINESS_NUMBER'|'FI_ID_NUMBER'|'FI_NATIONALITY'|'FI_ORGANIZATION_TYPE'|'IT_NATIONALITY'|'IT_PIN'|'IT_REGISTRANT_ENTITY_TYPE'|'RU_PASSPORT_DATA'|'SE_ID_NUMBER'|'SG_ID_NUMBER'|'VAT_NUMBER'|'UK_CONTACT_TYPE'|'UK_COMPANY_NUMBER',
                    'Value': 'string'
                },
            ]
        },
        TechContact={
            'FirstName': 'string',
            'LastName': 'string',
            'ContactType': 'PERSON'|'COMPANY'|'ASSOCIATION'|'PUBLIC_BODY'|'RESELLER',
            'OrganizationName': 'string',
            'AddressLine1': 'string',
            'AddressLine2': 'string',
            'City': 'string',
            'State': 'string',
            'CountryCode': 'AD'|'AE'|'AF'|'AG'|'AI'|'AL'|'AM'|'AN'|'AO'|'AQ'|'AR'|'AS'|'AT'|'AU'|'AW'|'AZ'|'BA'|'BB'|'BD'|'BE'|'BF'|'BG'|'BH'|'BI'|'BJ'|'BL'|'BM'|'BN'|'BO'|'BR'|'BS'|'BT'|'BW'|'BY'|'BZ'|'CA'|'CC'|'CD'|'CF'|'CG'|'CH'|'CI'|'CK'|'CL'|'CM'|'CN'|'CO'|'CR'|'CU'|'CV'|'CX'|'CY'|'CZ'|'DE'|'DJ'|'DK'|'DM'|'DO'|'DZ'|'EC'|'EE'|'EG'|'ER'|'ES'|'ET'|'FI'|'FJ'|'FK'|'FM'|'FO'|'FR'|'GA'|'GB'|'GD'|'GE'|'GH'|'GI'|'GL'|'GM'|'GN'|'GQ'|'GR'|'GT'|'GU'|'GW'|'GY'|'HK'|'HN'|'HR'|'HT'|'HU'|'ID'|'IE'|'IL'|'IM'|'IN'|'IQ'|'IR'|'IS'|'IT'|'JM'|'JO'|'JP'|'KE'|'KG'|'KH'|'KI'|'KM'|'KN'|'KP'|'KR'|'KW'|'KY'|'KZ'|'LA'|'LB'|'LC'|'LI'|'LK'|'LR'|'LS'|'LT'|'LU'|'LV'|'LY'|'MA'|'MC'|'MD'|'ME'|'MF'|'MG'|'MH'|'MK'|'ML'|'MM'|'MN'|'MO'|'MP'|'MR'|'MS'|'MT'|'MU'|'MV'|'MW'|'MX'|'MY'|'MZ'|'NA'|'NC'|'NE'|'NG'|'NI'|'NL'|'NO'|'NP'|'NR'|'NU'|'NZ'|'OM'|'PA'|'PE'|'PF'|'PG'|'PH'|'PK'|'PL'|'PM'|'PN'|'PR'|'PT'|'PW'|'PY'|'QA'|'RO'|'RS'|'RU'|'RW'|'SA'|'SB'|'SC'|'SD'|'SE'|'SG'|'SH'|'SI'|'SK'|'SL'|'SM'|'SN'|'SO'|'SR'|'ST'|'SV'|'SY'|'SZ'|'TC'|'TD'|'TG'|'TH'|'TJ'|'TK'|'TL'|'TM'|'TN'|'TO'|'TR'|'TT'|'TV'|'TW'|'TZ'|'UA'|'UG'|'US'|'UY'|'UZ'|'VA'|'VC'|'VE'|'VG'|'VI'|'VN'|'VU'|'WF'|'WS'|'YE'|'YT'|'ZA'|'ZM'|'ZW',
            'ZipCode': 'string',
            'PhoneNumber': 'string',
            'Email': 'string',
            'Fax': 'string',
            'ExtraParams': [
                {
                    'Name': 'DUNS_NUMBER'|'BRAND_NUMBER'|'BIRTH_DEPARTMENT'|'BIRTH_DATE_IN_YYYY_MM_DD'|'BIRTH_COUNTRY'|'BIRTH_CITY'|'DOCUMENT_NUMBER'|'AU_ID_NUMBER'|'AU_ID_TYPE'|'CA_LEGAL_TYPE'|'CA_BUSINESS_ENTITY_TYPE'|'CA_LEGAL_REPRESENTATIVE'|'CA_LEGAL_REPRESENTATIVE_CAPACITY'|'ES_IDENTIFICATION'|'ES_IDENTIFICATION_TYPE'|'ES_LEGAL_FORM'|'FI_BUSINESS_NUMBER'|'FI_ID_NUMBER'|'FI_NATIONALITY'|'FI_ORGANIZATION_TYPE'|'IT_NATIONALITY'|'IT_PIN'|'IT_REGISTRANT_ENTITY_TYPE'|'RU_PASSPORT_DATA'|'SE_ID_NUMBER'|'SG_ID_NUMBER'|'VAT_NUMBER'|'UK_CONTACT_TYPE'|'UK_COMPANY_NUMBER',
                    'Value': 'string'
                },
            ]
        }
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe name of the domain that you want to update contact information for.\n

    :type AdminContact: dict
    :param AdminContact: Provides detailed contact information.\n\nFirstName (string) --First name of contact.\n\nLastName (string) --Last name of contact.\n\nContactType (string) --Indicates whether the contact is a person, company, association, or public organization. Note the following:\n\nIf you specify a value other than PERSON , you must also specify a value for OrganizationName .\nFor some TLDs, the privacy protection available depends on the value that you specify for Contact Type . For the privacy protection settings for your TLD, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide\nFor .es domains, if you specify PERSON , you must specify INDIVIDUAL for the value of ES_LEGAL_FORM .\n\n\nOrganizationName (string) --Name of the organization for contact types other than PERSON .\n\nAddressLine1 (string) --First line of the contact\'s address.\n\nAddressLine2 (string) --Second line of contact\'s address, if any.\n\nCity (string) --The city of the contact\'s address.\n\nState (string) --The state or province of the contact\'s city.\n\nCountryCode (string) --Code for the country of the contact\'s address.\n\nZipCode (string) --The zip or postal code of the contact\'s address.\n\nPhoneNumber (string) --The phone number of the contact.\nConstraints: Phone number must be specified in the format '+[country dialing code].[number including any area code>]'. For example, a US phone number might appear as '+1.1234567890' .\n\nEmail (string) --Email address of the contact.\n\nFax (string) --Fax number of the contact.\nConstraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .\n\nExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.\n\n(dict) --ExtraParam includes the following elements.\n\nName (string) -- [REQUIRED]The name of an additional parameter that is required by a top-level domain. Here are the top-level domains that require additional parameters and the names of the parameters that they require:\n\n.com.au and .net.au\n\nAU_ID_NUMBER\nAU_ID_TYPE  Valid values include the following:\nABN (Australian business number)\nACN (Australian company number)\nTM (Trademark number)\n\n.ca\n\nBRAND_NUMBER\nCA_BUSINESS_ENTITY_TYPE  Valid values include the following:\nBANK (Bank)\nCOMMERCIAL_COMPANY (Commercial company)\nCOMPANY (Company)\nCOOPERATION (Cooperation)\nCOOPERATIVE (Cooperative)\nCOOPRIX (Cooprix)\nCORP (Corporation)\nCREDIT_UNION (Credit union)\nFOMIA (Federation of mutual insurance associations)\nINC (Incorporated)\nLTD (Limited)\nLTEE (Limit\xc3\xa9e)\nLLC (Limited liability corporation)\nLLP (Limited liability partnership)\nLTE (Lte.)\nMBA (Mutual benefit association)\nMIC (Mutual insurance company)\nNFP (Not-for-profit corporation)\nSA (S.A.)\nSAVINGS_COMPANY (Savings company)\nSAVINGS_UNION (Savings union)\nSARL (Soci\xc3\xa9t\xc3\xa9 \xc3\xa0 responsabilit\xc3\xa9 limit\xc3\xa9e)\nTRUST (Trust)\nULC (Unlimited liability corporation)\n\n\nCA_LEGAL_TYPE  When ContactType is PERSON , valid values include the following:\nABO (Aboriginal Peoples indigenous to Canada)\nCCT (Canadian citizen)\nLGR (Legal Representative of a Canadian Citizen or Permanent Resident)\nRES (Permanent resident of Canada)\n\n\n\nWhen ContactType is a value other than PERSON , valid values include the following:\n\n\nASS (Canadian unincorporated association)\nCCO (Canadian corporation)\nEDU (Canadian educational institution)\nGOV (Government or government entity in Canada)\nHOP (Canadian Hospital)\nINB (Indian Band recognized by the Indian Act of Canada)\nLAM (Canadian Library, Archive, or Museum)\nMAJ (Her/His Majesty the Queen/King)\nOMK (Official mark registered in Canada)\nPLT (Canadian Political Party)\nPRT (Partnership Registered in Canada)\nTDM (Trademark registered in Canada)\nTRD (Canadian Trade Union)\nTRS (Trust established in Canada)\n\n.es\n\n\nES_IDENTIFICATION  Specify the applicable value:\nFor contacts inside Spain: Enter your passport ID.\nFor contacts outside of Spain: Enter the VAT identification number for the company.\n\n\nNote\nFor .es domains, the value of ContactType must be PERSON .\n\n\nES_IDENTIFICATION_TYPE  Valid values include the following:\nDNI_AND_NIF (For Spanish contacts)\nNIE (For foreigners with legal residence)\nOTHER (For contacts outside of Spain)\n\n\nES_LEGAL_FORM  Valid values include the following:\nASSOCIATION\nCENTRAL_GOVERNMENT_BODY\nCIVIL_SOCIETY\nCOMMUNITY_OF_OWNERS\nCOMMUNITY_PROPERTY\nCONSULATE\nCOOPERATIVE\nDESIGNATION_OF_ORIGIN_SUPERVISORY_COUNCIL\nECONOMIC_INTEREST_GROUP\nEMBASSY\nENTITY_MANAGING_NATURAL_AREAS\nFARM_PARTNERSHIP\nFOUNDATION\nGENERAL_AND_LIMITED_PARTNERSHIP\nGENERAL_PARTNERSHIP\nINDIVIDUAL\nLIMITED_COMPANY\nLOCAL_AUTHORITY\nLOCAL_PUBLIC_ENTITY\nMUTUAL_INSURANCE_COMPANY\nNATIONAL_PUBLIC_ENTITY\nORDER_OR_RELIGIOUS_INSTITUTION\nOTHERS (Only for contacts outside of Spain)\nPOLITICAL_PARTY\nPROFESSIONAL_ASSOCIATION\nPUBLIC_LAW_ASSOCIATION\nPUBLIC_LIMITED_COMPANY\nREGIONAL_GOVERNMENT_BODY\nREGIONAL_PUBLIC_ENTITY\nSAVINGS_BANK\nSPANISH_OFFICE\nSPORTS_ASSOCIATION\nSPORTS_FEDERATION\nSPORTS_LIMITED_COMPANY\nTEMPORARY_ALLIANCE_OF_ENTERPRISES\nTRADE_UNION\nWORKER_OWNED_COMPANY\nWORKER_OWNED_LIMITED_COMPANY\n\n.fi\n\nBIRTH_DATE_IN_YYYY_MM_DD\nFI_BUSINESS_NUMBER\nFI_ID_NUMBER\nFI_NATIONALITY  Valid values include the following:\nFINNISH\nNOT_FINNISH\n\n\nFI_ORGANIZATION_TYPE  Valid values include the following:\nCOMPANY\nCORPORATION\nGOVERNMENT\nINSTITUTION\nPOLITICAL_PARTY\nPUBLIC_COMMUNITY\nTOWNSHIP\n\n.fr\n\nBIRTH_CITY\nBIRTH_COUNTRY\nBIRTH_DATE_IN_YYYY_MM_DD\nBIRTH_DEPARTMENT : Specify the INSEE code that corresponds with the department where the contact was born. If the contact was born somewhere other than France or its overseas departments, specify 99 . For more information, including a list of departments and the corresponding INSEE numbers, see the Wikipedia entry Departments of France .\nBRAND_NUMBER.it\n\nIT_NATIONALITY\nIT_PIN\nIT_REGISTRANT_ENTITY_TYPE  Valid values include the following:\nFOREIGNERS\nFREELANCE_WORKERS (Freelance workers and professionals)\nITALIAN_COMPANIES (Italian companies and one-person companies)\nNON_PROFIT_ORGANIZATIONS\nOTHER_SUBJECTS\nPUBLIC_ORGANIZATIONS\n\n.ru\n\nBIRTH_DATE_IN_YYYY_MM_DD\nRU_PASSPORT_DATA.se\n\nBIRTH_COUNTRY\nSE_ID_NUMBER.sg\n\nSG_ID_NUMBER.co.uk, .me.uk, and .org.uk\n\nUK_CONTACT_TYPE  Valid values include the following:\nCRC (UK Corporation by Royal Charter)\nFCORP (Non-UK Corporation)\nFIND (Non-UK Individual, representing self)\nFOTHER (Non-UK Entity that does not fit into any other category)\nGOV (UK Government Body)\nIND (UK Individual (representing self))\nIP (UK Industrial/Provident Registered Company)\nLLP (UK Limited Liability Partnership)\nLTD (UK Limited Company)\nOTHER (UK Entity that does not fit into any other category)\nPLC (UK Public Limited Company)\nPTNR (UK Partnership)\nRCHAR (UK Registered Charity)\nSCH (UK School)\nSTAT (UK Statutory Body)\nSTRA (UK Sole Trader)\n\n\nUK_COMPANY_NUMBER\n\nIn addition, many TLDs require a VAT_NUMBER .\n\nValue (string) -- [REQUIRED]The value that corresponds with the name of an extra parameter.\n\n\n\n\n\n\n

    :type RegistrantContact: dict
    :param RegistrantContact: Provides detailed contact information.\n\nFirstName (string) --First name of contact.\n\nLastName (string) --Last name of contact.\n\nContactType (string) --Indicates whether the contact is a person, company, association, or public organization. Note the following:\n\nIf you specify a value other than PERSON , you must also specify a value for OrganizationName .\nFor some TLDs, the privacy protection available depends on the value that you specify for Contact Type . For the privacy protection settings for your TLD, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide\nFor .es domains, if you specify PERSON , you must specify INDIVIDUAL for the value of ES_LEGAL_FORM .\n\n\nOrganizationName (string) --Name of the organization for contact types other than PERSON .\n\nAddressLine1 (string) --First line of the contact\'s address.\n\nAddressLine2 (string) --Second line of contact\'s address, if any.\n\nCity (string) --The city of the contact\'s address.\n\nState (string) --The state or province of the contact\'s city.\n\nCountryCode (string) --Code for the country of the contact\'s address.\n\nZipCode (string) --The zip or postal code of the contact\'s address.\n\nPhoneNumber (string) --The phone number of the contact.\nConstraints: Phone number must be specified in the format '+[country dialing code].[number including any area code>]'. For example, a US phone number might appear as '+1.1234567890' .\n\nEmail (string) --Email address of the contact.\n\nFax (string) --Fax number of the contact.\nConstraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .\n\nExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.\n\n(dict) --ExtraParam includes the following elements.\n\nName (string) -- [REQUIRED]The name of an additional parameter that is required by a top-level domain. Here are the top-level domains that require additional parameters and the names of the parameters that they require:\n\n.com.au and .net.au\n\nAU_ID_NUMBER\nAU_ID_TYPE  Valid values include the following:\nABN (Australian business number)\nACN (Australian company number)\nTM (Trademark number)\n\n.ca\n\nBRAND_NUMBER\nCA_BUSINESS_ENTITY_TYPE  Valid values include the following:\nBANK (Bank)\nCOMMERCIAL_COMPANY (Commercial company)\nCOMPANY (Company)\nCOOPERATION (Cooperation)\nCOOPERATIVE (Cooperative)\nCOOPRIX (Cooprix)\nCORP (Corporation)\nCREDIT_UNION (Credit union)\nFOMIA (Federation of mutual insurance associations)\nINC (Incorporated)\nLTD (Limited)\nLTEE (Limit\xc3\xa9e)\nLLC (Limited liability corporation)\nLLP (Limited liability partnership)\nLTE (Lte.)\nMBA (Mutual benefit association)\nMIC (Mutual insurance company)\nNFP (Not-for-profit corporation)\nSA (S.A.)\nSAVINGS_COMPANY (Savings company)\nSAVINGS_UNION (Savings union)\nSARL (Soci\xc3\xa9t\xc3\xa9 \xc3\xa0 responsabilit\xc3\xa9 limit\xc3\xa9e)\nTRUST (Trust)\nULC (Unlimited liability corporation)\n\n\nCA_LEGAL_TYPE  When ContactType is PERSON , valid values include the following:\nABO (Aboriginal Peoples indigenous to Canada)\nCCT (Canadian citizen)\nLGR (Legal Representative of a Canadian Citizen or Permanent Resident)\nRES (Permanent resident of Canada)\n\n\n\nWhen ContactType is a value other than PERSON , valid values include the following:\n\n\nASS (Canadian unincorporated association)\nCCO (Canadian corporation)\nEDU (Canadian educational institution)\nGOV (Government or government entity in Canada)\nHOP (Canadian Hospital)\nINB (Indian Band recognized by the Indian Act of Canada)\nLAM (Canadian Library, Archive, or Museum)\nMAJ (Her/His Majesty the Queen/King)\nOMK (Official mark registered in Canada)\nPLT (Canadian Political Party)\nPRT (Partnership Registered in Canada)\nTDM (Trademark registered in Canada)\nTRD (Canadian Trade Union)\nTRS (Trust established in Canada)\n\n.es\n\n\nES_IDENTIFICATION  Specify the applicable value:\nFor contacts inside Spain: Enter your passport ID.\nFor contacts outside of Spain: Enter the VAT identification number for the company.\n\n\nNote\nFor .es domains, the value of ContactType must be PERSON .\n\n\nES_IDENTIFICATION_TYPE  Valid values include the following:\nDNI_AND_NIF (For Spanish contacts)\nNIE (For foreigners with legal residence)\nOTHER (For contacts outside of Spain)\n\n\nES_LEGAL_FORM  Valid values include the following:\nASSOCIATION\nCENTRAL_GOVERNMENT_BODY\nCIVIL_SOCIETY\nCOMMUNITY_OF_OWNERS\nCOMMUNITY_PROPERTY\nCONSULATE\nCOOPERATIVE\nDESIGNATION_OF_ORIGIN_SUPERVISORY_COUNCIL\nECONOMIC_INTEREST_GROUP\nEMBASSY\nENTITY_MANAGING_NATURAL_AREAS\nFARM_PARTNERSHIP\nFOUNDATION\nGENERAL_AND_LIMITED_PARTNERSHIP\nGENERAL_PARTNERSHIP\nINDIVIDUAL\nLIMITED_COMPANY\nLOCAL_AUTHORITY\nLOCAL_PUBLIC_ENTITY\nMUTUAL_INSURANCE_COMPANY\nNATIONAL_PUBLIC_ENTITY\nORDER_OR_RELIGIOUS_INSTITUTION\nOTHERS (Only for contacts outside of Spain)\nPOLITICAL_PARTY\nPROFESSIONAL_ASSOCIATION\nPUBLIC_LAW_ASSOCIATION\nPUBLIC_LIMITED_COMPANY\nREGIONAL_GOVERNMENT_BODY\nREGIONAL_PUBLIC_ENTITY\nSAVINGS_BANK\nSPANISH_OFFICE\nSPORTS_ASSOCIATION\nSPORTS_FEDERATION\nSPORTS_LIMITED_COMPANY\nTEMPORARY_ALLIANCE_OF_ENTERPRISES\nTRADE_UNION\nWORKER_OWNED_COMPANY\nWORKER_OWNED_LIMITED_COMPANY\n\n.fi\n\nBIRTH_DATE_IN_YYYY_MM_DD\nFI_BUSINESS_NUMBER\nFI_ID_NUMBER\nFI_NATIONALITY  Valid values include the following:\nFINNISH\nNOT_FINNISH\n\n\nFI_ORGANIZATION_TYPE  Valid values include the following:\nCOMPANY\nCORPORATION\nGOVERNMENT\nINSTITUTION\nPOLITICAL_PARTY\nPUBLIC_COMMUNITY\nTOWNSHIP\n\n.fr\n\nBIRTH_CITY\nBIRTH_COUNTRY\nBIRTH_DATE_IN_YYYY_MM_DD\nBIRTH_DEPARTMENT : Specify the INSEE code that corresponds with the department where the contact was born. If the contact was born somewhere other than France or its overseas departments, specify 99 . For more information, including a list of departments and the corresponding INSEE numbers, see the Wikipedia entry Departments of France .\nBRAND_NUMBER.it\n\nIT_NATIONALITY\nIT_PIN\nIT_REGISTRANT_ENTITY_TYPE  Valid values include the following:\nFOREIGNERS\nFREELANCE_WORKERS (Freelance workers and professionals)\nITALIAN_COMPANIES (Italian companies and one-person companies)\nNON_PROFIT_ORGANIZATIONS\nOTHER_SUBJECTS\nPUBLIC_ORGANIZATIONS\n\n.ru\n\nBIRTH_DATE_IN_YYYY_MM_DD\nRU_PASSPORT_DATA.se\n\nBIRTH_COUNTRY\nSE_ID_NUMBER.sg\n\nSG_ID_NUMBER.co.uk, .me.uk, and .org.uk\n\nUK_CONTACT_TYPE  Valid values include the following:\nCRC (UK Corporation by Royal Charter)\nFCORP (Non-UK Corporation)\nFIND (Non-UK Individual, representing self)\nFOTHER (Non-UK Entity that does not fit into any other category)\nGOV (UK Government Body)\nIND (UK Individual (representing self))\nIP (UK Industrial/Provident Registered Company)\nLLP (UK Limited Liability Partnership)\nLTD (UK Limited Company)\nOTHER (UK Entity that does not fit into any other category)\nPLC (UK Public Limited Company)\nPTNR (UK Partnership)\nRCHAR (UK Registered Charity)\nSCH (UK School)\nSTAT (UK Statutory Body)\nSTRA (UK Sole Trader)\n\n\nUK_COMPANY_NUMBER\n\nIn addition, many TLDs require a VAT_NUMBER .\n\nValue (string) -- [REQUIRED]The value that corresponds with the name of an extra parameter.\n\n\n\n\n\n\n

    :type TechContact: dict
    :param TechContact: Provides detailed contact information.\n\nFirstName (string) --First name of contact.\n\nLastName (string) --Last name of contact.\n\nContactType (string) --Indicates whether the contact is a person, company, association, or public organization. Note the following:\n\nIf you specify a value other than PERSON , you must also specify a value for OrganizationName .\nFor some TLDs, the privacy protection available depends on the value that you specify for Contact Type . For the privacy protection settings for your TLD, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide\nFor .es domains, if you specify PERSON , you must specify INDIVIDUAL for the value of ES_LEGAL_FORM .\n\n\nOrganizationName (string) --Name of the organization for contact types other than PERSON .\n\nAddressLine1 (string) --First line of the contact\'s address.\n\nAddressLine2 (string) --Second line of contact\'s address, if any.\n\nCity (string) --The city of the contact\'s address.\n\nState (string) --The state or province of the contact\'s city.\n\nCountryCode (string) --Code for the country of the contact\'s address.\n\nZipCode (string) --The zip or postal code of the contact\'s address.\n\nPhoneNumber (string) --The phone number of the contact.\nConstraints: Phone number must be specified in the format '+[country dialing code].[number including any area code>]'. For example, a US phone number might appear as '+1.1234567890' .\n\nEmail (string) --Email address of the contact.\n\nFax (string) --Fax number of the contact.\nConstraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .\n\nExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.\n\n(dict) --ExtraParam includes the following elements.\n\nName (string) -- [REQUIRED]The name of an additional parameter that is required by a top-level domain. Here are the top-level domains that require additional parameters and the names of the parameters that they require:\n\n.com.au and .net.au\n\nAU_ID_NUMBER\nAU_ID_TYPE  Valid values include the following:\nABN (Australian business number)\nACN (Australian company number)\nTM (Trademark number)\n\n.ca\n\nBRAND_NUMBER\nCA_BUSINESS_ENTITY_TYPE  Valid values include the following:\nBANK (Bank)\nCOMMERCIAL_COMPANY (Commercial company)\nCOMPANY (Company)\nCOOPERATION (Cooperation)\nCOOPERATIVE (Cooperative)\nCOOPRIX (Cooprix)\nCORP (Corporation)\nCREDIT_UNION (Credit union)\nFOMIA (Federation of mutual insurance associations)\nINC (Incorporated)\nLTD (Limited)\nLTEE (Limit\xc3\xa9e)\nLLC (Limited liability corporation)\nLLP (Limited liability partnership)\nLTE (Lte.)\nMBA (Mutual benefit association)\nMIC (Mutual insurance company)\nNFP (Not-for-profit corporation)\nSA (S.A.)\nSAVINGS_COMPANY (Savings company)\nSAVINGS_UNION (Savings union)\nSARL (Soci\xc3\xa9t\xc3\xa9 \xc3\xa0 responsabilit\xc3\xa9 limit\xc3\xa9e)\nTRUST (Trust)\nULC (Unlimited liability corporation)\n\n\nCA_LEGAL_TYPE  When ContactType is PERSON , valid values include the following:\nABO (Aboriginal Peoples indigenous to Canada)\nCCT (Canadian citizen)\nLGR (Legal Representative of a Canadian Citizen or Permanent Resident)\nRES (Permanent resident of Canada)\n\n\n\nWhen ContactType is a value other than PERSON , valid values include the following:\n\n\nASS (Canadian unincorporated association)\nCCO (Canadian corporation)\nEDU (Canadian educational institution)\nGOV (Government or government entity in Canada)\nHOP (Canadian Hospital)\nINB (Indian Band recognized by the Indian Act of Canada)\nLAM (Canadian Library, Archive, or Museum)\nMAJ (Her/His Majesty the Queen/King)\nOMK (Official mark registered in Canada)\nPLT (Canadian Political Party)\nPRT (Partnership Registered in Canada)\nTDM (Trademark registered in Canada)\nTRD (Canadian Trade Union)\nTRS (Trust established in Canada)\n\n.es\n\n\nES_IDENTIFICATION  Specify the applicable value:\nFor contacts inside Spain: Enter your passport ID.\nFor contacts outside of Spain: Enter the VAT identification number for the company.\n\n\nNote\nFor .es domains, the value of ContactType must be PERSON .\n\n\nES_IDENTIFICATION_TYPE  Valid values include the following:\nDNI_AND_NIF (For Spanish contacts)\nNIE (For foreigners with legal residence)\nOTHER (For contacts outside of Spain)\n\n\nES_LEGAL_FORM  Valid values include the following:\nASSOCIATION\nCENTRAL_GOVERNMENT_BODY\nCIVIL_SOCIETY\nCOMMUNITY_OF_OWNERS\nCOMMUNITY_PROPERTY\nCONSULATE\nCOOPERATIVE\nDESIGNATION_OF_ORIGIN_SUPERVISORY_COUNCIL\nECONOMIC_INTEREST_GROUP\nEMBASSY\nENTITY_MANAGING_NATURAL_AREAS\nFARM_PARTNERSHIP\nFOUNDATION\nGENERAL_AND_LIMITED_PARTNERSHIP\nGENERAL_PARTNERSHIP\nINDIVIDUAL\nLIMITED_COMPANY\nLOCAL_AUTHORITY\nLOCAL_PUBLIC_ENTITY\nMUTUAL_INSURANCE_COMPANY\nNATIONAL_PUBLIC_ENTITY\nORDER_OR_RELIGIOUS_INSTITUTION\nOTHERS (Only for contacts outside of Spain)\nPOLITICAL_PARTY\nPROFESSIONAL_ASSOCIATION\nPUBLIC_LAW_ASSOCIATION\nPUBLIC_LIMITED_COMPANY\nREGIONAL_GOVERNMENT_BODY\nREGIONAL_PUBLIC_ENTITY\nSAVINGS_BANK\nSPANISH_OFFICE\nSPORTS_ASSOCIATION\nSPORTS_FEDERATION\nSPORTS_LIMITED_COMPANY\nTEMPORARY_ALLIANCE_OF_ENTERPRISES\nTRADE_UNION\nWORKER_OWNED_COMPANY\nWORKER_OWNED_LIMITED_COMPANY\n\n.fi\n\nBIRTH_DATE_IN_YYYY_MM_DD\nFI_BUSINESS_NUMBER\nFI_ID_NUMBER\nFI_NATIONALITY  Valid values include the following:\nFINNISH\nNOT_FINNISH\n\n\nFI_ORGANIZATION_TYPE  Valid values include the following:\nCOMPANY\nCORPORATION\nGOVERNMENT\nINSTITUTION\nPOLITICAL_PARTY\nPUBLIC_COMMUNITY\nTOWNSHIP\n\n.fr\n\nBIRTH_CITY\nBIRTH_COUNTRY\nBIRTH_DATE_IN_YYYY_MM_DD\nBIRTH_DEPARTMENT : Specify the INSEE code that corresponds with the department where the contact was born. If the contact was born somewhere other than France or its overseas departments, specify 99 . For more information, including a list of departments and the corresponding INSEE numbers, see the Wikipedia entry Departments of France .\nBRAND_NUMBER.it\n\nIT_NATIONALITY\nIT_PIN\nIT_REGISTRANT_ENTITY_TYPE  Valid values include the following:\nFOREIGNERS\nFREELANCE_WORKERS (Freelance workers and professionals)\nITALIAN_COMPANIES (Italian companies and one-person companies)\nNON_PROFIT_ORGANIZATIONS\nOTHER_SUBJECTS\nPUBLIC_ORGANIZATIONS\n\n.ru\n\nBIRTH_DATE_IN_YYYY_MM_DD\nRU_PASSPORT_DATA.se\n\nBIRTH_COUNTRY\nSE_ID_NUMBER.sg\n\nSG_ID_NUMBER.co.uk, .me.uk, and .org.uk\n\nUK_CONTACT_TYPE  Valid values include the following:\nCRC (UK Corporation by Royal Charter)\nFCORP (Non-UK Corporation)\nFIND (Non-UK Individual, representing self)\nFOTHER (Non-UK Entity that does not fit into any other category)\nGOV (UK Government Body)\nIND (UK Individual (representing self))\nIP (UK Industrial/Provident Registered Company)\nLLP (UK Limited Liability Partnership)\nLTD (UK Limited Company)\nOTHER (UK Entity that does not fit into any other category)\nPLC (UK Public Limited Company)\nPTNR (UK Partnership)\nRCHAR (UK Registered Charity)\nSCH (UK School)\nSTAT (UK Statutory Body)\nSTRA (UK Sole Trader)\n\n\nUK_COMPANY_NUMBER\n\nIn addition, many TLDs require a VAT_NUMBER .\n\nValue (string) -- [REQUIRED]The value that corresponds with the name of an extra parameter.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'OperationId': 'string'
}


Response Structure

(dict) --
The UpdateDomainContact response includes the following element.

OperationId (string) --
Identifier for tracking the progress of the request. To query the operation status, use GetOperationDetail .







Exceptions

Route53Domains.Client.exceptions.InvalidInput
Route53Domains.Client.exceptions.DuplicateRequest
Route53Domains.Client.exceptions.TLDRulesViolation
Route53Domains.Client.exceptions.OperationLimitExceeded
Route53Domains.Client.exceptions.UnsupportedTLD


    :return: {
        'OperationId': 'string'
    }
    
    
    :returns: 
    Route53Domains.Client.exceptions.InvalidInput
    Route53Domains.Client.exceptions.DuplicateRequest
    Route53Domains.Client.exceptions.TLDRulesViolation
    Route53Domains.Client.exceptions.OperationLimitExceeded
    Route53Domains.Client.exceptions.UnsupportedTLD
    
    """
    pass

def update_domain_contact_privacy(DomainName=None, AdminPrivacy=None, RegistrantPrivacy=None, TechPrivacy=None):
    """
    This operation updates the specified domain contact\'s privacy setting. When privacy protection is enabled, contact information such as email address is replaced either with contact information for Amazon Registrar (for .com, .net, and .org domains) or with contact information for our registrar associate, Gandi.
    This operation affects only the contact information for the specified contact type (registrant, administrator, or tech). If the request succeeds, Amazon Route 53 returns an operation ID that you can use with GetOperationDetail to track the progress and completion of the action. If the request doesn\'t complete successfully, the domain registrant will be notified by email.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_domain_contact_privacy(
        DomainName='string',
        AdminPrivacy=True|False,
        RegistrantPrivacy=True|False,
        TechPrivacy=True|False
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe name of the domain that you want to update the privacy setting for.\n

    :type AdminPrivacy: boolean
    :param AdminPrivacy: Whether you want to conceal contact information from WHOIS queries. If you specify true , WHOIS ('who is') queries return contact information either for Amazon Registrar (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other TLDs). If you specify false , WHOIS queries return the information that you entered for the admin contact.

    :type RegistrantPrivacy: boolean
    :param RegistrantPrivacy: Whether you want to conceal contact information from WHOIS queries. If you specify true , WHOIS ('who is') queries return contact information either for Amazon Registrar (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other TLDs). If you specify false , WHOIS queries return the information that you entered for the registrant contact (domain owner).

    :type TechPrivacy: boolean
    :param TechPrivacy: Whether you want to conceal contact information from WHOIS queries. If you specify true , WHOIS ('who is') queries return contact information either for Amazon Registrar (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other TLDs). If you specify false , WHOIS queries return the information that you entered for the technical contact.

    :rtype: dict

ReturnsResponse Syntax
{
    'OperationId': 'string'
}


Response Structure

(dict) --
The UpdateDomainContactPrivacy response includes the following element.

OperationId (string) --
Identifier for tracking the progress of the request. To use this ID to query the operation status, use GetOperationDetail.







Exceptions

Route53Domains.Client.exceptions.InvalidInput
Route53Domains.Client.exceptions.DuplicateRequest
Route53Domains.Client.exceptions.TLDRulesViolation
Route53Domains.Client.exceptions.OperationLimitExceeded
Route53Domains.Client.exceptions.UnsupportedTLD


    :return: {
        'OperationId': 'string'
    }
    
    
    :returns: 
    Route53Domains.Client.exceptions.InvalidInput
    Route53Domains.Client.exceptions.DuplicateRequest
    Route53Domains.Client.exceptions.TLDRulesViolation
    Route53Domains.Client.exceptions.OperationLimitExceeded
    Route53Domains.Client.exceptions.UnsupportedTLD
    
    """
    pass

def update_domain_nameservers(DomainName=None, FIAuthKey=None, Nameservers=None):
    """
    This operation replaces the current set of name servers for the domain with the specified set of name servers. If you use Amazon Route 53 as your DNS service, specify the four name servers in the delegation set for the hosted zone for the domain.
    If successful, this operation returns an operation ID that you can use to track the progress and completion of the action. If the request is not completed successfully, the domain registrant will be notified by email.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_domain_nameservers(
        DomainName='string',
        FIAuthKey='string',
        Nameservers=[
            {
                'Name': 'string',
                'GlueIps': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe name of the domain that you want to change name servers for.\n

    :type FIAuthKey: string
    :param FIAuthKey: The authorization key for .fi domains

    :type Nameservers: list
    :param Nameservers: [REQUIRED]\nA list of new name servers for the domain.\n\n(dict) --Nameserver includes the following elements.\n\nName (string) -- [REQUIRED]The fully qualified host name of the name server.\nConstraint: Maximum 255 characters\n\nGlueIps (list) --Glue IP address of a name server entry. Glue IP addresses are required only when the name of the name server is a subdomain of the domain. For example, if your domain is example.com and the name server for the domain is ns.example.com, you need to specify the IP address for ns.example.com.\nConstraints: The list can contain only one IPv4 and one IPv6 address.\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'OperationId': 'string'
}


Response Structure

(dict) --
The UpdateDomainNameservers response includes the following element.

OperationId (string) --
Identifier for tracking the progress of the request. To query the operation status, use GetOperationDetail .







Exceptions

Route53Domains.Client.exceptions.InvalidInput
Route53Domains.Client.exceptions.DuplicateRequest
Route53Domains.Client.exceptions.TLDRulesViolation
Route53Domains.Client.exceptions.OperationLimitExceeded
Route53Domains.Client.exceptions.UnsupportedTLD


    :return: {
        'OperationId': 'string'
    }
    
    
    :returns: 
    Route53Domains.Client.exceptions.InvalidInput
    Route53Domains.Client.exceptions.DuplicateRequest
    Route53Domains.Client.exceptions.TLDRulesViolation
    Route53Domains.Client.exceptions.OperationLimitExceeded
    Route53Domains.Client.exceptions.UnsupportedTLD
    
    """
    pass

def update_tags_for_domain(DomainName=None, TagsToUpdate=None):
    """
    This operation adds or updates tags for a specified domain.
    All tag operations are eventually consistent; subsequent operations might not immediately represent all issued operations.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_tags_for_domain(
        DomainName='string',
        TagsToUpdate=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe domain for which you want to add or update tags.\n

    :type TagsToUpdate: list
    :param TagsToUpdate: A list of the tag keys and values that you want to add or update. If you specify a key that already exists, the corresponding value will be replaced.\n\n(dict) --Each tag includes the following elements.\n\nKey (string) --The key (name) of a tag.\nValid values: A-Z, a-z, 0-9, space, '.:/=+-@'\nConstraints: Each key can be 1-128 characters long.\n\nValue (string) --The value of a tag.\nValid values: A-Z, a-z, 0-9, space, '.:/=+-@'\nConstraints: Each value can be 0-256 characters long.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Route53Domains.Client.exceptions.InvalidInput
Route53Domains.Client.exceptions.OperationLimitExceeded
Route53Domains.Client.exceptions.UnsupportedTLD


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def view_billing(Start=None, End=None, Marker=None, MaxItems=None):
    """
    Returns all the domain-related billing records for the current AWS account for a specified period
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.view_billing(
        Start=datetime(2015, 1, 1),
        End=datetime(2015, 1, 1),
        Marker='string',
        MaxItems=123
    )
    
    
    :type Start: datetime
    :param Start: The beginning date and time for the time period for which you want a list of billing records. Specify the date and time in Unix time format and Coordinated Universal time (UTC).

    :type End: datetime
    :param End: The end date and time for the time period for which you want a list of billing records. Specify the date and time in Unix time format and Coordinated Universal time (UTC).

    :type Marker: string
    :param Marker: For an initial request for a list of billing records, omit this element. If the number of billing records that are associated with the current AWS account during the specified period is greater than the value that you specified for MaxItems , you can use Marker to return additional billing records. Get the value of NextPageMarker from the previous response, and submit another request that includes the value of NextPageMarker in the Marker element.\nConstraints: The marker must match the value of NextPageMarker that was returned in the previous response.\n

    :type MaxItems: integer
    :param MaxItems: The number of billing records to be returned.\nDefault: 20\n

    :rtype: dict

ReturnsResponse Syntax
{
    'NextPageMarker': 'string',
    'BillingRecords': [
        {
            'DomainName': 'string',
            'Operation': 'REGISTER_DOMAIN'|'DELETE_DOMAIN'|'TRANSFER_IN_DOMAIN'|'UPDATE_DOMAIN_CONTACT'|'UPDATE_NAMESERVER'|'CHANGE_PRIVACY_PROTECTION'|'DOMAIN_LOCK'|'ENABLE_AUTORENEW'|'DISABLE_AUTORENEW'|'ADD_DNSSEC'|'REMOVE_DNSSEC'|'EXPIRE_DOMAIN'|'TRANSFER_OUT_DOMAIN'|'CHANGE_DOMAIN_OWNER'|'RENEW_DOMAIN'|'PUSH_DOMAIN'|'INTERNAL_TRANSFER_OUT_DOMAIN'|'INTERNAL_TRANSFER_IN_DOMAIN',
            'InvoiceId': 'string',
            'BillDate': datetime(2015, 1, 1),
            'Price': 123.0
        },
    ]
}


Response Structure

(dict) --
The ViewBilling response includes the following elements.

NextPageMarker (string) --
If there are more billing records than you specified for MaxItems in the request, submit another request and include the value of NextPageMarker in the value of Marker .

BillingRecords (list) --
A summary of billing records.

(dict) --
Information for one billing record.

DomainName (string) --
The name of the domain that the billing record applies to. If the domain name contains characters other than a-z, 0-9, and - (hyphen), such as an internationalized domain name, then this value is in Punycode. For more information, see DNS Domain Name Format in the Amazon Route 53 Developer Guide .

Operation (string) --
The operation that you were charged for.

InvoiceId (string) --
The ID of the invoice that is associated with the billing record.

BillDate (datetime) --
The date that the operation was billed, in Unix format.

Price (float) --
The price that you were charged for the operation, in US dollars.
Example value: 12.0











Exceptions

Route53Domains.Client.exceptions.InvalidInput


    :return: {
        'NextPageMarker': 'string',
        'BillingRecords': [
            {
                'DomainName': 'string',
                'Operation': 'REGISTER_DOMAIN'|'DELETE_DOMAIN'|'TRANSFER_IN_DOMAIN'|'UPDATE_DOMAIN_CONTACT'|'UPDATE_NAMESERVER'|'CHANGE_PRIVACY_PROTECTION'|'DOMAIN_LOCK'|'ENABLE_AUTORENEW'|'DISABLE_AUTORENEW'|'ADD_DNSSEC'|'REMOVE_DNSSEC'|'EXPIRE_DOMAIN'|'TRANSFER_OUT_DOMAIN'|'CHANGE_DOMAIN_OWNER'|'RENEW_DOMAIN'|'PUSH_DOMAIN'|'INTERNAL_TRANSFER_OUT_DOMAIN'|'INTERNAL_TRANSFER_IN_DOMAIN',
                'InvoiceId': 'string',
                'BillDate': datetime(2015, 1, 1),
                'Price': 123.0
            },
        ]
    }
    
    
    :returns: 
    Route53Domains.Client.exceptions.InvalidInput
    
    """
    pass

