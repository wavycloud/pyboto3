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

def associate_web_acl(WebACLId=None, ResourceArn=None):
    """
    Associates a web ACL with a resource, either an application load balancer or Amazon API Gateway stage.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_web_acl(
        WebACLId='string',
        ResourceArn='string'
    )
    
    
    :type WebACLId: string
    :param WebACLId: [REQUIRED]\nA unique identifier (ID) for the web ACL.\n

    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe ARN (Amazon Resource Name) of the resource to be protected, either an application load balancer or Amazon API Gateway stage.\nThe ARN should be in one of the following formats:\n\nFor an Application Load Balancer: ``arn:aws:elasticloadbalancing:region :account-id :loadbalancer/app/load-balancer-name /load-balancer-id ``\nFor an Amazon API Gateway stage: ``arn:aws:apigateway:region ::/restapis/api-id /stages/stage-name ``\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFInvalidParameterException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFUnavailableEntityException


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

def create_byte_match_set(Name=None, ChangeToken=None):
    """
    Creates a ByteMatchSet . You then use  UpdateByteMatchSet to identify the part of a web request that you want AWS WAF to inspect, such as the values of the User-Agent header or the query string. For example, you can create a ByteMatchSet that matches any requests with User-Agent headers that contain the string BadBot . You can then configure AWS WAF to reject those requests.
    To create and configure a ByteMatchSet , perform the following steps:
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_byte_match_set(
        Name='string',
        ChangeToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nA friendly name or description of the ByteMatchSet . You can\'t change Name after you create a ByteMatchSet .\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ByteMatchSet': {
        'ByteMatchSetId': 'string',
        'Name': 'string',
        'ByteMatchTuples': [
            {
                'FieldToMatch': {
                    'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY'|'SINGLE_QUERY_ARG'|'ALL_QUERY_ARGS',
                    'Data': 'string'
                },
                'TargetString': b'bytes',
                'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE',
                'PositionalConstraint': 'EXACTLY'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CONTAINS_WORD'
            },
        ]
    },
    'ChangeToken': 'string'
}


Response Structure

(dict) --

ByteMatchSet (dict) --
A  ByteMatchSet that contains no ByteMatchTuple objects.

ByteMatchSetId (string) --
The ByteMatchSetId for a ByteMatchSet . You use ByteMatchSetId to get information about a ByteMatchSet (see  GetByteMatchSet ), update a ByteMatchSet (see  UpdateByteMatchSet ), insert a ByteMatchSet into a Rule or delete one from a Rule (see  UpdateRule ), and delete a ByteMatchSet from AWS WAF (see  DeleteByteMatchSet ).

ByteMatchSetId is returned by  CreateByteMatchSet and by  ListByteMatchSets .


Name (string) --
A friendly name or description of the  ByteMatchSet . You can\'t change Name after you create a ByteMatchSet .

ByteMatchTuples (list) --
Specifies the bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to search for in web requests, the location in requests that you want AWS WAF to search, and other settings.

(dict) --

Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


The bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to search for in web requests, the location in requests that you want AWS WAF to search, and other settings.

FieldToMatch (dict) --
The part of a web request that you want AWS WAF to search, such as a specified header or a query string. For more information, see  FieldToMatch .

Type (string) --
The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:

HEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .
METHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .
QUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.
URI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .
BODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .
SINGLE_QUERY_ARG : The parameter in the query string that you will inspect, such as UserName or SalesRegion . The maximum length for SINGLE_QUERY_ARG is 30 characters.
ALL_QUERY_ARGS : Similar to SINGLE_QUERY_ARG , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in TargetString .


Data (string) --
When the value of Type is HEADER , enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer . The name of the header is not case sensitive.
When the value of Type is SINGLE_QUERY_ARG , enter the name of the parameter that you want AWS WAF to search, for example, UserName or SalesRegion . The parameter name is not case sensitive.
If the value of Type is any other value, omit Data .



TargetString (bytes) --
The value that you want AWS WAF to search for. AWS WAF searches for the specified string in the part of web requests that you specified in FieldToMatch . The maximum length of the value is 50 bytes.
Valid values depend on the values that you specified for FieldToMatch :

HEADER : The value that you want AWS WAF to search for in the request header that you specified in  FieldToMatch , for example, the value of the User-Agent or Referer header.
METHOD : The HTTP method, which indicates the type of operation specified in the request. CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .
QUERY_STRING : The value that you want AWS WAF to search for in the query string, which is the part of a URL that appears after a ? character.
URI : The value that you want AWS WAF to search for in the part of a URL that identifies a resource, for example, /images/daily-ad.jpg .
BODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .
SINGLE_QUERY_ARG : The parameter in the query string that you will inspect, such as UserName or SalesRegion . The maximum length for SINGLE_QUERY_ARG is 30 characters.
ALL_QUERY_ARGS : Similar to SINGLE_QUERY_ARG , but instead of inspecting a single parameter, AWS WAF inspects all parameters within the query string for the value or regex pattern that you specify in TargetString .

If TargetString includes alphabetic characters A-Z and a-z, note that the value is case sensitive.

If you\'re using the AWS WAF API

Specify a base64-encoded version of the value. The maximum length of the value before you base64-encode it is 50 bytes.
For example, suppose the value of Type is HEADER and the value of Data is User-Agent . If you want to search the User-Agent header for the value BadBot , you base64-encode BadBot using MIME base64-encoding and include the resulting value, QmFkQm90 , in the value of TargetString .

If you\'re using the AWS CLI or one of the AWS SDKs

The value that you want AWS WAF to search for. The SDK automatically base64 encodes the value.

TextTransformation (string) --
Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on FieldToMatch before inspecting it for a match.
You can only specify a single type of TextTransformation.

CMD_LINE

When you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: " \' ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE

Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.
HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a "less than" symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE

Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE

Use this option to decode a URL-encoded value.

NONE

Specify NONE if you don\'t want to perform any text transformations.

PositionalConstraint (string) --
Within the portion of a web request that you want to search (for example, in the query string, if any), specify where you want AWS WAF to search. Valid values include the following:

CONTAINS

The specified part of the web request must include the value of TargetString , but the location doesn\'t matter.

CONTAINS_WORD

The specified part of the web request must include the value of TargetString , and TargetString must contain only alphanumeric characters or underscore (A-Z, a-z, 0-9, or _). In addition, TargetString must be a word, which means one of the following:

TargetString exactly matches the value of the specified part of the web request, such as the value of a header.
TargetString is at the beginning of the specified part of the web request and is followed by a character other than an alphanumeric character or underscore (_), for example, BadBot; .
TargetString is at the end of the specified part of the web request and is preceded by a character other than an alphanumeric character or underscore (_), for example, ;BadBot .
TargetString is in the middle of the specified part of the web request and is preceded and followed by characters other than alphanumeric characters or underscore (_), for example, -BadBot; .


EXACTLY

The value of the specified part of the web request must exactly match the value of TargetString .

STARTS_WITH

The value of TargetString must appear at the beginning of the specified part of the web request.

ENDS_WITH

The value of TargetString must appear at the end of the specified part of the web request.







