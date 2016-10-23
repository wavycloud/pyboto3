"""
The MIT License (MIT)

Copyright (c) 2016 Gehad Shaat

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
"""


def can_paginate(operation_name=None):
    """
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').
            ReturnsTrue if the operation can be paginated,
            False otherwise.
            
    :type operation_name: string
    """
    pass


def check_domain_availability(DomainName=None, IdnLangCode=None):
    """
    :param DomainName: [REQUIRED]
            The name of a domain.
            Type: String
            Default: None
            Constraints: The domain name can contain only the letters a through z, the numbers 0 through 9, and hyphen (-). Internationalized Domain Names are not supported.
            Required: Yes
            
    :type DomainName: string
    :param IdnLangCode: Reserved for future use.
    :type IdnLangCode: string
    """
    pass


def delete_tags_for_domain(DomainName=None, TagsToDelete=None):
    """
    :param DomainName: [REQUIRED]
            The domain for which you want to delete one or more tags.
            The name of a domain.
            Type: String
            Default: None
            Constraints: The domain name can contain only the letters a through z, the numbers 0 through 9, and hyphen (-). Hyphens are allowed only when theyre surrounded by letters, numbers, or other hyphens. You cant specify a hyphen at the beginning or end of a label. To specify an Internationalized Domain Name, you must convert the name to Punycode.
            Required: Yes
            
    :type DomainName: string
    :param TagsToDelete: [REQUIRED]
            A list of tag keys to delete.
            Type: A list that contains the keys of the tags that you want to delete.
            Default: None
            Required: No
            '>
            (string) --
            
    :type TagsToDelete: list
    """
    pass


def disable_domain_auto_renew(DomainName=None):
    """
    :param DomainName: [REQUIRED]
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --
            
    :type DomainName: string
    """
    pass


def disable_domain_transfer_lock(DomainName=None):
    """
    :param DomainName: [REQUIRED]
            The name of a domain.
            Type: String
            Default: None
            Constraints: The domain name can contain only the letters a through z, the numbers 0 through 9, and hyphen (-). Internationalized Domain Names are not supported.
            Required: Yes
            Return typedict
            ReturnsResponse Syntax{
              'OperationId': 'string'
            }
            Response Structure
            (dict) --The DisableDomainTransferLock response includes the following element.
            OperationId (string) --Identifier for tracking the progress of the request. To use this ID to query the operation status, use GetOperationDetail.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            
            
    :type DomainName: string
    """
    pass


def enable_domain_auto_renew(DomainName=None):
    """
    :param DomainName: [REQUIRED]
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --
            
    :type DomainName: string
    """
    pass


def enable_domain_transfer_lock(DomainName=None):
    """
    :param DomainName: [REQUIRED]
            The name of a domain.
            Type: String
            Default: None
            Constraints: The domain name can contain only the letters a through z, the numbers 0 through 9, and hyphen (-). Internationalized Domain Names are not supported.
            Required: Yes
            Return typedict
            ReturnsResponse Syntax{
              'OperationId': 'string'
            }
            Response Structure
            (dict) --The EnableDomainTransferLock response includes the following elements.
            OperationId (string) --Identifier for tracking the progress of the request. To use this ID to query the operation status, use GetOperationDetail.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            
            
    :type DomainName: string
    """
    pass


def generate_presigned_url(ClientMethod=None, Params=None, ExpiresIn=None, HttpMethod=None):
    """
    :param ClientMethod: The client method to presign for
    :type ClientMethod: string
    :param Params: The parameters normally passed to
            ClientMethod.
    :type Params: dict
    :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)
    :type ExpiresIn: int
    :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method's model.
    :type HttpMethod: string
    """
    pass


def get_contact_reachability_status(domainName=None):
    """
    :param domainName: The name of the domain for which you want to know whether the registrant contact has confirmed that the email address is valid.
            Type: String
            Default: None
            Required: Yes
            Return typedict
            ReturnsResponse Syntax{
              'domainName': 'string',
              'status': 'PENDING'|'DONE'|'EXPIRED'
            }
            Response Structure
            (dict) --
            domainName (string) --The domain name for which you requested the reachability status.
            status (string) --Whether the registrant contact has responded. PENDING indicates that we sent the confirmation email and haven't received a response yet, DONE indicates that we sent the email and got confirmation from the registrant contact, and EXPIRED indicates that the time limit expired before the registrant contact responded.
            Type: String
            Valid values: PENDING , DONE , EXPIRED
            
            
    :type domainName: string
    """
    pass


