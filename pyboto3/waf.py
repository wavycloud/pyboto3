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

def create_byte_match_set(Name=None, ChangeToken=None):
    """
    Creates a ByteMatchSet . You then use  UpdateByteMatchSet to identify the part of a web request that you want AWS WAF to inspect, such as the values of the User-Agent header or the query string. For example, you can create a ByteMatchSet that matches any requests with User-Agent headers that contain the string BadBot . You can then configure AWS WAF to reject those requests.
    To create and configure a ByteMatchSet , perform the following steps:
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_byte_match_set(
        Name='string',
        ChangeToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            A friendly name or description of the ByteMatchSet . You can't change Name after you create a ByteMatchSet .
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :rtype: dict
    :return: {
        'ByteMatchSet': {
            'ByteMatchSetId': 'string',
            'Name': 'string',
            'ByteMatchTuples': [
                {
                    'FieldToMatch': {
                        'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY',
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
    A friendly name or description of the  ByteMatchSet . You can't change Name after you create a ByteMatchSet .
    
    ChangeToken (string) -- [REQUIRED]
    The value returned by the most recent call to  GetChangeToken .
    
    
    """
    pass

def create_geo_match_set(Name=None, ChangeToken=None):
    """
    Creates an  GeoMatchSet , which you use to specify which web requests you want to allow or block based on the country that the requests originate from. For example, if you're receiving a lot of requests from one or more countries and you want to block the requests, you can create an GeoMatchSet that contains those countries and then configure AWS WAF to block the requests.
    To create and configure a GeoMatchSet , perform the following steps:
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_geo_match_set(
        Name='string',
        ChangeToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            A friendly name or description of the GeoMatchSet . You can't change Name after you create the GeoMatchSet .
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :rtype: dict
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
    A friendly name or description of the  GeoMatchSet . You can't change Name after you create the GeoMatchSet .
    
    ChangeToken (string) -- [REQUIRED]
    The value returned by the most recent call to  GetChangeToken .
    
    
    """
    pass

def create_ip_set(Name=None, ChangeToken=None):
    """
    Creates an  IPSet , which you use to specify which web requests you want to allow or block based on the IP addresses that the requests originate from. For example, if you're receiving a lot of requests from one or more individual IP addresses or one or more ranges of IP addresses and you want to block the requests, you can create an IPSet that contains those IP addresses and then configure AWS WAF to block the requests.
    To create and configure an IPSet , perform the following steps:
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    Examples
    The following example creates an IP match set named MyIPSetFriendlyName.
    Expected Output:
    
    :example: response = client.create_ip_set(
        Name='string',
        ChangeToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            A friendly name or description of the IPSet . You can't change Name after you create the IPSet .
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :rtype: dict
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
    A friendly name or description of the  IPSet . You can't change Name after you create the IPSet .
    
    ChangeToken (string) -- [REQUIRED]
    The value returned by the most recent call to  GetChangeToken .
    
    
    """
    pass

def create_rate_based_rule(Name=None, MetricName=None, RateKey=None, RateLimit=None, ChangeToken=None):
    """
    Creates a  RateBasedRule . The RateBasedRule contains a RateLimit , which specifies the maximum number of requests that AWS WAF allows from a specified IP address in a five-minute period. The RateBasedRule also contains the IPSet objects, ByteMatchSet objects, and other predicates that identify the requests that you want to count or block if these requests exceed the RateLimit .
    If you add more than one predicate to a RateBasedRule , a request not only must exceed the RateLimit , but it also must match all the specifications to be counted or blocked. For example, suppose you add the following to a RateBasedRule :
    Further, you specify a RateLimit of 15,000.
    You then add the RateBasedRule to a WebACL and specify that you want to block requests that meet the conditions in the rule. For a request to be blocked, it must come from the IP address 192.0.2.44 and the User-Agent header in the request must contain the value BadBot . Further, requests that match these two conditions must be received at a rate of more than 15,000 requests every five minutes. If both conditions are met and the rate is exceeded, AWS WAF blocks the requests. If the rate drops below 15,000 for a five-minute period, AWS WAF no longer blocks the requests.
    As a second example, suppose you want to limit requests to a particular page on your site. To do this, you could add the following to a RateBasedRule :
    Further, you specify a RateLimit of 15,000.
    By adding this RateBasedRule to a WebACL , you could limit requests to your login page without affecting the rest of your site.
    To create and configure a RateBasedRule , perform the following steps:
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_rate_based_rule(
        Name='string',
        MetricName='string',
        RateKey='IP',
        RateLimit=123,
        ChangeToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            A friendly name or description of the RateBasedRule . You can't change the name of a RateBasedRule after you create it.
            

    :type MetricName: string
    :param MetricName: [REQUIRED]
            A friendly name or description for the metrics for this RateBasedRule . The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace. You can't change the name of the metric after you create the RateBasedRule .
            

    :type RateKey: string
    :param RateKey: [REQUIRED]
            The field that AWS WAF uses to determine if requests are likely arriving from a single source and thus subject to rate monitoring. The only valid value for RateKey is IP . IP indicates that requests that arrive from the same IP address are subject to the RateLimit that is specified in the RateBasedRule .
            

    :type RateLimit: integer
    :param RateLimit: [REQUIRED]
            The maximum number of requests, which have an identical value in the field that is specified by RateKey , allowed in a five-minute period. If the number of requests exceeds the RateLimit and the other predicates specified in the rule are also met, AWS WAF triggers the action that is specified for this rule.
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The ChangeToken that you used to submit the CreateRateBasedRule request. You can also use this value to query the status of the request. For more information, see GetChangeTokenStatus .
            

    :rtype: dict
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
    
    
    :example: response = client.create_regex_match_set(
        Name='string',
        ChangeToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            A friendly name or description of the RegexMatchSet . You can't change Name after you create a RegexMatchSet .
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :rtype: dict
    :return: {
        'RegexMatchSet': {
            'RegexMatchSetId': 'string',
            'Name': 'string',
            'RegexMatchTuples': [
                {
                    'FieldToMatch': {
                        'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY',
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
    A friendly name or description of the  RegexMatchSet . You can't change Name after you create a RegexMatchSet .
    
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
    
    
    :example: response = client.create_regex_pattern_set(
        Name='string',
        ChangeToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            A friendly name or description of the RegexPatternSet . You can't change Name after you create a RegexPatternSet .
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :rtype: dict
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
    A friendly name or description of the  RegexPatternSet . You can't change Name after you create a RegexPatternSet .
    
    ChangeToken (string) -- [REQUIRED]
    The value returned by the most recent call to  GetChangeToken .
    
    
    """
    pass

