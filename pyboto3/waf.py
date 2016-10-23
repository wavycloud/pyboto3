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


def create_byte_match_set(Name=None, ChangeToken=None):
    """
    :param Name: [REQUIRED]
            A friendly name or description of the ByteMatchSet . You can't change Name after you create a ByteMatchSet .
            
    :type Name: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            
    :type ChangeToken: string
    """
    pass


def create_ip_set(Name=None, ChangeToken=None):
    """
    :param Name: [REQUIRED]
            A friendly name or description of the IPSet . You can't change Name after you create the IPSet .
            
    :type Name: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            
    :type ChangeToken: string
    """
    pass


def create_rule(Name=None, MetricName=None, ChangeToken=None):
    """
    :param Name: [REQUIRED]
            A friendly name or description of the Rule . You can't change the name of a Rule after you create it.
            
    :type Name: string
    :param MetricName: [REQUIRED]
            A friendly name or description for the metrics for this Rule . The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace. You can't change the name of the metric after you create the Rule .
            
    :type MetricName: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            
    :type ChangeToken: string
    """
    pass


def create_size_constraint_set(Name=None, ChangeToken=None):
    """
    :param Name: [REQUIRED]
            A friendly name or description of the SizeConstraintSet . You can't change Name after you create a SizeConstraintSet .
            
    :type Name: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            
    :type ChangeToken: string
    """
    pass


def create_sql_injection_match_set(Name=None, ChangeToken=None):
    """
    :param Name: [REQUIRED]
            A friendly name or description for the SqlInjectionMatchSet that you're creating. You can't change Name after you create the SqlInjectionMatchSet .
            
    :type Name: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            
    :type ChangeToken: string
    """
    pass


def create_web_acl(Name=None, MetricName=None, DefaultAction=None, ChangeToken=None):
    """
    :param Name: [REQUIRED]
            A friendly name or description of the WebACL . You can't change Name after you create the WebACL .
            
    :type Name: string
    :param MetricName: [REQUIRED]
            A friendly name or description for the metrics for this WebACL . The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace. You can't change MetricName after you create the WebACL .
            
    :type MetricName: string
    :param DefaultAction: [REQUIRED]
            The action that you want AWS WAF to take when a request doesn't match the criteria specified in any of the Rule objects that are associated with the WebACL .
            Type (string) -- [REQUIRED]Specifies how you want AWS WAF to respond to requests that match the settings in a Rule . Valid settings include the following:
            ALLOW : AWS WAF allows requests
            BLOCK : AWS WAF blocks requests
            COUNT : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can't specify COUNT for the default action for a WebACL .
            
    :type DefaultAction: dict
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            
    :type ChangeToken: string
    """
    pass


def create_xss_match_set(Name=None, ChangeToken=None):
    """
    :param Name: [REQUIRED]
            A friendly name or description for the XssMatchSet that you're creating. You can't change Name after you create the XssMatchSet .
            
    :type Name: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            
    :type ChangeToken: string
    """
    pass


def delete_byte_match_set(ByteMatchSetId=None, ChangeToken=None):
    """
    :param ByteMatchSetId: [REQUIRED]
            The ByteMatchSetId of the ByteMatchSet that you want to delete. ByteMatchSetId is returned by CreateByteMatchSet and by ListByteMatchSets .
            
    :type ByteMatchSetId: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            
    :type ChangeToken: string
    """
    pass


def delete_ip_set(IPSetId=None, ChangeToken=None):
    """
    :param IPSetId: [REQUIRED]
            The IPSetId of the IPSet that you want to delete. IPSetId is returned by CreateIPSet and by ListIPSets .
            
    :type IPSetId: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            
    :type ChangeToken: string
    """
    pass


def delete_rule(RuleId=None, ChangeToken=None):
    """
    :param RuleId: [REQUIRED]
            The RuleId of the Rule that you want to delete. RuleId is returned by CreateRule and by ListRules .
            
    :type RuleId: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            
    :type ChangeToken: string
    """
    pass


def delete_size_constraint_set(SizeConstraintSetId=None, ChangeToken=None):
    """
    :param SizeConstraintSetId: [REQUIRED]
            The SizeConstraintSetId of the SizeConstraintSet that you want to delete. SizeConstraintSetId is returned by CreateSizeConstraintSet and by ListSizeConstraintSets .
            
    :type SizeConstraintSetId: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            
    :type ChangeToken: string
    """
    pass


def delete_sql_injection_match_set(SqlInjectionMatchSetId=None, ChangeToken=None):
    """
    :param SqlInjectionMatchSetId: [REQUIRED]
            The SqlInjectionMatchSetId of the SqlInjectionMatchSet that you want to delete. SqlInjectionMatchSetId is returned by CreateSqlInjectionMatchSet and by ListSqlInjectionMatchSets .
            
    :type SqlInjectionMatchSetId: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            
    :type ChangeToken: string
    """
    pass


def delete_web_acl(WebACLId=None, ChangeToken=None):
    """
    :param WebACLId: [REQUIRED]
            The WebACLId of the WebACL that you want to delete. WebACLId is returned by CreateWebACL and by ListWebACLs .
            
    :type WebACLId: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            
    :type ChangeToken: string
    """
    pass


