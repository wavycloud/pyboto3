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

def add_listener_certificates(ListenerArn=None, Certificates=None):
    """
    Adds the specified SSL server certificate to the certificate list for the specified HTTPS or TLS listener.
    If the certificate in already in the certificate list, the call is successful but the certificate is not added again.
    To get the certificate list for a listener, use  DescribeListenerCertificates . To remove certificates from the certificate list for a listener, use  RemoveListenerCertificates . To replace the default certificate for a listener, use  ModifyListener .
    For more information, see SSL Certificates in the Application Load Balancers Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.add_listener_certificates(
        ListenerArn='string',
        Certificates=[
            {
                'CertificateArn': 'string',
                'IsDefault': True|False
            },
        ]
    )
    
    
    :type ListenerArn: string
    :param ListenerArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the listener.\n

    :type Certificates: list
    :param Certificates: [REQUIRED]\nThe certificate to add. You can specify one certificate per call. Set CertificateArn to the certificate ARN but do not set IsDefault .\n\n(dict) --Information about an SSL server certificate.\n\nCertificateArn (string) --The Amazon Resource Name (ARN) of the certificate.\n\nIsDefault (boolean) --Indicates whether the certificate is the default certificate. Do not set this value when specifying a certificate as an input. This value is not included in the output when describing a listener, but is included when describing listener certificates.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Certificates': [
        {
            'CertificateArn': 'string',
            'IsDefault': True|False
        },
    ]
}


Response Structure

(dict) --

Certificates (list) --
Information about the certificates in the certificate list.

(dict) --
Information about an SSL server certificate.

CertificateArn (string) --
The Amazon Resource Name (ARN) of the certificate.

IsDefault (boolean) --
Indicates whether the certificate is the default certificate. Do not set this value when specifying a certificate as an input. This value is not included in the output when describing a listener, but is included when describing listener certificates.











Exceptions

ElasticLoadBalancingv2.Client.exceptions.ListenerNotFoundException
ElasticLoadBalancingv2.Client.exceptions.TooManyCertificatesException
ElasticLoadBalancingv2.Client.exceptions.CertificateNotFoundException


    :return: {
        'Certificates': [
            {
                'CertificateArn': 'string',
                'IsDefault': True|False
            },
        ]
    }
    
    
    :returns: 
    ElasticLoadBalancingv2.Client.exceptions.ListenerNotFoundException
    ElasticLoadBalancingv2.Client.exceptions.TooManyCertificatesException
    ElasticLoadBalancingv2.Client.exceptions.CertificateNotFoundException
    
    """
    pass

def add_tags(ResourceArns=None, Tags=None):
    """
    Adds the specified tags to the specified Elastic Load Balancing resource. You can tag your Application Load Balancers, Network Load Balancers, and your target groups.
    Each tag consists of a key and an optional value. If a resource already has a tag with the same key, AddTags updates its value.
    To list the current tags for your resources, use  DescribeTags . To remove tags from your resources, use  RemoveTags .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example adds the specified tags to the specified load balancer.
    Expected Output:
    
    :example: response = client.add_tags(
        ResourceArns=[
            'string',
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceArns: list
    :param ResourceArns: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource.\n\n(string) --\n\n

    :type Tags: list
    :param Tags: [REQUIRED]\nThe tags.\n\n(dict) --Information about a tag.\n\nKey (string) -- [REQUIRED]The key of the tag.\n\nValue (string) --The value of the tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ElasticLoadBalancingv2.Client.exceptions.DuplicateTagKeysException
ElasticLoadBalancingv2.Client.exceptions.TooManyTagsException
ElasticLoadBalancingv2.Client.exceptions.LoadBalancerNotFoundException
ElasticLoadBalancingv2.Client.exceptions.TargetGroupNotFoundException

Examples
This example adds the specified tags to the specified load balancer.
response = client.add_tags(
    ResourceArns=[
        'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
    ],
    Tags=[
        {
            'Key': 'project',
            'Value': 'lima',
        },
        {
            'Key': 'department',
            'Value': 'digital-media',
        },
    ],
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



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

def create_listener(LoadBalancerArn=None, Protocol=None, Port=None, SslPolicy=None, Certificates=None, DefaultActions=None, AlpnPolicy=None):
    """
    Creates a listener for the specified Application Load Balancer or Network Load Balancer.
    To update a listener, use  ModifyListener . When you are finished with a listener, you can delete it using  DeleteListener . If you are finished with both the listener and the load balancer, you can delete them both using  DeleteLoadBalancer .
    This operation is idempotent, which means that it completes at most one time. If you attempt to create multiple listeners with the same settings, each call succeeds.
    For more information, see Listeners for Your Application Load Balancers in the Application Load Balancers Guide and Listeners for Your Network Load Balancers in the Network Load Balancers Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example creates an HTTP listener for the specified load balancer that forwards requests to the specified target group.
    Expected Output:
    This example creates an HTTPS listener for the specified load balancer that forwards requests to the specified target group. Note that you must specify an SSL certificate for an HTTPS listener. You can create and manage certificates using AWS Certificate Manager (ACM). Alternatively, you can create a certificate using SSL/TLS tools, get the certificate signed by a certificate authority (CA), and upload the certificate to AWS Identity and Access Management (IAM).
    Expected Output:
    
    :example: response = client.create_listener(
        LoadBalancerArn='string',
        Protocol='HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
        Port=123,
        SslPolicy='string',
        Certificates=[
            {
                'CertificateArn': 'string',
                'IsDefault': True|False
            },
        ],
        DefaultActions=[
            {
                'Type': 'forward'|'authenticate-oidc'|'authenticate-cognito'|'redirect'|'fixed-response',
                'TargetGroupArn': 'string',
                'AuthenticateOidcConfig': {
                    'Issuer': 'string',
                    'AuthorizationEndpoint': 'string',
                    'TokenEndpoint': 'string',
                    'UserInfoEndpoint': 'string',
                    'ClientId': 'string',
                    'ClientSecret': 'string',
                    'SessionCookieName': 'string',
                    'Scope': 'string',
                    'SessionTimeout': 123,
                    'AuthenticationRequestExtraParams': {
                        'string': 'string'
                    },
                    'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate',
                    'UseExistingClientSecret': True|False
                },
                'AuthenticateCognitoConfig': {
                    'UserPoolArn': 'string',
                    'UserPoolClientId': 'string',
                    'UserPoolDomain': 'string',
                    'SessionCookieName': 'string',
                    'Scope': 'string',
                    'SessionTimeout': 123,
                    'AuthenticationRequestExtraParams': {
                        'string': 'string'
                    },
                    'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate'
                },
                'Order': 123,
                'RedirectConfig': {
                    'Protocol': 'string',
                    'Port': 'string',
                    'Host': 'string',
                    'Path': 'string',
                    'Query': 'string',
                    'StatusCode': 'HTTP_301'|'HTTP_302'
                },
                'FixedResponseConfig': {
                    'MessageBody': 'string',
                    'StatusCode': 'string',
                    'ContentType': 'string'
                },
                'ForwardConfig': {
                    'TargetGroups': [
                        {
                            'TargetGroupArn': 'string',
                            'Weight': 123
                        },
                    ],
                    'TargetGroupStickinessConfig': {
                        'Enabled': True|False,
                        'DurationSeconds': 123
                    }
                }
            },
        ],
        AlpnPolicy=[
            'string',
        ]
    )
    
    
    :type LoadBalancerArn: string
    :param LoadBalancerArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the load balancer.\n

    :type Protocol: string
    :param Protocol: [REQUIRED]\nThe protocol for connections from clients to the load balancer. For Application Load Balancers, the supported protocols are HTTP and HTTPS. For Network Load Balancers, the supported protocols are TCP, TLS, UDP, and TCP_UDP.\n

    :type Port: integer
    :param Port: [REQUIRED]\nThe port on which the load balancer is listening.\n

    :type SslPolicy: string
    :param SslPolicy: [HTTPS and TLS listeners] The security policy that defines which protocols and ciphers are supported. The following are the possible values:\n\nELBSecurityPolicy-2016-08\nELBSecurityPolicy-TLS-1-0-2015-04\nELBSecurityPolicy-TLS-1-1-2017-01\nELBSecurityPolicy-TLS-1-2-2017-01\nELBSecurityPolicy-TLS-1-2-Ext-2018-06\nELBSecurityPolicy-FS-2018-06\nELBSecurityPolicy-FS-1-1-2019-08\nELBSecurityPolicy-FS-1-2-2019-08\nELBSecurityPolicy-FS-1-2-Res-2019-08\n\nFor more information, see Security Policies in the Application Load Balancers Guide and Security Policies in the Network Load Balancers Guide .\n

    :type Certificates: list
    :param Certificates: [HTTPS and TLS listeners] The default certificate for the listener. You must provide exactly one certificate. Set CertificateArn to the certificate ARN but do not set IsDefault .\nTo create a certificate list for the listener, use AddListenerCertificates .\n\n(dict) --Information about an SSL server certificate.\n\nCertificateArn (string) --The Amazon Resource Name (ARN) of the certificate.\n\nIsDefault (boolean) --Indicates whether the certificate is the default certificate. Do not set this value when specifying a certificate as an input. This value is not included in the output when describing a listener, but is included when describing listener certificates.\n\n\n\n\n

    :type DefaultActions: list
    :param DefaultActions: [REQUIRED]\nThe actions for the default rule. The rule must include one forward action or one or more fixed-response actions.\nIf the action type is forward , you specify one or more target groups. The protocol of the target group must be HTTP or HTTPS for an Application Load Balancer. The protocol of the target group must be TCP, TLS, UDP, or TCP_UDP for a Network Load Balancer.\n[HTTPS listeners] If the action type is authenticate-oidc , you authenticate users through an identity provider that is OpenID Connect (OIDC) compliant.\n[HTTPS listeners] If the action type is authenticate-cognito , you authenticate users through the user pools supported by Amazon Cognito.\n[Application Load Balancer] If the action type is redirect , you redirect specified client requests from one URL to another.\n[Application Load Balancer] If the action type is fixed-response , you drop specified client requests and return a custom HTTP response.\n\n(dict) --Information about an action.\n\nType (string) -- [REQUIRED]The type of action.\n\nTargetGroupArn (string) --The Amazon Resource Name (ARN) of the target group. Specify only when Type is forward and you want to route to a single target group. To route to one or more target groups, use ForwardConfig instead.\n\nAuthenticateOidcConfig (dict) --[HTTPS listeners] Information about an identity provider that is compliant with OpenID Connect (OIDC). Specify only when Type is authenticate-oidc .\n\nIssuer (string) -- [REQUIRED]The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.\n\nAuthorizationEndpoint (string) -- [REQUIRED]The authorization endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.\n\nTokenEndpoint (string) -- [REQUIRED]The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.\n\nUserInfoEndpoint (string) -- [REQUIRED]The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.\n\nClientId (string) -- [REQUIRED]The OAuth 2.0 client identifier.\n\nClientSecret (string) --The OAuth 2.0 client secret. This parameter is required if you are creating a rule. If you are modifying a rule, you can omit this parameter if you set UseExistingClientSecret to true.\n\nSessionCookieName (string) --The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.\n\nScope (string) --The set of user claims to be requested from the IdP. The default is openid .\nTo verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.\n\nSessionTimeout (integer) --The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).\n\nAuthenticationRequestExtraParams (dict) --The query parameters (up to 10) to include in the redirect request to the authorization endpoint.\n\n(string) --\n(string) --\n\n\n\n\nOnUnauthenticatedRequest (string) --The behavior if the user is not authenticated. The following are possible values:\n\ndeny- Return an HTTP 401 Unauthorized error.\nallow- Allow the request to be forwarded to the target.\nauthenticate- Redirect the request to the IdP authorization endpoint. This is the default value.\n\n\nUseExistingClientSecret (boolean) --Indicates whether to use the existing client secret when modifying a rule. If you are creating a rule, you can omit this parameter or set it to false.\n\n\n\nAuthenticateCognitoConfig (dict) --[HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify only when Type is authenticate-cognito .\n\nUserPoolArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the Amazon Cognito user pool.\n\nUserPoolClientId (string) -- [REQUIRED]The ID of the Amazon Cognito user pool client.\n\nUserPoolDomain (string) -- [REQUIRED]The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.\n\nSessionCookieName (string) --The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.\n\nScope (string) --The set of user claims to be requested from the IdP. The default is openid .\nTo verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.\n\nSessionTimeout (integer) --The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).\n\nAuthenticationRequestExtraParams (dict) --The query parameters (up to 10) to include in the redirect request to the authorization endpoint.\n\n(string) --\n(string) --\n\n\n\n\nOnUnauthenticatedRequest (string) --The behavior if the user is not authenticated. The following are possible values:\n\ndeny- Return an HTTP 401 Unauthorized error.\nallow- Allow the request to be forwarded to the target.\nauthenticate- Redirect the request to the IdP authorization endpoint. This is the default value.\n\n\n\n\nOrder (integer) --The order for the action. This value is required for rules with multiple actions. The action with the lowest value for order is performed first. The last action to be performed must be one of the following types of actions: a forward , fixed-response , or redirect .\n\nRedirectConfig (dict) --[Application Load Balancer] Information for creating a redirect action. Specify only when Type is redirect .\n\nProtocol (string) --The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.\n\nPort (string) --The port. You can specify a value from 1 to 65535 or #{port}.\n\nHost (string) --The hostname. This component is not percent-encoded. The hostname can contain #{host}.\n\nPath (string) --The absolute path, starting with the leading '/'. This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}.\n\nQuery (string) --The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading '?', as it is automatically added. You can specify any of the reserved keywords.\n\nStatusCode (string) -- [REQUIRED]The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).\n\n\n\nFixedResponseConfig (dict) --[Application Load Balancer] Information for creating an action that returns a custom HTTP response. Specify only when Type is fixed-response .\n\nMessageBody (string) --The message.\n\nStatusCode (string) -- [REQUIRED]The HTTP response code (2XX, 4XX, or 5XX).\n\nContentType (string) --The content type.\nValid Values: text/plain | text/css | text/html | application/javascript | application/json\n\n\n\nForwardConfig (dict) --Information for creating an action that distributes requests among one or more target groups. For Network Load Balancers, you can specify a single target group. Specify only when Type is forward . If you specify both ForwardConfig and TargetGroupArn , you can specify only one target group using ForwardConfig and it must be the same target group specified in TargetGroupArn .\n\nTargetGroups (list) --One or more target groups. For Network Load Balancers, you can specify a single target group.\n\n(dict) --Information about how traffic will be distributed between multiple target groups in a forward rule.\n\nTargetGroupArn (string) --The Amazon Resource Name (ARN) of the target group.\n\nWeight (integer) --The weight. The range is 0 to 999.\n\n\n\n\n\nTargetGroupStickinessConfig (dict) --The target group stickiness for the rule.\n\nEnabled (boolean) --Indicates whether target group stickiness is enabled.\n\nDurationSeconds (integer) --The time period, in seconds, during which requests from a client should be routed to the same target group. The range is 1-604800 seconds (7 days).\n\n\n\n\n\n\n\n\n

    :type AlpnPolicy: list
    :param AlpnPolicy: [TLS listeners] The name of the Application-Layer Protocol Negotiation (ALPN) policy. You can specify one policy name. The following are the possible values:\n\nHTTP1Only\nHTTP2Only\nHTTP2Optional\nHTTP2Preferred\nNone\n\nFor more information, see ALPN Policies in the Network Load Balancers Guide .\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Listeners': [
        {
            'ListenerArn': 'string',
            'LoadBalancerArn': 'string',
            'Port': 123,
            'Protocol': 'HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
            'Certificates': [
                {
                    'CertificateArn': 'string',
                    'IsDefault': True|False
                },
            ],
            'SslPolicy': 'string',
            'DefaultActions': [
                {
                    'Type': 'forward'|'authenticate-oidc'|'authenticate-cognito'|'redirect'|'fixed-response',
                    'TargetGroupArn': 'string',
                    'AuthenticateOidcConfig': {
                        'Issuer': 'string',
                        'AuthorizationEndpoint': 'string',
                        'TokenEndpoint': 'string',
                        'UserInfoEndpoint': 'string',
                        'ClientId': 'string',
                        'ClientSecret': 'string',
                        'SessionCookieName': 'string',
                        'Scope': 'string',
                        'SessionTimeout': 123,
                        'AuthenticationRequestExtraParams': {
                            'string': 'string'
                        },
                        'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate',
                        'UseExistingClientSecret': True|False
                    },
                    'AuthenticateCognitoConfig': {
                        'UserPoolArn': 'string',
                        'UserPoolClientId': 'string',
                        'UserPoolDomain': 'string',
                        'SessionCookieName': 'string',
                        'Scope': 'string',
                        'SessionTimeout': 123,
                        'AuthenticationRequestExtraParams': {
                            'string': 'string'
                        },
                        'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate'
                    },
                    'Order': 123,
                    'RedirectConfig': {
                        'Protocol': 'string',
                        'Port': 'string',
                        'Host': 'string',
                        'Path': 'string',
                        'Query': 'string',
                        'StatusCode': 'HTTP_301'|'HTTP_302'
                    },
                    'FixedResponseConfig': {
                        'MessageBody': 'string',
                        'StatusCode': 'string',
                        'ContentType': 'string'
                    },
                    'ForwardConfig': {
                        'TargetGroups': [
                            {
                                'TargetGroupArn': 'string',
                                'Weight': 123
                            },
                        ],
                        'TargetGroupStickinessConfig': {
                            'Enabled': True|False,
                            'DurationSeconds': 123
                        }
                    }
                },
            ],
            'AlpnPolicy': [
                'string',
            ]
        },
    ]
}


Response Structure

(dict) --

Listeners (list) --
Information about the listener.

(dict) --
Information about a listener.

ListenerArn (string) --
The Amazon Resource Name (ARN) of the listener.

LoadBalancerArn (string) --
The Amazon Resource Name (ARN) of the load balancer.

Port (integer) --
The port on which the load balancer is listening.

Protocol (string) --
The protocol for connections from clients to the load balancer.

Certificates (list) --
[HTTPS or TLS listener] The default certificate for the listener.

(dict) --
Information about an SSL server certificate.

CertificateArn (string) --
The Amazon Resource Name (ARN) of the certificate.

IsDefault (boolean) --
Indicates whether the certificate is the default certificate. Do not set this value when specifying a certificate as an input. This value is not included in the output when describing a listener, but is included when describing listener certificates.





SslPolicy (string) --
[HTTPS or TLS listener] The security policy that defines which protocols and ciphers are supported.

DefaultActions (list) --
The default actions for the listener.

(dict) --
Information about an action.

Type (string) --
The type of action.

TargetGroupArn (string) --
The Amazon Resource Name (ARN) of the target group. Specify only when Type is forward and you want to route to a single target group. To route to one or more target groups, use ForwardConfig instead.

AuthenticateOidcConfig (dict) --
[HTTPS listeners] Information about an identity provider that is compliant with OpenID Connect (OIDC). Specify only when Type is authenticate-oidc .

Issuer (string) --
The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

AuthorizationEndpoint (string) --
The authorization endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

TokenEndpoint (string) --
The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

UserInfoEndpoint (string) --
The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

ClientId (string) --
The OAuth 2.0 client identifier.

ClientSecret (string) --
The OAuth 2.0 client secret. This parameter is required if you are creating a rule. If you are modifying a rule, you can omit this parameter if you set UseExistingClientSecret to true.

SessionCookieName (string) --
The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.

Scope (string) --
The set of user claims to be requested from the IdP. The default is openid .
To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.

SessionTimeout (integer) --
The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).

AuthenticationRequestExtraParams (dict) --
The query parameters (up to 10) to include in the redirect request to the authorization endpoint.

(string) --
(string) --




OnUnauthenticatedRequest (string) --
The behavior if the user is not authenticated. The following are possible values:

deny- Return an HTTP 401 Unauthorized error.
allow- Allow the request to be forwarded to the target.
authenticate- Redirect the request to the IdP authorization endpoint. This is the default value.


UseExistingClientSecret (boolean) --
Indicates whether to use the existing client secret when modifying a rule. If you are creating a rule, you can omit this parameter or set it to false.



AuthenticateCognitoConfig (dict) --
[HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify only when Type is authenticate-cognito .

UserPoolArn (string) --
The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

UserPoolClientId (string) --
The ID of the Amazon Cognito user pool client.

UserPoolDomain (string) --
The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

SessionCookieName (string) --
The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.

Scope (string) --
The set of user claims to be requested from the IdP. The default is openid .
To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.

SessionTimeout (integer) --
The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).

AuthenticationRequestExtraParams (dict) --
The query parameters (up to 10) to include in the redirect request to the authorization endpoint.

(string) --
(string) --




OnUnauthenticatedRequest (string) --
The behavior if the user is not authenticated. The following are possible values:

deny- Return an HTTP 401 Unauthorized error.
allow- Allow the request to be forwarded to the target.
authenticate- Redirect the request to the IdP authorization endpoint. This is the default value.




Order (integer) --
The order for the action. This value is required for rules with multiple actions. The action with the lowest value for order is performed first. The last action to be performed must be one of the following types of actions: a forward , fixed-response , or redirect .

RedirectConfig (dict) --
[Application Load Balancer] Information for creating a redirect action. Specify only when Type is redirect .

Protocol (string) --
The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

Port (string) --
The port. You can specify a value from 1 to 65535 or #{port}.

Host (string) --
The hostname. This component is not percent-encoded. The hostname can contain #{host}.

Path (string) --
The absolute path, starting with the leading "/". This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}.

Query (string) --
The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading "?", as it is automatically added. You can specify any of the reserved keywords.

StatusCode (string) --
The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).



FixedResponseConfig (dict) --
[Application Load Balancer] Information for creating an action that returns a custom HTTP response. Specify only when Type is fixed-response .

MessageBody (string) --
The message.

StatusCode (string) --
The HTTP response code (2XX, 4XX, or 5XX).

ContentType (string) --
The content type.
Valid Values: text/plain | text/css | text/html | application/javascript | application/json



ForwardConfig (dict) --
Information for creating an action that distributes requests among one or more target groups. For Network Load Balancers, you can specify a single target group. Specify only when Type is forward . If you specify both ForwardConfig and TargetGroupArn , you can specify only one target group using ForwardConfig and it must be the same target group specified in TargetGroupArn .

TargetGroups (list) --
One or more target groups. For Network Load Balancers, you can specify a single target group.

(dict) --
Information about how traffic will be distributed between multiple target groups in a forward rule.

TargetGroupArn (string) --
The Amazon Resource Name (ARN) of the target group.

Weight (integer) --
The weight. The range is 0 to 999.





TargetGroupStickinessConfig (dict) --
The target group stickiness for the rule.

Enabled (boolean) --
Indicates whether target group stickiness is enabled.

DurationSeconds (integer) --
The time period, in seconds, during which requests from a client should be routed to the same target group. The range is 1-604800 seconds (7 days).









AlpnPolicy (list) --
[TLS listener] The name of the Application-Layer Protocol Negotiation (ALPN) policy.

(string) --












Exceptions

ElasticLoadBalancingv2.Client.exceptions.DuplicateListenerException
ElasticLoadBalancingv2.Client.exceptions.TooManyListenersException
ElasticLoadBalancingv2.Client.exceptions.TooManyCertificatesException
ElasticLoadBalancingv2.Client.exceptions.LoadBalancerNotFoundException
ElasticLoadBalancingv2.Client.exceptions.TargetGroupNotFoundException
ElasticLoadBalancingv2.Client.exceptions.TargetGroupAssociationLimitException
ElasticLoadBalancingv2.Client.exceptions.InvalidConfigurationRequestException
ElasticLoadBalancingv2.Client.exceptions.IncompatibleProtocolsException
ElasticLoadBalancingv2.Client.exceptions.SSLPolicyNotFoundException
ElasticLoadBalancingv2.Client.exceptions.CertificateNotFoundException
ElasticLoadBalancingv2.Client.exceptions.UnsupportedProtocolException
ElasticLoadBalancingv2.Client.exceptions.TooManyRegistrationsForTargetIdException
ElasticLoadBalancingv2.Client.exceptions.TooManyTargetsException
ElasticLoadBalancingv2.Client.exceptions.TooManyActionsException
ElasticLoadBalancingv2.Client.exceptions.InvalidLoadBalancerActionException
ElasticLoadBalancingv2.Client.exceptions.TooManyUniqueTargetGroupsPerLoadBalancerException
ElasticLoadBalancingv2.Client.exceptions.ALPNPolicyNotSupportedException

Examples
This example creates an HTTP listener for the specified load balancer that forwards requests to the specified target group.
response = client.create_listener(
    DefaultActions=[
        {
            'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
            'Type': 'forward',
        },
    ],
    LoadBalancerArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
    Port=80,
    Protocol='HTTP',
)

print(response)