def get_domain_detail(DomainName=None):
    """
    :param DomainName: [REQUIRED]
            The name of a domain.
            Type: String
            Default: None
            Constraints: The domain name can contain only the letters a through z, the numbers 0 through 9, and hyphen (-). Internationalized Domain Names are not supported.
            Required: Yes
            Return typedict
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
            Response Structure
            (dict) --The GetDomainDetail response includes the following elements.
            DomainName (string) --The name of a domain.
            Type: String
            Nameservers (list) --The name of the domain.
            Type: String
            (dict) --Nameserver includes the following elements.
            Name (string) --The fully qualified host name of the name server.
            Type: String
            Constraint: Maximum 255 characterss
            Parent: Nameservers
            GlueIps (list) --Glue IP address of a name server entry. Glue IP addresses are required only when the name of the name server is a subdomain of the domain. For example, if your domain is example.com and the name server for the domain is ns.example.com, you need to specify the IP address for ns.example.com.
            Type: List of IP addresses.
            Constraints: The list can contain only one IPv4 and one IPv6 address.
            Parent: Nameservers
            (string) --
            
            AutoRenew (boolean) --Specifies whether the domain registration is set to renew automatically.
            Type: Boolean
            AdminContact (dict) --Provides details about the domain administrative contact.
            Type: Complex
            Children: FirstName , MiddleName , LastName , ContactType , OrganizationName , AddressLine1 , AddressLine2 , City , State , CountryCode , ZipCode , PhoneNumber , Email , Fax , ExtraParams
            FirstName (string) --First name of contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            LastName (string) --Last name of contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            ContactType (string) --Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than PERSON , you must enter an organization name, and you cant enable privacy protection for the contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Valid values: PERSON | COMPANY | ASSOCIATION | PUBLIC_BODY
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            OrganizationName (string) --Name of the organization for contact types other than PERSON .
            Type: String
            Default: None
            Constraints: Maximum 255 characters. Contact type must not be PERSON .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            AddressLine1 (string) --First line of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            AddressLine2 (string) --Second line of contacts address, if any.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            City (string) --The city of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            State (string) --The state or province of the contacts city.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            CountryCode (string) --Code for the country of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            ZipCode (string) --The zip or postal code of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            PhoneNumber (string) --The phone number of the contact.
            Type: String
            Default: None
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code>]'. For example, a US phone number might appear as '+1.1234567890' .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            Email (string) --Email address of the contact.
            Type: String
            Default: None
            Constraints: Maximum 254 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            Fax (string) --Fax number of the contact.
            Type: String
            Default: None
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            ExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.
            Type: Complex
            Default: None
            Parents: RegistrantContact , AdminContact , TechContact
            Children: Name , Value
            Required: No
            (dict) --ExtraParam includes the following elements.
            Name (string) --Name of the additional parameter required by the top-level domain.
            Type: String
            Default: None
            Valid values: DUNS_NUMBER | BRAND_NUMBER | BIRTH_DEPARTMENT | BIRTH_DATE_IN_YYYY_MM_DD | BIRTH_COUNTRY | BIRTH_CITY | DOCUMENT_NUMBER | AU_ID_NUMBER | AU_ID_TYPE | CA_LEGAL_TYPE | CA_BUSINESS_ENTITY_TYPE |ES_IDENTIFICATION | ES_IDENTIFICATION_TYPE | ES_LEGAL_FORM | FI_BUSINESS_NUMBER | FI_ID_NUMBER | IT_PIN | RU_PASSPORT_DATA | SE_ID_NUMBER | SG_ID_NUMBER | VAT_NUMBER
            Parent: ExtraParams
            Required: Yes
            Value (string) --Values corresponding to the additional parameter names required by some top-level domains.
            Type: String
            Default: None
            Constraints: Maximum 2048 characters.
            Parent: ExtraParams
            Required: Yes
            
            RegistrantContact (dict) --Provides details about the domain registrant.
            Type: Complex
            Children: FirstName , MiddleName , LastName , ContactType , OrganizationName , AddressLine1 , AddressLine2 , City , State , CountryCode , ZipCode , PhoneNumber , Email , Fax , ExtraParams
            FirstName (string) --First name of contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            LastName (string) --Last name of contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            ContactType (string) --Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than PERSON , you must enter an organization name, and you cant enable privacy protection for the contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Valid values: PERSON | COMPANY | ASSOCIATION | PUBLIC_BODY
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            OrganizationName (string) --Name of the organization for contact types other than PERSON .
            Type: String
            Default: None
            Constraints: Maximum 255 characters. Contact type must not be PERSON .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            AddressLine1 (string) --First line of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            AddressLine2 (string) --Second line of contacts address, if any.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            City (string) --The city of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            State (string) --The state or province of the contacts city.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            CountryCode (string) --Code for the country of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            ZipCode (string) --The zip or postal code of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            PhoneNumber (string) --The phone number of the contact.
            Type: String
            Default: None
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code>]'. For example, a US phone number might appear as '+1.1234567890' .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            Email (string) --Email address of the contact.
            Type: String
            Default: None
            Constraints: Maximum 254 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            Fax (string) --Fax number of the contact.
            Type: String
            Default: None
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            ExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.
            Type: Complex
            Default: None
            Parents: RegistrantContact , AdminContact , TechContact
            Children: Name , Value
            Required: No
            (dict) --ExtraParam includes the following elements.
            Name (string) --Name of the additional parameter required by the top-level domain.
            Type: String
            Default: None
            Valid values: DUNS_NUMBER | BRAND_NUMBER | BIRTH_DEPARTMENT | BIRTH_DATE_IN_YYYY_MM_DD | BIRTH_COUNTRY | BIRTH_CITY | DOCUMENT_NUMBER | AU_ID_NUMBER | AU_ID_TYPE | CA_LEGAL_TYPE | CA_BUSINESS_ENTITY_TYPE |ES_IDENTIFICATION | ES_IDENTIFICATION_TYPE | ES_LEGAL_FORM | FI_BUSINESS_NUMBER | FI_ID_NUMBER | IT_PIN | RU_PASSPORT_DATA | SE_ID_NUMBER | SG_ID_NUMBER | VAT_NUMBER
            Parent: ExtraParams
            Required: Yes
            Value (string) --Values corresponding to the additional parameter names required by some top-level domains.
            Type: String
            Default: None
            Constraints: Maximum 2048 characters.
            Parent: ExtraParams
            Required: Yes
            
            TechContact (dict) --Provides details about the domain technical contact.
            Type: Complex
            Children: FirstName , MiddleName , LastName , ContactType , OrganizationName , AddressLine1 , AddressLine2 , City , State , CountryCode , ZipCode , PhoneNumber , Email , Fax , ExtraParams
            FirstName (string) --First name of contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            LastName (string) --Last name of contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            ContactType (string) --Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than PERSON , you must enter an organization name, and you cant enable privacy protection for the contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Valid values: PERSON | COMPANY | ASSOCIATION | PUBLIC_BODY
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            OrganizationName (string) --Name of the organization for contact types other than PERSON .
            Type: String
            Default: None
            Constraints: Maximum 255 characters. Contact type must not be PERSON .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            AddressLine1 (string) --First line of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            AddressLine2 (string) --Second line of contacts address, if any.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            City (string) --The city of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            State (string) --The state or province of the contacts city.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            CountryCode (string) --Code for the country of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            ZipCode (string) --The zip or postal code of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            PhoneNumber (string) --The phone number of the contact.
            Type: String
            Default: None
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code>]'. For example, a US phone number might appear as '+1.1234567890' .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            Email (string) --Email address of the contact.
            Type: String
            Default: None
            Constraints: Maximum 254 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            Fax (string) --Fax number of the contact.
            Type: String
            Default: None
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            ExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.
            Type: Complex
            Default: None
            Parents: RegistrantContact , AdminContact , TechContact
            Children: Name , Value
            Required: No
            (dict) --ExtraParam includes the following elements.
            Name (string) --Name of the additional parameter required by the top-level domain.
            Type: String
            Default: None
            Valid values: DUNS_NUMBER | BRAND_NUMBER | BIRTH_DEPARTMENT | BIRTH_DATE_IN_YYYY_MM_DD | BIRTH_COUNTRY | BIRTH_CITY | DOCUMENT_NUMBER | AU_ID_NUMBER | AU_ID_TYPE | CA_LEGAL_TYPE | CA_BUSINESS_ENTITY_TYPE |ES_IDENTIFICATION | ES_IDENTIFICATION_TYPE | ES_LEGAL_FORM | FI_BUSINESS_NUMBER | FI_ID_NUMBER | IT_PIN | RU_PASSPORT_DATA | SE_ID_NUMBER | SG_ID_NUMBER | VAT_NUMBER
            Parent: ExtraParams
            Required: Yes
            Value (string) --Values corresponding to the additional parameter names required by some top-level domains.
            Type: String
            Default: None
            Constraints: Maximum 2048 characters.
            Parent: ExtraParams
            Required: Yes
            
            AdminPrivacy (boolean) --Specifies whether contact information for the admin contact is concealed from WHOIS queries. If the value is true , WHOIS ('who is') queries will return contact information for our registrar partner, Gandi, instead of the contact information that you enter.
            Type: Boolean
            RegistrantPrivacy (boolean) --Specifies whether contact information for the registrant contact is concealed from WHOIS queries. If the value is true , WHOIS ('who is') queries will return contact information for our registrar partner, Gandi, instead of the contact information that you enter.
            Type: Boolean
            TechPrivacy (boolean) --Specifies whether contact information for the tech contact is concealed from WHOIS queries. If the value is true , WHOIS ('who is') queries will return contact information for our registrar partner, Gandi, instead of the contact information that you enter.
            Type: Boolean
            RegistrarName (string) --Name of the registrar of the domain as identified in the registry. Amazon Route 53 domains are registered by registrar Gandi. The value is 'GANDI SAS' .
            Type: String
            WhoIsServer (string) --The fully qualified name of the WHOIS server that can answer the WHOIS query for the domain.
            Type: String
            RegistrarUrl (string) --Web address of the registrar.
            Type: String
            AbuseContactEmail (string) --Email address to contact to report incorrect contact information for a domain, to report that the domain is being used to send spam, to report that someone is cybersquatting on a domain name, or report some other type of abuse.
            Type: String
            AbuseContactPhone (string) --Phone number for reporting abuse.
            Type: String
            RegistryDomainId (string) --Reserved for future use.
            CreationDate (datetime) --The date when the domain was created as found in the response to a WHOIS query. The date format is Unix time.
            UpdatedDate (datetime) --The last updated date of the domain as found in the response to a WHOIS query. The date format is Unix time.
            ExpirationDate (datetime) --The date when the registration for the domain is set to expire. The date format is Unix time.
            Reseller (string) --Reseller of the domain. Domains registered or transferred using Amazon Route 53 domains will have 'Amazon' as the reseller.
            Type: String
            DnsSec (string) --Reserved for future use.
            StatusList (list) --An array of domain name status codes, also known as Extensible Provisioning Protocol (EPP) status codes.
            ICANN, the organization that maintains a central database of domain names, has developed a set of domain name status codes that tell you the status of a variety of operations on a domain name, for example, registering a domain name, transferring a domain name to another registrar, renewing the registration for a domain name, and so on. All registrars use this same set of status codes.
            For a current list of domain name status codes and an explanation of what each code means, go to the ICANN website and search for epp status codes . (Search on the ICANN website; web searches sometimes return an old version of the document.)
            Type: Array of String
            (string) --
            
            
    :type DomainName: string
    """
    pass


