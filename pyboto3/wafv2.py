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

def associate_web_acl(WebACLArn=None, ResourceArn=None):
    """
    Associates a Web ACL with a regional application resource, to protect the resource. A regional application can be an Application Load Balancer (ALB) or an API Gateway stage.
    For AWS CloudFront, don\'t use this call. Instead, use your CloudFront distribution configuration. To associate a Web ACL, in the CloudFront call UpdateDistribution , set the web ACL ID to the Amazon Resource Name (ARN) of the Web ACL. For information, see UpdateDistribution .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_web_acl(
        WebACLArn='string',
        ResourceArn='string'
    )
    
    
    :type WebACLArn: string
    :param WebACLArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the Web ACL that you want to associate with the resource.\n

    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource to associate with the web ACL.\nThe ARN must be in one of the following formats:\n\nFor an Application Load Balancer: ``arn:aws:elasticloadbalancing:region :account-id :loadbalancer/app/load-balancer-name /load-balancer-id ``\nFor an Amazon API Gateway stage: ``arn:aws:apigateway:region ::/restapis/api-id /stages/stage-name ``\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFNonexistentItemException
WAFV2.Client.exceptions.WAFUnavailableEntityException
WAFV2.Client.exceptions.WAFInvalidOperationException


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

def check_capacity(Scope=None, Rules=None):
    """
    Returns the web ACL capacity unit (WCU) requirements for a specified scope and set of rules. You can use this to check the capacity requirements for the rules you want to use in a  RuleGroup or  WebACL .
    AWS WAF uses WCUs to calculate and control the operating resources that are used to run your rules, rule groups, and web ACLs. AWS WAF calculates capacity differently for each rule type, to reflect the relative cost of each rule. Simple rules that cost little to run use fewer WCUs than more complex rules that use more processing power. Rule group capacity is fixed at creation, which helps users plan their web ACL WCU usage when they use a rule group. The WCU limit for web ACLs is 1,500.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.check_capacity(
        Scope='CLOUDFRONT'|'REGIONAL',
        Rules=[
            {
                'Name': 'string',
                'Priority': 123,
                'Statement': {
                    'ByteMatchStatement': {
                        'SearchString': b'bytes',
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {}
                            ,
                            'UriPath': {}
                            ,
                            'QueryString': {}
                            ,
                            'Body': {}
                            ,
                            'Method': {}
    
                        },
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ],
                        'PositionalConstraint': 'EXACTLY'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CONTAINS_WORD'
                    },
                    'SqliMatchStatement': {
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {}
                            ,
                            'UriPath': {}
                            ,
                            'QueryString': {}
                            ,
                            'Body': {}
                            ,
                            'Method': {}
    
                        },
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ]
                    },
                    'XssMatchStatement': {
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {}
                            ,
                            'UriPath': {}
                            ,
                            'QueryString': {}
                            ,
                            'Body': {}
                            ,
                            'Method': {}
    
                        },
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ]
                    },
                    'SizeConstraintStatement': {
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {}
                            ,
                            'UriPath': {}
                            ,
                            'QueryString': {}
                            ,
                            'Body': {}
                            ,
                            'Method': {}
    
                        },
                        'ComparisonOperator': 'EQ'|'NE'|'LE'|'LT'|'GE'|'GT',
                        'Size': 123,
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ]
                    },
                    'GeoMatchStatement': {
                        'CountryCodes': [
                            'AF'|'AX'|'AL'|'DZ'|'AS'|'AD'|'AO'|'AI'|'AQ'|'AG'|'AR'|'AM'|'AW'|'AU'|'AT'|'AZ'|'BS'|'BH'|'BD'|'BB'|'BY'|'BE'|'BZ'|'BJ'|'BM'|'BT'|'BO'|'BQ'|'BA'|'BW'|'BV'|'BR'|'IO'|'BN'|'BG'|'BF'|'BI'|'KH'|'CM'|'CA'|'CV'|'KY'|'CF'|'TD'|'CL'|'CN'|'CX'|'CC'|'CO'|'KM'|'CG'|'CD'|'CK'|'CR'|'CI'|'HR'|'CU'|'CW'|'CY'|'CZ'|'DK'|'DJ'|'DM'|'DO'|'EC'|'EG'|'SV'|'GQ'|'ER'|'EE'|'ET'|'FK'|'FO'|'FJ'|'FI'|'FR'|'GF'|'PF'|'TF'|'GA'|'GM'|'GE'|'DE'|'GH'|'GI'|'GR'|'GL'|'GD'|'GP'|'GU'|'GT'|'GG'|'GN'|'GW'|'GY'|'HT'|'HM'|'VA'|'HN'|'HK'|'HU'|'IS'|'IN'|'ID'|'IR'|'IQ'|'IE'|'IM'|'IL'|'IT'|'JM'|'JP'|'JE'|'JO'|'KZ'|'KE'|'KI'|'KP'|'KR'|'KW'|'KG'|'LA'|'LV'|'LB'|'LS'|'LR'|'LY'|'LI'|'LT'|'LU'|'MO'|'MK'|'MG'|'MW'|'MY'|'MV'|'ML'|'MT'|'MH'|'MQ'|'MR'|'MU'|'YT'|'MX'|'FM'|'MD'|'MC'|'MN'|'ME'|'MS'|'MA'|'MZ'|'MM'|'NA'|'NR'|'NP'|'NL'|'NC'|'NZ'|'NI'|'NE'|'NG'|'NU'|'NF'|'MP'|'NO'|'OM'|'PK'|'PW'|'PS'|'PA'|'PG'|'PY'|'PE'|'PH'|'PN'|'PL'|'PT'|'PR'|'QA'|'RE'|'RO'|'RU'|'RW'|'BL'|'SH'|'KN'|'LC'|'MF'|'PM'|'VC'|'WS'|'SM'|'ST'|'SA'|'SN'|'RS'|'SC'|'SL'|'SG'|'SX'|'SK'|'SI'|'SB'|'SO'|'ZA'|'GS'|'SS'|'ES'|'LK'|'SD'|'SR'|'SJ'|'SZ'|'SE'|'CH'|'SY'|'TW'|'TJ'|'TZ'|'TH'|'TL'|'TG'|'TK'|'TO'|'TT'|'TN'|'TR'|'TM'|'TC'|'TV'|'UG'|'UA'|'AE'|'GB'|'US'|'UM'|'UY'|'UZ'|'VU'|'VE'|'VN'|'VG'|'VI'|'WF'|'EH'|'YE'|'ZM'|'ZW',
                        ]
                    },
                    'RuleGroupReferenceStatement': {
                        'ARN': 'string',
                        'ExcludedRules': [
                            {
                                'Name': 'string'
                            },
                        ]
                    },
                    'IPSetReferenceStatement': {
                        'ARN': 'string'
                    },
                    'RegexPatternSetReferenceStatement': {
                        'ARN': 'string',
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {}
                            ,
                            'UriPath': {}
                            ,
                            'QueryString': {}
                            ,
                            'Body': {}
                            ,
                            'Method': {}
    
                        },
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ]
                    },
                    'RateBasedStatement': {
                        'Limit': 123,
                        'AggregateKeyType': 'IP',
                        'ScopeDownStatement': {'... recursive ...'}
                    },
                    'AndStatement': {
                        'Statements': [
                            {'... recursive ...'},
                        ]
                    },
                    'OrStatement': {
                        'Statements': [
                            {'... recursive ...'},
                        ]
                    },
                    'NotStatement': {
                        'Statement': {'... recursive ...'}
                    },
                    'ManagedRuleGroupStatement': {
                        'VendorName': 'string',
                        'Name': 'string',
                        'ExcludedRules': [
                            {
                                'Name': 'string'
                            },
                        ]
                    }
                },
                'Action': {
                    'Block': {}
                    ,
                    'Allow': {}
                    ,
                    'Count': {}
    
                },
                'OverrideAction': {
                    'Count': {}
                    ,
                    'None': {}
    
                },
                'VisibilityConfig': {
                    'SampledRequestsEnabled': True|False,
                    'CloudWatchMetricsEnabled': True|False,
                    'MetricName': 'string'
                }
            },
        ]
    )
    
    
    :type Scope: string
    :param Scope: [REQUIRED]\nSpecifies whether this is for an AWS CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB) or an API Gateway stage.\nTo work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:\n\nCLI - Specify the Region when you use the CloudFront scope: --scope=CLOUDFRONT --region=us-east-1 .\nAPI and SDKs - For all calls, use the Region endpoint us-east-1.\n\n

    :type Rules: list
    :param Rules: [REQUIRED]\nAn array of Rule that you\'re configuring to use in a rule group or web ACL.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nA single rule, which you can use in a WebACL or RuleGroup to identify web requests that you want to allow, block, or count. Each rule includes one top-level Statement that AWS WAF uses to identify matching web requests, and parameters that govern how AWS WAF handles them.\n\nName (string) -- [REQUIRED]The name of the rule. You can\'t change the name of a Rule after you create it.\n\nPriority (integer) -- [REQUIRED]If you define more than one Rule in a WebACL , AWS WAF evaluates each request against the Rules in order based on the value of Priority . AWS WAF processes rules with lower priority first. The priorities don\'t need to be consecutive, but they must all be different.\n\nStatement (dict) -- [REQUIRED]The AWS WAF processing statement for the rule, for example ByteMatchStatement or SizeConstraintStatement .\n\nByteMatchStatement (dict) --A rule statement that defines a string match search for AWS WAF to apply to web requests. The byte match statement provides the bytes to search for, the location in requests that you want AWS WAF to search, and other settings. The bytes to search for are typically a string that corresponds with ASCII characters. In the AWS WAF console and the developer guide, this is refered to as a string match statement.\n\nSearchString (bytes) -- [REQUIRED]A string value that you want AWS WAF to search for. AWS WAF searches only in the part of web requests that you designate for inspection in FieldToMatch . The maximum length of the value is 50 bytes.\nValid values depend on the component that you specify for inspection in FieldToMatch :\n\nMethod : The HTTP method that you want AWS WAF to search for. This indicates the type of operation specified in the request.\nUriPath : The value that you want AWS WAF to search for in the URI path, for example, /images/daily-ad.jpg .\n\nIf SearchString includes alphabetic characters A-Z and a-z, note that the value is case sensitive.\n\nIf you\'re using the AWS WAF API\nSpecify a base64-encoded version of the value. The maximum length of the value before you base64-encode it is 50 bytes.\nFor example, suppose the value of Type is HEADER and the value of Data is User-Agent . If you want to search the User-Agent header for the value BadBot , you base64-encode BadBot using MIME base64-encoding and include the resulting value, QmFkQm90 , in the value of SearchString .\n\nIf you\'re using the AWS CLI or one of the AWS SDKs\nThe value that you want AWS WAF to search for. The SDK automatically base64 encodes the value.\n\nFieldToMatch (dict) -- [REQUIRED]The part of a web request that you want AWS WAF to inspect. For more information, see FieldToMatch .\n\nSingleHeader (dict) --Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.\n\nName (string) -- [REQUIRED]The name of the query header to inspect.\n\n\n\nSingleQueryArgument (dict) --Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.\nThis is used only to indicate the web request component for AWS WAF to inspect, in the FieldToMatch specification.\n\nName (string) -- [REQUIRED]The name of the query argument to inspect.\n\n\n\nAllQueryArguments (dict) --Inspect all query arguments.\n\nUriPath (dict) --Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .\n\nQueryString (dict) --Inspect the query string. This is the part of a URL that appears after a ? character, if any.\n\nBody (dict) --Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.\nNote that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as ByteMatchStatement or RegexPatternSetReferenceStatement , with a SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.\n\nMethod (dict) --Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.\n\n\n\nTextTransformations (list) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nText transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.\n\nPriority (integer) -- [REQUIRED]Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.\n\nType (string) -- [REQUIRED]You can specify the following transformation types:\n\nCMD_LINE\nWhen you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:\n\nDelete the following characters: ' \' ^\nDelete spaces before the following characters: / (\nReplace the following characters with a space: , ;\nReplace multiple spaces with one space\nConvert uppercase letters (A-Z) to lowercase (a-z)\n\n\nCOMPRESS_WHITE_SPACE\nUse this option to replace the following characters with a space character (decimal 32):\n\nf, formfeed, decimal 12\nt, tab, decimal 9\nn, newline, decimal 10\nr, carriage return, decimal 13\nv, vertical tab, decimal 11\nnon-breaking space, decimal 160\n\n\nCOMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE\n\nUse this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:\n\nReplaces (ampersand)quot; with '\nReplaces (ampersand)nbsp; with a non-breaking space, decimal 160\nReplaces (ampersand)lt; with a 'less than' symbol\nReplaces (ampersand)gt; with >\nReplaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters\nReplaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters\n\n\nLOWERCASE\nUse this option to convert uppercase letters (A-Z) to lowercase (a-z).\n\nURL_DECODE\nUse this option to decode a URL-encoded value.\n\nNONE\nSpecify NONE if you don\'t want any text transformations.\n\n\n\n\n\nPositionalConstraint (string) -- [REQUIRED]The area within the portion of a web request that you want AWS WAF to search for SearchString . Valid values include the following:\n\nCONTAINS\nThe specified part of the web request must include the value of SearchString , but the location doesn\'t matter.\n\nCONTAINS_WORD\nThe specified part of the web request must include the value of SearchString , and SearchString must contain only alphanumeric characters or underscore (A-Z, a-z, 0-9, or _). In addition, SearchString must be a word, which means that both of the following are true:\n\nSearchString is at the beginning of the specified part of the web request or is preceded by a character other than an alphanumeric character or underscore (_). Examples include the value of a header and ;BadBot .\nSearchString is at the end of the specified part of the web request or is followed by a character other than an alphanumeric character or underscore (_), for example, BadBot; and -BadBot; .\n\n\nEXACTLY\nThe value of the specified part of the web request must exactly match the value of SearchString .\n\nSTARTS_WITH\nThe value of SearchString must appear at the beginning of the specified part of the web request.\n\nENDS_WITH\nThe value of SearchString must appear at the end of the specified part of the web request.\n\n\n\nSqliMatchStatement (dict) --Attackers sometimes insert malicious SQL code into web requests in an effort to extract data from your database. To allow or block web requests that appear to contain malicious SQL code, create one or more SQL injection match conditions. An SQL injection match condition identifies the part of web requests, such as the URI or the query string, that you want AWS WAF to inspect. Later in the process, when you create a web ACL, you specify whether to allow or block requests that appear to contain malicious SQL code.\n\nFieldToMatch (dict) -- [REQUIRED]The part of a web request that you want AWS WAF to inspect. For more information, see FieldToMatch .\n\nSingleHeader (dict) --Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.\n\nName (string) -- [REQUIRED]The name of the query header to inspect.\n\n\n\nSingleQueryArgument (dict) --Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.\nThis is used only to indicate the web request component for AWS WAF to inspect, in the FieldToMatch specification.\n\nName (string) -- [REQUIRED]The name of the query argument to inspect.\n\n\n\nAllQueryArguments (dict) --Inspect all query arguments.\n\nUriPath (dict) --Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .\n\nQueryString (dict) --Inspect the query string. This is the part of a URL that appears after a ? character, if any.\n\nBody (dict) --Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.\nNote that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as ByteMatchStatement or RegexPatternSetReferenceStatement , with a SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.\n\nMethod (dict) --Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.\n\n\n\nTextTransformations (list) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nText transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.\n\nPriority (integer) -- [REQUIRED]Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.\n\nType (string) -- [REQUIRED]You can specify the following transformation types:\n\nCMD_LINE\nWhen you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:\n\nDelete the following characters: ' \' ^\nDelete spaces before the following characters: / (\nReplace the following characters with a space: , ;\nReplace multiple spaces with one space\nConvert uppercase letters (A-Z) to lowercase (a-z)\n\n\nCOMPRESS_WHITE_SPACE\nUse this option to replace the following characters with a space character (decimal 32):\n\nf, formfeed, decimal 12\nt, tab, decimal 9\nn, newline, decimal 10\nr, carriage return, decimal 13\nv, vertical tab, decimal 11\nnon-breaking space, decimal 160\n\n\nCOMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE\n\nUse this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:\n\nReplaces (ampersand)quot; with '\nReplaces (ampersand)nbsp; with a non-breaking space, decimal 160\nReplaces (ampersand)lt; with a 'less than' symbol\nReplaces (ampersand)gt; with >\nReplaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters\nReplaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters\n\n\nLOWERCASE\nUse this option to convert uppercase letters (A-Z) to lowercase (a-z).\n\nURL_DECODE\nUse this option to decode a URL-encoded value.\n\nNONE\nSpecify NONE if you don\'t want any text transformations.\n\n\n\n\n\n\n\nXssMatchStatement (dict) --A rule statement that defines a cross-site scripting (XSS) match search for AWS WAF to apply to web requests. XSS attacks are those where the attacker uses vulnerabilities in a benign website as a vehicle to inject malicious client-site scripts into other legitimate web browsers. The XSS match statement provides the location in requests that you want AWS WAF to search and text transformations to use on the search area before AWS WAF searches for character sequences that are likely to be malicious strings.\n\nFieldToMatch (dict) -- [REQUIRED]The part of a web request that you want AWS WAF to inspect. For more information, see FieldToMatch .\n\nSingleHeader (dict) --Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.\n\nName (string) -- [REQUIRED]The name of the query header to inspect.\n\n\n\nSingleQueryArgument (dict) --Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.\nThis is used only to indicate the web request component for AWS WAF to inspect, in the FieldToMatch specification.\n\nName (string) -- [REQUIRED]The name of the query argument to inspect.\n\n\n\nAllQueryArguments (dict) --Inspect all query arguments.\n\nUriPath (dict) --Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .\n\nQueryString (dict) --Inspect the query string. This is the part of a URL that appears after a ? character, if any.\n\nBody (dict) --Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.\nNote that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as ByteMatchStatement or RegexPatternSetReferenceStatement , with a SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.\n\nMethod (dict) --Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.\n\n\n\nTextTransformations (list) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nText transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.\n\nPriority (integer) -- [REQUIRED]Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.\n\nType (string) -- [REQUIRED]You can specify the following transformation types:\n\nCMD_LINE\nWhen you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:\n\nDelete the following characters: ' \' ^\nDelete spaces before the following characters: / (\nReplace the following characters with a space: , ;\nReplace multiple spaces with one space\nConvert uppercase letters (A-Z) to lowercase (a-z)\n\n\nCOMPRESS_WHITE_SPACE\nUse this option to replace the following characters with a space character (decimal 32):\n\nf, formfeed, decimal 12\nt, tab, decimal 9\nn, newline, decimal 10\nr, carriage return, decimal 13\nv, vertical tab, decimal 11\nnon-breaking space, decimal 160\n\n\nCOMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE\n\nUse this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:\n\nReplaces (ampersand)quot; with '\nReplaces (ampersand)nbsp; with a non-breaking space, decimal 160\nReplaces (ampersand)lt; with a 'less than' symbol\nReplaces (ampersand)gt; with >\nReplaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters\nReplaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters\n\n\nLOWERCASE\nUse this option to convert uppercase letters (A-Z) to lowercase (a-z).\n\nURL_DECODE\nUse this option to decode a URL-encoded value.\n\nNONE\nSpecify NONE if you don\'t want any text transformations.\n\n\n\n\n\n\n\nSizeConstraintStatement (dict) --A rule statement that compares a number of bytes against the size of a request component, using a comparison operator, such as greater than (>) or less than (<). For example, you can use a size constraint statement to look for query strings that are longer than 100 bytes.\nIf you configure AWS WAF to inspect the request body, AWS WAF inspects only the first 8192 bytes (8 KB). If the request body for your web requests never exceeds 8192 bytes, you can create a size constraint condition and block requests that have a request body greater than 8192 bytes.\nIf you choose URI for the value of Part of the request to filter on, the slash (/) in the URI counts as one character. For example, the URI /logo.jpg is nine characters long.\n\nFieldToMatch (dict) -- [REQUIRED]The part of a web request that you want AWS WAF to inspect. For more information, see FieldToMatch .\n\nSingleHeader (dict) --Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.\n\nName (string) -- [REQUIRED]The name of the query header to inspect.\n\n\n\nSingleQueryArgument (dict) --Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.\nThis is used only to indicate the web request component for AWS WAF to inspect, in the FieldToMatch specification.\n\nName (string) -- [REQUIRED]The name of the query argument to inspect.\n\n\n\nAllQueryArguments (dict) --Inspect all query arguments.\n\nUriPath (dict) --Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .\n\nQueryString (dict) --Inspect the query string. This is the part of a URL that appears after a ? character, if any.\n\nBody (dict) --Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.\nNote that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as ByteMatchStatement or RegexPatternSetReferenceStatement , with a SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.\n\nMethod (dict) --Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.\n\n\n\nComparisonOperator (string) -- [REQUIRED]The operator to use to compare the request part to the size setting.\n\nSize (integer) -- [REQUIRED]The size, in byte, to compare to the request part, after any transformations.\n\nTextTransformations (list) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nText transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.\n\nPriority (integer) -- [REQUIRED]Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.\n\nType (string) -- [REQUIRED]You can specify the following transformation types:\n\nCMD_LINE\nWhen you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:\n\nDelete the following characters: ' \' ^\nDelete spaces before the following characters: / (\nReplace the following characters with a space: , ;\nReplace multiple spaces with one space\nConvert uppercase letters (A-Z) to lowercase (a-z)\n\n\nCOMPRESS_WHITE_SPACE\nUse this option to replace the following characters with a space character (decimal 32):\n\nf, formfeed, decimal 12\nt, tab, decimal 9\nn, newline, decimal 10\nr, carriage return, decimal 13\nv, vertical tab, decimal 11\nnon-breaking space, decimal 160\n\n\nCOMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE\n\nUse this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:\n\nReplaces (ampersand)quot; with '\nReplaces (ampersand)nbsp; with a non-breaking space, decimal 160\nReplaces (ampersand)lt; with a 'less than' symbol\nReplaces (ampersand)gt; with >\nReplaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters\nReplaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters\n\n\nLOWERCASE\nUse this option to convert uppercase letters (A-Z) to lowercase (a-z).\n\nURL_DECODE\nUse this option to decode a URL-encoded value.\n\nNONE\nSpecify NONE if you don\'t want any text transformations.\n\n\n\n\n\n\n\nGeoMatchStatement (dict) --A rule statement used to identify web requests based on country of origin.\n\nCountryCodes (list) --An array of two-character country codes, for example, [ 'US', 'CN' ] , from the alpha-2 country ISO codes of the ISO 3166 international standard.\n\n(string) --\n\n\n\n\nRuleGroupReferenceStatement (dict) --A rule statement used to run the rules that are defined in a RuleGroup . To use this, create a rule group with your rules, then provide the ARN of the rule group in this statement.\nYou cannot nest a RuleGroupReferenceStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.\n\nARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the entity.\n\nExcludedRules (list) --The names of rules that are in the referenced rule group, but that you want AWS WAF to exclude from processing for this rule statement.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nSpecifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.\n\nName (string) -- [REQUIRED]The name of the rule to exclude.\n\n\n\n\n\n\n\nIPSetReferenceStatement (dict) --A rule statement used to detect web requests coming from particular IP addresses or address ranges. To use this, create an IPSet that specifies the addresses you want to detect, then use the ARN of that set in this statement. To create an IP set, see CreateIPSet .\nEach IP set rule statement references an IP set. You create and maintain the set independent of your rules. This allows you to use the single set in multiple rules. When you update the referenced set, AWS WAF automatically updates all rules that reference it.\n\nARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the IPSet that this statement references.\n\n\n\nRegexPatternSetReferenceStatement (dict) --A rule statement used to search web request components for matches with regular expressions. To use this, create a RegexPatternSet that specifies the expressions that you want to detect, then use the ARN of that set in this statement. A web request matches the pattern set rule statement if the request component matches any of the patterns in the set. To create a regex pattern set, see CreateRegexPatternSet .\nEach regex pattern set rule statement references a regex pattern set. You create and maintain the set independent of your rules. This allows you to use the single set in multiple rules. When you update the referenced set, AWS WAF automatically updates all rules that reference it.\n\nARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the RegexPatternSet that this statement references.\n\nFieldToMatch (dict) -- [REQUIRED]The part of a web request that you want AWS WAF to inspect. For more information, see FieldToMatch .\n\nSingleHeader (dict) --Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.\n\nName (string) -- [REQUIRED]The name of the query header to inspect.\n\n\n\nSingleQueryArgument (dict) --Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.\nThis is used only to indicate the web request component for AWS WAF to inspect, in the FieldToMatch specification.\n\nName (string) -- [REQUIRED]The name of the query argument to inspect.\n\n\n\nAllQueryArguments (dict) --Inspect all query arguments.\n\nUriPath (dict) --Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .\n\nQueryString (dict) --Inspect the query string. This is the part of a URL that appears after a ? character, if any.\n\nBody (dict) --Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.\nNote that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as ByteMatchStatement or RegexPatternSetReferenceStatement , with a SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.\n\nMethod (dict) --Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.\n\n\n\nTextTransformations (list) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nText transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.\n\nPriority (integer) -- [REQUIRED]Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.\n\nType (string) -- [REQUIRED]You can specify the following transformation types:\n\nCMD_LINE\nWhen you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:\n\nDelete the following characters: ' \' ^\nDelete spaces before the following characters: / (\nReplace the following characters with a space: , ;\nReplace multiple spaces with one space\nConvert uppercase letters (A-Z) to lowercase (a-z)\n\n\nCOMPRESS_WHITE_SPACE\nUse this option to replace the following characters with a space character (decimal 32):\n\nf, formfeed, decimal 12\nt, tab, decimal 9\nn, newline, decimal 10\nr, carriage return, decimal 13\nv, vertical tab, decimal 11\nnon-breaking space, decimal 160\n\n\nCOMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE\n\nUse this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:\n\nReplaces (ampersand)quot; with '\nReplaces (ampersand)nbsp; with a non-breaking space, decimal 160\nReplaces (ampersand)lt; with a 'less than' symbol\nReplaces (ampersand)gt; with >\nReplaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters\nReplaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters\n\n\nLOWERCASE\nUse this option to convert uppercase letters (A-Z) to lowercase (a-z).\n\nURL_DECODE\nUse this option to decode a URL-encoded value.\n\nNONE\nSpecify NONE if you don\'t want any text transformations.\n\n\n\n\n\n\n\nRateBasedStatement (dict) --A rate-based rule tracks the rate of requests for each originating IP address, and triggers the rule action when the rate exceeds a limit that you specify on the number of requests in any 5-minute time span. You can use this to put a temporary block on requests from an IP address that is sending excessive requests.\nWhen the rule action triggers, AWS WAF blocks additional requests from the IP address until the request rate falls below the limit.\nYou can optionally nest another statement inside the rate-based statement, to narrow the scope of the rule so that it only counts requests that match the nested statement. For example, based on recent requests that you have seen from an attacker, you might create a rate-based rule with a nested AND rule statement that contains the following nested statements:\n\nAn IP match statement with an IP set that specified the address 192.0.2.44.\nA string match statement that searches in the User-Agent header for the string BadBot.\n\nIn this rate-based rule, you also define a rate limit. For this example, the rate limit is 1,000. Requests that meet both of the conditions in the statements are counted. If the count exceeds 1,000 requests per five minutes, the rule action triggers. Requests that do not meet both conditions are not counted towards the rate limit and are not affected by this rule.\nYou cannot nest a RateBasedStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.\n\nLimit (integer) -- [REQUIRED]The limit on requests per 5-minute period for a single originating IP address. If the statement includes a ScopDownStatement , this limit is applied only to the requests that match the statement.\n\nAggregateKeyType (string) -- [REQUIRED]Setting that indicates how to aggregate the request counts. Currently, you must set this to IP . The request counts are aggregated on IP addresses.\n\nScopeDownStatement (dict) --An optional nested statement that narrows the scope of the rate-based statement to matching web requests. This can be any nestable statement, and you can nest statements at any level below this scope-down statement.\n\n\n\nAndStatement (dict) --A logical rule statement used to combine other rule statements with AND logic. You provide more than one Statement within the AndStatement .\n\nStatements (list) -- [REQUIRED]The statements to combine with AND logic. You can use any statements that can be nested.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nThe processing guidance for a Rule , used by AWS WAF to determine whether a web request matches the rule.\n\n\n\n\n\nOrStatement (dict) --A logical rule statement used to combine other rule statements with OR logic. You provide more than one Statement within the OrStatement .\n\nStatements (list) -- [REQUIRED]The statements to combine with OR logic. You can use any statements that can be nested.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nThe processing guidance for a Rule , used by AWS WAF to determine whether a web request matches the rule.\n\n\n\n\n\nNotStatement (dict) --A logical rule statement used to negate the results of another rule statement. You provide one Statement within the NotStatement .\n\nStatement (dict) --The statement to negate. You can use any statement that can be nested.\n\n\n\nManagedRuleGroupStatement (dict) --A rule statement used to run the rules that are defined in a managed rule group. To use this, provide the vendor name and the name of the rule group in this statement. You can retrieve the required names by calling ListAvailableManagedRuleGroups .\nYou can\'t nest a ManagedRuleGroupStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.\n\nVendorName (string) -- [REQUIRED]The name of the managed rule group vendor. You use this, along with the rule group name, to identify the rule group.\n\nName (string) -- [REQUIRED]The name of the managed rule group. You use this, along with the vendor name, to identify the rule group.\n\nExcludedRules (list) --The rules whose actions are set to COUNT by the web ACL, regardless of the action that is set on the rule. This effectively excludes the rule from acting on web requests.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nSpecifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.\n\nName (string) -- [REQUIRED]The name of the rule to exclude.\n\n\n\n\n\n\n\n\n\nAction (dict) --The action that AWS WAF should take on a web request when it matches the rule statement. Settings at the web ACL level can override the rule action setting.\nThis is used only for rules whose statements do not reference a rule group. Rule statements that reference a rule group include RuleGroupReferenceStatement and ManagedRuleGroupStatement .\nYou must specify either this Action setting or the rule OverrideAction setting, but not both:\n\nIf the rule statement does not reference a rule group, use this rule action setting and not the rule override action setting.\nIf the rule statement references a rule group, use the override action setting and not this action setting.\n\n\nBlock (dict) --Instructs AWS WAF to block the web request.\n\nAllow (dict) --Instructs AWS WAF to allow the web request.\n\nCount (dict) --Instructs AWS WAF to count the web request and allow it.\n\n\n\nOverrideAction (dict) --The override action to apply to the rules in a rule group. Used only for rule statements that reference a rule group, like RuleGroupReferenceStatement and ManagedRuleGroupStatement .\nSet the override action to none to leave the rule actions in effect. Set it to count to only count matches, regardless of the rule action settings.\nIn a Rule , you must specify either this OverrideAction setting or the rule Action setting, but not both:\n\nIf the rule statement references a rule group, use this override action setting and not the action setting.\nIf the rule statement does not reference a rule group, use the rule action setting and not this rule override action setting.\n\n\nCount (dict) --Override the rule action setting to count.\n\nNone (dict) --Don\'t override the rule action setting.\n\n\n\nVisibilityConfig (dict) -- [REQUIRED]Defines and enables Amazon CloudWatch metrics and web request sample collection.\n\nSampledRequestsEnabled (boolean) -- [REQUIRED]A boolean indicating whether AWS WAF should store a sampling of the web requests that match the rules. You can view the sampled requests through the AWS WAF console.\n\nCloudWatchMetricsEnabled (boolean) -- [REQUIRED]A boolean indicating whether the associated resource sends metrics to CloudWatch. For the list of available metrics, see AWS WAF Metrics .\n\nMetricName (string) -- [REQUIRED]A name of the CloudWatch metric. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with length from one to 128 characters. It can\'t contain whitespace or metric names reserved for AWS WAF, for example 'All' and 'Default_Action.' You can\'t change a MetricName after you create a VisibilityConfig .\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Capacity': 123
}


Response Structure

(dict) --

Capacity (integer) --
The capacity required by the rules and scope.







Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFNonexistentItemException
WAFV2.Client.exceptions.WAFLimitsExceededException
WAFV2.Client.exceptions.WAFInvalidResourceException
WAFV2.Client.exceptions.WAFUnavailableEntityException
WAFV2.Client.exceptions.WAFSubscriptionNotFoundException


    :return: {
        'Capacity': 123
    }
    
    
    :returns: 
    WAFV2.Client.exceptions.WAFInternalErrorException
    WAFV2.Client.exceptions.WAFInvalidParameterException
    WAFV2.Client.exceptions.WAFNonexistentItemException
    WAFV2.Client.exceptions.WAFLimitsExceededException
    WAFV2.Client.exceptions.WAFInvalidResourceException
    WAFV2.Client.exceptions.WAFUnavailableEntityException
    WAFV2.Client.exceptions.WAFSubscriptionNotFoundException
    
    """
    pass

def create_ip_set(Name=None, Scope=None, Description=None, IPAddressVersion=None, Addresses=None, Tags=None):
    """
    Creates an  IPSet , which you use to identify web requests that originate from specific IP addresses or ranges of IP addresses. For example, if you\'re receiving a lot of requests from a ranges of IP addresses, you can configure AWS WAF to block them using an IPSet that lists those IP addresses.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_ip_set(
        Name='string',
        Scope='CLOUDFRONT'|'REGIONAL',
        Description='string',
        IPAddressVersion='IPV4'|'IPV6',
        Addresses=[
            'string',
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the IP set. You cannot change the name of an IPSet after you create it.\n

    :type Scope: string
    :param Scope: [REQUIRED]\nSpecifies whether this is for an AWS CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB) or an API Gateway stage.\nTo work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:\n\nCLI - Specify the Region when you use the CloudFront scope: --scope=CLOUDFRONT --region=us-east-1 .\nAPI and SDKs - For all calls, use the Region endpoint us-east-1.\n\n

    :type Description: string
    :param Description: A description of the IP set that helps with identification. You cannot change the description of an IP set after you create it.

    :type IPAddressVersion: string
    :param IPAddressVersion: [REQUIRED]\nSpecify IPV4 or IPV6.\n

    :type Addresses: list
    :param Addresses: [REQUIRED]\nContains an array of strings that specify one or more IP addresses or blocks of IP addresses in Classless Inter-Domain Routing (CIDR) notation. AWS WAF supports all address ranges for IP versions IPv4 and IPv6.\nExamples:\n\nTo configure AWS WAF to allow, block, or count requests that originated from the IP address 192.0.2.44, specify 192.0.2.44/32 .\nTo configure AWS WAF to allow, block, or count requests that originated from IP addresses from 192.0.2.0 to 192.0.2.255, specify 192.0.2.0/24 .\nTo configure AWS WAF to allow, block, or count requests that originated from the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify 1111:0000:0000:0000:0000:0000:0000:0111/128 .\nTo configure AWS WAF to allow, block, or count requests that originated from IP addresses 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify 1111:0000:0000:0000:0000:0000:0000:0000/64 .\n\nFor more information about CIDR notation, see the Wikipedia entry Classless Inter-Domain Routing .\n\n(string) --\n\n

    :type Tags: list
    :param Tags: An array of key:value pairs to associate with the resource.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nA collection of key:value pairs associated with an AWS resource. The key:value pair can be anything you define. Typically, the tag key represents a category (such as 'environment') and the tag value represents a specific value within that category (such as 'test,' 'development,' or 'production'). You can add up to 50 tags to each AWS resource.\n\nKey (string) -- [REQUIRED]Part of the key:value pair that defines a tag. You can use a tag key to describe a category of information, such as 'customer.' Tag keys are case-sensitive.\n\nValue (string) -- [REQUIRED]Part of the key:value pair that defines a tag. You can use a tag value to describe a specific value within a category, such as 'companyA' or 'companyB.' Tag values are case-sensitive.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Summary': {
        'Name': 'string',
        'Id': 'string',
        'Description': 'string',
        'LockToken': 'string',
        'ARN': 'string'
    }
}


Response Structure

(dict) --

Summary (dict) --
High-level information about an  IPSet , returned by operations like create and list. This provides information like the ID, that you can use to retrieve and manage an IPSet , and the ARN, that you provide to the  IPSetReferenceStatement to use the address set in a  Rule .

Name (string) --
The name of the IP set. You cannot change the name of an IPSet after you create it.

Id (string) --
A unique identifier for the set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.

Description (string) --
A description of the IP set that helps with identification. You cannot change the description of an IP set after you create it.

LockToken (string) --
A token used for optimistic locking. AWS WAF returns a token to your get and list requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like update and delete. AWS WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a WAFOptimisticLockException . If this happens, perform another get, and use the new token returned by that operation.

ARN (string) --
The Amazon Resource Name (ARN) of the entity.









Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFDuplicateItemException
WAFV2.Client.exceptions.WAFOptimisticLockException
WAFV2.Client.exceptions.WAFLimitsExceededException
WAFV2.Client.exceptions.WAFTagOperationException
WAFV2.Client.exceptions.WAFTagOperationInternalErrorException
WAFV2.Client.exceptions.WAFInvalidOperationException


    :return: {
        'Summary': {
            'Name': 'string',
            'Id': 'string',
            'Description': 'string',
            'LockToken': 'string',
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    WAFV2.Client.exceptions.WAFInternalErrorException
    WAFV2.Client.exceptions.WAFInvalidParameterException
    WAFV2.Client.exceptions.WAFDuplicateItemException
    WAFV2.Client.exceptions.WAFOptimisticLockException
    WAFV2.Client.exceptions.WAFLimitsExceededException
    WAFV2.Client.exceptions.WAFTagOperationException
    WAFV2.Client.exceptions.WAFTagOperationInternalErrorException
    WAFV2.Client.exceptions.WAFInvalidOperationException
    
    """
    pass

def create_regex_pattern_set(Name=None, Scope=None, Description=None, RegularExpressionList=None, Tags=None):
    """
    Creates a  RegexPatternSet , which you reference in a  RegexPatternSetReferenceStatement , to have AWS WAF inspect a web request component for the specified patterns.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_regex_pattern_set(
        Name='string',
        Scope='CLOUDFRONT'|'REGIONAL',
        Description='string',
        RegularExpressionList=[
            {
                'RegexString': 'string'
            },
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the set. You cannot change the name after you create the set.\n

    :type Scope: string
    :param Scope: [REQUIRED]\nSpecifies whether this is for an AWS CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB) or an API Gateway stage.\nTo work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:\n\nCLI - Specify the Region when you use the CloudFront scope: --scope=CLOUDFRONT --region=us-east-1 .\nAPI and SDKs - For all calls, use the Region endpoint us-east-1.\n\n

    :type Description: string
    :param Description: A description of the set that helps with identification. You cannot change the description of a set after you create it.

    :type RegularExpressionList: list
    :param RegularExpressionList: [REQUIRED]\nArray of regular expression strings.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nA single regular expression. This is used in a RegexPatternSet .\n\nRegexString (string) --The string representing the regular expression.\n\n\n\n\n

    :type Tags: list
    :param Tags: An array of key:value pairs to associate with the resource.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nA collection of key:value pairs associated with an AWS resource. The key:value pair can be anything you define. Typically, the tag key represents a category (such as 'environment') and the tag value represents a specific value within that category (such as 'test,' 'development,' or 'production'). You can add up to 50 tags to each AWS resource.\n\nKey (string) -- [REQUIRED]Part of the key:value pair that defines a tag. You can use a tag key to describe a category of information, such as 'customer.' Tag keys are case-sensitive.\n\nValue (string) -- [REQUIRED]Part of the key:value pair that defines a tag. You can use a tag value to describe a specific value within a category, such as 'companyA' or 'companyB.' Tag values are case-sensitive.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Summary': {
        'Name': 'string',
        'Id': 'string',
        'Description': 'string',
        'LockToken': 'string',
        'ARN': 'string'
    }
}


Response Structure

(dict) --

Summary (dict) --
High-level information about a  RegexPatternSet , returned by operations like create and list. This provides information like the ID, that you can use to retrieve and manage a RegexPatternSet , and the ARN, that you provide to the  RegexPatternSetReferenceStatement to use the pattern set in a  Rule .

Name (string) --
The name of the data type instance. You cannot change the name after you create the instance.

Id (string) --
A unique identifier for the set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.

Description (string) --
A description of the set that helps with identification. You cannot change the description of a set after you create it.

LockToken (string) --
A token used for optimistic locking. AWS WAF returns a token to your get and list requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like update and delete. AWS WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a WAFOptimisticLockException . If this happens, perform another get, and use the new token returned by that operation.

ARN (string) --
The Amazon Resource Name (ARN) of the entity.









Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFDuplicateItemException
WAFV2.Client.exceptions.WAFOptimisticLockException
WAFV2.Client.exceptions.WAFLimitsExceededException
WAFV2.Client.exceptions.WAFTagOperationException
WAFV2.Client.exceptions.WAFTagOperationInternalErrorException
WAFV2.Client.exceptions.WAFInvalidOperationException


    :return: {
        'Summary': {
            'Name': 'string',
            'Id': 'string',
            'Description': 'string',
            'LockToken': 'string',
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    WAFV2.Client.exceptions.WAFInternalErrorException
    WAFV2.Client.exceptions.WAFInvalidParameterException
    WAFV2.Client.exceptions.WAFDuplicateItemException
    WAFV2.Client.exceptions.WAFOptimisticLockException
    WAFV2.Client.exceptions.WAFLimitsExceededException
    WAFV2.Client.exceptions.WAFTagOperationException
    WAFV2.Client.exceptions.WAFTagOperationInternalErrorException
    WAFV2.Client.exceptions.WAFInvalidOperationException
    
    """
    pass

def create_rule_group(Name=None, Scope=None, Capacity=None, Description=None, Rules=None, VisibilityConfig=None, Tags=None):
    """
    Creates a  RuleGroup per the specifications provided.
    A rule group defines a collection of rules to inspect and control web requests that you can use in a  WebACL . When you create a rule group, you define an immutable capacity limit. If you update a rule group, you must stay within the capacity. This allows others to reuse the rule group with confidence in its capacity requirements.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_rule_group(
        Name='string',
        Scope='CLOUDFRONT'|'REGIONAL',
        Capacity=123,
        Description='string',
        Rules=[
            {
                'Name': 'string',
                'Priority': 123,
                'Statement': {
                    'ByteMatchStatement': {
                        'SearchString': b'bytes',
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {}
                            ,
                            'UriPath': {}
                            ,
                            'QueryString': {}
                            ,
                            'Body': {}
                            ,
                            'Method': {}
    
                        },
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ],
                        'PositionalConstraint': 'EXACTLY'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CONTAINS_WORD'
                    },
                    'SqliMatchStatement': {
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {}
                            ,
                            'UriPath': {}
                            ,
                            'QueryString': {}
                            ,
                            'Body': {}
                            ,
                            'Method': {}
    
                        },
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ]
                    },
                    'XssMatchStatement': {
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {}
                            ,
                            'UriPath': {}
                            ,
                            'QueryString': {}
                            ,
                            'Body': {}
                            ,
                            'Method': {}
    
                        },
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ]
                    },
                    'SizeConstraintStatement': {
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {}
                            ,
                            'UriPath': {}
                            ,
                            'QueryString': {}
                            ,
                            'Body': {}
                            ,
                            'Method': {}
    
                        },
                        'ComparisonOperator': 'EQ'|'NE'|'LE'|'LT'|'GE'|'GT',
                        'Size': 123,
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ]
                    },
                    'GeoMatchStatement': {
                        'CountryCodes': [
                            'AF'|'AX'|'AL'|'DZ'|'AS'|'AD'|'AO'|'AI'|'AQ'|'AG'|'AR'|'AM'|'AW'|'AU'|'AT'|'AZ'|'BS'|'BH'|'BD'|'BB'|'BY'|'BE'|'BZ'|'BJ'|'BM'|'BT'|'BO'|'BQ'|'BA'|'BW'|'BV'|'BR'|'IO'|'BN'|'BG'|'BF'|'BI'|'KH'|'CM'|'CA'|'CV'|'KY'|'CF'|'TD'|'CL'|'CN'|'CX'|'CC'|'CO'|'KM'|'CG'|'CD'|'CK'|'CR'|'CI'|'HR'|'CU'|'CW'|'CY'|'CZ'|'DK'|'DJ'|'DM'|'DO'|'EC'|'EG'|'SV'|'GQ'|'ER'|'EE'|'ET'|'FK'|'FO'|'FJ'|'FI'|'FR'|'GF'|'PF'|'TF'|'GA'|'GM'|'GE'|'DE'|'GH'|'GI'|'GR'|'GL'|'GD'|'GP'|'GU'|'GT'|'GG'|'GN'|'GW'|'GY'|'HT'|'HM'|'VA'|'HN'|'HK'|'HU'|'IS'|'IN'|'ID'|'IR'|'IQ'|'IE'|'IM'|'IL'|'IT'|'JM'|'JP'|'JE'|'JO'|'KZ'|'KE'|'KI'|'KP'|'KR'|'KW'|'KG'|'LA'|'LV'|'LB'|'LS'|'LR'|'LY'|'LI'|'LT'|'LU'|'MO'|'MK'|'MG'|'MW'|'MY'|'MV'|'ML'|'MT'|'MH'|'MQ'|'MR'|'MU'|'YT'|'MX'|'FM'|'MD'|'MC'|'MN'|'ME'|'MS'|'MA'|'MZ'|'MM'|'NA'|'NR'|'NP'|'NL'|'NC'|'NZ'|'NI'|'NE'|'NG'|'NU'|'NF'|'MP'|'NO'|'OM'|'PK'|'PW'|'PS'|'PA'|'PG'|'PY'|'PE'|'PH'|'PN'|'PL'|'PT'|'PR'|'QA'|'RE'|'RO'|'RU'|'RW'|'BL'|'SH'|'KN'|'LC'|'MF'|'PM'|'VC'|'WS'|'SM'|'ST'|'SA'|'SN'|'RS'|'SC'|'SL'|'SG'|'SX'|'SK'|'SI'|'SB'|'SO'|'ZA'|'GS'|'SS'|'ES'|'LK'|'SD'|'SR'|'SJ'|'SZ'|'SE'|'CH'|'SY'|'TW'|'TJ'|'TZ'|'TH'|'TL'|'TG'|'TK'|'TO'|'TT'|'TN'|'TR'|'TM'|'TC'|'TV'|'UG'|'UA'|'AE'|'GB'|'US'|'UM'|'UY'|'UZ'|'VU'|'VE'|'VN'|'VG'|'VI'|'WF'|'EH'|'YE'|'ZM'|'ZW',
                        ]
                    },
                    'RuleGroupReferenceStatement': {
                        'ARN': 'string',
                        'ExcludedRules': [
                            {
                                'Name': 'string'
                            },
                        ]
                    },
                    'IPSetReferenceStatement': {
                        'ARN': 'string'
                    },
                    'RegexPatternSetReferenceStatement': {
                        'ARN': 'string',
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {}
                            ,
                            'UriPath': {}
                            ,
                            'QueryString': {}
                            ,
                            'Body': {}
                            ,
                            'Method': {}
    
                        },
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ]
                    },
                    'RateBasedStatement': {
                        'Limit': 123,
                        'AggregateKeyType': 'IP',
                        'ScopeDownStatement': {'... recursive ...'}
                    },
                    'AndStatement': {
                        'Statements': [
                            {'... recursive ...'},
                        ]
                    },
                    'OrStatement': {
                        'Statements': [
                            {'... recursive ...'},
                        ]
                    },
                    'NotStatement': {
                        'Statement': {'... recursive ...'}
                    },
                    'ManagedRuleGroupStatement': {
                        'VendorName': 'string',
                        'Name': 'string',
                        'ExcludedRules': [
                            {
                                'Name': 'string'
                            },
                        ]
                    }
                },
                'Action': {
                    'Block': {}
                    ,
                    'Allow': {}
                    ,
                    'Count': {}
    
                },
                'OverrideAction': {
                    'Count': {}
                    ,
                    'None': {}
    
                },
                'VisibilityConfig': {
                    'SampledRequestsEnabled': True|False,
                    'CloudWatchMetricsEnabled': True|False,
                    'MetricName': 'string'
                }
            },
        ],
        VisibilityConfig={
            'SampledRequestsEnabled': True|False,
            'CloudWatchMetricsEnabled': True|False,
            'MetricName': 'string'
        },
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the rule group. You cannot change the name of a rule group after you create it.\n

    :type Scope: string
    :param Scope: [REQUIRED]\nSpecifies whether this is for an AWS CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB) or an API Gateway stage.\nTo work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:\n\nCLI - Specify the Region when you use the CloudFront scope: --scope=CLOUDFRONT --region=us-east-1 .\nAPI and SDKs - For all calls, use the Region endpoint us-east-1.\n\n

    :type Capacity: integer
    :param Capacity: [REQUIRED]\nThe web ACL capacity units (WCUs) required for this rule group.\nWhen you create your own rule group, you define this, and you cannot change it after creation. When you add or modify the rules in a rule group, AWS WAF enforces this limit. You can check the capacity for a set of rules using CheckCapacity .\nAWS WAF uses WCUs to calculate and control the operating resources that are used to run your rules, rule groups, and web ACLs. AWS WAF calculates capacity differently for each rule type, to reflect the relative cost of each rule. Simple rules that cost little to run use fewer WCUs than more complex rules that use more processing power. Rule group capacity is fixed at creation, which helps users plan their web ACL WCU usage when they use a rule group. The WCU limit for web ACLs is 1,500.\n

    :type Description: string
    :param Description: A description of the rule group that helps with identification. You cannot change the description of a rule group after you create it.

    :type Rules: list
    :param Rules: The Rule statements used to identify the web requests that you want to allow, block, or count. Each rule includes one top-level statement that AWS WAF uses to identify matching web requests, and parameters that govern how AWS WAF handles them.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nA single rule, which you can use in a WebACL or RuleGroup to identify web requests that you want to allow, block, or count. Each rule includes one top-level Statement that AWS WAF uses to identify matching web requests, and parameters that govern how AWS WAF handles them.\n\nName (string) -- [REQUIRED]The name of the rule. You can\'t change the name of a Rule after you create it.\n\nPriority (integer) -- [REQUIRED]If you define more than one Rule in a WebACL , AWS WAF evaluates each request against the Rules in order based on the value of Priority . AWS WAF processes rules with lower priority first. The priorities don\'t need to be consecutive, but they must all be different.\n\nStatement (dict) -- [REQUIRED]The AWS WAF processing statement for the rule, for example ByteMatchStatement or SizeConstraintStatement .\n\nByteMatchStatement (dict) --A rule statement that defines a string match search for AWS WAF to apply to web requests. The byte match statement provides the bytes to search for, the location in requests that you want AWS WAF to search, and other settings. The bytes to search for are typically a string that corresponds with ASCII characters. In the AWS WAF console and the developer guide, this is refered to as a string match statement.\n\nSearchString (bytes) -- [REQUIRED]A string value that you want AWS WAF to search for. AWS WAF searches only in the part of web requests that you designate for inspection in FieldToMatch . The maximum length of the value is 50 bytes.\nValid values depend on the component that you specify for inspection in FieldToMatch :\n\nMethod : The HTTP method that you want AWS WAF to search for. This indicates the type of operation specified in the request.\nUriPath : The value that you want AWS WAF to search for in the URI path, for example, /images/daily-ad.jpg .\n\nIf SearchString includes alphabetic characters A-Z and a-z, note that the value is case sensitive.\n\nIf you\'re using the AWS WAF API\nSpecify a base64-encoded version of the value. The maximum length of the value before you base64-encode it is 50 bytes.\nFor example, suppose the value of Type is HEADER and the value of Data is User-Agent . If you want to search the User-Agent header for the value BadBot , you base64-encode BadBot using MIME base64-encoding and include the resulting value, QmFkQm90 , in the value of SearchString .\n\nIf you\'re using the AWS CLI or one of the AWS SDKs\nThe value that you want AWS WAF to search for. The SDK automatically base64 encodes the value.\n\nFieldToMatch (dict) -- [REQUIRED]The part of a web request that you want AWS WAF to inspect. For more information, see FieldToMatch .\n\nSingleHeader (dict) --Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.\n\nName (string) -- [REQUIRED]The name of the query header to inspect.\n\n\n\nSingleQueryArgument (dict) --Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.\nThis is used only to indicate the web request component for AWS WAF to inspect, in the FieldToMatch specification.\n\nName (string) -- [REQUIRED]The name of the query argument to inspect.\n\n\n\nAllQueryArguments (dict) --Inspect all query arguments.\n\nUriPath (dict) --Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .\n\nQueryString (dict) --Inspect the query string. This is the part of a URL that appears after a ? character, if any.\n\nBody (dict) --Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.\nNote that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as ByteMatchStatement or RegexPatternSetReferenceStatement , with a SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.\n\nMethod (dict) --Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.\n\n\n\nTextTransformations (list) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nText transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.\n\nPriority (integer) -- [REQUIRED]Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.\n\nType (string) -- [REQUIRED]You can specify the following transformation types:\n\nCMD_LINE\nWhen you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:\n\nDelete the following characters: ' \' ^\nDelete spaces before the following characters: / (\nReplace the following characters with a space: , ;\nReplace multiple spaces with one space\nConvert uppercase letters (A-Z) to lowercase (a-z)\n\n\nCOMPRESS_WHITE_SPACE\nUse this option to replace the following characters with a space character (decimal 32):\n\nf, formfeed, decimal 12\nt, tab, decimal 9\nn, newline, decimal 10\nr, carriage return, decimal 13\nv, vertical tab, decimal 11\nnon-breaking space, decimal 160\n\n\nCOMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE\n\nUse this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:\n\nReplaces (ampersand)quot; with '\nReplaces (ampersand)nbsp; with a non-breaking space, decimal 160\nReplaces (ampersand)lt; with a 'less than' symbol\nReplaces (ampersand)gt; with >\nReplaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters\nReplaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters\n\n\nLOWERCASE\nUse this option to convert uppercase letters (A-Z) to lowercase (a-z).\n\nURL_DECODE\nUse this option to decode a URL-encoded value.\n\nNONE\nSpecify NONE if you don\'t want any text transformations.\n\n\n\n\n\nPositionalConstraint (string) -- [REQUIRED]The area within the portion of a web request that you want AWS WAF to search for SearchString . Valid values include the following:\n\nCONTAINS\nThe specified part of the web request must include the value of SearchString , but the location doesn\'t matter.\n\nCONTAINS_WORD\nThe specified part of the web request must include the value of SearchString , and SearchString must contain only alphanumeric characters or underscore (A-Z, a-z, 0-9, or _). In addition, SearchString must be a word, which means that both of the following are true:\n\nSearchString is at the beginning of the specified part of the web request or is preceded by a character other than an alphanumeric character or underscore (_). Examples include the value of a header and ;BadBot .\nSearchString is at the end of the specified part of the web request or is followed by a character other than an alphanumeric character or underscore (_), for example, BadBot; and -BadBot; .\n\n\nEXACTLY\nThe value of the specified part of the web request must exactly match the value of SearchString .\n\nSTARTS_WITH\nThe value of SearchString must appear at the beginning of the specified part of the web request.\n\nENDS_WITH\nThe value of SearchString must appear at the end of the specified part of the web request.\n\n\n\nSqliMatchStatement (dict) --Attackers sometimes insert malicious SQL code into web requests in an effort to extract data from your database. To allow or block web requests that appear to contain malicious SQL code, create one or more SQL injection match conditions. An SQL injection match condition identifies the part of web requests, such as the URI or the query string, that you want AWS WAF to inspect. Later in the process, when you create a web ACL, you specify whether to allow or block requests that appear to contain malicious SQL code.\n\nFieldToMatch (dict) -- [REQUIRED]The part of a web request that you want AWS WAF to inspect. For more information, see FieldToMatch .\n\nSingleHeader (dict) --Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.\n\nName (string) -- [REQUIRED]The name of the query header to inspect.\n\n\n\nSingleQueryArgument (dict) --Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.\nThis is used only to indicate the web request component for AWS WAF to inspect, in the FieldToMatch specification.\n\nName (string) -- [REQUIRED]The name of the query argument to inspect.\n\n\n\nAllQueryArguments (dict) --Inspect all query arguments.\n\nUriPath (dict) --Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .\n\nQueryString (dict) --Inspect the query string. This is the part of a URL that appears after a ? character, if any.\n\nBody (dict) --Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.\nNote that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as ByteMatchStatement or RegexPatternSetReferenceStatement , with a SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.\n\nMethod (dict) --Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.\n\n\n\nTextTransformations (list) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nText transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.\n\nPriority (integer) -- [REQUIRED]Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.\n\nType (string) -- [REQUIRED]You can specify the following transformation types:\n\nCMD_LINE\nWhen you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:\n\nDelete the following characters: ' \' ^\nDelete spaces before the following characters: / (\nReplace the following characters with a space: , ;\nReplace multiple spaces with one space\nConvert uppercase letters (A-Z) to lowercase (a-z)\n\n\nCOMPRESS_WHITE_SPACE\nUse this option to replace the following characters with a space character (decimal 32):\n\nf, formfeed, decimal 12\nt, tab, decimal 9\nn, newline, decimal 10\nr, carriage return, decimal 13\nv, vertical tab, decimal 11\nnon-breaking space, decimal 160\n\n\nCOMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE\n\nUse this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:\n\nReplaces (ampersand)quot; with '\nReplaces (ampersand)nbsp; with a non-breaking space, decimal 160\nReplaces (ampersand)lt; with a 'less than' symbol\nReplaces (ampersand)gt; with >\nReplaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters\nReplaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters\n\n\nLOWERCASE\nUse this option to convert uppercase letters (A-Z) to lowercase (a-z).\n\nURL_DECODE\nUse this option to decode a URL-encoded value.\n\nNONE\nSpecify NONE if you don\'t want any text transformations.\n\n\n\n\n\n\n\nXssMatchStatement (dict) --A rule statement that defines a cross-site scripting (XSS) match search for AWS WAF to apply to web requests. XSS attacks are those where the attacker uses vulnerabilities in a benign website as a vehicle to inject malicious client-site scripts into other legitimate web browsers. The XSS match statement provides the location in requests that you want AWS WAF to search and text transformations to use on the search area before AWS WAF searches for character sequences that are likely to be malicious strings.\n\nFieldToMatch (dict) -- [REQUIRED]The part of a web request that you want AWS WAF to inspect. For more information, see FieldToMatch .\n\nSingleHeader (dict) --Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.\n\nName (string) -- [REQUIRED]The name of the query header to inspect.\n\n\n\nSingleQueryArgument (dict) --Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.\nThis is used only to indicate the web request component for AWS WAF to inspect, in the FieldToMatch specification.\n\nName (string) -- [REQUIRED]The name of the query argument to inspect.\n\n\n\nAllQueryArguments (dict) --Inspect all query arguments.\n\nUriPath (dict) --Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .\n\nQueryString (dict) --Inspect the query string. This is the part of a URL that appears after a ? character, if any.\n\nBody (dict) --Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.\nNote that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as ByteMatchStatement or RegexPatternSetReferenceStatement , with a SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.\n\nMethod (dict) --Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.\n\n\n\nTextTransformations (list) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nText transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.\n\nPriority (integer) -- [REQUIRED]Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.\n\nType (string) -- [REQUIRED]You can specify the following transformation types:\n\nCMD_LINE\nWhen you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:\n\nDelete the following characters: ' \' ^\nDelete spaces before the following characters: / (\nReplace the following characters with a space: , ;\nReplace multiple spaces with one space\nConvert uppercase letters (A-Z) to lowercase (a-z)\n\n\nCOMPRESS_WHITE_SPACE\nUse this option to replace the following characters with a space character (decimal 32):\n\nf, formfeed, decimal 12\nt, tab, decimal 9\nn, newline, decimal 10\nr, carriage return, decimal 13\nv, vertical tab, decimal 11\nnon-breaking space, decimal 160\n\n\nCOMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE\n\nUse this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:\n\nReplaces (ampersand)quot; with '\nReplaces (ampersand)nbsp; with a non-breaking space, decimal 160\nReplaces (ampersand)lt; with a 'less than' symbol\nReplaces (ampersand)gt; with >\nReplaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters\nReplaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters\n\n\nLOWERCASE\nUse this option to convert uppercase letters (A-Z) to lowercase (a-z).\n\nURL_DECODE\nUse this option to decode a URL-encoded value.\n\nNONE\nSpecify NONE if you don\'t want any text transformations.\n\n\n\n\n\n\n\nSizeConstraintStatement (dict) --A rule statement that compares a number of bytes against the size of a request component, using a comparison operator, such as greater than (>) or less than (<). For example, you can use a size constraint statement to look for query strings that are longer than 100 bytes.\nIf you configure AWS WAF to inspect the request body, AWS WAF inspects only the first 8192 bytes (8 KB). If the request body for your web requests never exceeds 8192 bytes, you can create a size constraint condition and block requests that have a request body greater than 8192 bytes.\nIf you choose URI for the value of Part of the request to filter on, the slash (/) in the URI counts as one character. For example, the URI /logo.jpg is nine characters long.\n\nFieldToMatch (dict) -- [REQUIRED]The part of a web request that you want AWS WAF to inspect. For more information, see FieldToMatch .\n\nSingleHeader (dict) --Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.\n\nName (string) -- [REQUIRED]The name of the query header to inspect.\n\n\n\nSingleQueryArgument (dict) --Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.\nThis is used only to indicate the web request component for AWS WAF to inspect, in the FieldToMatch specification.\n\nName (string) -- [REQUIRED]The name of the query argument to inspect.\n\n\n\nAllQueryArguments (dict) --Inspect all query arguments.\n\nUriPath (dict) --Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .\n\nQueryString (dict) --Inspect the query string. This is the part of a URL that appears after a ? character, if any.\n\nBody (dict) --Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.\nNote that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as ByteMatchStatement or RegexPatternSetReferenceStatement , with a SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.\n\nMethod (dict) --Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.\n\n\n\nComparisonOperator (string) -- [REQUIRED]The operator to use to compare the request part to the size setting.\n\nSize (integer) -- [REQUIRED]The size, in byte, to compare to the request part, after any transformations.\n\nTextTransformations (list) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nText transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.\n\nPriority (integer) -- [REQUIRED]Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.\n\nType (string) -- [REQUIRED]You can specify the following transformation types:\n\nCMD_LINE\nWhen you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:\n\nDelete the following characters: ' \' ^\nDelete spaces before the following characters: / (\nReplace the following characters with a space: , ;\nReplace multiple spaces with one space\nConvert uppercase letters (A-Z) to lowercase (a-z)\n\n\nCOMPRESS_WHITE_SPACE\nUse this option to replace the following characters with a space character (decimal 32):\n\nf, formfeed, decimal 12\nt, tab, decimal 9\nn, newline, decimal 10\nr, carriage return, decimal 13\nv, vertical tab, decimal 11\nnon-breaking space, decimal 160\n\n\nCOMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE\n\nUse this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:\n\nReplaces (ampersand)quot; with '\nReplaces (ampersand)nbsp; with a non-breaking space, decimal 160\nReplaces (ampersand)lt; with a 'less than' symbol\nReplaces (ampersand)gt; with >\nReplaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters\nReplaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters\n\n\nLOWERCASE\nUse this option to convert uppercase letters (A-Z) to lowercase (a-z).\n\nURL_DECODE\nUse this option to decode a URL-encoded value.\n\nNONE\nSpecify NONE if you don\'t want any text transformations.\n\n\n\n\n\n\n\nGeoMatchStatement (dict) --A rule statement used to identify web requests based on country of origin.\n\nCountryCodes (list) --An array of two-character country codes, for example, [ 'US', 'CN' ] , from the alpha-2 country ISO codes of the ISO 3166 international standard.\n\n(string) --\n\n\n\n\nRuleGroupReferenceStatement (dict) --A rule statement used to run the rules that are defined in a RuleGroup . To use this, create a rule group with your rules, then provide the ARN of the rule group in this statement.\nYou cannot nest a RuleGroupReferenceStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.\n\nARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the entity.\n\nExcludedRules (list) --The names of rules that are in the referenced rule group, but that you want AWS WAF to exclude from processing for this rule statement.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nSpecifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.\n\nName (string) -- [REQUIRED]The name of the rule to exclude.\n\n\n\n\n\n\n\nIPSetReferenceStatement (dict) --A rule statement used to detect web requests coming from particular IP addresses or address ranges. To use this, create an IPSet that specifies the addresses you want to detect, then use the ARN of that set in this statement. To create an IP set, see CreateIPSet .\nEach IP set rule statement references an IP set. You create and maintain the set independent of your rules. This allows you to use the single set in multiple rules. When you update the referenced set, AWS WAF automatically updates all rules that reference it.\n\nARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the IPSet that this statement references.\n\n\n\nRegexPatternSetReferenceStatement (dict) --A rule statement used to search web request components for matches with regular expressions. To use this, create a RegexPatternSet that specifies the expressions that you want to detect, then use the ARN of that set in this statement. A web request matches the pattern set rule statement if the request component matches any of the patterns in the set. To create a regex pattern set, see CreateRegexPatternSet .\nEach regex pattern set rule statement references a regex pattern set. You create and maintain the set independent of your rules. This allows you to use the single set in multiple rules. When you update the referenced set, AWS WAF automatically updates all rules that reference it.\n\nARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the RegexPatternSet that this statement references.\n\nFieldToMatch (dict) -- [REQUIRED]The part of a web request that you want AWS WAF to inspect. For more information, see FieldToMatch .\n\nSingleHeader (dict) --Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.\n\nName (string) -- [REQUIRED]The name of the query header to inspect.\n\n\n\nSingleQueryArgument (dict) --Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.\nThis is used only to indicate the web request component for AWS WAF to inspect, in the FieldToMatch specification.\n\nName (string) -- [REQUIRED]The name of the query argument to inspect.\n\n\n\nAllQueryArguments (dict) --Inspect all query arguments.\n\nUriPath (dict) --Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .\n\nQueryString (dict) --Inspect the query string. This is the part of a URL that appears after a ? character, if any.\n\nBody (dict) --Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.\nNote that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as ByteMatchStatement or RegexPatternSetReferenceStatement , with a SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.\n\nMethod (dict) --Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.\n\n\n\nTextTransformations (list) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nText transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.\n\nPriority (integer) -- [REQUIRED]Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.\n\nType (string) -- [REQUIRED]You can specify the following transformation types:\n\nCMD_LINE\nWhen you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:\n\nDelete the following characters: ' \' ^\nDelete spaces before the following characters: / (\nReplace the following characters with a space: , ;\nReplace multiple spaces with one space\nConvert uppercase letters (A-Z) to lowercase (a-z)\n\n\nCOMPRESS_WHITE_SPACE\nUse this option to replace the following characters with a space character (decimal 32):\n\nf, formfeed, decimal 12\nt, tab, decimal 9\nn, newline, decimal 10\nr, carriage return, decimal 13\nv, vertical tab, decimal 11\nnon-breaking space, decimal 160\n\n\nCOMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE\n\nUse this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:\n\nReplaces (ampersand)quot; with '\nReplaces (ampersand)nbsp; with a non-breaking space, decimal 160\nReplaces (ampersand)lt; with a 'less than' symbol\nReplaces (ampersand)gt; with >\nReplaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters\nReplaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters\n\n\nLOWERCASE\nUse this option to convert uppercase letters (A-Z) to lowercase (a-z).\n\nURL_DECODE\nUse this option to decode a URL-encoded value.\n\nNONE\nSpecify NONE if you don\'t want any text transformations.\n\n\n\n\n\n\n\nRateBasedStatement (dict) --A rate-based rule tracks the rate of requests for each originating IP address, and triggers the rule action when the rate exceeds a limit that you specify on the number of requests in any 5-minute time span. You can use this to put a temporary block on requests from an IP address that is sending excessive requests.\nWhen the rule action triggers, AWS WAF blocks additional requests from the IP address until the request rate falls below the limit.\nYou can optionally nest another statement inside the rate-based statement, to narrow the scope of the rule so that it only counts requests that match the nested statement. For example, based on recent requests that you have seen from an attacker, you might create a rate-based rule with a nested AND rule statement that contains the following nested statements:\n\nAn IP match statement with an IP set that specified the address 192.0.2.44.\nA string match statement that searches in the User-Agent header for the string BadBot.\n\nIn this rate-based rule, you also define a rate limit. For this example, the rate limit is 1,000. Requests that meet both of the conditions in the statements are counted. If the count exceeds 1,000 requests per five minutes, the rule action triggers. Requests that do not meet both conditions are not counted towards the rate limit and are not affected by this rule.\nYou cannot nest a RateBasedStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.\n\nLimit (integer) -- [REQUIRED]The limit on requests per 5-minute period for a single originating IP address. If the statement includes a ScopDownStatement , this limit is applied only to the requests that match the statement.\n\nAggregateKeyType (string) -- [REQUIRED]Setting that indicates how to aggregate the request counts. Currently, you must set this to IP . The request counts are aggregated on IP addresses.\n\nScopeDownStatement (dict) --An optional nested statement that narrows the scope of the rate-based statement to matching web requests. This can be any nestable statement, and you can nest statements at any level below this scope-down statement.\n\n\n\nAndStatement (dict) --A logical rule statement used to combine other rule statements with AND logic. You provide more than one Statement within the AndStatement .\n\nStatements (list) -- [REQUIRED]The statements to combine with AND logic. You can use any statements that can be nested.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nThe processing guidance for a Rule , used by AWS WAF to determine whether a web request matches the rule.\n\n\n\n\n\nOrStatement (dict) --A logical rule statement used to combine other rule statements with OR logic. You provide more than one Statement within the OrStatement .\n\nStatements (list) -- [REQUIRED]The statements to combine with OR logic. You can use any statements that can be nested.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nThe processing guidance for a Rule , used by AWS WAF to determine whether a web request matches the rule.\n\n\n\n\n\nNotStatement (dict) --A logical rule statement used to negate the results of another rule statement. You provide one Statement within the NotStatement .\n\nStatement (dict) --The statement to negate. You can use any statement that can be nested.\n\n\n\nManagedRuleGroupStatement (dict) --A rule statement used to run the rules that are defined in a managed rule group. To use this, provide the vendor name and the name of the rule group in this statement. You can retrieve the required names by calling ListAvailableManagedRuleGroups .\nYou can\'t nest a ManagedRuleGroupStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.\n\nVendorName (string) -- [REQUIRED]The name of the managed rule group vendor. You use this, along with the rule group name, to identify the rule group.\n\nName (string) -- [REQUIRED]The name of the managed rule group. You use this, along with the vendor name, to identify the rule group.\n\nExcludedRules (list) --The rules whose actions are set to COUNT by the web ACL, regardless of the action that is set on the rule. This effectively excludes the rule from acting on web requests.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nSpecifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.\n\nName (string) -- [REQUIRED]The name of the rule to exclude.\n\n\n\n\n\n\n\n\n\nAction (dict) --The action that AWS WAF should take on a web request when it matches the rule statement. Settings at the web ACL level can override the rule action setting.\nThis is used only for rules whose statements do not reference a rule group. Rule statements that reference a rule group include RuleGroupReferenceStatement and ManagedRuleGroupStatement .\nYou must specify either this Action setting or the rule OverrideAction setting, but not both:\n\nIf the rule statement does not reference a rule group, use this rule action setting and not the rule override action setting.\nIf the rule statement references a rule group, use the override action setting and not this action setting.\n\n\nBlock (dict) --Instructs AWS WAF to block the web request.\n\nAllow (dict) --Instructs AWS WAF to allow the web request.\n\nCount (dict) --Instructs AWS WAF to count the web request and allow it.\n\n\n\nOverrideAction (dict) --The override action to apply to the rules in a rule group. Used only for rule statements that reference a rule group, like RuleGroupReferenceStatement and ManagedRuleGroupStatement .\nSet the override action to none to leave the rule actions in effect. Set it to count to only count matches, regardless of the rule action settings.\nIn a Rule , you must specify either this OverrideAction setting or the rule Action setting, but not both:\n\nIf the rule statement references a rule group, use this override action setting and not the action setting.\nIf the rule statement does not reference a rule group, use the rule action setting and not this rule override action setting.\n\n\nCount (dict) --Override the rule action setting to count.\n\nNone (dict) --Don\'t override the rule action setting.\n\n\n\nVisibilityConfig (dict) -- [REQUIRED]Defines and enables Amazon CloudWatch metrics and web request sample collection.\n\nSampledRequestsEnabled (boolean) -- [REQUIRED]A boolean indicating whether AWS WAF should store a sampling of the web requests that match the rules. You can view the sampled requests through the AWS WAF console.\n\nCloudWatchMetricsEnabled (boolean) -- [REQUIRED]A boolean indicating whether the associated resource sends metrics to CloudWatch. For the list of available metrics, see AWS WAF Metrics .\n\nMetricName (string) -- [REQUIRED]A name of the CloudWatch metric. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with length from one to 128 characters. It can\'t contain whitespace or metric names reserved for AWS WAF, for example 'All' and 'Default_Action.' You can\'t change a MetricName after you create a VisibilityConfig .\n\n\n\n\n\n\n

    :type VisibilityConfig: dict
    :param VisibilityConfig: [REQUIRED]\nDefines and enables Amazon CloudWatch metrics and web request sample collection.\n\nSampledRequestsEnabled (boolean) -- [REQUIRED]A boolean indicating whether AWS WAF should store a sampling of the web requests that match the rules. You can view the sampled requests through the AWS WAF console.\n\nCloudWatchMetricsEnabled (boolean) -- [REQUIRED]A boolean indicating whether the associated resource sends metrics to CloudWatch. For the list of available metrics, see AWS WAF Metrics .\n\nMetricName (string) -- [REQUIRED]A name of the CloudWatch metric. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with length from one to 128 characters. It can\'t contain whitespace or metric names reserved for AWS WAF, for example 'All' and 'Default_Action.' You can\'t change a MetricName after you create a VisibilityConfig .\n\n\n

    :type Tags: list
    :param Tags: An array of key:value pairs to associate with the resource.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nA collection of key:value pairs associated with an AWS resource. The key:value pair can be anything you define. Typically, the tag key represents a category (such as 'environment') and the tag value represents a specific value within that category (such as 'test,' 'development,' or 'production'). You can add up to 50 tags to each AWS resource.\n\nKey (string) -- [REQUIRED]Part of the key:value pair that defines a tag. You can use a tag key to describe a category of information, such as 'customer.' Tag keys are case-sensitive.\n\nValue (string) -- [REQUIRED]Part of the key:value pair that defines a tag. You can use a tag value to describe a specific value within a category, such as 'companyA' or 'companyB.' Tag values are case-sensitive.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Summary': {
        'Name': 'string',
        'Id': 'string',
        'Description': 'string',
        'LockToken': 'string',
        'ARN': 'string'
    }
}


Response Structure

(dict) --

Summary (dict) --
High-level information about a  RuleGroup , returned by operations like create and list. This provides information like the ID, that you can use to retrieve and manage a RuleGroup , and the ARN, that you provide to the  RuleGroupReferenceStatement to use the rule group in a  Rule .

Name (string) --
The name of the data type instance. You cannot change the name after you create the instance.

Id (string) --
A unique identifier for the rule group. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.

Description (string) --
A description of the rule group that helps with identification. You cannot change the description of a rule group after you create it.

LockToken (string) --
A token used for optimistic locking. AWS WAF returns a token to your get and list requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like update and delete. AWS WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a WAFOptimisticLockException . If this happens, perform another get, and use the new token returned by that operation.

ARN (string) --
The Amazon Resource Name (ARN) of the entity.









Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFDuplicateItemException
WAFV2.Client.exceptions.WAFOptimisticLockException
WAFV2.Client.exceptions.WAFLimitsExceededException
WAFV2.Client.exceptions.WAFUnavailableEntityException
WAFV2.Client.exceptions.WAFTagOperationException
WAFV2.Client.exceptions.WAFTagOperationInternalErrorException
WAFV2.Client.exceptions.WAFSubscriptionNotFoundException
WAFV2.Client.exceptions.WAFNonexistentItemException
WAFV2.Client.exceptions.WAFInvalidOperationException


    :return: {
        'Summary': {
            'Name': 'string',
            'Id': 'string',
            'Description': 'string',
            'LockToken': 'string',
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    WAFV2.Client.exceptions.WAFInternalErrorException
    WAFV2.Client.exceptions.WAFInvalidParameterException
    WAFV2.Client.exceptions.WAFDuplicateItemException
    WAFV2.Client.exceptions.WAFOptimisticLockException
    WAFV2.Client.exceptions.WAFLimitsExceededException
    WAFV2.Client.exceptions.WAFUnavailableEntityException
    WAFV2.Client.exceptions.WAFTagOperationException
    WAFV2.Client.exceptions.WAFTagOperationInternalErrorException
    WAFV2.Client.exceptions.WAFSubscriptionNotFoundException
    WAFV2.Client.exceptions.WAFNonexistentItemException
    WAFV2.Client.exceptions.WAFInvalidOperationException
    
    """
    pass

def create_web_acl(Name=None, Scope=None, DefaultAction=None, Description=None, Rules=None, VisibilityConfig=None, Tags=None):
    """
    Creates a  WebACL per the specifications provided.
    A Web ACL defines a collection of rules to use to inspect and control web requests. Each rule has an action defined (allow, block, or count) for requests that match the statement of the rule. In the Web ACL, you assign a default action to take (allow, block) for any request that does not match any of the rules. The rules in a Web ACL can be a combination of the types  Rule ,  RuleGroup , and managed rule group. You can associate a Web ACL with one or more AWS resources to protect. The resources can be Amazon CloudFront, an Amazon API Gateway API, or an Application Load Balancer.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_web_acl(
        Name='string',
        Scope='CLOUDFRONT'|'REGIONAL',
        DefaultAction={
            'Block': {}
            ,
            'Allow': {}
    
        },
        Description='string',
        Rules=[
            {
                'Name': 'string',
                'Priority': 123,
                'Statement': {
                    'ByteMatchStatement': {
                        'SearchString': b'bytes',
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {}
                            ,
                            'UriPath': {}
                            ,
                            'QueryString': {}
                            ,
                            'Body': {}
                            ,
                            'Method': {}
    
                        },
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ],
                        'PositionalConstraint': 'EXACTLY'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CONTAINS_WORD'
                    },
                    'SqliMatchStatement': {
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {}
                            ,
                            'UriPath': {}
                            ,
                            'QueryString': {}
                            ,
                            'Body': {}
                            ,
                            'Method': {}
    
                        },
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ]
                    },
                    'XssMatchStatement': {
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {}
                            ,
                            'UriPath': {}
                            ,
                            'QueryString': {}
                            ,
                            'Body': {}
                            ,
                            'Method': {}
    
                        },
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ]
                    },
                    'SizeConstraintStatement': {
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {}
                            ,
                            'UriPath': {}
                            ,
                            'QueryString': {}
                            ,
                            'Body': {}
                            ,
                            'Method': {}
    
                        },
                        'ComparisonOperator': 'EQ'|'NE'|'LE'|'LT'|'GE'|'GT',
                        'Size': 123,
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ]
                    },
                    'GeoMatchStatement': {
                        'CountryCodes': [
                            'AF'|'AX'|'AL'|'DZ'|'AS'|'AD'|'AO'|'AI'|'AQ'|'AG'|'AR'|'AM'|'AW'|'AU'|'AT'|'AZ'|'BS'|'BH'|'BD'|'BB'|'BY'|'BE'|'BZ'|'BJ'|'BM'|'BT'|'BO'|'BQ'|'BA'|'BW'|'BV'|'BR'|'IO'|'BN'|'BG'|'BF'|'BI'|'KH'|'CM'|'CA'|'CV'|'KY'|'CF'|'TD'|'CL'|'CN'|'CX'|'CC'|'CO'|'KM'|'CG'|'CD'|'CK'|'CR'|'CI'|'HR'|'CU'|'CW'|'CY'|'CZ'|'DK'|'DJ'|'DM'|'DO'|'EC'|'EG'|'SV'|'GQ'|'ER'|'EE'|'ET'|'FK'|'FO'|'FJ'|'FI'|'FR'|'GF'|'PF'|'TF'|'GA'|'GM'|'GE'|'DE'|'GH'|'GI'|'GR'|'GL'|'GD'|'GP'|'GU'|'GT'|'GG'|'GN'|'GW'|'GY'|'HT'|'HM'|'VA'|'HN'|'HK'|'HU'|'IS'|'IN'|'ID'|'IR'|'IQ'|'IE'|'IM'|'IL'|'IT'|'JM'|'JP'|'JE'|'JO'|'KZ'|'KE'|'KI'|'KP'|'KR'|'KW'|'KG'|'LA'|'LV'|'LB'|'LS'|'LR'|'LY'|'LI'|'LT'|'LU'|'MO'|'MK'|'MG'|'MW'|'MY'|'MV'|'ML'|'MT'|'MH'|'MQ'|'MR'|'MU'|'YT'|'MX'|'FM'|'MD'|'MC'|'MN'|'ME'|'MS'|'MA'|'MZ'|'MM'|'NA'|'NR'|'NP'|'NL'|'NC'|'NZ'|'NI'|'NE'|'NG'|'NU'|'NF'|'MP'|'NO'|'OM'|'PK'|'PW'|'PS'|'PA'|'PG'|'PY'|'PE'|'PH'|'PN'|'PL'|'PT'|'PR'|'QA'|'RE'|'RO'|'RU'|'RW'|'BL'|'SH'|'KN'|'LC'|'MF'|'PM'|'VC'|'WS'|'SM'|'ST'|'SA'|'SN'|'RS'|'SC'|'SL'|'SG'|'SX'|'SK'|'SI'|'SB'|'SO'|'ZA'|'GS'|'SS'|'ES'|'LK'|'SD'|'SR'|'SJ'|'SZ'|'SE'|'CH'|'SY'|'TW'|'TJ'|'TZ'|'TH'|'TL'|'TG'|'TK'|'TO'|'TT'|'TN'|'TR'|'TM'|'TC'|'TV'|'UG'|'UA'|'AE'|'GB'|'US'|'UM'|'UY'|'UZ'|'VU'|'VE'|'VN'|'VG'|'VI'|'WF'|'EH'|'YE'|'ZM'|'ZW',
                        ]
                    },
                    'RuleGroupReferenceStatement': {
                        'ARN': 'string',
                        'ExcludedRules': [
                            {
                                'Name': 'string'
                            },
                        ]
                    },
                    'IPSetReferenceStatement': {
                        'ARN': 'string'
                    },
                    'RegexPatternSetReferenceStatement': {
                        'ARN': 'string',
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {}
                            ,
                            'UriPath': {}
                            ,
                            'QueryString': {}
                            ,
                            'Body': {}
                            ,
                            'Method': {}
    
                        },
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ]
                    },
                    'RateBasedStatement': {
                        'Limit': 123,
                        'AggregateKeyType': 'IP',
                        'ScopeDownStatement': {'... recursive ...'}
                    },
                    'AndStatement': {
                        'Statements': [
                            {'... recursive ...'},
                        ]
                    },
                    'OrStatement': {
                        'Statements': [
                            {'... recursive ...'},
                        ]
                    },
                    'NotStatement': {
                        'Statement': {'... recursive ...'}
                    },
                    'ManagedRuleGroupStatement': {
                        'VendorName': 'string',
                        'Name': 'string',
                        'ExcludedRules': [
                            {
                                'Name': 'string'
                            },
                        ]
                    }
                },
                'Action': {
                    'Block': {}
                    ,
                    'Allow': {}
                    ,
                    'Count': {}
    
                },
                'OverrideAction': {
                    'Count': {}
                    ,
                    'None': {}
    
                },
                'VisibilityConfig': {
                    'SampledRequestsEnabled': True|False,
                    'CloudWatchMetricsEnabled': True|False,
                    'MetricName': 'string'
                }
            },
        ],
        VisibilityConfig={
            'SampledRequestsEnabled': True|False,
            'CloudWatchMetricsEnabled': True|False,
            'MetricName': 'string'
        },
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the Web ACL. You cannot change the name of a Web ACL after you create it.\n

    :type Scope: string
    :param Scope: [REQUIRED]\nSpecifies whether this is for an AWS CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB) or an API Gateway stage.\nTo work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:\n\nCLI - Specify the Region when you use the CloudFront scope: --scope=CLOUDFRONT --region=us-east-1 .\nAPI and SDKs - For all calls, use the Region endpoint us-east-1.\n\n

    :type DefaultAction: dict
    :param DefaultAction: [REQUIRED]\nThe action to perform if none of the Rules contained in the WebACL match.\n\nBlock (dict) --Specifies that AWS WAF should block requests by default.\n\nAllow (dict) --Specifies that AWS WAF should allow requests by default.\n\n\n

    :type Description: string
    :param Description: A description of the Web ACL that helps with identification. You cannot change the description of a Web ACL after you create it.

    :type Rules: list
    :param Rules: The Rule statements used to identify the web requests that you want to allow, block, or count. Each rule includes one top-level statement that AWS WAF uses to identify matching web requests, and parameters that govern how AWS WAF handles them.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nA single rule, which you can use in a WebACL or RuleGroup to identify web requests that you want to allow, block, or count. Each rule includes one top-level Statement that AWS WAF uses to identify matching web requests, and parameters that govern how AWS WAF handles them.\n\nName (string) -- [REQUIRED]The name of the rule. You can\'t change the name of a Rule after you create it.\n\nPriority (integer) -- [REQUIRED]If you define more than one Rule in a WebACL , AWS WAF evaluates each request against the Rules in order based on the value of Priority . AWS WAF processes rules with lower priority first. The priorities don\'t need to be consecutive, but they must all be different.\n\nStatement (dict) -- [REQUIRED]The AWS WAF processing statement for the rule, for example ByteMatchStatement or SizeConstraintStatement .\n\nByteMatchStatement (dict) --A rule statement that defines a string match search for AWS WAF to apply to web requests. The byte match statement provides the bytes to search for, the location in requests that you want AWS WAF to search, and other settings. The bytes to search for are typically a string that corresponds with ASCII characters. In the AWS WAF console and the developer guide, this is refered to as a string match statement.\n\nSearchString (bytes) -- [REQUIRED]A string value that you want AWS WAF to search for. AWS WAF searches only in the part of web requests that you designate for inspection in FieldToMatch . The maximum length of the value is 50 bytes.\nValid values depend on the component that you specify for inspection in FieldToMatch :\n\nMethod : The HTTP method that you want AWS WAF to search for. This indicates the type of operation specified in the request.\nUriPath : The value that you want AWS WAF to search for in the URI path, for example, /images/daily-ad.jpg .\n\nIf SearchString includes alphabetic characters A-Z and a-z, note that the value is case sensitive.\n\nIf you\'re using the AWS WAF API\nSpecify a base64-encoded version of the value. The maximum length of the value before you base64-encode it is 50 bytes.\nFor example, suppose the value of Type is HEADER and the value of Data is User-Agent . If you want to search the User-Agent header for the value BadBot , you base64-encode BadBot using MIME base64-encoding and include the resulting value, QmFkQm90 , in the value of SearchString .\n\nIf you\'re using the AWS CLI or one of the AWS SDKs\nThe value that you want AWS WAF to search for. The SDK automatically base64 encodes the value.\n\nFieldToMatch (dict) -- [REQUIRED]The part of a web request that you want AWS WAF to inspect. For more information, see FieldToMatch .\n\nSingleHeader (dict) --Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.\n\nName (string) -- [REQUIRED]The name of the query header to inspect.\n\n\n\nSingleQueryArgument (dict) --Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.\nThis is used only to indicate the web request component for AWS WAF to inspect, in the FieldToMatch specification.\n\nName (string) -- [REQUIRED]The name of the query argument to inspect.\n\n\n\nAllQueryArguments (dict) --Inspect all query arguments.\n\nUriPath (dict) --Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .\n\nQueryString (dict) --Inspect the query string. This is the part of a URL that appears after a ? character, if any.\n\nBody (dict) --Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.\nNote that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as ByteMatchStatement or RegexPatternSetReferenceStatement , with a SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.\n\nMethod (dict) --Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.\n\n\n\nTextTransformations (list) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nText transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.\n\nPriority (integer) -- [REQUIRED]Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.\n\nType (string) -- [REQUIRED]You can specify the following transformation types:\n\nCMD_LINE\nWhen you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:\n\nDelete the following characters: ' \' ^\nDelete spaces before the following characters: / (\nReplace the following characters with a space: , ;\nReplace multiple spaces with one space\nConvert uppercase letters (A-Z) to lowercase (a-z)\n\n\nCOMPRESS_WHITE_SPACE\nUse this option to replace the following characters with a space character (decimal 32):\n\nf, formfeed, decimal 12\nt, tab, decimal 9\nn, newline, decimal 10\nr, carriage return, decimal 13\nv, vertical tab, decimal 11\nnon-breaking space, decimal 160\n\n\nCOMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE\n\nUse this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:\n\nReplaces (ampersand)quot; with '\nReplaces (ampersand)nbsp; with a non-breaking space, decimal 160\nReplaces (ampersand)lt; with a 'less than' symbol\nReplaces (ampersand)gt; with >\nReplaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters\nReplaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters\n\n\nLOWERCASE\nUse this option to convert uppercase letters (A-Z) to lowercase (a-z).\n\nURL_DECODE\nUse this option to decode a URL-encoded value.\n\nNONE\nSpecify NONE if you don\'t want any text transformations.\n\n\n\n\n\nPositionalConstraint (string) -- [REQUIRED]The area within the portion of a web request that you want AWS WAF to search for SearchString . Valid values include the following:\n\nCONTAINS\nThe specified part of the web request must include the value of SearchString , but the location doesn\'t matter.\n\nCONTAINS_WORD\nThe specified part of the web request must include the value of SearchString , and SearchString must contain only alphanumeric characters or underscore (A-Z, a-z, 0-9, or _). In addition, SearchString must be a word, which means that both of the following are true:\n\nSearchString is at the beginning of the specified part of the web request or is preceded by a character other than an alphanumeric character or underscore (_). Examples include the value of a header and ;BadBot .\nSearchString is at the end of the specified part of the web request or is followed by a character other than an alphanumeric character or underscore (_), for example, BadBot; and -BadBot; .\n\n\nEXACTLY\nThe value of the specified part of the web request must exactly match the value of SearchString .\n\nSTARTS_WITH\nThe value of SearchString must appear at the beginning of the specified part of the web request.\n\nENDS_WITH\nThe value of SearchString must appear at the end of the specified part of the web request.\n\n\n\nSqliMatchStatement (dict) --Attackers sometimes insert malicious SQL code into web requests in an effort to extract data from your database. To allow or block web requests that appear to contain malicious SQL code, create one or more SQL injection match conditions. An SQL injection match condition identifies the part of web requests, such as the URI or the query string, that you want AWS WAF to inspect. Later in the process, when you create a web ACL, you specify whether to allow or block requests that appear to contain malicious SQL code.\n\nFieldToMatch (dict) -- [REQUIRED]The part of a web request that you want AWS WAF to inspect. For more information, see FieldToMatch .\n\nSingleHeader (dict) --Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.\n\nName (string) -- [REQUIRED]The name of the query header to inspect.\n\n\n\nSingleQueryArgument (dict) --Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.\nThis is used only to indicate the web request component for AWS WAF to inspect, in the FieldToMatch specification.\n\nName (string) -- [REQUIRED]The name of the query argument to inspect.\n\n\n\nAllQueryArguments (dict) --Inspect all query arguments.\n\nUriPath (dict) --Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .\n\nQueryString (dict) --Inspect the query string. This is the part of a URL that appears after a ? character, if any.\n\nBody (dict) --Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.\nNote that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as ByteMatchStatement or RegexPatternSetReferenceStatement , with a SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.\n\nMethod (dict) --Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.\n\n\n\nTextTransformations (list) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nText transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.\n\nPriority (integer) -- [REQUIRED]Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.\n\nType (string) -- [REQUIRED]You can specify the following transformation types:\n\nCMD_LINE\nWhen you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:\n\nDelete the following characters: ' \' ^\nDelete spaces before the following characters: / (\nReplace the following characters with a space: , ;\nReplace multiple spaces with one space\nConvert uppercase letters (A-Z) to lowercase (a-z)\n\n\nCOMPRESS_WHITE_SPACE\nUse this option to replace the following characters with a space character (decimal 32):\n\nf, formfeed, decimal 12\nt, tab, decimal 9\nn, newline, decimal 10\nr, carriage return, decimal 13\nv, vertical tab, decimal 11\nnon-breaking space, decimal 160\n\n\nCOMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE\n\nUse this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:\n\nReplaces (ampersand)quot; with '\nReplaces (ampersand)nbsp; with a non-breaking space, decimal 160\nReplaces (ampersand)lt; with a 'less than' symbol\nReplaces (ampersand)gt; with >\nReplaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters\nReplaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters\n\n\nLOWERCASE\nUse this option to convert uppercase letters (A-Z) to lowercase (a-z).\n\nURL_DECODE\nUse this option to decode a URL-encoded value.\n\nNONE\nSpecify NONE if you don\'t want any text transformations.\n\n\n\n\n\n\n\nXssMatchStatement (dict) --A rule statement that defines a cross-site scripting (XSS) match search for AWS WAF to apply to web requests. XSS attacks are those where the attacker uses vulnerabilities in a benign website as a vehicle to inject malicious client-site scripts into other legitimate web browsers. The XSS match statement provides the location in requests that you want AWS WAF to search and text transformations to use on the search area before AWS WAF searches for character sequences that are likely to be malicious strings.\n\nFieldToMatch (dict) -- [REQUIRED]The part of a web request that you want AWS WAF to inspect. For more information, see FieldToMatch .\n\nSingleHeader (dict) --Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.\n\nName (string) -- [REQUIRED]The name of the query header to inspect.\n\n\n\nSingleQueryArgument (dict) --Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.\nThis is used only to indicate the web request component for AWS WAF to inspect, in the FieldToMatch specification.\n\nName (string) -- [REQUIRED]The name of the query argument to inspect.\n\n\n\nAllQueryArguments (dict) --Inspect all query arguments.\n\nUriPath (dict) --Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .\n\nQueryString (dict) --Inspect the query string. This is the part of a URL that appears after a ? character, if any.\n\nBody (dict) --Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.\nNote that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as ByteMatchStatement or RegexPatternSetReferenceStatement , with a SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.\n\nMethod (dict) --Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.\n\n\n\nTextTransformations (list) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nText transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.\n\nPriority (integer) -- [REQUIRED]Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.\n\nType (string) -- [REQUIRED]You can specify the following transformation types:\n\nCMD_LINE\nWhen you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:\n\nDelete the following characters: ' \' ^\nDelete spaces before the following characters: / (\nReplace the following characters with a space: , ;\nReplace multiple spaces with one space\nConvert uppercase letters (A-Z) to lowercase (a-z)\n\n\nCOMPRESS_WHITE_SPACE\nUse this option to replace the following characters with a space character (decimal 32):\n\nf, formfeed, decimal 12\nt, tab, decimal 9\nn, newline, decimal 10\nr, carriage return, decimal 13\nv, vertical tab, decimal 11\nnon-breaking space, decimal 160\n\n\nCOMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE\n\nUse this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:\n\nReplaces (ampersand)quot; with '\nReplaces (ampersand)nbsp; with a non-breaking space, decimal 160\nReplaces (ampersand)lt; with a 'less than' symbol\nReplaces (ampersand)gt; with >\nReplaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters\nReplaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters\n\n\nLOWERCASE\nUse this option to convert uppercase letters (A-Z) to lowercase (a-z).\n\nURL_DECODE\nUse this option to decode a URL-encoded value.\n\nNONE\nSpecify NONE if you don\'t want any text transformations.\n\n\n\n\n\n\n\nSizeConstraintStatement (dict) --A rule statement that compares a number of bytes against the size of a request component, using a comparison operator, such as greater than (>) or less than (<). For example, you can use a size constraint statement to look for query strings that are longer than 100 bytes.\nIf you configure AWS WAF to inspect the request body, AWS WAF inspects only the first 8192 bytes (8 KB). If the request body for your web requests never exceeds 8192 bytes, you can create a size constraint condition and block requests that have a request body greater than 8192 bytes.\nIf you choose URI for the value of Part of the request to filter on, the slash (/) in the URI counts as one character. For example, the URI /logo.jpg is nine characters long.\n\nFieldToMatch (dict) -- [REQUIRED]The part of a web request that you want AWS WAF to inspect. For more information, see FieldToMatch .\n\nSingleHeader (dict) --Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.\n\nName (string) -- [REQUIRED]The name of the query header to inspect.\n\n\n\nSingleQueryArgument (dict) --Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.\nThis is used only to indicate the web request component for AWS WAF to inspect, in the FieldToMatch specification.\n\nName (string) -- [REQUIRED]The name of the query argument to inspect.\n\n\n\nAllQueryArguments (dict) --Inspect all query arguments.\n\nUriPath (dict) --Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .\n\nQueryString (dict) --Inspect the query string. This is the part of a URL that appears after a ? character, if any.\n\nBody (dict) --Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.\nNote that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as ByteMatchStatement or RegexPatternSetReferenceStatement , with a SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.\n\nMethod (dict) --Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.\n\n\n\nComparisonOperator (string) -- [REQUIRED]The operator to use to compare the request part to the size setting.\n\nSize (integer) -- [REQUIRED]The size, in byte, to compare to the request part, after any transformations.\n\nTextTransformations (list) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nText transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.\n\nPriority (integer) -- [REQUIRED]Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.\n\nType (string) -- [REQUIRED]You can specify the following transformation types:\n\nCMD_LINE\nWhen you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:\n\nDelete the following characters: ' \' ^\nDelete spaces before the following characters: / (\nReplace the following characters with a space: , ;\nReplace multiple spaces with one space\nConvert uppercase letters (A-Z) to lowercase (a-z)\n\n\nCOMPRESS_WHITE_SPACE\nUse this option to replace the following characters with a space character (decimal 32):\n\nf, formfeed, decimal 12\nt, tab, decimal 9\nn, newline, decimal 10\nr, carriage return, decimal 13\nv, vertical tab, decimal 11\nnon-breaking space, decimal 160\n\n\nCOMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE\n\nUse this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:\n\nReplaces (ampersand)quot; with '\nReplaces (ampersand)nbsp; with a non-breaking space, decimal 160\nReplaces (ampersand)lt; with a 'less than' symbol\nReplaces (ampersand)gt; with >\nReplaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters\nReplaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters\n\n\nLOWERCASE\nUse this option to convert uppercase letters (A-Z) to lowercase (a-z).\n\nURL_DECODE\nUse this option to decode a URL-encoded value.\n\nNONE\nSpecify NONE if you don\'t want any text transformations.\n\n\n\n\n\n\n\nGeoMatchStatement (dict) --A rule statement used to identify web requests based on country of origin.\n\nCountryCodes (list) --An array of two-character country codes, for example, [ 'US', 'CN' ] , from the alpha-2 country ISO codes of the ISO 3166 international standard.\n\n(string) --\n\n\n\n\nRuleGroupReferenceStatement (dict) --A rule statement used to run the rules that are defined in a RuleGroup . To use this, create a rule group with your rules, then provide the ARN of the rule group in this statement.\nYou cannot nest a RuleGroupReferenceStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.\n\nARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the entity.\n\nExcludedRules (list) --The names of rules that are in the referenced rule group, but that you want AWS WAF to exclude from processing for this rule statement.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nSpecifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.\n\nName (string) -- [REQUIRED]The name of the rule to exclude.\n\n\n\n\n\n\n\nIPSetReferenceStatement (dict) --A rule statement used to detect web requests coming from particular IP addresses or address ranges. To use this, create an IPSet that specifies the addresses you want to detect, then use the ARN of that set in this statement. To create an IP set, see CreateIPSet .\nEach IP set rule statement references an IP set. You create and maintain the set independent of your rules. This allows you to use the single set in multiple rules. When you update the referenced set, AWS WAF automatically updates all rules that reference it.\n\nARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the IPSet that this statement references.\n\n\n\nRegexPatternSetReferenceStatement (dict) --A rule statement used to search web request components for matches with regular expressions. To use this, create a RegexPatternSet that specifies the expressions that you want to detect, then use the ARN of that set in this statement. A web request matches the pattern set rule statement if the request component matches any of the patterns in the set. To create a regex pattern set, see CreateRegexPatternSet .\nEach regex pattern set rule statement references a regex pattern set. You create and maintain the set independent of your rules. This allows you to use the single set in multiple rules. When you update the referenced set, AWS WAF automatically updates all rules that reference it.\n\nARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the RegexPatternSet that this statement references.\n\nFieldToMatch (dict) -- [REQUIRED]The part of a web request that you want AWS WAF to inspect. For more information, see FieldToMatch .\n\nSingleHeader (dict) --Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.\n\nName (string) -- [REQUIRED]The name of the query header to inspect.\n\n\n\nSingleQueryArgument (dict) --Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.\nThis is used only to indicate the web request component for AWS WAF to inspect, in the FieldToMatch specification.\n\nName (string) -- [REQUIRED]The name of the query argument to inspect.\n\n\n\nAllQueryArguments (dict) --Inspect all query arguments.\n\nUriPath (dict) --Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .\n\nQueryString (dict) --Inspect the query string. This is the part of a URL that appears after a ? character, if any.\n\nBody (dict) --Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.\nNote that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as ByteMatchStatement or RegexPatternSetReferenceStatement , with a SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.\n\nMethod (dict) --Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.\n\n\n\nTextTransformations (list) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nText transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.\n\nPriority (integer) -- [REQUIRED]Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.\n\nType (string) -- [REQUIRED]You can specify the following transformation types:\n\nCMD_LINE\nWhen you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:\n\nDelete the following characters: ' \' ^\nDelete spaces before the following characters: / (\nReplace the following characters with a space: , ;\nReplace multiple spaces with one space\nConvert uppercase letters (A-Z) to lowercase (a-z)\n\n\nCOMPRESS_WHITE_SPACE\nUse this option to replace the following characters with a space character (decimal 32):\n\nf, formfeed, decimal 12\nt, tab, decimal 9\nn, newline, decimal 10\nr, carriage return, decimal 13\nv, vertical tab, decimal 11\nnon-breaking space, decimal 160\n\n\nCOMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE\n\nUse this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:\n\nReplaces (ampersand)quot; with '\nReplaces (ampersand)nbsp; with a non-breaking space, decimal 160\nReplaces (ampersand)lt; with a 'less than' symbol\nReplaces (ampersand)gt; with >\nReplaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters\nReplaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters\n\n\nLOWERCASE\nUse this option to convert uppercase letters (A-Z) to lowercase (a-z).\n\nURL_DECODE\nUse this option to decode a URL-encoded value.\n\nNONE\nSpecify NONE if you don\'t want any text transformations.\n\n\n\n\n\n\n\nRateBasedStatement (dict) --A rate-based rule tracks the rate of requests for each originating IP address, and triggers the rule action when the rate exceeds a limit that you specify on the number of requests in any 5-minute time span. You can use this to put a temporary block on requests from an IP address that is sending excessive requests.\nWhen the rule action triggers, AWS WAF blocks additional requests from the IP address until the request rate falls below the limit.\nYou can optionally nest another statement inside the rate-based statement, to narrow the scope of the rule so that it only counts requests that match the nested statement. For example, based on recent requests that you have seen from an attacker, you might create a rate-based rule with a nested AND rule statement that contains the following nested statements:\n\nAn IP match statement with an IP set that specified the address 192.0.2.44.\nA string match statement that searches in the User-Agent header for the string BadBot.\n\nIn this rate-based rule, you also define a rate limit. For this example, the rate limit is 1,000. Requests that meet both of the conditions in the statements are counted. If the count exceeds 1,000 requests per five minutes, the rule action triggers. Requests that do not meet both conditions are not counted towards the rate limit and are not affected by this rule.\nYou cannot nest a RateBasedStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.\n\nLimit (integer) -- [REQUIRED]The limit on requests per 5-minute period for a single originating IP address. If the statement includes a ScopDownStatement , this limit is applied only to the requests that match the statement.\n\nAggregateKeyType (string) -- [REQUIRED]Setting that indicates how to aggregate the request counts. Currently, you must set this to IP . The request counts are aggregated on IP addresses.\n\nScopeDownStatement (dict) --An optional nested statement that narrows the scope of the rate-based statement to matching web requests. This can be any nestable statement, and you can nest statements at any level below this scope-down statement.\n\n\n\nAndStatement (dict) --A logical rule statement used to combine other rule statements with AND logic. You provide more than one Statement within the AndStatement .\n\nStatements (list) -- [REQUIRED]The statements to combine with AND logic. You can use any statements that can be nested.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nThe processing guidance for a Rule , used by AWS WAF to determine whether a web request matches the rule.\n\n\n\n\n\nOrStatement (dict) --A logical rule statement used to combine other rule statements with OR logic. You provide more than one Statement within the OrStatement .\n\nStatements (list) -- [REQUIRED]The statements to combine with OR logic. You can use any statements that can be nested.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nThe processing guidance for a Rule , used by AWS WAF to determine whether a web request matches the rule.\n\n\n\n\n\nNotStatement (dict) --A logical rule statement used to negate the results of another rule statement. You provide one Statement within the NotStatement .\n\nStatement (dict) --The statement to negate. You can use any statement that can be nested.\n\n\n\nManagedRuleGroupStatement (dict) --A rule statement used to run the rules that are defined in a managed rule group. To use this, provide the vendor name and the name of the rule group in this statement. You can retrieve the required names by calling ListAvailableManagedRuleGroups .\nYou can\'t nest a ManagedRuleGroupStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.\n\nVendorName (string) -- [REQUIRED]The name of the managed rule group vendor. You use this, along with the rule group name, to identify the rule group.\n\nName (string) -- [REQUIRED]The name of the managed rule group. You use this, along with the vendor name, to identify the rule group.\n\nExcludedRules (list) --The rules whose actions are set to COUNT by the web ACL, regardless of the action that is set on the rule. This effectively excludes the rule from acting on web requests.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nSpecifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.\n\nName (string) -- [REQUIRED]The name of the rule to exclude.\n\n\n\n\n\n\n\n\n\nAction (dict) --The action that AWS WAF should take on a web request when it matches the rule statement. Settings at the web ACL level can override the rule action setting.\nThis is used only for rules whose statements do not reference a rule group. Rule statements that reference a rule group include RuleGroupReferenceStatement and ManagedRuleGroupStatement .\nYou must specify either this Action setting or the rule OverrideAction setting, but not both:\n\nIf the rule statement does not reference a rule group, use this rule action setting and not the rule override action setting.\nIf the rule statement references a rule group, use the override action setting and not this action setting.\n\n\nBlock (dict) --Instructs AWS WAF to block the web request.\n\nAllow (dict) --Instructs AWS WAF to allow the web request.\n\nCount (dict) --Instructs AWS WAF to count the web request and allow it.\n\n\n\nOverrideAction (dict) --The override action to apply to the rules in a rule group. Used only for rule statements that reference a rule group, like RuleGroupReferenceStatement and ManagedRuleGroupStatement .\nSet the override action to none to leave the rule actions in effect. Set it to count to only count matches, regardless of the rule action settings.\nIn a Rule , you must specify either this OverrideAction setting or the rule Action setting, but not both:\n\nIf the rule statement references a rule group, use this override action setting and not the action setting.\nIf the rule statement does not reference a rule group, use the rule action setting and not this rule override action setting.\n\n\nCount (dict) --Override the rule action setting to count.\n\nNone (dict) --Don\'t override the rule action setting.\n\n\n\nVisibilityConfig (dict) -- [REQUIRED]Defines and enables Amazon CloudWatch metrics and web request sample collection.\n\nSampledRequestsEnabled (boolean) -- [REQUIRED]A boolean indicating whether AWS WAF should store a sampling of the web requests that match the rules. You can view the sampled requests through the AWS WAF console.\n\nCloudWatchMetricsEnabled (boolean) -- [REQUIRED]A boolean indicating whether the associated resource sends metrics to CloudWatch. For the list of available metrics, see AWS WAF Metrics .\n\nMetricName (string) -- [REQUIRED]A name of the CloudWatch metric. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with length from one to 128 characters. It can\'t contain whitespace or metric names reserved for AWS WAF, for example 'All' and 'Default_Action.' You can\'t change a MetricName after you create a VisibilityConfig .\n\n\n\n\n\n\n

    :type VisibilityConfig: dict
    :param VisibilityConfig: [REQUIRED]\nDefines and enables Amazon CloudWatch metrics and web request sample collection.\n\nSampledRequestsEnabled (boolean) -- [REQUIRED]A boolean indicating whether AWS WAF should store a sampling of the web requests that match the rules. You can view the sampled requests through the AWS WAF console.\n\nCloudWatchMetricsEnabled (boolean) -- [REQUIRED]A boolean indicating whether the associated resource sends metrics to CloudWatch. For the list of available metrics, see AWS WAF Metrics .\n\nMetricName (string) -- [REQUIRED]A name of the CloudWatch metric. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with length from one to 128 characters. It can\'t contain whitespace or metric names reserved for AWS WAF, for example 'All' and 'Default_Action.' You can\'t change a MetricName after you create a VisibilityConfig .\n\n\n

    :type Tags: list
    :param Tags: An array of key:value pairs to associate with the resource.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nA collection of key:value pairs associated with an AWS resource. The key:value pair can be anything you define. Typically, the tag key represents a category (such as 'environment') and the tag value represents a specific value within that category (such as 'test,' 'development,' or 'production'). You can add up to 50 tags to each AWS resource.\n\nKey (string) -- [REQUIRED]Part of the key:value pair that defines a tag. You can use a tag key to describe a category of information, such as 'customer.' Tag keys are case-sensitive.\n\nValue (string) -- [REQUIRED]Part of the key:value pair that defines a tag. You can use a tag value to describe a specific value within a category, such as 'companyA' or 'companyB.' Tag values are case-sensitive.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Summary': {
        'Name': 'string',
        'Id': 'string',
        'Description': 'string',
        'LockToken': 'string',
        'ARN': 'string'
    }
}


Response Structure

(dict) --

Summary (dict) --
High-level information about a  WebACL , returned by operations like create and list. This provides information like the ID, that you can use to retrieve and manage a WebACL , and the ARN, that you provide to operations like  AssociateWebACL .

Name (string) --
The name of the Web ACL. You cannot change the name of a Web ACL after you create it.

Id (string) --
The unique identifier for the Web ACL. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.

Description (string) --
A description of the Web ACL that helps with identification. You cannot change the description of a Web ACL after you create it.

LockToken (string) --
A token used for optimistic locking. AWS WAF returns a token to your get and list requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like update and delete. AWS WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a WAFOptimisticLockException . If this happens, perform another get, and use the new token returned by that operation.

ARN (string) --
The Amazon Resource Name (ARN) of the entity.









Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFDuplicateItemException
WAFV2.Client.exceptions.WAFOptimisticLockException
WAFV2.Client.exceptions.WAFLimitsExceededException
WAFV2.Client.exceptions.WAFInvalidResourceException
WAFV2.Client.exceptions.WAFUnavailableEntityException
WAFV2.Client.exceptions.WAFNonexistentItemException
WAFV2.Client.exceptions.WAFTagOperationException
WAFV2.Client.exceptions.WAFTagOperationInternalErrorException
WAFV2.Client.exceptions.WAFSubscriptionNotFoundException
WAFV2.Client.exceptions.WAFInvalidOperationException


    :return: {
        'Summary': {
            'Name': 'string',
            'Id': 'string',
            'Description': 'string',
            'LockToken': 'string',
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    WAFV2.Client.exceptions.WAFInternalErrorException
    WAFV2.Client.exceptions.WAFInvalidParameterException
    WAFV2.Client.exceptions.WAFDuplicateItemException
    WAFV2.Client.exceptions.WAFOptimisticLockException
    WAFV2.Client.exceptions.WAFLimitsExceededException
    WAFV2.Client.exceptions.WAFInvalidResourceException
    WAFV2.Client.exceptions.WAFUnavailableEntityException
    WAFV2.Client.exceptions.WAFNonexistentItemException
    WAFV2.Client.exceptions.WAFTagOperationException
    WAFV2.Client.exceptions.WAFTagOperationInternalErrorException
    WAFV2.Client.exceptions.WAFSubscriptionNotFoundException
    WAFV2.Client.exceptions.WAFInvalidOperationException
    
    """
    pass

def delete_firewall_manager_rule_groups(WebACLArn=None, WebACLLockToken=None):
    """
    Deletes all rule groups that are managed by AWS Firewall Manager for the specified web ACL.
    You can only use this if ManagedByFirewallManager is false in the specified  WebACL .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_firewall_manager_rule_groups(
        WebACLArn='string',
        WebACLLockToken='string'
    )
    
    
    :type WebACLArn: string
    :param WebACLArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the web ACL.\n

    :type WebACLLockToken: string
    :param WebACLLockToken: [REQUIRED]\nA token used for optimistic locking. AWS WAF returns a token to your get and list requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like update and delete. AWS WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a WAFOptimisticLockException . If this happens, perform another get, and use the new token returned by that operation.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'NextWebACLLockToken': 'string'
}


Response Structure

(dict) --

NextWebACLLockToken (string) --
A token used for optimistic locking. AWS WAF returns a token to your get and list requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like update and delete. AWS WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a WAFOptimisticLockException . If this happens, perform another get, and use the new token returned by that operation.







Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFNonexistentItemException
WAFV2.Client.exceptions.WAFOptimisticLockException
WAFV2.Client.exceptions.WAFInvalidOperationException


    :return: {
        'NextWebACLLockToken': 'string'
    }
    
    
    :returns: 
    WAFV2.Client.exceptions.WAFInternalErrorException
    WAFV2.Client.exceptions.WAFInvalidParameterException
    WAFV2.Client.exceptions.WAFNonexistentItemException
    WAFV2.Client.exceptions.WAFOptimisticLockException
    WAFV2.Client.exceptions.WAFInvalidOperationException
    
    """
    pass

def delete_ip_set(Name=None, Scope=None, Id=None, LockToken=None):
    """
    Deletes the specified  IPSet .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_ip_set(
        Name='string',
        Scope='CLOUDFRONT'|'REGIONAL',
        Id='string',
        LockToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the IP set. You cannot change the name of an IPSet after you create it.\n

    :type Scope: string
    :param Scope: [REQUIRED]\nSpecifies whether this is for an AWS CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB) or an API Gateway stage.\nTo work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:\n\nCLI - Specify the Region when you use the CloudFront scope: --scope=CLOUDFRONT --region=us-east-1 .\nAPI and SDKs - For all calls, use the Region endpoint us-east-1.\n\n

    :type Id: string
    :param Id: [REQUIRED]\nA unique identifier for the set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.\n

    :type LockToken: string
    :param LockToken: [REQUIRED]\nA token used for optimistic locking. AWS WAF returns a token to your get and list requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like update and delete. AWS WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a WAFOptimisticLockException . If this happens, perform another get, and use the new token returned by that operation.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFNonexistentItemException
WAFV2.Client.exceptions.WAFOptimisticLockException
WAFV2.Client.exceptions.WAFAssociatedItemException
WAFV2.Client.exceptions.WAFTagOperationException
WAFV2.Client.exceptions.WAFTagOperationInternalErrorException
WAFV2.Client.exceptions.WAFInvalidOperationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_logging_configuration(ResourceArn=None):
    """
    Deletes the  LoggingConfiguration from the specified web ACL.
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

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFNonexistentItemException
WAFV2.Client.exceptions.WAFOptimisticLockException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFInvalidOperationException


    :return: {}
    
    
    :returns: 
    WAFV2.Client.exceptions.WAFInternalErrorException
    WAFV2.Client.exceptions.WAFNonexistentItemException
    WAFV2.Client.exceptions.WAFOptimisticLockException
    WAFV2.Client.exceptions.WAFInvalidParameterException
    WAFV2.Client.exceptions.WAFInvalidOperationException
    
    """
    pass

def delete_permission_policy(ResourceArn=None):
    """
    Permanently deletes an IAM policy from the specified rule group.
    You must be the owner of the rule group to perform this operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_permission_policy(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the rule group from which you want to delete the policy.\nYou must be the owner of the rule group to perform this operation.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

WAFV2.Client.exceptions.WAFNonexistentItemException
WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException


    :return: {}
    
    
    :returns: 
    WAFV2.Client.exceptions.WAFNonexistentItemException
    WAFV2.Client.exceptions.WAFInternalErrorException
    WAFV2.Client.exceptions.WAFInvalidParameterException
    
    """
    pass

def delete_regex_pattern_set(Name=None, Scope=None, Id=None, LockToken=None):
    """
    Deletes the specified  RegexPatternSet .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_regex_pattern_set(
        Name='string',
        Scope='CLOUDFRONT'|'REGIONAL',
        Id='string',
        LockToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the set. You cannot change the name after you create the set.\n

    :type Scope: string
    :param Scope: [REQUIRED]\nSpecifies whether this is for an AWS CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB) or an API Gateway stage.\nTo work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:\n\nCLI - Specify the Region when you use the CloudFront scope: --scope=CLOUDFRONT --region=us-east-1 .\nAPI and SDKs - For all calls, use the Region endpoint us-east-1.\n\n

    :type Id: string
    :param Id: [REQUIRED]\nA unique identifier for the set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.\n

    :type LockToken: string
    :param LockToken: [REQUIRED]\nA token used for optimistic locking. AWS WAF returns a token to your get and list requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like update and delete. AWS WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a WAFOptimisticLockException . If this happens, perform another get, and use the new token returned by that operation.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFNonexistentItemException
WAFV2.Client.exceptions.WAFOptimisticLockException
WAFV2.Client.exceptions.WAFAssociatedItemException
WAFV2.Client.exceptions.WAFTagOperationException
WAFV2.Client.exceptions.WAFTagOperationInternalErrorException
WAFV2.Client.exceptions.WAFInvalidOperationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_rule_group(Name=None, Scope=None, Id=None, LockToken=None):
    """
    Deletes the specified  RuleGroup .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_rule_group(
        Name='string',
        Scope='CLOUDFRONT'|'REGIONAL',
        Id='string',
        LockToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the rule group. You cannot change the name of a rule group after you create it.\n

    :type Scope: string
    :param Scope: [REQUIRED]\nSpecifies whether this is for an AWS CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB) or an API Gateway stage.\nTo work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:\n\nCLI - Specify the Region when you use the CloudFront scope: --scope=CLOUDFRONT --region=us-east-1 .\nAPI and SDKs - For all calls, use the Region endpoint us-east-1.\n\n

    :type Id: string
    :param Id: [REQUIRED]\nA unique identifier for the rule group. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.\n

    :type LockToken: string
    :param LockToken: [REQUIRED]\nA token used for optimistic locking. AWS WAF returns a token to your get and list requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like update and delete. AWS WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a WAFOptimisticLockException . If this happens, perform another get, and use the new token returned by that operation.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFNonexistentItemException
WAFV2.Client.exceptions.WAFOptimisticLockException
WAFV2.Client.exceptions.WAFAssociatedItemException
WAFV2.Client.exceptions.WAFTagOperationException
WAFV2.Client.exceptions.WAFTagOperationInternalErrorException
WAFV2.Client.exceptions.WAFInvalidOperationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_web_acl(Name=None, Scope=None, Id=None, LockToken=None):
    """
    Deletes the specified  WebACL .
    You can only use this if ManagedByFirewallManager is false in the specified  WebACL .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_web_acl(
        Name='string',
        Scope='CLOUDFRONT'|'REGIONAL',
        Id='string',
        LockToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the Web ACL. You cannot change the name of a Web ACL after you create it.\n

    :type Scope: string
    :param Scope: [REQUIRED]\nSpecifies whether this is for an AWS CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB) or an API Gateway stage.\nTo work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:\n\nCLI - Specify the Region when you use the CloudFront scope: --scope=CLOUDFRONT --region=us-east-1 .\nAPI and SDKs - For all calls, use the Region endpoint us-east-1.\n\n

    :type Id: string
    :param Id: [REQUIRED]\nThe unique identifier for the Web ACL. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.\n

    :type LockToken: string
    :param LockToken: [REQUIRED]\nA token used for optimistic locking. AWS WAF returns a token to your get and list requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like update and delete. AWS WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a WAFOptimisticLockException . If this happens, perform another get, and use the new token returned by that operation.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFNonexistentItemException
WAFV2.Client.exceptions.WAFOptimisticLockException
WAFV2.Client.exceptions.WAFAssociatedItemException
WAFV2.Client.exceptions.WAFTagOperationException
WAFV2.Client.exceptions.WAFTagOperationInternalErrorException
WAFV2.Client.exceptions.WAFInvalidOperationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def describe_managed_rule_group(VendorName=None, Name=None, Scope=None):
    """
    Provides high-level information for a managed rule group, including descriptions of the rules.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_managed_rule_group(
        VendorName='string',
        Name='string',
        Scope='CLOUDFRONT'|'REGIONAL'
    )
    
    
    :type VendorName: string
    :param VendorName: [REQUIRED]\nThe name of the managed rule group vendor. You use this, along with the rule group name, to identify the rule group.\n

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the managed rule group. You use this, along with the vendor name, to identify the rule group.\n

    :type Scope: string
    :param Scope: [REQUIRED]\nSpecifies whether this is for an AWS CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB) or an API Gateway stage.\nTo work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:\n\nCLI - Specify the Region when you use the CloudFront scope: --scope=CLOUDFRONT --region=us-east-1 .\nAPI and SDKs - For all calls, use the Region endpoint us-east-1.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Capacity': 123,
    'Rules': [
        {
            'Name': 'string',
            'Action': {
                'Block': {},
                'Allow': {},
                'Count': {}
            }
        },
    ]
}


Response Structure

(dict) --

Capacity (integer) --
The web ACL capacity units (WCUs) required for this rule group. AWS WAF uses web ACL capacity units (WCU) to calculate and control the operating resources that are used to run your rules, rule groups, and web ACLs. AWS WAF calculates capacity differently for each rule type, to reflect each rule\'s relative cost. Rule group capacity is fixed at creation, so users can plan their web ACL WCU usage when they use a rule group. The WCU limit for web ACLs is 1,500.

Rules (list) --

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

High-level information about a  Rule , returned by operations like  DescribeManagedRuleGroup . This provides information like the ID, that you can use to retrieve and manage a RuleGroup , and the ARN, that you provide to the  RuleGroupReferenceStatement to use the rule group in a  Rule .

Name (string) --
The name of the rule.

Action (dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

The action that AWS WAF should take on a web request when it matches a rule\'s statement. Settings at the web ACL level can override the rule action setting.

Block (dict) --
Instructs AWS WAF to block the web request.

Allow (dict) --
Instructs AWS WAF to allow the web request.

Count (dict) --
Instructs AWS WAF to count the web request and allow it.













Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFInvalidResourceException
WAFV2.Client.exceptions.WAFNonexistentItemException
WAFV2.Client.exceptions.WAFInvalidOperationException


    :return: {
        'Capacity': 123,
        'Rules': [
            {
                'Name': 'string',
                'Action': {
                    'Block': {},
                    'Allow': {},
                    'Count': {}
                }
            },
        ]
    }
    
    
    :returns: 
    WAFV2.Client.exceptions.WAFInternalErrorException
    WAFV2.Client.exceptions.WAFInvalidParameterException
    WAFV2.Client.exceptions.WAFInvalidResourceException
    WAFV2.Client.exceptions.WAFNonexistentItemException
    WAFV2.Client.exceptions.WAFInvalidOperationException
    
    """
    pass

def disassociate_web_acl(ResourceArn=None):
    """
    Disassociates a Web ACL from a regional application resource. A regional application can be an Application Load Balancer (ALB) or an API Gateway stage.
    For AWS CloudFront, don\'t use this call. Instead, use your CloudFront distribution configuration. To disassociate a Web ACL, provide an empty web ACL ID in the CloudFront call UpdateDistribution . For information, see UpdateDistribution .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_web_acl(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource to disassociate from the web ACL.\nThe ARN must be in one of the following formats:\n\nFor an Application Load Balancer: ``arn:aws:elasticloadbalancing:region :account-id :loadbalancer/app/load-balancer-name /load-balancer-id ``\nFor an Amazon API Gateway stage: ``arn:aws:apigateway:region ::/restapis/api-id /stages/stage-name ``\n\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFNonexistentItemException
WAFV2.Client.exceptions.WAFInvalidOperationException


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

def get_ip_set(Name=None, Scope=None, Id=None):
    """
    Retrieves the specified  IPSet .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_ip_set(
        Name='string',
        Scope='CLOUDFRONT'|'REGIONAL',
        Id='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the IP set. You cannot change the name of an IPSet after you create it.\n

    :type Scope: string
    :param Scope: [REQUIRED]\nSpecifies whether this is for an AWS CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB) or an API Gateway stage.\nTo work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:\n\nCLI - Specify the Region when you use the CloudFront scope: --scope=CLOUDFRONT --region=us-east-1 .\nAPI and SDKs - For all calls, use the Region endpoint us-east-1.\n\n

    :type Id: string
    :param Id: [REQUIRED]\nA unique identifier for the set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'IPSet': {
        'Name': 'string',
        'Id': 'string',
        'ARN': 'string',
        'Description': 'string',
        'IPAddressVersion': 'IPV4'|'IPV6',
        'Addresses': [
            'string',
        ]
    },
    'LockToken': 'string'
}


Response Structure

(dict) --

IPSet (dict) --

Name (string) --
The name of the IP set. You cannot change the name of an IPSet after you create it.

Id (string) --
A unique identifier for the set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.

ARN (string) --
The Amazon Resource Name (ARN) of the entity.

Description (string) --
A description of the IP set that helps with identification. You cannot change the description of an IP set after you create it.

IPAddressVersion (string) --
Specify IPV4 or IPV6.

Addresses (list) --
Contains an array of strings that specify one or more IP addresses or blocks of IP addresses in Classless Inter-Domain Routing (CIDR) notation. AWS WAF supports all address ranges for IP versions IPv4 and IPv6.
Examples:

To configure AWS WAF to allow, block, or count requests that originated from the IP address 192.0.2.44, specify 192.0.2.44/32 .
To configure AWS WAF to allow, block, or count requests that originated from IP addresses from 192.0.2.0 to 192.0.2.255, specify 192.0.2.0/24 .
To configure AWS WAF to allow, block, or count requests that originated from the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify 1111:0000:0000:0000:0000:0000:0000:0111/128 .
To configure AWS WAF to allow, block, or count requests that originated from IP addresses 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify 1111:0000:0000:0000:0000:0000:0000:0000/64 .

For more information about CIDR notation, see the Wikipedia entry Classless Inter-Domain Routing .

(string) --




LockToken (string) --
A token used for optimistic locking. AWS WAF returns a token to your get and list requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like update and delete. AWS WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a WAFOptimisticLockException . If this happens, perform another get, and use the new token returned by that operation.







Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFNonexistentItemException
WAFV2.Client.exceptions.WAFInvalidOperationException


    :return: {
        'IPSet': {
            'Name': 'string',
            'Id': 'string',
            'ARN': 'string',
            'Description': 'string',
            'IPAddressVersion': 'IPV4'|'IPV6',
            'Addresses': [
                'string',
            ]
        },
        'LockToken': 'string'
    }
    
    
    :returns: 
    To configure AWS WAF to allow, block, or count requests that originated from the IP address 192.0.2.44, specify 192.0.2.44/32 .
    To configure AWS WAF to allow, block, or count requests that originated from IP addresses from 192.0.2.0 to 192.0.2.255, specify 192.0.2.0/24 .
    To configure AWS WAF to allow, block, or count requests that originated from the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify 1111:0000:0000:0000:0000:0000:0000:0111/128 .
    To configure AWS WAF to allow, block, or count requests that originated from IP addresses 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify 1111:0000:0000:0000:0000:0000:0000:0000/64 .
    
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
                'SingleHeader': {
                    'Name': 'string'
                },
                'SingleQueryArgument': {
                    'Name': 'string'
                },
                'AllQueryArguments': {},
                'UriPath': {},
                'QueryString': {},
                'Body': {},
                'Method': {}
            },
        ]
    }
}


Response Structure

(dict) --
LoggingConfiguration (dict) --The  LoggingConfiguration for the specified web ACL.

ResourceArn (string) --The Amazon Resource Name (ARN) of the web ACL that you want to associate with LogDestinationConfigs .

LogDestinationConfigs (list) --The Amazon Kinesis Data Firehose Amazon Resource Name (ARNs) that you want to associate with the web ACL.

(string) --


RedactedFields (list) --The parts of the request that you want to keep out of the logs. For example, if you redact the cookie field, the cookie field in the firehose will be xxx .

(dict) --
Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

The part of a web request that you want AWS WAF to inspect. Include the single FieldToMatch type that you want to inspect, with additional specifications as needed, according to the type. You specify a single request component in FieldToMatch for each rule statement that requires it. To inspect more than one component of a web request, create a separate rule statement for each component.

SingleHeader (dict) --Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.

Name (string) --The name of the query header to inspect.



SingleQueryArgument (dict) --Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.

Name (string) --The name of the query argument to inspect.



AllQueryArguments (dict) --Inspect all query arguments.

UriPath (dict) --Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString (dict) --Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body (dict) --Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method (dict) --Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.












Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFNonexistentItemException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFInvalidOperationException


    :return: {
        'LoggingConfiguration': {
            'ResourceArn': 'string',
            'LogDestinationConfigs': [
                'string',
            ],
            'RedactedFields': [
                {
                    'SingleHeader': {
                        'Name': 'string'
                    },
                    'SingleQueryArgument': {
                        'Name': 'string'
                    },
                    'AllQueryArguments': {},
                    'UriPath': {},
                    'QueryString': {},
                    'Body': {},
                    'Method': {}
                },
            ]
        }
    }
    
    
    :returns: 
    WAFV2.Client.exceptions.WAFInternalErrorException
    WAFV2.Client.exceptions.WAFNonexistentItemException
    WAFV2.Client.exceptions.WAFInvalidParameterException
    WAFV2.Client.exceptions.WAFInvalidOperationException
    
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
    Returns the IAM policy that is attached to the specified rule group.
    You must be the owner of the rule group to perform this operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_permission_policy(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the rule group for which you want to get the policy.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Policy': 'string'
}


Response Structure

(dict) --
Policy (string) --The IAM policy that is attached to the specified rule group.






Exceptions

WAFV2.Client.exceptions.WAFNonexistentItemException
WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException


    :return: {
        'Policy': 'string'
    }
    
    
    """
    pass

def get_rate_based_statement_managed_keys(Scope=None, WebACLName=None, WebACLId=None, RuleName=None):
    """
    Retrieves the keys that are currently blocked by a rate-based rule. The maximum number of managed keys that can be blocked for a single rate-based rule is 10,000. If more than 10,000 addresses exceed the rate limit, those with the highest rates are blocked.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_rate_based_statement_managed_keys(
        Scope='CLOUDFRONT'|'REGIONAL',
        WebACLName='string',
        WebACLId='string',
        RuleName='string'
    )
    
    
    :type Scope: string
    :param Scope: [REQUIRED]\nSpecifies whether this is for an AWS CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB) or an API Gateway stage.\nTo work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:\n\nCLI - Specify the Region when you use the CloudFront scope: --scope=CLOUDFRONT --region=us-east-1 .\nAPI and SDKs - For all calls, use the Region endpoint us-east-1.\n\n

    :type WebACLName: string
    :param WebACLName: [REQUIRED]\nThe name of the Web ACL. You cannot change the name of a Web ACL after you create it.\n

    :type WebACLId: string
    :param WebACLId: [REQUIRED]\nThe unique identifier for the Web ACL. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.\n

    :type RuleName: string
    :param RuleName: [REQUIRED]\nThe name of the rate-based rule to get the keys for.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ManagedKeysIPV4': {
        'IPAddressVersion': 'IPV4'|'IPV6',
        'Addresses': [
            'string',
        ]
    },
    'ManagedKeysIPV6': {
        'IPAddressVersion': 'IPV4'|'IPV6',
        'Addresses': [
            'string',
        ]
    }
}


Response Structure

(dict) --

ManagedKeysIPV4 (dict) --
The keys that are of Internet Protocol version 4 (IPv4).

IPAddressVersion (string) --

Addresses (list) --
The IP addresses that are currently blocked.

(string) --




ManagedKeysIPV6 (dict) --
The keys that are of Internet Protocol version 6 (IPv6).

IPAddressVersion (string) --

Addresses (list) --
The IP addresses that are currently blocked.

(string) --










Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFNonexistentItemException
WAFV2.Client.exceptions.WAFInvalidOperationException


    :return: {
        'ManagedKeysIPV4': {
            'IPAddressVersion': 'IPV4'|'IPV6',
            'Addresses': [
                'string',
            ]
        },
        'ManagedKeysIPV6': {
            'IPAddressVersion': 'IPV4'|'IPV6',
            'Addresses': [
                'string',
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_regex_pattern_set(Name=None, Scope=None, Id=None):
    """
    Retrieves the specified  RegexPatternSet .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_regex_pattern_set(
        Name='string',
        Scope='CLOUDFRONT'|'REGIONAL',
        Id='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the set. You cannot change the name after you create the set.\n

    :type Scope: string
    :param Scope: [REQUIRED]\nSpecifies whether this is for an AWS CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB) or an API Gateway stage.\nTo work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:\n\nCLI - Specify the Region when you use the CloudFront scope: --scope=CLOUDFRONT --region=us-east-1 .\nAPI and SDKs - For all calls, use the Region endpoint us-east-1.\n\n

    :type Id: string
    :param Id: [REQUIRED]\nA unique identifier for the set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'RegexPatternSet': {
        'Name': 'string',
        'Id': 'string',
        'ARN': 'string',
        'Description': 'string',
        'RegularExpressionList': [
            {
                'RegexString': 'string'
            },
        ]
    },
    'LockToken': 'string'
}


Response Structure

(dict) --

RegexPatternSet (dict) --

Name (string) --
The name of the set. You cannot change the name after you create the set.

Id (string) --
A unique identifier for the set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.

ARN (string) --
The Amazon Resource Name (ARN) of the entity.

Description (string) --
A description of the set that helps with identification. You cannot change the description of a set after you create it.

RegularExpressionList (list) --
The regular expression patterns in the set.

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

A single regular expression. This is used in a  RegexPatternSet .

RegexString (string) --
The string representing the regular expression.







LockToken (string) --
A token used for optimistic locking. AWS WAF returns a token to your get and list requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like update and delete. AWS WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a WAFOptimisticLockException . If this happens, perform another get, and use the new token returned by that operation.







Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFNonexistentItemException
WAFV2.Client.exceptions.WAFInvalidOperationException


    :return: {
        'RegexPatternSet': {
            'Name': 'string',
            'Id': 'string',
            'ARN': 'string',
            'Description': 'string',
            'RegularExpressionList': [
                {
                    'RegexString': 'string'
                },
            ]
        },
        'LockToken': 'string'
    }
    
    
    :returns: 
    WAFV2.Client.exceptions.WAFInternalErrorException
    WAFV2.Client.exceptions.WAFInvalidParameterException
    WAFV2.Client.exceptions.WAFNonexistentItemException
    WAFV2.Client.exceptions.WAFInvalidOperationException
    
    """
    pass

def get_rule_group(Name=None, Scope=None, Id=None):
    """
    Retrieves the specified  RuleGroup .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_rule_group(
        Name='string',
        Scope='CLOUDFRONT'|'REGIONAL',
        Id='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the rule group. You cannot change the name of a rule group after you create it.\n

    :type Scope: string
    :param Scope: [REQUIRED]\nSpecifies whether this is for an AWS CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB) or an API Gateway stage.\nTo work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:\n\nCLI - Specify the Region when you use the CloudFront scope: --scope=CLOUDFRONT --region=us-east-1 .\nAPI and SDKs - For all calls, use the Region endpoint us-east-1.\n\n

    :type Id: string
    :param Id: [REQUIRED]\nA unique identifier for the rule group. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'RuleGroup': {
        'Name': 'string',
        'Id': 'string',
        'Capacity': 123,
        'ARN': 'string',
        'Description': 'string',
        'Rules': [
            {
                'Name': 'string',
                'Priority': 123,
                'Statement': {
                    'ByteMatchStatement': {
                        'SearchString': b'bytes',
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {},
                            'UriPath': {},
                            'QueryString': {},
                            'Body': {},
                            'Method': {}
                        },
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ],
                        'PositionalConstraint': 'EXACTLY'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CONTAINS_WORD'
                    },
                    'SqliMatchStatement': {
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {},
                            'UriPath': {},
                            'QueryString': {},
                            'Body': {},
                            'Method': {}
                        },
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ]
                    },
                    'XssMatchStatement': {
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {},
                            'UriPath': {},
                            'QueryString': {},
                            'Body': {},
                            'Method': {}
                        },
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ]
                    },
                    'SizeConstraintStatement': {
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {},
                            'UriPath': {},
                            'QueryString': {},
                            'Body': {},
                            'Method': {}
                        },
                        'ComparisonOperator': 'EQ'|'NE'|'LE'|'LT'|'GE'|'GT',
                        'Size': 123,
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ]
                    },
                    'GeoMatchStatement': {
                        'CountryCodes': [
                            'AF'|'AX'|'AL'|'DZ'|'AS'|'AD'|'AO'|'AI'|'AQ'|'AG'|'AR'|'AM'|'AW'|'AU'|'AT'|'AZ'|'BS'|'BH'|'BD'|'BB'|'BY'|'BE'|'BZ'|'BJ'|'BM'|'BT'|'BO'|'BQ'|'BA'|'BW'|'BV'|'BR'|'IO'|'BN'|'BG'|'BF'|'BI'|'KH'|'CM'|'CA'|'CV'|'KY'|'CF'|'TD'|'CL'|'CN'|'CX'|'CC'|'CO'|'KM'|'CG'|'CD'|'CK'|'CR'|'CI'|'HR'|'CU'|'CW'|'CY'|'CZ'|'DK'|'DJ'|'DM'|'DO'|'EC'|'EG'|'SV'|'GQ'|'ER'|'EE'|'ET'|'FK'|'FO'|'FJ'|'FI'|'FR'|'GF'|'PF'|'TF'|'GA'|'GM'|'GE'|'DE'|'GH'|'GI'|'GR'|'GL'|'GD'|'GP'|'GU'|'GT'|'GG'|'GN'|'GW'|'GY'|'HT'|'HM'|'VA'|'HN'|'HK'|'HU'|'IS'|'IN'|'ID'|'IR'|'IQ'|'IE'|'IM'|'IL'|'IT'|'JM'|'JP'|'JE'|'JO'|'KZ'|'KE'|'KI'|'KP'|'KR'|'KW'|'KG'|'LA'|'LV'|'LB'|'LS'|'LR'|'LY'|'LI'|'LT'|'LU'|'MO'|'MK'|'MG'|'MW'|'MY'|'MV'|'ML'|'MT'|'MH'|'MQ'|'MR'|'MU'|'YT'|'MX'|'FM'|'MD'|'MC'|'MN'|'ME'|'MS'|'MA'|'MZ'|'MM'|'NA'|'NR'|'NP'|'NL'|'NC'|'NZ'|'NI'|'NE'|'NG'|'NU'|'NF'|'MP'|'NO'|'OM'|'PK'|'PW'|'PS'|'PA'|'PG'|'PY'|'PE'|'PH'|'PN'|'PL'|'PT'|'PR'|'QA'|'RE'|'RO'|'RU'|'RW'|'BL'|'SH'|'KN'|'LC'|'MF'|'PM'|'VC'|'WS'|'SM'|'ST'|'SA'|'SN'|'RS'|'SC'|'SL'|'SG'|'SX'|'SK'|'SI'|'SB'|'SO'|'ZA'|'GS'|'SS'|'ES'|'LK'|'SD'|'SR'|'SJ'|'SZ'|'SE'|'CH'|'SY'|'TW'|'TJ'|'TZ'|'TH'|'TL'|'TG'|'TK'|'TO'|'TT'|'TN'|'TR'|'TM'|'TC'|'TV'|'UG'|'UA'|'AE'|'GB'|'US'|'UM'|'UY'|'UZ'|'VU'|'VE'|'VN'|'VG'|'VI'|'WF'|'EH'|'YE'|'ZM'|'ZW',
                        ]
                    },
                    'RuleGroupReferenceStatement': {
                        'ARN': 'string',
                        'ExcludedRules': [
                            {
                                'Name': 'string'
                            },
                        ]
                    },
                    'IPSetReferenceStatement': {
                        'ARN': 'string'
                    },
                    'RegexPatternSetReferenceStatement': {
                        'ARN': 'string',
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {},
                            'UriPath': {},
                            'QueryString': {},
                            'Body': {},
                            'Method': {}
                        },
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ]
                    },
                    'RateBasedStatement': {
                        'Limit': 123,
                        'AggregateKeyType': 'IP',
                        'ScopeDownStatement': {'... recursive ...'}
                    },
                    'AndStatement': {
                        'Statements': [
                            {'... recursive ...'},
                        ]
                    },
                    'OrStatement': {
                        'Statements': [
                            {'... recursive ...'},
                        ]
                    },
                    'NotStatement': {
                        'Statement': {'... recursive ...'}
                    },
                    'ManagedRuleGroupStatement': {
                        'VendorName': 'string',
                        'Name': 'string',
                        'ExcludedRules': [
                            {
                                'Name': 'string'
                            },
                        ]
                    }
                },
                'Action': {
                    'Block': {},
                    'Allow': {},
                    'Count': {}
                },
                'OverrideAction': {
                    'Count': {},
                    'None': {}
                },
                'VisibilityConfig': {
                    'SampledRequestsEnabled': True|False,
                    'CloudWatchMetricsEnabled': True|False,
                    'MetricName': 'string'
                }
            },
        ],
        'VisibilityConfig': {
            'SampledRequestsEnabled': True|False,
            'CloudWatchMetricsEnabled': True|False,
            'MetricName': 'string'
        }
    },
    'LockToken': 'string'
}


Response Structure

(dict) --

RuleGroup (dict) --

Name (string) --
The name of the rule group. You cannot change the name of a rule group after you create it.

Id (string) --
A unique identifier for the rule group. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.

Capacity (integer) --
The web ACL capacity units (WCUs) required for this rule group.
When you create your own rule group, you define this, and you cannot change it after creation. When you add or modify the rules in a rule group, AWS WAF enforces this limit. You can check the capacity for a set of rules using  CheckCapacity .
AWS WAF uses WCUs to calculate and control the operating resources that are used to run your rules, rule groups, and web ACLs. AWS WAF calculates capacity differently for each rule type, to reflect the relative cost of each rule. Simple rules that cost little to run use fewer WCUs than more complex rules that use more processing power. Rule group capacity is fixed at creation, which helps users plan their web ACL WCU usage when they use a rule group. The WCU limit for web ACLs is 1,500.

ARN (string) --
The Amazon Resource Name (ARN) of the entity.

Description (string) --
A description of the rule group that helps with identification. You cannot change the description of a rule group after you create it.

Rules (list) --
The  Rule statements used to identify the web requests that you want to allow, block, or count. Each rule includes one top-level statement that AWS WAF uses to identify matching web requests, and parameters that govern how AWS WAF handles them.

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

A single rule, which you can use in a  WebACL or  RuleGroup to identify web requests that you want to allow, block, or count. Each rule includes one top-level  Statement that AWS WAF uses to identify matching web requests, and parameters that govern how AWS WAF handles them.

Name (string) --
The name of the rule. You can\'t change the name of a Rule after you create it.

Priority (integer) --
If you define more than one Rule in a WebACL , AWS WAF evaluates each request against the Rules in order based on the value of Priority . AWS WAF processes rules with lower priority first. The priorities don\'t need to be consecutive, but they must all be different.

Statement (dict) --
The AWS WAF processing statement for the rule, for example  ByteMatchStatement or  SizeConstraintStatement .

ByteMatchStatement (dict) --
A rule statement that defines a string match search for AWS WAF to apply to web requests. The byte match statement provides the bytes to search for, the location in requests that you want AWS WAF to search, and other settings. The bytes to search for are typically a string that corresponds with ASCII characters. In the AWS WAF console and the developer guide, this is refered to as a string match statement.

SearchString (bytes) --
A string value that you want AWS WAF to search for. AWS WAF searches only in the part of web requests that you designate for inspection in  FieldToMatch . The maximum length of the value is 50 bytes.
Valid values depend on the component that you specify for inspection in FieldToMatch :

Method : The HTTP method that you want AWS WAF to search for. This indicates the type of operation specified in the request.
UriPath : The value that you want AWS WAF to search for in the URI path, for example, /images/daily-ad.jpg .

If SearchString includes alphabetic characters A-Z and a-z, note that the value is case sensitive.

If you\'re using the AWS WAF API

Specify a base64-encoded version of the value. The maximum length of the value before you base64-encode it is 50 bytes.
For example, suppose the value of Type is HEADER and the value of Data is User-Agent . If you want to search the User-Agent header for the value BadBot , you base64-encode BadBot using MIME base64-encoding and include the resulting value, QmFkQm90 , in the value of SearchString .

If you\'re using the AWS CLI or one of the AWS SDKs

The value that you want AWS WAF to search for. The SDK automatically base64 encodes the value.

FieldToMatch (dict) --
The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .

SingleHeader (dict) --
Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.

Name (string) --
The name of the query header to inspect.



SingleQueryArgument (dict) --
Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.

Name (string) --
The name of the query argument to inspect.



AllQueryArguments (dict) --
Inspect all query arguments.

UriPath (dict) --
Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString (dict) --
Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body (dict) --
Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method (dict) --
Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.



TextTransformations (list) --
Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.

Priority (integer) --
Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.

Type (string) --
You can specify the following transformation types:

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

Specify NONE if you don\'t want any text transformations.





PositionalConstraint (string) --
The area within the portion of a web request that you want AWS WAF to search for SearchString . Valid values include the following:

CONTAINS

The specified part of the web request must include the value of SearchString , but the location doesn\'t matter.

CONTAINS_WORD

The specified part of the web request must include the value of SearchString , and SearchString must contain only alphanumeric characters or underscore (A-Z, a-z, 0-9, or _). In addition, SearchString must be a word, which means that both of the following are true:

SearchString is at the beginning of the specified part of the web request or is preceded by a character other than an alphanumeric character or underscore (_). Examples include the value of a header and ;BadBot .
SearchString is at the end of the specified part of the web request or is followed by a character other than an alphanumeric character or underscore (_), for example, BadBot; and -BadBot; .


EXACTLY

The value of the specified part of the web request must exactly match the value of SearchString .

STARTS_WITH

The value of SearchString must appear at the beginning of the specified part of the web request.

ENDS_WITH

The value of SearchString must appear at the end of the specified part of the web request.



SqliMatchStatement (dict) --
Attackers sometimes insert malicious SQL code into web requests in an effort to extract data from your database. To allow or block web requests that appear to contain malicious SQL code, create one or more SQL injection match conditions. An SQL injection match condition identifies the part of web requests, such as the URI or the query string, that you want AWS WAF to inspect. Later in the process, when you create a web ACL, you specify whether to allow or block requests that appear to contain malicious SQL code.

FieldToMatch (dict) --
The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .

SingleHeader (dict) --
Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.

Name (string) --
The name of the query header to inspect.



SingleQueryArgument (dict) --
Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.

Name (string) --
The name of the query argument to inspect.



AllQueryArguments (dict) --
Inspect all query arguments.

UriPath (dict) --
Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString (dict) --
Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body (dict) --
Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method (dict) --
Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.



TextTransformations (list) --
Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.

Priority (integer) --
Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.

Type (string) --
You can specify the following transformation types:

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

Specify NONE if you don\'t want any text transformations.







XssMatchStatement (dict) --
A rule statement that defines a cross-site scripting (XSS) match search for AWS WAF to apply to web requests. XSS attacks are those where the attacker uses vulnerabilities in a benign website as a vehicle to inject malicious client-site scripts into other legitimate web browsers. The XSS match statement provides the location in requests that you want AWS WAF to search and text transformations to use on the search area before AWS WAF searches for character sequences that are likely to be malicious strings.

FieldToMatch (dict) --
The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .

SingleHeader (dict) --
Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.

Name (string) --
The name of the query header to inspect.



SingleQueryArgument (dict) --
Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.

Name (string) --
The name of the query argument to inspect.



AllQueryArguments (dict) --
Inspect all query arguments.

UriPath (dict) --
Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString (dict) --
Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body (dict) --
Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method (dict) --
Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.



TextTransformations (list) --
Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.

Priority (integer) --
Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.

Type (string) --
You can specify the following transformation types:

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

Specify NONE if you don\'t want any text transformations.







SizeConstraintStatement (dict) --
A rule statement that compares a number of bytes against the size of a request component, using a comparison operator, such as greater than (>) or less than (<). For example, you can use a size constraint statement to look for query strings that are longer than 100 bytes.
If you configure AWS WAF to inspect the request body, AWS WAF inspects only the first 8192 bytes (8 KB). If the request body for your web requests never exceeds 8192 bytes, you can create a size constraint condition and block requests that have a request body greater than 8192 bytes.
If you choose URI for the value of Part of the request to filter on, the slash (/) in the URI counts as one character. For example, the URI /logo.jpg is nine characters long.

FieldToMatch (dict) --
The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .

SingleHeader (dict) --
Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.

Name (string) --
The name of the query header to inspect.



SingleQueryArgument (dict) --
Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.

Name (string) --
The name of the query argument to inspect.



AllQueryArguments (dict) --
Inspect all query arguments.

UriPath (dict) --
Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString (dict) --
Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body (dict) --
Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method (dict) --
Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.



ComparisonOperator (string) --
The operator to use to compare the request part to the size setting.

Size (integer) --
The size, in byte, to compare to the request part, after any transformations.

TextTransformations (list) --
Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.

Priority (integer) --
Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.

Type (string) --
You can specify the following transformation types:

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

Specify NONE if you don\'t want any text transformations.







GeoMatchStatement (dict) --
A rule statement used to identify web requests based on country of origin.

CountryCodes (list) --
An array of two-character country codes, for example, [ "US", "CN" ] , from the alpha-2 country ISO codes of the ISO 3166 international standard.

(string) --




RuleGroupReferenceStatement (dict) --
A rule statement used to run the rules that are defined in a  RuleGroup . To use this, create a rule group with your rules, then provide the ARN of the rule group in this statement.
You cannot nest a RuleGroupReferenceStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.

ARN (string) --
The Amazon Resource Name (ARN) of the entity.

ExcludedRules (list) --
The names of rules that are in the referenced rule group, but that you want AWS WAF to exclude from processing for this rule statement.

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Specifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.

Name (string) --
The name of the rule to exclude.







IPSetReferenceStatement (dict) --
A rule statement used to detect web requests coming from particular IP addresses or address ranges. To use this, create an  IPSet that specifies the addresses you want to detect, then use the ARN of that set in this statement. To create an IP set, see  CreateIPSet .
Each IP set rule statement references an IP set. You create and maintain the set independent of your rules. This allows you to use the single set in multiple rules. When you update the referenced set, AWS WAF automatically updates all rules that reference it.

ARN (string) --
The Amazon Resource Name (ARN) of the  IPSet that this statement references.



RegexPatternSetReferenceStatement (dict) --
A rule statement used to search web request components for matches with regular expressions. To use this, create a  RegexPatternSet that specifies the expressions that you want to detect, then use the ARN of that set in this statement. A web request matches the pattern set rule statement if the request component matches any of the patterns in the set. To create a regex pattern set, see  CreateRegexPatternSet .
Each regex pattern set rule statement references a regex pattern set. You create and maintain the set independent of your rules. This allows you to use the single set in multiple rules. When you update the referenced set, AWS WAF automatically updates all rules that reference it.

ARN (string) --
The Amazon Resource Name (ARN) of the  RegexPatternSet that this statement references.

FieldToMatch (dict) --
The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .

SingleHeader (dict) --
Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.

Name (string) --
The name of the query header to inspect.



SingleQueryArgument (dict) --
Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.

Name (string) --
The name of the query argument to inspect.



AllQueryArguments (dict) --
Inspect all query arguments.

UriPath (dict) --
Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString (dict) --
Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body (dict) --
Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method (dict) --
Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.



TextTransformations (list) --
Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.

Priority (integer) --
Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.

Type (string) --
You can specify the following transformation types:

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

Specify NONE if you don\'t want any text transformations.







RateBasedStatement (dict) --
A rate-based rule tracks the rate of requests for each originating IP address, and triggers the rule action when the rate exceeds a limit that you specify on the number of requests in any 5-minute time span. You can use this to put a temporary block on requests from an IP address that is sending excessive requests.
When the rule action triggers, AWS WAF blocks additional requests from the IP address until the request rate falls below the limit.
You can optionally nest another statement inside the rate-based statement, to narrow the scope of the rule so that it only counts requests that match the nested statement. For example, based on recent requests that you have seen from an attacker, you might create a rate-based rule with a nested AND rule statement that contains the following nested statements:

An IP match statement with an IP set that specified the address 192.0.2.44.
A string match statement that searches in the User-Agent header for the string BadBot.

In this rate-based rule, you also define a rate limit. For this example, the rate limit is 1,000. Requests that meet both of the conditions in the statements are counted. If the count exceeds 1,000 requests per five minutes, the rule action triggers. Requests that do not meet both conditions are not counted towards the rate limit and are not affected by this rule.
You cannot nest a RateBasedStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.

Limit (integer) --
The limit on requests per 5-minute period for a single originating IP address. If the statement includes a ScopDownStatement , this limit is applied only to the requests that match the statement.

AggregateKeyType (string) --
Setting that indicates how to aggregate the request counts. Currently, you must set this to IP . The request counts are aggregated on IP addresses.

ScopeDownStatement (dict) --
An optional nested statement that narrows the scope of the rate-based statement to matching web requests. This can be any nestable statement, and you can nest statements at any level below this scope-down statement.



AndStatement (dict) --
A logical rule statement used to combine other rule statements with AND logic. You provide more than one  Statement within the AndStatement .

Statements (list) --
The statements to combine with AND logic. You can use any statements that can be nested.

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

The processing guidance for a  Rule , used by AWS WAF to determine whether a web request matches the rule.





OrStatement (dict) --
A logical rule statement used to combine other rule statements with OR logic. You provide more than one  Statement within the OrStatement .

Statements (list) --
The statements to combine with OR logic. You can use any statements that can be nested.

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

The processing guidance for a  Rule , used by AWS WAF to determine whether a web request matches the rule.





NotStatement (dict) --
A logical rule statement used to negate the results of another rule statement. You provide one  Statement within the NotStatement .

Statement (dict) --
The statement to negate. You can use any statement that can be nested.



ManagedRuleGroupStatement (dict) --
A rule statement used to run the rules that are defined in a managed rule group. To use this, provide the vendor name and the name of the rule group in this statement. You can retrieve the required names by calling  ListAvailableManagedRuleGroups .
You can\'t nest a ManagedRuleGroupStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.

VendorName (string) --
The name of the managed rule group vendor. You use this, along with the rule group name, to identify the rule group.

Name (string) --
The name of the managed rule group. You use this, along with the vendor name, to identify the rule group.

ExcludedRules (list) --
The rules whose actions are set to COUNT by the web ACL, regardless of the action that is set on the rule. This effectively excludes the rule from acting on web requests.

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Specifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.

Name (string) --
The name of the rule to exclude.









Action (dict) --
The action that AWS WAF should take on a web request when it matches the rule statement. Settings at the web ACL level can override the rule action setting.
This is used only for rules whose statements do not reference a rule group. Rule statements that reference a rule group include RuleGroupReferenceStatement and ManagedRuleGroupStatement .
You must specify either this Action setting or the rule OverrideAction setting, but not both:

If the rule statement does not reference a rule group, use this rule action setting and not the rule override action setting.
If the rule statement references a rule group, use the override action setting and not this action setting.


Block (dict) --
Instructs AWS WAF to block the web request.

Allow (dict) --
Instructs AWS WAF to allow the web request.

Count (dict) --
Instructs AWS WAF to count the web request and allow it.



OverrideAction (dict) --
The override action to apply to the rules in a rule group. Used only for rule statements that reference a rule group, like RuleGroupReferenceStatement and ManagedRuleGroupStatement .
Set the override action to none to leave the rule actions in effect. Set it to count to only count matches, regardless of the rule action settings.
In a  Rule , you must specify either this OverrideAction setting or the rule Action setting, but not both:

If the rule statement references a rule group, use this override action setting and not the action setting.
If the rule statement does not reference a rule group, use the rule action setting and not this rule override action setting.


Count (dict) --
Override the rule action setting to count.

None (dict) --
Don\'t override the rule action setting.



VisibilityConfig (dict) --
Defines and enables Amazon CloudWatch metrics and web request sample collection.

SampledRequestsEnabled (boolean) --
A boolean indicating whether AWS WAF should store a sampling of the web requests that match the rules. You can view the sampled requests through the AWS WAF console.

CloudWatchMetricsEnabled (boolean) --
A boolean indicating whether the associated resource sends metrics to CloudWatch. For the list of available metrics, see AWS WAF Metrics .

MetricName (string) --
A name of the CloudWatch metric. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with length from one to 128 characters. It can\'t contain whitespace or metric names reserved for AWS WAF, for example "All" and "Default_Action." You can\'t change a MetricName after you create a VisibilityConfig .







VisibilityConfig (dict) --
Defines and enables Amazon CloudWatch metrics and web request sample collection.

SampledRequestsEnabled (boolean) --
A boolean indicating whether AWS WAF should store a sampling of the web requests that match the rules. You can view the sampled requests through the AWS WAF console.

CloudWatchMetricsEnabled (boolean) --
A boolean indicating whether the associated resource sends metrics to CloudWatch. For the list of available metrics, see AWS WAF Metrics .

MetricName (string) --
A name of the CloudWatch metric. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with length from one to 128 characters. It can\'t contain whitespace or metric names reserved for AWS WAF, for example "All" and "Default_Action." You can\'t change a MetricName after you create a VisibilityConfig .





LockToken (string) --
A token used for optimistic locking. AWS WAF returns a token to your get and list requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like update and delete. AWS WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a WAFOptimisticLockException . If this happens, perform another get, and use the new token returned by that operation.







Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFNonexistentItemException
WAFV2.Client.exceptions.WAFInvalidOperationException


    :return: {
        'RuleGroup': {
            'Name': 'string',
            'Id': 'string',
            'Capacity': 123,
            'ARN': 'string',
            'Description': 'string',
            'Rules': [
                {
                    'Name': 'string',
                    'Priority': 123,
                    'Statement': {
                        'ByteMatchStatement': {
                            'SearchString': b'bytes',
                            'FieldToMatch': {
                                'SingleHeader': {
                                    'Name': 'string'
                                },
                                'SingleQueryArgument': {
                                    'Name': 'string'
                                },
                                'AllQueryArguments': {},
                                'UriPath': {},
                                'QueryString': {},
                                'Body': {},
                                'Method': {}
                            },
                            'TextTransformations': [
                                {
                                    'Priority': 123,
                                    'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                                },
                            ],
                            'PositionalConstraint': 'EXACTLY'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CONTAINS_WORD'
                        },
                        'SqliMatchStatement': {
                            'FieldToMatch': {
                                'SingleHeader': {
                                    'Name': 'string'
                                },
                                'SingleQueryArgument': {
                                    'Name': 'string'
                                },
                                'AllQueryArguments': {},
                                'UriPath': {},
                                'QueryString': {},
                                'Body': {},
                                'Method': {}
                            },
                            'TextTransformations': [
                                {
                                    'Priority': 123,
                                    'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                                },
                            ]
                        },
                        'XssMatchStatement': {
                            'FieldToMatch': {
                                'SingleHeader': {
                                    'Name': 'string'
                                },
                                'SingleQueryArgument': {
                                    'Name': 'string'
                                },
                                'AllQueryArguments': {},
                                'UriPath': {},
                                'QueryString': {},
                                'Body': {},
                                'Method': {}
                            },
                            'TextTransformations': [
                                {
                                    'Priority': 123,
                                    'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                                },
                            ]
                        },
                        'SizeConstraintStatement': {
                            'FieldToMatch': {
                                'SingleHeader': {
                                    'Name': 'string'
                                },
                                'SingleQueryArgument': {
                                    'Name': 'string'
                                },
                                'AllQueryArguments': {},
                                'UriPath': {},
                                'QueryString': {},
                                'Body': {},
                                'Method': {}
                            },
                            'ComparisonOperator': 'EQ'|'NE'|'LE'|'LT'|'GE'|'GT',
                            'Size': 123,
                            'TextTransformations': [
                                {
                                    'Priority': 123,
                                    'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                                },
                            ]
                        },
                        'GeoMatchStatement': {
                            'CountryCodes': [
                                'AF'|'AX'|'AL'|'DZ'|'AS'|'AD'|'AO'|'AI'|'AQ'|'AG'|'AR'|'AM'|'AW'|'AU'|'AT'|'AZ'|'BS'|'BH'|'BD'|'BB'|'BY'|'BE'|'BZ'|'BJ'|'BM'|'BT'|'BO'|'BQ'|'BA'|'BW'|'BV'|'BR'|'IO'|'BN'|'BG'|'BF'|'BI'|'KH'|'CM'|'CA'|'CV'|'KY'|'CF'|'TD'|'CL'|'CN'|'CX'|'CC'|'CO'|'KM'|'CG'|'CD'|'CK'|'CR'|'CI'|'HR'|'CU'|'CW'|'CY'|'CZ'|'DK'|'DJ'|'DM'|'DO'|'EC'|'EG'|'SV'|'GQ'|'ER'|'EE'|'ET'|'FK'|'FO'|'FJ'|'FI'|'FR'|'GF'|'PF'|'TF'|'GA'|'GM'|'GE'|'DE'|'GH'|'GI'|'GR'|'GL'|'GD'|'GP'|'GU'|'GT'|'GG'|'GN'|'GW'|'GY'|'HT'|'HM'|'VA'|'HN'|'HK'|'HU'|'IS'|'IN'|'ID'|'IR'|'IQ'|'IE'|'IM'|'IL'|'IT'|'JM'|'JP'|'JE'|'JO'|'KZ'|'KE'|'KI'|'KP'|'KR'|'KW'|'KG'|'LA'|'LV'|'LB'|'LS'|'LR'|'LY'|'LI'|'LT'|'LU'|'MO'|'MK'|'MG'|'MW'|'MY'|'MV'|'ML'|'MT'|'MH'|'MQ'|'MR'|'MU'|'YT'|'MX'|'FM'|'MD'|'MC'|'MN'|'ME'|'MS'|'MA'|'MZ'|'MM'|'NA'|'NR'|'NP'|'NL'|'NC'|'NZ'|'NI'|'NE'|'NG'|'NU'|'NF'|'MP'|'NO'|'OM'|'PK'|'PW'|'PS'|'PA'|'PG'|'PY'|'PE'|'PH'|'PN'|'PL'|'PT'|'PR'|'QA'|'RE'|'RO'|'RU'|'RW'|'BL'|'SH'|'KN'|'LC'|'MF'|'PM'|'VC'|'WS'|'SM'|'ST'|'SA'|'SN'|'RS'|'SC'|'SL'|'SG'|'SX'|'SK'|'SI'|'SB'|'SO'|'ZA'|'GS'|'SS'|'ES'|'LK'|'SD'|'SR'|'SJ'|'SZ'|'SE'|'CH'|'SY'|'TW'|'TJ'|'TZ'|'TH'|'TL'|'TG'|'TK'|'TO'|'TT'|'TN'|'TR'|'TM'|'TC'|'TV'|'UG'|'UA'|'AE'|'GB'|'US'|'UM'|'UY'|'UZ'|'VU'|'VE'|'VN'|'VG'|'VI'|'WF'|'EH'|'YE'|'ZM'|'ZW',
                            ]
                        },
                        'RuleGroupReferenceStatement': {
                            'ARN': 'string',
                            'ExcludedRules': [
                                {
                                    'Name': 'string'
                                },
                            ]
                        },
                        'IPSetReferenceStatement': {
                            'ARN': 'string'
                        },
                        'RegexPatternSetReferenceStatement': {
                            'ARN': 'string',
                            'FieldToMatch': {
                                'SingleHeader': {
                                    'Name': 'string'
                                },
                                'SingleQueryArgument': {
                                    'Name': 'string'
                                },
                                'AllQueryArguments': {},
                                'UriPath': {},
                                'QueryString': {},
                                'Body': {},
                                'Method': {}
                            },
                            'TextTransformations': [
                                {
                                    'Priority': 123,
                                    'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                                },
                            ]
                        },
                        'RateBasedStatement': {
                            'Limit': 123,
                            'AggregateKeyType': 'IP',
                            'ScopeDownStatement': {'... recursive ...'}
                        },
                        'AndStatement': {
                            'Statements': [
                                {'... recursive ...'},
                            ]
                        },
                        'OrStatement': {
                            'Statements': [
                                {'... recursive ...'},
                            ]
                        },
                        'NotStatement': {
                            'Statement': {'... recursive ...'}
                        },
                        'ManagedRuleGroupStatement': {
                            'VendorName': 'string',
                            'Name': 'string',
                            'ExcludedRules': [
                                {
                                    'Name': 'string'
                                },
                            ]
                        }
                    },
                    'Action': {
                        'Block': {},
                        'Allow': {},
                        'Count': {}
                    },
                    'OverrideAction': {
                        'Count': {},
                        'None': {}
                    },
                    'VisibilityConfig': {
                        'SampledRequestsEnabled': True|False,
                        'CloudWatchMetricsEnabled': True|False,
                        'MetricName': 'string'
                    }
                },
            ],
            'VisibilityConfig': {
                'SampledRequestsEnabled': True|False,
                'CloudWatchMetricsEnabled': True|False,
                'MetricName': 'string'
            }
        },
        'LockToken': 'string'
    }
    
    
    :returns: 
    Method : The HTTP method that you want AWS WAF to search for. This indicates the type of operation specified in the request.
    UriPath : The value that you want AWS WAF to search for in the URI path, for example, /images/daily-ad.jpg .
    
    """
    pass

def get_sampled_requests(WebAclArn=None, RuleMetricName=None, Scope=None, TimeWindow=None, MaxItems=None):
    """
    Gets detailed information about a specified number of requests--a sample--that AWS WAF randomly selects from among the first 5,000 requests that your AWS resource received during a time range that you choose. You can specify a sample size of up to 500 requests, and you can specify any time range in the previous three hours.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_sampled_requests(
        WebAclArn='string',
        RuleMetricName='string',
        Scope='CLOUDFRONT'|'REGIONAL',
        TimeWindow={
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1)
        },
        MaxItems=123
    )
    
    
    :type WebAclArn: string
    :param WebAclArn: [REQUIRED]\nThe Amazon resource name (ARN) of the WebACL for which you want a sample of requests.\n

    :type RuleMetricName: string
    :param RuleMetricName: [REQUIRED]\nThe metric name assigned to the Rule or RuleGroup for which you want a sample of requests.\n

    :type Scope: string
    :param Scope: [REQUIRED]\nSpecifies whether this is for an AWS CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB) or an API Gateway stage.\nTo work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:\n\nCLI - Specify the Region when you use the CloudFront scope: --scope=CLOUDFRONT --region=us-east-1 .\nAPI and SDKs - For all calls, use the Region endpoint us-east-1.\n\n

    :type TimeWindow: dict
    :param TimeWindow: [REQUIRED]\nThe start date and time and the end date and time of the range for which you want GetSampledRequests to return a sample of requests. Specify the date and time in the following format: '2016-09-27T14:50Z' . You can specify any time range in the previous three hours.\n\nStartTime (datetime) -- [REQUIRED]The beginning of the time range from which you want GetSampledRequests to return a sample of the requests that your AWS resource received. Specify the date and time in the following format: '2016-09-27T14:50Z' . You can specify any time range in the previous three hours.\n\nEndTime (datetime) -- [REQUIRED]The end of the time range from which you want GetSampledRequests to return a sample of the requests that your AWS resource received. Specify the date and time in the following format: '2016-09-27T14:50Z' . You can specify any time range in the previous three hours.\n\n\n

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
            'RuleNameWithinRuleGroup': 'string'
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
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Represents a single sampled web request. The response from  GetSampledRequests includes a SampledHTTPRequests complex type that appears as SampledRequests in the response syntax. SampledHTTPRequests contains an array of SampledHTTPRequest objects.

Request (dict) --
A complex type that contains detailed information about the request.

ClientIP (string) --
The IP address that the request originated from. If the web ACL is associated with a CloudFront distribution, this is the value of one of the following fields in CloudFront access logs:

c-ip , if the viewer did not use an HTTP proxy or a load balancer to send the request
x-forwarded-for , if the viewer did use an HTTP proxy or a load balancer to send the request


Country (string) --
The two-letter country code for the country that the request originated from. For a current list of country codes, see the Wikipedia entry ISO 3166-1 alpha-2 .

URI (string) --
The URI path of the request, which identifies the resource, for example, /images/daily-ad.jpg .

Method (string) --
The HTTP method specified in the sampled web request.

HTTPVersion (string) --
The HTTP version specified in the sampled web request, for example, HTTP/1.1 .

Headers (list) --
A complex type that contains the name and value for each header in the sampled web request.

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Part of the response from  GetSampledRequests . This is a complex type that appears as Headers in the response syntax. HTTPHeader contains the names and values of all of the headers that appear in one of the web requests.

Name (string) --
The name of the HTTP header.

Value (string) --
The value of the HTTP header.







Weight (integer) --
A value that indicates how one result in the response relates proportionally to other results in the response. For example, a result that has a weight of 2 represents roughly twice as many web requests as a result that has a weight of 1 .

Timestamp (datetime) --
The time at which AWS WAF received the request from your AWS resource, in Unix time format (in seconds).

Action (string) --
The action for the Rule that the request matched: ALLOW , BLOCK , or COUNT .

RuleNameWithinRuleGroup (string) --
The name of the Rule that the request matched. For managed rule groups, the format for this name is <vendor name>#<managed rule group name>#<rule name> . For your own rule groups, the format for this name is <rule group name>#<rule name> . If the rule is not in a rule group, the format is <rule name> .





PopulationSize (integer) --
The total number of requests from which GetSampledRequests got a sample of MaxItems requests. If PopulationSize is less than MaxItems , the sample includes every request that your AWS resource received during the specified time range.

TimeWindow (dict) --
Usually, TimeWindow is the time range that you specified in the GetSampledRequests request. However, if your AWS resource received more than 5,000 requests during the time range that you specified in the request, GetSampledRequests returns the time range for the first 5,000 requests.

StartTime (datetime) --
The beginning of the time range from which you want GetSampledRequests to return a sample of the requests that your AWS resource received. Specify the date and time in the following format: "2016-09-27T14:50Z" . You can specify any time range in the previous three hours.

EndTime (datetime) --
The end of the time range from which you want GetSampledRequests to return a sample of the requests that your AWS resource received. Specify the date and time in the following format: "2016-09-27T14:50Z" . You can specify any time range in the previous three hours.









Exceptions

WAFV2.Client.exceptions.WAFNonexistentItemException
WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException


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
                'RuleNameWithinRuleGroup': 'string'
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

def get_waiter(waiter_name=None):
    """
    Returns an object that can wait for some condition.
    
    :type waiter_name: str
    :param waiter_name: The name of the waiter to get. See the waiters\nsection of the service docs for a list of available waiters.

    :rtype: botocore.waiter.Waiter


    """
    pass

def get_web_acl(Name=None, Scope=None, Id=None):
    """
    Retrieves the specified  WebACL .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_web_acl(
        Name='string',
        Scope='CLOUDFRONT'|'REGIONAL',
        Id='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the Web ACL. You cannot change the name of a Web ACL after you create it.\n

    :type Scope: string
    :param Scope: [REQUIRED]\nSpecifies whether this is for an AWS CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB) or an API Gateway stage.\nTo work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:\n\nCLI - Specify the Region when you use the CloudFront scope: --scope=CLOUDFRONT --region=us-east-1 .\nAPI and SDKs - For all calls, use the Region endpoint us-east-1.\n\n

    :type Id: string
    :param Id: [REQUIRED]\nThe unique identifier for the Web ACL. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'WebACL': {
        'Name': 'string',
        'Id': 'string',
        'ARN': 'string',
        'DefaultAction': {
            'Block': {},
            'Allow': {}
        },
        'Description': 'string',
        'Rules': [
            {
                'Name': 'string',
                'Priority': 123,
                'Statement': {
                    'ByteMatchStatement': {
                        'SearchString': b'bytes',
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {},
                            'UriPath': {},
                            'QueryString': {},
                            'Body': {},
                            'Method': {}
                        },
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ],
                        'PositionalConstraint': 'EXACTLY'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CONTAINS_WORD'
                    },
                    'SqliMatchStatement': {
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {},
                            'UriPath': {},
                            'QueryString': {},
                            'Body': {},
                            'Method': {}
                        },
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ]
                    },
                    'XssMatchStatement': {
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {},
                            'UriPath': {},
                            'QueryString': {},
                            'Body': {},
                            'Method': {}
                        },
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ]
                    },
                    'SizeConstraintStatement': {
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {},
                            'UriPath': {},
                            'QueryString': {},
                            'Body': {},
                            'Method': {}
                        },
                        'ComparisonOperator': 'EQ'|'NE'|'LE'|'LT'|'GE'|'GT',
                        'Size': 123,
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ]
                    },
                    'GeoMatchStatement': {
                        'CountryCodes': [
                            'AF'|'AX'|'AL'|'DZ'|'AS'|'AD'|'AO'|'AI'|'AQ'|'AG'|'AR'|'AM'|'AW'|'AU'|'AT'|'AZ'|'BS'|'BH'|'BD'|'BB'|'BY'|'BE'|'BZ'|'BJ'|'BM'|'BT'|'BO'|'BQ'|'BA'|'BW'|'BV'|'BR'|'IO'|'BN'|'BG'|'BF'|'BI'|'KH'|'CM'|'CA'|'CV'|'KY'|'CF'|'TD'|'CL'|'CN'|'CX'|'CC'|'CO'|'KM'|'CG'|'CD'|'CK'|'CR'|'CI'|'HR'|'CU'|'CW'|'CY'|'CZ'|'DK'|'DJ'|'DM'|'DO'|'EC'|'EG'|'SV'|'GQ'|'ER'|'EE'|'ET'|'FK'|'FO'|'FJ'|'FI'|'FR'|'GF'|'PF'|'TF'|'GA'|'GM'|'GE'|'DE'|'GH'|'GI'|'GR'|'GL'|'GD'|'GP'|'GU'|'GT'|'GG'|'GN'|'GW'|'GY'|'HT'|'HM'|'VA'|'HN'|'HK'|'HU'|'IS'|'IN'|'ID'|'IR'|'IQ'|'IE'|'IM'|'IL'|'IT'|'JM'|'JP'|'JE'|'JO'|'KZ'|'KE'|'KI'|'KP'|'KR'|'KW'|'KG'|'LA'|'LV'|'LB'|'LS'|'LR'|'LY'|'LI'|'LT'|'LU'|'MO'|'MK'|'MG'|'MW'|'MY'|'MV'|'ML'|'MT'|'MH'|'MQ'|'MR'|'MU'|'YT'|'MX'|'FM'|'MD'|'MC'|'MN'|'ME'|'MS'|'MA'|'MZ'|'MM'|'NA'|'NR'|'NP'|'NL'|'NC'|'NZ'|'NI'|'NE'|'NG'|'NU'|'NF'|'MP'|'NO'|'OM'|'PK'|'PW'|'PS'|'PA'|'PG'|'PY'|'PE'|'PH'|'PN'|'PL'|'PT'|'PR'|'QA'|'RE'|'RO'|'RU'|'RW'|'BL'|'SH'|'KN'|'LC'|'MF'|'PM'|'VC'|'WS'|'SM'|'ST'|'SA'|'SN'|'RS'|'SC'|'SL'|'SG'|'SX'|'SK'|'SI'|'SB'|'SO'|'ZA'|'GS'|'SS'|'ES'|'LK'|'SD'|'SR'|'SJ'|'SZ'|'SE'|'CH'|'SY'|'TW'|'TJ'|'TZ'|'TH'|'TL'|'TG'|'TK'|'TO'|'TT'|'TN'|'TR'|'TM'|'TC'|'TV'|'UG'|'UA'|'AE'|'GB'|'US'|'UM'|'UY'|'UZ'|'VU'|'VE'|'VN'|'VG'|'VI'|'WF'|'EH'|'YE'|'ZM'|'ZW',
                        ]
                    },
                    'RuleGroupReferenceStatement': {
                        'ARN': 'string',
                        'ExcludedRules': [
                            {
                                'Name': 'string'
                            },
                        ]
                    },
                    'IPSetReferenceStatement': {
                        'ARN': 'string'
                    },
                    'RegexPatternSetReferenceStatement': {
                        'ARN': 'string',
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {},
                            'UriPath': {},
                            'QueryString': {},
                            'Body': {},
                            'Method': {}
                        },
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ]
                    },
                    'RateBasedStatement': {
                        'Limit': 123,
                        'AggregateKeyType': 'IP',
                        'ScopeDownStatement': {'... recursive ...'}
                    },
                    'AndStatement': {
                        'Statements': [
                            {'... recursive ...'},
                        ]
                    },
                    'OrStatement': {
                        'Statements': [
                            {'... recursive ...'},
                        ]
                    },
                    'NotStatement': {
                        'Statement': {'... recursive ...'}
                    },
                    'ManagedRuleGroupStatement': {
                        'VendorName': 'string',
                        'Name': 'string',
                        'ExcludedRules': [
                            {
                                'Name': 'string'
                            },
                        ]
                    }
                },
                'Action': {
                    'Block': {},
                    'Allow': {},
                    'Count': {}
                },
                'OverrideAction': {
                    'Count': {},
                    'None': {}
                },
                'VisibilityConfig': {
                    'SampledRequestsEnabled': True|False,
                    'CloudWatchMetricsEnabled': True|False,
                    'MetricName': 'string'
                }
            },
        ],
        'VisibilityConfig': {
            'SampledRequestsEnabled': True|False,
            'CloudWatchMetricsEnabled': True|False,
            'MetricName': 'string'
        },
        'Capacity': 123,
        'PreProcessFirewallManagerRuleGroups': [
            {
                'Name': 'string',
                'Priority': 123,
                'FirewallManagerStatement': {
                    'ManagedRuleGroupStatement': {
                        'VendorName': 'string',
                        'Name': 'string',
                        'ExcludedRules': [
                            {
                                'Name': 'string'
                            },
                        ]
                    },
                    'RuleGroupReferenceStatement': {
                        'ARN': 'string',
                        'ExcludedRules': [
                            {
                                'Name': 'string'
                            },
                        ]
                    }
                },
                'OverrideAction': {
                    'Count': {},
                    'None': {}
                },
                'VisibilityConfig': {
                    'SampledRequestsEnabled': True|False,
                    'CloudWatchMetricsEnabled': True|False,
                    'MetricName': 'string'
                }
            },
        ],
        'PostProcessFirewallManagerRuleGroups': [
            {
                'Name': 'string',
                'Priority': 123,
                'FirewallManagerStatement': {
                    'ManagedRuleGroupStatement': {
                        'VendorName': 'string',
                        'Name': 'string',
                        'ExcludedRules': [
                            {
                                'Name': 'string'
                            },
                        ]
                    },
                    'RuleGroupReferenceStatement': {
                        'ARN': 'string',
                        'ExcludedRules': [
                            {
                                'Name': 'string'
                            },
                        ]
                    }
                },
                'OverrideAction': {
                    'Count': {},
                    'None': {}
                },
                'VisibilityConfig': {
                    'SampledRequestsEnabled': True|False,
                    'CloudWatchMetricsEnabled': True|False,
                    'MetricName': 'string'
                }
            },
        ],
        'ManagedByFirewallManager': True|False
    },
    'LockToken': 'string'
}


Response Structure

(dict) --

WebACL (dict) --
The Web ACL specification. You can modify the settings in this Web ACL and use it to update this Web ACL or create a new one.

Name (string) --
The name of the Web ACL. You cannot change the name of a Web ACL after you create it.

Id (string) --
A unique identifier for the WebACL . This ID is returned in the responses to create and list commands. You use this ID to do things like get, update, and delete a WebACL .

ARN (string) --
The Amazon Resource Name (ARN) of the Web ACL that you want to associate with the resource.

DefaultAction (dict) --
The action to perform if none of the Rules contained in the WebACL match.

Block (dict) --
Specifies that AWS WAF should block requests by default.

Allow (dict) --
Specifies that AWS WAF should allow requests by default.



Description (string) --
A description of the Web ACL that helps with identification. You cannot change the description of a Web ACL after you create it.

Rules (list) --
The  Rule statements used to identify the web requests that you want to allow, block, or count. Each rule includes one top-level statement that AWS WAF uses to identify matching web requests, and parameters that govern how AWS WAF handles them.

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

A single rule, which you can use in a  WebACL or  RuleGroup to identify web requests that you want to allow, block, or count. Each rule includes one top-level  Statement that AWS WAF uses to identify matching web requests, and parameters that govern how AWS WAF handles them.

Name (string) --
The name of the rule. You can\'t change the name of a Rule after you create it.

Priority (integer) --
If you define more than one Rule in a WebACL , AWS WAF evaluates each request against the Rules in order based on the value of Priority . AWS WAF processes rules with lower priority first. The priorities don\'t need to be consecutive, but they must all be different.

Statement (dict) --
The AWS WAF processing statement for the rule, for example  ByteMatchStatement or  SizeConstraintStatement .

ByteMatchStatement (dict) --
A rule statement that defines a string match search for AWS WAF to apply to web requests. The byte match statement provides the bytes to search for, the location in requests that you want AWS WAF to search, and other settings. The bytes to search for are typically a string that corresponds with ASCII characters. In the AWS WAF console and the developer guide, this is refered to as a string match statement.

SearchString (bytes) --
A string value that you want AWS WAF to search for. AWS WAF searches only in the part of web requests that you designate for inspection in  FieldToMatch . The maximum length of the value is 50 bytes.
Valid values depend on the component that you specify for inspection in FieldToMatch :

Method : The HTTP method that you want AWS WAF to search for. This indicates the type of operation specified in the request.
UriPath : The value that you want AWS WAF to search for in the URI path, for example, /images/daily-ad.jpg .

If SearchString includes alphabetic characters A-Z and a-z, note that the value is case sensitive.

If you\'re using the AWS WAF API

Specify a base64-encoded version of the value. The maximum length of the value before you base64-encode it is 50 bytes.
For example, suppose the value of Type is HEADER and the value of Data is User-Agent . If you want to search the User-Agent header for the value BadBot , you base64-encode BadBot using MIME base64-encoding and include the resulting value, QmFkQm90 , in the value of SearchString .

If you\'re using the AWS CLI or one of the AWS SDKs

The value that you want AWS WAF to search for. The SDK automatically base64 encodes the value.

FieldToMatch (dict) --
The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .

SingleHeader (dict) --
Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.

Name (string) --
The name of the query header to inspect.



SingleQueryArgument (dict) --
Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.

Name (string) --
The name of the query argument to inspect.



AllQueryArguments (dict) --
Inspect all query arguments.

UriPath (dict) --
Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString (dict) --
Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body (dict) --
Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method (dict) --
Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.



TextTransformations (list) --
Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.

Priority (integer) --
Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.

Type (string) --
You can specify the following transformation types:

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

Specify NONE if you don\'t want any text transformations.





PositionalConstraint (string) --
The area within the portion of a web request that you want AWS WAF to search for SearchString . Valid values include the following:

CONTAINS

The specified part of the web request must include the value of SearchString , but the location doesn\'t matter.

CONTAINS_WORD

The specified part of the web request must include the value of SearchString , and SearchString must contain only alphanumeric characters or underscore (A-Z, a-z, 0-9, or _). In addition, SearchString must be a word, which means that both of the following are true:

SearchString is at the beginning of the specified part of the web request or is preceded by a character other than an alphanumeric character or underscore (_). Examples include the value of a header and ;BadBot .
SearchString is at the end of the specified part of the web request or is followed by a character other than an alphanumeric character or underscore (_), for example, BadBot; and -BadBot; .


EXACTLY

The value of the specified part of the web request must exactly match the value of SearchString .

STARTS_WITH

The value of SearchString must appear at the beginning of the specified part of the web request.

ENDS_WITH

The value of SearchString must appear at the end of the specified part of the web request.



SqliMatchStatement (dict) --
Attackers sometimes insert malicious SQL code into web requests in an effort to extract data from your database. To allow or block web requests that appear to contain malicious SQL code, create one or more SQL injection match conditions. An SQL injection match condition identifies the part of web requests, such as the URI or the query string, that you want AWS WAF to inspect. Later in the process, when you create a web ACL, you specify whether to allow or block requests that appear to contain malicious SQL code.

FieldToMatch (dict) --
The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .

SingleHeader (dict) --
Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.

Name (string) --
The name of the query header to inspect.



SingleQueryArgument (dict) --
Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.

Name (string) --
The name of the query argument to inspect.



AllQueryArguments (dict) --
Inspect all query arguments.

UriPath (dict) --
Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString (dict) --
Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body (dict) --
Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method (dict) --
Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.



TextTransformations (list) --
Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.

Priority (integer) --
Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.

Type (string) --
You can specify the following transformation types:

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

Specify NONE if you don\'t want any text transformations.







XssMatchStatement (dict) --
A rule statement that defines a cross-site scripting (XSS) match search for AWS WAF to apply to web requests. XSS attacks are those where the attacker uses vulnerabilities in a benign website as a vehicle to inject malicious client-site scripts into other legitimate web browsers. The XSS match statement provides the location in requests that you want AWS WAF to search and text transformations to use on the search area before AWS WAF searches for character sequences that are likely to be malicious strings.

FieldToMatch (dict) --
The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .

SingleHeader (dict) --
Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.

Name (string) --
The name of the query header to inspect.



SingleQueryArgument (dict) --
Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.

Name (string) --
The name of the query argument to inspect.



AllQueryArguments (dict) --
Inspect all query arguments.

UriPath (dict) --
Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString (dict) --
Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body (dict) --
Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method (dict) --
Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.



TextTransformations (list) --
Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.

Priority (integer) --
Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.

Type (string) --
You can specify the following transformation types:

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

Specify NONE if you don\'t want any text transformations.







SizeConstraintStatement (dict) --
A rule statement that compares a number of bytes against the size of a request component, using a comparison operator, such as greater than (>) or less than (<). For example, you can use a size constraint statement to look for query strings that are longer than 100 bytes.
If you configure AWS WAF to inspect the request body, AWS WAF inspects only the first 8192 bytes (8 KB). If the request body for your web requests never exceeds 8192 bytes, you can create a size constraint condition and block requests that have a request body greater than 8192 bytes.
If you choose URI for the value of Part of the request to filter on, the slash (/) in the URI counts as one character. For example, the URI /logo.jpg is nine characters long.

FieldToMatch (dict) --
The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .

SingleHeader (dict) --
Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.

Name (string) --
The name of the query header to inspect.



SingleQueryArgument (dict) --
Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.

Name (string) --
The name of the query argument to inspect.



AllQueryArguments (dict) --
Inspect all query arguments.

UriPath (dict) --
Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString (dict) --
Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body (dict) --
Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method (dict) --
Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.



ComparisonOperator (string) --
The operator to use to compare the request part to the size setting.

Size (integer) --
The size, in byte, to compare to the request part, after any transformations.

TextTransformations (list) --
Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.

Priority (integer) --
Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.

Type (string) --
You can specify the following transformation types:

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

Specify NONE if you don\'t want any text transformations.







GeoMatchStatement (dict) --
A rule statement used to identify web requests based on country of origin.

CountryCodes (list) --
An array of two-character country codes, for example, [ "US", "CN" ] , from the alpha-2 country ISO codes of the ISO 3166 international standard.

(string) --




RuleGroupReferenceStatement (dict) --
A rule statement used to run the rules that are defined in a  RuleGroup . To use this, create a rule group with your rules, then provide the ARN of the rule group in this statement.
You cannot nest a RuleGroupReferenceStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.

ARN (string) --
The Amazon Resource Name (ARN) of the entity.

ExcludedRules (list) --
The names of rules that are in the referenced rule group, but that you want AWS WAF to exclude from processing for this rule statement.

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Specifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.

Name (string) --
The name of the rule to exclude.







IPSetReferenceStatement (dict) --
A rule statement used to detect web requests coming from particular IP addresses or address ranges. To use this, create an  IPSet that specifies the addresses you want to detect, then use the ARN of that set in this statement. To create an IP set, see  CreateIPSet .
Each IP set rule statement references an IP set. You create and maintain the set independent of your rules. This allows you to use the single set in multiple rules. When you update the referenced set, AWS WAF automatically updates all rules that reference it.

ARN (string) --
The Amazon Resource Name (ARN) of the  IPSet that this statement references.



RegexPatternSetReferenceStatement (dict) --
A rule statement used to search web request components for matches with regular expressions. To use this, create a  RegexPatternSet that specifies the expressions that you want to detect, then use the ARN of that set in this statement. A web request matches the pattern set rule statement if the request component matches any of the patterns in the set. To create a regex pattern set, see  CreateRegexPatternSet .
Each regex pattern set rule statement references a regex pattern set. You create and maintain the set independent of your rules. This allows you to use the single set in multiple rules. When you update the referenced set, AWS WAF automatically updates all rules that reference it.

ARN (string) --
The Amazon Resource Name (ARN) of the  RegexPatternSet that this statement references.

FieldToMatch (dict) --
The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .

SingleHeader (dict) --
Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.

Name (string) --
The name of the query header to inspect.



SingleQueryArgument (dict) --
Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.

Name (string) --
The name of the query argument to inspect.



AllQueryArguments (dict) --
Inspect all query arguments.

UriPath (dict) --
Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString (dict) --
Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body (dict) --
Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method (dict) --
Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.



TextTransformations (list) --
Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.

Priority (integer) --
Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.

Type (string) --
You can specify the following transformation types:

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

Specify NONE if you don\'t want any text transformations.







RateBasedStatement (dict) --
A rate-based rule tracks the rate of requests for each originating IP address, and triggers the rule action when the rate exceeds a limit that you specify on the number of requests in any 5-minute time span. You can use this to put a temporary block on requests from an IP address that is sending excessive requests.
When the rule action triggers, AWS WAF blocks additional requests from the IP address until the request rate falls below the limit.
You can optionally nest another statement inside the rate-based statement, to narrow the scope of the rule so that it only counts requests that match the nested statement. For example, based on recent requests that you have seen from an attacker, you might create a rate-based rule with a nested AND rule statement that contains the following nested statements:

An IP match statement with an IP set that specified the address 192.0.2.44.
A string match statement that searches in the User-Agent header for the string BadBot.

In this rate-based rule, you also define a rate limit. For this example, the rate limit is 1,000. Requests that meet both of the conditions in the statements are counted. If the count exceeds 1,000 requests per five minutes, the rule action triggers. Requests that do not meet both conditions are not counted towards the rate limit and are not affected by this rule.
You cannot nest a RateBasedStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.

Limit (integer) --
The limit on requests per 5-minute period for a single originating IP address. If the statement includes a ScopDownStatement , this limit is applied only to the requests that match the statement.

AggregateKeyType (string) --
Setting that indicates how to aggregate the request counts. Currently, you must set this to IP . The request counts are aggregated on IP addresses.

ScopeDownStatement (dict) --
An optional nested statement that narrows the scope of the rate-based statement to matching web requests. This can be any nestable statement, and you can nest statements at any level below this scope-down statement.



AndStatement (dict) --
A logical rule statement used to combine other rule statements with AND logic. You provide more than one  Statement within the AndStatement .

Statements (list) --
The statements to combine with AND logic. You can use any statements that can be nested.

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

The processing guidance for a  Rule , used by AWS WAF to determine whether a web request matches the rule.





OrStatement (dict) --
A logical rule statement used to combine other rule statements with OR logic. You provide more than one  Statement within the OrStatement .

Statements (list) --
The statements to combine with OR logic. You can use any statements that can be nested.

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

The processing guidance for a  Rule , used by AWS WAF to determine whether a web request matches the rule.





NotStatement (dict) --
A logical rule statement used to negate the results of another rule statement. You provide one  Statement within the NotStatement .

Statement (dict) --
The statement to negate. You can use any statement that can be nested.



ManagedRuleGroupStatement (dict) --
A rule statement used to run the rules that are defined in a managed rule group. To use this, provide the vendor name and the name of the rule group in this statement. You can retrieve the required names by calling  ListAvailableManagedRuleGroups .
You can\'t nest a ManagedRuleGroupStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.

VendorName (string) --
The name of the managed rule group vendor. You use this, along with the rule group name, to identify the rule group.

Name (string) --
The name of the managed rule group. You use this, along with the vendor name, to identify the rule group.

ExcludedRules (list) --
The rules whose actions are set to COUNT by the web ACL, regardless of the action that is set on the rule. This effectively excludes the rule from acting on web requests.

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Specifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.

Name (string) --
The name of the rule to exclude.









Action (dict) --
The action that AWS WAF should take on a web request when it matches the rule statement. Settings at the web ACL level can override the rule action setting.
This is used only for rules whose statements do not reference a rule group. Rule statements that reference a rule group include RuleGroupReferenceStatement and ManagedRuleGroupStatement .
You must specify either this Action setting or the rule OverrideAction setting, but not both:

If the rule statement does not reference a rule group, use this rule action setting and not the rule override action setting.
If the rule statement references a rule group, use the override action setting and not this action setting.


Block (dict) --
Instructs AWS WAF to block the web request.

Allow (dict) --
Instructs AWS WAF to allow the web request.

Count (dict) --
Instructs AWS WAF to count the web request and allow it.



OverrideAction (dict) --
The override action to apply to the rules in a rule group. Used only for rule statements that reference a rule group, like RuleGroupReferenceStatement and ManagedRuleGroupStatement .
Set the override action to none to leave the rule actions in effect. Set it to count to only count matches, regardless of the rule action settings.
In a  Rule , you must specify either this OverrideAction setting or the rule Action setting, but not both:

If the rule statement references a rule group, use this override action setting and not the action setting.
If the rule statement does not reference a rule group, use the rule action setting and not this rule override action setting.


Count (dict) --
Override the rule action setting to count.

None (dict) --
Don\'t override the rule action setting.



VisibilityConfig (dict) --
Defines and enables Amazon CloudWatch metrics and web request sample collection.

SampledRequestsEnabled (boolean) --
A boolean indicating whether AWS WAF should store a sampling of the web requests that match the rules. You can view the sampled requests through the AWS WAF console.

CloudWatchMetricsEnabled (boolean) --
A boolean indicating whether the associated resource sends metrics to CloudWatch. For the list of available metrics, see AWS WAF Metrics .

MetricName (string) --
A name of the CloudWatch metric. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with length from one to 128 characters. It can\'t contain whitespace or metric names reserved for AWS WAF, for example "All" and "Default_Action." You can\'t change a MetricName after you create a VisibilityConfig .







VisibilityConfig (dict) --
Defines and enables Amazon CloudWatch metrics and web request sample collection.

SampledRequestsEnabled (boolean) --
A boolean indicating whether AWS WAF should store a sampling of the web requests that match the rules. You can view the sampled requests through the AWS WAF console.

CloudWatchMetricsEnabled (boolean) --
A boolean indicating whether the associated resource sends metrics to CloudWatch. For the list of available metrics, see AWS WAF Metrics .

MetricName (string) --
A name of the CloudWatch metric. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with length from one to 128 characters. It can\'t contain whitespace or metric names reserved for AWS WAF, for example "All" and "Default_Action." You can\'t change a MetricName after you create a VisibilityConfig .



Capacity (integer) --
The web ACL capacity units (WCUs) currently being used by this web ACL.
AWS WAF uses WCUs to calculate and control the operating resources that are used to run your rules, rule groups, and web ACLs. AWS WAF calculates capacity differently for each rule type, to reflect the relative cost of each rule. Simple rules that cost little to run use fewer WCUs than more complex rules that use more processing power. Rule group capacity is fixed at creation, which helps users plan their web ACL WCU usage when they use a rule group. The WCU limit for web ACLs is 1,500.

PreProcessFirewallManagerRuleGroups (list) --
The first set of rules for AWS WAF to process in the web ACL. This is defined in an AWS Firewall Manager WAF policy and contains only rule group references. You can\'t alter these. Any rules and rule groups that you define for the web ACL are prioritized after these.
In the Firewall Manager WAF policy, the Firewall Manager administrator can define a set of rule groups to run first in the web ACL and a set of rule groups to run last. Within each set, the administrator prioritizes the rule groups, to determine their relative processing order.

(dict) --
A rule group that\'s defined for an AWS Firewall Manager WAF policy.

Name (string) --
The name of the rule group. You cannot change the name of a rule group after you create it.

Priority (integer) --
If you define more than one rule group in the first or last Firewall Manager rule groups, AWS WAF evaluates each request against the rule groups in order, starting from the lowest priority setting. The priorities don\'t need to be consecutive, but they must all be different.

FirewallManagerStatement (dict) --
The processing guidance for an AWS Firewall Manager rule. This is like a regular rule  Statement , but it can only contain a rule group reference.

ManagedRuleGroupStatement (dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

A rule statement used to run the rules that are defined in a managed rule group. To use this, provide the vendor name and the name of the rule group in this statement. You can retrieve the required names by calling  ListAvailableManagedRuleGroups .
You can\'t nest a ManagedRuleGroupStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.

VendorName (string) --
The name of the managed rule group vendor. You use this, along with the rule group name, to identify the rule group.

Name (string) --
The name of the managed rule group. You use this, along with the vendor name, to identify the rule group.

ExcludedRules (list) --
The rules whose actions are set to COUNT by the web ACL, regardless of the action that is set on the rule. This effectively excludes the rule from acting on web requests.

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Specifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.

Name (string) --
The name of the rule to exclude.







RuleGroupReferenceStatement (dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

A rule statement used to run the rules that are defined in a  RuleGroup . To use this, create a rule group with your rules, then provide the ARN of the rule group in this statement.
You cannot nest a RuleGroupReferenceStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.

ARN (string) --
The Amazon Resource Name (ARN) of the entity.

ExcludedRules (list) --
The names of rules that are in the referenced rule group, but that you want AWS WAF to exclude from processing for this rule statement.

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Specifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.

Name (string) --
The name of the rule to exclude.









OverrideAction (dict) --
The override action to apply to the rules in a rule group. Used only for rule statements that reference a rule group, like RuleGroupReferenceStatement and ManagedRuleGroupStatement .
Set the override action to none to leave the rule actions in effect. Set it to count to only count matches, regardless of the rule action settings.
In a  Rule , you must specify either this OverrideAction setting or the rule Action setting, but not both:

If the rule statement references a rule group, use this override action setting and not the action setting.
If the rule statement does not reference a rule group, use the rule action setting and not this rule override action setting.


Count (dict) --
Override the rule action setting to count.

None (dict) --
Don\'t override the rule action setting.



VisibilityConfig (dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Defines and enables Amazon CloudWatch metrics and web request sample collection.

SampledRequestsEnabled (boolean) --
A boolean indicating whether AWS WAF should store a sampling of the web requests that match the rules. You can view the sampled requests through the AWS WAF console.

CloudWatchMetricsEnabled (boolean) --
A boolean indicating whether the associated resource sends metrics to CloudWatch. For the list of available metrics, see AWS WAF Metrics .

MetricName (string) --
A name of the CloudWatch metric. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with length from one to 128 characters. It can\'t contain whitespace or metric names reserved for AWS WAF, for example "All" and "Default_Action." You can\'t change a MetricName after you create a VisibilityConfig .







PostProcessFirewallManagerRuleGroups (list) --
The last set of rules for AWS WAF to process in the web ACL. This is defined in an AWS Firewall Manager WAF policy and contains only rule group references. You can\'t alter these. Any rules and rule groups that you define for the web ACL are prioritized before these.
In the Firewall Manager WAF policy, the Firewall Manager administrator can define a set of rule groups to run first in the web ACL and a set of rule groups to run last. Within each set, the administrator prioritizes the rule groups, to determine their relative processing order.

(dict) --
A rule group that\'s defined for an AWS Firewall Manager WAF policy.

Name (string) --
The name of the rule group. You cannot change the name of a rule group after you create it.

Priority (integer) --
If you define more than one rule group in the first or last Firewall Manager rule groups, AWS WAF evaluates each request against the rule groups in order, starting from the lowest priority setting. The priorities don\'t need to be consecutive, but they must all be different.

FirewallManagerStatement (dict) --
The processing guidance for an AWS Firewall Manager rule. This is like a regular rule  Statement , but it can only contain a rule group reference.

ManagedRuleGroupStatement (dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

A rule statement used to run the rules that are defined in a managed rule group. To use this, provide the vendor name and the name of the rule group in this statement. You can retrieve the required names by calling  ListAvailableManagedRuleGroups .
You can\'t nest a ManagedRuleGroupStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.

VendorName (string) --
The name of the managed rule group vendor. You use this, along with the rule group name, to identify the rule group.

Name (string) --
The name of the managed rule group. You use this, along with the vendor name, to identify the rule group.

ExcludedRules (list) --
The rules whose actions are set to COUNT by the web ACL, regardless of the action that is set on the rule. This effectively excludes the rule from acting on web requests.

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Specifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.

Name (string) --
The name of the rule to exclude.







RuleGroupReferenceStatement (dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

A rule statement used to run the rules that are defined in a  RuleGroup . To use this, create a rule group with your rules, then provide the ARN of the rule group in this statement.
You cannot nest a RuleGroupReferenceStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.

ARN (string) --
The Amazon Resource Name (ARN) of the entity.

ExcludedRules (list) --
The names of rules that are in the referenced rule group, but that you want AWS WAF to exclude from processing for this rule statement.

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Specifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.

Name (string) --
The name of the rule to exclude.









OverrideAction (dict) --
The override action to apply to the rules in a rule group. Used only for rule statements that reference a rule group, like RuleGroupReferenceStatement and ManagedRuleGroupStatement .
Set the override action to none to leave the rule actions in effect. Set it to count to only count matches, regardless of the rule action settings.
In a  Rule , you must specify either this OverrideAction setting or the rule Action setting, but not both:

If the rule statement references a rule group, use this override action setting and not the action setting.
If the rule statement does not reference a rule group, use the rule action setting and not this rule override action setting.


Count (dict) --
Override the rule action setting to count.

None (dict) --
Don\'t override the rule action setting.



VisibilityConfig (dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Defines and enables Amazon CloudWatch metrics and web request sample collection.

SampledRequestsEnabled (boolean) --
A boolean indicating whether AWS WAF should store a sampling of the web requests that match the rules. You can view the sampled requests through the AWS WAF console.

CloudWatchMetricsEnabled (boolean) --
A boolean indicating whether the associated resource sends metrics to CloudWatch. For the list of available metrics, see AWS WAF Metrics .

MetricName (string) --
A name of the CloudWatch metric. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with length from one to 128 characters. It can\'t contain whitespace or metric names reserved for AWS WAF, for example "All" and "Default_Action." You can\'t change a MetricName after you create a VisibilityConfig .







ManagedByFirewallManager (boolean) --
Indicates whether this web ACL is managed by AWS Firewall Manager. If true, then only AWS Firewall Manager can delete the web ACL or any Firewall Manager rule groups in the web ACL.



LockToken (string) --
A token used for optimistic locking. AWS WAF returns a token to your get and list requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like update and delete. AWS WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a WAFOptimisticLockException . If this happens, perform another get, and use the new token returned by that operation.







Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFNonexistentItemException
WAFV2.Client.exceptions.WAFInvalidOperationException


    :return: {
        'WebACL': {
            'Name': 'string',
            'Id': 'string',
            'ARN': 'string',
            'DefaultAction': {
                'Block': {},
                'Allow': {}
            },
            'Description': 'string',
            'Rules': [
                {
                    'Name': 'string',
                    'Priority': 123,
                    'Statement': {
                        'ByteMatchStatement': {
                            'SearchString': b'bytes',
                            'FieldToMatch': {
                                'SingleHeader': {
                                    'Name': 'string'
                                },
                                'SingleQueryArgument': {
                                    'Name': 'string'
                                },
                                'AllQueryArguments': {},
                                'UriPath': {},
                                'QueryString': {},
                                'Body': {},
                                'Method': {}
                            },
                            'TextTransformations': [
                                {
                                    'Priority': 123,
                                    'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                                },
                            ],
                            'PositionalConstraint': 'EXACTLY'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CONTAINS_WORD'
                        },
                        'SqliMatchStatement': {
                            'FieldToMatch': {
                                'SingleHeader': {
                                    'Name': 'string'
                                },
                                'SingleQueryArgument': {
                                    'Name': 'string'
                                },
                                'AllQueryArguments': {},
                                'UriPath': {},
                                'QueryString': {},
                                'Body': {},
                                'Method': {}
                            },
                            'TextTransformations': [
                                {
                                    'Priority': 123,
                                    'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                                },
                            ]
                        },
                        'XssMatchStatement': {
                            'FieldToMatch': {
                                'SingleHeader': {
                                    'Name': 'string'
                                },
                                'SingleQueryArgument': {
                                    'Name': 'string'
                                },
                                'AllQueryArguments': {},
                                'UriPath': {},
                                'QueryString': {},
                                'Body': {},
                                'Method': {}
                            },
                            'TextTransformations': [
                                {
                                    'Priority': 123,
                                    'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                                },
                            ]
                        },
                        'SizeConstraintStatement': {
                            'FieldToMatch': {
                                'SingleHeader': {
                                    'Name': 'string'
                                },
                                'SingleQueryArgument': {
                                    'Name': 'string'
                                },
                                'AllQueryArguments': {},
                                'UriPath': {},
                                'QueryString': {},
                                'Body': {},
                                'Method': {}
                            },
                            'ComparisonOperator': 'EQ'|'NE'|'LE'|'LT'|'GE'|'GT',
                            'Size': 123,
                            'TextTransformations': [
                                {
                                    'Priority': 123,
                                    'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                                },
                            ]
                        },
                        'GeoMatchStatement': {
                            'CountryCodes': [
                                'AF'|'AX'|'AL'|'DZ'|'AS'|'AD'|'AO'|'AI'|'AQ'|'AG'|'AR'|'AM'|'AW'|'AU'|'AT'|'AZ'|'BS'|'BH'|'BD'|'BB'|'BY'|'BE'|'BZ'|'BJ'|'BM'|'BT'|'BO'|'BQ'|'BA'|'BW'|'BV'|'BR'|'IO'|'BN'|'BG'|'BF'|'BI'|'KH'|'CM'|'CA'|'CV'|'KY'|'CF'|'TD'|'CL'|'CN'|'CX'|'CC'|'CO'|'KM'|'CG'|'CD'|'CK'|'CR'|'CI'|'HR'|'CU'|'CW'|'CY'|'CZ'|'DK'|'DJ'|'DM'|'DO'|'EC'|'EG'|'SV'|'GQ'|'ER'|'EE'|'ET'|'FK'|'FO'|'FJ'|'FI'|'FR'|'GF'|'PF'|'TF'|'GA'|'GM'|'GE'|'DE'|'GH'|'GI'|'GR'|'GL'|'GD'|'GP'|'GU'|'GT'|'GG'|'GN'|'GW'|'GY'|'HT'|'HM'|'VA'|'HN'|'HK'|'HU'|'IS'|'IN'|'ID'|'IR'|'IQ'|'IE'|'IM'|'IL'|'IT'|'JM'|'JP'|'JE'|'JO'|'KZ'|'KE'|'KI'|'KP'|'KR'|'KW'|'KG'|'LA'|'LV'|'LB'|'LS'|'LR'|'LY'|'LI'|'LT'|'LU'|'MO'|'MK'|'MG'|'MW'|'MY'|'MV'|'ML'|'MT'|'MH'|'MQ'|'MR'|'MU'|'YT'|'MX'|'FM'|'MD'|'MC'|'MN'|'ME'|'MS'|'MA'|'MZ'|'MM'|'NA'|'NR'|'NP'|'NL'|'NC'|'NZ'|'NI'|'NE'|'NG'|'NU'|'NF'|'MP'|'NO'|'OM'|'PK'|'PW'|'PS'|'PA'|'PG'|'PY'|'PE'|'PH'|'PN'|'PL'|'PT'|'PR'|'QA'|'RE'|'RO'|'RU'|'RW'|'BL'|'SH'|'KN'|'LC'|'MF'|'PM'|'VC'|'WS'|'SM'|'ST'|'SA'|'SN'|'RS'|'SC'|'SL'|'SG'|'SX'|'SK'|'SI'|'SB'|'SO'|'ZA'|'GS'|'SS'|'ES'|'LK'|'SD'|'SR'|'SJ'|'SZ'|'SE'|'CH'|'SY'|'TW'|'TJ'|'TZ'|'TH'|'TL'|'TG'|'TK'|'TO'|'TT'|'TN'|'TR'|'TM'|'TC'|'TV'|'UG'|'UA'|'AE'|'GB'|'US'|'UM'|'UY'|'UZ'|'VU'|'VE'|'VN'|'VG'|'VI'|'WF'|'EH'|'YE'|'ZM'|'ZW',
                            ]
                        },
                        'RuleGroupReferenceStatement': {
                            'ARN': 'string',
                            'ExcludedRules': [
                                {
                                    'Name': 'string'
                                },
                            ]
                        },
                        'IPSetReferenceStatement': {
                            'ARN': 'string'
                        },
                        'RegexPatternSetReferenceStatement': {
                            'ARN': 'string',
                            'FieldToMatch': {
                                'SingleHeader': {
                                    'Name': 'string'
                                },
                                'SingleQueryArgument': {
                                    'Name': 'string'
                                },
                                'AllQueryArguments': {},
                                'UriPath': {},
                                'QueryString': {},
                                'Body': {},
                                'Method': {}
                            },
                            'TextTransformations': [
                                {
                                    'Priority': 123,
                                    'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                                },
                            ]
                        },
                        'RateBasedStatement': {
                            'Limit': 123,
                            'AggregateKeyType': 'IP',
                            'ScopeDownStatement': {'... recursive ...'}
                        },
                        'AndStatement': {
                            'Statements': [
                                {'... recursive ...'},
                            ]
                        },
                        'OrStatement': {
                            'Statements': [
                                {'... recursive ...'},
                            ]
                        },
                        'NotStatement': {
                            'Statement': {'... recursive ...'}
                        },
                        'ManagedRuleGroupStatement': {
                            'VendorName': 'string',
                            'Name': 'string',
                            'ExcludedRules': [
                                {
                                    'Name': 'string'
                                },
                            ]
                        }
                    },
                    'Action': {
                        'Block': {},
                        'Allow': {},
                        'Count': {}
                    },
                    'OverrideAction': {
                        'Count': {},
                        'None': {}
                    },
                    'VisibilityConfig': {
                        'SampledRequestsEnabled': True|False,
                        'CloudWatchMetricsEnabled': True|False,
                        'MetricName': 'string'
                    }
                },
            ],
            'VisibilityConfig': {
                'SampledRequestsEnabled': True|False,
                'CloudWatchMetricsEnabled': True|False,
                'MetricName': 'string'
            },
            'Capacity': 123,
            'PreProcessFirewallManagerRuleGroups': [
                {
                    'Name': 'string',
                    'Priority': 123,
                    'FirewallManagerStatement': {
                        'ManagedRuleGroupStatement': {
                            'VendorName': 'string',
                            'Name': 'string',
                            'ExcludedRules': [
                                {
                                    'Name': 'string'
                                },
                            ]
                        },
                        'RuleGroupReferenceStatement': {
                            'ARN': 'string',
                            'ExcludedRules': [
                                {
                                    'Name': 'string'
                                },
                            ]
                        }
                    },
                    'OverrideAction': {
                        'Count': {},
                        'None': {}
                    },
                    'VisibilityConfig': {
                        'SampledRequestsEnabled': True|False,
                        'CloudWatchMetricsEnabled': True|False,
                        'MetricName': 'string'
                    }
                },
            ],
            'PostProcessFirewallManagerRuleGroups': [
                {
                    'Name': 'string',
                    'Priority': 123,
                    'FirewallManagerStatement': {
                        'ManagedRuleGroupStatement': {
                            'VendorName': 'string',
                            'Name': 'string',
                            'ExcludedRules': [
                                {
                                    'Name': 'string'
                                },
                            ]
                        },
                        'RuleGroupReferenceStatement': {
                            'ARN': 'string',
                            'ExcludedRules': [
                                {
                                    'Name': 'string'
                                },
                            ]
                        }
                    },
                    'OverrideAction': {
                        'Count': {},
                        'None': {}
                    },
                    'VisibilityConfig': {
                        'SampledRequestsEnabled': True|False,
                        'CloudWatchMetricsEnabled': True|False,
                        'MetricName': 'string'
                    }
                },
            ],
            'ManagedByFirewallManager': True|False
        },
        'LockToken': 'string'
    }
    
    
    :returns: 
    Method : The HTTP method that you want AWS WAF to search for. This indicates the type of operation specified in the request.
    UriPath : The value that you want AWS WAF to search for in the URI path, for example, /images/daily-ad.jpg .
    
    """
    pass

def get_web_acl_for_resource(ResourceArn=None):
    """
    Retrieves the  WebACL for the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_web_acl_for_resource(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe ARN (Amazon Resource Name) of the resource.\n

    :rtype: dict
ReturnsResponse Syntax{
    'WebACL': {
        'Name': 'string',
        'Id': 'string',
        'ARN': 'string',
        'DefaultAction': {
            'Block': {},
            'Allow': {}
        },
        'Description': 'string',
        'Rules': [
            {
                'Name': 'string',
                'Priority': 123,
                'Statement': {
                    'ByteMatchStatement': {
                        'SearchString': b'bytes',
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {},
                            'UriPath': {},
                            'QueryString': {},
                            'Body': {},
                            'Method': {}
                        },
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ],
                        'PositionalConstraint': 'EXACTLY'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CONTAINS_WORD'
                    },
                    'SqliMatchStatement': {
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {},
                            'UriPath': {},
                            'QueryString': {},
                            'Body': {},
                            'Method': {}
                        },
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ]
                    },
                    'XssMatchStatement': {
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {},
                            'UriPath': {},
                            'QueryString': {},
                            'Body': {},
                            'Method': {}
                        },
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ]
                    },
                    'SizeConstraintStatement': {
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {},
                            'UriPath': {},
                            'QueryString': {},
                            'Body': {},
                            'Method': {}
                        },
                        'ComparisonOperator': 'EQ'|'NE'|'LE'|'LT'|'GE'|'GT',
                        'Size': 123,
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ]
                    },
                    'GeoMatchStatement': {
                        'CountryCodes': [
                            'AF'|'AX'|'AL'|'DZ'|'AS'|'AD'|'AO'|'AI'|'AQ'|'AG'|'AR'|'AM'|'AW'|'AU'|'AT'|'AZ'|'BS'|'BH'|'BD'|'BB'|'BY'|'BE'|'BZ'|'BJ'|'BM'|'BT'|'BO'|'BQ'|'BA'|'BW'|'BV'|'BR'|'IO'|'BN'|'BG'|'BF'|'BI'|'KH'|'CM'|'CA'|'CV'|'KY'|'CF'|'TD'|'CL'|'CN'|'CX'|'CC'|'CO'|'KM'|'CG'|'CD'|'CK'|'CR'|'CI'|'HR'|'CU'|'CW'|'CY'|'CZ'|'DK'|'DJ'|'DM'|'DO'|'EC'|'EG'|'SV'|'GQ'|'ER'|'EE'|'ET'|'FK'|'FO'|'FJ'|'FI'|'FR'|'GF'|'PF'|'TF'|'GA'|'GM'|'GE'|'DE'|'GH'|'GI'|'GR'|'GL'|'GD'|'GP'|'GU'|'GT'|'GG'|'GN'|'GW'|'GY'|'HT'|'HM'|'VA'|'HN'|'HK'|'HU'|'IS'|'IN'|'ID'|'IR'|'IQ'|'IE'|'IM'|'IL'|'IT'|'JM'|'JP'|'JE'|'JO'|'KZ'|'KE'|'KI'|'KP'|'KR'|'KW'|'KG'|'LA'|'LV'|'LB'|'LS'|'LR'|'LY'|'LI'|'LT'|'LU'|'MO'|'MK'|'MG'|'MW'|'MY'|'MV'|'ML'|'MT'|'MH'|'MQ'|'MR'|'MU'|'YT'|'MX'|'FM'|'MD'|'MC'|'MN'|'ME'|'MS'|'MA'|'MZ'|'MM'|'NA'|'NR'|'NP'|'NL'|'NC'|'NZ'|'NI'|'NE'|'NG'|'NU'|'NF'|'MP'|'NO'|'OM'|'PK'|'PW'|'PS'|'PA'|'PG'|'PY'|'PE'|'PH'|'PN'|'PL'|'PT'|'PR'|'QA'|'RE'|'RO'|'RU'|'RW'|'BL'|'SH'|'KN'|'LC'|'MF'|'PM'|'VC'|'WS'|'SM'|'ST'|'SA'|'SN'|'RS'|'SC'|'SL'|'SG'|'SX'|'SK'|'SI'|'SB'|'SO'|'ZA'|'GS'|'SS'|'ES'|'LK'|'SD'|'SR'|'SJ'|'SZ'|'SE'|'CH'|'SY'|'TW'|'TJ'|'TZ'|'TH'|'TL'|'TG'|'TK'|'TO'|'TT'|'TN'|'TR'|'TM'|'TC'|'TV'|'UG'|'UA'|'AE'|'GB'|'US'|'UM'|'UY'|'UZ'|'VU'|'VE'|'VN'|'VG'|'VI'|'WF'|'EH'|'YE'|'ZM'|'ZW',
                        ]
                    },
                    'RuleGroupReferenceStatement': {
                        'ARN': 'string',
                        'ExcludedRules': [
                            {
                                'Name': 'string'
                            },
                        ]
                    },
                    'IPSetReferenceStatement': {
                        'ARN': 'string'
                    },
                    'RegexPatternSetReferenceStatement': {
                        'ARN': 'string',
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {},
                            'UriPath': {},
                            'QueryString': {},
                            'Body': {},
                            'Method': {}
                        },
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ]
                    },
                    'RateBasedStatement': {
                        'Limit': 123,
                        'AggregateKeyType': 'IP',
                        'ScopeDownStatement': {'... recursive ...'}
                    },
                    'AndStatement': {
                        'Statements': [
                            {'... recursive ...'},
                        ]
                    },
                    'OrStatement': {
                        'Statements': [
                            {'... recursive ...'},
                        ]
                    },
                    'NotStatement': {
                        'Statement': {'... recursive ...'}
                    },
                    'ManagedRuleGroupStatement': {
                        'VendorName': 'string',
                        'Name': 'string',
                        'ExcludedRules': [
                            {
                                'Name': 'string'
                            },
                        ]
                    }
                },
                'Action': {
                    'Block': {},
                    'Allow': {},
                    'Count': {}
                },
                'OverrideAction': {
                    'Count': {},
                    'None': {}
                },
                'VisibilityConfig': {
                    'SampledRequestsEnabled': True|False,
                    'CloudWatchMetricsEnabled': True|False,
                    'MetricName': 'string'
                }
            },
        ],
        'VisibilityConfig': {
            'SampledRequestsEnabled': True|False,
            'CloudWatchMetricsEnabled': True|False,
            'MetricName': 'string'
        },
        'Capacity': 123,
        'PreProcessFirewallManagerRuleGroups': [
            {
                'Name': 'string',
                'Priority': 123,
                'FirewallManagerStatement': {
                    'ManagedRuleGroupStatement': {
                        'VendorName': 'string',
                        'Name': 'string',
                        'ExcludedRules': [
                            {
                                'Name': 'string'
                            },
                        ]
                    },
                    'RuleGroupReferenceStatement': {
                        'ARN': 'string',
                        'ExcludedRules': [
                            {
                                'Name': 'string'
                            },
                        ]
                    }
                },
                'OverrideAction': {
                    'Count': {},
                    'None': {}
                },
                'VisibilityConfig': {
                    'SampledRequestsEnabled': True|False,
                    'CloudWatchMetricsEnabled': True|False,
                    'MetricName': 'string'
                }
            },
        ],
        'PostProcessFirewallManagerRuleGroups': [
            {
                'Name': 'string',
                'Priority': 123,
                'FirewallManagerStatement': {
                    'ManagedRuleGroupStatement': {
                        'VendorName': 'string',
                        'Name': 'string',
                        'ExcludedRules': [
                            {
                                'Name': 'string'
                            },
                        ]
                    },
                    'RuleGroupReferenceStatement': {
                        'ARN': 'string',
                        'ExcludedRules': [
                            {
                                'Name': 'string'
                            },
                        ]
                    }
                },
                'OverrideAction': {
                    'Count': {},
                    'None': {}
                },
                'VisibilityConfig': {
                    'SampledRequestsEnabled': True|False,
                    'CloudWatchMetricsEnabled': True|False,
                    'MetricName': 'string'
                }
            },
        ],
        'ManagedByFirewallManager': True|False
    }
}


Response Structure

(dict) --
WebACL (dict) --The Web ACL that is associated with the resource. If there is no associated resource, AWS WAF returns a null Web ACL.

Name (string) --The name of the Web ACL. You cannot change the name of a Web ACL after you create it.

Id (string) --A unique identifier for the WebACL . This ID is returned in the responses to create and list commands. You use this ID to do things like get, update, and delete a WebACL .

ARN (string) --The Amazon Resource Name (ARN) of the Web ACL that you want to associate with the resource.

DefaultAction (dict) --The action to perform if none of the Rules contained in the WebACL match.

Block (dict) --Specifies that AWS WAF should block requests by default.

Allow (dict) --Specifies that AWS WAF should allow requests by default.



Description (string) --A description of the Web ACL that helps with identification. You cannot change the description of a Web ACL after you create it.

Rules (list) --The  Rule statements used to identify the web requests that you want to allow, block, or count. Each rule includes one top-level statement that AWS WAF uses to identify matching web requests, and parameters that govern how AWS WAF handles them.

(dict) --
Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

A single rule, which you can use in a  WebACL or  RuleGroup to identify web requests that you want to allow, block, or count. Each rule includes one top-level  Statement that AWS WAF uses to identify matching web requests, and parameters that govern how AWS WAF handles them.

Name (string) --The name of the rule. You can\'t change the name of a Rule after you create it.

Priority (integer) --If you define more than one Rule in a WebACL , AWS WAF evaluates each request against the Rules in order based on the value of Priority . AWS WAF processes rules with lower priority first. The priorities don\'t need to be consecutive, but they must all be different.

Statement (dict) --The AWS WAF processing statement for the rule, for example  ByteMatchStatement or  SizeConstraintStatement .

ByteMatchStatement (dict) --A rule statement that defines a string match search for AWS WAF to apply to web requests. The byte match statement provides the bytes to search for, the location in requests that you want AWS WAF to search, and other settings. The bytes to search for are typically a string that corresponds with ASCII characters. In the AWS WAF console and the developer guide, this is refered to as a string match statement.

SearchString (bytes) --A string value that you want AWS WAF to search for. AWS WAF searches only in the part of web requests that you designate for inspection in  FieldToMatch . The maximum length of the value is 50 bytes.
Valid values depend on the component that you specify for inspection in FieldToMatch :

Method : The HTTP method that you want AWS WAF to search for. This indicates the type of operation specified in the request.
UriPath : The value that you want AWS WAF to search for in the URI path, for example, /images/daily-ad.jpg .

If SearchString includes alphabetic characters A-Z and a-z, note that the value is case sensitive.

If you\'re using the AWS WAF API
Specify a base64-encoded version of the value. The maximum length of the value before you base64-encode it is 50 bytes.
For example, suppose the value of Type is HEADER and the value of Data is User-Agent . If you want to search the User-Agent header for the value BadBot , you base64-encode BadBot using MIME base64-encoding and include the resulting value, QmFkQm90 , in the value of SearchString .

If you\'re using the AWS CLI or one of the AWS SDKs
The value that you want AWS WAF to search for. The SDK automatically base64 encodes the value.

FieldToMatch (dict) --The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .

SingleHeader (dict) --Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.

Name (string) --The name of the query header to inspect.



SingleQueryArgument (dict) --Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.

Name (string) --The name of the query argument to inspect.



AllQueryArguments (dict) --Inspect all query arguments.

UriPath (dict) --Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString (dict) --Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body (dict) --Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method (dict) --Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.



TextTransformations (list) --Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.

(dict) --
Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.

Priority (integer) --Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.

Type (string) --You can specify the following transformation types:

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
Specify NONE if you don\'t want any text transformations.





PositionalConstraint (string) --The area within the portion of a web request that you want AWS WAF to search for SearchString . Valid values include the following:

CONTAINS
The specified part of the web request must include the value of SearchString , but the location doesn\'t matter.

CONTAINS_WORD
The specified part of the web request must include the value of SearchString , and SearchString must contain only alphanumeric characters or underscore (A-Z, a-z, 0-9, or _). In addition, SearchString must be a word, which means that both of the following are true:

SearchString is at the beginning of the specified part of the web request or is preceded by a character other than an alphanumeric character or underscore (_). Examples include the value of a header and ;BadBot .
SearchString is at the end of the specified part of the web request or is followed by a character other than an alphanumeric character or underscore (_), for example, BadBot; and -BadBot; .


EXACTLY
The value of the specified part of the web request must exactly match the value of SearchString .

STARTS_WITH
The value of SearchString must appear at the beginning of the specified part of the web request.

ENDS_WITH
The value of SearchString must appear at the end of the specified part of the web request.



SqliMatchStatement (dict) --Attackers sometimes insert malicious SQL code into web requests in an effort to extract data from your database. To allow or block web requests that appear to contain malicious SQL code, create one or more SQL injection match conditions. An SQL injection match condition identifies the part of web requests, such as the URI or the query string, that you want AWS WAF to inspect. Later in the process, when you create a web ACL, you specify whether to allow or block requests that appear to contain malicious SQL code.

FieldToMatch (dict) --The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .

SingleHeader (dict) --Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.

Name (string) --The name of the query header to inspect.



SingleQueryArgument (dict) --Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.

Name (string) --The name of the query argument to inspect.



AllQueryArguments (dict) --Inspect all query arguments.

UriPath (dict) --Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString (dict) --Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body (dict) --Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method (dict) --Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.



TextTransformations (list) --Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.

(dict) --
Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.

Priority (integer) --Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.

Type (string) --You can specify the following transformation types:

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
Specify NONE if you don\'t want any text transformations.







XssMatchStatement (dict) --A rule statement that defines a cross-site scripting (XSS) match search for AWS WAF to apply to web requests. XSS attacks are those where the attacker uses vulnerabilities in a benign website as a vehicle to inject malicious client-site scripts into other legitimate web browsers. The XSS match statement provides the location in requests that you want AWS WAF to search and text transformations to use on the search area before AWS WAF searches for character sequences that are likely to be malicious strings.

FieldToMatch (dict) --The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .

SingleHeader (dict) --Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.

Name (string) --The name of the query header to inspect.



SingleQueryArgument (dict) --Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.

Name (string) --The name of the query argument to inspect.



AllQueryArguments (dict) --Inspect all query arguments.

UriPath (dict) --Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString (dict) --Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body (dict) --Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method (dict) --Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.



TextTransformations (list) --Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.

(dict) --
Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.

Priority (integer) --Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.

Type (string) --You can specify the following transformation types:

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
Specify NONE if you don\'t want any text transformations.







SizeConstraintStatement (dict) --A rule statement that compares a number of bytes against the size of a request component, using a comparison operator, such as greater than (>) or less than (<). For example, you can use a size constraint statement to look for query strings that are longer than 100 bytes.
If you configure AWS WAF to inspect the request body, AWS WAF inspects only the first 8192 bytes (8 KB). If the request body for your web requests never exceeds 8192 bytes, you can create a size constraint condition and block requests that have a request body greater than 8192 bytes.
If you choose URI for the value of Part of the request to filter on, the slash (/) in the URI counts as one character. For example, the URI /logo.jpg is nine characters long.

FieldToMatch (dict) --The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .

SingleHeader (dict) --Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.

Name (string) --The name of the query header to inspect.



SingleQueryArgument (dict) --Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.

Name (string) --The name of the query argument to inspect.



AllQueryArguments (dict) --Inspect all query arguments.

UriPath (dict) --Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString (dict) --Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body (dict) --Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method (dict) --Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.



ComparisonOperator (string) --The operator to use to compare the request part to the size setting.

Size (integer) --The size, in byte, to compare to the request part, after any transformations.

TextTransformations (list) --Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.

(dict) --
Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.

Priority (integer) --Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.

Type (string) --You can specify the following transformation types:

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
Specify NONE if you don\'t want any text transformations.







GeoMatchStatement (dict) --A rule statement used to identify web requests based on country of origin.

CountryCodes (list) --An array of two-character country codes, for example, [ "US", "CN" ] , from the alpha-2 country ISO codes of the ISO 3166 international standard.

(string) --




RuleGroupReferenceStatement (dict) --A rule statement used to run the rules that are defined in a  RuleGroup . To use this, create a rule group with your rules, then provide the ARN of the rule group in this statement.
You cannot nest a RuleGroupReferenceStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.

ARN (string) --The Amazon Resource Name (ARN) of the entity.

ExcludedRules (list) --The names of rules that are in the referenced rule group, but that you want AWS WAF to exclude from processing for this rule statement.

(dict) --
Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Specifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.

Name (string) --The name of the rule to exclude.







IPSetReferenceStatement (dict) --A rule statement used to detect web requests coming from particular IP addresses or address ranges. To use this, create an  IPSet that specifies the addresses you want to detect, then use the ARN of that set in this statement. To create an IP set, see  CreateIPSet .
Each IP set rule statement references an IP set. You create and maintain the set independent of your rules. This allows you to use the single set in multiple rules. When you update the referenced set, AWS WAF automatically updates all rules that reference it.

ARN (string) --The Amazon Resource Name (ARN) of the  IPSet that this statement references.



RegexPatternSetReferenceStatement (dict) --A rule statement used to search web request components for matches with regular expressions. To use this, create a  RegexPatternSet that specifies the expressions that you want to detect, then use the ARN of that set in this statement. A web request matches the pattern set rule statement if the request component matches any of the patterns in the set. To create a regex pattern set, see  CreateRegexPatternSet .
Each regex pattern set rule statement references a regex pattern set. You create and maintain the set independent of your rules. This allows you to use the single set in multiple rules. When you update the referenced set, AWS WAF automatically updates all rules that reference it.

ARN (string) --The Amazon Resource Name (ARN) of the  RegexPatternSet that this statement references.

FieldToMatch (dict) --The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .

SingleHeader (dict) --Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.

Name (string) --The name of the query header to inspect.



SingleQueryArgument (dict) --Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.

Name (string) --The name of the query argument to inspect.



AllQueryArguments (dict) --Inspect all query arguments.

UriPath (dict) --Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString (dict) --Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body (dict) --Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method (dict) --Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.



TextTransformations (list) --Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.

(dict) --
Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.

Priority (integer) --Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.

Type (string) --You can specify the following transformation types:

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
Specify NONE if you don\'t want any text transformations.







RateBasedStatement (dict) --A rate-based rule tracks the rate of requests for each originating IP address, and triggers the rule action when the rate exceeds a limit that you specify on the number of requests in any 5-minute time span. You can use this to put a temporary block on requests from an IP address that is sending excessive requests.
When the rule action triggers, AWS WAF blocks additional requests from the IP address until the request rate falls below the limit.
You can optionally nest another statement inside the rate-based statement, to narrow the scope of the rule so that it only counts requests that match the nested statement. For example, based on recent requests that you have seen from an attacker, you might create a rate-based rule with a nested AND rule statement that contains the following nested statements:

An IP match statement with an IP set that specified the address 192.0.2.44.
A string match statement that searches in the User-Agent header for the string BadBot.

In this rate-based rule, you also define a rate limit. For this example, the rate limit is 1,000. Requests that meet both of the conditions in the statements are counted. If the count exceeds 1,000 requests per five minutes, the rule action triggers. Requests that do not meet both conditions are not counted towards the rate limit and are not affected by this rule.
You cannot nest a RateBasedStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.

Limit (integer) --The limit on requests per 5-minute period for a single originating IP address. If the statement includes a ScopDownStatement , this limit is applied only to the requests that match the statement.

AggregateKeyType (string) --Setting that indicates how to aggregate the request counts. Currently, you must set this to IP . The request counts are aggregated on IP addresses.

ScopeDownStatement (dict) --An optional nested statement that narrows the scope of the rate-based statement to matching web requests. This can be any nestable statement, and you can nest statements at any level below this scope-down statement.



AndStatement (dict) --A logical rule statement used to combine other rule statements with AND logic. You provide more than one  Statement within the AndStatement .

Statements (list) --The statements to combine with AND logic. You can use any statements that can be nested.

(dict) --
Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

The processing guidance for a  Rule , used by AWS WAF to determine whether a web request matches the rule.





OrStatement (dict) --A logical rule statement used to combine other rule statements with OR logic. You provide more than one  Statement within the OrStatement .

Statements (list) --The statements to combine with OR logic. You can use any statements that can be nested.

(dict) --
Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

The processing guidance for a  Rule , used by AWS WAF to determine whether a web request matches the rule.





NotStatement (dict) --A logical rule statement used to negate the results of another rule statement. You provide one  Statement within the NotStatement .

Statement (dict) --The statement to negate. You can use any statement that can be nested.



ManagedRuleGroupStatement (dict) --A rule statement used to run the rules that are defined in a managed rule group. To use this, provide the vendor name and the name of the rule group in this statement. You can retrieve the required names by calling  ListAvailableManagedRuleGroups .
You can\'t nest a ManagedRuleGroupStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.

VendorName (string) --The name of the managed rule group vendor. You use this, along with the rule group name, to identify the rule group.

Name (string) --The name of the managed rule group. You use this, along with the vendor name, to identify the rule group.

ExcludedRules (list) --The rules whose actions are set to COUNT by the web ACL, regardless of the action that is set on the rule. This effectively excludes the rule from acting on web requests.

(dict) --
Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Specifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.

Name (string) --The name of the rule to exclude.









Action (dict) --The action that AWS WAF should take on a web request when it matches the rule statement. Settings at the web ACL level can override the rule action setting.
This is used only for rules whose statements do not reference a rule group. Rule statements that reference a rule group include RuleGroupReferenceStatement and ManagedRuleGroupStatement .
You must specify either this Action setting or the rule OverrideAction setting, but not both:

If the rule statement does not reference a rule group, use this rule action setting and not the rule override action setting.
If the rule statement references a rule group, use the override action setting and not this action setting.


Block (dict) --Instructs AWS WAF to block the web request.

Allow (dict) --Instructs AWS WAF to allow the web request.

Count (dict) --Instructs AWS WAF to count the web request and allow it.



OverrideAction (dict) --The override action to apply to the rules in a rule group. Used only for rule statements that reference a rule group, like RuleGroupReferenceStatement and ManagedRuleGroupStatement .
Set the override action to none to leave the rule actions in effect. Set it to count to only count matches, regardless of the rule action settings.
In a  Rule , you must specify either this OverrideAction setting or the rule Action setting, but not both:

If the rule statement references a rule group, use this override action setting and not the action setting.
If the rule statement does not reference a rule group, use the rule action setting and not this rule override action setting.


Count (dict) --Override the rule action setting to count.

None (dict) --Don\'t override the rule action setting.



VisibilityConfig (dict) --Defines and enables Amazon CloudWatch metrics and web request sample collection.

SampledRequestsEnabled (boolean) --A boolean indicating whether AWS WAF should store a sampling of the web requests that match the rules. You can view the sampled requests through the AWS WAF console.

CloudWatchMetricsEnabled (boolean) --A boolean indicating whether the associated resource sends metrics to CloudWatch. For the list of available metrics, see AWS WAF Metrics .

MetricName (string) --A name of the CloudWatch metric. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with length from one to 128 characters. It can\'t contain whitespace or metric names reserved for AWS WAF, for example "All" and "Default_Action." You can\'t change a MetricName after you create a VisibilityConfig .







VisibilityConfig (dict) --Defines and enables Amazon CloudWatch metrics and web request sample collection.

SampledRequestsEnabled (boolean) --A boolean indicating whether AWS WAF should store a sampling of the web requests that match the rules. You can view the sampled requests through the AWS WAF console.

CloudWatchMetricsEnabled (boolean) --A boolean indicating whether the associated resource sends metrics to CloudWatch. For the list of available metrics, see AWS WAF Metrics .

MetricName (string) --A name of the CloudWatch metric. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with length from one to 128 characters. It can\'t contain whitespace or metric names reserved for AWS WAF, for example "All" and "Default_Action." You can\'t change a MetricName after you create a VisibilityConfig .



Capacity (integer) --The web ACL capacity units (WCUs) currently being used by this web ACL.
AWS WAF uses WCUs to calculate and control the operating resources that are used to run your rules, rule groups, and web ACLs. AWS WAF calculates capacity differently for each rule type, to reflect the relative cost of each rule. Simple rules that cost little to run use fewer WCUs than more complex rules that use more processing power. Rule group capacity is fixed at creation, which helps users plan their web ACL WCU usage when they use a rule group. The WCU limit for web ACLs is 1,500.

PreProcessFirewallManagerRuleGroups (list) --The first set of rules for AWS WAF to process in the web ACL. This is defined in an AWS Firewall Manager WAF policy and contains only rule group references. You can\'t alter these. Any rules and rule groups that you define for the web ACL are prioritized after these.
In the Firewall Manager WAF policy, the Firewall Manager administrator can define a set of rule groups to run first in the web ACL and a set of rule groups to run last. Within each set, the administrator prioritizes the rule groups, to determine their relative processing order.

(dict) --A rule group that\'s defined for an AWS Firewall Manager WAF policy.

Name (string) --The name of the rule group. You cannot change the name of a rule group after you create it.

Priority (integer) --If you define more than one rule group in the first or last Firewall Manager rule groups, AWS WAF evaluates each request against the rule groups in order, starting from the lowest priority setting. The priorities don\'t need to be consecutive, but they must all be different.

FirewallManagerStatement (dict) --The processing guidance for an AWS Firewall Manager rule. This is like a regular rule  Statement , but it can only contain a rule group reference.

ManagedRuleGroupStatement (dict) --
Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

A rule statement used to run the rules that are defined in a managed rule group. To use this, provide the vendor name and the name of the rule group in this statement. You can retrieve the required names by calling  ListAvailableManagedRuleGroups .
You can\'t nest a ManagedRuleGroupStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.

VendorName (string) --The name of the managed rule group vendor. You use this, along with the rule group name, to identify the rule group.

Name (string) --The name of the managed rule group. You use this, along with the vendor name, to identify the rule group.

ExcludedRules (list) --The rules whose actions are set to COUNT by the web ACL, regardless of the action that is set on the rule. This effectively excludes the rule from acting on web requests.

(dict) --
Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Specifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.

Name (string) --The name of the rule to exclude.







RuleGroupReferenceStatement (dict) --
Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

A rule statement used to run the rules that are defined in a  RuleGroup . To use this, create a rule group with your rules, then provide the ARN of the rule group in this statement.
You cannot nest a RuleGroupReferenceStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.

ARN (string) --The Amazon Resource Name (ARN) of the entity.

ExcludedRules (list) --The names of rules that are in the referenced rule group, but that you want AWS WAF to exclude from processing for this rule statement.

(dict) --
Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Specifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.

Name (string) --The name of the rule to exclude.









OverrideAction (dict) --The override action to apply to the rules in a rule group. Used only for rule statements that reference a rule group, like RuleGroupReferenceStatement and ManagedRuleGroupStatement .
Set the override action to none to leave the rule actions in effect. Set it to count to only count matches, regardless of the rule action settings.
In a  Rule , you must specify either this OverrideAction setting or the rule Action setting, but not both:

If the rule statement references a rule group, use this override action setting and not the action setting.
If the rule statement does not reference a rule group, use the rule action setting and not this rule override action setting.


Count (dict) --Override the rule action setting to count.

None (dict) --Don\'t override the rule action setting.



VisibilityConfig (dict) --
Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Defines and enables Amazon CloudWatch metrics and web request sample collection.

SampledRequestsEnabled (boolean) --A boolean indicating whether AWS WAF should store a sampling of the web requests that match the rules. You can view the sampled requests through the AWS WAF console.

CloudWatchMetricsEnabled (boolean) --A boolean indicating whether the associated resource sends metrics to CloudWatch. For the list of available metrics, see AWS WAF Metrics .

MetricName (string) --A name of the CloudWatch metric. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with length from one to 128 characters. It can\'t contain whitespace or metric names reserved for AWS WAF, for example "All" and "Default_Action." You can\'t change a MetricName after you create a VisibilityConfig .







PostProcessFirewallManagerRuleGroups (list) --The last set of rules for AWS WAF to process in the web ACL. This is defined in an AWS Firewall Manager WAF policy and contains only rule group references. You can\'t alter these. Any rules and rule groups that you define for the web ACL are prioritized before these.
In the Firewall Manager WAF policy, the Firewall Manager administrator can define a set of rule groups to run first in the web ACL and a set of rule groups to run last. Within each set, the administrator prioritizes the rule groups, to determine their relative processing order.

(dict) --A rule group that\'s defined for an AWS Firewall Manager WAF policy.

Name (string) --The name of the rule group. You cannot change the name of a rule group after you create it.

Priority (integer) --If you define more than one rule group in the first or last Firewall Manager rule groups, AWS WAF evaluates each request against the rule groups in order, starting from the lowest priority setting. The priorities don\'t need to be consecutive, but they must all be different.

FirewallManagerStatement (dict) --The processing guidance for an AWS Firewall Manager rule. This is like a regular rule  Statement , but it can only contain a rule group reference.

ManagedRuleGroupStatement (dict) --
Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

A rule statement used to run the rules that are defined in a managed rule group. To use this, provide the vendor name and the name of the rule group in this statement. You can retrieve the required names by calling  ListAvailableManagedRuleGroups .
You can\'t nest a ManagedRuleGroupStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.

VendorName (string) --The name of the managed rule group vendor. You use this, along with the rule group name, to identify the rule group.

Name (string) --The name of the managed rule group. You use this, along with the vendor name, to identify the rule group.

ExcludedRules (list) --The rules whose actions are set to COUNT by the web ACL, regardless of the action that is set on the rule. This effectively excludes the rule from acting on web requests.

(dict) --
Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Specifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.

Name (string) --The name of the rule to exclude.







RuleGroupReferenceStatement (dict) --
Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

A rule statement used to run the rules that are defined in a  RuleGroup . To use this, create a rule group with your rules, then provide the ARN of the rule group in this statement.
You cannot nest a RuleGroupReferenceStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.

ARN (string) --The Amazon Resource Name (ARN) of the entity.

ExcludedRules (list) --The names of rules that are in the referenced rule group, but that you want AWS WAF to exclude from processing for this rule statement.

(dict) --
Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Specifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.

Name (string) --The name of the rule to exclude.









OverrideAction (dict) --The override action to apply to the rules in a rule group. Used only for rule statements that reference a rule group, like RuleGroupReferenceStatement and ManagedRuleGroupStatement .
Set the override action to none to leave the rule actions in effect. Set it to count to only count matches, regardless of the rule action settings.
In a  Rule , you must specify either this OverrideAction setting or the rule Action setting, but not both:

If the rule statement references a rule group, use this override action setting and not the action setting.
If the rule statement does not reference a rule group, use the rule action setting and not this rule override action setting.


Count (dict) --Override the rule action setting to count.

None (dict) --Don\'t override the rule action setting.



VisibilityConfig (dict) --
Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Defines and enables Amazon CloudWatch metrics and web request sample collection.

SampledRequestsEnabled (boolean) --A boolean indicating whether AWS WAF should store a sampling of the web requests that match the rules. You can view the sampled requests through the AWS WAF console.

CloudWatchMetricsEnabled (boolean) --A boolean indicating whether the associated resource sends metrics to CloudWatch. For the list of available metrics, see AWS WAF Metrics .

MetricName (string) --A name of the CloudWatch metric. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with length from one to 128 characters. It can\'t contain whitespace or metric names reserved for AWS WAF, for example "All" and "Default_Action." You can\'t change a MetricName after you create a VisibilityConfig .







ManagedByFirewallManager (boolean) --Indicates whether this web ACL is managed by AWS Firewall Manager. If true, then only AWS Firewall Manager can delete the web ACL or any Firewall Manager rule groups in the web ACL.








Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFNonexistentItemException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFUnavailableEntityException
WAFV2.Client.exceptions.WAFInvalidOperationException


    :return: {
        'WebACL': {
            'Name': 'string',
            'Id': 'string',
            'ARN': 'string',
            'DefaultAction': {
                'Block': {},
                'Allow': {}
            },
            'Description': 'string',
            'Rules': [
                {
                    'Name': 'string',
                    'Priority': 123,
                    'Statement': {
                        'ByteMatchStatement': {
                            'SearchString': b'bytes',
                            'FieldToMatch': {
                                'SingleHeader': {
                                    'Name': 'string'
                                },
                                'SingleQueryArgument': {
                                    'Name': 'string'
                                },
                                'AllQueryArguments': {},
                                'UriPath': {},
                                'QueryString': {},
                                'Body': {},
                                'Method': {}
                            },
                            'TextTransformations': [
                                {
                                    'Priority': 123,
                                    'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                                },
                            ],
                            'PositionalConstraint': 'EXACTLY'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CONTAINS_WORD'
                        },
                        'SqliMatchStatement': {
                            'FieldToMatch': {
                                'SingleHeader': {
                                    'Name': 'string'
                                },
                                'SingleQueryArgument': {
                                    'Name': 'string'
                                },
                                'AllQueryArguments': {},
                                'UriPath': {},
                                'QueryString': {},
                                'Body': {},
                                'Method': {}
                            },
                            'TextTransformations': [
                                {
                                    'Priority': 123,
                                    'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                                },
                            ]
                        },
                        'XssMatchStatement': {
                            'FieldToMatch': {
                                'SingleHeader': {
                                    'Name': 'string'
                                },
                                'SingleQueryArgument': {
                                    'Name': 'string'
                                },
                                'AllQueryArguments': {},
                                'UriPath': {},
                                'QueryString': {},
                                'Body': {},
                                'Method': {}
                            },
                            'TextTransformations': [
                                {
                                    'Priority': 123,
                                    'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                                },
                            ]
                        },
                        'SizeConstraintStatement': {
                            'FieldToMatch': {
                                'SingleHeader': {
                                    'Name': 'string'
                                },
                                'SingleQueryArgument': {
                                    'Name': 'string'
                                },
                                'AllQueryArguments': {},
                                'UriPath': {},
                                'QueryString': {},
                                'Body': {},
                                'Method': {}
                            },
                            'ComparisonOperator': 'EQ'|'NE'|'LE'|'LT'|'GE'|'GT',
                            'Size': 123,
                            'TextTransformations': [
                                {
                                    'Priority': 123,
                                    'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                                },
                            ]
                        },
                        'GeoMatchStatement': {
                            'CountryCodes': [
                                'AF'|'AX'|'AL'|'DZ'|'AS'|'AD'|'AO'|'AI'|'AQ'|'AG'|'AR'|'AM'|'AW'|'AU'|'AT'|'AZ'|'BS'|'BH'|'BD'|'BB'|'BY'|'BE'|'BZ'|'BJ'|'BM'|'BT'|'BO'|'BQ'|'BA'|'BW'|'BV'|'BR'|'IO'|'BN'|'BG'|'BF'|'BI'|'KH'|'CM'|'CA'|'CV'|'KY'|'CF'|'TD'|'CL'|'CN'|'CX'|'CC'|'CO'|'KM'|'CG'|'CD'|'CK'|'CR'|'CI'|'HR'|'CU'|'CW'|'CY'|'CZ'|'DK'|'DJ'|'DM'|'DO'|'EC'|'EG'|'SV'|'GQ'|'ER'|'EE'|'ET'|'FK'|'FO'|'FJ'|'FI'|'FR'|'GF'|'PF'|'TF'|'GA'|'GM'|'GE'|'DE'|'GH'|'GI'|'GR'|'GL'|'GD'|'GP'|'GU'|'GT'|'GG'|'GN'|'GW'|'GY'|'HT'|'HM'|'VA'|'HN'|'HK'|'HU'|'IS'|'IN'|'ID'|'IR'|'IQ'|'IE'|'IM'|'IL'|'IT'|'JM'|'JP'|'JE'|'JO'|'KZ'|'KE'|'KI'|'KP'|'KR'|'KW'|'KG'|'LA'|'LV'|'LB'|'LS'|'LR'|'LY'|'LI'|'LT'|'LU'|'MO'|'MK'|'MG'|'MW'|'MY'|'MV'|'ML'|'MT'|'MH'|'MQ'|'MR'|'MU'|'YT'|'MX'|'FM'|'MD'|'MC'|'MN'|'ME'|'MS'|'MA'|'MZ'|'MM'|'NA'|'NR'|'NP'|'NL'|'NC'|'NZ'|'NI'|'NE'|'NG'|'NU'|'NF'|'MP'|'NO'|'OM'|'PK'|'PW'|'PS'|'PA'|'PG'|'PY'|'PE'|'PH'|'PN'|'PL'|'PT'|'PR'|'QA'|'RE'|'RO'|'RU'|'RW'|'BL'|'SH'|'KN'|'LC'|'MF'|'PM'|'VC'|'WS'|'SM'|'ST'|'SA'|'SN'|'RS'|'SC'|'SL'|'SG'|'SX'|'SK'|'SI'|'SB'|'SO'|'ZA'|'GS'|'SS'|'ES'|'LK'|'SD'|'SR'|'SJ'|'SZ'|'SE'|'CH'|'SY'|'TW'|'TJ'|'TZ'|'TH'|'TL'|'TG'|'TK'|'TO'|'TT'|'TN'|'TR'|'TM'|'TC'|'TV'|'UG'|'UA'|'AE'|'GB'|'US'|'UM'|'UY'|'UZ'|'VU'|'VE'|'VN'|'VG'|'VI'|'WF'|'EH'|'YE'|'ZM'|'ZW',
                            ]
                        },
                        'RuleGroupReferenceStatement': {
                            'ARN': 'string',
                            'ExcludedRules': [
                                {
                                    'Name': 'string'
                                },
                            ]
                        },
                        'IPSetReferenceStatement': {
                            'ARN': 'string'
                        },
                        'RegexPatternSetReferenceStatement': {
                            'ARN': 'string',
                            'FieldToMatch': {
                                'SingleHeader': {
                                    'Name': 'string'
                                },
                                'SingleQueryArgument': {
                                    'Name': 'string'
                                },
                                'AllQueryArguments': {},
                                'UriPath': {},
                                'QueryString': {},
                                'Body': {},
                                'Method': {}
                            },
                            'TextTransformations': [
                                {
                                    'Priority': 123,
                                    'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                                },
                            ]
                        },
                        'RateBasedStatement': {
                            'Limit': 123,
                            'AggregateKeyType': 'IP',
                            'ScopeDownStatement': {'... recursive ...'}
                        },
                        'AndStatement': {
                            'Statements': [
                                {'... recursive ...'},
                            ]
                        },
                        'OrStatement': {
                            'Statements': [
                                {'... recursive ...'},
                            ]
                        },
                        'NotStatement': {
                            'Statement': {'... recursive ...'}
                        },
                        'ManagedRuleGroupStatement': {
                            'VendorName': 'string',
                            'Name': 'string',
                            'ExcludedRules': [
                                {
                                    'Name': 'string'
                                },
                            ]
                        }
                    },
                    'Action': {
                        'Block': {},
                        'Allow': {},
                        'Count': {}
                    },
                    'OverrideAction': {
                        'Count': {},
                        'None': {}
                    },
                    'VisibilityConfig': {
                        'SampledRequestsEnabled': True|False,
                        'CloudWatchMetricsEnabled': True|False,
                        'MetricName': 'string'
                    }
                },
            ],
            'VisibilityConfig': {
                'SampledRequestsEnabled': True|False,
                'CloudWatchMetricsEnabled': True|False,
                'MetricName': 'string'
            },
            'Capacity': 123,
            'PreProcessFirewallManagerRuleGroups': [
                {
                    'Name': 'string',
                    'Priority': 123,
                    'FirewallManagerStatement': {
                        'ManagedRuleGroupStatement': {
                            'VendorName': 'string',
                            'Name': 'string',
                            'ExcludedRules': [
                                {
                                    'Name': 'string'
                                },
                            ]
                        },
                        'RuleGroupReferenceStatement': {
                            'ARN': 'string',
                            'ExcludedRules': [
                                {
                                    'Name': 'string'
                                },
                            ]
                        }
                    },
                    'OverrideAction': {
                        'Count': {},
                        'None': {}
                    },
                    'VisibilityConfig': {
                        'SampledRequestsEnabled': True|False,
                        'CloudWatchMetricsEnabled': True|False,
                        'MetricName': 'string'
                    }
                },
            ],
            'PostProcessFirewallManagerRuleGroups': [
                {
                    'Name': 'string',
                    'Priority': 123,
                    'FirewallManagerStatement': {
                        'ManagedRuleGroupStatement': {
                            'VendorName': 'string',
                            'Name': 'string',
                            'ExcludedRules': [
                                {
                                    'Name': 'string'
                                },
                            ]
                        },
                        'RuleGroupReferenceStatement': {
                            'ARN': 'string',
                            'ExcludedRules': [
                                {
                                    'Name': 'string'
                                },
                            ]
                        }
                    },
                    'OverrideAction': {
                        'Count': {},
                        'None': {}
                    },
                    'VisibilityConfig': {
                        'SampledRequestsEnabled': True|False,
                        'CloudWatchMetricsEnabled': True|False,
                        'MetricName': 'string'
                    }
                },
            ],
            'ManagedByFirewallManager': True|False
        }
    }
    
    
    :returns: 
    Delete the following characters: " \' ^
    Delete spaces before the following characters: / (
    Replace the following characters with a space: , ;
    Replace multiple spaces with one space
    Convert uppercase letters (A-Z) to lowercase (a-z)
    
    """
    pass

def list_available_managed_rule_groups(Scope=None, NextMarker=None, Limit=None):
    """
    Retrieves an array of managed rule groups that are available for you to use. This list includes all AWS Managed Rules rule groups and the AWS Marketplace managed rule groups that you\'re subscribed to.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_available_managed_rule_groups(
        Scope='CLOUDFRONT'|'REGIONAL',
        NextMarker='string',
        Limit=123
    )
    
    
    :type Scope: string
    :param Scope: [REQUIRED]\nSpecifies whether this is for an AWS CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB) or an API Gateway stage.\nTo work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:\n\nCLI - Specify the Region when you use the CloudFront scope: --scope=CLOUDFRONT --region=us-east-1 .\nAPI and SDKs - For all calls, use the Region endpoint us-east-1.\n\n

    :type NextMarker: string
    :param NextMarker: When you request a list of objects with a Limit setting, if the number of objects that are still available for retrieval exceeds the limit, AWS WAF returns a NextMarker value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.

    :type Limit: integer
    :param Limit: The maximum number of objects that you want AWS WAF to return for this request. If more objects are available, in the response, AWS WAF provides a NextMarker value that you can use in a subsequent call to get the next batch of objects.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextMarker': 'string',
    'ManagedRuleGroups': [
        {
            'VendorName': 'string',
            'Name': 'string',
            'Description': 'string'
        },
    ]
}


Response Structure

(dict) --

NextMarker (string) --
When you request a list of objects with a Limit setting, if the number of objects that are still available for retrieval exceeds the limit, AWS WAF returns a NextMarker value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.

ManagedRuleGroups (list) --

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

High-level information about a managed rule group, returned by  ListAvailableManagedRuleGroups . This provides information like the name and vendor name, that you provide when you add a  ManagedRuleGroupStatement to a web ACL. Managed rule groups include AWS Managed Rules rule groups, which are free of charge to AWS WAF customers, and AWS Marketplace managed rule groups, which you can subscribe to through AWS Marketplace.

VendorName (string) --
The name of the managed rule group vendor. You use this, along with the rule group name, to identify the rule group.

Name (string) --
The name of the managed rule group. You use this, along with the vendor name, to identify the rule group.

Description (string) --
The description of the managed rule group, provided by AWS Managed Rules or the AWS Marketplace seller who manages it.











Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFInvalidOperationException


    :return: {
        'NextMarker': 'string',
        'ManagedRuleGroups': [
            {
                'VendorName': 'string',
                'Name': 'string',
                'Description': 'string'
            },
        ]
    }
    
    
    :returns: 
    WAFV2.Client.exceptions.WAFInternalErrorException
    WAFV2.Client.exceptions.WAFInvalidParameterException
    WAFV2.Client.exceptions.WAFInvalidOperationException
    
    """
    pass

def list_ip_sets(Scope=None, NextMarker=None, Limit=None):
    """
    Retrieves an array of  IPSetSummary objects for the IP sets that you manage.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_ip_sets(
        Scope='CLOUDFRONT'|'REGIONAL',
        NextMarker='string',
        Limit=123
    )
    
    
    :type Scope: string
    :param Scope: [REQUIRED]\nSpecifies whether this is for an AWS CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB) or an API Gateway stage.\nTo work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:\n\nCLI - Specify the Region when you use the CloudFront scope: --scope=CLOUDFRONT --region=us-east-1 .\nAPI and SDKs - For all calls, use the Region endpoint us-east-1.\n\n

    :type NextMarker: string
    :param NextMarker: When you request a list of objects with a Limit setting, if the number of objects that are still available for retrieval exceeds the limit, AWS WAF returns a NextMarker value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.

    :type Limit: integer
    :param Limit: The maximum number of objects that you want AWS WAF to return for this request. If more objects are available, in the response, AWS WAF provides a NextMarker value that you can use in a subsequent call to get the next batch of objects.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextMarker': 'string',
    'IPSets': [
        {
            'Name': 'string',
            'Id': 'string',
            'Description': 'string',
            'LockToken': 'string',
            'ARN': 'string'
        },
    ]
}


Response Structure

(dict) --

NextMarker (string) --
When you request a list of objects with a Limit setting, if the number of objects that are still available for retrieval exceeds the limit, AWS WAF returns a NextMarker value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.

IPSets (list) --
Array of IPSets. This may not be the full list of IPSets that you have defined. See the Limit specification for this request.

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

High-level information about an  IPSet , returned by operations like create and list. This provides information like the ID, that you can use to retrieve and manage an IPSet , and the ARN, that you provide to the  IPSetReferenceStatement to use the address set in a  Rule .

Name (string) --
The name of the IP set. You cannot change the name of an IPSet after you create it.

Id (string) --
A unique identifier for the set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.

Description (string) --
A description of the IP set that helps with identification. You cannot change the description of an IP set after you create it.

LockToken (string) --
A token used for optimistic locking. AWS WAF returns a token to your get and list requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like update and delete. AWS WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a WAFOptimisticLockException . If this happens, perform another get, and use the new token returned by that operation.

ARN (string) --
The Amazon Resource Name (ARN) of the entity.











Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFInvalidOperationException


    :return: {
        'NextMarker': 'string',
        'IPSets': [
            {
                'Name': 'string',
                'Id': 'string',
                'Description': 'string',
                'LockToken': 'string',
                'ARN': 'string'
            },
        ]
    }
    
    
    :returns: 
    WAFV2.Client.exceptions.WAFInternalErrorException
    WAFV2.Client.exceptions.WAFInvalidParameterException
    WAFV2.Client.exceptions.WAFInvalidOperationException
    
    """
    pass

def list_logging_configurations(Scope=None, NextMarker=None, Limit=None):
    """
    Retrieves an array of your  LoggingConfiguration objects.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_logging_configurations(
        Scope='CLOUDFRONT'|'REGIONAL',
        NextMarker='string',
        Limit=123
    )
    
    
    :type Scope: string
    :param Scope: Specifies whether this is for an AWS CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB) or an API Gateway stage.\nTo work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:\n\nCLI - Specify the Region when you use the CloudFront scope: --scope=CLOUDFRONT --region=us-east-1 .\nAPI and SDKs - For all calls, use the Region endpoint us-east-1.\n\n

    :type NextMarker: string
    :param NextMarker: When you request a list of objects with a Limit setting, if the number of objects that are still available for retrieval exceeds the limit, AWS WAF returns a NextMarker value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.

    :type Limit: integer
    :param Limit: The maximum number of objects that you want AWS WAF to return for this request. If more objects are available, in the response, AWS WAF provides a NextMarker value that you can use in a subsequent call to get the next batch of objects.

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
                    'SingleHeader': {
                        'Name': 'string'
                    },
                    'SingleQueryArgument': {
                        'Name': 'string'
                    },
                    'AllQueryArguments': {},
                    'UriPath': {},
                    'QueryString': {},
                    'Body': {},
                    'Method': {}
                },
            ]
        },
    ],
    'NextMarker': 'string'
}


Response Structure

(dict) --

LoggingConfigurations (list) --

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Defines an association between Amazon Kinesis Data Firehose destinations and a web ACL resource, for logging from AWS WAF. As part of the association, you can specify parts of the standard logging fields to keep out of the logs.

ResourceArn (string) --
The Amazon Resource Name (ARN) of the web ACL that you want to associate with LogDestinationConfigs .

LogDestinationConfigs (list) --
The Amazon Kinesis Data Firehose Amazon Resource Name (ARNs) that you want to associate with the web ACL.

(string) --


RedactedFields (list) --
The parts of the request that you want to keep out of the logs. For example, if you redact the cookie field, the cookie field in the firehose will be xxx .

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

The part of a web request that you want AWS WAF to inspect. Include the single FieldToMatch type that you want to inspect, with additional specifications as needed, according to the type. You specify a single request component in FieldToMatch for each rule statement that requires it. To inspect more than one component of a web request, create a separate rule statement for each component.

SingleHeader (dict) --
Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.

Name (string) --
The name of the query header to inspect.



SingleQueryArgument (dict) --
Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.

Name (string) --
The name of the query argument to inspect.



AllQueryArguments (dict) --
Inspect all query arguments.

UriPath (dict) --
Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString (dict) --
Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body (dict) --
Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method (dict) --
Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.









NextMarker (string) --
When you request a list of objects with a Limit setting, if the number of objects that are still available for retrieval exceeds the limit, AWS WAF returns a NextMarker value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.







Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFInvalidOperationException


    :return: {
        'LoggingConfigurations': [
            {
                'ResourceArn': 'string',
                'LogDestinationConfigs': [
                    'string',
                ],
                'RedactedFields': [
                    {
                        'SingleHeader': {
                            'Name': 'string'
                        },
                        'SingleQueryArgument': {
                            'Name': 'string'
                        },
                        'AllQueryArguments': {},
                        'UriPath': {},
                        'QueryString': {},
                        'Body': {},
                        'Method': {}
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

def list_regex_pattern_sets(Scope=None, NextMarker=None, Limit=None):
    """
    Retrieves an array of  RegexPatternSetSummary objects for the regex pattern sets that you manage.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_regex_pattern_sets(
        Scope='CLOUDFRONT'|'REGIONAL',
        NextMarker='string',
        Limit=123
    )
    
    
    :type Scope: string
    :param Scope: [REQUIRED]\nSpecifies whether this is for an AWS CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB) or an API Gateway stage.\nTo work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:\n\nCLI - Specify the Region when you use the CloudFront scope: --scope=CLOUDFRONT --region=us-east-1 .\nAPI and SDKs - For all calls, use the Region endpoint us-east-1.\n\n

    :type NextMarker: string
    :param NextMarker: When you request a list of objects with a Limit setting, if the number of objects that are still available for retrieval exceeds the limit, AWS WAF returns a NextMarker value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.

    :type Limit: integer
    :param Limit: The maximum number of objects that you want AWS WAF to return for this request. If more objects are available, in the response, AWS WAF provides a NextMarker value that you can use in a subsequent call to get the next batch of objects.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextMarker': 'string',
    'RegexPatternSets': [
        {
            'Name': 'string',
            'Id': 'string',
            'Description': 'string',
            'LockToken': 'string',
            'ARN': 'string'
        },
    ]
}


Response Structure

(dict) --

NextMarker (string) --
When you request a list of objects with a Limit setting, if the number of objects that are still available for retrieval exceeds the limit, AWS WAF returns a NextMarker value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.

RegexPatternSets (list) --

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

High-level information about a  RegexPatternSet , returned by operations like create and list. This provides information like the ID, that you can use to retrieve and manage a RegexPatternSet , and the ARN, that you provide to the  RegexPatternSetReferenceStatement to use the pattern set in a  Rule .

Name (string) --
The name of the data type instance. You cannot change the name after you create the instance.

Id (string) --
A unique identifier for the set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.

Description (string) --
A description of the set that helps with identification. You cannot change the description of a set after you create it.

LockToken (string) --
A token used for optimistic locking. AWS WAF returns a token to your get and list requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like update and delete. AWS WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a WAFOptimisticLockException . If this happens, perform another get, and use the new token returned by that operation.

ARN (string) --
The Amazon Resource Name (ARN) of the entity.











Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFInvalidOperationException


    :return: {
        'NextMarker': 'string',
        'RegexPatternSets': [
            {
                'Name': 'string',
                'Id': 'string',
                'Description': 'string',
                'LockToken': 'string',
                'ARN': 'string'
            },
        ]
    }
    
    
    :returns: 
    WAFV2.Client.exceptions.WAFInternalErrorException
    WAFV2.Client.exceptions.WAFInvalidParameterException
    WAFV2.Client.exceptions.WAFInvalidOperationException
    
    """
    pass

def list_resources_for_web_acl(WebACLArn=None, ResourceType=None):
    """
    Retrieves an array of the Amazon Resource Names (ARNs) for the regional resources that are associated with the specified web ACL. If you want the list of AWS CloudFront resources, use the AWS CloudFront call ListDistributionsByWebACLId .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_resources_for_web_acl(
        WebACLArn='string',
        ResourceType='APPLICATION_LOAD_BALANCER'|'API_GATEWAY'
    )
    
    
    :type WebACLArn: string
    :param WebACLArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the Web ACL.\n

    :type ResourceType: string
    :param ResourceType: Used for web ACLs that are scoped for regional applications. A regional application can be an Application Load Balancer (ALB) or an API Gateway stage.

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
The array of Amazon Resource Names (ARNs) of the associated resources.

(string) --








Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFNonexistentItemException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFInvalidOperationException


    :return: {
        'ResourceArns': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_rule_groups(Scope=None, NextMarker=None, Limit=None):
    """
    Retrieves an array of  RuleGroupSummary objects for the rule groups that you manage.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_rule_groups(
        Scope='CLOUDFRONT'|'REGIONAL',
        NextMarker='string',
        Limit=123
    )
    
    
    :type Scope: string
    :param Scope: [REQUIRED]\nSpecifies whether this is for an AWS CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB) or an API Gateway stage.\nTo work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:\n\nCLI - Specify the Region when you use the CloudFront scope: --scope=CLOUDFRONT --region=us-east-1 .\nAPI and SDKs - For all calls, use the Region endpoint us-east-1.\n\n

    :type NextMarker: string
    :param NextMarker: When you request a list of objects with a Limit setting, if the number of objects that are still available for retrieval exceeds the limit, AWS WAF returns a NextMarker value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.

    :type Limit: integer
    :param Limit: The maximum number of objects that you want AWS WAF to return for this request. If more objects are available, in the response, AWS WAF provides a NextMarker value that you can use in a subsequent call to get the next batch of objects.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextMarker': 'string',
    'RuleGroups': [
        {
            'Name': 'string',
            'Id': 'string',
            'Description': 'string',
            'LockToken': 'string',
            'ARN': 'string'
        },
    ]
}


Response Structure

(dict) --

NextMarker (string) --
When you request a list of objects with a Limit setting, if the number of objects that are still available for retrieval exceeds the limit, AWS WAF returns a NextMarker value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.

RuleGroups (list) --

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

High-level information about a  RuleGroup , returned by operations like create and list. This provides information like the ID, that you can use to retrieve and manage a RuleGroup , and the ARN, that you provide to the  RuleGroupReferenceStatement to use the rule group in a  Rule .

Name (string) --
The name of the data type instance. You cannot change the name after you create the instance.

Id (string) --
A unique identifier for the rule group. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.

Description (string) --
A description of the rule group that helps with identification. You cannot change the description of a rule group after you create it.

LockToken (string) --
A token used for optimistic locking. AWS WAF returns a token to your get and list requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like update and delete. AWS WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a WAFOptimisticLockException . If this happens, perform another get, and use the new token returned by that operation.

ARN (string) --
The Amazon Resource Name (ARN) of the entity.











Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFInvalidOperationException


    :return: {
        'NextMarker': 'string',
        'RuleGroups': [
            {
                'Name': 'string',
                'Id': 'string',
                'Description': 'string',
                'LockToken': 'string',
                'ARN': 'string'
            },
        ]
    }
    
    
    :returns: 
    WAFV2.Client.exceptions.WAFInternalErrorException
    WAFV2.Client.exceptions.WAFInvalidParameterException
    WAFV2.Client.exceptions.WAFInvalidOperationException
    
    """
    pass

def list_tags_for_resource(NextMarker=None, Limit=None, ResourceARN=None):
    """
    Retrieves the  TagInfoForResource for the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        NextMarker='string',
        Limit=123,
        ResourceARN='string'
    )
    
    
    :type NextMarker: string
    :param NextMarker: When you request a list of objects with a Limit setting, if the number of objects that are still available for retrieval exceeds the limit, AWS WAF returns a NextMarker value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.

    :type Limit: integer
    :param Limit: The maximum number of objects that you want AWS WAF to return for this request. If more objects are available, in the response, AWS WAF provides a NextMarker value that you can use in a subsequent call to get the next batch of objects.

    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource.\n

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
When you request a list of objects with a Limit setting, if the number of objects that are still available for retrieval exceeds the limit, AWS WAF returns a NextMarker value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.

TagInfoForResource (dict) --
The collection of tagging definitions for the resource.

ResourceARN (string) --
The Amazon Resource Name (ARN) of the resource.

TagList (list) --
The array of  Tag objects defined for the resource.

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

A collection of key:value pairs associated with an AWS resource. The key:value pair can be anything you define. Typically, the tag key represents a category (such as "environment") and the tag value represents a specific value within that category (such as "test," "development," or "production"). You can add up to 50 tags to each AWS resource.

Key (string) --
Part of the key:value pair that defines a tag. You can use a tag key to describe a category of information, such as "customer." Tag keys are case-sensitive.

Value (string) --
Part of the key:value pair that defines a tag. You can use a tag value to describe a specific value within a category, such as "companyA" or "companyB." Tag values are case-sensitive.













Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFNonexistentItemException
WAFV2.Client.exceptions.WAFTagOperationException
WAFV2.Client.exceptions.WAFTagOperationInternalErrorException
WAFV2.Client.exceptions.WAFInvalidOperationException


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
    WAFV2.Client.exceptions.WAFInternalErrorException
    WAFV2.Client.exceptions.WAFInvalidParameterException
    WAFV2.Client.exceptions.WAFNonexistentItemException
    WAFV2.Client.exceptions.WAFTagOperationException
    WAFV2.Client.exceptions.WAFTagOperationInternalErrorException
    WAFV2.Client.exceptions.WAFInvalidOperationException
    
    """
    pass

def list_web_acls(Scope=None, NextMarker=None, Limit=None):
    """
    Retrieves an array of  WebACLSummary objects for the web ACLs that you manage.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_web_acls(
        Scope='CLOUDFRONT'|'REGIONAL',
        NextMarker='string',
        Limit=123
    )
    
    
    :type Scope: string
    :param Scope: [REQUIRED]\nSpecifies whether this is for an AWS CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB) or an API Gateway stage.\nTo work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:\n\nCLI - Specify the Region when you use the CloudFront scope: --scope=CLOUDFRONT --region=us-east-1 .\nAPI and SDKs - For all calls, use the Region endpoint us-east-1.\n\n

    :type NextMarker: string
    :param NextMarker: When you request a list of objects with a Limit setting, if the number of objects that are still available for retrieval exceeds the limit, AWS WAF returns a NextMarker value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.

    :type Limit: integer
    :param Limit: The maximum number of objects that you want AWS WAF to return for this request. If more objects are available, in the response, AWS WAF provides a NextMarker value that you can use in a subsequent call to get the next batch of objects.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextMarker': 'string',
    'WebACLs': [
        {
            'Name': 'string',
            'Id': 'string',
            'Description': 'string',
            'LockToken': 'string',
            'ARN': 'string'
        },
    ]
}


Response Structure

(dict) --

NextMarker (string) --
When you request a list of objects with a Limit setting, if the number of objects that are still available for retrieval exceeds the limit, AWS WAF returns a NextMarker value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.

WebACLs (list) --

(dict) --

Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

High-level information about a  WebACL , returned by operations like create and list. This provides information like the ID, that you can use to retrieve and manage a WebACL , and the ARN, that you provide to operations like  AssociateWebACL .

Name (string) --
The name of the Web ACL. You cannot change the name of a Web ACL after you create it.

Id (string) --
The unique identifier for the Web ACL. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.

Description (string) --
A description of the Web ACL that helps with identification. You cannot change the description of a Web ACL after you create it.

LockToken (string) --
A token used for optimistic locking. AWS WAF returns a token to your get and list requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like update and delete. AWS WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a WAFOptimisticLockException . If this happens, perform another get, and use the new token returned by that operation.

ARN (string) --
The Amazon Resource Name (ARN) of the entity.











Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFInvalidOperationException


    :return: {
        'NextMarker': 'string',
        'WebACLs': [
            {
                'Name': 'string',
                'Id': 'string',
                'Description': 'string',
                'LockToken': 'string',
                'ARN': 'string'
            },
        ]
    }
    
    
    :returns: 
    WAFV2.Client.exceptions.WAFInternalErrorException
    WAFV2.Client.exceptions.WAFInvalidParameterException
    WAFV2.Client.exceptions.WAFInvalidOperationException
    
    """
    pass

def put_logging_configuration(LoggingConfiguration=None):
    """
    Enables the specified  LoggingConfiguration , to start logging from a web ACL, according to the configuration provided.
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
                    'SingleHeader': {
                        'Name': 'string'
                    },
                    'SingleQueryArgument': {
                        'Name': 'string'
                    },
                    'AllQueryArguments': {}
                    ,
                    'UriPath': {}
                    ,
                    'QueryString': {}
                    ,
                    'Body': {}
                    ,
                    'Method': {}
    
                },
            ]
        }
    )
    
    
    :type LoggingConfiguration: dict
    :param LoggingConfiguration: [REQUIRED]\n\nResourceArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the web ACL that you want to associate with LogDestinationConfigs .\n\nLogDestinationConfigs (list) -- [REQUIRED]The Amazon Kinesis Data Firehose Amazon Resource Name (ARNs) that you want to associate with the web ACL.\n\n(string) --\n\n\nRedactedFields (list) --The parts of the request that you want to keep out of the logs. For example, if you redact the cookie field, the cookie field in the firehose will be xxx .\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nThe part of a web request that you want AWS WAF to inspect. Include the single FieldToMatch type that you want to inspect, with additional specifications as needed, according to the type. You specify a single request component in FieldToMatch for each rule statement that requires it. To inspect more than one component of a web request, create a separate rule statement for each component.\n\nSingleHeader (dict) --Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.\n\nName (string) -- [REQUIRED]The name of the query header to inspect.\n\n\n\nSingleQueryArgument (dict) --Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.\nThis is used only to indicate the web request component for AWS WAF to inspect, in the FieldToMatch specification.\n\nName (string) -- [REQUIRED]The name of the query argument to inspect.\n\n\n\nAllQueryArguments (dict) --Inspect all query arguments.\n\nUriPath (dict) --Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .\n\nQueryString (dict) --Inspect the query string. This is the part of a URL that appears after a ? character, if any.\n\nBody (dict) --Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.\nNote that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as ByteMatchStatement or RegexPatternSetReferenceStatement , with a SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.\n\nMethod (dict) --Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.\n\n\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'LoggingConfiguration': {
        'ResourceArn': 'string',
        'LogDestinationConfigs': [
            'string',
        ],
        'RedactedFields': [
            {
                'SingleHeader': {
                    'Name': 'string'
                },
                'SingleQueryArgument': {
                    'Name': 'string'
                },
                'AllQueryArguments': {},
                'UriPath': {},
                'QueryString': {},
                'Body': {},
                'Method': {}
            },
        ]
    }
}


Response Structure

(dict) --
LoggingConfiguration (dict) --
ResourceArn (string) --The Amazon Resource Name (ARN) of the web ACL that you want to associate with LogDestinationConfigs .

LogDestinationConfigs (list) --The Amazon Kinesis Data Firehose Amazon Resource Name (ARNs) that you want to associate with the web ACL.

(string) --


RedactedFields (list) --The parts of the request that you want to keep out of the logs. For example, if you redact the cookie field, the cookie field in the firehose will be xxx .

(dict) --
Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

The part of a web request that you want AWS WAF to inspect. Include the single FieldToMatch type that you want to inspect, with additional specifications as needed, according to the type. You specify a single request component in FieldToMatch for each rule statement that requires it. To inspect more than one component of a web request, create a separate rule statement for each component.

SingleHeader (dict) --Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.

Name (string) --The name of the query header to inspect.



SingleQueryArgument (dict) --Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.

Name (string) --The name of the query argument to inspect.



AllQueryArguments (dict) --Inspect all query arguments.

UriPath (dict) --Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString (dict) --Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body (dict) --Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method (dict) --Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.












Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFNonexistentItemException
WAFV2.Client.exceptions.WAFOptimisticLockException
WAFV2.Client.exceptions.WAFServiceLinkedRoleErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFInvalidOperationException


    :return: {
        'LoggingConfiguration': {
            'ResourceArn': 'string',
            'LogDestinationConfigs': [
                'string',
            ],
            'RedactedFields': [
                {
                    'SingleHeader': {
                        'Name': 'string'
                    },
                    'SingleQueryArgument': {
                        'Name': 'string'
                    },
                    'AllQueryArguments': {},
                    'UriPath': {},
                    'QueryString': {},
                    'Body': {},
                    'Method': {}
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
    Attaches an IAM policy to the specified resource. Use this to share a rule group across accounts.
    You must be the owner of the rule group to perform this operation.
    This action is subject to the following restrictions:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_permission_policy(
        ResourceArn='string',
        Policy='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the RuleGroup to which you want to attach the policy.\n

    :type Policy: string
    :param Policy: [REQUIRED]\nThe policy to attach to the specified rule group.\nThe policy specifications must conform to the following:\n\nThe policy must be composed using IAM Policy version 2012-10-17 or version 2015-01-01.\nThe policy must include specifications for Effect , Action , and Principal .\nEffect must specify Allow .\nAction must specify wafv2:CreateWebACL , wafv2:UpdateWebACL , and wafv2:PutFirewallManagerRuleGroups . AWS WAF rejects any extra actions or wildcard actions in the policy.\nThe policy must not include a Resource parameter.\n\nFor more information, see IAM Policies .\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WAFV2.Client.exceptions.WAFNonexistentItemException
WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFInvalidPermissionPolicyException


    :return: {}
    
    
    :returns: 
    ResourceArn (string) -- [REQUIRED]
    The Amazon Resource Name (ARN) of the  RuleGroup to which you want to attach the policy.
    
    Policy (string) -- [REQUIRED]
    The policy to attach to the specified rule group.
    The policy specifications must conform to the following:
    
    The policy must be composed using IAM Policy version 2012-10-17 or version 2015-01-01.
    The policy must include specifications for Effect , Action , and Principal .
    Effect must specify Allow .
    Action must specify wafv2:CreateWebACL , wafv2:UpdateWebACL , and wafv2:PutFirewallManagerRuleGroups . AWS WAF rejects any extra actions or wildcard actions in the policy.
    The policy must not include a Resource parameter.
    
    For more information, see IAM Policies .
    
    
    """
    pass

def tag_resource(ResourceARN=None, Tags=None):
    """
    Associates tags with the specified AWS resource. Tags are key:value pairs that you can associate with AWS resources. For example, the tag key might be "customer" and the tag value might be "companyA." You can specify one or more tags to add to each container. You can add up to 50 tags to each AWS resource.
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
    :param ResourceARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nAn array of key:value pairs to associate with the resource.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nA collection of key:value pairs associated with an AWS resource. The key:value pair can be anything you define. Typically, the tag key represents a category (such as 'environment') and the tag value represents a specific value within that category (such as 'test,' 'development,' or 'production'). You can add up to 50 tags to each AWS resource.\n\nKey (string) -- [REQUIRED]Part of the key:value pair that defines a tag. You can use a tag key to describe a category of information, such as 'customer.' Tag keys are case-sensitive.\n\nValue (string) -- [REQUIRED]Part of the key:value pair that defines a tag. You can use a tag value to describe a specific value within a category, such as 'companyA' or 'companyB.' Tag values are case-sensitive.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFLimitsExceededException
WAFV2.Client.exceptions.WAFNonexistentItemException
WAFV2.Client.exceptions.WAFTagOperationException
WAFV2.Client.exceptions.WAFTagOperationInternalErrorException
WAFV2.Client.exceptions.WAFInvalidOperationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceARN=None, TagKeys=None):
    """
    Disassociates tags from an AWS resource. Tags are key:value pairs that you can associate with AWS resources. For example, the tag key might be "customer" and the tag value might be "companyA." You can specify one or more tags to add to each container. You can add up to 50 tags to each AWS resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceARN='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nAn array of keys identifying the tags to disassociate from the resource.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFNonexistentItemException
WAFV2.Client.exceptions.WAFTagOperationException
WAFV2.Client.exceptions.WAFTagOperationInternalErrorException
WAFV2.Client.exceptions.WAFInvalidOperationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_ip_set(Name=None, Scope=None, Id=None, Description=None, Addresses=None, LockToken=None):
    """
    Updates the specified  IPSet .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_ip_set(
        Name='string',
        Scope='CLOUDFRONT'|'REGIONAL',
        Id='string',
        Description='string',
        Addresses=[
            'string',
        ],
        LockToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the IP set. You cannot change the name of an IPSet after you create it.\n

    :type Scope: string
    :param Scope: [REQUIRED]\nSpecifies whether this is for an AWS CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB) or an API Gateway stage.\nTo work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:\n\nCLI - Specify the Region when you use the CloudFront scope: --scope=CLOUDFRONT --region=us-east-1 .\nAPI and SDKs - For all calls, use the Region endpoint us-east-1.\n\n

    :type Id: string
    :param Id: [REQUIRED]\nA unique identifier for the set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.\n

    :type Description: string
    :param Description: A description of the IP set that helps with identification. You cannot change the description of an IP set after you create it.

    :type Addresses: list
    :param Addresses: [REQUIRED]\nContains an array of strings that specify one or more IP addresses or blocks of IP addresses in Classless Inter-Domain Routing (CIDR) notation. AWS WAF supports all address ranges for IP versions IPv4 and IPv6.\nExamples:\n\nTo configure AWS WAF to allow, block, or count requests that originated from the IP address 192.0.2.44, specify 192.0.2.44/32 .\nTo configure AWS WAF to allow, block, or count requests that originated from IP addresses from 192.0.2.0 to 192.0.2.255, specify 192.0.2.0/24 .\nTo configure AWS WAF to allow, block, or count requests that originated from the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify 1111:0000:0000:0000:0000:0000:0000:0111/128 .\nTo configure AWS WAF to allow, block, or count requests that originated from IP addresses 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify 1111:0000:0000:0000:0000:0000:0000:0000/64 .\n\nFor more information about CIDR notation, see the Wikipedia entry Classless Inter-Domain Routing .\n\n(string) --\n\n

    :type LockToken: string
    :param LockToken: [REQUIRED]\nA token used for optimistic locking. AWS WAF returns a token to your get and list requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like update and delete. AWS WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a WAFOptimisticLockException . If this happens, perform another get, and use the new token returned by that operation.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'NextLockToken': 'string'
}


Response Structure

(dict) --

NextLockToken (string) --
A token used for optimistic locking. AWS WAF returns this token to your update requests. You use NextLockToken in the same manner as you use LockToken .







Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFNonexistentItemException
WAFV2.Client.exceptions.WAFDuplicateItemException
WAFV2.Client.exceptions.WAFOptimisticLockException
WAFV2.Client.exceptions.WAFLimitsExceededException
WAFV2.Client.exceptions.WAFInvalidOperationException


    :return: {
        'NextLockToken': 'string'
    }
    
    
    :returns: 
    WAFV2.Client.exceptions.WAFInternalErrorException
    WAFV2.Client.exceptions.WAFInvalidParameterException
    WAFV2.Client.exceptions.WAFNonexistentItemException
    WAFV2.Client.exceptions.WAFDuplicateItemException
    WAFV2.Client.exceptions.WAFOptimisticLockException
    WAFV2.Client.exceptions.WAFLimitsExceededException
    WAFV2.Client.exceptions.WAFInvalidOperationException
    
    """
    pass

def update_regex_pattern_set(Name=None, Scope=None, Id=None, Description=None, RegularExpressionList=None, LockToken=None):
    """
    Updates the specified  RegexPatternSet .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_regex_pattern_set(
        Name='string',
        Scope='CLOUDFRONT'|'REGIONAL',
        Id='string',
        Description='string',
        RegularExpressionList=[
            {
                'RegexString': 'string'
            },
        ],
        LockToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the set. You cannot change the name after you create the set.\n

    :type Scope: string
    :param Scope: [REQUIRED]\nSpecifies whether this is for an AWS CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB) or an API Gateway stage.\nTo work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:\n\nCLI - Specify the Region when you use the CloudFront scope: --scope=CLOUDFRONT --region=us-east-1 .\nAPI and SDKs - For all calls, use the Region endpoint us-east-1.\n\n

    :type Id: string
    :param Id: [REQUIRED]\nA unique identifier for the set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.\n

    :type Description: string
    :param Description: A description of the set that helps with identification. You cannot change the description of a set after you create it.

    :type RegularExpressionList: list
    :param RegularExpressionList: [REQUIRED]\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nA single regular expression. This is used in a RegexPatternSet .\n\nRegexString (string) --The string representing the regular expression.\n\n\n\n\n

    :type LockToken: string
    :param LockToken: [REQUIRED]\nA token used for optimistic locking. AWS WAF returns a token to your get and list requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like update and delete. AWS WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a WAFOptimisticLockException . If this happens, perform another get, and use the new token returned by that operation.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'NextLockToken': 'string'
}


Response Structure

(dict) --

NextLockToken (string) --
A token used for optimistic locking. AWS WAF returns this token to your update requests. You use NextLockToken in the same manner as you use LockToken .







Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFNonexistentItemException
WAFV2.Client.exceptions.WAFDuplicateItemException
WAFV2.Client.exceptions.WAFOptimisticLockException
WAFV2.Client.exceptions.WAFLimitsExceededException
WAFV2.Client.exceptions.WAFInvalidOperationException


    :return: {
        'NextLockToken': 'string'
    }
    
    
    :returns: 
    WAFV2.Client.exceptions.WAFInternalErrorException
    WAFV2.Client.exceptions.WAFInvalidParameterException
    WAFV2.Client.exceptions.WAFNonexistentItemException
    WAFV2.Client.exceptions.WAFDuplicateItemException
    WAFV2.Client.exceptions.WAFOptimisticLockException
    WAFV2.Client.exceptions.WAFLimitsExceededException
    WAFV2.Client.exceptions.WAFInvalidOperationException
    
    """
    pass

def update_rule_group(Name=None, Scope=None, Id=None, Description=None, Rules=None, VisibilityConfig=None, LockToken=None):
    """
    Updates the specified  RuleGroup .
    A rule group defines a collection of rules to inspect and control web requests that you can use in a  WebACL . When you create a rule group, you define an immutable capacity limit. If you update a rule group, you must stay within the capacity. This allows others to reuse the rule group with confidence in its capacity requirements.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_rule_group(
        Name='string',
        Scope='CLOUDFRONT'|'REGIONAL',
        Id='string',
        Description='string',
        Rules=[
            {
                'Name': 'string',
                'Priority': 123,
                'Statement': {
                    'ByteMatchStatement': {
                        'SearchString': b'bytes',
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {}
                            ,
                            'UriPath': {}
                            ,
                            'QueryString': {}
                            ,
                            'Body': {}
                            ,
                            'Method': {}
    
                        },
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ],
                        'PositionalConstraint': 'EXACTLY'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CONTAINS_WORD'
                    },
                    'SqliMatchStatement': {
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {}
                            ,
                            'UriPath': {}
                            ,
                            'QueryString': {}
                            ,
                            'Body': {}
                            ,
                            'Method': {}
    
                        },
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ]
                    },
                    'XssMatchStatement': {
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {}
                            ,
                            'UriPath': {}
                            ,
                            'QueryString': {}
                            ,
                            'Body': {}
                            ,
                            'Method': {}
    
                        },
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ]
                    },
                    'SizeConstraintStatement': {
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {}
                            ,
                            'UriPath': {}
                            ,
                            'QueryString': {}
                            ,
                            'Body': {}
                            ,
                            'Method': {}
    
                        },
                        'ComparisonOperator': 'EQ'|'NE'|'LE'|'LT'|'GE'|'GT',
                        'Size': 123,
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ]
                    },
                    'GeoMatchStatement': {
                        'CountryCodes': [
                            'AF'|'AX'|'AL'|'DZ'|'AS'|'AD'|'AO'|'AI'|'AQ'|'AG'|'AR'|'AM'|'AW'|'AU'|'AT'|'AZ'|'BS'|'BH'|'BD'|'BB'|'BY'|'BE'|'BZ'|'BJ'|'BM'|'BT'|'BO'|'BQ'|'BA'|'BW'|'BV'|'BR'|'IO'|'BN'|'BG'|'BF'|'BI'|'KH'|'CM'|'CA'|'CV'|'KY'|'CF'|'TD'|'CL'|'CN'|'CX'|'CC'|'CO'|'KM'|'CG'|'CD'|'CK'|'CR'|'CI'|'HR'|'CU'|'CW'|'CY'|'CZ'|'DK'|'DJ'|'DM'|'DO'|'EC'|'EG'|'SV'|'GQ'|'ER'|'EE'|'ET'|'FK'|'FO'|'FJ'|'FI'|'FR'|'GF'|'PF'|'TF'|'GA'|'GM'|'GE'|'DE'|'GH'|'GI'|'GR'|'GL'|'GD'|'GP'|'GU'|'GT'|'GG'|'GN'|'GW'|'GY'|'HT'|'HM'|'VA'|'HN'|'HK'|'HU'|'IS'|'IN'|'ID'|'IR'|'IQ'|'IE'|'IM'|'IL'|'IT'|'JM'|'JP'|'JE'|'JO'|'KZ'|'KE'|'KI'|'KP'|'KR'|'KW'|'KG'|'LA'|'LV'|'LB'|'LS'|'LR'|'LY'|'LI'|'LT'|'LU'|'MO'|'MK'|'MG'|'MW'|'MY'|'MV'|'ML'|'MT'|'MH'|'MQ'|'MR'|'MU'|'YT'|'MX'|'FM'|'MD'|'MC'|'MN'|'ME'|'MS'|'MA'|'MZ'|'MM'|'NA'|'NR'|'NP'|'NL'|'NC'|'NZ'|'NI'|'NE'|'NG'|'NU'|'NF'|'MP'|'NO'|'OM'|'PK'|'PW'|'PS'|'PA'|'PG'|'PY'|'PE'|'PH'|'PN'|'PL'|'PT'|'PR'|'QA'|'RE'|'RO'|'RU'|'RW'|'BL'|'SH'|'KN'|'LC'|'MF'|'PM'|'VC'|'WS'|'SM'|'ST'|'SA'|'SN'|'RS'|'SC'|'SL'|'SG'|'SX'|'SK'|'SI'|'SB'|'SO'|'ZA'|'GS'|'SS'|'ES'|'LK'|'SD'|'SR'|'SJ'|'SZ'|'SE'|'CH'|'SY'|'TW'|'TJ'|'TZ'|'TH'|'TL'|'TG'|'TK'|'TO'|'TT'|'TN'|'TR'|'TM'|'TC'|'TV'|'UG'|'UA'|'AE'|'GB'|'US'|'UM'|'UY'|'UZ'|'VU'|'VE'|'VN'|'VG'|'VI'|'WF'|'EH'|'YE'|'ZM'|'ZW',
                        ]
                    },
                    'RuleGroupReferenceStatement': {
                        'ARN': 'string',
                        'ExcludedRules': [
                            {
                                'Name': 'string'
                            },
                        ]
                    },
                    'IPSetReferenceStatement': {
                        'ARN': 'string'
                    },
                    'RegexPatternSetReferenceStatement': {
                        'ARN': 'string',
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {}
                            ,
                            'UriPath': {}
                            ,
                            'QueryString': {}
                            ,
                            'Body': {}
                            ,
                            'Method': {}
    
                        },
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ]
                    },
                    'RateBasedStatement': {
                        'Limit': 123,
                        'AggregateKeyType': 'IP',
                        'ScopeDownStatement': {'... recursive ...'}
                    },
                    'AndStatement': {
                        'Statements': [
                            {'... recursive ...'},
                        ]
                    },
                    'OrStatement': {
                        'Statements': [
                            {'... recursive ...'},
                        ]
                    },
                    'NotStatement': {
                        'Statement': {'... recursive ...'}
                    },
                    'ManagedRuleGroupStatement': {
                        'VendorName': 'string',
                        'Name': 'string',
                        'ExcludedRules': [
                            {
                                'Name': 'string'
                            },
                        ]
                    }
                },
                'Action': {
                    'Block': {}
                    ,
                    'Allow': {}
                    ,
                    'Count': {}
    
                },
                'OverrideAction': {
                    'Count': {}
                    ,
                    'None': {}
    
                },
                'VisibilityConfig': {
                    'SampledRequestsEnabled': True|False,
                    'CloudWatchMetricsEnabled': True|False,
                    'MetricName': 'string'
                }
            },
        ],
        VisibilityConfig={
            'SampledRequestsEnabled': True|False,
            'CloudWatchMetricsEnabled': True|False,
            'MetricName': 'string'
        },
        LockToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the rule group. You cannot change the name of a rule group after you create it.\n

    :type Scope: string
    :param Scope: [REQUIRED]\nSpecifies whether this is for an AWS CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB) or an API Gateway stage.\nTo work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:\n\nCLI - Specify the Region when you use the CloudFront scope: --scope=CLOUDFRONT --region=us-east-1 .\nAPI and SDKs - For all calls, use the Region endpoint us-east-1.\n\n

    :type Id: string
    :param Id: [REQUIRED]\nA unique identifier for the rule group. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.\n

    :type Description: string
    :param Description: A description of the rule group that helps with identification. You cannot change the description of a rule group after you create it.

    :type Rules: list
    :param Rules: The Rule statements used to identify the web requests that you want to allow, block, or count. Each rule includes one top-level statement that AWS WAF uses to identify matching web requests, and parameters that govern how AWS WAF handles them.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nA single rule, which you can use in a WebACL or RuleGroup to identify web requests that you want to allow, block, or count. Each rule includes one top-level Statement that AWS WAF uses to identify matching web requests, and parameters that govern how AWS WAF handles them.\n\nName (string) -- [REQUIRED]The name of the rule. You can\'t change the name of a Rule after you create it.\n\nPriority (integer) -- [REQUIRED]If you define more than one Rule in a WebACL , AWS WAF evaluates each request against the Rules in order based on the value of Priority . AWS WAF processes rules with lower priority first. The priorities don\'t need to be consecutive, but they must all be different.\n\nStatement (dict) -- [REQUIRED]The AWS WAF processing statement for the rule, for example ByteMatchStatement or SizeConstraintStatement .\n\nByteMatchStatement (dict) --A rule statement that defines a string match search for AWS WAF to apply to web requests. The byte match statement provides the bytes to search for, the location in requests that you want AWS WAF to search, and other settings. The bytes to search for are typically a string that corresponds with ASCII characters. In the AWS WAF console and the developer guide, this is refered to as a string match statement.\n\nSearchString (bytes) -- [REQUIRED]A string value that you want AWS WAF to search for. AWS WAF searches only in the part of web requests that you designate for inspection in FieldToMatch . The maximum length of the value is 50 bytes.\nValid values depend on the component that you specify for inspection in FieldToMatch :\n\nMethod : The HTTP method that you want AWS WAF to search for. This indicates the type of operation specified in the request.\nUriPath : The value that you want AWS WAF to search for in the URI path, for example, /images/daily-ad.jpg .\n\nIf SearchString includes alphabetic characters A-Z and a-z, note that the value is case sensitive.\n\nIf you\'re using the AWS WAF API\nSpecify a base64-encoded version of the value. The maximum length of the value before you base64-encode it is 50 bytes.\nFor example, suppose the value of Type is HEADER and the value of Data is User-Agent . If you want to search the User-Agent header for the value BadBot , you base64-encode BadBot using MIME base64-encoding and include the resulting value, QmFkQm90 , in the value of SearchString .\n\nIf you\'re using the AWS CLI or one of the AWS SDKs\nThe value that you want AWS WAF to search for. The SDK automatically base64 encodes the value.\n\nFieldToMatch (dict) -- [REQUIRED]The part of a web request that you want AWS WAF to inspect. For more information, see FieldToMatch .\n\nSingleHeader (dict) --Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.\n\nName (string) -- [REQUIRED]The name of the query header to inspect.\n\n\n\nSingleQueryArgument (dict) --Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.\nThis is used only to indicate the web request component for AWS WAF to inspect, in the FieldToMatch specification.\n\nName (string) -- [REQUIRED]The name of the query argument to inspect.\n\n\n\nAllQueryArguments (dict) --Inspect all query arguments.\n\nUriPath (dict) --Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .\n\nQueryString (dict) --Inspect the query string. This is the part of a URL that appears after a ? character, if any.\n\nBody (dict) --Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.\nNote that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as ByteMatchStatement or RegexPatternSetReferenceStatement , with a SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.\n\nMethod (dict) --Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.\n\n\n\nTextTransformations (list) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nText transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.\n\nPriority (integer) -- [REQUIRED]Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.\n\nType (string) -- [REQUIRED]You can specify the following transformation types:\n\nCMD_LINE\nWhen you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:\n\nDelete the following characters: ' \' ^\nDelete spaces before the following characters: / (\nReplace the following characters with a space: , ;\nReplace multiple spaces with one space\nConvert uppercase letters (A-Z) to lowercase (a-z)\n\n\nCOMPRESS_WHITE_SPACE\nUse this option to replace the following characters with a space character (decimal 32):\n\nf, formfeed, decimal 12\nt, tab, decimal 9\nn, newline, decimal 10\nr, carriage return, decimal 13\nv, vertical tab, decimal 11\nnon-breaking space, decimal 160\n\n\nCOMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE\n\nUse this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:\n\nReplaces (ampersand)quot; with '\nReplaces (ampersand)nbsp; with a non-breaking space, decimal 160\nReplaces (ampersand)lt; with a 'less than' symbol\nReplaces (ampersand)gt; with >\nReplaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters\nReplaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters\n\n\nLOWERCASE\nUse this option to convert uppercase letters (A-Z) to lowercase (a-z).\n\nURL_DECODE\nUse this option to decode a URL-encoded value.\n\nNONE\nSpecify NONE if you don\'t want any text transformations.\n\n\n\n\n\nPositionalConstraint (string) -- [REQUIRED]The area within the portion of a web request that you want AWS WAF to search for SearchString . Valid values include the following:\n\nCONTAINS\nThe specified part of the web request must include the value of SearchString , but the location doesn\'t matter.\n\nCONTAINS_WORD\nThe specified part of the web request must include the value of SearchString , and SearchString must contain only alphanumeric characters or underscore (A-Z, a-z, 0-9, or _). In addition, SearchString must be a word, which means that both of the following are true:\n\nSearchString is at the beginning of the specified part of the web request or is preceded by a character other than an alphanumeric character or underscore (_). Examples include the value of a header and ;BadBot .\nSearchString is at the end of the specified part of the web request or is followed by a character other than an alphanumeric character or underscore (_), for example, BadBot; and -BadBot; .\n\n\nEXACTLY\nThe value of the specified part of the web request must exactly match the value of SearchString .\n\nSTARTS_WITH\nThe value of SearchString must appear at the beginning of the specified part of the web request.\n\nENDS_WITH\nThe value of SearchString must appear at the end of the specified part of the web request.\n\n\n\nSqliMatchStatement (dict) --Attackers sometimes insert malicious SQL code into web requests in an effort to extract data from your database. To allow or block web requests that appear to contain malicious SQL code, create one or more SQL injection match conditions. An SQL injection match condition identifies the part of web requests, such as the URI or the query string, that you want AWS WAF to inspect. Later in the process, when you create a web ACL, you specify whether to allow or block requests that appear to contain malicious SQL code.\n\nFieldToMatch (dict) -- [REQUIRED]The part of a web request that you want AWS WAF to inspect. For more information, see FieldToMatch .\n\nSingleHeader (dict) --Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.\n\nName (string) -- [REQUIRED]The name of the query header to inspect.\n\n\n\nSingleQueryArgument (dict) --Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.\nThis is used only to indicate the web request component for AWS WAF to inspect, in the FieldToMatch specification.\n\nName (string) -- [REQUIRED]The name of the query argument to inspect.\n\n\n\nAllQueryArguments (dict) --Inspect all query arguments.\n\nUriPath (dict) --Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .\n\nQueryString (dict) --Inspect the query string. This is the part of a URL that appears after a ? character, if any.\n\nBody (dict) --Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.\nNote that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as ByteMatchStatement or RegexPatternSetReferenceStatement , with a SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.\n\nMethod (dict) --Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.\n\n\n\nTextTransformations (list) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nText transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.\n\nPriority (integer) -- [REQUIRED]Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.\n\nType (string) -- [REQUIRED]You can specify the following transformation types:\n\nCMD_LINE\nWhen you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:\n\nDelete the following characters: ' \' ^\nDelete spaces before the following characters: / (\nReplace the following characters with a space: , ;\nReplace multiple spaces with one space\nConvert uppercase letters (A-Z) to lowercase (a-z)\n\n\nCOMPRESS_WHITE_SPACE\nUse this option to replace the following characters with a space character (decimal 32):\n\nf, formfeed, decimal 12\nt, tab, decimal 9\nn, newline, decimal 10\nr, carriage return, decimal 13\nv, vertical tab, decimal 11\nnon-breaking space, decimal 160\n\n\nCOMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE\n\nUse this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:\n\nReplaces (ampersand)quot; with '\nReplaces (ampersand)nbsp; with a non-breaking space, decimal 160\nReplaces (ampersand)lt; with a 'less than' symbol\nReplaces (ampersand)gt; with >\nReplaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters\nReplaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters\n\n\nLOWERCASE\nUse this option to convert uppercase letters (A-Z) to lowercase (a-z).\n\nURL_DECODE\nUse this option to decode a URL-encoded value.\n\nNONE\nSpecify NONE if you don\'t want any text transformations.\n\n\n\n\n\n\n\nXssMatchStatement (dict) --A rule statement that defines a cross-site scripting (XSS) match search for AWS WAF to apply to web requests. XSS attacks are those where the attacker uses vulnerabilities in a benign website as a vehicle to inject malicious client-site scripts into other legitimate web browsers. The XSS match statement provides the location in requests that you want AWS WAF to search and text transformations to use on the search area before AWS WAF searches for character sequences that are likely to be malicious strings.\n\nFieldToMatch (dict) -- [REQUIRED]The part of a web request that you want AWS WAF to inspect. For more information, see FieldToMatch .\n\nSingleHeader (dict) --Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.\n\nName (string) -- [REQUIRED]The name of the query header to inspect.\n\n\n\nSingleQueryArgument (dict) --Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.\nThis is used only to indicate the web request component for AWS WAF to inspect, in the FieldToMatch specification.\n\nName (string) -- [REQUIRED]The name of the query argument to inspect.\n\n\n\nAllQueryArguments (dict) --Inspect all query arguments.\n\nUriPath (dict) --Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .\n\nQueryString (dict) --Inspect the query string. This is the part of a URL that appears after a ? character, if any.\n\nBody (dict) --Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.\nNote that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as ByteMatchStatement or RegexPatternSetReferenceStatement , with a SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.\n\nMethod (dict) --Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.\n\n\n\nTextTransformations (list) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nText transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.\n\nPriority (integer) -- [REQUIRED]Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.\n\nType (string) -- [REQUIRED]You can specify the following transformation types:\n\nCMD_LINE\nWhen you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:\n\nDelete the following characters: ' \' ^\nDelete spaces before the following characters: / (\nReplace the following characters with a space: , ;\nReplace multiple spaces with one space\nConvert uppercase letters (A-Z) to lowercase (a-z)\n\n\nCOMPRESS_WHITE_SPACE\nUse this option to replace the following characters with a space character (decimal 32):\n\nf, formfeed, decimal 12\nt, tab, decimal 9\nn, newline, decimal 10\nr, carriage return, decimal 13\nv, vertical tab, decimal 11\nnon-breaking space, decimal 160\n\n\nCOMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE\n\nUse this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:\n\nReplaces (ampersand)quot; with '\nReplaces (ampersand)nbsp; with a non-breaking space, decimal 160\nReplaces (ampersand)lt; with a 'less than' symbol\nReplaces (ampersand)gt; with >\nReplaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters\nReplaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters\n\n\nLOWERCASE\nUse this option to convert uppercase letters (A-Z) to lowercase (a-z).\n\nURL_DECODE\nUse this option to decode a URL-encoded value.\n\nNONE\nSpecify NONE if you don\'t want any text transformations.\n\n\n\n\n\n\n\nSizeConstraintStatement (dict) --A rule statement that compares a number of bytes against the size of a request component, using a comparison operator, such as greater than (>) or less than (<). For example, you can use a size constraint statement to look for query strings that are longer than 100 bytes.\nIf you configure AWS WAF to inspect the request body, AWS WAF inspects only the first 8192 bytes (8 KB). If the request body for your web requests never exceeds 8192 bytes, you can create a size constraint condition and block requests that have a request body greater than 8192 bytes.\nIf you choose URI for the value of Part of the request to filter on, the slash (/) in the URI counts as one character. For example, the URI /logo.jpg is nine characters long.\n\nFieldToMatch (dict) -- [REQUIRED]The part of a web request that you want AWS WAF to inspect. For more information, see FieldToMatch .\n\nSingleHeader (dict) --Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.\n\nName (string) -- [REQUIRED]The name of the query header to inspect.\n\n\n\nSingleQueryArgument (dict) --Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.\nThis is used only to indicate the web request component for AWS WAF to inspect, in the FieldToMatch specification.\n\nName (string) -- [REQUIRED]The name of the query argument to inspect.\n\n\n\nAllQueryArguments (dict) --Inspect all query arguments.\n\nUriPath (dict) --Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .\n\nQueryString (dict) --Inspect the query string. This is the part of a URL that appears after a ? character, if any.\n\nBody (dict) --Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.\nNote that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as ByteMatchStatement or RegexPatternSetReferenceStatement , with a SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.\n\nMethod (dict) --Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.\n\n\n\nComparisonOperator (string) -- [REQUIRED]The operator to use to compare the request part to the size setting.\n\nSize (integer) -- [REQUIRED]The size, in byte, to compare to the request part, after any transformations.\n\nTextTransformations (list) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nText transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.\n\nPriority (integer) -- [REQUIRED]Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.\n\nType (string) -- [REQUIRED]You can specify the following transformation types:\n\nCMD_LINE\nWhen you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:\n\nDelete the following characters: ' \' ^\nDelete spaces before the following characters: / (\nReplace the following characters with a space: , ;\nReplace multiple spaces with one space\nConvert uppercase letters (A-Z) to lowercase (a-z)\n\n\nCOMPRESS_WHITE_SPACE\nUse this option to replace the following characters with a space character (decimal 32):\n\nf, formfeed, decimal 12\nt, tab, decimal 9\nn, newline, decimal 10\nr, carriage return, decimal 13\nv, vertical tab, decimal 11\nnon-breaking space, decimal 160\n\n\nCOMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE\n\nUse this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:\n\nReplaces (ampersand)quot; with '\nReplaces (ampersand)nbsp; with a non-breaking space, decimal 160\nReplaces (ampersand)lt; with a 'less than' symbol\nReplaces (ampersand)gt; with >\nReplaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters\nReplaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters\n\n\nLOWERCASE\nUse this option to convert uppercase letters (A-Z) to lowercase (a-z).\n\nURL_DECODE\nUse this option to decode a URL-encoded value.\n\nNONE\nSpecify NONE if you don\'t want any text transformations.\n\n\n\n\n\n\n\nGeoMatchStatement (dict) --A rule statement used to identify web requests based on country of origin.\n\nCountryCodes (list) --An array of two-character country codes, for example, [ 'US', 'CN' ] , from the alpha-2 country ISO codes of the ISO 3166 international standard.\n\n(string) --\n\n\n\n\nRuleGroupReferenceStatement (dict) --A rule statement used to run the rules that are defined in a RuleGroup . To use this, create a rule group with your rules, then provide the ARN of the rule group in this statement.\nYou cannot nest a RuleGroupReferenceStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.\n\nARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the entity.\n\nExcludedRules (list) --The names of rules that are in the referenced rule group, but that you want AWS WAF to exclude from processing for this rule statement.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nSpecifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.\n\nName (string) -- [REQUIRED]The name of the rule to exclude.\n\n\n\n\n\n\n\nIPSetReferenceStatement (dict) --A rule statement used to detect web requests coming from particular IP addresses or address ranges. To use this, create an IPSet that specifies the addresses you want to detect, then use the ARN of that set in this statement. To create an IP set, see CreateIPSet .\nEach IP set rule statement references an IP set. You create and maintain the set independent of your rules. This allows you to use the single set in multiple rules. When you update the referenced set, AWS WAF automatically updates all rules that reference it.\n\nARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the IPSet that this statement references.\n\n\n\nRegexPatternSetReferenceStatement (dict) --A rule statement used to search web request components for matches with regular expressions. To use this, create a RegexPatternSet that specifies the expressions that you want to detect, then use the ARN of that set in this statement. A web request matches the pattern set rule statement if the request component matches any of the patterns in the set. To create a regex pattern set, see CreateRegexPatternSet .\nEach regex pattern set rule statement references a regex pattern set. You create and maintain the set independent of your rules. This allows you to use the single set in multiple rules. When you update the referenced set, AWS WAF automatically updates all rules that reference it.\n\nARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the RegexPatternSet that this statement references.\n\nFieldToMatch (dict) -- [REQUIRED]The part of a web request that you want AWS WAF to inspect. For more information, see FieldToMatch .\n\nSingleHeader (dict) --Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.\n\nName (string) -- [REQUIRED]The name of the query header to inspect.\n\n\n\nSingleQueryArgument (dict) --Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.\nThis is used only to indicate the web request component for AWS WAF to inspect, in the FieldToMatch specification.\n\nName (string) -- [REQUIRED]The name of the query argument to inspect.\n\n\n\nAllQueryArguments (dict) --Inspect all query arguments.\n\nUriPath (dict) --Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .\n\nQueryString (dict) --Inspect the query string. This is the part of a URL that appears after a ? character, if any.\n\nBody (dict) --Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.\nNote that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as ByteMatchStatement or RegexPatternSetReferenceStatement , with a SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.\n\nMethod (dict) --Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.\n\n\n\nTextTransformations (list) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nText transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.\n\nPriority (integer) -- [REQUIRED]Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.\n\nType (string) -- [REQUIRED]You can specify the following transformation types:\n\nCMD_LINE\nWhen you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:\n\nDelete the following characters: ' \' ^\nDelete spaces before the following characters: / (\nReplace the following characters with a space: , ;\nReplace multiple spaces with one space\nConvert uppercase letters (A-Z) to lowercase (a-z)\n\n\nCOMPRESS_WHITE_SPACE\nUse this option to replace the following characters with a space character (decimal 32):\n\nf, formfeed, decimal 12\nt, tab, decimal 9\nn, newline, decimal 10\nr, carriage return, decimal 13\nv, vertical tab, decimal 11\nnon-breaking space, decimal 160\n\n\nCOMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE\n\nUse this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:\n\nReplaces (ampersand)quot; with '\nReplaces (ampersand)nbsp; with a non-breaking space, decimal 160\nReplaces (ampersand)lt; with a 'less than' symbol\nReplaces (ampersand)gt; with >\nReplaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters\nReplaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters\n\n\nLOWERCASE\nUse this option to convert uppercase letters (A-Z) to lowercase (a-z).\n\nURL_DECODE\nUse this option to decode a URL-encoded value.\n\nNONE\nSpecify NONE if you don\'t want any text transformations.\n\n\n\n\n\n\n\nRateBasedStatement (dict) --A rate-based rule tracks the rate of requests for each originating IP address, and triggers the rule action when the rate exceeds a limit that you specify on the number of requests in any 5-minute time span. You can use this to put a temporary block on requests from an IP address that is sending excessive requests.\nWhen the rule action triggers, AWS WAF blocks additional requests from the IP address until the request rate falls below the limit.\nYou can optionally nest another statement inside the rate-based statement, to narrow the scope of the rule so that it only counts requests that match the nested statement. For example, based on recent requests that you have seen from an attacker, you might create a rate-based rule with a nested AND rule statement that contains the following nested statements:\n\nAn IP match statement with an IP set that specified the address 192.0.2.44.\nA string match statement that searches in the User-Agent header for the string BadBot.\n\nIn this rate-based rule, you also define a rate limit. For this example, the rate limit is 1,000. Requests that meet both of the conditions in the statements are counted. If the count exceeds 1,000 requests per five minutes, the rule action triggers. Requests that do not meet both conditions are not counted towards the rate limit and are not affected by this rule.\nYou cannot nest a RateBasedStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.\n\nLimit (integer) -- [REQUIRED]The limit on requests per 5-minute period for a single originating IP address. If the statement includes a ScopDownStatement , this limit is applied only to the requests that match the statement.\n\nAggregateKeyType (string) -- [REQUIRED]Setting that indicates how to aggregate the request counts. Currently, you must set this to IP . The request counts are aggregated on IP addresses.\n\nScopeDownStatement (dict) --An optional nested statement that narrows the scope of the rate-based statement to matching web requests. This can be any nestable statement, and you can nest statements at any level below this scope-down statement.\n\n\n\nAndStatement (dict) --A logical rule statement used to combine other rule statements with AND logic. You provide more than one Statement within the AndStatement .\n\nStatements (list) -- [REQUIRED]The statements to combine with AND logic. You can use any statements that can be nested.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nThe processing guidance for a Rule , used by AWS WAF to determine whether a web request matches the rule.\n\n\n\n\n\nOrStatement (dict) --A logical rule statement used to combine other rule statements with OR logic. You provide more than one Statement within the OrStatement .\n\nStatements (list) -- [REQUIRED]The statements to combine with OR logic. You can use any statements that can be nested.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nThe processing guidance for a Rule , used by AWS WAF to determine whether a web request matches the rule.\n\n\n\n\n\nNotStatement (dict) --A logical rule statement used to negate the results of another rule statement. You provide one Statement within the NotStatement .\n\nStatement (dict) --The statement to negate. You can use any statement that can be nested.\n\n\n\nManagedRuleGroupStatement (dict) --A rule statement used to run the rules that are defined in a managed rule group. To use this, provide the vendor name and the name of the rule group in this statement. You can retrieve the required names by calling ListAvailableManagedRuleGroups .\nYou can\'t nest a ManagedRuleGroupStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.\n\nVendorName (string) -- [REQUIRED]The name of the managed rule group vendor. You use this, along with the rule group name, to identify the rule group.\n\nName (string) -- [REQUIRED]The name of the managed rule group. You use this, along with the vendor name, to identify the rule group.\n\nExcludedRules (list) --The rules whose actions are set to COUNT by the web ACL, regardless of the action that is set on the rule. This effectively excludes the rule from acting on web requests.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nSpecifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.\n\nName (string) -- [REQUIRED]The name of the rule to exclude.\n\n\n\n\n\n\n\n\n\nAction (dict) --The action that AWS WAF should take on a web request when it matches the rule statement. Settings at the web ACL level can override the rule action setting.\nThis is used only for rules whose statements do not reference a rule group. Rule statements that reference a rule group include RuleGroupReferenceStatement and ManagedRuleGroupStatement .\nYou must specify either this Action setting or the rule OverrideAction setting, but not both:\n\nIf the rule statement does not reference a rule group, use this rule action setting and not the rule override action setting.\nIf the rule statement references a rule group, use the override action setting and not this action setting.\n\n\nBlock (dict) --Instructs AWS WAF to block the web request.\n\nAllow (dict) --Instructs AWS WAF to allow the web request.\n\nCount (dict) --Instructs AWS WAF to count the web request and allow it.\n\n\n\nOverrideAction (dict) --The override action to apply to the rules in a rule group. Used only for rule statements that reference a rule group, like RuleGroupReferenceStatement and ManagedRuleGroupStatement .\nSet the override action to none to leave the rule actions in effect. Set it to count to only count matches, regardless of the rule action settings.\nIn a Rule , you must specify either this OverrideAction setting or the rule Action setting, but not both:\n\nIf the rule statement references a rule group, use this override action setting and not the action setting.\nIf the rule statement does not reference a rule group, use the rule action setting and not this rule override action setting.\n\n\nCount (dict) --Override the rule action setting to count.\n\nNone (dict) --Don\'t override the rule action setting.\n\n\n\nVisibilityConfig (dict) -- [REQUIRED]Defines and enables Amazon CloudWatch metrics and web request sample collection.\n\nSampledRequestsEnabled (boolean) -- [REQUIRED]A boolean indicating whether AWS WAF should store a sampling of the web requests that match the rules. You can view the sampled requests through the AWS WAF console.\n\nCloudWatchMetricsEnabled (boolean) -- [REQUIRED]A boolean indicating whether the associated resource sends metrics to CloudWatch. For the list of available metrics, see AWS WAF Metrics .\n\nMetricName (string) -- [REQUIRED]A name of the CloudWatch metric. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with length from one to 128 characters. It can\'t contain whitespace or metric names reserved for AWS WAF, for example 'All' and 'Default_Action.' You can\'t change a MetricName after you create a VisibilityConfig .\n\n\n\n\n\n\n

    :type VisibilityConfig: dict
    :param VisibilityConfig: [REQUIRED]\nDefines and enables Amazon CloudWatch metrics and web request sample collection.\n\nSampledRequestsEnabled (boolean) -- [REQUIRED]A boolean indicating whether AWS WAF should store a sampling of the web requests that match the rules. You can view the sampled requests through the AWS WAF console.\n\nCloudWatchMetricsEnabled (boolean) -- [REQUIRED]A boolean indicating whether the associated resource sends metrics to CloudWatch. For the list of available metrics, see AWS WAF Metrics .\n\nMetricName (string) -- [REQUIRED]A name of the CloudWatch metric. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with length from one to 128 characters. It can\'t contain whitespace or metric names reserved for AWS WAF, for example 'All' and 'Default_Action.' You can\'t change a MetricName after you create a VisibilityConfig .\n\n\n

    :type LockToken: string
    :param LockToken: [REQUIRED]\nA token used for optimistic locking. AWS WAF returns a token to your get and list requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like update and delete. AWS WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a WAFOptimisticLockException . If this happens, perform another get, and use the new token returned by that operation.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'NextLockToken': 'string'
}


Response Structure

(dict) --

NextLockToken (string) --
A token used for optimistic locking. AWS WAF returns this token to your update requests. You use NextLockToken in the same manner as you use LockToken .







Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFNonexistentItemException
WAFV2.Client.exceptions.WAFDuplicateItemException
WAFV2.Client.exceptions.WAFOptimisticLockException
WAFV2.Client.exceptions.WAFLimitsExceededException
WAFV2.Client.exceptions.WAFUnavailableEntityException
WAFV2.Client.exceptions.WAFSubscriptionNotFoundException
WAFV2.Client.exceptions.WAFInvalidOperationException


    :return: {
        'NextLockToken': 'string'
    }
    
    
    :returns: 
    WAFV2.Client.exceptions.WAFInternalErrorException
    WAFV2.Client.exceptions.WAFInvalidParameterException
    WAFV2.Client.exceptions.WAFNonexistentItemException
    WAFV2.Client.exceptions.WAFDuplicateItemException
    WAFV2.Client.exceptions.WAFOptimisticLockException
    WAFV2.Client.exceptions.WAFLimitsExceededException
    WAFV2.Client.exceptions.WAFUnavailableEntityException
    WAFV2.Client.exceptions.WAFSubscriptionNotFoundException
    WAFV2.Client.exceptions.WAFInvalidOperationException
    
    """
    pass

def update_web_acl(Name=None, Scope=None, Id=None, DefaultAction=None, Description=None, Rules=None, VisibilityConfig=None, LockToken=None):
    """
    Updates the specified  WebACL .
    A Web ACL defines a collection of rules to use to inspect and control web requests. Each rule has an action defined (allow, block, or count) for requests that match the statement of the rule. In the Web ACL, you assign a default action to take (allow, block) for any request that does not match any of the rules. The rules in a Web ACL can be a combination of the types  Rule ,  RuleGroup , and managed rule group. You can associate a Web ACL with one or more AWS resources to protect. The resources can be Amazon CloudFront, an Amazon API Gateway API, or an Application Load Balancer.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_web_acl(
        Name='string',
        Scope='CLOUDFRONT'|'REGIONAL',
        Id='string',
        DefaultAction={
            'Block': {}
            ,
            'Allow': {}
    
        },
        Description='string',
        Rules=[
            {
                'Name': 'string',
                'Priority': 123,
                'Statement': {
                    'ByteMatchStatement': {
                        'SearchString': b'bytes',
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {}
                            ,
                            'UriPath': {}
                            ,
                            'QueryString': {}
                            ,
                            'Body': {}
                            ,
                            'Method': {}
    
                        },
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ],
                        'PositionalConstraint': 'EXACTLY'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CONTAINS_WORD'
                    },
                    'SqliMatchStatement': {
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {}
                            ,
                            'UriPath': {}
                            ,
                            'QueryString': {}
                            ,
                            'Body': {}
                            ,
                            'Method': {}
    
                        },
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ]
                    },
                    'XssMatchStatement': {
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {}
                            ,
                            'UriPath': {}
                            ,
                            'QueryString': {}
                            ,
                            'Body': {}
                            ,
                            'Method': {}
    
                        },
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ]
                    },
                    'SizeConstraintStatement': {
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {}
                            ,
                            'UriPath': {}
                            ,
                            'QueryString': {}
                            ,
                            'Body': {}
                            ,
                            'Method': {}
    
                        },
                        'ComparisonOperator': 'EQ'|'NE'|'LE'|'LT'|'GE'|'GT',
                        'Size': 123,
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ]
                    },
                    'GeoMatchStatement': {
                        'CountryCodes': [
                            'AF'|'AX'|'AL'|'DZ'|'AS'|'AD'|'AO'|'AI'|'AQ'|'AG'|'AR'|'AM'|'AW'|'AU'|'AT'|'AZ'|'BS'|'BH'|'BD'|'BB'|'BY'|'BE'|'BZ'|'BJ'|'BM'|'BT'|'BO'|'BQ'|'BA'|'BW'|'BV'|'BR'|'IO'|'BN'|'BG'|'BF'|'BI'|'KH'|'CM'|'CA'|'CV'|'KY'|'CF'|'TD'|'CL'|'CN'|'CX'|'CC'|'CO'|'KM'|'CG'|'CD'|'CK'|'CR'|'CI'|'HR'|'CU'|'CW'|'CY'|'CZ'|'DK'|'DJ'|'DM'|'DO'|'EC'|'EG'|'SV'|'GQ'|'ER'|'EE'|'ET'|'FK'|'FO'|'FJ'|'FI'|'FR'|'GF'|'PF'|'TF'|'GA'|'GM'|'GE'|'DE'|'GH'|'GI'|'GR'|'GL'|'GD'|'GP'|'GU'|'GT'|'GG'|'GN'|'GW'|'GY'|'HT'|'HM'|'VA'|'HN'|'HK'|'HU'|'IS'|'IN'|'ID'|'IR'|'IQ'|'IE'|'IM'|'IL'|'IT'|'JM'|'JP'|'JE'|'JO'|'KZ'|'KE'|'KI'|'KP'|'KR'|'KW'|'KG'|'LA'|'LV'|'LB'|'LS'|'LR'|'LY'|'LI'|'LT'|'LU'|'MO'|'MK'|'MG'|'MW'|'MY'|'MV'|'ML'|'MT'|'MH'|'MQ'|'MR'|'MU'|'YT'|'MX'|'FM'|'MD'|'MC'|'MN'|'ME'|'MS'|'MA'|'MZ'|'MM'|'NA'|'NR'|'NP'|'NL'|'NC'|'NZ'|'NI'|'NE'|'NG'|'NU'|'NF'|'MP'|'NO'|'OM'|'PK'|'PW'|'PS'|'PA'|'PG'|'PY'|'PE'|'PH'|'PN'|'PL'|'PT'|'PR'|'QA'|'RE'|'RO'|'RU'|'RW'|'BL'|'SH'|'KN'|'LC'|'MF'|'PM'|'VC'|'WS'|'SM'|'ST'|'SA'|'SN'|'RS'|'SC'|'SL'|'SG'|'SX'|'SK'|'SI'|'SB'|'SO'|'ZA'|'GS'|'SS'|'ES'|'LK'|'SD'|'SR'|'SJ'|'SZ'|'SE'|'CH'|'SY'|'TW'|'TJ'|'TZ'|'TH'|'TL'|'TG'|'TK'|'TO'|'TT'|'TN'|'TR'|'TM'|'TC'|'TV'|'UG'|'UA'|'AE'|'GB'|'US'|'UM'|'UY'|'UZ'|'VU'|'VE'|'VN'|'VG'|'VI'|'WF'|'EH'|'YE'|'ZM'|'ZW',
                        ]
                    },
                    'RuleGroupReferenceStatement': {
                        'ARN': 'string',
                        'ExcludedRules': [
                            {
                                'Name': 'string'
                            },
                        ]
                    },
                    'IPSetReferenceStatement': {
                        'ARN': 'string'
                    },
                    'RegexPatternSetReferenceStatement': {
                        'ARN': 'string',
                        'FieldToMatch': {
                            'SingleHeader': {
                                'Name': 'string'
                            },
                            'SingleQueryArgument': {
                                'Name': 'string'
                            },
                            'AllQueryArguments': {}
                            ,
                            'UriPath': {}
                            ,
                            'QueryString': {}
                            ,
                            'Body': {}
                            ,
                            'Method': {}
    
                        },
                        'TextTransformations': [
                            {
                                'Priority': 123,
                                'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                            },
                        ]
                    },
                    'RateBasedStatement': {
                        'Limit': 123,
                        'AggregateKeyType': 'IP',
                        'ScopeDownStatement': {'... recursive ...'}
                    },
                    'AndStatement': {
                        'Statements': [
                            {'... recursive ...'},
                        ]
                    },
                    'OrStatement': {
                        'Statements': [
                            {'... recursive ...'},
                        ]
                    },
                    'NotStatement': {
                        'Statement': {'... recursive ...'}
                    },
                    'ManagedRuleGroupStatement': {
                        'VendorName': 'string',
                        'Name': 'string',
                        'ExcludedRules': [
                            {
                                'Name': 'string'
                            },
                        ]
                    }
                },
                'Action': {
                    'Block': {}
                    ,
                    'Allow': {}
                    ,
                    'Count': {}
    
                },
                'OverrideAction': {
                    'Count': {}
                    ,
                    'None': {}
    
                },
                'VisibilityConfig': {
                    'SampledRequestsEnabled': True|False,
                    'CloudWatchMetricsEnabled': True|False,
                    'MetricName': 'string'
                }
            },
        ],
        VisibilityConfig={
            'SampledRequestsEnabled': True|False,
            'CloudWatchMetricsEnabled': True|False,
            'MetricName': 'string'
        },
        LockToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the Web ACL. You cannot change the name of a Web ACL after you create it.\n

    :type Scope: string
    :param Scope: [REQUIRED]\nSpecifies whether this is for an AWS CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB) or an API Gateway stage.\nTo work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:\n\nCLI - Specify the Region when you use the CloudFront scope: --scope=CLOUDFRONT --region=us-east-1 .\nAPI and SDKs - For all calls, use the Region endpoint us-east-1.\n\n

    :type Id: string
    :param Id: [REQUIRED]\nThe unique identifier for the Web ACL. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.\n

    :type DefaultAction: dict
    :param DefaultAction: [REQUIRED]\nThe action to perform if none of the Rules contained in the WebACL match.\n\nBlock (dict) --Specifies that AWS WAF should block requests by default.\n\nAllow (dict) --Specifies that AWS WAF should allow requests by default.\n\n\n

    :type Description: string
    :param Description: A description of the Web ACL that helps with identification. You cannot change the description of a Web ACL after you create it.

    :type Rules: list
    :param Rules: The Rule statements used to identify the web requests that you want to allow, block, or count. Each rule includes one top-level statement that AWS WAF uses to identify matching web requests, and parameters that govern how AWS WAF handles them.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nA single rule, which you can use in a WebACL or RuleGroup to identify web requests that you want to allow, block, or count. Each rule includes one top-level Statement that AWS WAF uses to identify matching web requests, and parameters that govern how AWS WAF handles them.\n\nName (string) -- [REQUIRED]The name of the rule. You can\'t change the name of a Rule after you create it.\n\nPriority (integer) -- [REQUIRED]If you define more than one Rule in a WebACL , AWS WAF evaluates each request against the Rules in order based on the value of Priority . AWS WAF processes rules with lower priority first. The priorities don\'t need to be consecutive, but they must all be different.\n\nStatement (dict) -- [REQUIRED]The AWS WAF processing statement for the rule, for example ByteMatchStatement or SizeConstraintStatement .\n\nByteMatchStatement (dict) --A rule statement that defines a string match search for AWS WAF to apply to web requests. The byte match statement provides the bytes to search for, the location in requests that you want AWS WAF to search, and other settings. The bytes to search for are typically a string that corresponds with ASCII characters. In the AWS WAF console and the developer guide, this is refered to as a string match statement.\n\nSearchString (bytes) -- [REQUIRED]A string value that you want AWS WAF to search for. AWS WAF searches only in the part of web requests that you designate for inspection in FieldToMatch . The maximum length of the value is 50 bytes.\nValid values depend on the component that you specify for inspection in FieldToMatch :\n\nMethod : The HTTP method that you want AWS WAF to search for. This indicates the type of operation specified in the request.\nUriPath : The value that you want AWS WAF to search for in the URI path, for example, /images/daily-ad.jpg .\n\nIf SearchString includes alphabetic characters A-Z and a-z, note that the value is case sensitive.\n\nIf you\'re using the AWS WAF API\nSpecify a base64-encoded version of the value. The maximum length of the value before you base64-encode it is 50 bytes.\nFor example, suppose the value of Type is HEADER and the value of Data is User-Agent . If you want to search the User-Agent header for the value BadBot , you base64-encode BadBot using MIME base64-encoding and include the resulting value, QmFkQm90 , in the value of SearchString .\n\nIf you\'re using the AWS CLI or one of the AWS SDKs\nThe value that you want AWS WAF to search for. The SDK automatically base64 encodes the value.\n\nFieldToMatch (dict) -- [REQUIRED]The part of a web request that you want AWS WAF to inspect. For more information, see FieldToMatch .\n\nSingleHeader (dict) --Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.\n\nName (string) -- [REQUIRED]The name of the query header to inspect.\n\n\n\nSingleQueryArgument (dict) --Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.\nThis is used only to indicate the web request component for AWS WAF to inspect, in the FieldToMatch specification.\n\nName (string) -- [REQUIRED]The name of the query argument to inspect.\n\n\n\nAllQueryArguments (dict) --Inspect all query arguments.\n\nUriPath (dict) --Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .\n\nQueryString (dict) --Inspect the query string. This is the part of a URL that appears after a ? character, if any.\n\nBody (dict) --Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.\nNote that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as ByteMatchStatement or RegexPatternSetReferenceStatement , with a SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.\n\nMethod (dict) --Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.\n\n\n\nTextTransformations (list) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nText transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.\n\nPriority (integer) -- [REQUIRED]Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.\n\nType (string) -- [REQUIRED]You can specify the following transformation types:\n\nCMD_LINE\nWhen you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:\n\nDelete the following characters: ' \' ^\nDelete spaces before the following characters: / (\nReplace the following characters with a space: , ;\nReplace multiple spaces with one space\nConvert uppercase letters (A-Z) to lowercase (a-z)\n\n\nCOMPRESS_WHITE_SPACE\nUse this option to replace the following characters with a space character (decimal 32):\n\nf, formfeed, decimal 12\nt, tab, decimal 9\nn, newline, decimal 10\nr, carriage return, decimal 13\nv, vertical tab, decimal 11\nnon-breaking space, decimal 160\n\n\nCOMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE\n\nUse this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:\n\nReplaces (ampersand)quot; with '\nReplaces (ampersand)nbsp; with a non-breaking space, decimal 160\nReplaces (ampersand)lt; with a 'less than' symbol\nReplaces (ampersand)gt; with >\nReplaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters\nReplaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters\n\n\nLOWERCASE\nUse this option to convert uppercase letters (A-Z) to lowercase (a-z).\n\nURL_DECODE\nUse this option to decode a URL-encoded value.\n\nNONE\nSpecify NONE if you don\'t want any text transformations.\n\n\n\n\n\nPositionalConstraint (string) -- [REQUIRED]The area within the portion of a web request that you want AWS WAF to search for SearchString . Valid values include the following:\n\nCONTAINS\nThe specified part of the web request must include the value of SearchString , but the location doesn\'t matter.\n\nCONTAINS_WORD\nThe specified part of the web request must include the value of SearchString , and SearchString must contain only alphanumeric characters or underscore (A-Z, a-z, 0-9, or _). In addition, SearchString must be a word, which means that both of the following are true:\n\nSearchString is at the beginning of the specified part of the web request or is preceded by a character other than an alphanumeric character or underscore (_). Examples include the value of a header and ;BadBot .\nSearchString is at the end of the specified part of the web request or is followed by a character other than an alphanumeric character or underscore (_), for example, BadBot; and -BadBot; .\n\n\nEXACTLY\nThe value of the specified part of the web request must exactly match the value of SearchString .\n\nSTARTS_WITH\nThe value of SearchString must appear at the beginning of the specified part of the web request.\n\nENDS_WITH\nThe value of SearchString must appear at the end of the specified part of the web request.\n\n\n\nSqliMatchStatement (dict) --Attackers sometimes insert malicious SQL code into web requests in an effort to extract data from your database. To allow or block web requests that appear to contain malicious SQL code, create one or more SQL injection match conditions. An SQL injection match condition identifies the part of web requests, such as the URI or the query string, that you want AWS WAF to inspect. Later in the process, when you create a web ACL, you specify whether to allow or block requests that appear to contain malicious SQL code.\n\nFieldToMatch (dict) -- [REQUIRED]The part of a web request that you want AWS WAF to inspect. For more information, see FieldToMatch .\n\nSingleHeader (dict) --Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.\n\nName (string) -- [REQUIRED]The name of the query header to inspect.\n\n\n\nSingleQueryArgument (dict) --Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.\nThis is used only to indicate the web request component for AWS WAF to inspect, in the FieldToMatch specification.\n\nName (string) -- [REQUIRED]The name of the query argument to inspect.\n\n\n\nAllQueryArguments (dict) --Inspect all query arguments.\n\nUriPath (dict) --Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .\n\nQueryString (dict) --Inspect the query string. This is the part of a URL that appears after a ? character, if any.\n\nBody (dict) --Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.\nNote that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as ByteMatchStatement or RegexPatternSetReferenceStatement , with a SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.\n\nMethod (dict) --Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.\n\n\n\nTextTransformations (list) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nText transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.\n\nPriority (integer) -- [REQUIRED]Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.\n\nType (string) -- [REQUIRED]You can specify the following transformation types:\n\nCMD_LINE\nWhen you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:\n\nDelete the following characters: ' \' ^\nDelete spaces before the following characters: / (\nReplace the following characters with a space: , ;\nReplace multiple spaces with one space\nConvert uppercase letters (A-Z) to lowercase (a-z)\n\n\nCOMPRESS_WHITE_SPACE\nUse this option to replace the following characters with a space character (decimal 32):\n\nf, formfeed, decimal 12\nt, tab, decimal 9\nn, newline, decimal 10\nr, carriage return, decimal 13\nv, vertical tab, decimal 11\nnon-breaking space, decimal 160\n\n\nCOMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE\n\nUse this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:\n\nReplaces (ampersand)quot; with '\nReplaces (ampersand)nbsp; with a non-breaking space, decimal 160\nReplaces (ampersand)lt; with a 'less than' symbol\nReplaces (ampersand)gt; with >\nReplaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters\nReplaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters\n\n\nLOWERCASE\nUse this option to convert uppercase letters (A-Z) to lowercase (a-z).\n\nURL_DECODE\nUse this option to decode a URL-encoded value.\n\nNONE\nSpecify NONE if you don\'t want any text transformations.\n\n\n\n\n\n\n\nXssMatchStatement (dict) --A rule statement that defines a cross-site scripting (XSS) match search for AWS WAF to apply to web requests. XSS attacks are those where the attacker uses vulnerabilities in a benign website as a vehicle to inject malicious client-site scripts into other legitimate web browsers. The XSS match statement provides the location in requests that you want AWS WAF to search and text transformations to use on the search area before AWS WAF searches for character sequences that are likely to be malicious strings.\n\nFieldToMatch (dict) -- [REQUIRED]The part of a web request that you want AWS WAF to inspect. For more information, see FieldToMatch .\n\nSingleHeader (dict) --Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.\n\nName (string) -- [REQUIRED]The name of the query header to inspect.\n\n\n\nSingleQueryArgument (dict) --Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.\nThis is used only to indicate the web request component for AWS WAF to inspect, in the FieldToMatch specification.\n\nName (string) -- [REQUIRED]The name of the query argument to inspect.\n\n\n\nAllQueryArguments (dict) --Inspect all query arguments.\n\nUriPath (dict) --Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .\n\nQueryString (dict) --Inspect the query string. This is the part of a URL that appears after a ? character, if any.\n\nBody (dict) --Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.\nNote that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as ByteMatchStatement or RegexPatternSetReferenceStatement , with a SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.\n\nMethod (dict) --Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.\n\n\n\nTextTransformations (list) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nText transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.\n\nPriority (integer) -- [REQUIRED]Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.\n\nType (string) -- [REQUIRED]You can specify the following transformation types:\n\nCMD_LINE\nWhen you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:\n\nDelete the following characters: ' \' ^\nDelete spaces before the following characters: / (\nReplace the following characters with a space: , ;\nReplace multiple spaces with one space\nConvert uppercase letters (A-Z) to lowercase (a-z)\n\n\nCOMPRESS_WHITE_SPACE\nUse this option to replace the following characters with a space character (decimal 32):\n\nf, formfeed, decimal 12\nt, tab, decimal 9\nn, newline, decimal 10\nr, carriage return, decimal 13\nv, vertical tab, decimal 11\nnon-breaking space, decimal 160\n\n\nCOMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE\n\nUse this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:\n\nReplaces (ampersand)quot; with '\nReplaces (ampersand)nbsp; with a non-breaking space, decimal 160\nReplaces (ampersand)lt; with a 'less than' symbol\nReplaces (ampersand)gt; with >\nReplaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters\nReplaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters\n\n\nLOWERCASE\nUse this option to convert uppercase letters (A-Z) to lowercase (a-z).\n\nURL_DECODE\nUse this option to decode a URL-encoded value.\n\nNONE\nSpecify NONE if you don\'t want any text transformations.\n\n\n\n\n\n\n\nSizeConstraintStatement (dict) --A rule statement that compares a number of bytes against the size of a request component, using a comparison operator, such as greater than (>) or less than (<). For example, you can use a size constraint statement to look for query strings that are longer than 100 bytes.\nIf you configure AWS WAF to inspect the request body, AWS WAF inspects only the first 8192 bytes (8 KB). If the request body for your web requests never exceeds 8192 bytes, you can create a size constraint condition and block requests that have a request body greater than 8192 bytes.\nIf you choose URI for the value of Part of the request to filter on, the slash (/) in the URI counts as one character. For example, the URI /logo.jpg is nine characters long.\n\nFieldToMatch (dict) -- [REQUIRED]The part of a web request that you want AWS WAF to inspect. For more information, see FieldToMatch .\n\nSingleHeader (dict) --Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.\n\nName (string) -- [REQUIRED]The name of the query header to inspect.\n\n\n\nSingleQueryArgument (dict) --Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.\nThis is used only to indicate the web request component for AWS WAF to inspect, in the FieldToMatch specification.\n\nName (string) -- [REQUIRED]The name of the query argument to inspect.\n\n\n\nAllQueryArguments (dict) --Inspect all query arguments.\n\nUriPath (dict) --Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .\n\nQueryString (dict) --Inspect the query string. This is the part of a URL that appears after a ? character, if any.\n\nBody (dict) --Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.\nNote that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as ByteMatchStatement or RegexPatternSetReferenceStatement , with a SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.\n\nMethod (dict) --Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.\n\n\n\nComparisonOperator (string) -- [REQUIRED]The operator to use to compare the request part to the size setting.\n\nSize (integer) -- [REQUIRED]The size, in byte, to compare to the request part, after any transformations.\n\nTextTransformations (list) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nText transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.\n\nPriority (integer) -- [REQUIRED]Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.\n\nType (string) -- [REQUIRED]You can specify the following transformation types:\n\nCMD_LINE\nWhen you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:\n\nDelete the following characters: ' \' ^\nDelete spaces before the following characters: / (\nReplace the following characters with a space: , ;\nReplace multiple spaces with one space\nConvert uppercase letters (A-Z) to lowercase (a-z)\n\n\nCOMPRESS_WHITE_SPACE\nUse this option to replace the following characters with a space character (decimal 32):\n\nf, formfeed, decimal 12\nt, tab, decimal 9\nn, newline, decimal 10\nr, carriage return, decimal 13\nv, vertical tab, decimal 11\nnon-breaking space, decimal 160\n\n\nCOMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE\n\nUse this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:\n\nReplaces (ampersand)quot; with '\nReplaces (ampersand)nbsp; with a non-breaking space, decimal 160\nReplaces (ampersand)lt; with a 'less than' symbol\nReplaces (ampersand)gt; with >\nReplaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters\nReplaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters\n\n\nLOWERCASE\nUse this option to convert uppercase letters (A-Z) to lowercase (a-z).\n\nURL_DECODE\nUse this option to decode a URL-encoded value.\n\nNONE\nSpecify NONE if you don\'t want any text transformations.\n\n\n\n\n\n\n\nGeoMatchStatement (dict) --A rule statement used to identify web requests based on country of origin.\n\nCountryCodes (list) --An array of two-character country codes, for example, [ 'US', 'CN' ] , from the alpha-2 country ISO codes of the ISO 3166 international standard.\n\n(string) --\n\n\n\n\nRuleGroupReferenceStatement (dict) --A rule statement used to run the rules that are defined in a RuleGroup . To use this, create a rule group with your rules, then provide the ARN of the rule group in this statement.\nYou cannot nest a RuleGroupReferenceStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.\n\nARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the entity.\n\nExcludedRules (list) --The names of rules that are in the referenced rule group, but that you want AWS WAF to exclude from processing for this rule statement.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nSpecifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.\n\nName (string) -- [REQUIRED]The name of the rule to exclude.\n\n\n\n\n\n\n\nIPSetReferenceStatement (dict) --A rule statement used to detect web requests coming from particular IP addresses or address ranges. To use this, create an IPSet that specifies the addresses you want to detect, then use the ARN of that set in this statement. To create an IP set, see CreateIPSet .\nEach IP set rule statement references an IP set. You create and maintain the set independent of your rules. This allows you to use the single set in multiple rules. When you update the referenced set, AWS WAF automatically updates all rules that reference it.\n\nARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the IPSet that this statement references.\n\n\n\nRegexPatternSetReferenceStatement (dict) --A rule statement used to search web request components for matches with regular expressions. To use this, create a RegexPatternSet that specifies the expressions that you want to detect, then use the ARN of that set in this statement. A web request matches the pattern set rule statement if the request component matches any of the patterns in the set. To create a regex pattern set, see CreateRegexPatternSet .\nEach regex pattern set rule statement references a regex pattern set. You create and maintain the set independent of your rules. This allows you to use the single set in multiple rules. When you update the referenced set, AWS WAF automatically updates all rules that reference it.\n\nARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the RegexPatternSet that this statement references.\n\nFieldToMatch (dict) -- [REQUIRED]The part of a web request that you want AWS WAF to inspect. For more information, see FieldToMatch .\n\nSingleHeader (dict) --Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isn\'t case sensitive.\n\nName (string) -- [REQUIRED]The name of the query header to inspect.\n\n\n\nSingleQueryArgument (dict) --Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isn\'t case sensitive.\nThis is used only to indicate the web request component for AWS WAF to inspect, in the FieldToMatch specification.\n\nName (string) -- [REQUIRED]The name of the query argument to inspect.\n\n\n\nAllQueryArguments (dict) --Inspect all query arguments.\n\nUriPath (dict) --Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .\n\nQueryString (dict) --Inspect the query string. This is the part of a URL that appears after a ? character, if any.\n\nBody (dict) --Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.\nNote that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you don\'t need to inspect more than 8 KB, you can guarantee that you don\'t allow additional bytes in by combining a statement that inspects the body of the web request, such as ByteMatchStatement or RegexPatternSetReferenceStatement , with a SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesn\'t support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.\n\nMethod (dict) --Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.\n\n\n\nTextTransformations (list) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nText transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.\n\nPriority (integer) -- [REQUIRED]Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don\'t need to be consecutive, but they must all be different.\n\nType (string) -- [REQUIRED]You can specify the following transformation types:\n\nCMD_LINE\nWhen you\'re concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:\n\nDelete the following characters: ' \' ^\nDelete spaces before the following characters: / (\nReplace the following characters with a space: , ;\nReplace multiple spaces with one space\nConvert uppercase letters (A-Z) to lowercase (a-z)\n\n\nCOMPRESS_WHITE_SPACE\nUse this option to replace the following characters with a space character (decimal 32):\n\nf, formfeed, decimal 12\nt, tab, decimal 9\nn, newline, decimal 10\nr, carriage return, decimal 13\nv, vertical tab, decimal 11\nnon-breaking space, decimal 160\n\n\nCOMPRESS_WHITE_SPACE also replaces multiple spaces with one space.HTML_ENTITY_DECODE\n\nUse this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:\n\nReplaces (ampersand)quot; with '\nReplaces (ampersand)nbsp; with a non-breaking space, decimal 160\nReplaces (ampersand)lt; with a 'less than' symbol\nReplaces (ampersand)gt; with >\nReplaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters\nReplaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters\n\n\nLOWERCASE\nUse this option to convert uppercase letters (A-Z) to lowercase (a-z).\n\nURL_DECODE\nUse this option to decode a URL-encoded value.\n\nNONE\nSpecify NONE if you don\'t want any text transformations.\n\n\n\n\n\n\n\nRateBasedStatement (dict) --A rate-based rule tracks the rate of requests for each originating IP address, and triggers the rule action when the rate exceeds a limit that you specify on the number of requests in any 5-minute time span. You can use this to put a temporary block on requests from an IP address that is sending excessive requests.\nWhen the rule action triggers, AWS WAF blocks additional requests from the IP address until the request rate falls below the limit.\nYou can optionally nest another statement inside the rate-based statement, to narrow the scope of the rule so that it only counts requests that match the nested statement. For example, based on recent requests that you have seen from an attacker, you might create a rate-based rule with a nested AND rule statement that contains the following nested statements:\n\nAn IP match statement with an IP set that specified the address 192.0.2.44.\nA string match statement that searches in the User-Agent header for the string BadBot.\n\nIn this rate-based rule, you also define a rate limit. For this example, the rate limit is 1,000. Requests that meet both of the conditions in the statements are counted. If the count exceeds 1,000 requests per five minutes, the rule action triggers. Requests that do not meet both conditions are not counted towards the rate limit and are not affected by this rule.\nYou cannot nest a RateBasedStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.\n\nLimit (integer) -- [REQUIRED]The limit on requests per 5-minute period for a single originating IP address. If the statement includes a ScopDownStatement , this limit is applied only to the requests that match the statement.\n\nAggregateKeyType (string) -- [REQUIRED]Setting that indicates how to aggregate the request counts. Currently, you must set this to IP . The request counts are aggregated on IP addresses.\n\nScopeDownStatement (dict) --An optional nested statement that narrows the scope of the rate-based statement to matching web requests. This can be any nestable statement, and you can nest statements at any level below this scope-down statement.\n\n\n\nAndStatement (dict) --A logical rule statement used to combine other rule statements with AND logic. You provide more than one Statement within the AndStatement .\n\nStatements (list) -- [REQUIRED]The statements to combine with AND logic. You can use any statements that can be nested.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nThe processing guidance for a Rule , used by AWS WAF to determine whether a web request matches the rule.\n\n\n\n\n\nOrStatement (dict) --A logical rule statement used to combine other rule statements with OR logic. You provide more than one Statement within the OrStatement .\n\nStatements (list) -- [REQUIRED]The statements to combine with OR logic. You can use any statements that can be nested.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nThe processing guidance for a Rule , used by AWS WAF to determine whether a web request matches the rule.\n\n\n\n\n\nNotStatement (dict) --A logical rule statement used to negate the results of another rule statement. You provide one Statement within the NotStatement .\n\nStatement (dict) --The statement to negate. You can use any statement that can be nested.\n\n\n\nManagedRuleGroupStatement (dict) --A rule statement used to run the rules that are defined in a managed rule group. To use this, provide the vendor name and the name of the rule group in this statement. You can retrieve the required names by calling ListAvailableManagedRuleGroups .\nYou can\'t nest a ManagedRuleGroupStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.\n\nVendorName (string) -- [REQUIRED]The name of the managed rule group vendor. You use this, along with the rule group name, to identify the rule group.\n\nName (string) -- [REQUIRED]The name of the managed rule group. You use this, along with the vendor name, to identify the rule group.\n\nExcludedRules (list) --The rules whose actions are set to COUNT by the web ACL, regardless of the action that is set on the rule. This effectively excludes the rule from acting on web requests.\n\n(dict) --\nNote\nThis is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .\n\nSpecifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.\n\nName (string) -- [REQUIRED]The name of the rule to exclude.\n\n\n\n\n\n\n\n\n\nAction (dict) --The action that AWS WAF should take on a web request when it matches the rule statement. Settings at the web ACL level can override the rule action setting.\nThis is used only for rules whose statements do not reference a rule group. Rule statements that reference a rule group include RuleGroupReferenceStatement and ManagedRuleGroupStatement .\nYou must specify either this Action setting or the rule OverrideAction setting, but not both:\n\nIf the rule statement does not reference a rule group, use this rule action setting and not the rule override action setting.\nIf the rule statement references a rule group, use the override action setting and not this action setting.\n\n\nBlock (dict) --Instructs AWS WAF to block the web request.\n\nAllow (dict) --Instructs AWS WAF to allow the web request.\n\nCount (dict) --Instructs AWS WAF to count the web request and allow it.\n\n\n\nOverrideAction (dict) --The override action to apply to the rules in a rule group. Used only for rule statements that reference a rule group, like RuleGroupReferenceStatement and ManagedRuleGroupStatement .\nSet the override action to none to leave the rule actions in effect. Set it to count to only count matches, regardless of the rule action settings.\nIn a Rule , you must specify either this OverrideAction setting or the rule Action setting, but not both:\n\nIf the rule statement references a rule group, use this override action setting and not the action setting.\nIf the rule statement does not reference a rule group, use the rule action setting and not this rule override action setting.\n\n\nCount (dict) --Override the rule action setting to count.\n\nNone (dict) --Don\'t override the rule action setting.\n\n\n\nVisibilityConfig (dict) -- [REQUIRED]Defines and enables Amazon CloudWatch metrics and web request sample collection.\n\nSampledRequestsEnabled (boolean) -- [REQUIRED]A boolean indicating whether AWS WAF should store a sampling of the web requests that match the rules. You can view the sampled requests through the AWS WAF console.\n\nCloudWatchMetricsEnabled (boolean) -- [REQUIRED]A boolean indicating whether the associated resource sends metrics to CloudWatch. For the list of available metrics, see AWS WAF Metrics .\n\nMetricName (string) -- [REQUIRED]A name of the CloudWatch metric. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with length from one to 128 characters. It can\'t contain whitespace or metric names reserved for AWS WAF, for example 'All' and 'Default_Action.' You can\'t change a MetricName after you create a VisibilityConfig .\n\n\n\n\n\n\n

    :type VisibilityConfig: dict
    :param VisibilityConfig: [REQUIRED]\nDefines and enables Amazon CloudWatch metrics and web request sample collection.\n\nSampledRequestsEnabled (boolean) -- [REQUIRED]A boolean indicating whether AWS WAF should store a sampling of the web requests that match the rules. You can view the sampled requests through the AWS WAF console.\n\nCloudWatchMetricsEnabled (boolean) -- [REQUIRED]A boolean indicating whether the associated resource sends metrics to CloudWatch. For the list of available metrics, see AWS WAF Metrics .\n\nMetricName (string) -- [REQUIRED]A name of the CloudWatch metric. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with length from one to 128 characters. It can\'t contain whitespace or metric names reserved for AWS WAF, for example 'All' and 'Default_Action.' You can\'t change a MetricName after you create a VisibilityConfig .\n\n\n

    :type LockToken: string
    :param LockToken: [REQUIRED]\nA token used for optimistic locking. AWS WAF returns a token to your get and list requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like update and delete. AWS WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a WAFOptimisticLockException . If this happens, perform another get, and use the new token returned by that operation.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'NextLockToken': 'string'
}


Response Structure

(dict) --

NextLockToken (string) --
A token used for optimistic locking. AWS WAF returns this token to your update requests. You use NextLockToken in the same manner as you use LockToken .







Exceptions

WAFV2.Client.exceptions.WAFInternalErrorException
WAFV2.Client.exceptions.WAFInvalidParameterException
WAFV2.Client.exceptions.WAFNonexistentItemException
WAFV2.Client.exceptions.WAFDuplicateItemException
WAFV2.Client.exceptions.WAFOptimisticLockException
WAFV2.Client.exceptions.WAFLimitsExceededException
WAFV2.Client.exceptions.WAFInvalidResourceException
WAFV2.Client.exceptions.WAFUnavailableEntityException
WAFV2.Client.exceptions.WAFSubscriptionNotFoundException
WAFV2.Client.exceptions.WAFInvalidOperationException


    :return: {
        'NextLockToken': 'string'
    }
    
    
    :returns: 
    WAFV2.Client.exceptions.WAFInternalErrorException
    WAFV2.Client.exceptions.WAFInvalidParameterException
    WAFV2.Client.exceptions.WAFNonexistentItemException
    WAFV2.Client.exceptions.WAFDuplicateItemException
    WAFV2.Client.exceptions.WAFOptimisticLockException
    WAFV2.Client.exceptions.WAFLimitsExceededException
    WAFV2.Client.exceptions.WAFInvalidResourceException
    WAFV2.Client.exceptions.WAFUnavailableEntityException
    WAFV2.Client.exceptions.WAFSubscriptionNotFoundException
    WAFV2.Client.exceptions.WAFInvalidOperationException
    
    """
    pass