def create_rule(Name=None, MetricName=None, ChangeToken=None):
    """
    Creates a Rule , which contains the IPSet objects, ByteMatchSet objects, and other predicates that identify the requests that you want to block. If you add more than one predicate to a Rule , a request must match all of the specifications to be allowed or blocked. For example, suppose you add the following to a Rule :
    You then add the Rule to a WebACL and specify that you want to blocks requests that satisfy the Rule . For a request to be blocked, it must come from the IP address 192.0.2.44 and the User-Agent header in the request must contain the value BadBot .
    To create and configure a Rule , perform the following steps:
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    Examples
    The following example creates a rule named WAFByteHeaderRule.
    Expected Output:
    
    :example: response = client.create_rule(
        Name='string',
        MetricName='string',
        ChangeToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            A friendly name or description of the Rule . You can't change the name of a Rule after you create it.
            

    :type MetricName: string
    :param MetricName: [REQUIRED]
            A friendly name or description for the metrics for this Rule . The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace. You can't change the name of the metric after you create the Rule .
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :rtype: dict
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

def create_rule_group(Name=None, MetricName=None, ChangeToken=None):
    """
    Creates a RuleGroup . A rule group is a collection of predefined rules that you add to a web ACL. You use  UpdateRuleGroup to add rules to the rule group.
    Rule groups are subject to the following limits:
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_rule_group(
        Name='string',
        MetricName='string',
        ChangeToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            A friendly name or description of the RuleGroup . You can't change Name after you create a RuleGroup .
            

    :type MetricName: string
    :param MetricName: [REQUIRED]
            A friendly name or description for the metrics for this RuleGroup . The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace. You can't change the name of the metric after you create the RuleGroup .
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :rtype: dict
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
    A friendly name or description of the  RuleGroup . You can't change Name after you create a RuleGroup .
    
    MetricName (string) -- [REQUIRED]
    A friendly name or description for the metrics for this RuleGroup . The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace. You can't change the name of the metric after you create the RuleGroup .
    
    ChangeToken (string) -- [REQUIRED]
    The value returned by the most recent call to  GetChangeToken .
    
    
    """
    pass

def create_size_constraint_set(Name=None, ChangeToken=None):
    """
    Creates a SizeConstraintSet . You then use  UpdateSizeConstraintSet to identify the part of a web request that you want AWS WAF to check for length, such as the length of the User-Agent header or the length of the query string. For example, you can create a SizeConstraintSet that matches any requests that have a query string that is longer than 100 bytes. You can then configure AWS WAF to reject those requests.
    To create and configure a SizeConstraintSet , perform the following steps:
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    Examples
    The following example creates size constraint set named MySampleSizeConstraintSet.
    Expected Output:
    
    :example: response = client.create_size_constraint_set(
        Name='string',
        ChangeToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            A friendly name or description of the SizeConstraintSet . You can't change Name after you create a SizeConstraintSet .
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :rtype: dict
    :return: {
        'SizeConstraintSet': {
            'SizeConstraintSetId': 'string',
            'Name': 'string',
            'SizeConstraints': [
                {
                    'FieldToMatch': {
                        'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY',
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
    A friendly name or description of the  SizeConstraintSet . You can't change Name after you create a SizeConstraintSet .
    
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
    
    Examples
    The following example creates a SQL injection match set named MySQLInjectionMatchSet.
    Expected Output:
    
    :example: response = client.create_sql_injection_match_set(
        Name='string',
        ChangeToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            A friendly name or description for the SqlInjectionMatchSet that you're creating. You can't change Name after you create the SqlInjectionMatchSet .
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :rtype: dict
    :return: {
        'SqlInjectionMatchSet': {
            'SqlInjectionMatchSetId': 'string',
            'Name': 'string',
            'SqlInjectionMatchTuples': [
                {
                    'FieldToMatch': {
                        'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY',
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
    A friendly name or description for the  SqlInjectionMatchSet that you're creating. You can't change Name after you create the SqlInjectionMatchSet .
    
    ChangeToken (string) -- [REQUIRED]
    The value returned by the most recent call to  GetChangeToken .
    
    
    """
    pass

def create_web_acl(Name=None, MetricName=None, DefaultAction=None, ChangeToken=None):
    """
    Creates a WebACL , which contains the Rules that identify the CloudFront web requests that you want to allow, block, or count. AWS WAF evaluates Rules in order based on the value of Priority for each Rule .
    You also specify a default action, either ALLOW or BLOCK . If a web request doesn't match any of the Rules in a WebACL , AWS WAF responds to the request with the default action.
    To create and configure a WebACL , perform the following steps:
    For more information about how to use the AWS WAF API, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    Examples
    The following example creates a web ACL named CreateExample.
    Expected Output:
    
    :example: response = client.create_web_acl(
        Name='string',
        MetricName='string',
        DefaultAction={
            'Type': 'BLOCK'|'ALLOW'|'COUNT'
        },
        ChangeToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            A friendly name or description of the WebACL . You can't change Name after you create the WebACL .
            

    :type MetricName: string
    :param MetricName: [REQUIRED]
            A friendly name or description for the metrics for this WebACL . The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace. You can't change MetricName after you create the WebACL .
            

    :type DefaultAction: dict
    :param DefaultAction: [REQUIRED]
            The action that you want AWS WAF to take when a request doesn't match the criteria specified in any of the Rule objects that are associated with the WebACL .
            Type (string) -- [REQUIRED]Specifies how you want AWS WAF to respond to requests that match the settings in a Rule . Valid settings include the following:
            ALLOW : AWS WAF allows requests
            BLOCK : AWS WAF blocks requests
            COUNT : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can't specify COUNT for the default action for a WebACL .
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :rtype: dict
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
                    'Type': 'REGULAR'|'RATE_BASED'|'GROUP'
                },
            ]
        },
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    Name (string) -- [REQUIRED]
    A friendly name or description of the  WebACL . You can't change Name after you create the WebACL .
    
    MetricName (string) -- [REQUIRED]
    A friendly name or description for the metrics for this WebACL . The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace. You can't change MetricName after you create the WebACL .
    
    DefaultAction (dict) -- [REQUIRED]
    The action that you want AWS WAF to take when a request doesn't match the criteria specified in any of the Rule objects that are associated with the WebACL .
    
    Type (string) -- [REQUIRED]Specifies how you want AWS WAF to respond to requests that match the settings in a Rule . Valid settings include the following:
    
    ALLOW : AWS WAF allows requests
    BLOCK : AWS WAF blocks requests
    COUNT : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can't specify COUNT for the default action for a WebACL .
    
    
    
    
    ChangeToken (string) -- [REQUIRED]
    The value returned by the most recent call to  GetChangeToken .
    
    
    """
    pass

def create_xss_match_set(Name=None, ChangeToken=None):
    """
    Creates an  XssMatchSet , which you use to allow, block, or count requests that contain cross-site scripting attacks in the specified part of web requests. AWS WAF searches for character sequences that are likely to be malicious strings.
    To create and configure an XssMatchSet , perform the following steps:
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
    Examples
    The following example creates an XSS match set named MySampleXssMatchSet.
    Expected Output:
    
    :example: response = client.create_xss_match_set(
        Name='string',
        ChangeToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            A friendly name or description for the XssMatchSet that you're creating. You can't change Name after you create the XssMatchSet .
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :rtype: dict
    :return: {
        'XssMatchSet': {
            'XssMatchSetId': 'string',
            'Name': 'string',
            'XssMatchTuples': [
                {
                    'FieldToMatch': {
                        'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY',
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
    A friendly name or description for the  XssMatchSet that you're creating. You can't change Name after you create the XssMatchSet .
    
    ChangeToken (string) -- [REQUIRED]
    The value returned by the most recent call to  GetChangeToken .
    
    
    """
    pass

def delete_byte_match_set(ByteMatchSetId=None, ChangeToken=None):
    """
    Permanently deletes a  ByteMatchSet . You can't delete a ByteMatchSet if it's still used in any Rules or if it still includes any  ByteMatchTuple objects (any filters).
    If you just want to remove a ByteMatchSet from a Rule , use  UpdateRule .
    To permanently delete a ByteMatchSet , perform the following steps:
    See also: AWS API Documentation
    
    Examples
    The following example deletes a byte match set with the ID exampleIDs3t-46da-4fdb-b8d5-abc321j569j5.
    Expected Output:
    
    :example: response = client.delete_byte_match_set(
        ByteMatchSetId='string',
        ChangeToken='string'
    )
    
    
    :type ByteMatchSetId: string
    :param ByteMatchSetId: [REQUIRED]
            The ByteMatchSetId of the ByteMatchSet that you want to delete. ByteMatchSetId is returned by CreateByteMatchSet and by ListByteMatchSets .
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :rtype: dict
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
    Permanently deletes a  GeoMatchSet . You can't delete a GeoMatchSet if it's still used in any Rules or if it still includes any countries.
    If you just want to remove a GeoMatchSet from a Rule , use  UpdateRule .
    To permanently delete a GeoMatchSet from AWS WAF, perform the following steps:
    See also: AWS API Documentation
    
    
    :example: response = client.delete_geo_match_set(
        GeoMatchSetId='string',
        ChangeToken='string'
    )
    
    
    :type GeoMatchSetId: string
    :param GeoMatchSetId: [REQUIRED]
            The GeoMatchSetID of the GeoMatchSet that you want to delete. GeoMatchSetId is returned by CreateGeoMatchSet and by ListGeoMatchSets .
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :rtype: dict
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
    Permanently deletes an  IPSet . You can't delete an IPSet if it's still used in any Rules or if it still includes any IP addresses.
    If you just want to remove an IPSet from a Rule , use  UpdateRule .
    To permanently delete an IPSet from AWS WAF, perform the following steps:
    See also: AWS API Documentation
    
    Examples
    The following example deletes an IP match set  with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    Expected Output:
    
    :example: response = client.delete_ip_set(
        IPSetId='string',
        ChangeToken='string'
    )
    
    
    :type IPSetId: string
    :param IPSetId: [REQUIRED]
            The IPSetId of the IPSet that you want to delete. IPSetId is returned by CreateIPSet and by ListIPSets .
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :rtype: dict
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

def delete_permission_policy(ResourceArn=None):
    """
    Permanently deletes an IAM policy from the specified RuleGroup.
    The user making the request must be the owner of the RuleGroup.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_permission_policy(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the RuleGroup from which you want to delete the policy.
            The user making the request must be the owner of the RuleGroup.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_rate_based_rule(RuleId=None, ChangeToken=None):
    """
    Permanently deletes a  RateBasedRule . You can't delete a rule if it's still used in any WebACL objects or if it still includes any predicates, such as ByteMatchSet objects.
    If you just want to remove a rule from a WebACL , use  UpdateWebACL .
    To permanently delete a RateBasedRule from AWS WAF, perform the following steps:
    See also: AWS API Documentation
    
    
    :example: response = client.delete_rate_based_rule(
        RuleId='string',
        ChangeToken='string'
    )
    
    
    :type RuleId: string
    :param RuleId: [REQUIRED]
            The RuleId of the RateBasedRule that you want to delete. RuleId is returned by CreateRateBasedRule and by ListRateBasedRules .
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :rtype: dict
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
    Permanently deletes a  RegexMatchSet . You can't delete a RegexMatchSet if it's still used in any Rules or if it still includes any RegexMatchTuples objects (any filters).
    If you just want to remove a RegexMatchSet from a Rule , use  UpdateRule .
    To permanently delete a RegexMatchSet , perform the following steps:
    See also: AWS API Documentation
    
    
    :example: response = client.delete_regex_match_set(
        RegexMatchSetId='string',
        ChangeToken='string'
    )
    
    
    :type RegexMatchSetId: string
    :param RegexMatchSetId: [REQUIRED]
            The RegexMatchSetId of the RegexMatchSet that you want to delete. RegexMatchSetId is returned by CreateRegexMatchSet and by ListRegexMatchSets .
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :rtype: dict
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
    Permanently deletes a  RegexPatternSet . You can't delete a RegexPatternSet if it's still used in any RegexMatchSet or if the RegexPatternSet is not empty.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_regex_pattern_set(
        RegexPatternSetId='string',
        ChangeToken='string'
    )
    
    
    :type RegexPatternSetId: string
    :param RegexPatternSetId: [REQUIRED]
            The RegexPatternSetId of the RegexPatternSet that you want to delete. RegexPatternSetId is returned by CreateRegexPatternSet and by ListRegexPatternSets .
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :rtype: dict
    :return: {
        'ChangeToken': 'string'
    }
    
    
    """
    pass

def delete_rule(RuleId=None, ChangeToken=None):
    """
    Permanently deletes a  Rule . You can't delete a Rule if it's still used in any WebACL objects or if it still includes any predicates, such as ByteMatchSet objects.
    If you just want to remove a Rule from a WebACL , use  UpdateWebACL .
    To permanently delete a Rule from AWS WAF, perform the following steps:
    See also: AWS API Documentation
    
    Examples
    The following example deletes a rule with the ID WAFRule-1-Example.
    Expected Output:
    
    :example: response = client.delete_rule(
        RuleId='string',
        ChangeToken='string'
    )
    
    
    :type RuleId: string
    :param RuleId: [REQUIRED]
            The RuleId of the Rule that you want to delete. RuleId is returned by CreateRule and by ListRules .
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :rtype: dict
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
    Permanently deletes a  RuleGroup . You can't delete a RuleGroup if it's still used in any WebACL objects or if it still includes any rules.
    If you just want to remove a RuleGroup from a WebACL , use  UpdateWebACL .
    To permanently delete a RuleGroup from AWS WAF, perform the following steps:
    See also: AWS API Documentation
    
    
    :example: response = client.delete_rule_group(
        RuleGroupId='string',
        ChangeToken='string'
    )
    
    
    :type RuleGroupId: string
    :param RuleGroupId: [REQUIRED]
            The RuleGroupId of the RuleGroup that you want to delete. RuleGroupId is returned by CreateRuleGroup and by ListRuleGroups .
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :rtype: dict
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
    Permanently deletes a  SizeConstraintSet . You can't delete a SizeConstraintSet if it's still used in any Rules or if it still includes any  SizeConstraint objects (any filters).
    If you just want to remove a SizeConstraintSet from a Rule , use  UpdateRule .
    To permanently delete a SizeConstraintSet , perform the following steps:
    See also: AWS API Documentation
    
    Examples
    The following example deletes a size constraint set  with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    Expected Output:
    
    :example: response = client.delete_size_constraint_set(
        SizeConstraintSetId='string',
        ChangeToken='string'
    )
    
    
    :type SizeConstraintSetId: string
    :param SizeConstraintSetId: [REQUIRED]
            The SizeConstraintSetId of the SizeConstraintSet that you want to delete. SizeConstraintSetId is returned by CreateSizeConstraintSet and by ListSizeConstraintSets .
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :rtype: dict
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
    Permanently deletes a  SqlInjectionMatchSet . You can't delete a SqlInjectionMatchSet if it's still used in any Rules or if it still contains any  SqlInjectionMatchTuple objects.
    If you just want to remove a SqlInjectionMatchSet from a Rule , use  UpdateRule .
    To permanently delete a SqlInjectionMatchSet from AWS WAF, perform the following steps:
    See also: AWS API Documentation
    
    Examples
    The following example deletes a SQL injection match set  with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    Expected Output:
    
    :example: response = client.delete_sql_injection_match_set(
        SqlInjectionMatchSetId='string',
        ChangeToken='string'
    )
    
    
    :type SqlInjectionMatchSetId: string
    :param SqlInjectionMatchSetId: [REQUIRED]
            The SqlInjectionMatchSetId of the SqlInjectionMatchSet that you want to delete. SqlInjectionMatchSetId is returned by CreateSqlInjectionMatchSet and by ListSqlInjectionMatchSets .
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :rtype: dict
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
    Permanently deletes a  WebACL . You can't delete a WebACL if it still contains any Rules .
    To delete a WebACL , perform the following steps:
    See also: AWS API Documentation
    
    Examples
    The following example deletes a web ACL with the ID example-46da-4444-5555-example.
    Expected Output:
    
    :example: response = client.delete_web_acl(
        WebACLId='string',
        ChangeToken='string'
    )
    
    
    :type WebACLId: string
    :param WebACLId: [REQUIRED]
            The WebACLId of the WebACL that you want to delete. WebACLId is returned by CreateWebACL and by ListWebACLs .
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :rtype: dict
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
    Permanently deletes an  XssMatchSet . You can't delete an XssMatchSet if it's still used in any Rules or if it still contains any  XssMatchTuple objects.
    If you just want to remove an XssMatchSet from a Rule , use  UpdateRule .
    To permanently delete an XssMatchSet from AWS WAF, perform the following steps:
    See also: AWS API Documentation
    
    Examples
    The following example deletes an XSS match set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    Expected Output:
    
    :example: response = client.delete_xss_match_set(
        XssMatchSetId='string',
        ChangeToken='string'
    )
    
    
    :type XssMatchSetId: string
    :param XssMatchSetId: [REQUIRED]
            The XssMatchSetId of the XssMatchSet that you want to delete. XssMatchSetId is returned by CreateXssMatchSet and by ListXssMatchSets .
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :rtype: dict
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

def get_byte_match_set(ByteMatchSetId=None):
    """
    Returns the  ByteMatchSet specified by ByteMatchSetId .
    See also: AWS API Documentation
    
    Examples
    The following example returns the details of a byte match set with the ID exampleIDs3t-46da-4fdb-b8d5-abc321j569j5.
    Expected Output:
    
    :example: response = client.get_byte_match_set(
        ByteMatchSetId='string'
    )
    
    
    :type ByteMatchSetId: string
    :param ByteMatchSetId: [REQUIRED]
            The ByteMatchSetId of the ByteMatchSet that you want to get. ByteMatchSetId is returned by CreateByteMatchSet and by ListByteMatchSets .
            

    :rtype: dict
    :return: {
        'ByteMatchSet': {
            'ByteMatchSetId': 'string',
            'Name': 'string',
            'ByteMatchTuples': [
                {
                    'FieldToMatch': {
                        'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY',
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
    
    """
    pass

def get_change_token():
    """
    When you want to create, update, or delete AWS WAF objects, get a change token and include the change token in the create, update, or delete request. Change tokens ensure that your application doesn't submit conflicting requests to AWS WAF.
    Each create, update, or delete request must use a unique change token. If your application submits a GetChangeToken request and then submits a second GetChangeToken request before submitting a create, update, or delete request, the second GetChangeToken request returns the same value as the first GetChangeToken request.
    When you use a change token in a create, update, or delete request, the status of the change token changes to PENDING , which indicates that AWS WAF is propagating the change to all AWS WAF servers. Use GetChangeTokenStatus to determine the status of your change token.
    See also: AWS API Documentation
    
    Examples
    The following example returns a change token to use for a create, update or delete operation.
    Expected Output:
    
    :example: response = client.get_change_token()
    
    
    :rtype: dict
    :return: {
        'ChangeToken': 'string'
    }
    
    
    """
    pass

def get_change_token_status(ChangeToken=None):
    """
    Returns the status of a ChangeToken that you got by calling  GetChangeToken . ChangeTokenStatus is one of the following values:
    See also: AWS API Documentation
    
    Examples
    The following example returns the status of a change token with the ID abcd12f2-46da-4fdb-b8d5-fbd4c466928f.
    Expected Output:
    
    :example: response = client.get_change_token_status(
        ChangeToken='string'
    )
    
    
    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The change token for which you want to get the status. This change token was previously returned in the GetChangeToken response.
            

    :rtype: dict
    :return: {
        'ChangeTokenStatus': 'PROVISIONED'|'PENDING'|'INSYNC'
    }
    
    
    """
    pass

def get_geo_match_set(GeoMatchSetId=None):
    """
    Returns the  GeoMatchSet that is specified by GeoMatchSetId .
    See also: AWS API Documentation
    
    
    :example: response = client.get_geo_match_set(
        GeoMatchSetId='string'
    )
    
    
    :type GeoMatchSetId: string
    :param GeoMatchSetId: [REQUIRED]
            The GeoMatchSetId of the GeoMatchSet that you want to get. GeoMatchSetId is returned by CreateGeoMatchSet and by ListGeoMatchSets .
            

    :rtype: dict
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
    
    Examples
    The following example returns the details of an IP match set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    Expected Output:
    
    :example: response = client.get_ip_set(
        IPSetId='string'
    )
    
    
    :type IPSetId: string
    :param IPSetId: [REQUIRED]
            The IPSetId of the IPSet that you want to get. IPSetId is returned by CreateIPSet and by ListIPSets .
            

    :rtype: dict
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

def get_permission_policy(ResourceArn=None):
    """
    Returns the IAM policy attached to the RuleGroup.
    See also: AWS API Documentation
    
    
    :example: response = client.get_permission_policy(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the RuleGroup for which you want to get the policy.
            

    :rtype: dict
    :return: {
        'Policy': 'string'
    }
    
    
    """
    pass

def get_rate_based_rule(RuleId=None):
    """
    Returns the  RateBasedRule that is specified by the RuleId that you included in the GetRateBasedRule request.
    See also: AWS API Documentation
    
    
    :example: response = client.get_rate_based_rule(
        RuleId='string'
    )
    
    
    :type RuleId: string
    :param RuleId: [REQUIRED]
            The RuleId of the RateBasedRule that you want to get. RuleId is returned by CreateRateBasedRule and by ListRateBasedRules .
            

    :rtype: dict
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
    
    
    :example: response = client.get_rate_based_rule_managed_keys(
        RuleId='string',
        NextMarker='string'
    )
    
    
    :type RuleId: string
    :param RuleId: [REQUIRED]
            The RuleId of the RateBasedRule for which you want to get a list of ManagedKeys . RuleId is returned by CreateRateBasedRule and by ListRateBasedRules .
            

    :type NextMarker: string
    :param NextMarker: A null value and not currently used. Do not include this in your request.

    :rtype: dict
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
    
    
    :example: response = client.get_regex_match_set(
        RegexMatchSetId='string'
    )
    
    
    :type RegexMatchSetId: string
    :param RegexMatchSetId: [REQUIRED]
            The RegexMatchSetId of the RegexMatchSet that you want to get. RegexMatchSetId is returned by CreateRegexMatchSet and by ListRegexMatchSets .
            

    :rtype: dict
    :return: {
        'RegexMatchSet': {
            'RegexMatchSetId': 'string',
            'Name': 'string',
            'RegexMatchTuples': [
                {
                    'FieldToMatch': {
                        'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY',
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
    
    
    :example: response = client.get_regex_pattern_set(
        RegexPatternSetId='string'
    )
    
    
    :type RegexPatternSetId: string
    :param RegexPatternSetId: [REQUIRED]
            The RegexPatternSetId of the RegexPatternSet that you want to get. RegexPatternSetId is returned by CreateRegexPatternSet and by ListRegexPatternSets .
            

    :rtype: dict
    :return: {
        'RegexPatternSet': {
            'RegexPatternSetId': 'string',
            'Name': 'string',
            'RegexPatternStrings': [
                'string',
            ]
        }
    }
    
    
    """
    pass

def get_rule(RuleId=None):
    """
    Returns the  Rule that is specified by the RuleId that you included in the GetRule request.
    See also: AWS API Documentation
    
    Examples
    The following example returns the details of a rule with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    Expected Output:
    
    :example: response = client.get_rule(
        RuleId='string'
    )
    
    
    :type RuleId: string
    :param RuleId: [REQUIRED]
            The RuleId of the Rule that you want to get. RuleId is returned by CreateRule and by ListRules .
            

    :rtype: dict
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
    
    
    """
    pass

def get_rule_group(RuleGroupId=None):
    """
    Returns the  RuleGroup that is specified by the RuleGroupId that you included in the GetRuleGroup request.
    To view the rules in a rule group, use  ListActivatedRulesInRuleGroup .
    See also: AWS API Documentation
    
    
    :example: response = client.get_rule_group(
        RuleGroupId='string'
    )
    
    
    :type RuleGroupId: string
    :param RuleGroupId: [REQUIRED]
            The RuleGroupId of the RuleGroup that you want to get. RuleGroupId is returned by CreateRuleGroup and by ListRuleGroups .
            

    :rtype: dict
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
    :param WebAclId: [REQUIRED]
            The WebACLId of the WebACL for which you want GetSampledRequests to return a sample of requests.
            

    :type RuleId: string
    :param RuleId: [REQUIRED]
            RuleId is one of three values:
            The RuleId of the Rule or the RuleGroupId of the RuleGroup for which you want GetSampledRequests to return a sample of requests.
            Default_Action , which causes GetSampledRequests to return a sample of the requests that didn't match any of the rules in the specified WebACL .
            

    :type TimeWindow: dict
    :param TimeWindow: [REQUIRED]
            The start date and time and the end date and time of the range for which you want GetSampledRequests to return a sample of requests. Specify the date and time in the following format: '2016-09-27T14:50Z' . You can specify any time range in the previous three hours.
            StartTime (datetime) -- [REQUIRED]The beginning of the time range from which you want GetSampledRequests to return a sample of the requests that your AWS resource received. Specify the date and time in the following format: '2016-09-27T14:50Z' . You can specify any time range in the previous three hours.
            EndTime (datetime) -- [REQUIRED]The end of the time range from which you want GetSampledRequests to return a sample of the requests that your AWS resource received. Specify the date and time in the following format: '2016-09-27T14:50Z' . You can specify any time range in the previous three hours.
            

    :type MaxItems: integer
    :param MaxItems: [REQUIRED]
            The number of requests that you want AWS WAF to return from among the first 5,000 requests that your AWS resource received during the time range. If your resource received fewer requests than the value of MaxItems , GetSampledRequests returns information about all of them.
            

    :rtype: dict
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
    
    Examples
    The following example returns the details of a size constraint match set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    Expected Output:
    
    :example: response = client.get_size_constraint_set(
        SizeConstraintSetId='string'
    )
    
    
    :type SizeConstraintSetId: string
    :param SizeConstraintSetId: [REQUIRED]
            The SizeConstraintSetId of the SizeConstraintSet that you want to get. SizeConstraintSetId is returned by CreateSizeConstraintSet and by ListSizeConstraintSets .
            

    :rtype: dict
    :return: {
        'SizeConstraintSet': {
            'SizeConstraintSetId': 'string',
            'Name': 'string',
            'SizeConstraints': [
                {
                    'FieldToMatch': {
                        'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY',
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
    
    """
    pass

def get_sql_injection_match_set(SqlInjectionMatchSetId=None):
    """
    Returns the  SqlInjectionMatchSet that is specified by SqlInjectionMatchSetId .
    See also: AWS API Documentation
    
    Examples
    The following example returns the details of a SQL injection match set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    Expected Output:
    
    :example: response = client.get_sql_injection_match_set(
        SqlInjectionMatchSetId='string'
    )
    
    
    :type SqlInjectionMatchSetId: string
    :param SqlInjectionMatchSetId: [REQUIRED]
            The SqlInjectionMatchSetId of the SqlInjectionMatchSet that you want to get. SqlInjectionMatchSetId is returned by CreateSqlInjectionMatchSet and by ListSqlInjectionMatchSets .
            

    :rtype: dict
    :return: {
        'SqlInjectionMatchSet': {
            'SqlInjectionMatchSetId': 'string',
            'Name': 'string',
            'SqlInjectionMatchTuples': [
                {
                    'FieldToMatch': {
                        'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY',
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
    
    """
    pass

def get_waiter():
    """
    
    """
    pass

def get_web_acl(WebACLId=None):
    """
    Returns the  WebACL that is specified by WebACLId .
    See also: AWS API Documentation
    
    Examples
    The following example returns the details of a web ACL with the ID createwebacl-1472061481310.
    Expected Output:
    
    :example: response = client.get_web_acl(
        WebACLId='string'
    )
    
    
    :type WebACLId: string
    :param WebACLId: [REQUIRED]
            The WebACLId of the WebACL that you want to get. WebACLId is returned by CreateWebACL and by ListWebACLs .
            

    :rtype: dict
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
                    'Type': 'REGULAR'|'RATE_BASED'|'GROUP'
                },
            ]
        }
    }
    
    
    :returns: 
    ALLOW : AWS WAF allows requests
    BLOCK : AWS WAF blocks requests
    COUNT : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can't specify COUNT for the default action for a WebACL .
    
    """
    pass

def get_xss_match_set(XssMatchSetId=None):
    """
    Returns the  XssMatchSet that is specified by XssMatchSetId .
    See also: AWS API Documentation
    
    Examples
    The following example returns the details of an XSS match set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    Expected Output:
    
    :example: response = client.get_xss_match_set(
        XssMatchSetId='string'
    )
    
    
    :type XssMatchSetId: string
    :param XssMatchSetId: [REQUIRED]
            The XssMatchSetId of the XssMatchSet that you want to get. XssMatchSetId is returned by CreateXssMatchSet and by ListXssMatchSets .
            

    :rtype: dict
    :return: {
        'XssMatchSet': {
            'XssMatchSetId': 'string',
            'Name': 'string',
            'XssMatchTuples': [
                {
                    'FieldToMatch': {
                        'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY',
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
    
    """
    pass

def list_activated_rules_in_rule_group(RuleGroupId=None, NextMarker=None, Limit=None):
    """
    Returns an array of  ActivatedRule objects.
    See also: AWS API Documentation
    
    
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
                'Type': 'REGULAR'|'RATE_BASED'|'GROUP'
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
    
    
    :example: response = client.list_byte_match_sets(
        NextMarker='string',
        Limit=123
    )
    
    
    :type NextMarker: string
    :param NextMarker: If you specify a value for Limit and you have more ByteMatchSets than the value of Limit , AWS WAF returns a NextMarker value in the response that allows you to list another group of ByteMatchSets . For the second and subsequent ListByteMatchSets requests, specify the value of NextMarker from the previous response to get information about another batch of ByteMatchSets .

    :type Limit: integer
    :param Limit: Specifies the number of ByteMatchSet objects that you want AWS WAF to return for this request. If you have more ByteMatchSets objects than the number you specify for Limit , the response includes a NextMarker value that you can use to get another batch of ByteMatchSet objects.

    :rtype: dict
    :return: {
        'NextMarker': 'string',
        'ByteMatchSets': [
            {
                'ByteMatchSetId': 'string',
                'Name': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_geo_match_sets(NextMarker=None, Limit=None):
    """
    Returns an array of  GeoMatchSetSummary objects in the response.
    See also: AWS API Documentation
    
    
    :example: response = client.list_geo_match_sets(
        NextMarker='string',
        Limit=123
    )
    
    
    :type NextMarker: string
    :param NextMarker: If you specify a value for Limit and you have more GeoMatchSet s than the value of Limit , AWS WAF returns a NextMarker value in the response that allows you to list another group of GeoMatchSet objects. For the second and subsequent ListGeoMatchSets requests, specify the value of NextMarker from the previous response to get information about another batch of GeoMatchSet objects.

    :type Limit: integer
    :param Limit: Specifies the number of GeoMatchSet objects that you want AWS WAF to return for this request. If you have more GeoMatchSet objects than the number you specify for Limit , the response includes a NextMarker value that you can use to get another batch of GeoMatchSet objects.

    :rtype: dict
    :return: {
        'NextMarker': 'string',
        'GeoMatchSets': [
            {
                'GeoMatchSetId': 'string',
                'Name': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_ip_sets(NextMarker=None, Limit=None):
    """
    Returns an array of  IPSetSummary objects in the response.
    See also: AWS API Documentation
    
    Examples
    The following example returns an array of up to 100 IP match sets.
    Expected Output:
    
    :example: response = client.list_ip_sets(
        NextMarker='string',
        Limit=123
    )
    
    
    :type NextMarker: string
    :param NextMarker: If you specify a value for Limit and you have more IPSets than the value of Limit , AWS WAF returns a NextMarker value in the response that allows you to list another group of IPSets . For the second and subsequent ListIPSets requests, specify the value of NextMarker from the previous response to get information about another batch of IPSets .

    :type Limit: integer
    :param Limit: Specifies the number of IPSet objects that you want AWS WAF to return for this request. If you have more IPSet objects than the number you specify for Limit , the response includes a NextMarker value that you can use to get another batch of IPSet objects.

    :rtype: dict
    :return: {
        'NextMarker': 'string',
        'IPSets': [
            {
                'IPSetId': 'string',
                'Name': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_rate_based_rules(NextMarker=None, Limit=None):
    """
    Returns an array of  RuleSummary objects.
    See also: AWS API Documentation
    
    
    :example: response = client.list_rate_based_rules(
        NextMarker='string',
        Limit=123
    )
    
    
    :type NextMarker: string
    :param NextMarker: If you specify a value for Limit and you have more Rules than the value of Limit , AWS WAF returns a NextMarker value in the response that allows you to list another group of Rules . For the second and subsequent ListRateBasedRules requests, specify the value of NextMarker from the previous response to get information about another batch of Rules .

    :type Limit: integer
    :param Limit: Specifies the number of Rules that you want AWS WAF to return for this request. If you have more Rules than the number that you specify for Limit , the response includes a NextMarker value that you can use to get another batch of Rules .

    :rtype: dict
    :return: {
        'NextMarker': 'string',
        'Rules': [
            {
                'RuleId': 'string',
                'Name': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_regex_match_sets(NextMarker=None, Limit=None):
    """
    Returns an array of  RegexMatchSetSummary objects.
    See also: AWS API Documentation
    
    
    :example: response = client.list_regex_match_sets(
        NextMarker='string',
        Limit=123
    )
    
    
    :type NextMarker: string
    :param NextMarker: If you specify a value for Limit and you have more RegexMatchSet objects than the value of Limit , AWS WAF returns a NextMarker value in the response that allows you to list another group of ByteMatchSets . For the second and subsequent ListRegexMatchSets requests, specify the value of NextMarker from the previous response to get information about another batch of RegexMatchSet objects.

    :type Limit: integer
    :param Limit: Specifies the number of RegexMatchSet objects that you want AWS WAF to return for this request. If you have more RegexMatchSet objects than the number you specify for Limit , the response includes a NextMarker value that you can use to get another batch of RegexMatchSet objects.

    :rtype: dict
    :return: {
        'NextMarker': 'string',
        'RegexMatchSets': [
            {
                'RegexMatchSetId': 'string',
                'Name': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_regex_pattern_sets(NextMarker=None, Limit=None):
    """
    Returns an array of  RegexPatternSetSummary objects.
    See also: AWS API Documentation
    
    
    :example: response = client.list_regex_pattern_sets(
        NextMarker='string',
        Limit=123
    )
    
    
    :type NextMarker: string
    :param NextMarker: If you specify a value for Limit and you have more RegexPatternSet objects than the value of Limit , AWS WAF returns a NextMarker value in the response that allows you to list another group of RegexPatternSet objects. For the second and subsequent ListRegexPatternSets requests, specify the value of NextMarker from the previous response to get information about another batch of RegexPatternSet objects.

    :type Limit: integer
    :param Limit: Specifies the number of RegexPatternSet objects that you want AWS WAF to return for this request. If you have more RegexPatternSet objects than the number you specify for Limit , the response includes a NextMarker value that you can use to get another batch of RegexPatternSet objects.

    :rtype: dict
    :return: {
        'NextMarker': 'string',
        'RegexPatternSets': [
            {
                'RegexPatternSetId': 'string',
                'Name': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_rule_groups(NextMarker=None, Limit=None):
    """
    Returns an array of  RuleGroup objects.
    See also: AWS API Documentation
    
    
    :example: response = client.list_rule_groups(
        NextMarker='string',
        Limit=123
    )
    
    
    :type NextMarker: string
    :param NextMarker: If you specify a value for Limit and you have more RuleGroups than the value of Limit , AWS WAF returns a NextMarker value in the response that allows you to list another group of RuleGroups . For the second and subsequent ListRuleGroups requests, specify the value of NextMarker from the previous response to get information about another batch of RuleGroups .

    :type Limit: integer
    :param Limit: Specifies the number of RuleGroups that you want AWS WAF to return for this request. If you have more RuleGroups than the number that you specify for Limit , the response includes a NextMarker value that you can use to get another batch of RuleGroups .

    :rtype: dict
    :return: {
        'NextMarker': 'string',
        'RuleGroups': [
            {
                'RuleGroupId': 'string',
                'Name': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_rules(NextMarker=None, Limit=None):
    """
    Returns an array of  RuleSummary objects.
    See also: AWS API Documentation
    
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
    :return: {
        'NextMarker': 'string',
        'Rules': [
            {
                'RuleId': 'string',
                'Name': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_size_constraint_sets(NextMarker=None, Limit=None):
    """
    Returns an array of  SizeConstraintSetSummary objects.
    See also: AWS API Documentation
    
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
    :return: {
        'NextMarker': 'string',
        'SizeConstraintSets': [
            {
                'SizeConstraintSetId': 'string',
                'Name': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_sql_injection_match_sets(NextMarker=None, Limit=None):
    """
    Returns an array of  SqlInjectionMatchSet objects.
    See also: AWS API Documentation
    
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
    :return: {
        'NextMarker': 'string',
        'SqlInjectionMatchSets': [
            {
                'SqlInjectionMatchSetId': 'string',
                'Name': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_subscribed_rule_groups(NextMarker=None, Limit=None):
    """
    Returns an array of  RuleGroup objects that you are subscribed to.
    See also: AWS API Documentation
    
    
    :example: response = client.list_subscribed_rule_groups(
        NextMarker='string',
        Limit=123
    )
    
    
    :type NextMarker: string
    :param NextMarker: If you specify a value for Limit and you have more ByteMatchSets subscribed rule groups than the value of Limit , AWS WAF returns a NextMarker value in the response that allows you to list another group of subscribed rule groups. For the second and subsequent ListSubscribedRuleGroupsRequest requests, specify the value of NextMarker from the previous response to get information about another batch of subscribed rule groups.

    :type Limit: integer
    :param Limit: Specifies the number of subscribed rule groups that you want AWS WAF to return for this request. If you have more objects than the number you specify for Limit , the response includes a NextMarker value that you can use to get another batch of objects.

    :rtype: dict
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
    
    
    """
    pass

def list_web_acls(NextMarker=None, Limit=None):
    """
    Returns an array of  WebACLSummary objects in the response.
    See also: AWS API Documentation
    
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
    :return: {
        'NextMarker': 'string',
        'WebACLs': [
            {
                'WebACLId': 'string',
                'Name': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_xss_match_sets(NextMarker=None, Limit=None):
    """
    Returns an array of  XssMatchSet objects.
    See also: AWS API Documentation
    
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
    :return: {
        'NextMarker': 'string',
        'XssMatchSets': [
            {
                'XssMatchSetId': 'string',
                'Name': 'string'
            },
        ]
    }
    
    
    """
    pass

def put_permission_policy(ResourceArn=None, Policy=None):
    """
    Attaches a IAM policy to the specified resource. The only supported use for this action is to share a RuleGroup across accounts.
    The PutPermissionPolicy is subject to the following restrictions:
    For more information, see IAM Policies .
    An example of a valid policy parameter is shown in the Examples section below.
    See also: AWS API Documentation
    
    
    :example: response = client.put_permission_policy(
        ResourceArn='string',
        Policy='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the RuleGroup to which you want to attach the policy.
            

    :type Policy: string
    :param Policy: [REQUIRED]
            The policy to attach to the specified RuleGroup.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    ResourceArn (string) -- [REQUIRED]
    The Amazon Resource Name (ARN) of the RuleGroup to which you want to attach the policy.
    
    Policy (string) -- [REQUIRED]
    The policy to attach to the specified RuleGroup.
    
    
    """
    pass

def update_byte_match_set(ByteMatchSetId=None, ChangeToken=None, Updates=None):
    """
    Inserts or deletes  ByteMatchTuple objects (filters) in a  ByteMatchSet . For each ByteMatchTuple object, you specify the following values:
    For example, you can add a ByteMatchSetUpdate object that matches web requests in which User-Agent headers contain the string BadBot . You can then configure AWS WAF to block those requests.
    To create and configure a ByteMatchSet , perform the following steps:
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
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
                        'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY',
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
    :param ByteMatchSetId: [REQUIRED]
            The ByteMatchSetId of the ByteMatchSet that you want to update. ByteMatchSetId is returned by CreateByteMatchSet and by ListByteMatchSets .
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :type Updates: list
    :param Updates: [REQUIRED]
            An array of ByteMatchSetUpdate objects that you want to insert into or delete from a ByteMatchSet . For more information, see the applicable data types:
            ByteMatchSetUpdate : Contains Action and ByteMatchTuple
            ByteMatchTuple : Contains FieldToMatch , PositionalConstraint , TargetString , and TextTransformation
            FieldToMatch : Contains Data and Type
            (dict) --In an UpdateByteMatchSet request, ByteMatchSetUpdate specifies whether to insert or delete a ByteMatchTuple and includes the settings for the ByteMatchTuple .
            Action (string) -- [REQUIRED]Specifies whether to insert or delete a ByteMatchTuple .
            ByteMatchTuple (dict) -- [REQUIRED]Information about the part of a web request that you want AWS WAF to inspect and the value that you want AWS WAF to search for. If you specify DELETE for the value of Action , the ByteMatchTuple values must exactly match the values in the ByteMatchTuple that you want to delete from the ByteMatchSet .
            FieldToMatch (dict) -- [REQUIRED]The part of a web request that you want AWS WAF to search, such as a specified header or a query string. For more information, see FieldToMatch .
            Type (string) -- [REQUIRED]The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:
            HEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .
            METHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .
            QUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.
            URI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .
            BODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see CreateSizeConstraintSet .
            Data (string) --When the value of Type is HEADER , enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer . If the value of Type is any other value, omit Data .
            The name of the header is not case sensitive.
            TargetString (bytes) -- [REQUIRED]The value that you want AWS WAF to search for. AWS WAF searches for the specified string in the part of web requests that you specified in FieldToMatch . The maximum length of the value is 50 bytes.
            Valid values depend on the values that you specified for FieldToMatch :
            HEADER : The value that you want AWS WAF to search for in the request header that you specified in FieldToMatch , for example, the value of the User-Agent or Referer header.
            METHOD : The HTTP method, which indicates the type of operation specified in the request. CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .
            QUERY_STRING : The value that you want AWS WAF to search for in the query string, which is the part of a URL that appears after a ? character.
            URI : The value that you want AWS WAF to search for in the part of a URL that identifies a resource, for example, /images/daily-ad.jpg .
            BODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see CreateSizeConstraintSet .
            If TargetString includes alphabetic characters A-Z and a-z, note that the value is case sensitive.
            If you're using the AWS WAF API
            Specify a base64-encoded version of the value. The maximum length of the value before you base64-encode it is 50 bytes.
            For example, suppose the value of Type is HEADER and the value of Data is User-Agent . If you want to search the User-Agent header for the value BadBot , you base64-encode BadBot using MIME base64 encoding and include the resulting value, QmFkQm90 , in the value of TargetString .
            If you're using the AWS CLI or one of the AWS SDKs
            The value that you want AWS WAF to search for. The SDK automatically base64 encodes the value.
            TextTransformation (string) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on TargetString before inspecting a request for a match.
            CMD_LINE
            When you're concerned that attackers are injecting an operating system commandline command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:
            Delete the following characters: ' ' ^
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
            Replaces (ampersand)quot; with '
            Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
            Replaces (ampersand)lt; with a 'less than' symbol
            Replaces (ampersand)gt; with
            Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
            Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters
            LOWERCASE
            Use this option to convert uppercase letters (A-Z) to lowercase (a-z).
            URL_DECODE
            Use this option to decode a URL-encoded value.
            NONE
            Specify NONE if you don't want to perform any text transformations.
            PositionalConstraint (string) -- [REQUIRED]Within the portion of a web request that you want to search (for example, in the query string, if any), specify where you want AWS WAF to search. Valid values include the following:
            CONTAINS
            The specified part of the web request must include the value of TargetString , but the location doesn't matter.
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
            
            

    :rtype: dict
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
    :param GeoMatchSetId: [REQUIRED]
            The GeoMatchSetId of the GeoMatchSet that you want to update. GeoMatchSetId is returned by CreateGeoMatchSet and by ListGeoMatchSets .
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :type Updates: list
    :param Updates: [REQUIRED]
            An array of GeoMatchSetUpdate objects that you want to insert into or delete from an GeoMatchSet . For more information, see the applicable data types:
            GeoMatchSetUpdate : Contains Action and GeoMatchConstraint
            GeoMatchConstraint : Contains Type and Value  You can have only one Type and Value per GeoMatchConstraint . To add multiple countries, include multiple GeoMatchSetUpdate objects in your request.
            (dict) --Specifies the type of update to perform to an GeoMatchSet with UpdateGeoMatchSet .
            Action (string) -- [REQUIRED]Specifies whether to insert or delete a country with UpdateGeoMatchSet .
            GeoMatchConstraint (dict) -- [REQUIRED]The country from which web requests originate that you want AWS WAF to search for.
            Type (string) -- [REQUIRED]The type of geographical area you want AWS WAF to search for. Currently Country is the only valid value.
            Value (string) -- [REQUIRED]The country that you want AWS WAF to search for.
            
            

    :rtype: dict
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
    AWS WAF supports /8, /16, /24, and /32 IP address ranges for IPv4, and /24, /32, /48, /56, /64 and /128 for IPv6. For more information about CIDR notation, see the Wikipedia entry Classless Inter-Domain Routing .
    IPv6 addresses can be represented using any of the following formats:
    You use an IPSet to specify which web requests you want to allow or block based on the IP addresses that the requests originated from. For example, if you're receiving a lot of requests from one or a small number of IP addresses and you want to block the requests, you can create an IPSet that specifies those IP addresses, and then configure AWS WAF to block the requests.
    To create and configure an IPSet , perform the following steps:
    When you update an IPSet , you specify the IP addresses that you want to add and/or the IP addresses that you want to delete. If you want to change an IP address, you delete the existing IP address and add the new one.
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
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
    :param IPSetId: [REQUIRED]
            The IPSetId of the IPSet that you want to update. IPSetId is returned by CreateIPSet and by ListIPSets .
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :type Updates: list
    :param Updates: [REQUIRED]
            An array of IPSetUpdate objects that you want to insert into or delete from an IPSet . For more information, see the applicable data types:
            IPSetUpdate : Contains Action and IPSetDescriptor
            IPSetDescriptor : Contains Type and Value
            (dict) --Specifies the type of update to perform to an IPSet with UpdateIPSet .
            Action (string) -- [REQUIRED]Specifies whether to insert or delete an IP address with UpdateIPSet .
            IPSetDescriptor (dict) -- [REQUIRED]The IP address type (IPV4 or IPV6 ) and the IP address range (in CIDR notation) that web requests originate from.
            Type (string) -- [REQUIRED]Specify IPV4 or IPV6 .
            Value (string) -- [REQUIRED]Specify an IPv4 address by using CIDR notation. For example:
            To configure AWS WAF to allow, block, or count requests that originated from the IP address 192.0.2.44, specify 192.0.2.44/32 .
            To configure AWS WAF to allow, block, or count requests that originated from IP addresses from 192.0.2.0 to 192.0.2.255, specify 192.0.2.0/24 .
            For more information about CIDR notation, see the Wikipedia entry Classless Inter-Domain Routing .
            Specify an IPv6 address by using CIDR notation. For example:
            To configure AWS WAF to allow, block, or count requests that originated from the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify 1111:0000:0000:0000:0000:0000:0000:0111/128 .
            To configure AWS WAF to allow, block, or count requests that originated from IP addresses 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify 1111:0000:0000:0000:0000:0000:0000:0000/64 .
            
            

    :rtype: dict
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
    Further, you specify a RateLimit of 15,000.
    You then add the RateBasedRule to a WebACL and specify that you want to block requests that satisfy the rule. For a request to be blocked, it must come from the IP address 192.0.2.44 and the User-Agent header in the request must contain the value BadBot . Further, requests that match these two conditions much be received at a rate of more than 15,000 every five minutes. If the rate drops below this limit, AWS WAF no longer blocks the requests.
    As a second example, suppose you want to limit requests to a particular page on your site. To do this, you could add the following to a RateBasedRule :
    Further, you specify a RateLimit of 15,000.
    By adding this RateBasedRule to a WebACL , you could limit requests to your login page without affecting the rest of your site.
    See also: AWS API Documentation
    
    
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
    :param RuleId: [REQUIRED]
            The RuleId of the RateBasedRule that you want to update. RuleId is returned by CreateRateBasedRule and by ListRateBasedRules .
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :type Updates: list
    :param Updates: [REQUIRED]
            An array of RuleUpdate objects that you want to insert into or delete from a RateBasedRule .
            (dict) --Specifies a Predicate (such as an IPSet ) and indicates whether you want to add it to a Rule or delete it from a Rule .
            Action (string) -- [REQUIRED]Specify INSERT to add a Predicate to a Rule . Use DELETE to remove a Predicate from a Rule .
            Predicate (dict) -- [REQUIRED]The ID of the Predicate (such as an IPSet ) that you want to add to a Rule .
            Negated (boolean) -- [REQUIRED]Set Negated to False if you want AWS WAF to allow, block, or count requests based on the settings in the specified ByteMatchSet , IPSet , SqlInjectionMatchSet , XssMatchSet , RegexMatchSet , GeoMatchSet , or SizeConstraintSet . For example, if an IPSet includes the IP address 192.0.2.44 , AWS WAF will allow or block requests based on that IP address.
            Set Negated to True if you want AWS WAF to allow or block a request based on the negation of the settings in the ByteMatchSet , IPSet , SqlInjectionMatchSet , XssMatchSet , RegexMatchSet , GeoMatchSet , or SizeConstraintSet . For example, if an IPSet includes the IP address 192.0.2.44 , AWS WAF will allow, block, or count requests based on all IP addresses except 192.0.2.44 .
            Type (string) -- [REQUIRED]The type of predicate in a Rule , such as ByteMatchSet or IPSet .
            DataId (string) -- [REQUIRED]A unique identifier for a predicate in a Rule , such as ByteMatchSetId or IPSetId . The ID is returned by the corresponding Create or List command.
            
            

    :type RateLimit: integer
    :param RateLimit: [REQUIRED]
            The maximum number of requests, which have an identical value in the field specified by the RateKey , allowed in a five-minute period. If the number of requests exceeds the RateLimit and the other predicates specified in the rule are also met, AWS WAF triggers the action that is specified for this rule.
            

    :rtype: dict
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
    
    
    :example: response = client.update_regex_match_set(
        RegexMatchSetId='string',
        Updates=[
            {
                'Action': 'INSERT'|'DELETE',
                'RegexMatchTuple': {
                    'FieldToMatch': {
                        'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY',
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
    :param RegexMatchSetId: [REQUIRED]
            The RegexMatchSetId of the RegexMatchSet that you want to update. RegexMatchSetId is returned by CreateRegexMatchSet and by ListRegexMatchSets .
            

    :type Updates: list
    :param Updates: [REQUIRED]
            An array of RegexMatchSetUpdate objects that you want to insert into or delete from a RegexMatchSet . For more information, see RegexMatchTuple .
            (dict) --In an UpdateRegexMatchSet request, RegexMatchSetUpdate specifies whether to insert or delete a RegexMatchTuple and includes the settings for the RegexMatchTuple .
            Action (string) -- [REQUIRED]Specifies whether to insert or delete a RegexMatchTuple .
            RegexMatchTuple (dict) -- [REQUIRED]Information about the part of a web request that you want AWS WAF to inspect and the identifier of the regular expression (regex) pattern that you want AWS WAF to search for. If you specify DELETE for the value of Action , the RegexMatchTuple values must exactly match the values in the RegexMatchTuple that you want to delete from the RegexMatchSet .
            FieldToMatch (dict) -- [REQUIRED]Specifies where in a web request to look for the RegexPatternSet .
            Type (string) -- [REQUIRED]The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:
            HEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .
            METHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .
            QUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.
            URI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .
            BODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see CreateSizeConstraintSet .
            Data (string) --When the value of Type is HEADER , enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer . If the value of Type is any other value, omit Data .
            The name of the header is not case sensitive.
            TextTransformation (string) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on RegexPatternSet before inspecting a request for a match.
            CMD_LINE
            When you're concerned that attackers are injecting an operating system commandline command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:
            Delete the following characters: ' ' ^
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
            Replaces (ampersand)quot; with '
            Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
            Replaces (ampersand)lt; with a 'less than' symbol
            Replaces (ampersand)gt; with
            Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
            Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters
            LOWERCASE
            Use this option to convert uppercase letters (A-Z) to lowercase (a-z).
            URL_DECODE
            Use this option to decode a URL-encoded value.
            NONE
            Specify NONE if you don't want to perform any text transformations.
            RegexPatternSetId (string) -- [REQUIRED]The RegexPatternSetId for a RegexPatternSet . You use RegexPatternSetId to get information about a RegexPatternSet (see GetRegexPatternSet ), update a RegexPatternSet (see UpdateRegexPatternSet ), insert a RegexPatternSet into a RegexMatchSet or delete one from a RegexMatchSet (see UpdateRegexMatchSet ), and delete an RegexPatternSet from AWS WAF (see DeleteRegexPatternSet ).
            RegexPatternSetId is returned by CreateRegexPatternSet and by ListRegexPatternSets .
            
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :rtype: dict
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
    :param RegexPatternSetId: [REQUIRED]
            The RegexPatternSetId of the RegexPatternSet that you want to update. RegexPatternSetId is returned by CreateRegexPatternSet and by ListRegexPatternSets .
            

    :type Updates: list
    :param Updates: [REQUIRED]
            An array of RegexPatternSetUpdate objects that you want to insert into or delete from a RegexPatternSet .
            (dict) --In an UpdateRegexPatternSet request, RegexPatternSetUpdate specifies whether to insert or delete a RegexPatternString and includes the settings for the RegexPatternString .
            Action (string) -- [REQUIRED]Specifies whether to insert or delete a RegexPatternString .
            RegexPatternString (string) -- [REQUIRED]Specifies the regular expression (regex) pattern that you want AWS WAF to search for, such as B[a@]dB[o0]t .
            
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :rtype: dict
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
    Inserts or deletes  Predicate objects in a Rule . Each Predicate object identifies a predicate, such as a  ByteMatchSet or an  IPSet , that specifies the web requests that you want to allow, block, or count. If you add more than one predicate to a Rule , a request must match all of the specifications to be allowed, blocked, or counted. For example, suppose you add the following to a Rule :
    You then add the Rule to a WebACL and specify that you want to block requests that satisfy the Rule . For a request to be blocked, the User-Agent header in the request must contain the value BadBot and the request must originate from the IP address 192.0.2.44.
    To create and configure a Rule , perform the following steps:
    If you want to replace one ByteMatchSet or IPSet with another, you delete the existing one and add the new one.
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
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
    :param RuleId: [REQUIRED]
            The RuleId of the Rule that you want to update. RuleId is returned by CreateRule and by ListRules .
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :type Updates: list
    :param Updates: [REQUIRED]
            An array of RuleUpdate objects that you want to insert into or delete from a Rule . For more information, see the applicable data types:
            RuleUpdate : Contains Action and Predicate
            Predicate : Contains DataId , Negated , and Type
            FieldToMatch : Contains Data and Type
            (dict) --Specifies a Predicate (such as an IPSet ) and indicates whether you want to add it to a Rule or delete it from a Rule .
            Action (string) -- [REQUIRED]Specify INSERT to add a Predicate to a Rule . Use DELETE to remove a Predicate from a Rule .
            Predicate (dict) -- [REQUIRED]The ID of the Predicate (such as an IPSet ) that you want to add to a Rule .
            Negated (boolean) -- [REQUIRED]Set Negated to False if you want AWS WAF to allow, block, or count requests based on the settings in the specified ByteMatchSet , IPSet , SqlInjectionMatchSet , XssMatchSet , RegexMatchSet , GeoMatchSet , or SizeConstraintSet . For example, if an IPSet includes the IP address 192.0.2.44 , AWS WAF will allow or block requests based on that IP address.
            Set Negated to True if you want AWS WAF to allow or block a request based on the negation of the settings in the ByteMatchSet , IPSet , SqlInjectionMatchSet , XssMatchSet , RegexMatchSet , GeoMatchSet , or SizeConstraintSet . For example, if an IPSet includes the IP address 192.0.2.44 , AWS WAF will allow, block, or count requests based on all IP addresses except 192.0.2.44 .
            Type (string) -- [REQUIRED]The type of predicate in a Rule , such as ByteMatchSet or IPSet .
            DataId (string) -- [REQUIRED]A unique identifier for a predicate in a Rule , such as ByteMatchSetId or IPSetId . The ID is returned by the corresponding Create or List command.
            
            

    :rtype: dict
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
                    'Type': 'REGULAR'|'RATE_BASED'|'GROUP'
                }
            },
        ],
        ChangeToken='string'
    )
    
    
    :type RuleGroupId: string
    :param RuleGroupId: [REQUIRED]
            The RuleGroupId of the RuleGroup that you want to update. RuleGroupId is returned by CreateRuleGroup and by ListRuleGroups .
            

    :type Updates: list
    :param Updates: [REQUIRED]
            An array of RuleGroupUpdate objects that you want to insert into or delete from a RuleGroup .
            You can only insert REGULAR rules into a rule group.
            ActivatedRule|OverrideAction applies only when updating or adding a RuleGroup to a WebACL . In this case you do not use ActivatedRule|Action . For all other update requests, ActivatedRule|Action is used instead of ActivatedRule|OverrideAction .
            (dict) --Specifies an ActivatedRule and indicates whether you want to add it to a RuleGroup or delete it from a RuleGroup .
            Action (string) -- [REQUIRED]Specify INSERT to add an ActivatedRule to a RuleGroup . Use DELETE to remove an ActivatedRule from a RuleGroup .
            ActivatedRule (dict) -- [REQUIRED]The ActivatedRule object specifies a Rule that you want to insert or delete, the priority of the Rule in the WebACL , and the action that you want AWS WAF to take when a web request matches the Rule (ALLOW , BLOCK , or COUNT ).
            Priority (integer) -- [REQUIRED]Specifies the order in which the Rules in a WebACL are evaluated. Rules with a lower value for Priority are evaluated before Rules with a higher value. The value must be a unique integer. If you add multiple Rules to a WebACL , the values don't need to be consecutive.
            RuleId (string) -- [REQUIRED]The RuleId for a Rule . You use RuleId to get more information about a Rule (see GetRule ), update a Rule (see UpdateRule ), insert a Rule into a WebACL or delete a one from a WebACL (see UpdateWebACL ), or delete a Rule from AWS WAF (see DeleteRule ).
            RuleId is returned by CreateRule and by ListRules .
            Action (dict) --Specifies the action that CloudFront or AWS WAF takes when a web request matches the conditions in the Rule . Valid values for Action include the following:
            ALLOW : CloudFront responds with the requested object.
            BLOCK : CloudFront responds with an HTTP 403 (Forbidden) status code.
            COUNT : AWS WAF increments a counter of requests that match the conditions in the rule and then continues to inspect the web request based on the remaining rules in the web ACL.
            ActivatedRule|OverrideAction applies only when updating or adding a RuleGroup to a WebACL . In this case you do not use ActivatedRule|Action . For all other update requests, ActivatedRule|Action is used instead of ActivatedRule|OverrideAction .
            Type (string) -- [REQUIRED]Specifies how you want AWS WAF to respond to requests that match the settings in a Rule . Valid settings include the following:
            ALLOW : AWS WAF allows requests
            BLOCK : AWS WAF blocks requests
            COUNT : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can't specify COUNT for the default action for a WebACL .
            
            OverrideAction (dict) --Use the OverrideAction to test your RuleGroup .
            Any rule in a RuleGroup can potentially block a request. If you set the OverrideAction to None , the RuleGroup will block a request if any individual rule in the RuleGroup matches the request and is configured to block that request. However if you first want to test the RuleGroup , set the OverrideAction to Count . The RuleGroup will then override any block action specified by individual rules contained within the group. Instead of blocking matching requests, those requests will be counted. You can view a record of counted requests using GetSampledRequests .
            ActivatedRule|OverrideAction applies only when updating or adding a RuleGroup to a WebACL . In this case you do not use ActivatedRule|Action . For all other update requests, ActivatedRule|Action is used instead of ActivatedRule|OverrideAction .
            Type (string) -- [REQUIRED]
            COUNT overrides the action specified by the individual rule within a RuleGroup . If set to NONE , the rule's action will take place.
            Type (string) --The rule type, either REGULAR , as defined by Rule , RATE_BASED , as defined by RateBasedRule , or GROUP , as defined by RuleGroup . The default is REGULAR. Although this field is optional, be aware that if you try to add a RATE_BASED rule to a web ACL without setting the type, the UpdateWebACL request will fail because the request tries to add a REGULAR rule with the specified ID, which does not exist.
            
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :rtype: dict
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
    
    (dict) --Specifies an ActivatedRule and indicates whether you want to add it to a RuleGroup or delete it from a RuleGroup .
    
    Action (string) -- [REQUIRED]Specify INSERT to add an ActivatedRule to a RuleGroup . Use DELETE to remove an ActivatedRule from a RuleGroup .
    
    ActivatedRule (dict) -- [REQUIRED]The ActivatedRule object specifies a Rule that you want to insert or delete, the priority of the Rule in the WebACL , and the action that you want AWS WAF to take when a web request matches the Rule (ALLOW , BLOCK , or COUNT ).
    
    Priority (integer) -- [REQUIRED]Specifies the order in which the Rules in a WebACL are evaluated. Rules with a lower value for Priority are evaluated before Rules with a higher value. The value must be a unique integer. If you add multiple Rules to a WebACL , the values don't need to be consecutive.
    
    RuleId (string) -- [REQUIRED]The RuleId for a Rule . You use RuleId to get more information about a Rule (see  GetRule ), update a Rule (see  UpdateRule ), insert a Rule into a WebACL or delete a one from a WebACL (see  UpdateWebACL ), or delete a Rule from AWS WAF (see  DeleteRule ).
    
    RuleId is returned by  CreateRule and by  ListRules .
    
    Action (dict) --Specifies the action that CloudFront or AWS WAF takes when a web request matches the conditions in the Rule . Valid values for Action include the following:
    
    ALLOW : CloudFront responds with the requested object.
    BLOCK : CloudFront responds with an HTTP 403 (Forbidden) status code.
    COUNT : AWS WAF increments a counter of requests that match the conditions in the rule and then continues to inspect the web request based on the remaining rules in the web ACL.
    
    
    ActivatedRule|OverrideAction applies only when updating or adding a RuleGroup to a WebACL . In this case you do not use ActivatedRule|Action . For all other update requests, ActivatedRule|Action is used instead of ActivatedRule|OverrideAction .
    
    Type (string) -- [REQUIRED]Specifies how you want AWS WAF to respond to requests that match the settings in a Rule . Valid settings include the following:
    
    ALLOW : AWS WAF allows requests
    BLOCK : AWS WAF blocks requests
    COUNT : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can't specify COUNT for the default action for a WebACL .
    
    
    
    
    OverrideAction (dict) --Use the OverrideAction to test your RuleGroup .
    Any rule in a RuleGroup can potentially block a request. If you set the OverrideAction to None , the RuleGroup will block a request if any individual rule in the RuleGroup matches the request and is configured to block that request. However if you first want to test the RuleGroup , set the OverrideAction to Count . The RuleGroup will then override any block action specified by individual rules contained within the group. Instead of blocking matching requests, those requests will be counted. You can view a record of counted requests using  GetSampledRequests .
    
    ActivatedRule|OverrideAction applies only when updating or adding a RuleGroup to a WebACL . In this case you do not use ActivatedRule|Action . For all other update requests, ActivatedRule|Action is used instead of ActivatedRule|OverrideAction .
    
    Type (string) -- [REQUIRED]
    COUNT overrides the action specified by the individual rule within a RuleGroup . If set to NONE , the rule's action will take place.
    
    
    
    Type (string) --The rule type, either REGULAR , as defined by  Rule , RATE_BASED , as defined by  RateBasedRule , or GROUP , as defined by  RuleGroup . The default is REGULAR. Although this field is optional, be aware that if you try to add a RATE_BASED rule to a web ACL without setting the type, the  UpdateWebACL request will fail because the request tries to add a REGULAR rule with the specified ID, which does not exist.
    
    
    
    
    
    
    
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
                        'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY',
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
    :param SizeConstraintSetId: [REQUIRED]
            The SizeConstraintSetId of the SizeConstraintSet that you want to update. SizeConstraintSetId is returned by CreateSizeConstraintSet and by ListSizeConstraintSets .
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :type Updates: list
    :param Updates: [REQUIRED]
            An array of SizeConstraintSetUpdate objects that you want to insert into or delete from a SizeConstraintSet . For more information, see the applicable data types:
            SizeConstraintSetUpdate : Contains Action and SizeConstraint
            SizeConstraint : Contains FieldToMatch , TextTransformation , ComparisonOperator , and Size
            FieldToMatch : Contains Data and Type
            (dict) --Specifies the part of a web request that you want to inspect the size of and indicates whether you want to add the specification to a SizeConstraintSet or delete it from a SizeConstraintSet .
            Action (string) -- [REQUIRED]Specify INSERT to add a SizeConstraintSetUpdate to a SizeConstraintSet . Use DELETE to remove a SizeConstraintSetUpdate from a SizeConstraintSet .
            SizeConstraint (dict) -- [REQUIRED]Specifies a constraint on the size of a part of the web request. AWS WAF uses the Size , ComparisonOperator , and FieldToMatch to build an expression in the form of 'Size ComparisonOperator size in bytes of FieldToMatch '. If that expression is true, the SizeConstraint is considered to match.
            FieldToMatch (dict) -- [REQUIRED]Specifies where in a web request to look for the size constraint.
            Type (string) -- [REQUIRED]The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:
            HEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .
            METHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .
            QUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.
            URI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .
            BODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see CreateSizeConstraintSet .
            Data (string) --When the value of Type is HEADER , enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer . If the value of Type is any other value, omit Data .
            The name of the header is not case sensitive.
            TextTransformation (string) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on FieldToMatch before inspecting a request for a match.
            Note that if you choose BODY for the value of Type , you must choose NONE for TextTransformation because CloudFront forwards only the first 8192 bytes for inspection.
            NONE
            Specify NONE if you don't want to perform any text transformations.
            CMD_LINE
            When you're concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:
            Delete the following characters: ' ' ^
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
            Replaces (ampersand)quot; with '
            Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
            Replaces (ampersand)lt; with a 'less than' symbol
            Replaces (ampersand)gt; with
            Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
            Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters
            LOWERCASE
            Use this option to convert uppercase letters (A-Z) to lowercase (a-z).
            URL_DECODE
            Use this option to decode a URL-encoded value.
            ComparisonOperator (string) -- [REQUIRED]The type of comparison you want AWS WAF to perform. AWS WAF uses this in combination with the provided Size and FieldToMatch to build an expression in the form of 'Size ComparisonOperator size in bytes of FieldToMatch '. If that expression is true, the SizeConstraint is considered to match.
            EQ : Used to test if the Size is equal to the size of the FieldToMatchNE : Used to test if the Size is not equal to the size of the FieldToMatch
            LE : Used to test if the Size is less than or equal to the size of the FieldToMatch
            LT : Used to test if the Size is strictly less than the size of the FieldToMatch
            GE : Used to test if the Size is greater than or equal to the size of the FieldToMatch
            GT : Used to test if the Size is strictly greater than the size of the FieldToMatch
            Size (integer) -- [REQUIRED]The size in bytes that you want AWS WAF to compare against the size of the specified FieldToMatch . AWS WAF uses this in combination with ComparisonOperator and FieldToMatch to build an expression in the form of 'Size ComparisonOperator size in bytes of FieldToMatch '. If that expression is true, the SizeConstraint is considered to match.
            Valid values for size are 0 - 21474836480 bytes (0 - 20 GB).
            If you specify URI for the value of Type , the / in the URI counts as one character. For example, the URI /logo.jpg is nine characters long.
            
            

    :rtype: dict
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
    You use SqlInjectionMatchSet objects to specify which CloudFront requests you want to allow, block, or count. For example, if you're receiving requests that contain snippets of SQL code in the query string and you want to block the requests, you can create a SqlInjectionMatchSet with the applicable settings, and then configure AWS WAF to block the requests.
    To create and configure a SqlInjectionMatchSet , perform the following steps:
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
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
                        'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY',
                        'Data': 'string'
                    },
                    'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                }
            },
        ]
    )
    
    
    :type SqlInjectionMatchSetId: string
    :param SqlInjectionMatchSetId: [REQUIRED]
            The SqlInjectionMatchSetId of the SqlInjectionMatchSet that you want to update. SqlInjectionMatchSetId is returned by CreateSqlInjectionMatchSet and by ListSqlInjectionMatchSets .
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :type Updates: list
    :param Updates: [REQUIRED]
            An array of SqlInjectionMatchSetUpdate objects that you want to insert into or delete from a SqlInjectionMatchSet . For more information, see the applicable data types:
            SqlInjectionMatchSetUpdate : Contains Action and SqlInjectionMatchTuple
            SqlInjectionMatchTuple : Contains FieldToMatch and TextTransformation
            FieldToMatch : Contains Data and Type
            (dict) --Specifies the part of a web request that you want to inspect for snippets of malicious SQL code and indicates whether you want to add the specification to a SqlInjectionMatchSet or delete it from a SqlInjectionMatchSet .
            Action (string) -- [REQUIRED]Specify INSERT to add a SqlInjectionMatchSetUpdate to a SqlInjectionMatchSet . Use DELETE to remove a SqlInjectionMatchSetUpdate from a SqlInjectionMatchSet .
            SqlInjectionMatchTuple (dict) -- [REQUIRED]Specifies the part of a web request that you want AWS WAF to inspect for snippets of malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.
            FieldToMatch (dict) -- [REQUIRED]Specifies where in a web request to look for snippets of malicious SQL code.
            Type (string) -- [REQUIRED]The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:
            HEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .
            METHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .
            QUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.
            URI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .
            BODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see CreateSizeConstraintSet .
            Data (string) --When the value of Type is HEADER , enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer . If the value of Type is any other value, omit Data .
            The name of the header is not case sensitive.
            TextTransformation (string) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on FieldToMatch before inspecting a request for a match.
            CMD_LINE
            When you're concerned that attackers are injecting an operating system commandline command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:
            Delete the following characters: ' ' ^
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
            Replaces (ampersand)quot; with '
            Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
            Replaces (ampersand)lt; with a 'less than' symbol
            Replaces (ampersand)gt; with
            Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
            Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters
            LOWERCASE
            Use this option to convert uppercase letters (A-Z) to lowercase (a-z).
            URL_DECODE
            Use this option to decode a URL-encoded value.
            NONE
            Specify NONE if you don't want to perform any text transformations.
            
            

    :rtype: dict
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
                    'Type': 'REGULAR'|'RATE_BASED'|'GROUP'
                }
            },
        ],
        DefaultAction={
            'Type': 'BLOCK'|'ALLOW'|'COUNT'
        }
    )
    
    
    :type WebACLId: string
    :param WebACLId: [REQUIRED]
            The WebACLId of the WebACL that you want to update. WebACLId is returned by CreateWebACL and by ListWebACLs .
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :type Updates: list
    :param Updates: An array of updates to make to the WebACL .
            An array of WebACLUpdate objects that you want to insert into or delete from a WebACL . For more information, see the applicable data types:
            WebACLUpdate : Contains Action and ActivatedRule
            ActivatedRule : Contains Action , OverrideAction , Priority , RuleId , and Type . ActivatedRule|OverrideAction applies only when updating or adding a RuleGroup to a WebACL . In this case you do not use ActivatedRule|Action . For all other update requests, ActivatedRule|Action is used instead of ActivatedRule|OverrideAction .
            WafAction : Contains Type
            (dict) --Specifies whether to insert a Rule into or delete a Rule from a WebACL .
            Action (string) -- [REQUIRED]Specifies whether to insert a Rule into or delete a Rule from a WebACL .
            ActivatedRule (dict) -- [REQUIRED]The ActivatedRule object in an UpdateWebACL request specifies a Rule that you want to insert or delete, the priority of the Rule in the WebACL , and the action that you want AWS WAF to take when a web request matches the Rule (ALLOW , BLOCK , or COUNT ).
            Priority (integer) -- [REQUIRED]Specifies the order in which the Rules in a WebACL are evaluated. Rules with a lower value for Priority are evaluated before Rules with a higher value. The value must be a unique integer. If you add multiple Rules to a WebACL , the values don't need to be consecutive.
            RuleId (string) -- [REQUIRED]The RuleId for a Rule . You use RuleId to get more information about a Rule (see GetRule ), update a Rule (see UpdateRule ), insert a Rule into a WebACL or delete a one from a WebACL (see UpdateWebACL ), or delete a Rule from AWS WAF (see DeleteRule ).
            RuleId is returned by CreateRule and by ListRules .
            Action (dict) --Specifies the action that CloudFront or AWS WAF takes when a web request matches the conditions in the Rule . Valid values for Action include the following:
            ALLOW : CloudFront responds with the requested object.
            BLOCK : CloudFront responds with an HTTP 403 (Forbidden) status code.
            COUNT : AWS WAF increments a counter of requests that match the conditions in the rule and then continues to inspect the web request based on the remaining rules in the web ACL.
            ActivatedRule|OverrideAction applies only when updating or adding a RuleGroup to a WebACL . In this case you do not use ActivatedRule|Action . For all other update requests, ActivatedRule|Action is used instead of ActivatedRule|OverrideAction .
            Type (string) -- [REQUIRED]Specifies how you want AWS WAF to respond to requests that match the settings in a Rule . Valid settings include the following:
            ALLOW : AWS WAF allows requests
            BLOCK : AWS WAF blocks requests
            COUNT : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can't specify COUNT for the default action for a WebACL .
            
            OverrideAction (dict) --Use the OverrideAction to test your RuleGroup .
            Any rule in a RuleGroup can potentially block a request. If you set the OverrideAction to None , the RuleGroup will block a request if any individual rule in the RuleGroup matches the request and is configured to block that request. However if you first want to test the RuleGroup , set the OverrideAction to Count . The RuleGroup will then override any block action specified by individual rules contained within the group. Instead of blocking matching requests, those requests will be counted. You can view a record of counted requests using GetSampledRequests .
            ActivatedRule|OverrideAction applies only when updating or adding a RuleGroup to a WebACL . In this case you do not use ActivatedRule|Action . For all other update requests, ActivatedRule|Action is used instead of ActivatedRule|OverrideAction .
            Type (string) -- [REQUIRED]
            COUNT overrides the action specified by the individual rule within a RuleGroup . If set to NONE , the rule's action will take place.
            Type (string) --The rule type, either REGULAR , as defined by Rule , RATE_BASED , as defined by RateBasedRule , or GROUP , as defined by RuleGroup . The default is REGULAR. Although this field is optional, be aware that if you try to add a RATE_BASED rule to a web ACL without setting the type, the UpdateWebACL request will fail because the request tries to add a REGULAR rule with the specified ID, which does not exist.
            
            

    :type DefaultAction: dict
    :param DefaultAction: A default action for the web ACL, either ALLOW or BLOCK. AWS WAF performs the default action if a request doesn't match the criteria in any of the rules in a web ACL.
            Type (string) -- [REQUIRED]Specifies how you want AWS WAF to respond to requests that match the settings in a Rule . Valid settings include the following:
            ALLOW : AWS WAF allows requests
            BLOCK : AWS WAF blocks requests
            COUNT : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can't specify COUNT for the default action for a WebACL .
            

    :rtype: dict
    :return: {
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    Create and update the predicates that you want to include in Rules . For more information, see  CreateByteMatchSet ,  UpdateByteMatchSet ,  CreateIPSet ,  UpdateIPSet ,  CreateSqlInjectionMatchSet , and  UpdateSqlInjectionMatchSet .
    Create and update the Rules that you want to include in the WebACL . For more information, see  CreateRule and  UpdateRule .
    Create a WebACL . See  CreateWebACL .
    Use GetChangeToken to get the change token that you provide in the ChangeToken parameter of an  UpdateWebACL request.
    Submit an UpdateWebACL request to specify the Rules that you want to include in the WebACL , to specify the default action, and to associate the WebACL with a CloudFront distribution.
    
    """
    pass

def update_xss_match_set(XssMatchSetId=None, ChangeToken=None, Updates=None):
    """
    Inserts or deletes  XssMatchTuple objects (filters) in an  XssMatchSet . For each XssMatchTuple object, you specify the following values:
    You use XssMatchSet objects to specify which CloudFront requests you want to allow, block, or count. For example, if you're receiving requests that contain cross-site scripting attacks in the request body and you want to block the requests, you can create an XssMatchSet with the applicable settings, and then configure AWS WAF to block the requests.
    To create and configure an XssMatchSet , perform the following steps:
    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the AWS WAF Developer Guide .
    See also: AWS API Documentation
    
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
                        'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY',
                        'Data': 'string'
                    },
                    'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                }
            },
        ]
    )
    
    
    :type XssMatchSetId: string
    :param XssMatchSetId: [REQUIRED]
            The XssMatchSetId of the XssMatchSet that you want to update. XssMatchSetId is returned by CreateXssMatchSet and by ListXssMatchSets .
            

    :type ChangeToken: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            

    :type Updates: list
    :param Updates: [REQUIRED]
            An array of XssMatchSetUpdate objects that you want to insert into or delete from a XssMatchSet . For more information, see the applicable data types:
            XssMatchSetUpdate : Contains Action and XssMatchTuple
            XssMatchTuple : Contains FieldToMatch and TextTransformation
            FieldToMatch : Contains Data and Type
            (dict) --Specifies the part of a web request that you want to inspect for cross-site scripting attacks and indicates whether you want to add the specification to an XssMatchSet or delete it from an XssMatchSet .
            Action (string) -- [REQUIRED]Specify INSERT to add a XssMatchSetUpdate to an XssMatchSet . Use DELETE to remove a XssMatchSetUpdate from an XssMatchSet .
            XssMatchTuple (dict) -- [REQUIRED]Specifies the part of a web request that you want AWS WAF to inspect for cross-site scripting attacks and, if you want AWS WAF to inspect a header, the name of the header.
            FieldToMatch (dict) -- [REQUIRED]Specifies where in a web request to look for cross-site scripting attacks.
            Type (string) -- [REQUIRED]The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:
            HEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .
            METHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .
            QUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.
            URI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .
            BODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see CreateSizeConstraintSet .
            Data (string) --When the value of Type is HEADER , enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer . If the value of Type is any other value, omit Data .
            The name of the header is not case sensitive.
            TextTransformation (string) -- [REQUIRED]Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on FieldToMatch before inspecting a request for a match.
            CMD_LINE
            When you're concerned that attackers are injecting an operating system commandline command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:
            Delete the following characters: ' ' ^
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
            Replaces (ampersand)quot; with '
            Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
            Replaces (ampersand)lt; with a 'less than' symbol
            Replaces (ampersand)gt; with
            Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
            Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters
            LOWERCASE
            Use this option to convert uppercase letters (A-Z) to lowercase (a-z).
            URL_DECODE
            Use this option to decode a URL-encoded value.
            NONE
            Specify NONE if you don't want to perform any text transformations.
            
            

    :rtype: dict
    :return: {
        'ChangeToken': 'string'
    }
    
    
    :returns: 
    Submit a  CreateXssMatchSet request.
    Use  GetChangeToken to get the change token that you provide in the ChangeToken parameter of an  UpdateIPSet request.
    Submit an UpdateXssMatchSet request to specify the parts of web requests that you want AWS WAF to inspect for cross-site scripting attacks.
    
    """
    pass