def get_domain_suggestions(DomainName=None, SuggestionCount=None, OnlyAvailable=None):
    """
    :param DomainName: [REQUIRED]
    :type DomainName: string
    :param SuggestionCount: [REQUIRED]
    :type SuggestionCount: integer
    :param OnlyAvailable: [REQUIRED]
    :type OnlyAvailable: boolean
    """
    pass


def get_operation_detail(OperationId=None):
    """
    :param OperationId: [REQUIRED]
            The identifier for the operation for which you want to get the status. Amazon Route 53 returned the identifier in the response to the original request.
            Type: String
            Default: None
            Required: Yes
            Return typedict
            ReturnsResponse Syntax{
              'OperationId': 'string',
              'Status': 'SUBMITTED'|'IN_PROGRESS'|'ERROR'|'SUCCESSFUL'|'FAILED',
              'Message': 'string',
              'DomainName': 'string',
              'Type': 'REGISTER_DOMAIN'|'DELETE_DOMAIN'|'TRANSFER_IN_DOMAIN'|'UPDATE_DOMAIN_CONTACT'|'UPDATE_NAMESERVER'|'CHANGE_PRIVACY_PROTECTION'|'DOMAIN_LOCK',
              'SubmittedDate': datetime(2015, 1, 1)
            }
            Response Structure
            (dict) --The GetOperationDetail response includes the following elements.
            OperationId (string) --The identifier for the operation.
            Type: String
            Status (string) --The current status of the requested operation in the system.
            Type: String
            Message (string) --Detailed information on the status including possible errors.
            Type: String
            DomainName (string) --The name of a domain.
            Type: String
            Type (string) --The type of operation that was requested.
            Type: String
            SubmittedDate (datetime) --The date when the request was submitted.
            
            
    :type OperationId: string
    """
    pass


def get_paginator(operation_name=None):
    """
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').
            Raises OperationNotPageableErrorRaised if the operation is not
            pageable. You can use the client.can_paginate method to
            check if an operation is pageable.
            Return typeL{botocore.paginate.Paginator}
            ReturnsA paginator object.
            
    :type operation_name: string
    """
    pass


def get_waiter():
    """
    """
    pass


def list_domains(Marker=None, MaxItems=None):
    """
    :param Marker: For an initial request for a list of domains, omit this element. If the number of domains that are associated with the current AWS account is greater than the value that you specified for MaxItems , you can use Marker to return additional domains. Get the value of NextPageMarker from the previous response, and submit another request that includes the value of NextPageMarker in the Marker element.
            Type: String
            Default: None
            Constraints: The marker must match the value specified in the previous request.
            Required: No
            
    :type Marker: string
    :param MaxItems: Number of domains to be returned.
            Type: Integer
            Default: 20
            Constraints: A numeral between 1 and 100.
            Required: No
            
    :type MaxItems: integer
    """
    pass


def list_operations(Marker=None, MaxItems=None):
    """
    :param Marker: For an initial request for a list of operations, omit this element. If the number of operations that are not yet complete is greater than the value that you specified for MaxItems , you can use Marker to return additional operations. Get the value of NextPageMarker from the previous response, and submit another request that includes the value of NextPageMarker in the Marker element.
            Type: String
            Default: None
            Required: No
            
    :type Marker: string
    :param MaxItems: Number of domains to be returned.
            Type: Integer
            Default: 20
            Constraints: A value between 1 and 100.
            Required: No
            
    :type MaxItems: integer
    """
    pass


def list_tags_for_domain(DomainName=None):
    """
    :param DomainName: [REQUIRED]
            The domain for which you want to get a list of tags.
            Return typedict
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
            Type: A complex type containing a list of tags
            Each tag includes the following elements.
            Key The key (name) of a tag. Type: String
            Value The value of a tag. Type: String
            (dict) --Each tag includes the following elements.
            Key (string) --The key (name) of a tag.
            Type: String
            Default: None
            Valid values: A-Z, a-z, 0-9, space, '.:/=+-@'
            Constraints: Each key can be 1-128 characters long.
            Required: Yes
            Value (string) --The value of a tag.
            Type: String
            Default: None
            Valid values: A-Z, a-z, 0-9, space, '.:/=+-@'
            Constraints: Each value can be 0-256 characters long.
            Required: Yes
            
            
            
    :type DomainName: string
    """
    pass


