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

def check_domain_availability(DomainName=None, IdnLangCode=None):
    """
    This operation checks the availability of one domain name. Note that if the availability status of a domain is pending, you must submit another request to determine the availability of the domain name.
    See also: AWS API Documentation
    
    
    :example: response = client.check_domain_availability(
        DomainName='string',
        IdnLangCode='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The name of the domain that you want to get availability for.
            Constraints: The domain name can contain only the letters a through z, the numbers 0 through 9, and hyphen (-). Internationalized Domain Names are not supported.
            

    :type IdnLangCode: string
    :param IdnLangCode: Reserved for future use.

    :rtype: dict
    :return: {
        'Availability': 'AVAILABLE'|'AVAILABLE_RESERVED'|'AVAILABLE_PREORDER'|'UNAVAILABLE'|'UNAVAILABLE_PREMIUM'|'UNAVAILABLE_RESTRICTED'|'RESERVED'|'DONT_KNOW'
    }
    
    
    """
    pass

def delete_tags_for_domain(DomainName=None, TagsToDelete=None):
    """
    This operation deletes the specified tags for a domain.
    All tag operations are eventually consistent; subsequent operations may not immediately represent all issued operations.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_tags_for_domain(
        DomainName='string',
        TagsToDelete=[
            'string',
        ]
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The domain for which you want to delete one or more tags.
            

    :type TagsToDelete: list
    :param TagsToDelete: [REQUIRED]
            A list of tag keys to delete.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def disable_domain_auto_renew(DomainName=None):
    """
    This operation disables automatic renewal of domain registration for the specified domain.
    See also: AWS API Documentation
    
    
    :example: response = client.disable_domain_auto_renew(
        DomainName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The name of the domain that you want to disable automatic renewal for.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def disable_domain_transfer_lock(DomainName=None):
    """
    This operation removes the transfer lock on the domain (specifically the clientTransferProhibited status) to allow domain transfers. We recommend you refrain from performing this action unless you intend to transfer the domain to a different registrar. Successful submission returns an operation ID that you can use to track the progress and completion of the action. If the request is not completed successfully, the domain registrant will be notified by email.
    See also: AWS API Documentation
    
    
    :example: response = client.disable_domain_transfer_lock(
        DomainName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The name of the domain that you want to remove the transfer lock for.
            

    :rtype: dict
    :return: {
        'OperationId': 'string'
    }
    
    
    """
    pass

def enable_domain_auto_renew(DomainName=None):
    """
    This operation configures Amazon Route 53 to automatically renew the specified domain before the domain registration expires. The cost of renewing your domain registration is billed to your AWS account.
    The period during which you can renew a domain name varies by TLD. For a list of TLDs and their renewal policies, see "Renewal, restoration, and deletion times" on the website for our registrar partner, Gandi. Route 53 requires that you renew before the end of the renewal period that is listed on the Gandi website so we can complete processing before the deadline.
    See also: AWS API Documentation
    
    
    :example: response = client.enable_domain_auto_renew(
        DomainName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The name of the domain that you want to enable automatic renewal for.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def enable_domain_transfer_lock(DomainName=None):
    """
    This operation sets the transfer lock on the domain (specifically the clientTransferProhibited status) to prevent domain transfers. Successful submission returns an operation ID that you can use to track the progress and completion of the action. If the request is not completed successfully, the domain registrant will be notified by email.
    See also: AWS API Documentation
    
    
    :example: response = client.enable_domain_transfer_lock(
        DomainName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The name of the domain that you want to set the transfer lock for.
            

    :rtype: dict
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

def get_contact_reachability_status(domainName=None):
    """
    For operations that require confirmation that the email address for the registrant contact is valid, such as registering a new domain, this operation returns information about whether the registrant contact has responded.
    If you want us to resend the email, use the ResendContactReachabilityEmail operation.
    See also: AWS API Documentation
    
    
    :example: response = client.get_contact_reachability_status(
        domainName='string'
    )
    
    
    :type domainName: string
    :param domainName: The name of the domain for which you want to know whether the registrant contact has confirmed that the email address is valid.

    :rtype: dict
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
    
    
    :example: response = client.get_domain_detail(
        DomainName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The name of the domain that you want to get detailed information about.
            

    :rtype: dict
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
                    'Name': 'DUNS_NUMBER'|'BRAND_NUMBER'|'BIRTH_DEPARTMENT'|'BIRTH_DATE_IN_YYYY_MM_DD'|'BIRTH_COUNTRY'|'BIRTH_CITY'|'DOCUMENT_NUMBER'|'AU_ID_NUMBER'|'AU_ID_TYPE'|'CA_LEGAL_TYPE'|'CA_BUSINESS_ENTITY_TYPE'|'ES_IDENTIFICATION'|'ES_IDENTIFICATION_TYPE'|'ES_LEGAL_FORM'|'FI_BUSINESS_NUMBER'|'FI_ID_NUMBER'|'IT_PIN'|'RU_PASSPORT_DATA'|'SE_ID_NUMBER'|'SG_ID_NUMBER'|'VAT_NUMBER',
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
                    'Name': 'DUNS_NUMBER'|'BRAND_NUMBER'|'BIRTH_DEPARTMENT'|'BIRTH_DATE_IN_YYYY_MM_DD'|'BIRTH_COUNTRY'|'BIRTH_CITY'|'DOCUMENT_NUMBER'|'AU_ID_NUMBER'|'AU_ID_TYPE'|'CA_LEGAL_TYPE'|'CA_BUSINESS_ENTITY_TYPE'|'ES_IDENTIFICATION'|'ES_IDENTIFICATION_TYPE'|'ES_LEGAL_FORM'|'FI_BUSINESS_NUMBER'|'FI_ID_NUMBER'|'IT_PIN'|'RU_PASSPORT_DATA'|'SE_ID_NUMBER'|'SG_ID_NUMBER'|'VAT_NUMBER',
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
                    'Name': 'DUNS_NUMBER'|'BRAND_NUMBER'|'BIRTH_DEPARTMENT'|'BIRTH_DATE_IN_YYYY_MM_DD'|'BIRTH_COUNTRY'|'BIRTH_CITY'|'DOCUMENT_NUMBER'|'AU_ID_NUMBER'|'AU_ID_TYPE'|'CA_LEGAL_TYPE'|'CA_BUSINESS_ENTITY_TYPE'|'ES_IDENTIFICATION'|'ES_IDENTIFICATION_TYPE'|'ES_LEGAL_FORM'|'FI_BUSINESS_NUMBER'|'FI_ID_NUMBER'|'IT_PIN'|'RU_PASSPORT_DATA'|'SE_ID_NUMBER'|'SG_ID_NUMBER'|'VAT_NUMBER',
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
    (string) --
    
    """
    pass

def get_domain_suggestions(DomainName=None, SuggestionCount=None, OnlyAvailable=None):
    """
    The GetDomainSuggestions operation returns a list of suggested domain names given a string, which can either be a domain name or simply a word or phrase (without spaces).
    See also: AWS API Documentation
    
    
    :example: response = client.get_domain_suggestions(
        DomainName='string',
        SuggestionCount=123,
        OnlyAvailable=True|False
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            A domain name that you want to use as the basis for a list of possible domain names. The domain name must contain a top-level domain (TLD), such as .com, that Amazon Route 53 supports. For a list of TLDs, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide .
            

    :type SuggestionCount: integer
    :param SuggestionCount: [REQUIRED]
            The number of suggested domain names that you want Amazon Route 53 to return.
            

    :type OnlyAvailable: boolean
    :param OnlyAvailable: [REQUIRED]
            If OnlyAvailable is true , Amazon Route 53 returns only domain names that are available. If OnlyAvailable is false , Amazon Route 53 returns domain names without checking whether they're available to be registered. To determine whether the domain is available, you can call checkDomainAvailability for each suggestion.
            

    :rtype: dict
    :return: {
        'SuggestionsList': [
            {
                'DomainName': 'string',
                'Availability': 'string'
            },
        ]
    }
    
    
    """
    pass

def get_operation_detail(OperationId=None):
    """
    This operation returns the current status of an operation that is not completed.
    See also: AWS API Documentation
    
    
    :example: response = client.get_operation_detail(
        OperationId='string'
    )
    
    
    :type OperationId: string
    :param OperationId: [REQUIRED]
            The identifier for the operation for which you want to get the status. Amazon Route 53 returned the identifier in the response to the original request.
            

    :rtype: dict
    :return: {
        'OperationId': 'string',
        'Status': 'SUBMITTED'|'IN_PROGRESS'|'ERROR'|'SUCCESSFUL'|'FAILED',
        'Message': 'string',
        'DomainName': 'string',
        'Type': 'REGISTER_DOMAIN'|'DELETE_DOMAIN'|'TRANSFER_IN_DOMAIN'|'UPDATE_DOMAIN_CONTACT'|'UPDATE_NAMESERVER'|'CHANGE_PRIVACY_PROTECTION'|'DOMAIN_LOCK',
        'SubmittedDate': datetime(2015, 1, 1)
    }
    
    
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

def list_domains(Marker=None, MaxItems=None):
    """
    This operation returns all the domain names registered with Amazon Route 53 for the current AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_domains(
        Marker='string',
        MaxItems=123
    )
    
    
    :type Marker: string
    :param Marker: For an initial request for a list of domains, omit this element. If the number of domains that are associated with the current AWS account is greater than the value that you specified for MaxItems , you can use Marker to return additional domains. Get the value of NextPageMarker from the previous response, and submit another request that includes the value of NextPageMarker in the Marker element.
            Constraints: The marker must match the value specified in the previous request.
            

    :type MaxItems: integer
    :param MaxItems: Number of domains to be returned.
            Default: 20
            

    :rtype: dict
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
    
    
    """
    pass

def list_operations(Marker=None, MaxItems=None):
    """
    This operation returns the operation IDs of operations that are not yet complete.
    See also: AWS API Documentation
    
    
    :example: response = client.list_operations(
        Marker='string',
        MaxItems=123
    )
    
    
    :type Marker: string
    :param Marker: For an initial request for a list of operations, omit this element. If the number of operations that are not yet complete is greater than the value that you specified for MaxItems , you can use Marker to return additional operations. Get the value of NextPageMarker from the previous response, and submit another request that includes the value of NextPageMarker in the Marker element.

    :type MaxItems: integer
    :param MaxItems: Number of domains to be returned.
            Default: 20
            

    :rtype: dict
    :return: {
        'Operations': [
            {
                'OperationId': 'string',
                'Status': 'SUBMITTED'|'IN_PROGRESS'|'ERROR'|'SUCCESSFUL'|'FAILED',
                'Type': 'REGISTER_DOMAIN'|'DELETE_DOMAIN'|'TRANSFER_IN_DOMAIN'|'UPDATE_DOMAIN_CONTACT'|'UPDATE_NAMESERVER'|'CHANGE_PRIVACY_PROTECTION'|'DOMAIN_LOCK',
                'SubmittedDate': datetime(2015, 1, 1)
            },
        ],
        'NextPageMarker': 'string'
    }
    
    
    """
    pass

def list_tags_for_domain(DomainName=None):
    """
    This operation returns all of the tags that are associated with the specified domain.
    All tag operations are eventually consistent; subsequent operations may not immediately represent all issued operations.
    See also: AWS API Documentation
    
    
    :example: response = client.list_tags_for_domain(
        DomainName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The domain for which you want to get a list of tags.
            

    :rtype: dict
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
    This operation registers a domain. Domains are registered by the AWS registrar partner, Gandi. For some top-level domains (TLDs), this operation requires extra parameters.
    When you register a domain, Amazon Route 53 does the following:
    See also: AWS API Documentation
    
    
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
                    'Name': 'DUNS_NUMBER'|'BRAND_NUMBER'|'BIRTH_DEPARTMENT'|'BIRTH_DATE_IN_YYYY_MM_DD'|'BIRTH_COUNTRY'|'BIRTH_CITY'|'DOCUMENT_NUMBER'|'AU_ID_NUMBER'|'AU_ID_TYPE'|'CA_LEGAL_TYPE'|'CA_BUSINESS_ENTITY_TYPE'|'ES_IDENTIFICATION'|'ES_IDENTIFICATION_TYPE'|'ES_LEGAL_FORM'|'FI_BUSINESS_NUMBER'|'FI_ID_NUMBER'|'IT_PIN'|'RU_PASSPORT_DATA'|'SE_ID_NUMBER'|'SG_ID_NUMBER'|'VAT_NUMBER',
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
                    'Name': 'DUNS_NUMBER'|'BRAND_NUMBER'|'BIRTH_DEPARTMENT'|'BIRTH_DATE_IN_YYYY_MM_DD'|'BIRTH_COUNTRY'|'BIRTH_CITY'|'DOCUMENT_NUMBER'|'AU_ID_NUMBER'|'AU_ID_TYPE'|'CA_LEGAL_TYPE'|'CA_BUSINESS_ENTITY_TYPE'|'ES_IDENTIFICATION'|'ES_IDENTIFICATION_TYPE'|'ES_LEGAL_FORM'|'FI_BUSINESS_NUMBER'|'FI_ID_NUMBER'|'IT_PIN'|'RU_PASSPORT_DATA'|'SE_ID_NUMBER'|'SG_ID_NUMBER'|'VAT_NUMBER',
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
                    'Name': 'DUNS_NUMBER'|'BRAND_NUMBER'|'BIRTH_DEPARTMENT'|'BIRTH_DATE_IN_YYYY_MM_DD'|'BIRTH_COUNTRY'|'BIRTH_CITY'|'DOCUMENT_NUMBER'|'AU_ID_NUMBER'|'AU_ID_TYPE'|'CA_LEGAL_TYPE'|'CA_BUSINESS_ENTITY_TYPE'|'ES_IDENTIFICATION'|'ES_IDENTIFICATION_TYPE'|'ES_LEGAL_FORM'|'FI_BUSINESS_NUMBER'|'FI_ID_NUMBER'|'IT_PIN'|'RU_PASSPORT_DATA'|'SE_ID_NUMBER'|'SG_ID_NUMBER'|'VAT_NUMBER',
                    'Value': 'string'
                },
            ]
        },
        PrivacyProtectAdminContact=True|False,
        PrivacyProtectRegistrantContact=True|False,
        PrivacyProtectTechContact=True|False
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The domain name that you want to register.
            Constraints: The domain name can contain only the letters a through z, the numbers 0 through 9, and hyphen (-). Internationalized Domain Names are not supported.
            

    :type IdnLangCode: string
    :param IdnLangCode: Reserved for future use.

    :type DurationInYears: integer
    :param DurationInYears: [REQUIRED]
            The number of years that you want to register the domain for. Domains are registered for a minimum of one year. The maximum period depends on the top-level domain. For the range of valid values for your domain, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide .
            Default: 1
            

    :type AutoRenew: boolean
    :param AutoRenew: Indicates whether the domain will be automatically renewed (true ) or not (false ). Autorenewal only takes effect after the account is charged.
            Default: true
            

    :type AdminContact: dict
    :param AdminContact: [REQUIRED]
            Provides detailed contact information.
            FirstName (string) --First name of contact.
            LastName (string) --Last name of contact.
            ContactType (string) --Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than PERSON , you must enter an organization name, and you can't enable privacy protection for the contact.
            OrganizationName (string) --Name of the organization for contact types other than PERSON .
            AddressLine1 (string) --First line of the contact's address.
            AddressLine2 (string) --Second line of contact's address, if any.
            City (string) --The city of the contact's address.
            State (string) --The state or province of the contact's city.
            CountryCode (string) --Code for the country of the contact's address.
            ZipCode (string) --The zip or postal code of the contact's address.
            PhoneNumber (string) --The phone number of the contact.
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .
            Email (string) --Email address of the contact.
            Fax (string) --Fax number of the contact.
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .
            ExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.
            (dict) --ExtraParam includes the following elements.
            Name (string) -- [REQUIRED]Name of the additional parameter required by the top-level domain.
            Value (string) -- [REQUIRED]Values corresponding to the additional parameter names required by some top-level domains.
            
            

    :type RegistrantContact: dict
    :param RegistrantContact: [REQUIRED]
            Provides detailed contact information.
            FirstName (string) --First name of contact.
            LastName (string) --Last name of contact.
            ContactType (string) --Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than PERSON , you must enter an organization name, and you can't enable privacy protection for the contact.
            OrganizationName (string) --Name of the organization for contact types other than PERSON .
            AddressLine1 (string) --First line of the contact's address.
            AddressLine2 (string) --Second line of contact's address, if any.
            City (string) --The city of the contact's address.
            State (string) --The state or province of the contact's city.
            CountryCode (string) --Code for the country of the contact's address.
            ZipCode (string) --The zip or postal code of the contact's address.
            PhoneNumber (string) --The phone number of the contact.
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .
            Email (string) --Email address of the contact.
            Fax (string) --Fax number of the contact.
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .
            ExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.
            (dict) --ExtraParam includes the following elements.
            Name (string) -- [REQUIRED]Name of the additional parameter required by the top-level domain.
            Value (string) -- [REQUIRED]Values corresponding to the additional parameter names required by some top-level domains.
            
            

    :type TechContact: dict
    :param TechContact: [REQUIRED]
            Provides detailed contact information.
            FirstName (string) --First name of contact.
            LastName (string) --Last name of contact.
            ContactType (string) --Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than PERSON , you must enter an organization name, and you can't enable privacy protection for the contact.
            OrganizationName (string) --Name of the organization for contact types other than PERSON .
            AddressLine1 (string) --First line of the contact's address.
            AddressLine2 (string) --Second line of contact's address, if any.
            City (string) --The city of the contact's address.
            State (string) --The state or province of the contact's city.
            CountryCode (string) --Code for the country of the contact's address.
            ZipCode (string) --The zip or postal code of the contact's address.
            PhoneNumber (string) --The phone number of the contact.
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .
            Email (string) --Email address of the contact.
            Fax (string) --Fax number of the contact.
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .
            ExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.
            (dict) --ExtraParam includes the following elements.
            Name (string) -- [REQUIRED]Name of the additional parameter required by the top-level domain.
            Value (string) -- [REQUIRED]Values corresponding to the additional parameter names required by some top-level domains.
            
            

    :type PrivacyProtectAdminContact: boolean
    :param PrivacyProtectAdminContact: Whether you want to conceal contact information from WHOIS queries. If you specify true , WHOIS ('who is') queries will return contact information for our registrar partner, Gandi, instead of the contact information that you enter.
            Default: true
            

    :type PrivacyProtectRegistrantContact: boolean
    :param PrivacyProtectRegistrantContact: Whether you want to conceal contact information from WHOIS queries. If you specify true , WHOIS ('who is') queries will return contact information for our registrar partner, Gandi, instead of the contact information that you enter.
            Default: true
            

    :type PrivacyProtectTechContact: boolean
    :param PrivacyProtectTechContact: Whether you want to conceal contact information from WHOIS queries. If you specify true , WHOIS ('who is') queries will return contact information for our registrar partner, Gandi, instead of the contact information that you enter.
            Default: true
            

    :rtype: dict
    :return: {
        'OperationId': 'string'
    }
    
    
    :returns: 
    DomainName (string) -- [REQUIRED]
    The domain name that you want to register.
    Constraints: The domain name can contain only the letters a through z, the numbers 0 through 9, and hyphen (-). Internationalized Domain Names are not supported.
    
    IdnLangCode (string) -- Reserved for future use.
    DurationInYears (integer) -- [REQUIRED]
    The number of years that you want to register the domain for. Domains are registered for a minimum of one year. The maximum period depends on the top-level domain. For the range of valid values for your domain, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide .
    Default: 1
    
    AutoRenew (boolean) -- Indicates whether the domain will be automatically renewed (true ) or not (false ). Autorenewal only takes effect after the account is charged.
    Default: true
    
    AdminContact (dict) -- [REQUIRED]
    Provides detailed contact information.
    
    FirstName (string) --First name of contact.
    
    LastName (string) --Last name of contact.
    
    ContactType (string) --Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than PERSON , you must enter an organization name, and you can't enable privacy protection for the contact.
    
    OrganizationName (string) --Name of the organization for contact types other than PERSON .
    
    AddressLine1 (string) --First line of the contact's address.
    
    AddressLine2 (string) --Second line of contact's address, if any.
    
    City (string) --The city of the contact's address.
    
    State (string) --The state or province of the contact's city.
    
    CountryCode (string) --Code for the country of the contact's address.
    
    ZipCode (string) --The zip or postal code of the contact's address.
    
    PhoneNumber (string) --The phone number of the contact.
    Constraints: Phone number must be specified in the format "+[country dialing code].[number including any area code]". For example, a US phone number might appear as "+1.1234567890" .
    
    Email (string) --Email address of the contact.
    
    Fax (string) --Fax number of the contact.
    Constraints: Phone number must be specified in the format "+[country dialing code].[number including any area code]". For example, a US phone number might appear as "+1.1234567890" .
    
    ExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.
    
    (dict) --ExtraParam includes the following elements.
    
    Name (string) -- [REQUIRED]Name of the additional parameter required by the top-level domain.
    
    Value (string) -- [REQUIRED]Values corresponding to the additional parameter names required by some top-level domains.
    
    
    
    
    
    
    
    RegistrantContact (dict) -- [REQUIRED]
    Provides detailed contact information.
    
    FirstName (string) --First name of contact.
    
    LastName (string) --Last name of contact.
    
    ContactType (string) --Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than PERSON , you must enter an organization name, and you can't enable privacy protection for the contact.
    
    OrganizationName (string) --Name of the organization for contact types other than PERSON .
    
    AddressLine1 (string) --First line of the contact's address.
    
    AddressLine2 (string) --Second line of contact's address, if any.
    
    City (string) --The city of the contact's address.
    
    State (string) --The state or province of the contact's city.
    
    CountryCode (string) --Code for the country of the contact's address.
    
    ZipCode (string) --The zip or postal code of the contact's address.
    
    PhoneNumber (string) --The phone number of the contact.
    Constraints: Phone number must be specified in the format "+[country dialing code].[number including any area code]". For example, a US phone number might appear as "+1.1234567890" .
    
    Email (string) --Email address of the contact.
    
    Fax (string) --Fax number of the contact.
    Constraints: Phone number must be specified in the format "+[country dialing code].[number including any area code]". For example, a US phone number might appear as "+1.1234567890" .
    
    ExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.
    
    (dict) --ExtraParam includes the following elements.
    
    Name (string) -- [REQUIRED]Name of the additional parameter required by the top-level domain.
    
    Value (string) -- [REQUIRED]Values corresponding to the additional parameter names required by some top-level domains.
    
    
    
    
    
    
    
    TechContact (dict) -- [REQUIRED]
    Provides detailed contact information.
    
    FirstName (string) --First name of contact.
    
    LastName (string) --Last name of contact.
    
    ContactType (string) --Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than PERSON , you must enter an organization name, and you can't enable privacy protection for the contact.
    
    OrganizationName (string) --Name of the organization for contact types other than PERSON .
    
    AddressLine1 (string) --First line of the contact's address.
    
    AddressLine2 (string) --Second line of contact's address, if any.
    
    City (string) --The city of the contact's address.
    
    State (string) --The state or province of the contact's city.
    
    CountryCode (string) --Code for the country of the contact's address.
    
    ZipCode (string) --The zip or postal code of the contact's address.
    
    PhoneNumber (string) --The phone number of the contact.
    Constraints: Phone number must be specified in the format "+[country dialing code].[number including any area code]". For example, a US phone number might appear as "+1.1234567890" .
    
    Email (string) --Email address of the contact.
    
    Fax (string) --Fax number of the contact.
    Constraints: Phone number must be specified in the format "+[country dialing code].[number including any area code]". For example, a US phone number might appear as "+1.1234567890" .
    
    ExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.
    
    (dict) --ExtraParam includes the following elements.
    
    Name (string) -- [REQUIRED]Name of the additional parameter required by the top-level domain.
    
    Value (string) -- [REQUIRED]Values corresponding to the additional parameter names required by some top-level domains.
    
    
    
    
    
    
    
    PrivacyProtectAdminContact (boolean) -- Whether you want to conceal contact information from WHOIS queries. If you specify true , WHOIS ("who is") queries will return contact information for our registrar partner, Gandi, instead of the contact information that you enter.
    Default: true
    
    PrivacyProtectRegistrantContact (boolean) -- Whether you want to conceal contact information from WHOIS queries. If you specify true , WHOIS ("who is") queries will return contact information for our registrar partner, Gandi, instead of the contact information that you enter.
    Default: true
    
    PrivacyProtectTechContact (boolean) -- Whether you want to conceal contact information from WHOIS queries. If you specify true , WHOIS ("who is") queries will return contact information for our registrar partner, Gandi, instead of the contact information that you enter.
    Default: true
    
    
    """
    pass

def renew_domain(DomainName=None, DurationInYears=None, CurrentExpiryYear=None):
    """
    This operation renews a domain for the specified number of years. The cost of renewing your domain is billed to your AWS account.
    We recommend that you renew your domain several weeks before the expiration date. Some TLD registries delete domains before the expiration date if you haven't renewed far enough in advance. For more information about renewing domain registration, see Renewing Registration for a Domain in the Amazon Route 53 Developer Guide.
    See also: AWS API Documentation
    
    
    :example: response = client.renew_domain(
        DomainName='string',
        DurationInYears=123,
        CurrentExpiryYear=123
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The name of the domain that you want to renew.
            

    :type DurationInYears: integer
    :param DurationInYears: The number of years that you want to renew the domain for. The maximum number of years depends on the top-level domain. For the range of valid values for your domain, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide .
            Default: 1
            

    :type CurrentExpiryYear: integer
    :param CurrentExpiryYear: [REQUIRED]
            The year when the registration for the domain is set to expire. This value must match the current expiration date for the domain.
            

    :rtype: dict
    :return: {
        'OperationId': 'string'
    }
    
    
    """
    pass

def resend_contact_reachability_email(domainName=None):
    """
    For operations that require confirmation that the email address for the registrant contact is valid, such as registering a new domain, this operation resends the confirmation email to the current email address for the registrant contact.
    See also: AWS API Documentation
    
    
    :example: response = client.resend_contact_reachability_email(
        domainName='string'
    )
    
    
    :type domainName: string
    :param domainName: The name of the domain for which you want Amazon Route 53 to resend a confirmation email to the registrant contact.

    :rtype: dict
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
    
    
    :example: response = client.retrieve_domain_auth_code(
        DomainName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The name of the domain that you want to get an authorization code for.
            

    :rtype: dict
    :return: {
        'AuthCode': 'string'
    }
    
    
    """
    pass

def transfer_domain(DomainName=None, IdnLangCode=None, DurationInYears=None, Nameservers=None, AuthCode=None, AutoRenew=None, AdminContact=None, RegistrantContact=None, TechContact=None, PrivacyProtectAdminContact=None, PrivacyProtectRegistrantContact=None, PrivacyProtectTechContact=None):
    """
    This operation transfers a domain from another registrar to Amazon Route 53. When the transfer is complete, the domain is registered with the AWS registrar partner, Gandi.
    For transfer requirements, a detailed procedure, and information about viewing the status of a domain transfer, see Transferring Registration for a Domain to Amazon Route 53 in the Amazon Route 53 Developer Guide .
    If the registrar for your domain is also the DNS service provider for the domain, we highly recommend that you consider transferring your DNS service to Amazon Route 53 or to another DNS service provider before you transfer your registration. Some registrars provide free DNS service when you purchase a domain registration. When you transfer the registration, the previous registrar will not renew your domain registration and could end your DNS service at any time.
    If the transfer is successful, this method returns an operation ID that you can use to track the progress and completion of the action. If the transfer doesn't complete successfully, the domain registrant will be notified by email.
    See also: AWS API Documentation
    
    
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
                    'Name': 'DUNS_NUMBER'|'BRAND_NUMBER'|'BIRTH_DEPARTMENT'|'BIRTH_DATE_IN_YYYY_MM_DD'|'BIRTH_COUNTRY'|'BIRTH_CITY'|'DOCUMENT_NUMBER'|'AU_ID_NUMBER'|'AU_ID_TYPE'|'CA_LEGAL_TYPE'|'CA_BUSINESS_ENTITY_TYPE'|'ES_IDENTIFICATION'|'ES_IDENTIFICATION_TYPE'|'ES_LEGAL_FORM'|'FI_BUSINESS_NUMBER'|'FI_ID_NUMBER'|'IT_PIN'|'RU_PASSPORT_DATA'|'SE_ID_NUMBER'|'SG_ID_NUMBER'|'VAT_NUMBER',
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
                    'Name': 'DUNS_NUMBER'|'BRAND_NUMBER'|'BIRTH_DEPARTMENT'|'BIRTH_DATE_IN_YYYY_MM_DD'|'BIRTH_COUNTRY'|'BIRTH_CITY'|'DOCUMENT_NUMBER'|'AU_ID_NUMBER'|'AU_ID_TYPE'|'CA_LEGAL_TYPE'|'CA_BUSINESS_ENTITY_TYPE'|'ES_IDENTIFICATION'|'ES_IDENTIFICATION_TYPE'|'ES_LEGAL_FORM'|'FI_BUSINESS_NUMBER'|'FI_ID_NUMBER'|'IT_PIN'|'RU_PASSPORT_DATA'|'SE_ID_NUMBER'|'SG_ID_NUMBER'|'VAT_NUMBER',
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
                    'Name': 'DUNS_NUMBER'|'BRAND_NUMBER'|'BIRTH_DEPARTMENT'|'BIRTH_DATE_IN_YYYY_MM_DD'|'BIRTH_COUNTRY'|'BIRTH_CITY'|'DOCUMENT_NUMBER'|'AU_ID_NUMBER'|'AU_ID_TYPE'|'CA_LEGAL_TYPE'|'CA_BUSINESS_ENTITY_TYPE'|'ES_IDENTIFICATION'|'ES_IDENTIFICATION_TYPE'|'ES_LEGAL_FORM'|'FI_BUSINESS_NUMBER'|'FI_ID_NUMBER'|'IT_PIN'|'RU_PASSPORT_DATA'|'SE_ID_NUMBER'|'SG_ID_NUMBER'|'VAT_NUMBER',
                    'Value': 'string'
                },
            ]
        },
        PrivacyProtectAdminContact=True|False,
        PrivacyProtectRegistrantContact=True|False,
        PrivacyProtectTechContact=True|False
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The name of the domain that you want to transfer to Amazon Route 53.
            Constraints: The domain name can contain only the letters a through z, the numbers 0 through 9, and hyphen (-). Internationalized Domain Names are not supported.
            

    :type IdnLangCode: string
    :param IdnLangCode: Reserved for future use.

    :type DurationInYears: integer
    :param DurationInYears: [REQUIRED]
            The number of years that you want to register the domain for. Domains are registered for a minimum of one year. The maximum period depends on the top-level domain.
            Default: 1
            

    :type Nameservers: list
    :param Nameservers: Contains details for the host and glue IP addresses.
            (dict) --Nameserver includes the following elements.
            Name (string) -- [REQUIRED]The fully qualified host name of the name server.
            Constraint: Maximum 255 characters
            GlueIps (list) --Glue IP address of a name server entry. Glue IP addresses are required only when the name of the name server is a subdomain of the domain. For example, if your domain is example.com and the name server for the domain is ns.example.com, you need to specify the IP address for ns.example.com.
            Constraints: The list can contain only one IPv4 and one IPv6 address.
            (string) --
            
            

    :type AuthCode: string
    :param AuthCode: The authorization code for the domain. You get this value from the current registrar.

    :type AutoRenew: boolean
    :param AutoRenew: Indicates whether the domain will be automatically renewed (true) or not (false). Autorenewal only takes effect after the account is charged.
            Default: true
            

    :type AdminContact: dict
    :param AdminContact: [REQUIRED]
            Provides detailed contact information.
            FirstName (string) --First name of contact.
            LastName (string) --Last name of contact.
            ContactType (string) --Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than PERSON , you must enter an organization name, and you can't enable privacy protection for the contact.
            OrganizationName (string) --Name of the organization for contact types other than PERSON .
            AddressLine1 (string) --First line of the contact's address.
            AddressLine2 (string) --Second line of contact's address, if any.
            City (string) --The city of the contact's address.
            State (string) --The state or province of the contact's city.
            CountryCode (string) --Code for the country of the contact's address.
            ZipCode (string) --The zip or postal code of the contact's address.
            PhoneNumber (string) --The phone number of the contact.
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .
            Email (string) --Email address of the contact.
            Fax (string) --Fax number of the contact.
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .
            ExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.
            (dict) --ExtraParam includes the following elements.
            Name (string) -- [REQUIRED]Name of the additional parameter required by the top-level domain.
            Value (string) -- [REQUIRED]Values corresponding to the additional parameter names required by some top-level domains.
            
            

    :type RegistrantContact: dict
    :param RegistrantContact: [REQUIRED]
            Provides detailed contact information.
            FirstName (string) --First name of contact.
            LastName (string) --Last name of contact.
            ContactType (string) --Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than PERSON , you must enter an organization name, and you can't enable privacy protection for the contact.
            OrganizationName (string) --Name of the organization for contact types other than PERSON .
            AddressLine1 (string) --First line of the contact's address.
            AddressLine2 (string) --Second line of contact's address, if any.
            City (string) --The city of the contact's address.
            State (string) --The state or province of the contact's city.
            CountryCode (string) --Code for the country of the contact's address.
            ZipCode (string) --The zip or postal code of the contact's address.
            PhoneNumber (string) --The phone number of the contact.
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .
            Email (string) --Email address of the contact.
            Fax (string) --Fax number of the contact.
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .
            ExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.
            (dict) --ExtraParam includes the following elements.
            Name (string) -- [REQUIRED]Name of the additional parameter required by the top-level domain.
            Value (string) -- [REQUIRED]Values corresponding to the additional parameter names required by some top-level domains.
            
            

    :type TechContact: dict
    :param TechContact: [REQUIRED]
            Provides detailed contact information.
            FirstName (string) --First name of contact.
            LastName (string) --Last name of contact.
            ContactType (string) --Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than PERSON , you must enter an organization name, and you can't enable privacy protection for the contact.
            OrganizationName (string) --Name of the organization for contact types other than PERSON .
            AddressLine1 (string) --First line of the contact's address.
            AddressLine2 (string) --Second line of contact's address, if any.
            City (string) --The city of the contact's address.
            State (string) --The state or province of the contact's city.
            CountryCode (string) --Code for the country of the contact's address.
            ZipCode (string) --The zip or postal code of the contact's address.
            PhoneNumber (string) --The phone number of the contact.
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .
            Email (string) --Email address of the contact.
            Fax (string) --Fax number of the contact.
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .
            ExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.
            (dict) --ExtraParam includes the following elements.
            Name (string) -- [REQUIRED]Name of the additional parameter required by the top-level domain.
            Value (string) -- [REQUIRED]Values corresponding to the additional parameter names required by some top-level domains.
            
            

    :type PrivacyProtectAdminContact: boolean
    :param PrivacyProtectAdminContact: Whether you want to conceal contact information from WHOIS queries. If you specify true , WHOIS ('who is') queries will return contact information for our registrar partner, Gandi, instead of the contact information that you enter.
            Default: true
            

    :type PrivacyProtectRegistrantContact: boolean
    :param PrivacyProtectRegistrantContact: Whether you want to conceal contact information from WHOIS queries. If you specify true , WHOIS ('who is') queries will return contact information for our registrar partner, Gandi, instead of the contact information that you enter.
            Default: true
            

    :type PrivacyProtectTechContact: boolean
    :param PrivacyProtectTechContact: Whether you want to conceal contact information from WHOIS queries. If you specify true , WHOIS ('who is') queries will return contact information for our registrar partner, Gandi, instead of the contact information that you enter.
            Default: true
            

    :rtype: dict
    :return: {
        'OperationId': 'string'
    }
    
    
    """
    pass

def update_domain_contact(DomainName=None, AdminContact=None, RegistrantContact=None, TechContact=None):
    """
    This operation updates the contact information for a particular domain. Information for at least one contact (registrant, administrator, or technical) must be supplied for update.
    If the update is successful, this method returns an operation ID that you can use to track the progress and completion of the action. If the request is not completed successfully, the domain registrant will be notified by email.
    See also: AWS API Documentation
    
    
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
                    'Name': 'DUNS_NUMBER'|'BRAND_NUMBER'|'BIRTH_DEPARTMENT'|'BIRTH_DATE_IN_YYYY_MM_DD'|'BIRTH_COUNTRY'|'BIRTH_CITY'|'DOCUMENT_NUMBER'|'AU_ID_NUMBER'|'AU_ID_TYPE'|'CA_LEGAL_TYPE'|'CA_BUSINESS_ENTITY_TYPE'|'ES_IDENTIFICATION'|'ES_IDENTIFICATION_TYPE'|'ES_LEGAL_FORM'|'FI_BUSINESS_NUMBER'|'FI_ID_NUMBER'|'IT_PIN'|'RU_PASSPORT_DATA'|'SE_ID_NUMBER'|'SG_ID_NUMBER'|'VAT_NUMBER',
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
                    'Name': 'DUNS_NUMBER'|'BRAND_NUMBER'|'BIRTH_DEPARTMENT'|'BIRTH_DATE_IN_YYYY_MM_DD'|'BIRTH_COUNTRY'|'BIRTH_CITY'|'DOCUMENT_NUMBER'|'AU_ID_NUMBER'|'AU_ID_TYPE'|'CA_LEGAL_TYPE'|'CA_BUSINESS_ENTITY_TYPE'|'ES_IDENTIFICATION'|'ES_IDENTIFICATION_TYPE'|'ES_LEGAL_FORM'|'FI_BUSINESS_NUMBER'|'FI_ID_NUMBER'|'IT_PIN'|'RU_PASSPORT_DATA'|'SE_ID_NUMBER'|'SG_ID_NUMBER'|'VAT_NUMBER',
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
                    'Name': 'DUNS_NUMBER'|'BRAND_NUMBER'|'BIRTH_DEPARTMENT'|'BIRTH_DATE_IN_YYYY_MM_DD'|'BIRTH_COUNTRY'|'BIRTH_CITY'|'DOCUMENT_NUMBER'|'AU_ID_NUMBER'|'AU_ID_TYPE'|'CA_LEGAL_TYPE'|'CA_BUSINESS_ENTITY_TYPE'|'ES_IDENTIFICATION'|'ES_IDENTIFICATION_TYPE'|'ES_LEGAL_FORM'|'FI_BUSINESS_NUMBER'|'FI_ID_NUMBER'|'IT_PIN'|'RU_PASSPORT_DATA'|'SE_ID_NUMBER'|'SG_ID_NUMBER'|'VAT_NUMBER',
                    'Value': 'string'
                },
            ]
        }
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The name of the domain that you want to update contact information for.
            

    :type AdminContact: dict
    :param AdminContact: Provides detailed contact information.
            FirstName (string) --First name of contact.
            LastName (string) --Last name of contact.
            ContactType (string) --Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than PERSON , you must enter an organization name, and you can't enable privacy protection for the contact.
            OrganizationName (string) --Name of the organization for contact types other than PERSON .
            AddressLine1 (string) --First line of the contact's address.
            AddressLine2 (string) --Second line of contact's address, if any.
            City (string) --The city of the contact's address.
            State (string) --The state or province of the contact's city.
            CountryCode (string) --Code for the country of the contact's address.
            ZipCode (string) --The zip or postal code of the contact's address.
            PhoneNumber (string) --The phone number of the contact.
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .
            Email (string) --Email address of the contact.
            Fax (string) --Fax number of the contact.
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .
            ExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.
            (dict) --ExtraParam includes the following elements.
            Name (string) -- [REQUIRED]Name of the additional parameter required by the top-level domain.
            Value (string) -- [REQUIRED]Values corresponding to the additional parameter names required by some top-level domains.
            
            

    :type RegistrantContact: dict
    :param RegistrantContact: Provides detailed contact information.
            FirstName (string) --First name of contact.
            LastName (string) --Last name of contact.
            ContactType (string) --Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than PERSON , you must enter an organization name, and you can't enable privacy protection for the contact.
            OrganizationName (string) --Name of the organization for contact types other than PERSON .
            AddressLine1 (string) --First line of the contact's address.
            AddressLine2 (string) --Second line of contact's address, if any.
            City (string) --The city of the contact's address.
            State (string) --The state or province of the contact's city.
            CountryCode (string) --Code for the country of the contact's address.
            ZipCode (string) --The zip or postal code of the contact's address.
            PhoneNumber (string) --The phone number of the contact.
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .
            Email (string) --Email address of the contact.
            Fax (string) --Fax number of the contact.
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .
            ExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.
            (dict) --ExtraParam includes the following elements.
            Name (string) -- [REQUIRED]Name of the additional parameter required by the top-level domain.
            Value (string) -- [REQUIRED]Values corresponding to the additional parameter names required by some top-level domains.
            
            

    :type TechContact: dict
    :param TechContact: Provides detailed contact information.
            FirstName (string) --First name of contact.
            LastName (string) --Last name of contact.
            ContactType (string) --Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than PERSON , you must enter an organization name, and you can't enable privacy protection for the contact.
            OrganizationName (string) --Name of the organization for contact types other than PERSON .
            AddressLine1 (string) --First line of the contact's address.
            AddressLine2 (string) --Second line of contact's address, if any.
            City (string) --The city of the contact's address.
            State (string) --The state or province of the contact's city.
            CountryCode (string) --Code for the country of the contact's address.
            ZipCode (string) --The zip or postal code of the contact's address.
            PhoneNumber (string) --The phone number of the contact.
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .
            Email (string) --Email address of the contact.
            Fax (string) --Fax number of the contact.
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .
            ExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.
            (dict) --ExtraParam includes the following elements.
            Name (string) -- [REQUIRED]Name of the additional parameter required by the top-level domain.
            Value (string) -- [REQUIRED]Values corresponding to the additional parameter names required by some top-level domains.
            
            

    :rtype: dict
    :return: {
        'OperationId': 'string'
    }
    
    
    """
    pass

def update_domain_contact_privacy(DomainName=None, AdminPrivacy=None, RegistrantPrivacy=None, TechPrivacy=None):
    """
    This operation updates the specified domain contact's privacy setting. When the privacy option is enabled, personal information such as postal or email address is hidden from the results of a public WHOIS query. The privacy services are provided by the AWS registrar, Gandi. For more information, see the Gandi privacy features .
    This operation only affects the privacy of the specified contact type (registrant, administrator, or tech). Successful acceptance returns an operation ID that you can use with  GetOperationDetail to track the progress and completion of the action. If the request is not completed successfully, the domain registrant will be notified by email.
    See also: AWS API Documentation
    
    
    :example: response = client.update_domain_contact_privacy(
        DomainName='string',
        AdminPrivacy=True|False,
        RegistrantPrivacy=True|False,
        TechPrivacy=True|False
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The name of the domain that you want to update the privacy setting for.
            

    :type AdminPrivacy: boolean
    :param AdminPrivacy: Whether you want to conceal contact information from WHOIS queries. If you specify true , WHOIS ('who is') queries will return contact information for our registrar partner, Gandi, instead of the contact information that you enter.

    :type RegistrantPrivacy: boolean
    :param RegistrantPrivacy: Whether you want to conceal contact information from WHOIS queries. If you specify true , WHOIS ('who is') queries will return contact information for our registrar partner, Gandi, instead of the contact information that you enter.

    :type TechPrivacy: boolean
    :param TechPrivacy: Whether you want to conceal contact information from WHOIS queries. If you specify true , WHOIS ('who is') queries will return contact information for our registrar partner, Gandi, instead of the contact information that you enter.

    :rtype: dict
    :return: {
        'OperationId': 'string'
    }
    
    
    """
    pass

def update_domain_nameservers(DomainName=None, FIAuthKey=None, Nameservers=None):
    """
    This operation replaces the current set of name servers for the domain with the specified set of name servers. If you use Amazon Route 53 as your DNS service, specify the four name servers in the delegation set for the hosted zone for the domain.
    If successful, this operation returns an operation ID that you can use to track the progress and completion of the action. If the request is not completed successfully, the domain registrant will be notified by email.
    See also: AWS API Documentation
    
    
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
    :param DomainName: [REQUIRED]
            The name of the domain that you want to change name servers for.
            

    :type FIAuthKey: string
    :param FIAuthKey: The authorization key for .fi domains

    :type Nameservers: list
    :param Nameservers: [REQUIRED]
            A list of new name servers for the domain.
            (dict) --Nameserver includes the following elements.
            Name (string) -- [REQUIRED]The fully qualified host name of the name server.
            Constraint: Maximum 255 characters
            GlueIps (list) --Glue IP address of a name server entry. Glue IP addresses are required only when the name of the name server is a subdomain of the domain. For example, if your domain is example.com and the name server for the domain is ns.example.com, you need to specify the IP address for ns.example.com.
            Constraints: The list can contain only one IPv4 and one IPv6 address.
            (string) --
            
            

    :rtype: dict
    :return: {
        'OperationId': 'string'
    }
    
    
    """
    pass

def update_tags_for_domain(DomainName=None, TagsToUpdate=None):
    """
    This operation adds or updates tags for a specified domain.
    All tag operations are eventually consistent; subsequent operations may not immediately represent all issued operations.
    See also: AWS API Documentation
    
    
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
    :param DomainName: [REQUIRED]
            The domain for which you want to add or update tags.
            

    :type TagsToUpdate: list
    :param TagsToUpdate: A list of the tag keys and values that you want to add or update. If you specify a key that already exists, the corresponding value will be replaced.
            (dict) --Each tag includes the following elements.
            Key (string) --The key (name) of a tag.
            Valid values: A-Z, a-z, 0-9, space, '.:/=+-@'
            Constraints: Each key can be 1-128 characters long.
            Value (string) --The value of a tag.
            Valid values: A-Z, a-z, 0-9, space, '.:/=+-@'
            Constraints: Each value can be 0-256 characters long.
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def view_billing(Start=None, End=None, Marker=None, MaxItems=None):
    """
    Returns all the domain-related billing records for the current AWS account for a specified period
    See also: AWS API Documentation
    
    
    :example: response = client.view_billing(
        Start=datetime(2015, 1, 1),
        End=datetime(2015, 1, 1),
        Marker='string',
        MaxItems=123
    )
    
    
    :type Start: datetime
    :param Start: The beginning date and time for the time period for which you want a list of billing records. Specify the date in Unix time format.

    :type End: datetime
    :param End: The end date and time for the time period for which you want a list of billing records. Specify the date in Unix time format.

    :type Marker: string
    :param Marker: For an initial request for a list of billing records, omit this element. If the number of billing records that are associated with the current AWS account during the specified period is greater than the value that you specified for MaxItems , you can use Marker to return additional billing records. Get the value of NextPageMarker from the previous response, and submit another request that includes the value of NextPageMarker in the Marker element.
            Constraints: The marker must match the value of NextPageMarker that was returned in the previous response.
            

    :type MaxItems: integer
    :param MaxItems: The number of billing records to be returned.
            Default: 20
            

    :rtype: dict
    :return: {
        'NextPageMarker': 'string',
        'BillingRecords': [
            {
                'DomainName': 'string',
                'Operation': 'REGISTER_DOMAIN'|'DELETE_DOMAIN'|'TRANSFER_IN_DOMAIN'|'UPDATE_DOMAIN_CONTACT'|'UPDATE_NAMESERVER'|'CHANGE_PRIVACY_PROTECTION'|'DOMAIN_LOCK',
                'InvoiceId': 'string',
                'BillDate': datetime(2015, 1, 1),
                'Price': 123.0
            },
        ]
    }
    
    
    """
    pass