def delete_xss_match_set(XssMatchSetId=None, ChangeToken=None):
    """
    :param XssMatchSetId: [REQUIRED]
            The XssMatchSetId of the XssMatchSet that you want to delete. XssMatchSetId is returned by CreateXssMatchSet and by ListXssMatchSets .
            
    :type XssMatchSetId: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            
    :type ChangeToken: string
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


def get_byte_match_set(ByteMatchSetId=None):
    """
    :param ByteMatchSetId: [REQUIRED]
            The ByteMatchSetId of the ByteMatchSet that you want to get. ByteMatchSetId is returned by CreateByteMatchSet and by ListByteMatchSets .
            Return typedict
            ReturnsResponse Syntax{
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
            Response Structure
            (dict) --
            ByteMatchSet (dict) --Information about the ByteMatchSet that you specified in the GetByteMatchSet request. For more information, see the following topics:
            ByteMatchSet : Contains ByteMatchSetId , ByteMatchTuples , and Name
            ByteMatchTuples : Contains an array of ByteMatchTuple objects. Each ByteMatchTuple object contains FieldToMatch , PositionalConstraint , TargetString , and TextTransformation
            FieldToMatch : Contains Data and Type
            ByteMatchSetId (string) --The ByteMatchSetId for a ByteMatchSet . You use ByteMatchSetId to get information about a ByteMatchSet (see GetByteMatchSet ), update a ByteMatchSet (see UpdateByteMatchSet ), insert a ByteMatchSet into a Rule or delete one from a Rule (see UpdateRule ), and delete a ByteMatchSet from AWS WAF (see DeleteByteMatchSet ).
            ByteMatchSetId is returned by CreateByteMatchSet and by ListByteMatchSets .
            Name (string) --A friendly name or description of the ByteMatchSet . You can't change Name after you create a ByteMatchSet .
            ByteMatchTuples (list) --Specifies the bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to search for in web requests, the location in requests that you want AWS WAF to search, and other settings.
            (dict) --The bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to search for in web requests, the location in requests that you want AWS WAF to search, and other settings.
            FieldToMatch (dict) --The part of a web request that you want AWS WAF to search, such as a specified header or a query string. For more information, see FieldToMatch .
            Type (string) --The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:
            HEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .
            METHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .
            QUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.
            URI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .
            BODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see CreateSizeConstraintSet .
            Data (string) --When the value of Type is HEADER , enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer . If the value of Type is any other value, omit Data .
            The name of the header is not case sensitive.
            TargetString (bytes) --The value that you want AWS WAF to search for. AWS WAF searches for the specified string in the part of web requests that you specified in FieldToMatch . The maximum length of the value is 50 bytes.
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
            TextTransformation (string) --Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on TargetString before inspecting a request for a match.
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
            Replaces (ampersand)gt; with ````
            Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
            Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters
            LOWERCASE
            Use this option to convert uppercase letters (A-Z) to lowercase (a-z).
            URL_DECODE
            Use this option to decode a URL-encoded value.
            NONE
            Specify NONE if you don't want to perform any text transformations.
            PositionalConstraint (string) --Within the portion of a web request that you want to search (for example, in the query string, if any), specify where you want AWS WAF to search. Valid values include the following:
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
            
            
            
            
    :type ByteMatchSetId: string
    """
    pass


def get_change_token():
    """
    """
    pass


def get_change_token_status(ChangeToken=None):
    """
    :param ChangeToken: [REQUIRED]
            The change token for which you want to get the status. This change token was previously returned in the GetChangeToken response.
            Return typedict
            ReturnsResponse Syntax{
              'ChangeTokenStatus': 'PROVISIONED'|'PENDING'|'INSYNC'
            }
            Response Structure
            (dict) --
            ChangeTokenStatus (string) --The status of the change token.
            
            
    :type ChangeToken: string
    """
    pass


def get_ip_set(IPSetId=None):
    """
    :param IPSetId: [REQUIRED]
            The IPSetId of the IPSet that you want to get. IPSetId is returned by CreateIPSet and by ListIPSets .
            Return typedict
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
            IPSet (dict) --Information about the IPSet that you specified in the GetIPSet request. For more information, see the following topics:
            IPSet : Contains IPSetDescriptors , IPSetId , and Name
            IPSetDescriptors : Contains an array of IPSetDescriptor objects. Each IPSetDescriptor object contains Type and Value
            IPSetId (string) --The IPSetId for an IPSet . You use IPSetId to get information about an IPSet (see GetIPSet ), update an IPSet (see UpdateIPSet ), insert an IPSet into a Rule or delete one from a Rule (see UpdateRule ), and delete an IPSet from AWS WAF (see DeleteIPSet ).
            IPSetId is returned by CreateIPSet and by ListIPSets .
            Name (string) --A friendly name or description of the IPSet . You can't change the name of an IPSet after you create it.
            IPSetDescriptors (list) --The IP address type (IPV4 ) and the IP address range (in CIDR notation) that web requests originate from. If the WebACL is associated with a CloudFront distribution, this is the value of one of the following fields in CloudFront access logs:
            c-ip , if the viewer did not use an HTTP proxy or a load balancer to send the request
            x-forwarded-for , if the viewer did use an HTTP proxy or a load balancer to send the request
            (dict) --Specifies the IP address type (IPV4 ) and the IP address range (in CIDR format) that web requests originate from.
            Type (string) --Specify IPV4 .
            Value (string) --Specify an IPv4 address by using CIDR notation. For example:
            To configure AWS WAF to allow, block, or count requests that originated from the IP address 192.0.2.44, specify 192.0.2.44/32 .
            To configure AWS WAF to allow, block, or count requests that originated from IP addresses from 192.0.2.0 to 192.0.2.255, specify 192.0.2.0/24 .
            AWS WAF supports only /8, /16, /24, and /32 IP addresses.
            For more information about CIDR notation, see the Wikipedia entry Classless Inter-Domain Routing .
            
            
            
            
    :type IPSetId: string
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


def get_rule(RuleId=None):
    """
    :param RuleId: [REQUIRED]
            The RuleId of the Rule that you want to get. RuleId is returned by CreateRule and by ListRules .
            Return typedict
            ReturnsResponse Syntax{
              'Rule': {
                'RuleId': 'string',
                'Name': 'string',
                'MetricName': 'string',
                'Predicates': [
                  {
                    'Negated': True|False,
                    'Type': 'IPMatch'|'ByteMatch'|'SqlInjectionMatch'|'SizeConstraint'|'XssMatch',
                    'DataId': 'string'
                  },
                ]
              }
            }
            Response Structure
            (dict) --
            Rule (dict) --Information about the Rule that you specified in the GetRule request. For more information, see the following topics:
            Rule : Contains MetricName , Name , an array of Predicate objects, and RuleId
            Predicate : Each Predicate object contains DataId , Negated , and Type
            RuleId (string) --A unique identifier for a Rule . You use RuleId to get more information about a Rule (see GetRule ), update a Rule (see UpdateRule ), insert a Rule into a WebACL or delete a one from a WebACL (see UpdateWebACL ), or delete a Rule from AWS WAF (see DeleteRule ).
            RuleId is returned by CreateRule and by ListRules .
            Name (string) --The friendly name or description for the Rule . You can't change the name of a Rule after you create it.
            MetricName (string) --
            Predicates (list) --The Predicates object contains one Predicate element for each ByteMatchSet , IPSet , or SqlInjectionMatchSet object that you want to include in a Rule .
            (dict) --Specifies the ByteMatchSet , IPSet , SqlInjectionMatchSet , XssMatchSet , and SizeConstraintSet objects that you want to add to a Rule and, for each object, indicates whether you want to negate the settings, for example, requests that do NOT originate from the IP address 192.0.2.44.
            Negated (boolean) --Set Negated to False if you want AWS WAF to allow, block, or count requests based on the settings in the specified ByteMatchSet , IPSet , SqlInjectionMatchSet , XssMatchSet , or SizeConstraintSet . For example, if an IPSet includes the IP address 192.0.2.44 , AWS WAF will allow or block requests based on that IP address.
            Set Negated to True if you want AWS WAF to allow or block a request based on the negation of the settings in the ByteMatchSet , IPSet , SqlInjectionMatchSet , XssMatchSet , or SizeConstraintSet . For example, if an IPSet includes the IP address 192.0.2.44 , AWS WAF will allow, block, or count requests based on all IP addresses except 192.0.2.44 .
            Type (string) --The type of predicate in a Rule , such as ByteMatchSet or IPSet .
            DataId (string) --A unique identifier for a predicate in a Rule , such as ByteMatchSetId or IPSetId . The ID is returned by the corresponding Create or List command.
            
            
            
            
    :type RuleId: string
    """
    pass


def get_sampled_requests(WebAclId=None, RuleId=None, TimeWindow=None, MaxItems=None):
    """
    :param WebAclId: [REQUIRED]
            The WebACLId of the WebACL for which you want GetSampledRequests to return a sample of requests.
            
    :type WebAclId: string
    :param RuleId: [REQUIRED]
            RuleId is one of two values:
            The RuleId of the Rule for which you want GetSampledRequests to return a sample of requests.
            Default_Action , which causes GetSampledRequests to return a sample of the requests that didn't match any of the rules in the specified WebACL .
            
    :type RuleId: string
    :param TimeWindow: [REQUIRED]
            The start date and time and the end date and time of the range for which you want GetSampledRequests to return a sample of requests. Specify the date and time in Unix time format (in seconds). You can specify any time range in the previous three hours.
            StartTime (datetime) -- [REQUIRED]The beginning of the time range from which you want GetSampledRequests to return a sample of the requests that your AWS resource received. You can specify any time range in the previous three hours.
            EndTime (datetime) -- [REQUIRED]The end of the time range from which you want GetSampledRequests to return a sample of the requests that your AWS resource received. You can specify any time range in the previous three hours.
            
    :type TimeWindow: dict
    :param MaxItems: [REQUIRED]
            The number of requests that you want AWS WAF to return from among the first 5,000 requests that your AWS resource received during the time range. If your resource received fewer requests than the value of MaxItems , GetSampledRequests returns information about all of them.
            
    :type MaxItems: integer
    """
    pass


def get_size_constraint_set(SizeConstraintSetId=None):
    """
    :param SizeConstraintSetId: [REQUIRED]
            The SizeConstraintSetId of the SizeConstraintSet that you want to get. SizeConstraintSetId is returned by CreateSizeConstraintSet and by ListSizeConstraintSets .
            Return typedict
            ReturnsResponse Syntax{
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
            Response Structure
            (dict) --
            SizeConstraintSet (dict) --Information about the SizeConstraintSet that you specified in the GetSizeConstraintSet request. For more information, see the following topics:
            SizeConstraintSet : Contains SizeConstraintSetId , SizeConstraints , and Name
            SizeConstraints : Contains an array of SizeConstraint objects. Each SizeConstraint object contains FieldToMatch , TextTransformation , ComparisonOperator , and Size
            FieldToMatch : Contains Data and Type
            SizeConstraintSetId (string) --A unique identifier for a SizeConstraintSet . You use SizeConstraintSetId to get information about a SizeConstraintSet (see GetSizeConstraintSet ), update a SizeConstraintSet (see UpdateSizeConstraintSet ), insert a SizeConstraintSet into a Rule or delete one from a Rule (see UpdateRule ), and delete a SizeConstraintSet from AWS WAF (see DeleteSizeConstraintSet ).
            SizeConstraintSetId is returned by CreateSizeConstraintSet and by ListSizeConstraintSets .
            Name (string) --The name, if any, of the SizeConstraintSet .
            SizeConstraints (list) --Specifies the parts of web requests that you want to inspect the size of.
            (dict) --Specifies a constraint on the size of a part of the web request. AWS WAF uses the Size , ComparisonOperator , and FieldToMatch to build an expression in the form of 'Size ComparisonOperator size in bytes of FieldToMatch '. If that expression is true, the SizeConstraint is considered to match.
            FieldToMatch (dict) --Specifies where in a web request to look for TargetString .
            Type (string) --The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:
            HEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .
            METHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .
            QUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.
            URI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .
            BODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see CreateSizeConstraintSet .
            Data (string) --When the value of Type is HEADER , enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer . If the value of Type is any other value, omit Data .
            The name of the header is not case sensitive.
            TextTransformation (string) --Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on FieldToMatch before inspecting a request for a match.
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
            Replaces (ampersand)gt; with ````
            Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
            Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters
            LOWERCASE
            Use this option to convert uppercase letters (A-Z) to lowercase (a-z).
            URL_DECODE
            Use this option to decode a URL-encoded value.
            ComparisonOperator (string) --The type of comparison you want AWS WAF to perform. AWS WAF uses this in combination with the provided Size and FieldToMatch to build an expression in the form of 'Size ComparisonOperator size in bytes of FieldToMatch '. If that expression is true, the SizeConstraint is considered to match.
            EQ : Used to test if the Size is equal to the size of the FieldToMatchNE : Used to test if the Size is not equal to the size of the FieldToMatch
            LE : Used to test if the Size is less than or equal to the size of the FieldToMatch
            LT : Used to test if the Size is strictly less than the size of the FieldToMatch
            GE : Used to test if the Size is greater than or equal to the size of the FieldToMatch
            GT : Used to test if the Size is strictly greater than the size of the FieldToMatch
            Size (integer) --The size in bytes that you want AWS WAF to compare against the size of the specified FieldToMatch . AWS WAF uses this in combination with ComparisonOperator and FieldToMatch to build an expression in the form of 'Size ComparisonOperator size in bytes of FieldToMatch '. If that expression is true, the SizeConstraint is considered to match.
            Valid values for size are 0 - 21474836480 bytes (0 - 20 GB).
            If you specify URI for the value of Type , the / in the URI counts as one character. For example, the URI /logo.jpg is nine characters long.
            
            
            
            
    :type SizeConstraintSetId: string
    """
    pass


def get_sql_injection_match_set(SqlInjectionMatchSetId=None):
    """
    :param SqlInjectionMatchSetId: [REQUIRED]
            The SqlInjectionMatchSetId of the SqlInjectionMatchSet that you want to get. SqlInjectionMatchSetId is returned by CreateSqlInjectionMatchSet and by ListSqlInjectionMatchSets .
            Return typedict
            ReturnsResponse Syntax{
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
            Response Structure
            (dict) --The response to a GetSqlInjectionMatchSet request.
            SqlInjectionMatchSet (dict) --Information about the SqlInjectionMatchSet that you specified in the GetSqlInjectionMatchSet request. For more information, see the following topics:
            SqlInjectionMatchSet : Contains Name , SqlInjectionMatchSetId , and an array of SqlInjectionMatchTuple objects
            SqlInjectionMatchTuple : Each SqlInjectionMatchTuple object contains FieldToMatch and TextTransformation
            FieldToMatch : Contains Data and Type
            SqlInjectionMatchSetId (string) --A unique identifier for a SqlInjectionMatchSet . You use SqlInjectionMatchSetId to get information about a SqlInjectionMatchSet (see GetSqlInjectionMatchSet ), update a SqlInjectionMatchSet (see UpdateSqlInjectionMatchSet ), insert a SqlInjectionMatchSet into a Rule or delete one from a Rule (see UpdateRule ), and delete a SqlInjectionMatchSet from AWS WAF (see DeleteSqlInjectionMatchSet ).
            SqlInjectionMatchSetId is returned by CreateSqlInjectionMatchSet and by ListSqlInjectionMatchSets .
            Name (string) --The name, if any, of the SqlInjectionMatchSet .
            SqlInjectionMatchTuples (list) --Specifies the parts of web requests that you want to inspect for snippets of malicious SQL code.
            (dict) --Specifies the part of a web request that you want AWS WAF to inspect for snippets of malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.
            FieldToMatch (dict) --Specifies where in a web request to look for TargetString .
            Type (string) --The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:
            HEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .
            METHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .
            QUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.
            URI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .
            BODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see CreateSizeConstraintSet .
            Data (string) --When the value of Type is HEADER , enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer . If the value of Type is any other value, omit Data .
            The name of the header is not case sensitive.
            TextTransformation (string) --Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on FieldToMatch before inspecting a request for a match.
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
            Replaces (ampersand)gt; with ````
            Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
            Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters
            LOWERCASE
            Use this option to convert uppercase letters (A-Z) to lowercase (a-z).
            URL_DECODE
            Use this option to decode a URL-encoded value.
            NONE
            Specify NONE if you don't want to perform any text transformations.
            
            
            
            
    :type SqlInjectionMatchSetId: string
    """
    pass


def get_waiter():
    """
    """
    pass


def get_web_acl(WebACLId=None):
    """
    :param WebACLId: [REQUIRED]
            The WebACLId of the WebACL that you want to get. WebACLId is returned by CreateWebACL and by ListWebACLs .
            Return typedict
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
                    }
                  },
                ]
              }
            }
            Response Structure
            (dict) --
            WebACL (dict) --Information about the WebACL that you specified in the GetWebACL request. For more information, see the following topics:
            WebACL : Contains DefaultAction , MetricName , Name , an array of Rule objects, and WebACLId
            DefaultAction (Data type is WafAction ): Contains Type
            Rules : Contains an array of ActivatedRule objects, which contain Action , Priority , and RuleId
            Action : Contains Type
            WebACLId (string) --A unique identifier for a WebACL . You use WebACLId to get information about a WebACL (see GetWebACL ), update a WebACL (see UpdateWebACL ), and delete a WebACL from AWS WAF (see DeleteWebACL ).
            WebACLId is returned by CreateWebACL and by ListWebACLs .
            Name (string) --A friendly name or description of the WebACL . You can't change the name of a WebACL after you create it.
            MetricName (string) --
            DefaultAction (dict) --The action to perform if none of the Rules contained in the WebACL match. The action is specified by the WafAction object.
            Type (string) --Specifies how you want AWS WAF to respond to requests that match the settings in a Rule . Valid settings include the following:
            ALLOW : AWS WAF allows requests
            BLOCK : AWS WAF blocks requests
            COUNT : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can't specify COUNT for the default action for a WebACL .
            
            Rules (list) --An array that contains the action for each Rule in a WebACL , the priority of the Rule , and the ID of the Rule .
            (dict) --The ActivatedRule object in an UpdateWebACL request specifies a Rule that you want to insert or delete, the priority of the Rule in the WebACL , and the action that you want AWS WAF to take when a web request matches the Rule (ALLOW , BLOCK , or COUNT ).
            To specify whether to insert or delete a Rule , use the Action parameter in the WebACLUpdate data type.
            Priority (integer) --Specifies the order in which the Rules in a WebACL are evaluated. Rules with a lower value for Priority are evaluated before Rules with a higher value. The value must be a unique integer. If you add multiple Rules to a WebACL , the values don't need to be consecutive.
            RuleId (string) --The RuleId for a Rule . You use RuleId to get more information about a Rule (see GetRule ), update a Rule (see UpdateRule ), insert a Rule into a WebACL or delete a one from a WebACL (see UpdateWebACL ), or delete a Rule from AWS WAF (see DeleteRule ).
            RuleId is returned by CreateRule and by ListRules .
            Action (dict) --Specifies the action that CloudFront or AWS WAF takes when a web request matches the conditions in the Rule . Valid values for Action include the following:
            ALLOW : CloudFront responds with the requested object.
            BLOCK : CloudFront responds with an HTTP 403 (Forbidden) status code.
            COUNT : AWS WAF increments a counter of requests that match the conditions in the rule and then continues to inspect the web request based on the remaining rules in the web ACL.
            Type (string) --Specifies how you want AWS WAF to respond to requests that match the settings in a Rule . Valid settings include the following:
            ALLOW : AWS WAF allows requests
            BLOCK : AWS WAF blocks requests
            COUNT : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can't specify COUNT for the default action for a WebACL .
            
            
            
            
    :type WebACLId: string
    """
    pass


def get_xss_match_set(XssMatchSetId=None):
    """
    :param XssMatchSetId: [REQUIRED]
            The XssMatchSetId of the XssMatchSet that you want to get. XssMatchSetId is returned by CreateXssMatchSet and by ListXssMatchSets .
            Return typedict
            ReturnsResponse Syntax{
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
            Response Structure
            (dict) --The response to a GetXssMatchSet request.
            XssMatchSet (dict) --Information about the XssMatchSet that you specified in the GetXssMatchSet request. For more information, see the following topics:
            XssMatchSet : Contains Name , XssMatchSetId , and an array of XssMatchTuple objects
            XssMatchTuple : Each XssMatchTuple object contains FieldToMatch and TextTransformation
            FieldToMatch : Contains Data and Type
            XssMatchSetId (string) --A unique identifier for an XssMatchSet . You use XssMatchSetId to get information about an XssMatchSet (see GetXssMatchSet ), update an XssMatchSet (see UpdateXssMatchSet ), insert an XssMatchSet into a Rule or delete one from a Rule (see UpdateRule ), and delete an XssMatchSet from AWS WAF (see DeleteXssMatchSet ).
            XssMatchSetId is returned by CreateXssMatchSet and by ListXssMatchSets .
            Name (string) --The name, if any, of the XssMatchSet .
            XssMatchTuples (list) --Specifies the parts of web requests that you want to inspect for cross-site scripting attacks.
            (dict) --Specifies the part of a web request that you want AWS WAF to inspect for cross-site scripting attacks and, if you want AWS WAF to inspect a header, the name of the header.
            FieldToMatch (dict) --Specifies where in a web request to look for TargetString .
            Type (string) --The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:
            HEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .
            METHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .
            QUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.
            URI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .
            BODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see CreateSizeConstraintSet .
            Data (string) --When the value of Type is HEADER , enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer . If the value of Type is any other value, omit Data .
            The name of the header is not case sensitive.
            TextTransformation (string) --Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on FieldToMatch before inspecting a request for a match.
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
            Replaces (ampersand)gt; with ````
            Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
            Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters
            LOWERCASE
            Use this option to convert uppercase letters (A-Z) to lowercase (a-z).
            URL_DECODE
            Use this option to decode a URL-encoded value.
            NONE
            Specify NONE if you don't want to perform any text transformations.
            
            
            
            
    :type XssMatchSetId: string
    """
    pass


def list_byte_match_sets(NextMarker=None, Limit=None):
    """
    :param NextMarker: If you specify a value for Limit and you have more ByteMatchSets than the value of Limit , AWS WAF returns a NextMarker value in the response that allows you to list another group of ByteMatchSets . For the second and subsequent ListByteMatchSets requests, specify the value of NextMarker from the previous response to get information about another batch of ByteMatchSets .
    :type NextMarker: string
    :param Limit: Specifies the number of ByteMatchSet objects that you want AWS WAF to return for this request. If you have more ByteMatchSets objects than the number you specify for Limit , the response includes a NextMarker value that you can use to get another batch of ByteMatchSet objects.
    :type Limit: integer
    """
    pass


def list_ip_sets(NextMarker=None, Limit=None):
    """
    :param NextMarker: If you specify a value for Limit and you have more IPSets than the value of Limit , AWS WAF returns a NextMarker value in the response that allows you to list another group of IPSets . For the second and subsequent ListIPSets requests, specify the value of NextMarker from the previous response to get information about another batch of ByteMatchSets .
    :type NextMarker: string
    :param Limit: Specifies the number of IPSet objects that you want AWS WAF to return for this request. If you have more IPSet objects than the number you specify for Limit , the response includes a NextMarker value that you can use to get another batch of IPSet objects.
    :type Limit: integer
    """
    pass


def list_rules(NextMarker=None, Limit=None):
    """
    :param NextMarker: If you specify a value for Limit and you have more Rules than the value of Limit , AWS WAF returns a NextMarker value in the response that allows you to list another group of Rules . For the second and subsequent ListRules requests, specify the value of NextMarker from the previous response to get information about another batch of Rules .
    :type NextMarker: string
    :param Limit: Specifies the number of Rules that you want AWS WAF to return for this request. If you have more Rules than the number that you specify for Limit , the response includes a NextMarker value that you can use to get another batch of Rules .
    :type Limit: integer
    """
    pass


def list_size_constraint_sets(NextMarker=None, Limit=None):
    """
    :param NextMarker: If you specify a value for Limit and you have more SizeConstraintSets than the value of Limit , AWS WAF returns a NextMarker value in the response that allows you to list another group of SizeConstraintSets . For the second and subsequent ListSizeConstraintSets requests, specify the value of NextMarker from the previous response to get information about another batch of SizeConstraintSets .
    :type NextMarker: string
    :param Limit: Specifies the number of SizeConstraintSet objects that you want AWS WAF to return for this request. If you have more SizeConstraintSets objects than the number you specify for Limit , the response includes a NextMarker value that you can use to get another batch of SizeConstraintSet objects.
    :type Limit: integer
    """
    pass


def list_sql_injection_match_sets(NextMarker=None, Limit=None):
    """
    :param NextMarker: If you specify a value for Limit and you have more SqlInjectionMatchSet objects than the value of Limit , AWS WAF returns a NextMarker value in the response that allows you to list another group of SqlInjectionMatchSets . For the second and subsequent ListSqlInjectionMatchSets requests, specify the value of NextMarker from the previous response to get information about another batch of SqlInjectionMatchSets .
    :type NextMarker: string
    :param Limit: Specifies the number of SqlInjectionMatchSet objects that you want AWS WAF to return for this request. If you have more SqlInjectionMatchSet objects than the number you specify for Limit , the response includes a NextMarker value that you can use to get another batch of Rules .
    :type Limit: integer
    """
    pass


def list_web_acls(NextMarker=None, Limit=None):
    """
    :param NextMarker: If you specify a value for Limit and you have more WebACL objects than the number that you specify for Limit , AWS WAF returns a NextMarker value in the response that allows you to list another group of WebACL objects. For the second and subsequent ListWebACLs requests, specify the value of NextMarker from the previous response to get information about another batch of WebACL objects.
    :type NextMarker: string
    :param Limit: Specifies the number of WebACL objects that you want AWS WAF to return for this request. If you have more WebACL objects than the number that you specify for Limit , the response includes a NextMarker value that you can use to get another batch of WebACL objects.
    :type Limit: integer
    """
    pass


def list_xss_match_sets(NextMarker=None, Limit=None):
    """
    :param NextMarker: If you specify a value for Limit and you have more XssMatchSet objects than the value of Limit , AWS WAF returns a NextMarker value in the response that allows you to list another group of XssMatchSets . For the second and subsequent ListXssMatchSets requests, specify the value of NextMarker from the previous response to get information about another batch of XssMatchSets .
    :type NextMarker: string
    :param Limit: Specifies the number of XssMatchSet objects that you want AWS WAF to return for this request. If you have more XssMatchSet objects than the number you specify for Limit , the response includes a NextMarker value that you can use to get another batch of Rules .
    :type Limit: integer
    """
    pass


def update_byte_match_set(ByteMatchSetId=None, ChangeToken=None, Updates=None):
    """
    :param ByteMatchSetId: [REQUIRED]
            The ByteMatchSetId of the ByteMatchSet that you want to update. ByteMatchSetId is returned by CreateByteMatchSet and by ListByteMatchSets .
            
    :type ByteMatchSetId: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            
    :type ChangeToken: string
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
            Replaces (ampersand)gt; with ````
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
            
            
    :type Updates: list
    """
    pass


def update_ip_set(IPSetId=None, ChangeToken=None, Updates=None):
    """
    :param IPSetId: [REQUIRED]
            The IPSetId of the IPSet that you want to update. IPSetId is returned by CreateIPSet and by ListIPSets .
            
    :type IPSetId: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            
    :type ChangeToken: string
    :param Updates: [REQUIRED]
            An array of IPSetUpdate objects that you want to insert into or delete from an IPSet . For more information, see the applicable data types:
            IPSetUpdate : Contains Action and IPSetDescriptor
            IPSetDescriptor : Contains Type and Value
            (dict) --Specifies the type of update to perform to an IPSet with UpdateIPSet .
            Action (string) -- [REQUIRED]Specifies whether to insert or delete an IP address with UpdateIPSet .
            IPSetDescriptor (dict) -- [REQUIRED]The IP address type (IPV4 ) and the IP address range (in CIDR notation) that web requests originate from.
            Type (string) -- [REQUIRED]Specify IPV4 .
            Value (string) -- [REQUIRED]Specify an IPv4 address by using CIDR notation. For example:
            To configure AWS WAF to allow, block, or count requests that originated from the IP address 192.0.2.44, specify 192.0.2.44/32 .
            To configure AWS WAF to allow, block, or count requests that originated from IP addresses from 192.0.2.0 to 192.0.2.255, specify 192.0.2.0/24 .
            AWS WAF supports only /8, /16, /24, and /32 IP addresses.
            For more information about CIDR notation, see the Wikipedia entry Classless Inter-Domain Routing .
            
            
    :type Updates: list
    """
    pass


def update_rule(RuleId=None, ChangeToken=None, Updates=None):
    """
    :param RuleId: [REQUIRED]
            The RuleId of the Rule that you want to update. RuleId is returned by CreateRule and by ListRules .
            
    :type RuleId: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            
    :type ChangeToken: string
    :param Updates: [REQUIRED]
            An array of RuleUpdate objects that you want to insert into or delete from a Rule . For more information, see the applicable data types:
            RuleUpdate : Contains Action and Predicate
            Predicate : Contains DataId , Negated , and Type
            FieldToMatch : Contains Data and Type
            (dict) --Specifies a Predicate (such as an IPSet ) and indicates whether you want to add it to a Rule or delete it from a Rule .
            Action (string) -- [REQUIRED]Specify INSERT to add a Predicate to a Rule . Use DELETE to remove a Predicate from a Rule .
            Predicate (dict) -- [REQUIRED]The ID of the Predicate (such as an IPSet ) that you want to add to a Rule .
            Negated (boolean) -- [REQUIRED]Set Negated to False if you want AWS WAF to allow, block, or count requests based on the settings in the specified ByteMatchSet , IPSet , SqlInjectionMatchSet , XssMatchSet , or SizeConstraintSet . For example, if an IPSet includes the IP address 192.0.2.44 , AWS WAF will allow or block requests based on that IP address.
            Set Negated to True if you want AWS WAF to allow or block a request based on the negation of the settings in the ByteMatchSet , IPSet , SqlInjectionMatchSet , XssMatchSet , or SizeConstraintSet . For example, if an IPSet includes the IP address 192.0.2.44 , AWS WAF will allow, block, or count requests based on all IP addresses except 192.0.2.44 .
            Type (string) -- [REQUIRED]The type of predicate in a Rule , such as ByteMatchSet or IPSet .
            DataId (string) -- [REQUIRED]A unique identifier for a predicate in a Rule , such as ByteMatchSetId or IPSetId . The ID is returned by the corresponding Create or List command.
            
            
    :type Updates: list
    """
    pass


def update_size_constraint_set(SizeConstraintSetId=None, ChangeToken=None, Updates=None):
    """
    :param SizeConstraintSetId: [REQUIRED]
            The SizeConstraintSetId of the SizeConstraintSet that you want to update. SizeConstraintSetId is returned by CreateSizeConstraintSet and by ListSizeConstraintSets .
            
    :type SizeConstraintSetId: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            
    :type ChangeToken: string
    :param Updates: [REQUIRED]
            An array of SizeConstraintSetUpdate objects that you want to insert into or delete from a SizeConstraintSet . For more information, see the applicable data types:
            SizeConstraintSetUpdate : Contains Action and SizeConstraint
            SizeConstraint : Contains FieldToMatch , TextTransformation , ComparisonOperator , and Size
            FieldToMatch : Contains Data and Type
            (dict) --Specifies the part of a web request that you want to inspect the size of and indicates whether you want to add the specification to a SizeConstraintSet or delete it from a SizeConstraintSet .
            Action (string) -- [REQUIRED]Specify INSERT to add a SizeConstraintSetUpdate to a SizeConstraintSet . Use DELETE to remove a SizeConstraintSetUpdate from a SizeConstraintSet .
            SizeConstraint (dict) -- [REQUIRED]Specifies a constraint on the size of a part of the web request. AWS WAF uses the Size , ComparisonOperator , and FieldToMatch to build an expression in the form of 'Size ComparisonOperator size in bytes of FieldToMatch '. If that expression is true, the SizeConstraint is considered to match.
            FieldToMatch (dict) -- [REQUIRED]Specifies where in a web request to look for TargetString .
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
            Replaces (ampersand)gt; with ````
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
            
            
    :type Updates: list
    """
    pass


def update_sql_injection_match_set(SqlInjectionMatchSetId=None, ChangeToken=None, Updates=None):
    """
    :param SqlInjectionMatchSetId: [REQUIRED]
            The SqlInjectionMatchSetId of the SqlInjectionMatchSet that you want to update. SqlInjectionMatchSetId is returned by CreateSqlInjectionMatchSet and by ListSqlInjectionMatchSets .
            
    :type SqlInjectionMatchSetId: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            
    :type ChangeToken: string
    :param Updates: [REQUIRED]
            An array of SqlInjectionMatchSetUpdate objects that you want to insert into or delete from a SqlInjectionMatchSet . For more information, see the applicable data types:
            SqlInjectionMatchSetUpdate : Contains Action and SqlInjectionMatchTuple
            SqlInjectionMatchTuple : Contains FieldToMatch and TextTransformation
            FieldToMatch : Contains Data and Type
            (dict) --Specifies the part of a web request that you want to inspect for snippets of malicious SQL code and indicates whether you want to add the specification to a SqlInjectionMatchSet or delete it from a SqlInjectionMatchSet .
            Action (string) -- [REQUIRED]Specify INSERT to add a SqlInjectionMatchSetUpdate to a SqlInjectionMatchSet . Use DELETE to remove a SqlInjectionMatchSetUpdate from a SqlInjectionMatchSet .
            SqlInjectionMatchTuple (dict) -- [REQUIRED]Specifies the part of a web request that you want AWS WAF to inspect for snippets of malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.
            FieldToMatch (dict) -- [REQUIRED]Specifies where in a web request to look for TargetString .
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
            Replaces (ampersand)gt; with ````
            Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
            Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters
            LOWERCASE
            Use this option to convert uppercase letters (A-Z) to lowercase (a-z).
            URL_DECODE
            Use this option to decode a URL-encoded value.
            NONE
            Specify NONE if you don't want to perform any text transformations.
            
            
    :type Updates: list
    """
    pass


def update_web_acl(WebACLId=None, ChangeToken=None, Updates=None, DefaultAction=None):
    """
    :param WebACLId: [REQUIRED]
            The WebACLId of the WebACL that you want to update. WebACLId is returned by CreateWebACL and by ListWebACLs .
            
    :type WebACLId: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            
    :type ChangeToken: string
    :param Updates: An array of updates to make to the WebACL .
            An array of WebACLUpdate objects that you want to insert into or delete from a WebACL . For more information, see the applicable data types:
            WebACLUpdate : Contains Action and ActivatedRule
            ActivatedRule : Contains Action , Priority , and RuleId
            WafAction : Contains Type
            (dict) --Specifies whether to insert a Rule into or delete a Rule from a WebACL .
            Action (string) -- [REQUIRED]Specifies whether to insert a Rule into or delete a Rule from a WebACL .
            ActivatedRule (dict) -- [REQUIRED]The ActivatedRule object in an UpdateWebACL request specifies a Rule that you want to insert or delete, the priority of the Rule in the WebACL , and the action that you want AWS WAF to take when a web request matches the Rule (ALLOW , BLOCK , or COUNT ).
            To specify whether to insert or delete a Rule , use the Action parameter in the WebACLUpdate data type.
            Priority (integer) -- [REQUIRED]Specifies the order in which the Rules in a WebACL are evaluated. Rules with a lower value for Priority are evaluated before Rules with a higher value. The value must be a unique integer. If you add multiple Rules to a WebACL , the values don't need to be consecutive.
            RuleId (string) -- [REQUIRED]The RuleId for a Rule . You use RuleId to get more information about a Rule (see GetRule ), update a Rule (see UpdateRule ), insert a Rule into a WebACL or delete a one from a WebACL (see UpdateWebACL ), or delete a Rule from AWS WAF (see DeleteRule ).
            RuleId is returned by CreateRule and by ListRules .
            Action (dict) -- [REQUIRED]Specifies the action that CloudFront or AWS WAF takes when a web request matches the conditions in the Rule . Valid values for Action include the following:
            ALLOW : CloudFront responds with the requested object.
            BLOCK : CloudFront responds with an HTTP 403 (Forbidden) status code.
            COUNT : AWS WAF increments a counter of requests that match the conditions in the rule and then continues to inspect the web request based on the remaining rules in the web ACL.
            Type (string) -- [REQUIRED]Specifies how you want AWS WAF to respond to requests that match the settings in a Rule . Valid settings include the following:
            ALLOW : AWS WAF allows requests
            BLOCK : AWS WAF blocks requests
            COUNT : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can't specify COUNT for the default action for a WebACL .
            
            
            
    :type Updates: list
    :param DefaultAction: For the action that is associated with a rule in a WebACL , specifies the action that you want AWS WAF to perform when a web request matches all of the conditions in a rule. For the default action in a WebACL , specifies the action that you want AWS WAF to take when a web request doesn't match all of the conditions in any of the rules in a WebACL .
            Type (string) -- [REQUIRED]Specifies how you want AWS WAF to respond to requests that match the settings in a Rule . Valid settings include the following:
            ALLOW : AWS WAF allows requests
            BLOCK : AWS WAF blocks requests
            COUNT : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can't specify COUNT for the default action for a WebACL .
            
    :type DefaultAction: dict
    """
    pass


def update_xss_match_set(XssMatchSetId=None, ChangeToken=None, Updates=None):
    """
    :param XssMatchSetId: [REQUIRED]
            The XssMatchSetId of the XssMatchSet that you want to update. XssMatchSetId is returned by CreateXssMatchSet and by ListXssMatchSets .
            
    :type XssMatchSetId: string
    :param ChangeToken: [REQUIRED]
            The value returned by the most recent call to GetChangeToken .
            
    :type ChangeToken: string
    :param Updates: [REQUIRED]
            An array of XssMatchSetUpdate objects that you want to insert into or delete from a XssMatchSet . For more information, see the applicable data types:
            XssMatchSetUpdate : Contains Action and XssMatchTuple
            XssMatchTuple : Contains FieldToMatch and TextTransformation
            FieldToMatch : Contains Data and Type
            (dict) --Specifies the part of a web request that you want to inspect for cross-site scripting attacks and indicates whether you want to add the specification to an XssMatchSet or delete it from an XssMatchSet .
            Action (string) -- [REQUIRED]Specify INSERT to add a XssMatchSetUpdate to an XssMatchSet . Use DELETE to remove a XssMatchSetUpdate from an XssMatchSet .
            XssMatchTuple (dict) -- [REQUIRED]Specifies the part of a web request that you want AWS WAF to inspect for cross-site scripting attacks and, if you want AWS WAF to inspect a header, the name of the header.
            FieldToMatch (dict) -- [REQUIRED]Specifies where in a web request to look for TargetString .
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
            Replaces (ampersand)gt; with ````
            Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
            Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters
            LOWERCASE
            Use this option to convert uppercase letters (A-Z) to lowercase (a-z).
            URL_DECODE
            Use this option to decode a URL-encoded value.
            NONE
            Specify NONE if you don't want to perform any text transformations.
            
            
    :type Updates: list
    """
    pass