def register_domain(DomainName=None, IdnLangCode=None, DurationInYears=None, AutoRenew=None, AdminContact=None,
                    RegistrantContact=None, TechContact=None, PrivacyProtectAdminContact=None,
                    PrivacyProtectRegistrantContact=None, PrivacyProtectTechContact=None):
    """
    :param DomainName: [REQUIRED]
            The name of a domain.
            Type: String
            Default: None
            Constraints: The domain name can contain only the letters a through z, the numbers 0 through 9, and hyphen (-). Internationalized Domain Names are not supported.
            Required: Yes
            
    :type DomainName: string
    :param IdnLangCode: Reserved for future use.
    :type IdnLangCode: string
    :param DurationInYears: [REQUIRED]
            The number of years the domain will be registered. Domains are registered for a minimum of one year. The maximum period depends on the top-level domain.
            Type: Integer
            Default: 1
            Valid values: Integer from 1 to 10
            Required: Yes
            
    :type DurationInYears: integer
    :param AutoRenew: Indicates whether the domain will be automatically renewed (true ) or not (false ). Autorenewal only takes effect after the account is charged.
            Type: Boolean
            Valid values: true | false
            Default: true
            Required: No
            
    :type AutoRenew: boolean
    :param AdminContact: [REQUIRED]
            Provides detailed contact information.
            Type: Complex
            Children: FirstName , MiddleName , LastName , ContactType , OrganizationName , AddressLine1 , AddressLine2 , City , State , CountryCode , ZipCode , PhoneNumber , Email , Fax , ExtraParams
            Required: Yes
            FirstName (string) --First name of contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            LastName (string) --Last name of contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            ContactType (string) --Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than PERSON , you must enter an organization name, and you cant enable privacy protection for the contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Valid values: PERSON | COMPANY | ASSOCIATION | PUBLIC_BODY
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            OrganizationName (string) --Name of the organization for contact types other than PERSON .
            Type: String
            Default: None
            Constraints: Maximum 255 characters. Contact type must not be PERSON .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            AddressLine1 (string) --First line of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            AddressLine2 (string) --Second line of contacts address, if any.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            City (string) --The city of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            State (string) --The state or province of the contacts city.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            CountryCode (string) --Code for the country of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            ZipCode (string) --The zip or postal code of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            PhoneNumber (string) --The phone number of the contact.
            Type: String
            Default: None
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code>]'. For example, a US phone number might appear as '+1.1234567890' .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            Email (string) --Email address of the contact.
            Type: String
            Default: None
            Constraints: Maximum 254 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            Fax (string) --Fax number of the contact.
            Type: String
            Default: None
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            ExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.
            Type: Complex
            Default: None
            Parents: RegistrantContact , AdminContact , TechContact
            Children: Name , Value
            Required: No
            (dict) --ExtraParam includes the following elements.
            Name (string) -- [REQUIRED]Name of the additional parameter required by the top-level domain.
            Type: String
            Default: None
            Valid values: DUNS_NUMBER | BRAND_NUMBER | BIRTH_DEPARTMENT | BIRTH_DATE_IN_YYYY_MM_DD | BIRTH_COUNTRY | BIRTH_CITY | DOCUMENT_NUMBER | AU_ID_NUMBER | AU_ID_TYPE | CA_LEGAL_TYPE | CA_BUSINESS_ENTITY_TYPE |ES_IDENTIFICATION | ES_IDENTIFICATION_TYPE | ES_LEGAL_FORM | FI_BUSINESS_NUMBER | FI_ID_NUMBER | IT_PIN | RU_PASSPORT_DATA | SE_ID_NUMBER | SG_ID_NUMBER | VAT_NUMBER
            Parent: ExtraParams
            Required: Yes
            Value (string) -- [REQUIRED]Values corresponding to the additional parameter names required by some top-level domains.
            Type: String
            Default: None
            Constraints: Maximum 2048 characters.
            Parent: ExtraParams
            Required: Yes
            
            
    :type AdminContact: dict
    :param RegistrantContact: [REQUIRED]
            Provides detailed contact information.
            Type: Complex
            Children: FirstName , MiddleName , LastName , ContactType , OrganizationName , AddressLine1 , AddressLine2 , City , State , CountryCode , ZipCode , PhoneNumber , Email , Fax , ExtraParams
            Required: Yes
            FirstName (string) --First name of contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            LastName (string) --Last name of contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            ContactType (string) --Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than PERSON , you must enter an organization name, and you cant enable privacy protection for the contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Valid values: PERSON | COMPANY | ASSOCIATION | PUBLIC_BODY
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            OrganizationName (string) --Name of the organization for contact types other than PERSON .
            Type: String
            Default: None
            Constraints: Maximum 255 characters. Contact type must not be PERSON .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            AddressLine1 (string) --First line of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            AddressLine2 (string) --Second line of contacts address, if any.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            City (string) --The city of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            State (string) --The state or province of the contacts city.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            CountryCode (string) --Code for the country of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            ZipCode (string) --The zip or postal code of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            PhoneNumber (string) --The phone number of the contact.
            Type: String
            Default: None
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code>]'. For example, a US phone number might appear as '+1.1234567890' .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            Email (string) --Email address of the contact.
            Type: String
            Default: None
            Constraints: Maximum 254 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            Fax (string) --Fax number of the contact.
            Type: String
            Default: None
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            ExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.
            Type: Complex
            Default: None
            Parents: RegistrantContact , AdminContact , TechContact
            Children: Name , Value
            Required: No
            (dict) --ExtraParam includes the following elements.
            Name (string) -- [REQUIRED]Name of the additional parameter required by the top-level domain.
            Type: String
            Default: None
            Valid values: DUNS_NUMBER | BRAND_NUMBER | BIRTH_DEPARTMENT | BIRTH_DATE_IN_YYYY_MM_DD | BIRTH_COUNTRY | BIRTH_CITY | DOCUMENT_NUMBER | AU_ID_NUMBER | AU_ID_TYPE | CA_LEGAL_TYPE | CA_BUSINESS_ENTITY_TYPE |ES_IDENTIFICATION | ES_IDENTIFICATION_TYPE | ES_LEGAL_FORM | FI_BUSINESS_NUMBER | FI_ID_NUMBER | IT_PIN | RU_PASSPORT_DATA | SE_ID_NUMBER | SG_ID_NUMBER | VAT_NUMBER
            Parent: ExtraParams
            Required: Yes
            Value (string) -- [REQUIRED]Values corresponding to the additional parameter names required by some top-level domains.
            Type: String
            Default: None
            Constraints: Maximum 2048 characters.
            Parent: ExtraParams
            Required: Yes
            
            
    :type RegistrantContact: dict
    :param TechContact: [REQUIRED]
            Provides detailed contact information.
            Type: Complex
            Children: FirstName , MiddleName , LastName , ContactType , OrganizationName , AddressLine1 , AddressLine2 , City , State , CountryCode , ZipCode , PhoneNumber , Email , Fax , ExtraParams
            Required: Yes
            FirstName (string) --First name of contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            LastName (string) --Last name of contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            ContactType (string) --Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than PERSON , you must enter an organization name, and you cant enable privacy protection for the contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Valid values: PERSON | COMPANY | ASSOCIATION | PUBLIC_BODY
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            OrganizationName (string) --Name of the organization for contact types other than PERSON .
            Type: String
            Default: None
            Constraints: Maximum 255 characters. Contact type must not be PERSON .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            AddressLine1 (string) --First line of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            AddressLine2 (string) --Second line of contacts address, if any.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            City (string) --The city of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            State (string) --The state or province of the contacts city.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            CountryCode (string) --Code for the country of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            ZipCode (string) --The zip or postal code of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            PhoneNumber (string) --The phone number of the contact.
            Type: String
            Default: None
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code>]'. For example, a US phone number might appear as '+1.1234567890' .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            Email (string) --Email address of the contact.
            Type: String
            Default: None
            Constraints: Maximum 254 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            Fax (string) --Fax number of the contact.
            Type: String
            Default: None
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            ExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.
            Type: Complex
            Default: None
            Parents: RegistrantContact , AdminContact , TechContact
            Children: Name , Value
            Required: No
            (dict) --ExtraParam includes the following elements.
            Name (string) -- [REQUIRED]Name of the additional parameter required by the top-level domain.
            Type: String
            Default: None
            Valid values: DUNS_NUMBER | BRAND_NUMBER | BIRTH_DEPARTMENT | BIRTH_DATE_IN_YYYY_MM_DD | BIRTH_COUNTRY | BIRTH_CITY | DOCUMENT_NUMBER | AU_ID_NUMBER | AU_ID_TYPE | CA_LEGAL_TYPE | CA_BUSINESS_ENTITY_TYPE |ES_IDENTIFICATION | ES_IDENTIFICATION_TYPE | ES_LEGAL_FORM | FI_BUSINESS_NUMBER | FI_ID_NUMBER | IT_PIN | RU_PASSPORT_DATA | SE_ID_NUMBER | SG_ID_NUMBER | VAT_NUMBER
            Parent: ExtraParams
            Required: Yes
            Value (string) -- [REQUIRED]Values corresponding to the additional parameter names required by some top-level domains.
            Type: String
            Default: None
            Constraints: Maximum 2048 characters.
            Parent: ExtraParams
            Required: Yes
            
            
    :type TechContact: dict
    :param PrivacyProtectAdminContact: Whether you want to conceal contact information from WHOIS queries. If you specify true, WHOIS ('who is') queries will return contact information for our registrar partner, Gandi, instead of the contact information that you enter.
            Type: Boolean
            Default: true
            Valid values: true | false
            Required: No
            
    :type PrivacyProtectAdminContact: boolean
    :param PrivacyProtectRegistrantContact: Whether you want to conceal contact information from WHOIS queries. If you specify true, WHOIS ('who is') queries will return contact information for our registrar partner, Gandi, instead of the contact information that you enter.
            Type: Boolean
            Default: true
            Valid values: true | false
            Required: No
            
    :type PrivacyProtectRegistrantContact: boolean
    :param PrivacyProtectTechContact: Whether you want to conceal contact information from WHOIS queries. If you specify true, WHOIS ('who is') queries will return contact information for our registrar partner, Gandi, instead of the contact information that you enter.
            Type: Boolean
            Default: true
            Valid values: true | false
            Required: No
            
    :type PrivacyProtectTechContact: boolean
    """
    pass