ChangeToken (string) --
The ChangeToken that you used to submit the CreateByteMatchSet request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFDisallowedNameException
WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFInvalidParameterException
WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFLimitsExceededException


    :return: {
        'ByteMatchSet': {
            'ByteMatchSetId': 'string',
            'Name': 'string',
            'ByteMatchTuples': [
                {
                    'FieldToMatch': {
                        'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY'|'SINGLE_QUERY_ARG'|'ALL_QUERY_ARGS',
                        'Data': 'string'
                    },
                    'TargetString': b'bytes',
                    'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE',
                    'PositionalConstraint': 'EXACTLY'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CONTAINS_WORD'
                },
            ]
        },
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    Name (string) -- [REQUIRED]
    A friendly name or description of the  ByteMatchSet . You can\'t change Name after you create a ByteMatchSet .
    
    ChangeToken (string) -- [REQUIRED]
    The value returned by the most recent call to  GetChangeToken .
    
    
    """
    pass

def create_geo_match_set(Name=None, ChangeToken=None):
    """
    Creates an  GeoMatchSet , which you use to specify which web requests you want to allow or block based on the country that the requests originate from. For example, if you\'re receiving a lot of requests from one or more countries and you want to block the requests, you can create an GeoMatchSet that contains those countries and then configure AWS WAF to block the requests.
    To create and configure a GeoMatchSet , perform the following steps:
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_geo_match_set(
        Name='string',
        ChangeToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nA friendly name or description of the GeoMatchSet . You can\'t change Name after you create the GeoMatchSet .\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GeoMatchSet': {
        'GeoMatchSetId': 'string',
        'Name': 'string',
        'GeoMatchConstraints': [
            {
                'Type': 'Country',
                'Value': 'AF'|'AX'|'AL'|'DZ'|'AS'|'AD'|'AO'|'AI'|'AQ'|'AG'|'AR'|'AM'|'AW'|'AU'|'AT'|'AZ'|'BS'|'BH'|'BD'|'BB'|'BY'|'BE'|'BZ'|'BJ'|'BM'|'BT'|'BO'|'BQ'|'BA'|'BW'|'BV'|'BR'|'IO'|'BN'|'BG'|'BF'|'BI'|'KH'|'CM'|'CA'|'CV'|'KY'|'CF'|'TD'|'CL'|'CN'|'CX'|'CC'|'CO'|'KM'|'CG'|'CD'|'CK'|'CR'|'CI'|'HR'|'CU'|'CW'|'CY'|'CZ'|'DK'|'DJ'|'DM'|'DO'|'EC'|'EG'|'SV'|'GQ'|'ER'|'EE'|'ET'|'FK'|'FO'|'FJ'|'FI'|'FR'|'GF'|'PF'|'TF'|'GA'|'GM'|'GE'|'DE'|'GH'|'GI'|'GR'|'GL'|'GD'|'GP'|'GU'|'GT'|'GG'|'GN'|'GW'|'GY'|'HT'|'HM'|'VA'|'HN'|'HK'|'HU'|'IS'|'IN'|'ID'|'IR'|'IQ'|'IE'|'IM'|'IL'|'IT'|'JM'|'JP'|'JE'|'JO'|'KZ'|'KE'|'KI'|'KP'|'KR'|'KW'|'KG'|'LA'|'LV'|'LB'|'LS'|'LR'|'LY'|'LI'|'LT'|'LU'|'MO'|'MK'|'MG'|'MW'|'MY'|'MV'|'ML'|'MT'|'MH'|'MQ'|'MR'|'MU'|'YT'|'MX'|'FM'|'MD'|'MC'|'MN'|'ME'|'MS'|'MA'|'MZ'|'MM'|'NA'|'NR'|'NP'|'NL'|'NC'|'NZ'|'NI'|'NE'|'NG'|'NU'|'NF'|'MP'|'NO'|'OM'|'PK'|'PW'|'PS'|'PA'|'PG'|'PY'|'PE'|'PH'|'PN'|'PL'|'PT'|'PR'|'QA'|'RE'|'RO'|'RU'|'RW'|'BL'|'SH'|'KN'|'LC'|'MF'|'PM'|'VC'|'WS'|'SM'|'ST'|'SA'|'SN'|'RS'|'SC'|'SL'|'SG'|'SX'|'SK'|'SI'|'SB'|'SO'|'ZA'|'GS'|'SS'|'ES'|'LK'|'SD'|'SR'|'SJ'|'SZ'|'SE'|'CH'|'SY'|'TW'|'TJ'|'TZ'|'TH'|'TL'|'TG'|'TK'|'TO'|'TT'|'TN'|'TR'|'TM'|'TC'|'TV'|'UG'|'UA'|'AE'|'GB'|'US'|'UM'|'UY'|'UZ'|'VU'|'VE'|'VN'|'VG'|'VI'|'WF'|'EH'|'YE'|'ZM'|'ZW'
            },
        ]
    },
    'ChangeToken': 'string'
}


Response Structure

(dict) --

GeoMatchSet (dict) --
The  GeoMatchSet returned in the CreateGeoMatchSet response. The GeoMatchSet contains no GeoMatchConstraints .

GeoMatchSetId (string) --
The GeoMatchSetId for an GeoMatchSet . You use GeoMatchSetId to get information about a GeoMatchSet (see  GeoMatchSet ), update a GeoMatchSet (see  UpdateGeoMatchSet ), insert a GeoMatchSet into a Rule or delete one from a Rule (see  UpdateRule ), and delete a GeoMatchSet from AWS WAF (see  DeleteGeoMatchSet ).

GeoMatchSetId is returned by  CreateGeoMatchSet and by  ListGeoMatchSets .


Name (string) --
A friendly name or description of the  GeoMatchSet . You can\'t change the name of an GeoMatchSet after you create it.

GeoMatchConstraints (list) --
An array of  GeoMatchConstraint objects, which contain the country that you want AWS WAF to search for.

(dict) --

Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


The country from which web requests originate that you want AWS WAF to search for.

Type (string) --
The type of geographical area you want AWS WAF to search for. Currently Country is the only valid value.

Value (string) --
The country that you want AWS WAF to search for.







ChangeToken (string) --
The ChangeToken that you used to submit the CreateGeoMatchSet request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFDisallowedNameException
WAFRegional.Client.exceptions.WAFInvalidParameterException
WAFRegional.Client.exceptions.WAFLimitsExceededException


    :return: {
        'GeoMatchSet': {
            'GeoMatchSetId': 'string',
            'Name': 'string',
            'GeoMatchConstraints': [
                {
                    'Type': 'Country',
                    'Value': 'AF'|'AX'|'AL'|'DZ'|'AS'|'AD'|'AO'|'AI'|'AQ'|'AG'|'AR'|'AM'|'AW'|'AU'|'AT'|'AZ'|'BS'|'BH'|'BD'|'BB'|'BY'|'BE'|'BZ'|'BJ'|'BM'|'BT'|'BO'|'BQ'|'BA'|'BW'|'BV'|'BR'|'IO'|'BN'|'BG'|'BF'|'BI'|'KH'|'CM'|'CA'|'CV'|'KY'|'CF'|'TD'|'CL'|'CN'|'CX'|'CC'|'CO'|'KM'|'CG'|'CD'|'CK'|'CR'|'CI'|'HR'|'CU'|'CW'|'CY'|'CZ'|'DK'|'DJ'|'DM'|'DO'|'EC'|'EG'|'SV'|'GQ'|'ER'|'EE'|'ET'|'FK'|'FO'|'FJ'|'FI'|'FR'|'GF'|'PF'|'TF'|'GA'|'GM'|'GE'|'DE'|'GH'|'GI'|'GR'|'GL'|'GD'|'GP'|'GU'|'GT'|'GG'|'GN'|'GW'|'GY'|'HT'|'HM'|'VA'|'HN'|'HK'|'HU'|'IS'|'IN'|'ID'|'IR'|'IQ'|'IE'|'IM'|'IL'|'IT'|'JM'|'JP'|'JE'|'JO'|'KZ'|'KE'|'KI'|'KP'|'KR'|'KW'|'KG'|'LA'|'LV'|'LB'|'LS'|'LR'|'LY'|'LI'|'LT'|'LU'|'MO'|'MK'|'MG'|'MW'|'MY'|'MV'|'ML'|'MT'|'MH'|'MQ'|'MR'|'MU'|'YT'|'MX'|'FM'|'MD'|'MC'|'MN'|'ME'|'MS'|'MA'|'MZ'|'MM'|'NA'|'NR'|'NP'|'NL'|'NC'|'NZ'|'NI'|'NE'|'NG'|'NU'|'NF'|'MP'|'NO'|'OM'|'PK'|'PW'|'PS'|'PA'|'PG'|'PY'|'PE'|'PH'|'PN'|'PL'|'PT'|'PR'|'QA'|'RE'|'RO'|'RU'|'RW'|'BL'|'SH'|'KN'|'LC'|'MF'|'PM'|'VC'|'WS'|'SM'|'ST'|'SA'|'SN'|'RS'|'SC'|'SL'|'SG'|'SX'|'SK'|'SI'|'SB'|'SO'|'ZA'|'GS'|'SS'|'ES'|'LK'|'SD'|'SR'|'SJ'|'SZ'|'SE'|'CH'|'SY'|'TW'|'TJ'|'TZ'|'TH'|'TL'|'TG'|'TK'|'TO'|'TT'|'TN'|'TR'|'TM'|'TC'|'TV'|'UG'|'UA'|'AE'|'GB'|'US'|'UM'|'UY'|'UZ'|'VU'|'VE'|'VN'|'VG'|'VI'|'WF'|'EH'|'YE'|'ZM'|'ZW'
                },
            ]
        },
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    Name (string) -- [REQUIRED]
    A friendly name or description of the  GeoMatchSet . You can\'t change Name after you create the GeoMatchSet .
    
    ChangeToken (string) -- [REQUIRED]
    The value returned by the most recent call to  GetChangeToken .
    
    
    """
    pass

def create_ip_set(Name=None, ChangeToken=None):
    """
    Creates an  IPSet , which you use to specify which web requests that you want to allow or block based on the IP addresses that the requests originate from. For example, if you\'re receiving a lot of requests from one or more individual IP addresses or one or more ranges of IP addresses and you want to block the requests, you can create an IPSet that contains those IP addresses and then configure AWS WAF to block the requests.
    To create and configure an IPSet , perform the following steps:
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example creates an IP match set named MyIPSetFriendlyName.
    Expected Output:
    
    :example: response = client.create_ip_set(
        Name='string',
        ChangeToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nA friendly name or description of the IPSet . You can\'t change Name after you create the IPSet .\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'IPSet': {
        'IPSetId': 'string',
        'Name': 'string',
        'IPSetDescriptors': [
            {
                'Type': 'IPV4'|'IPV6',
                'Value': 'string'
            },
        ]
    },
    'ChangeToken': 'string'
}


Response Structure

(dict) --

IPSet (dict) --
The  IPSet returned in the CreateIPSet response.

IPSetId (string) --
The IPSetId for an IPSet . You use IPSetId to get information about an IPSet (see  GetIPSet ), update an IPSet (see  UpdateIPSet ), insert an IPSet into a Rule or delete one from a Rule (see  UpdateRule ), and delete an IPSet from AWS WAF (see  DeleteIPSet ).

IPSetId is returned by  CreateIPSet and by  ListIPSets .


Name (string) --
A friendly name or description of the  IPSet . You can\'t change the name of an IPSet after you create it.

IPSetDescriptors (list) --
The IP address type (IPV4 or IPV6 ) and the IP address range (in CIDR notation) that web requests originate from. If the WebACL is associated with a CloudFront distribution and the viewer did not use an HTTP proxy or a load balancer to send the request, this is the value of the c-ip field in the CloudFront access logs.

(dict) --

Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


Specifies the IP address type (IPV4 or IPV6 ) and the IP address range (in CIDR format) that web requests originate from.

Type (string) --
Specify IPV4 or IPV6 .

Value (string) --
Specify an IPv4 address by using CIDR notation. For example:

To configure AWS WAF to allow, block, or count requests that originated from the IP address 192.0.2.44, specify 192.0.2.44/32 .
To configure AWS WAF to allow, block, or count requests that originated from IP addresses from 192.0.2.0 to 192.0.2.255, specify 192.0.2.0/24 .

For more information about CIDR notation, see the Wikipedia entry Classless Inter-Domain Routing .
Specify an IPv6 address by using CIDR notation. For example:

To configure AWS WAF to allow, block, or count requests that originated from the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify 1111:0000:0000:0000:0000:0000:0000:0111/128 .
To configure AWS WAF to allow, block, or count requests that originated from IP addresses 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify 1111:0000:0000:0000:0000:0000:0000:0000/64 .








ChangeToken (string) --
The ChangeToken that you used to submit the CreateIPSet request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFDisallowedNameException
WAFRegional.Client.exceptions.WAFInvalidParameterException
WAFRegional.Client.exceptions.WAFLimitsExceededException

Examples
The following example creates an IP match set named MyIPSetFriendlyName.
response = client.create_ip_set(
    ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    Name='MyIPSetFriendlyName',
)

print(response)


Expected Output:
{
    'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    'IPSet': {
        'IPSetDescriptors': [
            {
                'Type': 'IPV4',
                'Value': '192.0.2.44/32',
            },
        ],
        'IPSetId': 'example1ds3t-46da-4fdb-b8d5-abc321j569j5',
        'Name': 'MyIPSetFriendlyName',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'IPSet': {
            'IPSetId': 'string',
            'Name': 'string',
            'IPSetDescriptors': [
                {
                    'Type': 'IPV4'|'IPV6',
                    'Value': 'string'
                },
            ]
        },
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    Name (string) -- [REQUIRED]
    A friendly name or description of the  IPSet . You can\'t change Name after you create the IPSet .
    
    ChangeToken (string) -- [REQUIRED]
    The value returned by the most recent call to  GetChangeToken .
    
    
    """
    pass

def create_rate_based_rule(Name=None, MetricName=None, RateKey=None, RateLimit=None, ChangeToken=None, Tags=None):
    """
    Creates a  RateBasedRule . The RateBasedRule contains a RateLimit , which specifies the maximum number of requests that AWS WAF allows from a specified IP address in a five-minute period. The RateBasedRule also contains the IPSet objects, ByteMatchSet objects, and other predicates that identify the requests that you want to count or block if these requests exceed the RateLimit .
    If you add more than one predicate to a RateBasedRule , a request not only must exceed the RateLimit , but it also must match all the conditions to be counted or blocked. For example, suppose you add the following to a RateBasedRule :
    Further, you specify a RateLimit of 1,000.
    You then add the RateBasedRule to a WebACL and specify that you want to block requests that meet the conditions in the rule. For a request to be blocked, it must come from the IP address 192.0.2.44 and the User-Agent header in the request must contain the value BadBot . Further, requests that match these two conditions must be received at a rate of more than 1,000 requests every five minutes. If both conditions are met and the rate is exceeded, AWS WAF blocks the requests. If the rate drops below 1,000 for a five-minute period, AWS WAF no longer blocks the requests.
    As a second example, suppose you want to limit requests to a particular page on your site. To do this, you could add the following to a RateBasedRule :
    Further, you specify a RateLimit of 1,000.
    By adding this RateBasedRule to a WebACL , you could limit requests to your login page without affecting the rest of your site.
    To create and configure a RateBasedRule , perform the following steps:
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_rate_based_rule(
        Name='string',
        MetricName='string',
        RateKey='IP',
        RateLimit=123,
        ChangeToken='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nA friendly name or description of the RateBasedRule . You can\'t change the name of a RateBasedRule after you create it.\n

    :type MetricName: string
    :param MetricName: [REQUIRED]\nA friendly name or description for the metrics for this RateBasedRule . The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can\'t contain whitespace or metric names reserved for AWS WAF, including 'All' and 'Default_Action.' You can\'t change the name of the metric after you create the RateBasedRule .\n

    :type RateKey: string
    :param RateKey: [REQUIRED]\nThe field that AWS WAF uses to determine if requests are likely arriving from a single source and thus subject to rate monitoring. The only valid value for RateKey is IP . IP indicates that requests that arrive from the same IP address are subject to the RateLimit that is specified in the RateBasedRule .\n

    :type RateLimit: integer
    :param RateLimit: [REQUIRED]\nThe maximum number of requests, which have an identical value in the field that is specified by RateKey , allowed in a five-minute period. If the number of requests exceeds the RateLimit and the other predicates specified in the rule are also met, AWS WAF triggers the action that is specified for this rule.\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe ChangeToken that you used to submit the CreateRateBasedRule request. You can also use this value to query the status of the request. For more information, see GetChangeTokenStatus .\n

    :type Tags: list
    :param Tags: \n(dict) --\nNote\nThis is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.\n\nFor the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.\n\nA tag associated with an AWS resource. Tags are key:value pairs that you can use to categorize and manage your resources, for purposes like billing. For example, you might set the tag key to 'customer' and the value to the customer name or ID. You can specify one or more tags to add to each AWS resource, up to 50 tags for a resource.\nTagging is only available through the API, SDKs, and CLI. You can\'t manage or view tags through the AWS WAF Classic console. You can tag the AWS resources that you manage through AWS WAF Classic: web ACLs, rule groups, and rules.\n\nKey (string) -- [REQUIRED]\nValue (string) -- [REQUIRED]\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Rule': {
        'RuleId': 'string',
        'Name': 'string',
        'MetricName': 'string',
        'MatchPredicates': [
            {
                'Negated': True|False,
                'Type': 'IPMatch'|'ByteMatch'|'SqlInjectionMatch'|'GeoMatch'|'SizeConstraint'|'XssMatch'|'RegexMatch',
                'DataId': 'string'
            },
        ],
        'RateKey': 'IP',
        'RateLimit': 123
    },
    'ChangeToken': 'string'
}


Response Structure

(dict) --

Rule (dict) --
The  RateBasedRule that is returned in the CreateRateBasedRule response.

RuleId (string) --
A unique identifier for a RateBasedRule . You use RuleId to get more information about a RateBasedRule (see  GetRateBasedRule ), update a RateBasedRule (see  UpdateRateBasedRule ), insert a RateBasedRule into a WebACL or delete one from a WebACL (see  UpdateWebACL ), or delete a RateBasedRule from AWS WAF (see  DeleteRateBasedRule ).

Name (string) --
A friendly name or description for a RateBasedRule . You can\'t change the name of a RateBasedRule after you create it.

MetricName (string) --
A friendly name or description for the metrics for a RateBasedRule . The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can\'t contain whitespace or metric names reserved for AWS WAF, including "All" and "Default_Action." You can\'t change the name of the metric after you create the RateBasedRule .

MatchPredicates (list) --
The Predicates object contains one Predicate element for each  ByteMatchSet ,  IPSet , or  SqlInjectionMatchSet object that you want to include in a RateBasedRule .

(dict) --

Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


Specifies the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , and  SizeConstraintSet objects that you want to add to a Rule and, for each object, indicates whether you want to negate the settings, for example, requests that do NOT originate from the IP address 192.0.2.44.

Negated (boolean) --
Set Negated to False if you want AWS WAF to allow, block, or count requests based on the settings in the specified  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if an IPSet includes the IP address 192.0.2.44 , AWS WAF will allow or block requests based on that IP address.
Set Negated to True if you want AWS WAF to allow or block a request based on the negation of the settings in the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if an IPSet includes the IP address 192.0.2.44 , AWS WAF will allow, block, or count requests based on all IP addresses except 192.0.2.44 .

Type (string) --
The type of predicate in a Rule , such as ByteMatch or IPSet .

DataId (string) --
A unique identifier for a predicate in a Rule , such as ByteMatchSetId or IPSetId . The ID is returned by the corresponding Create or List command.





RateKey (string) --
The field that AWS WAF uses to determine if requests are likely arriving from single source and thus subject to rate monitoring. The only valid value for RateKey is IP . IP indicates that requests arriving from the same IP address are subject to the RateLimit that is specified in the RateBasedRule .

RateLimit (integer) --
The maximum number of requests, which have an identical value in the field specified by the RateKey , allowed in a five-minute period. If the number of requests exceeds the RateLimit and the other predicates specified in the rule are also met, AWS WAF triggers the action that is specified for this rule.



ChangeToken (string) --
The ChangeToken that you used to submit the CreateRateBasedRule request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFDisallowedNameException
WAFRegional.Client.exceptions.WAFInvalidParameterException
WAFRegional.Client.exceptions.WAFLimitsExceededException
WAFRegional.Client.exceptions.WAFTagOperationException
WAFRegional.Client.exceptions.WAFTagOperationInternalErrorException
WAFRegional.Client.exceptions.WAFBadRequestException


    :return: {
        'Rule': {
            'RuleId': 'string',
            'Name': 'string',
            'MetricName': 'string',
            'MatchPredicates': [
                {
                    'Negated': True|False,
                    'Type': 'IPMatch'|'ByteMatch'|'SqlInjectionMatch'|'GeoMatch'|'SizeConstraint'|'XssMatch'|'RegexMatch',
                    'DataId': 'string'
                },
            ],
            'RateKey': 'IP',
            'RateLimit': 123
        },
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    A ByteMatchSet with FieldToMatch of URI
    A PositionalConstraint of STARTS_WITH
    A TargetString of login
    
    """
    pass

def create_regex_match_set(Name=None, ChangeToken=None):
    """
    Creates a  RegexMatchSet . You then use  UpdateRegexMatchSet to identify the part of a web request that you want AWS WAF to inspect, such as the values of the User-Agent header or the query string. For example, you can create a RegexMatchSet that contains a RegexMatchTuple that looks for any requests with User-Agent headers that match a RegexPatternSet with pattern B[a@]dB[o0]t . You can then configure AWS WAF to reject those requests.
    To create and configure a RegexMatchSet , perform the following steps:
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_regex_match_set(
        Name='string',
        ChangeToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nA friendly name or description of the RegexMatchSet . You can\'t change Name after you create a RegexMatchSet .\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'RegexMatchSet': {
        'RegexMatchSetId': 'string',
        'Name': 'string',
        'RegexMatchTuples': [
            {
                'FieldToMatch': {
                    'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY'|'SINGLE_QUERY_ARG'|'ALL_QUERY_ARGS',
                    'Data': 'string'
                },
                'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE',
                'RegexPatternSetId': 'string'
            },
        ]
    },
    'ChangeToken': 'string'
}


Response Structure

(dict) --

RegexMatchSet (dict) --
A  RegexMatchSet that contains no RegexMatchTuple objects.

RegexMatchSetId (string) --
The RegexMatchSetId for a RegexMatchSet . You use RegexMatchSetId to get information about a RegexMatchSet (see  GetRegexMatchSet ), update a RegexMatchSet (see  UpdateRegexMatchSet ), insert a RegexMatchSet into a Rule or delete one from a Rule (see  UpdateRule ), and delete a RegexMatchSet from AWS WAF (see  DeleteRegexMatchSet ).

RegexMatchSetId is returned by  CreateRegexMatchSet and by  ListRegexMatchSets .


Name (string) --
A friendly name or description of the  RegexMatchSet . You can\'t change Name after you create a RegexMatchSet .

RegexMatchTuples (list) --
Contains an array of  RegexMatchTuple objects. Each RegexMatchTuple object contains:

The part of a web request that you want AWS WAF to inspect, such as a query string or the value of the User-Agent header.
The identifier of the pattern (a regular expression) that you want AWS WAF to look for. For more information, see  RegexPatternSet .
Whether to perform any conversions on the request, such as converting it to lowercase, before inspecting it for the specified string.


(dict) --

Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


The regular expression pattern that you want AWS WAF to search for in web requests, the location in requests that you want AWS WAF to search, and other settings. Each RegexMatchTuple object contains:

The part of a web request that you want AWS WAF to inspect, such as a query string or the value of the User-Agent header.
The identifier of the pattern (a regular expression) that you want AWS WAF to look for. For more information, see  RegexPatternSet .
Whether to perform any conversions on the request, such as converting it to lowercase, before inspecting it for the specified string.


FieldToMatch (dict) --
Specifies where in a web request to look for the RegexPatternSet .

Type (string) --
The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:

HEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .
METHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .
QUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.
URI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .
BODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .
SINGLE_QUERY_ARG : The parameter in the query string that you will inspect, such as UserName or SalesRegion . The maximum length for SINGLE_QUERY_ARG is 30 characters.
ALL_QUERY_ARGS : Similar to SINGLE_QUERY_ARG , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in TargetString .


Data (string) --
When the value of Type is HEADER , enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer . The name of the header is not case sensitive.
When the value of Type is SINGLE_QUERY_ARG , enter the name of the parameter that you want AWS WAF to search, for example, UserName or SalesRegion . The parameter name is not case sensitive.
If the value of Type is any other value, omit Data .



TextTransformation (string) --
Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on RegexPatternSet before inspecting a request for a match.
You can only specify a single type of TextTransformation.

CMD_LINE

When you\'re concerned that attackers are injecting an operating system commandline command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: " \' ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE

Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.
HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a "less than" symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE

Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE

Use this option to decode a URL-encoded value.

NONE

Specify NONE if you don\'t want to perform any text transformations.

RegexPatternSetId (string) --
The RegexPatternSetId for a RegexPatternSet . You use RegexPatternSetId to get information about a RegexPatternSet (see  GetRegexPatternSet ), update a RegexPatternSet (see  UpdateRegexPatternSet ), insert a RegexPatternSet into a RegexMatchSet or delete one from a RegexMatchSet (see  UpdateRegexMatchSet ), and delete an RegexPatternSet from AWS WAF (see  DeleteRegexPatternSet ).

RegexPatternSetId is returned by  CreateRegexPatternSet and by  ListRegexPatternSets .








ChangeToken (string) --
The ChangeToken that you used to submit the CreateRegexMatchSet request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFDisallowedNameException
WAFRegional.Client.exceptions.WAFLimitsExceededException


    :return: {
        'RegexMatchSet': {
            'RegexMatchSetId': 'string',
            'Name': 'string',
            'RegexMatchTuples': [
                {
                    'FieldToMatch': {
                        'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY'|'SINGLE_QUERY_ARG'|'ALL_QUERY_ARGS',
                        'Data': 'string'
                    },
                    'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE',
                    'RegexPatternSetId': 'string'
                },
            ]
        },
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    Name (string) -- [REQUIRED]
    A friendly name or description of the  RegexMatchSet . You can\'t change Name after you create a RegexMatchSet .
    
    ChangeToken (string) -- [REQUIRED]
    The value returned by the most recent call to  GetChangeToken .
    
    
    """
    pass

def create_regex_pattern_set(Name=None, ChangeToken=None):
    """
    Creates a RegexPatternSet . You then use  UpdateRegexPatternSet to specify the regular expression (regex) pattern that you want AWS WAF to search for, such as B[a@]dB[o0]t . You can then configure AWS WAF to reject those requests.
    To create and configure a RegexPatternSet , perform the following steps:
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_regex_pattern_set(
        Name='string',
        ChangeToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nA friendly name or description of the RegexPatternSet . You can\'t change Name after you create a RegexPatternSet .\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'RegexPatternSet': {
        'RegexPatternSetId': 'string',
        'Name': 'string',
        'RegexPatternStrings': [
            'string',
        ]
    },
    'ChangeToken': 'string'
}


Response Structure

(dict) --

RegexPatternSet (dict) --
A  RegexPatternSet that contains no objects.

RegexPatternSetId (string) --
The identifier for the RegexPatternSet . You use RegexPatternSetId to get information about a RegexPatternSet , update a RegexPatternSet , remove a RegexPatternSet from a RegexMatchSet , and delete a RegexPatternSet from AWS WAF.

RegexMatchSetId is returned by  CreateRegexPatternSet and by  ListRegexPatternSets .


Name (string) --
A friendly name or description of the  RegexPatternSet . You can\'t change Name after you create a RegexPatternSet .

RegexPatternStrings (list) --
Specifies the regular expression (regex) patterns that you want AWS WAF to search for, such as B[a@]dB[o0]t .

(string) --




ChangeToken (string) --
The ChangeToken that you used to submit the CreateRegexPatternSet request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFDisallowedNameException
WAFRegional.Client.exceptions.WAFLimitsExceededException


    :return: {
        'RegexPatternSet': {
            'RegexPatternSetId': 'string',
            'Name': 'string',
            'RegexPatternStrings': [
                'string',
            ]
        },
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    Name (string) -- [REQUIRED]
    A friendly name or description of the  RegexPatternSet . You can\'t change Name after you create a RegexPatternSet .
    
    ChangeToken (string) -- [REQUIRED]
    The value returned by the most recent call to  GetChangeToken .
    
    
    """
    pass

def create_rule(Name=None, MetricName=None, ChangeToken=None, Tags=None):
    """
    Creates a Rule , which contains the IPSet objects, ByteMatchSet objects, and other predicates that identify the requests that you want to block. If you add more than one predicate to a Rule , a request must match all of the specifications to be allowed or blocked. For example, suppose that you add the following to a Rule :
    You then add the Rule to a WebACL and specify that you want to blocks requests that satisfy the Rule . For a request to be blocked, it must come from the IP address 192.0.2.44 and the User-Agent header in the request must contain the value BadBot .
    To create and configure a Rule , perform the following steps:
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example creates a rule named WAFByteHeaderRule.
    Expected Output:
    
    :example: response = client.create_rule(
        Name='string',
        MetricName='string',
        ChangeToken='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nA friendly name or description of the Rule . You can\'t change the name of a Rule after you create it.\n

    :type MetricName: string
    :param MetricName: [REQUIRED]\nA friendly name or description for the metrics for this Rule . The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can\'t contain whitespace or metric names reserved for AWS WAF, including 'All' and 'Default_Action.' You can\'t change the name of the metric after you create the Rule .\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :type Tags: list
    :param Tags: \n(dict) --\nNote\nThis is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.\n\nFor the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.\n\nA tag associated with an AWS resource. Tags are key:value pairs that you can use to categorize and manage your resources, for purposes like billing. For example, you might set the tag key to 'customer' and the value to the customer name or ID. You can specify one or more tags to add to each AWS resource, up to 50 tags for a resource.\nTagging is only available through the API, SDKs, and CLI. You can\'t manage or view tags through the AWS WAF Classic console. You can tag the AWS resources that you manage through AWS WAF Classic: web ACLs, rule groups, and rules.\n\nKey (string) -- [REQUIRED]\nValue (string) -- [REQUIRED]\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Rule': {
        'RuleId': 'string',
        'Name': 'string',
        'MetricName': 'string',
        'Predicates': [
            {
                'Negated': True|False,
                'Type': 'IPMatch'|'ByteMatch'|'SqlInjectionMatch'|'GeoMatch'|'SizeConstraint'|'XssMatch'|'RegexMatch',
                'DataId': 'string'
            },
        ]
    },
    'ChangeToken': 'string'
}


Response Structure

(dict) --

Rule (dict) --
The  Rule returned in the CreateRule response.

RuleId (string) --
A unique identifier for a Rule . You use RuleId to get more information about a Rule (see  GetRule ), update a Rule (see  UpdateRule ), insert a Rule into a WebACL or delete a one from a WebACL (see  UpdateWebACL ), or delete a Rule from AWS WAF (see  DeleteRule ).

RuleId is returned by  CreateRule and by  ListRules .


Name (string) --
The friendly name or description for the Rule . You can\'t change the name of a Rule after you create it.

MetricName (string) --
A friendly name or description for the metrics for this Rule . The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can\'t contain whitespace or metric names reserved for AWS WAF, including "All" and "Default_Action." You can\'t change MetricName after you create the Rule .

Predicates (list) --
The Predicates object contains one Predicate element for each  ByteMatchSet ,  IPSet , or  SqlInjectionMatchSet object that you want to include in a Rule .

(dict) --

Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


Specifies the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , and  SizeConstraintSet objects that you want to add to a Rule and, for each object, indicates whether you want to negate the settings, for example, requests that do NOT originate from the IP address 192.0.2.44.

Negated (boolean) --
Set Negated to False if you want AWS WAF to allow, block, or count requests based on the settings in the specified  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if an IPSet includes the IP address 192.0.2.44 , AWS WAF will allow or block requests based on that IP address.
Set Negated to True if you want AWS WAF to allow or block a request based on the negation of the settings in the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if an IPSet includes the IP address 192.0.2.44 , AWS WAF will allow, block, or count requests based on all IP addresses except 192.0.2.44 .

Type (string) --
The type of predicate in a Rule , such as ByteMatch or IPSet .

DataId (string) --
A unique identifier for a predicate in a Rule , such as ByteMatchSetId or IPSetId . The ID is returned by the corresponding Create or List command.







ChangeToken (string) --
The ChangeToken that you used to submit the CreateRule request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFDisallowedNameException
WAFRegional.Client.exceptions.WAFInvalidParameterException
WAFRegional.Client.exceptions.WAFLimitsExceededException
WAFRegional.Client.exceptions.WAFTagOperationException
WAFRegional.Client.exceptions.WAFTagOperationInternalErrorException
WAFRegional.Client.exceptions.WAFBadRequestException

Examples
The following example creates a rule named WAFByteHeaderRule.
response = client.create_rule(
    ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    MetricName='WAFByteHeaderRule',
    Name='WAFByteHeaderRule',
)

print(response)


Expected Output:
{
    'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    'Rule': {
        'MetricName': 'WAFByteHeaderRule',
        'Name': 'WAFByteHeaderRule',
        'Predicates': [
            {
                'DataId': 'MyByteMatchSetID',
                'Negated': False,
                'Type': 'ByteMatch',
            },
        ],
        'RuleId': 'WAFRule-1-Example',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Rule': {
            'RuleId': 'string',
            'Name': 'string',
            'MetricName': 'string',
            'Predicates': [
                {
                    'Negated': True|False,
                    'Type': 'IPMatch'|'ByteMatch'|'SqlInjectionMatch'|'GeoMatch'|'SizeConstraint'|'XssMatch'|'RegexMatch',
                    'DataId': 'string'
                },
            ]
        },
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    Create and update the predicates that you want to include in the Rule . For more information, see  CreateByteMatchSet ,  CreateIPSet , and  CreateSqlInjectionMatchSet .
    Use  GetChangeToken to get the change token that you provide in the ChangeToken parameter of a CreateRule request.
    Submit a CreateRule request.
    Use GetChangeToken to get the change token that you provide in the ChangeToken parameter of an  UpdateRule request.
    Submit an UpdateRule request to specify the predicates that you want to include in the Rule .
    Create and update a WebACL that contains the Rule . For more information, see  CreateWebACL .
    
    """
    pass

def create_rule_group(Name=None, MetricName=None, ChangeToken=None, Tags=None):
    """
    Creates a RuleGroup . A rule group is a collection of predefined rules that you add to a web ACL. You use  UpdateRuleGroup to add rules to the rule group.
    Rule groups are subject to the following limits:
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_rule_group(
        Name='string',
        MetricName='string',
        ChangeToken='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nA friendly name or description of the RuleGroup . You can\'t change Name after you create a RuleGroup .\n

    :type MetricName: string
    :param MetricName: [REQUIRED]\nA friendly name or description for the metrics for this RuleGroup . The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can\'t contain whitespace or metric names reserved for AWS WAF, including 'All' and 'Default_Action.' You can\'t change the name of the metric after you create the RuleGroup .\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :type Tags: list
    :param Tags: \n(dict) --\nNote\nThis is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.\n\nFor the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.\n\nA tag associated with an AWS resource. Tags are key:value pairs that you can use to categorize and manage your resources, for purposes like billing. For example, you might set the tag key to 'customer' and the value to the customer name or ID. You can specify one or more tags to add to each AWS resource, up to 50 tags for a resource.\nTagging is only available through the API, SDKs, and CLI. You can\'t manage or view tags through the AWS WAF Classic console. You can tag the AWS resources that you manage through AWS WAF Classic: web ACLs, rule groups, and rules.\n\nKey (string) -- [REQUIRED]\nValue (string) -- [REQUIRED]\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'RuleGroup': {
        'RuleGroupId': 'string',
        'Name': 'string',
        'MetricName': 'string'
    },
    'ChangeToken': 'string'
}


Response Structure

(dict) --

RuleGroup (dict) --
An empty  RuleGroup .

RuleGroupId (string) --
A unique identifier for a RuleGroup . You use RuleGroupId to get more information about a RuleGroup (see  GetRuleGroup ), update a RuleGroup (see  UpdateRuleGroup ), insert a RuleGroup into a WebACL or delete a one from a WebACL (see  UpdateWebACL ), or delete a RuleGroup from AWS WAF (see  DeleteRuleGroup ).

RuleGroupId is returned by  CreateRuleGroup and by  ListRuleGroups .


Name (string) --
The friendly name or description for the RuleGroup . You can\'t change the name of a RuleGroup after you create it.

MetricName (string) --
A friendly name or description for the metrics for this RuleGroup . The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can\'t contain whitespace or metric names reserved for AWS WAF, including "All" and "Default_Action." You can\'t change the name of the metric after you create the RuleGroup .



ChangeToken (string) --
The ChangeToken that you used to submit the CreateRuleGroup request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFDisallowedNameException
WAFRegional.Client.exceptions.WAFLimitsExceededException
WAFRegional.Client.exceptions.WAFTagOperationException
WAFRegional.Client.exceptions.WAFTagOperationInternalErrorException
WAFRegional.Client.exceptions.WAFBadRequestException


    :return: {
        'RuleGroup': {
            'RuleGroupId': 'string',
            'Name': 'string',
            'MetricName': 'string'
        },
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    Name (string) -- [REQUIRED]
    A friendly name or description of the  RuleGroup . You can\'t change Name after you create a RuleGroup .
    
    MetricName (string) -- [REQUIRED]
    A friendly name or description for the metrics for this RuleGroup . The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can\'t contain whitespace or metric names reserved for AWS WAF, including "All" and "Default_Action." You can\'t change the name of the metric after you create the RuleGroup .
    
    ChangeToken (string) -- [REQUIRED]
    The value returned by the most recent call to  GetChangeToken .
    
    Tags (list) -- 
    (dict) --
    Note
    This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.
    
    For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.
    
    A tag associated with an AWS resource. Tags are key:value pairs that you can use to categorize and manage your resources, for purposes like billing. For example, you might set the tag key to "customer" and the value to the customer name or ID. You can specify one or more tags to add to each AWS resource, up to 50 tags for a resource.
    Tagging is only available through the API, SDKs, and CLI. You can\'t manage or view tags through the AWS WAF Classic console. You can tag the AWS resources that you manage through AWS WAF Classic: web ACLs, rule groups, and rules.
    
    Key (string) -- [REQUIRED]
    Value (string) -- [REQUIRED]
    
    
    
    
    
    """
    pass

def create_size_constraint_set(Name=None, ChangeToken=None):
    """
    Creates a SizeConstraintSet . You then use  UpdateSizeConstraintSet to identify the part of a web request that you want AWS WAF to check for length, such as the length of the User-Agent header or the length of the query string. For example, you can create a SizeConstraintSet that matches any requests that have a query string that is longer than 100 bytes. You can then configure AWS WAF to reject those requests.
    To create and configure a SizeConstraintSet , perform the following steps:
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example creates size constraint set named MySampleSizeConstraintSet.
    Expected Output:
    
    :example: response = client.create_size_constraint_set(
        Name='string',
        ChangeToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nA friendly name or description of the SizeConstraintSet . You can\'t change Name after you create a SizeConstraintSet .\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'SizeConstraintSet': {
        'SizeConstraintSetId': 'string',
        'Name': 'string',
        'SizeConstraints': [
            {
                'FieldToMatch': {
                    'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY'|'SINGLE_QUERY_ARG'|'ALL_QUERY_ARGS',
                    'Data': 'string'
                },
                'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE',
                'ComparisonOperator': 'EQ'|'NE'|'LE'|'LT'|'GE'|'GT',
                'Size': 123
            },
        ]
    },
    'ChangeToken': 'string'
}


Response Structure

(dict) --

SizeConstraintSet (dict) --
A  SizeConstraintSet that contains no SizeConstraint objects.

SizeConstraintSetId (string) --
A unique identifier for a SizeConstraintSet . You use SizeConstraintSetId to get information about a SizeConstraintSet (see  GetSizeConstraintSet ), update a SizeConstraintSet (see  UpdateSizeConstraintSet ), insert a SizeConstraintSet into a Rule or delete one from a Rule (see  UpdateRule ), and delete a SizeConstraintSet from AWS WAF (see  DeleteSizeConstraintSet ).

SizeConstraintSetId is returned by  CreateSizeConstraintSet and by  ListSizeConstraintSets .


Name (string) --
The name, if any, of the SizeConstraintSet .

SizeConstraints (list) --
Specifies the parts of web requests that you want to inspect the size of.

(dict) --

Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


Specifies a constraint on the size of a part of the web request. AWS WAF uses the Size , ComparisonOperator , and FieldToMatch to build an expression in the form of "Size ComparisonOperator size in bytes of FieldToMatch ". If that expression is true, the SizeConstraint is considered to match.

FieldToMatch (dict) --
Specifies where in a web request to look for the size constraint.

Type (string) --
The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:

HEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .
METHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .
QUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.
URI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .
BODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .
SINGLE_QUERY_ARG : The parameter in the query string that you will inspect, such as UserName or SalesRegion . The maximum length for SINGLE_QUERY_ARG is 30 characters.
ALL_QUERY_ARGS : Similar to SINGLE_QUERY_ARG , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in TargetString .


Data (string) --
When the value of Type is HEADER , enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer . The name of the header is not case sensitive.
When the value of Type is SINGLE_QUERY_ARG , enter the name of the parameter that you want AWS WAF to search, for example, UserName or SalesRegion . The parameter name is not case sensitive.
If the value of Type is any other value, omit Data .



TextTransformation (string) --
Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on FieldToMatch before inspecting it for a match.
You can only specify a single type of TextTransformation.
Note that if you choose BODY for the value of Type , you must choose NONE for TextTransformation because CloudFront forwards only the first 8192 bytes for inspection.

NONE

Specify NONE if you don\'t want to perform any text transformations.

CMD_LINE

When you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: " \' ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE

Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.
HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a "less than" symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE

Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE

Use this option to decode a URL-encoded value.

ComparisonOperator (string) --
The type of comparison you want AWS WAF to perform. AWS WAF uses this in combination with the provided Size and FieldToMatch to build an expression in the form of "Size ComparisonOperator size in bytes of FieldToMatch ". If that expression is true, the SizeConstraint is considered to match.

EQ : Used to test if the Size is equal to the size of the FieldToMatch
NE : Used to test if the Size is not equal to the size of the FieldToMatch
LE : Used to test if the Size is less than or equal to the size of the FieldToMatch
LT : Used to test if the Size is strictly less than the size of the FieldToMatch
GE : Used to test if the Size is greater than or equal to the size of the FieldToMatch
GT : Used to test if the Size is strictly greater than the size of the FieldToMatch


Size (integer) --
The size in bytes that you want AWS WAF to compare against the size of the specified FieldToMatch . AWS WAF uses this in combination with ComparisonOperator and FieldToMatch to build an expression in the form of "Size ComparisonOperator size in bytes of FieldToMatch ". If that expression is true, the SizeConstraint is considered to match.
Valid values for size are 0 - 21474836480 bytes (0 - 20 GB).
If you specify URI for the value of Type , the / in the URI counts as one character. For example, the URI /logo.jpg is nine characters long.







ChangeToken (string) --
The ChangeToken that you used to submit the CreateSizeConstraintSet request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFDisallowedNameException
WAFRegional.Client.exceptions.WAFInvalidParameterException
WAFRegional.Client.exceptions.WAFLimitsExceededException

Examples
The following example creates size constraint set named MySampleSizeConstraintSet.
response = client.create_size_constraint_set(
    ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    Name='MySampleSizeConstraintSet',
)

print(response)


Expected Output:
{
    'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    'SizeConstraintSet': {
        'Name': 'MySampleSizeConstraintSet',
        'SizeConstraintSetId': 'example1ds3t-46da-4fdb-b8d5-abc321j569j5',
        'SizeConstraints': [
            {
                'ComparisonOperator': 'GT',
                'FieldToMatch': {
                    'Type': 'QUERY_STRING',
                },
                'Size': 0,
                'TextTransformation': 'NONE',
            },
        ],
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'SizeConstraintSet': {
            'SizeConstraintSetId': 'string',
            'Name': 'string',
            'SizeConstraints': [
                {
                    'FieldToMatch': {
                        'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY'|'SINGLE_QUERY_ARG'|'ALL_QUERY_ARGS',
                        'Data': 'string'
                    },
                    'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE',
                    'ComparisonOperator': 'EQ'|'NE'|'LE'|'LT'|'GE'|'GT',
                    'Size': 123
                },
            ]
        },
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    Name (string) -- [REQUIRED]
    A friendly name or description of the  SizeConstraintSet . You can\'t change Name after you create a SizeConstraintSet .
    
    ChangeToken (string) -- [REQUIRED]
    The value returned by the most recent call to  GetChangeToken .
    
    
    """
    pass

def create_sql_injection_match_set(Name=None, ChangeToken=None):
    """
    Creates a  SqlInjectionMatchSet , which you use to allow, block, or count requests that contain snippets of SQL code in a specified part of web requests. AWS WAF searches for character sequences that are likely to be malicious strings.
    To create and configure a SqlInjectionMatchSet , perform the following steps:
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example creates a SQL injection match set named MySQLInjectionMatchSet.
    Expected Output:
    
    :example: response = client.create_sql_injection_match_set(
        Name='string',
        ChangeToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nA friendly name or description for the SqlInjectionMatchSet that you\'re creating. You can\'t change Name after you create the SqlInjectionMatchSet .\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'SqlInjectionMatchSet': {
        'SqlInjectionMatchSetId': 'string',
        'Name': 'string',
        'SqlInjectionMatchTuples': [
            {
                'FieldToMatch': {
                    'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY'|'SINGLE_QUERY_ARG'|'ALL_QUERY_ARGS',
                    'Data': 'string'
                },
                'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
            },
        ]
    },
    'ChangeToken': 'string'
}


Response Structure

(dict) --
The response to a CreateSqlInjectionMatchSet request.

SqlInjectionMatchSet (dict) --
A  SqlInjectionMatchSet .

SqlInjectionMatchSetId (string) --
A unique identifier for a SqlInjectionMatchSet . You use SqlInjectionMatchSetId to get information about a SqlInjectionMatchSet (see  GetSqlInjectionMatchSet ), update a SqlInjectionMatchSet (see  UpdateSqlInjectionMatchSet ), insert a SqlInjectionMatchSet into a Rule or delete one from a Rule (see  UpdateRule ), and delete a SqlInjectionMatchSet from AWS WAF (see  DeleteSqlInjectionMatchSet ).

SqlInjectionMatchSetId is returned by  CreateSqlInjectionMatchSet and by  ListSqlInjectionMatchSets .


Name (string) --
The name, if any, of the SqlInjectionMatchSet .

SqlInjectionMatchTuples (list) --
Specifies the parts of web requests that you want to inspect for snippets of malicious SQL code.

(dict) --

Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


Specifies the part of a web request that you want AWS WAF to inspect for snippets of malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.

FieldToMatch (dict) --
Specifies where in a web request to look for snippets of malicious SQL code.

Type (string) --
The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:

HEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .
METHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .
QUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.
URI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .
BODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .
SINGLE_QUERY_ARG : The parameter in the query string that you will inspect, such as UserName or SalesRegion . The maximum length for SINGLE_QUERY_ARG is 30 characters.
ALL_QUERY_ARGS : Similar to SINGLE_QUERY_ARG , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in TargetString .


Data (string) --
When the value of Type is HEADER , enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer . The name of the header is not case sensitive.
When the value of Type is SINGLE_QUERY_ARG , enter the name of the parameter that you want AWS WAF to search, for example, UserName or SalesRegion . The parameter name is not case sensitive.
If the value of Type is any other value, omit Data .



TextTransformation (string) --
Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on FieldToMatch before inspecting it for a match.
You can only specify a single type of TextTransformation.

CMD_LINE

When you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: " \' ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE

Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.
HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a "less than" symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE

Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE

Use this option to decode a URL-encoded value.

NONE

Specify NONE if you don\'t want to perform any text transformations.







ChangeToken (string) --
The ChangeToken that you used to submit the CreateSqlInjectionMatchSet request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFDisallowedNameException
WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFInvalidParameterException
WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFLimitsExceededException

Examples
The following example creates a SQL injection match set named MySQLInjectionMatchSet.
response = client.create_sql_injection_match_set(
    ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    Name='MySQLInjectionMatchSet',
)

print(response)


Expected Output:
{
    'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    'SqlInjectionMatchSet': {
        'Name': 'MySQLInjectionMatchSet',
        'SqlInjectionMatchSetId': 'example1ds3t-46da-4fdb-b8d5-abc321j569j5',
        'SqlInjectionMatchTuples': [
            {
                'FieldToMatch': {
                    'Type': 'QUERY_STRING',
                },
                'TextTransformation': 'URL_DECODE',
            },
        ],
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'SqlInjectionMatchSet': {
            'SqlInjectionMatchSetId': 'string',
            'Name': 'string',
            'SqlInjectionMatchTuples': [
                {
                    'FieldToMatch': {
                        'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY'|'SINGLE_QUERY_ARG'|'ALL_QUERY_ARGS',
                        'Data': 'string'
                    },
                    'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                },
            ]
        },
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    Name (string) -- [REQUIRED]
    A friendly name or description for the  SqlInjectionMatchSet that you\'re creating. You can\'t change Name after you create the SqlInjectionMatchSet .
    
    ChangeToken (string) -- [REQUIRED]
    The value returned by the most recent call to  GetChangeToken .
    
    
    """
    pass

def create_web_acl(Name=None, MetricName=None, DefaultAction=None, ChangeToken=None, Tags=None):
    """
    Creates a WebACL , which contains the Rules that identify the CloudFront web requests that you want to allow, block, or count. AWS WAF evaluates Rules in order based on the value of Priority for each Rule .
    You also specify a default action, either ALLOW or BLOCK . If a web request doesn\'t match any of the Rules in a WebACL , AWS WAF responds to the request with the default action.
    To create and configure a WebACL , perform the following steps:
    For more information about how to use the AWS WAF API, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example creates a web ACL named CreateExample.
    Expected Output:
    
    :example: response = client.create_web_acl(
        Name='string',
        MetricName='string',
        DefaultAction={
            'Type': 'BLOCK'|'ALLOW'|'COUNT'
        },
        ChangeToken='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nA friendly name or description of the WebACL . You can\'t change Name after you create the WebACL .\n

    :type MetricName: string
    :param MetricName: [REQUIRED]\nA friendly name or description for the metrics for this WebACL .The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can\'t contain whitespace or metric names reserved for AWS WAF, including 'All' and 'Default_Action.' You can\'t change MetricName after you create the WebACL .\n

    :type DefaultAction: dict
    :param DefaultAction: [REQUIRED]\nThe action that you want AWS WAF to take when a request doesn\'t match the criteria specified in any of the Rule objects that are associated with the WebACL .\n\nType (string) -- [REQUIRED]Specifies how you want AWS WAF to respond to requests that match the settings in a Rule . Valid settings include the following:\n\nALLOW : AWS WAF allows requests\nBLOCK : AWS WAF blocks requests\nCOUNT : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can\'t specify COUNT for the default action for a WebACL .\n\n\n\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :type Tags: list
    :param Tags: \n(dict) --\nNote\nThis is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.\n\nFor the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.\n\nA tag associated with an AWS resource. Tags are key:value pairs that you can use to categorize and manage your resources, for purposes like billing. For example, you might set the tag key to 'customer' and the value to the customer name or ID. You can specify one or more tags to add to each AWS resource, up to 50 tags for a resource.\nTagging is only available through the API, SDKs, and CLI. You can\'t manage or view tags through the AWS WAF Classic console. You can tag the AWS resources that you manage through AWS WAF Classic: web ACLs, rule groups, and rules.\n\nKey (string) -- [REQUIRED]\nValue (string) -- [REQUIRED]\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'WebACL': {
        'WebACLId': 'string',
        'Name': 'string',
        'MetricName': 'string',
        'DefaultAction': {
            'Type': 'BLOCK'|'ALLOW'|'COUNT'
        },
        'Rules': [
            {
                'Priority': 123,
                'RuleId': 'string',
                'Action': {
                    'Type': 'BLOCK'|'ALLOW'|'COUNT'
                },
                'OverrideAction': {
                    'Type': 'NONE'|'COUNT'
                },
                'Type': 'REGULAR'|'RATE_BASED'|'GROUP',
                'ExcludedRules': [
                    {
                        'RuleId': 'string'
                    },
                ]
            },
        ],
        'WebACLArn': 'string'
    },
    'ChangeToken': 'string'
}


Response Structure

(dict) --

WebACL (dict) --
The  WebACL returned in the CreateWebACL response.

WebACLId (string) --
A unique identifier for a WebACL . You use WebACLId to get information about a WebACL (see  GetWebACL ), update a WebACL (see  UpdateWebACL ), and delete a WebACL from AWS WAF (see  DeleteWebACL ).

WebACLId is returned by  CreateWebACL and by  ListWebACLs .


Name (string) --
A friendly name or description of the WebACL . You can\'t change the name of a WebACL after you create it.

MetricName (string) --
A friendly name or description for the metrics for this WebACL . The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can\'t contain whitespace or metric names reserved for AWS WAF, including "All" and "Default_Action." You can\'t change MetricName after you create the WebACL .

DefaultAction (dict) --
The action to perform if none of the Rules contained in the WebACL match. The action is specified by the  WafAction object.

Type (string) --
Specifies how you want AWS WAF to respond to requests that match the settings in a Rule . Valid settings include the following:

ALLOW : AWS WAF allows requests
BLOCK : AWS WAF blocks requests
COUNT : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can\'t specify COUNT for the default action for a WebACL .




Rules (list) --
An array that contains the action for each Rule in a WebACL , the priority of the Rule , and the ID of the Rule .

(dict) --

Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


The ActivatedRule object in an  UpdateWebACL request specifies a Rule that you want to insert or delete, the priority of the Rule in the WebACL , and the action that you want AWS WAF to take when a web request matches the Rule (ALLOW , BLOCK , or COUNT ).
To specify whether to insert or delete a Rule , use the Action parameter in the  WebACLUpdate data type.

Priority (integer) --
Specifies the order in which the Rules in a WebACL are evaluated. Rules with a lower value for Priority are evaluated before Rules with a higher value. The value must be a unique integer. If you add multiple Rules to a WebACL , the values don\'t need to be consecutive.

RuleId (string) --
The RuleId for a Rule . You use RuleId to get more information about a Rule (see  GetRule ), update a Rule (see  UpdateRule ), insert a Rule into a WebACL or delete a one from a WebACL (see  UpdateWebACL ), or delete a Rule from AWS WAF (see  DeleteRule ).

RuleId is returned by  CreateRule and by  ListRules .


Action (dict) --
Specifies the action that CloudFront or AWS WAF takes when a web request matches the conditions in the Rule . Valid values for Action include the following:

ALLOW : CloudFront responds with the requested object.
BLOCK : CloudFront responds with an HTTP 403 (Forbidden) status code.
COUNT : AWS WAF increments a counter of requests that match the conditions in the rule and then continues to inspect the web request based on the remaining rules in the web ACL.


ActivatedRule|OverrideAction applies only when updating or adding a RuleGroup to a WebACL . In this case, you do not use ActivatedRule|Action . For all other update requests, ActivatedRule|Action is used instead of ActivatedRule|OverrideAction .


Type (string) --
Specifies how you want AWS WAF to respond to requests that match the settings in a Rule . Valid settings include the following:

ALLOW : AWS WAF allows requests
BLOCK : AWS WAF blocks requests
COUNT : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can\'t specify COUNT for the default action for a WebACL .




OverrideAction (dict) --
Use the OverrideAction to test your RuleGroup .
Any rule in a RuleGroup can potentially block a request. If you set the OverrideAction to None , the RuleGroup will block a request if any individual rule in the RuleGroup matches the request and is configured to block that request. However if you first want to test the RuleGroup , set the OverrideAction to Count . The RuleGroup will then override any block action specified by individual rules contained within the group. Instead of blocking matching requests, those requests will be counted. You can view a record of counted requests using  GetSampledRequests .

ActivatedRule|OverrideAction applies only when updating or adding a RuleGroup to a WebACL . In this case you do not use ActivatedRule|Action . For all other update requests, ActivatedRule|Action is used instead of ActivatedRule|OverrideAction .


Type (string) --

COUNT overrides the action specified by the individual rule within a RuleGroup . If set to NONE , the rule\'s action will take place.




Type (string) --
The rule type, either REGULAR , as defined by  Rule , RATE_BASED , as defined by  RateBasedRule , or GROUP , as defined by  RuleGroup . The default is REGULAR. Although this field is optional, be aware that if you try to add a RATE_BASED rule to a web ACL without setting the type, the  UpdateWebACL request will fail because the request tries to add a REGULAR rule with the specified ID, which does not exist.

ExcludedRules (list) --
An array of rules to exclude from a rule group. This is applicable only when the ActivatedRule refers to a RuleGroup .
Sometimes it is necessary to troubleshoot rule groups that are blocking traffic unexpectedly (false positives). One troubleshooting technique is to identify the specific rule within the rule group that is blocking the legitimate traffic and then disable (exclude) that particular rule. You can exclude rules from both your own rule groups and AWS Marketplace rule groups that have been associated with a web ACL.
Specifying ExcludedRules does not remove those rules from the rule group. Rather, it changes the action for the rules to COUNT . Therefore, requests that match an ExcludedRule are counted but not blocked. The RuleGroup owner will receive COUNT metrics for each ExcludedRule .
If you want to exclude rules from a rule group that is already associated with a web ACL, perform the following steps:

Use the AWS WAF logs to identify the IDs of the rules that you want to exclude. For more information about the logs, see Logging Web ACL Traffic Information .
Submit an  UpdateWebACL request that has two actions:
The first action deletes the existing rule group from the web ACL. That is, in the  UpdateWebACL request, the first Updates:Action should be DELETE and Updates:ActivatedRule:RuleId should be the rule group that contains the rules that you want to exclude.
The second action inserts the same rule group back in, but specifying the rules to exclude. That is, the second Updates:Action should be INSERT , Updates:ActivatedRule:RuleId should be the rule group that you just removed, and ExcludedRules should contain the rules that you want to exclude.




(dict) --

Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


The rule to exclude from a rule group. This is applicable only when the ActivatedRule refers to a RuleGroup . The rule must belong to the RuleGroup that is specified by the ActivatedRule .

RuleId (string) --
The unique identifier for the rule to exclude from the rule group.









WebACLArn (string) --
Tha Amazon Resource Name (ARN) of the web ACL.



ChangeToken (string) --
The ChangeToken that you used to submit the CreateWebACL request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFDisallowedNameException
WAFRegional.Client.exceptions.WAFInvalidParameterException
WAFRegional.Client.exceptions.WAFLimitsExceededException
WAFRegional.Client.exceptions.WAFTagOperationException
WAFRegional.Client.exceptions.WAFTagOperationInternalErrorException
WAFRegional.Client.exceptions.WAFBadRequestException

Examples
The following example creates a web ACL named CreateExample.
response = client.create_web_acl(
    ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    DefaultAction={
        'Type': 'ALLOW',
    },
    MetricName='CreateExample',
    Name='CreateExample',
)

print(response)


Expected Output:
{
    'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    'WebACL': {
        'DefaultAction': {
            'Type': 'ALLOW',
        },
        'MetricName': 'CreateExample',
        'Name': 'CreateExample',
        'Rules': [
            {
                'Action': {
                    'Type': 'ALLOW',
                },
                'Priority': 1,
                'RuleId': 'WAFRule-1-Example',
            },
        ],
        'WebACLId': 'example-46da-4444-5555-example',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'WebACL': {
            'WebACLId': 'string',
            'Name': 'string',
            'MetricName': 'string',
            'DefaultAction': {
                'Type': 'BLOCK'|'ALLOW'|'COUNT'
            },
            'Rules': [
                {
                    'Priority': 123,
                    'RuleId': 'string',
                    'Action': {
                        'Type': 'BLOCK'|'ALLOW'|'COUNT'
                    },
                    'OverrideAction': {
                        'Type': 'NONE'|'COUNT'
                    },
                    'Type': 'REGULAR'|'RATE_BASED'|'GROUP',
                    'ExcludedRules': [
                        {
                            'RuleId': 'string'
                        },
                    ]
                },
            ],
            'WebACLArn': 'string'
        },
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    Name (string) -- [REQUIRED]
    A friendly name or description of the  WebACL . You can\'t change Name after you create the WebACL .
    
    MetricName (string) -- [REQUIRED]
    A friendly name or description for the metrics for this WebACL .The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can\'t contain whitespace or metric names reserved for AWS WAF, including "All" and "Default_Action." You can\'t change MetricName after you create the WebACL .
    
    DefaultAction (dict) -- [REQUIRED]
    The action that you want AWS WAF to take when a request doesn\'t match the criteria specified in any of the Rule objects that are associated with the WebACL .
    
    Type (string) -- [REQUIRED]Specifies how you want AWS WAF to respond to requests that match the settings in a Rule . Valid settings include the following:
    
    ALLOW : AWS WAF allows requests
    BLOCK : AWS WAF blocks requests
    COUNT : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can\'t specify COUNT for the default action for a WebACL .
    
    
    
    
    ChangeToken (string) -- [REQUIRED]
    The value returned by the most recent call to  GetChangeToken .
    
    Tags (list) -- 
    (dict) --
    Note
    This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.
    
    For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.
    
    A tag associated with an AWS resource. Tags are key:value pairs that you can use to categorize and manage your resources, for purposes like billing. For example, you might set the tag key to "customer" and the value to the customer name or ID. You can specify one or more tags to add to each AWS resource, up to 50 tags for a resource.
    Tagging is only available through the API, SDKs, and CLI. You can\'t manage or view tags through the AWS WAF Classic console. You can tag the AWS resources that you manage through AWS WAF Classic: web ACLs, rule groups, and rules.
    
    Key (string) -- [REQUIRED]
    Value (string) -- [REQUIRED]
    
    
    
    
    
    """
    pass

def create_web_acl_migration_stack(WebACLId=None, S3BucketName=None, IgnoreUnsupportedType=None):
    """
    Creates an AWS CloudFormation WAFV2 template for the specified web ACL in the specified Amazon S3 bucket. Then, in CloudFormation, you create a stack from the template, to create the web ACL and its resources in AWS WAFV2. Use this to migrate your AWS WAF Classic web ACL to the latest version of AWS WAF.
    This is part of a larger migration procedure for web ACLs from AWS WAF Classic to the latest version of AWS WAF. For the full procedure, including caveats and manual steps to complete the migration and switch over to the new web ACL, see Migrating your AWS WAF Classic resources to AWS WAF in the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_web_acl_migration_stack(
        WebACLId='string',
        S3BucketName='string',
        IgnoreUnsupportedType=True|False
    )
    
    
    :type WebACLId: string
    :param WebACLId: [REQUIRED]\nThe UUID of the WAF Classic web ACL that you want to migrate to WAF v2.\n

    :type S3BucketName: string
    :param S3BucketName: [REQUIRED]\nThe name of the Amazon S3 bucket to store the CloudFormation template in. The S3 bucket must be configured as follows for the migration:\n\nThe bucket name must start with aws-waf-migration- . For example, aws-waf-migration-my-web-acl .\nThe bucket must be in the Region where you are deploying the template. For example, for a web ACL in us-west-2, you must use an Amazon S3 bucket in us-west-2 and you must deploy the template stack to us-west-2.\nThe bucket policies must permit the migration process to write data. For listings of the bucket policies, see the Examples section.\n\n

    :type IgnoreUnsupportedType: boolean
    :param IgnoreUnsupportedType: [REQUIRED]\nIndicates whether to exclude entities that can\'t be migrated or to stop the migration. Set this to true to ignore unsupported entities in the web ACL during the migration. Otherwise, if AWS WAF encounters unsupported entities, it stops the process and throws an exception.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'S3ObjectUrl': 'string'
}


Response Structure

(dict) --

S3ObjectUrl (string) --
The URL of the template created in Amazon S3.







Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidParameterException
WAFRegional.Client.exceptions.WAFInvalidOperationException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFEntityMigrationException


    :return: {
        'S3ObjectUrl': 'string'
    }
    
    
    :returns: 
    WAFRegional.Client.exceptions.WAFInternalErrorException
    WAFRegional.Client.exceptions.WAFInvalidParameterException
    WAFRegional.Client.exceptions.WAFInvalidOperationException
    WAFRegional.Client.exceptions.WAFNonexistentItemException
    WAFRegional.Client.exceptions.WAFEntityMigrationException
    
    """
    pass

def create_xss_match_set(Name=None, ChangeToken=None):
    """
    Creates an  XssMatchSet , which you use to allow, block, or count requests that contain cross-site scripting attacks in the specified part of web requests. AWS WAF searches for character sequences that are likely to be malicious strings.
    To create and configure an XssMatchSet , perform the following steps:
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example creates an XSS match set named MySampleXssMatchSet.
    Expected Output:
    
    :example: response = client.create_xss_match_set(
        Name='string',
        ChangeToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nA friendly name or description for the XssMatchSet that you\'re creating. You can\'t change Name after you create the XssMatchSet .\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'XssMatchSet': {
        'XssMatchSetId': 'string',
        'Name': 'string',
        'XssMatchTuples': [
            {
                'FieldToMatch': {
                    'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY'|'SINGLE_QUERY_ARG'|'ALL_QUERY_ARGS',
                    'Data': 'string'
                },
                'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
            },
        ]
    },
    'ChangeToken': 'string'
}


Response Structure

(dict) --
The response to a CreateXssMatchSet request.

XssMatchSet (dict) --
An  XssMatchSet .

XssMatchSetId (string) --
A unique identifier for an XssMatchSet . You use XssMatchSetId to get information about an XssMatchSet (see  GetXssMatchSet ), update an XssMatchSet (see  UpdateXssMatchSet ), insert an XssMatchSet into a Rule or delete one from a Rule (see  UpdateRule ), and delete an XssMatchSet from AWS WAF (see  DeleteXssMatchSet ).

XssMatchSetId is returned by  CreateXssMatchSet and by  ListXssMatchSets .


Name (string) --
The name, if any, of the XssMatchSet .

XssMatchTuples (list) --
Specifies the parts of web requests that you want to inspect for cross-site scripting attacks.

(dict) --

Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


Specifies the part of a web request that you want AWS WAF to inspect for cross-site scripting attacks and, if you want AWS WAF to inspect a header, the name of the header.

FieldToMatch (dict) --
Specifies where in a web request to look for cross-site scripting attacks.

Type (string) --
The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:

HEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .
METHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .
QUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.
URI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .
BODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .
SINGLE_QUERY_ARG : The parameter in the query string that you will inspect, such as UserName or SalesRegion . The maximum length for SINGLE_QUERY_ARG is 30 characters.
ALL_QUERY_ARGS : Similar to SINGLE_QUERY_ARG , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in TargetString .


Data (string) --
When the value of Type is HEADER , enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer . The name of the header is not case sensitive.
When the value of Type is SINGLE_QUERY_ARG , enter the name of the parameter that you want AWS WAF to search, for example, UserName or SalesRegion . The parameter name is not case sensitive.
If the value of Type is any other value, omit Data .



TextTransformation (string) --
Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on FieldToMatch before inspecting it for a match.
You can only specify a single type of TextTransformation.

CMD_LINE

When you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: " \' ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE

Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.
HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a "less than" symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE

Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE

Use this option to decode a URL-encoded value.

NONE

Specify NONE if you don\'t want to perform any text transformations.







ChangeToken (string) --
The ChangeToken that you used to submit the CreateXssMatchSet request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFDisallowedNameException
WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFInvalidParameterException
WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFLimitsExceededException

Examples
The following example creates an XSS match set named MySampleXssMatchSet.
response = client.create_xss_match_set(
    ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    Name='MySampleXssMatchSet',
)

print(response)


Expected Output:
{
    'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    'XssMatchSet': {
        'Name': 'MySampleXssMatchSet',
        'XssMatchSetId': 'example1ds3t-46da-4fdb-b8d5-abc321j569j5',
        'XssMatchTuples': [
            {
                'FieldToMatch': {
                    'Type': 'QUERY_STRING',
                },
                'TextTransformation': 'URL_DECODE',
            },
        ],
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'XssMatchSet': {
            'XssMatchSetId': 'string',
            'Name': 'string',
            'XssMatchTuples': [
                {
                    'FieldToMatch': {
                        'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY'|'SINGLE_QUERY_ARG'|'ALL_QUERY_ARGS',
                        'Data': 'string'
                    },
                    'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                },
            ]
        },
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    Name (string) -- [REQUIRED]
    A friendly name or description for the  XssMatchSet that you\'re creating. You can\'t change Name after you create the XssMatchSet .
    
    ChangeToken (string) -- [REQUIRED]
    The value returned by the most recent call to  GetChangeToken .
    
    
    """
    pass

def delete_byte_match_set(ByteMatchSetId=None, ChangeToken=None):
    """
    Permanently deletes a  ByteMatchSet . You can\'t delete a ByteMatchSet if it\'s still used in any Rules or if it still includes any  ByteMatchTuple objects (any filters).
    If you just want to remove a ByteMatchSet from a Rule , use  UpdateRule .
    To permanently delete a ByteMatchSet , perform the following steps:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example deletes a byte match set with the ID exampleIDs3t-46da-4fdb-b8d5-abc321j569j5.
    Expected Output:
    
    :example: response = client.delete_byte_match_set(
        ByteMatchSetId='string',
        ChangeToken='string'
    )
    
    
    :type ByteMatchSetId: string
    :param ByteMatchSetId: [REQUIRED]\nThe ByteMatchSetId of the ByteMatchSet that you want to delete. ByteMatchSetId is returned by CreateByteMatchSet and by ListByteMatchSets .\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChangeToken': 'string'
}


Response Structure

(dict) --

ChangeToken (string) --
The ChangeToken that you used to submit the DeleteByteMatchSet request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFReferencedItemException
WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFNonEmptyEntityException

Examples
The following example deletes a byte match set with the ID exampleIDs3t-46da-4fdb-b8d5-abc321j569j5.
response = client.delete_byte_match_set(
    ByteMatchSetId='exampleIDs3t-46da-4fdb-b8d5-abc321j569j5',
    ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
)

print(response)


Expected Output:
{
    'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    ByteMatchSetId (string) -- [REQUIRED]
    The ByteMatchSetId of the  ByteMatchSet that you want to delete. ByteMatchSetId is returned by  CreateByteMatchSet and by  ListByteMatchSets .
    
    ChangeToken (string) -- [REQUIRED]
    The value returned by the most recent call to  GetChangeToken .
    
    
    """
    pass

def delete_geo_match_set(GeoMatchSetId=None, ChangeToken=None):
    """
    Permanently deletes a  GeoMatchSet . You can\'t delete a GeoMatchSet if it\'s still used in any Rules or if it still includes any countries.
    If you just want to remove a GeoMatchSet from a Rule , use  UpdateRule .
    To permanently delete a GeoMatchSet from AWS WAF, perform the following steps:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_geo_match_set(
        GeoMatchSetId='string',
        ChangeToken='string'
    )
    
    
    :type GeoMatchSetId: string
    :param GeoMatchSetId: [REQUIRED]\nThe GeoMatchSetID of the GeoMatchSet that you want to delete. GeoMatchSetId is returned by CreateGeoMatchSet and by ListGeoMatchSets .\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChangeToken': 'string'
}


Response Structure

(dict) --

ChangeToken (string) --
The ChangeToken that you used to submit the DeleteGeoMatchSet request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFReferencedItemException
WAFRegional.Client.exceptions.WAFNonEmptyEntityException


    :return: {
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    GeoMatchSetId (string) -- [REQUIRED]
    The GeoMatchSetID of the  GeoMatchSet that you want to delete. GeoMatchSetId is returned by  CreateGeoMatchSet and by  ListGeoMatchSets .
    
    ChangeToken (string) -- [REQUIRED]
    The value returned by the most recent call to  GetChangeToken .
    
    
    """
    pass

def delete_ip_set(IPSetId=None, ChangeToken=None):
    """
    Permanently deletes an  IPSet . You can\'t delete an IPSet if it\'s still used in any Rules or if it still includes any IP addresses.
    If you just want to remove an IPSet from a Rule , use  UpdateRule .
    To permanently delete an IPSet from AWS WAF, perform the following steps:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example deletes an IP match set  with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    Expected Output:
    
    :example: response = client.delete_ip_set(
        IPSetId='string',
        ChangeToken='string'
    )
    
    
    :type IPSetId: string
    :param IPSetId: [REQUIRED]\nThe IPSetId of the IPSet that you want to delete. IPSetId is returned by CreateIPSet and by ListIPSets .\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChangeToken': 'string'
}


Response Structure

(dict) --

ChangeToken (string) --
The ChangeToken that you used to submit the DeleteIPSet request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFReferencedItemException
WAFRegional.Client.exceptions.WAFNonEmptyEntityException

Examples
The following example deletes an IP match set  with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
response = client.delete_ip_set(
    ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    IPSetId='example1ds3t-46da-4fdb-b8d5-abc321j569j5',
)

print(response)


Expected Output:
{
    'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    IPSetId (string) -- [REQUIRED]
    The IPSetId of the  IPSet that you want to delete. IPSetId is returned by  CreateIPSet and by  ListIPSets .
    
    ChangeToken (string) -- [REQUIRED]
    The value returned by the most recent call to  GetChangeToken .
    
    
    """
    pass

def delete_logging_configuration(ResourceArn=None):
    """
    Permanently deletes the  LoggingConfiguration from the specified web ACL.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_logging_configuration(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the web ACL from which you want to delete the LoggingConfiguration .\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFStaleDataException


    :return: {}
    
    
    :returns: 
    WAFRegional.Client.exceptions.WAFInternalErrorException
    WAFRegional.Client.exceptions.WAFNonexistentItemException
    WAFRegional.Client.exceptions.WAFStaleDataException
    
    """
    pass

def delete_permission_policy(ResourceArn=None):
    """
    Permanently deletes an IAM policy from the specified RuleGroup.
    The user making the request must be the owner of the RuleGroup.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_permission_policy(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the RuleGroup from which you want to delete the policy.\nThe user making the request must be the owner of the RuleGroup.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFNonexistentItemException


    :return: {}
    
    
    :returns: 
    WAFRegional.Client.exceptions.WAFInternalErrorException
    WAFRegional.Client.exceptions.WAFStaleDataException
    WAFRegional.Client.exceptions.WAFNonexistentItemException
    
    """
    pass

def delete_rate_based_rule(RuleId=None, ChangeToken=None):
    """
    Permanently deletes a  RateBasedRule . You can\'t delete a rule if it\'s still used in any WebACL objects or if it still includes any predicates, such as ByteMatchSet objects.
    If you just want to remove a rule from a WebACL , use  UpdateWebACL .
    To permanently delete a RateBasedRule from AWS WAF, perform the following steps:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_rate_based_rule(
        RuleId='string',
        ChangeToken='string'
    )
    
    
    :type RuleId: string
    :param RuleId: [REQUIRED]\nThe RuleId of the RateBasedRule that you want to delete. RuleId is returned by CreateRateBasedRule and by ListRateBasedRules .\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChangeToken': 'string'
}


Response Structure

(dict) --

ChangeToken (string) --
The ChangeToken that you used to submit the DeleteRateBasedRule request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFReferencedItemException
WAFRegional.Client.exceptions.WAFNonEmptyEntityException
WAFRegional.Client.exceptions.WAFTagOperationException
WAFRegional.Client.exceptions.WAFTagOperationInternalErrorException


    :return: {
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    RuleId (string) -- [REQUIRED]
    The RuleId of the  RateBasedRule that you want to delete. RuleId is returned by  CreateRateBasedRule and by  ListRateBasedRules .
    
    ChangeToken (string) -- [REQUIRED]
    The value returned by the most recent call to  GetChangeToken .
    
    
    """
    pass

def delete_regex_match_set(RegexMatchSetId=None, ChangeToken=None):
    """
    Permanently deletes a  RegexMatchSet . You can\'t delete a RegexMatchSet if it\'s still used in any Rules or if it still includes any RegexMatchTuples objects (any filters).
    If you just want to remove a RegexMatchSet from a Rule , use  UpdateRule .
    To permanently delete a RegexMatchSet , perform the following steps:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_regex_match_set(
        RegexMatchSetId='string',
        ChangeToken='string'
    )
    
    
    :type RegexMatchSetId: string
    :param RegexMatchSetId: [REQUIRED]\nThe RegexMatchSetId of the RegexMatchSet that you want to delete. RegexMatchSetId is returned by CreateRegexMatchSet and by ListRegexMatchSets .\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChangeToken': 'string'
}


Response Structure

(dict) --

ChangeToken (string) --
The ChangeToken that you used to submit the DeleteRegexMatchSet request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFReferencedItemException
WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFNonEmptyEntityException


    :return: {
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    RegexMatchSetId (string) -- [REQUIRED]
    The RegexMatchSetId of the  RegexMatchSet that you want to delete. RegexMatchSetId is returned by  CreateRegexMatchSet and by  ListRegexMatchSets .
    
    ChangeToken (string) -- [REQUIRED]
    The value returned by the most recent call to  GetChangeToken .
    
    
    """
    pass

def delete_regex_pattern_set(RegexPatternSetId=None, ChangeToken=None):
    """
    Permanently deletes a  RegexPatternSet . You can\'t delete a RegexPatternSet if it\'s still used in any RegexMatchSet or if the RegexPatternSet is not empty.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_regex_pattern_set(
        RegexPatternSetId='string',
        ChangeToken='string'
    )
    
    
    :type RegexPatternSetId: string
    :param RegexPatternSetId: [REQUIRED]\nThe RegexPatternSetId of the RegexPatternSet that you want to delete. RegexPatternSetId is returned by CreateRegexPatternSet and by ListRegexPatternSets .\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChangeToken': 'string'
}


Response Structure

(dict) --

ChangeToken (string) --
The ChangeToken that you used to submit the DeleteRegexPatternSet request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFReferencedItemException
WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFNonEmptyEntityException


    :return: {
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    WAFRegional.Client.exceptions.WAFInternalErrorException
    WAFRegional.Client.exceptions.WAFInvalidAccountException
    WAFRegional.Client.exceptions.WAFNonexistentItemException
    WAFRegional.Client.exceptions.WAFReferencedItemException
    WAFRegional.Client.exceptions.WAFStaleDataException
    WAFRegional.Client.exceptions.WAFNonEmptyEntityException
    
    """
    pass

def delete_rule(RuleId=None, ChangeToken=None):
    """
    Permanently deletes a  Rule . You can\'t delete a Rule if it\'s still used in any WebACL objects or if it still includes any predicates, such as ByteMatchSet objects.
    If you just want to remove a Rule from a WebACL , use  UpdateWebACL .
    To permanently delete a Rule from AWS WAF, perform the following steps:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example deletes a rule with the ID WAFRule-1-Example.
    Expected Output:
    
    :example: response = client.delete_rule(
        RuleId='string',
        ChangeToken='string'
    )
    
    
    :type RuleId: string
    :param RuleId: [REQUIRED]\nThe RuleId of the Rule that you want to delete. RuleId is returned by CreateRule and by ListRules .\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChangeToken': 'string'
}


Response Structure

(dict) --

ChangeToken (string) --
The ChangeToken that you used to submit the DeleteRule request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFReferencedItemException
WAFRegional.Client.exceptions.WAFNonEmptyEntityException
WAFRegional.Client.exceptions.WAFTagOperationException
WAFRegional.Client.exceptions.WAFTagOperationInternalErrorException

Examples
The following example deletes a rule with the ID WAFRule-1-Example.
response = client.delete_rule(
    ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    RuleId='WAFRule-1-Example',
)

print(response)


Expected Output:
{
    'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    RuleId (string) -- [REQUIRED]
    The RuleId of the  Rule that you want to delete. RuleId is returned by  CreateRule and by  ListRules .
    
    ChangeToken (string) -- [REQUIRED]
    The value returned by the most recent call to  GetChangeToken .
    
    
    """
    pass

def delete_rule_group(RuleGroupId=None, ChangeToken=None):
    """
    Permanently deletes a  RuleGroup . You can\'t delete a RuleGroup if it\'s still used in any WebACL objects or if it still includes any rules.
    If you just want to remove a RuleGroup from a WebACL , use  UpdateWebACL .
    To permanently delete a RuleGroup from AWS WAF, perform the following steps:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_rule_group(
        RuleGroupId='string',
        ChangeToken='string'
    )
    
    
    :type RuleGroupId: string
    :param RuleGroupId: [REQUIRED]\nThe RuleGroupId of the RuleGroup that you want to delete. RuleGroupId is returned by CreateRuleGroup and by ListRuleGroups .\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChangeToken': 'string'
}


Response Structure

(dict) --

ChangeToken (string) --
The ChangeToken that you used to submit the DeleteRuleGroup request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFReferencedItemException
WAFRegional.Client.exceptions.WAFNonEmptyEntityException
WAFRegional.Client.exceptions.WAFInvalidOperationException
WAFRegional.Client.exceptions.WAFTagOperationException
WAFRegional.Client.exceptions.WAFTagOperationInternalErrorException


    :return: {
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    RuleGroupId (string) -- [REQUIRED]
    The RuleGroupId of the  RuleGroup that you want to delete. RuleGroupId is returned by  CreateRuleGroup and by  ListRuleGroups .
    
    ChangeToken (string) -- [REQUIRED]
    The value returned by the most recent call to  GetChangeToken .
    
    
    """
    pass

def delete_size_constraint_set(SizeConstraintSetId=None, ChangeToken=None):
    """
    Permanently deletes a  SizeConstraintSet . You can\'t delete a SizeConstraintSet if it\'s still used in any Rules or if it still includes any  SizeConstraint objects (any filters).
    If you just want to remove a SizeConstraintSet from a Rule , use  UpdateRule .
    To permanently delete a SizeConstraintSet , perform the following steps:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example deletes a size constraint set  with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    Expected Output:
    
    :example: response = client.delete_size_constraint_set(
        SizeConstraintSetId='string',
        ChangeToken='string'
    )
    
    
    :type SizeConstraintSetId: string
    :param SizeConstraintSetId: [REQUIRED]\nThe SizeConstraintSetId of the SizeConstraintSet that you want to delete. SizeConstraintSetId is returned by CreateSizeConstraintSet and by ListSizeConstraintSets .\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChangeToken': 'string'
}


Response Structure

(dict) --

ChangeToken (string) --
The ChangeToken that you used to submit the DeleteSizeConstraintSet request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFReferencedItemException
WAFRegional.Client.exceptions.WAFNonEmptyEntityException

Examples
The following example deletes a size constraint set  with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
response = client.delete_size_constraint_set(
    ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    SizeConstraintSetId='example1ds3t-46da-4fdb-b8d5-abc321j569j5',
)

print(response)


Expected Output:
{
    'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    SizeConstraintSetId (string) -- [REQUIRED]
    The SizeConstraintSetId of the  SizeConstraintSet that you want to delete. SizeConstraintSetId is returned by  CreateSizeConstraintSet and by  ListSizeConstraintSets .
    
    ChangeToken (string) -- [REQUIRED]
    The value returned by the most recent call to  GetChangeToken .
    
    
    """
    pass

def delete_sql_injection_match_set(SqlInjectionMatchSetId=None, ChangeToken=None):
    """
    Permanently deletes a  SqlInjectionMatchSet . You can\'t delete a SqlInjectionMatchSet if it\'s still used in any Rules or if it still contains any  SqlInjectionMatchTuple objects.
    If you just want to remove a SqlInjectionMatchSet from a Rule , use  UpdateRule .
    To permanently delete a SqlInjectionMatchSet from AWS WAF, perform the following steps:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example deletes a SQL injection match set  with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    Expected Output:
    
    :example: response = client.delete_sql_injection_match_set(
        SqlInjectionMatchSetId='string',
        ChangeToken='string'
    )
    
    
    :type SqlInjectionMatchSetId: string
    :param SqlInjectionMatchSetId: [REQUIRED]\nThe SqlInjectionMatchSetId of the SqlInjectionMatchSet that you want to delete. SqlInjectionMatchSetId is returned by CreateSqlInjectionMatchSet and by ListSqlInjectionMatchSets .\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChangeToken': 'string'
}


Response Structure

(dict) --
The response to a request to delete a  SqlInjectionMatchSet from AWS WAF.

ChangeToken (string) --
The ChangeToken that you used to submit the DeleteSqlInjectionMatchSet request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFReferencedItemException
WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFNonEmptyEntityException

Examples
The following example deletes a SQL injection match set  with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
response = client.delete_sql_injection_match_set(
    ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    SqlInjectionMatchSetId='example1ds3t-46da-4fdb-b8d5-abc321j569j5',
)

print(response)


Expected Output:
{
    'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    SqlInjectionMatchSetId (string) -- [REQUIRED]
    The SqlInjectionMatchSetId of the  SqlInjectionMatchSet that you want to delete. SqlInjectionMatchSetId is returned by  CreateSqlInjectionMatchSet and by  ListSqlInjectionMatchSets .
    
    ChangeToken (string) -- [REQUIRED]
    The value returned by the most recent call to  GetChangeToken .
    
    
    """
    pass

def delete_web_acl(WebACLId=None, ChangeToken=None):
    """
    Permanently deletes a  WebACL . You can\'t delete a WebACL if it still contains any Rules .
    To delete a WebACL , perform the following steps:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example deletes a web ACL with the ID example-46da-4444-5555-example.
    Expected Output:
    
    :example: response = client.delete_web_acl(
        WebACLId='string',
        ChangeToken='string'
    )
    
    
    :type WebACLId: string
    :param WebACLId: [REQUIRED]\nThe WebACLId of the WebACL that you want to delete. WebACLId is returned by CreateWebACL and by ListWebACLs .\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChangeToken': 'string'
}


Response Structure

(dict) --

ChangeToken (string) --
The ChangeToken that you used to submit the DeleteWebACL request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFReferencedItemException
WAFRegional.Client.exceptions.WAFNonEmptyEntityException
WAFRegional.Client.exceptions.WAFTagOperationException
WAFRegional.Client.exceptions.WAFTagOperationInternalErrorException

Examples
The following example deletes a web ACL with the ID example-46da-4444-5555-example.
response = client.delete_web_acl(
    ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    WebACLId='example-46da-4444-5555-example',
)

print(response)


Expected Output:
{
    'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    WebACLId (string) -- [REQUIRED]
    The WebACLId of the  WebACL that you want to delete. WebACLId is returned by  CreateWebACL and by  ListWebACLs .
    
    ChangeToken (string) -- [REQUIRED]
    The value returned by the most recent call to  GetChangeToken .
    
    
    """
    pass

def delete_xss_match_set(XssMatchSetId=None, ChangeToken=None):
    """
    Permanently deletes an  XssMatchSet . You can\'t delete an XssMatchSet if it\'s still used in any Rules or if it still contains any  XssMatchTuple objects.
    If you just want to remove an XssMatchSet from a Rule , use  UpdateRule .
    To permanently delete an XssMatchSet from AWS WAF, perform the following steps:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example deletes an XSS match set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    Expected Output:
    
    :example: response = client.delete_xss_match_set(
        XssMatchSetId='string',
        ChangeToken='string'
    )
    
    
    :type XssMatchSetId: string
    :param XssMatchSetId: [REQUIRED]\nThe XssMatchSetId of the XssMatchSet that you want to delete. XssMatchSetId is returned by CreateXssMatchSet and by ListXssMatchSets .\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChangeToken': 'string'
}


Response Structure

(dict) --
The response to a request to delete an  XssMatchSet from AWS WAF.

ChangeToken (string) --
The ChangeToken that you used to submit the DeleteXssMatchSet request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFReferencedItemException
WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFNonEmptyEntityException

Examples
The following example deletes an XSS match set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
response = client.delete_xss_match_set(
    ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    XssMatchSetId='example1ds3t-46da-4fdb-b8d5-abc321j569j5',
)

print(response)


Expected Output:
{
    'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    XssMatchSetId (string) -- [REQUIRED]
    The XssMatchSetId of the  XssMatchSet that you want to delete. XssMatchSetId is returned by  CreateXssMatchSet and by  ListXssMatchSets .
    
    ChangeToken (string) -- [REQUIRED]
    The value returned by the most recent call to  GetChangeToken .
    
    
    """
    pass

def disassociate_web_acl(ResourceArn=None):
    """
    Removes a web ACL from the specified resource, either an application load balancer or Amazon API Gateway stage.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_web_acl(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe ARN (Amazon Resource Name) of the resource from which the web ACL is being removed, either an application load balancer or Amazon API Gateway stage.\nThe ARN should be in one of the following formats:\n\nFor an Application Load Balancer: ``arn:aws:elasticloadbalancing:region :account-id :loadbalancer/app/load-balancer-name /load-balancer-id ``\nFor an Amazon API Gateway stage: ``arn:aws:apigateway:region ::/restapis/api-id /stages/stage-name ``\n\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFInvalidParameterException
WAFRegional.Client.exceptions.WAFNonexistentItemException


    :return: {}
    
    
    :returns: 
    (dict) --
    
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

def get_byte_match_set(ByteMatchSetId=None):
    """
    Returns the  ByteMatchSet specified by ByteMatchSetId .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns the details of a byte match set with the ID exampleIDs3t-46da-4fdb-b8d5-abc321j569j5.
    Expected Output:
    
    :example: response = client.get_byte_match_set(
        ByteMatchSetId='string'
    )
    
    
    :type ByteMatchSetId: string
    :param ByteMatchSetId: [REQUIRED]\nThe ByteMatchSetId of the ByteMatchSet that you want to get. ByteMatchSetId is returned by CreateByteMatchSet and by ListByteMatchSets .\n

    :rtype: dict
ReturnsResponse Syntax{
    'ByteMatchSet': {
        'ByteMatchSetId': 'string',
        'Name': 'string',
        'ByteMatchTuples': [
            {
                'FieldToMatch': {
                    'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY'|'SINGLE_QUERY_ARG'|'ALL_QUERY_ARGS',
                    'Data': 'string'
                },
                'TargetString': b'bytes',
                'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE',
                'PositionalConstraint': 'EXACTLY'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CONTAINS_WORD'
            },
        ]
    }
}


Response Structure

(dict) --
ByteMatchSet (dict) --Information about the  ByteMatchSet that you specified in the GetByteMatchSet request. For more information, see the following topics:

ByteMatchSet : Contains ByteMatchSetId , ByteMatchTuples , and Name
ByteMatchTuples : Contains an array of  ByteMatchTuple objects. Each ByteMatchTuple object contains  FieldToMatch , PositionalConstraint , TargetString , and TextTransformation
FieldToMatch : Contains Data and Type


ByteMatchSetId (string) --The ByteMatchSetId for a ByteMatchSet . You use ByteMatchSetId to get information about a ByteMatchSet (see  GetByteMatchSet ), update a ByteMatchSet (see  UpdateByteMatchSet ), insert a ByteMatchSet into a Rule or delete one from a Rule (see  UpdateRule ), and delete a ByteMatchSet from AWS WAF (see  DeleteByteMatchSet ).

ByteMatchSetId is returned by  CreateByteMatchSet and by  ListByteMatchSets .

Name (string) --A friendly name or description of the  ByteMatchSet . You can\'t change Name after you create a ByteMatchSet .

ByteMatchTuples (list) --Specifies the bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to search for in web requests, the location in requests that you want AWS WAF to search, and other settings.

(dict) --
Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

The bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to search for in web requests, the location in requests that you want AWS WAF to search, and other settings.

FieldToMatch (dict) --The part of a web request that you want AWS WAF to search, such as a specified header or a query string. For more information, see  FieldToMatch .

Type (string) --The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:

HEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .
METHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .
QUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.
URI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .
BODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .
SINGLE_QUERY_ARG : The parameter in the query string that you will inspect, such as UserName or SalesRegion . The maximum length for SINGLE_QUERY_ARG is 30 characters.
ALL_QUERY_ARGS : Similar to SINGLE_QUERY_ARG , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in TargetString .


Data (string) --When the value of Type is HEADER , enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer . The name of the header is not case sensitive.
When the value of Type is SINGLE_QUERY_ARG , enter the name of the parameter that you want AWS WAF to search, for example, UserName or SalesRegion . The parameter name is not case sensitive.
If the value of Type is any other value, omit Data .



TargetString (bytes) --The value that you want AWS WAF to search for. AWS WAF searches for the specified string in the part of web requests that you specified in FieldToMatch . The maximum length of the value is 50 bytes.
Valid values depend on the values that you specified for FieldToMatch :

HEADER : The value that you want AWS WAF to search for in the request header that you specified in  FieldToMatch , for example, the value of the User-Agent or Referer header.
METHOD : The HTTP method, which indicates the type of operation specified in the request. CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .
QUERY_STRING : The value that you want AWS WAF to search for in the query string, which is the part of a URL that appears after a ? character.
URI : The value that you want AWS WAF to search for in the part of a URL that identifies a resource, for example, /images/daily-ad.jpg .
BODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .
SINGLE_QUERY_ARG : The parameter in the query string that you will inspect, such as UserName or SalesRegion . The maximum length for SINGLE_QUERY_ARG is 30 characters.
ALL_QUERY_ARGS : Similar to SINGLE_QUERY_ARG , but instead of inspecting a single parameter, AWS WAF inspects all parameters within the query string for the value or regex pattern that you specify in TargetString .

If TargetString includes alphabetic characters A-Z and a-z, note that the value is case sensitive.

If you\'re using the AWS WAF API
Specify a base64-encoded version of the value. The maximum length of the value before you base64-encode it is 50 bytes.
For example, suppose the value of Type is HEADER and the value of Data is User-Agent . If you want to search the User-Agent header for the value BadBot , you base64-encode BadBot using MIME base64-encoding and include the resulting value, QmFkQm90 , in the value of TargetString .

If you\'re using the AWS CLI or one of the AWS SDKs
The value that you want AWS WAF to search for. The SDK automatically base64 encodes the value.

TextTransformation (string) --Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on FieldToMatch before inspecting it for a match.
You can only specify a single type of TextTransformation.

CMD_LINE
When you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: " \' ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE
Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a "less than" symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE
Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE
Use this option to decode a URL-encoded value.

NONE
Specify NONE if you don\'t want to perform any text transformations.

PositionalConstraint (string) --Within the portion of a web request that you want to search (for example, in the query string, if any), specify where you want AWS WAF to search. Valid values include the following:

CONTAINS
The specified part of the web request must include the value of TargetString , but the location doesn\'t matter.

CONTAINS_WORD
The specified part of the web request must include the value of TargetString , and TargetString must contain only alphanumeric characters or underscore (A-Z, a-z, 0-9, or _). In addition, TargetString must be a word, which means one of the following:

TargetString exactly matches the value of the specified part of the web request, such as the value of a header.
TargetString is at the beginning of the specified part of the web request and is followed by a character other than an alphanumeric character or underscore (_), for example, BadBot; .
TargetString is at the end of the specified part of the web request and is preceded by a character other than an alphanumeric character or underscore (_), for example, ;BadBot .
TargetString is in the middle of the specified part of the web request and is preceded and followed by characters other than alphanumeric characters or underscore (_), for example, -BadBot; .


EXACTLY
The value of the specified part of the web request must exactly match the value of TargetString .

STARTS_WITH
The value of TargetString must appear at the beginning of the specified part of the web request.

ENDS_WITH
The value of TargetString must appear at the end of the specified part of the web request.












Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFNonexistentItemException

Examples
The following example returns the details of a byte match set with the ID exampleIDs3t-46da-4fdb-b8d5-abc321j569j5.
response = client.get_byte_match_set(
    ByteMatchSetId='exampleIDs3t-46da-4fdb-b8d5-abc321j569j5',
)

print(response)


Expected Output:
{
    'ByteMatchSet': {
        'ByteMatchSetId': 'exampleIDs3t-46da-4fdb-b8d5-abc321j569j5',
        'ByteMatchTuples': [
            {
                'FieldToMatch': {
                    'Data': 'referer',
                    'Type': 'HEADER',
                },
                'PositionalConstraint': 'CONTAINS',
                'TargetString': 'badrefer1',
                'TextTransformation': 'NONE',
            },
        ],
        'Name': 'ByteMatchNameExample',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ByteMatchSet': {
            'ByteMatchSetId': 'string',
            'Name': 'string',
            'ByteMatchTuples': [
                {
                    'FieldToMatch': {
                        'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY'|'SINGLE_QUERY_ARG'|'ALL_QUERY_ARGS',
                        'Data': 'string'
                    },
                    'TargetString': b'bytes',
                    'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE',
                    'PositionalConstraint': 'EXACTLY'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CONTAINS_WORD'
                },
            ]
        }
    }
    
    
    :returns: 
    HEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .
    METHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .
    QUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.
    URI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .
    BODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .
    SINGLE_QUERY_ARG : The parameter in the query string that you will inspect, such as UserName or SalesRegion . The maximum length for SINGLE_QUERY_ARG is 30 characters.
    ALL_QUERY_ARGS : Similar to SINGLE_QUERY_ARG , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in TargetString .
    
    """
    pass

def get_change_token():
    """
    When you want to create, update, or delete AWS WAF objects, get a change token and include the change token in the create, update, or delete request. Change tokens ensure that your application doesn\'t submit conflicting requests to AWS WAF.
    Each create, update, or delete request must use a unique change token. If your application submits a GetChangeToken request and then submits a second GetChangeToken request before submitting a create, update, or delete request, the second GetChangeToken request returns the same value as the first GetChangeToken request.
    When you use a change token in a create, update, or delete request, the status of the change token changes to PENDING , which indicates that AWS WAF is propagating the change to all AWS WAF servers. Use GetChangeTokenStatus to determine the status of your change token.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns a change token to use for a create, update or delete operation.
    Expected Output:
    
    :example: response = client.get_change_token()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'ChangeToken': 'string'
}


Response Structure

(dict) --
ChangeToken (string) --The ChangeToken that you used in the request. Use this value in a GetChangeTokenStatus request to get the current status of the request.






Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException

Examples
The following example returns a change token to use for a create, update or delete operation.
response = client.get_change_token(
)

print(response)


Expected Output:
{
    'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ChangeToken': 'string'
    }
    
    
    """
    pass

def get_change_token_status(ChangeToken=None):
    """
    Returns the status of a ChangeToken that you got by calling  GetChangeToken . ChangeTokenStatus is one of the following values:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns the status of a change token with the ID abcd12f2-46da-4fdb-b8d5-fbd4c466928f.
    Expected Output:
    
    :example: response = client.get_change_token_status(
        ChangeToken='string'
    )
    
    
    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe change token for which you want to get the status. This change token was previously returned in the GetChangeToken response.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ChangeTokenStatus': 'PROVISIONED'|'PENDING'|'INSYNC'
}


Response Structure

(dict) --
ChangeTokenStatus (string) --The status of the change token.






Exceptions

WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFInternalErrorException

Examples
The following example returns the status of a change token with the ID abcd12f2-46da-4fdb-b8d5-fbd4c466928f.
response = client.get_change_token_status(
    ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
)

print(response)


Expected Output:
{
    'ChangeTokenStatus': 'PENDING',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ChangeTokenStatus': 'PROVISIONED'|'PENDING'|'INSYNC'
    }
    
    
    :returns: 
    WAFRegional.Client.exceptions.WAFNonexistentItemException
    WAFRegional.Client.exceptions.WAFInternalErrorException
    
    """
    pass

def get_geo_match_set(GeoMatchSetId=None):
    """
    Returns the  GeoMatchSet that is specified by GeoMatchSetId .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_geo_match_set(
        GeoMatchSetId='string'
    )
    
    
    :type GeoMatchSetId: string
    :param GeoMatchSetId: [REQUIRED]\nThe GeoMatchSetId of the GeoMatchSet that you want to get. GeoMatchSetId is returned by CreateGeoMatchSet and by ListGeoMatchSets .\n

    :rtype: dict
ReturnsResponse Syntax{
    'GeoMatchSet': {
        'GeoMatchSetId': 'string',
        'Name': 'string',
        'GeoMatchConstraints': [
            {
                'Type': 'Country',
                'Value': 'AF'|'AX'|'AL'|'DZ'|'AS'|'AD'|'AO'|'AI'|'AQ'|'AG'|'AR'|'AM'|'AW'|'AU'|'AT'|'AZ'|'BS'|'BH'|'BD'|'BB'|'BY'|'BE'|'BZ'|'BJ'|'BM'|'BT'|'BO'|'BQ'|'BA'|'BW'|'BV'|'BR'|'IO'|'BN'|'BG'|'BF'|'BI'|'KH'|'CM'|'CA'|'CV'|'KY'|'CF'|'TD'|'CL'|'CN'|'CX'|'CC'|'CO'|'KM'|'CG'|'CD'|'CK'|'CR'|'CI'|'HR'|'CU'|'CW'|'CY'|'CZ'|'DK'|'DJ'|'DM'|'DO'|'EC'|'EG'|'SV'|'GQ'|'ER'|'EE'|'ET'|'FK'|'FO'|'FJ'|'FI'|'FR'|'GF'|'PF'|'TF'|'GA'|'GM'|'GE'|'DE'|'GH'|'GI'|'GR'|'GL'|'GD'|'GP'|'GU'|'GT'|'GG'|'GN'|'GW'|'GY'|'HT'|'HM'|'VA'|'HN'|'HK'|'HU'|'IS'|'IN'|'ID'|'IR'|'IQ'|'IE'|'IM'|'IL'|'IT'|'JM'|'JP'|'JE'|'JO'|'KZ'|'KE'|'KI'|'KP'|'KR'|'KW'|'KG'|'LA'|'LV'|'LB'|'LS'|'LR'|'LY'|'LI'|'LT'|'LU'|'MO'|'MK'|'MG'|'MW'|'MY'|'MV'|'ML'|'MT'|'MH'|'MQ'|'MR'|'MU'|'YT'|'MX'|'FM'|'MD'|'MC'|'MN'|'ME'|'MS'|'MA'|'MZ'|'MM'|'NA'|'NR'|'NP'|'NL'|'NC'|'NZ'|'NI'|'NE'|'NG'|'NU'|'NF'|'MP'|'NO'|'OM'|'PK'|'PW'|'PS'|'PA'|'PG'|'PY'|'PE'|'PH'|'PN'|'PL'|'PT'|'PR'|'QA'|'RE'|'RO'|'RU'|'RW'|'BL'|'SH'|'KN'|'LC'|'MF'|'PM'|'VC'|'WS'|'SM'|'ST'|'SA'|'SN'|'RS'|'SC'|'SL'|'SG'|'SX'|'SK'|'SI'|'SB'|'SO'|'ZA'|'GS'|'SS'|'ES'|'LK'|'SD'|'SR'|'SJ'|'SZ'|'SE'|'CH'|'SY'|'TW'|'TJ'|'TZ'|'TH'|'TL'|'TG'|'TK'|'TO'|'TT'|'TN'|'TR'|'TM'|'TC'|'TV'|'UG'|'UA'|'AE'|'GB'|'US'|'UM'|'UY'|'UZ'|'VU'|'VE'|'VN'|'VG'|'VI'|'WF'|'EH'|'YE'|'ZM'|'ZW'
            },
        ]
    }
}


Response Structure

(dict) --
GeoMatchSet (dict) --Information about the  GeoMatchSet that you specified in the GetGeoMatchSet request. This includes the Type , which for a GeoMatchContraint is always Country , as well as the Value , which is the identifier for a specific country.

GeoMatchSetId (string) --The GeoMatchSetId for an GeoMatchSet . You use GeoMatchSetId to get information about a GeoMatchSet (see  GeoMatchSet ), update a GeoMatchSet (see  UpdateGeoMatchSet ), insert a GeoMatchSet into a Rule or delete one from a Rule (see  UpdateRule ), and delete a GeoMatchSet from AWS WAF (see  DeleteGeoMatchSet ).

GeoMatchSetId is returned by  CreateGeoMatchSet and by  ListGeoMatchSets .

Name (string) --A friendly name or description of the  GeoMatchSet . You can\'t change the name of an GeoMatchSet after you create it.

GeoMatchConstraints (list) --An array of  GeoMatchConstraint objects, which contain the country that you want AWS WAF to search for.

(dict) --
Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

The country from which web requests originate that you want AWS WAF to search for.

Type (string) --The type of geographical area you want AWS WAF to search for. Currently Country is the only valid value.

Value (string) --The country that you want AWS WAF to search for.












Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFNonexistentItemException


    :return: {
        'GeoMatchSet': {
            'GeoMatchSetId': 'string',
            'Name': 'string',
            'GeoMatchConstraints': [
                {
                    'Type': 'Country',
                    'Value': 'AF'|'AX'|'AL'|'DZ'|'AS'|'AD'|'AO'|'AI'|'AQ'|'AG'|'AR'|'AM'|'AW'|'AU'|'AT'|'AZ'|'BS'|'BH'|'BD'|'BB'|'BY'|'BE'|'BZ'|'BJ'|'BM'|'BT'|'BO'|'BQ'|'BA'|'BW'|'BV'|'BR'|'IO'|'BN'|'BG'|'BF'|'BI'|'KH'|'CM'|'CA'|'CV'|'KY'|'CF'|'TD'|'CL'|'CN'|'CX'|'CC'|'CO'|'KM'|'CG'|'CD'|'CK'|'CR'|'CI'|'HR'|'CU'|'CW'|'CY'|'CZ'|'DK'|'DJ'|'DM'|'DO'|'EC'|'EG'|'SV'|'GQ'|'ER'|'EE'|'ET'|'FK'|'FO'|'FJ'|'FI'|'FR'|'GF'|'PF'|'TF'|'GA'|'GM'|'GE'|'DE'|'GH'|'GI'|'GR'|'GL'|'GD'|'GP'|'GU'|'GT'|'GG'|'GN'|'GW'|'GY'|'HT'|'HM'|'VA'|'HN'|'HK'|'HU'|'IS'|'IN'|'ID'|'IR'|'IQ'|'IE'|'IM'|'IL'|'IT'|'JM'|'JP'|'JE'|'JO'|'KZ'|'KE'|'KI'|'KP'|'KR'|'KW'|'KG'|'LA'|'LV'|'LB'|'LS'|'LR'|'LY'|'LI'|'LT'|'LU'|'MO'|'MK'|'MG'|'MW'|'MY'|'MV'|'ML'|'MT'|'MH'|'MQ'|'MR'|'MU'|'YT'|'MX'|'FM'|'MD'|'MC'|'MN'|'ME'|'MS'|'MA'|'MZ'|'MM'|'NA'|'NR'|'NP'|'NL'|'NC'|'NZ'|'NI'|'NE'|'NG'|'NU'|'NF'|'MP'|'NO'|'OM'|'PK'|'PW'|'PS'|'PA'|'PG'|'PY'|'PE'|'PH'|'PN'|'PL'|'PT'|'PR'|'QA'|'RE'|'RO'|'RU'|'RW'|'BL'|'SH'|'KN'|'LC'|'MF'|'PM'|'VC'|'WS'|'SM'|'ST'|'SA'|'SN'|'RS'|'SC'|'SL'|'SG'|'SX'|'SK'|'SI'|'SB'|'SO'|'ZA'|'GS'|'SS'|'ES'|'LK'|'SD'|'SR'|'SJ'|'SZ'|'SE'|'CH'|'SY'|'TW'|'TJ'|'TZ'|'TH'|'TL'|'TG'|'TK'|'TO'|'TT'|'TN'|'TR'|'TM'|'TC'|'TV'|'UG'|'UA'|'AE'|'GB'|'US'|'UM'|'UY'|'UZ'|'VU'|'VE'|'VN'|'VG'|'VI'|'WF'|'EH'|'YE'|'ZM'|'ZW'
                },
            ]
        }
    }
    
    
    """
    pass

def get_ip_set(IPSetId=None):
    """
    Returns the  IPSet that is specified by IPSetId .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns the details of an IP match set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    Expected Output:
    
    :example: response = client.get_ip_set(
        IPSetId='string'
    )
    
    
    :type IPSetId: string
    :param IPSetId: [REQUIRED]\nThe IPSetId of the IPSet that you want to get. IPSetId is returned by CreateIPSet and by ListIPSets .\n

    :rtype: dict
ReturnsResponse Syntax{
    'IPSet': {
        'IPSetId': 'string',
        'Name': 'string',
        'IPSetDescriptors': [
            {
                'Type': 'IPV4'|'IPV6',
                'Value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --
IPSet (dict) --Information about the  IPSet that you specified in the GetIPSet request. For more information, see the following topics:

IPSet : Contains IPSetDescriptors , IPSetId , and Name
IPSetDescriptors : Contains an array of  IPSetDescriptor objects. Each IPSetDescriptor object contains Type and Value


IPSetId (string) --The IPSetId for an IPSet . You use IPSetId to get information about an IPSet (see  GetIPSet ), update an IPSet (see  UpdateIPSet ), insert an IPSet into a Rule or delete one from a Rule (see  UpdateRule ), and delete an IPSet from AWS WAF (see  DeleteIPSet ).

IPSetId is returned by  CreateIPSet and by  ListIPSets .

Name (string) --A friendly name or description of the  IPSet . You can\'t change the name of an IPSet after you create it.

IPSetDescriptors (list) --The IP address type (IPV4 or IPV6 ) and the IP address range (in CIDR notation) that web requests originate from. If the WebACL is associated with a CloudFront distribution and the viewer did not use an HTTP proxy or a load balancer to send the request, this is the value of the c-ip field in the CloudFront access logs.

(dict) --
Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Specifies the IP address type (IPV4 or IPV6 ) and the IP address range (in CIDR format) that web requests originate from.

Type (string) --Specify IPV4 or IPV6 .

Value (string) --Specify an IPv4 address by using CIDR notation. For example:

To configure AWS WAF to allow, block, or count requests that originated from the IP address 192.0.2.44, specify 192.0.2.44/32 .
To configure AWS WAF to allow, block, or count requests that originated from IP addresses from 192.0.2.0 to 192.0.2.255, specify 192.0.2.0/24 .

For more information about CIDR notation, see the Wikipedia entry Classless Inter-Domain Routing .
Specify an IPv6 address by using CIDR notation. For example:

To configure AWS WAF to allow, block, or count requests that originated from the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify 1111:0000:0000:0000:0000:0000:0000:0111/128 .
To configure AWS WAF to allow, block, or count requests that originated from IP addresses 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify 1111:0000:0000:0000:0000:0000:0000:0000/64 .













Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFNonexistentItemException

Examples
The following example returns the details of an IP match set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
response = client.get_ip_set(
    IPSetId='example1ds3t-46da-4fdb-b8d5-abc321j569j5',
)

print(response)


Expected Output:
{
    'IPSet': {
        'IPSetDescriptors': [
            {
                'Type': 'IPV4',
                'Value': '192.0.2.44/32',
            },
        ],
        'IPSetId': 'example1ds3t-46da-4fdb-b8d5-abc321j569j5',
        'Name': 'MyIPSetFriendlyName',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'IPSet': {
            'IPSetId': 'string',
            'Name': 'string',
            'IPSetDescriptors': [
                {
                    'Type': 'IPV4'|'IPV6',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    To configure AWS WAF to allow, block, or count requests that originated from the IP address 192.0.2.44, specify 192.0.2.44/32 .
    To configure AWS WAF to allow, block, or count requests that originated from IP addresses from 192.0.2.0 to 192.0.2.255, specify 192.0.2.0/24 .
    
    """
    pass

def get_logging_configuration(ResourceArn=None):
    """
    Returns the  LoggingConfiguration for the specified web ACL.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_logging_configuration(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the web ACL for which you want to get the LoggingConfiguration .\n

    :rtype: dict
ReturnsResponse Syntax{
    'LoggingConfiguration': {
        'ResourceArn': 'string',
        'LogDestinationConfigs': [
            'string',
        ],
        'RedactedFields': [
            {
                'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY'|'SINGLE_QUERY_ARG'|'ALL_QUERY_ARGS',
                'Data': 'string'
            },
        ]
    }
}


Response Structure

(dict) --
LoggingConfiguration (dict) --The  LoggingConfiguration for the specified web ACL.

ResourceArn (string) --The Amazon Resource Name (ARN) of the web ACL that you want to associate with LogDestinationConfigs .

LogDestinationConfigs (list) --An array of Amazon Kinesis Data Firehose ARNs.

(string) --


RedactedFields (list) --The parts of the request that you want redacted from the logs. For example, if you redact the cookie field, the cookie field in the firehose will be xxx .

(dict) --
Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Specifies where in a web request to look for TargetString .

Type (string) --The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:

HEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .
METHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .
QUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.
URI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .
BODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .
SINGLE_QUERY_ARG : The parameter in the query string that you will inspect, such as UserName or SalesRegion . The maximum length for SINGLE_QUERY_ARG is 30 characters.
ALL_QUERY_ARGS : Similar to SINGLE_QUERY_ARG , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in TargetString .


Data (string) --When the value of Type is HEADER , enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer . The name of the header is not case sensitive.
When the value of Type is SINGLE_QUERY_ARG , enter the name of the parameter that you want AWS WAF to search, for example, UserName or SalesRegion . The parameter name is not case sensitive.
If the value of Type is any other value, omit Data .












Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFNonexistentItemException


    :return: {
        'LoggingConfiguration': {
            'ResourceArn': 'string',
            'LogDestinationConfigs': [
                'string',
            ],
            'RedactedFields': [
                {
                    'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY'|'SINGLE_QUERY_ARG'|'ALL_QUERY_ARGS',
                    'Data': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    HEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .
    METHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .
    QUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.
    URI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .
    BODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .
    SINGLE_QUERY_ARG : The parameter in the query string that you will inspect, such as UserName or SalesRegion . The maximum length for SINGLE_QUERY_ARG is 30 characters.
    ALL_QUERY_ARGS : Similar to SINGLE_QUERY_ARG , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in TargetString .
    
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

def get_permission_policy(ResourceArn=None):
    """
    Returns the IAM policy attached to the RuleGroup.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_permission_policy(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the RuleGroup for which you want to get the policy.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Policy': 'string'
}


Response Structure

(dict) --
Policy (string) --The IAM policy attached to the specified RuleGroup.






Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFNonexistentItemException


    :return: {
        'Policy': 'string'
    }
    
    
    """
    pass

def get_rate_based_rule(RuleId=None):
    """
    Returns the  RateBasedRule that is specified by the RuleId that you included in the GetRateBasedRule request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_rate_based_rule(
        RuleId='string'
    )
    
    
    :type RuleId: string
    :param RuleId: [REQUIRED]\nThe RuleId of the RateBasedRule that you want to get. RuleId is returned by CreateRateBasedRule and by ListRateBasedRules .\n

    :rtype: dict
ReturnsResponse Syntax{
    'Rule': {
        'RuleId': 'string',
        'Name': 'string',
        'MetricName': 'string',
        'MatchPredicates': [
            {
                'Negated': True|False,
                'Type': 'IPMatch'|'ByteMatch'|'SqlInjectionMatch'|'GeoMatch'|'SizeConstraint'|'XssMatch'|'RegexMatch',
                'DataId': 'string'
            },
        ],
        'RateKey': 'IP',
        'RateLimit': 123
    }
}


Response Structure

(dict) --
Rule (dict) --Information about the  RateBasedRule that you specified in the GetRateBasedRule request.

RuleId (string) --A unique identifier for a RateBasedRule . You use RuleId to get more information about a RateBasedRule (see  GetRateBasedRule ), update a RateBasedRule (see  UpdateRateBasedRule ), insert a RateBasedRule into a WebACL or delete one from a WebACL (see  UpdateWebACL ), or delete a RateBasedRule from AWS WAF (see  DeleteRateBasedRule ).

Name (string) --A friendly name or description for a RateBasedRule . You can\'t change the name of a RateBasedRule after you create it.

MetricName (string) --A friendly name or description for the metrics for a RateBasedRule . The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can\'t contain whitespace or metric names reserved for AWS WAF, including "All" and "Default_Action." You can\'t change the name of the metric after you create the RateBasedRule .

MatchPredicates (list) --The Predicates object contains one Predicate element for each  ByteMatchSet ,  IPSet , or  SqlInjectionMatchSet object that you want to include in a RateBasedRule .

(dict) --
Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Specifies the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , and  SizeConstraintSet objects that you want to add to a Rule and, for each object, indicates whether you want to negate the settings, for example, requests that do NOT originate from the IP address 192.0.2.44.

Negated (boolean) --Set Negated to False if you want AWS WAF to allow, block, or count requests based on the settings in the specified  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if an IPSet includes the IP address 192.0.2.44 , AWS WAF will allow or block requests based on that IP address.
Set Negated to True if you want AWS WAF to allow or block a request based on the negation of the settings in the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if an IPSet includes the IP address 192.0.2.44 , AWS WAF will allow, block, or count requests based on all IP addresses except 192.0.2.44 .

Type (string) --The type of predicate in a Rule , such as ByteMatch or IPSet .

DataId (string) --A unique identifier for a predicate in a Rule , such as ByteMatchSetId or IPSetId . The ID is returned by the corresponding Create or List command.





RateKey (string) --The field that AWS WAF uses to determine if requests are likely arriving from single source and thus subject to rate monitoring. The only valid value for RateKey is IP . IP indicates that requests arriving from the same IP address are subject to the RateLimit that is specified in the RateBasedRule .

RateLimit (integer) --The maximum number of requests, which have an identical value in the field specified by the RateKey , allowed in a five-minute period. If the number of requests exceeds the RateLimit and the other predicates specified in the rule are also met, AWS WAF triggers the action that is specified for this rule.








Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFNonexistentItemException


    :return: {
        'Rule': {
            'RuleId': 'string',
            'Name': 'string',
            'MetricName': 'string',
            'MatchPredicates': [
                {
                    'Negated': True|False,
                    'Type': 'IPMatch'|'ByteMatch'|'SqlInjectionMatch'|'GeoMatch'|'SizeConstraint'|'XssMatch'|'RegexMatch',
                    'DataId': 'string'
                },
            ],
            'RateKey': 'IP',
            'RateLimit': 123
        }
    }
    
    
    """
    pass

def get_rate_based_rule_managed_keys(RuleId=None, NextMarker=None):
    """
    Returns an array of IP addresses currently being blocked by the  RateBasedRule that is specified by the RuleId . The maximum number of managed keys that will be blocked is 10,000. If more than 10,000 addresses exceed the rate limit, the 10,000 addresses with the highest rates will be blocked.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_rate_based_rule_managed_keys(
        RuleId='string',
        NextMarker='string'
    )
    
    
    :type RuleId: string
    :param RuleId: [REQUIRED]\nThe RuleId of the RateBasedRule for which you want to get a list of ManagedKeys . RuleId is returned by CreateRateBasedRule and by ListRateBasedRules .\n

    :type NextMarker: string
    :param NextMarker: A null value and not currently used. Do not include this in your request.

    :rtype: dict

ReturnsResponse Syntax
{
    'ManagedKeys': [
        'string',
    ],
    'NextMarker': 'string'
}


Response Structure

(dict) --

ManagedKeys (list) --
An array of IP addresses that currently are blocked by the specified  RateBasedRule .

(string) --


NextMarker (string) --
A null value and not currently used.







Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFInvalidParameterException


    :return: {
        'ManagedKeys': [
            'string',
        ],
        'NextMarker': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_regex_match_set(RegexMatchSetId=None):
    """
    Returns the  RegexMatchSet specified by RegexMatchSetId .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_regex_match_set(
        RegexMatchSetId='string'
    )
    
    
    :type RegexMatchSetId: string
    :param RegexMatchSetId: [REQUIRED]\nThe RegexMatchSetId of the RegexMatchSet that you want to get. RegexMatchSetId is returned by CreateRegexMatchSet and by ListRegexMatchSets .\n

    :rtype: dict
ReturnsResponse Syntax{
    'RegexMatchSet': {
        'RegexMatchSetId': 'string',
        'Name': 'string',
        'RegexMatchTuples': [
            {
                'FieldToMatch': {
                    'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY'|'SINGLE_QUERY_ARG'|'ALL_QUERY_ARGS',
                    'Data': 'string'
                },
                'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE',
                'RegexPatternSetId': 'string'
            },
        ]
    }
}


Response Structure

(dict) --
RegexMatchSet (dict) --Information about the  RegexMatchSet that you specified in the GetRegexMatchSet request. For more information, see  RegexMatchTuple .

RegexMatchSetId (string) --The RegexMatchSetId for a RegexMatchSet . You use RegexMatchSetId to get information about a RegexMatchSet (see  GetRegexMatchSet ), update a RegexMatchSet (see  UpdateRegexMatchSet ), insert a RegexMatchSet into a Rule or delete one from a Rule (see  UpdateRule ), and delete a RegexMatchSet from AWS WAF (see  DeleteRegexMatchSet ).

RegexMatchSetId is returned by  CreateRegexMatchSet and by  ListRegexMatchSets .

Name (string) --A friendly name or description of the  RegexMatchSet . You can\'t change Name after you create a RegexMatchSet .

RegexMatchTuples (list) --Contains an array of  RegexMatchTuple objects. Each RegexMatchTuple object contains:

The part of a web request that you want AWS WAF to inspect, such as a query string or the value of the User-Agent header.
The identifier of the pattern (a regular expression) that you want AWS WAF to look for. For more information, see  RegexPatternSet .
Whether to perform any conversions on the request, such as converting it to lowercase, before inspecting it for the specified string.


(dict) --
Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

The regular expression pattern that you want AWS WAF to search for in web requests, the location in requests that you want AWS WAF to search, and other settings. Each RegexMatchTuple object contains:

The part of a web request that you want AWS WAF to inspect, such as a query string or the value of the User-Agent header.
The identifier of the pattern (a regular expression) that you want AWS WAF to look for. For more information, see  RegexPatternSet .
Whether to perform any conversions on the request, such as converting it to lowercase, before inspecting it for the specified string.


FieldToMatch (dict) --Specifies where in a web request to look for the RegexPatternSet .

Type (string) --The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:

HEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .
METHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .
QUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.
URI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .
BODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .
SINGLE_QUERY_ARG : The parameter in the query string that you will inspect, such as UserName or SalesRegion . The maximum length for SINGLE_QUERY_ARG is 30 characters.
ALL_QUERY_ARGS : Similar to SINGLE_QUERY_ARG , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in TargetString .


Data (string) --When the value of Type is HEADER , enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer . The name of the header is not case sensitive.
When the value of Type is SINGLE_QUERY_ARG , enter the name of the parameter that you want AWS WAF to search, for example, UserName or SalesRegion . The parameter name is not case sensitive.
If the value of Type is any other value, omit Data .



TextTransformation (string) --Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on RegexPatternSet before inspecting a request for a match.
You can only specify a single type of TextTransformation.

CMD_LINE
When you\'re concerned that attackers are injecting an operating system commandline command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: " \' ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE
Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a "less than" symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE
Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE
Use this option to decode a URL-encoded value.

NONE
Specify NONE if you don\'t want to perform any text transformations.

RegexPatternSetId (string) --The RegexPatternSetId for a RegexPatternSet . You use RegexPatternSetId to get information about a RegexPatternSet (see  GetRegexPatternSet ), update a RegexPatternSet (see  UpdateRegexPatternSet ), insert a RegexPatternSet into a RegexMatchSet or delete one from a RegexMatchSet (see  UpdateRegexMatchSet ), and delete an RegexPatternSet from AWS WAF (see  DeleteRegexPatternSet ).

RegexPatternSetId is returned by  CreateRegexPatternSet and by  ListRegexPatternSets .












Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFNonexistentItemException


    :return: {
        'RegexMatchSet': {
            'RegexMatchSetId': 'string',
            'Name': 'string',
            'RegexMatchTuples': [
                {
                    'FieldToMatch': {
                        'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY'|'SINGLE_QUERY_ARG'|'ALL_QUERY_ARGS',
                        'Data': 'string'
                    },
                    'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE',
                    'RegexPatternSetId': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    The part of a web request that you want AWS WAF to inspect, such as a query string or the value of the User-Agent header.
    The identifier of the pattern (a regular expression) that you want AWS WAF to look for. For more information, see  RegexPatternSet .
    Whether to perform any conversions on the request, such as converting it to lowercase, before inspecting it for the specified string.
    
    """
    pass

def get_regex_pattern_set(RegexPatternSetId=None):
    """
    Returns the  RegexPatternSet specified by RegexPatternSetId .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_regex_pattern_set(
        RegexPatternSetId='string'
    )
    
    
    :type RegexPatternSetId: string
    :param RegexPatternSetId: [REQUIRED]\nThe RegexPatternSetId of the RegexPatternSet that you want to get. RegexPatternSetId is returned by CreateRegexPatternSet and by ListRegexPatternSets .\n

    :rtype: dict
ReturnsResponse Syntax{
    'RegexPatternSet': {
        'RegexPatternSetId': 'string',
        'Name': 'string',
        'RegexPatternStrings': [
            'string',
        ]
    }
}


Response Structure

(dict) --
RegexPatternSet (dict) --Information about the  RegexPatternSet that you specified in the GetRegexPatternSet request, including the identifier of the pattern set and the regular expression patterns you want AWS WAF to search for.

RegexPatternSetId (string) --The identifier for the RegexPatternSet . You use RegexPatternSetId to get information about a RegexPatternSet , update a RegexPatternSet , remove a RegexPatternSet from a RegexMatchSet , and delete a RegexPatternSet from AWS WAF.

RegexMatchSetId is returned by  CreateRegexPatternSet and by  ListRegexPatternSets .

Name (string) --A friendly name or description of the  RegexPatternSet . You can\'t change Name after you create a RegexPatternSet .

RegexPatternStrings (list) --Specifies the regular expression (regex) patterns that you want AWS WAF to search for, such as B[a@]dB[o0]t .

(string) --









Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFNonexistentItemException


    :return: {
        'RegexPatternSet': {
            'RegexPatternSetId': 'string',
            'Name': 'string',
            'RegexPatternStrings': [
                'string',
            ]
        }
    }
    
    
    :returns: 
    WAFRegional.Client.exceptions.WAFInternalErrorException
    WAFRegional.Client.exceptions.WAFInvalidAccountException
    WAFRegional.Client.exceptions.WAFNonexistentItemException
    
    """
    pass

def get_rule(RuleId=None):
    """
    Returns the  Rule that is specified by the RuleId that you included in the GetRule request.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns the details of a rule with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    Expected Output:
    
    :example: response = client.get_rule(
        RuleId='string'
    )
    
    
    :type RuleId: string
    :param RuleId: [REQUIRED]\nThe RuleId of the Rule that you want to get. RuleId is returned by CreateRule and by ListRules .\n

    :rtype: dict
ReturnsResponse Syntax{
    'Rule': {
        'RuleId': 'string',
        'Name': 'string',
        'MetricName': 'string',
        'Predicates': [
            {
                'Negated': True|False,
                'Type': 'IPMatch'|'ByteMatch'|'SqlInjectionMatch'|'GeoMatch'|'SizeConstraint'|'XssMatch'|'RegexMatch',
                'DataId': 'string'
            },
        ]
    }
}


Response Structure

(dict) --
Rule (dict) --Information about the  Rule that you specified in the GetRule request. For more information, see the following topics:

Rule : Contains MetricName , Name , an array of Predicate objects, and RuleId
Predicate : Each Predicate object contains DataId , Negated , and Type


RuleId (string) --A unique identifier for a Rule . You use RuleId to get more information about a Rule (see  GetRule ), update a Rule (see  UpdateRule ), insert a Rule into a WebACL or delete a one from a WebACL (see  UpdateWebACL ), or delete a Rule from AWS WAF (see  DeleteRule ).

RuleId is returned by  CreateRule and by  ListRules .

Name (string) --The friendly name or description for the Rule . You can\'t change the name of a Rule after you create it.

MetricName (string) --A friendly name or description for the metrics for this Rule . The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can\'t contain whitespace or metric names reserved for AWS WAF, including "All" and "Default_Action." You can\'t change MetricName after you create the Rule .

Predicates (list) --The Predicates object contains one Predicate element for each  ByteMatchSet ,  IPSet , or  SqlInjectionMatchSet object that you want to include in a Rule .

(dict) --
Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Specifies the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , and  SizeConstraintSet objects that you want to add to a Rule and, for each object, indicates whether you want to negate the settings, for example, requests that do NOT originate from the IP address 192.0.2.44.

Negated (boolean) --Set Negated to False if you want AWS WAF to allow, block, or count requests based on the settings in the specified  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if an IPSet includes the IP address 192.0.2.44 , AWS WAF will allow or block requests based on that IP address.
Set Negated to True if you want AWS WAF to allow or block a request based on the negation of the settings in the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if an IPSet includes the IP address 192.0.2.44 , AWS WAF will allow, block, or count requests based on all IP addresses except 192.0.2.44 .

Type (string) --The type of predicate in a Rule , such as ByteMatch or IPSet .

DataId (string) --A unique identifier for a predicate in a Rule , such as ByteMatchSetId or IPSetId . The ID is returned by the corresponding Create or List command.












Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFNonexistentItemException

Examples
The following example returns the details of a rule with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
response = client.get_rule(
    RuleId='example1ds3t-46da-4fdb-b8d5-abc321j569j5',
)

print(response)


Expected Output:
{
    'Rule': {
        'MetricName': 'WAFByteHeaderRule',
        'Name': 'WAFByteHeaderRule',
        'Predicates': [
            {
                'DataId': 'MyByteMatchSetID',
                'Negated': False,
                'Type': 'ByteMatch',
            },
        ],
        'RuleId': 'example1ds3t-46da-4fdb-b8d5-abc321j569j5',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Rule': {
            'RuleId': 'string',
            'Name': 'string',
            'MetricName': 'string',
            'Predicates': [
                {
                    'Negated': True|False,
                    'Type': 'IPMatch'|'ByteMatch'|'SqlInjectionMatch'|'GeoMatch'|'SizeConstraint'|'XssMatch'|'RegexMatch',
                    'DataId': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    WAFRegional.Client.exceptions.WAFInternalErrorException
    WAFRegional.Client.exceptions.WAFInvalidAccountException
    WAFRegional.Client.exceptions.WAFNonexistentItemException
    
    """
    pass

def get_rule_group(RuleGroupId=None):
    """
    Returns the  RuleGroup that is specified by the RuleGroupId that you included in the GetRuleGroup request.
    To view the rules in a rule group, use  ListActivatedRulesInRuleGroup .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_rule_group(
        RuleGroupId='string'
    )
    
    
    :type RuleGroupId: string
    :param RuleGroupId: [REQUIRED]\nThe RuleGroupId of the RuleGroup that you want to get. RuleGroupId is returned by CreateRuleGroup and by ListRuleGroups .\n

    :rtype: dict
ReturnsResponse Syntax{
    'RuleGroup': {
        'RuleGroupId': 'string',
        'Name': 'string',
        'MetricName': 'string'
    }
}


Response Structure

(dict) --
RuleGroup (dict) --Information about the  RuleGroup that you specified in the GetRuleGroup request.

RuleGroupId (string) --A unique identifier for a RuleGroup . You use RuleGroupId to get more information about a RuleGroup (see  GetRuleGroup ), update a RuleGroup (see  UpdateRuleGroup ), insert a RuleGroup into a WebACL or delete a one from a WebACL (see  UpdateWebACL ), or delete a RuleGroup from AWS WAF (see  DeleteRuleGroup ).

RuleGroupId is returned by  CreateRuleGroup and by  ListRuleGroups .

Name (string) --The friendly name or description for the RuleGroup . You can\'t change the name of a RuleGroup after you create it.

MetricName (string) --A friendly name or description for the metrics for this RuleGroup . The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can\'t contain whitespace or metric names reserved for AWS WAF, including "All" and "Default_Action." You can\'t change the name of the metric after you create the RuleGroup .








Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFNonexistentItemException


    :return: {
        'RuleGroup': {
            'RuleGroupId': 'string',
            'Name': 'string',
            'MetricName': 'string'
        }
    }
    
    
    """
    pass

def get_sampled_requests(WebAclId=None, RuleId=None, TimeWindow=None, MaxItems=None):
    """
    Gets detailed information about a specified number of requests--a sample--that AWS WAF randomly selects from among the first 5,000 requests that your AWS resource received during a time range that you choose. You can specify a sample size of up to 500 requests, and you can specify any time range in the previous three hours.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns detailed information about 100 requests --a sample-- that AWS WAF randomly selects from among the first 5,000 requests that your AWS resource received between the time period 2016-09-27T15:50Z to 2016-09-27T15:50Z.
    Expected Output:
    
    :example: response = client.get_sampled_requests(
        WebAclId='string',
        RuleId='string',
        TimeWindow={
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1)
        },
        MaxItems=123
    )
    
    
    :type WebAclId: string
    :param WebAclId: [REQUIRED]\nThe WebACLId of the WebACL for which you want GetSampledRequests to return a sample of requests.\n

    :type RuleId: string
    :param RuleId: [REQUIRED]\n\nRuleId is one of three values:\n\nThe RuleId of the Rule or the RuleGroupId of the RuleGroup for which you want GetSampledRequests to return a sample of requests.\nDefault_Action , which causes GetSampledRequests to return a sample of the requests that didn\'t match any of the rules in the specified WebACL .\n\n

    :type TimeWindow: dict
    :param TimeWindow: [REQUIRED]\nThe start date and time and the end date and time of the range for which you want GetSampledRequests to return a sample of requests. You must specify the times in Coordinated Universal Time (UTC) format. UTC format includes the special designator, Z . For example, '2016-09-27T14:50Z' . You can specify any time range in the previous three hours.\n\nStartTime (datetime) -- [REQUIRED]The beginning of the time range from which you want GetSampledRequests to return a sample of the requests that your AWS resource received. You must specify the date and time in Coordinated Universal Time (UTC) format. UTC format includes the special designator, Z . For example, '2016-09-27T14:50Z' . You can specify any time range in the previous three hours.\n\nEndTime (datetime) -- [REQUIRED]The end of the time range from which you want GetSampledRequests to return a sample of the requests that your AWS resource received. You must specify the date and time in Coordinated Universal Time (UTC) format. UTC format includes the special designator, Z . For example, '2016-09-27T14:50Z' . You can specify any time range in the previous three hours.\n\n\n

    :type MaxItems: integer
    :param MaxItems: [REQUIRED]\nThe number of requests that you want AWS WAF to return from among the first 5,000 requests that your AWS resource received during the time range. If your resource received fewer requests than the value of MaxItems , GetSampledRequests returns information about all of them.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'SampledRequests': [
        {
            'Request': {
                'ClientIP': 'string',
                'Country': 'string',
                'URI': 'string',
                'Method': 'string',
                'HTTPVersion': 'string',
                'Headers': [
                    {
                        'Name': 'string',
                        'Value': 'string'
                    },
                ]
            },
            'Weight': 123,
            'Timestamp': datetime(2015, 1, 1),
            'Action': 'string',
            'RuleWithinRuleGroup': 'string'
        },
    ],
    'PopulationSize': 123,
    'TimeWindow': {
        'StartTime': datetime(2015, 1, 1),
        'EndTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

SampledRequests (list) --
A complex type that contains detailed information about each of the requests in the sample.

(dict) --

Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


The response from a  GetSampledRequests request includes a SampledHTTPRequests complex type that appears as SampledRequests in the response syntax. SampledHTTPRequests contains one SampledHTTPRequest object for each web request that is returned by GetSampledRequests .

Request (dict) --
A complex type that contains detailed information about the request.

ClientIP (string) --
The IP address that the request originated from. If the WebACL is associated with a CloudFront distribution, this is the value of one of the following fields in CloudFront access logs:

c-ip , if the viewer did not use an HTTP proxy or a load balancer to send the request
x-forwarded-for , if the viewer did use an HTTP proxy or a load balancer to send the request


Country (string) --
The two-letter country code for the country that the request originated from. For a current list of country codes, see the Wikipedia entry ISO 3166-1 alpha-2 .

URI (string) --
The part of a web request that identifies the resource, for example, /images/daily-ad.jpg .

Method (string) --
The HTTP method specified in the sampled web request. CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .

HTTPVersion (string) --
The HTTP version specified in the sampled web request, for example, HTTP/1.1 .

Headers (list) --
A complex type that contains two values for each header in the sampled web request: the name of the header and the value of the header.

(dict) --

Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


The response from a  GetSampledRequests request includes an HTTPHeader complex type that appears as Headers in the response syntax. HTTPHeader contains the names and values of all of the headers that appear in one of the web requests that were returned by GetSampledRequests .

Name (string) --
The name of one of the headers in the sampled web request.

Value (string) --
The value of one of the headers in the sampled web request.







Weight (integer) --
A value that indicates how one result in the response relates proportionally to other results in the response. A result that has a weight of 2 represents roughly twice as many CloudFront web requests as a result that has a weight of 1 .

Timestamp (datetime) --
The time at which AWS WAF received the request from your AWS resource, in Unix time format (in seconds).

Action (string) --
The action for the Rule that the request matched: ALLOW , BLOCK , or COUNT .

RuleWithinRuleGroup (string) --
This value is returned if the GetSampledRequests request specifies the ID of a RuleGroup rather than the ID of an individual rule. RuleWithinRuleGroup is the rule within the specified RuleGroup that matched the request listed in the response.





PopulationSize (integer) --
The total number of requests from which GetSampledRequests got a sample of MaxItems requests. If PopulationSize is less than MaxItems , the sample includes every request that your AWS resource received during the specified time range.

TimeWindow (dict) --
Usually, TimeWindow is the time range that you specified in the GetSampledRequests request. However, if your AWS resource received more than 5,000 requests during the time range that you specified in the request, GetSampledRequests returns the time range for the first 5,000 requests. Times are in Coordinated Universal Time (UTC) format.

StartTime (datetime) --
The beginning of the time range from which you want GetSampledRequests to return a sample of the requests that your AWS resource received. You must specify the date and time in Coordinated Universal Time (UTC) format. UTC format includes the special designator, Z . For example, "2016-09-27T14:50Z" . You can specify any time range in the previous three hours.

EndTime (datetime) --
The end of the time range from which you want GetSampledRequests to return a sample of the requests that your AWS resource received. You must specify the date and time in Coordinated Universal Time (UTC) format. UTC format includes the special designator, Z . For example, "2016-09-27T14:50Z" . You can specify any time range in the previous three hours.









Exceptions

WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFInternalErrorException

Examples
The following example returns detailed information about 100 requests --a sample-- that AWS WAF randomly selects from among the first 5,000 requests that your AWS resource received between the time period 2016-09-27T15:50Z to 2016-09-27T15:50Z.
response = client.get_sampled_requests(
    MaxItems=100,
    RuleId='WAFRule-1-Example',
    TimeWindow={
        'EndTime': datetime(2016, 9, 27, 15, 50, 0, 1, 271, 0),
        'StartTime': datetime(2016, 9, 27, 15, 50, 0, 1, 271, 0),
    },
    WebAclId='createwebacl-1472061481310',
)

print(response)


Expected Output:
{
    'PopulationSize': 50,
    'SampledRequests': [
        {
            'Action': 'BLOCK',
            'Request': {
                'ClientIP': '192.0.2.44',
                'Country': 'US',
                'HTTPVersion': 'HTTP/1.1',
                'Headers': [
                    {
                        'Name': 'User-Agent',
                        'Value': 'BadBot ',
                    },
                ],
                'Method': 'HEAD',
            },
            'Timestamp': datetime(2016, 9, 27, 14, 55, 0, 1, 271, 0),
            'Weight': 1,
        },
    ],
    'TimeWindow': {
        'EndTime': datetime(2016, 9, 27, 15, 50, 0, 1, 271, 0),
        'StartTime': datetime(2016, 9, 27, 14, 50, 0, 1, 271, 0),
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'SampledRequests': [
            {
                'Request': {
                    'ClientIP': 'string',
                    'Country': 'string',
                    'URI': 'string',
                    'Method': 'string',
                    'HTTPVersion': 'string',
                    'Headers': [
                        {
                            'Name': 'string',
                            'Value': 'string'
                        },
                    ]
                },
                'Weight': 123,
                'Timestamp': datetime(2015, 1, 1),
                'Action': 'string',
                'RuleWithinRuleGroup': 'string'
            },
        ],
        'PopulationSize': 123,
        'TimeWindow': {
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    c-ip , if the viewer did not use an HTTP proxy or a load balancer to send the request
    x-forwarded-for , if the viewer did use an HTTP proxy or a load balancer to send the request
    
    """
    pass

def get_size_constraint_set(SizeConstraintSetId=None):
    """
    Returns the  SizeConstraintSet specified by SizeConstraintSetId .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns the details of a size constraint match set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    Expected Output:
    
    :example: response = client.get_size_constraint_set(
        SizeConstraintSetId='string'
    )
    
    
    :type SizeConstraintSetId: string
    :param SizeConstraintSetId: [REQUIRED]\nThe SizeConstraintSetId of the SizeConstraintSet that you want to get. SizeConstraintSetId is returned by CreateSizeConstraintSet and by ListSizeConstraintSets .\n

    :rtype: dict
ReturnsResponse Syntax{
    'SizeConstraintSet': {
        'SizeConstraintSetId': 'string',
        'Name': 'string',
        'SizeConstraints': [
            {
                'FieldToMatch': {
                    'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY'|'SINGLE_QUERY_ARG'|'ALL_QUERY_ARGS',
                    'Data': 'string'
                },
                'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE',
                'ComparisonOperator': 'EQ'|'NE'|'LE'|'LT'|'GE'|'GT',
                'Size': 123
            },
        ]
    }
}


Response Structure

(dict) --
SizeConstraintSet (dict) --Information about the  SizeConstraintSet that you specified in the GetSizeConstraintSet request. For more information, see the following topics:

SizeConstraintSet : Contains SizeConstraintSetId , SizeConstraints , and Name
SizeConstraints : Contains an array of  SizeConstraint objects. Each SizeConstraint object contains  FieldToMatch , TextTransformation , ComparisonOperator , and Size
FieldToMatch : Contains Data and Type


SizeConstraintSetId (string) --A unique identifier for a SizeConstraintSet . You use SizeConstraintSetId to get information about a SizeConstraintSet (see  GetSizeConstraintSet ), update a SizeConstraintSet (see  UpdateSizeConstraintSet ), insert a SizeConstraintSet into a Rule or delete one from a Rule (see  UpdateRule ), and delete a SizeConstraintSet from AWS WAF (see  DeleteSizeConstraintSet ).

SizeConstraintSetId is returned by  CreateSizeConstraintSet and by  ListSizeConstraintSets .

Name (string) --The name, if any, of the SizeConstraintSet .

SizeConstraints (list) --Specifies the parts of web requests that you want to inspect the size of.

(dict) --
Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Specifies a constraint on the size of a part of the web request. AWS WAF uses the Size , ComparisonOperator , and FieldToMatch to build an expression in the form of "Size ComparisonOperator size in bytes of FieldToMatch ". If that expression is true, the SizeConstraint is considered to match.

FieldToMatch (dict) --Specifies where in a web request to look for the size constraint.

Type (string) --The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:

HEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .
METHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .
QUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.
URI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .
BODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .
SINGLE_QUERY_ARG : The parameter in the query string that you will inspect, such as UserName or SalesRegion . The maximum length for SINGLE_QUERY_ARG is 30 characters.
ALL_QUERY_ARGS : Similar to SINGLE_QUERY_ARG , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in TargetString .


Data (string) --When the value of Type is HEADER , enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer . The name of the header is not case sensitive.
When the value of Type is SINGLE_QUERY_ARG , enter the name of the parameter that you want AWS WAF to search, for example, UserName or SalesRegion . The parameter name is not case sensitive.
If the value of Type is any other value, omit Data .



TextTransformation (string) --Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on FieldToMatch before inspecting it for a match.
You can only specify a single type of TextTransformation.
Note that if you choose BODY for the value of Type , you must choose NONE for TextTransformation because CloudFront forwards only the first 8192 bytes for inspection.

NONE
Specify NONE if you don\'t want to perform any text transformations.

CMD_LINE
When you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: " \' ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE
Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a "less than" symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE
Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE
Use this option to decode a URL-encoded value.

ComparisonOperator (string) --The type of comparison you want AWS WAF to perform. AWS WAF uses this in combination with the provided Size and FieldToMatch to build an expression in the form of "Size ComparisonOperator size in bytes of FieldToMatch ". If that expression is true, the SizeConstraint is considered to match.

EQ : Used to test if the Size is equal to the size of the FieldToMatchNE : Used to test if the Size is not equal to the size of the FieldToMatch
LE : Used to test if the Size is less than or equal to the size of the FieldToMatch
LT : Used to test if the Size is strictly less than the size of the FieldToMatch
GE : Used to test if the Size is greater than or equal to the size of the FieldToMatch
GT : Used to test if the Size is strictly greater than the size of the FieldToMatch


Size (integer) --The size in bytes that you want AWS WAF to compare against the size of the specified FieldToMatch . AWS WAF uses this in combination with ComparisonOperator and FieldToMatch to build an expression in the form of "Size ComparisonOperator size in bytes of FieldToMatch ". If that expression is true, the SizeConstraint is considered to match.
Valid values for size are 0 - 21474836480 bytes (0 - 20 GB).
If you specify URI for the value of Type , the / in the URI counts as one character. For example, the URI /logo.jpg is nine characters long.












Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFNonexistentItemException

Examples
The following example returns the details of a size constraint match set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
response = client.get_size_constraint_set(
    SizeConstraintSetId='example1ds3t-46da-4fdb-b8d5-abc321j569j5',
)

print(response)


Expected Output:
{
    'SizeConstraintSet': {
        'Name': 'MySampleSizeConstraintSet',
        'SizeConstraintSetId': 'example1ds3t-46da-4fdb-b8d5-abc321j569j5',
        'SizeConstraints': [
            {
                'ComparisonOperator': 'GT',
                'FieldToMatch': {
                    'Type': 'QUERY_STRING',
                },
                'Size': 0,
                'TextTransformation': 'NONE',
            },
        ],
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'SizeConstraintSet': {
            'SizeConstraintSetId': 'string',
            'Name': 'string',
            'SizeConstraints': [
                {
                    'FieldToMatch': {
                        'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY'|'SINGLE_QUERY_ARG'|'ALL_QUERY_ARGS',
                        'Data': 'string'
                    },
                    'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE',
                    'ComparisonOperator': 'EQ'|'NE'|'LE'|'LT'|'GE'|'GT',
                    'Size': 123
                },
            ]
        }
    }
    
    
    :returns: 
    HEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .
    METHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .
    QUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.
    URI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .
    BODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .
    SINGLE_QUERY_ARG : The parameter in the query string that you will inspect, such as UserName or SalesRegion . The maximum length for SINGLE_QUERY_ARG is 30 characters.
    ALL_QUERY_ARGS : Similar to SINGLE_QUERY_ARG , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in TargetString .
    
    """
    pass

def get_sql_injection_match_set(SqlInjectionMatchSetId=None):
    """
    Returns the  SqlInjectionMatchSet that is specified by SqlInjectionMatchSetId .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns the details of a SQL injection match set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    Expected Output:
    
    :example: response = client.get_sql_injection_match_set(
        SqlInjectionMatchSetId='string'
    )
    
    
    :type SqlInjectionMatchSetId: string
    :param SqlInjectionMatchSetId: [REQUIRED]\nThe SqlInjectionMatchSetId of the SqlInjectionMatchSet that you want to get. SqlInjectionMatchSetId is returned by CreateSqlInjectionMatchSet and by ListSqlInjectionMatchSets .\n

    :rtype: dict
ReturnsResponse Syntax{
    'SqlInjectionMatchSet': {
        'SqlInjectionMatchSetId': 'string',
        'Name': 'string',
        'SqlInjectionMatchTuples': [
            {
                'FieldToMatch': {
                    'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY'|'SINGLE_QUERY_ARG'|'ALL_QUERY_ARGS',
                    'Data': 'string'
                },
                'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
            },
        ]
    }
}


Response Structure

(dict) --The response to a  GetSqlInjectionMatchSet request.

SqlInjectionMatchSet (dict) --Information about the  SqlInjectionMatchSet that you specified in the GetSqlInjectionMatchSet request. For more information, see the following topics:

SqlInjectionMatchSet : Contains Name , SqlInjectionMatchSetId , and an array of SqlInjectionMatchTuple objects
SqlInjectionMatchTuple : Each SqlInjectionMatchTuple object contains FieldToMatch and TextTransformation
FieldToMatch : Contains Data and Type


SqlInjectionMatchSetId (string) --A unique identifier for a SqlInjectionMatchSet . You use SqlInjectionMatchSetId to get information about a SqlInjectionMatchSet (see  GetSqlInjectionMatchSet ), update a SqlInjectionMatchSet (see  UpdateSqlInjectionMatchSet ), insert a SqlInjectionMatchSet into a Rule or delete one from a Rule (see  UpdateRule ), and delete a SqlInjectionMatchSet from AWS WAF (see  DeleteSqlInjectionMatchSet ).

SqlInjectionMatchSetId is returned by  CreateSqlInjectionMatchSet and by  ListSqlInjectionMatchSets .

Name (string) --The name, if any, of the SqlInjectionMatchSet .

SqlInjectionMatchTuples (list) --Specifies the parts of web requests that you want to inspect for snippets of malicious SQL code.

(dict) --
Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Specifies the part of a web request that you want AWS WAF to inspect for snippets of malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.

FieldToMatch (dict) --Specifies where in a web request to look for snippets of malicious SQL code.

Type (string) --The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:

HEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .
METHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .
QUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.
URI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .
BODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .
SINGLE_QUERY_ARG : The parameter in the query string that you will inspect, such as UserName or SalesRegion . The maximum length for SINGLE_QUERY_ARG is 30 characters.
ALL_QUERY_ARGS : Similar to SINGLE_QUERY_ARG , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in TargetString .


Data (string) --When the value of Type is HEADER , enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer . The name of the header is not case sensitive.
When the value of Type is SINGLE_QUERY_ARG , enter the name of the parameter that you want AWS WAF to search, for example, UserName or SalesRegion . The parameter name is not case sensitive.
If the value of Type is any other value, omit Data .



TextTransformation (string) --Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on FieldToMatch before inspecting it for a match.
You can only specify a single type of TextTransformation.

CMD_LINE
When you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: " \' ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE
Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a "less than" symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE
Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE
Use this option to decode a URL-encoded value.

NONE
Specify NONE if you don\'t want to perform any text transformations.












Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFNonexistentItemException

Examples
The following example returns the details of a SQL injection match set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
response = client.get_sql_injection_match_set(
    SqlInjectionMatchSetId='example1ds3t-46da-4fdb-b8d5-abc321j569j5',
)

print(response)


Expected Output:
{
    'SqlInjectionMatchSet': {
        'Name': 'MySQLInjectionMatchSet',
        'SqlInjectionMatchSetId': 'example1ds3t-46da-4fdb-b8d5-abc321j569j5',
        'SqlInjectionMatchTuples': [
            {
                'FieldToMatch': {
                    'Type': 'QUERY_STRING',
                },
                'TextTransformation': 'URL_DECODE',
            },
        ],
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'SqlInjectionMatchSet': {
            'SqlInjectionMatchSetId': 'string',
            'Name': 'string',
            'SqlInjectionMatchTuples': [
                {
                    'FieldToMatch': {
                        'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY'|'SINGLE_QUERY_ARG'|'ALL_QUERY_ARGS',
                        'Data': 'string'
                    },
                    'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                },
            ]
        }
    }
    
    
    :returns: 
    HEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .
    METHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .
    QUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.
    URI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .
    BODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .
    SINGLE_QUERY_ARG : The parameter in the query string that you will inspect, such as UserName or SalesRegion . The maximum length for SINGLE_QUERY_ARG is 30 characters.
    ALL_QUERY_ARGS : Similar to SINGLE_QUERY_ARG , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in TargetString .
    
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

def get_web_acl(WebACLId=None):
    """
    Returns the  WebACL that is specified by WebACLId .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns the details of a web ACL with the ID createwebacl-1472061481310.
    Expected Output:
    
    :example: response = client.get_web_acl(
        WebACLId='string'
    )
    
    
    :type WebACLId: string
    :param WebACLId: [REQUIRED]\nThe WebACLId of the WebACL that you want to get. WebACLId is returned by CreateWebACL and by ListWebACLs .\n

    :rtype: dict
ReturnsResponse Syntax{
    'WebACL': {
        'WebACLId': 'string',
        'Name': 'string',
        'MetricName': 'string',
        'DefaultAction': {
            'Type': 'BLOCK'|'ALLOW'|'COUNT'
        },
        'Rules': [
            {
                'Priority': 123,
                'RuleId': 'string',
                'Action': {
                    'Type': 'BLOCK'|'ALLOW'|'COUNT'
                },
                'OverrideAction': {
                    'Type': 'NONE'|'COUNT'
                },
                'Type': 'REGULAR'|'RATE_BASED'|'GROUP',
                'ExcludedRules': [
                    {
                        'RuleId': 'string'
                    },
                ]
            },
        ],
        'WebACLArn': 'string'
    }
}


Response Structure

(dict) --
WebACL (dict) --Information about the  WebACL that you specified in the GetWebACL request. For more information, see the following topics:

WebACL : Contains DefaultAction , MetricName , Name , an array of Rule objects, and WebACLId
DefaultAction (Data type is  WafAction ): Contains Type
Rules : Contains an array of ActivatedRule objects, which contain Action , Priority , and RuleId
Action : Contains Type


WebACLId (string) --A unique identifier for a WebACL . You use WebACLId to get information about a WebACL (see  GetWebACL ), update a WebACL (see  UpdateWebACL ), and delete a WebACL from AWS WAF (see  DeleteWebACL ).

WebACLId is returned by  CreateWebACL and by  ListWebACLs .

Name (string) --A friendly name or description of the WebACL . You can\'t change the name of a WebACL after you create it.

MetricName (string) --A friendly name or description for the metrics for this WebACL . The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can\'t contain whitespace or metric names reserved for AWS WAF, including "All" and "Default_Action." You can\'t change MetricName after you create the WebACL .

DefaultAction (dict) --The action to perform if none of the Rules contained in the WebACL match. The action is specified by the  WafAction object.

Type (string) --Specifies how you want AWS WAF to respond to requests that match the settings in a Rule . Valid settings include the following:

ALLOW : AWS WAF allows requests
BLOCK : AWS WAF blocks requests
COUNT : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can\'t specify COUNT for the default action for a WebACL .




Rules (list) --An array that contains the action for each Rule in a WebACL , the priority of the Rule , and the ID of the Rule .

(dict) --
Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

The ActivatedRule object in an  UpdateWebACL request specifies a Rule that you want to insert or delete, the priority of the Rule in the WebACL , and the action that you want AWS WAF to take when a web request matches the Rule (ALLOW , BLOCK , or COUNT ).
To specify whether to insert or delete a Rule , use the Action parameter in the  WebACLUpdate data type.

Priority (integer) --Specifies the order in which the Rules in a WebACL are evaluated. Rules with a lower value for Priority are evaluated before Rules with a higher value. The value must be a unique integer. If you add multiple Rules to a WebACL , the values don\'t need to be consecutive.

RuleId (string) --The RuleId for a Rule . You use RuleId to get more information about a Rule (see  GetRule ), update a Rule (see  UpdateRule ), insert a Rule into a WebACL or delete a one from a WebACL (see  UpdateWebACL ), or delete a Rule from AWS WAF (see  DeleteRule ).

RuleId is returned by  CreateRule and by  ListRules .

Action (dict) --Specifies the action that CloudFront or AWS WAF takes when a web request matches the conditions in the Rule . Valid values for Action include the following:

ALLOW : CloudFront responds with the requested object.
BLOCK : CloudFront responds with an HTTP 403 (Forbidden) status code.
COUNT : AWS WAF increments a counter of requests that match the conditions in the rule and then continues to inspect the web request based on the remaining rules in the web ACL.


ActivatedRule|OverrideAction applies only when updating or adding a RuleGroup to a WebACL . In this case, you do not use ActivatedRule|Action . For all other update requests, ActivatedRule|Action is used instead of ActivatedRule|OverrideAction .

Type (string) --Specifies how you want AWS WAF to respond to requests that match the settings in a Rule . Valid settings include the following:

ALLOW : AWS WAF allows requests
BLOCK : AWS WAF blocks requests
COUNT : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can\'t specify COUNT for the default action for a WebACL .




OverrideAction (dict) --Use the OverrideAction to test your RuleGroup .
Any rule in a RuleGroup can potentially block a request. If you set the OverrideAction to None , the RuleGroup will block a request if any individual rule in the RuleGroup matches the request and is configured to block that request. However if you first want to test the RuleGroup , set the OverrideAction to Count . The RuleGroup will then override any block action specified by individual rules contained within the group. Instead of blocking matching requests, those requests will be counted. You can view a record of counted requests using  GetSampledRequests .

ActivatedRule|OverrideAction applies only when updating or adding a RuleGroup to a WebACL . In this case you do not use ActivatedRule|Action . For all other update requests, ActivatedRule|Action is used instead of ActivatedRule|OverrideAction .

Type (string) --
COUNT overrides the action specified by the individual rule within a RuleGroup . If set to NONE , the rule\'s action will take place.



Type (string) --The rule type, either REGULAR , as defined by  Rule , RATE_BASED , as defined by  RateBasedRule , or GROUP , as defined by  RuleGroup . The default is REGULAR. Although this field is optional, be aware that if you try to add a RATE_BASED rule to a web ACL without setting the type, the  UpdateWebACL request will fail because the request tries to add a REGULAR rule with the specified ID, which does not exist.

ExcludedRules (list) --An array of rules to exclude from a rule group. This is applicable only when the ActivatedRule refers to a RuleGroup .
Sometimes it is necessary to troubleshoot rule groups that are blocking traffic unexpectedly (false positives). One troubleshooting technique is to identify the specific rule within the rule group that is blocking the legitimate traffic and then disable (exclude) that particular rule. You can exclude rules from both your own rule groups and AWS Marketplace rule groups that have been associated with a web ACL.
Specifying ExcludedRules does not remove those rules from the rule group. Rather, it changes the action for the rules to COUNT . Therefore, requests that match an ExcludedRule are counted but not blocked. The RuleGroup owner will receive COUNT metrics for each ExcludedRule .
If you want to exclude rules from a rule group that is already associated with a web ACL, perform the following steps:

Use the AWS WAF logs to identify the IDs of the rules that you want to exclude. For more information about the logs, see Logging Web ACL Traffic Information .
Submit an  UpdateWebACL request that has two actions:
The first action deletes the existing rule group from the web ACL. That is, in the  UpdateWebACL request, the first Updates:Action should be DELETE and Updates:ActivatedRule:RuleId should be the rule group that contains the rules that you want to exclude.
The second action inserts the same rule group back in, but specifying the rules to exclude. That is, the second Updates:Action should be INSERT , Updates:ActivatedRule:RuleId should be the rule group that you just removed, and ExcludedRules should contain the rules that you want to exclude.




(dict) --
Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

The rule to exclude from a rule group. This is applicable only when the ActivatedRule refers to a RuleGroup . The rule must belong to the RuleGroup that is specified by the ActivatedRule .

RuleId (string) --The unique identifier for the rule to exclude from the rule group.









WebACLArn (string) --Tha Amazon Resource Name (ARN) of the web ACL.








Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFNonexistentItemException

Examples
The following example returns the details of a web ACL with the ID createwebacl-1472061481310.
response = client.get_web_acl(
    WebACLId='createwebacl-1472061481310',
)

print(response)


Expected Output:
{
    'WebACL': {
        'DefaultAction': {
            'Type': 'ALLOW',
        },
        'MetricName': 'CreateExample',
        'Name': 'CreateExample',
        'Rules': [
            {
                'Action': {
                    'Type': 'ALLOW',
                },
                'Priority': 1,
                'RuleId': 'WAFRule-1-Example',
            },
        ],
        'WebACLId': 'createwebacl-1472061481310',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'WebACL': {
            'WebACLId': 'string',
            'Name': 'string',
            'MetricName': 'string',
            'DefaultAction': {
                'Type': 'BLOCK'|'ALLOW'|'COUNT'
            },
            'Rules': [
                {
                    'Priority': 123,
                    'RuleId': 'string',
                    'Action': {
                        'Type': 'BLOCK'|'ALLOW'|'COUNT'
                    },
                    'OverrideAction': {
                        'Type': 'NONE'|'COUNT'
                    },
                    'Type': 'REGULAR'|'RATE_BASED'|'GROUP',
                    'ExcludedRules': [
                        {
                            'RuleId': 'string'
                        },
                    ]
                },
            ],
            'WebACLArn': 'string'
        }
    }
    
    
    :returns: 
    ALLOW : AWS WAF allows requests
    BLOCK : AWS WAF blocks requests
    COUNT : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can\'t specify COUNT for the default action for a WebACL .
    
    """
    pass

def get_web_acl_for_resource(ResourceArn=None):
    """
    Returns the web ACL for the specified resource, either an application load balancer or Amazon API Gateway stage.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_web_acl_for_resource(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe ARN (Amazon Resource Name) of the resource for which to get the web ACL, either an application load balancer or Amazon API Gateway stage.\nThe ARN should be in one of the following formats:\n\nFor an Application Load Balancer: ``arn:aws:elasticloadbalancing:region :account-id :loadbalancer/app/load-balancer-name /load-balancer-id ``\nFor an Amazon API Gateway stage: ``arn:aws:apigateway:region ::/restapis/api-id /stages/stage-name ``\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'WebACLSummary': {
        'WebACLId': 'string',
        'Name': 'string'
    }
}


Response Structure

(dict) --
WebACLSummary (dict) --Information about the web ACL that you specified in the GetWebACLForResource request. If there is no associated resource, a null WebACLSummary is returned.

WebACLId (string) --A unique identifier for a WebACL . You use WebACLId to get information about a WebACL (see  GetWebACL ), update a WebACL (see  UpdateWebACL ), and delete a WebACL from AWS WAF (see  DeleteWebACL ).

WebACLId is returned by  CreateWebACL and by  ListWebACLs .

Name (string) --A friendly name or description of the  WebACL . You can\'t change the name of a WebACL after you create it.








Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFInvalidParameterException
WAFRegional.Client.exceptions.WAFUnavailableEntityException


    :return: {
        'WebACLSummary': {
            'WebACLId': 'string',
            'Name': 'string'
        }
    }
    
    
    :returns: 
    WAFRegional.Client.exceptions.WAFInternalErrorException
    WAFRegional.Client.exceptions.WAFInvalidAccountException
    WAFRegional.Client.exceptions.WAFNonexistentItemException
    WAFRegional.Client.exceptions.WAFInvalidParameterException
    WAFRegional.Client.exceptions.WAFUnavailableEntityException
    
    """
    pass

def get_xss_match_set(XssMatchSetId=None):
    """
    Returns the  XssMatchSet that is specified by XssMatchSetId .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns the details of an XSS match set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    Expected Output:
    
    :example: response = client.get_xss_match_set(
        XssMatchSetId='string'
    )
    
    
    :type XssMatchSetId: string
    :param XssMatchSetId: [REQUIRED]\nThe XssMatchSetId of the XssMatchSet that you want to get. XssMatchSetId is returned by CreateXssMatchSet and by ListXssMatchSets .\n

    :rtype: dict
ReturnsResponse Syntax{
    'XssMatchSet': {
        'XssMatchSetId': 'string',
        'Name': 'string',
        'XssMatchTuples': [
            {
                'FieldToMatch': {
                    'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY'|'SINGLE_QUERY_ARG'|'ALL_QUERY_ARGS',
                    'Data': 'string'
                },
                'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
            },
        ]
    }
}


Response Structure

(dict) --The response to a  GetXssMatchSet request.

XssMatchSet (dict) --Information about the  XssMatchSet that you specified in the GetXssMatchSet request. For more information, see the following topics:

XssMatchSet : Contains Name , XssMatchSetId , and an array of XssMatchTuple objects
XssMatchTuple : Each XssMatchTuple object contains FieldToMatch and TextTransformation
FieldToMatch : Contains Data and Type


XssMatchSetId (string) --A unique identifier for an XssMatchSet . You use XssMatchSetId to get information about an XssMatchSet (see  GetXssMatchSet ), update an XssMatchSet (see  UpdateXssMatchSet ), insert an XssMatchSet into a Rule or delete one from a Rule (see  UpdateRule ), and delete an XssMatchSet from AWS WAF (see  DeleteXssMatchSet ).

XssMatchSetId is returned by  CreateXssMatchSet and by  ListXssMatchSets .

Name (string) --The name, if any, of the XssMatchSet .

XssMatchTuples (list) --Specifies the parts of web requests that you want to inspect for cross-site scripting attacks.

(dict) --
Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Specifies the part of a web request that you want AWS WAF to inspect for cross-site scripting attacks and, if you want AWS WAF to inspect a header, the name of the header.

FieldToMatch (dict) --Specifies where in a web request to look for cross-site scripting attacks.

Type (string) --The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:

HEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .
METHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .
QUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.
URI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .
BODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .
SINGLE_QUERY_ARG : The parameter in the query string that you will inspect, such as UserName or SalesRegion . The maximum length for SINGLE_QUERY_ARG is 30 characters.
ALL_QUERY_ARGS : Similar to SINGLE_QUERY_ARG , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in TargetString .


Data (string) --When the value of Type is HEADER , enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer . The name of the header is not case sensitive.
When the value of Type is SINGLE_QUERY_ARG , enter the name of the parameter that you want AWS WAF to search, for example, UserName or SalesRegion . The parameter name is not case sensitive.
If the value of Type is any other value, omit Data .



TextTransformation (string) --Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on FieldToMatch before inspecting it for a match.
You can only specify a single type of TextTransformation.

CMD_LINE
When you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: " \' ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE
Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a "less than" symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE
Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE
Use this option to decode a URL-encoded value.

NONE
Specify NONE if you don\'t want to perform any text transformations.












Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFNonexistentItemException

Examples
The following example returns the details of an XSS match set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
response = client.get_xss_match_set(
    XssMatchSetId='example1ds3t-46da-4fdb-b8d5-abc321j569j5',
)

print(response)


Expected Output:
{
    'XssMatchSet': {
        'Name': 'MySampleXssMatchSet',
        'XssMatchSetId': 'example1ds3t-46da-4fdb-b8d5-abc321j569j5',
        'XssMatchTuples': [
            {
                'FieldToMatch': {
                    'Type': 'QUERY_STRING',
                },
                'TextTransformation': 'URL_DECODE',
            },
        ],
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'XssMatchSet': {
            'XssMatchSetId': 'string',
            'Name': 'string',
            'XssMatchTuples': [
                {
                    'FieldToMatch': {
                        'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY'|'SINGLE_QUERY_ARG'|'ALL_QUERY_ARGS',
                        'Data': 'string'
                    },
                    'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                },
            ]
        }
    }
    
    
    :returns: 
    HEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .
    METHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .
    QUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.
    URI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .
    BODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .
    SINGLE_QUERY_ARG : The parameter in the query string that you will inspect, such as UserName or SalesRegion . The maximum length for SINGLE_QUERY_ARG is 30 characters.
    ALL_QUERY_ARGS : Similar to SINGLE_QUERY_ARG , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in TargetString .
    
    """
    pass

def list_activated_rules_in_rule_group(RuleGroupId=None, NextMarker=None, Limit=None):
    """
    Returns an array of  ActivatedRule objects.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_activated_rules_in_rule_group(
        RuleGroupId='string',
        NextMarker='string',
        Limit=123
    )
    
    
    :type RuleGroupId: string
    :param RuleGroupId: The RuleGroupId of the RuleGroup for which you want to get a list of ActivatedRule objects.

    :type NextMarker: string
    :param NextMarker: If you specify a value for Limit and you have more ActivatedRules than the value of Limit , AWS WAF returns a NextMarker value in the response that allows you to list another group of ActivatedRules . For the second and subsequent ListActivatedRulesInRuleGroup requests, specify the value of NextMarker from the previous response to get information about another batch of ActivatedRules .

    :type Limit: integer
    :param Limit: Specifies the number of ActivatedRules that you want AWS WAF to return for this request. If you have more ActivatedRules than the number that you specify for Limit , the response includes a NextMarker value that you can use to get another batch of ActivatedRules .

    :rtype: dict

ReturnsResponse Syntax
{
    'NextMarker': 'string',
    'ActivatedRules': [
        {
            'Priority': 123,
            'RuleId': 'string',
            'Action': {
                'Type': 'BLOCK'|'ALLOW'|'COUNT'
            },
            'OverrideAction': {
                'Type': 'NONE'|'COUNT'
            },
            'Type': 'REGULAR'|'RATE_BASED'|'GROUP',
            'ExcludedRules': [
                {
                    'RuleId': 'string'
                },
            ]
        },
    ]
}


Response Structure

(dict) --

NextMarker (string) --
If you have more ActivatedRules than the number that you specified for Limit in the request, the response includes a NextMarker value. To list more ActivatedRules , submit another ListActivatedRulesInRuleGroup request, and specify the NextMarker value from the response in the NextMarker value in the next request.

ActivatedRules (list) --
An array of ActivatedRules objects.

(dict) --

Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


The ActivatedRule object in an  UpdateWebACL request specifies a Rule that you want to insert or delete, the priority of the Rule in the WebACL , and the action that you want AWS WAF to take when a web request matches the Rule (ALLOW , BLOCK , or COUNT ).
To specify whether to insert or delete a Rule , use the Action parameter in the  WebACLUpdate data type.

Priority (integer) --
Specifies the order in which the Rules in a WebACL are evaluated. Rules with a lower value for Priority are evaluated before Rules with a higher value. The value must be a unique integer. If you add multiple Rules to a WebACL , the values don\'t need to be consecutive.

RuleId (string) --
The RuleId for a Rule . You use RuleId to get more information about a Rule (see  GetRule ), update a Rule (see  UpdateRule ), insert a Rule into a WebACL or delete a one from a WebACL (see  UpdateWebACL ), or delete a Rule from AWS WAF (see  DeleteRule ).

RuleId is returned by  CreateRule and by  ListRules .


Action (dict) --
Specifies the action that CloudFront or AWS WAF takes when a web request matches the conditions in the Rule . Valid values for Action include the following:

ALLOW : CloudFront responds with the requested object.
BLOCK : CloudFront responds with an HTTP 403 (Forbidden) status code.
COUNT : AWS WAF increments a counter of requests that match the conditions in the rule and then continues to inspect the web request based on the remaining rules in the web ACL.


ActivatedRule|OverrideAction applies only when updating or adding a RuleGroup to a WebACL . In this case, you do not use ActivatedRule|Action . For all other update requests, ActivatedRule|Action is used instead of ActivatedRule|OverrideAction .


Type (string) --
Specifies how you want AWS WAF to respond to requests that match the settings in a Rule . Valid settings include the following:

ALLOW : AWS WAF allows requests
BLOCK : AWS WAF blocks requests
COUNT : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can\'t specify COUNT for the default action for a WebACL .




OverrideAction (dict) --
Use the OverrideAction to test your RuleGroup .
Any rule in a RuleGroup can potentially block a request. If you set the OverrideAction to None , the RuleGroup will block a request if any individual rule in the RuleGroup matches the request and is configured to block that request. However if you first want to test the RuleGroup , set the OverrideAction to Count . The RuleGroup will then override any block action specified by individual rules contained within the group. Instead of blocking matching requests, those requests will be counted. You can view a record of counted requests using  GetSampledRequests .

ActivatedRule|OverrideAction applies only when updating or adding a RuleGroup to a WebACL . In this case you do not use ActivatedRule|Action . For all other update requests, ActivatedRule|Action is used instead of ActivatedRule|OverrideAction .


Type (string) --

COUNT overrides the action specified by the individual rule within a RuleGroup . If set to NONE , the rule\'s action will take place.




Type (string) --
The rule type, either REGULAR , as defined by  Rule , RATE_BASED , as defined by  RateBasedRule , or GROUP , as defined by  RuleGroup . The default is REGULAR. Although this field is optional, be aware that if you try to add a RATE_BASED rule to a web ACL without setting the type, the  UpdateWebACL request will fail because the request tries to add a REGULAR rule with the specified ID, which does not exist.

ExcludedRules (list) --
An array of rules to exclude from a rule group. This is applicable only when the ActivatedRule refers to a RuleGroup .
Sometimes it is necessary to troubleshoot rule groups that are blocking traffic unexpectedly (false positives). One troubleshooting technique is to identify the specific rule within the rule group that is blocking the legitimate traffic and then disable (exclude) that particular rule. You can exclude rules from both your own rule groups and AWS Marketplace rule groups that have been associated with a web ACL.
Specifying ExcludedRules does not remove those rules from the rule group. Rather, it changes the action for the rules to COUNT . Therefore, requests that match an ExcludedRule are counted but not blocked. The RuleGroup owner will receive COUNT metrics for each ExcludedRule .
If you want to exclude rules from a rule group that is already associated with a web ACL, perform the following steps:

Use the AWS WAF logs to identify the IDs of the rules that you want to exclude. For more information about the logs, see Logging Web ACL Traffic Information .
Submit an  UpdateWebACL request that has two actions:
The first action deletes the existing rule group from the web ACL. That is, in the  UpdateWebACL request, the first Updates:Action should be DELETE and Updates:ActivatedRule:RuleId should be the rule group that contains the rules that you want to exclude.
The second action inserts the same rule group back in, but specifying the rules to exclude. That is, the second Updates:Action should be INSERT , Updates:ActivatedRule:RuleId should be the rule group that you just removed, and ExcludedRules should contain the rules that you want to exclude.




(dict) --

Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


The rule to exclude from a rule group. This is applicable only when the ActivatedRule refers to a RuleGroup . The rule must belong to the RuleGroup that is specified by the ActivatedRule .

RuleId (string) --
The unique identifier for the rule to exclude from the rule group.















Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFInvalidParameterException


    :return: {
        'NextMarker': 'string',
        'ActivatedRules': [
            {
                'Priority': 123,
                'RuleId': 'string',
                'Action': {
                    'Type': 'BLOCK'|'ALLOW'|'COUNT'
                },
                'OverrideAction': {
                    'Type': 'NONE'|'COUNT'
                },
                'Type': 'REGULAR'|'RATE_BASED'|'GROUP',
                'ExcludedRules': [
                    {
                        'RuleId': 'string'
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    ALLOW : CloudFront responds with the requested object.
    BLOCK : CloudFront responds with an HTTP 403 (Forbidden) status code.
    COUNT : AWS WAF increments a counter of requests that match the conditions in the rule and then continues to inspect the web request based on the remaining rules in the web ACL.
    
    """
    pass

def list_byte_match_sets(NextMarker=None, Limit=None):
    """
    Returns an array of  ByteMatchSetSummary objects.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_byte_match_sets(
        NextMarker='string',
        Limit=123
    )
    
    
    :type NextMarker: string
    :param NextMarker: If you specify a value for Limit and you have more ByteMatchSets than the value of Limit , AWS WAF returns a NextMarker value in the response that allows you to list another group of ByteMatchSets . For the second and subsequent ListByteMatchSets requests, specify the value of NextMarker from the previous response to get information about another batch of ByteMatchSets .

    :type Limit: integer
    :param Limit: Specifies the number of ByteMatchSet objects that you want AWS WAF to return for this request. If you have more ByteMatchSets objects than the number you specify for Limit , the response includes a NextMarker value that you can use to get another batch of ByteMatchSet objects.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextMarker': 'string',
    'ByteMatchSets': [
        {
            'ByteMatchSetId': 'string',
            'Name': 'string'
        },
    ]
}


Response Structure

(dict) --

NextMarker (string) --
If you have more ByteMatchSet objects than the number that you specified for Limit in the request, the response includes a NextMarker value. To list more ByteMatchSet objects, submit another ListByteMatchSets request, and specify the NextMarker value from the response in the NextMarker value in the next request.

ByteMatchSets (list) --
An array of  ByteMatchSetSummary objects.

(dict) --

Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


Returned by  ListByteMatchSets . Each ByteMatchSetSummary object includes the Name and ByteMatchSetId for one  ByteMatchSet .

ByteMatchSetId (string) --
The ByteMatchSetId for a ByteMatchSet . You use ByteMatchSetId to get information about a ByteMatchSet , update a ByteMatchSet , remove a ByteMatchSet from a Rule , and delete a ByteMatchSet from AWS WAF.

ByteMatchSetId is returned by  CreateByteMatchSet and by  ListByteMatchSets .


Name (string) --
A friendly name or description of the  ByteMatchSet . You can\'t change Name after you create a ByteMatchSet .











Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException


    :return: {
        'NextMarker': 'string',
        'ByteMatchSets': [
            {
                'ByteMatchSetId': 'string',
                'Name': 'string'
            },
        ]
    }
    
    
    :returns: 
    WAFRegional.Client.exceptions.WAFInternalErrorException
    WAFRegional.Client.exceptions.WAFInvalidAccountException
    
    """
    pass

def list_geo_match_sets(NextMarker=None, Limit=None):
    """
    Returns an array of  GeoMatchSetSummary objects in the response.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_geo_match_sets(
        NextMarker='string',
        Limit=123
    )
    
    
    :type NextMarker: string
    :param NextMarker: If you specify a value for Limit and you have more GeoMatchSet s than the value of Limit , AWS WAF returns a NextMarker value in the response that allows you to list another group of GeoMatchSet objects. For the second and subsequent ListGeoMatchSets requests, specify the value of NextMarker from the previous response to get information about another batch of GeoMatchSet objects.

    :type Limit: integer
    :param Limit: Specifies the number of GeoMatchSet objects that you want AWS WAF to return for this request. If you have more GeoMatchSet objects than the number you specify for Limit , the response includes a NextMarker value that you can use to get another batch of GeoMatchSet objects.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextMarker': 'string',
    'GeoMatchSets': [
        {
            'GeoMatchSetId': 'string',
            'Name': 'string'
        },
    ]
}


Response Structure

(dict) --

NextMarker (string) --
If you have more GeoMatchSet objects than the number that you specified for Limit in the request, the response includes a NextMarker value. To list more GeoMatchSet objects, submit another ListGeoMatchSets request, and specify the NextMarker value from the response in the NextMarker value in the next request.

GeoMatchSets (list) --
An array of  GeoMatchSetSummary objects.

(dict) --

Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


Contains the identifier and the name of the GeoMatchSet .

GeoMatchSetId (string) --
The GeoMatchSetId for an  GeoMatchSet . You can use GeoMatchSetId in a  GetGeoMatchSet request to get detailed information about an  GeoMatchSet .

Name (string) --
A friendly name or description of the  GeoMatchSet . You can\'t change the name of an GeoMatchSet after you create it.











Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException


    :return: {
        'NextMarker': 'string',
        'GeoMatchSets': [
            {
                'GeoMatchSetId': 'string',
                'Name': 'string'
            },
        ]
    }
    
    
    :returns: 
    WAFRegional.Client.exceptions.WAFInternalErrorException
    WAFRegional.Client.exceptions.WAFInvalidAccountException
    
    """
    pass

def list_ip_sets(NextMarker=None, Limit=None):
    """
    Returns an array of  IPSetSummary objects in the response.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns an array of up to 100 IP match sets.
    Expected Output:
    
    :example: response = client.list_ip_sets(
        NextMarker='string',
        Limit=123
    )
    
    
    :type NextMarker: string
    :param NextMarker: AWS WAF returns a NextMarker value in the response that allows you to list another group of IPSets . For the second and subsequent ListIPSets requests, specify the value of NextMarker from the previous response to get information about another batch of IPSets .

    :type Limit: integer
    :param Limit: Specifies the number of IPSet objects that you want AWS WAF to return for this request. If you have more IPSet objects than the number you specify for Limit , the response includes a NextMarker value that you can use to get another batch of IPSet objects.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextMarker': 'string',
    'IPSets': [
        {
            'IPSetId': 'string',
            'Name': 'string'
        },
    ]
}


Response Structure

(dict) --

NextMarker (string) --
To list more IPSet objects, submit another ListIPSets request, and in the next request use the NextMarker response value as the NextMarker value.

IPSets (list) --
An array of  IPSetSummary objects.

(dict) --

Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


Contains the identifier and the name of the IPSet .

IPSetId (string) --
The IPSetId for an  IPSet . You can use IPSetId in a  GetIPSet request to get detailed information about an  IPSet .

Name (string) --
A friendly name or description of the  IPSet . You can\'t change the name of an IPSet after you create it.











Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException

Examples
The following example returns an array of up to 100 IP match sets.
response = client.list_ip_sets(
    Limit=100,
)

print(response)


Expected Output:
{
    'IPSets': [
        {
            'IPSetId': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
            'Name': 'MyIPSetFriendlyName',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'NextMarker': 'string',
        'IPSets': [
            {
                'IPSetId': 'string',
                'Name': 'string'
            },
        ]
    }
    
    
    :returns: 
    WAFRegional.Client.exceptions.WAFInternalErrorException
    WAFRegional.Client.exceptions.WAFInvalidAccountException
    
    """
    pass

def list_logging_configurations(NextMarker=None, Limit=None):
    """
    Returns an array of  LoggingConfiguration objects.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_logging_configurations(
        NextMarker='string',
        Limit=123
    )
    
    
    :type NextMarker: string
    :param NextMarker: If you specify a value for Limit and you have more LoggingConfigurations than the value of Limit , AWS WAF returns a NextMarker value in the response that allows you to list another group of LoggingConfigurations . For the second and subsequent ListLoggingConfigurations requests, specify the value of NextMarker from the previous response to get information about another batch of ListLoggingConfigurations .

    :type Limit: integer
    :param Limit: Specifies the number of LoggingConfigurations that you want AWS WAF to return for this request. If you have more LoggingConfigurations than the number that you specify for Limit , the response includes a NextMarker value that you can use to get another batch of LoggingConfigurations .

    :rtype: dict

ReturnsResponse Syntax
{
    'LoggingConfigurations': [
        {
            'ResourceArn': 'string',
            'LogDestinationConfigs': [
                'string',
            ],
            'RedactedFields': [
                {
                    'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY'|'SINGLE_QUERY_ARG'|'ALL_QUERY_ARGS',
                    'Data': 'string'
                },
            ]
        },
    ],
    'NextMarker': 'string'
}


Response Structure

(dict) --

LoggingConfigurations (list) --
An array of  LoggingConfiguration objects.

(dict) --

Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


The Amazon Kinesis Data Firehose, RedactedFields information, and the web ACL Amazon Resource Name (ARN).

ResourceArn (string) --
The Amazon Resource Name (ARN) of the web ACL that you want to associate with LogDestinationConfigs .

LogDestinationConfigs (list) --
An array of Amazon Kinesis Data Firehose ARNs.

(string) --


RedactedFields (list) --
The parts of the request that you want redacted from the logs. For example, if you redact the cookie field, the cookie field in the firehose will be xxx .

(dict) --

Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


Specifies where in a web request to look for TargetString .

Type (string) --
The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:

HEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .
METHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .
QUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.
URI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .
BODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .
SINGLE_QUERY_ARG : The parameter in the query string that you will inspect, such as UserName or SalesRegion . The maximum length for SINGLE_QUERY_ARG is 30 characters.
ALL_QUERY_ARGS : Similar to SINGLE_QUERY_ARG , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in TargetString .


Data (string) --
When the value of Type is HEADER , enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer . The name of the header is not case sensitive.
When the value of Type is SINGLE_QUERY_ARG , enter the name of the parameter that you want AWS WAF to search, for example, UserName or SalesRegion . The parameter name is not case sensitive.
If the value of Type is any other value, omit Data .









NextMarker (string) --
If you have more LoggingConfigurations than the number that you specified for Limit in the request, the response includes a NextMarker value. To list more LoggingConfigurations , submit another ListLoggingConfigurations request, and specify the NextMarker value from the response in the NextMarker value in the next request.







Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFInvalidParameterException


    :return: {
        'LoggingConfigurations': [
            {
                'ResourceArn': 'string',
                'LogDestinationConfigs': [
                    'string',
                ],
                'RedactedFields': [
                    {
                        'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY'|'SINGLE_QUERY_ARG'|'ALL_QUERY_ARGS',
                        'Data': 'string'
                    },
                ]
            },
        ],
        'NextMarker': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_rate_based_rules(NextMarker=None, Limit=None):
    """
    Returns an array of  RuleSummary objects.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_rate_based_rules(
        NextMarker='string',
        Limit=123
    )
    
    
    :type NextMarker: string
    :param NextMarker: If you specify a value for Limit and you have more Rules than the value of Limit , AWS WAF returns a NextMarker value in the response that allows you to list another group of Rules . For the second and subsequent ListRateBasedRules requests, specify the value of NextMarker from the previous response to get information about another batch of Rules .

    :type Limit: integer
    :param Limit: Specifies the number of Rules that you want AWS WAF to return for this request. If you have more Rules than the number that you specify for Limit , the response includes a NextMarker value that you can use to get another batch of Rules .

    :rtype: dict

ReturnsResponse Syntax
{
    'NextMarker': 'string',
    'Rules': [
        {
            'RuleId': 'string',
            'Name': 'string'
        },
    ]
}


Response Structure

(dict) --

NextMarker (string) --
If you have more Rules than the number that you specified for Limit in the request, the response includes a NextMarker value. To list more Rules , submit another ListRateBasedRules request, and specify the NextMarker value from the response in the NextMarker value in the next request.

Rules (list) --
An array of  RuleSummary objects.

(dict) --

Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


Contains the identifier and the friendly name or description of the Rule .

RuleId (string) --
A unique identifier for a Rule . You use RuleId to get more information about a Rule (see  GetRule ), update a Rule (see  UpdateRule ), insert a Rule into a WebACL or delete one from a WebACL (see  UpdateWebACL ), or delete a Rule from AWS WAF (see  DeleteRule ).

RuleId is returned by  CreateRule and by  ListRules .


Name (string) --
A friendly name or description of the  Rule . You can\'t change the name of a Rule after you create it.











Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException


    :return: {
        'NextMarker': 'string',
        'Rules': [
            {
                'RuleId': 'string',
                'Name': 'string'
            },
        ]
    }
    
    
    :returns: 
    WAFRegional.Client.exceptions.WAFInternalErrorException
    WAFRegional.Client.exceptions.WAFInvalidAccountException
    
    """
    pass

def list_regex_match_sets(NextMarker=None, Limit=None):
    """
    Returns an array of  RegexMatchSetSummary objects.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_regex_match_sets(
        NextMarker='string',
        Limit=123
    )
    
    
    :type NextMarker: string
    :param NextMarker: If you specify a value for Limit and you have more RegexMatchSet objects than the value of Limit , AWS WAF returns a NextMarker value in the response that allows you to list another group of ByteMatchSets . For the second and subsequent ListRegexMatchSets requests, specify the value of NextMarker from the previous response to get information about another batch of RegexMatchSet objects.

    :type Limit: integer
    :param Limit: Specifies the number of RegexMatchSet objects that you want AWS WAF to return for this request. If you have more RegexMatchSet objects than the number you specify for Limit , the response includes a NextMarker value that you can use to get another batch of RegexMatchSet objects.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextMarker': 'string',
    'RegexMatchSets': [
        {
            'RegexMatchSetId': 'string',
            'Name': 'string'
        },
    ]
}


Response Structure

(dict) --

NextMarker (string) --
If you have more RegexMatchSet objects than the number that you specified for Limit in the request, the response includes a NextMarker value. To list more RegexMatchSet objects, submit another ListRegexMatchSets request, and specify the NextMarker value from the response in the NextMarker value in the next request.

RegexMatchSets (list) --
An array of  RegexMatchSetSummary objects.

(dict) --

Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


Returned by  ListRegexMatchSets . Each RegexMatchSetSummary object includes the Name and RegexMatchSetId for one  RegexMatchSet .

RegexMatchSetId (string) --
The RegexMatchSetId for a RegexMatchSet . You use RegexMatchSetId to get information about a RegexMatchSet , update a RegexMatchSet , remove a RegexMatchSet from a Rule , and delete a RegexMatchSet from AWS WAF.

RegexMatchSetId is returned by  CreateRegexMatchSet and by  ListRegexMatchSets .


Name (string) --
A friendly name or description of the  RegexMatchSet . You can\'t change Name after you create a RegexMatchSet .











Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException


    :return: {
        'NextMarker': 'string',
        'RegexMatchSets': [
            {
                'RegexMatchSetId': 'string',
                'Name': 'string'
            },
        ]
    }
    
    
    :returns: 
    WAFRegional.Client.exceptions.WAFInternalErrorException
    WAFRegional.Client.exceptions.WAFInvalidAccountException
    
    """
    pass

def list_regex_pattern_sets(NextMarker=None, Limit=None):
    """
    Returns an array of  RegexPatternSetSummary objects.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_regex_pattern_sets(
        NextMarker='string',
        Limit=123
    )
    
    
    :type NextMarker: string
    :param NextMarker: If you specify a value for Limit and you have more RegexPatternSet objects than the value of Limit , AWS WAF returns a NextMarker value in the response that allows you to list another group of RegexPatternSet objects. For the second and subsequent ListRegexPatternSets requests, specify the value of NextMarker from the previous response to get information about another batch of RegexPatternSet objects.

    :type Limit: integer
    :param Limit: Specifies the number of RegexPatternSet objects that you want AWS WAF to return for this request. If you have more RegexPatternSet objects than the number you specify for Limit , the response includes a NextMarker value that you can use to get another batch of RegexPatternSet objects.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextMarker': 'string',
    'RegexPatternSets': [
        {
            'RegexPatternSetId': 'string',
            'Name': 'string'
        },
    ]
}


Response Structure

(dict) --

NextMarker (string) --
If you have more RegexPatternSet objects than the number that you specified for Limit in the request, the response includes a NextMarker value. To list more RegexPatternSet objects, submit another ListRegexPatternSets request, and specify the NextMarker value from the response in the NextMarker value in the next request.

RegexPatternSets (list) --
An array of  RegexPatternSetSummary objects.

(dict) --

Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


Returned by  ListRegexPatternSets . Each RegexPatternSetSummary object includes the Name and RegexPatternSetId for one  RegexPatternSet .

RegexPatternSetId (string) --
The RegexPatternSetId for a RegexPatternSet . You use RegexPatternSetId to get information about a RegexPatternSet , update a RegexPatternSet , remove a RegexPatternSet from a RegexMatchSet , and delete a RegexPatternSet from AWS WAF.

RegexPatternSetId is returned by  CreateRegexPatternSet and by  ListRegexPatternSets .


Name (string) --
A friendly name or description of the  RegexPatternSet . You can\'t change Name after you create a RegexPatternSet .











Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException


    :return: {
        'NextMarker': 'string',
        'RegexPatternSets': [
            {
                'RegexPatternSetId': 'string',
                'Name': 'string'
            },
        ]
    }
    
    
    :returns: 
    WAFRegional.Client.exceptions.WAFInternalErrorException
    WAFRegional.Client.exceptions.WAFInvalidAccountException
    
    """
    pass

def list_resources_for_web_acl(WebACLId=None, ResourceType=None):
    """
    Returns an array of resources associated with the specified web ACL.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_resources_for_web_acl(
        WebACLId='string',
        ResourceType='APPLICATION_LOAD_BALANCER'|'API_GATEWAY'
    )
    
    
    :type WebACLId: string
    :param WebACLId: [REQUIRED]\nThe unique identifier (ID) of the web ACL for which to list the associated resources.\n

    :type ResourceType: string
    :param ResourceType: The type of resource to list, either an application load balancer or Amazon API Gateway.

    :rtype: dict

ReturnsResponse Syntax
{
    'ResourceArns': [
        'string',
    ]
}


Response Structure

(dict) --

ResourceArns (list) --
An array of ARNs (Amazon Resource Names) of the resources associated with the specified web ACL. An array with zero elements is returned if there are no resources associated with the web ACL.

(string) --








Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFInvalidParameterException


    :return: {
        'ResourceArns': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_rule_groups(NextMarker=None, Limit=None):
    """
    Returns an array of  RuleGroup objects.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_rule_groups(
        NextMarker='string',
        Limit=123
    )
    
    
    :type NextMarker: string
    :param NextMarker: If you specify a value for Limit and you have more RuleGroups than the value of Limit , AWS WAF returns a NextMarker value in the response that allows you to list another group of RuleGroups . For the second and subsequent ListRuleGroups requests, specify the value of NextMarker from the previous response to get information about another batch of RuleGroups .

    :type Limit: integer
    :param Limit: Specifies the number of RuleGroups that you want AWS WAF to return for this request. If you have more RuleGroups than the number that you specify for Limit , the response includes a NextMarker value that you can use to get another batch of RuleGroups .

    :rtype: dict

ReturnsResponse Syntax
{
    'NextMarker': 'string',
    'RuleGroups': [
        {
            'RuleGroupId': 'string',
            'Name': 'string'
        },
    ]
}


Response Structure

(dict) --

NextMarker (string) --
If you have more RuleGroups than the number that you specified for Limit in the request, the response includes a NextMarker value. To list more RuleGroups , submit another ListRuleGroups request, and specify the NextMarker value from the response in the NextMarker value in the next request.

RuleGroups (list) --
An array of  RuleGroup objects.

(dict) --

Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


Contains the identifier and the friendly name or description of the RuleGroup .

RuleGroupId (string) --
A unique identifier for a RuleGroup . You use RuleGroupId to get more information about a RuleGroup (see  GetRuleGroup ), update a RuleGroup (see  UpdateRuleGroup ), insert a RuleGroup into a WebACL or delete one from a WebACL (see  UpdateWebACL ), or delete a RuleGroup from AWS WAF (see  DeleteRuleGroup ).

RuleGroupId is returned by  CreateRuleGroup and by  ListRuleGroups .


Name (string) --
A friendly name or description of the  RuleGroup . You can\'t change the name of a RuleGroup after you create it.











Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException


    :return: {
        'NextMarker': 'string',
        'RuleGroups': [
            {
                'RuleGroupId': 'string',
                'Name': 'string'
            },
        ]
    }
    
    
    :returns: 
    WAFRegional.Client.exceptions.WAFInternalErrorException
    
    """
    pass

def list_rules(NextMarker=None, Limit=None):
    """
    Returns an array of  RuleSummary objects.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns an array of up to 100 rules.
    Expected Output:
    
    :example: response = client.list_rules(
        NextMarker='string',
        Limit=123
    )
    
    
    :type NextMarker: string
    :param NextMarker: If you specify a value for Limit and you have more Rules than the value of Limit , AWS WAF returns a NextMarker value in the response that allows you to list another group of Rules . For the second and subsequent ListRules requests, specify the value of NextMarker from the previous response to get information about another batch of Rules .

    :type Limit: integer
    :param Limit: Specifies the number of Rules that you want AWS WAF to return for this request. If you have more Rules than the number that you specify for Limit , the response includes a NextMarker value that you can use to get another batch of Rules .

    :rtype: dict

ReturnsResponse Syntax
{
    'NextMarker': 'string',
    'Rules': [
        {
            'RuleId': 'string',
            'Name': 'string'
        },
    ]
}


Response Structure

(dict) --

NextMarker (string) --
If you have more Rules than the number that you specified for Limit in the request, the response includes a NextMarker value. To list more Rules , submit another ListRules request, and specify the NextMarker value from the response in the NextMarker value in the next request.

Rules (list) --
An array of  RuleSummary objects.

(dict) --

Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


Contains the identifier and the friendly name or description of the Rule .

RuleId (string) --
A unique identifier for a Rule . You use RuleId to get more information about a Rule (see  GetRule ), update a Rule (see  UpdateRule ), insert a Rule into a WebACL or delete one from a WebACL (see  UpdateWebACL ), or delete a Rule from AWS WAF (see  DeleteRule ).

RuleId is returned by  CreateRule and by  ListRules .


Name (string) --
A friendly name or description of the  Rule . You can\'t change the name of a Rule after you create it.











Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException

Examples
The following example returns an array of up to 100 rules.
response = client.list_rules(
    Limit=100,
)

print(response)


Expected Output:
{
    'Rules': [
        {
            'Name': 'WAFByteHeaderRule',
            'RuleId': 'WAFRule-1-Example',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'NextMarker': 'string',
        'Rules': [
            {
                'RuleId': 'string',
                'Name': 'string'
            },
        ]
    }
    
    
    :returns: 
    WAFRegional.Client.exceptions.WAFInternalErrorException
    WAFRegional.Client.exceptions.WAFInvalidAccountException
    
    """
    pass

def list_size_constraint_sets(NextMarker=None, Limit=None):
    """
    Returns an array of  SizeConstraintSetSummary objects.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns an array of up to 100 size contraint match sets.
    Expected Output:
    
    :example: response = client.list_size_constraint_sets(
        NextMarker='string',
        Limit=123
    )
    
    
    :type NextMarker: string
    :param NextMarker: If you specify a value for Limit and you have more SizeConstraintSets than the value of Limit , AWS WAF returns a NextMarker value in the response that allows you to list another group of SizeConstraintSets . For the second and subsequent ListSizeConstraintSets requests, specify the value of NextMarker from the previous response to get information about another batch of SizeConstraintSets .

    :type Limit: integer
    :param Limit: Specifies the number of SizeConstraintSet objects that you want AWS WAF to return for this request. If you have more SizeConstraintSets objects than the number you specify for Limit , the response includes a NextMarker value that you can use to get another batch of SizeConstraintSet objects.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextMarker': 'string',
    'SizeConstraintSets': [
        {
            'SizeConstraintSetId': 'string',
            'Name': 'string'
        },
    ]
}


Response Structure

(dict) --

NextMarker (string) --
If you have more SizeConstraintSet objects than the number that you specified for Limit in the request, the response includes a NextMarker value. To list more SizeConstraintSet objects, submit another ListSizeConstraintSets request, and specify the NextMarker value from the response in the NextMarker value in the next request.

SizeConstraintSets (list) --
An array of  SizeConstraintSetSummary objects.

(dict) --

Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


The Id and Name of a SizeConstraintSet .

SizeConstraintSetId (string) --
A unique identifier for a SizeConstraintSet . You use SizeConstraintSetId to get information about a SizeConstraintSet (see  GetSizeConstraintSet ), update a SizeConstraintSet (see  UpdateSizeConstraintSet ), insert a SizeConstraintSet into a Rule or delete one from a Rule (see  UpdateRule ), and delete a SizeConstraintSet from AWS WAF (see  DeleteSizeConstraintSet ).

SizeConstraintSetId is returned by  CreateSizeConstraintSet and by  ListSizeConstraintSets .


Name (string) --
The name of the SizeConstraintSet , if any.











Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException

Examples
The following example returns an array of up to 100 size contraint match sets.
response = client.list_size_constraint_sets(
    Limit=100,
)

print(response)


Expected Output:
{
    'SizeConstraintSets': [
        {
            'Name': 'MySampleSizeConstraintSet',
            'SizeConstraintSetId': 'example1ds3t-46da-4fdb-b8d5-abc321j569j5',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'NextMarker': 'string',
        'SizeConstraintSets': [
            {
                'SizeConstraintSetId': 'string',
                'Name': 'string'
            },
        ]
    }
    
    
    :returns: 
    WAFRegional.Client.exceptions.WAFInternalErrorException
    WAFRegional.Client.exceptions.WAFInvalidAccountException
    
    """
    pass

def list_sql_injection_match_sets(NextMarker=None, Limit=None):
    """
    Returns an array of  SqlInjectionMatchSet objects.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns an array of up to 100 SQL injection match sets.
    Expected Output:
    
    :example: response = client.list_sql_injection_match_sets(
        NextMarker='string',
        Limit=123
    )
    
    
    :type NextMarker: string
    :param NextMarker: If you specify a value for Limit and you have more SqlInjectionMatchSet objects than the value of Limit , AWS WAF returns a NextMarker value in the response that allows you to list another group of SqlInjectionMatchSets . For the second and subsequent ListSqlInjectionMatchSets requests, specify the value of NextMarker from the previous response to get information about another batch of SqlInjectionMatchSets .

    :type Limit: integer
    :param Limit: Specifies the number of SqlInjectionMatchSet objects that you want AWS WAF to return for this request. If you have more SqlInjectionMatchSet objects than the number you specify for Limit , the response includes a NextMarker value that you can use to get another batch of Rules .

    :rtype: dict

ReturnsResponse Syntax
{
    'NextMarker': 'string',
    'SqlInjectionMatchSets': [
        {
            'SqlInjectionMatchSetId': 'string',
            'Name': 'string'
        },
    ]
}


Response Structure

(dict) --
The response to a  ListSqlInjectionMatchSets request.

NextMarker (string) --
If you have more  SqlInjectionMatchSet objects than the number that you specified for Limit in the request, the response includes a NextMarker value. To list more SqlInjectionMatchSet objects, submit another ListSqlInjectionMatchSets request, and specify the NextMarker value from the response in the NextMarker value in the next request.

SqlInjectionMatchSets (list) --
An array of  SqlInjectionMatchSetSummary objects.

(dict) --

Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


The Id and Name of a SqlInjectionMatchSet .

SqlInjectionMatchSetId (string) --
A unique identifier for a SqlInjectionMatchSet . You use SqlInjectionMatchSetId to get information about a SqlInjectionMatchSet (see  GetSqlInjectionMatchSet ), update a SqlInjectionMatchSet (see  UpdateSqlInjectionMatchSet ), insert a SqlInjectionMatchSet into a Rule or delete one from a Rule (see  UpdateRule ), and delete a SqlInjectionMatchSet from AWS WAF (see  DeleteSqlInjectionMatchSet ).

SqlInjectionMatchSetId is returned by  CreateSqlInjectionMatchSet and by  ListSqlInjectionMatchSets .


Name (string) --
The name of the SqlInjectionMatchSet , if any, specified by Id .











Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException

Examples
The following example returns an array of up to 100 SQL injection match sets.
response = client.list_sql_injection_match_sets(
    Limit=100,
)

print(response)


Expected Output:
{
    'SqlInjectionMatchSets': [
        {
            'Name': 'MySQLInjectionMatchSet',
            'SqlInjectionMatchSetId': 'example1ds3t-46da-4fdb-b8d5-abc321j569j5',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'NextMarker': 'string',
        'SqlInjectionMatchSets': [
            {
                'SqlInjectionMatchSetId': 'string',
                'Name': 'string'
            },
        ]
    }
    
    
    :returns: 
    WAFRegional.Client.exceptions.WAFInternalErrorException
    WAFRegional.Client.exceptions.WAFInvalidAccountException
    
    """
    pass

def list_subscribed_rule_groups(NextMarker=None, Limit=None):
    """
    Returns an array of  RuleGroup objects that you are subscribed to.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_subscribed_rule_groups(
        NextMarker='string',
        Limit=123
    )
    
    
    :type NextMarker: string
    :param NextMarker: If you specify a value for Limit and you have more ByteMatchSets subscribed rule groups than the value of Limit , AWS WAF returns a NextMarker value in the response that allows you to list another group of subscribed rule groups. For the second and subsequent ListSubscribedRuleGroupsRequest requests, specify the value of NextMarker from the previous response to get information about another batch of subscribed rule groups.

    :type Limit: integer
    :param Limit: Specifies the number of subscribed rule groups that you want AWS WAF to return for this request. If you have more objects than the number you specify for Limit , the response includes a NextMarker value that you can use to get another batch of objects.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextMarker': 'string',
    'RuleGroups': [
        {
            'RuleGroupId': 'string',
            'Name': 'string',
            'MetricName': 'string'
        },
    ]
}


Response Structure

(dict) --

NextMarker (string) --
If you have more objects than the number that you specified for Limit in the request, the response includes a NextMarker value. To list more objects, submit another ListSubscribedRuleGroups request, and specify the NextMarker value from the response in the NextMarker value in the next request.

RuleGroups (list) --
An array of  RuleGroup objects.

(dict) --

Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


A summary of the rule groups you are subscribed to.

RuleGroupId (string) --
A unique identifier for a RuleGroup .

Name (string) --
A friendly name or description of the RuleGroup . You can\'t change the name of a RuleGroup after you create it.

MetricName (string) --
A friendly name or description for the metrics for this RuleGroup . The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can\'t contain whitespace or metric names reserved for AWS WAF, including "All" and "Default_Action." You can\'t change the name of the metric after you create the RuleGroup .











Exceptions

WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFInternalErrorException


    :return: {
        'NextMarker': 'string',
        'RuleGroups': [
            {
                'RuleGroupId': 'string',
                'Name': 'string',
                'MetricName': 'string'
            },
        ]
    }
    
    
    :returns: 
    WAFRegional.Client.exceptions.WAFNonexistentItemException
    WAFRegional.Client.exceptions.WAFInternalErrorException
    
    """
    pass

def list_tags_for_resource(NextMarker=None, Limit=None, ResourceARN=None):
    """
    Retrieves the tags associated with the specified AWS resource. Tags are key:value pairs that you can use to categorize and manage your resources, for purposes like billing. For example, you might set the tag key to "customer" and the value to the customer name or ID. You can specify one or more tags to add to each AWS resource, up to 50 tags for a resource.
    Tagging is only available through the API, SDKs, and CLI. You can\'t manage or view tags through the AWS WAF Classic console. You can tag the AWS resources that you manage through AWS WAF Classic: web ACLs, rule groups, and rules.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        NextMarker='string',
        Limit=123,
        ResourceARN='string'
    )
    
    
    :type NextMarker: string
    :param NextMarker: 

    :type Limit: integer
    :param Limit: 

    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]

    :rtype: dict

ReturnsResponse Syntax
{
    'NextMarker': 'string',
    'TagInfoForResource': {
        'ResourceARN': 'string',
        'TagList': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

NextMarker (string) --

TagInfoForResource (dict) --

ResourceARN (string) --

TagList (list) --

(dict) --

Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


A tag associated with an AWS resource. Tags are key:value pairs that you can use to categorize and manage your resources, for purposes like billing. For example, you might set the tag key to "customer" and the value to the customer name or ID. You can specify one or more tags to add to each AWS resource, up to 50 tags for a resource.
Tagging is only available through the API, SDKs, and CLI. You can\'t manage or view tags through the AWS WAF Classic console. You can tag the AWS resources that you manage through AWS WAF Classic: web ACLs, rule groups, and rules.

Key (string) --
Value (string) --












Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidParameterException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFBadRequestException
WAFRegional.Client.exceptions.WAFTagOperationException
WAFRegional.Client.exceptions.WAFTagOperationInternalErrorException


    :return: {
        'NextMarker': 'string',
        'TagInfoForResource': {
            'ResourceARN': 'string',
            'TagList': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    Key (string) --
    Value (string) --
    
    """
    pass

def list_web_acls(NextMarker=None, Limit=None):
    """
    Returns an array of  WebACLSummary objects in the response.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns an array of up to 100 web ACLs.
    Expected Output:
    
    :example: response = client.list_web_acls(
        NextMarker='string',
        Limit=123
    )
    
    
    :type NextMarker: string
    :param NextMarker: If you specify a value for Limit and you have more WebACL objects than the number that you specify for Limit , AWS WAF returns a NextMarker value in the response that allows you to list another group of WebACL objects. For the second and subsequent ListWebACLs requests, specify the value of NextMarker from the previous response to get information about another batch of WebACL objects.

    :type Limit: integer
    :param Limit: Specifies the number of WebACL objects that you want AWS WAF to return for this request. If you have more WebACL objects than the number that you specify for Limit , the response includes a NextMarker value that you can use to get another batch of WebACL objects.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextMarker': 'string',
    'WebACLs': [
        {
            'WebACLId': 'string',
            'Name': 'string'
        },
    ]
}


Response Structure

(dict) --

NextMarker (string) --
If you have more WebACL objects than the number that you specified for Limit in the request, the response includes a NextMarker value. To list more WebACL objects, submit another ListWebACLs request, and specify the NextMarker value from the response in the NextMarker value in the next request.

WebACLs (list) --
An array of  WebACLSummary objects.

(dict) --

Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


Contains the identifier and the name or description of the  WebACL .

WebACLId (string) --
A unique identifier for a WebACL . You use WebACLId to get information about a WebACL (see  GetWebACL ), update a WebACL (see  UpdateWebACL ), and delete a WebACL from AWS WAF (see  DeleteWebACL ).

WebACLId is returned by  CreateWebACL and by  ListWebACLs .


Name (string) --
A friendly name or description of the  WebACL . You can\'t change the name of a WebACL after you create it.











Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException

Examples
The following example returns an array of up to 100 web ACLs.
response = client.list_web_acls(
    Limit=100,
)

print(response)


Expected Output:
{
    'WebACLs': [
        {
            'Name': 'WebACLexample',
            'WebACLId': 'webacl-1472061481310',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'NextMarker': 'string',
        'WebACLs': [
            {
                'WebACLId': 'string',
                'Name': 'string'
            },
        ]
    }
    
    
    :returns: 
    WAFRegional.Client.exceptions.WAFInternalErrorException
    WAFRegional.Client.exceptions.WAFInvalidAccountException
    
    """
    pass

def list_xss_match_sets(NextMarker=None, Limit=None):
    """
    Returns an array of  XssMatchSet objects.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns an array of up to 100 XSS match sets.
    Expected Output:
    
    :example: response = client.list_xss_match_sets(
        NextMarker='string',
        Limit=123
    )
    
    
    :type NextMarker: string
    :param NextMarker: If you specify a value for Limit and you have more XssMatchSet objects than the value of Limit , AWS WAF returns a NextMarker value in the response that allows you to list another group of XssMatchSets . For the second and subsequent ListXssMatchSets requests, specify the value of NextMarker from the previous response to get information about another batch of XssMatchSets .

    :type Limit: integer
    :param Limit: Specifies the number of XssMatchSet objects that you want AWS WAF to return for this request. If you have more XssMatchSet objects than the number you specify for Limit , the response includes a NextMarker value that you can use to get another batch of Rules .

    :rtype: dict

ReturnsResponse Syntax
{
    'NextMarker': 'string',
    'XssMatchSets': [
        {
            'XssMatchSetId': 'string',
            'Name': 'string'
        },
    ]
}


Response Structure

(dict) --
The response to a  ListXssMatchSets request.

NextMarker (string) --
If you have more  XssMatchSet objects than the number that you specified for Limit in the request, the response includes a NextMarker value. To list more XssMatchSet objects, submit another ListXssMatchSets request, and specify the NextMarker value from the response in the NextMarker value in the next request.

XssMatchSets (list) --
An array of  XssMatchSetSummary objects.

(dict) --

Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


The Id and Name of an XssMatchSet .

XssMatchSetId (string) --
A unique identifier for an XssMatchSet . You use XssMatchSetId to get information about a XssMatchSet (see  GetXssMatchSet ), update an XssMatchSet (see  UpdateXssMatchSet ), insert an XssMatchSet into a Rule or delete one from a Rule (see  UpdateRule ), and delete an XssMatchSet from AWS WAF (see  DeleteXssMatchSet ).

XssMatchSetId is returned by  CreateXssMatchSet and by  ListXssMatchSets .


Name (string) --
The name of the XssMatchSet , if any, specified by Id .











Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException

Examples
The following example returns an array of up to 100 XSS match sets.
response = client.list_xss_match_sets(
    Limit=100,
)

print(response)


Expected Output:
{
    'XssMatchSets': [
        {
            'Name': 'MySampleXssMatchSet',
            'XssMatchSetId': 'example1ds3t-46da-4fdb-b8d5-abc321j569j5',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'NextMarker': 'string',
        'XssMatchSets': [
            {
                'XssMatchSetId': 'string',
                'Name': 'string'
            },
        ]
    }
    
    
    :returns: 
    WAFRegional.Client.exceptions.WAFInternalErrorException
    WAFRegional.Client.exceptions.WAFInvalidAccountException
    
    """
    pass

def put_logging_configuration(LoggingConfiguration=None):
    """
    Associates a  LoggingConfiguration with a specified web ACL.
    You can access information about all traffic that AWS WAF inspects using the following steps:
    When you successfully enable logging using a PutLoggingConfiguration request, AWS WAF will create a service linked role with the necessary permissions to write logs to the Amazon Kinesis Data Firehose. For more information, see Logging Web ACL Traffic Information in the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_logging_configuration(
        LoggingConfiguration={
            'ResourceArn': 'string',
            'LogDestinationConfigs': [
                'string',
            ],
            'RedactedFields': [
                {
                    'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY'|'SINGLE_QUERY_ARG'|'ALL_QUERY_ARGS',
                    'Data': 'string'
                },
            ]
        }
    )
    
    
    :type LoggingConfiguration: dict
    :param LoggingConfiguration: [REQUIRED]\nThe Amazon Kinesis Data Firehose that contains the inspected traffic information, the redacted fields details, and the Amazon Resource Name (ARN) of the web ACL to monitor.\n\nNote\nWhen specifying Type in RedactedFields , you must use one of the following values: URI , QUERY_STRING , HEADER , or METHOD .\n\n\nResourceArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the web ACL that you want to associate with LogDestinationConfigs .\n\nLogDestinationConfigs (list) -- [REQUIRED]An array of Amazon Kinesis Data Firehose ARNs.\n\n(string) --\n\n\nRedactedFields (list) --The parts of the request that you want redacted from the logs. For example, if you redact the cookie field, the cookie field in the firehose will be xxx .\n\n(dict) --\nNote\nThis is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.\n\nFor the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.\n\nSpecifies where in a web request to look for TargetString .\n\nType (string) -- [REQUIRED]The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:\n\nHEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .\nMETHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .\nQUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.\nURI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .\nBODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see CreateSizeConstraintSet .\nSINGLE_QUERY_ARG : The parameter in the query string that you will inspect, such as UserName or SalesRegion . The maximum length for SINGLE_QUERY_ARG is 30 characters.\nALL_QUERY_ARGS : Similar to SINGLE_QUERY_ARG , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in TargetString .\n\n\nData (string) --When the value of Type is HEADER , enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer . The name of the header is not case sensitive.\nWhen the value of Type is SINGLE_QUERY_ARG , enter the name of the parameter that you want AWS WAF to search, for example, UserName or SalesRegion . The parameter name is not case sensitive.\nIf the value of Type is any other value, omit Data .\n\n\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'LoggingConfiguration': {
        'ResourceArn': 'string',
        'LogDestinationConfigs': [
            'string',
        ],
        'RedactedFields': [
            {
                'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY'|'SINGLE_QUERY_ARG'|'ALL_QUERY_ARGS',
                'Data': 'string'
            },
        ]
    }
}


Response Structure

(dict) --
LoggingConfiguration (dict) --The  LoggingConfiguration that you submitted in the request.

ResourceArn (string) --The Amazon Resource Name (ARN) of the web ACL that you want to associate with LogDestinationConfigs .

LogDestinationConfigs (list) --An array of Amazon Kinesis Data Firehose ARNs.

(string) --


RedactedFields (list) --The parts of the request that you want redacted from the logs. For example, if you redact the cookie field, the cookie field in the firehose will be xxx .

(dict) --
Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Specifies where in a web request to look for TargetString .

Type (string) --The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:

HEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .
METHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .
QUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.
URI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .
BODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .
SINGLE_QUERY_ARG : The parameter in the query string that you will inspect, such as UserName or SalesRegion . The maximum length for SINGLE_QUERY_ARG is 30 characters.
ALL_QUERY_ARGS : Similar to SINGLE_QUERY_ARG , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in TargetString .


Data (string) --When the value of Type is HEADER , enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer . The name of the header is not case sensitive.
When the value of Type is SINGLE_QUERY_ARG , enter the name of the parameter that you want AWS WAF to search, for example, UserName or SalesRegion . The parameter name is not case sensitive.
If the value of Type is any other value, omit Data .












Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFServiceLinkedRoleErrorException


    :return: {
        'LoggingConfiguration': {
            'ResourceArn': 'string',
            'LogDestinationConfigs': [
                'string',
            ],
            'RedactedFields': [
                {
                    'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY'|'SINGLE_QUERY_ARG'|'ALL_QUERY_ARGS',
                    'Data': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    Associate that firehose to your web ACL using a PutLoggingConfiguration request.
    
    """
    pass

def put_permission_policy(ResourceArn=None, Policy=None):
    """
    Attaches an IAM policy to the specified resource. The only supported use for this action is to share a RuleGroup across accounts.
    The PutPermissionPolicy is subject to the following restrictions:
    For more information, see IAM Policies .
    An example of a valid policy parameter is shown in the Examples section below.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_permission_policy(
        ResourceArn='string',
        Policy='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the RuleGroup to which you want to attach the policy.\n

    :type Policy: string
    :param Policy: [REQUIRED]\nThe policy to attach to the specified RuleGroup.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFInvalidPermissionPolicyException


    :return: {}
    
    
    :returns: 
    ResourceArn (string) -- [REQUIRED]
    The Amazon Resource Name (ARN) of the RuleGroup to which you want to attach the policy.
    
    Policy (string) -- [REQUIRED]
    The policy to attach to the specified RuleGroup.
    
    
    """
    pass

def tag_resource(ResourceARN=None, Tags=None):
    """
    Associates tags with the specified AWS resource. Tags are key:value pairs that you can use to categorize and manage your resources, for purposes like billing. For example, you might set the tag key to "customer" and the value to the customer name or ID. You can specify one or more tags to add to each AWS resource, up to 50 tags for a resource.
    Tagging is only available through the API, SDKs, and CLI. You can\'t manage or view tags through the AWS WAF Classic console. You can use this action to tag the AWS resources that you manage through AWS WAF Classic: web ACLs, rule groups, and rules.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceARN='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]

    :type Tags: list
    :param Tags: [REQUIRED]\n\n(dict) --\nNote\nThis is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.\n\nFor the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.\n\nA tag associated with an AWS resource. Tags are key:value pairs that you can use to categorize and manage your resources, for purposes like billing. For example, you might set the tag key to 'customer' and the value to the customer name or ID. You can specify one or more tags to add to each AWS resource, up to 50 tags for a resource.\nTagging is only available through the API, SDKs, and CLI. You can\'t manage or view tags through the AWS WAF Classic console. You can tag the AWS resources that you manage through AWS WAF Classic: web ACLs, rule groups, and rules.\n\nKey (string) -- [REQUIRED]\nValue (string) -- [REQUIRED]\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidParameterException
WAFRegional.Client.exceptions.WAFLimitsExceededException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFBadRequestException
WAFRegional.Client.exceptions.WAFTagOperationException
WAFRegional.Client.exceptions.WAFTagOperationInternalErrorException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceARN=None, TagKeys=None):
    """
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceARN='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidParameterException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFBadRequestException
WAFRegional.Client.exceptions.WAFTagOperationException
WAFRegional.Client.exceptions.WAFTagOperationInternalErrorException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_byte_match_set(ByteMatchSetId=None, ChangeToken=None, Updates=None):
    """
    Inserts or deletes  ByteMatchTuple objects (filters) in a  ByteMatchSet . For each ByteMatchTuple object, you specify the following values:
    For example, you can add a ByteMatchSetUpdate object that matches web requests in which User-Agent headers contain the string BadBot . You can then configure AWS WAF to block those requests.
    To create and configure a ByteMatchSet , perform the following steps:
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example deletes a ByteMatchTuple object (filters) in an byte match set with the ID exampleIDs3t-46da-4fdb-b8d5-abc321j569j5.
    Expected Output:
    
    :example: response = client.update_byte_match_set(
        ByteMatchSetId='string',
        ChangeToken='string',
        Updates=[
            {
                'Action': 'INSERT'|'DELETE',
                'ByteMatchTuple': {
                    'FieldToMatch': {
                        'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY'|'SINGLE_QUERY_ARG'|'ALL_QUERY_ARGS',
                        'Data': 'string'
                    },
                    'TargetString': b'bytes',
                    'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE',
                    'PositionalConstraint': 'EXACTLY'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CONTAINS_WORD'
                }
            },
        ]
    )
    
    
    :type ByteMatchSetId: string
    :param ByteMatchSetId: [REQUIRED]\nThe ByteMatchSetId of the ByteMatchSet that you want to update. ByteMatchSetId is returned by CreateByteMatchSet and by ListByteMatchSets .\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :type Updates: list
    :param Updates: [REQUIRED]\nAn array of ByteMatchSetUpdate objects that you want to insert into or delete from a ByteMatchSet . For more information, see the applicable data types:\n\nByteMatchSetUpdate : Contains Action and ByteMatchTuple\nByteMatchTuple : Contains FieldToMatch , PositionalConstraint , TargetString , and TextTransformation\nFieldToMatch : Contains Data and Type\n\n\n(dict) --\nNote\nThis is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.\n\nFor the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.\n\nIn an UpdateByteMatchSet request, ByteMatchSetUpdate specifies whether to insert or delete a ByteMatchTuple and includes the settings for the ByteMatchTuple .\n\nAction (string) -- [REQUIRED]Specifies whether to insert or delete a ByteMatchTuple .\n\nByteMatchTuple (dict) -- [REQUIRED]Information about the part of a web request that you want AWS WAF to inspect and the value that you want AWS WAF to search for. If you specify DELETE for the value of Action , the ByteMatchTuple values must exactly match the values in the ByteMatchTuple that you want to delete from the ByteMatchSet .\n\nFieldToMatch (dict) -- [REQUIRED]The part of a web request that you want AWS WAF to search, such as a specified header or a query string. For more information, see FieldToMatch .\n\nType (string) -- [REQUIRED]The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:\n\nHEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .\nMETHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .\nQUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.\nURI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .\nBODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see CreateSizeConstraintSet .\nSINGLE_QUERY_ARG : The parameter in the query string that you will inspect, such as UserName or SalesRegion . The maximum length for SINGLE_QUERY_ARG is 30 characters.\nALL_QUERY_ARGS : Similar to SINGLE_QUERY_ARG , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in TargetString .\n\n\nData (string) --When the value of Type is HEADER , enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer . The name of the header is not case sensitive.\nWhen the value of Type is SINGLE_QUERY_ARG , enter the name of the parameter that you want AWS WAF to search, for example, UserName or SalesRegion . The parameter name is not case sensitive.\nIf the value of Type is any other value, omit Data .\n\n\n\nTargetString (bytes) -- [REQUIRED]The value that you want AWS WAF to search for. AWS WAF searches for the specified string in the part of web requests that you specified in FieldToMatch . The maximum length of the value is 50 bytes.\nValid values depend on the values that you specified for FieldToMatch :\n\nHEADER : The value that you want AWS WAF to search for in the request header that you specified in FieldToMatch , for example, the value of the User-Agent or Referer header.\nMETHOD : The HTTP method, which indicates the type of operation specified in the request. CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .\nQUERY_STRING : The value that you want AWS WAF to search for in the query string, which is the part of a URL that appears after a ? character.\nURI : The value that you want AWS WAF to search for in the part of a URL that identifies a resource, for example, /images/daily-ad.jpg .\nBODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see CreateSizeConstraintSet .\nSINGLE_QUERY_ARG : The parameter in the query string that you will inspect, such as UserName or SalesRegion . The maximum length for SINGLE_QUERY_ARG is 30 characters.\nALL_QUERY_ARGS : Similar to SINGLE_QUERY_ARG , but instead of inspecting a single parameter, AWS WAF inspects all parameters within the query string for the value or regex pattern that you specify in TargetString .\n\nIf TargetString includes alphabetic characters A-Z and a-z, note that the value is case sensitive.\n\nIf you\'re using the AWS WAF API\nSpecify a base64-encoded version of the value. The maximum length of the value before you base64-encode it is 50 bytes.\nFor example, suppose the value of Type is HEADER and the value of Data is User-Agent . If you want to search the User-Agent header for the value BadBot , you base64-encode BadBot using MIME base64-encoding and include the resulting value, QmFkQm90 , in the value of TargetString .\n\nIf you\'re using the AWS CLI or one of the AWS SDKs\nThe value that you want AWS WAF to search for. The SDK automatically base64 encodes the value.\n\nTextTransformation (string) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on FieldToMatch before inspecting it for a match.\nYou can only specify a single type of TextTransformation.\n\nCMD_LINE\nWhen you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:\n\nDelete the following characters: ' \' ^\nDelete spaces before the following characters: / (\nReplace the following characters with a space: , ;\nReplace multiple spaces with one space\nConvert uppercase letters (A-Z) to lowercase (a-z)\n\n\nCOMPRESS_WHITE_SPACE\nUse this option to replace the following characters with a space character (decimal 32):\n\nf, formfeed, decimal 12\nt, tab, decimal 9\nn, newline, decimal 10\nr, carriage return, decimal 13\nv, vertical tab, decimal 11\nnon-breaking space, decimal 160\n\n\nCOMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE\n\nUse this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:\n\nReplaces (ampersand)quot; with '\nReplaces (ampersand)nbsp; with a non-breaking space, decimal 160\nReplaces (ampersand)lt; with a 'less than' symbol\nReplaces (ampersand)gt; with >\nReplaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters\nReplaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters\n\n\nLOWERCASE\nUse this option to convert uppercase letters (A-Z) to lowercase (a-z).\n\nURL_DECODE\nUse this option to decode a URL-encoded value.\n\nNONE\nSpecify NONE if you don\'t want to perform any text transformations.\n\nPositionalConstraint (string) -- [REQUIRED]Within the portion of a web request that you want to search (for example, in the query string, if any), specify where you want AWS WAF to search. Valid values include the following:\n\nCONTAINS\nThe specified part of the web request must include the value of TargetString , but the location doesn\'t matter.\n\nCONTAINS_WORD\nThe specified part of the web request must include the value of TargetString , and TargetString must contain only alphanumeric characters or underscore (A-Z, a-z, 0-9, or _). In addition, TargetString must be a word, which means one of the following:\n\nTargetString exactly matches the value of the specified part of the web request, such as the value of a header.\nTargetString is at the beginning of the specified part of the web request and is followed by a character other than an alphanumeric character or underscore (_), for example, BadBot; .\nTargetString is at the end of the specified part of the web request and is preceded by a character other than an alphanumeric character or underscore (_), for example, ;BadBot .\nTargetString is in the middle of the specified part of the web request and is preceded and followed by characters other than alphanumeric characters or underscore (_), for example, -BadBot; .\n\n\nEXACTLY\nThe value of the specified part of the web request must exactly match the value of TargetString .\n\nSTARTS_WITH\nThe value of TargetString must appear at the beginning of the specified part of the web request.\n\nENDS_WITH\nThe value of TargetString must appear at the end of the specified part of the web request.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChangeToken': 'string'
}


Response Structure

(dict) --

ChangeToken (string) --
The ChangeToken that you used to submit the UpdateByteMatchSet request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFInvalidOperationException
WAFRegional.Client.exceptions.WAFInvalidParameterException
WAFRegional.Client.exceptions.WAFNonexistentContainerException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFLimitsExceededException

Examples
The following example deletes a ByteMatchTuple object (filters) in an byte match set with the ID exampleIDs3t-46da-4fdb-b8d5-abc321j569j5.
response = client.update_byte_match_set(
    ByteMatchSetId='exampleIDs3t-46da-4fdb-b8d5-abc321j569j5',
    ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    Updates=[
        {
            'Action': 'DELETE',
            'ByteMatchTuple': {
                'FieldToMatch': {
                    'Data': 'referer',
                    'Type': 'HEADER',
                },
                'PositionalConstraint': 'CONTAINS',
                'TargetString': 'badrefer1',
                'TextTransformation': 'NONE',
            },
        },
    ],
)

print(response)


Expected Output:
{
    'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    Create a ByteMatchSet. For more information, see  CreateByteMatchSet .
    Use  GetChangeToken to get the change token that you provide in the ChangeToken parameter of an UpdateByteMatchSet request.
    Submit an UpdateByteMatchSet request to specify the part of the request that you want AWS WAF to inspect (for example, the header or the URI) and the value that you want AWS WAF to watch for.
    
    """
    pass

def update_geo_match_set(GeoMatchSetId=None, ChangeToken=None, Updates=None):
    """
    Inserts or deletes  GeoMatchConstraint objects in an GeoMatchSet . For each GeoMatchConstraint object, you specify the following values:
    To create and configure an GeoMatchSet , perform the following steps:
    When you update an GeoMatchSet , you specify the country that you want to add and/or the country that you want to delete. If you want to change a country, you delete the existing country and add the new one.
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_geo_match_set(
        GeoMatchSetId='string',
        ChangeToken='string',
        Updates=[
            {
                'Action': 'INSERT'|'DELETE',
                'GeoMatchConstraint': {
                    'Type': 'Country',
                    'Value': 'AF'|'AX'|'AL'|'DZ'|'AS'|'AD'|'AO'|'AI'|'AQ'|'AG'|'AR'|'AM'|'AW'|'AU'|'AT'|'AZ'|'BS'|'BH'|'BD'|'BB'|'BY'|'BE'|'BZ'|'BJ'|'BM'|'BT'|'BO'|'BQ'|'BA'|'BW'|'BV'|'BR'|'IO'|'BN'|'BG'|'BF'|'BI'|'KH'|'CM'|'CA'|'CV'|'KY'|'CF'|'TD'|'CL'|'CN'|'CX'|'CC'|'CO'|'KM'|'CG'|'CD'|'CK'|'CR'|'CI'|'HR'|'CU'|'CW'|'CY'|'CZ'|'DK'|'DJ'|'DM'|'DO'|'EC'|'EG'|'SV'|'GQ'|'ER'|'EE'|'ET'|'FK'|'FO'|'FJ'|'FI'|'FR'|'GF'|'PF'|'TF'|'GA'|'GM'|'GE'|'DE'|'GH'|'GI'|'GR'|'GL'|'GD'|'GP'|'GU'|'GT'|'GG'|'GN'|'GW'|'GY'|'HT'|'HM'|'VA'|'HN'|'HK'|'HU'|'IS'|'IN'|'ID'|'IR'|'IQ'|'IE'|'IM'|'IL'|'IT'|'JM'|'JP'|'JE'|'JO'|'KZ'|'KE'|'KI'|'KP'|'KR'|'KW'|'KG'|'LA'|'LV'|'LB'|'LS'|'LR'|'LY'|'LI'|'LT'|'LU'|'MO'|'MK'|'MG'|'MW'|'MY'|'MV'|'ML'|'MT'|'MH'|'MQ'|'MR'|'MU'|'YT'|'MX'|'FM'|'MD'|'MC'|'MN'|'ME'|'MS'|'MA'|'MZ'|'MM'|'NA'|'NR'|'NP'|'NL'|'NC'|'NZ'|'NI'|'NE'|'NG'|'NU'|'NF'|'MP'|'NO'|'OM'|'PK'|'PW'|'PS'|'PA'|'PG'|'PY'|'PE'|'PH'|'PN'|'PL'|'PT'|'PR'|'QA'|'RE'|'RO'|'RU'|'RW'|'BL'|'SH'|'KN'|'LC'|'MF'|'PM'|'VC'|'WS'|'SM'|'ST'|'SA'|'SN'|'RS'|'SC'|'SL'|'SG'|'SX'|'SK'|'SI'|'SB'|'SO'|'ZA'|'GS'|'SS'|'ES'|'LK'|'SD'|'SR'|'SJ'|'SZ'|'SE'|'CH'|'SY'|'TW'|'TJ'|'TZ'|'TH'|'TL'|'TG'|'TK'|'TO'|'TT'|'TN'|'TR'|'TM'|'TC'|'TV'|'UG'|'UA'|'AE'|'GB'|'US'|'UM'|'UY'|'UZ'|'VU'|'VE'|'VN'|'VG'|'VI'|'WF'|'EH'|'YE'|'ZM'|'ZW'
                }
            },
        ]
    )
    
    
    :type GeoMatchSetId: string
    :param GeoMatchSetId: [REQUIRED]\nThe GeoMatchSetId of the GeoMatchSet that you want to update. GeoMatchSetId is returned by CreateGeoMatchSet and by ListGeoMatchSets .\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :type Updates: list
    :param Updates: [REQUIRED]\nAn array of GeoMatchSetUpdate objects that you want to insert into or delete from an GeoMatchSet . For more information, see the applicable data types:\n\nGeoMatchSetUpdate : Contains Action and GeoMatchConstraint\nGeoMatchConstraint : Contains Type and Value  You can have only one Type and Value per GeoMatchConstraint . To add multiple countries, include multiple GeoMatchSetUpdate objects in your request.\n\n\n(dict) --\nNote\nThis is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.\n\nFor the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.\n\nSpecifies the type of update to perform to an GeoMatchSet with UpdateGeoMatchSet .\n\nAction (string) -- [REQUIRED]Specifies whether to insert or delete a country with UpdateGeoMatchSet .\n\nGeoMatchConstraint (dict) -- [REQUIRED]The country from which web requests originate that you want AWS WAF to search for.\n\nType (string) -- [REQUIRED]The type of geographical area you want AWS WAF to search for. Currently Country is the only valid value.\n\nValue (string) -- [REQUIRED]The country that you want AWS WAF to search for.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChangeToken': 'string'
}


Response Structure

(dict) --

ChangeToken (string) --
The ChangeToken that you used to submit the UpdateGeoMatchSet request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFInvalidOperationException
WAFRegional.Client.exceptions.WAFInvalidParameterException
WAFRegional.Client.exceptions.WAFNonexistentContainerException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFReferencedItemException
WAFRegional.Client.exceptions.WAFLimitsExceededException


    :return: {
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    Submit a  CreateGeoMatchSet request.
    Use  GetChangeToken to get the change token that you provide in the ChangeToken parameter of an  UpdateGeoMatchSet request.
    Submit an UpdateGeoMatchSet request to specify the country that you want AWS WAF to watch for.
    
    """
    pass

def update_ip_set(IPSetId=None, ChangeToken=None, Updates=None):
    """
    Inserts or deletes  IPSetDescriptor objects in an IPSet . For each IPSetDescriptor object, you specify the following values:
    AWS WAF supports IPv4 address ranges: /8 and any range between /16 through /32. AWS WAF supports IPv6 address ranges: /24, /32, /48, /56, /64, and /128. For more information about CIDR notation, see the Wikipedia entry Classless Inter-Domain Routing .
    IPv6 addresses can be represented using any of the following formats:
    You use an IPSet to specify which web requests you want to allow or block based on the IP addresses that the requests originated from. For example, if you\'re receiving a lot of requests from one or a small number of IP addresses and you want to block the requests, you can create an IPSet that specifies those IP addresses, and then configure AWS WAF to block the requests.
    To create and configure an IPSet , perform the following steps:
    When you update an IPSet , you specify the IP addresses that you want to add and/or the IP addresses that you want to delete. If you want to change an IP address, you delete the existing IP address and add the new one.
    You can insert a maximum of 1000 addresses in a single request.
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example deletes an IPSetDescriptor object in an IP match set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    Expected Output:
    
    :example: response = client.update_ip_set(
        IPSetId='string',
        ChangeToken='string',
        Updates=[
            {
                'Action': 'INSERT'|'DELETE',
                'IPSetDescriptor': {
                    'Type': 'IPV4'|'IPV6',
                    'Value': 'string'
                }
            },
        ]
    )
    
    
    :type IPSetId: string
    :param IPSetId: [REQUIRED]\nThe IPSetId of the IPSet that you want to update. IPSetId is returned by CreateIPSet and by ListIPSets .\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :type Updates: list
    :param Updates: [REQUIRED]\nAn array of IPSetUpdate objects that you want to insert into or delete from an IPSet . For more information, see the applicable data types:\n\nIPSetUpdate : Contains Action and IPSetDescriptor\nIPSetDescriptor : Contains Type and Value\n\nYou can insert a maximum of 1000 addresses in a single request.\n\n(dict) --\nNote\nThis is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.\n\nFor the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.\n\nSpecifies the type of update to perform to an IPSet with UpdateIPSet .\n\nAction (string) -- [REQUIRED]Specifies whether to insert or delete an IP address with UpdateIPSet .\n\nIPSetDescriptor (dict) -- [REQUIRED]The IP address type (IPV4 or IPV6 ) and the IP address range (in CIDR notation) that web requests originate from.\n\nType (string) -- [REQUIRED]Specify IPV4 or IPV6 .\n\nValue (string) -- [REQUIRED]Specify an IPv4 address by using CIDR notation. For example:\n\nTo configure AWS WAF to allow, block, or count requests that originated from the IP address 192.0.2.44, specify 192.0.2.44/32 .\nTo configure AWS WAF to allow, block, or count requests that originated from IP addresses from 192.0.2.0 to 192.0.2.255, specify 192.0.2.0/24 .\n\nFor more information about CIDR notation, see the Wikipedia entry Classless Inter-Domain Routing .\nSpecify an IPv6 address by using CIDR notation. For example:\n\nTo configure AWS WAF to allow, block, or count requests that originated from the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify 1111:0000:0000:0000:0000:0000:0000:0111/128 .\nTo configure AWS WAF to allow, block, or count requests that originated from IP addresses 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify 1111:0000:0000:0000:0000:0000:0000:0000/64 .\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChangeToken': 'string'
}


Response Structure

(dict) --

ChangeToken (string) --
The ChangeToken that you used to submit the UpdateIPSet request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFInvalidOperationException
WAFRegional.Client.exceptions.WAFInvalidParameterException
WAFRegional.Client.exceptions.WAFNonexistentContainerException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFReferencedItemException
WAFRegional.Client.exceptions.WAFLimitsExceededException

Examples
The following example deletes an IPSetDescriptor object in an IP match set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
response = client.update_ip_set(
    ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    IPSetId='example1ds3t-46da-4fdb-b8d5-abc321j569j5',
    Updates=[
        {
            'Action': 'DELETE',
            'IPSetDescriptor': {
                'Type': 'IPV4',
                'Value': '192.0.2.44/32',
            },
        },
    ],
)

print(response)


Expected Output:
{
    'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    1111:0000:0000:0000:0000:0000:0000:0111/128
    1111:0:0:0:0:0:0:0111/128
    1111::0111/128
    1111::111/128
    
    """
    pass

def update_rate_based_rule(RuleId=None, ChangeToken=None, Updates=None, RateLimit=None):
    """
    Inserts or deletes  Predicate objects in a rule and updates the RateLimit in the rule.
    Each Predicate object identifies a predicate, such as a  ByteMatchSet or an  IPSet , that specifies the web requests that you want to block or count. The RateLimit specifies the number of requests every five minutes that triggers the rule.
    If you add more than one predicate to a RateBasedRule , a request must match all the predicates and exceed the RateLimit to be counted or blocked. For example, suppose you add the following to a RateBasedRule :
    Further, you specify a RateLimit of 1,000.
    You then add the RateBasedRule to a WebACL and specify that you want to block requests that satisfy the rule. For a request to be blocked, it must come from the IP address 192.0.2.44 and the User-Agent header in the request must contain the value BadBot . Further, requests that match these two conditions much be received at a rate of more than 1,000 every five minutes. If the rate drops below this limit, AWS WAF no longer blocks the requests.
    As a second example, suppose you want to limit requests to a particular page on your site. To do this, you could add the following to a RateBasedRule :
    Further, you specify a RateLimit of 1,000.
    By adding this RateBasedRule to a WebACL , you could limit requests to your login page without affecting the rest of your site.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_rate_based_rule(
        RuleId='string',
        ChangeToken='string',
        Updates=[
            {
                'Action': 'INSERT'|'DELETE',
                'Predicate': {
                    'Negated': True|False,
                    'Type': 'IPMatch'|'ByteMatch'|'SqlInjectionMatch'|'GeoMatch'|'SizeConstraint'|'XssMatch'|'RegexMatch',
                    'DataId': 'string'
                }
            },
        ],
        RateLimit=123
    )
    
    
    :type RuleId: string
    :param RuleId: [REQUIRED]\nThe RuleId of the RateBasedRule that you want to update. RuleId is returned by CreateRateBasedRule and by ListRateBasedRules .\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :type Updates: list
    :param Updates: [REQUIRED]\nAn array of RuleUpdate objects that you want to insert into or delete from a RateBasedRule .\n\n(dict) --\nNote\nThis is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.\n\nFor the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.\n\nSpecifies a Predicate (such as an IPSet ) and indicates whether you want to add it to a Rule or delete it from a Rule .\n\nAction (string) -- [REQUIRED]Specify INSERT to add a Predicate to a Rule . Use DELETE to remove a Predicate from a Rule .\n\nPredicate (dict) -- [REQUIRED]The ID of the Predicate (such as an IPSet ) that you want to add to a Rule .\n\nNegated (boolean) -- [REQUIRED]Set Negated to False if you want AWS WAF to allow, block, or count requests based on the settings in the specified ByteMatchSet , IPSet , SqlInjectionMatchSet , XssMatchSet , RegexMatchSet , GeoMatchSet , or SizeConstraintSet . For example, if an IPSet includes the IP address 192.0.2.44 , AWS WAF will allow or block requests based on that IP address.\nSet Negated to True if you want AWS WAF to allow or block a request based on the negation of the settings in the ByteMatchSet , IPSet , SqlInjectionMatchSet , XssMatchSet , RegexMatchSet , GeoMatchSet , or SizeConstraintSet . For example, if an IPSet includes the IP address 192.0.2.44 , AWS WAF will allow, block, or count requests based on all IP addresses except 192.0.2.44 .\n\nType (string) -- [REQUIRED]The type of predicate in a Rule , such as ByteMatch or IPSet .\n\nDataId (string) -- [REQUIRED]A unique identifier for a predicate in a Rule , such as ByteMatchSetId or IPSetId . The ID is returned by the corresponding Create or List command.\n\n\n\n\n\n\n

    :type RateLimit: integer
    :param RateLimit: [REQUIRED]\nThe maximum number of requests, which have an identical value in the field specified by the RateKey , allowed in a five-minute period. If the number of requests exceeds the RateLimit and the other predicates specified in the rule are also met, AWS WAF triggers the action that is specified for this rule.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChangeToken': 'string'
}


Response Structure

(dict) --

ChangeToken (string) --
The ChangeToken that you used to submit the UpdateRateBasedRule request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFInvalidOperationException
WAFRegional.Client.exceptions.WAFInvalidParameterException
WAFRegional.Client.exceptions.WAFNonexistentContainerException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFReferencedItemException
WAFRegional.Client.exceptions.WAFLimitsExceededException


    :return: {
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    A ByteMatchSet with FieldToMatch of URI
    A PositionalConstraint of STARTS_WITH
    A TargetString of login
    
    """
    pass

def update_regex_match_set(RegexMatchSetId=None, Updates=None, ChangeToken=None):
    """
    Inserts or deletes  RegexMatchTuple objects (filters) in a  RegexMatchSet . For each RegexMatchSetUpdate object, you specify the following values:
    For example, you can create a RegexPatternSet that matches any requests with User-Agent headers that contain the string B[a@]dB[o0]t . You can then configure AWS WAF to reject those requests.
    To create and configure a RegexMatchSet , perform the following steps:
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_regex_match_set(
        RegexMatchSetId='string',
        Updates=[
            {
                'Action': 'INSERT'|'DELETE',
                'RegexMatchTuple': {
                    'FieldToMatch': {
                        'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY'|'SINGLE_QUERY_ARG'|'ALL_QUERY_ARGS',
                        'Data': 'string'
                    },
                    'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE',
                    'RegexPatternSetId': 'string'
                }
            },
        ],
        ChangeToken='string'
    )
    
    
    :type RegexMatchSetId: string
    :param RegexMatchSetId: [REQUIRED]\nThe RegexMatchSetId of the RegexMatchSet that you want to update. RegexMatchSetId is returned by CreateRegexMatchSet and by ListRegexMatchSets .\n

    :type Updates: list
    :param Updates: [REQUIRED]\nAn array of RegexMatchSetUpdate objects that you want to insert into or delete from a RegexMatchSet . For more information, see RegexMatchTuple .\n\n(dict) --\nNote\nThis is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.\n\nFor the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.\n\nIn an UpdateRegexMatchSet request, RegexMatchSetUpdate specifies whether to insert or delete a RegexMatchTuple and includes the settings for the RegexMatchTuple .\n\nAction (string) -- [REQUIRED]Specifies whether to insert or delete a RegexMatchTuple .\n\nRegexMatchTuple (dict) -- [REQUIRED]Information about the part of a web request that you want AWS WAF to inspect and the identifier of the regular expression (regex) pattern that you want AWS WAF to search for. If you specify DELETE for the value of Action , the RegexMatchTuple values must exactly match the values in the RegexMatchTuple that you want to delete from the RegexMatchSet .\n\nFieldToMatch (dict) -- [REQUIRED]Specifies where in a web request to look for the RegexPatternSet .\n\nType (string) -- [REQUIRED]The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:\n\nHEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .\nMETHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .\nQUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.\nURI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .\nBODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see CreateSizeConstraintSet .\nSINGLE_QUERY_ARG : The parameter in the query string that you will inspect, such as UserName or SalesRegion . The maximum length for SINGLE_QUERY_ARG is 30 characters.\nALL_QUERY_ARGS : Similar to SINGLE_QUERY_ARG , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in TargetString .\n\n\nData (string) --When the value of Type is HEADER , enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer . The name of the header is not case sensitive.\nWhen the value of Type is SINGLE_QUERY_ARG , enter the name of the parameter that you want AWS WAF to search, for example, UserName or SalesRegion . The parameter name is not case sensitive.\nIf the value of Type is any other value, omit Data .\n\n\n\nTextTransformation (string) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on RegexPatternSet before inspecting a request for a match.\nYou can only specify a single type of TextTransformation.\n\nCMD_LINE\nWhen you\'re concerned that attackers are injecting an operating system commandline command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:\n\nDelete the following characters: ' \' ^\nDelete spaces before the following characters: / (\nReplace the following characters with a space: , ;\nReplace multiple spaces with one space\nConvert uppercase letters (A-Z) to lowercase (a-z)\n\n\nCOMPRESS_WHITE_SPACE\nUse this option to replace the following characters with a space character (decimal 32):\n\nf, formfeed, decimal 12\nt, tab, decimal 9\nn, newline, decimal 10\nr, carriage return, decimal 13\nv, vertical tab, decimal 11\nnon-breaking space, decimal 160\n\n\nCOMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE\n\nUse this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:\n\nReplaces (ampersand)quot; with '\nReplaces (ampersand)nbsp; with a non-breaking space, decimal 160\nReplaces (ampersand)lt; with a 'less than' symbol\nReplaces (ampersand)gt; with >\nReplaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters\nReplaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters\n\n\nLOWERCASE\nUse this option to convert uppercase letters (A-Z) to lowercase (a-z).\n\nURL_DECODE\nUse this option to decode a URL-encoded value.\n\nNONE\nSpecify NONE if you don\'t want to perform any text transformations.\n\nRegexPatternSetId (string) -- [REQUIRED]The RegexPatternSetId for a RegexPatternSet . You use RegexPatternSetId to get information about a RegexPatternSet (see GetRegexPatternSet ), update a RegexPatternSet (see UpdateRegexPatternSet ), insert a RegexPatternSet into a RegexMatchSet or delete one from a RegexMatchSet (see UpdateRegexMatchSet ), and delete an RegexPatternSet from AWS WAF (see DeleteRegexPatternSet ).\n\nRegexPatternSetId is returned by CreateRegexPatternSet and by ListRegexPatternSets .\n\n\n\n\n\n\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChangeToken': 'string'
}


Response Structure

(dict) --

ChangeToken (string) --
The ChangeToken that you used to submit the UpdateRegexMatchSet request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFDisallowedNameException
WAFRegional.Client.exceptions.WAFLimitsExceededException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFNonexistentContainerException
WAFRegional.Client.exceptions.WAFInvalidOperationException
WAFRegional.Client.exceptions.WAFInvalidAccountException


    :return: {
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    Create a RegexMatchSet. For more information, see  CreateRegexMatchSet .
    Use  GetChangeToken to get the change token that you provide in the ChangeToken parameter of an UpdateRegexMatchSet request.
    Submit an UpdateRegexMatchSet request to specify the part of the request that you want AWS WAF to inspect (for example, the header or the URI) and the identifier of the RegexPatternSet that contain the regular expression patters you want AWS WAF to watch for.
    
    """
    pass

def update_regex_pattern_set(RegexPatternSetId=None, Updates=None, ChangeToken=None):
    """
    Inserts or deletes RegexPatternString objects in a  RegexPatternSet . For each RegexPatternString object, you specify the following values:
    For example, you can create a RegexPatternString such as B[a@]dB[o0]t . AWS WAF will match this RegexPatternString to:
    To create and configure a RegexPatternSet , perform the following steps:
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_regex_pattern_set(
        RegexPatternSetId='string',
        Updates=[
            {
                'Action': 'INSERT'|'DELETE',
                'RegexPatternString': 'string'
            },
        ],
        ChangeToken='string'
    )
    
    
    :type RegexPatternSetId: string
    :param RegexPatternSetId: [REQUIRED]\nThe RegexPatternSetId of the RegexPatternSet that you want to update. RegexPatternSetId is returned by CreateRegexPatternSet and by ListRegexPatternSets .\n

    :type Updates: list
    :param Updates: [REQUIRED]\nAn array of RegexPatternSetUpdate objects that you want to insert into or delete from a RegexPatternSet .\n\n(dict) --\nNote\nThis is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.\n\nFor the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.\n\nIn an UpdateRegexPatternSet request, RegexPatternSetUpdate specifies whether to insert or delete a RegexPatternString and includes the settings for the RegexPatternString .\n\nAction (string) -- [REQUIRED]Specifies whether to insert or delete a RegexPatternString .\n\nRegexPatternString (string) -- [REQUIRED]Specifies the regular expression (regex) pattern that you want AWS WAF to search for, such as B[a@]dB[o0]t .\n\n\n\n\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChangeToken': 'string'
}


Response Structure

(dict) --

ChangeToken (string) --
The ChangeToken that you used to submit the UpdateRegexPatternSet request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFLimitsExceededException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFNonexistentContainerException
WAFRegional.Client.exceptions.WAFInvalidOperationException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFInvalidRegexPatternException


    :return: {
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    BadBot
    BadB0t
    B@dBot
    B@dB0t
    
    """
    pass

def update_rule(RuleId=None, ChangeToken=None, Updates=None):
    """
    Inserts or deletes  Predicate objects in a Rule . Each Predicate object identifies a predicate, such as a  ByteMatchSet or an  IPSet , that specifies the web requests that you want to allow, block, or count. If you add more than one predicate to a Rule , a request must match all of the specifications to be allowed, blocked, or counted. For example, suppose that you add the following to a Rule :
    You then add the Rule to a WebACL and specify that you want to block requests that satisfy the Rule . For a request to be blocked, the User-Agent header in the request must contain the value BadBot and the request must originate from the IP address 192.0.2.44.
    To create and configure a Rule , perform the following steps:
    If you want to replace one ByteMatchSet or IPSet with another, you delete the existing one and add the new one.
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example deletes a Predicate object in a rule with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    Expected Output:
    
    :example: response = client.update_rule(
        RuleId='string',
        ChangeToken='string',
        Updates=[
            {
                'Action': 'INSERT'|'DELETE',
                'Predicate': {
                    'Negated': True|False,
                    'Type': 'IPMatch'|'ByteMatch'|'SqlInjectionMatch'|'GeoMatch'|'SizeConstraint'|'XssMatch'|'RegexMatch',
                    'DataId': 'string'
                }
            },
        ]
    )
    
    
    :type RuleId: string
    :param RuleId: [REQUIRED]\nThe RuleId of the Rule that you want to update. RuleId is returned by CreateRule and by ListRules .\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :type Updates: list
    :param Updates: [REQUIRED]\nAn array of RuleUpdate objects that you want to insert into or delete from a Rule . For more information, see the applicable data types:\n\nRuleUpdate : Contains Action and Predicate\nPredicate : Contains DataId , Negated , and Type\nFieldToMatch : Contains Data and Type\n\n\n(dict) --\nNote\nThis is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.\n\nFor the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.\n\nSpecifies a Predicate (such as an IPSet ) and indicates whether you want to add it to a Rule or delete it from a Rule .\n\nAction (string) -- [REQUIRED]Specify INSERT to add a Predicate to a Rule . Use DELETE to remove a Predicate from a Rule .\n\nPredicate (dict) -- [REQUIRED]The ID of the Predicate (such as an IPSet ) that you want to add to a Rule .\n\nNegated (boolean) -- [REQUIRED]Set Negated to False if you want AWS WAF to allow, block, or count requests based on the settings in the specified ByteMatchSet , IPSet , SqlInjectionMatchSet , XssMatchSet , RegexMatchSet , GeoMatchSet , or SizeConstraintSet . For example, if an IPSet includes the IP address 192.0.2.44 , AWS WAF will allow or block requests based on that IP address.\nSet Negated to True if you want AWS WAF to allow or block a request based on the negation of the settings in the ByteMatchSet , IPSet , SqlInjectionMatchSet , XssMatchSet , RegexMatchSet , GeoMatchSet , or SizeConstraintSet . For example, if an IPSet includes the IP address 192.0.2.44 , AWS WAF will allow, block, or count requests based on all IP addresses except 192.0.2.44 .\n\nType (string) -- [REQUIRED]The type of predicate in a Rule , such as ByteMatch or IPSet .\n\nDataId (string) -- [REQUIRED]A unique identifier for a predicate in a Rule , such as ByteMatchSetId or IPSetId . The ID is returned by the corresponding Create or List command.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChangeToken': 'string'
}


Response Structure

(dict) --

ChangeToken (string) --
The ChangeToken that you used to submit the UpdateRule request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFInvalidOperationException
WAFRegional.Client.exceptions.WAFInvalidParameterException
WAFRegional.Client.exceptions.WAFNonexistentContainerException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFReferencedItemException
WAFRegional.Client.exceptions.WAFLimitsExceededException

Examples
The following example deletes a Predicate object in a rule with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
response = client.update_rule(
    ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    RuleId='example1ds3t-46da-4fdb-b8d5-abc321j569j5',
    Updates=[
        {
            'Action': 'DELETE',
            'Predicate': {
                'DataId': 'MyByteMatchSetID',
                'Negated': False,
                'Type': 'ByteMatch',
            },
        },
    ],
)

print(response)


Expected Output:
{
    'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    Create and update the predicates that you want to include in the Rule .
    Create the Rule . See  CreateRule .
    Use GetChangeToken to get the change token that you provide in the ChangeToken parameter of an  UpdateRule request.
    Submit an UpdateRule request to add predicates to the Rule .
    Create and update a WebACL that contains the Rule . See  CreateWebACL .
    
    """
    pass

def update_rule_group(RuleGroupId=None, Updates=None, ChangeToken=None):
    """
    Inserts or deletes  ActivatedRule objects in a RuleGroup .
    You can only insert REGULAR rules into a rule group.
    You can have a maximum of ten rules per rule group.
    To create and configure a RuleGroup , perform the following steps:
    If you want to replace one Rule with another, you delete the existing one and add the new one.
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_rule_group(
        RuleGroupId='string',
        Updates=[
            {
                'Action': 'INSERT'|'DELETE',
                'ActivatedRule': {
                    'Priority': 123,
                    'RuleId': 'string',
                    'Action': {
                        'Type': 'BLOCK'|'ALLOW'|'COUNT'
                    },
                    'OverrideAction': {
                        'Type': 'NONE'|'COUNT'
                    },
                    'Type': 'REGULAR'|'RATE_BASED'|'GROUP',
                    'ExcludedRules': [
                        {
                            'RuleId': 'string'
                        },
                    ]
                }
            },
        ],
        ChangeToken='string'
    )
    
    
    :type RuleGroupId: string
    :param RuleGroupId: [REQUIRED]\nThe RuleGroupId of the RuleGroup that you want to update. RuleGroupId is returned by CreateRuleGroup and by ListRuleGroups .\n

    :type Updates: list
    :param Updates: [REQUIRED]\nAn array of RuleGroupUpdate objects that you want to insert into or delete from a RuleGroup .\nYou can only insert REGULAR rules into a rule group.\n\nActivatedRule|OverrideAction applies only when updating or adding a RuleGroup to a WebACL . In this case you do not use ActivatedRule|Action . For all other update requests, ActivatedRule|Action is used instead of ActivatedRule|OverrideAction .\n\n(dict) --\nNote\nThis is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.\n\nFor the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.\n\nSpecifies an ActivatedRule and indicates whether you want to add it to a RuleGroup or delete it from a RuleGroup .\n\nAction (string) -- [REQUIRED]Specify INSERT to add an ActivatedRule to a RuleGroup . Use DELETE to remove an ActivatedRule from a RuleGroup .\n\nActivatedRule (dict) -- [REQUIRED]The ActivatedRule object specifies a Rule that you want to insert or delete, the priority of the Rule in the WebACL , and the action that you want AWS WAF to take when a web request matches the Rule (ALLOW , BLOCK , or COUNT ).\n\nPriority (integer) -- [REQUIRED]Specifies the order in which the Rules in a WebACL are evaluated. Rules with a lower value for Priority are evaluated before Rules with a higher value. The value must be a unique integer. If you add multiple Rules to a WebACL , the values don\'t need to be consecutive.\n\nRuleId (string) -- [REQUIRED]The RuleId for a Rule . You use RuleId to get more information about a Rule (see GetRule ), update a Rule (see UpdateRule ), insert a Rule into a WebACL or delete a one from a WebACL (see UpdateWebACL ), or delete a Rule from AWS WAF (see DeleteRule ).\n\nRuleId is returned by CreateRule and by ListRules .\n\nAction (dict) --Specifies the action that CloudFront or AWS WAF takes when a web request matches the conditions in the Rule . Valid values for Action include the following:\n\nALLOW : CloudFront responds with the requested object.\nBLOCK : CloudFront responds with an HTTP 403 (Forbidden) status code.\nCOUNT : AWS WAF increments a counter of requests that match the conditions in the rule and then continues to inspect the web request based on the remaining rules in the web ACL.\n\n\nActivatedRule|OverrideAction applies only when updating or adding a RuleGroup to a WebACL . In this case, you do not use ActivatedRule|Action . For all other update requests, ActivatedRule|Action is used instead of ActivatedRule|OverrideAction .\n\nType (string) -- [REQUIRED]Specifies how you want AWS WAF to respond to requests that match the settings in a Rule . Valid settings include the following:\n\nALLOW : AWS WAF allows requests\nBLOCK : AWS WAF blocks requests\nCOUNT : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can\'t specify COUNT for the default action for a WebACL .\n\n\n\n\nOverrideAction (dict) --Use the OverrideAction to test your RuleGroup .\nAny rule in a RuleGroup can potentially block a request. If you set the OverrideAction to None , the RuleGroup will block a request if any individual rule in the RuleGroup matches the request and is configured to block that request. However if you first want to test the RuleGroup , set the OverrideAction to Count . The RuleGroup will then override any block action specified by individual rules contained within the group. Instead of blocking matching requests, those requests will be counted. You can view a record of counted requests using GetSampledRequests .\n\nActivatedRule|OverrideAction applies only when updating or adding a RuleGroup to a WebACL . In this case you do not use ActivatedRule|Action . For all other update requests, ActivatedRule|Action is used instead of ActivatedRule|OverrideAction .\n\nType (string) -- [REQUIRED]\nCOUNT overrides the action specified by the individual rule within a RuleGroup . If set to NONE , the rule\'s action will take place.\n\n\n\nType (string) --The rule type, either REGULAR , as defined by Rule , RATE_BASED , as defined by RateBasedRule , or GROUP , as defined by RuleGroup . The default is REGULAR. Although this field is optional, be aware that if you try to add a RATE_BASED rule to a web ACL without setting the type, the UpdateWebACL request will fail because the request tries to add a REGULAR rule with the specified ID, which does not exist.\n\nExcludedRules (list) --An array of rules to exclude from a rule group. This is applicable only when the ActivatedRule refers to a RuleGroup .\nSometimes it is necessary to troubleshoot rule groups that are blocking traffic unexpectedly (false positives). One troubleshooting technique is to identify the specific rule within the rule group that is blocking the legitimate traffic and then disable (exclude) that particular rule. You can exclude rules from both your own rule groups and AWS Marketplace rule groups that have been associated with a web ACL.\nSpecifying ExcludedRules does not remove those rules from the rule group. Rather, it changes the action for the rules to COUNT . Therefore, requests that match an ExcludedRule are counted but not blocked. The RuleGroup owner will receive COUNT metrics for each ExcludedRule .\nIf you want to exclude rules from a rule group that is already associated with a web ACL, perform the following steps:\n\nUse the AWS WAF logs to identify the IDs of the rules that you want to exclude. For more information about the logs, see Logging Web ACL Traffic Information .\nSubmit an UpdateWebACL request that has two actions:\nThe first action deletes the existing rule group from the web ACL. That is, in the UpdateWebACL request, the first Updates:Action should be DELETE and Updates:ActivatedRule:RuleId should be the rule group that contains the rules that you want to exclude.\nThe second action inserts the same rule group back in, but specifying the rules to exclude. That is, the second Updates:Action should be INSERT , Updates:ActivatedRule:RuleId should be the rule group that you just removed, and ExcludedRules should contain the rules that you want to exclude.\n\n\n\n\n(dict) --\nNote\nThis is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.\n\nFor the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.\n\nThe rule to exclude from a rule group. This is applicable only when the ActivatedRule refers to a RuleGroup . The rule must belong to the RuleGroup that is specified by the ActivatedRule .\n\nRuleId (string) -- [REQUIRED]The unique identifier for the rule to exclude from the rule group.\n\n\n\n\n\n\n\n\n\n\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChangeToken': 'string'
}


Response Structure

(dict) --

ChangeToken (string) --
The ChangeToken that you used to submit the UpdateRuleGroup request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFNonexistentContainerException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFInvalidOperationException
WAFRegional.Client.exceptions.WAFLimitsExceededException
WAFRegional.Client.exceptions.WAFInvalidParameterException


    :return: {
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    RuleGroupId (string) -- [REQUIRED]
    The RuleGroupId of the  RuleGroup that you want to update. RuleGroupId is returned by  CreateRuleGroup and by  ListRuleGroups .
    
    Updates (list) -- [REQUIRED]
    An array of RuleGroupUpdate objects that you want to insert into or delete from a  RuleGroup .
    You can only insert REGULAR rules into a rule group.
    
    ActivatedRule|OverrideAction applies only when updating or adding a RuleGroup to a WebACL . In this case you do not use ActivatedRule|Action . For all other update requests, ActivatedRule|Action is used instead of ActivatedRule|OverrideAction .
    
    (dict) --
    Note
    This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.
    
    For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.
    
    Specifies an ActivatedRule and indicates whether you want to add it to a RuleGroup or delete it from a RuleGroup .
    
    Action (string) -- [REQUIRED]Specify INSERT to add an ActivatedRule to a RuleGroup . Use DELETE to remove an ActivatedRule from a RuleGroup .
    
    ActivatedRule (dict) -- [REQUIRED]The ActivatedRule object specifies a Rule that you want to insert or delete, the priority of the Rule in the WebACL , and the action that you want AWS WAF to take when a web request matches the Rule (ALLOW , BLOCK , or COUNT ).
    
    Priority (integer) -- [REQUIRED]Specifies the order in which the Rules in a WebACL are evaluated. Rules with a lower value for Priority are evaluated before Rules with a higher value. The value must be a unique integer. If you add multiple Rules to a WebACL , the values don\'t need to be consecutive.
    
    RuleId (string) -- [REQUIRED]The RuleId for a Rule . You use RuleId to get more information about a Rule (see  GetRule ), update a Rule (see  UpdateRule ), insert a Rule into a WebACL or delete a one from a WebACL (see  UpdateWebACL ), or delete a Rule from AWS WAF (see  DeleteRule ).
    
    RuleId is returned by  CreateRule and by  ListRules .
    
    Action (dict) --Specifies the action that CloudFront or AWS WAF takes when a web request matches the conditions in the Rule . Valid values for Action include the following:
    
    ALLOW : CloudFront responds with the requested object.
    BLOCK : CloudFront responds with an HTTP 403 (Forbidden) status code.
    COUNT : AWS WAF increments a counter of requests that match the conditions in the rule and then continues to inspect the web request based on the remaining rules in the web ACL.
    
    
    ActivatedRule|OverrideAction applies only when updating or adding a RuleGroup to a WebACL . In this case, you do not use ActivatedRule|Action . For all other update requests, ActivatedRule|Action is used instead of ActivatedRule|OverrideAction .
    
    Type (string) -- [REQUIRED]Specifies how you want AWS WAF to respond to requests that match the settings in a Rule . Valid settings include the following:
    
    ALLOW : AWS WAF allows requests
    BLOCK : AWS WAF blocks requests
    COUNT : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can\'t specify COUNT for the default action for a WebACL .
    
    
    
    
    OverrideAction (dict) --Use the OverrideAction to test your RuleGroup .
    Any rule in a RuleGroup can potentially block a request. If you set the OverrideAction to None , the RuleGroup will block a request if any individual rule in the RuleGroup matches the request and is configured to block that request. However if you first want to test the RuleGroup , set the OverrideAction to Count . The RuleGroup will then override any block action specified by individual rules contained within the group. Instead of blocking matching requests, those requests will be counted. You can view a record of counted requests using  GetSampledRequests .
    
    ActivatedRule|OverrideAction applies only when updating or adding a RuleGroup to a WebACL . In this case you do not use ActivatedRule|Action . For all other update requests, ActivatedRule|Action is used instead of ActivatedRule|OverrideAction .
    
    Type (string) -- [REQUIRED]
    COUNT overrides the action specified by the individual rule within a RuleGroup . If set to NONE , the rule\'s action will take place.
    
    
    
    Type (string) --The rule type, either REGULAR , as defined by  Rule , RATE_BASED , as defined by  RateBasedRule , or GROUP , as defined by  RuleGroup . The default is REGULAR. Although this field is optional, be aware that if you try to add a RATE_BASED rule to a web ACL without setting the type, the  UpdateWebACL request will fail because the request tries to add a REGULAR rule with the specified ID, which does not exist.
    
    ExcludedRules (list) --An array of rules to exclude from a rule group. This is applicable only when the ActivatedRule refers to a RuleGroup .
    Sometimes it is necessary to troubleshoot rule groups that are blocking traffic unexpectedly (false positives). One troubleshooting technique is to identify the specific rule within the rule group that is blocking the legitimate traffic and then disable (exclude) that particular rule. You can exclude rules from both your own rule groups and AWS Marketplace rule groups that have been associated with a web ACL.
    Specifying ExcludedRules does not remove those rules from the rule group. Rather, it changes the action for the rules to COUNT . Therefore, requests that match an ExcludedRule are counted but not blocked. The RuleGroup owner will receive COUNT metrics for each ExcludedRule .
    If you want to exclude rules from a rule group that is already associated with a web ACL, perform the following steps:
    
    Use the AWS WAF logs to identify the IDs of the rules that you want to exclude. For more information about the logs, see Logging Web ACL Traffic Information .
    Submit an  UpdateWebACL request that has two actions:
    The first action deletes the existing rule group from the web ACL. That is, in the  UpdateWebACL request, the first Updates:Action should be DELETE and Updates:ActivatedRule:RuleId should be the rule group that contains the rules that you want to exclude.
    The second action inserts the same rule group back in, but specifying the rules to exclude. That is, the second Updates:Action should be INSERT , Updates:ActivatedRule:RuleId should be the rule group that you just removed, and ExcludedRules should contain the rules that you want to exclude.
    
    
    
    
    (dict) --
    Note
    This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.
    
    For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.
    
    The rule to exclude from a rule group. This is applicable only when the ActivatedRule refers to a RuleGroup . The rule must belong to the RuleGroup that is specified by the ActivatedRule .
    
    RuleId (string) -- [REQUIRED]The unique identifier for the rule to exclude from the rule group.
    
    
    
    
    
    
    
    
    
    
    
    ChangeToken (string) -- [REQUIRED]
    The value returned by the most recent call to  GetChangeToken .
    
    
    """
    pass

def update_size_constraint_set(SizeConstraintSetId=None, ChangeToken=None, Updates=None):
    """
    Inserts or deletes  SizeConstraint objects (filters) in a  SizeConstraintSet . For each SizeConstraint object, you specify the following values:
    For example, you can add a SizeConstraintSetUpdate object that matches web requests in which the length of the User-Agent header is greater than 100 bytes. You can then configure AWS WAF to block those requests.
    To create and configure a SizeConstraintSet , perform the following steps:
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example deletes a SizeConstraint object (filters) in a size constraint set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    Expected Output:
    
    :example: response = client.update_size_constraint_set(
        SizeConstraintSetId='string',
        ChangeToken='string',
        Updates=[
            {
                'Action': 'INSERT'|'DELETE',
                'SizeConstraint': {
                    'FieldToMatch': {
                        'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY'|'SINGLE_QUERY_ARG'|'ALL_QUERY_ARGS',
                        'Data': 'string'
                    },
                    'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE',
                    'ComparisonOperator': 'EQ'|'NE'|'LE'|'LT'|'GE'|'GT',
                    'Size': 123
                }
            },
        ]
    )
    
    
    :type SizeConstraintSetId: string
    :param SizeConstraintSetId: [REQUIRED]\nThe SizeConstraintSetId of the SizeConstraintSet that you want to update. SizeConstraintSetId is returned by CreateSizeConstraintSet and by ListSizeConstraintSets .\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :type Updates: list
    :param Updates: [REQUIRED]\nAn array of SizeConstraintSetUpdate objects that you want to insert into or delete from a SizeConstraintSet . For more information, see the applicable data types:\n\nSizeConstraintSetUpdate : Contains Action and SizeConstraint\nSizeConstraint : Contains FieldToMatch , TextTransformation , ComparisonOperator , and Size\nFieldToMatch : Contains Data and Type\n\n\n(dict) --\nNote\nThis is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.\n\nFor the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.\n\nSpecifies the part of a web request that you want to inspect the size of and indicates whether you want to add the specification to a SizeConstraintSet or delete it from a SizeConstraintSet .\n\nAction (string) -- [REQUIRED]Specify INSERT to add a SizeConstraintSetUpdate to a SizeConstraintSet . Use DELETE to remove a SizeConstraintSetUpdate from a SizeConstraintSet .\n\nSizeConstraint (dict) -- [REQUIRED]Specifies a constraint on the size of a part of the web request. AWS WAF uses the Size , ComparisonOperator , and FieldToMatch to build an expression in the form of 'Size ComparisonOperator size in bytes of FieldToMatch '. If that expression is true, the SizeConstraint is considered to match.\n\nFieldToMatch (dict) -- [REQUIRED]Specifies where in a web request to look for the size constraint.\n\nType (string) -- [REQUIRED]The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:\n\nHEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .\nMETHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .\nQUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.\nURI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .\nBODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see CreateSizeConstraintSet .\nSINGLE_QUERY_ARG : The parameter in the query string that you will inspect, such as UserName or SalesRegion . The maximum length for SINGLE_QUERY_ARG is 30 characters.\nALL_QUERY_ARGS : Similar to SINGLE_QUERY_ARG , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in TargetString .\n\n\nData (string) --When the value of Type is HEADER , enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer . The name of the header is not case sensitive.\nWhen the value of Type is SINGLE_QUERY_ARG , enter the name of the parameter that you want AWS WAF to search, for example, UserName or SalesRegion . The parameter name is not case sensitive.\nIf the value of Type is any other value, omit Data .\n\n\n\nTextTransformation (string) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on FieldToMatch before inspecting it for a match.\nYou can only specify a single type of TextTransformation.\nNote that if you choose BODY for the value of Type , you must choose NONE for TextTransformation because CloudFront forwards only the first 8192 bytes for inspection.\n\nNONE\nSpecify NONE if you don\'t want to perform any text transformations.\n\nCMD_LINE\nWhen you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:\n\nDelete the following characters: ' \' ^\nDelete spaces before the following characters: / (\nReplace the following characters with a space: , ;\nReplace multiple spaces with one space\nConvert uppercase letters (A-Z) to lowercase (a-z)\n\n\nCOMPRESS_WHITE_SPACE\nUse this option to replace the following characters with a space character (decimal 32):\n\nf, formfeed, decimal 12\nt, tab, decimal 9\nn, newline, decimal 10\nr, carriage return, decimal 13\nv, vertical tab, decimal 11\nnon-breaking space, decimal 160\n\n\nCOMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE\n\nUse this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:\n\nReplaces (ampersand)quot; with '\nReplaces (ampersand)nbsp; with a non-breaking space, decimal 160\nReplaces (ampersand)lt; with a 'less than' symbol\nReplaces (ampersand)gt; with >\nReplaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters\nReplaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters\n\n\nLOWERCASE\nUse this option to convert uppercase letters (A-Z) to lowercase (a-z).\n\nURL_DECODE\nUse this option to decode a URL-encoded value.\n\nComparisonOperator (string) -- [REQUIRED]The type of comparison you want AWS WAF to perform. AWS WAF uses this in combination with the provided Size and FieldToMatch to build an expression in the form of 'Size ComparisonOperator size in bytes of FieldToMatch '. If that expression is true, the SizeConstraint is considered to match.\n\nEQ : Used to test if the Size is equal to the size of the FieldToMatchNE : Used to test if the Size is not equal to the size of the FieldToMatch\nLE : Used to test if the Size is less than or equal to the size of the FieldToMatch\nLT : Used to test if the Size is strictly less than the size of the FieldToMatch\nGE : Used to test if the Size is greater than or equal to the size of the FieldToMatch\nGT : Used to test if the Size is strictly greater than the size of the FieldToMatch\n\n\nSize (integer) -- [REQUIRED]The size in bytes that you want AWS WAF to compare against the size of the specified FieldToMatch . AWS WAF uses this in combination with ComparisonOperator and FieldToMatch to build an expression in the form of 'Size ComparisonOperator size in bytes of FieldToMatch '. If that expression is true, the SizeConstraint is considered to match.\nValid values for size are 0 - 21474836480 bytes (0 - 20 GB).\nIf you specify URI for the value of Type , the / in the URI counts as one character. For example, the URI /logo.jpg is nine characters long.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChangeToken': 'string'
}


Response Structure

(dict) --

ChangeToken (string) --
The ChangeToken that you used to submit the UpdateSizeConstraintSet request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFInvalidOperationException
WAFRegional.Client.exceptions.WAFInvalidParameterException
WAFRegional.Client.exceptions.WAFNonexistentContainerException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFReferencedItemException
WAFRegional.Client.exceptions.WAFLimitsExceededException

Examples
The following example deletes a SizeConstraint object (filters) in a size constraint set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
response = client.update_size_constraint_set(
    ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    SizeConstraintSetId='example1ds3t-46da-4fdb-b8d5-abc321j569j5',
    Updates=[
        {
            'Action': 'DELETE',
            'SizeConstraint': {
                'ComparisonOperator': 'GT',
                'FieldToMatch': {
                    'Type': 'QUERY_STRING',
                },
                'Size': 0,
                'TextTransformation': 'NONE',
            },
        },
    ],
)

print(response)


Expected Output:
{
    'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    Create a SizeConstraintSet. For more information, see  CreateSizeConstraintSet .
    Use  GetChangeToken to get the change token that you provide in the ChangeToken parameter of an UpdateSizeConstraintSet request.
    Submit an UpdateSizeConstraintSet request to specify the part of the request that you want AWS WAF to inspect (for example, the header or the URI) and the value that you want AWS WAF to watch for.
    
    """
    pass

def update_sql_injection_match_set(SqlInjectionMatchSetId=None, ChangeToken=None, Updates=None):
    """
    Inserts or deletes  SqlInjectionMatchTuple objects (filters) in a  SqlInjectionMatchSet . For each SqlInjectionMatchTuple object, you specify the following values:
    You use SqlInjectionMatchSet objects to specify which CloudFront requests that you want to allow, block, or count. For example, if you\'re receiving requests that contain snippets of SQL code in the query string and you want to block the requests, you can create a SqlInjectionMatchSet with the applicable settings, and then configure AWS WAF to block the requests.
    To create and configure a SqlInjectionMatchSet , perform the following steps:
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example deletes a SqlInjectionMatchTuple object (filters) in a SQL injection match set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    Expected Output:
    
    :example: response = client.update_sql_injection_match_set(
        SqlInjectionMatchSetId='string',
        ChangeToken='string',
        Updates=[
            {
                'Action': 'INSERT'|'DELETE',
                'SqlInjectionMatchTuple': {
                    'FieldToMatch': {
                        'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY'|'SINGLE_QUERY_ARG'|'ALL_QUERY_ARGS',
                        'Data': 'string'
                    },
                    'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                }
            },
        ]
    )
    
    
    :type SqlInjectionMatchSetId: string
    :param SqlInjectionMatchSetId: [REQUIRED]\nThe SqlInjectionMatchSetId of the SqlInjectionMatchSet that you want to update. SqlInjectionMatchSetId is returned by CreateSqlInjectionMatchSet and by ListSqlInjectionMatchSets .\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :type Updates: list
    :param Updates: [REQUIRED]\nAn array of SqlInjectionMatchSetUpdate objects that you want to insert into or delete from a SqlInjectionMatchSet . For more information, see the applicable data types:\n\nSqlInjectionMatchSetUpdate : Contains Action and SqlInjectionMatchTuple\nSqlInjectionMatchTuple : Contains FieldToMatch and TextTransformation\nFieldToMatch : Contains Data and Type\n\n\n(dict) --\nNote\nThis is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.\n\nFor the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.\n\nSpecifies the part of a web request that you want to inspect for snippets of malicious SQL code and indicates whether you want to add the specification to a SqlInjectionMatchSet or delete it from a SqlInjectionMatchSet .\n\nAction (string) -- [REQUIRED]Specify INSERT to add a SqlInjectionMatchSetUpdate to a SqlInjectionMatchSet . Use DELETE to remove a SqlInjectionMatchSetUpdate from a SqlInjectionMatchSet .\n\nSqlInjectionMatchTuple (dict) -- [REQUIRED]Specifies the part of a web request that you want AWS WAF to inspect for snippets of malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.\n\nFieldToMatch (dict) -- [REQUIRED]Specifies where in a web request to look for snippets of malicious SQL code.\n\nType (string) -- [REQUIRED]The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:\n\nHEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .\nMETHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .\nQUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.\nURI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .\nBODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see CreateSizeConstraintSet .\nSINGLE_QUERY_ARG : The parameter in the query string that you will inspect, such as UserName or SalesRegion . The maximum length for SINGLE_QUERY_ARG is 30 characters.\nALL_QUERY_ARGS : Similar to SINGLE_QUERY_ARG , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in TargetString .\n\n\nData (string) --When the value of Type is HEADER , enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer . The name of the header is not case sensitive.\nWhen the value of Type is SINGLE_QUERY_ARG , enter the name of the parameter that you want AWS WAF to search, for example, UserName or SalesRegion . The parameter name is not case sensitive.\nIf the value of Type is any other value, omit Data .\n\n\n\nTextTransformation (string) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on FieldToMatch before inspecting it for a match.\nYou can only specify a single type of TextTransformation.\n\nCMD_LINE\nWhen you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:\n\nDelete the following characters: ' \' ^\nDelete spaces before the following characters: / (\nReplace the following characters with a space: , ;\nReplace multiple spaces with one space\nConvert uppercase letters (A-Z) to lowercase (a-z)\n\n\nCOMPRESS_WHITE_SPACE\nUse this option to replace the following characters with a space character (decimal 32):\n\nf, formfeed, decimal 12\nt, tab, decimal 9\nn, newline, decimal 10\nr, carriage return, decimal 13\nv, vertical tab, decimal 11\nnon-breaking space, decimal 160\n\n\nCOMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE\n\nUse this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:\n\nReplaces (ampersand)quot; with '\nReplaces (ampersand)nbsp; with a non-breaking space, decimal 160\nReplaces (ampersand)lt; with a 'less than' symbol\nReplaces (ampersand)gt; with >\nReplaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters\nReplaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters\n\n\nLOWERCASE\nUse this option to convert uppercase letters (A-Z) to lowercase (a-z).\n\nURL_DECODE\nUse this option to decode a URL-encoded value.\n\nNONE\nSpecify NONE if you don\'t want to perform any text transformations.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChangeToken': 'string'
}


Response Structure

(dict) --
The response to an  UpdateSqlInjectionMatchSets request.

ChangeToken (string) --
The ChangeToken that you used to submit the UpdateSqlInjectionMatchSet request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFInvalidOperationException
WAFRegional.Client.exceptions.WAFInvalidParameterException
WAFRegional.Client.exceptions.WAFNonexistentContainerException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFLimitsExceededException

Examples
The following example deletes a SqlInjectionMatchTuple object (filters) in a SQL injection match set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
response = client.update_sql_injection_match_set(
    ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    SqlInjectionMatchSetId='example1ds3t-46da-4fdb-b8d5-abc321j569j5',
    Updates=[
        {
            'Action': 'DELETE',
            'SqlInjectionMatchTuple': {
                'FieldToMatch': {
                    'Type': 'QUERY_STRING',
                },
                'TextTransformation': 'URL_DECODE',
            },
        },
    ],
)

print(response)


Expected Output:
{
    'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    Submit a  CreateSqlInjectionMatchSet request.
    Use  GetChangeToken to get the change token that you provide in the ChangeToken parameter of an  UpdateIPSet request.
    Submit an UpdateSqlInjectionMatchSet request to specify the parts of web requests that you want AWS WAF to inspect for snippets of SQL code.
    
    """
    pass

def update_web_acl(WebACLId=None, ChangeToken=None, Updates=None, DefaultAction=None):
    """
    Inserts or deletes  ActivatedRule objects in a WebACL . Each Rule identifies web requests that you want to allow, block, or count. When you update a WebACL , you specify the following values:
    To create and configure a WebACL , perform the following steps:
    Be aware that if you try to add a RATE_BASED rule to a web ACL without setting the rule type when first creating the rule, the  UpdateWebACL request will fail because the request tries to add a REGULAR rule (the default rule type) with the specified ID, which does not exist.
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example deletes an ActivatedRule object in a WebACL with the ID webacl-1472061481310.
    Expected Output:
    
    :example: response = client.update_web_acl(
        WebACLId='string',
        ChangeToken='string',
        Updates=[
            {
                'Action': 'INSERT'|'DELETE',
                'ActivatedRule': {
                    'Priority': 123,
                    'RuleId': 'string',
                    'Action': {
                        'Type': 'BLOCK'|'ALLOW'|'COUNT'
                    },
                    'OverrideAction': {
                        'Type': 'NONE'|'COUNT'
                    },
                    'Type': 'REGULAR'|'RATE_BASED'|'GROUP',
                    'ExcludedRules': [
                        {
                            'RuleId': 'string'
                        },
                    ]
                }
            },
        ],
        DefaultAction={
            'Type': 'BLOCK'|'ALLOW'|'COUNT'
        }
    )
    
    
    :type WebACLId: string
    :param WebACLId: [REQUIRED]\nThe WebACLId of the WebACL that you want to update. WebACLId is returned by CreateWebACL and by ListWebACLs .\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :type Updates: list
    :param Updates: An array of updates to make to the WebACL .\nAn array of WebACLUpdate objects that you want to insert into or delete from a WebACL . For more information, see the applicable data types:\n\nWebACLUpdate : Contains Action and ActivatedRule\nActivatedRule : Contains Action , OverrideAction , Priority , RuleId , and Type . ActivatedRule|OverrideAction applies only when updating or adding a RuleGroup to a WebACL . In this case, you do not use ActivatedRule|Action . For all other update requests, ActivatedRule|Action is used instead of ActivatedRule|OverrideAction .\nWafAction : Contains Type\n\n\n(dict) --\nNote\nThis is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.\n\nFor the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.\n\nSpecifies whether to insert a Rule into or delete a Rule from a WebACL .\n\nAction (string) -- [REQUIRED]Specifies whether to insert a Rule into or delete a Rule from a WebACL .\n\nActivatedRule (dict) -- [REQUIRED]The ActivatedRule object in an UpdateWebACL request specifies a Rule that you want to insert or delete, the priority of the Rule in the WebACL , and the action that you want AWS WAF to take when a web request matches the Rule (ALLOW , BLOCK , or COUNT ).\n\nPriority (integer) -- [REQUIRED]Specifies the order in which the Rules in a WebACL are evaluated. Rules with a lower value for Priority are evaluated before Rules with a higher value. The value must be a unique integer. If you add multiple Rules to a WebACL , the values don\'t need to be consecutive.\n\nRuleId (string) -- [REQUIRED]The RuleId for a Rule . You use RuleId to get more information about a Rule (see GetRule ), update a Rule (see UpdateRule ), insert a Rule into a WebACL or delete a one from a WebACL (see UpdateWebACL ), or delete a Rule from AWS WAF (see DeleteRule ).\n\nRuleId is returned by CreateRule and by ListRules .\n\nAction (dict) --Specifies the action that CloudFront or AWS WAF takes when a web request matches the conditions in the Rule . Valid values for Action include the following:\n\nALLOW : CloudFront responds with the requested object.\nBLOCK : CloudFront responds with an HTTP 403 (Forbidden) status code.\nCOUNT : AWS WAF increments a counter of requests that match the conditions in the rule and then continues to inspect the web request based on the remaining rules in the web ACL.\n\n\nActivatedRule|OverrideAction applies only when updating or adding a RuleGroup to a WebACL . In this case, you do not use ActivatedRule|Action . For all other update requests, ActivatedRule|Action is used instead of ActivatedRule|OverrideAction .\n\nType (string) -- [REQUIRED]Specifies how you want AWS WAF to respond to requests that match the settings in a Rule . Valid settings include the following:\n\nALLOW : AWS WAF allows requests\nBLOCK : AWS WAF blocks requests\nCOUNT : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can\'t specify COUNT for the default action for a WebACL .\n\n\n\n\nOverrideAction (dict) --Use the OverrideAction to test your RuleGroup .\nAny rule in a RuleGroup can potentially block a request. If you set the OverrideAction to None , the RuleGroup will block a request if any individual rule in the RuleGroup matches the request and is configured to block that request. However if you first want to test the RuleGroup , set the OverrideAction to Count . The RuleGroup will then override any block action specified by individual rules contained within the group. Instead of blocking matching requests, those requests will be counted. You can view a record of counted requests using GetSampledRequests .\n\nActivatedRule|OverrideAction applies only when updating or adding a RuleGroup to a WebACL . In this case you do not use ActivatedRule|Action . For all other update requests, ActivatedRule|Action is used instead of ActivatedRule|OverrideAction .\n\nType (string) -- [REQUIRED]\nCOUNT overrides the action specified by the individual rule within a RuleGroup . If set to NONE , the rule\'s action will take place.\n\n\n\nType (string) --The rule type, either REGULAR , as defined by Rule , RATE_BASED , as defined by RateBasedRule , or GROUP , as defined by RuleGroup . The default is REGULAR. Although this field is optional, be aware that if you try to add a RATE_BASED rule to a web ACL without setting the type, the UpdateWebACL request will fail because the request tries to add a REGULAR rule with the specified ID, which does not exist.\n\nExcludedRules (list) --An array of rules to exclude from a rule group. This is applicable only when the ActivatedRule refers to a RuleGroup .\nSometimes it is necessary to troubleshoot rule groups that are blocking traffic unexpectedly (false positives). One troubleshooting technique is to identify the specific rule within the rule group that is blocking the legitimate traffic and then disable (exclude) that particular rule. You can exclude rules from both your own rule groups and AWS Marketplace rule groups that have been associated with a web ACL.\nSpecifying ExcludedRules does not remove those rules from the rule group. Rather, it changes the action for the rules to COUNT . Therefore, requests that match an ExcludedRule are counted but not blocked. The RuleGroup owner will receive COUNT metrics for each ExcludedRule .\nIf you want to exclude rules from a rule group that is already associated with a web ACL, perform the following steps:\n\nUse the AWS WAF logs to identify the IDs of the rules that you want to exclude. For more information about the logs, see Logging Web ACL Traffic Information .\nSubmit an UpdateWebACL request that has two actions:\nThe first action deletes the existing rule group from the web ACL. That is, in the UpdateWebACL request, the first Updates:Action should be DELETE and Updates:ActivatedRule:RuleId should be the rule group that contains the rules that you want to exclude.\nThe second action inserts the same rule group back in, but specifying the rules to exclude. That is, the second Updates:Action should be INSERT , Updates:ActivatedRule:RuleId should be the rule group that you just removed, and ExcludedRules should contain the rules that you want to exclude.\n\n\n\n\n(dict) --\nNote\nThis is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.\n\nFor the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.\n\nThe rule to exclude from a rule group. This is applicable only when the ActivatedRule refers to a RuleGroup . The rule must belong to the RuleGroup that is specified by the ActivatedRule .\n\nRuleId (string) -- [REQUIRED]The unique identifier for the rule to exclude from the rule group.\n\n\n\n\n\n\n\n\n\n\n

    :type DefaultAction: dict
    :param DefaultAction: A default action for the web ACL, either ALLOW or BLOCK. AWS WAF performs the default action if a request doesn\'t match the criteria in any of the rules in a web ACL.\n\nType (string) -- [REQUIRED]Specifies how you want AWS WAF to respond to requests that match the settings in a Rule . Valid settings include the following:\n\nALLOW : AWS WAF allows requests\nBLOCK : AWS WAF blocks requests\nCOUNT : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can\'t specify COUNT for the default action for a WebACL .\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChangeToken': 'string'
}


Response Structure

(dict) --

ChangeToken (string) --
The ChangeToken that you used to submit the UpdateWebACL request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFInvalidOperationException
WAFRegional.Client.exceptions.WAFInvalidParameterException
WAFRegional.Client.exceptions.WAFNonexistentContainerException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFReferencedItemException
WAFRegional.Client.exceptions.WAFLimitsExceededException
WAFRegional.Client.exceptions.WAFSubscriptionNotFoundException

Examples
The following example deletes an ActivatedRule object in a WebACL with the ID webacl-1472061481310.
response = client.update_web_acl(
    ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    DefaultAction={
        'Type': 'ALLOW',
    },
    Updates=[
        {
            'Action': 'DELETE',
            'ActivatedRule': {
                'Action': {
                    'Type': 'ALLOW',
                },
                'Priority': 1,
                'RuleId': 'WAFRule-1-Example',
            },
        },
    ],
    WebACLId='webacl-1472061481310',
)

print(response)


Expected Output:
{
    'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    Create and update the predicates that you want to include in Rules . For more information, see  CreateByteMatchSet ,  UpdateByteMatchSet ,  CreateIPSet ,  UpdateIPSet ,  CreateSqlInjectionMatchSet , and  UpdateSqlInjectionMatchSet .
    Create and update the Rules that you want to include in the WebACL . For more information, see  CreateRule and  UpdateRule .
    Create a WebACL . See  CreateWebACL .
    Use GetChangeToken to get the change token that you provide in the ChangeToken parameter of an  UpdateWebACL request.
    Submit an UpdateWebACL request to specify the Rules that you want to include in the WebACL , to specify the default action, and to associate the WebACL with a CloudFront distribution.  The ActivatedRule can be a rule group. If you specify a rule group as your ActivatedRule , you can exclude specific rules from that rule group. If you already have a rule group associated with a web ACL and want to submit an UpdateWebACL request to exclude certain rules from that rule group, you must first remove the rule group from the web ACL, the re-insert it again, specifying the excluded rules. For details, see  ActivatedRule$ExcludedRules .
    
    """
    pass

def update_xss_match_set(XssMatchSetId=None, ChangeToken=None, Updates=None):
    """
    Inserts or deletes  XssMatchTuple objects (filters) in an  XssMatchSet . For each XssMatchTuple object, you specify the following values:
    You use XssMatchSet objects to specify which CloudFront requests that you want to allow, block, or count. For example, if you\'re receiving requests that contain cross-site scripting attacks in the request body and you want to block the requests, you can create an XssMatchSet with the applicable settings, and then configure AWS WAF to block the requests.
    To create and configure an XssMatchSet , perform the following steps:
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example deletes an XssMatchTuple object (filters) in an XssMatchSet with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    Expected Output:
    
    :example: response = client.update_xss_match_set(
        XssMatchSetId='string',
        ChangeToken='string',
        Updates=[
            {
                'Action': 'INSERT'|'DELETE',
                'XssMatchTuple': {
                    'FieldToMatch': {
                        'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY'|'SINGLE_QUERY_ARG'|'ALL_QUERY_ARGS',
                        'Data': 'string'
                    },
                    'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                }
            },
        ]
    )
    
    
    :type XssMatchSetId: string
    :param XssMatchSetId: [REQUIRED]\nThe XssMatchSetId of the XssMatchSet that you want to update. XssMatchSetId is returned by CreateXssMatchSet and by ListXssMatchSets .\n

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]\nThe value returned by the most recent call to GetChangeToken .\n

    :type Updates: list
    :param Updates: [REQUIRED]\nAn array of XssMatchSetUpdate objects that you want to insert into or delete from an XssMatchSet . For more information, see the applicable data types:\n\nXssMatchSetUpdate : Contains Action and XssMatchTuple\nXssMatchTuple : Contains FieldToMatch and TextTransformation\nFieldToMatch : Contains Data and Type\n\n\n(dict) --\nNote\nThis is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.\n\nFor the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.\n\nSpecifies the part of a web request that you want to inspect for cross-site scripting attacks and indicates whether you want to add the specification to an XssMatchSet or delete it from an XssMatchSet .\n\nAction (string) -- [REQUIRED]Specify INSERT to add an XssMatchSetUpdate to an XssMatchSet . Use DELETE to remove an XssMatchSetUpdate from an XssMatchSet .\n\nXssMatchTuple (dict) -- [REQUIRED]Specifies the part of a web request that you want AWS WAF to inspect for cross-site scripting attacks and, if you want AWS WAF to inspect a header, the name of the header.\n\nFieldToMatch (dict) -- [REQUIRED]Specifies where in a web request to look for cross-site scripting attacks.\n\nType (string) -- [REQUIRED]The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:\n\nHEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .\nMETHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .\nQUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.\nURI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .\nBODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see CreateSizeConstraintSet .\nSINGLE_QUERY_ARG : The parameter in the query string that you will inspect, such as UserName or SalesRegion . The maximum length for SINGLE_QUERY_ARG is 30 characters.\nALL_QUERY_ARGS : Similar to SINGLE_QUERY_ARG , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in TargetString .\n\n\nData (string) --When the value of Type is HEADER , enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer . The name of the header is not case sensitive.\nWhen the value of Type is SINGLE_QUERY_ARG , enter the name of the parameter that you want AWS WAF to search, for example, UserName or SalesRegion . The parameter name is not case sensitive.\nIf the value of Type is any other value, omit Data .\n\n\n\nTextTransformation (string) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on FieldToMatch before inspecting it for a match.\nYou can only specify a single type of TextTransformation.\n\nCMD_LINE\nWhen you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:\n\nDelete the following characters: ' \' ^\nDelete spaces before the following characters: / (\nReplace the following characters with a space: , ;\nReplace multiple spaces with one space\nConvert uppercase letters (A-Z) to lowercase (a-z)\n\n\nCOMPRESS_WHITE_SPACE\nUse this option to replace the following characters with a space character (decimal 32):\n\nf, formfeed, decimal 12\nt, tab, decimal 9\nn, newline, decimal 10\nr, carriage return, decimal 13\nv, vertical tab, decimal 11\nnon-breaking space, decimal 160\n\n\nCOMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE\n\nUse this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:\n\nReplaces (ampersand)quot; with '\nReplaces (ampersand)nbsp; with a non-breaking space, decimal 160\nReplaces (ampersand)lt; with a 'less than' symbol\nReplaces (ampersand)gt; with >\nReplaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters\nReplaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters\n\n\nLOWERCASE\nUse this option to convert uppercase letters (A-Z) to lowercase (a-z).\n\nURL_DECODE\nUse this option to decode a URL-encoded value.\n\nNONE\nSpecify NONE if you don\'t want to perform any text transformations.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChangeToken': 'string'
}


Response Structure

(dict) --
The response to an  UpdateXssMatchSets request.

ChangeToken (string) --
The ChangeToken that you used to submit the UpdateXssMatchSet request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .







Exceptions

WAFRegional.Client.exceptions.WAFInternalErrorException
WAFRegional.Client.exceptions.WAFInvalidAccountException
WAFRegional.Client.exceptions.WAFInvalidOperationException
WAFRegional.Client.exceptions.WAFInvalidParameterException
WAFRegional.Client.exceptions.WAFNonexistentContainerException
WAFRegional.Client.exceptions.WAFNonexistentItemException
WAFRegional.Client.exceptions.WAFStaleDataException
WAFRegional.Client.exceptions.WAFLimitsExceededException

Examples
The following example deletes an XssMatchTuple object (filters) in an XssMatchSet with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
response = client.update_xss_match_set(
    ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    Updates=[
        {
            'Action': 'DELETE',
            'XssMatchTuple': {
                'FieldToMatch': {
                    'Type': 'QUERY_STRING',
                },
                'TextTransformation': 'URL_DECODE',
            },
        },
    ],
    XssMatchSetId='example1ds3t-46da-4fdb-b8d5-abc321j569j5',
)

print(response)


Expected Output:
{
    'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    Submit a  CreateXssMatchSet request.
    Use  GetChangeToken to get the change token that you provide in the ChangeToken parameter of an  UpdateIPSet request.
    Submit an UpdateXssMatchSet request to specify the parts of web requests that you want AWS WAF to inspect for cross-site scripting attacks.
    
    """
    pass