Expected Output:
{
    'Listeners': [
        {
            'DefaultActions': [
                {
                    'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
                    'Type': 'forward',
                },
            ],
            'ListenerArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2',
            'LoadBalancerArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
            'Port': 80,
            'Protocol': 'HTTP',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}


This example creates an HTTPS listener for the specified load balancer that forwards requests to the specified target group. Note that you must specify an SSL certificate for an HTTPS listener. You can create and manage certificates using AWS Certificate Manager (ACM). Alternatively, you can create a certificate using SSL/TLS tools, get the certificate signed by a certificate authority (CA), and upload the certificate to AWS Identity and Access Management (IAM).
response = client.create_listener(
    Certificates=[
        {
            'CertificateArn': 'arn:aws:iam::123456789012:server-certificate/my-server-cert',
        },
    ],
    DefaultActions=[
        {
            'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
            'Type': 'forward',
        },
    ],
    LoadBalancerArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
    Port=443,
    Protocol='HTTPS',
    SslPolicy='ELBSecurityPolicy-2015-05',
)

print(response)


Expected Output:
{
    'Listeners': [
        {
            'Certificates': [
                {
                    'CertificateArn': 'arn:aws:iam::123456789012:server-certificate/my-server-cert',
                },
            ],
            'DefaultActions': [
                {
                    'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
                    'Type': 'forward',
                },
            ],
            'ListenerArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2',
            'LoadBalancerArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
            'Port': 443,
            'Protocol': 'HTTPS',
            'SslPolicy': 'ELBSecurityPolicy-2015-05',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Listeners': [
            {
                'ListenerArn': 'string',
                'LoadBalancerArn': 'string',
                'Port': 123,
                'Protocol': 'HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
                'Certificates': [
                    {
                        'CertificateArn': 'string',
                        'IsDefault': True|False
                    },
                ],
                'SslPolicy': 'string',
                'DefaultActions': [
                    {
                        'Type': 'forward'|'authenticate-oidc'|'authenticate-cognito'|'redirect'|'fixed-response',
                        'TargetGroupArn': 'string',
                        'AuthenticateOidcConfig': {
                            'Issuer': 'string',
                            'AuthorizationEndpoint': 'string',
                            'TokenEndpoint': 'string',
                            'UserInfoEndpoint': 'string',
                            'ClientId': 'string',
                            'ClientSecret': 'string',
                            'SessionCookieName': 'string',
                            'Scope': 'string',
                            'SessionTimeout': 123,
                            'AuthenticationRequestExtraParams': {
                                'string': 'string'
                            },
                            'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate',
                            'UseExistingClientSecret': True|False
                        },
                        'AuthenticateCognitoConfig': {
                            'UserPoolArn': 'string',
                            'UserPoolClientId': 'string',
                            'UserPoolDomain': 'string',
                            'SessionCookieName': 'string',
                            'Scope': 'string',
                            'SessionTimeout': 123,
                            'AuthenticationRequestExtraParams': {
                                'string': 'string'
                            },
                            'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate'
                        },
                        'Order': 123,
                        'RedirectConfig': {
                            'Protocol': 'string',
                            'Port': 'string',
                            'Host': 'string',
                            'Path': 'string',
                            'Query': 'string',
                            'StatusCode': 'HTTP_301'|'HTTP_302'
                        },
                        'FixedResponseConfig': {
                            'MessageBody': 'string',
                            'StatusCode': 'string',
                            'ContentType': 'string'
                        },
                        'ForwardConfig': {
                            'TargetGroups': [
                                {
                                    'TargetGroupArn': 'string',
                                    'Weight': 123
                                },
                            ],
                            'TargetGroupStickinessConfig': {
                                'Enabled': True|False,
                                'DurationSeconds': 123
                            }
                        }
                    },
                ],
                'AlpnPolicy': [
                    'string',
                ]
            },
        ]
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def create_load_balancer(Name=None, Subnets=None, SubnetMappings=None, SecurityGroups=None, Scheme=None, Tags=None, Type=None, IpAddressType=None):
    """
    Creates an Application Load Balancer or a Network Load Balancer.
    When you create a load balancer, you can specify security groups, public subnets, IP address type, and tags. Otherwise, you could do so later using  SetSecurityGroups ,  SetSubnets ,  SetIpAddressType , and  AddTags .
    To create listeners for your load balancer, use  CreateListener . To describe your current load balancers, see  DescribeLoadBalancers . When you are finished with a load balancer, you can delete it using  DeleteLoadBalancer .
    For limit information, see Limits for Your Application Load Balancer in the Application Load Balancers Guide and Limits for Your Network Load Balancer in the Network Load Balancers Guide .
    This operation is idempotent, which means that it completes at most one time. If you attempt to create multiple load balancers with the same settings, each call succeeds.
    For more information, see Application Load Balancers in the Application Load Balancers Guide and Network Load Balancers in the Network Load Balancers Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example creates an Internet-facing load balancer and enables the Availability Zones for the specified subnets.
    Expected Output:
    This example creates an internal load balancer and enables the Availability Zones for the specified subnets.
    Expected Output:
    
    :example: response = client.create_load_balancer(
        Name='string',
        Subnets=[
            'string',
        ],
        SubnetMappings=[
            {
                'SubnetId': 'string',
                'AllocationId': 'string',
                'PrivateIPv4Address': 'string'
            },
        ],
        SecurityGroups=[
            'string',
        ],
        Scheme='internet-facing'|'internal',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        Type='application'|'network',
        IpAddressType='ipv4'|'dualstack'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the load balancer.\nThis name must be unique per region per account, can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, must not begin or end with a hyphen, and must not begin with 'internal-'.\n

    :type Subnets: list
    :param Subnets: The IDs of the public subnets. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings.\n[Application Load Balancers] You must specify subnets from at least two Availability Zones.\n[Network Load Balancers] You can specify subnets from one or more Availability Zones.\n\n(string) --\n\n

    :type SubnetMappings: list
    :param SubnetMappings: The IDs of the public subnets. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings.\n[Application Load Balancers] You must specify subnets from at least two Availability Zones. You cannot specify Elastic IP addresses for your subnets.\n[Network Load Balancers] You can specify subnets from one or more Availability Zones. You can specify one Elastic IP address per subnet if you need static IP addresses for your internet-facing load balancer. For internal load balancers, you can specify one private IP address per subnet from the IPv4 range of the subnet.\n\n(dict) --Information about a subnet mapping.\n\nSubnetId (string) --The ID of the subnet.\n\nAllocationId (string) --[Network Load Balancers] The allocation ID of the Elastic IP address for an internet-facing load balancer.\n\nPrivateIPv4Address (string) --[Network Load Balancers] The private IPv4 address for an internal load balancer.\n\n\n\n\n

    :type SecurityGroups: list
    :param SecurityGroups: [Application Load Balancers] The IDs of the security groups for the load balancer.\n\n(string) --\n\n

    :type Scheme: string
    :param Scheme: The nodes of an Internet-facing load balancer have public IP addresses. The DNS name of an Internet-facing load balancer is publicly resolvable to the public IP addresses of the nodes. Therefore, Internet-facing load balancers can route requests from clients over the internet.\nThe nodes of an internal load balancer have only private IP addresses. The DNS name of an internal load balancer is publicly resolvable to the private IP addresses of the nodes. Therefore, internal load balancers can route requests only from clients with access to the VPC for the load balancer.\nThe default is an Internet-facing load balancer.\n

    :type Tags: list
    :param Tags: One or more tags to assign to the load balancer.\n\n(dict) --Information about a tag.\n\nKey (string) -- [REQUIRED]The key of the tag.\n\nValue (string) --The value of the tag.\n\n\n\n\n

    :type Type: string
    :param Type: The type of load balancer. The default is application .

    :type IpAddressType: string
    :param IpAddressType: [Application Load Balancers] The type of IP addresses used by the subnets for your load balancer. The possible values are ipv4 (for IPv4 addresses) and dualstack (for IPv4 and IPv6 addresses). Internal load balancers must use ipv4 .

    :rtype: dict

ReturnsResponse Syntax
{
    'LoadBalancers': [
        {
            'LoadBalancerArn': 'string',
            'DNSName': 'string',
            'CanonicalHostedZoneId': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'LoadBalancerName': 'string',
            'Scheme': 'internet-facing'|'internal',
            'VpcId': 'string',
            'State': {
                'Code': 'active'|'provisioning'|'active_impaired'|'failed',
                'Reason': 'string'
            },
            'Type': 'application'|'network',
            'AvailabilityZones': [
                {
                    'ZoneName': 'string',
                    'SubnetId': 'string',
                    'LoadBalancerAddresses': [
                        {
                            'IpAddress': 'string',
                            'AllocationId': 'string',
                            'PrivateIPv4Address': 'string'
                        },
                    ]
                },
            ],
            'SecurityGroups': [
                'string',
            ],
            'IpAddressType': 'ipv4'|'dualstack'
        },
    ]
}


Response Structure

(dict) --

LoadBalancers (list) --
Information about the load balancer.

(dict) --
Information about a load balancer.

LoadBalancerArn (string) --
The Amazon Resource Name (ARN) of the load balancer.

DNSName (string) --
The public DNS name of the load balancer.

CanonicalHostedZoneId (string) --
The ID of the Amazon Route 53 hosted zone associated with the load balancer.

CreatedTime (datetime) --
The date and time the load balancer was created.

LoadBalancerName (string) --
The name of the load balancer.

Scheme (string) --
The nodes of an Internet-facing load balancer have public IP addresses. The DNS name of an Internet-facing load balancer is publicly resolvable to the public IP addresses of the nodes. Therefore, Internet-facing load balancers can route requests from clients over the internet.
The nodes of an internal load balancer have only private IP addresses. The DNS name of an internal load balancer is publicly resolvable to the private IP addresses of the nodes. Therefore, internal load balancers can route requests only from clients with access to the VPC for the load balancer.

VpcId (string) --
The ID of the VPC for the load balancer.

State (dict) --
The state of the load balancer.

Code (string) --
The state code. The initial state of the load balancer is provisioning . After the load balancer is fully set up and ready to route traffic, its state is active . If the load balancer could not be set up, its state is failed .

Reason (string) --
A description of the state.



Type (string) --
The type of load balancer.

AvailabilityZones (list) --
The Availability Zones for the load balancer.

(dict) --
Information about an Availability Zone.

ZoneName (string) --
The name of the Availability Zone.

SubnetId (string) --
The ID of the subnet. You can specify one subnet per Availability Zone.

LoadBalancerAddresses (list) --
[Network Load Balancers] If you need static IP addresses for your load balancer, you can specify one Elastic IP address per Availability Zone when you create an internal-facing load balancer. For internal load balancers, you can specify a private IP address from the IPv4 range of the subnet.

(dict) --
Information about a static IP address for a load balancer.

IpAddress (string) --
The static IP address.

AllocationId (string) --
[Network Load Balancers] The allocation ID of the Elastic IP address for an internal-facing load balancer.

PrivateIPv4Address (string) --
[Network Load Balancers] The private IPv4 address for an internal load balancer.









SecurityGroups (list) --
The IDs of the security groups for the load balancer.

(string) --


IpAddressType (string) --
The type of IP addresses used by the subnets for your load balancer. The possible values are ipv4 (for IPv4 addresses) and dualstack (for IPv4 and IPv6 addresses).











Exceptions

ElasticLoadBalancingv2.Client.exceptions.DuplicateLoadBalancerNameException
ElasticLoadBalancingv2.Client.exceptions.TooManyLoadBalancersException
ElasticLoadBalancingv2.Client.exceptions.InvalidConfigurationRequestException
ElasticLoadBalancingv2.Client.exceptions.SubnetNotFoundException
ElasticLoadBalancingv2.Client.exceptions.InvalidSubnetException
ElasticLoadBalancingv2.Client.exceptions.InvalidSecurityGroupException
ElasticLoadBalancingv2.Client.exceptions.InvalidSchemeException
ElasticLoadBalancingv2.Client.exceptions.TooManyTagsException
ElasticLoadBalancingv2.Client.exceptions.DuplicateTagKeysException
ElasticLoadBalancingv2.Client.exceptions.ResourceInUseException
ElasticLoadBalancingv2.Client.exceptions.AllocationIdNotFoundException
ElasticLoadBalancingv2.Client.exceptions.AvailabilityZoneNotSupportedException
ElasticLoadBalancingv2.Client.exceptions.OperationNotPermittedException

Examples
This example creates an Internet-facing load balancer and enables the Availability Zones for the specified subnets.
response = client.create_load_balancer(
    Name='my-load-balancer',
    Subnets=[
        'subnet-b7d581c0',
        'subnet-8360a9e7',
    ],
)

print(response)


Expected Output:
{
    'LoadBalancers': [
        {
            'AvailabilityZones': [
                {
                    'SubnetId': 'subnet-8360a9e7',
                    'ZoneName': 'us-west-2a',
                },
                {
                    'SubnetId': 'subnet-b7d581c0',
                    'ZoneName': 'us-west-2b',
                },
            ],
            'CanonicalHostedZoneId': 'Z2P70J7EXAMPLE',
            'CreatedTime': datetime(2016, 3, 25, 21, 26, 12, 4, 85, 0),
            'DNSName': 'my-load-balancer-424835706.us-west-2.elb.amazonaws.com',
            'LoadBalancerArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
            'LoadBalancerName': 'my-load-balancer',
            'Scheme': 'internet-facing',
            'SecurityGroups': [
                'sg-5943793c',
            ],
            'State': {
                'Code': 'provisioning',
            },
            'Type': 'application',
            'VpcId': 'vpc-3ac0fb5f',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}


This example creates an internal load balancer and enables the Availability Zones for the specified subnets.
response = client.create_load_balancer(
    Name='my-internal-load-balancer',
    Scheme='internal',
    SecurityGroups=[
    ],
    Subnets=[
        'subnet-b7d581c0',
        'subnet-8360a9e7',
    ],
)

print(response)


Expected Output:
{
    'LoadBalancers': [
        {
            'AvailabilityZones': [
                {
                    'SubnetId': 'subnet-8360a9e7',
                    'ZoneName': 'us-west-2a',
                },
                {
                    'SubnetId': 'subnet-b7d581c0',
                    'ZoneName': 'us-west-2b',
                },
            ],
            'CanonicalHostedZoneId': 'Z2P70J7EXAMPLE',
            'CreatedTime': datetime(2016, 3, 25, 21, 29, 48, 4, 85, 0),
            'DNSName': 'internal-my-internal-load-balancer-1529930873.us-west-2.elb.amazonaws.com',
            'LoadBalancerArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-internal-load-balancer/5b49b8d4303115c2',
            'LoadBalancerName': 'my-internal-load-balancer',
            'Scheme': 'internal',
            'SecurityGroups': [
                'sg-5943793c',
            ],
            'State': {
                'Code': 'provisioning',
            },
            'Type': 'application',
            'VpcId': 'vpc-3ac0fb5f',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'LoadBalancers': [
            {
                'LoadBalancerArn': 'string',
                'DNSName': 'string',
                'CanonicalHostedZoneId': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'LoadBalancerName': 'string',
                'Scheme': 'internet-facing'|'internal',
                'VpcId': 'string',
                'State': {
                    'Code': 'active'|'provisioning'|'active_impaired'|'failed',
                    'Reason': 'string'
                },
                'Type': 'application'|'network',
                'AvailabilityZones': [
                    {
                        'ZoneName': 'string',
                        'SubnetId': 'string',
                        'LoadBalancerAddresses': [
                            {
                                'IpAddress': 'string',
                                'AllocationId': 'string',
                                'PrivateIPv4Address': 'string'
                            },
                        ]
                    },
                ],
                'SecurityGroups': [
                    'string',
                ],
                'IpAddressType': 'ipv4'|'dualstack'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_rule(ListenerArn=None, Conditions=None, Priority=None, Actions=None):
    """
    Creates a rule for the specified listener. The listener must be associated with an Application Load Balancer.
    Rules are evaluated in priority order, from the lowest value to the highest value. When the conditions for a rule are met, its actions are performed. If the conditions for no rules are met, the actions for the default rule are performed. For more information, see Listener Rules in the Application Load Balancers Guide .
    To view your current rules, use  DescribeRules . To update a rule, use  ModifyRule . To set the priorities of your rules, use  SetRulePriorities . To delete a rule, use  DeleteRule .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example creates a rule that forwards requests to the specified target group if the URL contains the specified pattern (for example, /img/*).
    Expected Output:
    
    :example: response = client.create_rule(
        ListenerArn='string',
        Conditions=[
            {
                'Field': 'string',
                'Values': [
                    'string',
                ],
                'HostHeaderConfig': {
                    'Values': [
                        'string',
                    ]
                },
                'PathPatternConfig': {
                    'Values': [
                        'string',
                    ]
                },
                'HttpHeaderConfig': {
                    'HttpHeaderName': 'string',
                    'Values': [
                        'string',
                    ]
                },
                'QueryStringConfig': {
                    'Values': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ]
                },
                'HttpRequestMethodConfig': {
                    'Values': [
                        'string',
                    ]
                },
                'SourceIpConfig': {
                    'Values': [
                        'string',
                    ]
                }
            },
        ],
        Priority=123,
        Actions=[
            {
                'Type': 'forward'|'authenticate-oidc'|'authenticate-cognito'|'redirect'|'fixed-response',
                'TargetGroupArn': 'string',
                'AuthenticateOidcConfig': {
                    'Issuer': 'string',
                    'AuthorizationEndpoint': 'string',
                    'TokenEndpoint': 'string',
                    'UserInfoEndpoint': 'string',
                    'ClientId': 'string',
                    'ClientSecret': 'string',
                    'SessionCookieName': 'string',
                    'Scope': 'string',
                    'SessionTimeout': 123,
                    'AuthenticationRequestExtraParams': {
                        'string': 'string'
                    },
                    'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate',
                    'UseExistingClientSecret': True|False
                },
                'AuthenticateCognitoConfig': {
                    'UserPoolArn': 'string',
                    'UserPoolClientId': 'string',
                    'UserPoolDomain': 'string',
                    'SessionCookieName': 'string',
                    'Scope': 'string',
                    'SessionTimeout': 123,
                    'AuthenticationRequestExtraParams': {
                        'string': 'string'
                    },
                    'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate'
                },
                'Order': 123,
                'RedirectConfig': {
                    'Protocol': 'string',
                    'Port': 'string',
                    'Host': 'string',
                    'Path': 'string',
                    'Query': 'string',
                    'StatusCode': 'HTTP_301'|'HTTP_302'
                },
                'FixedResponseConfig': {
                    'MessageBody': 'string',
                    'StatusCode': 'string',
                    'ContentType': 'string'
                },
                'ForwardConfig': {
                    'TargetGroups': [
                        {
                            'TargetGroupArn': 'string',
                            'Weight': 123
                        },
                    ],
                    'TargetGroupStickinessConfig': {
                        'Enabled': True|False,
                        'DurationSeconds': 123
                    }
                }
            },
        ]
    )
    
    
    :type ListenerArn: string
    :param ListenerArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the listener.\n

    :type Conditions: list
    :param Conditions: [REQUIRED]\nThe conditions. Each rule can include zero or one of the following conditions: http-request-method , host-header , path-pattern , and source-ip , and zero or more of the following conditions: http-header and query-string .\n\n(dict) --Information about a condition for a rule.\n\nField (string) --The field in the HTTP request. The following are the possible values:\n\nhttp-header\nhttp-request-method\nhost-header\npath-pattern\nquery-string\nsource-ip\n\n\nValues (list) --The condition value. You can use Values if the rule contains only host-header and path-pattern conditions. Otherwise, you can use HostHeaderConfig for host-header conditions and PathPatternConfig for path-pattern conditions.\nIf Field is host-header , you can specify a single host name (for example, my.example.com). A host name is case insensitive, can be up to 128 characters in length, and can contain any of the following characters.\n\nA-Z, a-z, 0-9\n\n.\n\n\n\n(matches 0 or more characters)\n\n\n? (matches exactly 1 character)\n\nIf Field is path-pattern , you can specify a single path pattern (for example, /img/*). A path pattern is case-sensitive, can be up to 128 characters in length, and can contain any of the following characters.\n\nA-Z, a-z, 0-9\n_ - . $ / ~ ' \' @ : +\n& (using &amp;)\n\n(matches 0 or more characters)\n\n\n? (matches exactly 1 character)\n\n\n(string) --\n\n\nHostHeaderConfig (dict) --Information for a host header condition. Specify only when Field is host-header .\n\nValues (list) --One or more host names. The maximum size of each name is 128 characters. The comparison is case insensitive. The following wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly 1 character).\nIf you specify multiple strings, the condition is satisfied if one of the strings matches the host name.\n\n(string) --\n\n\n\n\nPathPatternConfig (dict) --Information for a path pattern condition. Specify only when Field is path-pattern .\n\nValues (list) --One or more path patterns to compare against the request URL. The maximum size of each string is 128 characters. The comparison is case sensitive. The following wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly 1 character).\nIf you specify multiple strings, the condition is satisfied if one of them matches the request URL. The path pattern is compared only to the path of the URL, not to its query string. To compare against the query string, use QueryStringConditionConfig .\n\n(string) --\n\n\n\n\nHttpHeaderConfig (dict) --Information for an HTTP header condition. Specify only when Field is http-header .\n\nHttpHeaderName (string) --The name of the HTTP header field. The maximum size is 40 characters. The header name is case insensitive. The allowed characters are specified by RFC 7230. Wildcards are not supported.\nYou can\'t use an HTTP header condition to specify the host header. Use HostHeaderConditionConfig to specify a host header condition.\n\nValues (list) --One or more strings to compare against the value of the HTTP header. The maximum size of each string is 128 characters. The comparison strings are case insensitive. The following wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly 1 character).\nIf the same header appears multiple times in the request, we search them in order until a match is found.\nIf you specify multiple strings, the condition is satisfied if one of the strings matches the value of the HTTP header. To require that all of the strings are a match, create one condition per string.\n\n(string) --\n\n\n\n\nQueryStringConfig (dict) --Information for a query string condition. Specify only when Field is query-string .\n\nValues (list) --One or more key/value pairs or values to find in the query string. The maximum size of each string is 128 characters. The comparison is case insensitive. The following wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly 1 character). To search for a literal \'*\' or \'?\' character in a query string, you must escape these characters in Values using a \'\' character.\nIf you specify multiple key/value pairs or values, the condition is satisfied if one of them is found in the query string.\n\n(dict) --Information about a key/value pair.\n\nKey (string) --The key. You can omit the key.\n\nValue (string) --The value.\n\n\n\n\n\n\n\nHttpRequestMethodConfig (dict) --Information for an HTTP method condition. Specify only when Field is http-request-method .\n\nValues (list) --The name of the request method. The maximum size is 40 characters. The allowed characters are A-Z, hyphen (-), and underscore (_). The comparison is case sensitive. Wildcards are not supported; therefore, the method name must be an exact match.\nIf you specify multiple strings, the condition is satisfied if one of the strings matches the HTTP request method. We recommend that you route GET and HEAD requests in the same way, because the response to a HEAD request may be cached.\n\n(string) --\n\n\n\n\nSourceIpConfig (dict) --Information for a source IP condition. Specify only when Field is source-ip .\n\nValues (list) --One or more source IP addresses, in CIDR format. You can use both IPv4 and IPv6 addresses. Wildcards are not supported.\nIf you specify multiple addresses, the condition is satisfied if the source IP address of the request matches one of the CIDR blocks. This condition is not satisfied by the addresses in the X-Forwarded-For header. To search for addresses in the X-Forwarded-For header, use HttpHeaderConditionConfig .\n\n(string) --\n\n\n\n\n\n\n\n

    :type Priority: integer
    :param Priority: [REQUIRED]\nThe rule priority. A listener can\'t have multiple rules with the same priority.\n

    :type Actions: list
    :param Actions: [REQUIRED]\nThe actions. Each rule must include exactly one of the following types of actions: forward , fixed-response , or redirect , and it must be the last action to be performed.\nIf the action type is forward , you specify one or more target groups. The protocol of the target group must be HTTP or HTTPS for an Application Load Balancer. The protocol of the target group must be TCP, TLS, UDP, or TCP_UDP for a Network Load Balancer.\n[HTTPS listeners] If the action type is authenticate-oidc , you authenticate users through an identity provider that is OpenID Connect (OIDC) compliant.\n[HTTPS listeners] If the action type is authenticate-cognito , you authenticate users through the user pools supported by Amazon Cognito.\n[Application Load Balancer] If the action type is redirect , you redirect specified client requests from one URL to another.\n[Application Load Balancer] If the action type is fixed-response , you drop specified client requests and return a custom HTTP response.\n\n(dict) --Information about an action.\n\nType (string) -- [REQUIRED]The type of action.\n\nTargetGroupArn (string) --The Amazon Resource Name (ARN) of the target group. Specify only when Type is forward and you want to route to a single target group. To route to one or more target groups, use ForwardConfig instead.\n\nAuthenticateOidcConfig (dict) --[HTTPS listeners] Information about an identity provider that is compliant with OpenID Connect (OIDC). Specify only when Type is authenticate-oidc .\n\nIssuer (string) -- [REQUIRED]The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.\n\nAuthorizationEndpoint (string) -- [REQUIRED]The authorization endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.\n\nTokenEndpoint (string) -- [REQUIRED]The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.\n\nUserInfoEndpoint (string) -- [REQUIRED]The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.\n\nClientId (string) -- [REQUIRED]The OAuth 2.0 client identifier.\n\nClientSecret (string) --The OAuth 2.0 client secret. This parameter is required if you are creating a rule. If you are modifying a rule, you can omit this parameter if you set UseExistingClientSecret to true.\n\nSessionCookieName (string) --The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.\n\nScope (string) --The set of user claims to be requested from the IdP. The default is openid .\nTo verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.\n\nSessionTimeout (integer) --The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).\n\nAuthenticationRequestExtraParams (dict) --The query parameters (up to 10) to include in the redirect request to the authorization endpoint.\n\n(string) --\n(string) --\n\n\n\n\nOnUnauthenticatedRequest (string) --The behavior if the user is not authenticated. The following are possible values:\n\ndeny- Return an HTTP 401 Unauthorized error.\nallow- Allow the request to be forwarded to the target.\nauthenticate- Redirect the request to the IdP authorization endpoint. This is the default value.\n\n\nUseExistingClientSecret (boolean) --Indicates whether to use the existing client secret when modifying a rule. If you are creating a rule, you can omit this parameter or set it to false.\n\n\n\nAuthenticateCognitoConfig (dict) --[HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify only when Type is authenticate-cognito .\n\nUserPoolArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the Amazon Cognito user pool.\n\nUserPoolClientId (string) -- [REQUIRED]The ID of the Amazon Cognito user pool client.\n\nUserPoolDomain (string) -- [REQUIRED]The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.\n\nSessionCookieName (string) --The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.\n\nScope (string) --The set of user claims to be requested from the IdP. The default is openid .\nTo verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.\n\nSessionTimeout (integer) --The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).\n\nAuthenticationRequestExtraParams (dict) --The query parameters (up to 10) to include in the redirect request to the authorization endpoint.\n\n(string) --\n(string) --\n\n\n\n\nOnUnauthenticatedRequest (string) --The behavior if the user is not authenticated. The following are possible values:\n\ndeny- Return an HTTP 401 Unauthorized error.\nallow- Allow the request to be forwarded to the target.\nauthenticate- Redirect the request to the IdP authorization endpoint. This is the default value.\n\n\n\n\nOrder (integer) --The order for the action. This value is required for rules with multiple actions. The action with the lowest value for order is performed first. The last action to be performed must be one of the following types of actions: a forward , fixed-response , or redirect .\n\nRedirectConfig (dict) --[Application Load Balancer] Information for creating a redirect action. Specify only when Type is redirect .\n\nProtocol (string) --The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.\n\nPort (string) --The port. You can specify a value from 1 to 65535 or #{port}.\n\nHost (string) --The hostname. This component is not percent-encoded. The hostname can contain #{host}.\n\nPath (string) --The absolute path, starting with the leading '/'. This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}.\n\nQuery (string) --The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading '?', as it is automatically added. You can specify any of the reserved keywords.\n\nStatusCode (string) -- [REQUIRED]The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).\n\n\n\nFixedResponseConfig (dict) --[Application Load Balancer] Information for creating an action that returns a custom HTTP response. Specify only when Type is fixed-response .\n\nMessageBody (string) --The message.\n\nStatusCode (string) -- [REQUIRED]The HTTP response code (2XX, 4XX, or 5XX).\n\nContentType (string) --The content type.\nValid Values: text/plain | text/css | text/html | application/javascript | application/json\n\n\n\nForwardConfig (dict) --Information for creating an action that distributes requests among one or more target groups. For Network Load Balancers, you can specify a single target group. Specify only when Type is forward . If you specify both ForwardConfig and TargetGroupArn , you can specify only one target group using ForwardConfig and it must be the same target group specified in TargetGroupArn .\n\nTargetGroups (list) --One or more target groups. For Network Load Balancers, you can specify a single target group.\n\n(dict) --Information about how traffic will be distributed between multiple target groups in a forward rule.\n\nTargetGroupArn (string) --The Amazon Resource Name (ARN) of the target group.\n\nWeight (integer) --The weight. The range is 0 to 999.\n\n\n\n\n\nTargetGroupStickinessConfig (dict) --The target group stickiness for the rule.\n\nEnabled (boolean) --Indicates whether target group stickiness is enabled.\n\nDurationSeconds (integer) --The time period, in seconds, during which requests from a client should be routed to the same target group. The range is 1-604800 seconds (7 days).\n\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Rules': [
        {
            'RuleArn': 'string',
            'Priority': 'string',
            'Conditions': [
                {
                    'Field': 'string',
                    'Values': [
                        'string',
                    ],
                    'HostHeaderConfig': {
                        'Values': [
                            'string',
                        ]
                    },
                    'PathPatternConfig': {
                        'Values': [
                            'string',
                        ]
                    },
                    'HttpHeaderConfig': {
                        'HttpHeaderName': 'string',
                        'Values': [
                            'string',
                        ]
                    },
                    'QueryStringConfig': {
                        'Values': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                    'HttpRequestMethodConfig': {
                        'Values': [
                            'string',
                        ]
                    },
                    'SourceIpConfig': {
                        'Values': [
                            'string',
                        ]
                    }
                },
            ],
            'Actions': [
                {
                    'Type': 'forward'|'authenticate-oidc'|'authenticate-cognito'|'redirect'|'fixed-response',
                    'TargetGroupArn': 'string',
                    'AuthenticateOidcConfig': {
                        'Issuer': 'string',
                        'AuthorizationEndpoint': 'string',
                        'TokenEndpoint': 'string',
                        'UserInfoEndpoint': 'string',
                        'ClientId': 'string',
                        'ClientSecret': 'string',
                        'SessionCookieName': 'string',
                        'Scope': 'string',
                        'SessionTimeout': 123,
                        'AuthenticationRequestExtraParams': {
                            'string': 'string'
                        },
                        'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate',
                        'UseExistingClientSecret': True|False
                    },
                    'AuthenticateCognitoConfig': {
                        'UserPoolArn': 'string',
                        'UserPoolClientId': 'string',
                        'UserPoolDomain': 'string',
                        'SessionCookieName': 'string',
                        'Scope': 'string',
                        'SessionTimeout': 123,
                        'AuthenticationRequestExtraParams': {
                            'string': 'string'
                        },
                        'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate'
                    },
                    'Order': 123,
                    'RedirectConfig': {
                        'Protocol': 'string',
                        'Port': 'string',
                        'Host': 'string',
                        'Path': 'string',
                        'Query': 'string',
                        'StatusCode': 'HTTP_301'|'HTTP_302'
                    },
                    'FixedResponseConfig': {
                        'MessageBody': 'string',
                        'StatusCode': 'string',
                        'ContentType': 'string'
                    },
                    'ForwardConfig': {
                        'TargetGroups': [
                            {
                                'TargetGroupArn': 'string',
                                'Weight': 123
                            },
                        ],
                        'TargetGroupStickinessConfig': {
                            'Enabled': True|False,
                            'DurationSeconds': 123
                        }
                    }
                },
            ],
            'IsDefault': True|False
        },
    ]
}


Response Structure

(dict) --

Rules (list) --
Information about the rule.

(dict) --
Information about a rule.

RuleArn (string) --
The Amazon Resource Name (ARN) of the rule.

Priority (string) --
The priority.

Conditions (list) --
The conditions. Each rule can include zero or one of the following conditions: http-request-method , host-header , path-pattern , and source-ip , and zero or more of the following conditions: http-header and query-string .

(dict) --
Information about a condition for a rule.

Field (string) --
The field in the HTTP request. The following are the possible values:

http-header
http-request-method
host-header
path-pattern
query-string
source-ip


Values (list) --
The condition value. You can use Values if the rule contains only host-header and path-pattern conditions. Otherwise, you can use HostHeaderConfig for host-header conditions and PathPatternConfig for path-pattern conditions.
If Field is host-header , you can specify a single host name (for example, my.example.com). A host name is case insensitive, can be up to 128 characters in length, and can contain any of the following characters.

A-Z, a-z, 0-9

.



(matches 0 or more characters)


? (matches exactly 1 character)

If Field is path-pattern , you can specify a single path pattern (for example, /img/*). A path pattern is case-sensitive, can be up to 128 characters in length, and can contain any of the following characters.

A-Z, a-z, 0-9
_ - . $ / ~ " \' @ : +
& (using &amp;)

(matches 0 or more characters)


? (matches exactly 1 character)


(string) --


HostHeaderConfig (dict) --
Information for a host header condition. Specify only when Field is host-header .

Values (list) --
One or more host names. The maximum size of each name is 128 characters. The comparison is case insensitive. The following wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly 1 character).
If you specify multiple strings, the condition is satisfied if one of the strings matches the host name.

(string) --




PathPatternConfig (dict) --
Information for a path pattern condition. Specify only when Field is path-pattern .

Values (list) --
One or more path patterns to compare against the request URL. The maximum size of each string is 128 characters. The comparison is case sensitive. The following wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly 1 character).
If you specify multiple strings, the condition is satisfied if one of them matches the request URL. The path pattern is compared only to the path of the URL, not to its query string. To compare against the query string, use  QueryStringConditionConfig .

(string) --




HttpHeaderConfig (dict) --
Information for an HTTP header condition. Specify only when Field is http-header .

HttpHeaderName (string) --
The name of the HTTP header field. The maximum size is 40 characters. The header name is case insensitive. The allowed characters are specified by RFC 7230. Wildcards are not supported.
You can\'t use an HTTP header condition to specify the host header. Use  HostHeaderConditionConfig to specify a host header condition.

Values (list) --
One or more strings to compare against the value of the HTTP header. The maximum size of each string is 128 characters. The comparison strings are case insensitive. The following wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly 1 character).
If the same header appears multiple times in the request, we search them in order until a match is found.
If you specify multiple strings, the condition is satisfied if one of the strings matches the value of the HTTP header. To require that all of the strings are a match, create one condition per string.

(string) --




QueryStringConfig (dict) --
Information for a query string condition. Specify only when Field is query-string .

Values (list) --
One or more key/value pairs or values to find in the query string. The maximum size of each string is 128 characters. The comparison is case insensitive. The following wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly 1 character). To search for a literal \'*\' or \'?\' character in a query string, you must escape these characters in Values using a \'\' character.
If you specify multiple key/value pairs or values, the condition is satisfied if one of them is found in the query string.

(dict) --
Information about a key/value pair.

Key (string) --
The key. You can omit the key.

Value (string) --
The value.







HttpRequestMethodConfig (dict) --
Information for an HTTP method condition. Specify only when Field is http-request-method .

Values (list) --
The name of the request method. The maximum size is 40 characters. The allowed characters are A-Z, hyphen (-), and underscore (_). The comparison is case sensitive. Wildcards are not supported; therefore, the method name must be an exact match.
If you specify multiple strings, the condition is satisfied if one of the strings matches the HTTP request method. We recommend that you route GET and HEAD requests in the same way, because the response to a HEAD request may be cached.

(string) --




SourceIpConfig (dict) --
Information for a source IP condition. Specify only when Field is source-ip .

Values (list) --
One or more source IP addresses, in CIDR format. You can use both IPv4 and IPv6 addresses. Wildcards are not supported.
If you specify multiple addresses, the condition is satisfied if the source IP address of the request matches one of the CIDR blocks. This condition is not satisfied by the addresses in the X-Forwarded-For header. To search for addresses in the X-Forwarded-For header, use  HttpHeaderConditionConfig .

(string) --








Actions (list) --
The actions. Each rule must include exactly one of the following types of actions: forward , redirect , or fixed-response , and it must be the last action to be performed.

(dict) --
Information about an action.

Type (string) --
The type of action.

TargetGroupArn (string) --
The Amazon Resource Name (ARN) of the target group. Specify only when Type is forward and you want to route to a single target group. To route to one or more target groups, use ForwardConfig instead.

AuthenticateOidcConfig (dict) --
[HTTPS listeners] Information about an identity provider that is compliant with OpenID Connect (OIDC). Specify only when Type is authenticate-oidc .

Issuer (string) --
The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

AuthorizationEndpoint (string) --
The authorization endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

TokenEndpoint (string) --
The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

UserInfoEndpoint (string) --
The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

ClientId (string) --
The OAuth 2.0 client identifier.

ClientSecret (string) --
The OAuth 2.0 client secret. This parameter is required if you are creating a rule. If you are modifying a rule, you can omit this parameter if you set UseExistingClientSecret to true.

SessionCookieName (string) --
The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.

Scope (string) --
The set of user claims to be requested from the IdP. The default is openid .
To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.

SessionTimeout (integer) --
The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).

AuthenticationRequestExtraParams (dict) --
The query parameters (up to 10) to include in the redirect request to the authorization endpoint.

(string) --
(string) --




OnUnauthenticatedRequest (string) --
The behavior if the user is not authenticated. The following are possible values:

deny- Return an HTTP 401 Unauthorized error.
allow- Allow the request to be forwarded to the target.
authenticate- Redirect the request to the IdP authorization endpoint. This is the default value.


UseExistingClientSecret (boolean) --
Indicates whether to use the existing client secret when modifying a rule. If you are creating a rule, you can omit this parameter or set it to false.



AuthenticateCognitoConfig (dict) --
[HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify only when Type is authenticate-cognito .

UserPoolArn (string) --
The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

UserPoolClientId (string) --
The ID of the Amazon Cognito user pool client.

UserPoolDomain (string) --
The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

SessionCookieName (string) --
The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.

Scope (string) --
The set of user claims to be requested from the IdP. The default is openid .
To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.

SessionTimeout (integer) --
The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).

AuthenticationRequestExtraParams (dict) --
The query parameters (up to 10) to include in the redirect request to the authorization endpoint.

(string) --
(string) --




OnUnauthenticatedRequest (string) --
The behavior if the user is not authenticated. The following are possible values:

deny- Return an HTTP 401 Unauthorized error.
allow- Allow the request to be forwarded to the target.
authenticate- Redirect the request to the IdP authorization endpoint. This is the default value.




Order (integer) --
The order for the action. This value is required for rules with multiple actions. The action with the lowest value for order is performed first. The last action to be performed must be one of the following types of actions: a forward , fixed-response , or redirect .

RedirectConfig (dict) --
[Application Load Balancer] Information for creating a redirect action. Specify only when Type is redirect .

Protocol (string) --
The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

Port (string) --
The port. You can specify a value from 1 to 65535 or #{port}.

Host (string) --
The hostname. This component is not percent-encoded. The hostname can contain #{host}.

Path (string) --
The absolute path, starting with the leading "/". This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}.

Query (string) --
The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading "?", as it is automatically added. You can specify any of the reserved keywords.

StatusCode (string) --
The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).



FixedResponseConfig (dict) --
[Application Load Balancer] Information for creating an action that returns a custom HTTP response. Specify only when Type is fixed-response .

MessageBody (string) --
The message.

StatusCode (string) --
The HTTP response code (2XX, 4XX, or 5XX).

ContentType (string) --
The content type.
Valid Values: text/plain | text/css | text/html | application/javascript | application/json



ForwardConfig (dict) --
Information for creating an action that distributes requests among one or more target groups. For Network Load Balancers, you can specify a single target group. Specify only when Type is forward . If you specify both ForwardConfig and TargetGroupArn , you can specify only one target group using ForwardConfig and it must be the same target group specified in TargetGroupArn .

TargetGroups (list) --
One or more target groups. For Network Load Balancers, you can specify a single target group.

(dict) --
Information about how traffic will be distributed between multiple target groups in a forward rule.

TargetGroupArn (string) --
The Amazon Resource Name (ARN) of the target group.

Weight (integer) --
The weight. The range is 0 to 999.





TargetGroupStickinessConfig (dict) --
The target group stickiness for the rule.

Enabled (boolean) --
Indicates whether target group stickiness is enabled.

DurationSeconds (integer) --
The time period, in seconds, during which requests from a client should be routed to the same target group. The range is 1-604800 seconds (7 days).









IsDefault (boolean) --
Indicates whether this is the default rule.











Exceptions

ElasticLoadBalancingv2.Client.exceptions.PriorityInUseException
ElasticLoadBalancingv2.Client.exceptions.TooManyTargetGroupsException
ElasticLoadBalancingv2.Client.exceptions.TooManyRulesException
ElasticLoadBalancingv2.Client.exceptions.TargetGroupAssociationLimitException
ElasticLoadBalancingv2.Client.exceptions.IncompatibleProtocolsException
ElasticLoadBalancingv2.Client.exceptions.ListenerNotFoundException
ElasticLoadBalancingv2.Client.exceptions.TargetGroupNotFoundException
ElasticLoadBalancingv2.Client.exceptions.InvalidConfigurationRequestException
ElasticLoadBalancingv2.Client.exceptions.TooManyRegistrationsForTargetIdException
ElasticLoadBalancingv2.Client.exceptions.TooManyTargetsException
ElasticLoadBalancingv2.Client.exceptions.UnsupportedProtocolException
ElasticLoadBalancingv2.Client.exceptions.TooManyActionsException
ElasticLoadBalancingv2.Client.exceptions.InvalidLoadBalancerActionException
ElasticLoadBalancingv2.Client.exceptions.TooManyUniqueTargetGroupsPerLoadBalancerException

Examples
This example creates a rule that forwards requests to the specified target group if the URL contains the specified pattern (for example, /img/*).
response = client.create_rule(
    Actions=[
        {
            'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
            'Type': 'forward',
        },
    ],
    Conditions=[
        {
            'Field': 'path-pattern',
            'Values': [
                '/img/*',
            ],
        },
    ],
    ListenerArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2',
    Priority=10,
)

print(response)


Expected Output:
{
    'Rules': [
        {
            'Actions': [
                {
                    'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
                    'Type': 'forward',
                },
            ],
            'Conditions': [
                {
                    'Field': 'path-pattern',
                    'Values': [
                        '/img/*',
                    ],
                },
            ],
            'IsDefault': False,
            'Priority': '10',
            'RuleArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/9683b2d02a6cabee',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Rules': [
            {
                'RuleArn': 'string',
                'Priority': 'string',
                'Conditions': [
                    {
                        'Field': 'string',
                        'Values': [
                            'string',
                        ],
                        'HostHeaderConfig': {
                            'Values': [
                                'string',
                            ]
                        },
                        'PathPatternConfig': {
                            'Values': [
                                'string',
                            ]
                        },
                        'HttpHeaderConfig': {
                            'HttpHeaderName': 'string',
                            'Values': [
                                'string',
                            ]
                        },
                        'QueryStringConfig': {
                            'Values': [
                                {
                                    'Key': 'string',
                                    'Value': 'string'
                                },
                            ]
                        },
                        'HttpRequestMethodConfig': {
                            'Values': [
                                'string',
                            ]
                        },
                        'SourceIpConfig': {
                            'Values': [
                                'string',
                            ]
                        }
                    },
                ],
                'Actions': [
                    {
                        'Type': 'forward'|'authenticate-oidc'|'authenticate-cognito'|'redirect'|'fixed-response',
                        'TargetGroupArn': 'string',
                        'AuthenticateOidcConfig': {
                            'Issuer': 'string',
                            'AuthorizationEndpoint': 'string',
                            'TokenEndpoint': 'string',
                            'UserInfoEndpoint': 'string',
                            'ClientId': 'string',
                            'ClientSecret': 'string',
                            'SessionCookieName': 'string',
                            'Scope': 'string',
                            'SessionTimeout': 123,
                            'AuthenticationRequestExtraParams': {
                                'string': 'string'
                            },
                            'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate',
                            'UseExistingClientSecret': True|False
                        },
                        'AuthenticateCognitoConfig': {
                            'UserPoolArn': 'string',
                            'UserPoolClientId': 'string',
                            'UserPoolDomain': 'string',
                            'SessionCookieName': 'string',
                            'Scope': 'string',
                            'SessionTimeout': 123,
                            'AuthenticationRequestExtraParams': {
                                'string': 'string'
                            },
                            'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate'
                        },
                        'Order': 123,
                        'RedirectConfig': {
                            'Protocol': 'string',
                            'Port': 'string',
                            'Host': 'string',
                            'Path': 'string',
                            'Query': 'string',
                            'StatusCode': 'HTTP_301'|'HTTP_302'
                        },
                        'FixedResponseConfig': {
                            'MessageBody': 'string',
                            'StatusCode': 'string',
                            'ContentType': 'string'
                        },
                        'ForwardConfig': {
                            'TargetGroups': [
                                {
                                    'TargetGroupArn': 'string',
                                    'Weight': 123
                                },
                            ],
                            'TargetGroupStickinessConfig': {
                                'Enabled': True|False,
                                'DurationSeconds': 123
                            }
                        }
                    },
                ],
                'IsDefault': True|False
            },
        ]
    }
    
    
    :returns: 
    http-header
    http-request-method
    host-header
    path-pattern
    query-string
    source-ip
    
    """
    pass

def create_target_group(Name=None, Protocol=None, Port=None, VpcId=None, HealthCheckProtocol=None, HealthCheckPort=None, HealthCheckEnabled=None, HealthCheckPath=None, HealthCheckIntervalSeconds=None, HealthCheckTimeoutSeconds=None, HealthyThresholdCount=None, UnhealthyThresholdCount=None, Matcher=None, TargetType=None):
    """
    Creates a target group.
    To register targets with the target group, use  RegisterTargets . To update the health check settings for the target group, use  ModifyTargetGroup . To monitor the health of targets in the target group, use  DescribeTargetHealth .
    To route traffic to the targets in a target group, specify the target group in an action using  CreateListener or  CreateRule .
    To delete a target group, use  DeleteTargetGroup .
    This operation is idempotent, which means that it completes at most one time. If you attempt to create multiple target groups with the same settings, each call succeeds.
    For more information, see Target Groups for Your Application Load Balancers in the Application Load Balancers Guide or Target Groups for Your Network Load Balancers in the Network Load Balancers Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example creates a target group that you can use to route traffic to targets using HTTP on port 80. This target group uses the default health check configuration.
    Expected Output:
    
    :example: response = client.create_target_group(
        Name='string',
        Protocol='HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
        Port=123,
        VpcId='string',
        HealthCheckProtocol='HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
        HealthCheckPort='string',
        HealthCheckEnabled=True|False,
        HealthCheckPath='string',
        HealthCheckIntervalSeconds=123,
        HealthCheckTimeoutSeconds=123,
        HealthyThresholdCount=123,
        UnhealthyThresholdCount=123,
        Matcher={
            'HttpCode': 'string'
        },
        TargetType='instance'|'ip'|'lambda'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the target group.\nThis name must be unique per region per account, can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.\n

    :type Protocol: string
    :param Protocol: The protocol to use for routing traffic to the targets. For Application Load Balancers, the supported protocols are HTTP and HTTPS. For Network Load Balancers, the supported protocols are TCP, TLS, UDP, or TCP_UDP. A TCP_UDP listener must be associated with a TCP_UDP target group. If the target is a Lambda function, this parameter does not apply.

    :type Port: integer
    :param Port: The port on which the targets receive traffic. This port is used unless you specify a port override when registering the target. If the target is a Lambda function, this parameter does not apply.

    :type VpcId: string
    :param VpcId: The identifier of the virtual private cloud (VPC). If the target is a Lambda function, this parameter does not apply. Otherwise, this parameter is required.

    :type HealthCheckProtocol: string
    :param HealthCheckProtocol: The protocol the load balancer uses when performing health checks on targets. For Application Load Balancers, the default is HTTP. For Network Load Balancers, the default is TCP. The TCP protocol is supported for health checks only if the protocol of the target group is TCP, TLS, UDP, or TCP_UDP. The TLS, UDP, and TCP_UDP protocols are not supported for health checks.

    :type HealthCheckPort: string
    :param HealthCheckPort: The port the load balancer uses when performing health checks on targets. The default is traffic-port , which is the port on which each target receives traffic from the load balancer.

    :type HealthCheckEnabled: boolean
    :param HealthCheckEnabled: Indicates whether health checks are enabled. If the target type is lambda , health checks are disabled by default but can be enabled. If the target type is instance or ip , health checks are always enabled and cannot be disabled.

    :type HealthCheckPath: string
    :param HealthCheckPath: [HTTP/HTTPS health checks] The ping path that is the destination on the targets for health checks. The default is /.

    :type HealthCheckIntervalSeconds: integer
    :param HealthCheckIntervalSeconds: The approximate amount of time, in seconds, between health checks of an individual target. For HTTP and HTTPS health checks, the range is 5\xe2\x80\x93300 seconds. For TCP health checks, the supported values are 10 and 30 seconds. If the target type is instance or ip , the default is 30 seconds. If the target type is lambda , the default is 35 seconds.

    :type HealthCheckTimeoutSeconds: integer
    :param HealthCheckTimeoutSeconds: The amount of time, in seconds, during which no response from a target means a failed health check. For target groups with a protocol of HTTP or HTTPS, the default is 5 seconds. For target groups with a protocol of TCP or TLS, this value must be 6 seconds for HTTP health checks and 10 seconds for TCP and HTTPS health checks. If the target type is lambda , the default is 30 seconds.

    :type HealthyThresholdCount: integer
    :param HealthyThresholdCount: The number of consecutive health checks successes required before considering an unhealthy target healthy. For target groups with a protocol of HTTP or HTTPS, the default is 5. For target groups with a protocol of TCP or TLS, the default is 3. If the target type is lambda , the default is 5.

    :type UnhealthyThresholdCount: integer
    :param UnhealthyThresholdCount: The number of consecutive health check failures required before considering a target unhealthy. For target groups with a protocol of HTTP or HTTPS, the default is 2. For target groups with a protocol of TCP or TLS, this value must be the same as the healthy threshold count. If the target type is lambda , the default is 2.

    :type Matcher: dict
    :param Matcher: [HTTP/HTTPS health checks] The HTTP codes to use when checking for a successful response from a target.\n\nHttpCode (string) -- [REQUIRED]The HTTP codes.\nFor Application Load Balancers, you can specify values between 200 and 499, and the default value is 200. You can specify multiple values (for example, '200,202') or a range of values (for example, '200-299').\nFor Network Load Balancers, this is 200\xe2\x80\x93399.\n\n\n

    :type TargetType: string
    :param TargetType: The type of target that you must specify when registering targets with this target group. You can\'t specify targets for a target group using more than one target type.\n\ninstance - Targets are specified by instance ID. This is the default value. If the target group protocol is UDP or TCP_UDP, the target type must be instance .\nip - Targets are specified by IP address. You can specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group, the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10). You can\'t specify publicly routable IP addresses.\nlambda - The target groups contains a single Lambda function.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TargetGroups': [
        {
            'TargetGroupArn': 'string',
            'TargetGroupName': 'string',
            'Protocol': 'HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
            'Port': 123,
            'VpcId': 'string',
            'HealthCheckProtocol': 'HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
            'HealthCheckPort': 'string',
            'HealthCheckEnabled': True|False,
            'HealthCheckIntervalSeconds': 123,
            'HealthCheckTimeoutSeconds': 123,
            'HealthyThresholdCount': 123,
            'UnhealthyThresholdCount': 123,
            'HealthCheckPath': 'string',
            'Matcher': {
                'HttpCode': 'string'
            },
            'LoadBalancerArns': [
                'string',
            ],
            'TargetType': 'instance'|'ip'|'lambda'
        },
    ]
}


Response Structure

(dict) --

TargetGroups (list) --
Information about the target group.

(dict) --
Information about a target group.

TargetGroupArn (string) --
The Amazon Resource Name (ARN) of the target group.

TargetGroupName (string) --
The name of the target group.

Protocol (string) --
The protocol to use for routing traffic to the targets.

Port (integer) --
The port on which the targets are listening. Not used if the target is a Lambda function.

VpcId (string) --
The ID of the VPC for the targets.

HealthCheckProtocol (string) --
The protocol to use to connect with the target.

HealthCheckPort (string) --
The port to use to connect with the target.

HealthCheckEnabled (boolean) --
Indicates whether health checks are enabled.

HealthCheckIntervalSeconds (integer) --
The approximate amount of time, in seconds, between health checks of an individual target.

HealthCheckTimeoutSeconds (integer) --
The amount of time, in seconds, during which no response means a failed health check.

HealthyThresholdCount (integer) --
The number of consecutive health checks successes required before considering an unhealthy target healthy.

UnhealthyThresholdCount (integer) --
The number of consecutive health check failures required before considering the target unhealthy.

HealthCheckPath (string) --
The destination for the health check request.

Matcher (dict) --
The HTTP codes to use when checking for a successful response from a target.

HttpCode (string) --
The HTTP codes.
For Application Load Balancers, you can specify values between 200 and 499, and the default value is 200. You can specify multiple values (for example, "200,202") or a range of values (for example, "200-299").
For Network Load Balancers, this is 200\xe2\x80\x93399.



LoadBalancerArns (list) --
The Amazon Resource Names (ARN) of the load balancers that route traffic to this target group.

(string) --


TargetType (string) --
The type of target that you must specify when registering targets with this target group. The possible values are instance (targets are specified by instance ID) or ip (targets are specified by IP address).











Exceptions

ElasticLoadBalancingv2.Client.exceptions.DuplicateTargetGroupNameException
ElasticLoadBalancingv2.Client.exceptions.TooManyTargetGroupsException
ElasticLoadBalancingv2.Client.exceptions.InvalidConfigurationRequestException

Examples
This example creates a target group that you can use to route traffic to targets using HTTP on port 80. This target group uses the default health check configuration.
response = client.create_target_group(
    Name='my-targets',
    Port=80,
    Protocol='HTTP',
    VpcId='vpc-3ac0fb5f',
)

print(response)


Expected Output:
{
    'TargetGroups': [
        {
            'HealthCheckIntervalSeconds': 30,
            'HealthCheckPath': '/',
            'HealthCheckPort': 'traffic-port',
            'HealthCheckProtocol': 'HTTP',
            'HealthCheckTimeoutSeconds': 5,
            'HealthyThresholdCount': 5,
            'Matcher': {
                'HttpCode': '200',
            },
            'Port': 80,
            'Protocol': 'HTTP',
            'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
            'TargetGroupName': 'my-targets',
            'UnhealthyThresholdCount': 2,
            'VpcId': 'vpc-3ac0fb5f',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'TargetGroups': [
            {
                'TargetGroupArn': 'string',
                'TargetGroupName': 'string',
                'Protocol': 'HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
                'Port': 123,
                'VpcId': 'string',
                'HealthCheckProtocol': 'HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
                'HealthCheckPort': 'string',
                'HealthCheckEnabled': True|False,
                'HealthCheckIntervalSeconds': 123,
                'HealthCheckTimeoutSeconds': 123,
                'HealthyThresholdCount': 123,
                'UnhealthyThresholdCount': 123,
                'HealthCheckPath': 'string',
                'Matcher': {
                    'HttpCode': 'string'
                },
                'LoadBalancerArns': [
                    'string',
                ],
                'TargetType': 'instance'|'ip'|'lambda'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_listener(ListenerArn=None):
    """
    Deletes the specified listener.
    Alternatively, your listener is deleted when you delete the load balancer to which it is attached, using  DeleteLoadBalancer .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example deletes the specified listener.
    Expected Output:
    
    :example: response = client.delete_listener(
        ListenerArn='string'
    )
    
    
    :type ListenerArn: string
    :param ListenerArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the listener.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

ElasticLoadBalancingv2.Client.exceptions.ListenerNotFoundException

Examples
This example deletes the specified listener.
response = client.delete_listener(
    ListenerArn='arn:aws:elasticloadbalancing:ua-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    ElasticLoadBalancingv2.Client.exceptions.ListenerNotFoundException
    
    """
    pass

def delete_load_balancer(LoadBalancerArn=None):
    """
    Deletes the specified Application Load Balancer or Network Load Balancer and its attached listeners.
    You can\'t delete a load balancer if deletion protection is enabled. If the load balancer does not exist or has already been deleted, the call succeeds.
    Deleting a load balancer does not affect its registered targets. For example, your EC2 instances continue to run and are still registered to their target groups. If you no longer need these EC2 instances, you can stop or terminate them.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example deletes the specified load balancer.
    Expected Output:
    
    :example: response = client.delete_load_balancer(
        LoadBalancerArn='string'
    )
    
    
    :type LoadBalancerArn: string
    :param LoadBalancerArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the load balancer.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

ElasticLoadBalancingv2.Client.exceptions.LoadBalancerNotFoundException
ElasticLoadBalancingv2.Client.exceptions.OperationNotPermittedException
ElasticLoadBalancingv2.Client.exceptions.ResourceInUseException

Examples
This example deletes the specified load balancer.
response = client.delete_load_balancer(
    LoadBalancerArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    ElasticLoadBalancingv2.Client.exceptions.LoadBalancerNotFoundException
    ElasticLoadBalancingv2.Client.exceptions.OperationNotPermittedException
    ElasticLoadBalancingv2.Client.exceptions.ResourceInUseException
    
    """
    pass

def delete_rule(RuleArn=None):
    """
    Deletes the specified rule.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example deletes the specified rule.
    Expected Output:
    
    :example: response = client.delete_rule(
        RuleArn='string'
    )
    
    
    :type RuleArn: string
    :param RuleArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the rule.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

ElasticLoadBalancingv2.Client.exceptions.RuleNotFoundException
ElasticLoadBalancingv2.Client.exceptions.OperationNotPermittedException

Examples
This example deletes the specified rule.
response = client.delete_rule(
    RuleArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/1291d13826f405c3',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    ElasticLoadBalancingv2.Client.exceptions.RuleNotFoundException
    ElasticLoadBalancingv2.Client.exceptions.OperationNotPermittedException
    
    """
    pass

def delete_target_group(TargetGroupArn=None):
    """
    Deletes the specified target group.
    You can delete a target group if it is not referenced by any actions. Deleting a target group also deletes any associated health checks.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example deletes the specified target group.
    Expected Output:
    
    :example: response = client.delete_target_group(
        TargetGroupArn='string'
    )
    
    
    :type TargetGroupArn: string
    :param TargetGroupArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the target group.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

ElasticLoadBalancingv2.Client.exceptions.ResourceInUseException

Examples
This example deletes the specified target group.
response = client.delete_target_group(
    TargetGroupArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    ElasticLoadBalancingv2.Client.exceptions.ResourceInUseException
    
    """
    pass

def deregister_targets(TargetGroupArn=None, Targets=None):
    """
    Deregisters the specified targets from the specified target group. After the targets are deregistered, they no longer receive traffic from the load balancer.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example deregisters the specified instance from the specified target group.
    Expected Output:
    
    :example: response = client.deregister_targets(
        TargetGroupArn='string',
        Targets=[
            {
                'Id': 'string',
                'Port': 123,
                'AvailabilityZone': 'string'
            },
        ]
    )
    
    
    :type TargetGroupArn: string
    :param TargetGroupArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the target group.\n

    :type Targets: list
    :param Targets: [REQUIRED]\nThe targets. If you specified a port override when you registered a target, you must specify both the target ID and the port when you deregister it.\n\n(dict) --Information about a target.\n\nId (string) -- [REQUIRED]The ID of the target. If the target type of the target group is instance , specify an instance ID. If the target type is ip , specify an IP address. If the target type is lambda , specify the ARN of the Lambda function.\n\nPort (integer) --The port on which the target is listening. Not used if the target is a Lambda function.\n\nAvailabilityZone (string) --An Availability Zone or all . This determines whether the target receives traffic from the load balancer nodes in the specified Availability Zone or from all enabled Availability Zones for the load balancer.\nThis parameter is not supported if the target type of the target group is instance .\nIf the target type is ip and the IP address is in a subnet of the VPC for the target group, the Availability Zone is automatically detected and this parameter is optional. If the IP address is outside the VPC, this parameter is required.\nWith an Application Load Balancer, if the target type is ip and the IP address is outside the VPC for the target group, the only supported value is all .\nIf the target type is lambda , this parameter is optional and the only supported value is all .\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ElasticLoadBalancingv2.Client.exceptions.TargetGroupNotFoundException
ElasticLoadBalancingv2.Client.exceptions.InvalidTargetException

Examples
This example deregisters the specified instance from the specified target group.
response = client.deregister_targets(
    TargetGroupArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
    Targets=[
        {
            'Id': 'i-0f76fade',
        },
    ],
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def describe_account_limits(Marker=None, PageSize=None):
    """
    Describes the current Elastic Load Balancing resource limits for your AWS account.
    For more information, see Limits for Your Application Load Balancers in the Application Load Balancer Guide or Limits for Your Network Load Balancers in the Network Load Balancers Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_account_limits(
        Marker='string',
        PageSize=123
    )
    
    
    :type Marker: string
    :param Marker: The marker for the next set of results. (You received this marker from a previous call.)

    :type PageSize: integer
    :param PageSize: The maximum number of results to return with this call.

    :rtype: dict

ReturnsResponse Syntax
{
    'Limits': [
        {
            'Name': 'string',
            'Max': 'string'
        },
    ],
    'NextMarker': 'string'
}


Response Structure

(dict) --

Limits (list) --
Information about the limits.

(dict) --
Information about an Elastic Load Balancing resource limit for your AWS account.

Name (string) --
The name of the limit. The possible values are:

application-load-balancers
listeners-per-application-load-balancer
listeners-per-network-load-balancer
network-load-balancers
rules-per-application-load-balancer
target-groups
target-groups-per-action-on-application-load-balancer
target-groups-per-action-on-network-load-balancer
target-groups-per-application-load-balancer
targets-per-application-load-balancer
targets-per-availability-zone-per-network-load-balancer
targets-per-network-load-balancer


Max (string) --
The maximum value of the limit.





NextMarker (string) --
If there are additional results, this is the marker for the next set of results. Otherwise, this is null.








    :return: {
        'Limits': [
            {
                'Name': 'string',
                'Max': 'string'
            },
        ],
        'NextMarker': 'string'
    }
    
    
    :returns: 
    application-load-balancers
    listeners-per-application-load-balancer
    listeners-per-network-load-balancer
    network-load-balancers
    rules-per-application-load-balancer
    target-groups
    target-groups-per-action-on-application-load-balancer
    target-groups-per-action-on-network-load-balancer
    target-groups-per-application-load-balancer
    targets-per-application-load-balancer
    targets-per-availability-zone-per-network-load-balancer
    targets-per-network-load-balancer
    
    """
    pass

def describe_listener_certificates(ListenerArn=None, Marker=None, PageSize=None):
    """
    Describes the default certificate and the certificate list for the specified HTTPS or TLS listener.
    If the default certificate is also in the certificate list, it appears twice in the results (once with IsDefault set to true and once with IsDefault set to false).
    For more information, see SSL Certificates in the Application Load Balancers Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_listener_certificates(
        ListenerArn='string',
        Marker='string',
        PageSize=123
    )
    
    
    :type ListenerArn: string
    :param ListenerArn: [REQUIRED]\nThe Amazon Resource Names (ARN) of the listener.\n

    :type Marker: string
    :param Marker: The marker for the next set of results. (You received this marker from a previous call.)

    :type PageSize: integer
    :param PageSize: The maximum number of results to return with this call.

    :rtype: dict

ReturnsResponse Syntax
{
    'Certificates': [
        {
            'CertificateArn': 'string',
            'IsDefault': True|False
        },
    ],
    'NextMarker': 'string'
}


Response Structure

(dict) --

Certificates (list) --
Information about the certificates.

(dict) --
Information about an SSL server certificate.

CertificateArn (string) --
The Amazon Resource Name (ARN) of the certificate.

IsDefault (boolean) --
Indicates whether the certificate is the default certificate. Do not set this value when specifying a certificate as an input. This value is not included in the output when describing a listener, but is included when describing listener certificates.





NextMarker (string) --
If there are additional results, this is the marker for the next set of results. Otherwise, this is null.







Exceptions

ElasticLoadBalancingv2.Client.exceptions.ListenerNotFoundException


    :return: {
        'Certificates': [
            {
                'CertificateArn': 'string',
                'IsDefault': True|False
            },
        ],
        'NextMarker': 'string'
    }
    
    
    :returns: 
    ElasticLoadBalancingv2.Client.exceptions.ListenerNotFoundException
    
    """
    pass

def describe_listeners(LoadBalancerArn=None, ListenerArns=None, Marker=None, PageSize=None):
    """
    Describes the specified listeners or the listeners for the specified Application Load Balancer or Network Load Balancer. You must specify either a load balancer or one or more listeners.
    For an HTTPS or TLS listener, the output includes the default certificate for the listener. To describe the certificate list for the listener, use  DescribeListenerCertificates .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the specified listener.
    Expected Output:
    
    :example: response = client.describe_listeners(
        LoadBalancerArn='string',
        ListenerArns=[
            'string',
        ],
        Marker='string',
        PageSize=123
    )
    
    
    :type LoadBalancerArn: string
    :param LoadBalancerArn: The Amazon Resource Name (ARN) of the load balancer.

    :type ListenerArns: list
    :param ListenerArns: The Amazon Resource Names (ARN) of the listeners.\n\n(string) --\n\n

    :type Marker: string
    :param Marker: The marker for the next set of results. (You received this marker from a previous call.)

    :type PageSize: integer
    :param PageSize: The maximum number of results to return with this call.

    :rtype: dict

ReturnsResponse Syntax
{
    'Listeners': [
        {
            'ListenerArn': 'string',
            'LoadBalancerArn': 'string',
            'Port': 123,
            'Protocol': 'HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
            'Certificates': [
                {
                    'CertificateArn': 'string',
                    'IsDefault': True|False
                },
            ],
            'SslPolicy': 'string',
            'DefaultActions': [
                {
                    'Type': 'forward'|'authenticate-oidc'|'authenticate-cognito'|'redirect'|'fixed-response',
                    'TargetGroupArn': 'string',
                    'AuthenticateOidcConfig': {
                        'Issuer': 'string',
                        'AuthorizationEndpoint': 'string',
                        'TokenEndpoint': 'string',
                        'UserInfoEndpoint': 'string',
                        'ClientId': 'string',
                        'ClientSecret': 'string',
                        'SessionCookieName': 'string',
                        'Scope': 'string',
                        'SessionTimeout': 123,
                        'AuthenticationRequestExtraParams': {
                            'string': 'string'
                        },
                        'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate',
                        'UseExistingClientSecret': True|False
                    },
                    'AuthenticateCognitoConfig': {
                        'UserPoolArn': 'string',
                        'UserPoolClientId': 'string',
                        'UserPoolDomain': 'string',
                        'SessionCookieName': 'string',
                        'Scope': 'string',
                        'SessionTimeout': 123,
                        'AuthenticationRequestExtraParams': {
                            'string': 'string'
                        },
                        'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate'
                    },
                    'Order': 123,
                    'RedirectConfig': {
                        'Protocol': 'string',
                        'Port': 'string',
                        'Host': 'string',
                        'Path': 'string',
                        'Query': 'string',
                        'StatusCode': 'HTTP_301'|'HTTP_302'
                    },
                    'FixedResponseConfig': {
                        'MessageBody': 'string',
                        'StatusCode': 'string',
                        'ContentType': 'string'
                    },
                    'ForwardConfig': {
                        'TargetGroups': [
                            {
                                'TargetGroupArn': 'string',
                                'Weight': 123
                            },
                        ],
                        'TargetGroupStickinessConfig': {
                            'Enabled': True|False,
                            'DurationSeconds': 123
                        }
                    }
                },
            ],
            'AlpnPolicy': [
                'string',
            ]
        },
    ],
    'NextMarker': 'string'
}


Response Structure

(dict) --

Listeners (list) --
Information about the listeners.

(dict) --
Information about a listener.

ListenerArn (string) --
The Amazon Resource Name (ARN) of the listener.

LoadBalancerArn (string) --
The Amazon Resource Name (ARN) of the load balancer.

Port (integer) --
The port on which the load balancer is listening.

Protocol (string) --
The protocol for connections from clients to the load balancer.

Certificates (list) --
[HTTPS or TLS listener] The default certificate for the listener.

(dict) --
Information about an SSL server certificate.

CertificateArn (string) --
The Amazon Resource Name (ARN) of the certificate.

IsDefault (boolean) --
Indicates whether the certificate is the default certificate. Do not set this value when specifying a certificate as an input. This value is not included in the output when describing a listener, but is included when describing listener certificates.





SslPolicy (string) --
[HTTPS or TLS listener] The security policy that defines which protocols and ciphers are supported.

DefaultActions (list) --
The default actions for the listener.

(dict) --
Information about an action.

Type (string) --
The type of action.

TargetGroupArn (string) --
The Amazon Resource Name (ARN) of the target group. Specify only when Type is forward and you want to route to a single target group. To route to one or more target groups, use ForwardConfig instead.

AuthenticateOidcConfig (dict) --
[HTTPS listeners] Information about an identity provider that is compliant with OpenID Connect (OIDC). Specify only when Type is authenticate-oidc .

Issuer (string) --
The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

AuthorizationEndpoint (string) --
The authorization endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

TokenEndpoint (string) --
The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

UserInfoEndpoint (string) --
The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

ClientId (string) --
The OAuth 2.0 client identifier.

ClientSecret (string) --
The OAuth 2.0 client secret. This parameter is required if you are creating a rule. If you are modifying a rule, you can omit this parameter if you set UseExistingClientSecret to true.

SessionCookieName (string) --
The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.

Scope (string) --
The set of user claims to be requested from the IdP. The default is openid .
To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.

SessionTimeout (integer) --
The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).

AuthenticationRequestExtraParams (dict) --
The query parameters (up to 10) to include in the redirect request to the authorization endpoint.

(string) --
(string) --




OnUnauthenticatedRequest (string) --
The behavior if the user is not authenticated. The following are possible values:

deny- Return an HTTP 401 Unauthorized error.
allow- Allow the request to be forwarded to the target.
authenticate- Redirect the request to the IdP authorization endpoint. This is the default value.


UseExistingClientSecret (boolean) --
Indicates whether to use the existing client secret when modifying a rule. If you are creating a rule, you can omit this parameter or set it to false.



AuthenticateCognitoConfig (dict) --
[HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify only when Type is authenticate-cognito .

UserPoolArn (string) --
The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

UserPoolClientId (string) --
The ID of the Amazon Cognito user pool client.

UserPoolDomain (string) --
The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

SessionCookieName (string) --
The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.

Scope (string) --
The set of user claims to be requested from the IdP. The default is openid .
To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.

SessionTimeout (integer) --
The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).

AuthenticationRequestExtraParams (dict) --
The query parameters (up to 10) to include in the redirect request to the authorization endpoint.

(string) --
(string) --




OnUnauthenticatedRequest (string) --
The behavior if the user is not authenticated. The following are possible values:

deny- Return an HTTP 401 Unauthorized error.
allow- Allow the request to be forwarded to the target.
authenticate- Redirect the request to the IdP authorization endpoint. This is the default value.




Order (integer) --
The order for the action. This value is required for rules with multiple actions. The action with the lowest value for order is performed first. The last action to be performed must be one of the following types of actions: a forward , fixed-response , or redirect .

RedirectConfig (dict) --
[Application Load Balancer] Information for creating a redirect action. Specify only when Type is redirect .

Protocol (string) --
The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

Port (string) --
The port. You can specify a value from 1 to 65535 or #{port}.

Host (string) --
The hostname. This component is not percent-encoded. The hostname can contain #{host}.

Path (string) --
The absolute path, starting with the leading "/". This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}.

Query (string) --
The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading "?", as it is automatically added. You can specify any of the reserved keywords.

StatusCode (string) --
The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).



FixedResponseConfig (dict) --
[Application Load Balancer] Information for creating an action that returns a custom HTTP response. Specify only when Type is fixed-response .

MessageBody (string) --
The message.

StatusCode (string) --
The HTTP response code (2XX, 4XX, or 5XX).

ContentType (string) --
The content type.
Valid Values: text/plain | text/css | text/html | application/javascript | application/json



ForwardConfig (dict) --
Information for creating an action that distributes requests among one or more target groups. For Network Load Balancers, you can specify a single target group. Specify only when Type is forward . If you specify both ForwardConfig and TargetGroupArn , you can specify only one target group using ForwardConfig and it must be the same target group specified in TargetGroupArn .

TargetGroups (list) --
One or more target groups. For Network Load Balancers, you can specify a single target group.

(dict) --
Information about how traffic will be distributed between multiple target groups in a forward rule.

TargetGroupArn (string) --
The Amazon Resource Name (ARN) of the target group.

Weight (integer) --
The weight. The range is 0 to 999.





TargetGroupStickinessConfig (dict) --
The target group stickiness for the rule.

Enabled (boolean) --
Indicates whether target group stickiness is enabled.

DurationSeconds (integer) --
The time period, in seconds, during which requests from a client should be routed to the same target group. The range is 1-604800 seconds (7 days).









AlpnPolicy (list) --
[TLS listener] The name of the Application-Layer Protocol Negotiation (ALPN) policy.

(string) --






NextMarker (string) --
If there are additional results, this is the marker for the next set of results. Otherwise, this is null.







Exceptions

ElasticLoadBalancingv2.Client.exceptions.ListenerNotFoundException
ElasticLoadBalancingv2.Client.exceptions.LoadBalancerNotFoundException
ElasticLoadBalancingv2.Client.exceptions.UnsupportedProtocolException

Examples
This example describes the specified listener.
response = client.describe_listeners(
    ListenerArns=[
        'arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2',
    ],
)

print(response)


Expected Output:
{
    'Listeners': [
        {
            'DefaultActions': [
                {
                    'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
                    'Type': 'forward',
                },
            ],
            'ListenerArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2',
            'LoadBalancerArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
            'Port': 80,
            'Protocol': 'HTTP',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Listeners': [
            {
                'ListenerArn': 'string',
                'LoadBalancerArn': 'string',
                'Port': 123,
                'Protocol': 'HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
                'Certificates': [
                    {
                        'CertificateArn': 'string',
                        'IsDefault': True|False
                    },
                ],
                'SslPolicy': 'string',
                'DefaultActions': [
                    {
                        'Type': 'forward'|'authenticate-oidc'|'authenticate-cognito'|'redirect'|'fixed-response',
                        'TargetGroupArn': 'string',
                        'AuthenticateOidcConfig': {
                            'Issuer': 'string',
                            'AuthorizationEndpoint': 'string',
                            'TokenEndpoint': 'string',
                            'UserInfoEndpoint': 'string',
                            'ClientId': 'string',
                            'ClientSecret': 'string',
                            'SessionCookieName': 'string',
                            'Scope': 'string',
                            'SessionTimeout': 123,
                            'AuthenticationRequestExtraParams': {
                                'string': 'string'
                            },
                            'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate',
                            'UseExistingClientSecret': True|False
                        },
                        'AuthenticateCognitoConfig': {
                            'UserPoolArn': 'string',
                            'UserPoolClientId': 'string',
                            'UserPoolDomain': 'string',
                            'SessionCookieName': 'string',
                            'Scope': 'string',
                            'SessionTimeout': 123,
                            'AuthenticationRequestExtraParams': {
                                'string': 'string'
                            },
                            'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate'
                        },
                        'Order': 123,
                        'RedirectConfig': {
                            'Protocol': 'string',
                            'Port': 'string',
                            'Host': 'string',
                            'Path': 'string',
                            'Query': 'string',
                            'StatusCode': 'HTTP_301'|'HTTP_302'
                        },
                        'FixedResponseConfig': {
                            'MessageBody': 'string',
                            'StatusCode': 'string',
                            'ContentType': 'string'
                        },
                        'ForwardConfig': {
                            'TargetGroups': [
                                {
                                    'TargetGroupArn': 'string',
                                    'Weight': 123
                                },
                            ],
                            'TargetGroupStickinessConfig': {
                                'Enabled': True|False,
                                'DurationSeconds': 123
                            }
                        }
                    },
                ],
                'AlpnPolicy': [
                    'string',
                ]
            },
        ],
        'NextMarker': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def describe_load_balancer_attributes(LoadBalancerArn=None):
    """
    Describes the attributes for the specified Application Load Balancer or Network Load Balancer.
    For more information, see Load Balancer Attributes in the Application Load Balancers Guide or Load Balancer Attributes in the Network Load Balancers Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the attributes of the specified load balancer.
    Expected Output:
    
    :example: response = client.describe_load_balancer_attributes(
        LoadBalancerArn='string'
    )
    
    
    :type LoadBalancerArn: string
    :param LoadBalancerArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the load balancer.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Attributes': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --
Attributes (list) --Information about the load balancer attributes.

(dict) --Information about a load balancer attribute.

Key (string) --The name of the attribute.
The following attributes are supported by both Application Load Balancers and Network Load Balancers:

access_logs.s3.enabled - Indicates whether access logs are enabled. The value is true or false . The default is false .
access_logs.s3.bucket - The name of the S3 bucket for the access logs. This attribute is required if access logs are enabled. The bucket must exist in the same region as the load balancer and have a bucket policy that grants Elastic Load Balancing permissions to write to the bucket.
access_logs.s3.prefix - The prefix for the location in the S3 bucket for the access logs.
deletion_protection.enabled - Indicates whether deletion protection is enabled. The value is true or false . The default is false .

The following attributes are supported by only Application Load Balancers:

idle_timeout.timeout_seconds - The idle timeout value, in seconds. The valid range is 1-4000 seconds. The default is 60 seconds.
routing.http.drop_invalid_header_fields.enabled - Indicates whether HTTP headers with invalid header fields are removed by the load balancer (true ) or routed to targets (false ). The default is false .
routing.http2.enabled - Indicates whether HTTP/2 is enabled. The value is true or false . The default is true . Elastic Load Balancing requires that message header names contain only alphanumeric characters and hyphens.

The following attributes are supported by only Network Load Balancers:

load_balancing.cross_zone.enabled - Indicates whether cross-zone load balancing is enabled. The value is true or false . The default is false .


Value (string) --The value of the attribute.










Exceptions

ElasticLoadBalancingv2.Client.exceptions.LoadBalancerNotFoundException

Examples
This example describes the attributes of the specified load balancer.
response = client.describe_load_balancer_attributes(
    LoadBalancerArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
)

print(response)


Expected Output:
{
    'Attributes': [
        {
            'Key': 'access_logs.s3.enabled',
            'Value': 'false',
        },
        {
            'Key': 'idle_timeout.timeout_seconds',
            'Value': '60',
        },
        {
            'Key': 'access_logs.s3.prefix',
            'Value': '',
        },
        {
            'Key': 'deletion_protection.enabled',
            'Value': 'false',
        },
        {
            'Key': 'access_logs.s3.bucket',
            'Value': '',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Attributes': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    :returns: 
    idle_timeout.timeout_seconds - The idle timeout value, in seconds. The valid range is 1-4000 seconds. The default is 60 seconds.
    routing.http.drop_invalid_header_fields.enabled - Indicates whether HTTP headers with invalid header fields are removed by the load balancer (true ) or routed to targets (false ). The default is false .
    routing.http2.enabled - Indicates whether HTTP/2 is enabled. The value is true or false . The default is true . Elastic Load Balancing requires that message header names contain only alphanumeric characters and hyphens.
    
    """
    pass

def describe_load_balancers(LoadBalancerArns=None, Names=None, Marker=None, PageSize=None):
    """
    Describes the specified load balancers or all of your load balancers.
    To describe the listeners for a load balancer, use  DescribeListeners . To describe the attributes for a load balancer, use  DescribeLoadBalancerAttributes .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the specified load balancer.
    Expected Output:
    
    :example: response = client.describe_load_balancers(
        LoadBalancerArns=[
            'string',
        ],
        Names=[
            'string',
        ],
        Marker='string',
        PageSize=123
    )
    
    
    :type LoadBalancerArns: list
    :param LoadBalancerArns: The Amazon Resource Names (ARN) of the load balancers. You can specify up to 20 load balancers in a single call.\n\n(string) --\n\n

    :type Names: list
    :param Names: The names of the load balancers.\n\n(string) --\n\n

    :type Marker: string
    :param Marker: The marker for the next set of results. (You received this marker from a previous call.)

    :type PageSize: integer
    :param PageSize: The maximum number of results to return with this call.

    :rtype: dict

ReturnsResponse Syntax
{
    'LoadBalancers': [
        {
            'LoadBalancerArn': 'string',
            'DNSName': 'string',
            'CanonicalHostedZoneId': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'LoadBalancerName': 'string',
            'Scheme': 'internet-facing'|'internal',
            'VpcId': 'string',
            'State': {
                'Code': 'active'|'provisioning'|'active_impaired'|'failed',
                'Reason': 'string'
            },
            'Type': 'application'|'network',
            'AvailabilityZones': [
                {
                    'ZoneName': 'string',
                    'SubnetId': 'string',
                    'LoadBalancerAddresses': [
                        {
                            'IpAddress': 'string',
                            'AllocationId': 'string',
                            'PrivateIPv4Address': 'string'
                        },
                    ]
                },
            ],
            'SecurityGroups': [
                'string',
            ],
            'IpAddressType': 'ipv4'|'dualstack'
        },
    ],
    'NextMarker': 'string'
}


Response Structure

(dict) --

LoadBalancers (list) --
Information about the load balancers.

(dict) --
Information about a load balancer.

LoadBalancerArn (string) --
The Amazon Resource Name (ARN) of the load balancer.

DNSName (string) --
The public DNS name of the load balancer.

CanonicalHostedZoneId (string) --
The ID of the Amazon Route 53 hosted zone associated with the load balancer.

CreatedTime (datetime) --
The date and time the load balancer was created.

LoadBalancerName (string) --
The name of the load balancer.

Scheme (string) --
The nodes of an Internet-facing load balancer have public IP addresses. The DNS name of an Internet-facing load balancer is publicly resolvable to the public IP addresses of the nodes. Therefore, Internet-facing load balancers can route requests from clients over the internet.
The nodes of an internal load balancer have only private IP addresses. The DNS name of an internal load balancer is publicly resolvable to the private IP addresses of the nodes. Therefore, internal load balancers can route requests only from clients with access to the VPC for the load balancer.

VpcId (string) --
The ID of the VPC for the load balancer.

State (dict) --
The state of the load balancer.

Code (string) --
The state code. The initial state of the load balancer is provisioning . After the load balancer is fully set up and ready to route traffic, its state is active . If the load balancer could not be set up, its state is failed .

Reason (string) --
A description of the state.



Type (string) --
The type of load balancer.

AvailabilityZones (list) --
The Availability Zones for the load balancer.

(dict) --
Information about an Availability Zone.

ZoneName (string) --
The name of the Availability Zone.

SubnetId (string) --
The ID of the subnet. You can specify one subnet per Availability Zone.

LoadBalancerAddresses (list) --
[Network Load Balancers] If you need static IP addresses for your load balancer, you can specify one Elastic IP address per Availability Zone when you create an internal-facing load balancer. For internal load balancers, you can specify a private IP address from the IPv4 range of the subnet.

(dict) --
Information about a static IP address for a load balancer.

IpAddress (string) --
The static IP address.

AllocationId (string) --
[Network Load Balancers] The allocation ID of the Elastic IP address for an internal-facing load balancer.

PrivateIPv4Address (string) --
[Network Load Balancers] The private IPv4 address for an internal load balancer.









SecurityGroups (list) --
The IDs of the security groups for the load balancer.

(string) --


IpAddressType (string) --
The type of IP addresses used by the subnets for your load balancer. The possible values are ipv4 (for IPv4 addresses) and dualstack (for IPv4 and IPv6 addresses).





NextMarker (string) --
If there are additional results, this is the marker for the next set of results. Otherwise, this is null.







Exceptions

ElasticLoadBalancingv2.Client.exceptions.LoadBalancerNotFoundException

Examples
This example describes the specified load balancer.
response = client.describe_load_balancers(
    LoadBalancerArns=[
        'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
    ],
)

print(response)


Expected Output:
{
    'LoadBalancers': [
        {
            'AvailabilityZones': [
                {
                    'SubnetId': 'subnet-8360a9e7',
                    'ZoneName': 'us-west-2a',
                },
                {
                    'SubnetId': 'subnet-b7d581c0',
                    'ZoneName': 'us-west-2b',
                },
            ],
            'CanonicalHostedZoneId': 'Z2P70J7EXAMPLE',
            'CreatedTime': datetime(2016, 3, 25, 21, 26, 12, 4, 85, 0),
            'DNSName': 'my-load-balancer-424835706.us-west-2.elb.amazonaws.com',
            'LoadBalancerArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
            'LoadBalancerName': 'my-load-balancer',
            'Scheme': 'internet-facing',
            'SecurityGroups': [
                'sg-5943793c',
            ],
            'State': {
                'Code': 'active',
            },
            'Type': 'application',
            'VpcId': 'vpc-3ac0fb5f',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'LoadBalancers': [
            {
                'LoadBalancerArn': 'string',
                'DNSName': 'string',
                'CanonicalHostedZoneId': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'LoadBalancerName': 'string',
                'Scheme': 'internet-facing'|'internal',
                'VpcId': 'string',
                'State': {
                    'Code': 'active'|'provisioning'|'active_impaired'|'failed',
                    'Reason': 'string'
                },
                'Type': 'application'|'network',
                'AvailabilityZones': [
                    {
                        'ZoneName': 'string',
                        'SubnetId': 'string',
                        'LoadBalancerAddresses': [
                            {
                                'IpAddress': 'string',
                                'AllocationId': 'string',
                                'PrivateIPv4Address': 'string'
                            },
                        ]
                    },
                ],
                'SecurityGroups': [
                    'string',
                ],
                'IpAddressType': 'ipv4'|'dualstack'
            },
        ],
        'NextMarker': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_rules(ListenerArn=None, RuleArns=None, Marker=None, PageSize=None):
    """
    Describes the specified rules or the rules for the specified listener. You must specify either a listener or one or more rules.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the specified rule.
    Expected Output:
    
    :example: response = client.describe_rules(
        ListenerArn='string',
        RuleArns=[
            'string',
        ],
        Marker='string',
        PageSize=123
    )
    
    
    :type ListenerArn: string
    :param ListenerArn: The Amazon Resource Name (ARN) of the listener.

    :type RuleArns: list
    :param RuleArns: The Amazon Resource Names (ARN) of the rules.\n\n(string) --\n\n

    :type Marker: string
    :param Marker: The marker for the next set of results. (You received this marker from a previous call.)

    :type PageSize: integer
    :param PageSize: The maximum number of results to return with this call.

    :rtype: dict

ReturnsResponse Syntax
{
    'Rules': [
        {
            'RuleArn': 'string',
            'Priority': 'string',
            'Conditions': [
                {
                    'Field': 'string',
                    'Values': [
                        'string',
                    ],
                    'HostHeaderConfig': {
                        'Values': [
                            'string',
                        ]
                    },
                    'PathPatternConfig': {
                        'Values': [
                            'string',
                        ]
                    },
                    'HttpHeaderConfig': {
                        'HttpHeaderName': 'string',
                        'Values': [
                            'string',
                        ]
                    },
                    'QueryStringConfig': {
                        'Values': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                    'HttpRequestMethodConfig': {
                        'Values': [
                            'string',
                        ]
                    },
                    'SourceIpConfig': {
                        'Values': [
                            'string',
                        ]
                    }
                },
            ],
            'Actions': [
                {
                    'Type': 'forward'|'authenticate-oidc'|'authenticate-cognito'|'redirect'|'fixed-response',
                    'TargetGroupArn': 'string',
                    'AuthenticateOidcConfig': {
                        'Issuer': 'string',
                        'AuthorizationEndpoint': 'string',
                        'TokenEndpoint': 'string',
                        'UserInfoEndpoint': 'string',
                        'ClientId': 'string',
                        'ClientSecret': 'string',
                        'SessionCookieName': 'string',
                        'Scope': 'string',
                        'SessionTimeout': 123,
                        'AuthenticationRequestExtraParams': {
                            'string': 'string'
                        },
                        'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate',
                        'UseExistingClientSecret': True|False
                    },
                    'AuthenticateCognitoConfig': {
                        'UserPoolArn': 'string',
                        'UserPoolClientId': 'string',
                        'UserPoolDomain': 'string',
                        'SessionCookieName': 'string',
                        'Scope': 'string',
                        'SessionTimeout': 123,
                        'AuthenticationRequestExtraParams': {
                            'string': 'string'
                        },
                        'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate'
                    },
                    'Order': 123,
                    'RedirectConfig': {
                        'Protocol': 'string',
                        'Port': 'string',
                        'Host': 'string',
                        'Path': 'string',
                        'Query': 'string',
                        'StatusCode': 'HTTP_301'|'HTTP_302'
                    },
                    'FixedResponseConfig': {
                        'MessageBody': 'string',
                        'StatusCode': 'string',
                        'ContentType': 'string'
                    },
                    'ForwardConfig': {
                        'TargetGroups': [
                            {
                                'TargetGroupArn': 'string',
                                'Weight': 123
                            },
                        ],
                        'TargetGroupStickinessConfig': {
                            'Enabled': True|False,
                            'DurationSeconds': 123
                        }
                    }
                },
            ],
            'IsDefault': True|False
        },
    ],
    'NextMarker': 'string'
}


Response Structure

(dict) --

Rules (list) --
Information about the rules.

(dict) --
Information about a rule.

RuleArn (string) --
The Amazon Resource Name (ARN) of the rule.

Priority (string) --
The priority.

Conditions (list) --
The conditions. Each rule can include zero or one of the following conditions: http-request-method , host-header , path-pattern , and source-ip , and zero or more of the following conditions: http-header and query-string .

(dict) --
Information about a condition for a rule.

Field (string) --
The field in the HTTP request. The following are the possible values:

http-header
http-request-method
host-header
path-pattern
query-string
source-ip


Values (list) --
The condition value. You can use Values if the rule contains only host-header and path-pattern conditions. Otherwise, you can use HostHeaderConfig for host-header conditions and PathPatternConfig for path-pattern conditions.
If Field is host-header , you can specify a single host name (for example, my.example.com). A host name is case insensitive, can be up to 128 characters in length, and can contain any of the following characters.

A-Z, a-z, 0-9

.



(matches 0 or more characters)


? (matches exactly 1 character)

If Field is path-pattern , you can specify a single path pattern (for example, /img/*). A path pattern is case-sensitive, can be up to 128 characters in length, and can contain any of the following characters.

A-Z, a-z, 0-9
_ - . $ / ~ " \' @ : +
& (using &amp;)

(matches 0 or more characters)


? (matches exactly 1 character)


(string) --


HostHeaderConfig (dict) --
Information for a host header condition. Specify only when Field is host-header .

Values (list) --
One or more host names. The maximum size of each name is 128 characters. The comparison is case insensitive. The following wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly 1 character).
If you specify multiple strings, the condition is satisfied if one of the strings matches the host name.

(string) --




PathPatternConfig (dict) --
Information for a path pattern condition. Specify only when Field is path-pattern .

Values (list) --
One or more path patterns to compare against the request URL. The maximum size of each string is 128 characters. The comparison is case sensitive. The following wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly 1 character).
If you specify multiple strings, the condition is satisfied if one of them matches the request URL. The path pattern is compared only to the path of the URL, not to its query string. To compare against the query string, use  QueryStringConditionConfig .

(string) --




HttpHeaderConfig (dict) --
Information for an HTTP header condition. Specify only when Field is http-header .

HttpHeaderName (string) --
The name of the HTTP header field. The maximum size is 40 characters. The header name is case insensitive. The allowed characters are specified by RFC 7230. Wildcards are not supported.
You can\'t use an HTTP header condition to specify the host header. Use  HostHeaderConditionConfig to specify a host header condition.

Values (list) --
One or more strings to compare against the value of the HTTP header. The maximum size of each string is 128 characters. The comparison strings are case insensitive. The following wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly 1 character).
If the same header appears multiple times in the request, we search them in order until a match is found.
If you specify multiple strings, the condition is satisfied if one of the strings matches the value of the HTTP header. To require that all of the strings are a match, create one condition per string.

(string) --




QueryStringConfig (dict) --
Information for a query string condition. Specify only when Field is query-string .

Values (list) --
One or more key/value pairs or values to find in the query string. The maximum size of each string is 128 characters. The comparison is case insensitive. The following wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly 1 character). To search for a literal \'*\' or \'?\' character in a query string, you must escape these characters in Values using a \'\' character.
If you specify multiple key/value pairs or values, the condition is satisfied if one of them is found in the query string.

(dict) --
Information about a key/value pair.

Key (string) --
The key. You can omit the key.

Value (string) --
The value.







HttpRequestMethodConfig (dict) --
Information for an HTTP method condition. Specify only when Field is http-request-method .

Values (list) --
The name of the request method. The maximum size is 40 characters. The allowed characters are A-Z, hyphen (-), and underscore (_). The comparison is case sensitive. Wildcards are not supported; therefore, the method name must be an exact match.
If you specify multiple strings, the condition is satisfied if one of the strings matches the HTTP request method. We recommend that you route GET and HEAD requests in the same way, because the response to a HEAD request may be cached.

(string) --




SourceIpConfig (dict) --
Information for a source IP condition. Specify only when Field is source-ip .

Values (list) --
One or more source IP addresses, in CIDR format. You can use both IPv4 and IPv6 addresses. Wildcards are not supported.
If you specify multiple addresses, the condition is satisfied if the source IP address of the request matches one of the CIDR blocks. This condition is not satisfied by the addresses in the X-Forwarded-For header. To search for addresses in the X-Forwarded-For header, use  HttpHeaderConditionConfig .

(string) --








Actions (list) --
The actions. Each rule must include exactly one of the following types of actions: forward , redirect , or fixed-response , and it must be the last action to be performed.

(dict) --
Information about an action.

Type (string) --
The type of action.

TargetGroupArn (string) --
The Amazon Resource Name (ARN) of the target group. Specify only when Type is forward and you want to route to a single target group. To route to one or more target groups, use ForwardConfig instead.

AuthenticateOidcConfig (dict) --
[HTTPS listeners] Information about an identity provider that is compliant with OpenID Connect (OIDC). Specify only when Type is authenticate-oidc .

Issuer (string) --
The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

AuthorizationEndpoint (string) --
The authorization endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

TokenEndpoint (string) --
The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

UserInfoEndpoint (string) --
The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

ClientId (string) --
The OAuth 2.0 client identifier.

ClientSecret (string) --
The OAuth 2.0 client secret. This parameter is required if you are creating a rule. If you are modifying a rule, you can omit this parameter if you set UseExistingClientSecret to true.

SessionCookieName (string) --
The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.

Scope (string) --
The set of user claims to be requested from the IdP. The default is openid .
To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.

SessionTimeout (integer) --
The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).

AuthenticationRequestExtraParams (dict) --
The query parameters (up to 10) to include in the redirect request to the authorization endpoint.

(string) --
(string) --




OnUnauthenticatedRequest (string) --
The behavior if the user is not authenticated. The following are possible values:

deny- Return an HTTP 401 Unauthorized error.
allow- Allow the request to be forwarded to the target.
authenticate- Redirect the request to the IdP authorization endpoint. This is the default value.


UseExistingClientSecret (boolean) --
Indicates whether to use the existing client secret when modifying a rule. If you are creating a rule, you can omit this parameter or set it to false.



AuthenticateCognitoConfig (dict) --
[HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify only when Type is authenticate-cognito .

UserPoolArn (string) --
The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

UserPoolClientId (string) --
The ID of the Amazon Cognito user pool client.

UserPoolDomain (string) --
The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

SessionCookieName (string) --
The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.

Scope (string) --
The set of user claims to be requested from the IdP. The default is openid .
To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.

SessionTimeout (integer) --
The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).

AuthenticationRequestExtraParams (dict) --
The query parameters (up to 10) to include in the redirect request to the authorization endpoint.

(string) --
(string) --




OnUnauthenticatedRequest (string) --
The behavior if the user is not authenticated. The following are possible values:

deny- Return an HTTP 401 Unauthorized error.
allow- Allow the request to be forwarded to the target.
authenticate- Redirect the request to the IdP authorization endpoint. This is the default value.




Order (integer) --
The order for the action. This value is required for rules with multiple actions. The action with the lowest value for order is performed first. The last action to be performed must be one of the following types of actions: a forward , fixed-response , or redirect .

RedirectConfig (dict) --
[Application Load Balancer] Information for creating a redirect action. Specify only when Type is redirect .

Protocol (string) --
The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

Port (string) --
The port. You can specify a value from 1 to 65535 or #{port}.

Host (string) --
The hostname. This component is not percent-encoded. The hostname can contain #{host}.

Path (string) --
The absolute path, starting with the leading "/". This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}.

Query (string) --
The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading "?", as it is automatically added. You can specify any of the reserved keywords.

StatusCode (string) --
The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).



FixedResponseConfig (dict) --
[Application Load Balancer] Information for creating an action that returns a custom HTTP response. Specify only when Type is fixed-response .

MessageBody (string) --
The message.

StatusCode (string) --
The HTTP response code (2XX, 4XX, or 5XX).

ContentType (string) --
The content type.
Valid Values: text/plain | text/css | text/html | application/javascript | application/json



ForwardConfig (dict) --
Information for creating an action that distributes requests among one or more target groups. For Network Load Balancers, you can specify a single target group. Specify only when Type is forward . If you specify both ForwardConfig and TargetGroupArn , you can specify only one target group using ForwardConfig and it must be the same target group specified in TargetGroupArn .

TargetGroups (list) --
One or more target groups. For Network Load Balancers, you can specify a single target group.

(dict) --
Information about how traffic will be distributed between multiple target groups in a forward rule.

TargetGroupArn (string) --
The Amazon Resource Name (ARN) of the target group.

Weight (integer) --
The weight. The range is 0 to 999.





TargetGroupStickinessConfig (dict) --
The target group stickiness for the rule.

Enabled (boolean) --
Indicates whether target group stickiness is enabled.

DurationSeconds (integer) --
The time period, in seconds, during which requests from a client should be routed to the same target group. The range is 1-604800 seconds (7 days).









IsDefault (boolean) --
Indicates whether this is the default rule.





NextMarker (string) --
If there are additional results, this is the marker for the next set of results. Otherwise, this is null.







Exceptions

ElasticLoadBalancingv2.Client.exceptions.ListenerNotFoundException
ElasticLoadBalancingv2.Client.exceptions.RuleNotFoundException
ElasticLoadBalancingv2.Client.exceptions.UnsupportedProtocolException

Examples
This example describes the specified rule.
response = client.describe_rules(
    RuleArns=[
        'arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/9683b2d02a6cabee',
    ],
)

print(response)


Expected Output:
{
    'Rules': [
        {
            'Actions': [
                {
                    'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
                    'Type': 'forward',
                },
            ],
            'Conditions': [
                {
                    'Field': 'path-pattern',
                    'Values': [
                        '/img/*',
                    ],
                },
            ],
            'IsDefault': False,
            'Priority': '10',
            'RuleArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/9683b2d02a6cabee',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Rules': [
            {
                'RuleArn': 'string',
                'Priority': 'string',
                'Conditions': [
                    {
                        'Field': 'string',
                        'Values': [
                            'string',
                        ],
                        'HostHeaderConfig': {
                            'Values': [
                                'string',
                            ]
                        },
                        'PathPatternConfig': {
                            'Values': [
                                'string',
                            ]
                        },
                        'HttpHeaderConfig': {
                            'HttpHeaderName': 'string',
                            'Values': [
                                'string',
                            ]
                        },
                        'QueryStringConfig': {
                            'Values': [
                                {
                                    'Key': 'string',
                                    'Value': 'string'
                                },
                            ]
                        },
                        'HttpRequestMethodConfig': {
                            'Values': [
                                'string',
                            ]
                        },
                        'SourceIpConfig': {
                            'Values': [
                                'string',
                            ]
                        }
                    },
                ],
                'Actions': [
                    {
                        'Type': 'forward'|'authenticate-oidc'|'authenticate-cognito'|'redirect'|'fixed-response',
                        'TargetGroupArn': 'string',
                        'AuthenticateOidcConfig': {
                            'Issuer': 'string',
                            'AuthorizationEndpoint': 'string',
                            'TokenEndpoint': 'string',
                            'UserInfoEndpoint': 'string',
                            'ClientId': 'string',
                            'ClientSecret': 'string',
                            'SessionCookieName': 'string',
                            'Scope': 'string',
                            'SessionTimeout': 123,
                            'AuthenticationRequestExtraParams': {
                                'string': 'string'
                            },
                            'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate',
                            'UseExistingClientSecret': True|False
                        },
                        'AuthenticateCognitoConfig': {
                            'UserPoolArn': 'string',
                            'UserPoolClientId': 'string',
                            'UserPoolDomain': 'string',
                            'SessionCookieName': 'string',
                            'Scope': 'string',
                            'SessionTimeout': 123,
                            'AuthenticationRequestExtraParams': {
                                'string': 'string'
                            },
                            'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate'
                        },
                        'Order': 123,
                        'RedirectConfig': {
                            'Protocol': 'string',
                            'Port': 'string',
                            'Host': 'string',
                            'Path': 'string',
                            'Query': 'string',
                            'StatusCode': 'HTTP_301'|'HTTP_302'
                        },
                        'FixedResponseConfig': {
                            'MessageBody': 'string',
                            'StatusCode': 'string',
                            'ContentType': 'string'
                        },
                        'ForwardConfig': {
                            'TargetGroups': [
                                {
                                    'TargetGroupArn': 'string',
                                    'Weight': 123
                                },
                            ],
                            'TargetGroupStickinessConfig': {
                                'Enabled': True|False,
                                'DurationSeconds': 123
                            }
                        }
                    },
                ],
                'IsDefault': True|False
            },
        ],
        'NextMarker': 'string'
    }
    
    
    :returns: 
    http-header
    http-request-method
    host-header
    path-pattern
    query-string
    source-ip
    
    """
    pass

def describe_ssl_policies(Names=None, Marker=None, PageSize=None):
    """
    Describes the specified policies or all policies used for SSL negotiation.
    For more information, see Security Policies in the Application Load Balancers Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the specified policy used for SSL negotiation.
    Expected Output:
    
    :example: response = client.describe_ssl_policies(
        Names=[
            'string',
        ],
        Marker='string',
        PageSize=123
    )
    
    
    :type Names: list
    :param Names: The names of the policies.\n\n(string) --\n\n

    :type Marker: string
    :param Marker: The marker for the next set of results. (You received this marker from a previous call.)

    :type PageSize: integer
    :param PageSize: The maximum number of results to return with this call.

    :rtype: dict

ReturnsResponse Syntax
{
    'SslPolicies': [
        {
            'SslProtocols': [
                'string',
            ],
            'Ciphers': [
                {
                    'Name': 'string',
                    'Priority': 123
                },
            ],
            'Name': 'string'
        },
    ],
    'NextMarker': 'string'
}


Response Structure

(dict) --

SslPolicies (list) --
Information about the security policies.

(dict) --
Information about a policy used for SSL negotiation.

SslProtocols (list) --
The protocols.

(string) --


Ciphers (list) --
The ciphers.

(dict) --
Information about a cipher used in a policy.

Name (string) --
The name of the cipher.

Priority (integer) --
The priority of the cipher.





Name (string) --
The name of the policy.





NextMarker (string) --
If there are additional results, this is the marker for the next set of results. Otherwise, this is null.







Exceptions

ElasticLoadBalancingv2.Client.exceptions.SSLPolicyNotFoundException

Examples
This example describes the specified policy used for SSL negotiation.
response = client.describe_ssl_policies(
    Names=[
        'ELBSecurityPolicy-2015-05',
    ],
)

print(response)


Expected Output:
{
    'SslPolicies': [
        {
            'Ciphers': [
                {
                    'Name': 'ECDHE-ECDSA-AES128-GCM-SHA256',
                    'Priority': 1,
                },
                {
                    'Name': 'ECDHE-RSA-AES128-GCM-SHA256',
                    'Priority': 2,
                },
                {
                    'Name': 'ECDHE-ECDSA-AES128-SHA256',
                    'Priority': 3,
                },
                {
                    'Name': 'ECDHE-RSA-AES128-SHA256',
                    'Priority': 4,
                },
                {
                    'Name': 'ECDHE-ECDSA-AES128-SHA',
                    'Priority': 5,
                },
                {
                    'Name': 'ECDHE-RSA-AES128-SHA',
                    'Priority': 6,
                },
                {
                    'Name': 'DHE-RSA-AES128-SHA',
                    'Priority': 7,
                },
                {
                    'Name': 'ECDHE-ECDSA-AES256-GCM-SHA384',
                    'Priority': 8,
                },
                {
                    'Name': 'ECDHE-RSA-AES256-GCM-SHA384',
                    'Priority': 9,
                },
                {
                    'Name': 'ECDHE-ECDSA-AES256-SHA384',
                    'Priority': 10,
                },
                {
                    'Name': 'ECDHE-RSA-AES256-SHA384',
                    'Priority': 11,
                },
                {
                    'Name': 'ECDHE-RSA-AES256-SHA',
                    'Priority': 12,
                },
                {
                    'Name': 'ECDHE-ECDSA-AES256-SHA',
                    'Priority': 13,
                },
                {
                    'Name': 'AES128-GCM-SHA256',
                    'Priority': 14,
                },
                {
                    'Name': 'AES128-SHA256',
                    'Priority': 15,
                },
                {
                    'Name': 'AES128-SHA',
                    'Priority': 16,
                },
                {
                    'Name': 'AES256-GCM-SHA384',
                    'Priority': 17,
                },
                {
                    'Name': 'AES256-SHA256',
                    'Priority': 18,
                },
                {
                    'Name': 'AES256-SHA',
                    'Priority': 19,
                },
            ],
            'Name': 'ELBSecurityPolicy-2015-05',
            'SslProtocols': [
                'TLSv1',
                'TLSv1.1',
                'TLSv1.2',
            ],
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'SslPolicies': [
            {
                'SslProtocols': [
                    'string',
                ],
                'Ciphers': [
                    {
                        'Name': 'string',
                        'Priority': 123
                    },
                ],
                'Name': 'string'
            },
        ],
        'NextMarker': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_tags(ResourceArns=None):
    """
    Describes the tags for the specified resources. You can describe the tags for one or more Application Load Balancers, Network Load Balancers, and target groups.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the tags assigned to the specified load balancer.
    Expected Output:
    
    :example: response = client.describe_tags(
        ResourceArns=[
            'string',
        ]
    )
    
    
    :type ResourceArns: list
    :param ResourceArns: [REQUIRED]\nThe Amazon Resource Names (ARN) of the resources. You can specify up to 20 resources in a single call.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'TagDescriptions': [
        {
            'ResourceArn': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        },
    ]
}


Response Structure

(dict) --
TagDescriptions (list) --Information about the tags.

(dict) --The tags associated with a resource.

ResourceArn (string) --The Amazon Resource Name (ARN) of the resource.

Tags (list) --Information about the tags.

(dict) --Information about a tag.

Key (string) --The key of the tag.

Value (string) --The value of the tag.














Exceptions

ElasticLoadBalancingv2.Client.exceptions.LoadBalancerNotFoundException
ElasticLoadBalancingv2.Client.exceptions.TargetGroupNotFoundException
ElasticLoadBalancingv2.Client.exceptions.ListenerNotFoundException
ElasticLoadBalancingv2.Client.exceptions.RuleNotFoundException

Examples
This example describes the tags assigned to the specified load balancer.
response = client.describe_tags(
    ResourceArns=[
        'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
    ],
)

print(response)


Expected Output:
{
    'TagDescriptions': [
        {
            'ResourceArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
            'Tags': [
                {
                    'Key': 'project',
                    'Value': 'lima',
                },
                {
                    'Key': 'department',
                    'Value': 'digital-media',
                },
            ],
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'TagDescriptions': [
            {
                'ResourceArn': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    ElasticLoadBalancingv2.Client.exceptions.LoadBalancerNotFoundException
    ElasticLoadBalancingv2.Client.exceptions.TargetGroupNotFoundException
    ElasticLoadBalancingv2.Client.exceptions.ListenerNotFoundException
    ElasticLoadBalancingv2.Client.exceptions.RuleNotFoundException
    
    """
    pass

def describe_target_group_attributes(TargetGroupArn=None):
    """
    Describes the attributes for the specified target group.
    For more information, see Target Group Attributes in the Application Load Balancers Guide or Target Group Attributes in the Network Load Balancers Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the attributes of the specified target group.
    Expected Output:
    
    :example: response = client.describe_target_group_attributes(
        TargetGroupArn='string'
    )
    
    
    :type TargetGroupArn: string
    :param TargetGroupArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the target group.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Attributes': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --
Attributes (list) --Information about the target group attributes

(dict) --Information about a target group attribute.

Key (string) --The name of the attribute.
The following attributes are supported by both Application Load Balancers and Network Load Balancers:

deregistration_delay.timeout_seconds - The amount of time, in seconds, for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused . The range is 0-3600 seconds. The default value is 300 seconds. If the target is a Lambda function, this attribute is not supported.
stickiness.enabled - Indicates whether sticky sessions are enabled. The value is true or false . The default is false .
stickiness.type - The type of sticky sessions. The possible values are lb_cookie for Application Load Balancers or source_ip for Network Load Balancers.

The following attributes are supported only if the load balancer is an Application Load Balancer and the target is an instance or an IP address:

load_balancing.algorithm.type - The load balancing algorithm determines how the load balancer selects targets when routing requests. The value is round_robin or least_outstanding_requests . The default is round_robin .
slow_start.duration_seconds - The time period, in seconds, during which a newly registered target receives an increasing share of the traffic to the target group. After this time period ends, the target receives its full share of traffic. The range is 30-900 seconds (15 minutes). Slow start mode is disabled by default.
stickiness.lb_cookie.duration_seconds - The time period, in seconds, during which requests from a client should be routed to the same target. After this time period expires, the load balancer-generated cookie is considered stale. The range is 1 second to 1 week (604800 seconds). The default value is 1 day (86400 seconds).

The following attribute is supported only if the load balancer is an Application Load Balancer and the target is a Lambda function:

lambda.multi_value_headers.enabled - Indicates whether the request and response headers that are exchanged between the load balancer and the Lambda function include arrays of values or strings. The value is true or false . The default is false . If the value is false and the request contains a duplicate header field name or query parameter key, the load balancer uses the last value sent by the client.

The following attribute is supported only by Network Load Balancers:

proxy_protocol_v2.enabled - Indicates whether Proxy Protocol version 2 is enabled. The value is true or false . The default is false .


Value (string) --The value of the attribute.










Exceptions

ElasticLoadBalancingv2.Client.exceptions.TargetGroupNotFoundException

Examples
This example describes the attributes of the specified target group.
response = client.describe_target_group_attributes(
    TargetGroupArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
)

print(response)


Expected Output:
{
    'Attributes': [
        {
            'Key': 'stickiness.enabled',
            'Value': 'false',
        },
        {
            'Key': 'deregistration_delay.timeout_seconds',
            'Value': '300',
        },
        {
            'Key': 'stickiness.type',
            'Value': 'lb_cookie',
        },
        {
            'Key': 'stickiness.lb_cookie.duration_seconds',
            'Value': '86400',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Attributes': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    :returns: 
    load_balancing.algorithm.type - The load balancing algorithm determines how the load balancer selects targets when routing requests. The value is round_robin or least_outstanding_requests . The default is round_robin .
    slow_start.duration_seconds - The time period, in seconds, during which a newly registered target receives an increasing share of the traffic to the target group. After this time period ends, the target receives its full share of traffic. The range is 30-900 seconds (15 minutes). Slow start mode is disabled by default.
    stickiness.lb_cookie.duration_seconds - The time period, in seconds, during which requests from a client should be routed to the same target. After this time period expires, the load balancer-generated cookie is considered stale. The range is 1 second to 1 week (604800 seconds). The default value is 1 day (86400 seconds).
    
    """
    pass

def describe_target_groups(LoadBalancerArn=None, TargetGroupArns=None, Names=None, Marker=None, PageSize=None):
    """
    Describes the specified target groups or all of your target groups. By default, all target groups are described. Alternatively, you can specify one of the following to filter the results: the ARN of the load balancer, the names of one or more target groups, or the ARNs of one or more target groups.
    To describe the targets for a target group, use  DescribeTargetHealth . To describe the attributes of a target group, use  DescribeTargetGroupAttributes .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the specified target group.
    Expected Output:
    
    :example: response = client.describe_target_groups(
        LoadBalancerArn='string',
        TargetGroupArns=[
            'string',
        ],
        Names=[
            'string',
        ],
        Marker='string',
        PageSize=123
    )
    
    
    :type LoadBalancerArn: string
    :param LoadBalancerArn: The Amazon Resource Name (ARN) of the load balancer.

    :type TargetGroupArns: list
    :param TargetGroupArns: The Amazon Resource Names (ARN) of the target groups.\n\n(string) --\n\n

    :type Names: list
    :param Names: The names of the target groups.\n\n(string) --\n\n

    :type Marker: string
    :param Marker: The marker for the next set of results. (You received this marker from a previous call.)

    :type PageSize: integer
    :param PageSize: The maximum number of results to return with this call.

    :rtype: dict

ReturnsResponse Syntax
{
    'TargetGroups': [
        {
            'TargetGroupArn': 'string',
            'TargetGroupName': 'string',
            'Protocol': 'HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
            'Port': 123,
            'VpcId': 'string',
            'HealthCheckProtocol': 'HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
            'HealthCheckPort': 'string',
            'HealthCheckEnabled': True|False,
            'HealthCheckIntervalSeconds': 123,
            'HealthCheckTimeoutSeconds': 123,
            'HealthyThresholdCount': 123,
            'UnhealthyThresholdCount': 123,
            'HealthCheckPath': 'string',
            'Matcher': {
                'HttpCode': 'string'
            },
            'LoadBalancerArns': [
                'string',
            ],
            'TargetType': 'instance'|'ip'|'lambda'
        },
    ],
    'NextMarker': 'string'
}


Response Structure

(dict) --

TargetGroups (list) --
Information about the target groups.

(dict) --
Information about a target group.

TargetGroupArn (string) --
The Amazon Resource Name (ARN) of the target group.

TargetGroupName (string) --
The name of the target group.

Protocol (string) --
The protocol to use for routing traffic to the targets.

Port (integer) --
The port on which the targets are listening. Not used if the target is a Lambda function.

VpcId (string) --
The ID of the VPC for the targets.

HealthCheckProtocol (string) --
The protocol to use to connect with the target.

HealthCheckPort (string) --
The port to use to connect with the target.

HealthCheckEnabled (boolean) --
Indicates whether health checks are enabled.

HealthCheckIntervalSeconds (integer) --
The approximate amount of time, in seconds, between health checks of an individual target.

HealthCheckTimeoutSeconds (integer) --
The amount of time, in seconds, during which no response means a failed health check.

HealthyThresholdCount (integer) --
The number of consecutive health checks successes required before considering an unhealthy target healthy.

UnhealthyThresholdCount (integer) --
The number of consecutive health check failures required before considering the target unhealthy.

HealthCheckPath (string) --
The destination for the health check request.

Matcher (dict) --
The HTTP codes to use when checking for a successful response from a target.

HttpCode (string) --
The HTTP codes.
For Application Load Balancers, you can specify values between 200 and 499, and the default value is 200. You can specify multiple values (for example, "200,202") or a range of values (for example, "200-299").
For Network Load Balancers, this is 200\xe2\x80\x93399.



LoadBalancerArns (list) --
The Amazon Resource Names (ARN) of the load balancers that route traffic to this target group.

(string) --


TargetType (string) --
The type of target that you must specify when registering targets with this target group. The possible values are instance (targets are specified by instance ID) or ip (targets are specified by IP address).





NextMarker (string) --
If there are additional results, this is the marker for the next set of results. Otherwise, this is null.







Exceptions

ElasticLoadBalancingv2.Client.exceptions.LoadBalancerNotFoundException
ElasticLoadBalancingv2.Client.exceptions.TargetGroupNotFoundException

Examples
This example describes the specified target group.
response = client.describe_target_groups(
    TargetGroupArns=[
        'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
    ],
)

print(response)


Expected Output:
{
    'TargetGroups': [
        {
            'HealthCheckIntervalSeconds': 30,
            'HealthCheckPath': '/',
            'HealthCheckPort': 'traffic-port',
            'HealthCheckProtocol': 'HTTP',
            'HealthCheckTimeoutSeconds': 5,
            'HealthyThresholdCount': 5,
            'LoadBalancerArns': [
                'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
            ],
            'Matcher': {
                'HttpCode': '200',
            },
            'Port': 80,
            'Protocol': 'HTTP',
            'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
            'TargetGroupName': 'my-targets',
            'UnhealthyThresholdCount': 2,
            'VpcId': 'vpc-3ac0fb5f',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'TargetGroups': [
            {
                'TargetGroupArn': 'string',
                'TargetGroupName': 'string',
                'Protocol': 'HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
                'Port': 123,
                'VpcId': 'string',
                'HealthCheckProtocol': 'HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
                'HealthCheckPort': 'string',
                'HealthCheckEnabled': True|False,
                'HealthCheckIntervalSeconds': 123,
                'HealthCheckTimeoutSeconds': 123,
                'HealthyThresholdCount': 123,
                'UnhealthyThresholdCount': 123,
                'HealthCheckPath': 'string',
                'Matcher': {
                    'HttpCode': 'string'
                },
                'LoadBalancerArns': [
                    'string',
                ],
                'TargetType': 'instance'|'ip'|'lambda'
            },
        ],
        'NextMarker': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_target_health(TargetGroupArn=None, Targets=None):
    """
    Describes the health of the specified targets or all of your targets.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the health of the targets for the specified target group. One target is healthy but the other is not specified in an action, so it can\'t receive traffic from the load balancer.
    Expected Output:
    This example describes the health of the specified target. This target is healthy.
    Expected Output:
    
    :example: response = client.describe_target_health(
        TargetGroupArn='string',
        Targets=[
            {
                'Id': 'string',
                'Port': 123,
                'AvailabilityZone': 'string'
            },
        ]
    )
    
    
    :type TargetGroupArn: string
    :param TargetGroupArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the target group.\n

    :type Targets: list
    :param Targets: The targets.\n\n(dict) --Information about a target.\n\nId (string) -- [REQUIRED]The ID of the target. If the target type of the target group is instance , specify an instance ID. If the target type is ip , specify an IP address. If the target type is lambda , specify the ARN of the Lambda function.\n\nPort (integer) --The port on which the target is listening. Not used if the target is a Lambda function.\n\nAvailabilityZone (string) --An Availability Zone or all . This determines whether the target receives traffic from the load balancer nodes in the specified Availability Zone or from all enabled Availability Zones for the load balancer.\nThis parameter is not supported if the target type of the target group is instance .\nIf the target type is ip and the IP address is in a subnet of the VPC for the target group, the Availability Zone is automatically detected and this parameter is optional. If the IP address is outside the VPC, this parameter is required.\nWith an Application Load Balancer, if the target type is ip and the IP address is outside the VPC for the target group, the only supported value is all .\nIf the target type is lambda , this parameter is optional and the only supported value is all .\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TargetHealthDescriptions': [
        {
            'Target': {
                'Id': 'string',
                'Port': 123,
                'AvailabilityZone': 'string'
            },
            'HealthCheckPort': 'string',
            'TargetHealth': {
                'State': 'initial'|'healthy'|'unhealthy'|'unused'|'draining'|'unavailable',
                'Reason': 'Elb.RegistrationInProgress'|'Elb.InitialHealthChecking'|'Target.ResponseCodeMismatch'|'Target.Timeout'|'Target.FailedHealthChecks'|'Target.NotRegistered'|'Target.NotInUse'|'Target.DeregistrationInProgress'|'Target.InvalidState'|'Target.IpUnusable'|'Target.HealthCheckDisabled'|'Elb.InternalError',
                'Description': 'string'
            }
        },
    ]
}


Response Structure

(dict) --

TargetHealthDescriptions (list) --
Information about the health of the targets.

(dict) --
Information about the health of a target.

Target (dict) --
The description of the target.

Id (string) --
The ID of the target. If the target type of the target group is instance , specify an instance ID. If the target type is ip , specify an IP address. If the target type is lambda , specify the ARN of the Lambda function.

Port (integer) --
The port on which the target is listening. Not used if the target is a Lambda function.

AvailabilityZone (string) --
An Availability Zone or all . This determines whether the target receives traffic from the load balancer nodes in the specified Availability Zone or from all enabled Availability Zones for the load balancer.
This parameter is not supported if the target type of the target group is instance .
If the target type is ip and the IP address is in a subnet of the VPC for the target group, the Availability Zone is automatically detected and this parameter is optional. If the IP address is outside the VPC, this parameter is required.
With an Application Load Balancer, if the target type is ip and the IP address is outside the VPC for the target group, the only supported value is all .
If the target type is lambda , this parameter is optional and the only supported value is all .



HealthCheckPort (string) --
The port to use to connect with the target.

TargetHealth (dict) --
The health information for the target.

State (string) --
The state of the target.

Reason (string) --
The reason code.
If the target state is healthy , a reason code is not provided.
If the target state is initial , the reason code can be one of the following values:

Elb.RegistrationInProgress - The target is in the process of being registered with the load balancer.
Elb.InitialHealthChecking - The load balancer is still sending the target the minimum number of health checks required to determine its health status.

If the target state is unhealthy , the reason code can be one of the following values:

Target.ResponseCodeMismatch - The health checks did not return an expected HTTP code. Applies only to Application Load Balancers.
Target.Timeout - The health check requests timed out. Applies only to Application Load Balancers.
Target.FailedHealthChecks - The load balancer received an error while establishing a connection to the target or the target response was malformed.
Elb.InternalError - The health checks failed due to an internal error. Applies only to Application Load Balancers.

If the target state is unused , the reason code can be one of the following values:

Target.NotRegistered - The target is not registered with the target group.
Target.NotInUse - The target group is not used by any load balancer or the target is in an Availability Zone that is not enabled for its load balancer.
Target.InvalidState - The target is in the stopped or terminated state.
Target.IpUnusable - The target IP address is reserved for use by a load balancer.

If the target state is draining , the reason code can be the following value:

Target.DeregistrationInProgress - The target is in the process of being deregistered and the deregistration delay period has not expired.

If the target state is unavailable , the reason code can be the following value:

Target.HealthCheckDisabled - Health checks are disabled for the target group. Applies only to Application Load Balancers.
Elb.InternalError - Target health is unavailable due to an internal error. Applies only to Network Load Balancers.


Description (string) --
A description of the target health that provides additional details. If the state is healthy , a description is not provided.













Exceptions

ElasticLoadBalancingv2.Client.exceptions.InvalidTargetException
ElasticLoadBalancingv2.Client.exceptions.TargetGroupNotFoundException
ElasticLoadBalancingv2.Client.exceptions.HealthUnavailableException

Examples
This example describes the health of the targets for the specified target group. One target is healthy but the other is not specified in an action, so it can\'t receive traffic from the load balancer.
response = client.describe_target_health(
    TargetGroupArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
)

print(response)


Expected Output:
{
    'TargetHealthDescriptions': [
        {
            'Target': {
                'Id': 'i-0f76fade',
                'Port': 80,
            },
            'TargetHealth': {
                'Description': 'Given target group is not configured to receive traffic from ELB',
                'Reason': 'Target.NotInUse',
                'State': 'unused',
            },
        },
        {
            'HealthCheckPort': '80',
            'Target': {
                'Id': 'i-0f76fade',
                'Port': 80,
            },
            'TargetHealth': {
                'State': 'healthy',
            },
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}


This example describes the health of the specified target. This target is healthy.
response = client.describe_target_health(
    TargetGroupArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
    Targets=[
        {
            'Id': 'i-0f76fade',
            'Port': 80,
        },
    ],
)

print(response)


Expected Output:
{
    'TargetHealthDescriptions': [
        {
            'HealthCheckPort': '80',
            'Target': {
                'Id': 'i-0f76fade',
                'Port': 80,
            },
            'TargetHealth': {
                'State': 'healthy',
            },
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'TargetHealthDescriptions': [
            {
                'Target': {
                    'Id': 'string',
                    'Port': 123,
                    'AvailabilityZone': 'string'
                },
                'HealthCheckPort': 'string',
                'TargetHealth': {
                    'State': 'initial'|'healthy'|'unhealthy'|'unused'|'draining'|'unavailable',
                    'Reason': 'Elb.RegistrationInProgress'|'Elb.InitialHealthChecking'|'Target.ResponseCodeMismatch'|'Target.Timeout'|'Target.FailedHealthChecks'|'Target.NotRegistered'|'Target.NotInUse'|'Target.DeregistrationInProgress'|'Target.InvalidState'|'Target.IpUnusable'|'Target.HealthCheckDisabled'|'Elb.InternalError',
                    'Description': 'string'
                }
            },
        ]
    }
    
    
    :returns: 
    Elb.RegistrationInProgress - The target is in the process of being registered with the load balancer.
    Elb.InitialHealthChecking - The load balancer is still sending the target the minimum number of health checks required to determine its health status.
    
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

def modify_listener(ListenerArn=None, Port=None, Protocol=None, SslPolicy=None, Certificates=None, DefaultActions=None, AlpnPolicy=None):
    """
    Replaces the specified properties of the specified listener. Any properties that you do not specify remain unchanged.
    Changing the protocol from HTTPS to HTTP, or from TLS to TCP, removes the security policy and default certificate properties. If you change the protocol from HTTP to HTTPS, or from TCP to TLS, you must add the security policy and default certificate properties.
    To add an item to a list, remove an item from a list, or update an item in a list, you must provide the entire list. For example, to add an action, specify a list with the current actions plus the new action.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example changes the default action for the specified listener.
    Expected Output:
    This example changes the server certificate for the specified HTTPS listener.
    Expected Output:
    
    :example: response = client.modify_listener(
        ListenerArn='string',
        Port=123,
        Protocol='HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
        SslPolicy='string',
        Certificates=[
            {
                'CertificateArn': 'string',
                'IsDefault': True|False
            },
        ],
        DefaultActions=[
            {
                'Type': 'forward'|'authenticate-oidc'|'authenticate-cognito'|'redirect'|'fixed-response',
                'TargetGroupArn': 'string',
                'AuthenticateOidcConfig': {
                    'Issuer': 'string',
                    'AuthorizationEndpoint': 'string',
                    'TokenEndpoint': 'string',
                    'UserInfoEndpoint': 'string',
                    'ClientId': 'string',
                    'ClientSecret': 'string',
                    'SessionCookieName': 'string',
                    'Scope': 'string',
                    'SessionTimeout': 123,
                    'AuthenticationRequestExtraParams': {
                        'string': 'string'
                    },
                    'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate',
                    'UseExistingClientSecret': True|False
                },
                'AuthenticateCognitoConfig': {
                    'UserPoolArn': 'string',
                    'UserPoolClientId': 'string',
                    'UserPoolDomain': 'string',
                    'SessionCookieName': 'string',
                    'Scope': 'string',
                    'SessionTimeout': 123,
                    'AuthenticationRequestExtraParams': {
                        'string': 'string'
                    },
                    'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate'
                },
                'Order': 123,
                'RedirectConfig': {
                    'Protocol': 'string',
                    'Port': 'string',
                    'Host': 'string',
                    'Path': 'string',
                    'Query': 'string',
                    'StatusCode': 'HTTP_301'|'HTTP_302'
                },
                'FixedResponseConfig': {
                    'MessageBody': 'string',
                    'StatusCode': 'string',
                    'ContentType': 'string'
                },
                'ForwardConfig': {
                    'TargetGroups': [
                        {
                            'TargetGroupArn': 'string',
                            'Weight': 123
                        },
                    ],
                    'TargetGroupStickinessConfig': {
                        'Enabled': True|False,
                        'DurationSeconds': 123
                    }
                }
            },
        ],
        AlpnPolicy=[
            'string',
        ]
    )
    
    
    :type ListenerArn: string
    :param ListenerArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the listener.\n

    :type Port: integer
    :param Port: The port for connections from clients to the load balancer.

    :type Protocol: string
    :param Protocol: The protocol for connections from clients to the load balancer. Application Load Balancers support the HTTP and HTTPS protocols. Network Load Balancers support the TCP, TLS, UDP, and TCP_UDP protocols.

    :type SslPolicy: string
    :param SslPolicy: [HTTPS and TLS listeners] The security policy that defines which protocols and ciphers are supported. The following are the possible values:\n\nELBSecurityPolicy-2016-08\nELBSecurityPolicy-TLS-1-0-2015-04\nELBSecurityPolicy-TLS-1-1-2017-01\nELBSecurityPolicy-TLS-1-2-2017-01\nELBSecurityPolicy-TLS-1-2-Ext-2018-06\nELBSecurityPolicy-FS-2018-06\nELBSecurityPolicy-FS-1-1-2019-08\nELBSecurityPolicy-FS-1-2-2019-08\nELBSecurityPolicy-FS-1-2-Res-2019-08\n\nFor more information, see Security Policies in the Application Load Balancers Guide and Security Policies in the Network Load Balancers Guide .\n

    :type Certificates: list
    :param Certificates: [HTTPS and TLS listeners] The default certificate for the listener. You must provide exactly one certificate. Set CertificateArn to the certificate ARN but do not set IsDefault .\nTo create a certificate list, use AddListenerCertificates .\n\n(dict) --Information about an SSL server certificate.\n\nCertificateArn (string) --The Amazon Resource Name (ARN) of the certificate.\n\nIsDefault (boolean) --Indicates whether the certificate is the default certificate. Do not set this value when specifying a certificate as an input. This value is not included in the output when describing a listener, but is included when describing listener certificates.\n\n\n\n\n

    :type DefaultActions: list
    :param DefaultActions: The actions for the default rule. The rule must include one forward action or one or more fixed-response actions.\nIf the action type is forward , you specify one or more target groups. The protocol of the target group must be HTTP or HTTPS for an Application Load Balancer. The protocol of the target group must be TCP, TLS, UDP, or TCP_UDP for a Network Load Balancer.\n[HTTPS listeners] If the action type is authenticate-oidc , you authenticate users through an identity provider that is OpenID Connect (OIDC) compliant.\n[HTTPS listeners] If the action type is authenticate-cognito , you authenticate users through the user pools supported by Amazon Cognito.\n[Application Load Balancer] If the action type is redirect , you redirect specified client requests from one URL to another.\n[Application Load Balancer] If the action type is fixed-response , you drop specified client requests and return a custom HTTP response.\n\n(dict) --Information about an action.\n\nType (string) -- [REQUIRED]The type of action.\n\nTargetGroupArn (string) --The Amazon Resource Name (ARN) of the target group. Specify only when Type is forward and you want to route to a single target group. To route to one or more target groups, use ForwardConfig instead.\n\nAuthenticateOidcConfig (dict) --[HTTPS listeners] Information about an identity provider that is compliant with OpenID Connect (OIDC). Specify only when Type is authenticate-oidc .\n\nIssuer (string) -- [REQUIRED]The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.\n\nAuthorizationEndpoint (string) -- [REQUIRED]The authorization endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.\n\nTokenEndpoint (string) -- [REQUIRED]The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.\n\nUserInfoEndpoint (string) -- [REQUIRED]The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.\n\nClientId (string) -- [REQUIRED]The OAuth 2.0 client identifier.\n\nClientSecret (string) --The OAuth 2.0 client secret. This parameter is required if you are creating a rule. If you are modifying a rule, you can omit this parameter if you set UseExistingClientSecret to true.\n\nSessionCookieName (string) --The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.\n\nScope (string) --The set of user claims to be requested from the IdP. The default is openid .\nTo verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.\n\nSessionTimeout (integer) --The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).\n\nAuthenticationRequestExtraParams (dict) --The query parameters (up to 10) to include in the redirect request to the authorization endpoint.\n\n(string) --\n(string) --\n\n\n\n\nOnUnauthenticatedRequest (string) --The behavior if the user is not authenticated. The following are possible values:\n\ndeny- Return an HTTP 401 Unauthorized error.\nallow- Allow the request to be forwarded to the target.\nauthenticate- Redirect the request to the IdP authorization endpoint. This is the default value.\n\n\nUseExistingClientSecret (boolean) --Indicates whether to use the existing client secret when modifying a rule. If you are creating a rule, you can omit this parameter or set it to false.\n\n\n\nAuthenticateCognitoConfig (dict) --[HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify only when Type is authenticate-cognito .\n\nUserPoolArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the Amazon Cognito user pool.\n\nUserPoolClientId (string) -- [REQUIRED]The ID of the Amazon Cognito user pool client.\n\nUserPoolDomain (string) -- [REQUIRED]The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.\n\nSessionCookieName (string) --The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.\n\nScope (string) --The set of user claims to be requested from the IdP. The default is openid .\nTo verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.\n\nSessionTimeout (integer) --The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).\n\nAuthenticationRequestExtraParams (dict) --The query parameters (up to 10) to include in the redirect request to the authorization endpoint.\n\n(string) --\n(string) --\n\n\n\n\nOnUnauthenticatedRequest (string) --The behavior if the user is not authenticated. The following are possible values:\n\ndeny- Return an HTTP 401 Unauthorized error.\nallow- Allow the request to be forwarded to the target.\nauthenticate- Redirect the request to the IdP authorization endpoint. This is the default value.\n\n\n\n\nOrder (integer) --The order for the action. This value is required for rules with multiple actions. The action with the lowest value for order is performed first. The last action to be performed must be one of the following types of actions: a forward , fixed-response , or redirect .\n\nRedirectConfig (dict) --[Application Load Balancer] Information for creating a redirect action. Specify only when Type is redirect .\n\nProtocol (string) --The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.\n\nPort (string) --The port. You can specify a value from 1 to 65535 or #{port}.\n\nHost (string) --The hostname. This component is not percent-encoded. The hostname can contain #{host}.\n\nPath (string) --The absolute path, starting with the leading '/'. This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}.\n\nQuery (string) --The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading '?', as it is automatically added. You can specify any of the reserved keywords.\n\nStatusCode (string) -- [REQUIRED]The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).\n\n\n\nFixedResponseConfig (dict) --[Application Load Balancer] Information for creating an action that returns a custom HTTP response. Specify only when Type is fixed-response .\n\nMessageBody (string) --The message.\n\nStatusCode (string) -- [REQUIRED]The HTTP response code (2XX, 4XX, or 5XX).\n\nContentType (string) --The content type.\nValid Values: text/plain | text/css | text/html | application/javascript | application/json\n\n\n\nForwardConfig (dict) --Information for creating an action that distributes requests among one or more target groups. For Network Load Balancers, you can specify a single target group. Specify only when Type is forward . If you specify both ForwardConfig and TargetGroupArn , you can specify only one target group using ForwardConfig and it must be the same target group specified in TargetGroupArn .\n\nTargetGroups (list) --One or more target groups. For Network Load Balancers, you can specify a single target group.\n\n(dict) --Information about how traffic will be distributed between multiple target groups in a forward rule.\n\nTargetGroupArn (string) --The Amazon Resource Name (ARN) of the target group.\n\nWeight (integer) --The weight. The range is 0 to 999.\n\n\n\n\n\nTargetGroupStickinessConfig (dict) --The target group stickiness for the rule.\n\nEnabled (boolean) --Indicates whether target group stickiness is enabled.\n\nDurationSeconds (integer) --The time period, in seconds, during which requests from a client should be routed to the same target group. The range is 1-604800 seconds (7 days).\n\n\n\n\n\n\n\n\n

    :type AlpnPolicy: list
    :param AlpnPolicy: [TLS listeners] The name of the Application-Layer Protocol Negotiation (ALPN) policy. You can specify one policy name. The following are the possible values:\n\nHTTP1Only\nHTTP2Only\nHTTP2Optional\nHTTP2Preferred\nNone\n\nFor more information, see ALPN Policies in the Network Load Balancers Guide .\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Listeners': [
        {
            'ListenerArn': 'string',
            'LoadBalancerArn': 'string',
            'Port': 123,
            'Protocol': 'HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
            'Certificates': [
                {
                    'CertificateArn': 'string',
                    'IsDefault': True|False
                },
            ],
            'SslPolicy': 'string',
            'DefaultActions': [
                {
                    'Type': 'forward'|'authenticate-oidc'|'authenticate-cognito'|'redirect'|'fixed-response',
                    'TargetGroupArn': 'string',
                    'AuthenticateOidcConfig': {
                        'Issuer': 'string',
                        'AuthorizationEndpoint': 'string',
                        'TokenEndpoint': 'string',
                        'UserInfoEndpoint': 'string',
                        'ClientId': 'string',
                        'ClientSecret': 'string',
                        'SessionCookieName': 'string',
                        'Scope': 'string',
                        'SessionTimeout': 123,
                        'AuthenticationRequestExtraParams': {
                            'string': 'string'
                        },
                        'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate',
                        'UseExistingClientSecret': True|False
                    },
                    'AuthenticateCognitoConfig': {
                        'UserPoolArn': 'string',
                        'UserPoolClientId': 'string',
                        'UserPoolDomain': 'string',
                        'SessionCookieName': 'string',
                        'Scope': 'string',
                        'SessionTimeout': 123,
                        'AuthenticationRequestExtraParams': {
                            'string': 'string'
                        },
                        'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate'
                    },
                    'Order': 123,
                    'RedirectConfig': {
                        'Protocol': 'string',
                        'Port': 'string',
                        'Host': 'string',
                        'Path': 'string',
                        'Query': 'string',
                        'StatusCode': 'HTTP_301'|'HTTP_302'
                    },
                    'FixedResponseConfig': {
                        'MessageBody': 'string',
                        'StatusCode': 'string',
                        'ContentType': 'string'
                    },
                    'ForwardConfig': {
                        'TargetGroups': [
                            {
                                'TargetGroupArn': 'string',
                                'Weight': 123
                            },
                        ],
                        'TargetGroupStickinessConfig': {
                            'Enabled': True|False,
                            'DurationSeconds': 123
                        }
                    }
                },
            ],
            'AlpnPolicy': [
                'string',
            ]
        },
    ]
}


Response Structure

(dict) --

Listeners (list) --
Information about the modified listener.

(dict) --
Information about a listener.

ListenerArn (string) --
The Amazon Resource Name (ARN) of the listener.

LoadBalancerArn (string) --
The Amazon Resource Name (ARN) of the load balancer.

Port (integer) --
The port on which the load balancer is listening.

Protocol (string) --
The protocol for connections from clients to the load balancer.

Certificates (list) --
[HTTPS or TLS listener] The default certificate for the listener.

(dict) --
Information about an SSL server certificate.

CertificateArn (string) --
The Amazon Resource Name (ARN) of the certificate.

IsDefault (boolean) --
Indicates whether the certificate is the default certificate. Do not set this value when specifying a certificate as an input. This value is not included in the output when describing a listener, but is included when describing listener certificates.





SslPolicy (string) --
[HTTPS or TLS listener] The security policy that defines which protocols and ciphers are supported.

DefaultActions (list) --
The default actions for the listener.

(dict) --
Information about an action.

Type (string) --
The type of action.

TargetGroupArn (string) --
The Amazon Resource Name (ARN) of the target group. Specify only when Type is forward and you want to route to a single target group. To route to one or more target groups, use ForwardConfig instead.

AuthenticateOidcConfig (dict) --
[HTTPS listeners] Information about an identity provider that is compliant with OpenID Connect (OIDC). Specify only when Type is authenticate-oidc .

Issuer (string) --
The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

AuthorizationEndpoint (string) --
The authorization endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

TokenEndpoint (string) --
The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

UserInfoEndpoint (string) --
The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

ClientId (string) --
The OAuth 2.0 client identifier.

ClientSecret (string) --
The OAuth 2.0 client secret. This parameter is required if you are creating a rule. If you are modifying a rule, you can omit this parameter if you set UseExistingClientSecret to true.

SessionCookieName (string) --
The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.

Scope (string) --
The set of user claims to be requested from the IdP. The default is openid .
To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.

SessionTimeout (integer) --
The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).

AuthenticationRequestExtraParams (dict) --
The query parameters (up to 10) to include in the redirect request to the authorization endpoint.

(string) --
(string) --




OnUnauthenticatedRequest (string) --
The behavior if the user is not authenticated. The following are possible values:

deny- Return an HTTP 401 Unauthorized error.
allow- Allow the request to be forwarded to the target.
authenticate- Redirect the request to the IdP authorization endpoint. This is the default value.


UseExistingClientSecret (boolean) --
Indicates whether to use the existing client secret when modifying a rule. If you are creating a rule, you can omit this parameter or set it to false.



AuthenticateCognitoConfig (dict) --
[HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify only when Type is authenticate-cognito .

UserPoolArn (string) --
The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

UserPoolClientId (string) --
The ID of the Amazon Cognito user pool client.

UserPoolDomain (string) --
The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

SessionCookieName (string) --
The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.

Scope (string) --
The set of user claims to be requested from the IdP. The default is openid .
To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.

SessionTimeout (integer) --
The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).

AuthenticationRequestExtraParams (dict) --
The query parameters (up to 10) to include in the redirect request to the authorization endpoint.

(string) --
(string) --




OnUnauthenticatedRequest (string) --
The behavior if the user is not authenticated. The following are possible values:

deny- Return an HTTP 401 Unauthorized error.
allow- Allow the request to be forwarded to the target.
authenticate- Redirect the request to the IdP authorization endpoint. This is the default value.




Order (integer) --
The order for the action. This value is required for rules with multiple actions. The action with the lowest value for order is performed first. The last action to be performed must be one of the following types of actions: a forward , fixed-response , or redirect .

RedirectConfig (dict) --
[Application Load Balancer] Information for creating a redirect action. Specify only when Type is redirect .

Protocol (string) --
The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

Port (string) --
The port. You can specify a value from 1 to 65535 or #{port}.

Host (string) --
The hostname. This component is not percent-encoded. The hostname can contain #{host}.

Path (string) --
The absolute path, starting with the leading "/". This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}.

Query (string) --
The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading "?", as it is automatically added. You can specify any of the reserved keywords.

StatusCode (string) --
The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).



FixedResponseConfig (dict) --
[Application Load Balancer] Information for creating an action that returns a custom HTTP response. Specify only when Type is fixed-response .

MessageBody (string) --
The message.

StatusCode (string) --
The HTTP response code (2XX, 4XX, or 5XX).

ContentType (string) --
The content type.
Valid Values: text/plain | text/css | text/html | application/javascript | application/json



ForwardConfig (dict) --
Information for creating an action that distributes requests among one or more target groups. For Network Load Balancers, you can specify a single target group. Specify only when Type is forward . If you specify both ForwardConfig and TargetGroupArn , you can specify only one target group using ForwardConfig and it must be the same target group specified in TargetGroupArn .

TargetGroups (list) --
One or more target groups. For Network Load Balancers, you can specify a single target group.

(dict) --
Information about how traffic will be distributed between multiple target groups in a forward rule.

TargetGroupArn (string) --
The Amazon Resource Name (ARN) of the target group.

Weight (integer) --
The weight. The range is 0 to 999.





TargetGroupStickinessConfig (dict) --
The target group stickiness for the rule.

Enabled (boolean) --
Indicates whether target group stickiness is enabled.

DurationSeconds (integer) --
The time period, in seconds, during which requests from a client should be routed to the same target group. The range is 1-604800 seconds (7 days).









AlpnPolicy (list) --
[TLS listener] The name of the Application-Layer Protocol Negotiation (ALPN) policy.

(string) --












Exceptions

ElasticLoadBalancingv2.Client.exceptions.DuplicateListenerException
ElasticLoadBalancingv2.Client.exceptions.TooManyListenersException
ElasticLoadBalancingv2.Client.exceptions.TooManyCertificatesException
ElasticLoadBalancingv2.Client.exceptions.ListenerNotFoundException
ElasticLoadBalancingv2.Client.exceptions.TargetGroupNotFoundException
ElasticLoadBalancingv2.Client.exceptions.TargetGroupAssociationLimitException
ElasticLoadBalancingv2.Client.exceptions.IncompatibleProtocolsException
ElasticLoadBalancingv2.Client.exceptions.SSLPolicyNotFoundException
ElasticLoadBalancingv2.Client.exceptions.CertificateNotFoundException
ElasticLoadBalancingv2.Client.exceptions.InvalidConfigurationRequestException
ElasticLoadBalancingv2.Client.exceptions.UnsupportedProtocolException
ElasticLoadBalancingv2.Client.exceptions.TooManyRegistrationsForTargetIdException
ElasticLoadBalancingv2.Client.exceptions.TooManyTargetsException
ElasticLoadBalancingv2.Client.exceptions.TooManyActionsException
ElasticLoadBalancingv2.Client.exceptions.InvalidLoadBalancerActionException
ElasticLoadBalancingv2.Client.exceptions.TooManyUniqueTargetGroupsPerLoadBalancerException
ElasticLoadBalancingv2.Client.exceptions.ALPNPolicyNotSupportedException

Examples
This example changes the default action for the specified listener.
response = client.modify_listener(
    DefaultActions=[
        {
            'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-new-targets/2453ed029918f21f',
            'Type': 'forward',
        },
    ],
    ListenerArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2',
)

print(response)


Expected Output:
{
    'Listeners': [
        {
            'DefaultActions': [
                {
                    'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-new-targets/2453ed029918f21f',
                    'Type': 'forward',
                },
            ],
            'ListenerArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2',
            'LoadBalancerArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
            'Port': 80,
            'Protocol': 'HTTP',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}


This example changes the server certificate for the specified HTTPS listener.
response = client.modify_listener(
    Certificates=[
        {
            'CertificateArn': 'arn:aws:iam::123456789012:server-certificate/my-new-server-cert',
        },
    ],
    ListenerArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/0467ef3c8400ae65',
)

print(response)


Expected Output:
{
    'Listeners': [
        {
            'Certificates': [
                {
                    'CertificateArn': 'arn:aws:iam::123456789012:server-certificate/my-new-server-cert',
                },
            ],
            'DefaultActions': [
                {
                    'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
                    'Type': 'forward',
                },
            ],
            'ListenerArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/0467ef3c8400ae65',
            'LoadBalancerArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
            'Port': 443,
            'Protocol': 'HTTPS',
            'SslPolicy': 'ELBSecurityPolicy-2015-05',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Listeners': [
            {
                'ListenerArn': 'string',
                'LoadBalancerArn': 'string',
                'Port': 123,
                'Protocol': 'HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
                'Certificates': [
                    {
                        'CertificateArn': 'string',
                        'IsDefault': True|False
                    },
                ],
                'SslPolicy': 'string',
                'DefaultActions': [
                    {
                        'Type': 'forward'|'authenticate-oidc'|'authenticate-cognito'|'redirect'|'fixed-response',
                        'TargetGroupArn': 'string',
                        'AuthenticateOidcConfig': {
                            'Issuer': 'string',
                            'AuthorizationEndpoint': 'string',
                            'TokenEndpoint': 'string',
                            'UserInfoEndpoint': 'string',
                            'ClientId': 'string',
                            'ClientSecret': 'string',
                            'SessionCookieName': 'string',
                            'Scope': 'string',
                            'SessionTimeout': 123,
                            'AuthenticationRequestExtraParams': {
                                'string': 'string'
                            },
                            'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate',
                            'UseExistingClientSecret': True|False
                        },
                        'AuthenticateCognitoConfig': {
                            'UserPoolArn': 'string',
                            'UserPoolClientId': 'string',
                            'UserPoolDomain': 'string',
                            'SessionCookieName': 'string',
                            'Scope': 'string',
                            'SessionTimeout': 123,
                            'AuthenticationRequestExtraParams': {
                                'string': 'string'
                            },
                            'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate'
                        },
                        'Order': 123,
                        'RedirectConfig': {
                            'Protocol': 'string',
                            'Port': 'string',
                            'Host': 'string',
                            'Path': 'string',
                            'Query': 'string',
                            'StatusCode': 'HTTP_301'|'HTTP_302'
                        },
                        'FixedResponseConfig': {
                            'MessageBody': 'string',
                            'StatusCode': 'string',
                            'ContentType': 'string'
                        },
                        'ForwardConfig': {
                            'TargetGroups': [
                                {
                                    'TargetGroupArn': 'string',
                                    'Weight': 123
                                },
                            ],
                            'TargetGroupStickinessConfig': {
                                'Enabled': True|False,
                                'DurationSeconds': 123
                            }
                        }
                    },
                ],
                'AlpnPolicy': [
                    'string',
                ]
            },
        ]
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def modify_load_balancer_attributes(LoadBalancerArn=None, Attributes=None):
    """
    Modifies the specified attributes of the specified Application Load Balancer or Network Load Balancer.
    If any of the specified attributes can\'t be modified as requested, the call fails. Any existing attributes that you do not modify retain their current values.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example enables deletion protection for the specified load balancer.
    Expected Output:
    This example changes the idle timeout value for the specified load balancer.
    Expected Output:
    This example enables access logs for the specified load balancer. Note that the S3 bucket must exist in the same region as the load balancer and must have a policy attached that grants access to the Elastic Load Balancing service.
    Expected Output:
    
    :example: response = client.modify_load_balancer_attributes(
        LoadBalancerArn='string',
        Attributes=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type LoadBalancerArn: string
    :param LoadBalancerArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the load balancer.\n

    :type Attributes: list
    :param Attributes: [REQUIRED]\nThe load balancer attributes.\n\n(dict) --Information about a load balancer attribute.\n\nKey (string) --The name of the attribute.\nThe following attributes are supported by both Application Load Balancers and Network Load Balancers:\n\naccess_logs.s3.enabled - Indicates whether access logs are enabled. The value is true or false . The default is false .\naccess_logs.s3.bucket - The name of the S3 bucket for the access logs. This attribute is required if access logs are enabled. The bucket must exist in the same region as the load balancer and have a bucket policy that grants Elastic Load Balancing permissions to write to the bucket.\naccess_logs.s3.prefix - The prefix for the location in the S3 bucket for the access logs.\ndeletion_protection.enabled - Indicates whether deletion protection is enabled. The value is true or false . The default is false .\n\nThe following attributes are supported by only Application Load Balancers:\n\nidle_timeout.timeout_seconds - The idle timeout value, in seconds. The valid range is 1-4000 seconds. The default is 60 seconds.\nrouting.http.drop_invalid_header_fields.enabled - Indicates whether HTTP headers with invalid header fields are removed by the load balancer (true ) or routed to targets (false ). The default is false .\nrouting.http2.enabled - Indicates whether HTTP/2 is enabled. The value is true or false . The default is true . Elastic Load Balancing requires that message header names contain only alphanumeric characters and hyphens.\n\nThe following attributes are supported by only Network Load Balancers:\n\nload_balancing.cross_zone.enabled - Indicates whether cross-zone load balancing is enabled. The value is true or false . The default is false .\n\n\nValue (string) --The value of the attribute.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Attributes': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --

Attributes (list) --
Information about the load balancer attributes.

(dict) --
Information about a load balancer attribute.

Key (string) --
The name of the attribute.
The following attributes are supported by both Application Load Balancers and Network Load Balancers:

access_logs.s3.enabled - Indicates whether access logs are enabled. The value is true or false . The default is false .
access_logs.s3.bucket - The name of the S3 bucket for the access logs. This attribute is required if access logs are enabled. The bucket must exist in the same region as the load balancer and have a bucket policy that grants Elastic Load Balancing permissions to write to the bucket.
access_logs.s3.prefix - The prefix for the location in the S3 bucket for the access logs.
deletion_protection.enabled - Indicates whether deletion protection is enabled. The value is true or false . The default is false .

The following attributes are supported by only Application Load Balancers:

idle_timeout.timeout_seconds - The idle timeout value, in seconds. The valid range is 1-4000 seconds. The default is 60 seconds.
routing.http.drop_invalid_header_fields.enabled - Indicates whether HTTP headers with invalid header fields are removed by the load balancer (true ) or routed to targets (false ). The default is false .
routing.http2.enabled - Indicates whether HTTP/2 is enabled. The value is true or false . The default is true . Elastic Load Balancing requires that message header names contain only alphanumeric characters and hyphens.

The following attributes are supported by only Network Load Balancers:

load_balancing.cross_zone.enabled - Indicates whether cross-zone load balancing is enabled. The value is true or false . The default is false .


Value (string) --
The value of the attribute.











Exceptions

ElasticLoadBalancingv2.Client.exceptions.LoadBalancerNotFoundException
ElasticLoadBalancingv2.Client.exceptions.InvalidConfigurationRequestException

Examples
This example enables deletion protection for the specified load balancer.
response = client.modify_load_balancer_attributes(
    Attributes=[
        {
            'Key': 'deletion_protection.enabled',
            'Value': 'true',
        },
    ],
    LoadBalancerArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
)

print(response)


Expected Output:
{
    'Attributes': [
        {
            'Key': 'deletion_protection.enabled',
            'Value': 'true',
        },
        {
            'Key': 'access_logs.s3.enabled',
            'Value': 'false',
        },
        {
            'Key': 'idle_timeout.timeout_seconds',
            'Value': '60',
        },
        {
            'Key': 'access_logs.s3.prefix',
            'Value': '',
        },
        {
            'Key': 'access_logs.s3.bucket',
            'Value': '',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}


This example changes the idle timeout value for the specified load balancer.
response = client.modify_load_balancer_attributes(
    Attributes=[
        {
            'Key': 'idle_timeout.timeout_seconds',
            'Value': '30',
        },
    ],
    LoadBalancerArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
)

print(response)


Expected Output:
{
    'Attributes': [
        {
            'Key': 'idle_timeout.timeout_seconds',
            'Value': '30',
        },
        {
            'Key': 'access_logs.s3.enabled',
            'Value': 'false',
        },
        {
            'Key': 'access_logs.s3.prefix',
            'Value': '',
        },
        {
            'Key': 'deletion_protection.enabled',
            'Value': 'true',
        },
        {
            'Key': 'access_logs.s3.bucket',
            'Value': '',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}


This example enables access logs for the specified load balancer. Note that the S3 bucket must exist in the same region as the load balancer and must have a policy attached that grants access to the Elastic Load Balancing service.
response = client.modify_load_balancer_attributes(
    Attributes=[
        {
            'Key': 'access_logs.s3.enabled',
            'Value': 'true',
        },
        {
            'Key': 'access_logs.s3.bucket',
            'Value': 'my-loadbalancer-logs',
        },
        {
            'Key': 'access_logs.s3.prefix',
            'Value': 'myapp',
        },
    ],
    LoadBalancerArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
)

print(response)


Expected Output:
{
    'Attributes': [
        {
            'Key': 'access_logs.s3.enabled',
            'Value': 'true',
        },
        {
            'Key': 'access_logs.s3.bucket',
            'Value': 'my-load-balancer-logs',
        },
        {
            'Key': 'access_logs.s3.prefix',
            'Value': 'myapp',
        },
        {
            'Key': 'idle_timeout.timeout_seconds',
            'Value': '60',
        },
        {
            'Key': 'deletion_protection.enabled',
            'Value': 'false',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Attributes': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    :returns: 
    access_logs.s3.enabled - Indicates whether access logs are enabled. The value is true or false . The default is false .
    access_logs.s3.bucket - The name of the S3 bucket for the access logs. This attribute is required if access logs are enabled. The bucket must exist in the same region as the load balancer and have a bucket policy that grants Elastic Load Balancing permissions to write to the bucket.
    access_logs.s3.prefix - The prefix for the location in the S3 bucket for the access logs.
    deletion_protection.enabled - Indicates whether deletion protection is enabled. The value is true or false . The default is false .
    
    """
    pass

def modify_rule(RuleArn=None, Conditions=None, Actions=None):
    """
    Replaces the specified properties of the specified rule. Any properties that you do not specify are unchanged.
    To add an item to a list, remove an item from a list, or update an item in a list, you must provide the entire list. For example, to add an action, specify a list with the current actions plus the new action.
    To modify the actions for the default rule, use  ModifyListener .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example modifies the condition for the specified rule.
    Expected Output:
    
    :example: response = client.modify_rule(
        RuleArn='string',
        Conditions=[
            {
                'Field': 'string',
                'Values': [
                    'string',
                ],
                'HostHeaderConfig': {
                    'Values': [
                        'string',
                    ]
                },
                'PathPatternConfig': {
                    'Values': [
                        'string',
                    ]
                },
                'HttpHeaderConfig': {
                    'HttpHeaderName': 'string',
                    'Values': [
                        'string',
                    ]
                },
                'QueryStringConfig': {
                    'Values': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ]
                },
                'HttpRequestMethodConfig': {
                    'Values': [
                        'string',
                    ]
                },
                'SourceIpConfig': {
                    'Values': [
                        'string',
                    ]
                }
            },
        ],
        Actions=[
            {
                'Type': 'forward'|'authenticate-oidc'|'authenticate-cognito'|'redirect'|'fixed-response',
                'TargetGroupArn': 'string',
                'AuthenticateOidcConfig': {
                    'Issuer': 'string',
                    'AuthorizationEndpoint': 'string',
                    'TokenEndpoint': 'string',
                    'UserInfoEndpoint': 'string',
                    'ClientId': 'string',
                    'ClientSecret': 'string',
                    'SessionCookieName': 'string',
                    'Scope': 'string',
                    'SessionTimeout': 123,
                    'AuthenticationRequestExtraParams': {
                        'string': 'string'
                    },
                    'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate',
                    'UseExistingClientSecret': True|False
                },
                'AuthenticateCognitoConfig': {
                    'UserPoolArn': 'string',
                    'UserPoolClientId': 'string',
                    'UserPoolDomain': 'string',
                    'SessionCookieName': 'string',
                    'Scope': 'string',
                    'SessionTimeout': 123,
                    'AuthenticationRequestExtraParams': {
                        'string': 'string'
                    },
                    'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate'
                },
                'Order': 123,
                'RedirectConfig': {
                    'Protocol': 'string',
                    'Port': 'string',
                    'Host': 'string',
                    'Path': 'string',
                    'Query': 'string',
                    'StatusCode': 'HTTP_301'|'HTTP_302'
                },
                'FixedResponseConfig': {
                    'MessageBody': 'string',
                    'StatusCode': 'string',
                    'ContentType': 'string'
                },
                'ForwardConfig': {
                    'TargetGroups': [
                        {
                            'TargetGroupArn': 'string',
                            'Weight': 123
                        },
                    ],
                    'TargetGroupStickinessConfig': {
                        'Enabled': True|False,
                        'DurationSeconds': 123
                    }
                }
            },
        ]
    )
    
    
    :type RuleArn: string
    :param RuleArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the rule.\n

    :type Conditions: list
    :param Conditions: The conditions. Each rule can include zero or one of the following conditions: http-request-method , host-header , path-pattern , and source-ip , and zero or more of the following conditions: http-header and query-string .\n\n(dict) --Information about a condition for a rule.\n\nField (string) --The field in the HTTP request. The following are the possible values:\n\nhttp-header\nhttp-request-method\nhost-header\npath-pattern\nquery-string\nsource-ip\n\n\nValues (list) --The condition value. You can use Values if the rule contains only host-header and path-pattern conditions. Otherwise, you can use HostHeaderConfig for host-header conditions and PathPatternConfig for path-pattern conditions.\nIf Field is host-header , you can specify a single host name (for example, my.example.com). A host name is case insensitive, can be up to 128 characters in length, and can contain any of the following characters.\n\nA-Z, a-z, 0-9\n\n.\n\n\n\n(matches 0 or more characters)\n\n\n? (matches exactly 1 character)\n\nIf Field is path-pattern , you can specify a single path pattern (for example, /img/*). A path pattern is case-sensitive, can be up to 128 characters in length, and can contain any of the following characters.\n\nA-Z, a-z, 0-9\n_ - . $ / ~ ' \' @ : +\n& (using &amp;)\n\n(matches 0 or more characters)\n\n\n? (matches exactly 1 character)\n\n\n(string) --\n\n\nHostHeaderConfig (dict) --Information for a host header condition. Specify only when Field is host-header .\n\nValues (list) --One or more host names. The maximum size of each name is 128 characters. The comparison is case insensitive. The following wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly 1 character).\nIf you specify multiple strings, the condition is satisfied if one of the strings matches the host name.\n\n(string) --\n\n\n\n\nPathPatternConfig (dict) --Information for a path pattern condition. Specify only when Field is path-pattern .\n\nValues (list) --One or more path patterns to compare against the request URL. The maximum size of each string is 128 characters. The comparison is case sensitive. The following wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly 1 character).\nIf you specify multiple strings, the condition is satisfied if one of them matches the request URL. The path pattern is compared only to the path of the URL, not to its query string. To compare against the query string, use QueryStringConditionConfig .\n\n(string) --\n\n\n\n\nHttpHeaderConfig (dict) --Information for an HTTP header condition. Specify only when Field is http-header .\n\nHttpHeaderName (string) --The name of the HTTP header field. The maximum size is 40 characters. The header name is case insensitive. The allowed characters are specified by RFC 7230. Wildcards are not supported.\nYou can\'t use an HTTP header condition to specify the host header. Use HostHeaderConditionConfig to specify a host header condition.\n\nValues (list) --One or more strings to compare against the value of the HTTP header. The maximum size of each string is 128 characters. The comparison strings are case insensitive. The following wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly 1 character).\nIf the same header appears multiple times in the request, we search them in order until a match is found.\nIf you specify multiple strings, the condition is satisfied if one of the strings matches the value of the HTTP header. To require that all of the strings are a match, create one condition per string.\n\n(string) --\n\n\n\n\nQueryStringConfig (dict) --Information for a query string condition. Specify only when Field is query-string .\n\nValues (list) --One or more key/value pairs or values to find in the query string. The maximum size of each string is 128 characters. The comparison is case insensitive. The following wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly 1 character). To search for a literal \'*\' or \'?\' character in a query string, you must escape these characters in Values using a \'\' character.\nIf you specify multiple key/value pairs or values, the condition is satisfied if one of them is found in the query string.\n\n(dict) --Information about a key/value pair.\n\nKey (string) --The key. You can omit the key.\n\nValue (string) --The value.\n\n\n\n\n\n\n\nHttpRequestMethodConfig (dict) --Information for an HTTP method condition. Specify only when Field is http-request-method .\n\nValues (list) --The name of the request method. The maximum size is 40 characters. The allowed characters are A-Z, hyphen (-), and underscore (_). The comparison is case sensitive. Wildcards are not supported; therefore, the method name must be an exact match.\nIf you specify multiple strings, the condition is satisfied if one of the strings matches the HTTP request method. We recommend that you route GET and HEAD requests in the same way, because the response to a HEAD request may be cached.\n\n(string) --\n\n\n\n\nSourceIpConfig (dict) --Information for a source IP condition. Specify only when Field is source-ip .\n\nValues (list) --One or more source IP addresses, in CIDR format. You can use both IPv4 and IPv6 addresses. Wildcards are not supported.\nIf you specify multiple addresses, the condition is satisfied if the source IP address of the request matches one of the CIDR blocks. This condition is not satisfied by the addresses in the X-Forwarded-For header. To search for addresses in the X-Forwarded-For header, use HttpHeaderConditionConfig .\n\n(string) --\n\n\n\n\n\n\n\n

    :type Actions: list
    :param Actions: The actions. Each rule must include exactly one of the following types of actions: forward , fixed-response , or redirect , and it must be the last action to be performed.\nIf the action type is forward , you specify one or more target groups. The protocol of the target group must be HTTP or HTTPS for an Application Load Balancer. The protocol of the target group must be TCP, TLS, UDP, or TCP_UDP for a Network Load Balancer.\n[HTTPS listeners] If the action type is authenticate-oidc , you authenticate users through an identity provider that is OpenID Connect (OIDC) compliant.\n[HTTPS listeners] If the action type is authenticate-cognito , you authenticate users through the user pools supported by Amazon Cognito.\n[Application Load Balancer] If the action type is redirect , you redirect specified client requests from one URL to another.\n[Application Load Balancer] If the action type is fixed-response , you drop specified client requests and return a custom HTTP response.\n\n(dict) --Information about an action.\n\nType (string) -- [REQUIRED]The type of action.\n\nTargetGroupArn (string) --The Amazon Resource Name (ARN) of the target group. Specify only when Type is forward and you want to route to a single target group. To route to one or more target groups, use ForwardConfig instead.\n\nAuthenticateOidcConfig (dict) --[HTTPS listeners] Information about an identity provider that is compliant with OpenID Connect (OIDC). Specify only when Type is authenticate-oidc .\n\nIssuer (string) -- [REQUIRED]The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.\n\nAuthorizationEndpoint (string) -- [REQUIRED]The authorization endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.\n\nTokenEndpoint (string) -- [REQUIRED]The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.\n\nUserInfoEndpoint (string) -- [REQUIRED]The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.\n\nClientId (string) -- [REQUIRED]The OAuth 2.0 client identifier.\n\nClientSecret (string) --The OAuth 2.0 client secret. This parameter is required if you are creating a rule. If you are modifying a rule, you can omit this parameter if you set UseExistingClientSecret to true.\n\nSessionCookieName (string) --The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.\n\nScope (string) --The set of user claims to be requested from the IdP. The default is openid .\nTo verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.\n\nSessionTimeout (integer) --The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).\n\nAuthenticationRequestExtraParams (dict) --The query parameters (up to 10) to include in the redirect request to the authorization endpoint.\n\n(string) --\n(string) --\n\n\n\n\nOnUnauthenticatedRequest (string) --The behavior if the user is not authenticated. The following are possible values:\n\ndeny- Return an HTTP 401 Unauthorized error.\nallow- Allow the request to be forwarded to the target.\nauthenticate- Redirect the request to the IdP authorization endpoint. This is the default value.\n\n\nUseExistingClientSecret (boolean) --Indicates whether to use the existing client secret when modifying a rule. If you are creating a rule, you can omit this parameter or set it to false.\n\n\n\nAuthenticateCognitoConfig (dict) --[HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify only when Type is authenticate-cognito .\n\nUserPoolArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the Amazon Cognito user pool.\n\nUserPoolClientId (string) -- [REQUIRED]The ID of the Amazon Cognito user pool client.\n\nUserPoolDomain (string) -- [REQUIRED]The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.\n\nSessionCookieName (string) --The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.\n\nScope (string) --The set of user claims to be requested from the IdP. The default is openid .\nTo verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.\n\nSessionTimeout (integer) --The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).\n\nAuthenticationRequestExtraParams (dict) --The query parameters (up to 10) to include in the redirect request to the authorization endpoint.\n\n(string) --\n(string) --\n\n\n\n\nOnUnauthenticatedRequest (string) --The behavior if the user is not authenticated. The following are possible values:\n\ndeny- Return an HTTP 401 Unauthorized error.\nallow- Allow the request to be forwarded to the target.\nauthenticate- Redirect the request to the IdP authorization endpoint. This is the default value.\n\n\n\n\nOrder (integer) --The order for the action. This value is required for rules with multiple actions. The action with the lowest value for order is performed first. The last action to be performed must be one of the following types of actions: a forward , fixed-response , or redirect .\n\nRedirectConfig (dict) --[Application Load Balancer] Information for creating a redirect action. Specify only when Type is redirect .\n\nProtocol (string) --The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.\n\nPort (string) --The port. You can specify a value from 1 to 65535 or #{port}.\n\nHost (string) --The hostname. This component is not percent-encoded. The hostname can contain #{host}.\n\nPath (string) --The absolute path, starting with the leading '/'. This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}.\n\nQuery (string) --The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading '?', as it is automatically added. You can specify any of the reserved keywords.\n\nStatusCode (string) -- [REQUIRED]The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).\n\n\n\nFixedResponseConfig (dict) --[Application Load Balancer] Information for creating an action that returns a custom HTTP response. Specify only when Type is fixed-response .\n\nMessageBody (string) --The message.\n\nStatusCode (string) -- [REQUIRED]The HTTP response code (2XX, 4XX, or 5XX).\n\nContentType (string) --The content type.\nValid Values: text/plain | text/css | text/html | application/javascript | application/json\n\n\n\nForwardConfig (dict) --Information for creating an action that distributes requests among one or more target groups. For Network Load Balancers, you can specify a single target group. Specify only when Type is forward . If you specify both ForwardConfig and TargetGroupArn , you can specify only one target group using ForwardConfig and it must be the same target group specified in TargetGroupArn .\n\nTargetGroups (list) --One or more target groups. For Network Load Balancers, you can specify a single target group.\n\n(dict) --Information about how traffic will be distributed between multiple target groups in a forward rule.\n\nTargetGroupArn (string) --The Amazon Resource Name (ARN) of the target group.\n\nWeight (integer) --The weight. The range is 0 to 999.\n\n\n\n\n\nTargetGroupStickinessConfig (dict) --The target group stickiness for the rule.\n\nEnabled (boolean) --Indicates whether target group stickiness is enabled.\n\nDurationSeconds (integer) --The time period, in seconds, during which requests from a client should be routed to the same target group. The range is 1-604800 seconds (7 days).\n\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Rules': [
        {
            'RuleArn': 'string',
            'Priority': 'string',
            'Conditions': [
                {
                    'Field': 'string',
                    'Values': [
                        'string',
                    ],
                    'HostHeaderConfig': {
                        'Values': [
                            'string',
                        ]
                    },
                    'PathPatternConfig': {
                        'Values': [
                            'string',
                        ]
                    },
                    'HttpHeaderConfig': {
                        'HttpHeaderName': 'string',
                        'Values': [
                            'string',
                        ]
                    },
                    'QueryStringConfig': {
                        'Values': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                    'HttpRequestMethodConfig': {
                        'Values': [
                            'string',
                        ]
                    },
                    'SourceIpConfig': {
                        'Values': [
                            'string',
                        ]
                    }
                },
            ],
            'Actions': [
                {
                    'Type': 'forward'|'authenticate-oidc'|'authenticate-cognito'|'redirect'|'fixed-response',
                    'TargetGroupArn': 'string',
                    'AuthenticateOidcConfig': {
                        'Issuer': 'string',
                        'AuthorizationEndpoint': 'string',
                        'TokenEndpoint': 'string',
                        'UserInfoEndpoint': 'string',
                        'ClientId': 'string',
                        'ClientSecret': 'string',
                        'SessionCookieName': 'string',
                        'Scope': 'string',
                        'SessionTimeout': 123,
                        'AuthenticationRequestExtraParams': {
                            'string': 'string'
                        },
                        'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate',
                        'UseExistingClientSecret': True|False
                    },
                    'AuthenticateCognitoConfig': {
                        'UserPoolArn': 'string',
                        'UserPoolClientId': 'string',
                        'UserPoolDomain': 'string',
                        'SessionCookieName': 'string',
                        'Scope': 'string',
                        'SessionTimeout': 123,
                        'AuthenticationRequestExtraParams': {
                            'string': 'string'
                        },
                        'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate'
                    },
                    'Order': 123,
                    'RedirectConfig': {
                        'Protocol': 'string',
                        'Port': 'string',
                        'Host': 'string',
                        'Path': 'string',
                        'Query': 'string',
                        'StatusCode': 'HTTP_301'|'HTTP_302'
                    },
                    'FixedResponseConfig': {
                        'MessageBody': 'string',
                        'StatusCode': 'string',
                        'ContentType': 'string'
                    },
                    'ForwardConfig': {
                        'TargetGroups': [
                            {
                                'TargetGroupArn': 'string',
                                'Weight': 123
                            },
                        ],
                        'TargetGroupStickinessConfig': {
                            'Enabled': True|False,
                            'DurationSeconds': 123
                        }
                    }
                },
            ],
            'IsDefault': True|False
        },
    ]
}


Response Structure

(dict) --

Rules (list) --
Information about the modified rule.

(dict) --
Information about a rule.

RuleArn (string) --
The Amazon Resource Name (ARN) of the rule.

Priority (string) --
The priority.

Conditions (list) --
The conditions. Each rule can include zero or one of the following conditions: http-request-method , host-header , path-pattern , and source-ip , and zero or more of the following conditions: http-header and query-string .

(dict) --
Information about a condition for a rule.

Field (string) --
The field in the HTTP request. The following are the possible values:

http-header
http-request-method
host-header
path-pattern
query-string
source-ip


Values (list) --
The condition value. You can use Values if the rule contains only host-header and path-pattern conditions. Otherwise, you can use HostHeaderConfig for host-header conditions and PathPatternConfig for path-pattern conditions.
If Field is host-header , you can specify a single host name (for example, my.example.com). A host name is case insensitive, can be up to 128 characters in length, and can contain any of the following characters.

A-Z, a-z, 0-9

.



(matches 0 or more characters)


? (matches exactly 1 character)

If Field is path-pattern , you can specify a single path pattern (for example, /img/*). A path pattern is case-sensitive, can be up to 128 characters in length, and can contain any of the following characters.

A-Z, a-z, 0-9
_ - . $ / ~ " \' @ : +
& (using &amp;)

(matches 0 or more characters)


? (matches exactly 1 character)


(string) --


HostHeaderConfig (dict) --
Information for a host header condition. Specify only when Field is host-header .

Values (list) --
One or more host names. The maximum size of each name is 128 characters. The comparison is case insensitive. The following wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly 1 character).
If you specify multiple strings, the condition is satisfied if one of the strings matches the host name.

(string) --




PathPatternConfig (dict) --
Information for a path pattern condition. Specify only when Field is path-pattern .

Values (list) --
One or more path patterns to compare against the request URL. The maximum size of each string is 128 characters. The comparison is case sensitive. The following wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly 1 character).
If you specify multiple strings, the condition is satisfied if one of them matches the request URL. The path pattern is compared only to the path of the URL, not to its query string. To compare against the query string, use  QueryStringConditionConfig .

(string) --




HttpHeaderConfig (dict) --
Information for an HTTP header condition. Specify only when Field is http-header .

HttpHeaderName (string) --
The name of the HTTP header field. The maximum size is 40 characters. The header name is case insensitive. The allowed characters are specified by RFC 7230. Wildcards are not supported.
You can\'t use an HTTP header condition to specify the host header. Use  HostHeaderConditionConfig to specify a host header condition.

Values (list) --
One or more strings to compare against the value of the HTTP header. The maximum size of each string is 128 characters. The comparison strings are case insensitive. The following wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly 1 character).
If the same header appears multiple times in the request, we search them in order until a match is found.
If you specify multiple strings, the condition is satisfied if one of the strings matches the value of the HTTP header. To require that all of the strings are a match, create one condition per string.

(string) --




QueryStringConfig (dict) --
Information for a query string condition. Specify only when Field is query-string .

Values (list) --
One or more key/value pairs or values to find in the query string. The maximum size of each string is 128 characters. The comparison is case insensitive. The following wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly 1 character). To search for a literal \'*\' or \'?\' character in a query string, you must escape these characters in Values using a \'\' character.
If you specify multiple key/value pairs or values, the condition is satisfied if one of them is found in the query string.

(dict) --
Information about a key/value pair.

Key (string) --
The key. You can omit the key.

Value (string) --
The value.







HttpRequestMethodConfig (dict) --
Information for an HTTP method condition. Specify only when Field is http-request-method .

Values (list) --
The name of the request method. The maximum size is 40 characters. The allowed characters are A-Z, hyphen (-), and underscore (_). The comparison is case sensitive. Wildcards are not supported; therefore, the method name must be an exact match.
If you specify multiple strings, the condition is satisfied if one of the strings matches the HTTP request method. We recommend that you route GET and HEAD requests in the same way, because the response to a HEAD request may be cached.

(string) --




SourceIpConfig (dict) --
Information for a source IP condition. Specify only when Field is source-ip .

Values (list) --
One or more source IP addresses, in CIDR format. You can use both IPv4 and IPv6 addresses. Wildcards are not supported.
If you specify multiple addresses, the condition is satisfied if the source IP address of the request matches one of the CIDR blocks. This condition is not satisfied by the addresses in the X-Forwarded-For header. To search for addresses in the X-Forwarded-For header, use  HttpHeaderConditionConfig .

(string) --








Actions (list) --
The actions. Each rule must include exactly one of the following types of actions: forward , redirect , or fixed-response , and it must be the last action to be performed.

(dict) --
Information about an action.

Type (string) --
The type of action.

TargetGroupArn (string) --
The Amazon Resource Name (ARN) of the target group. Specify only when Type is forward and you want to route to a single target group. To route to one or more target groups, use ForwardConfig instead.

AuthenticateOidcConfig (dict) --
[HTTPS listeners] Information about an identity provider that is compliant with OpenID Connect (OIDC). Specify only when Type is authenticate-oidc .

Issuer (string) --
The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

AuthorizationEndpoint (string) --
The authorization endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

TokenEndpoint (string) --
The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

UserInfoEndpoint (string) --
The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

ClientId (string) --
The OAuth 2.0 client identifier.

ClientSecret (string) --
The OAuth 2.0 client secret. This parameter is required if you are creating a rule. If you are modifying a rule, you can omit this parameter if you set UseExistingClientSecret to true.

SessionCookieName (string) --
The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.

Scope (string) --
The set of user claims to be requested from the IdP. The default is openid .
To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.

SessionTimeout (integer) --
The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).

AuthenticationRequestExtraParams (dict) --
The query parameters (up to 10) to include in the redirect request to the authorization endpoint.

(string) --
(string) --




OnUnauthenticatedRequest (string) --
The behavior if the user is not authenticated. The following are possible values:

deny- Return an HTTP 401 Unauthorized error.
allow- Allow the request to be forwarded to the target.
authenticate- Redirect the request to the IdP authorization endpoint. This is the default value.


UseExistingClientSecret (boolean) --
Indicates whether to use the existing client secret when modifying a rule. If you are creating a rule, you can omit this parameter or set it to false.



AuthenticateCognitoConfig (dict) --
[HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify only when Type is authenticate-cognito .

UserPoolArn (string) --
The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

UserPoolClientId (string) --
The ID of the Amazon Cognito user pool client.

UserPoolDomain (string) --
The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

SessionCookieName (string) --
The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.

Scope (string) --
The set of user claims to be requested from the IdP. The default is openid .
To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.

SessionTimeout (integer) --
The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).

AuthenticationRequestExtraParams (dict) --
The query parameters (up to 10) to include in the redirect request to the authorization endpoint.

(string) --
(string) --




OnUnauthenticatedRequest (string) --
The behavior if the user is not authenticated. The following are possible values:

deny- Return an HTTP 401 Unauthorized error.
allow- Allow the request to be forwarded to the target.
authenticate- Redirect the request to the IdP authorization endpoint. This is the default value.




Order (integer) --
The order for the action. This value is required for rules with multiple actions. The action with the lowest value for order is performed first. The last action to be performed must be one of the following types of actions: a forward , fixed-response , or redirect .

RedirectConfig (dict) --
[Application Load Balancer] Information for creating a redirect action. Specify only when Type is redirect .

Protocol (string) --
The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

Port (string) --
The port. You can specify a value from 1 to 65535 or #{port}.

Host (string) --
The hostname. This component is not percent-encoded. The hostname can contain #{host}.

Path (string) --
The absolute path, starting with the leading "/". This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}.

Query (string) --
The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading "?", as it is automatically added. You can specify any of the reserved keywords.

StatusCode (string) --
The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).



FixedResponseConfig (dict) --
[Application Load Balancer] Information for creating an action that returns a custom HTTP response. Specify only when Type is fixed-response .

MessageBody (string) --
The message.

StatusCode (string) --
The HTTP response code (2XX, 4XX, or 5XX).

ContentType (string) --
The content type.
Valid Values: text/plain | text/css | text/html | application/javascript | application/json



ForwardConfig (dict) --
Information for creating an action that distributes requests among one or more target groups. For Network Load Balancers, you can specify a single target group. Specify only when Type is forward . If you specify both ForwardConfig and TargetGroupArn , you can specify only one target group using ForwardConfig and it must be the same target group specified in TargetGroupArn .

TargetGroups (list) --
One or more target groups. For Network Load Balancers, you can specify a single target group.

(dict) --
Information about how traffic will be distributed between multiple target groups in a forward rule.

TargetGroupArn (string) --
The Amazon Resource Name (ARN) of the target group.

Weight (integer) --
The weight. The range is 0 to 999.





TargetGroupStickinessConfig (dict) --
The target group stickiness for the rule.

Enabled (boolean) --
Indicates whether target group stickiness is enabled.

DurationSeconds (integer) --
The time period, in seconds, during which requests from a client should be routed to the same target group. The range is 1-604800 seconds (7 days).









IsDefault (boolean) --
Indicates whether this is the default rule.











Exceptions

ElasticLoadBalancingv2.Client.exceptions.TargetGroupAssociationLimitException
ElasticLoadBalancingv2.Client.exceptions.IncompatibleProtocolsException
ElasticLoadBalancingv2.Client.exceptions.RuleNotFoundException
ElasticLoadBalancingv2.Client.exceptions.OperationNotPermittedException
ElasticLoadBalancingv2.Client.exceptions.TooManyRegistrationsForTargetIdException
ElasticLoadBalancingv2.Client.exceptions.TooManyTargetsException
ElasticLoadBalancingv2.Client.exceptions.TargetGroupNotFoundException
ElasticLoadBalancingv2.Client.exceptions.UnsupportedProtocolException
ElasticLoadBalancingv2.Client.exceptions.TooManyActionsException
ElasticLoadBalancingv2.Client.exceptions.InvalidLoadBalancerActionException
ElasticLoadBalancingv2.Client.exceptions.TooManyUniqueTargetGroupsPerLoadBalancerException

Examples
This example modifies the condition for the specified rule.
response = client.modify_rule(
    Conditions=[
        {
            'Field': 'path-pattern',
            'Values': [
                '/images/*',
            ],
        },
    ],
    RuleArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/9683b2d02a6cabee',
)

print(response)


Expected Output:
{
    'Rules': [
        {
            'Actions': [
                {
                    'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
                    'Type': 'forward',
                },
            ],
            'Conditions': [
                {
                    'Field': 'path-pattern',
                    'Values': [
                        '/images/*',
                    ],
                },
            ],
            'IsDefault': False,
            'Priority': '10',
            'RuleArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/9683b2d02a6cabee',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Rules': [
            {
                'RuleArn': 'string',
                'Priority': 'string',
                'Conditions': [
                    {
                        'Field': 'string',
                        'Values': [
                            'string',
                        ],
                        'HostHeaderConfig': {
                            'Values': [
                                'string',
                            ]
                        },
                        'PathPatternConfig': {
                            'Values': [
                                'string',
                            ]
                        },
                        'HttpHeaderConfig': {
                            'HttpHeaderName': 'string',
                            'Values': [
                                'string',
                            ]
                        },
                        'QueryStringConfig': {
                            'Values': [
                                {
                                    'Key': 'string',
                                    'Value': 'string'
                                },
                            ]
                        },
                        'HttpRequestMethodConfig': {
                            'Values': [
                                'string',
                            ]
                        },
                        'SourceIpConfig': {
                            'Values': [
                                'string',
                            ]
                        }
                    },
                ],
                'Actions': [
                    {
                        'Type': 'forward'|'authenticate-oidc'|'authenticate-cognito'|'redirect'|'fixed-response',
                        'TargetGroupArn': 'string',
                        'AuthenticateOidcConfig': {
                            'Issuer': 'string',
                            'AuthorizationEndpoint': 'string',
                            'TokenEndpoint': 'string',
                            'UserInfoEndpoint': 'string',
                            'ClientId': 'string',
                            'ClientSecret': 'string',
                            'SessionCookieName': 'string',
                            'Scope': 'string',
                            'SessionTimeout': 123,
                            'AuthenticationRequestExtraParams': {
                                'string': 'string'
                            },
                            'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate',
                            'UseExistingClientSecret': True|False
                        },
                        'AuthenticateCognitoConfig': {
                            'UserPoolArn': 'string',
                            'UserPoolClientId': 'string',
                            'UserPoolDomain': 'string',
                            'SessionCookieName': 'string',
                            'Scope': 'string',
                            'SessionTimeout': 123,
                            'AuthenticationRequestExtraParams': {
                                'string': 'string'
                            },
                            'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate'
                        },
                        'Order': 123,
                        'RedirectConfig': {
                            'Protocol': 'string',
                            'Port': 'string',
                            'Host': 'string',
                            'Path': 'string',
                            'Query': 'string',
                            'StatusCode': 'HTTP_301'|'HTTP_302'
                        },
                        'FixedResponseConfig': {
                            'MessageBody': 'string',
                            'StatusCode': 'string',
                            'ContentType': 'string'
                        },
                        'ForwardConfig': {
                            'TargetGroups': [
                                {
                                    'TargetGroupArn': 'string',
                                    'Weight': 123
                                },
                            ],
                            'TargetGroupStickinessConfig': {
                                'Enabled': True|False,
                                'DurationSeconds': 123
                            }
                        }
                    },
                ],
                'IsDefault': True|False
            },
        ]
    }
    
    
    :returns: 
    http-header
    http-request-method
    host-header
    path-pattern
    query-string
    source-ip
    
    """
    pass

def modify_target_group(TargetGroupArn=None, HealthCheckProtocol=None, HealthCheckPort=None, HealthCheckPath=None, HealthCheckEnabled=None, HealthCheckIntervalSeconds=None, HealthCheckTimeoutSeconds=None, HealthyThresholdCount=None, UnhealthyThresholdCount=None, Matcher=None):
    """
    Modifies the health checks used when evaluating the health state of the targets in the specified target group.
    To monitor the health of the targets, use  DescribeTargetHealth .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example changes the configuration of the health checks used to evaluate the health of the targets for the specified target group.
    Expected Output:
    
    :example: response = client.modify_target_group(
        TargetGroupArn='string',
        HealthCheckProtocol='HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
        HealthCheckPort='string',
        HealthCheckPath='string',
        HealthCheckEnabled=True|False,
        HealthCheckIntervalSeconds=123,
        HealthCheckTimeoutSeconds=123,
        HealthyThresholdCount=123,
        UnhealthyThresholdCount=123,
        Matcher={
            'HttpCode': 'string'
        }
    )
    
    
    :type TargetGroupArn: string
    :param TargetGroupArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the target group.\n

    :type HealthCheckProtocol: string
    :param HealthCheckProtocol: The protocol the load balancer uses when performing health checks on targets. The TCP protocol is supported for health checks only if the protocol of the target group is TCP, TLS, UDP, or TCP_UDP. The TLS, UDP, and TCP_UDP protocols are not supported for health checks.\nWith Network Load Balancers, you can\'t modify this setting.\n

    :type HealthCheckPort: string
    :param HealthCheckPort: The port the load balancer uses when performing health checks on targets.

    :type HealthCheckPath: string
    :param HealthCheckPath: [HTTP/HTTPS health checks] The ping path that is the destination for the health check request.

    :type HealthCheckEnabled: boolean
    :param HealthCheckEnabled: Indicates whether health checks are enabled.

    :type HealthCheckIntervalSeconds: integer
    :param HealthCheckIntervalSeconds: The approximate amount of time, in seconds, between health checks of an individual target. For Application Load Balancers, the range is 5 to 300 seconds. For Network Load Balancers, the supported values are 10 or 30 seconds.\nWith Network Load Balancers, you can\'t modify this setting.\n

    :type HealthCheckTimeoutSeconds: integer
    :param HealthCheckTimeoutSeconds: [HTTP/HTTPS health checks] The amount of time, in seconds, during which no response means a failed health check.\nWith Network Load Balancers, you can\'t modify this setting.\n

    :type HealthyThresholdCount: integer
    :param HealthyThresholdCount: The number of consecutive health checks successes required before considering an unhealthy target healthy.

    :type UnhealthyThresholdCount: integer
    :param UnhealthyThresholdCount: The number of consecutive health check failures required before considering the target unhealthy. For Network Load Balancers, this value must be the same as the healthy threshold count.

    :type Matcher: dict
    :param Matcher: [HTTP/HTTPS health checks] The HTTP codes to use when checking for a successful response from a target.\nWith Network Load Balancers, you can\'t modify this setting.\n\nHttpCode (string) -- [REQUIRED]The HTTP codes.\nFor Application Load Balancers, you can specify values between 200 and 499, and the default value is 200. You can specify multiple values (for example, '200,202') or a range of values (for example, '200-299').\nFor Network Load Balancers, this is 200\xe2\x80\x93399.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TargetGroups': [
        {
            'TargetGroupArn': 'string',
            'TargetGroupName': 'string',
            'Protocol': 'HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
            'Port': 123,
            'VpcId': 'string',
            'HealthCheckProtocol': 'HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
            'HealthCheckPort': 'string',
            'HealthCheckEnabled': True|False,
            'HealthCheckIntervalSeconds': 123,
            'HealthCheckTimeoutSeconds': 123,
            'HealthyThresholdCount': 123,
            'UnhealthyThresholdCount': 123,
            'HealthCheckPath': 'string',
            'Matcher': {
                'HttpCode': 'string'
            },
            'LoadBalancerArns': [
                'string',
            ],
            'TargetType': 'instance'|'ip'|'lambda'
        },
    ]
}


Response Structure

(dict) --

TargetGroups (list) --
Information about the modified target group.

(dict) --
Information about a target group.

TargetGroupArn (string) --
The Amazon Resource Name (ARN) of the target group.

TargetGroupName (string) --
The name of the target group.

Protocol (string) --
The protocol to use for routing traffic to the targets.

Port (integer) --
The port on which the targets are listening. Not used if the target is a Lambda function.

VpcId (string) --
The ID of the VPC for the targets.

HealthCheckProtocol (string) --
The protocol to use to connect with the target.

HealthCheckPort (string) --
The port to use to connect with the target.

HealthCheckEnabled (boolean) --
Indicates whether health checks are enabled.

HealthCheckIntervalSeconds (integer) --
The approximate amount of time, in seconds, between health checks of an individual target.

HealthCheckTimeoutSeconds (integer) --
The amount of time, in seconds, during which no response means a failed health check.

HealthyThresholdCount (integer) --
The number of consecutive health checks successes required before considering an unhealthy target healthy.

UnhealthyThresholdCount (integer) --
The number of consecutive health check failures required before considering the target unhealthy.

HealthCheckPath (string) --
The destination for the health check request.

Matcher (dict) --
The HTTP codes to use when checking for a successful response from a target.

HttpCode (string) --
The HTTP codes.
For Application Load Balancers, you can specify values between 200 and 499, and the default value is 200. You can specify multiple values (for example, "200,202") or a range of values (for example, "200-299").
For Network Load Balancers, this is 200\xe2\x80\x93399.



LoadBalancerArns (list) --
The Amazon Resource Names (ARN) of the load balancers that route traffic to this target group.

(string) --


TargetType (string) --
The type of target that you must specify when registering targets with this target group. The possible values are instance (targets are specified by instance ID) or ip (targets are specified by IP address).











Exceptions

ElasticLoadBalancingv2.Client.exceptions.TargetGroupNotFoundException
ElasticLoadBalancingv2.Client.exceptions.InvalidConfigurationRequestException

Examples
This example changes the configuration of the health checks used to evaluate the health of the targets for the specified target group.
response = client.modify_target_group(
    HealthCheckPort='443',
    HealthCheckProtocol='HTTPS',
    TargetGroupArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-https-targets/2453ed029918f21f',
)

print(response)


Expected Output:
{
    'TargetGroups': [
        {
            'HealthCheckIntervalSeconds': 30,
            'HealthCheckPort': '443',
            'HealthCheckProtocol': 'HTTPS',
            'HealthCheckTimeoutSeconds': 5,
            'HealthyThresholdCount': 5,
            'LoadBalancerArns': [
                'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
            ],
            'Matcher': {
                'HttpCode': '200',
            },
            'Port': 443,
            'Protocol': 'HTTPS',
            'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-https-targets/2453ed029918f21f',
            'TargetGroupName': 'my-https-targets',
            'UnhealthyThresholdCount': 2,
            'VpcId': 'vpc-3ac0fb5f',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'TargetGroups': [
            {
                'TargetGroupArn': 'string',
                'TargetGroupName': 'string',
                'Protocol': 'HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
                'Port': 123,
                'VpcId': 'string',
                'HealthCheckProtocol': 'HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
                'HealthCheckPort': 'string',
                'HealthCheckEnabled': True|False,
                'HealthCheckIntervalSeconds': 123,
                'HealthCheckTimeoutSeconds': 123,
                'HealthyThresholdCount': 123,
                'UnhealthyThresholdCount': 123,
                'HealthCheckPath': 'string',
                'Matcher': {
                    'HttpCode': 'string'
                },
                'LoadBalancerArns': [
                    'string',
                ],
                'TargetType': 'instance'|'ip'|'lambda'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def modify_target_group_attributes(TargetGroupArn=None, Attributes=None):
    """
    Modifies the specified attributes of the specified target group.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example sets the deregistration delay timeout to the specified value for the specified target group.
    Expected Output:
    
    :example: response = client.modify_target_group_attributes(
        TargetGroupArn='string',
        Attributes=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type TargetGroupArn: string
    :param TargetGroupArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the target group.\n

    :type Attributes: list
    :param Attributes: [REQUIRED]\nThe attributes.\n\n(dict) --Information about a target group attribute.\n\nKey (string) --The name of the attribute.\nThe following attributes are supported by both Application Load Balancers and Network Load Balancers:\n\nderegistration_delay.timeout_seconds - The amount of time, in seconds, for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused . The range is 0-3600 seconds. The default value is 300 seconds. If the target is a Lambda function, this attribute is not supported.\nstickiness.enabled - Indicates whether sticky sessions are enabled. The value is true or false . The default is false .\nstickiness.type - The type of sticky sessions. The possible values are lb_cookie for Application Load Balancers or source_ip for Network Load Balancers.\n\nThe following attributes are supported only if the load balancer is an Application Load Balancer and the target is an instance or an IP address:\n\nload_balancing.algorithm.type - The load balancing algorithm determines how the load balancer selects targets when routing requests. The value is round_robin or least_outstanding_requests . The default is round_robin .\nslow_start.duration_seconds - The time period, in seconds, during which a newly registered target receives an increasing share of the traffic to the target group. After this time period ends, the target receives its full share of traffic. The range is 30-900 seconds (15 minutes). Slow start mode is disabled by default.\nstickiness.lb_cookie.duration_seconds - The time period, in seconds, during which requests from a client should be routed to the same target. After this time period expires, the load balancer-generated cookie is considered stale. The range is 1 second to 1 week (604800 seconds). The default value is 1 day (86400 seconds).\n\nThe following attribute is supported only if the load balancer is an Application Load Balancer and the target is a Lambda function:\n\nlambda.multi_value_headers.enabled - Indicates whether the request and response headers that are exchanged between the load balancer and the Lambda function include arrays of values or strings. The value is true or false . The default is false . If the value is false and the request contains a duplicate header field name or query parameter key, the load balancer uses the last value sent by the client.\n\nThe following attribute is supported only by Network Load Balancers:\n\nproxy_protocol_v2.enabled - Indicates whether Proxy Protocol version 2 is enabled. The value is true or false . The default is false .\n\n\nValue (string) --The value of the attribute.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Attributes': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --

Attributes (list) --
Information about the attributes.

(dict) --
Information about a target group attribute.

Key (string) --
The name of the attribute.
The following attributes are supported by both Application Load Balancers and Network Load Balancers:

deregistration_delay.timeout_seconds - The amount of time, in seconds, for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused . The range is 0-3600 seconds. The default value is 300 seconds. If the target is a Lambda function, this attribute is not supported.
stickiness.enabled - Indicates whether sticky sessions are enabled. The value is true or false . The default is false .
stickiness.type - The type of sticky sessions. The possible values are lb_cookie for Application Load Balancers or source_ip for Network Load Balancers.

The following attributes are supported only if the load balancer is an Application Load Balancer and the target is an instance or an IP address:

load_balancing.algorithm.type - The load balancing algorithm determines how the load balancer selects targets when routing requests. The value is round_robin or least_outstanding_requests . The default is round_robin .
slow_start.duration_seconds - The time period, in seconds, during which a newly registered target receives an increasing share of the traffic to the target group. After this time period ends, the target receives its full share of traffic. The range is 30-900 seconds (15 minutes). Slow start mode is disabled by default.
stickiness.lb_cookie.duration_seconds - The time period, in seconds, during which requests from a client should be routed to the same target. After this time period expires, the load balancer-generated cookie is considered stale. The range is 1 second to 1 week (604800 seconds). The default value is 1 day (86400 seconds).

The following attribute is supported only if the load balancer is an Application Load Balancer and the target is a Lambda function:

lambda.multi_value_headers.enabled - Indicates whether the request and response headers that are exchanged between the load balancer and the Lambda function include arrays of values or strings. The value is true or false . The default is false . If the value is false and the request contains a duplicate header field name or query parameter key, the load balancer uses the last value sent by the client.

The following attribute is supported only by Network Load Balancers:

proxy_protocol_v2.enabled - Indicates whether Proxy Protocol version 2 is enabled. The value is true or false . The default is false .


Value (string) --
The value of the attribute.











Exceptions

ElasticLoadBalancingv2.Client.exceptions.TargetGroupNotFoundException
ElasticLoadBalancingv2.Client.exceptions.InvalidConfigurationRequestException

Examples
This example sets the deregistration delay timeout to the specified value for the specified target group.
response = client.modify_target_group_attributes(
    Attributes=[
        {
            'Key': 'deregistration_delay.timeout_seconds',
            'Value': '600',
        },
    ],
    TargetGroupArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
)

print(response)


Expected Output:
{
    'Attributes': [
        {
            'Key': 'stickiness.enabled',
            'Value': 'false',
        },
        {
            'Key': 'deregistration_delay.timeout_seconds',
            'Value': '600',
        },
        {
            'Key': 'stickiness.type',
            'Value': 'lb_cookie',
        },
        {
            'Key': 'stickiness.lb_cookie.duration_seconds',
            'Value': '86400',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Attributes': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    :returns: 
    deregistration_delay.timeout_seconds - The amount of time, in seconds, for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused . The range is 0-3600 seconds. The default value is 300 seconds. If the target is a Lambda function, this attribute is not supported.
    stickiness.enabled - Indicates whether sticky sessions are enabled. The value is true or false . The default is false .
    stickiness.type - The type of sticky sessions. The possible values are lb_cookie for Application Load Balancers or source_ip for Network Load Balancers.
    
    """
    pass

def register_targets(TargetGroupArn=None, Targets=None):
    """
    Registers the specified targets with the specified target group.
    If the target is an EC2 instance, it must be in the running state when you register it.
    By default, the load balancer routes requests to registered targets using the protocol and port for the target group. Alternatively, you can override the port for a target when you register it. You can register each EC2 instance or IP address with the same target group multiple times using different ports.
    With a Network Load Balancer, you cannot register instances by instance ID if they have the following instance types: C1, CC1, CC2, CG1, CG2, CR1, CS1, G1, G2, HI1, HS1, M1, M2, M3, and T1. You can register instances of these types by IP address.
    To remove a target from a target group, use  DeregisterTargets .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example registers the specified instances with the specified target group.
    Expected Output:
    This example registers the specified instance with the specified target group using multiple ports. This enables you to register ECS containers on the same instance as targets in the target group.
    Expected Output:
    
    :example: response = client.register_targets(
        TargetGroupArn='string',
        Targets=[
            {
                'Id': 'string',
                'Port': 123,
                'AvailabilityZone': 'string'
            },
        ]
    )
    
    
    :type TargetGroupArn: string
    :param TargetGroupArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the target group.\n

    :type Targets: list
    :param Targets: [REQUIRED]\nThe targets.\nTo register a target by instance ID, specify the instance ID. To register a target by IP address, specify the IP address. To register a Lambda function, specify the ARN of the Lambda function.\n\n(dict) --Information about a target.\n\nId (string) -- [REQUIRED]The ID of the target. If the target type of the target group is instance , specify an instance ID. If the target type is ip , specify an IP address. If the target type is lambda , specify the ARN of the Lambda function.\n\nPort (integer) --The port on which the target is listening. Not used if the target is a Lambda function.\n\nAvailabilityZone (string) --An Availability Zone or all . This determines whether the target receives traffic from the load balancer nodes in the specified Availability Zone or from all enabled Availability Zones for the load balancer.\nThis parameter is not supported if the target type of the target group is instance .\nIf the target type is ip and the IP address is in a subnet of the VPC for the target group, the Availability Zone is automatically detected and this parameter is optional. If the IP address is outside the VPC, this parameter is required.\nWith an Application Load Balancer, if the target type is ip and the IP address is outside the VPC for the target group, the only supported value is all .\nIf the target type is lambda , this parameter is optional and the only supported value is all .\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ElasticLoadBalancingv2.Client.exceptions.TargetGroupNotFoundException
ElasticLoadBalancingv2.Client.exceptions.TooManyTargetsException
ElasticLoadBalancingv2.Client.exceptions.InvalidTargetException
ElasticLoadBalancingv2.Client.exceptions.TooManyRegistrationsForTargetIdException

Examples
This example registers the specified instances with the specified target group.
response = client.register_targets(
    TargetGroupArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
    Targets=[
        {
            'Id': 'i-80c8dd94',
        },
        {
            'Id': 'i-ceddcd4d',
        },
    ],
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}


This example registers the specified instance with the specified target group using multiple ports. This enables you to register ECS containers on the same instance as targets in the target group.
response = client.register_targets(
    TargetGroupArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-new-targets/3bb63f11dfb0faf9',
    Targets=[
        {
            'Id': 'i-80c8dd94',
            'Port': 80,
        },
        {
            'Id': 'i-80c8dd94',
            'Port': 766,
        },
    ],
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def remove_listener_certificates(ListenerArn=None, Certificates=None):
    """
    Removes the specified certificate from the certificate list for the specified HTTPS or TLS listener.
    You can\'t remove the default certificate for a listener. To replace the default certificate, call  ModifyListener .
    To list the certificates for your listener, use  DescribeListenerCertificates .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.remove_listener_certificates(
        ListenerArn='string',
        Certificates=[
            {
                'CertificateArn': 'string',
                'IsDefault': True|False
            },
        ]
    )
    
    
    :type ListenerArn: string
    :param ListenerArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the listener.\n

    :type Certificates: list
    :param Certificates: [REQUIRED]\nThe certificate to remove. You can specify one certificate per call. Set CertificateArn to the certificate ARN but do not set IsDefault .\n\n(dict) --Information about an SSL server certificate.\n\nCertificateArn (string) --The Amazon Resource Name (ARN) of the certificate.\n\nIsDefault (boolean) --Indicates whether the certificate is the default certificate. Do not set this value when specifying a certificate as an input. This value is not included in the output when describing a listener, but is included when describing listener certificates.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ElasticLoadBalancingv2.Client.exceptions.ListenerNotFoundException
ElasticLoadBalancingv2.Client.exceptions.OperationNotPermittedException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def remove_tags(ResourceArns=None, TagKeys=None):
    """
    Removes the specified tags from the specified Elastic Load Balancing resource.
    To list the current tags for your resources, use  DescribeTags .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example removes the specified tags from the specified load balancer.
    Expected Output:
    
    :example: response = client.remove_tags(
        ResourceArns=[
            'string',
        ],
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArns: list
    :param ResourceArns: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource.\n\n(string) --\n\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe tag keys for the tags to remove.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ElasticLoadBalancingv2.Client.exceptions.LoadBalancerNotFoundException
ElasticLoadBalancingv2.Client.exceptions.TargetGroupNotFoundException
ElasticLoadBalancingv2.Client.exceptions.ListenerNotFoundException
ElasticLoadBalancingv2.Client.exceptions.RuleNotFoundException
ElasticLoadBalancingv2.Client.exceptions.TooManyTagsException

Examples
This example removes the specified tags from the specified load balancer.
response = client.remove_tags(
    ResourceArns=[
        'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
    ],
    TagKeys=[
        'project',
        'department',
    ],
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def set_ip_address_type(LoadBalancerArn=None, IpAddressType=None):
    """
    Sets the type of IP addresses used by the subnets of the specified Application Load Balancer or Network Load Balancer.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.set_ip_address_type(
        LoadBalancerArn='string',
        IpAddressType='ipv4'|'dualstack'
    )
    
    
    :type LoadBalancerArn: string
    :param LoadBalancerArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the load balancer.\n

    :type IpAddressType: string
    :param IpAddressType: [REQUIRED]\nThe IP address type. The possible values are ipv4 (for IPv4 addresses) and dualstack (for IPv4 and IPv6 addresses). Internal load balancers must use ipv4 . Network Load Balancers must use ipv4 .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'IpAddressType': 'ipv4'|'dualstack'
}


Response Structure

(dict) --

IpAddressType (string) --
The IP address type.







Exceptions

ElasticLoadBalancingv2.Client.exceptions.LoadBalancerNotFoundException
ElasticLoadBalancingv2.Client.exceptions.InvalidConfigurationRequestException
ElasticLoadBalancingv2.Client.exceptions.InvalidSubnetException


    :return: {
        'IpAddressType': 'ipv4'|'dualstack'
    }
    
    
    :returns: 
    ElasticLoadBalancingv2.Client.exceptions.LoadBalancerNotFoundException
    ElasticLoadBalancingv2.Client.exceptions.InvalidConfigurationRequestException
    ElasticLoadBalancingv2.Client.exceptions.InvalidSubnetException
    
    """
    pass

def set_rule_priorities(RulePriorities=None):
    """
    Sets the priorities of the specified rules.
    You can reorder the rules as long as there are no priority conflicts in the new order. Any existing rules that you do not specify retain their current priority.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example sets the priority of the specified rule.
    Expected Output:
    
    :example: response = client.set_rule_priorities(
        RulePriorities=[
            {
                'RuleArn': 'string',
                'Priority': 123
            },
        ]
    )
    
    
    :type RulePriorities: list
    :param RulePriorities: [REQUIRED]\nThe rule priorities.\n\n(dict) --Information about the priorities for the rules for a listener.\n\nRuleArn (string) --The Amazon Resource Name (ARN) of the rule.\n\nPriority (integer) --The rule priority.\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'Rules': [
        {
            'RuleArn': 'string',
            'Priority': 'string',
            'Conditions': [
                {
                    'Field': 'string',
                    'Values': [
                        'string',
                    ],
                    'HostHeaderConfig': {
                        'Values': [
                            'string',
                        ]
                    },
                    'PathPatternConfig': {
                        'Values': [
                            'string',
                        ]
                    },
                    'HttpHeaderConfig': {
                        'HttpHeaderName': 'string',
                        'Values': [
                            'string',
                        ]
                    },
                    'QueryStringConfig': {
                        'Values': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                    'HttpRequestMethodConfig': {
                        'Values': [
                            'string',
                        ]
                    },
                    'SourceIpConfig': {
                        'Values': [
                            'string',
                        ]
                    }
                },
            ],
            'Actions': [
                {
                    'Type': 'forward'|'authenticate-oidc'|'authenticate-cognito'|'redirect'|'fixed-response',
                    'TargetGroupArn': 'string',
                    'AuthenticateOidcConfig': {
                        'Issuer': 'string',
                        'AuthorizationEndpoint': 'string',
                        'TokenEndpoint': 'string',
                        'UserInfoEndpoint': 'string',
                        'ClientId': 'string',
                        'ClientSecret': 'string',
                        'SessionCookieName': 'string',
                        'Scope': 'string',
                        'SessionTimeout': 123,
                        'AuthenticationRequestExtraParams': {
                            'string': 'string'
                        },
                        'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate',
                        'UseExistingClientSecret': True|False
                    },
                    'AuthenticateCognitoConfig': {
                        'UserPoolArn': 'string',
                        'UserPoolClientId': 'string',
                        'UserPoolDomain': 'string',
                        'SessionCookieName': 'string',
                        'Scope': 'string',
                        'SessionTimeout': 123,
                        'AuthenticationRequestExtraParams': {
                            'string': 'string'
                        },
                        'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate'
                    },
                    'Order': 123,
                    'RedirectConfig': {
                        'Protocol': 'string',
                        'Port': 'string',
                        'Host': 'string',
                        'Path': 'string',
                        'Query': 'string',
                        'StatusCode': 'HTTP_301'|'HTTP_302'
                    },
                    'FixedResponseConfig': {
                        'MessageBody': 'string',
                        'StatusCode': 'string',
                        'ContentType': 'string'
                    },
                    'ForwardConfig': {
                        'TargetGroups': [
                            {
                                'TargetGroupArn': 'string',
                                'Weight': 123
                            },
                        ],
                        'TargetGroupStickinessConfig': {
                            'Enabled': True|False,
                            'DurationSeconds': 123
                        }
                    }
                },
            ],
            'IsDefault': True|False
        },
    ]
}


Response Structure

(dict) --
Rules (list) --Information about the rules.

(dict) --Information about a rule.

RuleArn (string) --The Amazon Resource Name (ARN) of the rule.

Priority (string) --The priority.

Conditions (list) --The conditions. Each rule can include zero or one of the following conditions: http-request-method , host-header , path-pattern , and source-ip , and zero or more of the following conditions: http-header and query-string .

(dict) --Information about a condition for a rule.

Field (string) --The field in the HTTP request. The following are the possible values:

http-header
http-request-method
host-header
path-pattern
query-string
source-ip


Values (list) --The condition value. You can use Values if the rule contains only host-header and path-pattern conditions. Otherwise, you can use HostHeaderConfig for host-header conditions and PathPatternConfig for path-pattern conditions.
If Field is host-header , you can specify a single host name (for example, my.example.com). A host name is case insensitive, can be up to 128 characters in length, and can contain any of the following characters.

A-Z, a-z, 0-9

.



(matches 0 or more characters)


? (matches exactly 1 character)

If Field is path-pattern , you can specify a single path pattern (for example, /img/*). A path pattern is case-sensitive, can be up to 128 characters in length, and can contain any of the following characters.

A-Z, a-z, 0-9
_ - . $ / ~ " \' @ : +
& (using &amp;)

(matches 0 or more characters)


? (matches exactly 1 character)


(string) --


HostHeaderConfig (dict) --Information for a host header condition. Specify only when Field is host-header .

Values (list) --One or more host names. The maximum size of each name is 128 characters. The comparison is case insensitive. The following wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly 1 character).
If you specify multiple strings, the condition is satisfied if one of the strings matches the host name.

(string) --




PathPatternConfig (dict) --Information for a path pattern condition. Specify only when Field is path-pattern .

Values (list) --One or more path patterns to compare against the request URL. The maximum size of each string is 128 characters. The comparison is case sensitive. The following wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly 1 character).
If you specify multiple strings, the condition is satisfied if one of them matches the request URL. The path pattern is compared only to the path of the URL, not to its query string. To compare against the query string, use  QueryStringConditionConfig .

(string) --




HttpHeaderConfig (dict) --Information for an HTTP header condition. Specify only when Field is http-header .

HttpHeaderName (string) --The name of the HTTP header field. The maximum size is 40 characters. The header name is case insensitive. The allowed characters are specified by RFC 7230. Wildcards are not supported.
You can\'t use an HTTP header condition to specify the host header. Use  HostHeaderConditionConfig to specify a host header condition.

Values (list) --One or more strings to compare against the value of the HTTP header. The maximum size of each string is 128 characters. The comparison strings are case insensitive. The following wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly 1 character).
If the same header appears multiple times in the request, we search them in order until a match is found.
If you specify multiple strings, the condition is satisfied if one of the strings matches the value of the HTTP header. To require that all of the strings are a match, create one condition per string.

(string) --




QueryStringConfig (dict) --Information for a query string condition. Specify only when Field is query-string .

Values (list) --One or more key/value pairs or values to find in the query string. The maximum size of each string is 128 characters. The comparison is case insensitive. The following wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly 1 character). To search for a literal \'*\' or \'?\' character in a query string, you must escape these characters in Values using a \'\' character.
If you specify multiple key/value pairs or values, the condition is satisfied if one of them is found in the query string.

(dict) --Information about a key/value pair.

Key (string) --The key. You can omit the key.

Value (string) --The value.







HttpRequestMethodConfig (dict) --Information for an HTTP method condition. Specify only when Field is http-request-method .

Values (list) --The name of the request method. The maximum size is 40 characters. The allowed characters are A-Z, hyphen (-), and underscore (_). The comparison is case sensitive. Wildcards are not supported; therefore, the method name must be an exact match.
If you specify multiple strings, the condition is satisfied if one of the strings matches the HTTP request method. We recommend that you route GET and HEAD requests in the same way, because the response to a HEAD request may be cached.

(string) --




SourceIpConfig (dict) --Information for a source IP condition. Specify only when Field is source-ip .

Values (list) --One or more source IP addresses, in CIDR format. You can use both IPv4 and IPv6 addresses. Wildcards are not supported.
If you specify multiple addresses, the condition is satisfied if the source IP address of the request matches one of the CIDR blocks. This condition is not satisfied by the addresses in the X-Forwarded-For header. To search for addresses in the X-Forwarded-For header, use  HttpHeaderConditionConfig .

(string) --








Actions (list) --The actions. Each rule must include exactly one of the following types of actions: forward , redirect , or fixed-response , and it must be the last action to be performed.

(dict) --Information about an action.

Type (string) --The type of action.

TargetGroupArn (string) --The Amazon Resource Name (ARN) of the target group. Specify only when Type is forward and you want to route to a single target group. To route to one or more target groups, use ForwardConfig instead.

AuthenticateOidcConfig (dict) --[HTTPS listeners] Information about an identity provider that is compliant with OpenID Connect (OIDC). Specify only when Type is authenticate-oidc .

Issuer (string) --The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

AuthorizationEndpoint (string) --The authorization endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

TokenEndpoint (string) --The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

UserInfoEndpoint (string) --The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

ClientId (string) --The OAuth 2.0 client identifier.

ClientSecret (string) --The OAuth 2.0 client secret. This parameter is required if you are creating a rule. If you are modifying a rule, you can omit this parameter if you set UseExistingClientSecret to true.

SessionCookieName (string) --The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.

Scope (string) --The set of user claims to be requested from the IdP. The default is openid .
To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.

SessionTimeout (integer) --The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).

AuthenticationRequestExtraParams (dict) --The query parameters (up to 10) to include in the redirect request to the authorization endpoint.

(string) --
(string) --




OnUnauthenticatedRequest (string) --The behavior if the user is not authenticated. The following are possible values:

deny- Return an HTTP 401 Unauthorized error.
allow- Allow the request to be forwarded to the target.
authenticate- Redirect the request to the IdP authorization endpoint. This is the default value.


UseExistingClientSecret (boolean) --Indicates whether to use the existing client secret when modifying a rule. If you are creating a rule, you can omit this parameter or set it to false.



AuthenticateCognitoConfig (dict) --[HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify only when Type is authenticate-cognito .

UserPoolArn (string) --The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

UserPoolClientId (string) --The ID of the Amazon Cognito user pool client.

UserPoolDomain (string) --The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

SessionCookieName (string) --The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.

Scope (string) --The set of user claims to be requested from the IdP. The default is openid .
To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.

SessionTimeout (integer) --The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).

AuthenticationRequestExtraParams (dict) --The query parameters (up to 10) to include in the redirect request to the authorization endpoint.

(string) --
(string) --




OnUnauthenticatedRequest (string) --The behavior if the user is not authenticated. The following are possible values:

deny- Return an HTTP 401 Unauthorized error.
allow- Allow the request to be forwarded to the target.
authenticate- Redirect the request to the IdP authorization endpoint. This is the default value.




Order (integer) --The order for the action. This value is required for rules with multiple actions. The action with the lowest value for order is performed first. The last action to be performed must be one of the following types of actions: a forward , fixed-response , or redirect .

RedirectConfig (dict) --[Application Load Balancer] Information for creating a redirect action. Specify only when Type is redirect .

Protocol (string) --The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

Port (string) --The port. You can specify a value from 1 to 65535 or #{port}.

Host (string) --The hostname. This component is not percent-encoded. The hostname can contain #{host}.

Path (string) --The absolute path, starting with the leading "/". This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}.

Query (string) --The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading "?", as it is automatically added. You can specify any of the reserved keywords.

StatusCode (string) --The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).



FixedResponseConfig (dict) --[Application Load Balancer] Information for creating an action that returns a custom HTTP response. Specify only when Type is fixed-response .

MessageBody (string) --The message.

StatusCode (string) --The HTTP response code (2XX, 4XX, or 5XX).

ContentType (string) --The content type.
Valid Values: text/plain | text/css | text/html | application/javascript | application/json



ForwardConfig (dict) --Information for creating an action that distributes requests among one or more target groups. For Network Load Balancers, you can specify a single target group. Specify only when Type is forward . If you specify both ForwardConfig and TargetGroupArn , you can specify only one target group using ForwardConfig and it must be the same target group specified in TargetGroupArn .

TargetGroups (list) --One or more target groups. For Network Load Balancers, you can specify a single target group.

(dict) --Information about how traffic will be distributed between multiple target groups in a forward rule.

TargetGroupArn (string) --The Amazon Resource Name (ARN) of the target group.

Weight (integer) --The weight. The range is 0 to 999.





TargetGroupStickinessConfig (dict) --The target group stickiness for the rule.

Enabled (boolean) --Indicates whether target group stickiness is enabled.

DurationSeconds (integer) --The time period, in seconds, during which requests from a client should be routed to the same target group. The range is 1-604800 seconds (7 days).









IsDefault (boolean) --Indicates whether this is the default rule.










Exceptions

ElasticLoadBalancingv2.Client.exceptions.RuleNotFoundException
ElasticLoadBalancingv2.Client.exceptions.PriorityInUseException
ElasticLoadBalancingv2.Client.exceptions.OperationNotPermittedException

Examples
This example sets the priority of the specified rule.
response = client.set_rule_priorities(
    RulePriorities=[
        {
            'Priority': 5,
            'RuleArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/1291d13826f405c3',
        },
    ],
)

print(response)


Expected Output:
{
    'Rules': [
        {
            'Actions': [
                {
                    'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
                    'Type': 'forward',
                },
            ],
            'Conditions': [
                {
                    'Field': 'path-pattern',
                    'Values': [
                        '/img/*',
                    ],
                },
            ],
            'IsDefault': False,
            'Priority': '5',
            'RuleArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/1291d13826f405c3',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Rules': [
            {
                'RuleArn': 'string',
                'Priority': 'string',
                'Conditions': [
                    {
                        'Field': 'string',
                        'Values': [
                            'string',
                        ],
                        'HostHeaderConfig': {
                            'Values': [
                                'string',
                            ]
                        },
                        'PathPatternConfig': {
                            'Values': [
                                'string',
                            ]
                        },
                        'HttpHeaderConfig': {
                            'HttpHeaderName': 'string',
                            'Values': [
                                'string',
                            ]
                        },
                        'QueryStringConfig': {
                            'Values': [
                                {
                                    'Key': 'string',
                                    'Value': 'string'
                                },
                            ]
                        },
                        'HttpRequestMethodConfig': {
                            'Values': [
                                'string',
                            ]
                        },
                        'SourceIpConfig': {
                            'Values': [
                                'string',
                            ]
                        }
                    },
                ],
                'Actions': [
                    {
                        'Type': 'forward'|'authenticate-oidc'|'authenticate-cognito'|'redirect'|'fixed-response',
                        'TargetGroupArn': 'string',
                        'AuthenticateOidcConfig': {
                            'Issuer': 'string',
                            'AuthorizationEndpoint': 'string',
                            'TokenEndpoint': 'string',
                            'UserInfoEndpoint': 'string',
                            'ClientId': 'string',
                            'ClientSecret': 'string',
                            'SessionCookieName': 'string',
                            'Scope': 'string',
                            'SessionTimeout': 123,
                            'AuthenticationRequestExtraParams': {
                                'string': 'string'
                            },
                            'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate',
                            'UseExistingClientSecret': True|False
                        },
                        'AuthenticateCognitoConfig': {
                            'UserPoolArn': 'string',
                            'UserPoolClientId': 'string',
                            'UserPoolDomain': 'string',
                            'SessionCookieName': 'string',
                            'Scope': 'string',
                            'SessionTimeout': 123,
                            'AuthenticationRequestExtraParams': {
                                'string': 'string'
                            },
                            'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate'
                        },
                        'Order': 123,
                        'RedirectConfig': {
                            'Protocol': 'string',
                            'Port': 'string',
                            'Host': 'string',
                            'Path': 'string',
                            'Query': 'string',
                            'StatusCode': 'HTTP_301'|'HTTP_302'
                        },
                        'FixedResponseConfig': {
                            'MessageBody': 'string',
                            'StatusCode': 'string',
                            'ContentType': 'string'
                        },
                        'ForwardConfig': {
                            'TargetGroups': [
                                {
                                    'TargetGroupArn': 'string',
                                    'Weight': 123
                                },
                            ],
                            'TargetGroupStickinessConfig': {
                                'Enabled': True|False,
                                'DurationSeconds': 123
                            }
                        }
                    },
                ],
                'IsDefault': True|False
            },
        ]
    }
    
    
    :returns: 
    A-Z, a-z, 0-9
    
    .
    
    
    
    (matches 0 or more characters)
    
    
    ? (matches exactly 1 character)
    
    """
    pass

def set_security_groups(LoadBalancerArn=None, SecurityGroups=None):
    """
    Associates the specified security groups with the specified Application Load Balancer. The specified security groups override the previously associated security groups.
    You can\'t specify a security group for a Network Load Balancer.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example associates the specified security group with the specified load balancer.
    Expected Output:
    
    :example: response = client.set_security_groups(
        LoadBalancerArn='string',
        SecurityGroups=[
            'string',
        ]
    )
    
    
    :type LoadBalancerArn: string
    :param LoadBalancerArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the load balancer.\n

    :type SecurityGroups: list
    :param SecurityGroups: [REQUIRED]\nThe IDs of the security groups.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'SecurityGroupIds': [
        'string',
    ]
}


Response Structure

(dict) --

SecurityGroupIds (list) --
The IDs of the security groups associated with the load balancer.

(string) --








Exceptions

ElasticLoadBalancingv2.Client.exceptions.LoadBalancerNotFoundException
ElasticLoadBalancingv2.Client.exceptions.InvalidConfigurationRequestException
ElasticLoadBalancingv2.Client.exceptions.InvalidSecurityGroupException

Examples
This example associates the specified security group with the specified load balancer.
response = client.set_security_groups(
    LoadBalancerArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
    SecurityGroups=[
        'sg-5943793c',
    ],
)

print(response)


Expected Output:
{
    'SecurityGroupIds': [
        'sg-5943793c',
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'SecurityGroupIds': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def set_subnets(LoadBalancerArn=None, Subnets=None, SubnetMappings=None):
    """
    Enables the Availability Zones for the specified public subnets for the specified load balancer. The specified subnets replace the previously enabled subnets.
    When you specify subnets for a Network Load Balancer, you must include all subnets that were enabled previously, with their existing configurations, plus any additional subnets.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example enables the Availability Zones for the specified subnets for the specified load balancer.
    Expected Output:
    
    :example: response = client.set_subnets(
        LoadBalancerArn='string',
        Subnets=[
            'string',
        ],
        SubnetMappings=[
            {
                'SubnetId': 'string',
                'AllocationId': 'string',
                'PrivateIPv4Address': 'string'
            },
        ]
    )
    
    
    :type LoadBalancerArn: string
    :param LoadBalancerArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the load balancer.\n

    :type Subnets: list
    :param Subnets: The IDs of the public subnets. You must specify subnets from at least two Availability Zones. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings.\n\n(string) --\n\n

    :type SubnetMappings: list
    :param SubnetMappings: The IDs of the public subnets. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings.\n[Application Load Balancers] You must specify subnets from at least two Availability Zones. You cannot specify Elastic IP addresses for your subnets.\n[Network Load Balancers] You can specify subnets from one or more Availability Zones. If you need static IP addresses for your internet-facing load balancer, you can specify one Elastic IP address per subnet. For internal load balancers, you can specify one private IP address per subnet from the IPv4 range of the subnet.\n\n(dict) --Information about a subnet mapping.\n\nSubnetId (string) --The ID of the subnet.\n\nAllocationId (string) --[Network Load Balancers] The allocation ID of the Elastic IP address for an internet-facing load balancer.\n\nPrivateIPv4Address (string) --[Network Load Balancers] The private IPv4 address for an internal load balancer.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AvailabilityZones': [
        {
            'ZoneName': 'string',
            'SubnetId': 'string',
            'LoadBalancerAddresses': [
                {
                    'IpAddress': 'string',
                    'AllocationId': 'string',
                    'PrivateIPv4Address': 'string'
                },
            ]
        },
    ]
}


Response Structure

(dict) --

AvailabilityZones (list) --
Information about the subnet and Availability Zone.

(dict) --
Information about an Availability Zone.

ZoneName (string) --
The name of the Availability Zone.

SubnetId (string) --
The ID of the subnet. You can specify one subnet per Availability Zone.

LoadBalancerAddresses (list) --
[Network Load Balancers] If you need static IP addresses for your load balancer, you can specify one Elastic IP address per Availability Zone when you create an internal-facing load balancer. For internal load balancers, you can specify a private IP address from the IPv4 range of the subnet.

(dict) --
Information about a static IP address for a load balancer.

IpAddress (string) --
The static IP address.

AllocationId (string) --
[Network Load Balancers] The allocation ID of the Elastic IP address for an internal-facing load balancer.

PrivateIPv4Address (string) --
[Network Load Balancers] The private IPv4 address for an internal load balancer.















Exceptions

ElasticLoadBalancingv2.Client.exceptions.LoadBalancerNotFoundException
ElasticLoadBalancingv2.Client.exceptions.InvalidConfigurationRequestException
ElasticLoadBalancingv2.Client.exceptions.SubnetNotFoundException
ElasticLoadBalancingv2.Client.exceptions.InvalidSubnetException
ElasticLoadBalancingv2.Client.exceptions.AllocationIdNotFoundException
ElasticLoadBalancingv2.Client.exceptions.AvailabilityZoneNotSupportedException

Examples
This example enables the Availability Zones for the specified subnets for the specified load balancer.
response = client.set_subnets(
    LoadBalancerArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
    Subnets=[
        'subnet-8360a9e7',
        'subnet-b7d581c0',
    ],
)

print(response)


Expected Output:
{
    'AvailabilityZones': [
        {
            'SubnetId': 'subnet-8360a9e7',
            'ZoneName': 'us-west-2a',
        },
        {
            'SubnetId': 'subnet-b7d581c0',
            'ZoneName': 'us-west-2b',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'AvailabilityZones': [
            {
                'ZoneName': 'string',
                'SubnetId': 'string',
                'LoadBalancerAddresses': [
                    {
                        'IpAddress': 'string',
                        'AllocationId': 'string',
                        'PrivateIPv4Address': 'string'
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    ElasticLoadBalancingv2.Client.exceptions.LoadBalancerNotFoundException
    ElasticLoadBalancingv2.Client.exceptions.InvalidConfigurationRequestException
    ElasticLoadBalancingv2.Client.exceptions.SubnetNotFoundException
    ElasticLoadBalancingv2.Client.exceptions.InvalidSubnetException
    ElasticLoadBalancingv2.Client.exceptions.AllocationIdNotFoundException
    ElasticLoadBalancingv2.Client.exceptions.AvailabilityZoneNotSupportedException
    
    """
    pass