def renew_domain(DomainName=None, DurationInYears=None, CurrentExpiryYear=None):
    """
    :param DomainName: [REQUIRED]
    :type DomainName: string
    :param DurationInYears: The number of years that you want to renew the domain for. The maximum number of years depends on the top-level domain. For the range of valid values for your domain, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 documentation.
            Type: Integer
            Default: 1
            Valid values: Integer from 1 to 10
            Required: No
            
    :type DurationInYears: integer
    :param CurrentExpiryYear: [REQUIRED]
            The year when the registration for the domain is set to expire. This value must match the current expiration date for the domain.
            Type: Integer
            Default: None
            Valid values: Integer
            Required: Yes
            
    :type CurrentExpiryYear: integer
    """
    pass


def resend_contact_reachability_email(domainName=None):
    """
    :param domainName: The name of the domain for which you want Amazon Route 53 to resend a confirmation email to the registrant contact.
            Type: String
            Default: None
            Required: Yes
            Return typedict
            ReturnsResponse Syntax{
              'domainName': 'string',
              'emailAddress': 'string',
              'isAlreadyVerified': True|False
            }
            Response Structure
            (dict) --
            domainName (string) --The domain name for which you requested a confirmation email.
            emailAddress (string) --The email address for the registrant contact at the time that we sent the verification email.
            isAlreadyVerified (boolean) --True if the email address for the registrant contact has already been verified, and false otherwise. If the email address has already been verified, we don't send another confirmation email.
            
            
    :type domainName: string
    """
    pass


def retrieve_domain_auth_code(DomainName=None):
    """
    :param DomainName: [REQUIRED]
            The name of a domain.
            Type: String
            Default: None
            Constraints: The domain name can contain only the letters a through z, the numbers 0 through 9, and hyphen (-). Internationalized Domain Names are not supported.
            Required: Yes
            Return typedict
            ReturnsResponse Syntax{
              'AuthCode': 'string'
            }
            Response Structure
            (dict) --The RetrieveDomainAuthCode response includes the following element.
            AuthCode (string) --The authorization code for the domain.
            Type: String
            
            
    :type DomainName: string
    """
    pass


def transfer_domain(DomainName=None, IdnLangCode=None, DurationInYears=None, Nameservers=None, AuthCode=None,
                    AutoRenew=None, AdminContact=None, RegistrantContact=None, TechContact=None,
                    PrivacyProtectAdminContact=None, PrivacyProtectRegistrantContact=None,
                    PrivacyProtectTechContact=None):
    """
    :param DomainName: [REQUIRED]
            The name of a domain.
            Type: String
            Default: None
            Constraints: The domain name can contain only the letters a through z, the numbers 0 through 9, and hyphen (-). Internationalized Domain Names are not supported.
            Required: Yes
            
    :type DomainName: string
    :param IdnLangCode: Reserved for future use.
    :type IdnLangCode: string
    :param DurationInYears: [REQUIRED]
            The number of years the domain will be registered. Domains are registered for a minimum of one year. The maximum period depends on the top-level domain.
            Type: Integer
            Default: 1
            Valid values: Integer from 1 to 10
            Required: Yes
            
    :type DurationInYears: integer
    :param Nameservers: Contains details for the host and glue IP addresses.
            Type: Complex
            Children: GlueIps , Name
            Required: No
            (dict) --Nameserver includes the following elements.
            Name (string) -- [REQUIRED]The fully qualified host name of the name server.
            Type: String
            Constraint: Maximum 255 characterss
            Parent: Nameservers
            GlueIps (list) --Glue IP address of a name server entry. Glue IP addresses are required only when the name of the name server is a subdomain of the domain. For example, if your domain is example.com and the name server for the domain is ns.example.com, you need to specify the IP address for ns.example.com.
            Type: List of IP addresses.
            Constraints: The list can contain only one IPv4 and one IPv6 address.
            Parent: Nameservers
            (string) --
            
            
    :type Nameservers: list
    :param AuthCode: The authorization code for the domain. You get this value from the current registrar.
            Type: String
            Required: Yes
            
    :type AuthCode: string
    :param AutoRenew: Indicates whether the domain will be automatically renewed (true) or not (false). Autorenewal only takes effect after the account is charged.
            Type: Boolean
            Valid values: true | false
            Default: true
            Required: No
            
    :type AutoRenew: boolean
    :param AdminContact: [REQUIRED]
            Provides detailed contact information.
            Type: Complex
            Children: FirstName , MiddleName , LastName , ContactType , OrganizationName , AddressLine1 , AddressLine2 , City , State , CountryCode , ZipCode , PhoneNumber , Email , Fax , ExtraParams
            Required: Yes
            FirstName (string) --First name of contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            LastName (string) --Last name of contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            ContactType (string) --Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than PERSON , you must enter an organization name, and you cant enable privacy protection for the contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Valid values: PERSON | COMPANY | ASSOCIATION | PUBLIC_BODY
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            OrganizationName (string) --Name of the organization for contact types other than PERSON .
            Type: String
            Default: None
            Constraints: Maximum 255 characters. Contact type must not be PERSON .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            AddressLine1 (string) --First line of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            AddressLine2 (string) --Second line of contacts address, if any.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            City (string) --The city of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            State (string) --The state or province of the contacts city.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            CountryCode (string) --Code for the country of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            ZipCode (string) --The zip or postal code of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            PhoneNumber (string) --The phone number of the contact.
            Type: String
            Default: None
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code>]'. For example, a US phone number might appear as '+1.1234567890' .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            Email (string) --Email address of the contact.
            Type: String
            Default: None
            Constraints: Maximum 254 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            Fax (string) --Fax number of the contact.
            Type: String
            Default: None
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            ExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.
            Type: Complex
            Default: None
            Parents: RegistrantContact , AdminContact , TechContact
            Children: Name , Value
            Required: No
            (dict) --ExtraParam includes the following elements.
            Name (string) -- [REQUIRED]Name of the additional parameter required by the top-level domain.
            Type: String
            Default: None
            Valid values: DUNS_NUMBER | BRAND_NUMBER | BIRTH_DEPARTMENT | BIRTH_DATE_IN_YYYY_MM_DD | BIRTH_COUNTRY | BIRTH_CITY | DOCUMENT_NUMBER | AU_ID_NUMBER | AU_ID_TYPE | CA_LEGAL_TYPE | CA_BUSINESS_ENTITY_TYPE |ES_IDENTIFICATION | ES_IDENTIFICATION_TYPE | ES_LEGAL_FORM | FI_BUSINESS_NUMBER | FI_ID_NUMBER | IT_PIN | RU_PASSPORT_DATA | SE_ID_NUMBER | SG_ID_NUMBER | VAT_NUMBER
            Parent: ExtraParams
            Required: Yes
            Value (string) -- [REQUIRED]Values corresponding to the additional parameter names required by some top-level domains.
            Type: String
            Default: None
            Constraints: Maximum 2048 characters.
            Parent: ExtraParams
            Required: Yes
            
            
    :type AdminContact: dict
    :param RegistrantContact: [REQUIRED]
            Provides detailed contact information.
            Type: Complex
            Children: FirstName , MiddleName , LastName , ContactType , OrganizationName , AddressLine1 , AddressLine2 , City , State , CountryCode , ZipCode , PhoneNumber , Email , Fax , ExtraParams
            Required: Yes
            FirstName (string) --First name of contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            LastName (string) --Last name of contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            ContactType (string) --Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than PERSON , you must enter an organization name, and you cant enable privacy protection for the contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Valid values: PERSON | COMPANY | ASSOCIATION | PUBLIC_BODY
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            OrganizationName (string) --Name of the organization for contact types other than PERSON .
            Type: String
            Default: None
            Constraints: Maximum 255 characters. Contact type must not be PERSON .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            AddressLine1 (string) --First line of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            AddressLine2 (string) --Second line of contacts address, if any.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            City (string) --The city of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            State (string) --The state or province of the contacts city.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            CountryCode (string) --Code for the country of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            ZipCode (string) --The zip or postal code of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            PhoneNumber (string) --The phone number of the contact.
            Type: String
            Default: None
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code>]'. For example, a US phone number might appear as '+1.1234567890' .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            Email (string) --Email address of the contact.
            Type: String
            Default: None
            Constraints: Maximum 254 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            Fax (string) --Fax number of the contact.
            Type: String
            Default: None
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            ExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.
            Type: Complex
            Default: None
            Parents: RegistrantContact , AdminContact , TechContact
            Children: Name , Value
            Required: No
            (dict) --ExtraParam includes the following elements.
            Name (string) -- [REQUIRED]Name of the additional parameter required by the top-level domain.
            Type: String
            Default: None
            Valid values: DUNS_NUMBER | BRAND_NUMBER | BIRTH_DEPARTMENT | BIRTH_DATE_IN_YYYY_MM_DD | BIRTH_COUNTRY | BIRTH_CITY | DOCUMENT_NUMBER | AU_ID_NUMBER | AU_ID_TYPE | CA_LEGAL_TYPE | CA_BUSINESS_ENTITY_TYPE |ES_IDENTIFICATION | ES_IDENTIFICATION_TYPE | ES_LEGAL_FORM | FI_BUSINESS_NUMBER | FI_ID_NUMBER | IT_PIN | RU_PASSPORT_DATA | SE_ID_NUMBER | SG_ID_NUMBER | VAT_NUMBER
            Parent: ExtraParams
            Required: Yes
            Value (string) -- [REQUIRED]Values corresponding to the additional parameter names required by some top-level domains.
            Type: String
            Default: None
            Constraints: Maximum 2048 characters.
            Parent: ExtraParams
            Required: Yes
            
            
    :type RegistrantContact: dict
    :param TechContact: [REQUIRED]
            Provides detailed contact information.
            Type: Complex
            Children: FirstName , MiddleName , LastName , ContactType , OrganizationName , AddressLine1 , AddressLine2 , City , State , CountryCode , ZipCode , PhoneNumber , Email , Fax , ExtraParams
            Required: Yes
            FirstName (string) --First name of contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            LastName (string) --Last name of contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            ContactType (string) --Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than PERSON , you must enter an organization name, and you cant enable privacy protection for the contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Valid values: PERSON | COMPANY | ASSOCIATION | PUBLIC_BODY
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            OrganizationName (string) --Name of the organization for contact types other than PERSON .
            Type: String
            Default: None
            Constraints: Maximum 255 characters. Contact type must not be PERSON .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            AddressLine1 (string) --First line of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            AddressLine2 (string) --Second line of contacts address, if any.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            City (string) --The city of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            State (string) --The state or province of the contacts city.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            CountryCode (string) --Code for the country of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            ZipCode (string) --The zip or postal code of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            PhoneNumber (string) --The phone number of the contact.
            Type: String
            Default: None
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code>]'. For example, a US phone number might appear as '+1.1234567890' .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            Email (string) --Email address of the contact.
            Type: String
            Default: None
            Constraints: Maximum 254 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            Fax (string) --Fax number of the contact.
            Type: String
            Default: None
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            ExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.
            Type: Complex
            Default: None
            Parents: RegistrantContact , AdminContact , TechContact
            Children: Name , Value
            Required: No
            (dict) --ExtraParam includes the following elements.
            Name (string) -- [REQUIRED]Name of the additional parameter required by the top-level domain.
            Type: String
            Default: None
            Valid values: DUNS_NUMBER | BRAND_NUMBER | BIRTH_DEPARTMENT | BIRTH_DATE_IN_YYYY_MM_DD | BIRTH_COUNTRY | BIRTH_CITY | DOCUMENT_NUMBER | AU_ID_NUMBER | AU_ID_TYPE | CA_LEGAL_TYPE | CA_BUSINESS_ENTITY_TYPE |ES_IDENTIFICATION | ES_IDENTIFICATION_TYPE | ES_LEGAL_FORM | FI_BUSINESS_NUMBER | FI_ID_NUMBER | IT_PIN | RU_PASSPORT_DATA | SE_ID_NUMBER | SG_ID_NUMBER | VAT_NUMBER
            Parent: ExtraParams
            Required: Yes
            Value (string) -- [REQUIRED]Values corresponding to the additional parameter names required by some top-level domains.
            Type: String
            Default: None
            Constraints: Maximum 2048 characters.
            Parent: ExtraParams
            Required: Yes
            
            
    :type TechContact: dict
    :param PrivacyProtectAdminContact: Whether you want to conceal contact information from WHOIS queries. If you specify true, WHOIS ('who is') queries will return contact information for our registrar partner, Gandi, instead of the contact information that you enter.
            Type: Boolean
            Default: true
            Valid values: true | false
            Required: No
            
    :type PrivacyProtectAdminContact: boolean
    :param PrivacyProtectRegistrantContact: Whether you want to conceal contact information from WHOIS queries. If you specify true, WHOIS ('who is') queries will return contact information for our registrar partner, Gandi, instead of the contact information that you enter.
            Type: Boolean
            Default: true
            Valid values: true | false
            Required: No
            
    :type PrivacyProtectRegistrantContact: boolean
    :param PrivacyProtectTechContact: Whether you want to conceal contact information from WHOIS queries. If you specify true, WHOIS ('who is') queries will return contact information for our registrar partner, Gandi, instead of the contact information that you enter.
            Type: Boolean
            Default: true
            Valid values: true | false
            Required: No
            
    :type PrivacyProtectTechContact: boolean
    """
    pass


def update_domain_contact(DomainName=None, AdminContact=None, RegistrantContact=None, TechContact=None):
    """
    :param DomainName: [REQUIRED]
            The name of a domain.
            Type: String
            Default: None
            Constraints: The domain name can contain only the letters a through z, the numbers 0 through 9, and hyphen (-). Internationalized Domain Names are not supported.
            Required: Yes
            
    :type DomainName: string
    :param AdminContact: Provides detailed contact information.
            Type: Complex
            Children: FirstName , MiddleName , LastName , ContactType , OrganizationName , AddressLine1 , AddressLine2 , City , State , CountryCode , ZipCode , PhoneNumber , Email , Fax , ExtraParams
            Required: Yes
            FirstName (string) --First name of contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            LastName (string) --Last name of contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            ContactType (string) --Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than PERSON , you must enter an organization name, and you cant enable privacy protection for the contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Valid values: PERSON | COMPANY | ASSOCIATION | PUBLIC_BODY
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            OrganizationName (string) --Name of the organization for contact types other than PERSON .
            Type: String
            Default: None
            Constraints: Maximum 255 characters. Contact type must not be PERSON .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            AddressLine1 (string) --First line of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            AddressLine2 (string) --Second line of contacts address, if any.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            City (string) --The city of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            State (string) --The state or province of the contacts city.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            CountryCode (string) --Code for the country of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            ZipCode (string) --The zip or postal code of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            PhoneNumber (string) --The phone number of the contact.
            Type: String
            Default: None
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code>]'. For example, a US phone number might appear as '+1.1234567890' .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            Email (string) --Email address of the contact.
            Type: String
            Default: None
            Constraints: Maximum 254 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            Fax (string) --Fax number of the contact.
            Type: String
            Default: None
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            ExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.
            Type: Complex
            Default: None
            Parents: RegistrantContact , AdminContact , TechContact
            Children: Name , Value
            Required: No
            (dict) --ExtraParam includes the following elements.
            Name (string) -- [REQUIRED]Name of the additional parameter required by the top-level domain.
            Type: String
            Default: None
            Valid values: DUNS_NUMBER | BRAND_NUMBER | BIRTH_DEPARTMENT | BIRTH_DATE_IN_YYYY_MM_DD | BIRTH_COUNTRY | BIRTH_CITY | DOCUMENT_NUMBER | AU_ID_NUMBER | AU_ID_TYPE | CA_LEGAL_TYPE | CA_BUSINESS_ENTITY_TYPE |ES_IDENTIFICATION | ES_IDENTIFICATION_TYPE | ES_LEGAL_FORM | FI_BUSINESS_NUMBER | FI_ID_NUMBER | IT_PIN | RU_PASSPORT_DATA | SE_ID_NUMBER | SG_ID_NUMBER | VAT_NUMBER
            Parent: ExtraParams
            Required: Yes
            Value (string) -- [REQUIRED]Values corresponding to the additional parameter names required by some top-level domains.
            Type: String
            Default: None
            Constraints: Maximum 2048 characters.
            Parent: ExtraParams
            Required: Yes
            
            
    :type AdminContact: dict
    :param RegistrantContact: Provides detailed contact information.
            Type: Complex
            Children: FirstName , MiddleName , LastName , ContactType , OrganizationName , AddressLine1 , AddressLine2 , City , State , CountryCode , ZipCode , PhoneNumber , Email , Fax , ExtraParams
            Required: Yes
            FirstName (string) --First name of contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            LastName (string) --Last name of contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            ContactType (string) --Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than PERSON , you must enter an organization name, and you cant enable privacy protection for the contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Valid values: PERSON | COMPANY | ASSOCIATION | PUBLIC_BODY
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            OrganizationName (string) --Name of the organization for contact types other than PERSON .
            Type: String
            Default: None
            Constraints: Maximum 255 characters. Contact type must not be PERSON .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            AddressLine1 (string) --First line of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            AddressLine2 (string) --Second line of contacts address, if any.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            City (string) --The city of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            State (string) --The state or province of the contacts city.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            CountryCode (string) --Code for the country of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            ZipCode (string) --The zip or postal code of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            PhoneNumber (string) --The phone number of the contact.
            Type: String
            Default: None
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code>]'. For example, a US phone number might appear as '+1.1234567890' .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            Email (string) --Email address of the contact.
            Type: String
            Default: None
            Constraints: Maximum 254 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            Fax (string) --Fax number of the contact.
            Type: String
            Default: None
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            ExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.
            Type: Complex
            Default: None
            Parents: RegistrantContact , AdminContact , TechContact
            Children: Name , Value
            Required: No
            (dict) --ExtraParam includes the following elements.
            Name (string) -- [REQUIRED]Name of the additional parameter required by the top-level domain.
            Type: String
            Default: None
            Valid values: DUNS_NUMBER | BRAND_NUMBER | BIRTH_DEPARTMENT | BIRTH_DATE_IN_YYYY_MM_DD | BIRTH_COUNTRY | BIRTH_CITY | DOCUMENT_NUMBER | AU_ID_NUMBER | AU_ID_TYPE | CA_LEGAL_TYPE | CA_BUSINESS_ENTITY_TYPE |ES_IDENTIFICATION | ES_IDENTIFICATION_TYPE | ES_LEGAL_FORM | FI_BUSINESS_NUMBER | FI_ID_NUMBER | IT_PIN | RU_PASSPORT_DATA | SE_ID_NUMBER | SG_ID_NUMBER | VAT_NUMBER
            Parent: ExtraParams
            Required: Yes
            Value (string) -- [REQUIRED]Values corresponding to the additional parameter names required by some top-level domains.
            Type: String
            Default: None
            Constraints: Maximum 2048 characters.
            Parent: ExtraParams
            Required: Yes
            
            
    :type RegistrantContact: dict
    :param TechContact: Provides detailed contact information.
            Type: Complex
            Children: FirstName , MiddleName , LastName , ContactType , OrganizationName , AddressLine1 , AddressLine2 , City , State , CountryCode , ZipCode , PhoneNumber , Email , Fax , ExtraParams
            Required: Yes
            FirstName (string) --First name of contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            LastName (string) --Last name of contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            ContactType (string) --Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than PERSON , you must enter an organization name, and you cant enable privacy protection for the contact.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Valid values: PERSON | COMPANY | ASSOCIATION | PUBLIC_BODY
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            OrganizationName (string) --Name of the organization for contact types other than PERSON .
            Type: String
            Default: None
            Constraints: Maximum 255 characters. Contact type must not be PERSON .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            AddressLine1 (string) --First line of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            AddressLine2 (string) --Second line of contacts address, if any.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            City (string) --The city of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            State (string) --The state or province of the contacts city.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            CountryCode (string) --Code for the country of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            ZipCode (string) --The zip or postal code of the contacts address.
            Type: String
            Default: None
            Constraints: Maximum 255 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            PhoneNumber (string) --The phone number of the contact.
            Type: String
            Default: None
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code>]'. For example, a US phone number might appear as '+1.1234567890' .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            Email (string) --Email address of the contact.
            Type: String
            Default: None
            Constraints: Maximum 254 characters.
            Parents: RegistrantContact , AdminContact , TechContact
            Required: Yes
            Fax (string) --Fax number of the contact.
            Type: String
            Default: None
            Constraints: Phone number must be specified in the format '+[country dialing code].[number including any area code]'. For example, a US phone number might appear as '+1.1234567890' .
            Parents: RegistrantContact , AdminContact , TechContact
            Required: No
            ExtraParams (list) --A list of name-value pairs for parameters required by certain top-level domains.
            Type: Complex
            Default: None
            Parents: RegistrantContact , AdminContact , TechContact
            Children: Name , Value
            Required: No
            (dict) --ExtraParam includes the following elements.
            Name (string) -- [REQUIRED]Name of the additional parameter required by the top-level domain.
            Type: String
            Default: None
            Valid values: DUNS_NUMBER | BRAND_NUMBER | BIRTH_DEPARTMENT | BIRTH_DATE_IN_YYYY_MM_DD | BIRTH_COUNTRY | BIRTH_CITY | DOCUMENT_NUMBER | AU_ID_NUMBER | AU_ID_TYPE | CA_LEGAL_TYPE | CA_BUSINESS_ENTITY_TYPE |ES_IDENTIFICATION | ES_IDENTIFICATION_TYPE | ES_LEGAL_FORM | FI_BUSINESS_NUMBER | FI_ID_NUMBER | IT_PIN | RU_PASSPORT_DATA | SE_ID_NUMBER | SG_ID_NUMBER | VAT_NUMBER
            Parent: ExtraParams
            Required: Yes
            Value (string) -- [REQUIRED]Values corresponding to the additional parameter names required by some top-level domains.
            Type: String
            Default: None
            Constraints: Maximum 2048 characters.
            Parent: ExtraParams
            Required: Yes
            
            
    :type TechContact: dict
    """
    pass


def update_domain_contact_privacy(DomainName=None, AdminPrivacy=None, RegistrantPrivacy=None, TechPrivacy=None):
    """
    :param DomainName: [REQUIRED]
            The name of a domain.
            Type: String
            Default: None
            Constraints: The domain name can contain only the letters a through z, the numbers 0 through 9, and hyphen (-). Internationalized Domain Names are not supported.
            Required: Yes
            
    :type DomainName: string
    :param AdminPrivacy: Whether you want to conceal contact information from WHOIS queries. If you specify true, WHOIS ('who is') queries will return contact information for our registrar partner, Gandi, instead of the contact information that you enter.
            Type: Boolean
            Default: None
            Valid values: true | false
            Required: No
            
    :type AdminPrivacy: boolean
    :param RegistrantPrivacy: Whether you want to conceal contact information from WHOIS queries. If you specify true, WHOIS ('who is') queries will return contact information for our registrar partner, Gandi, instead of the contact information that you enter.
            Type: Boolean
            Default: None
            Valid values: true | false
            Required: No
            
    :type RegistrantPrivacy: boolean
    :param TechPrivacy: Whether you want to conceal contact information from WHOIS queries. If you specify true, WHOIS ('who is') queries will return contact information for our registrar partner, Gandi, instead of the contact information that you enter.
            Type: Boolean
            Default: None
            Valid values: true | false
            Required: No
            
    :type TechPrivacy: boolean
    """
    pass


def update_domain_nameservers(DomainName=None, FIAuthKey=None, Nameservers=None):
    """
    :param DomainName: [REQUIRED]
            The name of a domain.
            Type: String
            Default: None
            Constraints: The domain name can contain only the letters a through z, the numbers 0 through 9, and hyphen (-). Internationalized Domain Names are not supported.
            Required: Yes
            
    :type DomainName: string
    :param FIAuthKey: The authorization key for .fi domains
    :type FIAuthKey: string
    :param Nameservers: [REQUIRED]
            A list of new name servers for the domain.
            Type: Complex
            Children: Name , GlueIps
            Required: Yes
            (dict) --Nameserver includes the following elements.
            Name (string) -- [REQUIRED]The fully qualified host name of the name server.
            Type: String
            Constraint: Maximum 255 characterss
            Parent: Nameservers
            GlueIps (list) --Glue IP address of a name server entry. Glue IP addresses are required only when the name of the name server is a subdomain of the domain. For example, if your domain is example.com and the name server for the domain is ns.example.com, you need to specify the IP address for ns.example.com.
            Type: List of IP addresses.
            Constraints: The list can contain only one IPv4 and one IPv6 address.
            Parent: Nameservers
            (string) --
            
            
    :type Nameservers: list
    """
    pass


def update_tags_for_domain(DomainName=None, TagsToUpdate=None):
    """
    :param DomainName: [REQUIRED]
            The domain for which you want to add or update tags.
            The name of a domain.
            Type: String
            Default: None
            Constraints: The domain name can contain only the letters a through z, the numbers 0 through 9, and hyphen (-). Hyphens are allowed only when theyre surrounded by letters, numbers, or other hyphens. You cant specify a hyphen at the beginning or end of a label. To specify an Internationalized Domain Name, you must convert the name to Punycode.
            Required: Yes
            
    :type DomainName: string
    :param TagsToUpdate: A list of the tag keys and values that you want to add or update. If you specify a key that already exists, the corresponding value will be replaced.
            Type: A complex type containing a list of tags
            Default: None
            Required: No
            '>
            Each tag includes the following elements:
            Key The key (name) of a tag. Type: String Default: None Valid values: Unicode characters including alphanumeric, space, and '.:/=+-@' Constraints: Each key can be 1-128 characters long. Required: Yes
            Value The value of a tag. Type: String Default: None Valid values: Unicode characters including alphanumeric, space, and '.:/=+-@' Constraints: Each value can be 0-256 characters long. Required: Yes
            (dict) --Each tag includes the following elements.
            Key (string) --The key (name) of a tag.
            Type: String
            Default: None
            Valid values: A-Z, a-z, 0-9, space, '.:/=+-@'
            Constraints: Each key can be 1-128 characters long.
            Required: Yes
            Value (string) --The value of a tag.
            Type: String
            Default: None
            Valid values: A-Z, a-z, 0-9, space, '.:/=+-@'
            Constraints: Each value can be 0-256 characters long.
            Required: Yes
            
            
    :type TagsToUpdate: list
    """
    pass


def view_billing(Start=None, End=None, Marker=None, MaxItems=None):
    """
    :param Start: The beginning date and time for the time period for which you want a list of billing records. Specify the date in Unix time format.
            Type: Double
            Default: None
            Required: Yes
            
    :type Start: datetime
    :param End: The end date and time for the time period for which you want a list of billing records. Specify the date in Unix time format.
            Type: Double
            Default: None
            Required: Yes
            
    :type End: datetime
    :param Marker: For an initial request for a list of billing records, omit this element. If the number of billing records that are associated with the current AWS account during the specified period is greater than the value that you specified for MaxItems , you can use Marker to return additional billing records. Get the value of NextPageMarker from the previous response, and submit another request that includes the value of NextPageMarker in the Marker element.
            Type: String
            Default: None
            Constraints: The marker must match the value of NextPageMarker that was returned in the previous response.
            Required: No
            
    :type Marker: string
    :param MaxItems: The number of billing records to be returned.
            Type: Integer
            Default: 20
            Constraints: A value between 1 and 100.
            Required: No
            
    :type MaxItems: integer
    """
    pass
