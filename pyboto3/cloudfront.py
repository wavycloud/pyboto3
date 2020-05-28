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
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_cloud_front_origin_access_identity(CloudFrontOriginAccessIdentityConfig=None):
    """
    Creates a new origin access identity. If you\'re using Amazon S3 for your origin, you can use an origin access identity to require users to access your content using a CloudFront URL instead of the Amazon S3 URL. For more information about how to use origin access identities, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_cloud_front_origin_access_identity(
        CloudFrontOriginAccessIdentityConfig={
            'CallerReference': 'string',
            'Comment': 'string'
        }
    )
    
    
    :type CloudFrontOriginAccessIdentityConfig: dict
    :param CloudFrontOriginAccessIdentityConfig: [REQUIRED]\nThe current configuration information for the identity.\n\nCallerReference (string) -- [REQUIRED]A unique value (for example, a date-time stamp) that ensures that the request can\'t be replayed.\nIf the value of CallerReference is new (regardless of the content of the CloudFrontOriginAccessIdentityConfig object), a new origin access identity is created.\nIf the CallerReference is a value already sent in a previous identity request, and the content of the CloudFrontOriginAccessIdentityConfig is identical to the original request (ignoring white space), the response includes the same information returned to the original request.\nIf the CallerReference is a value you already sent in a previous request to create an identity, but the content of the CloudFrontOriginAccessIdentityConfig is different from the original request, CloudFront returns a CloudFrontOriginAccessIdentityAlreadyExists error.\n\nComment (string) -- [REQUIRED]Any comments you want to include about the origin access identity.\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'CloudFrontOriginAccessIdentity': {
        'Id': 'string',
        'S3CanonicalUserId': 'string',
        'CloudFrontOriginAccessIdentityConfig': {
            'CallerReference': 'string',
            'Comment': 'string'
        }
    },
    'Location': 'string',
    'ETag': 'string'
}


Response Structure

(dict) --The returned result of the corresponding request.

CloudFrontOriginAccessIdentity (dict) --The origin access identity\'s information.

Id (string) --The ID for the origin access identity, for example, E74FTE3AJFJ256A .

S3CanonicalUserId (string) --The Amazon S3 canonical user ID for the origin access identity, used when giving the origin access identity read permission to an object in Amazon S3.

CloudFrontOriginAccessIdentityConfig (dict) --The current configuration information for the identity.

CallerReference (string) --A unique value (for example, a date-time stamp) that ensures that the request can\'t be replayed.
If the value of CallerReference is new (regardless of the content of the CloudFrontOriginAccessIdentityConfig object), a new origin access identity is created.
If the CallerReference is a value already sent in a previous identity request, and the content of the CloudFrontOriginAccessIdentityConfig is identical to the original request (ignoring white space), the response includes the same information returned to the original request.
If the CallerReference is a value you already sent in a previous request to create an identity, but the content of the CloudFrontOriginAccessIdentityConfig is different from the original request, CloudFront returns a CloudFrontOriginAccessIdentityAlreadyExists error.

Comment (string) --Any comments you want to include about the origin access identity.





Location (string) --The fully qualified URI of the new origin access identity just created. For example: https://cloudfront.amazonaws.com/2010-11-01/origin-access-identity/cloudfront/E74FTE3AJFJ256A .

ETag (string) --The current version of the origin access identity created.






Exceptions

CloudFront.Client.exceptions.CloudFrontOriginAccessIdentityAlreadyExists
CloudFront.Client.exceptions.MissingBody
CloudFront.Client.exceptions.TooManyCloudFrontOriginAccessIdentities
CloudFront.Client.exceptions.InvalidArgument
CloudFront.Client.exceptions.InconsistentQuantities


    :return: {
        'CloudFrontOriginAccessIdentity': {
            'Id': 'string',
            'S3CanonicalUserId': 'string',
            'CloudFrontOriginAccessIdentityConfig': {
                'CallerReference': 'string',
                'Comment': 'string'
            }
        },
        'Location': 'string',
        'ETag': 'string'
    }
    
    
    """
    pass

def create_distribution(DistributionConfig=None):
    """
    Creates a new web distribution. You create a CloudFront distribution to tell CloudFront where you want content to be delivered from, and the details about how to track and manage content delivery. Send a POST request to the /*CloudFront API version* /distribution /distribution ID resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_distribution(
        DistributionConfig={
            'CallerReference': 'string',
            'Aliases': {
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'DefaultRootObject': 'string',
            'Origins': {
                'Quantity': 123,
                'Items': [
                    {
                        'Id': 'string',
                        'DomainName': 'string',
                        'OriginPath': 'string',
                        'CustomHeaders': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'HeaderName': 'string',
                                    'HeaderValue': 'string'
                                },
                            ]
                        },
                        'S3OriginConfig': {
                            'OriginAccessIdentity': 'string'
                        },
                        'CustomOriginConfig': {
                            'HTTPPort': 123,
                            'HTTPSPort': 123,
                            'OriginProtocolPolicy': 'http-only'|'match-viewer'|'https-only',
                            'OriginSslProtocols': {
                                'Quantity': 123,
                                'Items': [
                                    'SSLv3'|'TLSv1'|'TLSv1.1'|'TLSv1.2',
                                ]
                            },
                            'OriginReadTimeout': 123,
                            'OriginKeepaliveTimeout': 123
                        }
                    },
                ]
            },
            'OriginGroups': {
                'Quantity': 123,
                'Items': [
                    {
                        'Id': 'string',
                        'FailoverCriteria': {
                            'StatusCodes': {
                                'Quantity': 123,
                                'Items': [
                                    123,
                                ]
                            }
                        },
                        'Members': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'OriginId': 'string'
                                },
                            ]
                        }
                    },
                ]
            },
            'DefaultCacheBehavior': {
                'TargetOriginId': 'string',
                'ForwardedValues': {
                    'QueryString': True|False,
                    'Cookies': {
                        'Forward': 'none'|'whitelist'|'all',
                        'WhitelistedNames': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                    'Headers': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    },
                    'QueryStringCacheKeys': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    }
                },
                'TrustedSigners': {
                    'Enabled': True|False,
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                'MinTTL': 123,
                'AllowedMethods': {
                    'Quantity': 123,
                    'Items': [
                        'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                    ],
                    'CachedMethods': {
                        'Quantity': 123,
                        'Items': [
                            'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                        ]
                    }
                },
                'SmoothStreaming': True|False,
                'DefaultTTL': 123,
                'MaxTTL': 123,
                'Compress': True|False,
                'LambdaFunctionAssociations': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'LambdaFunctionARN': 'string',
                            'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                            'IncludeBody': True|False
                        },
                    ]
                },
                'FieldLevelEncryptionId': 'string'
            },
            'CacheBehaviors': {
                'Quantity': 123,
                'Items': [
                    {
                        'PathPattern': 'string',
                        'TargetOriginId': 'string',
                        'ForwardedValues': {
                            'QueryString': True|False,
                            'Cookies': {
                                'Forward': 'none'|'whitelist'|'all',
                                'WhitelistedNames': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                }
                            },
                            'Headers': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            },
                            'QueryStringCacheKeys': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                        'TrustedSigners': {
                            'Enabled': True|False,
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        },
                        'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                        'MinTTL': 123,
                        'AllowedMethods': {
                            'Quantity': 123,
                            'Items': [
                                'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                            ],
                            'CachedMethods': {
                                'Quantity': 123,
                                'Items': [
                                    'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                ]
                            }
                        },
                        'SmoothStreaming': True|False,
                        'DefaultTTL': 123,
                        'MaxTTL': 123,
                        'Compress': True|False,
                        'LambdaFunctionAssociations': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'LambdaFunctionARN': 'string',
                                    'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                    'IncludeBody': True|False
                                },
                            ]
                        },
                        'FieldLevelEncryptionId': 'string'
                    },
                ]
            },
            'CustomErrorResponses': {
                'Quantity': 123,
                'Items': [
                    {
                        'ErrorCode': 123,
                        'ResponsePagePath': 'string',
                        'ResponseCode': 'string',
                        'ErrorCachingMinTTL': 123
                    },
                ]
            },
            'Comment': 'string',
            'Logging': {
                'Enabled': True|False,
                'IncludeCookies': True|False,
                'Bucket': 'string',
                'Prefix': 'string'
            },
            'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
            'Enabled': True|False,
            'ViewerCertificate': {
                'CloudFrontDefaultCertificate': True|False,
                'IAMCertificateId': 'string',
                'ACMCertificateArn': 'string',
                'SSLSupportMethod': 'sni-only'|'vip',
                'MinimumProtocolVersion': 'SSLv3'|'TLSv1'|'TLSv1_2016'|'TLSv1.1_2016'|'TLSv1.2_2018',
                'Certificate': 'string',
                'CertificateSource': 'cloudfront'|'iam'|'acm'
            },
            'Restrictions': {
                'GeoRestriction': {
                    'RestrictionType': 'blacklist'|'whitelist'|'none',
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                }
            },
            'WebACLId': 'string',
            'HttpVersion': 'http1.1'|'http2',
            'IsIPV6Enabled': True|False
        }
    )
    
    
    :type DistributionConfig: dict
    :param DistributionConfig: [REQUIRED]\nThe distribution\'s configuration information.\n\nCallerReference (string) -- [REQUIRED]A unique value (for example, a date-time stamp) that ensures that the request can\'t be replayed.\nIf the value of CallerReference is new (regardless of the content of the DistributionConfig object), CloudFront creates a new distribution.\nIf CallerReference is a value that you already sent in a previous request to create a distribution, CloudFront returns a DistributionAlreadyExists error.\n\nAliases (dict) --A complex type that contains information about CNAMEs (alternate domain names), if any, for this distribution.\n\nQuantity (integer) -- [REQUIRED]The number of CNAME aliases, if any, that you want to associate with this distribution.\n\nItems (list) --A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.\n\n(string) --\n\n\n\n\nDefaultRootObject (string) --The object that you want CloudFront to request from your origin (for example, index.html ) when a viewer requests the root URL for your distribution (http://www.example.com ) instead of an object in your distribution (http://www.example.com/product-description.html ). Specifying a default root object avoids exposing the contents of your distribution.\nSpecify only the object name, for example, index.html . Don\'t add a / before the object name.\nIf you don\'t want to specify a default root object when you create a distribution, include an empty DefaultRootObject element.\nTo delete the default root object from an existing distribution, update the distribution configuration and include an empty DefaultRootObject element.\nTo replace the default root object, update the distribution configuration and specify the new object.\nFor more information about the default root object, see Creating a Default Root Object in the Amazon CloudFront Developer Guide .\n\nOrigins (dict) -- [REQUIRED]A complex type that contains information about origins for this distribution.\n\nQuantity (integer) -- [REQUIRED]The number of origins or origin groups for this distribution.\n\nItems (list) -- [REQUIRED]A complex type that contains origins or origin groups for this distribution.\n\n(dict) --A complex type that describes the Amazon S3 bucket, HTTP server (for example, a web server), Amazon MediaStore, or other server from which CloudFront gets your files. This can also be an origin group, if you\'ve created an origin group. You must specify at least one origin or origin group.\nFor the current limit on the number of origins or origin groups that you can specify for a distribution, see Amazon CloudFront Limits in the AWS General Reference .\n\nId (string) -- [REQUIRED]A unique identifier for the origin or origin group. The value of Id must be unique within the distribution.\nWhen you specify the value of TargetOriginId for the default cache behavior or for another cache behavior, you indicate the origin to which you want the cache behavior to route requests by specifying the value of the Id element for that origin. When a request matches the path pattern for that cache behavior, CloudFront routes the request to the specified origin. For more information, see Cache Behavior Settings in the Amazon CloudFront Developer Guide .\n\nDomainName (string) -- [REQUIRED]\nAmazon S3 origins : The DNS name of the Amazon S3 bucket from which you want CloudFront to get objects for this origin, for example, myawsbucket.s3.amazonaws.com . If you set up your bucket to be configured as a website endpoint, enter the Amazon S3 static website hosting endpoint for the bucket.\nFor more information about specifying this value for different types of origins, see Origin Domain Name in the Amazon CloudFront Developer Guide .\nConstraints for Amazon S3 origins:\n\nIf you configured Amazon S3 Transfer Acceleration for your bucket, don\'t specify the s3-accelerate endpoint for DomainName .\nThe bucket name must be between 3 and 63 characters long (inclusive).\nThe bucket name must contain only lowercase characters, numbers, periods, underscores, and dashes.\nThe bucket name must not contain adjacent periods.\n\n\nCustom Origins : The DNS domain name for the HTTP server from which you want CloudFront to get objects for this origin, for example, www.example.com .\nConstraints for custom origins:\n\nDomainName must be a valid DNS name that contains only a-z, A-Z, 0-9, dot (.), hyphen (-), or underscore (_) characters.\nThe name cannot exceed 128 characters.\n\n\nOriginPath (string) --An optional element that causes CloudFront to request your content from a directory in your Amazon S3 bucket or your custom origin. When you include the OriginPath element, specify the directory name, beginning with a / . CloudFront appends the directory name to the value of DomainName , for example, example.com/production . Do not include a / at the end of the directory name.\nFor example, suppose you\'ve specified the following values for your distribution:\n\nDomainName : An Amazon S3 bucket named myawsbucket .\nOriginPath : /production\nCNAME : example.com\n\nWhen a user enters example.com/index.html in a browser, CloudFront sends a request to Amazon S3 for myawsbucket/production/index.html .\nWhen a user enters example.com/acme/index.html in a browser, CloudFront sends a request to Amazon S3 for myawsbucket/production/acme/index.html .\n\nCustomHeaders (dict) --A complex type that contains names and values for the custom headers that you want.\n\nQuantity (integer) -- [REQUIRED]The number of custom headers, if any, for this distribution.\n\nItems (list) --\nOptional : A list that contains one OriginCustomHeader element for each custom header that you want CloudFront to forward to the origin. If Quantity is 0 , omit Items .\n\n(dict) --A complex type that contains HeaderName and HeaderValue elements, if any, for this distribution.\n\nHeaderName (string) -- [REQUIRED]The name of a header that you want CloudFront to forward to your origin. For more information, see Forwarding Custom Headers to Your Origin (Web Distributions Only) in the Amazon CloudFront Developer Guide .\n\nHeaderValue (string) -- [REQUIRED]The value for the header that you specified in the HeaderName field.\n\n\n\n\n\n\n\nS3OriginConfig (dict) --A complex type that contains information about the Amazon S3 origin. If the origin is a custom origin, use the CustomOriginConfig element instead.\n\nOriginAccessIdentity (string) -- [REQUIRED]The CloudFront origin access identity to associate with the origin. Use an origin access identity to configure the origin so that viewers can only access objects in an Amazon S3 bucket through CloudFront. The format of the value is:\norigin-access-identity/cloudfront/ID-of-origin-access-identity\nwhere `` ID-of-origin-access-identity `` is the value that CloudFront returned in the ID element when you created the origin access identity.\nIf you want viewers to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty OriginAccessIdentity element.\nTo delete the origin access identity from an existing distribution, update the distribution configuration and include an empty OriginAccessIdentity element.\nTo replace the origin access identity, update the distribution configuration and specify the new origin access identity.\nFor more information about the origin access identity, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .\n\n\n\nCustomOriginConfig (dict) --A complex type that contains information about a custom origin. If the origin is an Amazon S3 bucket, use the S3OriginConfig element instead.\n\nHTTPPort (integer) -- [REQUIRED]The HTTP port the custom origin listens on.\n\nHTTPSPort (integer) -- [REQUIRED]The HTTPS port the custom origin listens on.\n\nOriginProtocolPolicy (string) -- [REQUIRED]The origin protocol policy to apply to your origin.\n\nOriginSslProtocols (dict) --The SSL/TLS protocols that you want CloudFront to use when communicating with your origin over HTTPS.\n\nQuantity (integer) -- [REQUIRED]The number of SSL/TLS protocols that you want to allow CloudFront to use when establishing an HTTPS connection with this origin.\n\nItems (list) -- [REQUIRED]A list that contains allowed SSL/TLS protocols for this distribution.\n\n(string) --\n\n\n\n\nOriginReadTimeout (integer) --You can create a custom origin read timeout. All timeout units are in seconds. The default origin read timeout is 30 seconds, but you can configure custom timeout lengths using the CloudFront API. The minimum timeout length is 4 seconds; the maximum is 60 seconds.\nIf you need to increase the maximum time limit, contact the AWS Support Center .\n\nOriginKeepaliveTimeout (integer) --You can create a custom keep-alive timeout. All timeout units are in seconds. The default keep-alive timeout is 5 seconds, but you can configure custom timeout lengths using the CloudFront API. The minimum timeout length is 1 second; the maximum is 60 seconds.\nIf you need to increase the maximum time limit, contact the AWS Support Center .\n\n\n\n\n\n\n\n\n\nOriginGroups (dict) --A complex type that contains information about origin groups for this distribution.\n\nQuantity (integer) -- [REQUIRED]The number of origin groups.\n\nItems (list) --The items (origin groups) in a distribution.\n\n(dict) --An origin group includes two origins (a primary origin and a second origin to failover to) and a failover criteria that you specify. You create an origin group to support origin failover in CloudFront. When you create or update a distribution, you can specifiy the origin group instead of a single origin, and CloudFront will failover from the primary origin to the second origin under the failover conditions that you\'ve chosen.\n\nId (string) -- [REQUIRED]The origin group\'s ID.\n\nFailoverCriteria (dict) -- [REQUIRED]A complex type that contains information about the failover criteria for an origin group.\n\nStatusCodes (dict) -- [REQUIRED]The status codes that, when returned from the primary origin, will trigger CloudFront to failover to the second origin.\n\nQuantity (integer) -- [REQUIRED]The number of status codes.\n\nItems (list) -- [REQUIRED]The items (status codes) for an origin group.\n\n(integer) --\n\n\n\n\n\n\nMembers (dict) -- [REQUIRED]A complex type that contains information about the origins in an origin group.\n\nQuantity (integer) -- [REQUIRED]The number of origins in an origin group.\n\nItems (list) -- [REQUIRED]Items (origins) in an origin group.\n\n(dict) --An origin in an origin group.\n\nOriginId (string) -- [REQUIRED]The ID for an origin in an origin group.\n\n\n\n\n\n\n\n\n\n\n\n\n\nDefaultCacheBehavior (dict) -- [REQUIRED]A complex type that describes the default cache behavior if you don\'t specify a CacheBehavior element or if files don\'t match any of the values of PathPattern in CacheBehavior elements. You must create exactly one default cache behavior.\n\nTargetOriginId (string) -- [REQUIRED]The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior in your distribution.\n\nForwardedValues (dict) -- [REQUIRED]A complex type that specifies how CloudFront handles query strings, cookies, and HTTP headers.\n\nQueryString (boolean) -- [REQUIRED]Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior and cache based on the query string parameters. CloudFront behavior depends on the value of QueryString and on the values that you specify for QueryStringCacheKeys , if any:\nIf you specify true for QueryString and you don\'t specify any values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin and caches based on all query string parameters. Depending on how many query string parameters and values you have, this can adversely affect performance because CloudFront must forward more requests to the origin.\nIf you specify true for QueryString and you specify one or more values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin, but it only caches based on the query string parameters that you specify.\nIf you specify false for QueryString , CloudFront doesn\'t forward any query string parameters to the origin, and doesn\'t cache based on query string parameters.\nFor more information, see Configuring CloudFront to Cache Based on Query String Parameters in the Amazon CloudFront Developer Guide .\n\nCookies (dict) -- [REQUIRED]A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see How CloudFront Forwards, Caches, and Logs Cookies in the Amazon CloudFront Developer Guide .\n\nForward (string) -- [REQUIRED]Specifies which cookies to forward to the origin for this cache behavior: all, none, or the list of cookies specified in the WhitelistedNames complex type.\nAmazon S3 doesn\'t process cookies. When the cache behavior is forwarding requests to an Amazon S3 origin, specify none for the Forward element.\n\nWhitelistedNames (dict) --Required if you specify whitelist for the value of Forward . A complex type that specifies how many different cookies you want CloudFront to forward to the origin for this cache behavior and, if you want to forward selected cookies, the names of those cookies.\nIf you specify all or none for the value of Forward , omit WhitelistedNames . If you change the value of Forward from whitelist to all or none and you don\'t delete the WhitelistedNames element and its child elements, CloudFront deletes them automatically.\nFor the current limit on the number of cookie names that you can whitelist for each cache behavior, see CloudFront Limits in the AWS General Reference .\n\nQuantity (integer) -- [REQUIRED]The number of different cookies that you want CloudFront to forward to the origin for this cache behavior. The value must equal the number of items that are in the Items field.\nWhen you set Forward = whitelist (in the CookiePreferences object), this value must be 1 or higher.\n\nItems (list) --A complex type that contains one Name element for each cookie that you want CloudFront to forward to the origin for this cache behavior. It must contain the same number of items that is specified in the Quantity field.\nWhen you set Forward = whitelist (in the CookiePreferences object), this field must contain at least one item.\n\n(string) --\n\n\n\n\n\n\nHeaders (dict) --A complex type that specifies the Headers , if any, that you want CloudFront to forward to the origin for this cache behavior (whitelisted headers). For the headers that you specify, CloudFront also caches separate versions of a specified object that is based on the header values in viewer requests.\nFor more information, see Caching Content Based on Request Headers in the Amazon CloudFront Developer Guide .\n\nQuantity (integer) -- [REQUIRED]The number of different headers that you want CloudFront to base caching on for this cache behavior. You can configure each cache behavior in a web distribution to do one of the following:\n\nForward all headers to your origin : Specify 1 for Quantity and * for Name .\n\n\nWarning\nCloudFront doesn\'t cache the objects that are associated with this cache behavior. Instead, CloudFront sends every request to the origin.\n\n\nForward a whitelist of headers you specify : Specify the number of headers that you want CloudFront to base caching on. Then specify the header names in Name elements. CloudFront caches your objects based on the values in the specified headers.\nForward only the default headers : Specify 0 for Quantity and omit Items . In this configuration, CloudFront doesn\'t cache based on the values in the request headers.\n\nRegardless of which option you choose, CloudFront forwards headers to your origin based on whether the origin is an S3 bucket or a custom origin. See the following documentation:\n\nS3 bucket : See HTTP Request Headers That CloudFront Removes or Updates\nCustom origin : See HTTP Request Headers and CloudFront Behavior\n\n\nItems (list) --A list that contains one Name element for each header that you want CloudFront to use for caching in this cache behavior. If Quantity is 0 , omit Items .\n\n(string) --\n\n\n\n\nQueryStringCacheKeys (dict) --A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.\n\nQuantity (integer) -- [REQUIRED]The number of whitelisted query string parameters for a cache behavior.\n\nItems (list) --A list that contains the query string parameters that you want CloudFront to use as a basis for caching for a cache behavior. If Quantity is 0, you can omit Items .\n\n(string) --\n\n\n\n\n\n\nTrustedSigners (dict) -- [REQUIRED]A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content.\nIf you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled , and specify the applicable values for Quantity and Items . For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .\nIf you don\'t want to require signed URLs in requests for objects that match PathPattern , specify false for Enabled and 0 for Quantity . Omit Items .\nTo add, change, or remove one or more trusted signers, change Enabled to true (if it\'s currently false ), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.\n\nEnabled (boolean) -- [REQUIRED]Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .\n\nQuantity (integer) -- [REQUIRED]The number of trusted signers for this cache behavior.\n\nItems (list) --\nOptional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .\n\n(string) --\n\n\n\n\nViewerProtocolPolicy (string) -- [REQUIRED]The protocol that viewers can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern . You can specify the following options:\n\nallow-all : Viewers can use HTTP or HTTPS.\nredirect-to-https : If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.\nhttps-only : If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).\n\nFor more information about requiring the HTTPS protocol, see Using an HTTPS Connection to Access Your Objects in the Amazon CloudFront Developer Guide .\n\nNote\nThe only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects\' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .\n\n\nMinTTL (integer) -- [REQUIRED]The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .\nYou must specify 0 for MinTTL if you configure CloudFront to forward all headers to your origin (under Headers , if you specify 1 for Quantity and * for Name ).\n\nAllowedMethods (dict) --A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices:\n\nCloudFront forwards only GET and HEAD requests.\nCloudFront forwards only GET , HEAD , and OPTIONS requests.\nCloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests.\n\nIf you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can\'t perform operations that you don\'t want them to. For example, you might not want users to have permissions to delete objects from your origin.\n\nQuantity (integer) -- [REQUIRED]The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET , HEAD , and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests).\n\nItems (list) -- [REQUIRED]A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.\n\n(string) --\n\n\nCachedMethods (dict) --A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices:\n\nCloudFront caches responses to GET and HEAD requests.\nCloudFront caches responses to GET , HEAD , and OPTIONS requests.\n\nIf you pick the second choice for your Amazon S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers, and Origin headers for the responses to be cached correctly.\n\nQuantity (integer) -- [REQUIRED]The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET , HEAD , and OPTIONS requests).\n\nItems (list) -- [REQUIRED]A complex type that contains the HTTP methods that you want CloudFront to cache responses to.\n\n(string) --\n\n\n\n\n\n\nSmoothStreaming (boolean) --Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true ; if not, specify false . If you specify true for SmoothStreaming , you can still distribute other content using this cache behavior if the content matches the value of PathPattern .\n\nDefaultTTL (integer) --The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .\n\nMaxTTL (integer) --The maximum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .\n\nCompress (boolean) --Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify true ; if not, specify false . For more information, see Serving Compressed Files in the Amazon CloudFront Developer Guide .\n\nLambdaFunctionAssociations (dict) --A complex type that contains zero or more Lambda function associations for a cache behavior.\n\nQuantity (integer) -- [REQUIRED]The number of Lambda function associations for this cache behavior.\n\nItems (list) --\nOptional : A complex type that contains LambdaFunctionAssociation items for this cache behavior. If Quantity is 0 , you can omit Items .\n\n(dict) --A complex type that contains a Lambda function association.\n\nLambdaFunctionARN (string) -- [REQUIRED]The ARN of the Lambda function. You must specify the ARN of a function version; you can\'t specify a Lambda alias or $LATEST.\n\nEventType (string) -- [REQUIRED]Specifies the event type that triggers a Lambda function invocation. You can specify the following values:\n\nviewer-request : The function executes when CloudFront receives a request from a viewer and before it checks to see whether the requested object is in the edge cache.\norigin-request : The function executes only when CloudFront forwards a request to your origin. When the requested object is in the edge cache, the function doesn\'t execute.\norigin-response : The function executes after CloudFront receives a response from the origin and before it caches the object in the response. When the requested object is in the edge cache, the function doesn\'t execute.\nviewer-response : The function executes before CloudFront returns the requested object to the viewer. The function executes regardless of whether the object was already in the edge cache. If the origin returns an HTTP status code other than HTTP 200 (OK), the function doesn\'t execute.\n\n\nIncludeBody (boolean) --A flag that allows a Lambda function to have read access to the body content. For more information, see Accessing the Request Body by Choosing the Include Body Option in the Amazon CloudFront Developer Guide.\n\n\n\n\n\n\n\nFieldLevelEncryptionId (string) --The value of ID for the field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data for a cache behavior or for the default cache behavior in your distribution.\n\n\n\nCacheBehaviors (dict) --A complex type that contains zero or more CacheBehavior elements.\n\nQuantity (integer) -- [REQUIRED]The number of cache behaviors for this distribution.\n\nItems (list) --Optional: A complex type that contains cache behaviors for this distribution. If Quantity is 0 , you can omit Items .\n\n(dict) --A complex type that describes how CloudFront processes requests.\nYou must create at least as many cache behaviors (including the default cache behavior) as you have origins if you want CloudFront to distribute objects from all of the origins. Each cache behavior specifies the one origin from which you want CloudFront to get objects. If you have two origins and only the default cache behavior, the default cache behavior will cause CloudFront to get objects from one of the origins, but the other origin is never used.\nFor the current limit on the number of cache behaviors that you can add to a distribution, see Amazon CloudFront Limits in the AWS General Reference .\nIf you don\'t want to specify any cache behaviors, include only an empty CacheBehaviors element. Don\'t include an empty CacheBehavior element, or CloudFront returns a MalformedXML error.\nTo delete all cache behaviors in an existing distribution, update the distribution configuration and include only an empty CacheBehaviors element.\nTo add, change, or remove one or more cache behaviors, update the distribution configuration and specify all of the cache behaviors that you want to include in the updated distribution.\nFor more information about cache behaviors, see Cache Behaviors in the Amazon CloudFront Developer Guide .\n\nPathPattern (string) -- [REQUIRED]The pattern (for example, images/*.jpg ) that specifies which requests to apply the behavior to. When CloudFront receives a viewer request, the requested path is compared with path patterns in the order in which cache behaviors are listed in the distribution.\n\nNote\nYou can optionally include a slash (/ ) at the beginning of the path pattern. For example, /images/*.jpg . CloudFront behavior is the same with or without the leading / .\n\nThe path pattern for the default cache behavior is * and cannot be changed. If the request for an object does not match the path pattern for any cache behaviors, CloudFront applies the behavior in the default cache behavior.\nFor more information, see Path Pattern in the Amazon CloudFront Developer Guide .\n\nTargetOriginId (string) -- [REQUIRED]The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior in your distribution.\n\nForwardedValues (dict) -- [REQUIRED]A complex type that specifies how CloudFront handles query strings, cookies, and HTTP headers.\n\nQueryString (boolean) -- [REQUIRED]Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior and cache based on the query string parameters. CloudFront behavior depends on the value of QueryString and on the values that you specify for QueryStringCacheKeys , if any:\nIf you specify true for QueryString and you don\'t specify any values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin and caches based on all query string parameters. Depending on how many query string parameters and values you have, this can adversely affect performance because CloudFront must forward more requests to the origin.\nIf you specify true for QueryString and you specify one or more values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin, but it only caches based on the query string parameters that you specify.\nIf you specify false for QueryString , CloudFront doesn\'t forward any query string parameters to the origin, and doesn\'t cache based on query string parameters.\nFor more information, see Configuring CloudFront to Cache Based on Query String Parameters in the Amazon CloudFront Developer Guide .\n\nCookies (dict) -- [REQUIRED]A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see How CloudFront Forwards, Caches, and Logs Cookies in the Amazon CloudFront Developer Guide .\n\nForward (string) -- [REQUIRED]Specifies which cookies to forward to the origin for this cache behavior: all, none, or the list of cookies specified in the WhitelistedNames complex type.\nAmazon S3 doesn\'t process cookies. When the cache behavior is forwarding requests to an Amazon S3 origin, specify none for the Forward element.\n\nWhitelistedNames (dict) --Required if you specify whitelist for the value of Forward . A complex type that specifies how many different cookies you want CloudFront to forward to the origin for this cache behavior and, if you want to forward selected cookies, the names of those cookies.\nIf you specify all or none for the value of Forward , omit WhitelistedNames . If you change the value of Forward from whitelist to all or none and you don\'t delete the WhitelistedNames element and its child elements, CloudFront deletes them automatically.\nFor the current limit on the number of cookie names that you can whitelist for each cache behavior, see CloudFront Limits in the AWS General Reference .\n\nQuantity (integer) -- [REQUIRED]The number of different cookies that you want CloudFront to forward to the origin for this cache behavior. The value must equal the number of items that are in the Items field.\nWhen you set Forward = whitelist (in the CookiePreferences object), this value must be 1 or higher.\n\nItems (list) --A complex type that contains one Name element for each cookie that you want CloudFront to forward to the origin for this cache behavior. It must contain the same number of items that is specified in the Quantity field.\nWhen you set Forward = whitelist (in the CookiePreferences object), this field must contain at least one item.\n\n(string) --\n\n\n\n\n\n\nHeaders (dict) --A complex type that specifies the Headers , if any, that you want CloudFront to forward to the origin for this cache behavior (whitelisted headers). For the headers that you specify, CloudFront also caches separate versions of a specified object that is based on the header values in viewer requests.\nFor more information, see Caching Content Based on Request Headers in the Amazon CloudFront Developer Guide .\n\nQuantity (integer) -- [REQUIRED]The number of different headers that you want CloudFront to base caching on for this cache behavior. You can configure each cache behavior in a web distribution to do one of the following:\n\nForward all headers to your origin : Specify 1 for Quantity and * for Name .\n\n\nWarning\nCloudFront doesn\'t cache the objects that are associated with this cache behavior. Instead, CloudFront sends every request to the origin.\n\n\nForward a whitelist of headers you specify : Specify the number of headers that you want CloudFront to base caching on. Then specify the header names in Name elements. CloudFront caches your objects based on the values in the specified headers.\nForward only the default headers : Specify 0 for Quantity and omit Items . In this configuration, CloudFront doesn\'t cache based on the values in the request headers.\n\nRegardless of which option you choose, CloudFront forwards headers to your origin based on whether the origin is an S3 bucket or a custom origin. See the following documentation:\n\nS3 bucket : See HTTP Request Headers That CloudFront Removes or Updates\nCustom origin : See HTTP Request Headers and CloudFront Behavior\n\n\nItems (list) --A list that contains one Name element for each header that you want CloudFront to use for caching in this cache behavior. If Quantity is 0 , omit Items .\n\n(string) --\n\n\n\n\nQueryStringCacheKeys (dict) --A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.\n\nQuantity (integer) -- [REQUIRED]The number of whitelisted query string parameters for a cache behavior.\n\nItems (list) --A list that contains the query string parameters that you want CloudFront to use as a basis for caching for a cache behavior. If Quantity is 0, you can omit Items .\n\n(string) --\n\n\n\n\n\n\nTrustedSigners (dict) -- [REQUIRED]A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content.\nIf you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled , and specify the applicable values for Quantity and Items . For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .\nIf you don\'t want to require signed URLs in requests for objects that match PathPattern , specify false for Enabled and 0 for Quantity . Omit Items .\nTo add, change, or remove one or more trusted signers, change Enabled to true (if it\'s currently false ), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.\n\nEnabled (boolean) -- [REQUIRED]Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .\n\nQuantity (integer) -- [REQUIRED]The number of trusted signers for this cache behavior.\n\nItems (list) --\nOptional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .\n\n(string) --\n\n\n\n\nViewerProtocolPolicy (string) -- [REQUIRED]The protocol that viewers can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern . You can specify the following options:\n\nallow-all : Viewers can use HTTP or HTTPS.\nredirect-to-https : If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.\nhttps-only : If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).\n\nFor more information about requiring the HTTPS protocol, see Using an HTTPS Connection to Access Your Objects in the Amazon CloudFront Developer Guide .\n\nNote\nThe only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects\' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .\n\n\nMinTTL (integer) -- [REQUIRED]The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .\nYou must specify 0 for MinTTL if you configure CloudFront to forward all headers to your origin (under Headers , if you specify 1 for Quantity and * for Name ).\n\nAllowedMethods (dict) --A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices:\n\nCloudFront forwards only GET and HEAD requests.\nCloudFront forwards only GET , HEAD , and OPTIONS requests.\nCloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests.\n\nIf you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can\'t perform operations that you don\'t want them to. For example, you might not want users to have permissions to delete objects from your origin.\n\nQuantity (integer) -- [REQUIRED]The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET , HEAD , and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests).\n\nItems (list) -- [REQUIRED]A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.\n\n(string) --\n\n\nCachedMethods (dict) --A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices:\n\nCloudFront caches responses to GET and HEAD requests.\nCloudFront caches responses to GET , HEAD , and OPTIONS requests.\n\nIf you pick the second choice for your Amazon S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers, and Origin headers for the responses to be cached correctly.\n\nQuantity (integer) -- [REQUIRED]The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET , HEAD , and OPTIONS requests).\n\nItems (list) -- [REQUIRED]A complex type that contains the HTTP methods that you want CloudFront to cache responses to.\n\n(string) --\n\n\n\n\n\n\nSmoothStreaming (boolean) --Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true ; if not, specify false . If you specify true for SmoothStreaming , you can still distribute other content using this cache behavior if the content matches the value of PathPattern .\n\nDefaultTTL (integer) --The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .\n\nMaxTTL (integer) --The maximum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .\n\nCompress (boolean) --Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify true; if not, specify false. For more information, see Serving Compressed Files in the Amazon CloudFront Developer Guide .\n\nLambdaFunctionAssociations (dict) --A complex type that contains zero or more Lambda function associations for a cache behavior.\n\nQuantity (integer) -- [REQUIRED]The number of Lambda function associations for this cache behavior.\n\nItems (list) --\nOptional : A complex type that contains LambdaFunctionAssociation items for this cache behavior. If Quantity is 0 , you can omit Items .\n\n(dict) --A complex type that contains a Lambda function association.\n\nLambdaFunctionARN (string) -- [REQUIRED]The ARN of the Lambda function. You must specify the ARN of a function version; you can\'t specify a Lambda alias or $LATEST.\n\nEventType (string) -- [REQUIRED]Specifies the event type that triggers a Lambda function invocation. You can specify the following values:\n\nviewer-request : The function executes when CloudFront receives a request from a viewer and before it checks to see whether the requested object is in the edge cache.\norigin-request : The function executes only when CloudFront forwards a request to your origin. When the requested object is in the edge cache, the function doesn\'t execute.\norigin-response : The function executes after CloudFront receives a response from the origin and before it caches the object in the response. When the requested object is in the edge cache, the function doesn\'t execute.\nviewer-response : The function executes before CloudFront returns the requested object to the viewer. The function executes regardless of whether the object was already in the edge cache. If the origin returns an HTTP status code other than HTTP 200 (OK), the function doesn\'t execute.\n\n\nIncludeBody (boolean) --A flag that allows a Lambda function to have read access to the body content. For more information, see Accessing the Request Body by Choosing the Include Body Option in the Amazon CloudFront Developer Guide.\n\n\n\n\n\n\n\nFieldLevelEncryptionId (string) --The value of ID for the field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data for a cache behavior or for the default cache behavior in your distribution.\n\n\n\n\n\n\n\nCustomErrorResponses (dict) --A complex type that controls the following:\n\nWhether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.\nHow long CloudFront caches HTTP status codes in the 4xx and 5xx range.\n\nFor more information about custom error pages, see Customizing Error Responses in the Amazon CloudFront Developer Guide .\n\nQuantity (integer) -- [REQUIRED]The number of HTTP status codes for which you want to specify a custom error page and/or a caching duration. If Quantity is 0 , you can omit Items .\n\nItems (list) --A complex type that contains a CustomErrorResponse element for each HTTP status code for which you want to specify a custom error page and/or a caching duration.\n\n(dict) --A complex type that controls:\n\nWhether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.\nHow long CloudFront caches HTTP status codes in the 4xx and 5xx range.\n\nFor more information about custom error pages, see Customizing Error Responses in the Amazon CloudFront Developer Guide .\n\nErrorCode (integer) -- [REQUIRED]The HTTP status code for which you want to specify a custom error page and/or a caching duration.\n\nResponsePagePath (string) --The path to the custom error page that you want CloudFront to return to a viewer when your origin returns the HTTP status code specified by ErrorCode , for example, /4xx-errors/403-forbidden.html . If you want to store your objects and your custom error pages in different locations, your distribution must include a cache behavior for which the following is true:\n\nThe value of PathPattern matches the path to your custom error messages. For example, suppose you saved custom error pages for 4xx errors in an Amazon S3 bucket in a directory named /4xx-errors . Your distribution must include a cache behavior for which the path pattern routes requests for your custom error pages to that location, for example, /4xx-errors/* .\nThe value of TargetOriginId specifies the value of the ID element for the origin that contains your custom error pages.\n\nIf you specify a value for ResponsePagePath , you must also specify a value for ResponseCode .\nWe recommend that you store custom error pages in an Amazon S3 bucket. If you store custom error pages on an HTTP server and the server starts to return 5xx errors, CloudFront can\'t get the files that you want to return to viewers because the origin server is unavailable.\n\nResponseCode (string) --The HTTP status code that you want CloudFront to return to the viewer along with the custom error page. There are a variety of reasons that you might want CloudFront to return a status code different from the status code that your origin returned to CloudFront, for example:\n\nSome Internet devices (some firewalls and corporate proxies, for example) intercept HTTP 4xx and 5xx and prevent the response from being returned to the viewer. If you substitute 200 , the response typically won\'t be intercepted.\nIf you don\'t care about distinguishing among different client errors or server errors, you can specify 400 or 500 as the ResponseCode for all 4xx or 5xx errors.\nYou might want to return a 200 status code (OK) and static website so your customers don\'t know that your website is down.\n\nIf you specify a value for ResponseCode , you must also specify a value for ResponsePagePath .\n\nErrorCachingMinTTL (integer) --The minimum amount of time, in seconds, that you want CloudFront to cache the HTTP status code specified in ErrorCode . When this time period has elapsed, CloudFront queries your origin to see whether the problem that caused the error has been resolved and the requested object is now available.\nFor more information, see Customizing Error Responses in the Amazon CloudFront Developer Guide .\n\n\n\n\n\n\n\nComment (string) -- [REQUIRED]Any comments you want to include about the distribution.\nIf you don\'t want to specify a comment, include an empty Comment element.\nTo delete an existing comment, update the distribution configuration and include an empty Comment element.\nTo add or change a comment, update the distribution configuration and specify the new comment.\n\nLogging (dict) --A complex type that controls whether access logs are written for the distribution.\nFor more information about logging, see Access Logs in the Amazon CloudFront Developer Guide .\n\nEnabled (boolean) -- [REQUIRED]Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you don\'t want to enable logging when you create a distribution or if you want to disable logging for an existing distribution, specify false for Enabled , and specify empty Bucket and Prefix elements. If you specify false for Enabled but you specify values for Bucket , prefix , and IncludeCookies , the values are automatically deleted.\n\nIncludeCookies (boolean) -- [REQUIRED]Specifies whether you want CloudFront to include cookies in access logs, specify true for IncludeCookies . If you choose to include cookies in logs, CloudFront logs all cookies regardless of how you configure the cache behaviors for this distribution. If you don\'t want to include cookies when you create a distribution or if you want to disable include cookies for an existing distribution, specify false for IncludeCookies .\n\nBucket (string) -- [REQUIRED]The Amazon S3 bucket to store the access logs in, for example, myawslogbucket.s3.amazonaws.com .\n\nPrefix (string) -- [REQUIRED]An optional string that you want CloudFront to prefix to the access log filenames for this distribution, for example, myprefix/ . If you want to enable logging, but you don\'t want to specify a prefix, you still must include an empty Prefix element in the Logging element.\n\n\n\nPriceClass (string) --The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify PriceClass_All , CloudFront responds to requests for your objects from all CloudFront edge locations.\nIf you specify a price class other than PriceClass_All , CloudFront serves your objects from the CloudFront edge location that has the lowest latency among the edge locations in your price class. Viewers who are in or near regions that are excluded from your specified price class may encounter slower performance.\nFor more information about price classes, see Choosing the Price Class for a CloudFront Distribution in the Amazon CloudFront Developer Guide . For information about CloudFront pricing, including how price classes (such as Price Class 100) map to CloudFront regions, see Amazon CloudFront Pricing . For price class information, scroll down to see the table at the bottom of the page.\n\nEnabled (boolean) -- [REQUIRED]From this field, you can enable or disable the selected distribution.\n\nViewerCertificate (dict) --A complex type that determines the distribution\xe2\x80\x99s SSL/TLS configuration for communicating with viewers.\n\nCloudFrontDefaultCertificate (boolean) --If the distribution uses the CloudFront domain name such as d111111abcdef8.cloudfront.net , set this field to true .\nIf the distribution uses Aliases (alternate domain names or CNAMEs), set this field to false and specify values for the following fields:\n\nACMCertificateArn or IAMCertificateId (specify a value for one, not both)\nMinimumProtocolVersion\nSSLSupportMethod\n\n\nIAMCertificateId (string) --If the distribution uses Aliases (alternate domain names or CNAMEs) and the SSL/TLS certificate is stored in AWS Identity and Access Management (AWS IAM) , provide the ID of the IAM certificate.\nIf you specify an IAM certificate ID, you must also specify values for MinimumProtocolVerison and SSLSupportMethod .\n\nACMCertificateArn (string) --If the distribution uses Aliases (alternate domain names or CNAMEs) and the SSL/TLS certificate is stored in AWS Certificate Manager (ACM) , provide the Amazon Resource Name (ARN) of the ACM certificate. CloudFront only supports ACM certificates in the US East (N. Virginia) Region (us-east-1 ).\nIf you specify an ACM certificate ARN, you must also specify values for MinimumProtocolVerison and SSLSupportMethod .\n\nSSLSupportMethod (string) --If the distribution uses Aliases (alternate domain names or CNAMEs), specify which viewers the distribution accepts HTTPS connections from.\n\nsni-only \xe2\x80\x93 The distribution accepts HTTPS connections from only viewers that support server name indication (SNI) . This is recommended. Most browsers and clients released after 2010 support SNI.\nvip \xe2\x80\x93 The distribution accepts HTTPS connections from all viewers including those that don\xe2\x80\x99t support SNI. This is not recommended, and results in additional monthly charges from CloudFront.\n\nIf the distribution uses the CloudFront domain name such as d111111abcdef8.cloudfront.net , don\xe2\x80\x99t set a value for this field.\n\nMinimumProtocolVersion (string) --If the distribution uses Aliases (alternate domain names or CNAMEs), specify the security policy that you want CloudFront to use for HTTPS connections with viewers. The security policy determines two settings:\n\nThe minimum SSL/TLS protocol that CloudFront can use to communicate with viewers.\nThe ciphers that CloudFront can use to encrypt the content that it returns to viewers.\n\nFor more information, see Security Policy and Supported Protocols and Ciphers Between Viewers and CloudFront in the Amazon CloudFront Developer Guide .\n\nNote\nOn the CloudFront console, this setting is called Security Policy .\n\nWe recommend that you specify TLSv1.2_2018 unless your viewers are using browsers or devices that don\xe2\x80\x99t support TLSv1.2.\nWhen you\xe2\x80\x99re using SNI only (you set SSLSupportMethod to sni-only ), you must specify TLSv1 or higher.\nIf the distribution uses the CloudFront domain name such as d111111abcdef8.cloudfront.net (you set CloudFrontDefaultCertificate to true ), CloudFront automatically sets the security policy to TLSv1 regardless of the value that you set here.\n\nCertificate (string) --This field is deprecated. Use one of the following fields instead:\n\nACMCertificateArn\nIAMCertificateId\nCloudFrontDefaultCertificate\n\n\nCertificateSource (string) --This field is deprecated. Use one of the following fields instead:\n\nACMCertificateArn\nIAMCertificateId\nCloudFrontDefaultCertificate\n\n\n\n\nRestrictions (dict) --A complex type that identifies ways in which you want to restrict distribution of your content.\n\nGeoRestriction (dict) -- [REQUIRED]A complex type that controls the countries in which your content is distributed. CloudFront determines the location of your users using MaxMind GeoIP databases.\n\nRestrictionType (string) -- [REQUIRED]The method that you want to use to restrict distribution of your content by country:\n\nnone : No geo restriction is enabled, meaning access to content is not restricted by client geo location.\nblacklist : The Location elements specify the countries in which you don\'t want CloudFront to distribute your content.\nwhitelist : The Location elements specify the countries in which you want CloudFront to distribute your content.\n\n\nQuantity (integer) -- [REQUIRED]When geo restriction is enabled , this is the number of countries in your whitelist or blacklist . Otherwise, when it is not enabled, Quantity is 0 , and you can omit Items .\n\nItems (list) --A complex type that contains a Location element for each country in which you want CloudFront either to distribute your content (whitelist ) or not distribute your content (blacklist ).\nThe Location element is a two-letter, uppercase country code for a country that you want to include in your blacklist or whitelist . Include one Location element for each country.\nCloudFront and MaxMind both use ISO 3166 country codes. For the current list of countries and the corresponding codes, see ISO 3166-1-alpha-2 code on the International Organization for Standardization website. You can also refer to the country list on the CloudFront console, which includes both country names and codes.\n\n(string) --\n\n\n\n\n\n\nWebACLId (string) --A unique identifier that specifies the AWS WAF web ACL, if any, to associate with this distribution. To specify a web ACL created using the latest version of AWS WAF, use the ACL ARN, for example arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/473e64fd-f30b-4765-81a0-62ad96dd167a . To specify a web ACL created using AWS WAF Classic, use the ACL ID, for example 473e64fd-f30b-4765-81a0-62ad96dd167a .\nAWS WAF is a web application firewall that lets you monitor the HTTP and HTTPS requests that are forwarded to CloudFront, and lets you control access to your content. Based on conditions that you specify, such as the IP addresses that requests originate from or the values of query strings, CloudFront responds to requests either with the requested content or with an HTTP 403 status code (Forbidden). You can also configure CloudFront to return a custom error page when a request is blocked. For more information about AWS WAF, see the AWS WAF Developer Guide .\n\nHttpVersion (string) --(Optional) Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront. The default value for new web distributions is http2. Viewers that don\'t support HTTP/2 automatically use an earlier HTTP version.\nFor viewers and CloudFront to use HTTP/2, viewers must support TLS 1.2 or later, and must support Server Name Identification (SNI).\nIn general, configuring CloudFront to communicate with viewers using HTTP/2 reduces latency. You can improve performance by optimizing for HTTP/2. For more information, do an Internet search for 'http/2 optimization.'\n\nIsIPV6Enabled (boolean) --If you want CloudFront to respond to IPv6 DNS requests with an IPv6 address for your distribution, specify true . If you specify false , CloudFront responds to IPv6 DNS requests with the DNS response code NOERROR and with no IP addresses. This allows viewers to submit a second request, for an IPv4 address for your distribution.\nIn general, you should enable IPv6 if you have users on IPv6 networks who want to access your content. However, if you\'re using signed URLs or signed cookies to restrict access to your content, and if you\'re using a custom policy that includes the IpAddress parameter to restrict the IP addresses that can access your content, don\'t enable IPv6. If you want to restrict access to some content by IP address and not restrict access to other content (or restrict access but not by IP address), you can create two distributions. For more information, see Creating a Signed URL Using a Custom Policy in the Amazon CloudFront Developer Guide .\nIf you\'re using an Amazon Route 53 alias resource record set to route traffic to your CloudFront distribution, you need to create a second alias resource record set when both of the following are true:\n\nYou enable IPv6 for the distribution\nYou\'re using alternate domain names in the URLs for your objects\n\nFor more information, see Routing Traffic to an Amazon CloudFront Web Distribution by Using Your Domain Name in the Amazon Route 53 Developer Guide .\nIf you created a CNAME resource record set, either with Amazon Route 53 or with another DNS service, you don\'t need to make any changes. A CNAME record will route traffic to your distribution regardless of the IP address format of the viewer request.\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'Distribution': {
        'Id': 'string',
        'ARN': 'string',
        'Status': 'string',
        'LastModifiedTime': datetime(2015, 1, 1),
        'InProgressInvalidationBatches': 123,
        'DomainName': 'string',
        'ActiveTrustedSigners': {
            'Enabled': True|False,
            'Quantity': 123,
            'Items': [
                {
                    'AwsAccountNumber': 'string',
                    'KeyPairIds': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    }
                },
            ]
        },
        'DistributionConfig': {
            'CallerReference': 'string',
            'Aliases': {
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'DefaultRootObject': 'string',
            'Origins': {
                'Quantity': 123,
                'Items': [
                    {
                        'Id': 'string',
                        'DomainName': 'string',
                        'OriginPath': 'string',
                        'CustomHeaders': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'HeaderName': 'string',
                                    'HeaderValue': 'string'
                                },
                            ]
                        },
                        'S3OriginConfig': {
                            'OriginAccessIdentity': 'string'
                        },
                        'CustomOriginConfig': {
                            'HTTPPort': 123,
                            'HTTPSPort': 123,
                            'OriginProtocolPolicy': 'http-only'|'match-viewer'|'https-only',
                            'OriginSslProtocols': {
                                'Quantity': 123,
                                'Items': [
                                    'SSLv3'|'TLSv1'|'TLSv1.1'|'TLSv1.2',
                                ]
                            },
                            'OriginReadTimeout': 123,
                            'OriginKeepaliveTimeout': 123
                        }
                    },
                ]
            },
            'OriginGroups': {
                'Quantity': 123,
                'Items': [
                    {
                        'Id': 'string',
                        'FailoverCriteria': {
                            'StatusCodes': {
                                'Quantity': 123,
                                'Items': [
                                    123,
                                ]
                            }
                        },
                        'Members': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'OriginId': 'string'
                                },
                            ]
                        }
                    },
                ]
            },
            'DefaultCacheBehavior': {
                'TargetOriginId': 'string',
                'ForwardedValues': {
                    'QueryString': True|False,
                    'Cookies': {
                        'Forward': 'none'|'whitelist'|'all',
                        'WhitelistedNames': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                    'Headers': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    },
                    'QueryStringCacheKeys': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    }
                },
                'TrustedSigners': {
                    'Enabled': True|False,
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                'MinTTL': 123,
                'AllowedMethods': {
                    'Quantity': 123,
                    'Items': [
                        'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                    ],
                    'CachedMethods': {
                        'Quantity': 123,
                        'Items': [
                            'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                        ]
                    }
                },
                'SmoothStreaming': True|False,
                'DefaultTTL': 123,
                'MaxTTL': 123,
                'Compress': True|False,
                'LambdaFunctionAssociations': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'LambdaFunctionARN': 'string',
                            'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                            'IncludeBody': True|False
                        },
                    ]
                },
                'FieldLevelEncryptionId': 'string'
            },
            'CacheBehaviors': {
                'Quantity': 123,
                'Items': [
                    {
                        'PathPattern': 'string',
                        'TargetOriginId': 'string',
                        'ForwardedValues': {
                            'QueryString': True|False,
                            'Cookies': {
                                'Forward': 'none'|'whitelist'|'all',
                                'WhitelistedNames': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                }
                            },
                            'Headers': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            },
                            'QueryStringCacheKeys': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                        'TrustedSigners': {
                            'Enabled': True|False,
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        },
                        'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                        'MinTTL': 123,
                        'AllowedMethods': {
                            'Quantity': 123,
                            'Items': [
                                'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                            ],
                            'CachedMethods': {
                                'Quantity': 123,
                                'Items': [
                                    'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                ]
                            }
                        },
                        'SmoothStreaming': True|False,
                        'DefaultTTL': 123,
                        'MaxTTL': 123,
                        'Compress': True|False,
                        'LambdaFunctionAssociations': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'LambdaFunctionARN': 'string',
                                    'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                    'IncludeBody': True|False
                                },
                            ]
                        },
                        'FieldLevelEncryptionId': 'string'
                    },
                ]
            },
            'CustomErrorResponses': {
                'Quantity': 123,
                'Items': [
                    {
                        'ErrorCode': 123,
                        'ResponsePagePath': 'string',
                        'ResponseCode': 'string',
                        'ErrorCachingMinTTL': 123
                    },
                ]
            },
            'Comment': 'string',
            'Logging': {
                'Enabled': True|False,
                'IncludeCookies': True|False,
                'Bucket': 'string',
                'Prefix': 'string'
            },
            'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
            'Enabled': True|False,
            'ViewerCertificate': {
                'CloudFrontDefaultCertificate': True|False,
                'IAMCertificateId': 'string',
                'ACMCertificateArn': 'string',
                'SSLSupportMethod': 'sni-only'|'vip',
                'MinimumProtocolVersion': 'SSLv3'|'TLSv1'|'TLSv1_2016'|'TLSv1.1_2016'|'TLSv1.2_2018',
                'Certificate': 'string',
                'CertificateSource': 'cloudfront'|'iam'|'acm'
            },
            'Restrictions': {
                'GeoRestriction': {
                    'RestrictionType': 'blacklist'|'whitelist'|'none',
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                }
            },
            'WebACLId': 'string',
            'HttpVersion': 'http1.1'|'http2',
            'IsIPV6Enabled': True|False
        },
        'AliasICPRecordals': [
            {
                'CNAME': 'string',
                'ICPRecordalStatus': 'APPROVED'|'SUSPENDED'|'PENDING'
            },
        ]
    },
    'Location': 'string',
    'ETag': 'string'
}


Response Structure

(dict) --The returned result of the corresponding request.

Distribution (dict) --The distribution\'s information.

Id (string) --The identifier for the distribution. For example: EDFDVBD632BHDS5 .

ARN (string) --The ARN (Amazon Resource Name) for the distribution. For example: arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5 , where 123456789012 is your AWS account ID.

Status (string) --This response element indicates the current status of the distribution. When the status is Deployed , the distribution\'s information is fully propagated to all CloudFront edge locations.

LastModifiedTime (datetime) --The date and time the distribution was last modified.

InProgressInvalidationBatches (integer) --The number of invalidation batches currently in progress.

DomainName (string) --The domain name corresponding to the distribution, for example, d111111abcdef8.cloudfront.net .

ActiveTrustedSigners (dict) --CloudFront automatically adds this element to the response only if you\'ve set up the distribution to serve private content with signed URLs. The element lists the key pair IDs that CloudFront is aware of for each trusted signer. The Signer child element lists the AWS account number of the trusted signer (or an empty Self element if the signer is you). The Signer element also includes the IDs of any active key pairs associated with the trusted signer\'s AWS account. If no KeyPairId element appears for a Signer , that signer can\'t create working signed URLs.

Enabled (boolean) --Enabled is true if any of the AWS accounts listed in the TrustedSigners complex type for this distribution have active CloudFront key pairs. If not, Enabled is false .

Quantity (integer) --The number of trusted signers specified in the TrustedSigners complex type.

Items (list) --A complex type that contains one Signer complex type for each trusted signer that is specified in the TrustedSigners complex type.

(dict) --A complex type that lists the AWS accounts that were included in the TrustedSigners complex type, as well as their active CloudFront key pair IDs, if any.

AwsAccountNumber (string) --An AWS account that is included in the TrustedSigners complex type for this distribution. Valid values include:

self , which is the AWS account used to create the distribution.
An AWS account number.


KeyPairIds (dict) --A complex type that lists the active CloudFront key pairs, if any, that are associated with AwsAccountNumber .

Quantity (integer) --The number of active CloudFront key pairs for AwsAccountNumber .
For more information, see ActiveTrustedSigners .

Items (list) --A complex type that lists the active CloudFront key pairs, if any, that are associated with AwsAccountNumber .
For more information, see ActiveTrustedSigners .

(string) --










DistributionConfig (dict) --The current configuration information for the distribution. Send a GET request to the /*CloudFront API version* /distribution ID/config resource.

CallerReference (string) --A unique value (for example, a date-time stamp) that ensures that the request can\'t be replayed.
If the value of CallerReference is new (regardless of the content of the DistributionConfig object), CloudFront creates a new distribution.
If CallerReference is a value that you already sent in a previous request to create a distribution, CloudFront returns a DistributionAlreadyExists error.

Aliases (dict) --A complex type that contains information about CNAMEs (alternate domain names), if any, for this distribution.

Quantity (integer) --The number of CNAME aliases, if any, that you want to associate with this distribution.

Items (list) --A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.

(string) --




DefaultRootObject (string) --The object that you want CloudFront to request from your origin (for example, index.html ) when a viewer requests the root URL for your distribution (http://www.example.com ) instead of an object in your distribution (http://www.example.com/product-description.html ). Specifying a default root object avoids exposing the contents of your distribution.
Specify only the object name, for example, index.html . Don\'t add a / before the object name.
If you don\'t want to specify a default root object when you create a distribution, include an empty DefaultRootObject element.
To delete the default root object from an existing distribution, update the distribution configuration and include an empty DefaultRootObject element.
To replace the default root object, update the distribution configuration and specify the new object.
For more information about the default root object, see Creating a Default Root Object in the Amazon CloudFront Developer Guide .

Origins (dict) --A complex type that contains information about origins for this distribution.

Quantity (integer) --The number of origins or origin groups for this distribution.

Items (list) --A complex type that contains origins or origin groups for this distribution.

(dict) --A complex type that describes the Amazon S3 bucket, HTTP server (for example, a web server), Amazon MediaStore, or other server from which CloudFront gets your files. This can also be an origin group, if you\'ve created an origin group. You must specify at least one origin or origin group.
For the current limit on the number of origins or origin groups that you can specify for a distribution, see Amazon CloudFront Limits in the AWS General Reference .

Id (string) --A unique identifier for the origin or origin group. The value of Id must be unique within the distribution.
When you specify the value of TargetOriginId for the default cache behavior or for another cache behavior, you indicate the origin to which you want the cache behavior to route requests by specifying the value of the Id element for that origin. When a request matches the path pattern for that cache behavior, CloudFront routes the request to the specified origin. For more information, see Cache Behavior Settings in the Amazon CloudFront Developer Guide .

DomainName (string) --
Amazon S3 origins : The DNS name of the Amazon S3 bucket from which you want CloudFront to get objects for this origin, for example, myawsbucket.s3.amazonaws.com . If you set up your bucket to be configured as a website endpoint, enter the Amazon S3 static website hosting endpoint for the bucket.
For more information about specifying this value for different types of origins, see Origin Domain Name in the Amazon CloudFront Developer Guide .
Constraints for Amazon S3 origins:

If you configured Amazon S3 Transfer Acceleration for your bucket, don\'t specify the s3-accelerate endpoint for DomainName .
The bucket name must be between 3 and 63 characters long (inclusive).
The bucket name must contain only lowercase characters, numbers, periods, underscores, and dashes.
The bucket name must not contain adjacent periods.


Custom Origins : The DNS domain name for the HTTP server from which you want CloudFront to get objects for this origin, for example, www.example.com .
Constraints for custom origins:

DomainName must be a valid DNS name that contains only a-z, A-Z, 0-9, dot (.), hyphen (-), or underscore (_) characters.
The name cannot exceed 128 characters.


OriginPath (string) --An optional element that causes CloudFront to request your content from a directory in your Amazon S3 bucket or your custom origin. When you include the OriginPath element, specify the directory name, beginning with a / . CloudFront appends the directory name to the value of DomainName , for example, example.com/production . Do not include a / at the end of the directory name.
For example, suppose you\'ve specified the following values for your distribution:

DomainName : An Amazon S3 bucket named myawsbucket .
OriginPath : /production
CNAME : example.com

When a user enters example.com/index.html in a browser, CloudFront sends a request to Amazon S3 for myawsbucket/production/index.html .
When a user enters example.com/acme/index.html in a browser, CloudFront sends a request to Amazon S3 for myawsbucket/production/acme/index.html .

CustomHeaders (dict) --A complex type that contains names and values for the custom headers that you want.

Quantity (integer) --The number of custom headers, if any, for this distribution.

Items (list) --
Optional : A list that contains one OriginCustomHeader element for each custom header that you want CloudFront to forward to the origin. If Quantity is 0 , omit Items .

(dict) --A complex type that contains HeaderName and HeaderValue elements, if any, for this distribution.

HeaderName (string) --The name of a header that you want CloudFront to forward to your origin. For more information, see Forwarding Custom Headers to Your Origin (Web Distributions Only) in the Amazon CloudFront Developer Guide .

HeaderValue (string) --The value for the header that you specified in the HeaderName field.







S3OriginConfig (dict) --A complex type that contains information about the Amazon S3 origin. If the origin is a custom origin, use the CustomOriginConfig element instead.

OriginAccessIdentity (string) --The CloudFront origin access identity to associate with the origin. Use an origin access identity to configure the origin so that viewers can only access objects in an Amazon S3 bucket through CloudFront. The format of the value is:
origin-access-identity/cloudfront/ID-of-origin-access-identity
where `` ID-of-origin-access-identity `` is the value that CloudFront returned in the ID element when you created the origin access identity.
If you want viewers to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty OriginAccessIdentity element.
To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty OriginAccessIdentity element.
To replace the origin access identity, update the distribution configuration and specify the new origin access identity.
For more information about the origin access identity, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .



CustomOriginConfig (dict) --A complex type that contains information about a custom origin. If the origin is an Amazon S3 bucket, use the S3OriginConfig element instead.

HTTPPort (integer) --The HTTP port the custom origin listens on.

HTTPSPort (integer) --The HTTPS port the custom origin listens on.

OriginProtocolPolicy (string) --The origin protocol policy to apply to your origin.

OriginSslProtocols (dict) --The SSL/TLS protocols that you want CloudFront to use when communicating with your origin over HTTPS.

Quantity (integer) --The number of SSL/TLS protocols that you want to allow CloudFront to use when establishing an HTTPS connection with this origin.

Items (list) --A list that contains allowed SSL/TLS protocols for this distribution.

(string) --




OriginReadTimeout (integer) --You can create a custom origin read timeout. All timeout units are in seconds. The default origin read timeout is 30 seconds, but you can configure custom timeout lengths using the CloudFront API. The minimum timeout length is 4 seconds; the maximum is 60 seconds.
If you need to increase the maximum time limit, contact the AWS Support Center .

OriginKeepaliveTimeout (integer) --You can create a custom keep-alive timeout. All timeout units are in seconds. The default keep-alive timeout is 5 seconds, but you can configure custom timeout lengths using the CloudFront API. The minimum timeout length is 1 second; the maximum is 60 seconds.
If you need to increase the maximum time limit, contact the AWS Support Center .









OriginGroups (dict) --A complex type that contains information about origin groups for this distribution.

Quantity (integer) --The number of origin groups.

Items (list) --The items (origin groups) in a distribution.

(dict) --An origin group includes two origins (a primary origin and a second origin to failover to) and a failover criteria that you specify. You create an origin group to support origin failover in CloudFront. When you create or update a distribution, you can specifiy the origin group instead of a single origin, and CloudFront will failover from the primary origin to the second origin under the failover conditions that you\'ve chosen.

Id (string) --The origin group\'s ID.

FailoverCriteria (dict) --A complex type that contains information about the failover criteria for an origin group.

StatusCodes (dict) --The status codes that, when returned from the primary origin, will trigger CloudFront to failover to the second origin.

Quantity (integer) --The number of status codes.

Items (list) --The items (status codes) for an origin group.

(integer) --






Members (dict) --A complex type that contains information about the origins in an origin group.

Quantity (integer) --The number of origins in an origin group.

Items (list) --Items (origins) in an origin group.

(dict) --An origin in an origin group.

OriginId (string) --The ID for an origin in an origin group.













DefaultCacheBehavior (dict) --A complex type that describes the default cache behavior if you don\'t specify a CacheBehavior element or if files don\'t match any of the values of PathPattern in CacheBehavior elements. You must create exactly one default cache behavior.

TargetOriginId (string) --The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior in your distribution.

ForwardedValues (dict) --A complex type that specifies how CloudFront handles query strings, cookies, and HTTP headers.

QueryString (boolean) --Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior and cache based on the query string parameters. CloudFront behavior depends on the value of QueryString and on the values that you specify for QueryStringCacheKeys , if any:
If you specify true for QueryString and you don\'t specify any values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin and caches based on all query string parameters. Depending on how many query string parameters and values you have, this can adversely affect performance because CloudFront must forward more requests to the origin.
If you specify true for QueryString and you specify one or more values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin, but it only caches based on the query string parameters that you specify.
If you specify false for QueryString , CloudFront doesn\'t forward any query string parameters to the origin, and doesn\'t cache based on query string parameters.
For more information, see Configuring CloudFront to Cache Based on Query String Parameters in the Amazon CloudFront Developer Guide .

Cookies (dict) --A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see How CloudFront Forwards, Caches, and Logs Cookies in the Amazon CloudFront Developer Guide .

Forward (string) --Specifies which cookies to forward to the origin for this cache behavior: all, none, or the list of cookies specified in the WhitelistedNames complex type.
Amazon S3 doesn\'t process cookies. When the cache behavior is forwarding requests to an Amazon S3 origin, specify none for the Forward element.

WhitelistedNames (dict) --Required if you specify whitelist for the value of Forward . A complex type that specifies how many different cookies you want CloudFront to forward to the origin for this cache behavior and, if you want to forward selected cookies, the names of those cookies.
If you specify all or none for the value of Forward , omit WhitelistedNames . If you change the value of Forward from whitelist to all or none and you don\'t delete the WhitelistedNames element and its child elements, CloudFront deletes them automatically.
For the current limit on the number of cookie names that you can whitelist for each cache behavior, see CloudFront Limits in the AWS General Reference .

Quantity (integer) --The number of different cookies that you want CloudFront to forward to the origin for this cache behavior. The value must equal the number of items that are in the Items field.
When you set Forward = whitelist (in the CookiePreferences object), this value must be 1 or higher.

Items (list) --A complex type that contains one Name element for each cookie that you want CloudFront to forward to the origin for this cache behavior. It must contain the same number of items that is specified in the Quantity field.
When you set Forward = whitelist (in the CookiePreferences object), this field must contain at least one item.

(string) --






Headers (dict) --A complex type that specifies the Headers , if any, that you want CloudFront to forward to the origin for this cache behavior (whitelisted headers). For the headers that you specify, CloudFront also caches separate versions of a specified object that is based on the header values in viewer requests.
For more information, see Caching Content Based on Request Headers in the Amazon CloudFront Developer Guide .

Quantity (integer) --The number of different headers that you want CloudFront to base caching on for this cache behavior. You can configure each cache behavior in a web distribution to do one of the following:

Forward all headers to your origin : Specify 1 for Quantity and * for Name .


Warning
CloudFront doesn\'t cache the objects that are associated with this cache behavior. Instead, CloudFront sends every request to the origin.


Forward a whitelist of headers you specify : Specify the number of headers that you want CloudFront to base caching on. Then specify the header names in Name elements. CloudFront caches your objects based on the values in the specified headers.
Forward only the default headers : Specify 0 for Quantity and omit Items . In this configuration, CloudFront doesn\'t cache based on the values in the request headers.

Regardless of which option you choose, CloudFront forwards headers to your origin based on whether the origin is an S3 bucket or a custom origin. See the following documentation:

S3 bucket : See HTTP Request Headers That CloudFront Removes or Updates
Custom origin : See HTTP Request Headers and CloudFront Behavior


Items (list) --A list that contains one Name element for each header that you want CloudFront to use for caching in this cache behavior. If Quantity is 0 , omit Items .

(string) --




QueryStringCacheKeys (dict) --A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.

Quantity (integer) --The number of whitelisted query string parameters for a cache behavior.

Items (list) --A list that contains the query string parameters that you want CloudFront to use as a basis for caching for a cache behavior. If Quantity is 0, you can omit Items .

(string) --






TrustedSigners (dict) --A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content.
If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled , and specify the applicable values for Quantity and Items . For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .
If you don\'t want to require signed URLs in requests for objects that match PathPattern , specify false for Enabled and 0 for Quantity . Omit Items .
To add, change, or remove one or more trusted signers, change Enabled to true (if it\'s currently false ), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.

Enabled (boolean) --Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .

Quantity (integer) --The number of trusted signers for this cache behavior.

Items (list) --
Optional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .

(string) --




ViewerProtocolPolicy (string) --The protocol that viewers can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern . You can specify the following options:

allow-all : Viewers can use HTTP or HTTPS.
redirect-to-https : If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.
https-only : If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).

For more information about requiring the HTTPS protocol, see Using an HTTPS Connection to Access Your Objects in the Amazon CloudFront Developer Guide .

Note
The only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects\' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .


MinTTL (integer) --The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .
You must specify 0 for MinTTL if you configure CloudFront to forward all headers to your origin (under Headers , if you specify 1 for Quantity and * for Name ).

AllowedMethods (dict) --A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices:

CloudFront forwards only GET and HEAD requests.
CloudFront forwards only GET , HEAD , and OPTIONS requests.
CloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests.

If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can\'t perform operations that you don\'t want them to. For example, you might not want users to have permissions to delete objects from your origin.

Quantity (integer) --The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET , HEAD , and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests).

Items (list) --A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.

(string) --


CachedMethods (dict) --A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices:

CloudFront caches responses to GET and HEAD requests.
CloudFront caches responses to GET , HEAD , and OPTIONS requests.

If you pick the second choice for your Amazon S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers, and Origin headers for the responses to be cached correctly.

Quantity (integer) --The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET , HEAD , and OPTIONS requests).

Items (list) --A complex type that contains the HTTP methods that you want CloudFront to cache responses to.

(string) --






SmoothStreaming (boolean) --Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true ; if not, specify false . If you specify true for SmoothStreaming , you can still distribute other content using this cache behavior if the content matches the value of PathPattern .

DefaultTTL (integer) --The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .

MaxTTL (integer) --The maximum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .

Compress (boolean) --Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify true ; if not, specify false . For more information, see Serving Compressed Files in the Amazon CloudFront Developer Guide .

LambdaFunctionAssociations (dict) --A complex type that contains zero or more Lambda function associations for a cache behavior.

Quantity (integer) --The number of Lambda function associations for this cache behavior.

Items (list) --
Optional : A complex type that contains LambdaFunctionAssociation items for this cache behavior. If Quantity is 0 , you can omit Items .

(dict) --A complex type that contains a Lambda function association.

LambdaFunctionARN (string) --The ARN of the Lambda function. You must specify the ARN of a function version; you can\'t specify a Lambda alias or $LATEST.

EventType (string) --Specifies the event type that triggers a Lambda function invocation. You can specify the following values:

viewer-request : The function executes when CloudFront receives a request from a viewer and before it checks to see whether the requested object is in the edge cache.
origin-request : The function executes only when CloudFront forwards a request to your origin. When the requested object is in the edge cache, the function doesn\'t execute.
origin-response : The function executes after CloudFront receives a response from the origin and before it caches the object in the response. When the requested object is in the edge cache, the function doesn\'t execute.
viewer-response : The function executes before CloudFront returns the requested object to the viewer. The function executes regardless of whether the object was already in the edge cache. If the origin returns an HTTP status code other than HTTP 200 (OK), the function doesn\'t execute.


IncludeBody (boolean) --A flag that allows a Lambda function to have read access to the body content. For more information, see Accessing the Request Body by Choosing the Include Body Option in the Amazon CloudFront Developer Guide.







FieldLevelEncryptionId (string) --The value of ID for the field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data for a cache behavior or for the default cache behavior in your distribution.



CacheBehaviors (dict) --A complex type that contains zero or more CacheBehavior elements.

Quantity (integer) --The number of cache behaviors for this distribution.

Items (list) --Optional: A complex type that contains cache behaviors for this distribution. If Quantity is 0 , you can omit Items .

(dict) --A complex type that describes how CloudFront processes requests.
You must create at least as many cache behaviors (including the default cache behavior) as you have origins if you want CloudFront to distribute objects from all of the origins. Each cache behavior specifies the one origin from which you want CloudFront to get objects. If you have two origins and only the default cache behavior, the default cache behavior will cause CloudFront to get objects from one of the origins, but the other origin is never used.
For the current limit on the number of cache behaviors that you can add to a distribution, see Amazon CloudFront Limits in the AWS General Reference .
If you don\'t want to specify any cache behaviors, include only an empty CacheBehaviors element. Don\'t include an empty CacheBehavior element, or CloudFront returns a MalformedXML error.
To delete all cache behaviors in an existing distribution, update the distribution configuration and include only an empty CacheBehaviors element.
To add, change, or remove one or more cache behaviors, update the distribution configuration and specify all of the cache behaviors that you want to include in the updated distribution.
For more information about cache behaviors, see Cache Behaviors in the Amazon CloudFront Developer Guide .

PathPattern (string) --The pattern (for example, images/*.jpg ) that specifies which requests to apply the behavior to. When CloudFront receives a viewer request, the requested path is compared with path patterns in the order in which cache behaviors are listed in the distribution.

Note
You can optionally include a slash (/ ) at the beginning of the path pattern. For example, /images/*.jpg . CloudFront behavior is the same with or without the leading / .

The path pattern for the default cache behavior is * and cannot be changed. If the request for an object does not match the path pattern for any cache behaviors, CloudFront applies the behavior in the default cache behavior.
For more information, see Path Pattern in the Amazon CloudFront Developer Guide .

TargetOriginId (string) --The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior in your distribution.

ForwardedValues (dict) --A complex type that specifies how CloudFront handles query strings, cookies, and HTTP headers.

QueryString (boolean) --Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior and cache based on the query string parameters. CloudFront behavior depends on the value of QueryString and on the values that you specify for QueryStringCacheKeys , if any:
If you specify true for QueryString and you don\'t specify any values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin and caches based on all query string parameters. Depending on how many query string parameters and values you have, this can adversely affect performance because CloudFront must forward more requests to the origin.
If you specify true for QueryString and you specify one or more values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin, but it only caches based on the query string parameters that you specify.
If you specify false for QueryString , CloudFront doesn\'t forward any query string parameters to the origin, and doesn\'t cache based on query string parameters.
For more information, see Configuring CloudFront to Cache Based on Query String Parameters in the Amazon CloudFront Developer Guide .

Cookies (dict) --A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see How CloudFront Forwards, Caches, and Logs Cookies in the Amazon CloudFront Developer Guide .

Forward (string) --Specifies which cookies to forward to the origin for this cache behavior: all, none, or the list of cookies specified in the WhitelistedNames complex type.
Amazon S3 doesn\'t process cookies. When the cache behavior is forwarding requests to an Amazon S3 origin, specify none for the Forward element.

WhitelistedNames (dict) --Required if you specify whitelist for the value of Forward . A complex type that specifies how many different cookies you want CloudFront to forward to the origin for this cache behavior and, if you want to forward selected cookies, the names of those cookies.
If you specify all or none for the value of Forward , omit WhitelistedNames . If you change the value of Forward from whitelist to all or none and you don\'t delete the WhitelistedNames element and its child elements, CloudFront deletes them automatically.
For the current limit on the number of cookie names that you can whitelist for each cache behavior, see CloudFront Limits in the AWS General Reference .

Quantity (integer) --The number of different cookies that you want CloudFront to forward to the origin for this cache behavior. The value must equal the number of items that are in the Items field.
When you set Forward = whitelist (in the CookiePreferences object), this value must be 1 or higher.

Items (list) --A complex type that contains one Name element for each cookie that you want CloudFront to forward to the origin for this cache behavior. It must contain the same number of items that is specified in the Quantity field.
When you set Forward = whitelist (in the CookiePreferences object), this field must contain at least one item.

(string) --






Headers (dict) --A complex type that specifies the Headers , if any, that you want CloudFront to forward to the origin for this cache behavior (whitelisted headers). For the headers that you specify, CloudFront also caches separate versions of a specified object that is based on the header values in viewer requests.
For more information, see Caching Content Based on Request Headers in the Amazon CloudFront Developer Guide .

Quantity (integer) --The number of different headers that you want CloudFront to base caching on for this cache behavior. You can configure each cache behavior in a web distribution to do one of the following:

Forward all headers to your origin : Specify 1 for Quantity and * for Name .


Warning
CloudFront doesn\'t cache the objects that are associated with this cache behavior. Instead, CloudFront sends every request to the origin.


Forward a whitelist of headers you specify : Specify the number of headers that you want CloudFront to base caching on. Then specify the header names in Name elements. CloudFront caches your objects based on the values in the specified headers.
Forward only the default headers : Specify 0 for Quantity and omit Items . In this configuration, CloudFront doesn\'t cache based on the values in the request headers.

Regardless of which option you choose, CloudFront forwards headers to your origin based on whether the origin is an S3 bucket or a custom origin. See the following documentation:

S3 bucket : See HTTP Request Headers That CloudFront Removes or Updates
Custom origin : See HTTP Request Headers and CloudFront Behavior


Items (list) --A list that contains one Name element for each header that you want CloudFront to use for caching in this cache behavior. If Quantity is 0 , omit Items .

(string) --




QueryStringCacheKeys (dict) --A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.

Quantity (integer) --The number of whitelisted query string parameters for a cache behavior.

Items (list) --A list that contains the query string parameters that you want CloudFront to use as a basis for caching for a cache behavior. If Quantity is 0, you can omit Items .

(string) --






TrustedSigners (dict) --A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content.
If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled , and specify the applicable values for Quantity and Items . For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .
If you don\'t want to require signed URLs in requests for objects that match PathPattern , specify false for Enabled and 0 for Quantity . Omit Items .
To add, change, or remove one or more trusted signers, change Enabled to true (if it\'s currently false ), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.

Enabled (boolean) --Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .

Quantity (integer) --The number of trusted signers for this cache behavior.

Items (list) --
Optional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .

(string) --




ViewerProtocolPolicy (string) --The protocol that viewers can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern . You can specify the following options:

allow-all : Viewers can use HTTP or HTTPS.
redirect-to-https : If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.
https-only : If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).

For more information about requiring the HTTPS protocol, see Using an HTTPS Connection to Access Your Objects in the Amazon CloudFront Developer Guide .

Note
The only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects\' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .


MinTTL (integer) --The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .
You must specify 0 for MinTTL if you configure CloudFront to forward all headers to your origin (under Headers , if you specify 1 for Quantity and * for Name ).

AllowedMethods (dict) --A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices:

CloudFront forwards only GET and HEAD requests.
CloudFront forwards only GET , HEAD , and OPTIONS requests.
CloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests.

If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can\'t perform operations that you don\'t want them to. For example, you might not want users to have permissions to delete objects from your origin.

Quantity (integer) --The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET , HEAD , and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests).

Items (list) --A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.

(string) --


CachedMethods (dict) --A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices:

CloudFront caches responses to GET and HEAD requests.
CloudFront caches responses to GET , HEAD , and OPTIONS requests.

If you pick the second choice for your Amazon S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers, and Origin headers for the responses to be cached correctly.

Quantity (integer) --The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET , HEAD , and OPTIONS requests).

Items (list) --A complex type that contains the HTTP methods that you want CloudFront to cache responses to.

(string) --






SmoothStreaming (boolean) --Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true ; if not, specify false . If you specify true for SmoothStreaming , you can still distribute other content using this cache behavior if the content matches the value of PathPattern .

DefaultTTL (integer) --The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .

MaxTTL (integer) --The maximum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .

Compress (boolean) --Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify true; if not, specify false. For more information, see Serving Compressed Files in the Amazon CloudFront Developer Guide .

LambdaFunctionAssociations (dict) --A complex type that contains zero or more Lambda function associations for a cache behavior.

Quantity (integer) --The number of Lambda function associations for this cache behavior.

Items (list) --
Optional : A complex type that contains LambdaFunctionAssociation items for this cache behavior. If Quantity is 0 , you can omit Items .

(dict) --A complex type that contains a Lambda function association.

LambdaFunctionARN (string) --The ARN of the Lambda function. You must specify the ARN of a function version; you can\'t specify a Lambda alias or $LATEST.

EventType (string) --Specifies the event type that triggers a Lambda function invocation. You can specify the following values:

viewer-request : The function executes when CloudFront receives a request from a viewer and before it checks to see whether the requested object is in the edge cache.
origin-request : The function executes only when CloudFront forwards a request to your origin. When the requested object is in the edge cache, the function doesn\'t execute.
origin-response : The function executes after CloudFront receives a response from the origin and before it caches the object in the response. When the requested object is in the edge cache, the function doesn\'t execute.
viewer-response : The function executes before CloudFront returns the requested object to the viewer. The function executes regardless of whether the object was already in the edge cache. If the origin returns an HTTP status code other than HTTP 200 (OK), the function doesn\'t execute.


IncludeBody (boolean) --A flag that allows a Lambda function to have read access to the body content. For more information, see Accessing the Request Body by Choosing the Include Body Option in the Amazon CloudFront Developer Guide.







FieldLevelEncryptionId (string) --The value of ID for the field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data for a cache behavior or for the default cache behavior in your distribution.







CustomErrorResponses (dict) --A complex type that controls the following:

Whether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.
How long CloudFront caches HTTP status codes in the 4xx and 5xx range.

For more information about custom error pages, see Customizing Error Responses in the Amazon CloudFront Developer Guide .

Quantity (integer) --The number of HTTP status codes for which you want to specify a custom error page and/or a caching duration. If Quantity is 0 , you can omit Items .

Items (list) --A complex type that contains a CustomErrorResponse element for each HTTP status code for which you want to specify a custom error page and/or a caching duration.

(dict) --A complex type that controls:

Whether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.
How long CloudFront caches HTTP status codes in the 4xx and 5xx range.

For more information about custom error pages, see Customizing Error Responses in the Amazon CloudFront Developer Guide .

ErrorCode (integer) --The HTTP status code for which you want to specify a custom error page and/or a caching duration.

ResponsePagePath (string) --The path to the custom error page that you want CloudFront to return to a viewer when your origin returns the HTTP status code specified by ErrorCode , for example, /4xx-errors/403-forbidden.html . If you want to store your objects and your custom error pages in different locations, your distribution must include a cache behavior for which the following is true:

The value of PathPattern matches the path to your custom error messages. For example, suppose you saved custom error pages for 4xx errors in an Amazon S3 bucket in a directory named /4xx-errors . Your distribution must include a cache behavior for which the path pattern routes requests for your custom error pages to that location, for example, /4xx-errors/* .
The value of TargetOriginId specifies the value of the ID element for the origin that contains your custom error pages.

If you specify a value for ResponsePagePath , you must also specify a value for ResponseCode .
We recommend that you store custom error pages in an Amazon S3 bucket. If you store custom error pages on an HTTP server and the server starts to return 5xx errors, CloudFront can\'t get the files that you want to return to viewers because the origin server is unavailable.

ResponseCode (string) --The HTTP status code that you want CloudFront to return to the viewer along with the custom error page. There are a variety of reasons that you might want CloudFront to return a status code different from the status code that your origin returned to CloudFront, for example:

Some Internet devices (some firewalls and corporate proxies, for example) intercept HTTP 4xx and 5xx and prevent the response from being returned to the viewer. If you substitute 200 , the response typically won\'t be intercepted.
If you don\'t care about distinguishing among different client errors or server errors, you can specify 400 or 500 as the ResponseCode for all 4xx or 5xx errors.
You might want to return a 200 status code (OK) and static website so your customers don\'t know that your website is down.

If you specify a value for ResponseCode , you must also specify a value for ResponsePagePath .

ErrorCachingMinTTL (integer) --The minimum amount of time, in seconds, that you want CloudFront to cache the HTTP status code specified in ErrorCode . When this time period has elapsed, CloudFront queries your origin to see whether the problem that caused the error has been resolved and the requested object is now available.
For more information, see Customizing Error Responses in the Amazon CloudFront Developer Guide .







Comment (string) --Any comments you want to include about the distribution.
If you don\'t want to specify a comment, include an empty Comment element.
To delete an existing comment, update the distribution configuration and include an empty Comment element.
To add or change a comment, update the distribution configuration and specify the new comment.

Logging (dict) --A complex type that controls whether access logs are written for the distribution.
For more information about logging, see Access Logs in the Amazon CloudFront Developer Guide .

Enabled (boolean) --Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you don\'t want to enable logging when you create a distribution or if you want to disable logging for an existing distribution, specify false for Enabled , and specify empty Bucket and Prefix elements. If you specify false for Enabled but you specify values for Bucket , prefix , and IncludeCookies , the values are automatically deleted.

IncludeCookies (boolean) --Specifies whether you want CloudFront to include cookies in access logs, specify true for IncludeCookies . If you choose to include cookies in logs, CloudFront logs all cookies regardless of how you configure the cache behaviors for this distribution. If you don\'t want to include cookies when you create a distribution or if you want to disable include cookies for an existing distribution, specify false for IncludeCookies .

Bucket (string) --The Amazon S3 bucket to store the access logs in, for example, myawslogbucket.s3.amazonaws.com .

Prefix (string) --An optional string that you want CloudFront to prefix to the access log filenames for this distribution, for example, myprefix/ . If you want to enable logging, but you don\'t want to specify a prefix, you still must include an empty Prefix element in the Logging element.



PriceClass (string) --The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify PriceClass_All , CloudFront responds to requests for your objects from all CloudFront edge locations.
If you specify a price class other than PriceClass_All , CloudFront serves your objects from the CloudFront edge location that has the lowest latency among the edge locations in your price class. Viewers who are in or near regions that are excluded from your specified price class may encounter slower performance.
For more information about price classes, see Choosing the Price Class for a CloudFront Distribution in the Amazon CloudFront Developer Guide . For information about CloudFront pricing, including how price classes (such as Price Class 100) map to CloudFront regions, see Amazon CloudFront Pricing . For price class information, scroll down to see the table at the bottom of the page.

Enabled (boolean) --From this field, you can enable or disable the selected distribution.

ViewerCertificate (dict) --A complex type that determines the distribution\xe2\x80\x99s SSL/TLS configuration for communicating with viewers.

CloudFrontDefaultCertificate (boolean) --If the distribution uses the CloudFront domain name such as d111111abcdef8.cloudfront.net , set this field to true .
If the distribution uses Aliases (alternate domain names or CNAMEs), set this field to false and specify values for the following fields:

ACMCertificateArn or IAMCertificateId (specify a value for one, not both)
MinimumProtocolVersion
SSLSupportMethod


IAMCertificateId (string) --If the distribution uses Aliases (alternate domain names or CNAMEs) and the SSL/TLS certificate is stored in AWS Identity and Access Management (AWS IAM) , provide the ID of the IAM certificate.
If you specify an IAM certificate ID, you must also specify values for MinimumProtocolVerison and SSLSupportMethod .

ACMCertificateArn (string) --If the distribution uses Aliases (alternate domain names or CNAMEs) and the SSL/TLS certificate is stored in AWS Certificate Manager (ACM) , provide the Amazon Resource Name (ARN) of the ACM certificate. CloudFront only supports ACM certificates in the US East (N. Virginia) Region (us-east-1 ).
If you specify an ACM certificate ARN, you must also specify values for MinimumProtocolVerison and SSLSupportMethod .

SSLSupportMethod (string) --If the distribution uses Aliases (alternate domain names or CNAMEs), specify which viewers the distribution accepts HTTPS connections from.

sni-only \xe2\x80\x93 The distribution accepts HTTPS connections from only viewers that support server name indication (SNI) . This is recommended. Most browsers and clients released after 2010 support SNI.
vip \xe2\x80\x93 The distribution accepts HTTPS connections from all viewers including those that don\xe2\x80\x99t support SNI. This is not recommended, and results in additional monthly charges from CloudFront.

If the distribution uses the CloudFront domain name such as d111111abcdef8.cloudfront.net , don\xe2\x80\x99t set a value for this field.

MinimumProtocolVersion (string) --If the distribution uses Aliases (alternate domain names or CNAMEs), specify the security policy that you want CloudFront to use for HTTPS connections with viewers. The security policy determines two settings:

The minimum SSL/TLS protocol that CloudFront can use to communicate with viewers.
The ciphers that CloudFront can use to encrypt the content that it returns to viewers.

For more information, see Security Policy and Supported Protocols and Ciphers Between Viewers and CloudFront in the Amazon CloudFront Developer Guide .

Note
On the CloudFront console, this setting is called Security Policy .

We recommend that you specify TLSv1.2_2018 unless your viewers are using browsers or devices that don\xe2\x80\x99t support TLSv1.2.
When you\xe2\x80\x99re using SNI only (you set SSLSupportMethod to sni-only ), you must specify TLSv1 or higher.
If the distribution uses the CloudFront domain name such as d111111abcdef8.cloudfront.net (you set CloudFrontDefaultCertificate to true ), CloudFront automatically sets the security policy to TLSv1 regardless of the value that you set here.

Certificate (string) --This field is deprecated. Use one of the following fields instead:

ACMCertificateArn
IAMCertificateId
CloudFrontDefaultCertificate


CertificateSource (string) --This field is deprecated. Use one of the following fields instead:

ACMCertificateArn
IAMCertificateId
CloudFrontDefaultCertificate




Restrictions (dict) --A complex type that identifies ways in which you want to restrict distribution of your content.

GeoRestriction (dict) --A complex type that controls the countries in which your content is distributed. CloudFront determines the location of your users using MaxMind GeoIP databases.

RestrictionType (string) --The method that you want to use to restrict distribution of your content by country:

none : No geo restriction is enabled, meaning access to content is not restricted by client geo location.
blacklist : The Location elements specify the countries in which you don\'t want CloudFront to distribute your content.
whitelist : The Location elements specify the countries in which you want CloudFront to distribute your content.


Quantity (integer) --When geo restriction is enabled , this is the number of countries in your whitelist or blacklist . Otherwise, when it is not enabled, Quantity is 0 , and you can omit Items .

Items (list) --A complex type that contains a Location element for each country in which you want CloudFront either to distribute your content (whitelist ) or not distribute your content (blacklist ).
The Location element is a two-letter, uppercase country code for a country that you want to include in your blacklist or whitelist . Include one Location element for each country.
CloudFront and MaxMind both use ISO 3166 country codes. For the current list of countries and the corresponding codes, see ISO 3166-1-alpha-2 code on the International Organization for Standardization website. You can also refer to the country list on the CloudFront console, which includes both country names and codes.

(string) --






WebACLId (string) --A unique identifier that specifies the AWS WAF web ACL, if any, to associate with this distribution. To specify a web ACL created using the latest version of AWS WAF, use the ACL ARN, for example arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/473e64fd-f30b-4765-81a0-62ad96dd167a . To specify a web ACL created using AWS WAF Classic, use the ACL ID, for example 473e64fd-f30b-4765-81a0-62ad96dd167a .
AWS WAF is a web application firewall that lets you monitor the HTTP and HTTPS requests that are forwarded to CloudFront, and lets you control access to your content. Based on conditions that you specify, such as the IP addresses that requests originate from or the values of query strings, CloudFront responds to requests either with the requested content or with an HTTP 403 status code (Forbidden). You can also configure CloudFront to return a custom error page when a request is blocked. For more information about AWS WAF, see the AWS WAF Developer Guide .

HttpVersion (string) --(Optional) Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront. The default value for new web distributions is http2. Viewers that don\'t support HTTP/2 automatically use an earlier HTTP version.
For viewers and CloudFront to use HTTP/2, viewers must support TLS 1.2 or later, and must support Server Name Identification (SNI).
In general, configuring CloudFront to communicate with viewers using HTTP/2 reduces latency. You can improve performance by optimizing for HTTP/2. For more information, do an Internet search for "http/2 optimization."

IsIPV6Enabled (boolean) --If you want CloudFront to respond to IPv6 DNS requests with an IPv6 address for your distribution, specify true . If you specify false , CloudFront responds to IPv6 DNS requests with the DNS response code NOERROR and with no IP addresses. This allows viewers to submit a second request, for an IPv4 address for your distribution.
In general, you should enable IPv6 if you have users on IPv6 networks who want to access your content. However, if you\'re using signed URLs or signed cookies to restrict access to your content, and if you\'re using a custom policy that includes the IpAddress parameter to restrict the IP addresses that can access your content, don\'t enable IPv6. If you want to restrict access to some content by IP address and not restrict access to other content (or restrict access but not by IP address), you can create two distributions. For more information, see Creating a Signed URL Using a Custom Policy in the Amazon CloudFront Developer Guide .
If you\'re using an Amazon Route 53 alias resource record set to route traffic to your CloudFront distribution, you need to create a second alias resource record set when both of the following are true:

You enable IPv6 for the distribution
You\'re using alternate domain names in the URLs for your objects

For more information, see Routing Traffic to an Amazon CloudFront Web Distribution by Using Your Domain Name in the Amazon Route 53 Developer Guide .
If you created a CNAME resource record set, either with Amazon Route 53 or with another DNS service, you don\'t need to make any changes. A CNAME record will route traffic to your distribution regardless of the IP address format of the viewer request.



AliasICPRecordals (list) --AWS services in China customers must file for an Internet Content Provider (ICP) recordal if they want to serve content publicly on an alternate domain name, also known as a CNAME, that they\'ve added to CloudFront. AliasICPRecordal provides the ICP recordal status for CNAMEs associated with distributions.
For more information about ICP recordals, see Signup, Accounts, and Credentials in Getting Started with AWS services in China .

(dict) --AWS services in China customers must file for an Internet Content Provider (ICP) recordal if they want to serve content publicly on an alternate domain name, also known as a CNAME, that they\'ve added to CloudFront. AliasICPRecordal provides the ICP recordal status for CNAMEs associated with distributions. The status is returned in the CloudFront response; you can\'t configure it yourself.
For more information about ICP recordals, see Signup, Accounts, and Credentials in Getting Started with AWS services in China .

CNAME (string) --A domain name associated with a distribution.

ICPRecordalStatus (string) --The Internet Content Provider (ICP) recordal status for a CNAME. The ICPRecordalStatus is set to APPROVED for all CNAMEs (aliases) in regions outside of China.
The status values returned are the following:

APPROVED indicates that the associated CNAME has a valid ICP recordal number. Multiple CNAMEs can be associated with a distribution, and CNAMEs can correspond to different ICP recordals. To be marked as APPROVED, that is, valid to use with China region, a CNAME must have one ICP recordal number associated with it.
SUSPENDED indicates that the associated CNAME does not have a valid ICP recordal number.
PENDING indicates that CloudFront can\'t determine the ICP recordal status of the CNAME associated with the distribution because there was an error in trying to determine the status. You can try again to see if the error is resolved in which case CloudFront returns an APPROVED or SUSPENDED status.








Location (string) --The fully qualified URI of the new distribution resource just created. For example: https://cloudfront.amazonaws.com/2010-11-01/distribution/EDFDVBD632BHDS5 .

ETag (string) --The current version of the distribution created.






Exceptions

CloudFront.Client.exceptions.CNAMEAlreadyExists
CloudFront.Client.exceptions.DistributionAlreadyExists
CloudFront.Client.exceptions.InvalidOrigin
CloudFront.Client.exceptions.InvalidOriginAccessIdentity
CloudFront.Client.exceptions.AccessDenied
CloudFront.Client.exceptions.TooManyTrustedSigners
CloudFront.Client.exceptions.TrustedSignerDoesNotExist
CloudFront.Client.exceptions.InvalidViewerCertificate
CloudFront.Client.exceptions.InvalidMinimumProtocolVersion
CloudFront.Client.exceptions.MissingBody
CloudFront.Client.exceptions.TooManyDistributionCNAMEs
CloudFront.Client.exceptions.TooManyDistributions
CloudFront.Client.exceptions.InvalidDefaultRootObject
CloudFront.Client.exceptions.InvalidRelativePath
CloudFront.Client.exceptions.InvalidErrorCode
CloudFront.Client.exceptions.InvalidResponseCode
CloudFront.Client.exceptions.InvalidArgument
CloudFront.Client.exceptions.InvalidRequiredProtocol
CloudFront.Client.exceptions.NoSuchOrigin
CloudFront.Client.exceptions.TooManyOrigins
CloudFront.Client.exceptions.TooManyOriginGroupsPerDistribution
CloudFront.Client.exceptions.TooManyCacheBehaviors
CloudFront.Client.exceptions.TooManyCookieNamesInWhiteList
CloudFront.Client.exceptions.InvalidForwardCookies
CloudFront.Client.exceptions.TooManyHeadersInForwardedValues
CloudFront.Client.exceptions.InvalidHeadersForS3Origin
CloudFront.Client.exceptions.InconsistentQuantities
CloudFront.Client.exceptions.TooManyCertificates
CloudFront.Client.exceptions.InvalidLocationCode
CloudFront.Client.exceptions.InvalidGeoRestrictionParameter
CloudFront.Client.exceptions.InvalidProtocolSettings
CloudFront.Client.exceptions.InvalidTTLOrder
CloudFront.Client.exceptions.InvalidWebACLId
CloudFront.Client.exceptions.TooManyOriginCustomHeaders
CloudFront.Client.exceptions.TooManyQueryStringParameters
CloudFront.Client.exceptions.InvalidQueryStringParameters
CloudFront.Client.exceptions.TooManyDistributionsWithLambdaAssociations
CloudFront.Client.exceptions.TooManyLambdaFunctionAssociations
CloudFront.Client.exceptions.InvalidLambdaFunctionAssociation
CloudFront.Client.exceptions.InvalidOriginReadTimeout
CloudFront.Client.exceptions.InvalidOriginKeepaliveTimeout
CloudFront.Client.exceptions.NoSuchFieldLevelEncryptionConfig
CloudFront.Client.exceptions.IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior
CloudFront.Client.exceptions.TooManyDistributionsAssociatedToFieldLevelEncryptionConfig


    :return: {
        'Distribution': {
            'Id': 'string',
            'ARN': 'string',
            'Status': 'string',
            'LastModifiedTime': datetime(2015, 1, 1),
            'InProgressInvalidationBatches': 123,
            'DomainName': 'string',
            'ActiveTrustedSigners': {
                'Enabled': True|False,
                'Quantity': 123,
                'Items': [
                    {
                        'AwsAccountNumber': 'string',
                        'KeyPairIds': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                ]
            },
            'DistributionConfig': {
                'CallerReference': 'string',
                'Aliases': {
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'DefaultRootObject': 'string',
                'Origins': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'Id': 'string',
                            'DomainName': 'string',
                            'OriginPath': 'string',
                            'CustomHeaders': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'HeaderName': 'string',
                                        'HeaderValue': 'string'
                                    },
                                ]
                            },
                            'S3OriginConfig': {
                                'OriginAccessIdentity': 'string'
                            },
                            'CustomOriginConfig': {
                                'HTTPPort': 123,
                                'HTTPSPort': 123,
                                'OriginProtocolPolicy': 'http-only'|'match-viewer'|'https-only',
                                'OriginSslProtocols': {
                                    'Quantity': 123,
                                    'Items': [
                                        'SSLv3'|'TLSv1'|'TLSv1.1'|'TLSv1.2',
                                    ]
                                },
                                'OriginReadTimeout': 123,
                                'OriginKeepaliveTimeout': 123
                            }
                        },
                    ]
                },
                'OriginGroups': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'Id': 'string',
                            'FailoverCriteria': {
                                'StatusCodes': {
                                    'Quantity': 123,
                                    'Items': [
                                        123,
                                    ]
                                }
                            },
                            'Members': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'OriginId': 'string'
                                    },
                                ]
                            }
                        },
                    ]
                },
                'DefaultCacheBehavior': {
                    'TargetOriginId': 'string',
                    'ForwardedValues': {
                        'QueryString': True|False,
                        'Cookies': {
                            'Forward': 'none'|'whitelist'|'all',
                            'WhitelistedNames': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                        'Headers': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        },
                        'QueryStringCacheKeys': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                    'TrustedSigners': {
                        'Enabled': True|False,
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    },
                    'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                    'MinTTL': 123,
                    'AllowedMethods': {
                        'Quantity': 123,
                        'Items': [
                            'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                        ],
                        'CachedMethods': {
                            'Quantity': 123,
                            'Items': [
                                'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                            ]
                        }
                    },
                    'SmoothStreaming': True|False,
                    'DefaultTTL': 123,
                    'MaxTTL': 123,
                    'Compress': True|False,
                    'LambdaFunctionAssociations': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'LambdaFunctionARN': 'string',
                                'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                'IncludeBody': True|False
                            },
                        ]
                    },
                    'FieldLevelEncryptionId': 'string'
                },
                'CacheBehaviors': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'PathPattern': 'string',
                            'TargetOriginId': 'string',
                            'ForwardedValues': {
                                'QueryString': True|False,
                                'Cookies': {
                                    'Forward': 'none'|'whitelist'|'all',
                                    'WhitelistedNames': {
                                        'Quantity': 123,
                                        'Items': [
                                            'string',
                                        ]
                                    }
                                },
                                'Headers': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                },
                                'QueryStringCacheKeys': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                }
                            },
                            'TrustedSigners': {
                                'Enabled': True|False,
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            },
                            'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                            'MinTTL': 123,
                            'AllowedMethods': {
                                'Quantity': 123,
                                'Items': [
                                    'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                ],
                                'CachedMethods': {
                                    'Quantity': 123,
                                    'Items': [
                                        'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                    ]
                                }
                            },
                            'SmoothStreaming': True|False,
                            'DefaultTTL': 123,
                            'MaxTTL': 123,
                            'Compress': True|False,
                            'LambdaFunctionAssociations': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'LambdaFunctionARN': 'string',
                                        'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                        'IncludeBody': True|False
                                    },
                                ]
                            },
                            'FieldLevelEncryptionId': 'string'
                        },
                    ]
                },
                'CustomErrorResponses': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'ErrorCode': 123,
                            'ResponsePagePath': 'string',
                            'ResponseCode': 'string',
                            'ErrorCachingMinTTL': 123
                        },
                    ]
                },
                'Comment': 'string',
                'Logging': {
                    'Enabled': True|False,
                    'IncludeCookies': True|False,
                    'Bucket': 'string',
                    'Prefix': 'string'
                },
                'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
                'Enabled': True|False,
                'ViewerCertificate': {
                    'CloudFrontDefaultCertificate': True|False,
                    'IAMCertificateId': 'string',
                    'ACMCertificateArn': 'string',
                    'SSLSupportMethod': 'sni-only'|'vip',
                    'MinimumProtocolVersion': 'SSLv3'|'TLSv1'|'TLSv1_2016'|'TLSv1.1_2016'|'TLSv1.2_2018',
                    'Certificate': 'string',
                    'CertificateSource': 'cloudfront'|'iam'|'acm'
                },
                'Restrictions': {
                    'GeoRestriction': {
                        'RestrictionType': 'blacklist'|'whitelist'|'none',
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    }
                },
                'WebACLId': 'string',
                'HttpVersion': 'http1.1'|'http2',
                'IsIPV6Enabled': True|False
            },
            'AliasICPRecordals': [
                {
                    'CNAME': 'string',
                    'ICPRecordalStatus': 'APPROVED'|'SUSPENDED'|'PENDING'
                },
            ]
        },
        'Location': 'string',
        'ETag': 'string'
    }
    
    
    :returns: 
    If you configured Amazon S3 Transfer Acceleration for your bucket, don\'t specify the s3-accelerate endpoint for DomainName .
    The bucket name must be between 3 and 63 characters long (inclusive).
    The bucket name must contain only lowercase characters, numbers, periods, underscores, and dashes.
    The bucket name must not contain adjacent periods.
    
    """
    pass

def create_distribution_with_tags(DistributionConfigWithTags=None):
    """
    Create a new distribution with tags.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_distribution_with_tags(
        DistributionConfigWithTags={
            'DistributionConfig': {
                'CallerReference': 'string',
                'Aliases': {
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'DefaultRootObject': 'string',
                'Origins': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'Id': 'string',
                            'DomainName': 'string',
                            'OriginPath': 'string',
                            'CustomHeaders': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'HeaderName': 'string',
                                        'HeaderValue': 'string'
                                    },
                                ]
                            },
                            'S3OriginConfig': {
                                'OriginAccessIdentity': 'string'
                            },
                            'CustomOriginConfig': {
                                'HTTPPort': 123,
                                'HTTPSPort': 123,
                                'OriginProtocolPolicy': 'http-only'|'match-viewer'|'https-only',
                                'OriginSslProtocols': {
                                    'Quantity': 123,
                                    'Items': [
                                        'SSLv3'|'TLSv1'|'TLSv1.1'|'TLSv1.2',
                                    ]
                                },
                                'OriginReadTimeout': 123,
                                'OriginKeepaliveTimeout': 123
                            }
                        },
                    ]
                },
                'OriginGroups': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'Id': 'string',
                            'FailoverCriteria': {
                                'StatusCodes': {
                                    'Quantity': 123,
                                    'Items': [
                                        123,
                                    ]
                                }
                            },
                            'Members': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'OriginId': 'string'
                                    },
                                ]
                            }
                        },
                    ]
                },
                'DefaultCacheBehavior': {
                    'TargetOriginId': 'string',
                    'ForwardedValues': {
                        'QueryString': True|False,
                        'Cookies': {
                            'Forward': 'none'|'whitelist'|'all',
                            'WhitelistedNames': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                        'Headers': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        },
                        'QueryStringCacheKeys': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                    'TrustedSigners': {
                        'Enabled': True|False,
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    },
                    'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                    'MinTTL': 123,
                    'AllowedMethods': {
                        'Quantity': 123,
                        'Items': [
                            'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                        ],
                        'CachedMethods': {
                            'Quantity': 123,
                            'Items': [
                                'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                            ]
                        }
                    },
                    'SmoothStreaming': True|False,
                    'DefaultTTL': 123,
                    'MaxTTL': 123,
                    'Compress': True|False,
                    'LambdaFunctionAssociations': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'LambdaFunctionARN': 'string',
                                'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                'IncludeBody': True|False
                            },
                        ]
                    },
                    'FieldLevelEncryptionId': 'string'
                },
                'CacheBehaviors': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'PathPattern': 'string',
                            'TargetOriginId': 'string',
                            'ForwardedValues': {
                                'QueryString': True|False,
                                'Cookies': {
                                    'Forward': 'none'|'whitelist'|'all',
                                    'WhitelistedNames': {
                                        'Quantity': 123,
                                        'Items': [
                                            'string',
                                        ]
                                    }
                                },
                                'Headers': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                },
                                'QueryStringCacheKeys': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                }
                            },
                            'TrustedSigners': {
                                'Enabled': True|False,
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            },
                            'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                            'MinTTL': 123,
                            'AllowedMethods': {
                                'Quantity': 123,
                                'Items': [
                                    'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                ],
                                'CachedMethods': {
                                    'Quantity': 123,
                                    'Items': [
                                        'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                    ]
                                }
                            },
                            'SmoothStreaming': True|False,
                            'DefaultTTL': 123,
                            'MaxTTL': 123,
                            'Compress': True|False,
                            'LambdaFunctionAssociations': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'LambdaFunctionARN': 'string',
                                        'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                        'IncludeBody': True|False
                                    },
                                ]
                            },
                            'FieldLevelEncryptionId': 'string'
                        },
                    ]
                },
                'CustomErrorResponses': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'ErrorCode': 123,
                            'ResponsePagePath': 'string',
                            'ResponseCode': 'string',
                            'ErrorCachingMinTTL': 123
                        },
                    ]
                },
                'Comment': 'string',
                'Logging': {
                    'Enabled': True|False,
                    'IncludeCookies': True|False,
                    'Bucket': 'string',
                    'Prefix': 'string'
                },
                'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
                'Enabled': True|False,
                'ViewerCertificate': {
                    'CloudFrontDefaultCertificate': True|False,
                    'IAMCertificateId': 'string',
                    'ACMCertificateArn': 'string',
                    'SSLSupportMethod': 'sni-only'|'vip',
                    'MinimumProtocolVersion': 'SSLv3'|'TLSv1'|'TLSv1_2016'|'TLSv1.1_2016'|'TLSv1.2_2018',
                    'Certificate': 'string',
                    'CertificateSource': 'cloudfront'|'iam'|'acm'
                },
                'Restrictions': {
                    'GeoRestriction': {
                        'RestrictionType': 'blacklist'|'whitelist'|'none',
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    }
                },
                'WebACLId': 'string',
                'HttpVersion': 'http1.1'|'http2',
                'IsIPV6Enabled': True|False
            },
            'Tags': {
                'Items': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
        }
    )
    
    
    :type DistributionConfigWithTags: dict
    :param DistributionConfigWithTags: [REQUIRED]\nThe distribution\'s configuration information.\n\nDistributionConfig (dict) -- [REQUIRED]A distribution configuration.\n\nCallerReference (string) -- [REQUIRED]A unique value (for example, a date-time stamp) that ensures that the request can\'t be replayed.\nIf the value of CallerReference is new (regardless of the content of the DistributionConfig object), CloudFront creates a new distribution.\nIf CallerReference is a value that you already sent in a previous request to create a distribution, CloudFront returns a DistributionAlreadyExists error.\n\nAliases (dict) --A complex type that contains information about CNAMEs (alternate domain names), if any, for this distribution.\n\nQuantity (integer) -- [REQUIRED]The number of CNAME aliases, if any, that you want to associate with this distribution.\n\nItems (list) --A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.\n\n(string) --\n\n\n\n\nDefaultRootObject (string) --The object that you want CloudFront to request from your origin (for example, index.html ) when a viewer requests the root URL for your distribution (http://www.example.com ) instead of an object in your distribution (http://www.example.com/product-description.html ). Specifying a default root object avoids exposing the contents of your distribution.\nSpecify only the object name, for example, index.html . Don\'t add a / before the object name.\nIf you don\'t want to specify a default root object when you create a distribution, include an empty DefaultRootObject element.\nTo delete the default root object from an existing distribution, update the distribution configuration and include an empty DefaultRootObject element.\nTo replace the default root object, update the distribution configuration and specify the new object.\nFor more information about the default root object, see Creating a Default Root Object in the Amazon CloudFront Developer Guide .\n\nOrigins (dict) -- [REQUIRED]A complex type that contains information about origins for this distribution.\n\nQuantity (integer) -- [REQUIRED]The number of origins or origin groups for this distribution.\n\nItems (list) -- [REQUIRED]A complex type that contains origins or origin groups for this distribution.\n\n(dict) --A complex type that describes the Amazon S3 bucket, HTTP server (for example, a web server), Amazon MediaStore, or other server from which CloudFront gets your files. This can also be an origin group, if you\'ve created an origin group. You must specify at least one origin or origin group.\nFor the current limit on the number of origins or origin groups that you can specify for a distribution, see Amazon CloudFront Limits in the AWS General Reference .\n\nId (string) -- [REQUIRED]A unique identifier for the origin or origin group. The value of Id must be unique within the distribution.\nWhen you specify the value of TargetOriginId for the default cache behavior or for another cache behavior, you indicate the origin to which you want the cache behavior to route requests by specifying the value of the Id element for that origin. When a request matches the path pattern for that cache behavior, CloudFront routes the request to the specified origin. For more information, see Cache Behavior Settings in the Amazon CloudFront Developer Guide .\n\nDomainName (string) -- [REQUIRED]\nAmazon S3 origins : The DNS name of the Amazon S3 bucket from which you want CloudFront to get objects for this origin, for example, myawsbucket.s3.amazonaws.com . If you set up your bucket to be configured as a website endpoint, enter the Amazon S3 static website hosting endpoint for the bucket.\nFor more information about specifying this value for different types of origins, see Origin Domain Name in the Amazon CloudFront Developer Guide .\nConstraints for Amazon S3 origins:\n\nIf you configured Amazon S3 Transfer Acceleration for your bucket, don\'t specify the s3-accelerate endpoint for DomainName .\nThe bucket name must be between 3 and 63 characters long (inclusive).\nThe bucket name must contain only lowercase characters, numbers, periods, underscores, and dashes.\nThe bucket name must not contain adjacent periods.\n\n\nCustom Origins : The DNS domain name for the HTTP server from which you want CloudFront to get objects for this origin, for example, www.example.com .\nConstraints for custom origins:\n\nDomainName must be a valid DNS name that contains only a-z, A-Z, 0-9, dot (.), hyphen (-), or underscore (_) characters.\nThe name cannot exceed 128 characters.\n\n\nOriginPath (string) --An optional element that causes CloudFront to request your content from a directory in your Amazon S3 bucket or your custom origin. When you include the OriginPath element, specify the directory name, beginning with a / . CloudFront appends the directory name to the value of DomainName , for example, example.com/production . Do not include a / at the end of the directory name.\nFor example, suppose you\'ve specified the following values for your distribution:\n\nDomainName : An Amazon S3 bucket named myawsbucket .\nOriginPath : /production\nCNAME : example.com\n\nWhen a user enters example.com/index.html in a browser, CloudFront sends a request to Amazon S3 for myawsbucket/production/index.html .\nWhen a user enters example.com/acme/index.html in a browser, CloudFront sends a request to Amazon S3 for myawsbucket/production/acme/index.html .\n\nCustomHeaders (dict) --A complex type that contains names and values for the custom headers that you want.\n\nQuantity (integer) -- [REQUIRED]The number of custom headers, if any, for this distribution.\n\nItems (list) --\nOptional : A list that contains one OriginCustomHeader element for each custom header that you want CloudFront to forward to the origin. If Quantity is 0 , omit Items .\n\n(dict) --A complex type that contains HeaderName and HeaderValue elements, if any, for this distribution.\n\nHeaderName (string) -- [REQUIRED]The name of a header that you want CloudFront to forward to your origin. For more information, see Forwarding Custom Headers to Your Origin (Web Distributions Only) in the Amazon CloudFront Developer Guide .\n\nHeaderValue (string) -- [REQUIRED]The value for the header that you specified in the HeaderName field.\n\n\n\n\n\n\n\nS3OriginConfig (dict) --A complex type that contains information about the Amazon S3 origin. If the origin is a custom origin, use the CustomOriginConfig element instead.\n\nOriginAccessIdentity (string) -- [REQUIRED]The CloudFront origin access identity to associate with the origin. Use an origin access identity to configure the origin so that viewers can only access objects in an Amazon S3 bucket through CloudFront. The format of the value is:\norigin-access-identity/cloudfront/ID-of-origin-access-identity\nwhere `` ID-of-origin-access-identity `` is the value that CloudFront returned in the ID element when you created the origin access identity.\nIf you want viewers to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty OriginAccessIdentity element.\nTo delete the origin access identity from an existing distribution, update the distribution configuration and include an empty OriginAccessIdentity element.\nTo replace the origin access identity, update the distribution configuration and specify the new origin access identity.\nFor more information about the origin access identity, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .\n\n\n\nCustomOriginConfig (dict) --A complex type that contains information about a custom origin. If the origin is an Amazon S3 bucket, use the S3OriginConfig element instead.\n\nHTTPPort (integer) -- [REQUIRED]The HTTP port the custom origin listens on.\n\nHTTPSPort (integer) -- [REQUIRED]The HTTPS port the custom origin listens on.\n\nOriginProtocolPolicy (string) -- [REQUIRED]The origin protocol policy to apply to your origin.\n\nOriginSslProtocols (dict) --The SSL/TLS protocols that you want CloudFront to use when communicating with your origin over HTTPS.\n\nQuantity (integer) -- [REQUIRED]The number of SSL/TLS protocols that you want to allow CloudFront to use when establishing an HTTPS connection with this origin.\n\nItems (list) -- [REQUIRED]A list that contains allowed SSL/TLS protocols for this distribution.\n\n(string) --\n\n\n\n\nOriginReadTimeout (integer) --You can create a custom origin read timeout. All timeout units are in seconds. The default origin read timeout is 30 seconds, but you can configure custom timeout lengths using the CloudFront API. The minimum timeout length is 4 seconds; the maximum is 60 seconds.\nIf you need to increase the maximum time limit, contact the AWS Support Center .\n\nOriginKeepaliveTimeout (integer) --You can create a custom keep-alive timeout. All timeout units are in seconds. The default keep-alive timeout is 5 seconds, but you can configure custom timeout lengths using the CloudFront API. The minimum timeout length is 1 second; the maximum is 60 seconds.\nIf you need to increase the maximum time limit, contact the AWS Support Center .\n\n\n\n\n\n\n\n\n\nOriginGroups (dict) --A complex type that contains information about origin groups for this distribution.\n\nQuantity (integer) -- [REQUIRED]The number of origin groups.\n\nItems (list) --The items (origin groups) in a distribution.\n\n(dict) --An origin group includes two origins (a primary origin and a second origin to failover to) and a failover criteria that you specify. You create an origin group to support origin failover in CloudFront. When you create or update a distribution, you can specifiy the origin group instead of a single origin, and CloudFront will failover from the primary origin to the second origin under the failover conditions that you\'ve chosen.\n\nId (string) -- [REQUIRED]The origin group\'s ID.\n\nFailoverCriteria (dict) -- [REQUIRED]A complex type that contains information about the failover criteria for an origin group.\n\nStatusCodes (dict) -- [REQUIRED]The status codes that, when returned from the primary origin, will trigger CloudFront to failover to the second origin.\n\nQuantity (integer) -- [REQUIRED]The number of status codes.\n\nItems (list) -- [REQUIRED]The items (status codes) for an origin group.\n\n(integer) --\n\n\n\n\n\n\nMembers (dict) -- [REQUIRED]A complex type that contains information about the origins in an origin group.\n\nQuantity (integer) -- [REQUIRED]The number of origins in an origin group.\n\nItems (list) -- [REQUIRED]Items (origins) in an origin group.\n\n(dict) --An origin in an origin group.\n\nOriginId (string) -- [REQUIRED]The ID for an origin in an origin group.\n\n\n\n\n\n\n\n\n\n\n\n\n\nDefaultCacheBehavior (dict) -- [REQUIRED]A complex type that describes the default cache behavior if you don\'t specify a CacheBehavior element or if files don\'t match any of the values of PathPattern in CacheBehavior elements. You must create exactly one default cache behavior.\n\nTargetOriginId (string) -- [REQUIRED]The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior in your distribution.\n\nForwardedValues (dict) -- [REQUIRED]A complex type that specifies how CloudFront handles query strings, cookies, and HTTP headers.\n\nQueryString (boolean) -- [REQUIRED]Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior and cache based on the query string parameters. CloudFront behavior depends on the value of QueryString and on the values that you specify for QueryStringCacheKeys , if any:\nIf you specify true for QueryString and you don\'t specify any values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin and caches based on all query string parameters. Depending on how many query string parameters and values you have, this can adversely affect performance because CloudFront must forward more requests to the origin.\nIf you specify true for QueryString and you specify one or more values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin, but it only caches based on the query string parameters that you specify.\nIf you specify false for QueryString , CloudFront doesn\'t forward any query string parameters to the origin, and doesn\'t cache based on query string parameters.\nFor more information, see Configuring CloudFront to Cache Based on Query String Parameters in the Amazon CloudFront Developer Guide .\n\nCookies (dict) -- [REQUIRED]A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see How CloudFront Forwards, Caches, and Logs Cookies in the Amazon CloudFront Developer Guide .\n\nForward (string) -- [REQUIRED]Specifies which cookies to forward to the origin for this cache behavior: all, none, or the list of cookies specified in the WhitelistedNames complex type.\nAmazon S3 doesn\'t process cookies. When the cache behavior is forwarding requests to an Amazon S3 origin, specify none for the Forward element.\n\nWhitelistedNames (dict) --Required if you specify whitelist for the value of Forward . A complex type that specifies how many different cookies you want CloudFront to forward to the origin for this cache behavior and, if you want to forward selected cookies, the names of those cookies.\nIf you specify all or none for the value of Forward , omit WhitelistedNames . If you change the value of Forward from whitelist to all or none and you don\'t delete the WhitelistedNames element and its child elements, CloudFront deletes them automatically.\nFor the current limit on the number of cookie names that you can whitelist for each cache behavior, see CloudFront Limits in the AWS General Reference .\n\nQuantity (integer) -- [REQUIRED]The number of different cookies that you want CloudFront to forward to the origin for this cache behavior. The value must equal the number of items that are in the Items field.\nWhen you set Forward = whitelist (in the CookiePreferences object), this value must be 1 or higher.\n\nItems (list) --A complex type that contains one Name element for each cookie that you want CloudFront to forward to the origin for this cache behavior. It must contain the same number of items that is specified in the Quantity field.\nWhen you set Forward = whitelist (in the CookiePreferences object), this field must contain at least one item.\n\n(string) --\n\n\n\n\n\n\nHeaders (dict) --A complex type that specifies the Headers , if any, that you want CloudFront to forward to the origin for this cache behavior (whitelisted headers). For the headers that you specify, CloudFront also caches separate versions of a specified object that is based on the header values in viewer requests.\nFor more information, see Caching Content Based on Request Headers in the Amazon CloudFront Developer Guide .\n\nQuantity (integer) -- [REQUIRED]The number of different headers that you want CloudFront to base caching on for this cache behavior. You can configure each cache behavior in a web distribution to do one of the following:\n\nForward all headers to your origin : Specify 1 for Quantity and * for Name .\n\n\nWarning\nCloudFront doesn\'t cache the objects that are associated with this cache behavior. Instead, CloudFront sends every request to the origin.\n\n\nForward a whitelist of headers you specify : Specify the number of headers that you want CloudFront to base caching on. Then specify the header names in Name elements. CloudFront caches your objects based on the values in the specified headers.\nForward only the default headers : Specify 0 for Quantity and omit Items . In this configuration, CloudFront doesn\'t cache based on the values in the request headers.\n\nRegardless of which option you choose, CloudFront forwards headers to your origin based on whether the origin is an S3 bucket or a custom origin. See the following documentation:\n\nS3 bucket : See HTTP Request Headers That CloudFront Removes or Updates\nCustom origin : See HTTP Request Headers and CloudFront Behavior\n\n\nItems (list) --A list that contains one Name element for each header that you want CloudFront to use for caching in this cache behavior. If Quantity is 0 , omit Items .\n\n(string) --\n\n\n\n\nQueryStringCacheKeys (dict) --A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.\n\nQuantity (integer) -- [REQUIRED]The number of whitelisted query string parameters for a cache behavior.\n\nItems (list) --A list that contains the query string parameters that you want CloudFront to use as a basis for caching for a cache behavior. If Quantity is 0, you can omit Items .\n\n(string) --\n\n\n\n\n\n\nTrustedSigners (dict) -- [REQUIRED]A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content.\nIf you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled , and specify the applicable values for Quantity and Items . For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .\nIf you don\'t want to require signed URLs in requests for objects that match PathPattern , specify false for Enabled and 0 for Quantity . Omit Items .\nTo add, change, or remove one or more trusted signers, change Enabled to true (if it\'s currently false ), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.\n\nEnabled (boolean) -- [REQUIRED]Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .\n\nQuantity (integer) -- [REQUIRED]The number of trusted signers for this cache behavior.\n\nItems (list) --\nOptional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .\n\n(string) --\n\n\n\n\nViewerProtocolPolicy (string) -- [REQUIRED]The protocol that viewers can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern . You can specify the following options:\n\nallow-all : Viewers can use HTTP or HTTPS.\nredirect-to-https : If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.\nhttps-only : If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).\n\nFor more information about requiring the HTTPS protocol, see Using an HTTPS Connection to Access Your Objects in the Amazon CloudFront Developer Guide .\n\nNote\nThe only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects\' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .\n\n\nMinTTL (integer) -- [REQUIRED]The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .\nYou must specify 0 for MinTTL if you configure CloudFront to forward all headers to your origin (under Headers , if you specify 1 for Quantity and * for Name ).\n\nAllowedMethods (dict) --A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices:\n\nCloudFront forwards only GET and HEAD requests.\nCloudFront forwards only GET , HEAD , and OPTIONS requests.\nCloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests.\n\nIf you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can\'t perform operations that you don\'t want them to. For example, you might not want users to have permissions to delete objects from your origin.\n\nQuantity (integer) -- [REQUIRED]The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET , HEAD , and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests).\n\nItems (list) -- [REQUIRED]A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.\n\n(string) --\n\n\nCachedMethods (dict) --A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices:\n\nCloudFront caches responses to GET and HEAD requests.\nCloudFront caches responses to GET , HEAD , and OPTIONS requests.\n\nIf you pick the second choice for your Amazon S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers, and Origin headers for the responses to be cached correctly.\n\nQuantity (integer) -- [REQUIRED]The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET , HEAD , and OPTIONS requests).\n\nItems (list) -- [REQUIRED]A complex type that contains the HTTP methods that you want CloudFront to cache responses to.\n\n(string) --\n\n\n\n\n\n\nSmoothStreaming (boolean) --Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true ; if not, specify false . If you specify true for SmoothStreaming , you can still distribute other content using this cache behavior if the content matches the value of PathPattern .\n\nDefaultTTL (integer) --The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .\n\nMaxTTL (integer) --The maximum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .\n\nCompress (boolean) --Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify true ; if not, specify false . For more information, see Serving Compressed Files in the Amazon CloudFront Developer Guide .\n\nLambdaFunctionAssociations (dict) --A complex type that contains zero or more Lambda function associations for a cache behavior.\n\nQuantity (integer) -- [REQUIRED]The number of Lambda function associations for this cache behavior.\n\nItems (list) --\nOptional : A complex type that contains LambdaFunctionAssociation items for this cache behavior. If Quantity is 0 , you can omit Items .\n\n(dict) --A complex type that contains a Lambda function association.\n\nLambdaFunctionARN (string) -- [REQUIRED]The ARN of the Lambda function. You must specify the ARN of a function version; you can\'t specify a Lambda alias or $LATEST.\n\nEventType (string) -- [REQUIRED]Specifies the event type that triggers a Lambda function invocation. You can specify the following values:\n\nviewer-request : The function executes when CloudFront receives a request from a viewer and before it checks to see whether the requested object is in the edge cache.\norigin-request : The function executes only when CloudFront forwards a request to your origin. When the requested object is in the edge cache, the function doesn\'t execute.\norigin-response : The function executes after CloudFront receives a response from the origin and before it caches the object in the response. When the requested object is in the edge cache, the function doesn\'t execute.\nviewer-response : The function executes before CloudFront returns the requested object to the viewer. The function executes regardless of whether the object was already in the edge cache. If the origin returns an HTTP status code other than HTTP 200 (OK), the function doesn\'t execute.\n\n\nIncludeBody (boolean) --A flag that allows a Lambda function to have read access to the body content. For more information, see Accessing the Request Body by Choosing the Include Body Option in the Amazon CloudFront Developer Guide.\n\n\n\n\n\n\n\nFieldLevelEncryptionId (string) --The value of ID for the field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data for a cache behavior or for the default cache behavior in your distribution.\n\n\n\nCacheBehaviors (dict) --A complex type that contains zero or more CacheBehavior elements.\n\nQuantity (integer) -- [REQUIRED]The number of cache behaviors for this distribution.\n\nItems (list) --Optional: A complex type that contains cache behaviors for this distribution. If Quantity is 0 , you can omit Items .\n\n(dict) --A complex type that describes how CloudFront processes requests.\nYou must create at least as many cache behaviors (including the default cache behavior) as you have origins if you want CloudFront to distribute objects from all of the origins. Each cache behavior specifies the one origin from which you want CloudFront to get objects. If you have two origins and only the default cache behavior, the default cache behavior will cause CloudFront to get objects from one of the origins, but the other origin is never used.\nFor the current limit on the number of cache behaviors that you can add to a distribution, see Amazon CloudFront Limits in the AWS General Reference .\nIf you don\'t want to specify any cache behaviors, include only an empty CacheBehaviors element. Don\'t include an empty CacheBehavior element, or CloudFront returns a MalformedXML error.\nTo delete all cache behaviors in an existing distribution, update the distribution configuration and include only an empty CacheBehaviors element.\nTo add, change, or remove one or more cache behaviors, update the distribution configuration and specify all of the cache behaviors that you want to include in the updated distribution.\nFor more information about cache behaviors, see Cache Behaviors in the Amazon CloudFront Developer Guide .\n\nPathPattern (string) -- [REQUIRED]The pattern (for example, images/*.jpg ) that specifies which requests to apply the behavior to. When CloudFront receives a viewer request, the requested path is compared with path patterns in the order in which cache behaviors are listed in the distribution.\n\nNote\nYou can optionally include a slash (/ ) at the beginning of the path pattern. For example, /images/*.jpg . CloudFront behavior is the same with or without the leading / .\n\nThe path pattern for the default cache behavior is * and cannot be changed. If the request for an object does not match the path pattern for any cache behaviors, CloudFront applies the behavior in the default cache behavior.\nFor more information, see Path Pattern in the Amazon CloudFront Developer Guide .\n\nTargetOriginId (string) -- [REQUIRED]The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior in your distribution.\n\nForwardedValues (dict) -- [REQUIRED]A complex type that specifies how CloudFront handles query strings, cookies, and HTTP headers.\n\nQueryString (boolean) -- [REQUIRED]Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior and cache based on the query string parameters. CloudFront behavior depends on the value of QueryString and on the values that you specify for QueryStringCacheKeys , if any:\nIf you specify true for QueryString and you don\'t specify any values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin and caches based on all query string parameters. Depending on how many query string parameters and values you have, this can adversely affect performance because CloudFront must forward more requests to the origin.\nIf you specify true for QueryString and you specify one or more values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin, but it only caches based on the query string parameters that you specify.\nIf you specify false for QueryString , CloudFront doesn\'t forward any query string parameters to the origin, and doesn\'t cache based on query string parameters.\nFor more information, see Configuring CloudFront to Cache Based on Query String Parameters in the Amazon CloudFront Developer Guide .\n\nCookies (dict) -- [REQUIRED]A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see How CloudFront Forwards, Caches, and Logs Cookies in the Amazon CloudFront Developer Guide .\n\nForward (string) -- [REQUIRED]Specifies which cookies to forward to the origin for this cache behavior: all, none, or the list of cookies specified in the WhitelistedNames complex type.\nAmazon S3 doesn\'t process cookies. When the cache behavior is forwarding requests to an Amazon S3 origin, specify none for the Forward element.\n\nWhitelistedNames (dict) --Required if you specify whitelist for the value of Forward . A complex type that specifies how many different cookies you want CloudFront to forward to the origin for this cache behavior and, if you want to forward selected cookies, the names of those cookies.\nIf you specify all or none for the value of Forward , omit WhitelistedNames . If you change the value of Forward from whitelist to all or none and you don\'t delete the WhitelistedNames element and its child elements, CloudFront deletes them automatically.\nFor the current limit on the number of cookie names that you can whitelist for each cache behavior, see CloudFront Limits in the AWS General Reference .\n\nQuantity (integer) -- [REQUIRED]The number of different cookies that you want CloudFront to forward to the origin for this cache behavior. The value must equal the number of items that are in the Items field.\nWhen you set Forward = whitelist (in the CookiePreferences object), this value must be 1 or higher.\n\nItems (list) --A complex type that contains one Name element for each cookie that you want CloudFront to forward to the origin for this cache behavior. It must contain the same number of items that is specified in the Quantity field.\nWhen you set Forward = whitelist (in the CookiePreferences object), this field must contain at least one item.\n\n(string) --\n\n\n\n\n\n\nHeaders (dict) --A complex type that specifies the Headers , if any, that you want CloudFront to forward to the origin for this cache behavior (whitelisted headers). For the headers that you specify, CloudFront also caches separate versions of a specified object that is based on the header values in viewer requests.\nFor more information, see Caching Content Based on Request Headers in the Amazon CloudFront Developer Guide .\n\nQuantity (integer) -- [REQUIRED]The number of different headers that you want CloudFront to base caching on for this cache behavior. You can configure each cache behavior in a web distribution to do one of the following:\n\nForward all headers to your origin : Specify 1 for Quantity and * for Name .\n\n\nWarning\nCloudFront doesn\'t cache the objects that are associated with this cache behavior. Instead, CloudFront sends every request to the origin.\n\n\nForward a whitelist of headers you specify : Specify the number of headers that you want CloudFront to base caching on. Then specify the header names in Name elements. CloudFront caches your objects based on the values in the specified headers.\nForward only the default headers : Specify 0 for Quantity and omit Items . In this configuration, CloudFront doesn\'t cache based on the values in the request headers.\n\nRegardless of which option you choose, CloudFront forwards headers to your origin based on whether the origin is an S3 bucket or a custom origin. See the following documentation:\n\nS3 bucket : See HTTP Request Headers That CloudFront Removes or Updates\nCustom origin : See HTTP Request Headers and CloudFront Behavior\n\n\nItems (list) --A list that contains one Name element for each header that you want CloudFront to use for caching in this cache behavior. If Quantity is 0 , omit Items .\n\n(string) --\n\n\n\n\nQueryStringCacheKeys (dict) --A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.\n\nQuantity (integer) -- [REQUIRED]The number of whitelisted query string parameters for a cache behavior.\n\nItems (list) --A list that contains the query string parameters that you want CloudFront to use as a basis for caching for a cache behavior. If Quantity is 0, you can omit Items .\n\n(string) --\n\n\n\n\n\n\nTrustedSigners (dict) -- [REQUIRED]A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content.\nIf you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled , and specify the applicable values for Quantity and Items . For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .\nIf you don\'t want to require signed URLs in requests for objects that match PathPattern , specify false for Enabled and 0 for Quantity . Omit Items .\nTo add, change, or remove one or more trusted signers, change Enabled to true (if it\'s currently false ), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.\n\nEnabled (boolean) -- [REQUIRED]Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .\n\nQuantity (integer) -- [REQUIRED]The number of trusted signers for this cache behavior.\n\nItems (list) --\nOptional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .\n\n(string) --\n\n\n\n\nViewerProtocolPolicy (string) -- [REQUIRED]The protocol that viewers can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern . You can specify the following options:\n\nallow-all : Viewers can use HTTP or HTTPS.\nredirect-to-https : If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.\nhttps-only : If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).\n\nFor more information about requiring the HTTPS protocol, see Using an HTTPS Connection to Access Your Objects in the Amazon CloudFront Developer Guide .\n\nNote\nThe only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects\' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .\n\n\nMinTTL (integer) -- [REQUIRED]The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .\nYou must specify 0 for MinTTL if you configure CloudFront to forward all headers to your origin (under Headers , if you specify 1 for Quantity and * for Name ).\n\nAllowedMethods (dict) --A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices:\n\nCloudFront forwards only GET and HEAD requests.\nCloudFront forwards only GET , HEAD , and OPTIONS requests.\nCloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests.\n\nIf you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can\'t perform operations that you don\'t want them to. For example, you might not want users to have permissions to delete objects from your origin.\n\nQuantity (integer) -- [REQUIRED]The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET , HEAD , and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests).\n\nItems (list) -- [REQUIRED]A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.\n\n(string) --\n\n\nCachedMethods (dict) --A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices:\n\nCloudFront caches responses to GET and HEAD requests.\nCloudFront caches responses to GET , HEAD , and OPTIONS requests.\n\nIf you pick the second choice for your Amazon S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers, and Origin headers for the responses to be cached correctly.\n\nQuantity (integer) -- [REQUIRED]The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET , HEAD , and OPTIONS requests).\n\nItems (list) -- [REQUIRED]A complex type that contains the HTTP methods that you want CloudFront to cache responses to.\n\n(string) --\n\n\n\n\n\n\nSmoothStreaming (boolean) --Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true ; if not, specify false . If you specify true for SmoothStreaming , you can still distribute other content using this cache behavior if the content matches the value of PathPattern .\n\nDefaultTTL (integer) --The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .\n\nMaxTTL (integer) --The maximum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .\n\nCompress (boolean) --Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify true; if not, specify false. For more information, see Serving Compressed Files in the Amazon CloudFront Developer Guide .\n\nLambdaFunctionAssociations (dict) --A complex type that contains zero or more Lambda function associations for a cache behavior.\n\nQuantity (integer) -- [REQUIRED]The number of Lambda function associations for this cache behavior.\n\nItems (list) --\nOptional : A complex type that contains LambdaFunctionAssociation items for this cache behavior. If Quantity is 0 , you can omit Items .\n\n(dict) --A complex type that contains a Lambda function association.\n\nLambdaFunctionARN (string) -- [REQUIRED]The ARN of the Lambda function. You must specify the ARN of a function version; you can\'t specify a Lambda alias or $LATEST.\n\nEventType (string) -- [REQUIRED]Specifies the event type that triggers a Lambda function invocation. You can specify the following values:\n\nviewer-request : The function executes when CloudFront receives a request from a viewer and before it checks to see whether the requested object is in the edge cache.\norigin-request : The function executes only when CloudFront forwards a request to your origin. When the requested object is in the edge cache, the function doesn\'t execute.\norigin-response : The function executes after CloudFront receives a response from the origin and before it caches the object in the response. When the requested object is in the edge cache, the function doesn\'t execute.\nviewer-response : The function executes before CloudFront returns the requested object to the viewer. The function executes regardless of whether the object was already in the edge cache. If the origin returns an HTTP status code other than HTTP 200 (OK), the function doesn\'t execute.\n\n\nIncludeBody (boolean) --A flag that allows a Lambda function to have read access to the body content. For more information, see Accessing the Request Body by Choosing the Include Body Option in the Amazon CloudFront Developer Guide.\n\n\n\n\n\n\n\nFieldLevelEncryptionId (string) --The value of ID for the field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data for a cache behavior or for the default cache behavior in your distribution.\n\n\n\n\n\n\n\nCustomErrorResponses (dict) --A complex type that controls the following:\n\nWhether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.\nHow long CloudFront caches HTTP status codes in the 4xx and 5xx range.\n\nFor more information about custom error pages, see Customizing Error Responses in the Amazon CloudFront Developer Guide .\n\nQuantity (integer) -- [REQUIRED]The number of HTTP status codes for which you want to specify a custom error page and/or a caching duration. If Quantity is 0 , you can omit Items .\n\nItems (list) --A complex type that contains a CustomErrorResponse element for each HTTP status code for which you want to specify a custom error page and/or a caching duration.\n\n(dict) --A complex type that controls:\n\nWhether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.\nHow long CloudFront caches HTTP status codes in the 4xx and 5xx range.\n\nFor more information about custom error pages, see Customizing Error Responses in the Amazon CloudFront Developer Guide .\n\nErrorCode (integer) -- [REQUIRED]The HTTP status code for which you want to specify a custom error page and/or a caching duration.\n\nResponsePagePath (string) --The path to the custom error page that you want CloudFront to return to a viewer when your origin returns the HTTP status code specified by ErrorCode , for example, /4xx-errors/403-forbidden.html . If you want to store your objects and your custom error pages in different locations, your distribution must include a cache behavior for which the following is true:\n\nThe value of PathPattern matches the path to your custom error messages. For example, suppose you saved custom error pages for 4xx errors in an Amazon S3 bucket in a directory named /4xx-errors . Your distribution must include a cache behavior for which the path pattern routes requests for your custom error pages to that location, for example, /4xx-errors/* .\nThe value of TargetOriginId specifies the value of the ID element for the origin that contains your custom error pages.\n\nIf you specify a value for ResponsePagePath , you must also specify a value for ResponseCode .\nWe recommend that you store custom error pages in an Amazon S3 bucket. If you store custom error pages on an HTTP server and the server starts to return 5xx errors, CloudFront can\'t get the files that you want to return to viewers because the origin server is unavailable.\n\nResponseCode (string) --The HTTP status code that you want CloudFront to return to the viewer along with the custom error page. There are a variety of reasons that you might want CloudFront to return a status code different from the status code that your origin returned to CloudFront, for example:\n\nSome Internet devices (some firewalls and corporate proxies, for example) intercept HTTP 4xx and 5xx and prevent the response from being returned to the viewer. If you substitute 200 , the response typically won\'t be intercepted.\nIf you don\'t care about distinguishing among different client errors or server errors, you can specify 400 or 500 as the ResponseCode for all 4xx or 5xx errors.\nYou might want to return a 200 status code (OK) and static website so your customers don\'t know that your website is down.\n\nIf you specify a value for ResponseCode , you must also specify a value for ResponsePagePath .\n\nErrorCachingMinTTL (integer) --The minimum amount of time, in seconds, that you want CloudFront to cache the HTTP status code specified in ErrorCode . When this time period has elapsed, CloudFront queries your origin to see whether the problem that caused the error has been resolved and the requested object is now available.\nFor more information, see Customizing Error Responses in the Amazon CloudFront Developer Guide .\n\n\n\n\n\n\n\nComment (string) -- [REQUIRED]Any comments you want to include about the distribution.\nIf you don\'t want to specify a comment, include an empty Comment element.\nTo delete an existing comment, update the distribution configuration and include an empty Comment element.\nTo add or change a comment, update the distribution configuration and specify the new comment.\n\nLogging (dict) --A complex type that controls whether access logs are written for the distribution.\nFor more information about logging, see Access Logs in the Amazon CloudFront Developer Guide .\n\nEnabled (boolean) -- [REQUIRED]Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you don\'t want to enable logging when you create a distribution or if you want to disable logging for an existing distribution, specify false for Enabled , and specify empty Bucket and Prefix elements. If you specify false for Enabled but you specify values for Bucket , prefix , and IncludeCookies , the values are automatically deleted.\n\nIncludeCookies (boolean) -- [REQUIRED]Specifies whether you want CloudFront to include cookies in access logs, specify true for IncludeCookies . If you choose to include cookies in logs, CloudFront logs all cookies regardless of how you configure the cache behaviors for this distribution. If you don\'t want to include cookies when you create a distribution or if you want to disable include cookies for an existing distribution, specify false for IncludeCookies .\n\nBucket (string) -- [REQUIRED]The Amazon S3 bucket to store the access logs in, for example, myawslogbucket.s3.amazonaws.com .\n\nPrefix (string) -- [REQUIRED]An optional string that you want CloudFront to prefix to the access log filenames for this distribution, for example, myprefix/ . If you want to enable logging, but you don\'t want to specify a prefix, you still must include an empty Prefix element in the Logging element.\n\n\n\nPriceClass (string) --The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify PriceClass_All , CloudFront responds to requests for your objects from all CloudFront edge locations.\nIf you specify a price class other than PriceClass_All , CloudFront serves your objects from the CloudFront edge location that has the lowest latency among the edge locations in your price class. Viewers who are in or near regions that are excluded from your specified price class may encounter slower performance.\nFor more information about price classes, see Choosing the Price Class for a CloudFront Distribution in the Amazon CloudFront Developer Guide . For information about CloudFront pricing, including how price classes (such as Price Class 100) map to CloudFront regions, see Amazon CloudFront Pricing . For price class information, scroll down to see the table at the bottom of the page.\n\nEnabled (boolean) -- [REQUIRED]From this field, you can enable or disable the selected distribution.\n\nViewerCertificate (dict) --A complex type that determines the distribution\xe2\x80\x99s SSL/TLS configuration for communicating with viewers.\n\nCloudFrontDefaultCertificate (boolean) --If the distribution uses the CloudFront domain name such as d111111abcdef8.cloudfront.net , set this field to true .\nIf the distribution uses Aliases (alternate domain names or CNAMEs), set this field to false and specify values for the following fields:\n\nACMCertificateArn or IAMCertificateId (specify a value for one, not both)\nMinimumProtocolVersion\nSSLSupportMethod\n\n\nIAMCertificateId (string) --If the distribution uses Aliases (alternate domain names or CNAMEs) and the SSL/TLS certificate is stored in AWS Identity and Access Management (AWS IAM) , provide the ID of the IAM certificate.\nIf you specify an IAM certificate ID, you must also specify values for MinimumProtocolVerison and SSLSupportMethod .\n\nACMCertificateArn (string) --If the distribution uses Aliases (alternate domain names or CNAMEs) and the SSL/TLS certificate is stored in AWS Certificate Manager (ACM) , provide the Amazon Resource Name (ARN) of the ACM certificate. CloudFront only supports ACM certificates in the US East (N. Virginia) Region (us-east-1 ).\nIf you specify an ACM certificate ARN, you must also specify values for MinimumProtocolVerison and SSLSupportMethod .\n\nSSLSupportMethod (string) --If the distribution uses Aliases (alternate domain names or CNAMEs), specify which viewers the distribution accepts HTTPS connections from.\n\nsni-only \xe2\x80\x93 The distribution accepts HTTPS connections from only viewers that support server name indication (SNI) . This is recommended. Most browsers and clients released after 2010 support SNI.\nvip \xe2\x80\x93 The distribution accepts HTTPS connections from all viewers including those that don\xe2\x80\x99t support SNI. This is not recommended, and results in additional monthly charges from CloudFront.\n\nIf the distribution uses the CloudFront domain name such as d111111abcdef8.cloudfront.net , don\xe2\x80\x99t set a value for this field.\n\nMinimumProtocolVersion (string) --If the distribution uses Aliases (alternate domain names or CNAMEs), specify the security policy that you want CloudFront to use for HTTPS connections with viewers. The security policy determines two settings:\n\nThe minimum SSL/TLS protocol that CloudFront can use to communicate with viewers.\nThe ciphers that CloudFront can use to encrypt the content that it returns to viewers.\n\nFor more information, see Security Policy and Supported Protocols and Ciphers Between Viewers and CloudFront in the Amazon CloudFront Developer Guide .\n\nNote\nOn the CloudFront console, this setting is called Security Policy .\n\nWe recommend that you specify TLSv1.2_2018 unless your viewers are using browsers or devices that don\xe2\x80\x99t support TLSv1.2.\nWhen you\xe2\x80\x99re using SNI only (you set SSLSupportMethod to sni-only ), you must specify TLSv1 or higher.\nIf the distribution uses the CloudFront domain name such as d111111abcdef8.cloudfront.net (you set CloudFrontDefaultCertificate to true ), CloudFront automatically sets the security policy to TLSv1 regardless of the value that you set here.\n\nCertificate (string) --This field is deprecated. Use one of the following fields instead:\n\nACMCertificateArn\nIAMCertificateId\nCloudFrontDefaultCertificate\n\n\nCertificateSource (string) --This field is deprecated. Use one of the following fields instead:\n\nACMCertificateArn\nIAMCertificateId\nCloudFrontDefaultCertificate\n\n\n\n\nRestrictions (dict) --A complex type that identifies ways in which you want to restrict distribution of your content.\n\nGeoRestriction (dict) -- [REQUIRED]A complex type that controls the countries in which your content is distributed. CloudFront determines the location of your users using MaxMind GeoIP databases.\n\nRestrictionType (string) -- [REQUIRED]The method that you want to use to restrict distribution of your content by country:\n\nnone : No geo restriction is enabled, meaning access to content is not restricted by client geo location.\nblacklist : The Location elements specify the countries in which you don\'t want CloudFront to distribute your content.\nwhitelist : The Location elements specify the countries in which you want CloudFront to distribute your content.\n\n\nQuantity (integer) -- [REQUIRED]When geo restriction is enabled , this is the number of countries in your whitelist or blacklist . Otherwise, when it is not enabled, Quantity is 0 , and you can omit Items .\n\nItems (list) --A complex type that contains a Location element for each country in which you want CloudFront either to distribute your content (whitelist ) or not distribute your content (blacklist ).\nThe Location element is a two-letter, uppercase country code for a country that you want to include in your blacklist or whitelist . Include one Location element for each country.\nCloudFront and MaxMind both use ISO 3166 country codes. For the current list of countries and the corresponding codes, see ISO 3166-1-alpha-2 code on the International Organization for Standardization website. You can also refer to the country list on the CloudFront console, which includes both country names and codes.\n\n(string) --\n\n\n\n\n\n\nWebACLId (string) --A unique identifier that specifies the AWS WAF web ACL, if any, to associate with this distribution. To specify a web ACL created using the latest version of AWS WAF, use the ACL ARN, for example arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/473e64fd-f30b-4765-81a0-62ad96dd167a . To specify a web ACL created using AWS WAF Classic, use the ACL ID, for example 473e64fd-f30b-4765-81a0-62ad96dd167a .\nAWS WAF is a web application firewall that lets you monitor the HTTP and HTTPS requests that are forwarded to CloudFront, and lets you control access to your content. Based on conditions that you specify, such as the IP addresses that requests originate from or the values of query strings, CloudFront responds to requests either with the requested content or with an HTTP 403 status code (Forbidden). You can also configure CloudFront to return a custom error page when a request is blocked. For more information about AWS WAF, see the AWS WAF Developer Guide .\n\nHttpVersion (string) --(Optional) Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront. The default value for new web distributions is http2. Viewers that don\'t support HTTP/2 automatically use an earlier HTTP version.\nFor viewers and CloudFront to use HTTP/2, viewers must support TLS 1.2 or later, and must support Server Name Identification (SNI).\nIn general, configuring CloudFront to communicate with viewers using HTTP/2 reduces latency. You can improve performance by optimizing for HTTP/2. For more information, do an Internet search for 'http/2 optimization.'\n\nIsIPV6Enabled (boolean) --If you want CloudFront to respond to IPv6 DNS requests with an IPv6 address for your distribution, specify true . If you specify false , CloudFront responds to IPv6 DNS requests with the DNS response code NOERROR and with no IP addresses. This allows viewers to submit a second request, for an IPv4 address for your distribution.\nIn general, you should enable IPv6 if you have users on IPv6 networks who want to access your content. However, if you\'re using signed URLs or signed cookies to restrict access to your content, and if you\'re using a custom policy that includes the IpAddress parameter to restrict the IP addresses that can access your content, don\'t enable IPv6. If you want to restrict access to some content by IP address and not restrict access to other content (or restrict access but not by IP address), you can create two distributions. For more information, see Creating a Signed URL Using a Custom Policy in the Amazon CloudFront Developer Guide .\nIf you\'re using an Amazon Route 53 alias resource record set to route traffic to your CloudFront distribution, you need to create a second alias resource record set when both of the following are true:\n\nYou enable IPv6 for the distribution\nYou\'re using alternate domain names in the URLs for your objects\n\nFor more information, see Routing Traffic to an Amazon CloudFront Web Distribution by Using Your Domain Name in the Amazon Route 53 Developer Guide .\nIf you created a CNAME resource record set, either with Amazon Route 53 or with another DNS service, you don\'t need to make any changes. A CNAME record will route traffic to your distribution regardless of the IP address format of the viewer request.\n\n\n\nTags (dict) -- [REQUIRED]A complex type that contains zero or more Tag elements.\n\nItems (list) --A complex type that contains Tag elements.\n\n(dict) --A complex type that contains Tag key and Tag value.\n\nKey (string) -- [REQUIRED]A string that contains Tag key.\nThe string length should be between 1 and 128 characters. Valid characters include a-z , A-Z , 0-9 , space, and the special characters _ - . : / = + @ .\n\nValue (string) --A string that contains an optional Tag value.\nThe string length should be between 0 and 256 characters. Valid characters include a-z , A-Z , 0-9 , space, and the special characters _ - . : / = + @ .\n\n\n\n\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'Distribution': {
        'Id': 'string',
        'ARN': 'string',
        'Status': 'string',
        'LastModifiedTime': datetime(2015, 1, 1),
        'InProgressInvalidationBatches': 123,
        'DomainName': 'string',
        'ActiveTrustedSigners': {
            'Enabled': True|False,
            'Quantity': 123,
            'Items': [
                {
                    'AwsAccountNumber': 'string',
                    'KeyPairIds': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    }
                },
            ]
        },
        'DistributionConfig': {
            'CallerReference': 'string',
            'Aliases': {
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'DefaultRootObject': 'string',
            'Origins': {
                'Quantity': 123,
                'Items': [
                    {
                        'Id': 'string',
                        'DomainName': 'string',
                        'OriginPath': 'string',
                        'CustomHeaders': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'HeaderName': 'string',
                                    'HeaderValue': 'string'
                                },
                            ]
                        },
                        'S3OriginConfig': {
                            'OriginAccessIdentity': 'string'
                        },
                        'CustomOriginConfig': {
                            'HTTPPort': 123,
                            'HTTPSPort': 123,
                            'OriginProtocolPolicy': 'http-only'|'match-viewer'|'https-only',
                            'OriginSslProtocols': {
                                'Quantity': 123,
                                'Items': [
                                    'SSLv3'|'TLSv1'|'TLSv1.1'|'TLSv1.2',
                                ]
                            },
                            'OriginReadTimeout': 123,
                            'OriginKeepaliveTimeout': 123
                        }
                    },
                ]
            },
            'OriginGroups': {
                'Quantity': 123,
                'Items': [
                    {
                        'Id': 'string',
                        'FailoverCriteria': {
                            'StatusCodes': {
                                'Quantity': 123,
                                'Items': [
                                    123,
                                ]
                            }
                        },
                        'Members': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'OriginId': 'string'
                                },
                            ]
                        }
                    },
                ]
            },
            'DefaultCacheBehavior': {
                'TargetOriginId': 'string',
                'ForwardedValues': {
                    'QueryString': True|False,
                    'Cookies': {
                        'Forward': 'none'|'whitelist'|'all',
                        'WhitelistedNames': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                    'Headers': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    },
                    'QueryStringCacheKeys': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    }
                },
                'TrustedSigners': {
                    'Enabled': True|False,
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                'MinTTL': 123,
                'AllowedMethods': {
                    'Quantity': 123,
                    'Items': [
                        'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                    ],
                    'CachedMethods': {
                        'Quantity': 123,
                        'Items': [
                            'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                        ]
                    }
                },
                'SmoothStreaming': True|False,
                'DefaultTTL': 123,
                'MaxTTL': 123,
                'Compress': True|False,
                'LambdaFunctionAssociations': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'LambdaFunctionARN': 'string',
                            'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                            'IncludeBody': True|False
                        },
                    ]
                },
                'FieldLevelEncryptionId': 'string'
            },
            'CacheBehaviors': {
                'Quantity': 123,
                'Items': [
                    {
                        'PathPattern': 'string',
                        'TargetOriginId': 'string',
                        'ForwardedValues': {
                            'QueryString': True|False,
                            'Cookies': {
                                'Forward': 'none'|'whitelist'|'all',
                                'WhitelistedNames': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                }
                            },
                            'Headers': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            },
                            'QueryStringCacheKeys': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                        'TrustedSigners': {
                            'Enabled': True|False,
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        },
                        'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                        'MinTTL': 123,
                        'AllowedMethods': {
                            'Quantity': 123,
                            'Items': [
                                'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                            ],
                            'CachedMethods': {
                                'Quantity': 123,
                                'Items': [
                                    'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                ]
                            }
                        },
                        'SmoothStreaming': True|False,
                        'DefaultTTL': 123,
                        'MaxTTL': 123,
                        'Compress': True|False,
                        'LambdaFunctionAssociations': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'LambdaFunctionARN': 'string',
                                    'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                    'IncludeBody': True|False
                                },
                            ]
                        },
                        'FieldLevelEncryptionId': 'string'
                    },
                ]
            },
            'CustomErrorResponses': {
                'Quantity': 123,
                'Items': [
                    {
                        'ErrorCode': 123,
                        'ResponsePagePath': 'string',
                        'ResponseCode': 'string',
                        'ErrorCachingMinTTL': 123
                    },
                ]
            },
            'Comment': 'string',
            'Logging': {
                'Enabled': True|False,
                'IncludeCookies': True|False,
                'Bucket': 'string',
                'Prefix': 'string'
            },
            'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
            'Enabled': True|False,
            'ViewerCertificate': {
                'CloudFrontDefaultCertificate': True|False,
                'IAMCertificateId': 'string',
                'ACMCertificateArn': 'string',
                'SSLSupportMethod': 'sni-only'|'vip',
                'MinimumProtocolVersion': 'SSLv3'|'TLSv1'|'TLSv1_2016'|'TLSv1.1_2016'|'TLSv1.2_2018',
                'Certificate': 'string',
                'CertificateSource': 'cloudfront'|'iam'|'acm'
            },
            'Restrictions': {
                'GeoRestriction': {
                    'RestrictionType': 'blacklist'|'whitelist'|'none',
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                }
            },
            'WebACLId': 'string',
            'HttpVersion': 'http1.1'|'http2',
            'IsIPV6Enabled': True|False
        },
        'AliasICPRecordals': [
            {
                'CNAME': 'string',
                'ICPRecordalStatus': 'APPROVED'|'SUSPENDED'|'PENDING'
            },
        ]
    },
    'Location': 'string',
    'ETag': 'string'
}


Response Structure

(dict) --The returned result of the corresponding request.

Distribution (dict) --The distribution\'s information.

Id (string) --The identifier for the distribution. For example: EDFDVBD632BHDS5 .

ARN (string) --The ARN (Amazon Resource Name) for the distribution. For example: arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5 , where 123456789012 is your AWS account ID.

Status (string) --This response element indicates the current status of the distribution. When the status is Deployed , the distribution\'s information is fully propagated to all CloudFront edge locations.

LastModifiedTime (datetime) --The date and time the distribution was last modified.

InProgressInvalidationBatches (integer) --The number of invalidation batches currently in progress.

DomainName (string) --The domain name corresponding to the distribution, for example, d111111abcdef8.cloudfront.net .

ActiveTrustedSigners (dict) --CloudFront automatically adds this element to the response only if you\'ve set up the distribution to serve private content with signed URLs. The element lists the key pair IDs that CloudFront is aware of for each trusted signer. The Signer child element lists the AWS account number of the trusted signer (or an empty Self element if the signer is you). The Signer element also includes the IDs of any active key pairs associated with the trusted signer\'s AWS account. If no KeyPairId element appears for a Signer , that signer can\'t create working signed URLs.

Enabled (boolean) --Enabled is true if any of the AWS accounts listed in the TrustedSigners complex type for this distribution have active CloudFront key pairs. If not, Enabled is false .

Quantity (integer) --The number of trusted signers specified in the TrustedSigners complex type.

Items (list) --A complex type that contains one Signer complex type for each trusted signer that is specified in the TrustedSigners complex type.

(dict) --A complex type that lists the AWS accounts that were included in the TrustedSigners complex type, as well as their active CloudFront key pair IDs, if any.

AwsAccountNumber (string) --An AWS account that is included in the TrustedSigners complex type for this distribution. Valid values include:

self , which is the AWS account used to create the distribution.
An AWS account number.


KeyPairIds (dict) --A complex type that lists the active CloudFront key pairs, if any, that are associated with AwsAccountNumber .

Quantity (integer) --The number of active CloudFront key pairs for AwsAccountNumber .
For more information, see ActiveTrustedSigners .

Items (list) --A complex type that lists the active CloudFront key pairs, if any, that are associated with AwsAccountNumber .
For more information, see ActiveTrustedSigners .

(string) --










DistributionConfig (dict) --The current configuration information for the distribution. Send a GET request to the /*CloudFront API version* /distribution ID/config resource.

CallerReference (string) --A unique value (for example, a date-time stamp) that ensures that the request can\'t be replayed.
If the value of CallerReference is new (regardless of the content of the DistributionConfig object), CloudFront creates a new distribution.
If CallerReference is a value that you already sent in a previous request to create a distribution, CloudFront returns a DistributionAlreadyExists error.

Aliases (dict) --A complex type that contains information about CNAMEs (alternate domain names), if any, for this distribution.

Quantity (integer) --The number of CNAME aliases, if any, that you want to associate with this distribution.

Items (list) --A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.

(string) --




DefaultRootObject (string) --The object that you want CloudFront to request from your origin (for example, index.html ) when a viewer requests the root URL for your distribution (http://www.example.com ) instead of an object in your distribution (http://www.example.com/product-description.html ). Specifying a default root object avoids exposing the contents of your distribution.
Specify only the object name, for example, index.html . Don\'t add a / before the object name.
If you don\'t want to specify a default root object when you create a distribution, include an empty DefaultRootObject element.
To delete the default root object from an existing distribution, update the distribution configuration and include an empty DefaultRootObject element.
To replace the default root object, update the distribution configuration and specify the new object.
For more information about the default root object, see Creating a Default Root Object in the Amazon CloudFront Developer Guide .

Origins (dict) --A complex type that contains information about origins for this distribution.

Quantity (integer) --The number of origins or origin groups for this distribution.

Items (list) --A complex type that contains origins or origin groups for this distribution.

(dict) --A complex type that describes the Amazon S3 bucket, HTTP server (for example, a web server), Amazon MediaStore, or other server from which CloudFront gets your files. This can also be an origin group, if you\'ve created an origin group. You must specify at least one origin or origin group.
For the current limit on the number of origins or origin groups that you can specify for a distribution, see Amazon CloudFront Limits in the AWS General Reference .

Id (string) --A unique identifier for the origin or origin group. The value of Id must be unique within the distribution.
When you specify the value of TargetOriginId for the default cache behavior or for another cache behavior, you indicate the origin to which you want the cache behavior to route requests by specifying the value of the Id element for that origin. When a request matches the path pattern for that cache behavior, CloudFront routes the request to the specified origin. For more information, see Cache Behavior Settings in the Amazon CloudFront Developer Guide .

DomainName (string) --
Amazon S3 origins : The DNS name of the Amazon S3 bucket from which you want CloudFront to get objects for this origin, for example, myawsbucket.s3.amazonaws.com . If you set up your bucket to be configured as a website endpoint, enter the Amazon S3 static website hosting endpoint for the bucket.
For more information about specifying this value for different types of origins, see Origin Domain Name in the Amazon CloudFront Developer Guide .
Constraints for Amazon S3 origins:

If you configured Amazon S3 Transfer Acceleration for your bucket, don\'t specify the s3-accelerate endpoint for DomainName .
The bucket name must be between 3 and 63 characters long (inclusive).
The bucket name must contain only lowercase characters, numbers, periods, underscores, and dashes.
The bucket name must not contain adjacent periods.


Custom Origins : The DNS domain name for the HTTP server from which you want CloudFront to get objects for this origin, for example, www.example.com .
Constraints for custom origins:

DomainName must be a valid DNS name that contains only a-z, A-Z, 0-9, dot (.), hyphen (-), or underscore (_) characters.
The name cannot exceed 128 characters.


OriginPath (string) --An optional element that causes CloudFront to request your content from a directory in your Amazon S3 bucket or your custom origin. When you include the OriginPath element, specify the directory name, beginning with a / . CloudFront appends the directory name to the value of DomainName , for example, example.com/production . Do not include a / at the end of the directory name.
For example, suppose you\'ve specified the following values for your distribution:

DomainName : An Amazon S3 bucket named myawsbucket .
OriginPath : /production
CNAME : example.com

When a user enters example.com/index.html in a browser, CloudFront sends a request to Amazon S3 for myawsbucket/production/index.html .
When a user enters example.com/acme/index.html in a browser, CloudFront sends a request to Amazon S3 for myawsbucket/production/acme/index.html .

CustomHeaders (dict) --A complex type that contains names and values for the custom headers that you want.

Quantity (integer) --The number of custom headers, if any, for this distribution.

Items (list) --
Optional : A list that contains one OriginCustomHeader element for each custom header that you want CloudFront to forward to the origin. If Quantity is 0 , omit Items .

(dict) --A complex type that contains HeaderName and HeaderValue elements, if any, for this distribution.

HeaderName (string) --The name of a header that you want CloudFront to forward to your origin. For more information, see Forwarding Custom Headers to Your Origin (Web Distributions Only) in the Amazon CloudFront Developer Guide .

HeaderValue (string) --The value for the header that you specified in the HeaderName field.







S3OriginConfig (dict) --A complex type that contains information about the Amazon S3 origin. If the origin is a custom origin, use the CustomOriginConfig element instead.

OriginAccessIdentity (string) --The CloudFront origin access identity to associate with the origin. Use an origin access identity to configure the origin so that viewers can only access objects in an Amazon S3 bucket through CloudFront. The format of the value is:
origin-access-identity/cloudfront/ID-of-origin-access-identity
where `` ID-of-origin-access-identity `` is the value that CloudFront returned in the ID element when you created the origin access identity.
If you want viewers to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty OriginAccessIdentity element.
To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty OriginAccessIdentity element.
To replace the origin access identity, update the distribution configuration and specify the new origin access identity.
For more information about the origin access identity, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .



CustomOriginConfig (dict) --A complex type that contains information about a custom origin. If the origin is an Amazon S3 bucket, use the S3OriginConfig element instead.

HTTPPort (integer) --The HTTP port the custom origin listens on.

HTTPSPort (integer) --The HTTPS port the custom origin listens on.

OriginProtocolPolicy (string) --The origin protocol policy to apply to your origin.

OriginSslProtocols (dict) --The SSL/TLS protocols that you want CloudFront to use when communicating with your origin over HTTPS.

Quantity (integer) --The number of SSL/TLS protocols that you want to allow CloudFront to use when establishing an HTTPS connection with this origin.

Items (list) --A list that contains allowed SSL/TLS protocols for this distribution.

(string) --




OriginReadTimeout (integer) --You can create a custom origin read timeout. All timeout units are in seconds. The default origin read timeout is 30 seconds, but you can configure custom timeout lengths using the CloudFront API. The minimum timeout length is 4 seconds; the maximum is 60 seconds.
If you need to increase the maximum time limit, contact the AWS Support Center .

OriginKeepaliveTimeout (integer) --You can create a custom keep-alive timeout. All timeout units are in seconds. The default keep-alive timeout is 5 seconds, but you can configure custom timeout lengths using the CloudFront API. The minimum timeout length is 1 second; the maximum is 60 seconds.
If you need to increase the maximum time limit, contact the AWS Support Center .









OriginGroups (dict) --A complex type that contains information about origin groups for this distribution.

Quantity (integer) --The number of origin groups.

Items (list) --The items (origin groups) in a distribution.

(dict) --An origin group includes two origins (a primary origin and a second origin to failover to) and a failover criteria that you specify. You create an origin group to support origin failover in CloudFront. When you create or update a distribution, you can specifiy the origin group instead of a single origin, and CloudFront will failover from the primary origin to the second origin under the failover conditions that you\'ve chosen.

Id (string) --The origin group\'s ID.

FailoverCriteria (dict) --A complex type that contains information about the failover criteria for an origin group.

StatusCodes (dict) --The status codes that, when returned from the primary origin, will trigger CloudFront to failover to the second origin.

Quantity (integer) --The number of status codes.

Items (list) --The items (status codes) for an origin group.

(integer) --






Members (dict) --A complex type that contains information about the origins in an origin group.

Quantity (integer) --The number of origins in an origin group.

Items (list) --Items (origins) in an origin group.

(dict) --An origin in an origin group.

OriginId (string) --The ID for an origin in an origin group.













DefaultCacheBehavior (dict) --A complex type that describes the default cache behavior if you don\'t specify a CacheBehavior element or if files don\'t match any of the values of PathPattern in CacheBehavior elements. You must create exactly one default cache behavior.

TargetOriginId (string) --The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior in your distribution.

ForwardedValues (dict) --A complex type that specifies how CloudFront handles query strings, cookies, and HTTP headers.

QueryString (boolean) --Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior and cache based on the query string parameters. CloudFront behavior depends on the value of QueryString and on the values that you specify for QueryStringCacheKeys , if any:
If you specify true for QueryString and you don\'t specify any values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin and caches based on all query string parameters. Depending on how many query string parameters and values you have, this can adversely affect performance because CloudFront must forward more requests to the origin.
If you specify true for QueryString and you specify one or more values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin, but it only caches based on the query string parameters that you specify.
If you specify false for QueryString , CloudFront doesn\'t forward any query string parameters to the origin, and doesn\'t cache based on query string parameters.
For more information, see Configuring CloudFront to Cache Based on Query String Parameters in the Amazon CloudFront Developer Guide .

Cookies (dict) --A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see How CloudFront Forwards, Caches, and Logs Cookies in the Amazon CloudFront Developer Guide .

Forward (string) --Specifies which cookies to forward to the origin for this cache behavior: all, none, or the list of cookies specified in the WhitelistedNames complex type.
Amazon S3 doesn\'t process cookies. When the cache behavior is forwarding requests to an Amazon S3 origin, specify none for the Forward element.

WhitelistedNames (dict) --Required if you specify whitelist for the value of Forward . A complex type that specifies how many different cookies you want CloudFront to forward to the origin for this cache behavior and, if you want to forward selected cookies, the names of those cookies.
If you specify all or none for the value of Forward , omit WhitelistedNames . If you change the value of Forward from whitelist to all or none and you don\'t delete the WhitelistedNames element and its child elements, CloudFront deletes them automatically.
For the current limit on the number of cookie names that you can whitelist for each cache behavior, see CloudFront Limits in the AWS General Reference .

Quantity (integer) --The number of different cookies that you want CloudFront to forward to the origin for this cache behavior. The value must equal the number of items that are in the Items field.
When you set Forward = whitelist (in the CookiePreferences object), this value must be 1 or higher.

Items (list) --A complex type that contains one Name element for each cookie that you want CloudFront to forward to the origin for this cache behavior. It must contain the same number of items that is specified in the Quantity field.
When you set Forward = whitelist (in the CookiePreferences object), this field must contain at least one item.

(string) --






Headers (dict) --A complex type that specifies the Headers , if any, that you want CloudFront to forward to the origin for this cache behavior (whitelisted headers). For the headers that you specify, CloudFront also caches separate versions of a specified object that is based on the header values in viewer requests.
For more information, see Caching Content Based on Request Headers in the Amazon CloudFront Developer Guide .

Quantity (integer) --The number of different headers that you want CloudFront to base caching on for this cache behavior. You can configure each cache behavior in a web distribution to do one of the following:

Forward all headers to your origin : Specify 1 for Quantity and * for Name .


Warning
CloudFront doesn\'t cache the objects that are associated with this cache behavior. Instead, CloudFront sends every request to the origin.


Forward a whitelist of headers you specify : Specify the number of headers that you want CloudFront to base caching on. Then specify the header names in Name elements. CloudFront caches your objects based on the values in the specified headers.
Forward only the default headers : Specify 0 for Quantity and omit Items . In this configuration, CloudFront doesn\'t cache based on the values in the request headers.

Regardless of which option you choose, CloudFront forwards headers to your origin based on whether the origin is an S3 bucket or a custom origin. See the following documentation:

S3 bucket : See HTTP Request Headers That CloudFront Removes or Updates
Custom origin : See HTTP Request Headers and CloudFront Behavior


Items (list) --A list that contains one Name element for each header that you want CloudFront to use for caching in this cache behavior. If Quantity is 0 , omit Items .

(string) --




QueryStringCacheKeys (dict) --A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.

Quantity (integer) --The number of whitelisted query string parameters for a cache behavior.

Items (list) --A list that contains the query string parameters that you want CloudFront to use as a basis for caching for a cache behavior. If Quantity is 0, you can omit Items .

(string) --






TrustedSigners (dict) --A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content.
If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled , and specify the applicable values for Quantity and Items . For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .
If you don\'t want to require signed URLs in requests for objects that match PathPattern , specify false for Enabled and 0 for Quantity . Omit Items .
To add, change, or remove one or more trusted signers, change Enabled to true (if it\'s currently false ), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.

Enabled (boolean) --Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .

Quantity (integer) --The number of trusted signers for this cache behavior.

Items (list) --
Optional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .

(string) --




ViewerProtocolPolicy (string) --The protocol that viewers can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern . You can specify the following options:

allow-all : Viewers can use HTTP or HTTPS.
redirect-to-https : If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.
https-only : If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).

For more information about requiring the HTTPS protocol, see Using an HTTPS Connection to Access Your Objects in the Amazon CloudFront Developer Guide .

Note
The only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects\' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .


MinTTL (integer) --The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .
You must specify 0 for MinTTL if you configure CloudFront to forward all headers to your origin (under Headers , if you specify 1 for Quantity and * for Name ).

AllowedMethods (dict) --A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices:

CloudFront forwards only GET and HEAD requests.
CloudFront forwards only GET , HEAD , and OPTIONS requests.
CloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests.

If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can\'t perform operations that you don\'t want them to. For example, you might not want users to have permissions to delete objects from your origin.

Quantity (integer) --The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET , HEAD , and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests).

Items (list) --A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.

(string) --


CachedMethods (dict) --A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices:

CloudFront caches responses to GET and HEAD requests.
CloudFront caches responses to GET , HEAD , and OPTIONS requests.

If you pick the second choice for your Amazon S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers, and Origin headers for the responses to be cached correctly.

Quantity (integer) --The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET , HEAD , and OPTIONS requests).

Items (list) --A complex type that contains the HTTP methods that you want CloudFront to cache responses to.

(string) --






SmoothStreaming (boolean) --Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true ; if not, specify false . If you specify true for SmoothStreaming , you can still distribute other content using this cache behavior if the content matches the value of PathPattern .

DefaultTTL (integer) --The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .

MaxTTL (integer) --The maximum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .

Compress (boolean) --Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify true ; if not, specify false . For more information, see Serving Compressed Files in the Amazon CloudFront Developer Guide .

LambdaFunctionAssociations (dict) --A complex type that contains zero or more Lambda function associations for a cache behavior.

Quantity (integer) --The number of Lambda function associations for this cache behavior.

Items (list) --
Optional : A complex type that contains LambdaFunctionAssociation items for this cache behavior. If Quantity is 0 , you can omit Items .

(dict) --A complex type that contains a Lambda function association.

LambdaFunctionARN (string) --The ARN of the Lambda function. You must specify the ARN of a function version; you can\'t specify a Lambda alias or $LATEST.

EventType (string) --Specifies the event type that triggers a Lambda function invocation. You can specify the following values:

viewer-request : The function executes when CloudFront receives a request from a viewer and before it checks to see whether the requested object is in the edge cache.
origin-request : The function executes only when CloudFront forwards a request to your origin. When the requested object is in the edge cache, the function doesn\'t execute.
origin-response : The function executes after CloudFront receives a response from the origin and before it caches the object in the response. When the requested object is in the edge cache, the function doesn\'t execute.
viewer-response : The function executes before CloudFront returns the requested object to the viewer. The function executes regardless of whether the object was already in the edge cache. If the origin returns an HTTP status code other than HTTP 200 (OK), the function doesn\'t execute.


IncludeBody (boolean) --A flag that allows a Lambda function to have read access to the body content. For more information, see Accessing the Request Body by Choosing the Include Body Option in the Amazon CloudFront Developer Guide.







FieldLevelEncryptionId (string) --The value of ID for the field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data for a cache behavior or for the default cache behavior in your distribution.



CacheBehaviors (dict) --A complex type that contains zero or more CacheBehavior elements.

Quantity (integer) --The number of cache behaviors for this distribution.

Items (list) --Optional: A complex type that contains cache behaviors for this distribution. If Quantity is 0 , you can omit Items .

(dict) --A complex type that describes how CloudFront processes requests.
You must create at least as many cache behaviors (including the default cache behavior) as you have origins if you want CloudFront to distribute objects from all of the origins. Each cache behavior specifies the one origin from which you want CloudFront to get objects. If you have two origins and only the default cache behavior, the default cache behavior will cause CloudFront to get objects from one of the origins, but the other origin is never used.
For the current limit on the number of cache behaviors that you can add to a distribution, see Amazon CloudFront Limits in the AWS General Reference .
If you don\'t want to specify any cache behaviors, include only an empty CacheBehaviors element. Don\'t include an empty CacheBehavior element, or CloudFront returns a MalformedXML error.
To delete all cache behaviors in an existing distribution, update the distribution configuration and include only an empty CacheBehaviors element.
To add, change, or remove one or more cache behaviors, update the distribution configuration and specify all of the cache behaviors that you want to include in the updated distribution.
For more information about cache behaviors, see Cache Behaviors in the Amazon CloudFront Developer Guide .

PathPattern (string) --The pattern (for example, images/*.jpg ) that specifies which requests to apply the behavior to. When CloudFront receives a viewer request, the requested path is compared with path patterns in the order in which cache behaviors are listed in the distribution.

Note
You can optionally include a slash (/ ) at the beginning of the path pattern. For example, /images/*.jpg . CloudFront behavior is the same with or without the leading / .

The path pattern for the default cache behavior is * and cannot be changed. If the request for an object does not match the path pattern for any cache behaviors, CloudFront applies the behavior in the default cache behavior.
For more information, see Path Pattern in the Amazon CloudFront Developer Guide .

TargetOriginId (string) --The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior in your distribution.

ForwardedValues (dict) --A complex type that specifies how CloudFront handles query strings, cookies, and HTTP headers.

QueryString (boolean) --Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior and cache based on the query string parameters. CloudFront behavior depends on the value of QueryString and on the values that you specify for QueryStringCacheKeys , if any:
If you specify true for QueryString and you don\'t specify any values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin and caches based on all query string parameters. Depending on how many query string parameters and values you have, this can adversely affect performance because CloudFront must forward more requests to the origin.
If you specify true for QueryString and you specify one or more values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin, but it only caches based on the query string parameters that you specify.
If you specify false for QueryString , CloudFront doesn\'t forward any query string parameters to the origin, and doesn\'t cache based on query string parameters.
For more information, see Configuring CloudFront to Cache Based on Query String Parameters in the Amazon CloudFront Developer Guide .

Cookies (dict) --A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see How CloudFront Forwards, Caches, and Logs Cookies in the Amazon CloudFront Developer Guide .

Forward (string) --Specifies which cookies to forward to the origin for this cache behavior: all, none, or the list of cookies specified in the WhitelistedNames complex type.
Amazon S3 doesn\'t process cookies. When the cache behavior is forwarding requests to an Amazon S3 origin, specify none for the Forward element.

WhitelistedNames (dict) --Required if you specify whitelist for the value of Forward . A complex type that specifies how many different cookies you want CloudFront to forward to the origin for this cache behavior and, if you want to forward selected cookies, the names of those cookies.
If you specify all or none for the value of Forward , omit WhitelistedNames . If you change the value of Forward from whitelist to all or none and you don\'t delete the WhitelistedNames element and its child elements, CloudFront deletes them automatically.
For the current limit on the number of cookie names that you can whitelist for each cache behavior, see CloudFront Limits in the AWS General Reference .

Quantity (integer) --The number of different cookies that you want CloudFront to forward to the origin for this cache behavior. The value must equal the number of items that are in the Items field.
When you set Forward = whitelist (in the CookiePreferences object), this value must be 1 or higher.

Items (list) --A complex type that contains one Name element for each cookie that you want CloudFront to forward to the origin for this cache behavior. It must contain the same number of items that is specified in the Quantity field.
When you set Forward = whitelist (in the CookiePreferences object), this field must contain at least one item.

(string) --






Headers (dict) --A complex type that specifies the Headers , if any, that you want CloudFront to forward to the origin for this cache behavior (whitelisted headers). For the headers that you specify, CloudFront also caches separate versions of a specified object that is based on the header values in viewer requests.
For more information, see Caching Content Based on Request Headers in the Amazon CloudFront Developer Guide .

Quantity (integer) --The number of different headers that you want CloudFront to base caching on for this cache behavior. You can configure each cache behavior in a web distribution to do one of the following:

Forward all headers to your origin : Specify 1 for Quantity and * for Name .


Warning
CloudFront doesn\'t cache the objects that are associated with this cache behavior. Instead, CloudFront sends every request to the origin.


Forward a whitelist of headers you specify : Specify the number of headers that you want CloudFront to base caching on. Then specify the header names in Name elements. CloudFront caches your objects based on the values in the specified headers.
Forward only the default headers : Specify 0 for Quantity and omit Items . In this configuration, CloudFront doesn\'t cache based on the values in the request headers.

Regardless of which option you choose, CloudFront forwards headers to your origin based on whether the origin is an S3 bucket or a custom origin. See the following documentation:

S3 bucket : See HTTP Request Headers That CloudFront Removes or Updates
Custom origin : See HTTP Request Headers and CloudFront Behavior


Items (list) --A list that contains one Name element for each header that you want CloudFront to use for caching in this cache behavior. If Quantity is 0 , omit Items .

(string) --




QueryStringCacheKeys (dict) --A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.

Quantity (integer) --The number of whitelisted query string parameters for a cache behavior.

Items (list) --A list that contains the query string parameters that you want CloudFront to use as a basis for caching for a cache behavior. If Quantity is 0, you can omit Items .

(string) --






TrustedSigners (dict) --A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content.
If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled , and specify the applicable values for Quantity and Items . For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .
If you don\'t want to require signed URLs in requests for objects that match PathPattern , specify false for Enabled and 0 for Quantity . Omit Items .
To add, change, or remove one or more trusted signers, change Enabled to true (if it\'s currently false ), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.

Enabled (boolean) --Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .

Quantity (integer) --The number of trusted signers for this cache behavior.

Items (list) --
Optional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .

(string) --




ViewerProtocolPolicy (string) --The protocol that viewers can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern . You can specify the following options:

allow-all : Viewers can use HTTP or HTTPS.
redirect-to-https : If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.
https-only : If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).

For more information about requiring the HTTPS protocol, see Using an HTTPS Connection to Access Your Objects in the Amazon CloudFront Developer Guide .

Note
The only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects\' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .


MinTTL (integer) --The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .
You must specify 0 for MinTTL if you configure CloudFront to forward all headers to your origin (under Headers , if you specify 1 for Quantity and * for Name ).

AllowedMethods (dict) --A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices:

CloudFront forwards only GET and HEAD requests.
CloudFront forwards only GET , HEAD , and OPTIONS requests.
CloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests.

If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can\'t perform operations that you don\'t want them to. For example, you might not want users to have permissions to delete objects from your origin.

Quantity (integer) --The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET , HEAD , and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests).

Items (list) --A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.

(string) --


CachedMethods (dict) --A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices:

CloudFront caches responses to GET and HEAD requests.
CloudFront caches responses to GET , HEAD , and OPTIONS requests.

If you pick the second choice for your Amazon S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers, and Origin headers for the responses to be cached correctly.

Quantity (integer) --The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET , HEAD , and OPTIONS requests).

Items (list) --A complex type that contains the HTTP methods that you want CloudFront to cache responses to.

(string) --






SmoothStreaming (boolean) --Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true ; if not, specify false . If you specify true for SmoothStreaming , you can still distribute other content using this cache behavior if the content matches the value of PathPattern .

DefaultTTL (integer) --The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .

MaxTTL (integer) --The maximum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .

Compress (boolean) --Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify true; if not, specify false. For more information, see Serving Compressed Files in the Amazon CloudFront Developer Guide .

LambdaFunctionAssociations (dict) --A complex type that contains zero or more Lambda function associations for a cache behavior.

Quantity (integer) --The number of Lambda function associations for this cache behavior.

Items (list) --
Optional : A complex type that contains LambdaFunctionAssociation items for this cache behavior. If Quantity is 0 , you can omit Items .

(dict) --A complex type that contains a Lambda function association.

LambdaFunctionARN (string) --The ARN of the Lambda function. You must specify the ARN of a function version; you can\'t specify a Lambda alias or $LATEST.

EventType (string) --Specifies the event type that triggers a Lambda function invocation. You can specify the following values:

viewer-request : The function executes when CloudFront receives a request from a viewer and before it checks to see whether the requested object is in the edge cache.
origin-request : The function executes only when CloudFront forwards a request to your origin. When the requested object is in the edge cache, the function doesn\'t execute.
origin-response : The function executes after CloudFront receives a response from the origin and before it caches the object in the response. When the requested object is in the edge cache, the function doesn\'t execute.
viewer-response : The function executes before CloudFront returns the requested object to the viewer. The function executes regardless of whether the object was already in the edge cache. If the origin returns an HTTP status code other than HTTP 200 (OK), the function doesn\'t execute.


IncludeBody (boolean) --A flag that allows a Lambda function to have read access to the body content. For more information, see Accessing the Request Body by Choosing the Include Body Option in the Amazon CloudFront Developer Guide.







FieldLevelEncryptionId (string) --The value of ID for the field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data for a cache behavior or for the default cache behavior in your distribution.







CustomErrorResponses (dict) --A complex type that controls the following:

Whether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.
How long CloudFront caches HTTP status codes in the 4xx and 5xx range.

For more information about custom error pages, see Customizing Error Responses in the Amazon CloudFront Developer Guide .

Quantity (integer) --The number of HTTP status codes for which you want to specify a custom error page and/or a caching duration. If Quantity is 0 , you can omit Items .

Items (list) --A complex type that contains a CustomErrorResponse element for each HTTP status code for which you want to specify a custom error page and/or a caching duration.

(dict) --A complex type that controls:

Whether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.
How long CloudFront caches HTTP status codes in the 4xx and 5xx range.

For more information about custom error pages, see Customizing Error Responses in the Amazon CloudFront Developer Guide .

ErrorCode (integer) --The HTTP status code for which you want to specify a custom error page and/or a caching duration.

ResponsePagePath (string) --The path to the custom error page that you want CloudFront to return to a viewer when your origin returns the HTTP status code specified by ErrorCode , for example, /4xx-errors/403-forbidden.html . If you want to store your objects and your custom error pages in different locations, your distribution must include a cache behavior for which the following is true:

The value of PathPattern matches the path to your custom error messages. For example, suppose you saved custom error pages for 4xx errors in an Amazon S3 bucket in a directory named /4xx-errors . Your distribution must include a cache behavior for which the path pattern routes requests for your custom error pages to that location, for example, /4xx-errors/* .
The value of TargetOriginId specifies the value of the ID element for the origin that contains your custom error pages.

If you specify a value for ResponsePagePath , you must also specify a value for ResponseCode .
We recommend that you store custom error pages in an Amazon S3 bucket. If you store custom error pages on an HTTP server and the server starts to return 5xx errors, CloudFront can\'t get the files that you want to return to viewers because the origin server is unavailable.

ResponseCode (string) --The HTTP status code that you want CloudFront to return to the viewer along with the custom error page. There are a variety of reasons that you might want CloudFront to return a status code different from the status code that your origin returned to CloudFront, for example:

Some Internet devices (some firewalls and corporate proxies, for example) intercept HTTP 4xx and 5xx and prevent the response from being returned to the viewer. If you substitute 200 , the response typically won\'t be intercepted.
If you don\'t care about distinguishing among different client errors or server errors, you can specify 400 or 500 as the ResponseCode for all 4xx or 5xx errors.
You might want to return a 200 status code (OK) and static website so your customers don\'t know that your website is down.

If you specify a value for ResponseCode , you must also specify a value for ResponsePagePath .

ErrorCachingMinTTL (integer) --The minimum amount of time, in seconds, that you want CloudFront to cache the HTTP status code specified in ErrorCode . When this time period has elapsed, CloudFront queries your origin to see whether the problem that caused the error has been resolved and the requested object is now available.
For more information, see Customizing Error Responses in the Amazon CloudFront Developer Guide .







Comment (string) --Any comments you want to include about the distribution.
If you don\'t want to specify a comment, include an empty Comment element.
To delete an existing comment, update the distribution configuration and include an empty Comment element.
To add or change a comment, update the distribution configuration and specify the new comment.

Logging (dict) --A complex type that controls whether access logs are written for the distribution.
For more information about logging, see Access Logs in the Amazon CloudFront Developer Guide .

Enabled (boolean) --Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you don\'t want to enable logging when you create a distribution or if you want to disable logging for an existing distribution, specify false for Enabled , and specify empty Bucket and Prefix elements. If you specify false for Enabled but you specify values for Bucket , prefix , and IncludeCookies , the values are automatically deleted.

IncludeCookies (boolean) --Specifies whether you want CloudFront to include cookies in access logs, specify true for IncludeCookies . If you choose to include cookies in logs, CloudFront logs all cookies regardless of how you configure the cache behaviors for this distribution. If you don\'t want to include cookies when you create a distribution or if you want to disable include cookies for an existing distribution, specify false for IncludeCookies .

Bucket (string) --The Amazon S3 bucket to store the access logs in, for example, myawslogbucket.s3.amazonaws.com .

Prefix (string) --An optional string that you want CloudFront to prefix to the access log filenames for this distribution, for example, myprefix/ . If you want to enable logging, but you don\'t want to specify a prefix, you still must include an empty Prefix element in the Logging element.



PriceClass (string) --The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify PriceClass_All , CloudFront responds to requests for your objects from all CloudFront edge locations.
If you specify a price class other than PriceClass_All , CloudFront serves your objects from the CloudFront edge location that has the lowest latency among the edge locations in your price class. Viewers who are in or near regions that are excluded from your specified price class may encounter slower performance.
For more information about price classes, see Choosing the Price Class for a CloudFront Distribution in the Amazon CloudFront Developer Guide . For information about CloudFront pricing, including how price classes (such as Price Class 100) map to CloudFront regions, see Amazon CloudFront Pricing . For price class information, scroll down to see the table at the bottom of the page.

Enabled (boolean) --From this field, you can enable or disable the selected distribution.

ViewerCertificate (dict) --A complex type that determines the distribution\xe2\x80\x99s SSL/TLS configuration for communicating with viewers.

CloudFrontDefaultCertificate (boolean) --If the distribution uses the CloudFront domain name such as d111111abcdef8.cloudfront.net , set this field to true .
If the distribution uses Aliases (alternate domain names or CNAMEs), set this field to false and specify values for the following fields:

ACMCertificateArn or IAMCertificateId (specify a value for one, not both)
MinimumProtocolVersion
SSLSupportMethod


IAMCertificateId (string) --If the distribution uses Aliases (alternate domain names or CNAMEs) and the SSL/TLS certificate is stored in AWS Identity and Access Management (AWS IAM) , provide the ID of the IAM certificate.
If you specify an IAM certificate ID, you must also specify values for MinimumProtocolVerison and SSLSupportMethod .

ACMCertificateArn (string) --If the distribution uses Aliases (alternate domain names or CNAMEs) and the SSL/TLS certificate is stored in AWS Certificate Manager (ACM) , provide the Amazon Resource Name (ARN) of the ACM certificate. CloudFront only supports ACM certificates in the US East (N. Virginia) Region (us-east-1 ).
If you specify an ACM certificate ARN, you must also specify values for MinimumProtocolVerison and SSLSupportMethod .

SSLSupportMethod (string) --If the distribution uses Aliases (alternate domain names or CNAMEs), specify which viewers the distribution accepts HTTPS connections from.

sni-only \xe2\x80\x93 The distribution accepts HTTPS connections from only viewers that support server name indication (SNI) . This is recommended. Most browsers and clients released after 2010 support SNI.
vip \xe2\x80\x93 The distribution accepts HTTPS connections from all viewers including those that don\xe2\x80\x99t support SNI. This is not recommended, and results in additional monthly charges from CloudFront.

If the distribution uses the CloudFront domain name such as d111111abcdef8.cloudfront.net , don\xe2\x80\x99t set a value for this field.

MinimumProtocolVersion (string) --If the distribution uses Aliases (alternate domain names or CNAMEs), specify the security policy that you want CloudFront to use for HTTPS connections with viewers. The security policy determines two settings:

The minimum SSL/TLS protocol that CloudFront can use to communicate with viewers.
The ciphers that CloudFront can use to encrypt the content that it returns to viewers.

For more information, see Security Policy and Supported Protocols and Ciphers Between Viewers and CloudFront in the Amazon CloudFront Developer Guide .

Note
On the CloudFront console, this setting is called Security Policy .

We recommend that you specify TLSv1.2_2018 unless your viewers are using browsers or devices that don\xe2\x80\x99t support TLSv1.2.
When you\xe2\x80\x99re using SNI only (you set SSLSupportMethod to sni-only ), you must specify TLSv1 or higher.
If the distribution uses the CloudFront domain name such as d111111abcdef8.cloudfront.net (you set CloudFrontDefaultCertificate to true ), CloudFront automatically sets the security policy to TLSv1 regardless of the value that you set here.

Certificate (string) --This field is deprecated. Use one of the following fields instead:

ACMCertificateArn
IAMCertificateId
CloudFrontDefaultCertificate


CertificateSource (string) --This field is deprecated. Use one of the following fields instead:

ACMCertificateArn
IAMCertificateId
CloudFrontDefaultCertificate




Restrictions (dict) --A complex type that identifies ways in which you want to restrict distribution of your content.

GeoRestriction (dict) --A complex type that controls the countries in which your content is distributed. CloudFront determines the location of your users using MaxMind GeoIP databases.

RestrictionType (string) --The method that you want to use to restrict distribution of your content by country:

none : No geo restriction is enabled, meaning access to content is not restricted by client geo location.
blacklist : The Location elements specify the countries in which you don\'t want CloudFront to distribute your content.
whitelist : The Location elements specify the countries in which you want CloudFront to distribute your content.


Quantity (integer) --When geo restriction is enabled , this is the number of countries in your whitelist or blacklist . Otherwise, when it is not enabled, Quantity is 0 , and you can omit Items .

Items (list) --A complex type that contains a Location element for each country in which you want CloudFront either to distribute your content (whitelist ) or not distribute your content (blacklist ).
The Location element is a two-letter, uppercase country code for a country that you want to include in your blacklist or whitelist . Include one Location element for each country.
CloudFront and MaxMind both use ISO 3166 country codes. For the current list of countries and the corresponding codes, see ISO 3166-1-alpha-2 code on the International Organization for Standardization website. You can also refer to the country list on the CloudFront console, which includes both country names and codes.

(string) --






WebACLId (string) --A unique identifier that specifies the AWS WAF web ACL, if any, to associate with this distribution. To specify a web ACL created using the latest version of AWS WAF, use the ACL ARN, for example arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/473e64fd-f30b-4765-81a0-62ad96dd167a . To specify a web ACL created using AWS WAF Classic, use the ACL ID, for example 473e64fd-f30b-4765-81a0-62ad96dd167a .
AWS WAF is a web application firewall that lets you monitor the HTTP and HTTPS requests that are forwarded to CloudFront, and lets you control access to your content. Based on conditions that you specify, such as the IP addresses that requests originate from or the values of query strings, CloudFront responds to requests either with the requested content or with an HTTP 403 status code (Forbidden). You can also configure CloudFront to return a custom error page when a request is blocked. For more information about AWS WAF, see the AWS WAF Developer Guide .

HttpVersion (string) --(Optional) Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront. The default value for new web distributions is http2. Viewers that don\'t support HTTP/2 automatically use an earlier HTTP version.
For viewers and CloudFront to use HTTP/2, viewers must support TLS 1.2 or later, and must support Server Name Identification (SNI).
In general, configuring CloudFront to communicate with viewers using HTTP/2 reduces latency. You can improve performance by optimizing for HTTP/2. For more information, do an Internet search for "http/2 optimization."

IsIPV6Enabled (boolean) --If you want CloudFront to respond to IPv6 DNS requests with an IPv6 address for your distribution, specify true . If you specify false , CloudFront responds to IPv6 DNS requests with the DNS response code NOERROR and with no IP addresses. This allows viewers to submit a second request, for an IPv4 address for your distribution.
In general, you should enable IPv6 if you have users on IPv6 networks who want to access your content. However, if you\'re using signed URLs or signed cookies to restrict access to your content, and if you\'re using a custom policy that includes the IpAddress parameter to restrict the IP addresses that can access your content, don\'t enable IPv6. If you want to restrict access to some content by IP address and not restrict access to other content (or restrict access but not by IP address), you can create two distributions. For more information, see Creating a Signed URL Using a Custom Policy in the Amazon CloudFront Developer Guide .
If you\'re using an Amazon Route 53 alias resource record set to route traffic to your CloudFront distribution, you need to create a second alias resource record set when both of the following are true:

You enable IPv6 for the distribution
You\'re using alternate domain names in the URLs for your objects

For more information, see Routing Traffic to an Amazon CloudFront Web Distribution by Using Your Domain Name in the Amazon Route 53 Developer Guide .
If you created a CNAME resource record set, either with Amazon Route 53 or with another DNS service, you don\'t need to make any changes. A CNAME record will route traffic to your distribution regardless of the IP address format of the viewer request.



AliasICPRecordals (list) --AWS services in China customers must file for an Internet Content Provider (ICP) recordal if they want to serve content publicly on an alternate domain name, also known as a CNAME, that they\'ve added to CloudFront. AliasICPRecordal provides the ICP recordal status for CNAMEs associated with distributions.
For more information about ICP recordals, see Signup, Accounts, and Credentials in Getting Started with AWS services in China .

(dict) --AWS services in China customers must file for an Internet Content Provider (ICP) recordal if they want to serve content publicly on an alternate domain name, also known as a CNAME, that they\'ve added to CloudFront. AliasICPRecordal provides the ICP recordal status for CNAMEs associated with distributions. The status is returned in the CloudFront response; you can\'t configure it yourself.
For more information about ICP recordals, see Signup, Accounts, and Credentials in Getting Started with AWS services in China .

CNAME (string) --A domain name associated with a distribution.

ICPRecordalStatus (string) --The Internet Content Provider (ICP) recordal status for a CNAME. The ICPRecordalStatus is set to APPROVED for all CNAMEs (aliases) in regions outside of China.
The status values returned are the following:

APPROVED indicates that the associated CNAME has a valid ICP recordal number. Multiple CNAMEs can be associated with a distribution, and CNAMEs can correspond to different ICP recordals. To be marked as APPROVED, that is, valid to use with China region, a CNAME must have one ICP recordal number associated with it.
SUSPENDED indicates that the associated CNAME does not have a valid ICP recordal number.
PENDING indicates that CloudFront can\'t determine the ICP recordal status of the CNAME associated with the distribution because there was an error in trying to determine the status. You can try again to see if the error is resolved in which case CloudFront returns an APPROVED or SUSPENDED status.








Location (string) --The fully qualified URI of the new distribution resource just created. For example: https://cloudfront.amazonaws.com/2010-11-01/distribution/EDFDVBD632BHDS5 .

ETag (string) --The current version of the distribution created.






Exceptions

CloudFront.Client.exceptions.CNAMEAlreadyExists
CloudFront.Client.exceptions.DistributionAlreadyExists
CloudFront.Client.exceptions.InvalidOrigin
CloudFront.Client.exceptions.InvalidOriginAccessIdentity
CloudFront.Client.exceptions.AccessDenied
CloudFront.Client.exceptions.TooManyTrustedSigners
CloudFront.Client.exceptions.TrustedSignerDoesNotExist
CloudFront.Client.exceptions.InvalidViewerCertificate
CloudFront.Client.exceptions.InvalidMinimumProtocolVersion
CloudFront.Client.exceptions.MissingBody
CloudFront.Client.exceptions.TooManyDistributionCNAMEs
CloudFront.Client.exceptions.TooManyDistributions
CloudFront.Client.exceptions.InvalidDefaultRootObject
CloudFront.Client.exceptions.InvalidRelativePath
CloudFront.Client.exceptions.InvalidErrorCode
CloudFront.Client.exceptions.InvalidResponseCode
CloudFront.Client.exceptions.InvalidArgument
CloudFront.Client.exceptions.InvalidRequiredProtocol
CloudFront.Client.exceptions.NoSuchOrigin
CloudFront.Client.exceptions.TooManyOrigins
CloudFront.Client.exceptions.TooManyOriginGroupsPerDistribution
CloudFront.Client.exceptions.TooManyCacheBehaviors
CloudFront.Client.exceptions.TooManyCookieNamesInWhiteList
CloudFront.Client.exceptions.InvalidForwardCookies
CloudFront.Client.exceptions.TooManyHeadersInForwardedValues
CloudFront.Client.exceptions.InvalidHeadersForS3Origin
CloudFront.Client.exceptions.InconsistentQuantities
CloudFront.Client.exceptions.TooManyCertificates
CloudFront.Client.exceptions.InvalidLocationCode
CloudFront.Client.exceptions.InvalidGeoRestrictionParameter
CloudFront.Client.exceptions.InvalidProtocolSettings
CloudFront.Client.exceptions.InvalidTTLOrder
CloudFront.Client.exceptions.InvalidWebACLId
CloudFront.Client.exceptions.TooManyOriginCustomHeaders
CloudFront.Client.exceptions.InvalidTagging
CloudFront.Client.exceptions.TooManyQueryStringParameters
CloudFront.Client.exceptions.InvalidQueryStringParameters
CloudFront.Client.exceptions.TooManyDistributionsWithLambdaAssociations
CloudFront.Client.exceptions.TooManyLambdaFunctionAssociations
CloudFront.Client.exceptions.InvalidLambdaFunctionAssociation
CloudFront.Client.exceptions.InvalidOriginReadTimeout
CloudFront.Client.exceptions.InvalidOriginKeepaliveTimeout
CloudFront.Client.exceptions.NoSuchFieldLevelEncryptionConfig
CloudFront.Client.exceptions.IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior
CloudFront.Client.exceptions.TooManyDistributionsAssociatedToFieldLevelEncryptionConfig


    :return: {
        'Distribution': {
            'Id': 'string',
            'ARN': 'string',
            'Status': 'string',
            'LastModifiedTime': datetime(2015, 1, 1),
            'InProgressInvalidationBatches': 123,
            'DomainName': 'string',
            'ActiveTrustedSigners': {
                'Enabled': True|False,
                'Quantity': 123,
                'Items': [
                    {
                        'AwsAccountNumber': 'string',
                        'KeyPairIds': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                ]
            },
            'DistributionConfig': {
                'CallerReference': 'string',
                'Aliases': {
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'DefaultRootObject': 'string',
                'Origins': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'Id': 'string',
                            'DomainName': 'string',
                            'OriginPath': 'string',
                            'CustomHeaders': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'HeaderName': 'string',
                                        'HeaderValue': 'string'
                                    },
                                ]
                            },
                            'S3OriginConfig': {
                                'OriginAccessIdentity': 'string'
                            },
                            'CustomOriginConfig': {
                                'HTTPPort': 123,
                                'HTTPSPort': 123,
                                'OriginProtocolPolicy': 'http-only'|'match-viewer'|'https-only',
                                'OriginSslProtocols': {
                                    'Quantity': 123,
                                    'Items': [
                                        'SSLv3'|'TLSv1'|'TLSv1.1'|'TLSv1.2',
                                    ]
                                },
                                'OriginReadTimeout': 123,
                                'OriginKeepaliveTimeout': 123
                            }
                        },
                    ]
                },
                'OriginGroups': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'Id': 'string',
                            'FailoverCriteria': {
                                'StatusCodes': {
                                    'Quantity': 123,
                                    'Items': [
                                        123,
                                    ]
                                }
                            },
                            'Members': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'OriginId': 'string'
                                    },
                                ]
                            }
                        },
                    ]
                },
                'DefaultCacheBehavior': {
                    'TargetOriginId': 'string',
                    'ForwardedValues': {
                        'QueryString': True|False,
                        'Cookies': {
                            'Forward': 'none'|'whitelist'|'all',
                            'WhitelistedNames': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                        'Headers': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        },
                        'QueryStringCacheKeys': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                    'TrustedSigners': {
                        'Enabled': True|False,
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    },
                    'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                    'MinTTL': 123,
                    'AllowedMethods': {
                        'Quantity': 123,
                        'Items': [
                            'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                        ],
                        'CachedMethods': {
                            'Quantity': 123,
                            'Items': [
                                'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                            ]
                        }
                    },
                    'SmoothStreaming': True|False,
                    'DefaultTTL': 123,
                    'MaxTTL': 123,
                    'Compress': True|False,
                    'LambdaFunctionAssociations': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'LambdaFunctionARN': 'string',
                                'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                'IncludeBody': True|False
                            },
                        ]
                    },
                    'FieldLevelEncryptionId': 'string'
                },
                'CacheBehaviors': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'PathPattern': 'string',
                            'TargetOriginId': 'string',
                            'ForwardedValues': {
                                'QueryString': True|False,
                                'Cookies': {
                                    'Forward': 'none'|'whitelist'|'all',
                                    'WhitelistedNames': {
                                        'Quantity': 123,
                                        'Items': [
                                            'string',
                                        ]
                                    }
                                },
                                'Headers': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                },
                                'QueryStringCacheKeys': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                }
                            },
                            'TrustedSigners': {
                                'Enabled': True|False,
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            },
                            'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                            'MinTTL': 123,
                            'AllowedMethods': {
                                'Quantity': 123,
                                'Items': [
                                    'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                ],
                                'CachedMethods': {
                                    'Quantity': 123,
                                    'Items': [
                                        'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                    ]
                                }
                            },
                            'SmoothStreaming': True|False,
                            'DefaultTTL': 123,
                            'MaxTTL': 123,
                            'Compress': True|False,
                            'LambdaFunctionAssociations': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'LambdaFunctionARN': 'string',
                                        'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                        'IncludeBody': True|False
                                    },
                                ]
                            },
                            'FieldLevelEncryptionId': 'string'
                        },
                    ]
                },
                'CustomErrorResponses': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'ErrorCode': 123,
                            'ResponsePagePath': 'string',
                            'ResponseCode': 'string',
                            'ErrorCachingMinTTL': 123
                        },
                    ]
                },
                'Comment': 'string',
                'Logging': {
                    'Enabled': True|False,
                    'IncludeCookies': True|False,
                    'Bucket': 'string',
                    'Prefix': 'string'
                },
                'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
                'Enabled': True|False,
                'ViewerCertificate': {
                    'CloudFrontDefaultCertificate': True|False,
                    'IAMCertificateId': 'string',
                    'ACMCertificateArn': 'string',
                    'SSLSupportMethod': 'sni-only'|'vip',
                    'MinimumProtocolVersion': 'SSLv3'|'TLSv1'|'TLSv1_2016'|'TLSv1.1_2016'|'TLSv1.2_2018',
                    'Certificate': 'string',
                    'CertificateSource': 'cloudfront'|'iam'|'acm'
                },
                'Restrictions': {
                    'GeoRestriction': {
                        'RestrictionType': 'blacklist'|'whitelist'|'none',
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    }
                },
                'WebACLId': 'string',
                'HttpVersion': 'http1.1'|'http2',
                'IsIPV6Enabled': True|False
            },
            'AliasICPRecordals': [
                {
                    'CNAME': 'string',
                    'ICPRecordalStatus': 'APPROVED'|'SUSPENDED'|'PENDING'
                },
            ]
        },
        'Location': 'string',
        'ETag': 'string'
    }
    
    
    :returns: 
    If you configured Amazon S3 Transfer Acceleration for your bucket, don\'t specify the s3-accelerate endpoint for DomainName .
    The bucket name must be between 3 and 63 characters long (inclusive).
    The bucket name must contain only lowercase characters, numbers, periods, underscores, and dashes.
    The bucket name must not contain adjacent periods.
    
    """
    pass

def create_field_level_encryption_config(FieldLevelEncryptionConfig=None):
    """
    Create a new field-level encryption configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_field_level_encryption_config(
        FieldLevelEncryptionConfig={
            'CallerReference': 'string',
            'Comment': 'string',
            'QueryArgProfileConfig': {
                'ForwardWhenQueryArgProfileIsUnknown': True|False,
                'QueryArgProfiles': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'QueryArg': 'string',
                            'ProfileId': 'string'
                        },
                    ]
                }
            },
            'ContentTypeProfileConfig': {
                'ForwardWhenContentTypeIsUnknown': True|False,
                'ContentTypeProfiles': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'Format': 'URLEncoded',
                            'ProfileId': 'string',
                            'ContentType': 'string'
                        },
                    ]
                }
            }
        }
    )
    
    
    :type FieldLevelEncryptionConfig: dict
    :param FieldLevelEncryptionConfig: [REQUIRED]\nThe request to create a new field-level encryption configuration.\n\nCallerReference (string) -- [REQUIRED]A unique number that ensures the request can\'t be replayed.\n\nComment (string) --An optional comment about the configuration.\n\nQueryArgProfileConfig (dict) --A complex data type that specifies when to forward content if a profile isn\'t found and the profile that can be provided as a query argument in a request.\n\nForwardWhenQueryArgProfileIsUnknown (boolean) -- [REQUIRED]Flag to set if you want a request to be forwarded to the origin even if the profile specified by the field-level encryption query argument, fle-profile, is unknown.\n\nQueryArgProfiles (dict) --Profiles specified for query argument-profile mapping for field-level encryption.\n\nQuantity (integer) -- [REQUIRED]Number of profiles for query argument-profile mapping for field-level encryption.\n\nItems (list) --Number of items for query argument-profile mapping for field-level encryption.\n\n(dict) --Query argument-profile mapping for field-level encryption.\n\nQueryArg (string) -- [REQUIRED]Query argument for field-level encryption query argument-profile mapping.\n\nProfileId (string) -- [REQUIRED]ID of profile to use for field-level encryption query argument-profile mapping\n\n\n\n\n\n\n\n\n\nContentTypeProfileConfig (dict) --A complex data type that specifies when to forward content if a content type isn\'t recognized and profiles to use as by default in a request if a query argument doesn\'t specify a profile to use.\n\nForwardWhenContentTypeIsUnknown (boolean) -- [REQUIRED]The setting in a field-level encryption content type-profile mapping that specifies what to do when an unknown content type is provided for the profile. If true, content is forwarded without being encrypted when the content type is unknown. If false (the default), an error is returned when the content type is unknown.\n\nContentTypeProfiles (dict) --The configuration for a field-level encryption content type-profile.\n\nQuantity (integer) -- [REQUIRED]The number of field-level encryption content type-profile mappings.\n\nItems (list) --Items in a field-level encryption content type-profile mapping.\n\n(dict) --A field-level encryption content type profile.\n\nFormat (string) -- [REQUIRED]The format for a field-level encryption content type-profile mapping.\n\nProfileId (string) --The profile ID for a field-level encryption content type-profile mapping.\n\nContentType (string) -- [REQUIRED]The content type for a field-level encryption content type-profile mapping.\n\n\n\n\n\n\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'FieldLevelEncryption': {
        'Id': 'string',
        'LastModifiedTime': datetime(2015, 1, 1),
        'FieldLevelEncryptionConfig': {
            'CallerReference': 'string',
            'Comment': 'string',
            'QueryArgProfileConfig': {
                'ForwardWhenQueryArgProfileIsUnknown': True|False,
                'QueryArgProfiles': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'QueryArg': 'string',
                            'ProfileId': 'string'
                        },
                    ]
                }
            },
            'ContentTypeProfileConfig': {
                'ForwardWhenContentTypeIsUnknown': True|False,
                'ContentTypeProfiles': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'Format': 'URLEncoded',
                            'ProfileId': 'string',
                            'ContentType': 'string'
                        },
                    ]
                }
            }
        }
    },
    'Location': 'string',
    'ETag': 'string'
}


Response Structure

(dict) --
FieldLevelEncryption (dict) --Returned when you create a new field-level encryption configuration.

Id (string) --The configuration ID for a field-level encryption configuration which includes a set of profiles that specify certain selected data fields to be encrypted by specific public keys.

LastModifiedTime (datetime) --The last time the field-level encryption configuration was changed.

FieldLevelEncryptionConfig (dict) --A complex data type that includes the profile configurations specified for field-level encryption.

CallerReference (string) --A unique number that ensures the request can\'t be replayed.

Comment (string) --An optional comment about the configuration.

QueryArgProfileConfig (dict) --A complex data type that specifies when to forward content if a profile isn\'t found and the profile that can be provided as a query argument in a request.

ForwardWhenQueryArgProfileIsUnknown (boolean) --Flag to set if you want a request to be forwarded to the origin even if the profile specified by the field-level encryption query argument, fle-profile, is unknown.

QueryArgProfiles (dict) --Profiles specified for query argument-profile mapping for field-level encryption.

Quantity (integer) --Number of profiles for query argument-profile mapping for field-level encryption.

Items (list) --Number of items for query argument-profile mapping for field-level encryption.

(dict) --Query argument-profile mapping for field-level encryption.

QueryArg (string) --Query argument for field-level encryption query argument-profile mapping.

ProfileId (string) --ID of profile to use for field-level encryption query argument-profile mapping









ContentTypeProfileConfig (dict) --A complex data type that specifies when to forward content if a content type isn\'t recognized and profiles to use as by default in a request if a query argument doesn\'t specify a profile to use.

ForwardWhenContentTypeIsUnknown (boolean) --The setting in a field-level encryption content type-profile mapping that specifies what to do when an unknown content type is provided for the profile. If true, content is forwarded without being encrypted when the content type is unknown. If false (the default), an error is returned when the content type is unknown.

ContentTypeProfiles (dict) --The configuration for a field-level encryption content type-profile.

Quantity (integer) --The number of field-level encryption content type-profile mappings.

Items (list) --Items in a field-level encryption content type-profile mapping.

(dict) --A field-level encryption content type profile.

Format (string) --The format for a field-level encryption content type-profile mapping.

ProfileId (string) --The profile ID for a field-level encryption content type-profile mapping.

ContentType (string) --The content type for a field-level encryption content type-profile mapping.













Location (string) --The fully qualified URI of the new configuration resource just created. For example: https://cloudfront.amazonaws.com/2010-11-01/field-level-encryption-config/EDFDVBD632BHDS5 .

ETag (string) --The current version of the field level encryption configuration. For example: E2QWRUHAPOMQZL .






Exceptions

CloudFront.Client.exceptions.InconsistentQuantities
CloudFront.Client.exceptions.InvalidArgument
CloudFront.Client.exceptions.NoSuchFieldLevelEncryptionProfile
CloudFront.Client.exceptions.FieldLevelEncryptionConfigAlreadyExists
CloudFront.Client.exceptions.TooManyFieldLevelEncryptionConfigs
CloudFront.Client.exceptions.TooManyFieldLevelEncryptionQueryArgProfiles
CloudFront.Client.exceptions.TooManyFieldLevelEncryptionContentTypeProfiles
CloudFront.Client.exceptions.QueryArgProfileEmpty


    :return: {
        'FieldLevelEncryption': {
            'Id': 'string',
            'LastModifiedTime': datetime(2015, 1, 1),
            'FieldLevelEncryptionConfig': {
                'CallerReference': 'string',
                'Comment': 'string',
                'QueryArgProfileConfig': {
                    'ForwardWhenQueryArgProfileIsUnknown': True|False,
                    'QueryArgProfiles': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'QueryArg': 'string',
                                'ProfileId': 'string'
                            },
                        ]
                    }
                },
                'ContentTypeProfileConfig': {
                    'ForwardWhenContentTypeIsUnknown': True|False,
                    'ContentTypeProfiles': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'Format': 'URLEncoded',
                                'ProfileId': 'string',
                                'ContentType': 'string'
                            },
                        ]
                    }
                }
            }
        },
        'Location': 'string',
        'ETag': 'string'
    }
    
    
    """
    pass

def create_field_level_encryption_profile(FieldLevelEncryptionProfileConfig=None):
    """
    Create a field-level encryption profile.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_field_level_encryption_profile(
        FieldLevelEncryptionProfileConfig={
            'Name': 'string',
            'CallerReference': 'string',
            'Comment': 'string',
            'EncryptionEntities': {
                'Quantity': 123,
                'Items': [
                    {
                        'PublicKeyId': 'string',
                        'ProviderId': 'string',
                        'FieldPatterns': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                ]
            }
        }
    )
    
    
    :type FieldLevelEncryptionProfileConfig: dict
    :param FieldLevelEncryptionProfileConfig: [REQUIRED]\nThe request to create a field-level encryption profile.\n\nName (string) -- [REQUIRED]Profile name for the field-level encryption profile.\n\nCallerReference (string) -- [REQUIRED]A unique number that ensures that the request can\'t be replayed.\n\nComment (string) --An optional comment for the field-level encryption profile.\n\nEncryptionEntities (dict) -- [REQUIRED]A complex data type of encryption entities for the field-level encryption profile that include the public key ID, provider, and field patterns for specifying which fields to encrypt with this key.\n\nQuantity (integer) -- [REQUIRED]Number of field pattern items in a field-level encryption content type-profile mapping.\n\nItems (list) --An array of field patterns in a field-level encryption content type-profile mapping.\n\n(dict) --Complex data type for field-level encryption profiles that includes the encryption key and field pattern specifications.\n\nPublicKeyId (string) -- [REQUIRED]The public key associated with a set of field-level encryption patterns, to be used when encrypting the fields that match the patterns.\n\nProviderId (string) -- [REQUIRED]The provider associated with the public key being used for encryption. This value must also be provided with the private key for applications to be able to decrypt data.\n\nFieldPatterns (dict) -- [REQUIRED]Field patterns in a field-level encryption content type profile specify the fields that you want to be encrypted. You can provide the full field name, or any beginning characters followed by a wildcard (*). You can\'t overlap field patterns. For example, you can\'t have both ABC* and AB*. Note that field patterns are case-sensitive.\n\nQuantity (integer) -- [REQUIRED]The number of field-level encryption field patterns.\n\nItems (list) --An array of the field-level encryption field patterns.\n\n(string) --\n\n\n\n\n\n\n\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'FieldLevelEncryptionProfile': {
        'Id': 'string',
        'LastModifiedTime': datetime(2015, 1, 1),
        'FieldLevelEncryptionProfileConfig': {
            'Name': 'string',
            'CallerReference': 'string',
            'Comment': 'string',
            'EncryptionEntities': {
                'Quantity': 123,
                'Items': [
                    {
                        'PublicKeyId': 'string',
                        'ProviderId': 'string',
                        'FieldPatterns': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                ]
            }
        }
    },
    'Location': 'string',
    'ETag': 'string'
}


Response Structure

(dict) --
FieldLevelEncryptionProfile (dict) --Returned when you create a new field-level encryption profile.

Id (string) --The ID for a field-level encryption profile configuration which includes a set of profiles that specify certain selected data fields to be encrypted by specific public keys.

LastModifiedTime (datetime) --The last time the field-level encryption profile was updated.

FieldLevelEncryptionProfileConfig (dict) --A complex data type that includes the profile name and the encryption entities for the field-level encryption profile.

Name (string) --Profile name for the field-level encryption profile.

CallerReference (string) --A unique number that ensures that the request can\'t be replayed.

Comment (string) --An optional comment for the field-level encryption profile.

EncryptionEntities (dict) --A complex data type of encryption entities for the field-level encryption profile that include the public key ID, provider, and field patterns for specifying which fields to encrypt with this key.

Quantity (integer) --Number of field pattern items in a field-level encryption content type-profile mapping.

Items (list) --An array of field patterns in a field-level encryption content type-profile mapping.

(dict) --Complex data type for field-level encryption profiles that includes the encryption key and field pattern specifications.

PublicKeyId (string) --The public key associated with a set of field-level encryption patterns, to be used when encrypting the fields that match the patterns.

ProviderId (string) --The provider associated with the public key being used for encryption. This value must also be provided with the private key for applications to be able to decrypt data.

FieldPatterns (dict) --Field patterns in a field-level encryption content type profile specify the fields that you want to be encrypted. You can provide the full field name, or any beginning characters followed by a wildcard (*). You can\'t overlap field patterns. For example, you can\'t have both ABC* and AB*. Note that field patterns are case-sensitive.

Quantity (integer) --The number of field-level encryption field patterns.

Items (list) --An array of the field-level encryption field patterns.

(string) --














Location (string) --The fully qualified URI of the new profile resource just created. For example: https://cloudfront.amazonaws.com/2010-11-01/field-level-encryption-profile/EDFDVBD632BHDS5 .

ETag (string) --The current version of the field level encryption profile. For example: E2QWRUHAPOMQZL .






Exceptions

CloudFront.Client.exceptions.InconsistentQuantities
CloudFront.Client.exceptions.InvalidArgument
CloudFront.Client.exceptions.NoSuchPublicKey
CloudFront.Client.exceptions.FieldLevelEncryptionProfileAlreadyExists
CloudFront.Client.exceptions.FieldLevelEncryptionProfileSizeExceeded
CloudFront.Client.exceptions.TooManyFieldLevelEncryptionProfiles
CloudFront.Client.exceptions.TooManyFieldLevelEncryptionEncryptionEntities
CloudFront.Client.exceptions.TooManyFieldLevelEncryptionFieldPatterns


    :return: {
        'FieldLevelEncryptionProfile': {
            'Id': 'string',
            'LastModifiedTime': datetime(2015, 1, 1),
            'FieldLevelEncryptionProfileConfig': {
                'Name': 'string',
                'CallerReference': 'string',
                'Comment': 'string',
                'EncryptionEntities': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'PublicKeyId': 'string',
                            'ProviderId': 'string',
                            'FieldPatterns': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                    ]
                }
            }
        },
        'Location': 'string',
        'ETag': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_invalidation(DistributionId=None, InvalidationBatch=None):
    """
    Create a new invalidation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_invalidation(
        DistributionId='string',
        InvalidationBatch={
            'Paths': {
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'CallerReference': 'string'
        }
    )
    
    
    :type DistributionId: string
    :param DistributionId: [REQUIRED]\nThe distribution\'s id.\n

    :type InvalidationBatch: dict
    :param InvalidationBatch: [REQUIRED]\nThe batch information for the invalidation.\n\nPaths (dict) -- [REQUIRED]A complex type that contains information about the objects that you want to invalidate. For more information, see Specifying the Objects to Invalidate in the Amazon CloudFront Developer Guide .\n\nQuantity (integer) -- [REQUIRED]The number of invalidation paths specified for the objects that you want to invalidate.\n\nItems (list) --A complex type that contains a list of the paths that you want to invalidate.\n\n(string) --\n\n\n\n\nCallerReference (string) -- [REQUIRED]A value that you specify to uniquely identify an invalidation request. CloudFront uses the value to prevent you from accidentally resubmitting an identical request. Whenever you create a new invalidation request, you must specify a new value for CallerReference and change other values in the request as applicable. One way to ensure that the value of CallerReference is unique is to use a timestamp , for example, 20120301090000 .\nIf you make a second invalidation request with the same value for CallerReference , and if the rest of the request is the same, CloudFront doesn\'t create a new invalidation request. Instead, CloudFront returns information about the invalidation request that you previously created with the same CallerReference .\nIf CallerReference is a value you already sent in a previous invalidation batch request but the content of any Path is different from the original request, CloudFront returns an InvalidationBatchAlreadyExists error.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Location': 'string',
    'Invalidation': {
        'Id': 'string',
        'Status': 'string',
        'CreateTime': datetime(2015, 1, 1),
        'InvalidationBatch': {
            'Paths': {
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'CallerReference': 'string'
        }
    }
}


Response Structure

(dict) --
The returned result of the corresponding request.

Location (string) --
The fully qualified URI of the distribution and invalidation batch request, including the Invalidation ID .

Invalidation (dict) --
The invalidation\'s information.

Id (string) --
The identifier for the invalidation request. For example: IDFDVBD632BHDS5 .

Status (string) --
The status of the invalidation request. When the invalidation batch is finished, the status is Completed .

CreateTime (datetime) --
The date and time the invalidation request was first made.

InvalidationBatch (dict) --
The current invalidation information for the batch request.

Paths (dict) --
A complex type that contains information about the objects that you want to invalidate. For more information, see Specifying the Objects to Invalidate in the Amazon CloudFront Developer Guide .

Quantity (integer) --
The number of invalidation paths specified for the objects that you want to invalidate.

Items (list) --
A complex type that contains a list of the paths that you want to invalidate.

(string) --




CallerReference (string) --
A value that you specify to uniquely identify an invalidation request. CloudFront uses the value to prevent you from accidentally resubmitting an identical request. Whenever you create a new invalidation request, you must specify a new value for CallerReference and change other values in the request as applicable. One way to ensure that the value of CallerReference is unique is to use a timestamp , for example, 20120301090000 .
If you make a second invalidation request with the same value for CallerReference , and if the rest of the request is the same, CloudFront doesn\'t create a new invalidation request. Instead, CloudFront returns information about the invalidation request that you previously created with the same CallerReference .
If CallerReference is a value you already sent in a previous invalidation batch request but the content of any Path is different from the original request, CloudFront returns an InvalidationBatchAlreadyExists error.











Exceptions

CloudFront.Client.exceptions.AccessDenied
CloudFront.Client.exceptions.MissingBody
CloudFront.Client.exceptions.InvalidArgument
CloudFront.Client.exceptions.NoSuchDistribution
CloudFront.Client.exceptions.BatchTooLarge
CloudFront.Client.exceptions.TooManyInvalidationsInProgress
CloudFront.Client.exceptions.InconsistentQuantities


    :return: {
        'Location': 'string',
        'Invalidation': {
            'Id': 'string',
            'Status': 'string',
            'CreateTime': datetime(2015, 1, 1),
            'InvalidationBatch': {
                'Paths': {
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'CallerReference': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_public_key(PublicKeyConfig=None):
    """
    Add a new public key to CloudFront to use, for example, for field-level encryption. You can add a maximum of 10 public keys with one AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_public_key(
        PublicKeyConfig={
            'CallerReference': 'string',
            'Name': 'string',
            'EncodedKey': 'string',
            'Comment': 'string'
        }
    )
    
    
    :type PublicKeyConfig: dict
    :param PublicKeyConfig: [REQUIRED]\nThe request to add a public key to CloudFront.\n\nCallerReference (string) -- [REQUIRED]A unique number that ensures that the request can\'t be replayed.\n\nName (string) -- [REQUIRED]The name for a public key you add to CloudFront to use with features like field-level encryption.\n\nEncodedKey (string) -- [REQUIRED]The encoded public key that you want to add to CloudFront to use with features like field-level encryption.\n\nComment (string) --An optional comment about a public key.\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'PublicKey': {
        'Id': 'string',
        'CreatedTime': datetime(2015, 1, 1),
        'PublicKeyConfig': {
            'CallerReference': 'string',
            'Name': 'string',
            'EncodedKey': 'string',
            'Comment': 'string'
        }
    },
    'Location': 'string',
    'ETag': 'string'
}


Response Structure

(dict) --
PublicKey (dict) --Returned when you add a public key.

Id (string) --A unique ID assigned to a public key you\'ve added to CloudFront.

CreatedTime (datetime) --A time you added a public key to CloudFront.

PublicKeyConfig (dict) --A complex data type for a public key you add to CloudFront to use with features like field-level encryption.

CallerReference (string) --A unique number that ensures that the request can\'t be replayed.

Name (string) --The name for a public key you add to CloudFront to use with features like field-level encryption.

EncodedKey (string) --The encoded public key that you want to add to CloudFront to use with features like field-level encryption.

Comment (string) --An optional comment about a public key.





Location (string) --The fully qualified URI of the new public key resource just created. For example: https://cloudfront.amazonaws.com/2010-11-01/cloudfront-public-key/EDFDVBD632BHDS5 .

ETag (string) --The current version of the public key. For example: E2QWRUHAPOMQZL .






Exceptions

CloudFront.Client.exceptions.PublicKeyAlreadyExists
CloudFront.Client.exceptions.InvalidArgument
CloudFront.Client.exceptions.TooManyPublicKeys


    :return: {
        'PublicKey': {
            'Id': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'PublicKeyConfig': {
                'CallerReference': 'string',
                'Name': 'string',
                'EncodedKey': 'string',
                'Comment': 'string'
            }
        },
        'Location': 'string',
        'ETag': 'string'
    }
    
    
    """
    pass

def create_streaming_distribution(StreamingDistributionConfig=None):
    """
    Creates a new RTMP distribution. An RTMP distribution is similar to a web distribution, but an RTMP distribution streams media files using the Adobe Real-Time Messaging Protocol (RTMP) instead of serving files using HTTP.
    To create a new distribution, submit a POST request to the CloudFront API version /distribution resource. The request body must include a document with a StreamingDistributionConfig element. The response echoes the StreamingDistributionConfig element and returns other information about the RTMP distribution.
    To get the status of your request, use the GET StreamingDistribution API action. When the value of Enabled is true and the value of Status is Deployed , your distribution is ready. A distribution usually deploys in less than 15 minutes.
    For more information about web distributions, see Working with RTMP Distributions in the Amazon CloudFront Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_streaming_distribution(
        StreamingDistributionConfig={
            'CallerReference': 'string',
            'S3Origin': {
                'DomainName': 'string',
                'OriginAccessIdentity': 'string'
            },
            'Aliases': {
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'Comment': 'string',
            'Logging': {
                'Enabled': True|False,
                'Bucket': 'string',
                'Prefix': 'string'
            },
            'TrustedSigners': {
                'Enabled': True|False,
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
            'Enabled': True|False
        }
    )
    
    
    :type StreamingDistributionConfig: dict
    :param StreamingDistributionConfig: [REQUIRED]\nThe streaming distribution\'s configuration information.\n\nCallerReference (string) -- [REQUIRED]A unique value (for example, a date-time stamp) that ensures that the request can\'t be replayed.\nIf the value of CallerReference is new (regardless of the content of the StreamingDistributionConfig object), CloudFront creates a new distribution.\nIf CallerReference is a value that you already sent in a previous request to create a distribution, CloudFront returns a DistributionAlreadyExists error.\n\nS3Origin (dict) -- [REQUIRED]A complex type that contains information about the Amazon S3 bucket from which you want CloudFront to get your media files for distribution.\n\nDomainName (string) -- [REQUIRED]The DNS name of the Amazon S3 origin.\n\nOriginAccessIdentity (string) -- [REQUIRED]The CloudFront origin access identity to associate with the distribution. Use an origin access identity to configure the distribution so that end users can only access objects in an Amazon S3 bucket through CloudFront.\nIf you want end users to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty OriginAccessIdentity element.\nTo delete the origin access identity from an existing distribution, update the distribution configuration and include an empty OriginAccessIdentity element.\nTo replace the origin access identity, update the distribution configuration and specify the new origin access identity.\nFor more information, see Using an Origin Access Identity to Restrict Access to Your Amazon S3 Content in the Amazon CloudFront Developer Guide .\n\n\n\nAliases (dict) --A complex type that contains information about CNAMEs (alternate domain names), if any, for this streaming distribution.\n\nQuantity (integer) -- [REQUIRED]The number of CNAME aliases, if any, that you want to associate with this distribution.\n\nItems (list) --A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.\n\n(string) --\n\n\n\n\nComment (string) -- [REQUIRED]Any comments you want to include about the streaming distribution.\n\nLogging (dict) --A complex type that controls whether access logs are written for the streaming distribution.\n\nEnabled (boolean) -- [REQUIRED]Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you don\'t want to enable logging when you create a streaming distribution or if you want to disable logging for an existing streaming distribution, specify false for Enabled , and specify empty Bucket and Prefix elements. If you specify false for Enabled but you specify values for Bucket and Prefix , the values are automatically deleted.\n\nBucket (string) -- [REQUIRED]The Amazon S3 bucket to store the access logs in, for example, myawslogbucket.s3.amazonaws.com .\n\nPrefix (string) -- [REQUIRED]An optional string that you want CloudFront to prefix to the access log filenames for this streaming distribution, for example, myprefix/ . If you want to enable logging, but you don\'t want to specify a prefix, you still must include an empty Prefix element in the Logging element.\n\n\n\nTrustedSigners (dict) -- [REQUIRED]A complex type that specifies any AWS accounts that you want to permit to create signed URLs for private content. If you want the distribution to use signed URLs, include this element; if you want the distribution to use public URLs, remove this element. For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .\n\nEnabled (boolean) -- [REQUIRED]Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .\n\nQuantity (integer) -- [REQUIRED]The number of trusted signers for this cache behavior.\n\nItems (list) --\nOptional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .\n\n(string) --\n\n\n\n\nPriceClass (string) --A complex type that contains information about price class for this streaming distribution.\n\nEnabled (boolean) -- [REQUIRED]Whether the streaming distribution is enabled to accept user requests for content.\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'StreamingDistribution': {
        'Id': 'string',
        'ARN': 'string',
        'Status': 'string',
        'LastModifiedTime': datetime(2015, 1, 1),
        'DomainName': 'string',
        'ActiveTrustedSigners': {
            'Enabled': True|False,
            'Quantity': 123,
            'Items': [
                {
                    'AwsAccountNumber': 'string',
                    'KeyPairIds': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    }
                },
            ]
        },
        'StreamingDistributionConfig': {
            'CallerReference': 'string',
            'S3Origin': {
                'DomainName': 'string',
                'OriginAccessIdentity': 'string'
            },
            'Aliases': {
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'Comment': 'string',
            'Logging': {
                'Enabled': True|False,
                'Bucket': 'string',
                'Prefix': 'string'
            },
            'TrustedSigners': {
                'Enabled': True|False,
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
            'Enabled': True|False
        }
    },
    'Location': 'string',
    'ETag': 'string'
}


Response Structure

(dict) --The returned result of the corresponding request.

StreamingDistribution (dict) --The streaming distribution\'s information.

Id (string) --The identifier for the RTMP distribution. For example: EGTXBD79EXAMPLE .

ARN (string) --The ARN (Amazon Resource Name) for the distribution. For example: arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5 , where 123456789012 is your AWS account ID.

Status (string) --The current status of the RTMP distribution. When the status is Deployed , the distribution\'s information is propagated to all CloudFront edge locations.

LastModifiedTime (datetime) --The date and time that the distribution was last modified.

DomainName (string) --The domain name that corresponds to the streaming distribution, for example, s5c39gqb8ow64r.cloudfront.net .

ActiveTrustedSigners (dict) --A complex type that lists the AWS accounts, if any, that you included in the TrustedSigners complex type for this distribution. These are the accounts that you want to allow to create signed URLs for private content.
The Signer complex type lists the AWS account number of the trusted signer or self if the signer is the AWS account that created the distribution. The Signer element also includes the IDs of any active CloudFront key pairs that are associated with the trusted signer\'s AWS account. If no KeyPairId element appears for a Signer , that signer can\'t create signed URLs.
For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .

Enabled (boolean) --Enabled is true if any of the AWS accounts listed in the TrustedSigners complex type for this distribution have active CloudFront key pairs. If not, Enabled is false .

Quantity (integer) --The number of trusted signers specified in the TrustedSigners complex type.

Items (list) --A complex type that contains one Signer complex type for each trusted signer that is specified in the TrustedSigners complex type.

(dict) --A complex type that lists the AWS accounts that were included in the TrustedSigners complex type, as well as their active CloudFront key pair IDs, if any.

AwsAccountNumber (string) --An AWS account that is included in the TrustedSigners complex type for this distribution. Valid values include:

self , which is the AWS account used to create the distribution.
An AWS account number.


KeyPairIds (dict) --A complex type that lists the active CloudFront key pairs, if any, that are associated with AwsAccountNumber .

Quantity (integer) --The number of active CloudFront key pairs for AwsAccountNumber .
For more information, see ActiveTrustedSigners .

Items (list) --A complex type that lists the active CloudFront key pairs, if any, that are associated with AwsAccountNumber .
For more information, see ActiveTrustedSigners .

(string) --










StreamingDistributionConfig (dict) --The current configuration information for the RTMP distribution.

CallerReference (string) --A unique value (for example, a date-time stamp) that ensures that the request can\'t be replayed.
If the value of CallerReference is new (regardless of the content of the StreamingDistributionConfig object), CloudFront creates a new distribution.
If CallerReference is a value that you already sent in a previous request to create a distribution, CloudFront returns a DistributionAlreadyExists error.

S3Origin (dict) --A complex type that contains information about the Amazon S3 bucket from which you want CloudFront to get your media files for distribution.

DomainName (string) --The DNS name of the Amazon S3 origin.

OriginAccessIdentity (string) --The CloudFront origin access identity to associate with the distribution. Use an origin access identity to configure the distribution so that end users can only access objects in an Amazon S3 bucket through CloudFront.
If you want end users to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty OriginAccessIdentity element.
To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty OriginAccessIdentity element.
To replace the origin access identity, update the distribution configuration and specify the new origin access identity.
For more information, see Using an Origin Access Identity to Restrict Access to Your Amazon S3 Content in the Amazon CloudFront Developer Guide .



Aliases (dict) --A complex type that contains information about CNAMEs (alternate domain names), if any, for this streaming distribution.

Quantity (integer) --The number of CNAME aliases, if any, that you want to associate with this distribution.

Items (list) --A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.

(string) --




Comment (string) --Any comments you want to include about the streaming distribution.

Logging (dict) --A complex type that controls whether access logs are written for the streaming distribution.

Enabled (boolean) --Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you don\'t want to enable logging when you create a streaming distribution or if you want to disable logging for an existing streaming distribution, specify false for Enabled , and specify empty Bucket and Prefix elements. If you specify false for Enabled but you specify values for Bucket and Prefix , the values are automatically deleted.

Bucket (string) --The Amazon S3 bucket to store the access logs in, for example, myawslogbucket.s3.amazonaws.com .

Prefix (string) --An optional string that you want CloudFront to prefix to the access log filenames for this streaming distribution, for example, myprefix/ . If you want to enable logging, but you don\'t want to specify a prefix, you still must include an empty Prefix element in the Logging element.



TrustedSigners (dict) --A complex type that specifies any AWS accounts that you want to permit to create signed URLs for private content. If you want the distribution to use signed URLs, include this element; if you want the distribution to use public URLs, remove this element. For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .

Enabled (boolean) --Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .

Quantity (integer) --The number of trusted signers for this cache behavior.

Items (list) --
Optional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .

(string) --




PriceClass (string) --A complex type that contains information about price class for this streaming distribution.

Enabled (boolean) --Whether the streaming distribution is enabled to accept user requests for content.





Location (string) --The fully qualified URI of the new streaming distribution resource just created. For example: https://cloudfront.amazonaws.com/2010-11-01/streaming-distribution/EGTXBD79H29TRA8 .

ETag (string) --The current version of the streaming distribution created.






Exceptions

CloudFront.Client.exceptions.CNAMEAlreadyExists
CloudFront.Client.exceptions.StreamingDistributionAlreadyExists
CloudFront.Client.exceptions.InvalidOrigin
CloudFront.Client.exceptions.InvalidOriginAccessIdentity
CloudFront.Client.exceptions.AccessDenied
CloudFront.Client.exceptions.TooManyTrustedSigners
CloudFront.Client.exceptions.TrustedSignerDoesNotExist
CloudFront.Client.exceptions.MissingBody
CloudFront.Client.exceptions.TooManyStreamingDistributionCNAMEs
CloudFront.Client.exceptions.TooManyStreamingDistributions
CloudFront.Client.exceptions.InvalidArgument
CloudFront.Client.exceptions.InconsistentQuantities


    :return: {
        'StreamingDistribution': {
            'Id': 'string',
            'ARN': 'string',
            'Status': 'string',
            'LastModifiedTime': datetime(2015, 1, 1),
            'DomainName': 'string',
            'ActiveTrustedSigners': {
                'Enabled': True|False,
                'Quantity': 123,
                'Items': [
                    {
                        'AwsAccountNumber': 'string',
                        'KeyPairIds': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                ]
            },
            'StreamingDistributionConfig': {
                'CallerReference': 'string',
                'S3Origin': {
                    'DomainName': 'string',
                    'OriginAccessIdentity': 'string'
                },
                'Aliases': {
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'Comment': 'string',
                'Logging': {
                    'Enabled': True|False,
                    'Bucket': 'string',
                    'Prefix': 'string'
                },
                'TrustedSigners': {
                    'Enabled': True|False,
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
                'Enabled': True|False
            }
        },
        'Location': 'string',
        'ETag': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_streaming_distribution_with_tags(StreamingDistributionConfigWithTags=None):
    """
    Create a new streaming distribution with tags.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_streaming_distribution_with_tags(
        StreamingDistributionConfigWithTags={
            'StreamingDistributionConfig': {
                'CallerReference': 'string',
                'S3Origin': {
                    'DomainName': 'string',
                    'OriginAccessIdentity': 'string'
                },
                'Aliases': {
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'Comment': 'string',
                'Logging': {
                    'Enabled': True|False,
                    'Bucket': 'string',
                    'Prefix': 'string'
                },
                'TrustedSigners': {
                    'Enabled': True|False,
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
                'Enabled': True|False
            },
            'Tags': {
                'Items': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
        }
    )
    
    
    :type StreamingDistributionConfigWithTags: dict
    :param StreamingDistributionConfigWithTags: [REQUIRED]\nThe streaming distribution\'s configuration information.\n\nStreamingDistributionConfig (dict) -- [REQUIRED]A streaming distribution Configuration.\n\nCallerReference (string) -- [REQUIRED]A unique value (for example, a date-time stamp) that ensures that the request can\'t be replayed.\nIf the value of CallerReference is new (regardless of the content of the StreamingDistributionConfig object), CloudFront creates a new distribution.\nIf CallerReference is a value that you already sent in a previous request to create a distribution, CloudFront returns a DistributionAlreadyExists error.\n\nS3Origin (dict) -- [REQUIRED]A complex type that contains information about the Amazon S3 bucket from which you want CloudFront to get your media files for distribution.\n\nDomainName (string) -- [REQUIRED]The DNS name of the Amazon S3 origin.\n\nOriginAccessIdentity (string) -- [REQUIRED]The CloudFront origin access identity to associate with the distribution. Use an origin access identity to configure the distribution so that end users can only access objects in an Amazon S3 bucket through CloudFront.\nIf you want end users to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty OriginAccessIdentity element.\nTo delete the origin access identity from an existing distribution, update the distribution configuration and include an empty OriginAccessIdentity element.\nTo replace the origin access identity, update the distribution configuration and specify the new origin access identity.\nFor more information, see Using an Origin Access Identity to Restrict Access to Your Amazon S3 Content in the Amazon CloudFront Developer Guide .\n\n\n\nAliases (dict) --A complex type that contains information about CNAMEs (alternate domain names), if any, for this streaming distribution.\n\nQuantity (integer) -- [REQUIRED]The number of CNAME aliases, if any, that you want to associate with this distribution.\n\nItems (list) --A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.\n\n(string) --\n\n\n\n\nComment (string) -- [REQUIRED]Any comments you want to include about the streaming distribution.\n\nLogging (dict) --A complex type that controls whether access logs are written for the streaming distribution.\n\nEnabled (boolean) -- [REQUIRED]Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you don\'t want to enable logging when you create a streaming distribution or if you want to disable logging for an existing streaming distribution, specify false for Enabled , and specify empty Bucket and Prefix elements. If you specify false for Enabled but you specify values for Bucket and Prefix , the values are automatically deleted.\n\nBucket (string) -- [REQUIRED]The Amazon S3 bucket to store the access logs in, for example, myawslogbucket.s3.amazonaws.com .\n\nPrefix (string) -- [REQUIRED]An optional string that you want CloudFront to prefix to the access log filenames for this streaming distribution, for example, myprefix/ . If you want to enable logging, but you don\'t want to specify a prefix, you still must include an empty Prefix element in the Logging element.\n\n\n\nTrustedSigners (dict) -- [REQUIRED]A complex type that specifies any AWS accounts that you want to permit to create signed URLs for private content. If you want the distribution to use signed URLs, include this element; if you want the distribution to use public URLs, remove this element. For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .\n\nEnabled (boolean) -- [REQUIRED]Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .\n\nQuantity (integer) -- [REQUIRED]The number of trusted signers for this cache behavior.\n\nItems (list) --\nOptional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .\n\n(string) --\n\n\n\n\nPriceClass (string) --A complex type that contains information about price class for this streaming distribution.\n\nEnabled (boolean) -- [REQUIRED]Whether the streaming distribution is enabled to accept user requests for content.\n\n\n\nTags (dict) -- [REQUIRED]A complex type that contains zero or more Tag elements.\n\nItems (list) --A complex type that contains Tag elements.\n\n(dict) --A complex type that contains Tag key and Tag value.\n\nKey (string) -- [REQUIRED]A string that contains Tag key.\nThe string length should be between 1 and 128 characters. Valid characters include a-z , A-Z , 0-9 , space, and the special characters _ - . : / = + @ .\n\nValue (string) --A string that contains an optional Tag value.\nThe string length should be between 0 and 256 characters. Valid characters include a-z , A-Z , 0-9 , space, and the special characters _ - . : / = + @ .\n\n\n\n\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'StreamingDistribution': {
        'Id': 'string',
        'ARN': 'string',
        'Status': 'string',
        'LastModifiedTime': datetime(2015, 1, 1),
        'DomainName': 'string',
        'ActiveTrustedSigners': {
            'Enabled': True|False,
            'Quantity': 123,
            'Items': [
                {
                    'AwsAccountNumber': 'string',
                    'KeyPairIds': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    }
                },
            ]
        },
        'StreamingDistributionConfig': {
            'CallerReference': 'string',
            'S3Origin': {
                'DomainName': 'string',
                'OriginAccessIdentity': 'string'
            },
            'Aliases': {
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'Comment': 'string',
            'Logging': {
                'Enabled': True|False,
                'Bucket': 'string',
                'Prefix': 'string'
            },
            'TrustedSigners': {
                'Enabled': True|False,
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
            'Enabled': True|False
        }
    },
    'Location': 'string',
    'ETag': 'string'
}


Response Structure

(dict) --The returned result of the corresponding request.

StreamingDistribution (dict) --The streaming distribution\'s information.

Id (string) --The identifier for the RTMP distribution. For example: EGTXBD79EXAMPLE .

ARN (string) --The ARN (Amazon Resource Name) for the distribution. For example: arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5 , where 123456789012 is your AWS account ID.

Status (string) --The current status of the RTMP distribution. When the status is Deployed , the distribution\'s information is propagated to all CloudFront edge locations.

LastModifiedTime (datetime) --The date and time that the distribution was last modified.

DomainName (string) --The domain name that corresponds to the streaming distribution, for example, s5c39gqb8ow64r.cloudfront.net .

ActiveTrustedSigners (dict) --A complex type that lists the AWS accounts, if any, that you included in the TrustedSigners complex type for this distribution. These are the accounts that you want to allow to create signed URLs for private content.
The Signer complex type lists the AWS account number of the trusted signer or self if the signer is the AWS account that created the distribution. The Signer element also includes the IDs of any active CloudFront key pairs that are associated with the trusted signer\'s AWS account. If no KeyPairId element appears for a Signer , that signer can\'t create signed URLs.
For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .

Enabled (boolean) --Enabled is true if any of the AWS accounts listed in the TrustedSigners complex type for this distribution have active CloudFront key pairs. If not, Enabled is false .

Quantity (integer) --The number of trusted signers specified in the TrustedSigners complex type.

Items (list) --A complex type that contains one Signer complex type for each trusted signer that is specified in the TrustedSigners complex type.

(dict) --A complex type that lists the AWS accounts that were included in the TrustedSigners complex type, as well as their active CloudFront key pair IDs, if any.

AwsAccountNumber (string) --An AWS account that is included in the TrustedSigners complex type for this distribution. Valid values include:

self , which is the AWS account used to create the distribution.
An AWS account number.


KeyPairIds (dict) --A complex type that lists the active CloudFront key pairs, if any, that are associated with AwsAccountNumber .

Quantity (integer) --The number of active CloudFront key pairs for AwsAccountNumber .
For more information, see ActiveTrustedSigners .

Items (list) --A complex type that lists the active CloudFront key pairs, if any, that are associated with AwsAccountNumber .
For more information, see ActiveTrustedSigners .

(string) --










StreamingDistributionConfig (dict) --The current configuration information for the RTMP distribution.

CallerReference (string) --A unique value (for example, a date-time stamp) that ensures that the request can\'t be replayed.
If the value of CallerReference is new (regardless of the content of the StreamingDistributionConfig object), CloudFront creates a new distribution.
If CallerReference is a value that you already sent in a previous request to create a distribution, CloudFront returns a DistributionAlreadyExists error.

S3Origin (dict) --A complex type that contains information about the Amazon S3 bucket from which you want CloudFront to get your media files for distribution.

DomainName (string) --The DNS name of the Amazon S3 origin.

OriginAccessIdentity (string) --The CloudFront origin access identity to associate with the distribution. Use an origin access identity to configure the distribution so that end users can only access objects in an Amazon S3 bucket through CloudFront.
If you want end users to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty OriginAccessIdentity element.
To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty OriginAccessIdentity element.
To replace the origin access identity, update the distribution configuration and specify the new origin access identity.
For more information, see Using an Origin Access Identity to Restrict Access to Your Amazon S3 Content in the Amazon CloudFront Developer Guide .



Aliases (dict) --A complex type that contains information about CNAMEs (alternate domain names), if any, for this streaming distribution.

Quantity (integer) --The number of CNAME aliases, if any, that you want to associate with this distribution.

Items (list) --A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.

(string) --




Comment (string) --Any comments you want to include about the streaming distribution.

Logging (dict) --A complex type that controls whether access logs are written for the streaming distribution.

Enabled (boolean) --Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you don\'t want to enable logging when you create a streaming distribution or if you want to disable logging for an existing streaming distribution, specify false for Enabled , and specify empty Bucket and Prefix elements. If you specify false for Enabled but you specify values for Bucket and Prefix , the values are automatically deleted.

Bucket (string) --The Amazon S3 bucket to store the access logs in, for example, myawslogbucket.s3.amazonaws.com .

Prefix (string) --An optional string that you want CloudFront to prefix to the access log filenames for this streaming distribution, for example, myprefix/ . If you want to enable logging, but you don\'t want to specify a prefix, you still must include an empty Prefix element in the Logging element.



TrustedSigners (dict) --A complex type that specifies any AWS accounts that you want to permit to create signed URLs for private content. If you want the distribution to use signed URLs, include this element; if you want the distribution to use public URLs, remove this element. For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .

Enabled (boolean) --Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .

Quantity (integer) --The number of trusted signers for this cache behavior.

Items (list) --
Optional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .

(string) --




PriceClass (string) --A complex type that contains information about price class for this streaming distribution.

Enabled (boolean) --Whether the streaming distribution is enabled to accept user requests for content.





Location (string) --The fully qualified URI of the new streaming distribution resource just created. For example:https://cloudfront.amazonaws.com/2010-11-01/streaming-distribution/EGTXBD79H29TRA8 .

ETag (string) --The current version of the distribution created.






Exceptions

CloudFront.Client.exceptions.CNAMEAlreadyExists
CloudFront.Client.exceptions.StreamingDistributionAlreadyExists
CloudFront.Client.exceptions.InvalidOrigin
CloudFront.Client.exceptions.InvalidOriginAccessIdentity
CloudFront.Client.exceptions.AccessDenied
CloudFront.Client.exceptions.TooManyTrustedSigners
CloudFront.Client.exceptions.TrustedSignerDoesNotExist
CloudFront.Client.exceptions.MissingBody
CloudFront.Client.exceptions.TooManyStreamingDistributionCNAMEs
CloudFront.Client.exceptions.TooManyStreamingDistributions
CloudFront.Client.exceptions.InvalidArgument
CloudFront.Client.exceptions.InconsistentQuantities
CloudFront.Client.exceptions.InvalidTagging


    :return: {
        'StreamingDistribution': {
            'Id': 'string',
            'ARN': 'string',
            'Status': 'string',
            'LastModifiedTime': datetime(2015, 1, 1),
            'DomainName': 'string',
            'ActiveTrustedSigners': {
                'Enabled': True|False,
                'Quantity': 123,
                'Items': [
                    {
                        'AwsAccountNumber': 'string',
                        'KeyPairIds': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                ]
            },
            'StreamingDistributionConfig': {
                'CallerReference': 'string',
                'S3Origin': {
                    'DomainName': 'string',
                    'OriginAccessIdentity': 'string'
                },
                'Aliases': {
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'Comment': 'string',
                'Logging': {
                    'Enabled': True|False,
                    'Bucket': 'string',
                    'Prefix': 'string'
                },
                'TrustedSigners': {
                    'Enabled': True|False,
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
                'Enabled': True|False
            }
        },
        'Location': 'string',
        'ETag': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_cloud_front_origin_access_identity(Id=None, IfMatch=None):
    """
    Delete an origin access identity.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_cloud_front_origin_access_identity(
        Id='string',
        IfMatch='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe origin access identity\'s ID.\n

    :type IfMatch: string
    :param IfMatch: The value of the ETag header you received from a previous GET or PUT request. For example: E2QWRUHAPOMQZL .

    :returns: 
    CloudFront.Client.exceptions.AccessDenied
    CloudFront.Client.exceptions.InvalidIfMatchVersion
    CloudFront.Client.exceptions.NoSuchCloudFrontOriginAccessIdentity
    CloudFront.Client.exceptions.PreconditionFailed
    CloudFront.Client.exceptions.CloudFrontOriginAccessIdentityInUse
    
    """
    pass

def delete_distribution(Id=None, IfMatch=None):
    """
    Delete a distribution.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_distribution(
        Id='string',
        IfMatch='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe distribution ID.\n

    :type IfMatch: string
    :param IfMatch: The value of the ETag header that you received when you disabled the distribution. For example: E2QWRUHAPOMQZL .

    :returns: 
    CloudFront.Client.exceptions.AccessDenied
    CloudFront.Client.exceptions.DistributionNotDisabled
    CloudFront.Client.exceptions.InvalidIfMatchVersion
    CloudFront.Client.exceptions.NoSuchDistribution
    CloudFront.Client.exceptions.PreconditionFailed
    
    """
    pass

def delete_field_level_encryption_config(Id=None, IfMatch=None):
    """
    Remove a field-level encryption configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_field_level_encryption_config(
        Id='string',
        IfMatch='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe ID of the configuration you want to delete from CloudFront.\n

    :type IfMatch: string
    :param IfMatch: The value of the ETag header that you received when retrieving the configuration identity to delete. For example: E2QWRUHAPOMQZL .

    :returns: 
    CloudFront.Client.exceptions.AccessDenied
    CloudFront.Client.exceptions.InvalidIfMatchVersion
    CloudFront.Client.exceptions.NoSuchFieldLevelEncryptionConfig
    CloudFront.Client.exceptions.PreconditionFailed
    CloudFront.Client.exceptions.FieldLevelEncryptionConfigInUse
    
    """
    pass

def delete_field_level_encryption_profile(Id=None, IfMatch=None):
    """
    Remove a field-level encryption profile.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_field_level_encryption_profile(
        Id='string',
        IfMatch='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nRequest the ID of the profile you want to delete from CloudFront.\n

    :type IfMatch: string
    :param IfMatch: The value of the ETag header that you received when retrieving the profile to delete. For example: E2QWRUHAPOMQZL .

    :returns: 
    CloudFront.Client.exceptions.AccessDenied
    CloudFront.Client.exceptions.InvalidIfMatchVersion
    CloudFront.Client.exceptions.NoSuchFieldLevelEncryptionProfile
    CloudFront.Client.exceptions.PreconditionFailed
    CloudFront.Client.exceptions.FieldLevelEncryptionProfileInUse
    
    """
    pass

def delete_public_key(Id=None, IfMatch=None):
    """
    Remove a public key you previously added to CloudFront.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_public_key(
        Id='string',
        IfMatch='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe ID of the public key you want to remove from CloudFront.\n

    :type IfMatch: string
    :param IfMatch: The value of the ETag header that you received when retrieving the public key identity to delete. For example: E2QWRUHAPOMQZL .

    :returns: 
    CloudFront.Client.exceptions.AccessDenied
    CloudFront.Client.exceptions.PublicKeyInUse
    CloudFront.Client.exceptions.InvalidIfMatchVersion
    CloudFront.Client.exceptions.NoSuchPublicKey
    CloudFront.Client.exceptions.PreconditionFailed
    
    """
    pass

def delete_streaming_distribution(Id=None, IfMatch=None):
    """
    Delete a streaming distribution. To delete an RTMP distribution using the CloudFront API, perform the following steps.
    For information about deleting a distribution using the CloudFront console, see Deleting a Distribution in the Amazon CloudFront Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_streaming_distribution(
        Id='string',
        IfMatch='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe distribution ID.\n

    :type IfMatch: string
    :param IfMatch: The value of the ETag header that you received when you disabled the streaming distribution. For example: E2QWRUHAPOMQZL .

    :returns: 
    Id (string) -- [REQUIRED]
    The distribution ID.
    
    IfMatch (string) -- The value of the ETag header that you received when you disabled the streaming distribution. For example: E2QWRUHAPOMQZL .
    
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

def get_cloud_front_origin_access_identity(Id=None):
    """
    Get the information about an origin access identity.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_cloud_front_origin_access_identity(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe identity\'s ID.\n

    :rtype: dict
ReturnsResponse Syntax{
    'CloudFrontOriginAccessIdentity': {
        'Id': 'string',
        'S3CanonicalUserId': 'string',
        'CloudFrontOriginAccessIdentityConfig': {
            'CallerReference': 'string',
            'Comment': 'string'
        }
    },
    'ETag': 'string'
}


Response Structure

(dict) --The returned result of the corresponding request.

CloudFrontOriginAccessIdentity (dict) --The origin access identity\'s information.

Id (string) --The ID for the origin access identity, for example, E74FTE3AJFJ256A .

S3CanonicalUserId (string) --The Amazon S3 canonical user ID for the origin access identity, used when giving the origin access identity read permission to an object in Amazon S3.

CloudFrontOriginAccessIdentityConfig (dict) --The current configuration information for the identity.

CallerReference (string) --A unique value (for example, a date-time stamp) that ensures that the request can\'t be replayed.
If the value of CallerReference is new (regardless of the content of the CloudFrontOriginAccessIdentityConfig object), a new origin access identity is created.
If the CallerReference is a value already sent in a previous identity request, and the content of the CloudFrontOriginAccessIdentityConfig is identical to the original request (ignoring white space), the response includes the same information returned to the original request.
If the CallerReference is a value you already sent in a previous request to create an identity, but the content of the CloudFrontOriginAccessIdentityConfig is different from the original request, CloudFront returns a CloudFrontOriginAccessIdentityAlreadyExists error.

Comment (string) --Any comments you want to include about the origin access identity.





ETag (string) --The current version of the origin access identity\'s information. For example: E2QWRUHAPOMQZL .






Exceptions

CloudFront.Client.exceptions.NoSuchCloudFrontOriginAccessIdentity
CloudFront.Client.exceptions.AccessDenied


    :return: {
        'CloudFrontOriginAccessIdentity': {
            'Id': 'string',
            'S3CanonicalUserId': 'string',
            'CloudFrontOriginAccessIdentityConfig': {
                'CallerReference': 'string',
                'Comment': 'string'
            }
        },
        'ETag': 'string'
    }
    
    
    """
    pass

def get_cloud_front_origin_access_identity_config(Id=None):
    """
    Get the configuration information about an origin access identity.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_cloud_front_origin_access_identity_config(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe identity\'s ID.\n

    :rtype: dict
ReturnsResponse Syntax{
    'CloudFrontOriginAccessIdentityConfig': {
        'CallerReference': 'string',
        'Comment': 'string'
    },
    'ETag': 'string'
}


Response Structure

(dict) --The returned result of the corresponding request.

CloudFrontOriginAccessIdentityConfig (dict) --The origin access identity\'s configuration information.

CallerReference (string) --A unique value (for example, a date-time stamp) that ensures that the request can\'t be replayed.
If the value of CallerReference is new (regardless of the content of the CloudFrontOriginAccessIdentityConfig object), a new origin access identity is created.
If the CallerReference is a value already sent in a previous identity request, and the content of the CloudFrontOriginAccessIdentityConfig is identical to the original request (ignoring white space), the response includes the same information returned to the original request.
If the CallerReference is a value you already sent in a previous request to create an identity, but the content of the CloudFrontOriginAccessIdentityConfig is different from the original request, CloudFront returns a CloudFrontOriginAccessIdentityAlreadyExists error.

Comment (string) --Any comments you want to include about the origin access identity.



ETag (string) --The current version of the configuration. For example: E2QWRUHAPOMQZL .






Exceptions

CloudFront.Client.exceptions.NoSuchCloudFrontOriginAccessIdentity
CloudFront.Client.exceptions.AccessDenied


    :return: {
        'CloudFrontOriginAccessIdentityConfig': {
            'CallerReference': 'string',
            'Comment': 'string'
        },
        'ETag': 'string'
    }
    
    
    """
    pass

def get_distribution(Id=None):
    """
    Get the information about a distribution.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_distribution(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe distribution\'s ID. If the ID is empty, an empty distribution configuration is returned.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Distribution': {
        'Id': 'string',
        'ARN': 'string',
        'Status': 'string',
        'LastModifiedTime': datetime(2015, 1, 1),
        'InProgressInvalidationBatches': 123,
        'DomainName': 'string',
        'ActiveTrustedSigners': {
            'Enabled': True|False,
            'Quantity': 123,
            'Items': [
                {
                    'AwsAccountNumber': 'string',
                    'KeyPairIds': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    }
                },
            ]
        },
        'DistributionConfig': {
            'CallerReference': 'string',
            'Aliases': {
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'DefaultRootObject': 'string',
            'Origins': {
                'Quantity': 123,
                'Items': [
                    {
                        'Id': 'string',
                        'DomainName': 'string',
                        'OriginPath': 'string',
                        'CustomHeaders': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'HeaderName': 'string',
                                    'HeaderValue': 'string'
                                },
                            ]
                        },
                        'S3OriginConfig': {
                            'OriginAccessIdentity': 'string'
                        },
                        'CustomOriginConfig': {
                            'HTTPPort': 123,
                            'HTTPSPort': 123,
                            'OriginProtocolPolicy': 'http-only'|'match-viewer'|'https-only',
                            'OriginSslProtocols': {
                                'Quantity': 123,
                                'Items': [
                                    'SSLv3'|'TLSv1'|'TLSv1.1'|'TLSv1.2',
                                ]
                            },
                            'OriginReadTimeout': 123,
                            'OriginKeepaliveTimeout': 123
                        }
                    },
                ]
            },
            'OriginGroups': {
                'Quantity': 123,
                'Items': [
                    {
                        'Id': 'string',
                        'FailoverCriteria': {
                            'StatusCodes': {
                                'Quantity': 123,
                                'Items': [
                                    123,
                                ]
                            }
                        },
                        'Members': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'OriginId': 'string'
                                },
                            ]
                        }
                    },
                ]
            },
            'DefaultCacheBehavior': {
                'TargetOriginId': 'string',
                'ForwardedValues': {
                    'QueryString': True|False,
                    'Cookies': {
                        'Forward': 'none'|'whitelist'|'all',
                        'WhitelistedNames': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                    'Headers': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    },
                    'QueryStringCacheKeys': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    }
                },
                'TrustedSigners': {
                    'Enabled': True|False,
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                'MinTTL': 123,
                'AllowedMethods': {
                    'Quantity': 123,
                    'Items': [
                        'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                    ],
                    'CachedMethods': {
                        'Quantity': 123,
                        'Items': [
                            'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                        ]
                    }
                },
                'SmoothStreaming': True|False,
                'DefaultTTL': 123,
                'MaxTTL': 123,
                'Compress': True|False,
                'LambdaFunctionAssociations': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'LambdaFunctionARN': 'string',
                            'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                            'IncludeBody': True|False
                        },
                    ]
                },
                'FieldLevelEncryptionId': 'string'
            },
            'CacheBehaviors': {
                'Quantity': 123,
                'Items': [
                    {
                        'PathPattern': 'string',
                        'TargetOriginId': 'string',
                        'ForwardedValues': {
                            'QueryString': True|False,
                            'Cookies': {
                                'Forward': 'none'|'whitelist'|'all',
                                'WhitelistedNames': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                }
                            },
                            'Headers': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            },
                            'QueryStringCacheKeys': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                        'TrustedSigners': {
                            'Enabled': True|False,
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        },
                        'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                        'MinTTL': 123,
                        'AllowedMethods': {
                            'Quantity': 123,
                            'Items': [
                                'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                            ],
                            'CachedMethods': {
                                'Quantity': 123,
                                'Items': [
                                    'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                ]
                            }
                        },
                        'SmoothStreaming': True|False,
                        'DefaultTTL': 123,
                        'MaxTTL': 123,
                        'Compress': True|False,
                        'LambdaFunctionAssociations': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'LambdaFunctionARN': 'string',
                                    'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                    'IncludeBody': True|False
                                },
                            ]
                        },
                        'FieldLevelEncryptionId': 'string'
                    },
                ]
            },
            'CustomErrorResponses': {
                'Quantity': 123,
                'Items': [
                    {
                        'ErrorCode': 123,
                        'ResponsePagePath': 'string',
                        'ResponseCode': 'string',
                        'ErrorCachingMinTTL': 123
                    },
                ]
            },
            'Comment': 'string',
            'Logging': {
                'Enabled': True|False,
                'IncludeCookies': True|False,
                'Bucket': 'string',
                'Prefix': 'string'
            },
            'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
            'Enabled': True|False,
            'ViewerCertificate': {
                'CloudFrontDefaultCertificate': True|False,
                'IAMCertificateId': 'string',
                'ACMCertificateArn': 'string',
                'SSLSupportMethod': 'sni-only'|'vip',
                'MinimumProtocolVersion': 'SSLv3'|'TLSv1'|'TLSv1_2016'|'TLSv1.1_2016'|'TLSv1.2_2018',
                'Certificate': 'string',
                'CertificateSource': 'cloudfront'|'iam'|'acm'
            },
            'Restrictions': {
                'GeoRestriction': {
                    'RestrictionType': 'blacklist'|'whitelist'|'none',
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                }
            },
            'WebACLId': 'string',
            'HttpVersion': 'http1.1'|'http2',
            'IsIPV6Enabled': True|False
        },
        'AliasICPRecordals': [
            {
                'CNAME': 'string',
                'ICPRecordalStatus': 'APPROVED'|'SUSPENDED'|'PENDING'
            },
        ]
    },
    'ETag': 'string'
}


Response Structure

(dict) --The returned result of the corresponding request.

Distribution (dict) --The distribution\'s information.

Id (string) --The identifier for the distribution. For example: EDFDVBD632BHDS5 .

ARN (string) --The ARN (Amazon Resource Name) for the distribution. For example: arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5 , where 123456789012 is your AWS account ID.

Status (string) --This response element indicates the current status of the distribution. When the status is Deployed , the distribution\'s information is fully propagated to all CloudFront edge locations.

LastModifiedTime (datetime) --The date and time the distribution was last modified.

InProgressInvalidationBatches (integer) --The number of invalidation batches currently in progress.

DomainName (string) --The domain name corresponding to the distribution, for example, d111111abcdef8.cloudfront.net .

ActiveTrustedSigners (dict) --CloudFront automatically adds this element to the response only if you\'ve set up the distribution to serve private content with signed URLs. The element lists the key pair IDs that CloudFront is aware of for each trusted signer. The Signer child element lists the AWS account number of the trusted signer (or an empty Self element if the signer is you). The Signer element also includes the IDs of any active key pairs associated with the trusted signer\'s AWS account. If no KeyPairId element appears for a Signer , that signer can\'t create working signed URLs.

Enabled (boolean) --Enabled is true if any of the AWS accounts listed in the TrustedSigners complex type for this distribution have active CloudFront key pairs. If not, Enabled is false .

Quantity (integer) --The number of trusted signers specified in the TrustedSigners complex type.

Items (list) --A complex type that contains one Signer complex type for each trusted signer that is specified in the TrustedSigners complex type.

(dict) --A complex type that lists the AWS accounts that were included in the TrustedSigners complex type, as well as their active CloudFront key pair IDs, if any.

AwsAccountNumber (string) --An AWS account that is included in the TrustedSigners complex type for this distribution. Valid values include:

self , which is the AWS account used to create the distribution.
An AWS account number.


KeyPairIds (dict) --A complex type that lists the active CloudFront key pairs, if any, that are associated with AwsAccountNumber .

Quantity (integer) --The number of active CloudFront key pairs for AwsAccountNumber .
For more information, see ActiveTrustedSigners .

Items (list) --A complex type that lists the active CloudFront key pairs, if any, that are associated with AwsAccountNumber .
For more information, see ActiveTrustedSigners .

(string) --










DistributionConfig (dict) --The current configuration information for the distribution. Send a GET request to the /*CloudFront API version* /distribution ID/config resource.

CallerReference (string) --A unique value (for example, a date-time stamp) that ensures that the request can\'t be replayed.
If the value of CallerReference is new (regardless of the content of the DistributionConfig object), CloudFront creates a new distribution.
If CallerReference is a value that you already sent in a previous request to create a distribution, CloudFront returns a DistributionAlreadyExists error.

Aliases (dict) --A complex type that contains information about CNAMEs (alternate domain names), if any, for this distribution.

Quantity (integer) --The number of CNAME aliases, if any, that you want to associate with this distribution.

Items (list) --A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.

(string) --




DefaultRootObject (string) --The object that you want CloudFront to request from your origin (for example, index.html ) when a viewer requests the root URL for your distribution (http://www.example.com ) instead of an object in your distribution (http://www.example.com/product-description.html ). Specifying a default root object avoids exposing the contents of your distribution.
Specify only the object name, for example, index.html . Don\'t add a / before the object name.
If you don\'t want to specify a default root object when you create a distribution, include an empty DefaultRootObject element.
To delete the default root object from an existing distribution, update the distribution configuration and include an empty DefaultRootObject element.
To replace the default root object, update the distribution configuration and specify the new object.
For more information about the default root object, see Creating a Default Root Object in the Amazon CloudFront Developer Guide .

Origins (dict) --A complex type that contains information about origins for this distribution.

Quantity (integer) --The number of origins or origin groups for this distribution.

Items (list) --A complex type that contains origins or origin groups for this distribution.

(dict) --A complex type that describes the Amazon S3 bucket, HTTP server (for example, a web server), Amazon MediaStore, or other server from which CloudFront gets your files. This can also be an origin group, if you\'ve created an origin group. You must specify at least one origin or origin group.
For the current limit on the number of origins or origin groups that you can specify for a distribution, see Amazon CloudFront Limits in the AWS General Reference .

Id (string) --A unique identifier for the origin or origin group. The value of Id must be unique within the distribution.
When you specify the value of TargetOriginId for the default cache behavior or for another cache behavior, you indicate the origin to which you want the cache behavior to route requests by specifying the value of the Id element for that origin. When a request matches the path pattern for that cache behavior, CloudFront routes the request to the specified origin. For more information, see Cache Behavior Settings in the Amazon CloudFront Developer Guide .

DomainName (string) --
Amazon S3 origins : The DNS name of the Amazon S3 bucket from which you want CloudFront to get objects for this origin, for example, myawsbucket.s3.amazonaws.com . If you set up your bucket to be configured as a website endpoint, enter the Amazon S3 static website hosting endpoint for the bucket.
For more information about specifying this value for different types of origins, see Origin Domain Name in the Amazon CloudFront Developer Guide .
Constraints for Amazon S3 origins:

If you configured Amazon S3 Transfer Acceleration for your bucket, don\'t specify the s3-accelerate endpoint for DomainName .
The bucket name must be between 3 and 63 characters long (inclusive).
The bucket name must contain only lowercase characters, numbers, periods, underscores, and dashes.
The bucket name must not contain adjacent periods.


Custom Origins : The DNS domain name for the HTTP server from which you want CloudFront to get objects for this origin, for example, www.example.com .
Constraints for custom origins:

DomainName must be a valid DNS name that contains only a-z, A-Z, 0-9, dot (.), hyphen (-), or underscore (_) characters.
The name cannot exceed 128 characters.


OriginPath (string) --An optional element that causes CloudFront to request your content from a directory in your Amazon S3 bucket or your custom origin. When you include the OriginPath element, specify the directory name, beginning with a / . CloudFront appends the directory name to the value of DomainName , for example, example.com/production . Do not include a / at the end of the directory name.
For example, suppose you\'ve specified the following values for your distribution:

DomainName : An Amazon S3 bucket named myawsbucket .
OriginPath : /production
CNAME : example.com

When a user enters example.com/index.html in a browser, CloudFront sends a request to Amazon S3 for myawsbucket/production/index.html .
When a user enters example.com/acme/index.html in a browser, CloudFront sends a request to Amazon S3 for myawsbucket/production/acme/index.html .

CustomHeaders (dict) --A complex type that contains names and values for the custom headers that you want.

Quantity (integer) --The number of custom headers, if any, for this distribution.

Items (list) --
Optional : A list that contains one OriginCustomHeader element for each custom header that you want CloudFront to forward to the origin. If Quantity is 0 , omit Items .

(dict) --A complex type that contains HeaderName and HeaderValue elements, if any, for this distribution.

HeaderName (string) --The name of a header that you want CloudFront to forward to your origin. For more information, see Forwarding Custom Headers to Your Origin (Web Distributions Only) in the Amazon CloudFront Developer Guide .

HeaderValue (string) --The value for the header that you specified in the HeaderName field.







S3OriginConfig (dict) --A complex type that contains information about the Amazon S3 origin. If the origin is a custom origin, use the CustomOriginConfig element instead.

OriginAccessIdentity (string) --The CloudFront origin access identity to associate with the origin. Use an origin access identity to configure the origin so that viewers can only access objects in an Amazon S3 bucket through CloudFront. The format of the value is:
origin-access-identity/cloudfront/ID-of-origin-access-identity
where `` ID-of-origin-access-identity `` is the value that CloudFront returned in the ID element when you created the origin access identity.
If you want viewers to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty OriginAccessIdentity element.
To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty OriginAccessIdentity element.
To replace the origin access identity, update the distribution configuration and specify the new origin access identity.
For more information about the origin access identity, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .



CustomOriginConfig (dict) --A complex type that contains information about a custom origin. If the origin is an Amazon S3 bucket, use the S3OriginConfig element instead.

HTTPPort (integer) --The HTTP port the custom origin listens on.

HTTPSPort (integer) --The HTTPS port the custom origin listens on.

OriginProtocolPolicy (string) --The origin protocol policy to apply to your origin.

OriginSslProtocols (dict) --The SSL/TLS protocols that you want CloudFront to use when communicating with your origin over HTTPS.

Quantity (integer) --The number of SSL/TLS protocols that you want to allow CloudFront to use when establishing an HTTPS connection with this origin.

Items (list) --A list that contains allowed SSL/TLS protocols for this distribution.

(string) --




OriginReadTimeout (integer) --You can create a custom origin read timeout. All timeout units are in seconds. The default origin read timeout is 30 seconds, but you can configure custom timeout lengths using the CloudFront API. The minimum timeout length is 4 seconds; the maximum is 60 seconds.
If you need to increase the maximum time limit, contact the AWS Support Center .

OriginKeepaliveTimeout (integer) --You can create a custom keep-alive timeout. All timeout units are in seconds. The default keep-alive timeout is 5 seconds, but you can configure custom timeout lengths using the CloudFront API. The minimum timeout length is 1 second; the maximum is 60 seconds.
If you need to increase the maximum time limit, contact the AWS Support Center .









OriginGroups (dict) --A complex type that contains information about origin groups for this distribution.

Quantity (integer) --The number of origin groups.

Items (list) --The items (origin groups) in a distribution.

(dict) --An origin group includes two origins (a primary origin and a second origin to failover to) and a failover criteria that you specify. You create an origin group to support origin failover in CloudFront. When you create or update a distribution, you can specifiy the origin group instead of a single origin, and CloudFront will failover from the primary origin to the second origin under the failover conditions that you\'ve chosen.

Id (string) --The origin group\'s ID.

FailoverCriteria (dict) --A complex type that contains information about the failover criteria for an origin group.

StatusCodes (dict) --The status codes that, when returned from the primary origin, will trigger CloudFront to failover to the second origin.

Quantity (integer) --The number of status codes.

Items (list) --The items (status codes) for an origin group.

(integer) --






Members (dict) --A complex type that contains information about the origins in an origin group.

Quantity (integer) --The number of origins in an origin group.

Items (list) --Items (origins) in an origin group.

(dict) --An origin in an origin group.

OriginId (string) --The ID for an origin in an origin group.













DefaultCacheBehavior (dict) --A complex type that describes the default cache behavior if you don\'t specify a CacheBehavior element or if files don\'t match any of the values of PathPattern in CacheBehavior elements. You must create exactly one default cache behavior.

TargetOriginId (string) --The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior in your distribution.

ForwardedValues (dict) --A complex type that specifies how CloudFront handles query strings, cookies, and HTTP headers.

QueryString (boolean) --Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior and cache based on the query string parameters. CloudFront behavior depends on the value of QueryString and on the values that you specify for QueryStringCacheKeys , if any:
If you specify true for QueryString and you don\'t specify any values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin and caches based on all query string parameters. Depending on how many query string parameters and values you have, this can adversely affect performance because CloudFront must forward more requests to the origin.
If you specify true for QueryString and you specify one or more values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin, but it only caches based on the query string parameters that you specify.
If you specify false for QueryString , CloudFront doesn\'t forward any query string parameters to the origin, and doesn\'t cache based on query string parameters.
For more information, see Configuring CloudFront to Cache Based on Query String Parameters in the Amazon CloudFront Developer Guide .

Cookies (dict) --A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see How CloudFront Forwards, Caches, and Logs Cookies in the Amazon CloudFront Developer Guide .

Forward (string) --Specifies which cookies to forward to the origin for this cache behavior: all, none, or the list of cookies specified in the WhitelistedNames complex type.
Amazon S3 doesn\'t process cookies. When the cache behavior is forwarding requests to an Amazon S3 origin, specify none for the Forward element.

WhitelistedNames (dict) --Required if you specify whitelist for the value of Forward . A complex type that specifies how many different cookies you want CloudFront to forward to the origin for this cache behavior and, if you want to forward selected cookies, the names of those cookies.
If you specify all or none for the value of Forward , omit WhitelistedNames . If you change the value of Forward from whitelist to all or none and you don\'t delete the WhitelistedNames element and its child elements, CloudFront deletes them automatically.
For the current limit on the number of cookie names that you can whitelist for each cache behavior, see CloudFront Limits in the AWS General Reference .

Quantity (integer) --The number of different cookies that you want CloudFront to forward to the origin for this cache behavior. The value must equal the number of items that are in the Items field.
When you set Forward = whitelist (in the CookiePreferences object), this value must be 1 or higher.

Items (list) --A complex type that contains one Name element for each cookie that you want CloudFront to forward to the origin for this cache behavior. It must contain the same number of items that is specified in the Quantity field.
When you set Forward = whitelist (in the CookiePreferences object), this field must contain at least one item.

(string) --






Headers (dict) --A complex type that specifies the Headers , if any, that you want CloudFront to forward to the origin for this cache behavior (whitelisted headers). For the headers that you specify, CloudFront also caches separate versions of a specified object that is based on the header values in viewer requests.
For more information, see Caching Content Based on Request Headers in the Amazon CloudFront Developer Guide .

Quantity (integer) --The number of different headers that you want CloudFront to base caching on for this cache behavior. You can configure each cache behavior in a web distribution to do one of the following:

Forward all headers to your origin : Specify 1 for Quantity and * for Name .


Warning
CloudFront doesn\'t cache the objects that are associated with this cache behavior. Instead, CloudFront sends every request to the origin.


Forward a whitelist of headers you specify : Specify the number of headers that you want CloudFront to base caching on. Then specify the header names in Name elements. CloudFront caches your objects based on the values in the specified headers.
Forward only the default headers : Specify 0 for Quantity and omit Items . In this configuration, CloudFront doesn\'t cache based on the values in the request headers.

Regardless of which option you choose, CloudFront forwards headers to your origin based on whether the origin is an S3 bucket or a custom origin. See the following documentation:

S3 bucket : See HTTP Request Headers That CloudFront Removes or Updates
Custom origin : See HTTP Request Headers and CloudFront Behavior


Items (list) --A list that contains one Name element for each header that you want CloudFront to use for caching in this cache behavior. If Quantity is 0 , omit Items .

(string) --




QueryStringCacheKeys (dict) --A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.

Quantity (integer) --The number of whitelisted query string parameters for a cache behavior.

Items (list) --A list that contains the query string parameters that you want CloudFront to use as a basis for caching for a cache behavior. If Quantity is 0, you can omit Items .

(string) --






TrustedSigners (dict) --A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content.
If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled , and specify the applicable values for Quantity and Items . For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .
If you don\'t want to require signed URLs in requests for objects that match PathPattern , specify false for Enabled and 0 for Quantity . Omit Items .
To add, change, or remove one or more trusted signers, change Enabled to true (if it\'s currently false ), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.

Enabled (boolean) --Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .

Quantity (integer) --The number of trusted signers for this cache behavior.

Items (list) --
Optional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .

(string) --




ViewerProtocolPolicy (string) --The protocol that viewers can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern . You can specify the following options:

allow-all : Viewers can use HTTP or HTTPS.
redirect-to-https : If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.
https-only : If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).

For more information about requiring the HTTPS protocol, see Using an HTTPS Connection to Access Your Objects in the Amazon CloudFront Developer Guide .

Note
The only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects\' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .


MinTTL (integer) --The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .
You must specify 0 for MinTTL if you configure CloudFront to forward all headers to your origin (under Headers , if you specify 1 for Quantity and * for Name ).

AllowedMethods (dict) --A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices:

CloudFront forwards only GET and HEAD requests.
CloudFront forwards only GET , HEAD , and OPTIONS requests.
CloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests.

If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can\'t perform operations that you don\'t want them to. For example, you might not want users to have permissions to delete objects from your origin.

Quantity (integer) --The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET , HEAD , and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests).

Items (list) --A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.

(string) --


CachedMethods (dict) --A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices:

CloudFront caches responses to GET and HEAD requests.
CloudFront caches responses to GET , HEAD , and OPTIONS requests.

If you pick the second choice for your Amazon S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers, and Origin headers for the responses to be cached correctly.

Quantity (integer) --The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET , HEAD , and OPTIONS requests).

Items (list) --A complex type that contains the HTTP methods that you want CloudFront to cache responses to.

(string) --






SmoothStreaming (boolean) --Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true ; if not, specify false . If you specify true for SmoothStreaming , you can still distribute other content using this cache behavior if the content matches the value of PathPattern .

DefaultTTL (integer) --The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .

MaxTTL (integer) --The maximum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .

Compress (boolean) --Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify true ; if not, specify false . For more information, see Serving Compressed Files in the Amazon CloudFront Developer Guide .

LambdaFunctionAssociations (dict) --A complex type that contains zero or more Lambda function associations for a cache behavior.

Quantity (integer) --The number of Lambda function associations for this cache behavior.

Items (list) --
Optional : A complex type that contains LambdaFunctionAssociation items for this cache behavior. If Quantity is 0 , you can omit Items .

(dict) --A complex type that contains a Lambda function association.

LambdaFunctionARN (string) --The ARN of the Lambda function. You must specify the ARN of a function version; you can\'t specify a Lambda alias or $LATEST.

EventType (string) --Specifies the event type that triggers a Lambda function invocation. You can specify the following values:

viewer-request : The function executes when CloudFront receives a request from a viewer and before it checks to see whether the requested object is in the edge cache.
origin-request : The function executes only when CloudFront forwards a request to your origin. When the requested object is in the edge cache, the function doesn\'t execute.
origin-response : The function executes after CloudFront receives a response from the origin and before it caches the object in the response. When the requested object is in the edge cache, the function doesn\'t execute.
viewer-response : The function executes before CloudFront returns the requested object to the viewer. The function executes regardless of whether the object was already in the edge cache. If the origin returns an HTTP status code other than HTTP 200 (OK), the function doesn\'t execute.


IncludeBody (boolean) --A flag that allows a Lambda function to have read access to the body content. For more information, see Accessing the Request Body by Choosing the Include Body Option in the Amazon CloudFront Developer Guide.







FieldLevelEncryptionId (string) --The value of ID for the field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data for a cache behavior or for the default cache behavior in your distribution.



CacheBehaviors (dict) --A complex type that contains zero or more CacheBehavior elements.

Quantity (integer) --The number of cache behaviors for this distribution.

Items (list) --Optional: A complex type that contains cache behaviors for this distribution. If Quantity is 0 , you can omit Items .

(dict) --A complex type that describes how CloudFront processes requests.
You must create at least as many cache behaviors (including the default cache behavior) as you have origins if you want CloudFront to distribute objects from all of the origins. Each cache behavior specifies the one origin from which you want CloudFront to get objects. If you have two origins and only the default cache behavior, the default cache behavior will cause CloudFront to get objects from one of the origins, but the other origin is never used.
For the current limit on the number of cache behaviors that you can add to a distribution, see Amazon CloudFront Limits in the AWS General Reference .
If you don\'t want to specify any cache behaviors, include only an empty CacheBehaviors element. Don\'t include an empty CacheBehavior element, or CloudFront returns a MalformedXML error.
To delete all cache behaviors in an existing distribution, update the distribution configuration and include only an empty CacheBehaviors element.
To add, change, or remove one or more cache behaviors, update the distribution configuration and specify all of the cache behaviors that you want to include in the updated distribution.
For more information about cache behaviors, see Cache Behaviors in the Amazon CloudFront Developer Guide .

PathPattern (string) --The pattern (for example, images/*.jpg ) that specifies which requests to apply the behavior to. When CloudFront receives a viewer request, the requested path is compared with path patterns in the order in which cache behaviors are listed in the distribution.

Note
You can optionally include a slash (/ ) at the beginning of the path pattern. For example, /images/*.jpg . CloudFront behavior is the same with or without the leading / .

The path pattern for the default cache behavior is * and cannot be changed. If the request for an object does not match the path pattern for any cache behaviors, CloudFront applies the behavior in the default cache behavior.
For more information, see Path Pattern in the Amazon CloudFront Developer Guide .

TargetOriginId (string) --The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior in your distribution.

ForwardedValues (dict) --A complex type that specifies how CloudFront handles query strings, cookies, and HTTP headers.

QueryString (boolean) --Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior and cache based on the query string parameters. CloudFront behavior depends on the value of QueryString and on the values that you specify for QueryStringCacheKeys , if any:
If you specify true for QueryString and you don\'t specify any values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin and caches based on all query string parameters. Depending on how many query string parameters and values you have, this can adversely affect performance because CloudFront must forward more requests to the origin.
If you specify true for QueryString and you specify one or more values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin, but it only caches based on the query string parameters that you specify.
If you specify false for QueryString , CloudFront doesn\'t forward any query string parameters to the origin, and doesn\'t cache based on query string parameters.
For more information, see Configuring CloudFront to Cache Based on Query String Parameters in the Amazon CloudFront Developer Guide .

Cookies (dict) --A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see How CloudFront Forwards, Caches, and Logs Cookies in the Amazon CloudFront Developer Guide .

Forward (string) --Specifies which cookies to forward to the origin for this cache behavior: all, none, or the list of cookies specified in the WhitelistedNames complex type.
Amazon S3 doesn\'t process cookies. When the cache behavior is forwarding requests to an Amazon S3 origin, specify none for the Forward element.

WhitelistedNames (dict) --Required if you specify whitelist for the value of Forward . A complex type that specifies how many different cookies you want CloudFront to forward to the origin for this cache behavior and, if you want to forward selected cookies, the names of those cookies.
If you specify all or none for the value of Forward , omit WhitelistedNames . If you change the value of Forward from whitelist to all or none and you don\'t delete the WhitelistedNames element and its child elements, CloudFront deletes them automatically.
For the current limit on the number of cookie names that you can whitelist for each cache behavior, see CloudFront Limits in the AWS General Reference .

Quantity (integer) --The number of different cookies that you want CloudFront to forward to the origin for this cache behavior. The value must equal the number of items that are in the Items field.
When you set Forward = whitelist (in the CookiePreferences object), this value must be 1 or higher.

Items (list) --A complex type that contains one Name element for each cookie that you want CloudFront to forward to the origin for this cache behavior. It must contain the same number of items that is specified in the Quantity field.
When you set Forward = whitelist (in the CookiePreferences object), this field must contain at least one item.

(string) --






Headers (dict) --A complex type that specifies the Headers , if any, that you want CloudFront to forward to the origin for this cache behavior (whitelisted headers). For the headers that you specify, CloudFront also caches separate versions of a specified object that is based on the header values in viewer requests.
For more information, see Caching Content Based on Request Headers in the Amazon CloudFront Developer Guide .

Quantity (integer) --The number of different headers that you want CloudFront to base caching on for this cache behavior. You can configure each cache behavior in a web distribution to do one of the following:

Forward all headers to your origin : Specify 1 for Quantity and * for Name .


Warning
CloudFront doesn\'t cache the objects that are associated with this cache behavior. Instead, CloudFront sends every request to the origin.


Forward a whitelist of headers you specify : Specify the number of headers that you want CloudFront to base caching on. Then specify the header names in Name elements. CloudFront caches your objects based on the values in the specified headers.
Forward only the default headers : Specify 0 for Quantity and omit Items . In this configuration, CloudFront doesn\'t cache based on the values in the request headers.

Regardless of which option you choose, CloudFront forwards headers to your origin based on whether the origin is an S3 bucket or a custom origin. See the following documentation:

S3 bucket : See HTTP Request Headers That CloudFront Removes or Updates
Custom origin : See HTTP Request Headers and CloudFront Behavior


Items (list) --A list that contains one Name element for each header that you want CloudFront to use for caching in this cache behavior. If Quantity is 0 , omit Items .

(string) --




QueryStringCacheKeys (dict) --A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.

Quantity (integer) --The number of whitelisted query string parameters for a cache behavior.

Items (list) --A list that contains the query string parameters that you want CloudFront to use as a basis for caching for a cache behavior. If Quantity is 0, you can omit Items .

(string) --






TrustedSigners (dict) --A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content.
If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled , and specify the applicable values for Quantity and Items . For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .
If you don\'t want to require signed URLs in requests for objects that match PathPattern , specify false for Enabled and 0 for Quantity . Omit Items .
To add, change, or remove one or more trusted signers, change Enabled to true (if it\'s currently false ), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.

Enabled (boolean) --Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .

Quantity (integer) --The number of trusted signers for this cache behavior.

Items (list) --
Optional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .

(string) --




ViewerProtocolPolicy (string) --The protocol that viewers can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern . You can specify the following options:

allow-all : Viewers can use HTTP or HTTPS.
redirect-to-https : If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.
https-only : If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).

For more information about requiring the HTTPS protocol, see Using an HTTPS Connection to Access Your Objects in the Amazon CloudFront Developer Guide .

Note
The only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects\' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .


MinTTL (integer) --The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .
You must specify 0 for MinTTL if you configure CloudFront to forward all headers to your origin (under Headers , if you specify 1 for Quantity and * for Name ).

AllowedMethods (dict) --A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices:

CloudFront forwards only GET and HEAD requests.
CloudFront forwards only GET , HEAD , and OPTIONS requests.
CloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests.

If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can\'t perform operations that you don\'t want them to. For example, you might not want users to have permissions to delete objects from your origin.

Quantity (integer) --The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET , HEAD , and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests).

Items (list) --A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.

(string) --


CachedMethods (dict) --A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices:

CloudFront caches responses to GET and HEAD requests.
CloudFront caches responses to GET , HEAD , and OPTIONS requests.

If you pick the second choice for your Amazon S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers, and Origin headers for the responses to be cached correctly.

Quantity (integer) --The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET , HEAD , and OPTIONS requests).

Items (list) --A complex type that contains the HTTP methods that you want CloudFront to cache responses to.

(string) --






SmoothStreaming (boolean) --Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true ; if not, specify false . If you specify true for SmoothStreaming , you can still distribute other content using this cache behavior if the content matches the value of PathPattern .

DefaultTTL (integer) --The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .

MaxTTL (integer) --The maximum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .

Compress (boolean) --Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify true; if not, specify false. For more information, see Serving Compressed Files in the Amazon CloudFront Developer Guide .

LambdaFunctionAssociations (dict) --A complex type that contains zero or more Lambda function associations for a cache behavior.

Quantity (integer) --The number of Lambda function associations for this cache behavior.

Items (list) --
Optional : A complex type that contains LambdaFunctionAssociation items for this cache behavior. If Quantity is 0 , you can omit Items .

(dict) --A complex type that contains a Lambda function association.

LambdaFunctionARN (string) --The ARN of the Lambda function. You must specify the ARN of a function version; you can\'t specify a Lambda alias or $LATEST.

EventType (string) --Specifies the event type that triggers a Lambda function invocation. You can specify the following values:

viewer-request : The function executes when CloudFront receives a request from a viewer and before it checks to see whether the requested object is in the edge cache.
origin-request : The function executes only when CloudFront forwards a request to your origin. When the requested object is in the edge cache, the function doesn\'t execute.
origin-response : The function executes after CloudFront receives a response from the origin and before it caches the object in the response. When the requested object is in the edge cache, the function doesn\'t execute.
viewer-response : The function executes before CloudFront returns the requested object to the viewer. The function executes regardless of whether the object was already in the edge cache. If the origin returns an HTTP status code other than HTTP 200 (OK), the function doesn\'t execute.


IncludeBody (boolean) --A flag that allows a Lambda function to have read access to the body content. For more information, see Accessing the Request Body by Choosing the Include Body Option in the Amazon CloudFront Developer Guide.







FieldLevelEncryptionId (string) --The value of ID for the field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data for a cache behavior or for the default cache behavior in your distribution.







CustomErrorResponses (dict) --A complex type that controls the following:

Whether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.
How long CloudFront caches HTTP status codes in the 4xx and 5xx range.

For more information about custom error pages, see Customizing Error Responses in the Amazon CloudFront Developer Guide .

Quantity (integer) --The number of HTTP status codes for which you want to specify a custom error page and/or a caching duration. If Quantity is 0 , you can omit Items .

Items (list) --A complex type that contains a CustomErrorResponse element for each HTTP status code for which you want to specify a custom error page and/or a caching duration.

(dict) --A complex type that controls:

Whether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.
How long CloudFront caches HTTP status codes in the 4xx and 5xx range.

For more information about custom error pages, see Customizing Error Responses in the Amazon CloudFront Developer Guide .

ErrorCode (integer) --The HTTP status code for which you want to specify a custom error page and/or a caching duration.

ResponsePagePath (string) --The path to the custom error page that you want CloudFront to return to a viewer when your origin returns the HTTP status code specified by ErrorCode , for example, /4xx-errors/403-forbidden.html . If you want to store your objects and your custom error pages in different locations, your distribution must include a cache behavior for which the following is true:

The value of PathPattern matches the path to your custom error messages. For example, suppose you saved custom error pages for 4xx errors in an Amazon S3 bucket in a directory named /4xx-errors . Your distribution must include a cache behavior for which the path pattern routes requests for your custom error pages to that location, for example, /4xx-errors/* .
The value of TargetOriginId specifies the value of the ID element for the origin that contains your custom error pages.

If you specify a value for ResponsePagePath , you must also specify a value for ResponseCode .
We recommend that you store custom error pages in an Amazon S3 bucket. If you store custom error pages on an HTTP server and the server starts to return 5xx errors, CloudFront can\'t get the files that you want to return to viewers because the origin server is unavailable.

ResponseCode (string) --The HTTP status code that you want CloudFront to return to the viewer along with the custom error page. There are a variety of reasons that you might want CloudFront to return a status code different from the status code that your origin returned to CloudFront, for example:

Some Internet devices (some firewalls and corporate proxies, for example) intercept HTTP 4xx and 5xx and prevent the response from being returned to the viewer. If you substitute 200 , the response typically won\'t be intercepted.
If you don\'t care about distinguishing among different client errors or server errors, you can specify 400 or 500 as the ResponseCode for all 4xx or 5xx errors.
You might want to return a 200 status code (OK) and static website so your customers don\'t know that your website is down.

If you specify a value for ResponseCode , you must also specify a value for ResponsePagePath .

ErrorCachingMinTTL (integer) --The minimum amount of time, in seconds, that you want CloudFront to cache the HTTP status code specified in ErrorCode . When this time period has elapsed, CloudFront queries your origin to see whether the problem that caused the error has been resolved and the requested object is now available.
For more information, see Customizing Error Responses in the Amazon CloudFront Developer Guide .







Comment (string) --Any comments you want to include about the distribution.
If you don\'t want to specify a comment, include an empty Comment element.
To delete an existing comment, update the distribution configuration and include an empty Comment element.
To add or change a comment, update the distribution configuration and specify the new comment.

Logging (dict) --A complex type that controls whether access logs are written for the distribution.
For more information about logging, see Access Logs in the Amazon CloudFront Developer Guide .

Enabled (boolean) --Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you don\'t want to enable logging when you create a distribution or if you want to disable logging for an existing distribution, specify false for Enabled , and specify empty Bucket and Prefix elements. If you specify false for Enabled but you specify values for Bucket , prefix , and IncludeCookies , the values are automatically deleted.

IncludeCookies (boolean) --Specifies whether you want CloudFront to include cookies in access logs, specify true for IncludeCookies . If you choose to include cookies in logs, CloudFront logs all cookies regardless of how you configure the cache behaviors for this distribution. If you don\'t want to include cookies when you create a distribution or if you want to disable include cookies for an existing distribution, specify false for IncludeCookies .

Bucket (string) --The Amazon S3 bucket to store the access logs in, for example, myawslogbucket.s3.amazonaws.com .

Prefix (string) --An optional string that you want CloudFront to prefix to the access log filenames for this distribution, for example, myprefix/ . If you want to enable logging, but you don\'t want to specify a prefix, you still must include an empty Prefix element in the Logging element.



PriceClass (string) --The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify PriceClass_All , CloudFront responds to requests for your objects from all CloudFront edge locations.
If you specify a price class other than PriceClass_All , CloudFront serves your objects from the CloudFront edge location that has the lowest latency among the edge locations in your price class. Viewers who are in or near regions that are excluded from your specified price class may encounter slower performance.
For more information about price classes, see Choosing the Price Class for a CloudFront Distribution in the Amazon CloudFront Developer Guide . For information about CloudFront pricing, including how price classes (such as Price Class 100) map to CloudFront regions, see Amazon CloudFront Pricing . For price class information, scroll down to see the table at the bottom of the page.

Enabled (boolean) --From this field, you can enable or disable the selected distribution.

ViewerCertificate (dict) --A complex type that determines the distribution\xe2\x80\x99s SSL/TLS configuration for communicating with viewers.

CloudFrontDefaultCertificate (boolean) --If the distribution uses the CloudFront domain name such as d111111abcdef8.cloudfront.net , set this field to true .
If the distribution uses Aliases (alternate domain names or CNAMEs), set this field to false and specify values for the following fields:

ACMCertificateArn or IAMCertificateId (specify a value for one, not both)
MinimumProtocolVersion
SSLSupportMethod


IAMCertificateId (string) --If the distribution uses Aliases (alternate domain names or CNAMEs) and the SSL/TLS certificate is stored in AWS Identity and Access Management (AWS IAM) , provide the ID of the IAM certificate.
If you specify an IAM certificate ID, you must also specify values for MinimumProtocolVerison and SSLSupportMethod .

ACMCertificateArn (string) --If the distribution uses Aliases (alternate domain names or CNAMEs) and the SSL/TLS certificate is stored in AWS Certificate Manager (ACM) , provide the Amazon Resource Name (ARN) of the ACM certificate. CloudFront only supports ACM certificates in the US East (N. Virginia) Region (us-east-1 ).
If you specify an ACM certificate ARN, you must also specify values for MinimumProtocolVerison and SSLSupportMethod .

SSLSupportMethod (string) --If the distribution uses Aliases (alternate domain names or CNAMEs), specify which viewers the distribution accepts HTTPS connections from.

sni-only \xe2\x80\x93 The distribution accepts HTTPS connections from only viewers that support server name indication (SNI) . This is recommended. Most browsers and clients released after 2010 support SNI.
vip \xe2\x80\x93 The distribution accepts HTTPS connections from all viewers including those that don\xe2\x80\x99t support SNI. This is not recommended, and results in additional monthly charges from CloudFront.

If the distribution uses the CloudFront domain name such as d111111abcdef8.cloudfront.net , don\xe2\x80\x99t set a value for this field.

MinimumProtocolVersion (string) --If the distribution uses Aliases (alternate domain names or CNAMEs), specify the security policy that you want CloudFront to use for HTTPS connections with viewers. The security policy determines two settings:

The minimum SSL/TLS protocol that CloudFront can use to communicate with viewers.
The ciphers that CloudFront can use to encrypt the content that it returns to viewers.

For more information, see Security Policy and Supported Protocols and Ciphers Between Viewers and CloudFront in the Amazon CloudFront Developer Guide .

Note
On the CloudFront console, this setting is called Security Policy .

We recommend that you specify TLSv1.2_2018 unless your viewers are using browsers or devices that don\xe2\x80\x99t support TLSv1.2.
When you\xe2\x80\x99re using SNI only (you set SSLSupportMethod to sni-only ), you must specify TLSv1 or higher.
If the distribution uses the CloudFront domain name such as d111111abcdef8.cloudfront.net (you set CloudFrontDefaultCertificate to true ), CloudFront automatically sets the security policy to TLSv1 regardless of the value that you set here.

Certificate (string) --This field is deprecated. Use one of the following fields instead:

ACMCertificateArn
IAMCertificateId
CloudFrontDefaultCertificate


CertificateSource (string) --This field is deprecated. Use one of the following fields instead:

ACMCertificateArn
IAMCertificateId
CloudFrontDefaultCertificate




Restrictions (dict) --A complex type that identifies ways in which you want to restrict distribution of your content.

GeoRestriction (dict) --A complex type that controls the countries in which your content is distributed. CloudFront determines the location of your users using MaxMind GeoIP databases.

RestrictionType (string) --The method that you want to use to restrict distribution of your content by country:

none : No geo restriction is enabled, meaning access to content is not restricted by client geo location.
blacklist : The Location elements specify the countries in which you don\'t want CloudFront to distribute your content.
whitelist : The Location elements specify the countries in which you want CloudFront to distribute your content.


Quantity (integer) --When geo restriction is enabled , this is the number of countries in your whitelist or blacklist . Otherwise, when it is not enabled, Quantity is 0 , and you can omit Items .

Items (list) --A complex type that contains a Location element for each country in which you want CloudFront either to distribute your content (whitelist ) or not distribute your content (blacklist ).
The Location element is a two-letter, uppercase country code for a country that you want to include in your blacklist or whitelist . Include one Location element for each country.
CloudFront and MaxMind both use ISO 3166 country codes. For the current list of countries and the corresponding codes, see ISO 3166-1-alpha-2 code on the International Organization for Standardization website. You can also refer to the country list on the CloudFront console, which includes both country names and codes.

(string) --






WebACLId (string) --A unique identifier that specifies the AWS WAF web ACL, if any, to associate with this distribution. To specify a web ACL created using the latest version of AWS WAF, use the ACL ARN, for example arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/473e64fd-f30b-4765-81a0-62ad96dd167a . To specify a web ACL created using AWS WAF Classic, use the ACL ID, for example 473e64fd-f30b-4765-81a0-62ad96dd167a .
AWS WAF is a web application firewall that lets you monitor the HTTP and HTTPS requests that are forwarded to CloudFront, and lets you control access to your content. Based on conditions that you specify, such as the IP addresses that requests originate from or the values of query strings, CloudFront responds to requests either with the requested content or with an HTTP 403 status code (Forbidden). You can also configure CloudFront to return a custom error page when a request is blocked. For more information about AWS WAF, see the AWS WAF Developer Guide .

HttpVersion (string) --(Optional) Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront. The default value for new web distributions is http2. Viewers that don\'t support HTTP/2 automatically use an earlier HTTP version.
For viewers and CloudFront to use HTTP/2, viewers must support TLS 1.2 or later, and must support Server Name Identification (SNI).
In general, configuring CloudFront to communicate with viewers using HTTP/2 reduces latency. You can improve performance by optimizing for HTTP/2. For more information, do an Internet search for "http/2 optimization."

IsIPV6Enabled (boolean) --If you want CloudFront to respond to IPv6 DNS requests with an IPv6 address for your distribution, specify true . If you specify false , CloudFront responds to IPv6 DNS requests with the DNS response code NOERROR and with no IP addresses. This allows viewers to submit a second request, for an IPv4 address for your distribution.
In general, you should enable IPv6 if you have users on IPv6 networks who want to access your content. However, if you\'re using signed URLs or signed cookies to restrict access to your content, and if you\'re using a custom policy that includes the IpAddress parameter to restrict the IP addresses that can access your content, don\'t enable IPv6. If you want to restrict access to some content by IP address and not restrict access to other content (or restrict access but not by IP address), you can create two distributions. For more information, see Creating a Signed URL Using a Custom Policy in the Amazon CloudFront Developer Guide .
If you\'re using an Amazon Route 53 alias resource record set to route traffic to your CloudFront distribution, you need to create a second alias resource record set when both of the following are true:

You enable IPv6 for the distribution
You\'re using alternate domain names in the URLs for your objects

For more information, see Routing Traffic to an Amazon CloudFront Web Distribution by Using Your Domain Name in the Amazon Route 53 Developer Guide .
If you created a CNAME resource record set, either with Amazon Route 53 or with another DNS service, you don\'t need to make any changes. A CNAME record will route traffic to your distribution regardless of the IP address format of the viewer request.



AliasICPRecordals (list) --AWS services in China customers must file for an Internet Content Provider (ICP) recordal if they want to serve content publicly on an alternate domain name, also known as a CNAME, that they\'ve added to CloudFront. AliasICPRecordal provides the ICP recordal status for CNAMEs associated with distributions.
For more information about ICP recordals, see Signup, Accounts, and Credentials in Getting Started with AWS services in China .

(dict) --AWS services in China customers must file for an Internet Content Provider (ICP) recordal if they want to serve content publicly on an alternate domain name, also known as a CNAME, that they\'ve added to CloudFront. AliasICPRecordal provides the ICP recordal status for CNAMEs associated with distributions. The status is returned in the CloudFront response; you can\'t configure it yourself.
For more information about ICP recordals, see Signup, Accounts, and Credentials in Getting Started with AWS services in China .

CNAME (string) --A domain name associated with a distribution.

ICPRecordalStatus (string) --The Internet Content Provider (ICP) recordal status for a CNAME. The ICPRecordalStatus is set to APPROVED for all CNAMEs (aliases) in regions outside of China.
The status values returned are the following:

APPROVED indicates that the associated CNAME has a valid ICP recordal number. Multiple CNAMEs can be associated with a distribution, and CNAMEs can correspond to different ICP recordals. To be marked as APPROVED, that is, valid to use with China region, a CNAME must have one ICP recordal number associated with it.
SUSPENDED indicates that the associated CNAME does not have a valid ICP recordal number.
PENDING indicates that CloudFront can\'t determine the ICP recordal status of the CNAME associated with the distribution because there was an error in trying to determine the status. You can try again to see if the error is resolved in which case CloudFront returns an APPROVED or SUSPENDED status.








ETag (string) --The current version of the distribution\'s information. For example: E2QWRUHAPOMQZL .






Exceptions

CloudFront.Client.exceptions.NoSuchDistribution
CloudFront.Client.exceptions.AccessDenied


    :return: {
        'Distribution': {
            'Id': 'string',
            'ARN': 'string',
            'Status': 'string',
            'LastModifiedTime': datetime(2015, 1, 1),
            'InProgressInvalidationBatches': 123,
            'DomainName': 'string',
            'ActiveTrustedSigners': {
                'Enabled': True|False,
                'Quantity': 123,
                'Items': [
                    {
                        'AwsAccountNumber': 'string',
                        'KeyPairIds': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                ]
            },
            'DistributionConfig': {
                'CallerReference': 'string',
                'Aliases': {
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'DefaultRootObject': 'string',
                'Origins': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'Id': 'string',
                            'DomainName': 'string',
                            'OriginPath': 'string',
                            'CustomHeaders': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'HeaderName': 'string',
                                        'HeaderValue': 'string'
                                    },
                                ]
                            },
                            'S3OriginConfig': {
                                'OriginAccessIdentity': 'string'
                            },
                            'CustomOriginConfig': {
                                'HTTPPort': 123,
                                'HTTPSPort': 123,
                                'OriginProtocolPolicy': 'http-only'|'match-viewer'|'https-only',
                                'OriginSslProtocols': {
                                    'Quantity': 123,
                                    'Items': [
                                        'SSLv3'|'TLSv1'|'TLSv1.1'|'TLSv1.2',
                                    ]
                                },
                                'OriginReadTimeout': 123,
                                'OriginKeepaliveTimeout': 123
                            }
                        },
                    ]
                },
                'OriginGroups': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'Id': 'string',
                            'FailoverCriteria': {
                                'StatusCodes': {
                                    'Quantity': 123,
                                    'Items': [
                                        123,
                                    ]
                                }
                            },
                            'Members': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'OriginId': 'string'
                                    },
                                ]
                            }
                        },
                    ]
                },
                'DefaultCacheBehavior': {
                    'TargetOriginId': 'string',
                    'ForwardedValues': {
                        'QueryString': True|False,
                        'Cookies': {
                            'Forward': 'none'|'whitelist'|'all',
                            'WhitelistedNames': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                        'Headers': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        },
                        'QueryStringCacheKeys': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                    'TrustedSigners': {
                        'Enabled': True|False,
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    },
                    'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                    'MinTTL': 123,
                    'AllowedMethods': {
                        'Quantity': 123,
                        'Items': [
                            'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                        ],
                        'CachedMethods': {
                            'Quantity': 123,
                            'Items': [
                                'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                            ]
                        }
                    },
                    'SmoothStreaming': True|False,
                    'DefaultTTL': 123,
                    'MaxTTL': 123,
                    'Compress': True|False,
                    'LambdaFunctionAssociations': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'LambdaFunctionARN': 'string',
                                'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                'IncludeBody': True|False
                            },
                        ]
                    },
                    'FieldLevelEncryptionId': 'string'
                },
                'CacheBehaviors': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'PathPattern': 'string',
                            'TargetOriginId': 'string',
                            'ForwardedValues': {
                                'QueryString': True|False,
                                'Cookies': {
                                    'Forward': 'none'|'whitelist'|'all',
                                    'WhitelistedNames': {
                                        'Quantity': 123,
                                        'Items': [
                                            'string',
                                        ]
                                    }
                                },
                                'Headers': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                },
                                'QueryStringCacheKeys': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                }
                            },
                            'TrustedSigners': {
                                'Enabled': True|False,
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            },
                            'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                            'MinTTL': 123,
                            'AllowedMethods': {
                                'Quantity': 123,
                                'Items': [
                                    'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                ],
                                'CachedMethods': {
                                    'Quantity': 123,
                                    'Items': [
                                        'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                    ]
                                }
                            },
                            'SmoothStreaming': True|False,
                            'DefaultTTL': 123,
                            'MaxTTL': 123,
                            'Compress': True|False,
                            'LambdaFunctionAssociations': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'LambdaFunctionARN': 'string',
                                        'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                        'IncludeBody': True|False
                                    },
                                ]
                            },
                            'FieldLevelEncryptionId': 'string'
                        },
                    ]
                },
                'CustomErrorResponses': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'ErrorCode': 123,
                            'ResponsePagePath': 'string',
                            'ResponseCode': 'string',
                            'ErrorCachingMinTTL': 123
                        },
                    ]
                },
                'Comment': 'string',
                'Logging': {
                    'Enabled': True|False,
                    'IncludeCookies': True|False,
                    'Bucket': 'string',
                    'Prefix': 'string'
                },
                'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
                'Enabled': True|False,
                'ViewerCertificate': {
                    'CloudFrontDefaultCertificate': True|False,
                    'IAMCertificateId': 'string',
                    'ACMCertificateArn': 'string',
                    'SSLSupportMethod': 'sni-only'|'vip',
                    'MinimumProtocolVersion': 'SSLv3'|'TLSv1'|'TLSv1_2016'|'TLSv1.1_2016'|'TLSv1.2_2018',
                    'Certificate': 'string',
                    'CertificateSource': 'cloudfront'|'iam'|'acm'
                },
                'Restrictions': {
                    'GeoRestriction': {
                        'RestrictionType': 'blacklist'|'whitelist'|'none',
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    }
                },
                'WebACLId': 'string',
                'HttpVersion': 'http1.1'|'http2',
                'IsIPV6Enabled': True|False
            },
            'AliasICPRecordals': [
                {
                    'CNAME': 'string',
                    'ICPRecordalStatus': 'APPROVED'|'SUSPENDED'|'PENDING'
                },
            ]
        },
        'ETag': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_distribution_config(Id=None):
    """
    Get the configuration information about a distribution.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_distribution_config(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe distribution\'s ID. If the ID is empty, an empty distribution configuration is returned.\n

    :rtype: dict
ReturnsResponse Syntax{
    'DistributionConfig': {
        'CallerReference': 'string',
        'Aliases': {
            'Quantity': 123,
            'Items': [
                'string',
            ]
        },
        'DefaultRootObject': 'string',
        'Origins': {
            'Quantity': 123,
            'Items': [
                {
                    'Id': 'string',
                    'DomainName': 'string',
                    'OriginPath': 'string',
                    'CustomHeaders': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'HeaderName': 'string',
                                'HeaderValue': 'string'
                            },
                        ]
                    },
                    'S3OriginConfig': {
                        'OriginAccessIdentity': 'string'
                    },
                    'CustomOriginConfig': {
                        'HTTPPort': 123,
                        'HTTPSPort': 123,
                        'OriginProtocolPolicy': 'http-only'|'match-viewer'|'https-only',
                        'OriginSslProtocols': {
                            'Quantity': 123,
                            'Items': [
                                'SSLv3'|'TLSv1'|'TLSv1.1'|'TLSv1.2',
                            ]
                        },
                        'OriginReadTimeout': 123,
                        'OriginKeepaliveTimeout': 123
                    }
                },
            ]
        },
        'OriginGroups': {
            'Quantity': 123,
            'Items': [
                {
                    'Id': 'string',
                    'FailoverCriteria': {
                        'StatusCodes': {
                            'Quantity': 123,
                            'Items': [
                                123,
                            ]
                        }
                    },
                    'Members': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'OriginId': 'string'
                            },
                        ]
                    }
                },
            ]
        },
        'DefaultCacheBehavior': {
            'TargetOriginId': 'string',
            'ForwardedValues': {
                'QueryString': True|False,
                'Cookies': {
                    'Forward': 'none'|'whitelist'|'all',
                    'WhitelistedNames': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    }
                },
                'Headers': {
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'QueryStringCacheKeys': {
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                }
            },
            'TrustedSigners': {
                'Enabled': True|False,
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
            'MinTTL': 123,
            'AllowedMethods': {
                'Quantity': 123,
                'Items': [
                    'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                ],
                'CachedMethods': {
                    'Quantity': 123,
                    'Items': [
                        'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                    ]
                }
            },
            'SmoothStreaming': True|False,
            'DefaultTTL': 123,
            'MaxTTL': 123,
            'Compress': True|False,
            'LambdaFunctionAssociations': {
                'Quantity': 123,
                'Items': [
                    {
                        'LambdaFunctionARN': 'string',
                        'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                        'IncludeBody': True|False
                    },
                ]
            },
            'FieldLevelEncryptionId': 'string'
        },
        'CacheBehaviors': {
            'Quantity': 123,
            'Items': [
                {
                    'PathPattern': 'string',
                    'TargetOriginId': 'string',
                    'ForwardedValues': {
                        'QueryString': True|False,
                        'Cookies': {
                            'Forward': 'none'|'whitelist'|'all',
                            'WhitelistedNames': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                        'Headers': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        },
                        'QueryStringCacheKeys': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                    'TrustedSigners': {
                        'Enabled': True|False,
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    },
                    'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                    'MinTTL': 123,
                    'AllowedMethods': {
                        'Quantity': 123,
                        'Items': [
                            'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                        ],
                        'CachedMethods': {
                            'Quantity': 123,
                            'Items': [
                                'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                            ]
                        }
                    },
                    'SmoothStreaming': True|False,
                    'DefaultTTL': 123,
                    'MaxTTL': 123,
                    'Compress': True|False,
                    'LambdaFunctionAssociations': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'LambdaFunctionARN': 'string',
                                'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                'IncludeBody': True|False
                            },
                        ]
                    },
                    'FieldLevelEncryptionId': 'string'
                },
            ]
        },
        'CustomErrorResponses': {
            'Quantity': 123,
            'Items': [
                {
                    'ErrorCode': 123,
                    'ResponsePagePath': 'string',
                    'ResponseCode': 'string',
                    'ErrorCachingMinTTL': 123
                },
            ]
        },
        'Comment': 'string',
        'Logging': {
            'Enabled': True|False,
            'IncludeCookies': True|False,
            'Bucket': 'string',
            'Prefix': 'string'
        },
        'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
        'Enabled': True|False,
        'ViewerCertificate': {
            'CloudFrontDefaultCertificate': True|False,
            'IAMCertificateId': 'string',
            'ACMCertificateArn': 'string',
            'SSLSupportMethod': 'sni-only'|'vip',
            'MinimumProtocolVersion': 'SSLv3'|'TLSv1'|'TLSv1_2016'|'TLSv1.1_2016'|'TLSv1.2_2018',
            'Certificate': 'string',
            'CertificateSource': 'cloudfront'|'iam'|'acm'
        },
        'Restrictions': {
            'GeoRestriction': {
                'RestrictionType': 'blacklist'|'whitelist'|'none',
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            }
        },
        'WebACLId': 'string',
        'HttpVersion': 'http1.1'|'http2',
        'IsIPV6Enabled': True|False
    },
    'ETag': 'string'
}


Response Structure

(dict) --The returned result of the corresponding request.

DistributionConfig (dict) --The distribution\'s configuration information.

CallerReference (string) --A unique value (for example, a date-time stamp) that ensures that the request can\'t be replayed.
If the value of CallerReference is new (regardless of the content of the DistributionConfig object), CloudFront creates a new distribution.
If CallerReference is a value that you already sent in a previous request to create a distribution, CloudFront returns a DistributionAlreadyExists error.

Aliases (dict) --A complex type that contains information about CNAMEs (alternate domain names), if any, for this distribution.

Quantity (integer) --The number of CNAME aliases, if any, that you want to associate with this distribution.

Items (list) --A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.

(string) --




DefaultRootObject (string) --The object that you want CloudFront to request from your origin (for example, index.html ) when a viewer requests the root URL for your distribution (http://www.example.com ) instead of an object in your distribution (http://www.example.com/product-description.html ). Specifying a default root object avoids exposing the contents of your distribution.
Specify only the object name, for example, index.html . Don\'t add a / before the object name.
If you don\'t want to specify a default root object when you create a distribution, include an empty DefaultRootObject element.
To delete the default root object from an existing distribution, update the distribution configuration and include an empty DefaultRootObject element.
To replace the default root object, update the distribution configuration and specify the new object.
For more information about the default root object, see Creating a Default Root Object in the Amazon CloudFront Developer Guide .

Origins (dict) --A complex type that contains information about origins for this distribution.

Quantity (integer) --The number of origins or origin groups for this distribution.

Items (list) --A complex type that contains origins or origin groups for this distribution.

(dict) --A complex type that describes the Amazon S3 bucket, HTTP server (for example, a web server), Amazon MediaStore, or other server from which CloudFront gets your files. This can also be an origin group, if you\'ve created an origin group. You must specify at least one origin or origin group.
For the current limit on the number of origins or origin groups that you can specify for a distribution, see Amazon CloudFront Limits in the AWS General Reference .

Id (string) --A unique identifier for the origin or origin group. The value of Id must be unique within the distribution.
When you specify the value of TargetOriginId for the default cache behavior or for another cache behavior, you indicate the origin to which you want the cache behavior to route requests by specifying the value of the Id element for that origin. When a request matches the path pattern for that cache behavior, CloudFront routes the request to the specified origin. For more information, see Cache Behavior Settings in the Amazon CloudFront Developer Guide .

DomainName (string) --
Amazon S3 origins : The DNS name of the Amazon S3 bucket from which you want CloudFront to get objects for this origin, for example, myawsbucket.s3.amazonaws.com . If you set up your bucket to be configured as a website endpoint, enter the Amazon S3 static website hosting endpoint for the bucket.
For more information about specifying this value for different types of origins, see Origin Domain Name in the Amazon CloudFront Developer Guide .
Constraints for Amazon S3 origins:

If you configured Amazon S3 Transfer Acceleration for your bucket, don\'t specify the s3-accelerate endpoint for DomainName .
The bucket name must be between 3 and 63 characters long (inclusive).
The bucket name must contain only lowercase characters, numbers, periods, underscores, and dashes.
The bucket name must not contain adjacent periods.


Custom Origins : The DNS domain name for the HTTP server from which you want CloudFront to get objects for this origin, for example, www.example.com .
Constraints for custom origins:

DomainName must be a valid DNS name that contains only a-z, A-Z, 0-9, dot (.), hyphen (-), or underscore (_) characters.
The name cannot exceed 128 characters.


OriginPath (string) --An optional element that causes CloudFront to request your content from a directory in your Amazon S3 bucket or your custom origin. When you include the OriginPath element, specify the directory name, beginning with a / . CloudFront appends the directory name to the value of DomainName , for example, example.com/production . Do not include a / at the end of the directory name.
For example, suppose you\'ve specified the following values for your distribution:

DomainName : An Amazon S3 bucket named myawsbucket .
OriginPath : /production
CNAME : example.com

When a user enters example.com/index.html in a browser, CloudFront sends a request to Amazon S3 for myawsbucket/production/index.html .
When a user enters example.com/acme/index.html in a browser, CloudFront sends a request to Amazon S3 for myawsbucket/production/acme/index.html .

CustomHeaders (dict) --A complex type that contains names and values for the custom headers that you want.

Quantity (integer) --The number of custom headers, if any, for this distribution.

Items (list) --
Optional : A list that contains one OriginCustomHeader element for each custom header that you want CloudFront to forward to the origin. If Quantity is 0 , omit Items .

(dict) --A complex type that contains HeaderName and HeaderValue elements, if any, for this distribution.

HeaderName (string) --The name of a header that you want CloudFront to forward to your origin. For more information, see Forwarding Custom Headers to Your Origin (Web Distributions Only) in the Amazon CloudFront Developer Guide .

HeaderValue (string) --The value for the header that you specified in the HeaderName field.







S3OriginConfig (dict) --A complex type that contains information about the Amazon S3 origin. If the origin is a custom origin, use the CustomOriginConfig element instead.

OriginAccessIdentity (string) --The CloudFront origin access identity to associate with the origin. Use an origin access identity to configure the origin so that viewers can only access objects in an Amazon S3 bucket through CloudFront. The format of the value is:
origin-access-identity/cloudfront/ID-of-origin-access-identity
where `` ID-of-origin-access-identity `` is the value that CloudFront returned in the ID element when you created the origin access identity.
If you want viewers to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty OriginAccessIdentity element.
To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty OriginAccessIdentity element.
To replace the origin access identity, update the distribution configuration and specify the new origin access identity.
For more information about the origin access identity, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .



CustomOriginConfig (dict) --A complex type that contains information about a custom origin. If the origin is an Amazon S3 bucket, use the S3OriginConfig element instead.

HTTPPort (integer) --The HTTP port the custom origin listens on.

HTTPSPort (integer) --The HTTPS port the custom origin listens on.

OriginProtocolPolicy (string) --The origin protocol policy to apply to your origin.

OriginSslProtocols (dict) --The SSL/TLS protocols that you want CloudFront to use when communicating with your origin over HTTPS.

Quantity (integer) --The number of SSL/TLS protocols that you want to allow CloudFront to use when establishing an HTTPS connection with this origin.

Items (list) --A list that contains allowed SSL/TLS protocols for this distribution.

(string) --




OriginReadTimeout (integer) --You can create a custom origin read timeout. All timeout units are in seconds. The default origin read timeout is 30 seconds, but you can configure custom timeout lengths using the CloudFront API. The minimum timeout length is 4 seconds; the maximum is 60 seconds.
If you need to increase the maximum time limit, contact the AWS Support Center .

OriginKeepaliveTimeout (integer) --You can create a custom keep-alive timeout. All timeout units are in seconds. The default keep-alive timeout is 5 seconds, but you can configure custom timeout lengths using the CloudFront API. The minimum timeout length is 1 second; the maximum is 60 seconds.
If you need to increase the maximum time limit, contact the AWS Support Center .









OriginGroups (dict) --A complex type that contains information about origin groups for this distribution.

Quantity (integer) --The number of origin groups.

Items (list) --The items (origin groups) in a distribution.

(dict) --An origin group includes two origins (a primary origin and a second origin to failover to) and a failover criteria that you specify. You create an origin group to support origin failover in CloudFront. When you create or update a distribution, you can specifiy the origin group instead of a single origin, and CloudFront will failover from the primary origin to the second origin under the failover conditions that you\'ve chosen.

Id (string) --The origin group\'s ID.

FailoverCriteria (dict) --A complex type that contains information about the failover criteria for an origin group.

StatusCodes (dict) --The status codes that, when returned from the primary origin, will trigger CloudFront to failover to the second origin.

Quantity (integer) --The number of status codes.

Items (list) --The items (status codes) for an origin group.

(integer) --






Members (dict) --A complex type that contains information about the origins in an origin group.

Quantity (integer) --The number of origins in an origin group.

Items (list) --Items (origins) in an origin group.

(dict) --An origin in an origin group.

OriginId (string) --The ID for an origin in an origin group.













DefaultCacheBehavior (dict) --A complex type that describes the default cache behavior if you don\'t specify a CacheBehavior element or if files don\'t match any of the values of PathPattern in CacheBehavior elements. You must create exactly one default cache behavior.

TargetOriginId (string) --The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior in your distribution.

ForwardedValues (dict) --A complex type that specifies how CloudFront handles query strings, cookies, and HTTP headers.

QueryString (boolean) --Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior and cache based on the query string parameters. CloudFront behavior depends on the value of QueryString and on the values that you specify for QueryStringCacheKeys , if any:
If you specify true for QueryString and you don\'t specify any values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin and caches based on all query string parameters. Depending on how many query string parameters and values you have, this can adversely affect performance because CloudFront must forward more requests to the origin.
If you specify true for QueryString and you specify one or more values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin, but it only caches based on the query string parameters that you specify.
If you specify false for QueryString , CloudFront doesn\'t forward any query string parameters to the origin, and doesn\'t cache based on query string parameters.
For more information, see Configuring CloudFront to Cache Based on Query String Parameters in the Amazon CloudFront Developer Guide .

Cookies (dict) --A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see How CloudFront Forwards, Caches, and Logs Cookies in the Amazon CloudFront Developer Guide .

Forward (string) --Specifies which cookies to forward to the origin for this cache behavior: all, none, or the list of cookies specified in the WhitelistedNames complex type.
Amazon S3 doesn\'t process cookies. When the cache behavior is forwarding requests to an Amazon S3 origin, specify none for the Forward element.

WhitelistedNames (dict) --Required if you specify whitelist for the value of Forward . A complex type that specifies how many different cookies you want CloudFront to forward to the origin for this cache behavior and, if you want to forward selected cookies, the names of those cookies.
If you specify all or none for the value of Forward , omit WhitelistedNames . If you change the value of Forward from whitelist to all or none and you don\'t delete the WhitelistedNames element and its child elements, CloudFront deletes them automatically.
For the current limit on the number of cookie names that you can whitelist for each cache behavior, see CloudFront Limits in the AWS General Reference .

Quantity (integer) --The number of different cookies that you want CloudFront to forward to the origin for this cache behavior. The value must equal the number of items that are in the Items field.
When you set Forward = whitelist (in the CookiePreferences object), this value must be 1 or higher.

Items (list) --A complex type that contains one Name element for each cookie that you want CloudFront to forward to the origin for this cache behavior. It must contain the same number of items that is specified in the Quantity field.
When you set Forward = whitelist (in the CookiePreferences object), this field must contain at least one item.

(string) --






Headers (dict) --A complex type that specifies the Headers , if any, that you want CloudFront to forward to the origin for this cache behavior (whitelisted headers). For the headers that you specify, CloudFront also caches separate versions of a specified object that is based on the header values in viewer requests.
For more information, see Caching Content Based on Request Headers in the Amazon CloudFront Developer Guide .

Quantity (integer) --The number of different headers that you want CloudFront to base caching on for this cache behavior. You can configure each cache behavior in a web distribution to do one of the following:

Forward all headers to your origin : Specify 1 for Quantity and * for Name .


Warning
CloudFront doesn\'t cache the objects that are associated with this cache behavior. Instead, CloudFront sends every request to the origin.


Forward a whitelist of headers you specify : Specify the number of headers that you want CloudFront to base caching on. Then specify the header names in Name elements. CloudFront caches your objects based on the values in the specified headers.
Forward only the default headers : Specify 0 for Quantity and omit Items . In this configuration, CloudFront doesn\'t cache based on the values in the request headers.

Regardless of which option you choose, CloudFront forwards headers to your origin based on whether the origin is an S3 bucket or a custom origin. See the following documentation:

S3 bucket : See HTTP Request Headers That CloudFront Removes or Updates
Custom origin : See HTTP Request Headers and CloudFront Behavior


Items (list) --A list that contains one Name element for each header that you want CloudFront to use for caching in this cache behavior. If Quantity is 0 , omit Items .

(string) --




QueryStringCacheKeys (dict) --A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.

Quantity (integer) --The number of whitelisted query string parameters for a cache behavior.

Items (list) --A list that contains the query string parameters that you want CloudFront to use as a basis for caching for a cache behavior. If Quantity is 0, you can omit Items .

(string) --






TrustedSigners (dict) --A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content.
If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled , and specify the applicable values for Quantity and Items . For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .
If you don\'t want to require signed URLs in requests for objects that match PathPattern , specify false for Enabled and 0 for Quantity . Omit Items .
To add, change, or remove one or more trusted signers, change Enabled to true (if it\'s currently false ), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.

Enabled (boolean) --Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .

Quantity (integer) --The number of trusted signers for this cache behavior.

Items (list) --
Optional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .

(string) --




ViewerProtocolPolicy (string) --The protocol that viewers can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern . You can specify the following options:

allow-all : Viewers can use HTTP or HTTPS.
redirect-to-https : If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.
https-only : If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).

For more information about requiring the HTTPS protocol, see Using an HTTPS Connection to Access Your Objects in the Amazon CloudFront Developer Guide .

Note
The only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects\' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .


MinTTL (integer) --The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .
You must specify 0 for MinTTL if you configure CloudFront to forward all headers to your origin (under Headers , if you specify 1 for Quantity and * for Name ).

AllowedMethods (dict) --A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices:

CloudFront forwards only GET and HEAD requests.
CloudFront forwards only GET , HEAD , and OPTIONS requests.
CloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests.

If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can\'t perform operations that you don\'t want them to. For example, you might not want users to have permissions to delete objects from your origin.

Quantity (integer) --The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET , HEAD , and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests).

Items (list) --A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.

(string) --


CachedMethods (dict) --A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices:

CloudFront caches responses to GET and HEAD requests.
CloudFront caches responses to GET , HEAD , and OPTIONS requests.

If you pick the second choice for your Amazon S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers, and Origin headers for the responses to be cached correctly.

Quantity (integer) --The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET , HEAD , and OPTIONS requests).

Items (list) --A complex type that contains the HTTP methods that you want CloudFront to cache responses to.

(string) --






SmoothStreaming (boolean) --Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true ; if not, specify false . If you specify true for SmoothStreaming , you can still distribute other content using this cache behavior if the content matches the value of PathPattern .

DefaultTTL (integer) --The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .

MaxTTL (integer) --The maximum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .

Compress (boolean) --Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify true ; if not, specify false . For more information, see Serving Compressed Files in the Amazon CloudFront Developer Guide .

LambdaFunctionAssociations (dict) --A complex type that contains zero or more Lambda function associations for a cache behavior.

Quantity (integer) --The number of Lambda function associations for this cache behavior.

Items (list) --
Optional : A complex type that contains LambdaFunctionAssociation items for this cache behavior. If Quantity is 0 , you can omit Items .

(dict) --A complex type that contains a Lambda function association.

LambdaFunctionARN (string) --The ARN of the Lambda function. You must specify the ARN of a function version; you can\'t specify a Lambda alias or $LATEST.

EventType (string) --Specifies the event type that triggers a Lambda function invocation. You can specify the following values:

viewer-request : The function executes when CloudFront receives a request from a viewer and before it checks to see whether the requested object is in the edge cache.
origin-request : The function executes only when CloudFront forwards a request to your origin. When the requested object is in the edge cache, the function doesn\'t execute.
origin-response : The function executes after CloudFront receives a response from the origin and before it caches the object in the response. When the requested object is in the edge cache, the function doesn\'t execute.
viewer-response : The function executes before CloudFront returns the requested object to the viewer. The function executes regardless of whether the object was already in the edge cache. If the origin returns an HTTP status code other than HTTP 200 (OK), the function doesn\'t execute.


IncludeBody (boolean) --A flag that allows a Lambda function to have read access to the body content. For more information, see Accessing the Request Body by Choosing the Include Body Option in the Amazon CloudFront Developer Guide.







FieldLevelEncryptionId (string) --The value of ID for the field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data for a cache behavior or for the default cache behavior in your distribution.



CacheBehaviors (dict) --A complex type that contains zero or more CacheBehavior elements.

Quantity (integer) --The number of cache behaviors for this distribution.

Items (list) --Optional: A complex type that contains cache behaviors for this distribution. If Quantity is 0 , you can omit Items .

(dict) --A complex type that describes how CloudFront processes requests.
You must create at least as many cache behaviors (including the default cache behavior) as you have origins if you want CloudFront to distribute objects from all of the origins. Each cache behavior specifies the one origin from which you want CloudFront to get objects. If you have two origins and only the default cache behavior, the default cache behavior will cause CloudFront to get objects from one of the origins, but the other origin is never used.
For the current limit on the number of cache behaviors that you can add to a distribution, see Amazon CloudFront Limits in the AWS General Reference .
If you don\'t want to specify any cache behaviors, include only an empty CacheBehaviors element. Don\'t include an empty CacheBehavior element, or CloudFront returns a MalformedXML error.
To delete all cache behaviors in an existing distribution, update the distribution configuration and include only an empty CacheBehaviors element.
To add, change, or remove one or more cache behaviors, update the distribution configuration and specify all of the cache behaviors that you want to include in the updated distribution.
For more information about cache behaviors, see Cache Behaviors in the Amazon CloudFront Developer Guide .

PathPattern (string) --The pattern (for example, images/*.jpg ) that specifies which requests to apply the behavior to. When CloudFront receives a viewer request, the requested path is compared with path patterns in the order in which cache behaviors are listed in the distribution.

Note
You can optionally include a slash (/ ) at the beginning of the path pattern. For example, /images/*.jpg . CloudFront behavior is the same with or without the leading / .

The path pattern for the default cache behavior is * and cannot be changed. If the request for an object does not match the path pattern for any cache behaviors, CloudFront applies the behavior in the default cache behavior.
For more information, see Path Pattern in the Amazon CloudFront Developer Guide .

TargetOriginId (string) --The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior in your distribution.

ForwardedValues (dict) --A complex type that specifies how CloudFront handles query strings, cookies, and HTTP headers.

QueryString (boolean) --Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior and cache based on the query string parameters. CloudFront behavior depends on the value of QueryString and on the values that you specify for QueryStringCacheKeys , if any:
If you specify true for QueryString and you don\'t specify any values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin and caches based on all query string parameters. Depending on how many query string parameters and values you have, this can adversely affect performance because CloudFront must forward more requests to the origin.
If you specify true for QueryString and you specify one or more values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin, but it only caches based on the query string parameters that you specify.
If you specify false for QueryString , CloudFront doesn\'t forward any query string parameters to the origin, and doesn\'t cache based on query string parameters.
For more information, see Configuring CloudFront to Cache Based on Query String Parameters in the Amazon CloudFront Developer Guide .

Cookies (dict) --A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see How CloudFront Forwards, Caches, and Logs Cookies in the Amazon CloudFront Developer Guide .

Forward (string) --Specifies which cookies to forward to the origin for this cache behavior: all, none, or the list of cookies specified in the WhitelistedNames complex type.
Amazon S3 doesn\'t process cookies. When the cache behavior is forwarding requests to an Amazon S3 origin, specify none for the Forward element.

WhitelistedNames (dict) --Required if you specify whitelist for the value of Forward . A complex type that specifies how many different cookies you want CloudFront to forward to the origin for this cache behavior and, if you want to forward selected cookies, the names of those cookies.
If you specify all or none for the value of Forward , omit WhitelistedNames . If you change the value of Forward from whitelist to all or none and you don\'t delete the WhitelistedNames element and its child elements, CloudFront deletes them automatically.
For the current limit on the number of cookie names that you can whitelist for each cache behavior, see CloudFront Limits in the AWS General Reference .

Quantity (integer) --The number of different cookies that you want CloudFront to forward to the origin for this cache behavior. The value must equal the number of items that are in the Items field.
When you set Forward = whitelist (in the CookiePreferences object), this value must be 1 or higher.

Items (list) --A complex type that contains one Name element for each cookie that you want CloudFront to forward to the origin for this cache behavior. It must contain the same number of items that is specified in the Quantity field.
When you set Forward = whitelist (in the CookiePreferences object), this field must contain at least one item.

(string) --






Headers (dict) --A complex type that specifies the Headers , if any, that you want CloudFront to forward to the origin for this cache behavior (whitelisted headers). For the headers that you specify, CloudFront also caches separate versions of a specified object that is based on the header values in viewer requests.
For more information, see Caching Content Based on Request Headers in the Amazon CloudFront Developer Guide .

Quantity (integer) --The number of different headers that you want CloudFront to base caching on for this cache behavior. You can configure each cache behavior in a web distribution to do one of the following:

Forward all headers to your origin : Specify 1 for Quantity and * for Name .


Warning
CloudFront doesn\'t cache the objects that are associated with this cache behavior. Instead, CloudFront sends every request to the origin.


Forward a whitelist of headers you specify : Specify the number of headers that you want CloudFront to base caching on. Then specify the header names in Name elements. CloudFront caches your objects based on the values in the specified headers.
Forward only the default headers : Specify 0 for Quantity and omit Items . In this configuration, CloudFront doesn\'t cache based on the values in the request headers.

Regardless of which option you choose, CloudFront forwards headers to your origin based on whether the origin is an S3 bucket or a custom origin. See the following documentation:

S3 bucket : See HTTP Request Headers That CloudFront Removes or Updates
Custom origin : See HTTP Request Headers and CloudFront Behavior


Items (list) --A list that contains one Name element for each header that you want CloudFront to use for caching in this cache behavior. If Quantity is 0 , omit Items .

(string) --




QueryStringCacheKeys (dict) --A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.

Quantity (integer) --The number of whitelisted query string parameters for a cache behavior.

Items (list) --A list that contains the query string parameters that you want CloudFront to use as a basis for caching for a cache behavior. If Quantity is 0, you can omit Items .

(string) --






TrustedSigners (dict) --A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content.
If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled , and specify the applicable values for Quantity and Items . For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .
If you don\'t want to require signed URLs in requests for objects that match PathPattern , specify false for Enabled and 0 for Quantity . Omit Items .
To add, change, or remove one or more trusted signers, change Enabled to true (if it\'s currently false ), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.

Enabled (boolean) --Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .

Quantity (integer) --The number of trusted signers for this cache behavior.

Items (list) --
Optional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .

(string) --




ViewerProtocolPolicy (string) --The protocol that viewers can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern . You can specify the following options:

allow-all : Viewers can use HTTP or HTTPS.
redirect-to-https : If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.
https-only : If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).

For more information about requiring the HTTPS protocol, see Using an HTTPS Connection to Access Your Objects in the Amazon CloudFront Developer Guide .

Note
The only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects\' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .


MinTTL (integer) --The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .
You must specify 0 for MinTTL if you configure CloudFront to forward all headers to your origin (under Headers , if you specify 1 for Quantity and * for Name ).

AllowedMethods (dict) --A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices:

CloudFront forwards only GET and HEAD requests.
CloudFront forwards only GET , HEAD , and OPTIONS requests.
CloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests.

If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can\'t perform operations that you don\'t want them to. For example, you might not want users to have permissions to delete objects from your origin.

Quantity (integer) --The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET , HEAD , and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests).

Items (list) --A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.

(string) --


CachedMethods (dict) --A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices:

CloudFront caches responses to GET and HEAD requests.
CloudFront caches responses to GET , HEAD , and OPTIONS requests.

If you pick the second choice for your Amazon S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers, and Origin headers for the responses to be cached correctly.

Quantity (integer) --The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET , HEAD , and OPTIONS requests).

Items (list) --A complex type that contains the HTTP methods that you want CloudFront to cache responses to.

(string) --






SmoothStreaming (boolean) --Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true ; if not, specify false . If you specify true for SmoothStreaming , you can still distribute other content using this cache behavior if the content matches the value of PathPattern .

DefaultTTL (integer) --The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .

MaxTTL (integer) --The maximum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .

Compress (boolean) --Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify true; if not, specify false. For more information, see Serving Compressed Files in the Amazon CloudFront Developer Guide .

LambdaFunctionAssociations (dict) --A complex type that contains zero or more Lambda function associations for a cache behavior.

Quantity (integer) --The number of Lambda function associations for this cache behavior.

Items (list) --
Optional : A complex type that contains LambdaFunctionAssociation items for this cache behavior. If Quantity is 0 , you can omit Items .

(dict) --A complex type that contains a Lambda function association.

LambdaFunctionARN (string) --The ARN of the Lambda function. You must specify the ARN of a function version; you can\'t specify a Lambda alias or $LATEST.

EventType (string) --Specifies the event type that triggers a Lambda function invocation. You can specify the following values:

viewer-request : The function executes when CloudFront receives a request from a viewer and before it checks to see whether the requested object is in the edge cache.
origin-request : The function executes only when CloudFront forwards a request to your origin. When the requested object is in the edge cache, the function doesn\'t execute.
origin-response : The function executes after CloudFront receives a response from the origin and before it caches the object in the response. When the requested object is in the edge cache, the function doesn\'t execute.
viewer-response : The function executes before CloudFront returns the requested object to the viewer. The function executes regardless of whether the object was already in the edge cache. If the origin returns an HTTP status code other than HTTP 200 (OK), the function doesn\'t execute.


IncludeBody (boolean) --A flag that allows a Lambda function to have read access to the body content. For more information, see Accessing the Request Body by Choosing the Include Body Option in the Amazon CloudFront Developer Guide.







FieldLevelEncryptionId (string) --The value of ID for the field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data for a cache behavior or for the default cache behavior in your distribution.







CustomErrorResponses (dict) --A complex type that controls the following:

Whether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.
How long CloudFront caches HTTP status codes in the 4xx and 5xx range.

For more information about custom error pages, see Customizing Error Responses in the Amazon CloudFront Developer Guide .

Quantity (integer) --The number of HTTP status codes for which you want to specify a custom error page and/or a caching duration. If Quantity is 0 , you can omit Items .

Items (list) --A complex type that contains a CustomErrorResponse element for each HTTP status code for which you want to specify a custom error page and/or a caching duration.

(dict) --A complex type that controls:

Whether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.
How long CloudFront caches HTTP status codes in the 4xx and 5xx range.

For more information about custom error pages, see Customizing Error Responses in the Amazon CloudFront Developer Guide .

ErrorCode (integer) --The HTTP status code for which you want to specify a custom error page and/or a caching duration.

ResponsePagePath (string) --The path to the custom error page that you want CloudFront to return to a viewer when your origin returns the HTTP status code specified by ErrorCode , for example, /4xx-errors/403-forbidden.html . If you want to store your objects and your custom error pages in different locations, your distribution must include a cache behavior for which the following is true:

The value of PathPattern matches the path to your custom error messages. For example, suppose you saved custom error pages for 4xx errors in an Amazon S3 bucket in a directory named /4xx-errors . Your distribution must include a cache behavior for which the path pattern routes requests for your custom error pages to that location, for example, /4xx-errors/* .
The value of TargetOriginId specifies the value of the ID element for the origin that contains your custom error pages.

If you specify a value for ResponsePagePath , you must also specify a value for ResponseCode .
We recommend that you store custom error pages in an Amazon S3 bucket. If you store custom error pages on an HTTP server and the server starts to return 5xx errors, CloudFront can\'t get the files that you want to return to viewers because the origin server is unavailable.

ResponseCode (string) --The HTTP status code that you want CloudFront to return to the viewer along with the custom error page. There are a variety of reasons that you might want CloudFront to return a status code different from the status code that your origin returned to CloudFront, for example:

Some Internet devices (some firewalls and corporate proxies, for example) intercept HTTP 4xx and 5xx and prevent the response from being returned to the viewer. If you substitute 200 , the response typically won\'t be intercepted.
If you don\'t care about distinguishing among different client errors or server errors, you can specify 400 or 500 as the ResponseCode for all 4xx or 5xx errors.
You might want to return a 200 status code (OK) and static website so your customers don\'t know that your website is down.

If you specify a value for ResponseCode , you must also specify a value for ResponsePagePath .

ErrorCachingMinTTL (integer) --The minimum amount of time, in seconds, that you want CloudFront to cache the HTTP status code specified in ErrorCode . When this time period has elapsed, CloudFront queries your origin to see whether the problem that caused the error has been resolved and the requested object is now available.
For more information, see Customizing Error Responses in the Amazon CloudFront Developer Guide .







Comment (string) --Any comments you want to include about the distribution.
If you don\'t want to specify a comment, include an empty Comment element.
To delete an existing comment, update the distribution configuration and include an empty Comment element.
To add or change a comment, update the distribution configuration and specify the new comment.

Logging (dict) --A complex type that controls whether access logs are written for the distribution.
For more information about logging, see Access Logs in the Amazon CloudFront Developer Guide .

Enabled (boolean) --Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you don\'t want to enable logging when you create a distribution or if you want to disable logging for an existing distribution, specify false for Enabled , and specify empty Bucket and Prefix elements. If you specify false for Enabled but you specify values for Bucket , prefix , and IncludeCookies , the values are automatically deleted.

IncludeCookies (boolean) --Specifies whether you want CloudFront to include cookies in access logs, specify true for IncludeCookies . If you choose to include cookies in logs, CloudFront logs all cookies regardless of how you configure the cache behaviors for this distribution. If you don\'t want to include cookies when you create a distribution or if you want to disable include cookies for an existing distribution, specify false for IncludeCookies .

Bucket (string) --The Amazon S3 bucket to store the access logs in, for example, myawslogbucket.s3.amazonaws.com .

Prefix (string) --An optional string that you want CloudFront to prefix to the access log filenames for this distribution, for example, myprefix/ . If you want to enable logging, but you don\'t want to specify a prefix, you still must include an empty Prefix element in the Logging element.



PriceClass (string) --The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify PriceClass_All , CloudFront responds to requests for your objects from all CloudFront edge locations.
If you specify a price class other than PriceClass_All , CloudFront serves your objects from the CloudFront edge location that has the lowest latency among the edge locations in your price class. Viewers who are in or near regions that are excluded from your specified price class may encounter slower performance.
For more information about price classes, see Choosing the Price Class for a CloudFront Distribution in the Amazon CloudFront Developer Guide . For information about CloudFront pricing, including how price classes (such as Price Class 100) map to CloudFront regions, see Amazon CloudFront Pricing . For price class information, scroll down to see the table at the bottom of the page.

Enabled (boolean) --From this field, you can enable or disable the selected distribution.

ViewerCertificate (dict) --A complex type that determines the distribution\xe2\x80\x99s SSL/TLS configuration for communicating with viewers.

CloudFrontDefaultCertificate (boolean) --If the distribution uses the CloudFront domain name such as d111111abcdef8.cloudfront.net , set this field to true .
If the distribution uses Aliases (alternate domain names or CNAMEs), set this field to false and specify values for the following fields:

ACMCertificateArn or IAMCertificateId (specify a value for one, not both)
MinimumProtocolVersion
SSLSupportMethod


IAMCertificateId (string) --If the distribution uses Aliases (alternate domain names or CNAMEs) and the SSL/TLS certificate is stored in AWS Identity and Access Management (AWS IAM) , provide the ID of the IAM certificate.
If you specify an IAM certificate ID, you must also specify values for MinimumProtocolVerison and SSLSupportMethod .

ACMCertificateArn (string) --If the distribution uses Aliases (alternate domain names or CNAMEs) and the SSL/TLS certificate is stored in AWS Certificate Manager (ACM) , provide the Amazon Resource Name (ARN) of the ACM certificate. CloudFront only supports ACM certificates in the US East (N. Virginia) Region (us-east-1 ).
If you specify an ACM certificate ARN, you must also specify values for MinimumProtocolVerison and SSLSupportMethod .

SSLSupportMethod (string) --If the distribution uses Aliases (alternate domain names or CNAMEs), specify which viewers the distribution accepts HTTPS connections from.

sni-only \xe2\x80\x93 The distribution accepts HTTPS connections from only viewers that support server name indication (SNI) . This is recommended. Most browsers and clients released after 2010 support SNI.
vip \xe2\x80\x93 The distribution accepts HTTPS connections from all viewers including those that don\xe2\x80\x99t support SNI. This is not recommended, and results in additional monthly charges from CloudFront.

If the distribution uses the CloudFront domain name such as d111111abcdef8.cloudfront.net , don\xe2\x80\x99t set a value for this field.

MinimumProtocolVersion (string) --If the distribution uses Aliases (alternate domain names or CNAMEs), specify the security policy that you want CloudFront to use for HTTPS connections with viewers. The security policy determines two settings:

The minimum SSL/TLS protocol that CloudFront can use to communicate with viewers.
The ciphers that CloudFront can use to encrypt the content that it returns to viewers.

For more information, see Security Policy and Supported Protocols and Ciphers Between Viewers and CloudFront in the Amazon CloudFront Developer Guide .

Note
On the CloudFront console, this setting is called Security Policy .

We recommend that you specify TLSv1.2_2018 unless your viewers are using browsers or devices that don\xe2\x80\x99t support TLSv1.2.
When you\xe2\x80\x99re using SNI only (you set SSLSupportMethod to sni-only ), you must specify TLSv1 or higher.
If the distribution uses the CloudFront domain name such as d111111abcdef8.cloudfront.net (you set CloudFrontDefaultCertificate to true ), CloudFront automatically sets the security policy to TLSv1 regardless of the value that you set here.

Certificate (string) --This field is deprecated. Use one of the following fields instead:

ACMCertificateArn
IAMCertificateId
CloudFrontDefaultCertificate


CertificateSource (string) --This field is deprecated. Use one of the following fields instead:

ACMCertificateArn
IAMCertificateId
CloudFrontDefaultCertificate




Restrictions (dict) --A complex type that identifies ways in which you want to restrict distribution of your content.

GeoRestriction (dict) --A complex type that controls the countries in which your content is distributed. CloudFront determines the location of your users using MaxMind GeoIP databases.

RestrictionType (string) --The method that you want to use to restrict distribution of your content by country:

none : No geo restriction is enabled, meaning access to content is not restricted by client geo location.
blacklist : The Location elements specify the countries in which you don\'t want CloudFront to distribute your content.
whitelist : The Location elements specify the countries in which you want CloudFront to distribute your content.


Quantity (integer) --When geo restriction is enabled , this is the number of countries in your whitelist or blacklist . Otherwise, when it is not enabled, Quantity is 0 , and you can omit Items .

Items (list) --A complex type that contains a Location element for each country in which you want CloudFront either to distribute your content (whitelist ) or not distribute your content (blacklist ).
The Location element is a two-letter, uppercase country code for a country that you want to include in your blacklist or whitelist . Include one Location element for each country.
CloudFront and MaxMind both use ISO 3166 country codes. For the current list of countries and the corresponding codes, see ISO 3166-1-alpha-2 code on the International Organization for Standardization website. You can also refer to the country list on the CloudFront console, which includes both country names and codes.

(string) --






WebACLId (string) --A unique identifier that specifies the AWS WAF web ACL, if any, to associate with this distribution. To specify a web ACL created using the latest version of AWS WAF, use the ACL ARN, for example arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/473e64fd-f30b-4765-81a0-62ad96dd167a . To specify a web ACL created using AWS WAF Classic, use the ACL ID, for example 473e64fd-f30b-4765-81a0-62ad96dd167a .
AWS WAF is a web application firewall that lets you monitor the HTTP and HTTPS requests that are forwarded to CloudFront, and lets you control access to your content. Based on conditions that you specify, such as the IP addresses that requests originate from or the values of query strings, CloudFront responds to requests either with the requested content or with an HTTP 403 status code (Forbidden). You can also configure CloudFront to return a custom error page when a request is blocked. For more information about AWS WAF, see the AWS WAF Developer Guide .

HttpVersion (string) --(Optional) Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront. The default value for new web distributions is http2. Viewers that don\'t support HTTP/2 automatically use an earlier HTTP version.
For viewers and CloudFront to use HTTP/2, viewers must support TLS 1.2 or later, and must support Server Name Identification (SNI).
In general, configuring CloudFront to communicate with viewers using HTTP/2 reduces latency. You can improve performance by optimizing for HTTP/2. For more information, do an Internet search for "http/2 optimization."

IsIPV6Enabled (boolean) --If you want CloudFront to respond to IPv6 DNS requests with an IPv6 address for your distribution, specify true . If you specify false , CloudFront responds to IPv6 DNS requests with the DNS response code NOERROR and with no IP addresses. This allows viewers to submit a second request, for an IPv4 address for your distribution.
In general, you should enable IPv6 if you have users on IPv6 networks who want to access your content. However, if you\'re using signed URLs or signed cookies to restrict access to your content, and if you\'re using a custom policy that includes the IpAddress parameter to restrict the IP addresses that can access your content, don\'t enable IPv6. If you want to restrict access to some content by IP address and not restrict access to other content (or restrict access but not by IP address), you can create two distributions. For more information, see Creating a Signed URL Using a Custom Policy in the Amazon CloudFront Developer Guide .
If you\'re using an Amazon Route 53 alias resource record set to route traffic to your CloudFront distribution, you need to create a second alias resource record set when both of the following are true:

You enable IPv6 for the distribution
You\'re using alternate domain names in the URLs for your objects

For more information, see Routing Traffic to an Amazon CloudFront Web Distribution by Using Your Domain Name in the Amazon Route 53 Developer Guide .
If you created a CNAME resource record set, either with Amazon Route 53 or with another DNS service, you don\'t need to make any changes. A CNAME record will route traffic to your distribution regardless of the IP address format of the viewer request.



ETag (string) --The current version of the configuration. For example: E2QWRUHAPOMQZL .






Exceptions

CloudFront.Client.exceptions.NoSuchDistribution
CloudFront.Client.exceptions.AccessDenied


    :return: {
        'DistributionConfig': {
            'CallerReference': 'string',
            'Aliases': {
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'DefaultRootObject': 'string',
            'Origins': {
                'Quantity': 123,
                'Items': [
                    {
                        'Id': 'string',
                        'DomainName': 'string',
                        'OriginPath': 'string',
                        'CustomHeaders': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'HeaderName': 'string',
                                    'HeaderValue': 'string'
                                },
                            ]
                        },
                        'S3OriginConfig': {
                            'OriginAccessIdentity': 'string'
                        },
                        'CustomOriginConfig': {
                            'HTTPPort': 123,
                            'HTTPSPort': 123,
                            'OriginProtocolPolicy': 'http-only'|'match-viewer'|'https-only',
                            'OriginSslProtocols': {
                                'Quantity': 123,
                                'Items': [
                                    'SSLv3'|'TLSv1'|'TLSv1.1'|'TLSv1.2',
                                ]
                            },
                            'OriginReadTimeout': 123,
                            'OriginKeepaliveTimeout': 123
                        }
                    },
                ]
            },
            'OriginGroups': {
                'Quantity': 123,
                'Items': [
                    {
                        'Id': 'string',
                        'FailoverCriteria': {
                            'StatusCodes': {
                                'Quantity': 123,
                                'Items': [
                                    123,
                                ]
                            }
                        },
                        'Members': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'OriginId': 'string'
                                },
                            ]
                        }
                    },
                ]
            },
            'DefaultCacheBehavior': {
                'TargetOriginId': 'string',
                'ForwardedValues': {
                    'QueryString': True|False,
                    'Cookies': {
                        'Forward': 'none'|'whitelist'|'all',
                        'WhitelistedNames': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                    'Headers': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    },
                    'QueryStringCacheKeys': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    }
                },
                'TrustedSigners': {
                    'Enabled': True|False,
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                'MinTTL': 123,
                'AllowedMethods': {
                    'Quantity': 123,
                    'Items': [
                        'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                    ],
                    'CachedMethods': {
                        'Quantity': 123,
                        'Items': [
                            'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                        ]
                    }
                },
                'SmoothStreaming': True|False,
                'DefaultTTL': 123,
                'MaxTTL': 123,
                'Compress': True|False,
                'LambdaFunctionAssociations': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'LambdaFunctionARN': 'string',
                            'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                            'IncludeBody': True|False
                        },
                    ]
                },
                'FieldLevelEncryptionId': 'string'
            },
            'CacheBehaviors': {
                'Quantity': 123,
                'Items': [
                    {
                        'PathPattern': 'string',
                        'TargetOriginId': 'string',
                        'ForwardedValues': {
                            'QueryString': True|False,
                            'Cookies': {
                                'Forward': 'none'|'whitelist'|'all',
                                'WhitelistedNames': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                }
                            },
                            'Headers': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            },
                            'QueryStringCacheKeys': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                        'TrustedSigners': {
                            'Enabled': True|False,
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        },
                        'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                        'MinTTL': 123,
                        'AllowedMethods': {
                            'Quantity': 123,
                            'Items': [
                                'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                            ],
                            'CachedMethods': {
                                'Quantity': 123,
                                'Items': [
                                    'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                ]
                            }
                        },
                        'SmoothStreaming': True|False,
                        'DefaultTTL': 123,
                        'MaxTTL': 123,
                        'Compress': True|False,
                        'LambdaFunctionAssociations': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'LambdaFunctionARN': 'string',
                                    'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                    'IncludeBody': True|False
                                },
                            ]
                        },
                        'FieldLevelEncryptionId': 'string'
                    },
                ]
            },
            'CustomErrorResponses': {
                'Quantity': 123,
                'Items': [
                    {
                        'ErrorCode': 123,
                        'ResponsePagePath': 'string',
                        'ResponseCode': 'string',
                        'ErrorCachingMinTTL': 123
                    },
                ]
            },
            'Comment': 'string',
            'Logging': {
                'Enabled': True|False,
                'IncludeCookies': True|False,
                'Bucket': 'string',
                'Prefix': 'string'
            },
            'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
            'Enabled': True|False,
            'ViewerCertificate': {
                'CloudFrontDefaultCertificate': True|False,
                'IAMCertificateId': 'string',
                'ACMCertificateArn': 'string',
                'SSLSupportMethod': 'sni-only'|'vip',
                'MinimumProtocolVersion': 'SSLv3'|'TLSv1'|'TLSv1_2016'|'TLSv1.1_2016'|'TLSv1.2_2018',
                'Certificate': 'string',
                'CertificateSource': 'cloudfront'|'iam'|'acm'
            },
            'Restrictions': {
                'GeoRestriction': {
                    'RestrictionType': 'blacklist'|'whitelist'|'none',
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                }
            },
            'WebACLId': 'string',
            'HttpVersion': 'http1.1'|'http2',
            'IsIPV6Enabled': True|False
        },
        'ETag': 'string'
    }
    
    
    :returns: 
    If you configured Amazon S3 Transfer Acceleration for your bucket, don\'t specify the s3-accelerate endpoint for DomainName .
    The bucket name must be between 3 and 63 characters long (inclusive).
    The bucket name must contain only lowercase characters, numbers, periods, underscores, and dashes.
    The bucket name must not contain adjacent periods.
    
    """
    pass

def get_field_level_encryption(Id=None):
    """
    Get the field-level encryption configuration information.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_field_level_encryption(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nRequest the ID for the field-level encryption configuration information.\n

    :rtype: dict
ReturnsResponse Syntax{
    'FieldLevelEncryption': {
        'Id': 'string',
        'LastModifiedTime': datetime(2015, 1, 1),
        'FieldLevelEncryptionConfig': {
            'CallerReference': 'string',
            'Comment': 'string',
            'QueryArgProfileConfig': {
                'ForwardWhenQueryArgProfileIsUnknown': True|False,
                'QueryArgProfiles': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'QueryArg': 'string',
                            'ProfileId': 'string'
                        },
                    ]
                }
            },
            'ContentTypeProfileConfig': {
                'ForwardWhenContentTypeIsUnknown': True|False,
                'ContentTypeProfiles': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'Format': 'URLEncoded',
                            'ProfileId': 'string',
                            'ContentType': 'string'
                        },
                    ]
                }
            }
        }
    },
    'ETag': 'string'
}


Response Structure

(dict) --
FieldLevelEncryption (dict) --Return the field-level encryption configuration information.

Id (string) --The configuration ID for a field-level encryption configuration which includes a set of profiles that specify certain selected data fields to be encrypted by specific public keys.

LastModifiedTime (datetime) --The last time the field-level encryption configuration was changed.

FieldLevelEncryptionConfig (dict) --A complex data type that includes the profile configurations specified for field-level encryption.

CallerReference (string) --A unique number that ensures the request can\'t be replayed.

Comment (string) --An optional comment about the configuration.

QueryArgProfileConfig (dict) --A complex data type that specifies when to forward content if a profile isn\'t found and the profile that can be provided as a query argument in a request.

ForwardWhenQueryArgProfileIsUnknown (boolean) --Flag to set if you want a request to be forwarded to the origin even if the profile specified by the field-level encryption query argument, fle-profile, is unknown.

QueryArgProfiles (dict) --Profiles specified for query argument-profile mapping for field-level encryption.

Quantity (integer) --Number of profiles for query argument-profile mapping for field-level encryption.

Items (list) --Number of items for query argument-profile mapping for field-level encryption.

(dict) --Query argument-profile mapping for field-level encryption.

QueryArg (string) --Query argument for field-level encryption query argument-profile mapping.

ProfileId (string) --ID of profile to use for field-level encryption query argument-profile mapping









ContentTypeProfileConfig (dict) --A complex data type that specifies when to forward content if a content type isn\'t recognized and profiles to use as by default in a request if a query argument doesn\'t specify a profile to use.

ForwardWhenContentTypeIsUnknown (boolean) --The setting in a field-level encryption content type-profile mapping that specifies what to do when an unknown content type is provided for the profile. If true, content is forwarded without being encrypted when the content type is unknown. If false (the default), an error is returned when the content type is unknown.

ContentTypeProfiles (dict) --The configuration for a field-level encryption content type-profile.

Quantity (integer) --The number of field-level encryption content type-profile mappings.

Items (list) --Items in a field-level encryption content type-profile mapping.

(dict) --A field-level encryption content type profile.

Format (string) --The format for a field-level encryption content type-profile mapping.

ProfileId (string) --The profile ID for a field-level encryption content type-profile mapping.

ContentType (string) --The content type for a field-level encryption content type-profile mapping.













ETag (string) --The current version of the field level encryption configuration. For example: E2QWRUHAPOMQZL .






Exceptions

CloudFront.Client.exceptions.AccessDenied
CloudFront.Client.exceptions.NoSuchFieldLevelEncryptionConfig


    :return: {
        'FieldLevelEncryption': {
            'Id': 'string',
            'LastModifiedTime': datetime(2015, 1, 1),
            'FieldLevelEncryptionConfig': {
                'CallerReference': 'string',
                'Comment': 'string',
                'QueryArgProfileConfig': {
                    'ForwardWhenQueryArgProfileIsUnknown': True|False,
                    'QueryArgProfiles': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'QueryArg': 'string',
                                'ProfileId': 'string'
                            },
                        ]
                    }
                },
                'ContentTypeProfileConfig': {
                    'ForwardWhenContentTypeIsUnknown': True|False,
                    'ContentTypeProfiles': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'Format': 'URLEncoded',
                                'ProfileId': 'string',
                                'ContentType': 'string'
                            },
                        ]
                    }
                }
            }
        },
        'ETag': 'string'
    }
    
    
    """
    pass

def get_field_level_encryption_config(Id=None):
    """
    Get the field-level encryption configuration information.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_field_level_encryption_config(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nRequest the ID for the field-level encryption configuration information.\n

    :rtype: dict
ReturnsResponse Syntax{
    'FieldLevelEncryptionConfig': {
        'CallerReference': 'string',
        'Comment': 'string',
        'QueryArgProfileConfig': {
            'ForwardWhenQueryArgProfileIsUnknown': True|False,
            'QueryArgProfiles': {
                'Quantity': 123,
                'Items': [
                    {
                        'QueryArg': 'string',
                        'ProfileId': 'string'
                    },
                ]
            }
        },
        'ContentTypeProfileConfig': {
            'ForwardWhenContentTypeIsUnknown': True|False,
            'ContentTypeProfiles': {
                'Quantity': 123,
                'Items': [
                    {
                        'Format': 'URLEncoded',
                        'ProfileId': 'string',
                        'ContentType': 'string'
                    },
                ]
            }
        }
    },
    'ETag': 'string'
}


Response Structure

(dict) --
FieldLevelEncryptionConfig (dict) --Return the field-level encryption configuration information.

CallerReference (string) --A unique number that ensures the request can\'t be replayed.

Comment (string) --An optional comment about the configuration.

QueryArgProfileConfig (dict) --A complex data type that specifies when to forward content if a profile isn\'t found and the profile that can be provided as a query argument in a request.

ForwardWhenQueryArgProfileIsUnknown (boolean) --Flag to set if you want a request to be forwarded to the origin even if the profile specified by the field-level encryption query argument, fle-profile, is unknown.

QueryArgProfiles (dict) --Profiles specified for query argument-profile mapping for field-level encryption.

Quantity (integer) --Number of profiles for query argument-profile mapping for field-level encryption.

Items (list) --Number of items for query argument-profile mapping for field-level encryption.

(dict) --Query argument-profile mapping for field-level encryption.

QueryArg (string) --Query argument for field-level encryption query argument-profile mapping.

ProfileId (string) --ID of profile to use for field-level encryption query argument-profile mapping









ContentTypeProfileConfig (dict) --A complex data type that specifies when to forward content if a content type isn\'t recognized and profiles to use as by default in a request if a query argument doesn\'t specify a profile to use.

ForwardWhenContentTypeIsUnknown (boolean) --The setting in a field-level encryption content type-profile mapping that specifies what to do when an unknown content type is provided for the profile. If true, content is forwarded without being encrypted when the content type is unknown. If false (the default), an error is returned when the content type is unknown.

ContentTypeProfiles (dict) --The configuration for a field-level encryption content type-profile.

Quantity (integer) --The number of field-level encryption content type-profile mappings.

Items (list) --Items in a field-level encryption content type-profile mapping.

(dict) --A field-level encryption content type profile.

Format (string) --The format for a field-level encryption content type-profile mapping.

ProfileId (string) --The profile ID for a field-level encryption content type-profile mapping.

ContentType (string) --The content type for a field-level encryption content type-profile mapping.











ETag (string) --The current version of the field level encryption configuration. For example: E2QWRUHAPOMQZL .






Exceptions

CloudFront.Client.exceptions.AccessDenied
CloudFront.Client.exceptions.NoSuchFieldLevelEncryptionConfig


    :return: {
        'FieldLevelEncryptionConfig': {
            'CallerReference': 'string',
            'Comment': 'string',
            'QueryArgProfileConfig': {
                'ForwardWhenQueryArgProfileIsUnknown': True|False,
                'QueryArgProfiles': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'QueryArg': 'string',
                            'ProfileId': 'string'
                        },
                    ]
                }
            },
            'ContentTypeProfileConfig': {
                'ForwardWhenContentTypeIsUnknown': True|False,
                'ContentTypeProfiles': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'Format': 'URLEncoded',
                            'ProfileId': 'string',
                            'ContentType': 'string'
                        },
                    ]
                }
            }
        },
        'ETag': 'string'
    }
    
    
    """
    pass

def get_field_level_encryption_profile(Id=None):
    """
    Get the field-level encryption profile information.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_field_level_encryption_profile(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nGet the ID for the field-level encryption profile information.\n

    :rtype: dict
ReturnsResponse Syntax{
    'FieldLevelEncryptionProfile': {
        'Id': 'string',
        'LastModifiedTime': datetime(2015, 1, 1),
        'FieldLevelEncryptionProfileConfig': {
            'Name': 'string',
            'CallerReference': 'string',
            'Comment': 'string',
            'EncryptionEntities': {
                'Quantity': 123,
                'Items': [
                    {
                        'PublicKeyId': 'string',
                        'ProviderId': 'string',
                        'FieldPatterns': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                ]
            }
        }
    },
    'ETag': 'string'
}


Response Structure

(dict) --
FieldLevelEncryptionProfile (dict) --Return the field-level encryption profile information.

Id (string) --The ID for a field-level encryption profile configuration which includes a set of profiles that specify certain selected data fields to be encrypted by specific public keys.

LastModifiedTime (datetime) --The last time the field-level encryption profile was updated.

FieldLevelEncryptionProfileConfig (dict) --A complex data type that includes the profile name and the encryption entities for the field-level encryption profile.

Name (string) --Profile name for the field-level encryption profile.

CallerReference (string) --A unique number that ensures that the request can\'t be replayed.

Comment (string) --An optional comment for the field-level encryption profile.

EncryptionEntities (dict) --A complex data type of encryption entities for the field-level encryption profile that include the public key ID, provider, and field patterns for specifying which fields to encrypt with this key.

Quantity (integer) --Number of field pattern items in a field-level encryption content type-profile mapping.

Items (list) --An array of field patterns in a field-level encryption content type-profile mapping.

(dict) --Complex data type for field-level encryption profiles that includes the encryption key and field pattern specifications.

PublicKeyId (string) --The public key associated with a set of field-level encryption patterns, to be used when encrypting the fields that match the patterns.

ProviderId (string) --The provider associated with the public key being used for encryption. This value must also be provided with the private key for applications to be able to decrypt data.

FieldPatterns (dict) --Field patterns in a field-level encryption content type profile specify the fields that you want to be encrypted. You can provide the full field name, or any beginning characters followed by a wildcard (*). You can\'t overlap field patterns. For example, you can\'t have both ABC* and AB*. Note that field patterns are case-sensitive.

Quantity (integer) --The number of field-level encryption field patterns.

Items (list) --An array of the field-level encryption field patterns.

(string) --














ETag (string) --The current version of the field level encryption profile. For example: E2QWRUHAPOMQZL .






Exceptions

CloudFront.Client.exceptions.AccessDenied
CloudFront.Client.exceptions.NoSuchFieldLevelEncryptionProfile


    :return: {
        'FieldLevelEncryptionProfile': {
            'Id': 'string',
            'LastModifiedTime': datetime(2015, 1, 1),
            'FieldLevelEncryptionProfileConfig': {
                'Name': 'string',
                'CallerReference': 'string',
                'Comment': 'string',
                'EncryptionEntities': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'PublicKeyId': 'string',
                            'ProviderId': 'string',
                            'FieldPatterns': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                    ]
                }
            }
        },
        'ETag': 'string'
    }
    
    
    :returns: 
    CloudFront.Client.exceptions.AccessDenied
    CloudFront.Client.exceptions.NoSuchFieldLevelEncryptionProfile
    
    """
    pass

def get_field_level_encryption_profile_config(Id=None):
    """
    Get the field-level encryption profile configuration information.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_field_level_encryption_profile_config(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nGet the ID for the field-level encryption profile configuration information.\n

    :rtype: dict
ReturnsResponse Syntax{
    'FieldLevelEncryptionProfileConfig': {
        'Name': 'string',
        'CallerReference': 'string',
        'Comment': 'string',
        'EncryptionEntities': {
            'Quantity': 123,
            'Items': [
                {
                    'PublicKeyId': 'string',
                    'ProviderId': 'string',
                    'FieldPatterns': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    }
                },
            ]
        }
    },
    'ETag': 'string'
}


Response Structure

(dict) --
FieldLevelEncryptionProfileConfig (dict) --Return the field-level encryption profile configuration information.

Name (string) --Profile name for the field-level encryption profile.

CallerReference (string) --A unique number that ensures that the request can\'t be replayed.

Comment (string) --An optional comment for the field-level encryption profile.

EncryptionEntities (dict) --A complex data type of encryption entities for the field-level encryption profile that include the public key ID, provider, and field patterns for specifying which fields to encrypt with this key.

Quantity (integer) --Number of field pattern items in a field-level encryption content type-profile mapping.

Items (list) --An array of field patterns in a field-level encryption content type-profile mapping.

(dict) --Complex data type for field-level encryption profiles that includes the encryption key and field pattern specifications.

PublicKeyId (string) --The public key associated with a set of field-level encryption patterns, to be used when encrypting the fields that match the patterns.

ProviderId (string) --The provider associated with the public key being used for encryption. This value must also be provided with the private key for applications to be able to decrypt data.

FieldPatterns (dict) --Field patterns in a field-level encryption content type profile specify the fields that you want to be encrypted. You can provide the full field name, or any beginning characters followed by a wildcard (*). You can\'t overlap field patterns. For example, you can\'t have both ABC* and AB*. Note that field patterns are case-sensitive.

Quantity (integer) --The number of field-level encryption field patterns.

Items (list) --An array of the field-level encryption field patterns.

(string) --












ETag (string) --The current version of the field-level encryption profile configuration result. For example: E2QWRUHAPOMQZL .






Exceptions

CloudFront.Client.exceptions.AccessDenied
CloudFront.Client.exceptions.NoSuchFieldLevelEncryptionProfile


    :return: {
        'FieldLevelEncryptionProfileConfig': {
            'Name': 'string',
            'CallerReference': 'string',
            'Comment': 'string',
            'EncryptionEntities': {
                'Quantity': 123,
                'Items': [
                    {
                        'PublicKeyId': 'string',
                        'ProviderId': 'string',
                        'FieldPatterns': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                ]
            }
        },
        'ETag': 'string'
    }
    
    
    :returns: 
    CloudFront.Client.exceptions.AccessDenied
    CloudFront.Client.exceptions.NoSuchFieldLevelEncryptionProfile
    
    """
    pass

def get_invalidation(DistributionId=None, Id=None):
    """
    Get the information about an invalidation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_invalidation(
        DistributionId='string',
        Id='string'
    )
    
    
    :type DistributionId: string
    :param DistributionId: [REQUIRED]\nThe distribution\'s ID.\n

    :type Id: string
    :param Id: [REQUIRED]\nThe identifier for the invalidation request, for example, IDFDVBD632BHDS5 .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Invalidation': {
        'Id': 'string',
        'Status': 'string',
        'CreateTime': datetime(2015, 1, 1),
        'InvalidationBatch': {
            'Paths': {
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'CallerReference': 'string'
        }
    }
}


Response Structure

(dict) --
The returned result of the corresponding request.

Invalidation (dict) --
The invalidation\'s information. For more information, see Invalidation Complex Type .

Id (string) --
The identifier for the invalidation request. For example: IDFDVBD632BHDS5 .

Status (string) --
The status of the invalidation request. When the invalidation batch is finished, the status is Completed .

CreateTime (datetime) --
The date and time the invalidation request was first made.

InvalidationBatch (dict) --
The current invalidation information for the batch request.

Paths (dict) --
A complex type that contains information about the objects that you want to invalidate. For more information, see Specifying the Objects to Invalidate in the Amazon CloudFront Developer Guide .

Quantity (integer) --
The number of invalidation paths specified for the objects that you want to invalidate.

Items (list) --
A complex type that contains a list of the paths that you want to invalidate.

(string) --




CallerReference (string) --
A value that you specify to uniquely identify an invalidation request. CloudFront uses the value to prevent you from accidentally resubmitting an identical request. Whenever you create a new invalidation request, you must specify a new value for CallerReference and change other values in the request as applicable. One way to ensure that the value of CallerReference is unique is to use a timestamp , for example, 20120301090000 .
If you make a second invalidation request with the same value for CallerReference , and if the rest of the request is the same, CloudFront doesn\'t create a new invalidation request. Instead, CloudFront returns information about the invalidation request that you previously created with the same CallerReference .
If CallerReference is a value you already sent in a previous invalidation batch request but the content of any Path is different from the original request, CloudFront returns an InvalidationBatchAlreadyExists error.











Exceptions

CloudFront.Client.exceptions.NoSuchInvalidation
CloudFront.Client.exceptions.NoSuchDistribution
CloudFront.Client.exceptions.AccessDenied


    :return: {
        'Invalidation': {
            'Id': 'string',
            'Status': 'string',
            'CreateTime': datetime(2015, 1, 1),
            'InvalidationBatch': {
                'Paths': {
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'CallerReference': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    
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

def get_public_key(Id=None):
    """
    Get the public key information.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_public_key(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nRequest the ID for the public key.\n

    :rtype: dict
ReturnsResponse Syntax{
    'PublicKey': {
        'Id': 'string',
        'CreatedTime': datetime(2015, 1, 1),
        'PublicKeyConfig': {
            'CallerReference': 'string',
            'Name': 'string',
            'EncodedKey': 'string',
            'Comment': 'string'
        }
    },
    'ETag': 'string'
}


Response Structure

(dict) --
PublicKey (dict) --Return the public key.

Id (string) --A unique ID assigned to a public key you\'ve added to CloudFront.

CreatedTime (datetime) --A time you added a public key to CloudFront.

PublicKeyConfig (dict) --A complex data type for a public key you add to CloudFront to use with features like field-level encryption.

CallerReference (string) --A unique number that ensures that the request can\'t be replayed.

Name (string) --The name for a public key you add to CloudFront to use with features like field-level encryption.

EncodedKey (string) --The encoded public key that you want to add to CloudFront to use with features like field-level encryption.

Comment (string) --An optional comment about a public key.





ETag (string) --The current version of the public key. For example: E2QWRUHAPOMQZL .






Exceptions

CloudFront.Client.exceptions.AccessDenied
CloudFront.Client.exceptions.NoSuchPublicKey


    :return: {
        'PublicKey': {
            'Id': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'PublicKeyConfig': {
                'CallerReference': 'string',
                'Name': 'string',
                'EncodedKey': 'string',
                'Comment': 'string'
            }
        },
        'ETag': 'string'
    }
    
    
    """
    pass

def get_public_key_config(Id=None):
    """
    Return public key configuration informaation
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_public_key_config(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nRequest the ID for the public key configuration.\n

    :rtype: dict
ReturnsResponse Syntax{
    'PublicKeyConfig': {
        'CallerReference': 'string',
        'Name': 'string',
        'EncodedKey': 'string',
        'Comment': 'string'
    },
    'ETag': 'string'
}


Response Structure

(dict) --
PublicKeyConfig (dict) --Return the result for the public key configuration.

CallerReference (string) --A unique number that ensures that the request can\'t be replayed.

Name (string) --The name for a public key you add to CloudFront to use with features like field-level encryption.

EncodedKey (string) --The encoded public key that you want to add to CloudFront to use with features like field-level encryption.

Comment (string) --An optional comment about a public key.



ETag (string) --The current version of the public key configuration. For example: E2QWRUHAPOMQZL .






Exceptions

CloudFront.Client.exceptions.AccessDenied
CloudFront.Client.exceptions.NoSuchPublicKey


    :return: {
        'PublicKeyConfig': {
            'CallerReference': 'string',
            'Name': 'string',
            'EncodedKey': 'string',
            'Comment': 'string'
        },
        'ETag': 'string'
    }
    
    
    """
    pass

def get_streaming_distribution(Id=None):
    """
    Gets information about a specified RTMP distribution, including the distribution configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_streaming_distribution(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe streaming distribution\'s ID.\n

    :rtype: dict
ReturnsResponse Syntax{
    'StreamingDistribution': {
        'Id': 'string',
        'ARN': 'string',
        'Status': 'string',
        'LastModifiedTime': datetime(2015, 1, 1),
        'DomainName': 'string',
        'ActiveTrustedSigners': {
            'Enabled': True|False,
            'Quantity': 123,
            'Items': [
                {
                    'AwsAccountNumber': 'string',
                    'KeyPairIds': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    }
                },
            ]
        },
        'StreamingDistributionConfig': {
            'CallerReference': 'string',
            'S3Origin': {
                'DomainName': 'string',
                'OriginAccessIdentity': 'string'
            },
            'Aliases': {
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'Comment': 'string',
            'Logging': {
                'Enabled': True|False,
                'Bucket': 'string',
                'Prefix': 'string'
            },
            'TrustedSigners': {
                'Enabled': True|False,
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
            'Enabled': True|False
        }
    },
    'ETag': 'string'
}


Response Structure

(dict) --The returned result of the corresponding request.

StreamingDistribution (dict) --The streaming distribution\'s information.

Id (string) --The identifier for the RTMP distribution. For example: EGTXBD79EXAMPLE .

ARN (string) --The ARN (Amazon Resource Name) for the distribution. For example: arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5 , where 123456789012 is your AWS account ID.

Status (string) --The current status of the RTMP distribution. When the status is Deployed , the distribution\'s information is propagated to all CloudFront edge locations.

LastModifiedTime (datetime) --The date and time that the distribution was last modified.

DomainName (string) --The domain name that corresponds to the streaming distribution, for example, s5c39gqb8ow64r.cloudfront.net .

ActiveTrustedSigners (dict) --A complex type that lists the AWS accounts, if any, that you included in the TrustedSigners complex type for this distribution. These are the accounts that you want to allow to create signed URLs for private content.
The Signer complex type lists the AWS account number of the trusted signer or self if the signer is the AWS account that created the distribution. The Signer element also includes the IDs of any active CloudFront key pairs that are associated with the trusted signer\'s AWS account. If no KeyPairId element appears for a Signer , that signer can\'t create signed URLs.
For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .

Enabled (boolean) --Enabled is true if any of the AWS accounts listed in the TrustedSigners complex type for this distribution have active CloudFront key pairs. If not, Enabled is false .

Quantity (integer) --The number of trusted signers specified in the TrustedSigners complex type.

Items (list) --A complex type that contains one Signer complex type for each trusted signer that is specified in the TrustedSigners complex type.

(dict) --A complex type that lists the AWS accounts that were included in the TrustedSigners complex type, as well as their active CloudFront key pair IDs, if any.

AwsAccountNumber (string) --An AWS account that is included in the TrustedSigners complex type for this distribution. Valid values include:

self , which is the AWS account used to create the distribution.
An AWS account number.


KeyPairIds (dict) --A complex type that lists the active CloudFront key pairs, if any, that are associated with AwsAccountNumber .

Quantity (integer) --The number of active CloudFront key pairs for AwsAccountNumber .
For more information, see ActiveTrustedSigners .

Items (list) --A complex type that lists the active CloudFront key pairs, if any, that are associated with AwsAccountNumber .
For more information, see ActiveTrustedSigners .

(string) --










StreamingDistributionConfig (dict) --The current configuration information for the RTMP distribution.

CallerReference (string) --A unique value (for example, a date-time stamp) that ensures that the request can\'t be replayed.
If the value of CallerReference is new (regardless of the content of the StreamingDistributionConfig object), CloudFront creates a new distribution.
If CallerReference is a value that you already sent in a previous request to create a distribution, CloudFront returns a DistributionAlreadyExists error.

S3Origin (dict) --A complex type that contains information about the Amazon S3 bucket from which you want CloudFront to get your media files for distribution.

DomainName (string) --The DNS name of the Amazon S3 origin.

OriginAccessIdentity (string) --The CloudFront origin access identity to associate with the distribution. Use an origin access identity to configure the distribution so that end users can only access objects in an Amazon S3 bucket through CloudFront.
If you want end users to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty OriginAccessIdentity element.
To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty OriginAccessIdentity element.
To replace the origin access identity, update the distribution configuration and specify the new origin access identity.
For more information, see Using an Origin Access Identity to Restrict Access to Your Amazon S3 Content in the Amazon CloudFront Developer Guide .



Aliases (dict) --A complex type that contains information about CNAMEs (alternate domain names), if any, for this streaming distribution.

Quantity (integer) --The number of CNAME aliases, if any, that you want to associate with this distribution.

Items (list) --A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.

(string) --




Comment (string) --Any comments you want to include about the streaming distribution.

Logging (dict) --A complex type that controls whether access logs are written for the streaming distribution.

Enabled (boolean) --Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you don\'t want to enable logging when you create a streaming distribution or if you want to disable logging for an existing streaming distribution, specify false for Enabled , and specify empty Bucket and Prefix elements. If you specify false for Enabled but you specify values for Bucket and Prefix , the values are automatically deleted.

Bucket (string) --The Amazon S3 bucket to store the access logs in, for example, myawslogbucket.s3.amazonaws.com .

Prefix (string) --An optional string that you want CloudFront to prefix to the access log filenames for this streaming distribution, for example, myprefix/ . If you want to enable logging, but you don\'t want to specify a prefix, you still must include an empty Prefix element in the Logging element.



TrustedSigners (dict) --A complex type that specifies any AWS accounts that you want to permit to create signed URLs for private content. If you want the distribution to use signed URLs, include this element; if you want the distribution to use public URLs, remove this element. For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .

Enabled (boolean) --Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .

Quantity (integer) --The number of trusted signers for this cache behavior.

Items (list) --
Optional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .

(string) --




PriceClass (string) --A complex type that contains information about price class for this streaming distribution.

Enabled (boolean) --Whether the streaming distribution is enabled to accept user requests for content.





ETag (string) --The current version of the streaming distribution\'s information. For example: E2QWRUHAPOMQZL .






Exceptions

CloudFront.Client.exceptions.NoSuchStreamingDistribution
CloudFront.Client.exceptions.AccessDenied


    :return: {
        'StreamingDistribution': {
            'Id': 'string',
            'ARN': 'string',
            'Status': 'string',
            'LastModifiedTime': datetime(2015, 1, 1),
            'DomainName': 'string',
            'ActiveTrustedSigners': {
                'Enabled': True|False,
                'Quantity': 123,
                'Items': [
                    {
                        'AwsAccountNumber': 'string',
                        'KeyPairIds': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                ]
            },
            'StreamingDistributionConfig': {
                'CallerReference': 'string',
                'S3Origin': {
                    'DomainName': 'string',
                    'OriginAccessIdentity': 'string'
                },
                'Aliases': {
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'Comment': 'string',
                'Logging': {
                    'Enabled': True|False,
                    'Bucket': 'string',
                    'Prefix': 'string'
                },
                'TrustedSigners': {
                    'Enabled': True|False,
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
                'Enabled': True|False
            }
        },
        'ETag': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_streaming_distribution_config(Id=None):
    """
    Get the configuration information about a streaming distribution.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_streaming_distribution_config(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe streaming distribution\'s ID.\n

    :rtype: dict
ReturnsResponse Syntax{
    'StreamingDistributionConfig': {
        'CallerReference': 'string',
        'S3Origin': {
            'DomainName': 'string',
            'OriginAccessIdentity': 'string'
        },
        'Aliases': {
            'Quantity': 123,
            'Items': [
                'string',
            ]
        },
        'Comment': 'string',
        'Logging': {
            'Enabled': True|False,
            'Bucket': 'string',
            'Prefix': 'string'
        },
        'TrustedSigners': {
            'Enabled': True|False,
            'Quantity': 123,
            'Items': [
                'string',
            ]
        },
        'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
        'Enabled': True|False
    },
    'ETag': 'string'
}


Response Structure

(dict) --The returned result of the corresponding request.

StreamingDistributionConfig (dict) --The streaming distribution\'s configuration information.

CallerReference (string) --A unique value (for example, a date-time stamp) that ensures that the request can\'t be replayed.
If the value of CallerReference is new (regardless of the content of the StreamingDistributionConfig object), CloudFront creates a new distribution.
If CallerReference is a value that you already sent in a previous request to create a distribution, CloudFront returns a DistributionAlreadyExists error.

S3Origin (dict) --A complex type that contains information about the Amazon S3 bucket from which you want CloudFront to get your media files for distribution.

DomainName (string) --The DNS name of the Amazon S3 origin.

OriginAccessIdentity (string) --The CloudFront origin access identity to associate with the distribution. Use an origin access identity to configure the distribution so that end users can only access objects in an Amazon S3 bucket through CloudFront.
If you want end users to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty OriginAccessIdentity element.
To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty OriginAccessIdentity element.
To replace the origin access identity, update the distribution configuration and specify the new origin access identity.
For more information, see Using an Origin Access Identity to Restrict Access to Your Amazon S3 Content in the Amazon CloudFront Developer Guide .



Aliases (dict) --A complex type that contains information about CNAMEs (alternate domain names), if any, for this streaming distribution.

Quantity (integer) --The number of CNAME aliases, if any, that you want to associate with this distribution.

Items (list) --A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.

(string) --




Comment (string) --Any comments you want to include about the streaming distribution.

Logging (dict) --A complex type that controls whether access logs are written for the streaming distribution.

Enabled (boolean) --Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you don\'t want to enable logging when you create a streaming distribution or if you want to disable logging for an existing streaming distribution, specify false for Enabled , and specify empty Bucket and Prefix elements. If you specify false for Enabled but you specify values for Bucket and Prefix , the values are automatically deleted.

Bucket (string) --The Amazon S3 bucket to store the access logs in, for example, myawslogbucket.s3.amazonaws.com .

Prefix (string) --An optional string that you want CloudFront to prefix to the access log filenames for this streaming distribution, for example, myprefix/ . If you want to enable logging, but you don\'t want to specify a prefix, you still must include an empty Prefix element in the Logging element.



TrustedSigners (dict) --A complex type that specifies any AWS accounts that you want to permit to create signed URLs for private content. If you want the distribution to use signed URLs, include this element; if you want the distribution to use public URLs, remove this element. For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .

Enabled (boolean) --Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .

Quantity (integer) --The number of trusted signers for this cache behavior.

Items (list) --
Optional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .

(string) --




PriceClass (string) --A complex type that contains information about price class for this streaming distribution.

Enabled (boolean) --Whether the streaming distribution is enabled to accept user requests for content.



ETag (string) --The current version of the configuration. For example: E2QWRUHAPOMQZL .






Exceptions

CloudFront.Client.exceptions.NoSuchStreamingDistribution
CloudFront.Client.exceptions.AccessDenied


    :return: {
        'StreamingDistributionConfig': {
            'CallerReference': 'string',
            'S3Origin': {
                'DomainName': 'string',
                'OriginAccessIdentity': 'string'
            },
            'Aliases': {
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'Comment': 'string',
            'Logging': {
                'Enabled': True|False,
                'Bucket': 'string',
                'Prefix': 'string'
            },
            'TrustedSigners': {
                'Enabled': True|False,
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
            'Enabled': True|False
        },
        'ETag': 'string'
    }
    
    
    :returns: 
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

def list_cloud_front_origin_access_identities(Marker=None, MaxItems=None):
    """
    Lists origin access identities.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_cloud_front_origin_access_identities(
        Marker='string',
        MaxItems='string'
    )
    
    
    :type Marker: string
    :param Marker: Use this when paginating results to indicate where to begin in your list of origin access identities. The results include identities in the list that occur after the marker. To get the next page of results, set the Marker to the value of the NextMarker from the current page\'s response (which is also the ID of the last identity on that page).

    :type MaxItems: string
    :param MaxItems: The maximum number of origin access identities you want in the response body.

    :rtype: dict

ReturnsResponse Syntax
{
    'CloudFrontOriginAccessIdentityList': {
        'Marker': 'string',
        'NextMarker': 'string',
        'MaxItems': 123,
        'IsTruncated': True|False,
        'Quantity': 123,
        'Items': [
            {
                'Id': 'string',
                'S3CanonicalUserId': 'string',
                'Comment': 'string'
            },
        ]
    }
}


Response Structure

(dict) --
The returned result of the corresponding request.

CloudFrontOriginAccessIdentityList (dict) --
The CloudFrontOriginAccessIdentityList type.

Marker (string) --
Use this when paginating results to indicate where to begin in your list of origin access identities. The results include identities in the list that occur after the marker. To get the next page of results, set the Marker to the value of the NextMarker from the current page\'s response (which is also the ID of the last identity on that page).

NextMarker (string) --
If IsTruncated is true , this element is present and contains the value you can use for the Marker request parameter to continue listing your origin access identities where they left off.

MaxItems (integer) --
The maximum number of origin access identities you want in the response body.

IsTruncated (boolean) --
A flag that indicates whether more origin access identities remain to be listed. If your results were truncated, you can make a follow-up pagination request using the Marker request parameter to retrieve more items in the list.

Quantity (integer) --
The number of CloudFront origin access identities that were created by the current AWS account.

Items (list) --
A complex type that contains one CloudFrontOriginAccessIdentitySummary element for each origin access identity that was created by the current AWS account.

(dict) --
Summary of the information about a CloudFront origin access identity.

Id (string) --
The ID for the origin access identity. For example: E74FTE3AJFJ256A .

S3CanonicalUserId (string) --
The Amazon S3 canonical user ID for the origin access identity, which you use when giving the origin access identity read permission to an object in Amazon S3.

Comment (string) --
The comment for this origin access identity, as originally specified when created.













Exceptions

CloudFront.Client.exceptions.InvalidArgument


    :return: {
        'CloudFrontOriginAccessIdentityList': {
            'Marker': 'string',
            'NextMarker': 'string',
            'MaxItems': 123,
            'IsTruncated': True|False,
            'Quantity': 123,
            'Items': [
                {
                    'Id': 'string',
                    'S3CanonicalUserId': 'string',
                    'Comment': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    CloudFront.Client.exceptions.InvalidArgument
    
    """
    pass

def list_distributions(Marker=None, MaxItems=None):
    """
    List CloudFront distributions.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_distributions(
        Marker='string',
        MaxItems='string'
    )
    
    
    :type Marker: string
    :param Marker: Use this when paginating results to indicate where to begin in your list of distributions. The results include distributions in the list that occur after the marker. To get the next page of results, set the Marker to the value of the NextMarker from the current page\'s response (which is also the ID of the last distribution on that page).

    :type MaxItems: string
    :param MaxItems: The maximum number of distributions you want in the response body.

    :rtype: dict

ReturnsResponse Syntax
{
    'DistributionList': {
        'Marker': 'string',
        'NextMarker': 'string',
        'MaxItems': 123,
        'IsTruncated': True|False,
        'Quantity': 123,
        'Items': [
            {
                'Id': 'string',
                'ARN': 'string',
                'Status': 'string',
                'LastModifiedTime': datetime(2015, 1, 1),
                'DomainName': 'string',
                'Aliases': {
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'Origins': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'Id': 'string',
                            'DomainName': 'string',
                            'OriginPath': 'string',
                            'CustomHeaders': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'HeaderName': 'string',
                                        'HeaderValue': 'string'
                                    },
                                ]
                            },
                            'S3OriginConfig': {
                                'OriginAccessIdentity': 'string'
                            },
                            'CustomOriginConfig': {
                                'HTTPPort': 123,
                                'HTTPSPort': 123,
                                'OriginProtocolPolicy': 'http-only'|'match-viewer'|'https-only',
                                'OriginSslProtocols': {
                                    'Quantity': 123,
                                    'Items': [
                                        'SSLv3'|'TLSv1'|'TLSv1.1'|'TLSv1.2',
                                    ]
                                },
                                'OriginReadTimeout': 123,
                                'OriginKeepaliveTimeout': 123
                            }
                        },
                    ]
                },
                'OriginGroups': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'Id': 'string',
                            'FailoverCriteria': {
                                'StatusCodes': {
                                    'Quantity': 123,
                                    'Items': [
                                        123,
                                    ]
                                }
                            },
                            'Members': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'OriginId': 'string'
                                    },
                                ]
                            }
                        },
                    ]
                },
                'DefaultCacheBehavior': {
                    'TargetOriginId': 'string',
                    'ForwardedValues': {
                        'QueryString': True|False,
                        'Cookies': {
                            'Forward': 'none'|'whitelist'|'all',
                            'WhitelistedNames': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                        'Headers': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        },
                        'QueryStringCacheKeys': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                    'TrustedSigners': {
                        'Enabled': True|False,
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    },
                    'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                    'MinTTL': 123,
                    'AllowedMethods': {
                        'Quantity': 123,
                        'Items': [
                            'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                        ],
                        'CachedMethods': {
                            'Quantity': 123,
                            'Items': [
                                'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                            ]
                        }
                    },
                    'SmoothStreaming': True|False,
                    'DefaultTTL': 123,
                    'MaxTTL': 123,
                    'Compress': True|False,
                    'LambdaFunctionAssociations': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'LambdaFunctionARN': 'string',
                                'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                'IncludeBody': True|False
                            },
                        ]
                    },
                    'FieldLevelEncryptionId': 'string'
                },
                'CacheBehaviors': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'PathPattern': 'string',
                            'TargetOriginId': 'string',
                            'ForwardedValues': {
                                'QueryString': True|False,
                                'Cookies': {
                                    'Forward': 'none'|'whitelist'|'all',
                                    'WhitelistedNames': {
                                        'Quantity': 123,
                                        'Items': [
                                            'string',
                                        ]
                                    }
                                },
                                'Headers': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                },
                                'QueryStringCacheKeys': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                }
                            },
                            'TrustedSigners': {
                                'Enabled': True|False,
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            },
                            'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                            'MinTTL': 123,
                            'AllowedMethods': {
                                'Quantity': 123,
                                'Items': [
                                    'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                ],
                                'CachedMethods': {
                                    'Quantity': 123,
                                    'Items': [
                                        'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                    ]
                                }
                            },
                            'SmoothStreaming': True|False,
                            'DefaultTTL': 123,
                            'MaxTTL': 123,
                            'Compress': True|False,
                            'LambdaFunctionAssociations': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'LambdaFunctionARN': 'string',
                                        'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                        'IncludeBody': True|False
                                    },
                                ]
                            },
                            'FieldLevelEncryptionId': 'string'
                        },
                    ]
                },
                'CustomErrorResponses': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'ErrorCode': 123,
                            'ResponsePagePath': 'string',
                            'ResponseCode': 'string',
                            'ErrorCachingMinTTL': 123
                        },
                    ]
                },
                'Comment': 'string',
                'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
                'Enabled': True|False,
                'ViewerCertificate': {
                    'CloudFrontDefaultCertificate': True|False,
                    'IAMCertificateId': 'string',
                    'ACMCertificateArn': 'string',
                    'SSLSupportMethod': 'sni-only'|'vip',
                    'MinimumProtocolVersion': 'SSLv3'|'TLSv1'|'TLSv1_2016'|'TLSv1.1_2016'|'TLSv1.2_2018',
                    'Certificate': 'string',
                    'CertificateSource': 'cloudfront'|'iam'|'acm'
                },
                'Restrictions': {
                    'GeoRestriction': {
                        'RestrictionType': 'blacklist'|'whitelist'|'none',
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    }
                },
                'WebACLId': 'string',
                'HttpVersion': 'http1.1'|'http2',
                'IsIPV6Enabled': True|False,
                'AliasICPRecordals': [
                    {
                        'CNAME': 'string',
                        'ICPRecordalStatus': 'APPROVED'|'SUSPENDED'|'PENDING'
                    },
                ]
            },
        ]
    }
}


Response Structure

(dict) --
The returned result of the corresponding request.

DistributionList (dict) --
The DistributionList type.

Marker (string) --
The value you provided for the Marker request parameter.

NextMarker (string) --
If IsTruncated is true , this element is present and contains the value you can use for the Marker request parameter to continue listing your distributions where they left off.

MaxItems (integer) --
The value you provided for the MaxItems request parameter.

IsTruncated (boolean) --
A flag that indicates whether more distributions remain to be listed. If your results were truncated, you can make a follow-up pagination request using the Marker request parameter to retrieve more distributions in the list.

Quantity (integer) --
The number of distributions that were created by the current AWS account.

Items (list) --
A complex type that contains one DistributionSummary element for each distribution that was created by the current AWS account.

(dict) --
A summary of the information about a CloudFront distribution.

Id (string) --
The identifier for the distribution. For example: EDFDVBD632BHDS5 .

ARN (string) --
The ARN (Amazon Resource Name) for the distribution. For example: arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5 , where 123456789012 is your AWS account ID.

Status (string) --
The current status of the distribution. When the status is Deployed , the distribution\'s information is propagated to all CloudFront edge locations.

LastModifiedTime (datetime) --
The date and time the distribution was last modified.

DomainName (string) --
The domain name that corresponds to the distribution, for example, d111111abcdef8.cloudfront.net .

Aliases (dict) --
A complex type that contains information about CNAMEs (alternate domain names), if any, for this distribution.

Quantity (integer) --
The number of CNAME aliases, if any, that you want to associate with this distribution.

Items (list) --
A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.

(string) --




Origins (dict) --
A complex type that contains information about origins for this distribution.

Quantity (integer) --
The number of origins or origin groups for this distribution.

Items (list) --
A complex type that contains origins or origin groups for this distribution.

(dict) --
A complex type that describes the Amazon S3 bucket, HTTP server (for example, a web server), Amazon MediaStore, or other server from which CloudFront gets your files. This can also be an origin group, if you\'ve created an origin group. You must specify at least one origin or origin group.
For the current limit on the number of origins or origin groups that you can specify for a distribution, see Amazon CloudFront Limits in the AWS General Reference .

Id (string) --
A unique identifier for the origin or origin group. The value of Id must be unique within the distribution.
When you specify the value of TargetOriginId for the default cache behavior or for another cache behavior, you indicate the origin to which you want the cache behavior to route requests by specifying the value of the Id element for that origin. When a request matches the path pattern for that cache behavior, CloudFront routes the request to the specified origin. For more information, see Cache Behavior Settings in the Amazon CloudFront Developer Guide .

DomainName (string) --

Amazon S3 origins : The DNS name of the Amazon S3 bucket from which you want CloudFront to get objects for this origin, for example, myawsbucket.s3.amazonaws.com . If you set up your bucket to be configured as a website endpoint, enter the Amazon S3 static website hosting endpoint for the bucket.

For more information about specifying this value for different types of origins, see Origin Domain Name in the Amazon CloudFront Developer Guide .
Constraints for Amazon S3 origins:

If you configured Amazon S3 Transfer Acceleration for your bucket, don\'t specify the s3-accelerate endpoint for DomainName .
The bucket name must be between 3 and 63 characters long (inclusive).
The bucket name must contain only lowercase characters, numbers, periods, underscores, and dashes.
The bucket name must not contain adjacent periods.


Custom Origins : The DNS domain name for the HTTP server from which you want CloudFront to get objects for this origin, for example, www.example.com .

Constraints for custom origins:

DomainName must be a valid DNS name that contains only a-z, A-Z, 0-9, dot (.), hyphen (-), or underscore (_) characters.
The name cannot exceed 128 characters.


OriginPath (string) --
An optional element that causes CloudFront to request your content from a directory in your Amazon S3 bucket or your custom origin. When you include the OriginPath element, specify the directory name, beginning with a / . CloudFront appends the directory name to the value of DomainName , for example, example.com/production . Do not include a / at the end of the directory name.
For example, suppose you\'ve specified the following values for your distribution:

DomainName : An Amazon S3 bucket named myawsbucket .
OriginPath : /production
CNAME : example.com

When a user enters example.com/index.html in a browser, CloudFront sends a request to Amazon S3 for myawsbucket/production/index.html .
When a user enters example.com/acme/index.html in a browser, CloudFront sends a request to Amazon S3 for myawsbucket/production/acme/index.html .

CustomHeaders (dict) --
A complex type that contains names and values for the custom headers that you want.

Quantity (integer) --
The number of custom headers, if any, for this distribution.

Items (list) --

Optional : A list that contains one OriginCustomHeader element for each custom header that you want CloudFront to forward to the origin. If Quantity is 0 , omit Items .


(dict) --
A complex type that contains HeaderName and HeaderValue elements, if any, for this distribution.

HeaderName (string) --
The name of a header that you want CloudFront to forward to your origin. For more information, see Forwarding Custom Headers to Your Origin (Web Distributions Only) in the Amazon CloudFront Developer Guide .

HeaderValue (string) --
The value for the header that you specified in the HeaderName field.







S3OriginConfig (dict) --
A complex type that contains information about the Amazon S3 origin. If the origin is a custom origin, use the CustomOriginConfig element instead.

OriginAccessIdentity (string) --
The CloudFront origin access identity to associate with the origin. Use an origin access identity to configure the origin so that viewers can only access objects in an Amazon S3 bucket through CloudFront. The format of the value is:
origin-access-identity/cloudfront/ID-of-origin-access-identity
where `` ID-of-origin-access-identity `` is the value that CloudFront returned in the ID element when you created the origin access identity.
If you want viewers to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty OriginAccessIdentity element.
To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty OriginAccessIdentity element.
To replace the origin access identity, update the distribution configuration and specify the new origin access identity.
For more information about the origin access identity, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .



CustomOriginConfig (dict) --
A complex type that contains information about a custom origin. If the origin is an Amazon S3 bucket, use the S3OriginConfig element instead.

HTTPPort (integer) --
The HTTP port the custom origin listens on.

HTTPSPort (integer) --
The HTTPS port the custom origin listens on.

OriginProtocolPolicy (string) --
The origin protocol policy to apply to your origin.

OriginSslProtocols (dict) --
The SSL/TLS protocols that you want CloudFront to use when communicating with your origin over HTTPS.

Quantity (integer) --
The number of SSL/TLS protocols that you want to allow CloudFront to use when establishing an HTTPS connection with this origin.

Items (list) --
A list that contains allowed SSL/TLS protocols for this distribution.

(string) --




OriginReadTimeout (integer) --
You can create a custom origin read timeout. All timeout units are in seconds. The default origin read timeout is 30 seconds, but you can configure custom timeout lengths using the CloudFront API. The minimum timeout length is 4 seconds; the maximum is 60 seconds.
If you need to increase the maximum time limit, contact the AWS Support Center .

OriginKeepaliveTimeout (integer) --
You can create a custom keep-alive timeout. All timeout units are in seconds. The default keep-alive timeout is 5 seconds, but you can configure custom timeout lengths using the CloudFront API. The minimum timeout length is 1 second; the maximum is 60 seconds.
If you need to increase the maximum time limit, contact the AWS Support Center .









OriginGroups (dict) --
A complex type that contains information about origin groups for this distribution.

Quantity (integer) --
The number of origin groups.

Items (list) --
The items (origin groups) in a distribution.

(dict) --
An origin group includes two origins (a primary origin and a second origin to failover to) and a failover criteria that you specify. You create an origin group to support origin failover in CloudFront. When you create or update a distribution, you can specifiy the origin group instead of a single origin, and CloudFront will failover from the primary origin to the second origin under the failover conditions that you\'ve chosen.

Id (string) --
The origin group\'s ID.

FailoverCriteria (dict) --
A complex type that contains information about the failover criteria for an origin group.

StatusCodes (dict) --
The status codes that, when returned from the primary origin, will trigger CloudFront to failover to the second origin.

Quantity (integer) --
The number of status codes.

Items (list) --
The items (status codes) for an origin group.

(integer) --






Members (dict) --
A complex type that contains information about the origins in an origin group.

Quantity (integer) --
The number of origins in an origin group.

Items (list) --
Items (origins) in an origin group.

(dict) --
An origin in an origin group.

OriginId (string) --
The ID for an origin in an origin group.













DefaultCacheBehavior (dict) --
A complex type that describes the default cache behavior if you don\'t specify a CacheBehavior element or if files don\'t match any of the values of PathPattern in CacheBehavior elements. You must create exactly one default cache behavior.

TargetOriginId (string) --
The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior in your distribution.

ForwardedValues (dict) --
A complex type that specifies how CloudFront handles query strings, cookies, and HTTP headers.

QueryString (boolean) --
Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior and cache based on the query string parameters. CloudFront behavior depends on the value of QueryString and on the values that you specify for QueryStringCacheKeys , if any:
If you specify true for QueryString and you don\'t specify any values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin and caches based on all query string parameters. Depending on how many query string parameters and values you have, this can adversely affect performance because CloudFront must forward more requests to the origin.
If you specify true for QueryString and you specify one or more values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin, but it only caches based on the query string parameters that you specify.
If you specify false for QueryString , CloudFront doesn\'t forward any query string parameters to the origin, and doesn\'t cache based on query string parameters.
For more information, see Configuring CloudFront to Cache Based on Query String Parameters in the Amazon CloudFront Developer Guide .

Cookies (dict) --
A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see How CloudFront Forwards, Caches, and Logs Cookies in the Amazon CloudFront Developer Guide .

Forward (string) --
Specifies which cookies to forward to the origin for this cache behavior: all, none, or the list of cookies specified in the WhitelistedNames complex type.
Amazon S3 doesn\'t process cookies. When the cache behavior is forwarding requests to an Amazon S3 origin, specify none for the Forward element.

WhitelistedNames (dict) --
Required if you specify whitelist for the value of Forward . A complex type that specifies how many different cookies you want CloudFront to forward to the origin for this cache behavior and, if you want to forward selected cookies, the names of those cookies.
If you specify all or none for the value of Forward , omit WhitelistedNames . If you change the value of Forward from whitelist to all or none and you don\'t delete the WhitelistedNames element and its child elements, CloudFront deletes them automatically.
For the current limit on the number of cookie names that you can whitelist for each cache behavior, see CloudFront Limits in the AWS General Reference .

Quantity (integer) --
The number of different cookies that you want CloudFront to forward to the origin for this cache behavior. The value must equal the number of items that are in the Items field.
When you set Forward = whitelist (in the CookiePreferences object), this value must be 1 or higher.

Items (list) --
A complex type that contains one Name element for each cookie that you want CloudFront to forward to the origin for this cache behavior. It must contain the same number of items that is specified in the Quantity field.
When you set Forward = whitelist (in the CookiePreferences object), this field must contain at least one item.

(string) --






Headers (dict) --
A complex type that specifies the Headers , if any, that you want CloudFront to forward to the origin for this cache behavior (whitelisted headers). For the headers that you specify, CloudFront also caches separate versions of a specified object that is based on the header values in viewer requests.
For more information, see Caching Content Based on Request Headers in the Amazon CloudFront Developer Guide .

Quantity (integer) --
The number of different headers that you want CloudFront to base caching on for this cache behavior. You can configure each cache behavior in a web distribution to do one of the following:

Forward all headers to your origin : Specify 1 for Quantity and * for Name .


Warning
CloudFront doesn\'t cache the objects that are associated with this cache behavior. Instead, CloudFront sends every request to the origin.


Forward a whitelist of headers you specify : Specify the number of headers that you want CloudFront to base caching on. Then specify the header names in Name elements. CloudFront caches your objects based on the values in the specified headers.
Forward only the default headers : Specify 0 for Quantity and omit Items . In this configuration, CloudFront doesn\'t cache based on the values in the request headers.

Regardless of which option you choose, CloudFront forwards headers to your origin based on whether the origin is an S3 bucket or a custom origin. See the following documentation:

S3 bucket : See HTTP Request Headers That CloudFront Removes or Updates
Custom origin : See HTTP Request Headers and CloudFront Behavior


Items (list) --
A list that contains one Name element for each header that you want CloudFront to use for caching in this cache behavior. If Quantity is 0 , omit Items .

(string) --




QueryStringCacheKeys (dict) --
A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.

Quantity (integer) --
The number of whitelisted query string parameters for a cache behavior.

Items (list) --
A list that contains the query string parameters that you want CloudFront to use as a basis for caching for a cache behavior. If Quantity is 0, you can omit Items .

(string) --






TrustedSigners (dict) --
A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content.
If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled , and specify the applicable values for Quantity and Items . For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .
If you don\'t want to require signed URLs in requests for objects that match PathPattern , specify false for Enabled and 0 for Quantity . Omit Items .
To add, change, or remove one or more trusted signers, change Enabled to true (if it\'s currently false ), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.

Enabled (boolean) --
Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .

Quantity (integer) --
The number of trusted signers for this cache behavior.

Items (list) --

Optional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .


(string) --




ViewerProtocolPolicy (string) --
The protocol that viewers can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern . You can specify the following options:

allow-all : Viewers can use HTTP or HTTPS.
redirect-to-https : If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.
https-only : If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).

For more information about requiring the HTTPS protocol, see Using an HTTPS Connection to Access Your Objects in the Amazon CloudFront Developer Guide .

Note
The only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects\' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .


MinTTL (integer) --
The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .
You must specify 0 for MinTTL if you configure CloudFront to forward all headers to your origin (under Headers , if you specify 1 for Quantity and * for Name ).

AllowedMethods (dict) --
A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices:

CloudFront forwards only GET and HEAD requests.
CloudFront forwards only GET , HEAD , and OPTIONS requests.
CloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests.

If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can\'t perform operations that you don\'t want them to. For example, you might not want users to have permissions to delete objects from your origin.

Quantity (integer) --
The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET , HEAD , and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests).

Items (list) --
A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.

(string) --


CachedMethods (dict) --
A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices:

CloudFront caches responses to GET and HEAD requests.
CloudFront caches responses to GET , HEAD , and OPTIONS requests.

If you pick the second choice for your Amazon S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers, and Origin headers for the responses to be cached correctly.

Quantity (integer) --
The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET , HEAD , and OPTIONS requests).

Items (list) --
A complex type that contains the HTTP methods that you want CloudFront to cache responses to.

(string) --






SmoothStreaming (boolean) --
Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true ; if not, specify false . If you specify true for SmoothStreaming , you can still distribute other content using this cache behavior if the content matches the value of PathPattern .

DefaultTTL (integer) --
The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .

MaxTTL (integer) --
The maximum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .

Compress (boolean) --
Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify true ; if not, specify false . For more information, see Serving Compressed Files in the Amazon CloudFront Developer Guide .

LambdaFunctionAssociations (dict) --
A complex type that contains zero or more Lambda function associations for a cache behavior.

Quantity (integer) --
The number of Lambda function associations for this cache behavior.

Items (list) --

Optional : A complex type that contains LambdaFunctionAssociation items for this cache behavior. If Quantity is 0 , you can omit Items .


(dict) --
A complex type that contains a Lambda function association.

LambdaFunctionARN (string) --
The ARN of the Lambda function. You must specify the ARN of a function version; you can\'t specify a Lambda alias or $LATEST.

EventType (string) --
Specifies the event type that triggers a Lambda function invocation. You can specify the following values:

viewer-request : The function executes when CloudFront receives a request from a viewer and before it checks to see whether the requested object is in the edge cache.
origin-request : The function executes only when CloudFront forwards a request to your origin. When the requested object is in the edge cache, the function doesn\'t execute.
origin-response : The function executes after CloudFront receives a response from the origin and before it caches the object in the response. When the requested object is in the edge cache, the function doesn\'t execute.
viewer-response : The function executes before CloudFront returns the requested object to the viewer. The function executes regardless of whether the object was already in the edge cache. If the origin returns an HTTP status code other than HTTP 200 (OK), the function doesn\'t execute.


IncludeBody (boolean) --
A flag that allows a Lambda function to have read access to the body content. For more information, see Accessing the Request Body by Choosing the Include Body Option in the Amazon CloudFront Developer Guide.







FieldLevelEncryptionId (string) --
The value of ID for the field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data for a cache behavior or for the default cache behavior in your distribution.



CacheBehaviors (dict) --
A complex type that contains zero or more CacheBehavior elements.

Quantity (integer) --
The number of cache behaviors for this distribution.

Items (list) --
Optional: A complex type that contains cache behaviors for this distribution. If Quantity is 0 , you can omit Items .

(dict) --
A complex type that describes how CloudFront processes requests.
You must create at least as many cache behaviors (including the default cache behavior) as you have origins if you want CloudFront to distribute objects from all of the origins. Each cache behavior specifies the one origin from which you want CloudFront to get objects. If you have two origins and only the default cache behavior, the default cache behavior will cause CloudFront to get objects from one of the origins, but the other origin is never used.
For the current limit on the number of cache behaviors that you can add to a distribution, see Amazon CloudFront Limits in the AWS General Reference .
If you don\'t want to specify any cache behaviors, include only an empty CacheBehaviors element. Don\'t include an empty CacheBehavior element, or CloudFront returns a MalformedXML error.
To delete all cache behaviors in an existing distribution, update the distribution configuration and include only an empty CacheBehaviors element.
To add, change, or remove one or more cache behaviors, update the distribution configuration and specify all of the cache behaviors that you want to include in the updated distribution.
For more information about cache behaviors, see Cache Behaviors in the Amazon CloudFront Developer Guide .

PathPattern (string) --
The pattern (for example, images/*.jpg ) that specifies which requests to apply the behavior to. When CloudFront receives a viewer request, the requested path is compared with path patterns in the order in which cache behaviors are listed in the distribution.

Note
You can optionally include a slash (/ ) at the beginning of the path pattern. For example, /images/*.jpg . CloudFront behavior is the same with or without the leading / .

The path pattern for the default cache behavior is * and cannot be changed. If the request for an object does not match the path pattern for any cache behaviors, CloudFront applies the behavior in the default cache behavior.
For more information, see Path Pattern in the Amazon CloudFront Developer Guide .

TargetOriginId (string) --
The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior in your distribution.

ForwardedValues (dict) --
A complex type that specifies how CloudFront handles query strings, cookies, and HTTP headers.

QueryString (boolean) --
Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior and cache based on the query string parameters. CloudFront behavior depends on the value of QueryString and on the values that you specify for QueryStringCacheKeys , if any:
If you specify true for QueryString and you don\'t specify any values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin and caches based on all query string parameters. Depending on how many query string parameters and values you have, this can adversely affect performance because CloudFront must forward more requests to the origin.
If you specify true for QueryString and you specify one or more values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin, but it only caches based on the query string parameters that you specify.
If you specify false for QueryString , CloudFront doesn\'t forward any query string parameters to the origin, and doesn\'t cache based on query string parameters.
For more information, see Configuring CloudFront to Cache Based on Query String Parameters in the Amazon CloudFront Developer Guide .

Cookies (dict) --
A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see How CloudFront Forwards, Caches, and Logs Cookies in the Amazon CloudFront Developer Guide .

Forward (string) --
Specifies which cookies to forward to the origin for this cache behavior: all, none, or the list of cookies specified in the WhitelistedNames complex type.
Amazon S3 doesn\'t process cookies. When the cache behavior is forwarding requests to an Amazon S3 origin, specify none for the Forward element.

WhitelistedNames (dict) --
Required if you specify whitelist for the value of Forward . A complex type that specifies how many different cookies you want CloudFront to forward to the origin for this cache behavior and, if you want to forward selected cookies, the names of those cookies.
If you specify all or none for the value of Forward , omit WhitelistedNames . If you change the value of Forward from whitelist to all or none and you don\'t delete the WhitelistedNames element and its child elements, CloudFront deletes them automatically.
For the current limit on the number of cookie names that you can whitelist for each cache behavior, see CloudFront Limits in the AWS General Reference .

Quantity (integer) --
The number of different cookies that you want CloudFront to forward to the origin for this cache behavior. The value must equal the number of items that are in the Items field.
When you set Forward = whitelist (in the CookiePreferences object), this value must be 1 or higher.

Items (list) --
A complex type that contains one Name element for each cookie that you want CloudFront to forward to the origin for this cache behavior. It must contain the same number of items that is specified in the Quantity field.
When you set Forward = whitelist (in the CookiePreferences object), this field must contain at least one item.

(string) --






Headers (dict) --
A complex type that specifies the Headers , if any, that you want CloudFront to forward to the origin for this cache behavior (whitelisted headers). For the headers that you specify, CloudFront also caches separate versions of a specified object that is based on the header values in viewer requests.
For more information, see Caching Content Based on Request Headers in the Amazon CloudFront Developer Guide .

Quantity (integer) --
The number of different headers that you want CloudFront to base caching on for this cache behavior. You can configure each cache behavior in a web distribution to do one of the following:

Forward all headers to your origin : Specify 1 for Quantity and * for Name .


Warning
CloudFront doesn\'t cache the objects that are associated with this cache behavior. Instead, CloudFront sends every request to the origin.


Forward a whitelist of headers you specify : Specify the number of headers that you want CloudFront to base caching on. Then specify the header names in Name elements. CloudFront caches your objects based on the values in the specified headers.
Forward only the default headers : Specify 0 for Quantity and omit Items . In this configuration, CloudFront doesn\'t cache based on the values in the request headers.

Regardless of which option you choose, CloudFront forwards headers to your origin based on whether the origin is an S3 bucket or a custom origin. See the following documentation:

S3 bucket : See HTTP Request Headers That CloudFront Removes or Updates
Custom origin : See HTTP Request Headers and CloudFront Behavior


Items (list) --
A list that contains one Name element for each header that you want CloudFront to use for caching in this cache behavior. If Quantity is 0 , omit Items .

(string) --




QueryStringCacheKeys (dict) --
A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.

Quantity (integer) --
The number of whitelisted query string parameters for a cache behavior.

Items (list) --
A list that contains the query string parameters that you want CloudFront to use as a basis for caching for a cache behavior. If Quantity is 0, you can omit Items .

(string) --






TrustedSigners (dict) --
A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content.
If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled , and specify the applicable values for Quantity and Items . For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .
If you don\'t want to require signed URLs in requests for objects that match PathPattern , specify false for Enabled and 0 for Quantity . Omit Items .
To add, change, or remove one or more trusted signers, change Enabled to true (if it\'s currently false ), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.

Enabled (boolean) --
Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .

Quantity (integer) --
The number of trusted signers for this cache behavior.

Items (list) --

Optional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .


(string) --




ViewerProtocolPolicy (string) --
The protocol that viewers can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern . You can specify the following options:

allow-all : Viewers can use HTTP or HTTPS.
redirect-to-https : If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.
https-only : If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).

For more information about requiring the HTTPS protocol, see Using an HTTPS Connection to Access Your Objects in the Amazon CloudFront Developer Guide .

Note
The only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects\' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .


MinTTL (integer) --
The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .
You must specify 0 for MinTTL if you configure CloudFront to forward all headers to your origin (under Headers , if you specify 1 for Quantity and * for Name ).

AllowedMethods (dict) --
A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices:

CloudFront forwards only GET and HEAD requests.
CloudFront forwards only GET , HEAD , and OPTIONS requests.
CloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests.

If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can\'t perform operations that you don\'t want them to. For example, you might not want users to have permissions to delete objects from your origin.

Quantity (integer) --
The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET , HEAD , and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests).

Items (list) --
A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.

(string) --


CachedMethods (dict) --
A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices:

CloudFront caches responses to GET and HEAD requests.
CloudFront caches responses to GET , HEAD , and OPTIONS requests.

If you pick the second choice for your Amazon S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers, and Origin headers for the responses to be cached correctly.

Quantity (integer) --
The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET , HEAD , and OPTIONS requests).

Items (list) --
A complex type that contains the HTTP methods that you want CloudFront to cache responses to.

(string) --






SmoothStreaming (boolean) --
Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true ; if not, specify false . If you specify true for SmoothStreaming , you can still distribute other content using this cache behavior if the content matches the value of PathPattern .

DefaultTTL (integer) --
The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .

MaxTTL (integer) --
The maximum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .

Compress (boolean) --
Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify true; if not, specify false. For more information, see Serving Compressed Files in the Amazon CloudFront Developer Guide .

LambdaFunctionAssociations (dict) --
A complex type that contains zero or more Lambda function associations for a cache behavior.

Quantity (integer) --
The number of Lambda function associations for this cache behavior.

Items (list) --

Optional : A complex type that contains LambdaFunctionAssociation items for this cache behavior. If Quantity is 0 , you can omit Items .


(dict) --
A complex type that contains a Lambda function association.

LambdaFunctionARN (string) --
The ARN of the Lambda function. You must specify the ARN of a function version; you can\'t specify a Lambda alias or $LATEST.

EventType (string) --
Specifies the event type that triggers a Lambda function invocation. You can specify the following values:

viewer-request : The function executes when CloudFront receives a request from a viewer and before it checks to see whether the requested object is in the edge cache.
origin-request : The function executes only when CloudFront forwards a request to your origin. When the requested object is in the edge cache, the function doesn\'t execute.
origin-response : The function executes after CloudFront receives a response from the origin and before it caches the object in the response. When the requested object is in the edge cache, the function doesn\'t execute.
viewer-response : The function executes before CloudFront returns the requested object to the viewer. The function executes regardless of whether the object was already in the edge cache. If the origin returns an HTTP status code other than HTTP 200 (OK), the function doesn\'t execute.


IncludeBody (boolean) --
A flag that allows a Lambda function to have read access to the body content. For more information, see Accessing the Request Body by Choosing the Include Body Option in the Amazon CloudFront Developer Guide.







FieldLevelEncryptionId (string) --
The value of ID for the field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data for a cache behavior or for the default cache behavior in your distribution.







CustomErrorResponses (dict) --
A complex type that contains zero or more CustomErrorResponses elements.

Quantity (integer) --
The number of HTTP status codes for which you want to specify a custom error page and/or a caching duration. If Quantity is 0 , you can omit Items .

Items (list) --
A complex type that contains a CustomErrorResponse element for each HTTP status code for which you want to specify a custom error page and/or a caching duration.

(dict) --
A complex type that controls:

Whether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.
How long CloudFront caches HTTP status codes in the 4xx and 5xx range.

For more information about custom error pages, see Customizing Error Responses in the Amazon CloudFront Developer Guide .

ErrorCode (integer) --
The HTTP status code for which you want to specify a custom error page and/or a caching duration.

ResponsePagePath (string) --
The path to the custom error page that you want CloudFront to return to a viewer when your origin returns the HTTP status code specified by ErrorCode , for example, /4xx-errors/403-forbidden.html . If you want to store your objects and your custom error pages in different locations, your distribution must include a cache behavior for which the following is true:

The value of PathPattern matches the path to your custom error messages. For example, suppose you saved custom error pages for 4xx errors in an Amazon S3 bucket in a directory named /4xx-errors . Your distribution must include a cache behavior for which the path pattern routes requests for your custom error pages to that location, for example, /4xx-errors/* .
The value of TargetOriginId specifies the value of the ID element for the origin that contains your custom error pages.

If you specify a value for ResponsePagePath , you must also specify a value for ResponseCode .
We recommend that you store custom error pages in an Amazon S3 bucket. If you store custom error pages on an HTTP server and the server starts to return 5xx errors, CloudFront can\'t get the files that you want to return to viewers because the origin server is unavailable.

ResponseCode (string) --
The HTTP status code that you want CloudFront to return to the viewer along with the custom error page. There are a variety of reasons that you might want CloudFront to return a status code different from the status code that your origin returned to CloudFront, for example:

Some Internet devices (some firewalls and corporate proxies, for example) intercept HTTP 4xx and 5xx and prevent the response from being returned to the viewer. If you substitute 200 , the response typically won\'t be intercepted.
If you don\'t care about distinguishing among different client errors or server errors, you can specify 400 or 500 as the ResponseCode for all 4xx or 5xx errors.
You might want to return a 200 status code (OK) and static website so your customers don\'t know that your website is down.

If you specify a value for ResponseCode , you must also specify a value for ResponsePagePath .

ErrorCachingMinTTL (integer) --
The minimum amount of time, in seconds, that you want CloudFront to cache the HTTP status code specified in ErrorCode . When this time period has elapsed, CloudFront queries your origin to see whether the problem that caused the error has been resolved and the requested object is now available.
For more information, see Customizing Error Responses in the Amazon CloudFront Developer Guide .







Comment (string) --
The comment originally specified when this distribution was created.

PriceClass (string) --
A complex type that contains information about price class for this streaming distribution.

Enabled (boolean) --
Whether the distribution is enabled to accept user requests for content.

ViewerCertificate (dict) --
A complex type that determines the distribution\xe2\x80\x99s SSL/TLS configuration for communicating with viewers.

CloudFrontDefaultCertificate (boolean) --
If the distribution uses the CloudFront domain name such as d111111abcdef8.cloudfront.net , set this field to true .
If the distribution uses Aliases (alternate domain names or CNAMEs), set this field to false and specify values for the following fields:

ACMCertificateArn or IAMCertificateId (specify a value for one, not both)
MinimumProtocolVersion
SSLSupportMethod


IAMCertificateId (string) --
If the distribution uses Aliases (alternate domain names or CNAMEs) and the SSL/TLS certificate is stored in AWS Identity and Access Management (AWS IAM) , provide the ID of the IAM certificate.
If you specify an IAM certificate ID, you must also specify values for MinimumProtocolVerison and SSLSupportMethod .

ACMCertificateArn (string) --
If the distribution uses Aliases (alternate domain names or CNAMEs) and the SSL/TLS certificate is stored in AWS Certificate Manager (ACM) , provide the Amazon Resource Name (ARN) of the ACM certificate. CloudFront only supports ACM certificates in the US East (N. Virginia) Region (us-east-1 ).
If you specify an ACM certificate ARN, you must also specify values for MinimumProtocolVerison and SSLSupportMethod .

SSLSupportMethod (string) --
If the distribution uses Aliases (alternate domain names or CNAMEs), specify which viewers the distribution accepts HTTPS connections from.

sni-only \xe2\x80\x93 The distribution accepts HTTPS connections from only viewers that support server name indication (SNI) . This is recommended. Most browsers and clients released after 2010 support SNI.
vip \xe2\x80\x93 The distribution accepts HTTPS connections from all viewers including those that don\xe2\x80\x99t support SNI. This is not recommended, and results in additional monthly charges from CloudFront.

If the distribution uses the CloudFront domain name such as d111111abcdef8.cloudfront.net , don\xe2\x80\x99t set a value for this field.

MinimumProtocolVersion (string) --
If the distribution uses Aliases (alternate domain names or CNAMEs), specify the security policy that you want CloudFront to use for HTTPS connections with viewers. The security policy determines two settings:

The minimum SSL/TLS protocol that CloudFront can use to communicate with viewers.
The ciphers that CloudFront can use to encrypt the content that it returns to viewers.

For more information, see Security Policy and Supported Protocols and Ciphers Between Viewers and CloudFront in the Amazon CloudFront Developer Guide .

Note
On the CloudFront console, this setting is called Security Policy .

We recommend that you specify TLSv1.2_2018 unless your viewers are using browsers or devices that don\xe2\x80\x99t support TLSv1.2.
When you\xe2\x80\x99re using SNI only (you set SSLSupportMethod to sni-only ), you must specify TLSv1 or higher.
If the distribution uses the CloudFront domain name such as d111111abcdef8.cloudfront.net (you set CloudFrontDefaultCertificate to true ), CloudFront automatically sets the security policy to TLSv1 regardless of the value that you set here.

Certificate (string) --
This field is deprecated. Use one of the following fields instead:

ACMCertificateArn
IAMCertificateId
CloudFrontDefaultCertificate


CertificateSource (string) --
This field is deprecated. Use one of the following fields instead:

ACMCertificateArn
IAMCertificateId
CloudFrontDefaultCertificate




Restrictions (dict) --
A complex type that identifies ways in which you want to restrict distribution of your content.

GeoRestriction (dict) --
A complex type that controls the countries in which your content is distributed. CloudFront determines the location of your users using MaxMind GeoIP databases.

RestrictionType (string) --
The method that you want to use to restrict distribution of your content by country:

none : No geo restriction is enabled, meaning access to content is not restricted by client geo location.
blacklist : The Location elements specify the countries in which you don\'t want CloudFront to distribute your content.
whitelist : The Location elements specify the countries in which you want CloudFront to distribute your content.


Quantity (integer) --
When geo restriction is enabled , this is the number of countries in your whitelist or blacklist . Otherwise, when it is not enabled, Quantity is 0 , and you can omit Items .

Items (list) --
A complex type that contains a Location element for each country in which you want CloudFront either to distribute your content (whitelist ) or not distribute your content (blacklist ).
The Location element is a two-letter, uppercase country code for a country that you want to include in your blacklist or whitelist . Include one Location element for each country.
CloudFront and MaxMind both use ISO 3166 country codes. For the current list of countries and the corresponding codes, see ISO 3166-1-alpha-2 code on the International Organization for Standardization website. You can also refer to the country list on the CloudFront console, which includes both country names and codes.

(string) --






WebACLId (string) --
The Web ACL Id (if any) associated with the distribution.

HttpVersion (string) --
Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront. The default value for new web distributions is http2 . Viewers that don\'t support HTTP/2 will automatically use an earlier version.

IsIPV6Enabled (boolean) --
Whether CloudFront responds to IPv6 DNS requests with an IPv6 address for your distribution.

AliasICPRecordals (list) --
AWS services in China customers must file for an Internet Content Provider (ICP) recordal if they want to serve content publicly on an alternate domain name, also known as a CNAME, that they\'ve added to CloudFront. AliasICPRecordal provides the ICP recordal status for CNAMEs associated with distributions.
For more information about ICP recordals, see Signup, Accounts, and Credentials in Getting Started with AWS services in China .

(dict) --
AWS services in China customers must file for an Internet Content Provider (ICP) recordal if they want to serve content publicly on an alternate domain name, also known as a CNAME, that they\'ve added to CloudFront. AliasICPRecordal provides the ICP recordal status for CNAMEs associated with distributions. The status is returned in the CloudFront response; you can\'t configure it yourself.
For more information about ICP recordals, see Signup, Accounts, and Credentials in Getting Started with AWS services in China .

CNAME (string) --
A domain name associated with a distribution.

ICPRecordalStatus (string) --
The Internet Content Provider (ICP) recordal status for a CNAME. The ICPRecordalStatus is set to APPROVED for all CNAMEs (aliases) in regions outside of China.
The status values returned are the following:

APPROVED indicates that the associated CNAME has a valid ICP recordal number. Multiple CNAMEs can be associated with a distribution, and CNAMEs can correspond to different ICP recordals. To be marked as APPROVED, that is, valid to use with China region, a CNAME must have one ICP recordal number associated with it.
SUSPENDED indicates that the associated CNAME does not have a valid ICP recordal number.
PENDING indicates that CloudFront can\'t determine the ICP recordal status of the CNAME associated with the distribution because there was an error in trying to determine the status. You can try again to see if the error is resolved in which case CloudFront returns an APPROVED or SUSPENDED status.


















Exceptions

CloudFront.Client.exceptions.InvalidArgument


    :return: {
        'DistributionList': {
            'Marker': 'string',
            'NextMarker': 'string',
            'MaxItems': 123,
            'IsTruncated': True|False,
            'Quantity': 123,
            'Items': [
                {
                    'Id': 'string',
                    'ARN': 'string',
                    'Status': 'string',
                    'LastModifiedTime': datetime(2015, 1, 1),
                    'DomainName': 'string',
                    'Aliases': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    },
                    'Origins': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'Id': 'string',
                                'DomainName': 'string',
                                'OriginPath': 'string',
                                'CustomHeaders': {
                                    'Quantity': 123,
                                    'Items': [
                                        {
                                            'HeaderName': 'string',
                                            'HeaderValue': 'string'
                                        },
                                    ]
                                },
                                'S3OriginConfig': {
                                    'OriginAccessIdentity': 'string'
                                },
                                'CustomOriginConfig': {
                                    'HTTPPort': 123,
                                    'HTTPSPort': 123,
                                    'OriginProtocolPolicy': 'http-only'|'match-viewer'|'https-only',
                                    'OriginSslProtocols': {
                                        'Quantity': 123,
                                        'Items': [
                                            'SSLv3'|'TLSv1'|'TLSv1.1'|'TLSv1.2',
                                        ]
                                    },
                                    'OriginReadTimeout': 123,
                                    'OriginKeepaliveTimeout': 123
                                }
                            },
                        ]
                    },
                    'OriginGroups': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'Id': 'string',
                                'FailoverCriteria': {
                                    'StatusCodes': {
                                        'Quantity': 123,
                                        'Items': [
                                            123,
                                        ]
                                    }
                                },
                                'Members': {
                                    'Quantity': 123,
                                    'Items': [
                                        {
                                            'OriginId': 'string'
                                        },
                                    ]
                                }
                            },
                        ]
                    },
                    'DefaultCacheBehavior': {
                        'TargetOriginId': 'string',
                        'ForwardedValues': {
                            'QueryString': True|False,
                            'Cookies': {
                                'Forward': 'none'|'whitelist'|'all',
                                'WhitelistedNames': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                }
                            },
                            'Headers': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            },
                            'QueryStringCacheKeys': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                        'TrustedSigners': {
                            'Enabled': True|False,
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        },
                        'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                        'MinTTL': 123,
                        'AllowedMethods': {
                            'Quantity': 123,
                            'Items': [
                                'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                            ],
                            'CachedMethods': {
                                'Quantity': 123,
                                'Items': [
                                    'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                ]
                            }
                        },
                        'SmoothStreaming': True|False,
                        'DefaultTTL': 123,
                        'MaxTTL': 123,
                        'Compress': True|False,
                        'LambdaFunctionAssociations': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'LambdaFunctionARN': 'string',
                                    'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                    'IncludeBody': True|False
                                },
                            ]
                        },
                        'FieldLevelEncryptionId': 'string'
                    },
                    'CacheBehaviors': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'PathPattern': 'string',
                                'TargetOriginId': 'string',
                                'ForwardedValues': {
                                    'QueryString': True|False,
                                    'Cookies': {
                                        'Forward': 'none'|'whitelist'|'all',
                                        'WhitelistedNames': {
                                            'Quantity': 123,
                                            'Items': [
                                                'string',
                                            ]
                                        }
                                    },
                                    'Headers': {
                                        'Quantity': 123,
                                        'Items': [
                                            'string',
                                        ]
                                    },
                                    'QueryStringCacheKeys': {
                                        'Quantity': 123,
                                        'Items': [
                                            'string',
                                        ]
                                    }
                                },
                                'TrustedSigners': {
                                    'Enabled': True|False,
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                },
                                'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                                'MinTTL': 123,
                                'AllowedMethods': {
                                    'Quantity': 123,
                                    'Items': [
                                        'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                    ],
                                    'CachedMethods': {
                                        'Quantity': 123,
                                        'Items': [
                                            'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                        ]
                                    }
                                },
                                'SmoothStreaming': True|False,
                                'DefaultTTL': 123,
                                'MaxTTL': 123,
                                'Compress': True|False,
                                'LambdaFunctionAssociations': {
                                    'Quantity': 123,
                                    'Items': [
                                        {
                                            'LambdaFunctionARN': 'string',
                                            'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                            'IncludeBody': True|False
                                        },
                                    ]
                                },
                                'FieldLevelEncryptionId': 'string'
                            },
                        ]
                    },
                    'CustomErrorResponses': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'ErrorCode': 123,
                                'ResponsePagePath': 'string',
                                'ResponseCode': 'string',
                                'ErrorCachingMinTTL': 123
                            },
                        ]
                    },
                    'Comment': 'string',
                    'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
                    'Enabled': True|False,
                    'ViewerCertificate': {
                        'CloudFrontDefaultCertificate': True|False,
                        'IAMCertificateId': 'string',
                        'ACMCertificateArn': 'string',
                        'SSLSupportMethod': 'sni-only'|'vip',
                        'MinimumProtocolVersion': 'SSLv3'|'TLSv1'|'TLSv1_2016'|'TLSv1.1_2016'|'TLSv1.2_2018',
                        'Certificate': 'string',
                        'CertificateSource': 'cloudfront'|'iam'|'acm'
                    },
                    'Restrictions': {
                        'GeoRestriction': {
                            'RestrictionType': 'blacklist'|'whitelist'|'none',
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                    'WebACLId': 'string',
                    'HttpVersion': 'http1.1'|'http2',
                    'IsIPV6Enabled': True|False,
                    'AliasICPRecordals': [
                        {
                            'CNAME': 'string',
                            'ICPRecordalStatus': 'APPROVED'|'SUSPENDED'|'PENDING'
                        },
                    ]
                },
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_distributions_by_web_acl_id(Marker=None, MaxItems=None, WebACLId=None):
    """
    List the distributions that are associated with a specified AWS WAF web ACL.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_distributions_by_web_acl_id(
        Marker='string',
        MaxItems='string',
        WebACLId='string'
    )
    
    
    :type Marker: string
    :param Marker: Use Marker and MaxItems to control pagination of results. If you have more than MaxItems distributions that satisfy the request, the response includes a NextMarker element. To get the next page of results, submit another request. For the value of Marker , specify the value of NextMarker from the last response. (For the first request, omit Marker .)

    :type MaxItems: string
    :param MaxItems: The maximum number of distributions that you want CloudFront to return in the response body. The maximum and default values are both 100.

    :type WebACLId: string
    :param WebACLId: [REQUIRED]\nThe ID of the AWS WAF web ACL that you want to list the associated distributions. If you specify 'null' for the ID, the request returns a list of the distributions that aren\'t associated with a web ACL.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DistributionList': {
        'Marker': 'string',
        'NextMarker': 'string',
        'MaxItems': 123,
        'IsTruncated': True|False,
        'Quantity': 123,
        'Items': [
            {
                'Id': 'string',
                'ARN': 'string',
                'Status': 'string',
                'LastModifiedTime': datetime(2015, 1, 1),
                'DomainName': 'string',
                'Aliases': {
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'Origins': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'Id': 'string',
                            'DomainName': 'string',
                            'OriginPath': 'string',
                            'CustomHeaders': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'HeaderName': 'string',
                                        'HeaderValue': 'string'
                                    },
                                ]
                            },
                            'S3OriginConfig': {
                                'OriginAccessIdentity': 'string'
                            },
                            'CustomOriginConfig': {
                                'HTTPPort': 123,
                                'HTTPSPort': 123,
                                'OriginProtocolPolicy': 'http-only'|'match-viewer'|'https-only',
                                'OriginSslProtocols': {
                                    'Quantity': 123,
                                    'Items': [
                                        'SSLv3'|'TLSv1'|'TLSv1.1'|'TLSv1.2',
                                    ]
                                },
                                'OriginReadTimeout': 123,
                                'OriginKeepaliveTimeout': 123
                            }
                        },
                    ]
                },
                'OriginGroups': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'Id': 'string',
                            'FailoverCriteria': {
                                'StatusCodes': {
                                    'Quantity': 123,
                                    'Items': [
                                        123,
                                    ]
                                }
                            },
                            'Members': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'OriginId': 'string'
                                    },
                                ]
                            }
                        },
                    ]
                },
                'DefaultCacheBehavior': {
                    'TargetOriginId': 'string',
                    'ForwardedValues': {
                        'QueryString': True|False,
                        'Cookies': {
                            'Forward': 'none'|'whitelist'|'all',
                            'WhitelistedNames': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                        'Headers': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        },
                        'QueryStringCacheKeys': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                    'TrustedSigners': {
                        'Enabled': True|False,
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    },
                    'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                    'MinTTL': 123,
                    'AllowedMethods': {
                        'Quantity': 123,
                        'Items': [
                            'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                        ],
                        'CachedMethods': {
                            'Quantity': 123,
                            'Items': [
                                'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                            ]
                        }
                    },
                    'SmoothStreaming': True|False,
                    'DefaultTTL': 123,
                    'MaxTTL': 123,
                    'Compress': True|False,
                    'LambdaFunctionAssociations': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'LambdaFunctionARN': 'string',
                                'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                'IncludeBody': True|False
                            },
                        ]
                    },
                    'FieldLevelEncryptionId': 'string'
                },
                'CacheBehaviors': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'PathPattern': 'string',
                            'TargetOriginId': 'string',
                            'ForwardedValues': {
                                'QueryString': True|False,
                                'Cookies': {
                                    'Forward': 'none'|'whitelist'|'all',
                                    'WhitelistedNames': {
                                        'Quantity': 123,
                                        'Items': [
                                            'string',
                                        ]
                                    }
                                },
                                'Headers': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                },
                                'QueryStringCacheKeys': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                }
                            },
                            'TrustedSigners': {
                                'Enabled': True|False,
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            },
                            'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                            'MinTTL': 123,
                            'AllowedMethods': {
                                'Quantity': 123,
                                'Items': [
                                    'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                ],
                                'CachedMethods': {
                                    'Quantity': 123,
                                    'Items': [
                                        'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                    ]
                                }
                            },
                            'SmoothStreaming': True|False,
                            'DefaultTTL': 123,
                            'MaxTTL': 123,
                            'Compress': True|False,
                            'LambdaFunctionAssociations': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'LambdaFunctionARN': 'string',
                                        'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                        'IncludeBody': True|False
                                    },
                                ]
                            },
                            'FieldLevelEncryptionId': 'string'
                        },
                    ]
                },
                'CustomErrorResponses': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'ErrorCode': 123,
                            'ResponsePagePath': 'string',
                            'ResponseCode': 'string',
                            'ErrorCachingMinTTL': 123
                        },
                    ]
                },
                'Comment': 'string',
                'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
                'Enabled': True|False,
                'ViewerCertificate': {
                    'CloudFrontDefaultCertificate': True|False,
                    'IAMCertificateId': 'string',
                    'ACMCertificateArn': 'string',
                    'SSLSupportMethod': 'sni-only'|'vip',
                    'MinimumProtocolVersion': 'SSLv3'|'TLSv1'|'TLSv1_2016'|'TLSv1.1_2016'|'TLSv1.2_2018',
                    'Certificate': 'string',
                    'CertificateSource': 'cloudfront'|'iam'|'acm'
                },
                'Restrictions': {
                    'GeoRestriction': {
                        'RestrictionType': 'blacklist'|'whitelist'|'none',
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    }
                },
                'WebACLId': 'string',
                'HttpVersion': 'http1.1'|'http2',
                'IsIPV6Enabled': True|False,
                'AliasICPRecordals': [
                    {
                        'CNAME': 'string',
                        'ICPRecordalStatus': 'APPROVED'|'SUSPENDED'|'PENDING'
                    },
                ]
            },
        ]
    }
}


Response Structure

(dict) --
The response to a request to list the distributions that are associated with a specified AWS WAF web ACL.

DistributionList (dict) --
The DistributionList type.

Marker (string) --
The value you provided for the Marker request parameter.

NextMarker (string) --
If IsTruncated is true , this element is present and contains the value you can use for the Marker request parameter to continue listing your distributions where they left off.

MaxItems (integer) --
The value you provided for the MaxItems request parameter.

IsTruncated (boolean) --
A flag that indicates whether more distributions remain to be listed. If your results were truncated, you can make a follow-up pagination request using the Marker request parameter to retrieve more distributions in the list.

Quantity (integer) --
The number of distributions that were created by the current AWS account.

Items (list) --
A complex type that contains one DistributionSummary element for each distribution that was created by the current AWS account.

(dict) --
A summary of the information about a CloudFront distribution.

Id (string) --
The identifier for the distribution. For example: EDFDVBD632BHDS5 .

ARN (string) --
The ARN (Amazon Resource Name) for the distribution. For example: arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5 , where 123456789012 is your AWS account ID.

Status (string) --
The current status of the distribution. When the status is Deployed , the distribution\'s information is propagated to all CloudFront edge locations.

LastModifiedTime (datetime) --
The date and time the distribution was last modified.

DomainName (string) --
The domain name that corresponds to the distribution, for example, d111111abcdef8.cloudfront.net .

Aliases (dict) --
A complex type that contains information about CNAMEs (alternate domain names), if any, for this distribution.

Quantity (integer) --
The number of CNAME aliases, if any, that you want to associate with this distribution.

Items (list) --
A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.

(string) --




Origins (dict) --
A complex type that contains information about origins for this distribution.

Quantity (integer) --
The number of origins or origin groups for this distribution.

Items (list) --
A complex type that contains origins or origin groups for this distribution.

(dict) --
A complex type that describes the Amazon S3 bucket, HTTP server (for example, a web server), Amazon MediaStore, or other server from which CloudFront gets your files. This can also be an origin group, if you\'ve created an origin group. You must specify at least one origin or origin group.
For the current limit on the number of origins or origin groups that you can specify for a distribution, see Amazon CloudFront Limits in the AWS General Reference .

Id (string) --
A unique identifier for the origin or origin group. The value of Id must be unique within the distribution.
When you specify the value of TargetOriginId for the default cache behavior or for another cache behavior, you indicate the origin to which you want the cache behavior to route requests by specifying the value of the Id element for that origin. When a request matches the path pattern for that cache behavior, CloudFront routes the request to the specified origin. For more information, see Cache Behavior Settings in the Amazon CloudFront Developer Guide .

DomainName (string) --

Amazon S3 origins : The DNS name of the Amazon S3 bucket from which you want CloudFront to get objects for this origin, for example, myawsbucket.s3.amazonaws.com . If you set up your bucket to be configured as a website endpoint, enter the Amazon S3 static website hosting endpoint for the bucket.

For more information about specifying this value for different types of origins, see Origin Domain Name in the Amazon CloudFront Developer Guide .
Constraints for Amazon S3 origins:

If you configured Amazon S3 Transfer Acceleration for your bucket, don\'t specify the s3-accelerate endpoint for DomainName .
The bucket name must be between 3 and 63 characters long (inclusive).
The bucket name must contain only lowercase characters, numbers, periods, underscores, and dashes.
The bucket name must not contain adjacent periods.


Custom Origins : The DNS domain name for the HTTP server from which you want CloudFront to get objects for this origin, for example, www.example.com .

Constraints for custom origins:

DomainName must be a valid DNS name that contains only a-z, A-Z, 0-9, dot (.), hyphen (-), or underscore (_) characters.
The name cannot exceed 128 characters.


OriginPath (string) --
An optional element that causes CloudFront to request your content from a directory in your Amazon S3 bucket or your custom origin. When you include the OriginPath element, specify the directory name, beginning with a / . CloudFront appends the directory name to the value of DomainName , for example, example.com/production . Do not include a / at the end of the directory name.
For example, suppose you\'ve specified the following values for your distribution:

DomainName : An Amazon S3 bucket named myawsbucket .
OriginPath : /production
CNAME : example.com

When a user enters example.com/index.html in a browser, CloudFront sends a request to Amazon S3 for myawsbucket/production/index.html .
When a user enters example.com/acme/index.html in a browser, CloudFront sends a request to Amazon S3 for myawsbucket/production/acme/index.html .

CustomHeaders (dict) --
A complex type that contains names and values for the custom headers that you want.

Quantity (integer) --
The number of custom headers, if any, for this distribution.

Items (list) --

Optional : A list that contains one OriginCustomHeader element for each custom header that you want CloudFront to forward to the origin. If Quantity is 0 , omit Items .


(dict) --
A complex type that contains HeaderName and HeaderValue elements, if any, for this distribution.

HeaderName (string) --
The name of a header that you want CloudFront to forward to your origin. For more information, see Forwarding Custom Headers to Your Origin (Web Distributions Only) in the Amazon CloudFront Developer Guide .

HeaderValue (string) --
The value for the header that you specified in the HeaderName field.







S3OriginConfig (dict) --
A complex type that contains information about the Amazon S3 origin. If the origin is a custom origin, use the CustomOriginConfig element instead.

OriginAccessIdentity (string) --
The CloudFront origin access identity to associate with the origin. Use an origin access identity to configure the origin so that viewers can only access objects in an Amazon S3 bucket through CloudFront. The format of the value is:
origin-access-identity/cloudfront/ID-of-origin-access-identity
where `` ID-of-origin-access-identity `` is the value that CloudFront returned in the ID element when you created the origin access identity.
If you want viewers to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty OriginAccessIdentity element.
To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty OriginAccessIdentity element.
To replace the origin access identity, update the distribution configuration and specify the new origin access identity.
For more information about the origin access identity, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .



CustomOriginConfig (dict) --
A complex type that contains information about a custom origin. If the origin is an Amazon S3 bucket, use the S3OriginConfig element instead.

HTTPPort (integer) --
The HTTP port the custom origin listens on.

HTTPSPort (integer) --
The HTTPS port the custom origin listens on.

OriginProtocolPolicy (string) --
The origin protocol policy to apply to your origin.

OriginSslProtocols (dict) --
The SSL/TLS protocols that you want CloudFront to use when communicating with your origin over HTTPS.

Quantity (integer) --
The number of SSL/TLS protocols that you want to allow CloudFront to use when establishing an HTTPS connection with this origin.

Items (list) --
A list that contains allowed SSL/TLS protocols for this distribution.

(string) --




OriginReadTimeout (integer) --
You can create a custom origin read timeout. All timeout units are in seconds. The default origin read timeout is 30 seconds, but you can configure custom timeout lengths using the CloudFront API. The minimum timeout length is 4 seconds; the maximum is 60 seconds.
If you need to increase the maximum time limit, contact the AWS Support Center .

OriginKeepaliveTimeout (integer) --
You can create a custom keep-alive timeout. All timeout units are in seconds. The default keep-alive timeout is 5 seconds, but you can configure custom timeout lengths using the CloudFront API. The minimum timeout length is 1 second; the maximum is 60 seconds.
If you need to increase the maximum time limit, contact the AWS Support Center .









OriginGroups (dict) --
A complex type that contains information about origin groups for this distribution.

Quantity (integer) --
The number of origin groups.

Items (list) --
The items (origin groups) in a distribution.

(dict) --
An origin group includes two origins (a primary origin and a second origin to failover to) and a failover criteria that you specify. You create an origin group to support origin failover in CloudFront. When you create or update a distribution, you can specifiy the origin group instead of a single origin, and CloudFront will failover from the primary origin to the second origin under the failover conditions that you\'ve chosen.

Id (string) --
The origin group\'s ID.

FailoverCriteria (dict) --
A complex type that contains information about the failover criteria for an origin group.

StatusCodes (dict) --
The status codes that, when returned from the primary origin, will trigger CloudFront to failover to the second origin.

Quantity (integer) --
The number of status codes.

Items (list) --
The items (status codes) for an origin group.

(integer) --






Members (dict) --
A complex type that contains information about the origins in an origin group.

Quantity (integer) --
The number of origins in an origin group.

Items (list) --
Items (origins) in an origin group.

(dict) --
An origin in an origin group.

OriginId (string) --
The ID for an origin in an origin group.













DefaultCacheBehavior (dict) --
A complex type that describes the default cache behavior if you don\'t specify a CacheBehavior element or if files don\'t match any of the values of PathPattern in CacheBehavior elements. You must create exactly one default cache behavior.

TargetOriginId (string) --
The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior in your distribution.

ForwardedValues (dict) --
A complex type that specifies how CloudFront handles query strings, cookies, and HTTP headers.

QueryString (boolean) --
Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior and cache based on the query string parameters. CloudFront behavior depends on the value of QueryString and on the values that you specify for QueryStringCacheKeys , if any:
If you specify true for QueryString and you don\'t specify any values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin and caches based on all query string parameters. Depending on how many query string parameters and values you have, this can adversely affect performance because CloudFront must forward more requests to the origin.
If you specify true for QueryString and you specify one or more values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin, but it only caches based on the query string parameters that you specify.
If you specify false for QueryString , CloudFront doesn\'t forward any query string parameters to the origin, and doesn\'t cache based on query string parameters.
For more information, see Configuring CloudFront to Cache Based on Query String Parameters in the Amazon CloudFront Developer Guide .

Cookies (dict) --
A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see How CloudFront Forwards, Caches, and Logs Cookies in the Amazon CloudFront Developer Guide .

Forward (string) --
Specifies which cookies to forward to the origin for this cache behavior: all, none, or the list of cookies specified in the WhitelistedNames complex type.
Amazon S3 doesn\'t process cookies. When the cache behavior is forwarding requests to an Amazon S3 origin, specify none for the Forward element.

WhitelistedNames (dict) --
Required if you specify whitelist for the value of Forward . A complex type that specifies how many different cookies you want CloudFront to forward to the origin for this cache behavior and, if you want to forward selected cookies, the names of those cookies.
If you specify all or none for the value of Forward , omit WhitelistedNames . If you change the value of Forward from whitelist to all or none and you don\'t delete the WhitelistedNames element and its child elements, CloudFront deletes them automatically.
For the current limit on the number of cookie names that you can whitelist for each cache behavior, see CloudFront Limits in the AWS General Reference .

Quantity (integer) --
The number of different cookies that you want CloudFront to forward to the origin for this cache behavior. The value must equal the number of items that are in the Items field.
When you set Forward = whitelist (in the CookiePreferences object), this value must be 1 or higher.

Items (list) --
A complex type that contains one Name element for each cookie that you want CloudFront to forward to the origin for this cache behavior. It must contain the same number of items that is specified in the Quantity field.
When you set Forward = whitelist (in the CookiePreferences object), this field must contain at least one item.

(string) --






Headers (dict) --
A complex type that specifies the Headers , if any, that you want CloudFront to forward to the origin for this cache behavior (whitelisted headers). For the headers that you specify, CloudFront also caches separate versions of a specified object that is based on the header values in viewer requests.
For more information, see Caching Content Based on Request Headers in the Amazon CloudFront Developer Guide .

Quantity (integer) --
The number of different headers that you want CloudFront to base caching on for this cache behavior. You can configure each cache behavior in a web distribution to do one of the following:

Forward all headers to your origin : Specify 1 for Quantity and * for Name .


Warning
CloudFront doesn\'t cache the objects that are associated with this cache behavior. Instead, CloudFront sends every request to the origin.


Forward a whitelist of headers you specify : Specify the number of headers that you want CloudFront to base caching on. Then specify the header names in Name elements. CloudFront caches your objects based on the values in the specified headers.
Forward only the default headers : Specify 0 for Quantity and omit Items . In this configuration, CloudFront doesn\'t cache based on the values in the request headers.

Regardless of which option you choose, CloudFront forwards headers to your origin based on whether the origin is an S3 bucket or a custom origin. See the following documentation:

S3 bucket : See HTTP Request Headers That CloudFront Removes or Updates
Custom origin : See HTTP Request Headers and CloudFront Behavior


Items (list) --
A list that contains one Name element for each header that you want CloudFront to use for caching in this cache behavior. If Quantity is 0 , omit Items .

(string) --




QueryStringCacheKeys (dict) --
A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.

Quantity (integer) --
The number of whitelisted query string parameters for a cache behavior.

Items (list) --
A list that contains the query string parameters that you want CloudFront to use as a basis for caching for a cache behavior. If Quantity is 0, you can omit Items .

(string) --






TrustedSigners (dict) --
A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content.
If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled , and specify the applicable values for Quantity and Items . For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .
If you don\'t want to require signed URLs in requests for objects that match PathPattern , specify false for Enabled and 0 for Quantity . Omit Items .
To add, change, or remove one or more trusted signers, change Enabled to true (if it\'s currently false ), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.

Enabled (boolean) --
Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .

Quantity (integer) --
The number of trusted signers for this cache behavior.

Items (list) --

Optional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .


(string) --




ViewerProtocolPolicy (string) --
The protocol that viewers can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern . You can specify the following options:

allow-all : Viewers can use HTTP or HTTPS.
redirect-to-https : If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.
https-only : If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).

For more information about requiring the HTTPS protocol, see Using an HTTPS Connection to Access Your Objects in the Amazon CloudFront Developer Guide .

Note
The only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects\' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .


MinTTL (integer) --
The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .
You must specify 0 for MinTTL if you configure CloudFront to forward all headers to your origin (under Headers , if you specify 1 for Quantity and * for Name ).

AllowedMethods (dict) --
A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices:

CloudFront forwards only GET and HEAD requests.
CloudFront forwards only GET , HEAD , and OPTIONS requests.
CloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests.

If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can\'t perform operations that you don\'t want them to. For example, you might not want users to have permissions to delete objects from your origin.

Quantity (integer) --
The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET , HEAD , and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests).

Items (list) --
A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.

(string) --


CachedMethods (dict) --
A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices:

CloudFront caches responses to GET and HEAD requests.
CloudFront caches responses to GET , HEAD , and OPTIONS requests.

If you pick the second choice for your Amazon S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers, and Origin headers for the responses to be cached correctly.

Quantity (integer) --
The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET , HEAD , and OPTIONS requests).

Items (list) --
A complex type that contains the HTTP methods that you want CloudFront to cache responses to.

(string) --






SmoothStreaming (boolean) --
Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true ; if not, specify false . If you specify true for SmoothStreaming , you can still distribute other content using this cache behavior if the content matches the value of PathPattern .

DefaultTTL (integer) --
The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .

MaxTTL (integer) --
The maximum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .

Compress (boolean) --
Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify true ; if not, specify false . For more information, see Serving Compressed Files in the Amazon CloudFront Developer Guide .

LambdaFunctionAssociations (dict) --
A complex type that contains zero or more Lambda function associations for a cache behavior.

Quantity (integer) --
The number of Lambda function associations for this cache behavior.

Items (list) --

Optional : A complex type that contains LambdaFunctionAssociation items for this cache behavior. If Quantity is 0 , you can omit Items .


(dict) --
A complex type that contains a Lambda function association.

LambdaFunctionARN (string) --
The ARN of the Lambda function. You must specify the ARN of a function version; you can\'t specify a Lambda alias or $LATEST.

EventType (string) --
Specifies the event type that triggers a Lambda function invocation. You can specify the following values:

viewer-request : The function executes when CloudFront receives a request from a viewer and before it checks to see whether the requested object is in the edge cache.
origin-request : The function executes only when CloudFront forwards a request to your origin. When the requested object is in the edge cache, the function doesn\'t execute.
origin-response : The function executes after CloudFront receives a response from the origin and before it caches the object in the response. When the requested object is in the edge cache, the function doesn\'t execute.
viewer-response : The function executes before CloudFront returns the requested object to the viewer. The function executes regardless of whether the object was already in the edge cache. If the origin returns an HTTP status code other than HTTP 200 (OK), the function doesn\'t execute.


IncludeBody (boolean) --
A flag that allows a Lambda function to have read access to the body content. For more information, see Accessing the Request Body by Choosing the Include Body Option in the Amazon CloudFront Developer Guide.







FieldLevelEncryptionId (string) --
The value of ID for the field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data for a cache behavior or for the default cache behavior in your distribution.



CacheBehaviors (dict) --
A complex type that contains zero or more CacheBehavior elements.

Quantity (integer) --
The number of cache behaviors for this distribution.

Items (list) --
Optional: A complex type that contains cache behaviors for this distribution. If Quantity is 0 , you can omit Items .

(dict) --
A complex type that describes how CloudFront processes requests.
You must create at least as many cache behaviors (including the default cache behavior) as you have origins if you want CloudFront to distribute objects from all of the origins. Each cache behavior specifies the one origin from which you want CloudFront to get objects. If you have two origins and only the default cache behavior, the default cache behavior will cause CloudFront to get objects from one of the origins, but the other origin is never used.
For the current limit on the number of cache behaviors that you can add to a distribution, see Amazon CloudFront Limits in the AWS General Reference .
If you don\'t want to specify any cache behaviors, include only an empty CacheBehaviors element. Don\'t include an empty CacheBehavior element, or CloudFront returns a MalformedXML error.
To delete all cache behaviors in an existing distribution, update the distribution configuration and include only an empty CacheBehaviors element.
To add, change, or remove one or more cache behaviors, update the distribution configuration and specify all of the cache behaviors that you want to include in the updated distribution.
For more information about cache behaviors, see Cache Behaviors in the Amazon CloudFront Developer Guide .

PathPattern (string) --
The pattern (for example, images/*.jpg ) that specifies which requests to apply the behavior to. When CloudFront receives a viewer request, the requested path is compared with path patterns in the order in which cache behaviors are listed in the distribution.

Note
You can optionally include a slash (/ ) at the beginning of the path pattern. For example, /images/*.jpg . CloudFront behavior is the same with or without the leading / .

The path pattern for the default cache behavior is * and cannot be changed. If the request for an object does not match the path pattern for any cache behaviors, CloudFront applies the behavior in the default cache behavior.
For more information, see Path Pattern in the Amazon CloudFront Developer Guide .

TargetOriginId (string) --
The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior in your distribution.

ForwardedValues (dict) --
A complex type that specifies how CloudFront handles query strings, cookies, and HTTP headers.

QueryString (boolean) --
Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior and cache based on the query string parameters. CloudFront behavior depends on the value of QueryString and on the values that you specify for QueryStringCacheKeys , if any:
If you specify true for QueryString and you don\'t specify any values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin and caches based on all query string parameters. Depending on how many query string parameters and values you have, this can adversely affect performance because CloudFront must forward more requests to the origin.
If you specify true for QueryString and you specify one or more values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin, but it only caches based on the query string parameters that you specify.
If you specify false for QueryString , CloudFront doesn\'t forward any query string parameters to the origin, and doesn\'t cache based on query string parameters.
For more information, see Configuring CloudFront to Cache Based on Query String Parameters in the Amazon CloudFront Developer Guide .

Cookies (dict) --
A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see How CloudFront Forwards, Caches, and Logs Cookies in the Amazon CloudFront Developer Guide .

Forward (string) --
Specifies which cookies to forward to the origin for this cache behavior: all, none, or the list of cookies specified in the WhitelistedNames complex type.
Amazon S3 doesn\'t process cookies. When the cache behavior is forwarding requests to an Amazon S3 origin, specify none for the Forward element.

WhitelistedNames (dict) --
Required if you specify whitelist for the value of Forward . A complex type that specifies how many different cookies you want CloudFront to forward to the origin for this cache behavior and, if you want to forward selected cookies, the names of those cookies.
If you specify all or none for the value of Forward , omit WhitelistedNames . If you change the value of Forward from whitelist to all or none and you don\'t delete the WhitelistedNames element and its child elements, CloudFront deletes them automatically.
For the current limit on the number of cookie names that you can whitelist for each cache behavior, see CloudFront Limits in the AWS General Reference .

Quantity (integer) --
The number of different cookies that you want CloudFront to forward to the origin for this cache behavior. The value must equal the number of items that are in the Items field.
When you set Forward = whitelist (in the CookiePreferences object), this value must be 1 or higher.

Items (list) --
A complex type that contains one Name element for each cookie that you want CloudFront to forward to the origin for this cache behavior. It must contain the same number of items that is specified in the Quantity field.
When you set Forward = whitelist (in the CookiePreferences object), this field must contain at least one item.

(string) --






Headers (dict) --
A complex type that specifies the Headers , if any, that you want CloudFront to forward to the origin for this cache behavior (whitelisted headers). For the headers that you specify, CloudFront also caches separate versions of a specified object that is based on the header values in viewer requests.
For more information, see Caching Content Based on Request Headers in the Amazon CloudFront Developer Guide .

Quantity (integer) --
The number of different headers that you want CloudFront to base caching on for this cache behavior. You can configure each cache behavior in a web distribution to do one of the following:

Forward all headers to your origin : Specify 1 for Quantity and * for Name .


Warning
CloudFront doesn\'t cache the objects that are associated with this cache behavior. Instead, CloudFront sends every request to the origin.


Forward a whitelist of headers you specify : Specify the number of headers that you want CloudFront to base caching on. Then specify the header names in Name elements. CloudFront caches your objects based on the values in the specified headers.
Forward only the default headers : Specify 0 for Quantity and omit Items . In this configuration, CloudFront doesn\'t cache based on the values in the request headers.

Regardless of which option you choose, CloudFront forwards headers to your origin based on whether the origin is an S3 bucket or a custom origin. See the following documentation:

S3 bucket : See HTTP Request Headers That CloudFront Removes or Updates
Custom origin : See HTTP Request Headers and CloudFront Behavior


Items (list) --
A list that contains one Name element for each header that you want CloudFront to use for caching in this cache behavior. If Quantity is 0 , omit Items .

(string) --




QueryStringCacheKeys (dict) --
A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.

Quantity (integer) --
The number of whitelisted query string parameters for a cache behavior.

Items (list) --
A list that contains the query string parameters that you want CloudFront to use as a basis for caching for a cache behavior. If Quantity is 0, you can omit Items .

(string) --






TrustedSigners (dict) --
A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content.
If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled , and specify the applicable values for Quantity and Items . For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .
If you don\'t want to require signed URLs in requests for objects that match PathPattern , specify false for Enabled and 0 for Quantity . Omit Items .
To add, change, or remove one or more trusted signers, change Enabled to true (if it\'s currently false ), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.

Enabled (boolean) --
Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .

Quantity (integer) --
The number of trusted signers for this cache behavior.

Items (list) --

Optional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .


(string) --




ViewerProtocolPolicy (string) --
The protocol that viewers can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern . You can specify the following options:

allow-all : Viewers can use HTTP or HTTPS.
redirect-to-https : If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.
https-only : If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).

For more information about requiring the HTTPS protocol, see Using an HTTPS Connection to Access Your Objects in the Amazon CloudFront Developer Guide .

Note
The only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects\' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .


MinTTL (integer) --
The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .
You must specify 0 for MinTTL if you configure CloudFront to forward all headers to your origin (under Headers , if you specify 1 for Quantity and * for Name ).

AllowedMethods (dict) --
A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices:

CloudFront forwards only GET and HEAD requests.
CloudFront forwards only GET , HEAD , and OPTIONS requests.
CloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests.

If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can\'t perform operations that you don\'t want them to. For example, you might not want users to have permissions to delete objects from your origin.

Quantity (integer) --
The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET , HEAD , and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests).

Items (list) --
A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.

(string) --


CachedMethods (dict) --
A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices:

CloudFront caches responses to GET and HEAD requests.
CloudFront caches responses to GET , HEAD , and OPTIONS requests.

If you pick the second choice for your Amazon S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers, and Origin headers for the responses to be cached correctly.

Quantity (integer) --
The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET , HEAD , and OPTIONS requests).

Items (list) --
A complex type that contains the HTTP methods that you want CloudFront to cache responses to.

(string) --






SmoothStreaming (boolean) --
Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true ; if not, specify false . If you specify true for SmoothStreaming , you can still distribute other content using this cache behavior if the content matches the value of PathPattern .

DefaultTTL (integer) --
The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .

MaxTTL (integer) --
The maximum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .

Compress (boolean) --
Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify true; if not, specify false. For more information, see Serving Compressed Files in the Amazon CloudFront Developer Guide .

LambdaFunctionAssociations (dict) --
A complex type that contains zero or more Lambda function associations for a cache behavior.

Quantity (integer) --
The number of Lambda function associations for this cache behavior.

Items (list) --

Optional : A complex type that contains LambdaFunctionAssociation items for this cache behavior. If Quantity is 0 , you can omit Items .


(dict) --
A complex type that contains a Lambda function association.

LambdaFunctionARN (string) --
The ARN of the Lambda function. You must specify the ARN of a function version; you can\'t specify a Lambda alias or $LATEST.

EventType (string) --
Specifies the event type that triggers a Lambda function invocation. You can specify the following values:

viewer-request : The function executes when CloudFront receives a request from a viewer and before it checks to see whether the requested object is in the edge cache.
origin-request : The function executes only when CloudFront forwards a request to your origin. When the requested object is in the edge cache, the function doesn\'t execute.
origin-response : The function executes after CloudFront receives a response from the origin and before it caches the object in the response. When the requested object is in the edge cache, the function doesn\'t execute.
viewer-response : The function executes before CloudFront returns the requested object to the viewer. The function executes regardless of whether the object was already in the edge cache. If the origin returns an HTTP status code other than HTTP 200 (OK), the function doesn\'t execute.


IncludeBody (boolean) --
A flag that allows a Lambda function to have read access to the body content. For more information, see Accessing the Request Body by Choosing the Include Body Option in the Amazon CloudFront Developer Guide.







FieldLevelEncryptionId (string) --
The value of ID for the field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data for a cache behavior or for the default cache behavior in your distribution.







CustomErrorResponses (dict) --
A complex type that contains zero or more CustomErrorResponses elements.

Quantity (integer) --
The number of HTTP status codes for which you want to specify a custom error page and/or a caching duration. If Quantity is 0 , you can omit Items .

Items (list) --
A complex type that contains a CustomErrorResponse element for each HTTP status code for which you want to specify a custom error page and/or a caching duration.

(dict) --
A complex type that controls:

Whether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.
How long CloudFront caches HTTP status codes in the 4xx and 5xx range.

For more information about custom error pages, see Customizing Error Responses in the Amazon CloudFront Developer Guide .

ErrorCode (integer) --
The HTTP status code for which you want to specify a custom error page and/or a caching duration.

ResponsePagePath (string) --
The path to the custom error page that you want CloudFront to return to a viewer when your origin returns the HTTP status code specified by ErrorCode , for example, /4xx-errors/403-forbidden.html . If you want to store your objects and your custom error pages in different locations, your distribution must include a cache behavior for which the following is true:

The value of PathPattern matches the path to your custom error messages. For example, suppose you saved custom error pages for 4xx errors in an Amazon S3 bucket in a directory named /4xx-errors . Your distribution must include a cache behavior for which the path pattern routes requests for your custom error pages to that location, for example, /4xx-errors/* .
The value of TargetOriginId specifies the value of the ID element for the origin that contains your custom error pages.

If you specify a value for ResponsePagePath , you must also specify a value for ResponseCode .
We recommend that you store custom error pages in an Amazon S3 bucket. If you store custom error pages on an HTTP server and the server starts to return 5xx errors, CloudFront can\'t get the files that you want to return to viewers because the origin server is unavailable.

ResponseCode (string) --
The HTTP status code that you want CloudFront to return to the viewer along with the custom error page. There are a variety of reasons that you might want CloudFront to return a status code different from the status code that your origin returned to CloudFront, for example:

Some Internet devices (some firewalls and corporate proxies, for example) intercept HTTP 4xx and 5xx and prevent the response from being returned to the viewer. If you substitute 200 , the response typically won\'t be intercepted.
If you don\'t care about distinguishing among different client errors or server errors, you can specify 400 or 500 as the ResponseCode for all 4xx or 5xx errors.
You might want to return a 200 status code (OK) and static website so your customers don\'t know that your website is down.

If you specify a value for ResponseCode , you must also specify a value for ResponsePagePath .

ErrorCachingMinTTL (integer) --
The minimum amount of time, in seconds, that you want CloudFront to cache the HTTP status code specified in ErrorCode . When this time period has elapsed, CloudFront queries your origin to see whether the problem that caused the error has been resolved and the requested object is now available.
For more information, see Customizing Error Responses in the Amazon CloudFront Developer Guide .







Comment (string) --
The comment originally specified when this distribution was created.

PriceClass (string) --
A complex type that contains information about price class for this streaming distribution.

Enabled (boolean) --
Whether the distribution is enabled to accept user requests for content.

ViewerCertificate (dict) --
A complex type that determines the distribution\xe2\x80\x99s SSL/TLS configuration for communicating with viewers.

CloudFrontDefaultCertificate (boolean) --
If the distribution uses the CloudFront domain name such as d111111abcdef8.cloudfront.net , set this field to true .
If the distribution uses Aliases (alternate domain names or CNAMEs), set this field to false and specify values for the following fields:

ACMCertificateArn or IAMCertificateId (specify a value for one, not both)
MinimumProtocolVersion
SSLSupportMethod


IAMCertificateId (string) --
If the distribution uses Aliases (alternate domain names or CNAMEs) and the SSL/TLS certificate is stored in AWS Identity and Access Management (AWS IAM) , provide the ID of the IAM certificate.
If you specify an IAM certificate ID, you must also specify values for MinimumProtocolVerison and SSLSupportMethod .

ACMCertificateArn (string) --
If the distribution uses Aliases (alternate domain names or CNAMEs) and the SSL/TLS certificate is stored in AWS Certificate Manager (ACM) , provide the Amazon Resource Name (ARN) of the ACM certificate. CloudFront only supports ACM certificates in the US East (N. Virginia) Region (us-east-1 ).
If you specify an ACM certificate ARN, you must also specify values for MinimumProtocolVerison and SSLSupportMethod .

SSLSupportMethod (string) --
If the distribution uses Aliases (alternate domain names or CNAMEs), specify which viewers the distribution accepts HTTPS connections from.

sni-only \xe2\x80\x93 The distribution accepts HTTPS connections from only viewers that support server name indication (SNI) . This is recommended. Most browsers and clients released after 2010 support SNI.
vip \xe2\x80\x93 The distribution accepts HTTPS connections from all viewers including those that don\xe2\x80\x99t support SNI. This is not recommended, and results in additional monthly charges from CloudFront.

If the distribution uses the CloudFront domain name such as d111111abcdef8.cloudfront.net , don\xe2\x80\x99t set a value for this field.

MinimumProtocolVersion (string) --
If the distribution uses Aliases (alternate domain names or CNAMEs), specify the security policy that you want CloudFront to use for HTTPS connections with viewers. The security policy determines two settings:

The minimum SSL/TLS protocol that CloudFront can use to communicate with viewers.
The ciphers that CloudFront can use to encrypt the content that it returns to viewers.

For more information, see Security Policy and Supported Protocols and Ciphers Between Viewers and CloudFront in the Amazon CloudFront Developer Guide .

Note
On the CloudFront console, this setting is called Security Policy .

We recommend that you specify TLSv1.2_2018 unless your viewers are using browsers or devices that don\xe2\x80\x99t support TLSv1.2.
When you\xe2\x80\x99re using SNI only (you set SSLSupportMethod to sni-only ), you must specify TLSv1 or higher.
If the distribution uses the CloudFront domain name such as d111111abcdef8.cloudfront.net (you set CloudFrontDefaultCertificate to true ), CloudFront automatically sets the security policy to TLSv1 regardless of the value that you set here.

Certificate (string) --
This field is deprecated. Use one of the following fields instead:

ACMCertificateArn
IAMCertificateId
CloudFrontDefaultCertificate


CertificateSource (string) --
This field is deprecated. Use one of the following fields instead:

ACMCertificateArn
IAMCertificateId
CloudFrontDefaultCertificate




Restrictions (dict) --
A complex type that identifies ways in which you want to restrict distribution of your content.

GeoRestriction (dict) --
A complex type that controls the countries in which your content is distributed. CloudFront determines the location of your users using MaxMind GeoIP databases.

RestrictionType (string) --
The method that you want to use to restrict distribution of your content by country:

none : No geo restriction is enabled, meaning access to content is not restricted by client geo location.
blacklist : The Location elements specify the countries in which you don\'t want CloudFront to distribute your content.
whitelist : The Location elements specify the countries in which you want CloudFront to distribute your content.


Quantity (integer) --
When geo restriction is enabled , this is the number of countries in your whitelist or blacklist . Otherwise, when it is not enabled, Quantity is 0 , and you can omit Items .

Items (list) --
A complex type that contains a Location element for each country in which you want CloudFront either to distribute your content (whitelist ) or not distribute your content (blacklist ).
The Location element is a two-letter, uppercase country code for a country that you want to include in your blacklist or whitelist . Include one Location element for each country.
CloudFront and MaxMind both use ISO 3166 country codes. For the current list of countries and the corresponding codes, see ISO 3166-1-alpha-2 code on the International Organization for Standardization website. You can also refer to the country list on the CloudFront console, which includes both country names and codes.

(string) --






WebACLId (string) --
The Web ACL Id (if any) associated with the distribution.

HttpVersion (string) --
Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront. The default value for new web distributions is http2 . Viewers that don\'t support HTTP/2 will automatically use an earlier version.

IsIPV6Enabled (boolean) --
Whether CloudFront responds to IPv6 DNS requests with an IPv6 address for your distribution.

AliasICPRecordals (list) --
AWS services in China customers must file for an Internet Content Provider (ICP) recordal if they want to serve content publicly on an alternate domain name, also known as a CNAME, that they\'ve added to CloudFront. AliasICPRecordal provides the ICP recordal status for CNAMEs associated with distributions.
For more information about ICP recordals, see Signup, Accounts, and Credentials in Getting Started with AWS services in China .

(dict) --
AWS services in China customers must file for an Internet Content Provider (ICP) recordal if they want to serve content publicly on an alternate domain name, also known as a CNAME, that they\'ve added to CloudFront. AliasICPRecordal provides the ICP recordal status for CNAMEs associated with distributions. The status is returned in the CloudFront response; you can\'t configure it yourself.
For more information about ICP recordals, see Signup, Accounts, and Credentials in Getting Started with AWS services in China .

CNAME (string) --
A domain name associated with a distribution.

ICPRecordalStatus (string) --
The Internet Content Provider (ICP) recordal status for a CNAME. The ICPRecordalStatus is set to APPROVED for all CNAMEs (aliases) in regions outside of China.
The status values returned are the following:

APPROVED indicates that the associated CNAME has a valid ICP recordal number. Multiple CNAMEs can be associated with a distribution, and CNAMEs can correspond to different ICP recordals. To be marked as APPROVED, that is, valid to use with China region, a CNAME must have one ICP recordal number associated with it.
SUSPENDED indicates that the associated CNAME does not have a valid ICP recordal number.
PENDING indicates that CloudFront can\'t determine the ICP recordal status of the CNAME associated with the distribution because there was an error in trying to determine the status. You can try again to see if the error is resolved in which case CloudFront returns an APPROVED or SUSPENDED status.


















Exceptions

CloudFront.Client.exceptions.InvalidArgument
CloudFront.Client.exceptions.InvalidWebACLId


    :return: {
        'DistributionList': {
            'Marker': 'string',
            'NextMarker': 'string',
            'MaxItems': 123,
            'IsTruncated': True|False,
            'Quantity': 123,
            'Items': [
                {
                    'Id': 'string',
                    'ARN': 'string',
                    'Status': 'string',
                    'LastModifiedTime': datetime(2015, 1, 1),
                    'DomainName': 'string',
                    'Aliases': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    },
                    'Origins': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'Id': 'string',
                                'DomainName': 'string',
                                'OriginPath': 'string',
                                'CustomHeaders': {
                                    'Quantity': 123,
                                    'Items': [
                                        {
                                            'HeaderName': 'string',
                                            'HeaderValue': 'string'
                                        },
                                    ]
                                },
                                'S3OriginConfig': {
                                    'OriginAccessIdentity': 'string'
                                },
                                'CustomOriginConfig': {
                                    'HTTPPort': 123,
                                    'HTTPSPort': 123,
                                    'OriginProtocolPolicy': 'http-only'|'match-viewer'|'https-only',
                                    'OriginSslProtocols': {
                                        'Quantity': 123,
                                        'Items': [
                                            'SSLv3'|'TLSv1'|'TLSv1.1'|'TLSv1.2',
                                        ]
                                    },
                                    'OriginReadTimeout': 123,
                                    'OriginKeepaliveTimeout': 123
                                }
                            },
                        ]
                    },
                    'OriginGroups': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'Id': 'string',
                                'FailoverCriteria': {
                                    'StatusCodes': {
                                        'Quantity': 123,
                                        'Items': [
                                            123,
                                        ]
                                    }
                                },
                                'Members': {
                                    'Quantity': 123,
                                    'Items': [
                                        {
                                            'OriginId': 'string'
                                        },
                                    ]
                                }
                            },
                        ]
                    },
                    'DefaultCacheBehavior': {
                        'TargetOriginId': 'string',
                        'ForwardedValues': {
                            'QueryString': True|False,
                            'Cookies': {
                                'Forward': 'none'|'whitelist'|'all',
                                'WhitelistedNames': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                }
                            },
                            'Headers': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            },
                            'QueryStringCacheKeys': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                        'TrustedSigners': {
                            'Enabled': True|False,
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        },
                        'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                        'MinTTL': 123,
                        'AllowedMethods': {
                            'Quantity': 123,
                            'Items': [
                                'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                            ],
                            'CachedMethods': {
                                'Quantity': 123,
                                'Items': [
                                    'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                ]
                            }
                        },
                        'SmoothStreaming': True|False,
                        'DefaultTTL': 123,
                        'MaxTTL': 123,
                        'Compress': True|False,
                        'LambdaFunctionAssociations': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'LambdaFunctionARN': 'string',
                                    'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                    'IncludeBody': True|False
                                },
                            ]
                        },
                        'FieldLevelEncryptionId': 'string'
                    },
                    'CacheBehaviors': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'PathPattern': 'string',
                                'TargetOriginId': 'string',
                                'ForwardedValues': {
                                    'QueryString': True|False,
                                    'Cookies': {
                                        'Forward': 'none'|'whitelist'|'all',
                                        'WhitelistedNames': {
                                            'Quantity': 123,
                                            'Items': [
                                                'string',
                                            ]
                                        }
                                    },
                                    'Headers': {
                                        'Quantity': 123,
                                        'Items': [
                                            'string',
                                        ]
                                    },
                                    'QueryStringCacheKeys': {
                                        'Quantity': 123,
                                        'Items': [
                                            'string',
                                        ]
                                    }
                                },
                                'TrustedSigners': {
                                    'Enabled': True|False,
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                },
                                'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                                'MinTTL': 123,
                                'AllowedMethods': {
                                    'Quantity': 123,
                                    'Items': [
                                        'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                    ],
                                    'CachedMethods': {
                                        'Quantity': 123,
                                        'Items': [
                                            'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                        ]
                                    }
                                },
                                'SmoothStreaming': True|False,
                                'DefaultTTL': 123,
                                'MaxTTL': 123,
                                'Compress': True|False,
                                'LambdaFunctionAssociations': {
                                    'Quantity': 123,
                                    'Items': [
                                        {
                                            'LambdaFunctionARN': 'string',
                                            'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                            'IncludeBody': True|False
                                        },
                                    ]
                                },
                                'FieldLevelEncryptionId': 'string'
                            },
                        ]
                    },
                    'CustomErrorResponses': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'ErrorCode': 123,
                                'ResponsePagePath': 'string',
                                'ResponseCode': 'string',
                                'ErrorCachingMinTTL': 123
                            },
                        ]
                    },
                    'Comment': 'string',
                    'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
                    'Enabled': True|False,
                    'ViewerCertificate': {
                        'CloudFrontDefaultCertificate': True|False,
                        'IAMCertificateId': 'string',
                        'ACMCertificateArn': 'string',
                        'SSLSupportMethod': 'sni-only'|'vip',
                        'MinimumProtocolVersion': 'SSLv3'|'TLSv1'|'TLSv1_2016'|'TLSv1.1_2016'|'TLSv1.2_2018',
                        'Certificate': 'string',
                        'CertificateSource': 'cloudfront'|'iam'|'acm'
                    },
                    'Restrictions': {
                        'GeoRestriction': {
                            'RestrictionType': 'blacklist'|'whitelist'|'none',
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                    'WebACLId': 'string',
                    'HttpVersion': 'http1.1'|'http2',
                    'IsIPV6Enabled': True|False,
                    'AliasICPRecordals': [
                        {
                            'CNAME': 'string',
                            'ICPRecordalStatus': 'APPROVED'|'SUSPENDED'|'PENDING'
                        },
                    ]
                },
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_field_level_encryption_configs(Marker=None, MaxItems=None):
    """
    List all field-level encryption configurations that have been created in CloudFront for this account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_field_level_encryption_configs(
        Marker='string',
        MaxItems='string'
    )
    
    
    :type Marker: string
    :param Marker: Use this when paginating results to indicate where to begin in your list of configurations. The results include configurations in the list that occur after the marker. To get the next page of results, set the Marker to the value of the NextMarker from the current page\'s response (which is also the ID of the last configuration on that page).

    :type MaxItems: string
    :param MaxItems: The maximum number of field-level encryption configurations you want in the response body.

    :rtype: dict

ReturnsResponse Syntax
{
    'FieldLevelEncryptionList': {
        'NextMarker': 'string',
        'MaxItems': 123,
        'Quantity': 123,
        'Items': [
            {
                'Id': 'string',
                'LastModifiedTime': datetime(2015, 1, 1),
                'Comment': 'string',
                'QueryArgProfileConfig': {
                    'ForwardWhenQueryArgProfileIsUnknown': True|False,
                    'QueryArgProfiles': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'QueryArg': 'string',
                                'ProfileId': 'string'
                            },
                        ]
                    }
                },
                'ContentTypeProfileConfig': {
                    'ForwardWhenContentTypeIsUnknown': True|False,
                    'ContentTypeProfiles': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'Format': 'URLEncoded',
                                'ProfileId': 'string',
                                'ContentType': 'string'
                            },
                        ]
                    }
                }
            },
        ]
    }
}


Response Structure

(dict) --

FieldLevelEncryptionList (dict) --
Returns a list of all field-level encryption configurations that have been created in CloudFront for this account.

NextMarker (string) --
If there are more elements to be listed, this element is present and contains the value that you can use for the Marker request parameter to continue listing your configurations where you left off.

MaxItems (integer) --
The maximum number of elements you want in the response body.

Quantity (integer) --
The number of field-level encryption items.

Items (list) --
An array of field-level encryption items.

(dict) --
A summary of a field-level encryption item.

Id (string) --
The unique ID of a field-level encryption item.

LastModifiedTime (datetime) --
The last time that the summary of field-level encryption items was modified.

Comment (string) --
An optional comment about the field-level encryption item.

QueryArgProfileConfig (dict) --
A summary of a query argument-profile mapping.

ForwardWhenQueryArgProfileIsUnknown (boolean) --
Flag to set if you want a request to be forwarded to the origin even if the profile specified by the field-level encryption query argument, fle-profile, is unknown.

QueryArgProfiles (dict) --
Profiles specified for query argument-profile mapping for field-level encryption.

Quantity (integer) --
Number of profiles for query argument-profile mapping for field-level encryption.

Items (list) --
Number of items for query argument-profile mapping for field-level encryption.

(dict) --
Query argument-profile mapping for field-level encryption.

QueryArg (string) --
Query argument for field-level encryption query argument-profile mapping.

ProfileId (string) --
ID of profile to use for field-level encryption query argument-profile mapping









ContentTypeProfileConfig (dict) --
A summary of a content type-profile mapping.

ForwardWhenContentTypeIsUnknown (boolean) --
The setting in a field-level encryption content type-profile mapping that specifies what to do when an unknown content type is provided for the profile. If true, content is forwarded without being encrypted when the content type is unknown. If false (the default), an error is returned when the content type is unknown.

ContentTypeProfiles (dict) --
The configuration for a field-level encryption content type-profile.

Quantity (integer) --
The number of field-level encryption content type-profile mappings.

Items (list) --
Items in a field-level encryption content type-profile mapping.

(dict) --
A field-level encryption content type profile.

Format (string) --
The format for a field-level encryption content type-profile mapping.

ProfileId (string) --
The profile ID for a field-level encryption content type-profile mapping.

ContentType (string) --
The content type for a field-level encryption content type-profile mapping.





















Exceptions

CloudFront.Client.exceptions.InvalidArgument


    :return: {
        'FieldLevelEncryptionList': {
            'NextMarker': 'string',
            'MaxItems': 123,
            'Quantity': 123,
            'Items': [
                {
                    'Id': 'string',
                    'LastModifiedTime': datetime(2015, 1, 1),
                    'Comment': 'string',
                    'QueryArgProfileConfig': {
                        'ForwardWhenQueryArgProfileIsUnknown': True|False,
                        'QueryArgProfiles': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'QueryArg': 'string',
                                    'ProfileId': 'string'
                                },
                            ]
                        }
                    },
                    'ContentTypeProfileConfig': {
                        'ForwardWhenContentTypeIsUnknown': True|False,
                        'ContentTypeProfiles': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'Format': 'URLEncoded',
                                    'ProfileId': 'string',
                                    'ContentType': 'string'
                                },
                            ]
                        }
                    }
                },
            ]
        }
    }
    
    
    :returns: 
    CloudFront.Client.exceptions.InvalidArgument
    
    """
    pass

def list_field_level_encryption_profiles(Marker=None, MaxItems=None):
    """
    Request a list of field-level encryption profiles that have been created in CloudFront for this account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_field_level_encryption_profiles(
        Marker='string',
        MaxItems='string'
    )
    
    
    :type Marker: string
    :param Marker: Use this when paginating results to indicate where to begin in your list of profiles. The results include profiles in the list that occur after the marker. To get the next page of results, set the Marker to the value of the NextMarker from the current page\'s response (which is also the ID of the last profile on that page).

    :type MaxItems: string
    :param MaxItems: The maximum number of field-level encryption profiles you want in the response body.

    :rtype: dict

ReturnsResponse Syntax
{
    'FieldLevelEncryptionProfileList': {
        'NextMarker': 'string',
        'MaxItems': 123,
        'Quantity': 123,
        'Items': [
            {
                'Id': 'string',
                'LastModifiedTime': datetime(2015, 1, 1),
                'Name': 'string',
                'EncryptionEntities': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'PublicKeyId': 'string',
                            'ProviderId': 'string',
                            'FieldPatterns': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                    ]
                },
                'Comment': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

FieldLevelEncryptionProfileList (dict) --
Returns a list of the field-level encryption profiles that have been created in CloudFront for this account.

NextMarker (string) --
If there are more elements to be listed, this element is present and contains the value that you can use for the Marker request parameter to continue listing your profiles where you left off.

MaxItems (integer) --
The maximum number of field-level encryption profiles you want in the response body.

Quantity (integer) --
The number of field-level encryption profiles.

Items (list) --
The field-level encryption profile items.

(dict) --
The field-level encryption profile summary.

Id (string) --
ID for the field-level encryption profile summary.

LastModifiedTime (datetime) --
The time when the the field-level encryption profile summary was last updated.

Name (string) --
Name for the field-level encryption profile summary.

EncryptionEntities (dict) --
A complex data type of encryption entities for the field-level encryption profile that include the public key ID, provider, and field patterns for specifying which fields to encrypt with this key.

Quantity (integer) --
Number of field pattern items in a field-level encryption content type-profile mapping.

Items (list) --
An array of field patterns in a field-level encryption content type-profile mapping.

(dict) --
Complex data type for field-level encryption profiles that includes the encryption key and field pattern specifications.

PublicKeyId (string) --
The public key associated with a set of field-level encryption patterns, to be used when encrypting the fields that match the patterns.

ProviderId (string) --
The provider associated with the public key being used for encryption. This value must also be provided with the private key for applications to be able to decrypt data.

FieldPatterns (dict) --
Field patterns in a field-level encryption content type profile specify the fields that you want to be encrypted. You can provide the full field name, or any beginning characters followed by a wildcard (*). You can\'t overlap field patterns. For example, you can\'t have both ABC* and AB*. Note that field patterns are case-sensitive.

Quantity (integer) --
The number of field-level encryption field patterns.

Items (list) --
An array of the field-level encryption field patterns.

(string) --










Comment (string) --
An optional comment for the field-level encryption profile summary.













Exceptions

CloudFront.Client.exceptions.InvalidArgument


    :return: {
        'FieldLevelEncryptionProfileList': {
            'NextMarker': 'string',
            'MaxItems': 123,
            'Quantity': 123,
            'Items': [
                {
                    'Id': 'string',
                    'LastModifiedTime': datetime(2015, 1, 1),
                    'Name': 'string',
                    'EncryptionEntities': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'PublicKeyId': 'string',
                                'ProviderId': 'string',
                                'FieldPatterns': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                }
                            },
                        ]
                    },
                    'Comment': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_invalidations(DistributionId=None, Marker=None, MaxItems=None):
    """
    Lists invalidation batches.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_invalidations(
        DistributionId='string',
        Marker='string',
        MaxItems='string'
    )
    
    
    :type DistributionId: string
    :param DistributionId: [REQUIRED]\nThe distribution\'s ID.\n

    :type Marker: string
    :param Marker: Use this parameter when paginating results to indicate where to begin in your list of invalidation batches. Because the results are returned in decreasing order from most recent to oldest, the most recent results are on the first page, the second page will contain earlier results, and so on. To get the next page of results, set Marker to the value of the NextMarker from the current page\'s response. This value is the same as the ID of the last invalidation batch on that page.

    :type MaxItems: string
    :param MaxItems: The maximum number of invalidation batches that you want in the response body.

    :rtype: dict

ReturnsResponse Syntax
{
    'InvalidationList': {
        'Marker': 'string',
        'NextMarker': 'string',
        'MaxItems': 123,
        'IsTruncated': True|False,
        'Quantity': 123,
        'Items': [
            {
                'Id': 'string',
                'CreateTime': datetime(2015, 1, 1),
                'Status': 'string'
            },
        ]
    }
}


Response Structure

(dict) --
The returned result of the corresponding request.

InvalidationList (dict) --
Information about invalidation batches.

Marker (string) --
The value that you provided for the Marker request parameter.

NextMarker (string) --
If IsTruncated is true , this element is present and contains the value that you can use for the Marker request parameter to continue listing your invalidation batches where they left off.

MaxItems (integer) --
The value that you provided for the MaxItems request parameter.

IsTruncated (boolean) --
A flag that indicates whether more invalidation batch requests remain to be listed. If your results were truncated, you can make a follow-up pagination request using the Marker request parameter to retrieve more invalidation batches in the list.

Quantity (integer) --
The number of invalidation batches that were created by the current AWS account.

Items (list) --
A complex type that contains one InvalidationSummary element for each invalidation batch created by the current AWS account.

(dict) --
A summary of an invalidation request.

Id (string) --
The unique ID for an invalidation request.

CreateTime (datetime) --
The time that an invalidation request was created.

Status (string) --
The status of an invalidation request.













Exceptions

CloudFront.Client.exceptions.InvalidArgument
CloudFront.Client.exceptions.NoSuchDistribution
CloudFront.Client.exceptions.AccessDenied


    :return: {
        'InvalidationList': {
            'Marker': 'string',
            'NextMarker': 'string',
            'MaxItems': 123,
            'IsTruncated': True|False,
            'Quantity': 123,
            'Items': [
                {
                    'Id': 'string',
                    'CreateTime': datetime(2015, 1, 1),
                    'Status': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    CloudFront.Client.exceptions.InvalidArgument
    CloudFront.Client.exceptions.NoSuchDistribution
    CloudFront.Client.exceptions.AccessDenied
    
    """
    pass

def list_public_keys(Marker=None, MaxItems=None):
    """
    List all public keys that have been added to CloudFront for this account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_public_keys(
        Marker='string',
        MaxItems='string'
    )
    
    
    :type Marker: string
    :param Marker: Use this when paginating results to indicate where to begin in your list of public keys. The results include public keys in the list that occur after the marker. To get the next page of results, set the Marker to the value of the NextMarker from the current page\'s response (which is also the ID of the last public key on that page).

    :type MaxItems: string
    :param MaxItems: The maximum number of public keys you want in the response body.

    :rtype: dict

ReturnsResponse Syntax
{
    'PublicKeyList': {
        'NextMarker': 'string',
        'MaxItems': 123,
        'Quantity': 123,
        'Items': [
            {
                'Id': 'string',
                'Name': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'EncodedKey': 'string',
                'Comment': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

PublicKeyList (dict) --
Returns a list of all public keys that have been added to CloudFront for this account.

NextMarker (string) --
If there are more elements to be listed, this element is present and contains the value that you can use for the Marker request parameter to continue listing your public keys where you left off.

MaxItems (integer) --
The maximum number of public keys you want in the response body.

Quantity (integer) --
The number of public keys you added to CloudFront to use with features like field-level encryption.

Items (list) --
An array of information about a public key you add to CloudFront to use with features like field-level encryption.

(dict) --
A complex data type for public key information.

Id (string) --
ID for public key information summary.

Name (string) --
Name for public key information summary.

CreatedTime (datetime) --
Creation time for public key information summary.

EncodedKey (string) --
Encoded key for public key information summary.

Comment (string) --
Comment for public key information summary.













Exceptions

CloudFront.Client.exceptions.InvalidArgument


    :return: {
        'PublicKeyList': {
            'NextMarker': 'string',
            'MaxItems': 123,
            'Quantity': 123,
            'Items': [
                {
                    'Id': 'string',
                    'Name': 'string',
                    'CreatedTime': datetime(2015, 1, 1),
                    'EncodedKey': 'string',
                    'Comment': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    CloudFront.Client.exceptions.InvalidArgument
    
    """
    pass

def list_streaming_distributions(Marker=None, MaxItems=None):
    """
    List streaming distributions.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_streaming_distributions(
        Marker='string',
        MaxItems='string'
    )
    
    
    :type Marker: string
    :param Marker: The value that you provided for the Marker request parameter.

    :type MaxItems: string
    :param MaxItems: The value that you provided for the MaxItems request parameter.

    :rtype: dict

ReturnsResponse Syntax
{
    'StreamingDistributionList': {
        'Marker': 'string',
        'NextMarker': 'string',
        'MaxItems': 123,
        'IsTruncated': True|False,
        'Quantity': 123,
        'Items': [
            {
                'Id': 'string',
                'ARN': 'string',
                'Status': 'string',
                'LastModifiedTime': datetime(2015, 1, 1),
                'DomainName': 'string',
                'S3Origin': {
                    'DomainName': 'string',
                    'OriginAccessIdentity': 'string'
                },
                'Aliases': {
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'TrustedSigners': {
                    'Enabled': True|False,
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'Comment': 'string',
                'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
                'Enabled': True|False
            },
        ]
    }
}


Response Structure

(dict) --
The returned result of the corresponding request.

StreamingDistributionList (dict) --
The StreamingDistributionList type.

Marker (string) --
The value you provided for the Marker request parameter.

NextMarker (string) --
If IsTruncated is true , this element is present and contains the value you can use for the Marker request parameter to continue listing your RTMP distributions where they left off.

MaxItems (integer) --
The value you provided for the MaxItems request parameter.

IsTruncated (boolean) --
A flag that indicates whether more streaming distributions remain to be listed. If your results were truncated, you can make a follow-up pagination request using the Marker request parameter to retrieve more distributions in the list.

Quantity (integer) --
The number of streaming distributions that were created by the current AWS account.

Items (list) --
A complex type that contains one StreamingDistributionSummary element for each distribution that was created by the current AWS account.

(dict) --
A summary of the information for a CloudFront streaming distribution.

Id (string) --
The identifier for the distribution, for example, EDFDVBD632BHDS5 .

ARN (string) --
The ARN (Amazon Resource Name) for the streaming distribution. For example: arn:aws:cloudfront::123456789012:streaming-distribution/EDFDVBD632BHDS5 , where 123456789012 is your AWS account ID.

Status (string) --
Indicates the current status of the distribution. When the status is Deployed , the distribution\'s information is fully propagated throughout the Amazon CloudFront system.

LastModifiedTime (datetime) --
The date and time the distribution was last modified.

DomainName (string) --
The domain name corresponding to the distribution, for example, d111111abcdef8.cloudfront.net .

S3Origin (dict) --
A complex type that contains information about the Amazon S3 bucket from which you want CloudFront to get your media files for distribution.

DomainName (string) --
The DNS name of the Amazon S3 origin.

OriginAccessIdentity (string) --
The CloudFront origin access identity to associate with the distribution. Use an origin access identity to configure the distribution so that end users can only access objects in an Amazon S3 bucket through CloudFront.
If you want end users to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty OriginAccessIdentity element.
To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty OriginAccessIdentity element.
To replace the origin access identity, update the distribution configuration and specify the new origin access identity.
For more information, see Using an Origin Access Identity to Restrict Access to Your Amazon S3 Content in the Amazon CloudFront Developer Guide .



Aliases (dict) --
A complex type that contains information about CNAMEs (alternate domain names), if any, for this streaming distribution.

Quantity (integer) --
The number of CNAME aliases, if any, that you want to associate with this distribution.

Items (list) --
A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.

(string) --




TrustedSigners (dict) --
A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content. If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled , and specify the applicable values for Quantity and Items .If you don\'t want to require signed URLs in requests for objects that match PathPattern , specify false for Enabled and 0 for Quantity . Omit Items . To add, change, or remove one or more trusted signers, change Enabled to true (if it\'s currently false ), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.
For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .

Enabled (boolean) --
Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .

Quantity (integer) --
The number of trusted signers for this cache behavior.

Items (list) --

Optional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .


(string) --




Comment (string) --
The comment originally specified when this distribution was created.

PriceClass (string) --
A complex type that contains information about price class for this streaming distribution.

Enabled (boolean) --
Whether the distribution is enabled to accept end user requests for content.













Exceptions

CloudFront.Client.exceptions.InvalidArgument


    :return: {
        'StreamingDistributionList': {
            'Marker': 'string',
            'NextMarker': 'string',
            'MaxItems': 123,
            'IsTruncated': True|False,
            'Quantity': 123,
            'Items': [
                {
                    'Id': 'string',
                    'ARN': 'string',
                    'Status': 'string',
                    'LastModifiedTime': datetime(2015, 1, 1),
                    'DomainName': 'string',
                    'S3Origin': {
                        'DomainName': 'string',
                        'OriginAccessIdentity': 'string'
                    },
                    'Aliases': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    },
                    'TrustedSigners': {
                        'Enabled': True|False,
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    },
                    'Comment': 'string',
                    'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
                    'Enabled': True|False
                },
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_tags_for_resource(Resource=None):
    """
    List tags for a CloudFront resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        Resource='string'
    )
    
    
    :type Resource: string
    :param Resource: [REQUIRED]\nAn ARN of a CloudFront resource.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Tags': {
        'Items': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --The returned result of the corresponding request.

Tags (dict) --A complex type that contains zero or more Tag elements.

Items (list) --A complex type that contains Tag elements.

(dict) --A complex type that contains Tag key and Tag value.

Key (string) --A string that contains Tag key.
The string length should be between 1 and 128 characters. Valid characters include a-z , A-Z , 0-9 , space, and the special characters _ - . : / = + @ .

Value (string) --A string that contains an optional Tag value.
The string length should be between 0 and 256 characters. Valid characters include a-z , A-Z , 0-9 , space, and the special characters _ - . : / = + @ .












Exceptions

CloudFront.Client.exceptions.AccessDenied
CloudFront.Client.exceptions.InvalidArgument
CloudFront.Client.exceptions.InvalidTagging
CloudFront.Client.exceptions.NoSuchResource


    :return: {
        'Tags': {
            'Items': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def tag_resource(Resource=None, Tags=None):
    """
    Add tags to a CloudFront resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        Resource='string',
        Tags={
            'Items': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    )
    
    
    :type Resource: string
    :param Resource: [REQUIRED]\nAn ARN of a CloudFront resource.\n

    :type Tags: dict
    :param Tags: [REQUIRED]\nA complex type that contains zero or more Tag elements.\n\nItems (list) --A complex type that contains Tag elements.\n\n(dict) --A complex type that contains Tag key and Tag value.\n\nKey (string) -- [REQUIRED]A string that contains Tag key.\nThe string length should be between 1 and 128 characters. Valid characters include a-z , A-Z , 0-9 , space, and the special characters _ - . : / = + @ .\n\nValue (string) --A string that contains an optional Tag value.\nThe string length should be between 0 and 256 characters. Valid characters include a-z , A-Z , 0-9 , space, and the special characters _ - . : / = + @ .\n\n\n\n\n\n\n

    :returns: 
    CloudFront.Client.exceptions.AccessDenied
    CloudFront.Client.exceptions.InvalidArgument
    CloudFront.Client.exceptions.InvalidTagging
    CloudFront.Client.exceptions.NoSuchResource
    
    """
    pass

def untag_resource(Resource=None, TagKeys=None):
    """
    Remove tags from a CloudFront resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        Resource='string',
        TagKeys={
            'Items': [
                'string',
            ]
        }
    )
    
    
    :type Resource: string
    :param Resource: [REQUIRED]\nAn ARN of a CloudFront resource.\n

    :type TagKeys: dict
    :param TagKeys: [REQUIRED]\nA complex type that contains zero or more Tag key elements.\n\nItems (list) --A complex type that contains Tag key elements.\n\n(string) --A string that contains Tag key.\nThe string length should be between 1 and 128 characters. Valid characters include a-z , A-Z , 0-9 , space, and the special characters _ - . : / = + @ .\n\n\n\n\n

    :returns: 
    CloudFront.Client.exceptions.AccessDenied
    CloudFront.Client.exceptions.InvalidArgument
    CloudFront.Client.exceptions.InvalidTagging
    CloudFront.Client.exceptions.NoSuchResource
    
    """
    pass

def update_cloud_front_origin_access_identity(CloudFrontOriginAccessIdentityConfig=None, Id=None, IfMatch=None):
    """
    Update an origin access identity.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_cloud_front_origin_access_identity(
        CloudFrontOriginAccessIdentityConfig={
            'CallerReference': 'string',
            'Comment': 'string'
        },
        Id='string',
        IfMatch='string'
    )
    
    
    :type CloudFrontOriginAccessIdentityConfig: dict
    :param CloudFrontOriginAccessIdentityConfig: [REQUIRED]\nThe identity\'s configuration information.\n\nCallerReference (string) -- [REQUIRED]A unique value (for example, a date-time stamp) that ensures that the request can\'t be replayed.\nIf the value of CallerReference is new (regardless of the content of the CloudFrontOriginAccessIdentityConfig object), a new origin access identity is created.\nIf the CallerReference is a value already sent in a previous identity request, and the content of the CloudFrontOriginAccessIdentityConfig is identical to the original request (ignoring white space), the response includes the same information returned to the original request.\nIf the CallerReference is a value you already sent in a previous request to create an identity, but the content of the CloudFrontOriginAccessIdentityConfig is different from the original request, CloudFront returns a CloudFrontOriginAccessIdentityAlreadyExists error.\n\nComment (string) -- [REQUIRED]Any comments you want to include about the origin access identity.\n\n\n

    :type Id: string
    :param Id: [REQUIRED]\nThe identity\'s id.\n

    :type IfMatch: string
    :param IfMatch: The value of the ETag header that you received when retrieving the identity\'s configuration. For example: E2QWRUHAPOMQZL .

    :rtype: dict

ReturnsResponse Syntax
{
    'CloudFrontOriginAccessIdentity': {
        'Id': 'string',
        'S3CanonicalUserId': 'string',
        'CloudFrontOriginAccessIdentityConfig': {
            'CallerReference': 'string',
            'Comment': 'string'
        }
    },
    'ETag': 'string'
}


Response Structure

(dict) --
The returned result of the corresponding request.

CloudFrontOriginAccessIdentity (dict) --
The origin access identity\'s information.

Id (string) --
The ID for the origin access identity, for example, E74FTE3AJFJ256A .

S3CanonicalUserId (string) --
The Amazon S3 canonical user ID for the origin access identity, used when giving the origin access identity read permission to an object in Amazon S3.

CloudFrontOriginAccessIdentityConfig (dict) --
The current configuration information for the identity.

CallerReference (string) --
A unique value (for example, a date-time stamp) that ensures that the request can\'t be replayed.
If the value of CallerReference is new (regardless of the content of the CloudFrontOriginAccessIdentityConfig object), a new origin access identity is created.
If the CallerReference is a value already sent in a previous identity request, and the content of the CloudFrontOriginAccessIdentityConfig is identical to the original request (ignoring white space), the response includes the same information returned to the original request.
If the CallerReference is a value you already sent in a previous request to create an identity, but the content of the CloudFrontOriginAccessIdentityConfig is different from the original request, CloudFront returns a CloudFrontOriginAccessIdentityAlreadyExists error.

Comment (string) --
Any comments you want to include about the origin access identity.





ETag (string) --
The current version of the configuration. For example: E2QWRUHAPOMQZL .







Exceptions

CloudFront.Client.exceptions.AccessDenied
CloudFront.Client.exceptions.IllegalUpdate
CloudFront.Client.exceptions.InvalidIfMatchVersion
CloudFront.Client.exceptions.MissingBody
CloudFront.Client.exceptions.NoSuchCloudFrontOriginAccessIdentity
CloudFront.Client.exceptions.PreconditionFailed
CloudFront.Client.exceptions.InvalidArgument
CloudFront.Client.exceptions.InconsistentQuantities


    :return: {
        'CloudFrontOriginAccessIdentity': {
            'Id': 'string',
            'S3CanonicalUserId': 'string',
            'CloudFrontOriginAccessIdentityConfig': {
                'CallerReference': 'string',
                'Comment': 'string'
            }
        },
        'ETag': 'string'
    }
    
    
    :returns: 
    CloudFront.Client.exceptions.AccessDenied
    CloudFront.Client.exceptions.IllegalUpdate
    CloudFront.Client.exceptions.InvalidIfMatchVersion
    CloudFront.Client.exceptions.MissingBody
    CloudFront.Client.exceptions.NoSuchCloudFrontOriginAccessIdentity
    CloudFront.Client.exceptions.PreconditionFailed
    CloudFront.Client.exceptions.InvalidArgument
    CloudFront.Client.exceptions.InconsistentQuantities
    
    """
    pass

def update_distribution(DistributionConfig=None, Id=None, IfMatch=None):
    """
    Updates the configuration for a web distribution.
    The update process includes getting the current distribution configuration, updating the XML document that is returned to make your changes, and then submitting an UpdateDistribution request to make the updates.
    For information about updating a distribution using the CloudFront console instead, see Creating a Distribution in the Amazon CloudFront Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_distribution(
        DistributionConfig={
            'CallerReference': 'string',
            'Aliases': {
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'DefaultRootObject': 'string',
            'Origins': {
                'Quantity': 123,
                'Items': [
                    {
                        'Id': 'string',
                        'DomainName': 'string',
                        'OriginPath': 'string',
                        'CustomHeaders': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'HeaderName': 'string',
                                    'HeaderValue': 'string'
                                },
                            ]
                        },
                        'S3OriginConfig': {
                            'OriginAccessIdentity': 'string'
                        },
                        'CustomOriginConfig': {
                            'HTTPPort': 123,
                            'HTTPSPort': 123,
                            'OriginProtocolPolicy': 'http-only'|'match-viewer'|'https-only',
                            'OriginSslProtocols': {
                                'Quantity': 123,
                                'Items': [
                                    'SSLv3'|'TLSv1'|'TLSv1.1'|'TLSv1.2',
                                ]
                            },
                            'OriginReadTimeout': 123,
                            'OriginKeepaliveTimeout': 123
                        }
                    },
                ]
            },
            'OriginGroups': {
                'Quantity': 123,
                'Items': [
                    {
                        'Id': 'string',
                        'FailoverCriteria': {
                            'StatusCodes': {
                                'Quantity': 123,
                                'Items': [
                                    123,
                                ]
                            }
                        },
                        'Members': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'OriginId': 'string'
                                },
                            ]
                        }
                    },
                ]
            },
            'DefaultCacheBehavior': {
                'TargetOriginId': 'string',
                'ForwardedValues': {
                    'QueryString': True|False,
                    'Cookies': {
                        'Forward': 'none'|'whitelist'|'all',
                        'WhitelistedNames': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                    'Headers': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    },
                    'QueryStringCacheKeys': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    }
                },
                'TrustedSigners': {
                    'Enabled': True|False,
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                'MinTTL': 123,
                'AllowedMethods': {
                    'Quantity': 123,
                    'Items': [
                        'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                    ],
                    'CachedMethods': {
                        'Quantity': 123,
                        'Items': [
                            'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                        ]
                    }
                },
                'SmoothStreaming': True|False,
                'DefaultTTL': 123,
                'MaxTTL': 123,
                'Compress': True|False,
                'LambdaFunctionAssociations': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'LambdaFunctionARN': 'string',
                            'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                            'IncludeBody': True|False
                        },
                    ]
                },
                'FieldLevelEncryptionId': 'string'
            },
            'CacheBehaviors': {
                'Quantity': 123,
                'Items': [
                    {
                        'PathPattern': 'string',
                        'TargetOriginId': 'string',
                        'ForwardedValues': {
                            'QueryString': True|False,
                            'Cookies': {
                                'Forward': 'none'|'whitelist'|'all',
                                'WhitelistedNames': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                }
                            },
                            'Headers': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            },
                            'QueryStringCacheKeys': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                        'TrustedSigners': {
                            'Enabled': True|False,
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        },
                        'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                        'MinTTL': 123,
                        'AllowedMethods': {
                            'Quantity': 123,
                            'Items': [
                                'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                            ],
                            'CachedMethods': {
                                'Quantity': 123,
                                'Items': [
                                    'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                ]
                            }
                        },
                        'SmoothStreaming': True|False,
                        'DefaultTTL': 123,
                        'MaxTTL': 123,
                        'Compress': True|False,
                        'LambdaFunctionAssociations': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'LambdaFunctionARN': 'string',
                                    'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                    'IncludeBody': True|False
                                },
                            ]
                        },
                        'FieldLevelEncryptionId': 'string'
                    },
                ]
            },
            'CustomErrorResponses': {
                'Quantity': 123,
                'Items': [
                    {
                        'ErrorCode': 123,
                        'ResponsePagePath': 'string',
                        'ResponseCode': 'string',
                        'ErrorCachingMinTTL': 123
                    },
                ]
            },
            'Comment': 'string',
            'Logging': {
                'Enabled': True|False,
                'IncludeCookies': True|False,
                'Bucket': 'string',
                'Prefix': 'string'
            },
            'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
            'Enabled': True|False,
            'ViewerCertificate': {
                'CloudFrontDefaultCertificate': True|False,
                'IAMCertificateId': 'string',
                'ACMCertificateArn': 'string',
                'SSLSupportMethod': 'sni-only'|'vip',
                'MinimumProtocolVersion': 'SSLv3'|'TLSv1'|'TLSv1_2016'|'TLSv1.1_2016'|'TLSv1.2_2018',
                'Certificate': 'string',
                'CertificateSource': 'cloudfront'|'iam'|'acm'
            },
            'Restrictions': {
                'GeoRestriction': {
                    'RestrictionType': 'blacklist'|'whitelist'|'none',
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                }
            },
            'WebACLId': 'string',
            'HttpVersion': 'http1.1'|'http2',
            'IsIPV6Enabled': True|False
        },
        Id='string',
        IfMatch='string'
    )
    
    
    :type DistributionConfig: dict
    :param DistributionConfig: [REQUIRED]\nThe distribution\'s configuration information.\n\nCallerReference (string) -- [REQUIRED]A unique value (for example, a date-time stamp) that ensures that the request can\'t be replayed.\nIf the value of CallerReference is new (regardless of the content of the DistributionConfig object), CloudFront creates a new distribution.\nIf CallerReference is a value that you already sent in a previous request to create a distribution, CloudFront returns a DistributionAlreadyExists error.\n\nAliases (dict) --A complex type that contains information about CNAMEs (alternate domain names), if any, for this distribution.\n\nQuantity (integer) -- [REQUIRED]The number of CNAME aliases, if any, that you want to associate with this distribution.\n\nItems (list) --A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.\n\n(string) --\n\n\n\n\nDefaultRootObject (string) --The object that you want CloudFront to request from your origin (for example, index.html ) when a viewer requests the root URL for your distribution (http://www.example.com ) instead of an object in your distribution (http://www.example.com/product-description.html ). Specifying a default root object avoids exposing the contents of your distribution.\nSpecify only the object name, for example, index.html . Don\'t add a / before the object name.\nIf you don\'t want to specify a default root object when you create a distribution, include an empty DefaultRootObject element.\nTo delete the default root object from an existing distribution, update the distribution configuration and include an empty DefaultRootObject element.\nTo replace the default root object, update the distribution configuration and specify the new object.\nFor more information about the default root object, see Creating a Default Root Object in the Amazon CloudFront Developer Guide .\n\nOrigins (dict) -- [REQUIRED]A complex type that contains information about origins for this distribution.\n\nQuantity (integer) -- [REQUIRED]The number of origins or origin groups for this distribution.\n\nItems (list) -- [REQUIRED]A complex type that contains origins or origin groups for this distribution.\n\n(dict) --A complex type that describes the Amazon S3 bucket, HTTP server (for example, a web server), Amazon MediaStore, or other server from which CloudFront gets your files. This can also be an origin group, if you\'ve created an origin group. You must specify at least one origin or origin group.\nFor the current limit on the number of origins or origin groups that you can specify for a distribution, see Amazon CloudFront Limits in the AWS General Reference .\n\nId (string) -- [REQUIRED]A unique identifier for the origin or origin group. The value of Id must be unique within the distribution.\nWhen you specify the value of TargetOriginId for the default cache behavior or for another cache behavior, you indicate the origin to which you want the cache behavior to route requests by specifying the value of the Id element for that origin. When a request matches the path pattern for that cache behavior, CloudFront routes the request to the specified origin. For more information, see Cache Behavior Settings in the Amazon CloudFront Developer Guide .\n\nDomainName (string) -- [REQUIRED]\nAmazon S3 origins : The DNS name of the Amazon S3 bucket from which you want CloudFront to get objects for this origin, for example, myawsbucket.s3.amazonaws.com . If you set up your bucket to be configured as a website endpoint, enter the Amazon S3 static website hosting endpoint for the bucket.\nFor more information about specifying this value for different types of origins, see Origin Domain Name in the Amazon CloudFront Developer Guide .\nConstraints for Amazon S3 origins:\n\nIf you configured Amazon S3 Transfer Acceleration for your bucket, don\'t specify the s3-accelerate endpoint for DomainName .\nThe bucket name must be between 3 and 63 characters long (inclusive).\nThe bucket name must contain only lowercase characters, numbers, periods, underscores, and dashes.\nThe bucket name must not contain adjacent periods.\n\n\nCustom Origins : The DNS domain name for the HTTP server from which you want CloudFront to get objects for this origin, for example, www.example.com .\nConstraints for custom origins:\n\nDomainName must be a valid DNS name that contains only a-z, A-Z, 0-9, dot (.), hyphen (-), or underscore (_) characters.\nThe name cannot exceed 128 characters.\n\n\nOriginPath (string) --An optional element that causes CloudFront to request your content from a directory in your Amazon S3 bucket or your custom origin. When you include the OriginPath element, specify the directory name, beginning with a / . CloudFront appends the directory name to the value of DomainName , for example, example.com/production . Do not include a / at the end of the directory name.\nFor example, suppose you\'ve specified the following values for your distribution:\n\nDomainName : An Amazon S3 bucket named myawsbucket .\nOriginPath : /production\nCNAME : example.com\n\nWhen a user enters example.com/index.html in a browser, CloudFront sends a request to Amazon S3 for myawsbucket/production/index.html .\nWhen a user enters example.com/acme/index.html in a browser, CloudFront sends a request to Amazon S3 for myawsbucket/production/acme/index.html .\n\nCustomHeaders (dict) --A complex type that contains names and values for the custom headers that you want.\n\nQuantity (integer) -- [REQUIRED]The number of custom headers, if any, for this distribution.\n\nItems (list) --\nOptional : A list that contains one OriginCustomHeader element for each custom header that you want CloudFront to forward to the origin. If Quantity is 0 , omit Items .\n\n(dict) --A complex type that contains HeaderName and HeaderValue elements, if any, for this distribution.\n\nHeaderName (string) -- [REQUIRED]The name of a header that you want CloudFront to forward to your origin. For more information, see Forwarding Custom Headers to Your Origin (Web Distributions Only) in the Amazon CloudFront Developer Guide .\n\nHeaderValue (string) -- [REQUIRED]The value for the header that you specified in the HeaderName field.\n\n\n\n\n\n\n\nS3OriginConfig (dict) --A complex type that contains information about the Amazon S3 origin. If the origin is a custom origin, use the CustomOriginConfig element instead.\n\nOriginAccessIdentity (string) -- [REQUIRED]The CloudFront origin access identity to associate with the origin. Use an origin access identity to configure the origin so that viewers can only access objects in an Amazon S3 bucket through CloudFront. The format of the value is:\norigin-access-identity/cloudfront/ID-of-origin-access-identity\nwhere `` ID-of-origin-access-identity `` is the value that CloudFront returned in the ID element when you created the origin access identity.\nIf you want viewers to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty OriginAccessIdentity element.\nTo delete the origin access identity from an existing distribution, update the distribution configuration and include an empty OriginAccessIdentity element.\nTo replace the origin access identity, update the distribution configuration and specify the new origin access identity.\nFor more information about the origin access identity, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .\n\n\n\nCustomOriginConfig (dict) --A complex type that contains information about a custom origin. If the origin is an Amazon S3 bucket, use the S3OriginConfig element instead.\n\nHTTPPort (integer) -- [REQUIRED]The HTTP port the custom origin listens on.\n\nHTTPSPort (integer) -- [REQUIRED]The HTTPS port the custom origin listens on.\n\nOriginProtocolPolicy (string) -- [REQUIRED]The origin protocol policy to apply to your origin.\n\nOriginSslProtocols (dict) --The SSL/TLS protocols that you want CloudFront to use when communicating with your origin over HTTPS.\n\nQuantity (integer) -- [REQUIRED]The number of SSL/TLS protocols that you want to allow CloudFront to use when establishing an HTTPS connection with this origin.\n\nItems (list) -- [REQUIRED]A list that contains allowed SSL/TLS protocols for this distribution.\n\n(string) --\n\n\n\n\nOriginReadTimeout (integer) --You can create a custom origin read timeout. All timeout units are in seconds. The default origin read timeout is 30 seconds, but you can configure custom timeout lengths using the CloudFront API. The minimum timeout length is 4 seconds; the maximum is 60 seconds.\nIf you need to increase the maximum time limit, contact the AWS Support Center .\n\nOriginKeepaliveTimeout (integer) --You can create a custom keep-alive timeout. All timeout units are in seconds. The default keep-alive timeout is 5 seconds, but you can configure custom timeout lengths using the CloudFront API. The minimum timeout length is 1 second; the maximum is 60 seconds.\nIf you need to increase the maximum time limit, contact the AWS Support Center .\n\n\n\n\n\n\n\n\n\nOriginGroups (dict) --A complex type that contains information about origin groups for this distribution.\n\nQuantity (integer) -- [REQUIRED]The number of origin groups.\n\nItems (list) --The items (origin groups) in a distribution.\n\n(dict) --An origin group includes two origins (a primary origin and a second origin to failover to) and a failover criteria that you specify. You create an origin group to support origin failover in CloudFront. When you create or update a distribution, you can specifiy the origin group instead of a single origin, and CloudFront will failover from the primary origin to the second origin under the failover conditions that you\'ve chosen.\n\nId (string) -- [REQUIRED]The origin group\'s ID.\n\nFailoverCriteria (dict) -- [REQUIRED]A complex type that contains information about the failover criteria for an origin group.\n\nStatusCodes (dict) -- [REQUIRED]The status codes that, when returned from the primary origin, will trigger CloudFront to failover to the second origin.\n\nQuantity (integer) -- [REQUIRED]The number of status codes.\n\nItems (list) -- [REQUIRED]The items (status codes) for an origin group.\n\n(integer) --\n\n\n\n\n\n\nMembers (dict) -- [REQUIRED]A complex type that contains information about the origins in an origin group.\n\nQuantity (integer) -- [REQUIRED]The number of origins in an origin group.\n\nItems (list) -- [REQUIRED]Items (origins) in an origin group.\n\n(dict) --An origin in an origin group.\n\nOriginId (string) -- [REQUIRED]The ID for an origin in an origin group.\n\n\n\n\n\n\n\n\n\n\n\n\n\nDefaultCacheBehavior (dict) -- [REQUIRED]A complex type that describes the default cache behavior if you don\'t specify a CacheBehavior element or if files don\'t match any of the values of PathPattern in CacheBehavior elements. You must create exactly one default cache behavior.\n\nTargetOriginId (string) -- [REQUIRED]The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior in your distribution.\n\nForwardedValues (dict) -- [REQUIRED]A complex type that specifies how CloudFront handles query strings, cookies, and HTTP headers.\n\nQueryString (boolean) -- [REQUIRED]Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior and cache based on the query string parameters. CloudFront behavior depends on the value of QueryString and on the values that you specify for QueryStringCacheKeys , if any:\nIf you specify true for QueryString and you don\'t specify any values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin and caches based on all query string parameters. Depending on how many query string parameters and values you have, this can adversely affect performance because CloudFront must forward more requests to the origin.\nIf you specify true for QueryString and you specify one or more values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin, but it only caches based on the query string parameters that you specify.\nIf you specify false for QueryString , CloudFront doesn\'t forward any query string parameters to the origin, and doesn\'t cache based on query string parameters.\nFor more information, see Configuring CloudFront to Cache Based on Query String Parameters in the Amazon CloudFront Developer Guide .\n\nCookies (dict) -- [REQUIRED]A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see How CloudFront Forwards, Caches, and Logs Cookies in the Amazon CloudFront Developer Guide .\n\nForward (string) -- [REQUIRED]Specifies which cookies to forward to the origin for this cache behavior: all, none, or the list of cookies specified in the WhitelistedNames complex type.\nAmazon S3 doesn\'t process cookies. When the cache behavior is forwarding requests to an Amazon S3 origin, specify none for the Forward element.\n\nWhitelistedNames (dict) --Required if you specify whitelist for the value of Forward . A complex type that specifies how many different cookies you want CloudFront to forward to the origin for this cache behavior and, if you want to forward selected cookies, the names of those cookies.\nIf you specify all or none for the value of Forward , omit WhitelistedNames . If you change the value of Forward from whitelist to all or none and you don\'t delete the WhitelistedNames element and its child elements, CloudFront deletes them automatically.\nFor the current limit on the number of cookie names that you can whitelist for each cache behavior, see CloudFront Limits in the AWS General Reference .\n\nQuantity (integer) -- [REQUIRED]The number of different cookies that you want CloudFront to forward to the origin for this cache behavior. The value must equal the number of items that are in the Items field.\nWhen you set Forward = whitelist (in the CookiePreferences object), this value must be 1 or higher.\n\nItems (list) --A complex type that contains one Name element for each cookie that you want CloudFront to forward to the origin for this cache behavior. It must contain the same number of items that is specified in the Quantity field.\nWhen you set Forward = whitelist (in the CookiePreferences object), this field must contain at least one item.\n\n(string) --\n\n\n\n\n\n\nHeaders (dict) --A complex type that specifies the Headers , if any, that you want CloudFront to forward to the origin for this cache behavior (whitelisted headers). For the headers that you specify, CloudFront also caches separate versions of a specified object that is based on the header values in viewer requests.\nFor more information, see Caching Content Based on Request Headers in the Amazon CloudFront Developer Guide .\n\nQuantity (integer) -- [REQUIRED]The number of different headers that you want CloudFront to base caching on for this cache behavior. You can configure each cache behavior in a web distribution to do one of the following:\n\nForward all headers to your origin : Specify 1 for Quantity and * for Name .\n\n\nWarning\nCloudFront doesn\'t cache the objects that are associated with this cache behavior. Instead, CloudFront sends every request to the origin.\n\n\nForward a whitelist of headers you specify : Specify the number of headers that you want CloudFront to base caching on. Then specify the header names in Name elements. CloudFront caches your objects based on the values in the specified headers.\nForward only the default headers : Specify 0 for Quantity and omit Items . In this configuration, CloudFront doesn\'t cache based on the values in the request headers.\n\nRegardless of which option you choose, CloudFront forwards headers to your origin based on whether the origin is an S3 bucket or a custom origin. See the following documentation:\n\nS3 bucket : See HTTP Request Headers That CloudFront Removes or Updates\nCustom origin : See HTTP Request Headers and CloudFront Behavior\n\n\nItems (list) --A list that contains one Name element for each header that you want CloudFront to use for caching in this cache behavior. If Quantity is 0 , omit Items .\n\n(string) --\n\n\n\n\nQueryStringCacheKeys (dict) --A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.\n\nQuantity (integer) -- [REQUIRED]The number of whitelisted query string parameters for a cache behavior.\n\nItems (list) --A list that contains the query string parameters that you want CloudFront to use as a basis for caching for a cache behavior. If Quantity is 0, you can omit Items .\n\n(string) --\n\n\n\n\n\n\nTrustedSigners (dict) -- [REQUIRED]A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content.\nIf you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled , and specify the applicable values for Quantity and Items . For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .\nIf you don\'t want to require signed URLs in requests for objects that match PathPattern , specify false for Enabled and 0 for Quantity . Omit Items .\nTo add, change, or remove one or more trusted signers, change Enabled to true (if it\'s currently false ), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.\n\nEnabled (boolean) -- [REQUIRED]Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .\n\nQuantity (integer) -- [REQUIRED]The number of trusted signers for this cache behavior.\n\nItems (list) --\nOptional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .\n\n(string) --\n\n\n\n\nViewerProtocolPolicy (string) -- [REQUIRED]The protocol that viewers can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern . You can specify the following options:\n\nallow-all : Viewers can use HTTP or HTTPS.\nredirect-to-https : If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.\nhttps-only : If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).\n\nFor more information about requiring the HTTPS protocol, see Using an HTTPS Connection to Access Your Objects in the Amazon CloudFront Developer Guide .\n\nNote\nThe only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects\' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .\n\n\nMinTTL (integer) -- [REQUIRED]The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .\nYou must specify 0 for MinTTL if you configure CloudFront to forward all headers to your origin (under Headers , if you specify 1 for Quantity and * for Name ).\n\nAllowedMethods (dict) --A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices:\n\nCloudFront forwards only GET and HEAD requests.\nCloudFront forwards only GET , HEAD , and OPTIONS requests.\nCloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests.\n\nIf you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can\'t perform operations that you don\'t want them to. For example, you might not want users to have permissions to delete objects from your origin.\n\nQuantity (integer) -- [REQUIRED]The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET , HEAD , and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests).\n\nItems (list) -- [REQUIRED]A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.\n\n(string) --\n\n\nCachedMethods (dict) --A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices:\n\nCloudFront caches responses to GET and HEAD requests.\nCloudFront caches responses to GET , HEAD , and OPTIONS requests.\n\nIf you pick the second choice for your Amazon S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers, and Origin headers for the responses to be cached correctly.\n\nQuantity (integer) -- [REQUIRED]The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET , HEAD , and OPTIONS requests).\n\nItems (list) -- [REQUIRED]A complex type that contains the HTTP methods that you want CloudFront to cache responses to.\n\n(string) --\n\n\n\n\n\n\nSmoothStreaming (boolean) --Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true ; if not, specify false . If you specify true for SmoothStreaming , you can still distribute other content using this cache behavior if the content matches the value of PathPattern .\n\nDefaultTTL (integer) --The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .\n\nMaxTTL (integer) --The maximum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .\n\nCompress (boolean) --Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify true ; if not, specify false . For more information, see Serving Compressed Files in the Amazon CloudFront Developer Guide .\n\nLambdaFunctionAssociations (dict) --A complex type that contains zero or more Lambda function associations for a cache behavior.\n\nQuantity (integer) -- [REQUIRED]The number of Lambda function associations for this cache behavior.\n\nItems (list) --\nOptional : A complex type that contains LambdaFunctionAssociation items for this cache behavior. If Quantity is 0 , you can omit Items .\n\n(dict) --A complex type that contains a Lambda function association.\n\nLambdaFunctionARN (string) -- [REQUIRED]The ARN of the Lambda function. You must specify the ARN of a function version; you can\'t specify a Lambda alias or $LATEST.\n\nEventType (string) -- [REQUIRED]Specifies the event type that triggers a Lambda function invocation. You can specify the following values:\n\nviewer-request : The function executes when CloudFront receives a request from a viewer and before it checks to see whether the requested object is in the edge cache.\norigin-request : The function executes only when CloudFront forwards a request to your origin. When the requested object is in the edge cache, the function doesn\'t execute.\norigin-response : The function executes after CloudFront receives a response from the origin and before it caches the object in the response. When the requested object is in the edge cache, the function doesn\'t execute.\nviewer-response : The function executes before CloudFront returns the requested object to the viewer. The function executes regardless of whether the object was already in the edge cache. If the origin returns an HTTP status code other than HTTP 200 (OK), the function doesn\'t execute.\n\n\nIncludeBody (boolean) --A flag that allows a Lambda function to have read access to the body content. For more information, see Accessing the Request Body by Choosing the Include Body Option in the Amazon CloudFront Developer Guide.\n\n\n\n\n\n\n\nFieldLevelEncryptionId (string) --The value of ID for the field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data for a cache behavior or for the default cache behavior in your distribution.\n\n\n\nCacheBehaviors (dict) --A complex type that contains zero or more CacheBehavior elements.\n\nQuantity (integer) -- [REQUIRED]The number of cache behaviors for this distribution.\n\nItems (list) --Optional: A complex type that contains cache behaviors for this distribution. If Quantity is 0 , you can omit Items .\n\n(dict) --A complex type that describes how CloudFront processes requests.\nYou must create at least as many cache behaviors (including the default cache behavior) as you have origins if you want CloudFront to distribute objects from all of the origins. Each cache behavior specifies the one origin from which you want CloudFront to get objects. If you have two origins and only the default cache behavior, the default cache behavior will cause CloudFront to get objects from one of the origins, but the other origin is never used.\nFor the current limit on the number of cache behaviors that you can add to a distribution, see Amazon CloudFront Limits in the AWS General Reference .\nIf you don\'t want to specify any cache behaviors, include only an empty CacheBehaviors element. Don\'t include an empty CacheBehavior element, or CloudFront returns a MalformedXML error.\nTo delete all cache behaviors in an existing distribution, update the distribution configuration and include only an empty CacheBehaviors element.\nTo add, change, or remove one or more cache behaviors, update the distribution configuration and specify all of the cache behaviors that you want to include in the updated distribution.\nFor more information about cache behaviors, see Cache Behaviors in the Amazon CloudFront Developer Guide .\n\nPathPattern (string) -- [REQUIRED]The pattern (for example, images/*.jpg ) that specifies which requests to apply the behavior to. When CloudFront receives a viewer request, the requested path is compared with path patterns in the order in which cache behaviors are listed in the distribution.\n\nNote\nYou can optionally include a slash (/ ) at the beginning of the path pattern. For example, /images/*.jpg . CloudFront behavior is the same with or without the leading / .\n\nThe path pattern for the default cache behavior is * and cannot be changed. If the request for an object does not match the path pattern for any cache behaviors, CloudFront applies the behavior in the default cache behavior.\nFor more information, see Path Pattern in the Amazon CloudFront Developer Guide .\n\nTargetOriginId (string) -- [REQUIRED]The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior in your distribution.\n\nForwardedValues (dict) -- [REQUIRED]A complex type that specifies how CloudFront handles query strings, cookies, and HTTP headers.\n\nQueryString (boolean) -- [REQUIRED]Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior and cache based on the query string parameters. CloudFront behavior depends on the value of QueryString and on the values that you specify for QueryStringCacheKeys , if any:\nIf you specify true for QueryString and you don\'t specify any values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin and caches based on all query string parameters. Depending on how many query string parameters and values you have, this can adversely affect performance because CloudFront must forward more requests to the origin.\nIf you specify true for QueryString and you specify one or more values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin, but it only caches based on the query string parameters that you specify.\nIf you specify false for QueryString , CloudFront doesn\'t forward any query string parameters to the origin, and doesn\'t cache based on query string parameters.\nFor more information, see Configuring CloudFront to Cache Based on Query String Parameters in the Amazon CloudFront Developer Guide .\n\nCookies (dict) -- [REQUIRED]A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see How CloudFront Forwards, Caches, and Logs Cookies in the Amazon CloudFront Developer Guide .\n\nForward (string) -- [REQUIRED]Specifies which cookies to forward to the origin for this cache behavior: all, none, or the list of cookies specified in the WhitelistedNames complex type.\nAmazon S3 doesn\'t process cookies. When the cache behavior is forwarding requests to an Amazon S3 origin, specify none for the Forward element.\n\nWhitelistedNames (dict) --Required if you specify whitelist for the value of Forward . A complex type that specifies how many different cookies you want CloudFront to forward to the origin for this cache behavior and, if you want to forward selected cookies, the names of those cookies.\nIf you specify all or none for the value of Forward , omit WhitelistedNames . If you change the value of Forward from whitelist to all or none and you don\'t delete the WhitelistedNames element and its child elements, CloudFront deletes them automatically.\nFor the current limit on the number of cookie names that you can whitelist for each cache behavior, see CloudFront Limits in the AWS General Reference .\n\nQuantity (integer) -- [REQUIRED]The number of different cookies that you want CloudFront to forward to the origin for this cache behavior. The value must equal the number of items that are in the Items field.\nWhen you set Forward = whitelist (in the CookiePreferences object), this value must be 1 or higher.\n\nItems (list) --A complex type that contains one Name element for each cookie that you want CloudFront to forward to the origin for this cache behavior. It must contain the same number of items that is specified in the Quantity field.\nWhen you set Forward = whitelist (in the CookiePreferences object), this field must contain at least one item.\n\n(string) --\n\n\n\n\n\n\nHeaders (dict) --A complex type that specifies the Headers , if any, that you want CloudFront to forward to the origin for this cache behavior (whitelisted headers). For the headers that you specify, CloudFront also caches separate versions of a specified object that is based on the header values in viewer requests.\nFor more information, see Caching Content Based on Request Headers in the Amazon CloudFront Developer Guide .\n\nQuantity (integer) -- [REQUIRED]The number of different headers that you want CloudFront to base caching on for this cache behavior. You can configure each cache behavior in a web distribution to do one of the following:\n\nForward all headers to your origin : Specify 1 for Quantity and * for Name .\n\n\nWarning\nCloudFront doesn\'t cache the objects that are associated with this cache behavior. Instead, CloudFront sends every request to the origin.\n\n\nForward a whitelist of headers you specify : Specify the number of headers that you want CloudFront to base caching on. Then specify the header names in Name elements. CloudFront caches your objects based on the values in the specified headers.\nForward only the default headers : Specify 0 for Quantity and omit Items . In this configuration, CloudFront doesn\'t cache based on the values in the request headers.\n\nRegardless of which option you choose, CloudFront forwards headers to your origin based on whether the origin is an S3 bucket or a custom origin. See the following documentation:\n\nS3 bucket : See HTTP Request Headers That CloudFront Removes or Updates\nCustom origin : See HTTP Request Headers and CloudFront Behavior\n\n\nItems (list) --A list that contains one Name element for each header that you want CloudFront to use for caching in this cache behavior. If Quantity is 0 , omit Items .\n\n(string) --\n\n\n\n\nQueryStringCacheKeys (dict) --A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.\n\nQuantity (integer) -- [REQUIRED]The number of whitelisted query string parameters for a cache behavior.\n\nItems (list) --A list that contains the query string parameters that you want CloudFront to use as a basis for caching for a cache behavior. If Quantity is 0, you can omit Items .\n\n(string) --\n\n\n\n\n\n\nTrustedSigners (dict) -- [REQUIRED]A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content.\nIf you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled , and specify the applicable values for Quantity and Items . For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .\nIf you don\'t want to require signed URLs in requests for objects that match PathPattern , specify false for Enabled and 0 for Quantity . Omit Items .\nTo add, change, or remove one or more trusted signers, change Enabled to true (if it\'s currently false ), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.\n\nEnabled (boolean) -- [REQUIRED]Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .\n\nQuantity (integer) -- [REQUIRED]The number of trusted signers for this cache behavior.\n\nItems (list) --\nOptional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .\n\n(string) --\n\n\n\n\nViewerProtocolPolicy (string) -- [REQUIRED]The protocol that viewers can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern . You can specify the following options:\n\nallow-all : Viewers can use HTTP or HTTPS.\nredirect-to-https : If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.\nhttps-only : If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).\n\nFor more information about requiring the HTTPS protocol, see Using an HTTPS Connection to Access Your Objects in the Amazon CloudFront Developer Guide .\n\nNote\nThe only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects\' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .\n\n\nMinTTL (integer) -- [REQUIRED]The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .\nYou must specify 0 for MinTTL if you configure CloudFront to forward all headers to your origin (under Headers , if you specify 1 for Quantity and * for Name ).\n\nAllowedMethods (dict) --A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices:\n\nCloudFront forwards only GET and HEAD requests.\nCloudFront forwards only GET , HEAD , and OPTIONS requests.\nCloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests.\n\nIf you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can\'t perform operations that you don\'t want them to. For example, you might not want users to have permissions to delete objects from your origin.\n\nQuantity (integer) -- [REQUIRED]The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET , HEAD , and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests).\n\nItems (list) -- [REQUIRED]A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.\n\n(string) --\n\n\nCachedMethods (dict) --A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices:\n\nCloudFront caches responses to GET and HEAD requests.\nCloudFront caches responses to GET , HEAD , and OPTIONS requests.\n\nIf you pick the second choice for your Amazon S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers, and Origin headers for the responses to be cached correctly.\n\nQuantity (integer) -- [REQUIRED]The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET , HEAD , and OPTIONS requests).\n\nItems (list) -- [REQUIRED]A complex type that contains the HTTP methods that you want CloudFront to cache responses to.\n\n(string) --\n\n\n\n\n\n\nSmoothStreaming (boolean) --Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true ; if not, specify false . If you specify true for SmoothStreaming , you can still distribute other content using this cache behavior if the content matches the value of PathPattern .\n\nDefaultTTL (integer) --The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .\n\nMaxTTL (integer) --The maximum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .\n\nCompress (boolean) --Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify true; if not, specify false. For more information, see Serving Compressed Files in the Amazon CloudFront Developer Guide .\n\nLambdaFunctionAssociations (dict) --A complex type that contains zero or more Lambda function associations for a cache behavior.\n\nQuantity (integer) -- [REQUIRED]The number of Lambda function associations for this cache behavior.\n\nItems (list) --\nOptional : A complex type that contains LambdaFunctionAssociation items for this cache behavior. If Quantity is 0 , you can omit Items .\n\n(dict) --A complex type that contains a Lambda function association.\n\nLambdaFunctionARN (string) -- [REQUIRED]The ARN of the Lambda function. You must specify the ARN of a function version; you can\'t specify a Lambda alias or $LATEST.\n\nEventType (string) -- [REQUIRED]Specifies the event type that triggers a Lambda function invocation. You can specify the following values:\n\nviewer-request : The function executes when CloudFront receives a request from a viewer and before it checks to see whether the requested object is in the edge cache.\norigin-request : The function executes only when CloudFront forwards a request to your origin. When the requested object is in the edge cache, the function doesn\'t execute.\norigin-response : The function executes after CloudFront receives a response from the origin and before it caches the object in the response. When the requested object is in the edge cache, the function doesn\'t execute.\nviewer-response : The function executes before CloudFront returns the requested object to the viewer. The function executes regardless of whether the object was already in the edge cache. If the origin returns an HTTP status code other than HTTP 200 (OK), the function doesn\'t execute.\n\n\nIncludeBody (boolean) --A flag that allows a Lambda function to have read access to the body content. For more information, see Accessing the Request Body by Choosing the Include Body Option in the Amazon CloudFront Developer Guide.\n\n\n\n\n\n\n\nFieldLevelEncryptionId (string) --The value of ID for the field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data for a cache behavior or for the default cache behavior in your distribution.\n\n\n\n\n\n\n\nCustomErrorResponses (dict) --A complex type that controls the following:\n\nWhether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.\nHow long CloudFront caches HTTP status codes in the 4xx and 5xx range.\n\nFor more information about custom error pages, see Customizing Error Responses in the Amazon CloudFront Developer Guide .\n\nQuantity (integer) -- [REQUIRED]The number of HTTP status codes for which you want to specify a custom error page and/or a caching duration. If Quantity is 0 , you can omit Items .\n\nItems (list) --A complex type that contains a CustomErrorResponse element for each HTTP status code for which you want to specify a custom error page and/or a caching duration.\n\n(dict) --A complex type that controls:\n\nWhether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.\nHow long CloudFront caches HTTP status codes in the 4xx and 5xx range.\n\nFor more information about custom error pages, see Customizing Error Responses in the Amazon CloudFront Developer Guide .\n\nErrorCode (integer) -- [REQUIRED]The HTTP status code for which you want to specify a custom error page and/or a caching duration.\n\nResponsePagePath (string) --The path to the custom error page that you want CloudFront to return to a viewer when your origin returns the HTTP status code specified by ErrorCode , for example, /4xx-errors/403-forbidden.html . If you want to store your objects and your custom error pages in different locations, your distribution must include a cache behavior for which the following is true:\n\nThe value of PathPattern matches the path to your custom error messages. For example, suppose you saved custom error pages for 4xx errors in an Amazon S3 bucket in a directory named /4xx-errors . Your distribution must include a cache behavior for which the path pattern routes requests for your custom error pages to that location, for example, /4xx-errors/* .\nThe value of TargetOriginId specifies the value of the ID element for the origin that contains your custom error pages.\n\nIf you specify a value for ResponsePagePath , you must also specify a value for ResponseCode .\nWe recommend that you store custom error pages in an Amazon S3 bucket. If you store custom error pages on an HTTP server and the server starts to return 5xx errors, CloudFront can\'t get the files that you want to return to viewers because the origin server is unavailable.\n\nResponseCode (string) --The HTTP status code that you want CloudFront to return to the viewer along with the custom error page. There are a variety of reasons that you might want CloudFront to return a status code different from the status code that your origin returned to CloudFront, for example:\n\nSome Internet devices (some firewalls and corporate proxies, for example) intercept HTTP 4xx and 5xx and prevent the response from being returned to the viewer. If you substitute 200 , the response typically won\'t be intercepted.\nIf you don\'t care about distinguishing among different client errors or server errors, you can specify 400 or 500 as the ResponseCode for all 4xx or 5xx errors.\nYou might want to return a 200 status code (OK) and static website so your customers don\'t know that your website is down.\n\nIf you specify a value for ResponseCode , you must also specify a value for ResponsePagePath .\n\nErrorCachingMinTTL (integer) --The minimum amount of time, in seconds, that you want CloudFront to cache the HTTP status code specified in ErrorCode . When this time period has elapsed, CloudFront queries your origin to see whether the problem that caused the error has been resolved and the requested object is now available.\nFor more information, see Customizing Error Responses in the Amazon CloudFront Developer Guide .\n\n\n\n\n\n\n\nComment (string) -- [REQUIRED]Any comments you want to include about the distribution.\nIf you don\'t want to specify a comment, include an empty Comment element.\nTo delete an existing comment, update the distribution configuration and include an empty Comment element.\nTo add or change a comment, update the distribution configuration and specify the new comment.\n\nLogging (dict) --A complex type that controls whether access logs are written for the distribution.\nFor more information about logging, see Access Logs in the Amazon CloudFront Developer Guide .\n\nEnabled (boolean) -- [REQUIRED]Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you don\'t want to enable logging when you create a distribution or if you want to disable logging for an existing distribution, specify false for Enabled , and specify empty Bucket and Prefix elements. If you specify false for Enabled but you specify values for Bucket , prefix , and IncludeCookies , the values are automatically deleted.\n\nIncludeCookies (boolean) -- [REQUIRED]Specifies whether you want CloudFront to include cookies in access logs, specify true for IncludeCookies . If you choose to include cookies in logs, CloudFront logs all cookies regardless of how you configure the cache behaviors for this distribution. If you don\'t want to include cookies when you create a distribution or if you want to disable include cookies for an existing distribution, specify false for IncludeCookies .\n\nBucket (string) -- [REQUIRED]The Amazon S3 bucket to store the access logs in, for example, myawslogbucket.s3.amazonaws.com .\n\nPrefix (string) -- [REQUIRED]An optional string that you want CloudFront to prefix to the access log filenames for this distribution, for example, myprefix/ . If you want to enable logging, but you don\'t want to specify a prefix, you still must include an empty Prefix element in the Logging element.\n\n\n\nPriceClass (string) --The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify PriceClass_All , CloudFront responds to requests for your objects from all CloudFront edge locations.\nIf you specify a price class other than PriceClass_All , CloudFront serves your objects from the CloudFront edge location that has the lowest latency among the edge locations in your price class. Viewers who are in or near regions that are excluded from your specified price class may encounter slower performance.\nFor more information about price classes, see Choosing the Price Class for a CloudFront Distribution in the Amazon CloudFront Developer Guide . For information about CloudFront pricing, including how price classes (such as Price Class 100) map to CloudFront regions, see Amazon CloudFront Pricing . For price class information, scroll down to see the table at the bottom of the page.\n\nEnabled (boolean) -- [REQUIRED]From this field, you can enable or disable the selected distribution.\n\nViewerCertificate (dict) --A complex type that determines the distribution\xe2\x80\x99s SSL/TLS configuration for communicating with viewers.\n\nCloudFrontDefaultCertificate (boolean) --If the distribution uses the CloudFront domain name such as d111111abcdef8.cloudfront.net , set this field to true .\nIf the distribution uses Aliases (alternate domain names or CNAMEs), set this field to false and specify values for the following fields:\n\nACMCertificateArn or IAMCertificateId (specify a value for one, not both)\nMinimumProtocolVersion\nSSLSupportMethod\n\n\nIAMCertificateId (string) --If the distribution uses Aliases (alternate domain names or CNAMEs) and the SSL/TLS certificate is stored in AWS Identity and Access Management (AWS IAM) , provide the ID of the IAM certificate.\nIf you specify an IAM certificate ID, you must also specify values for MinimumProtocolVerison and SSLSupportMethod .\n\nACMCertificateArn (string) --If the distribution uses Aliases (alternate domain names or CNAMEs) and the SSL/TLS certificate is stored in AWS Certificate Manager (ACM) , provide the Amazon Resource Name (ARN) of the ACM certificate. CloudFront only supports ACM certificates in the US East (N. Virginia) Region (us-east-1 ).\nIf you specify an ACM certificate ARN, you must also specify values for MinimumProtocolVerison and SSLSupportMethod .\n\nSSLSupportMethod (string) --If the distribution uses Aliases (alternate domain names or CNAMEs), specify which viewers the distribution accepts HTTPS connections from.\n\nsni-only \xe2\x80\x93 The distribution accepts HTTPS connections from only viewers that support server name indication (SNI) . This is recommended. Most browsers and clients released after 2010 support SNI.\nvip \xe2\x80\x93 The distribution accepts HTTPS connections from all viewers including those that don\xe2\x80\x99t support SNI. This is not recommended, and results in additional monthly charges from CloudFront.\n\nIf the distribution uses the CloudFront domain name such as d111111abcdef8.cloudfront.net , don\xe2\x80\x99t set a value for this field.\n\nMinimumProtocolVersion (string) --If the distribution uses Aliases (alternate domain names or CNAMEs), specify the security policy that you want CloudFront to use for HTTPS connections with viewers. The security policy determines two settings:\n\nThe minimum SSL/TLS protocol that CloudFront can use to communicate with viewers.\nThe ciphers that CloudFront can use to encrypt the content that it returns to viewers.\n\nFor more information, see Security Policy and Supported Protocols and Ciphers Between Viewers and CloudFront in the Amazon CloudFront Developer Guide .\n\nNote\nOn the CloudFront console, this setting is called Security Policy .\n\nWe recommend that you specify TLSv1.2_2018 unless your viewers are using browsers or devices that don\xe2\x80\x99t support TLSv1.2.\nWhen you\xe2\x80\x99re using SNI only (you set SSLSupportMethod to sni-only ), you must specify TLSv1 or higher.\nIf the distribution uses the CloudFront domain name such as d111111abcdef8.cloudfront.net (you set CloudFrontDefaultCertificate to true ), CloudFront automatically sets the security policy to TLSv1 regardless of the value that you set here.\n\nCertificate (string) --This field is deprecated. Use one of the following fields instead:\n\nACMCertificateArn\nIAMCertificateId\nCloudFrontDefaultCertificate\n\n\nCertificateSource (string) --This field is deprecated. Use one of the following fields instead:\n\nACMCertificateArn\nIAMCertificateId\nCloudFrontDefaultCertificate\n\n\n\n\nRestrictions (dict) --A complex type that identifies ways in which you want to restrict distribution of your content.\n\nGeoRestriction (dict) -- [REQUIRED]A complex type that controls the countries in which your content is distributed. CloudFront determines the location of your users using MaxMind GeoIP databases.\n\nRestrictionType (string) -- [REQUIRED]The method that you want to use to restrict distribution of your content by country:\n\nnone : No geo restriction is enabled, meaning access to content is not restricted by client geo location.\nblacklist : The Location elements specify the countries in which you don\'t want CloudFront to distribute your content.\nwhitelist : The Location elements specify the countries in which you want CloudFront to distribute your content.\n\n\nQuantity (integer) -- [REQUIRED]When geo restriction is enabled , this is the number of countries in your whitelist or blacklist . Otherwise, when it is not enabled, Quantity is 0 , and you can omit Items .\n\nItems (list) --A complex type that contains a Location element for each country in which you want CloudFront either to distribute your content (whitelist ) or not distribute your content (blacklist ).\nThe Location element is a two-letter, uppercase country code for a country that you want to include in your blacklist or whitelist . Include one Location element for each country.\nCloudFront and MaxMind both use ISO 3166 country codes. For the current list of countries and the corresponding codes, see ISO 3166-1-alpha-2 code on the International Organization for Standardization website. You can also refer to the country list on the CloudFront console, which includes both country names and codes.\n\n(string) --\n\n\n\n\n\n\nWebACLId (string) --A unique identifier that specifies the AWS WAF web ACL, if any, to associate with this distribution. To specify a web ACL created using the latest version of AWS WAF, use the ACL ARN, for example arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/473e64fd-f30b-4765-81a0-62ad96dd167a . To specify a web ACL created using AWS WAF Classic, use the ACL ID, for example 473e64fd-f30b-4765-81a0-62ad96dd167a .\nAWS WAF is a web application firewall that lets you monitor the HTTP and HTTPS requests that are forwarded to CloudFront, and lets you control access to your content. Based on conditions that you specify, such as the IP addresses that requests originate from or the values of query strings, CloudFront responds to requests either with the requested content or with an HTTP 403 status code (Forbidden). You can also configure CloudFront to return a custom error page when a request is blocked. For more information about AWS WAF, see the AWS WAF Developer Guide .\n\nHttpVersion (string) --(Optional) Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront. The default value for new web distributions is http2. Viewers that don\'t support HTTP/2 automatically use an earlier HTTP version.\nFor viewers and CloudFront to use HTTP/2, viewers must support TLS 1.2 or later, and must support Server Name Identification (SNI).\nIn general, configuring CloudFront to communicate with viewers using HTTP/2 reduces latency. You can improve performance by optimizing for HTTP/2. For more information, do an Internet search for 'http/2 optimization.'\n\nIsIPV6Enabled (boolean) --If you want CloudFront to respond to IPv6 DNS requests with an IPv6 address for your distribution, specify true . If you specify false , CloudFront responds to IPv6 DNS requests with the DNS response code NOERROR and with no IP addresses. This allows viewers to submit a second request, for an IPv4 address for your distribution.\nIn general, you should enable IPv6 if you have users on IPv6 networks who want to access your content. However, if you\'re using signed URLs or signed cookies to restrict access to your content, and if you\'re using a custom policy that includes the IpAddress parameter to restrict the IP addresses that can access your content, don\'t enable IPv6. If you want to restrict access to some content by IP address and not restrict access to other content (or restrict access but not by IP address), you can create two distributions. For more information, see Creating a Signed URL Using a Custom Policy in the Amazon CloudFront Developer Guide .\nIf you\'re using an Amazon Route 53 alias resource record set to route traffic to your CloudFront distribution, you need to create a second alias resource record set when both of the following are true:\n\nYou enable IPv6 for the distribution\nYou\'re using alternate domain names in the URLs for your objects\n\nFor more information, see Routing Traffic to an Amazon CloudFront Web Distribution by Using Your Domain Name in the Amazon Route 53 Developer Guide .\nIf you created a CNAME resource record set, either with Amazon Route 53 or with another DNS service, you don\'t need to make any changes. A CNAME record will route traffic to your distribution regardless of the IP address format of the viewer request.\n\n\n

    :type Id: string
    :param Id: [REQUIRED]\nThe distribution\'s id.\n

    :type IfMatch: string
    :param IfMatch: The value of the ETag header that you received when retrieving the distribution\'s configuration. For example: E2QWRUHAPOMQZL .

    :rtype: dict

ReturnsResponse Syntax
{
    'Distribution': {
        'Id': 'string',
        'ARN': 'string',
        'Status': 'string',
        'LastModifiedTime': datetime(2015, 1, 1),
        'InProgressInvalidationBatches': 123,
        'DomainName': 'string',
        'ActiveTrustedSigners': {
            'Enabled': True|False,
            'Quantity': 123,
            'Items': [
                {
                    'AwsAccountNumber': 'string',
                    'KeyPairIds': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    }
                },
            ]
        },
        'DistributionConfig': {
            'CallerReference': 'string',
            'Aliases': {
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'DefaultRootObject': 'string',
            'Origins': {
                'Quantity': 123,
                'Items': [
                    {
                        'Id': 'string',
                        'DomainName': 'string',
                        'OriginPath': 'string',
                        'CustomHeaders': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'HeaderName': 'string',
                                    'HeaderValue': 'string'
                                },
                            ]
                        },
                        'S3OriginConfig': {
                            'OriginAccessIdentity': 'string'
                        },
                        'CustomOriginConfig': {
                            'HTTPPort': 123,
                            'HTTPSPort': 123,
                            'OriginProtocolPolicy': 'http-only'|'match-viewer'|'https-only',
                            'OriginSslProtocols': {
                                'Quantity': 123,
                                'Items': [
                                    'SSLv3'|'TLSv1'|'TLSv1.1'|'TLSv1.2',
                                ]
                            },
                            'OriginReadTimeout': 123,
                            'OriginKeepaliveTimeout': 123
                        }
                    },
                ]
            },
            'OriginGroups': {
                'Quantity': 123,
                'Items': [
                    {
                        'Id': 'string',
                        'FailoverCriteria': {
                            'StatusCodes': {
                                'Quantity': 123,
                                'Items': [
                                    123,
                                ]
                            }
                        },
                        'Members': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'OriginId': 'string'
                                },
                            ]
                        }
                    },
                ]
            },
            'DefaultCacheBehavior': {
                'TargetOriginId': 'string',
                'ForwardedValues': {
                    'QueryString': True|False,
                    'Cookies': {
                        'Forward': 'none'|'whitelist'|'all',
                        'WhitelistedNames': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                    'Headers': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    },
                    'QueryStringCacheKeys': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    }
                },
                'TrustedSigners': {
                    'Enabled': True|False,
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                'MinTTL': 123,
                'AllowedMethods': {
                    'Quantity': 123,
                    'Items': [
                        'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                    ],
                    'CachedMethods': {
                        'Quantity': 123,
                        'Items': [
                            'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                        ]
                    }
                },
                'SmoothStreaming': True|False,
                'DefaultTTL': 123,
                'MaxTTL': 123,
                'Compress': True|False,
                'LambdaFunctionAssociations': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'LambdaFunctionARN': 'string',
                            'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                            'IncludeBody': True|False
                        },
                    ]
                },
                'FieldLevelEncryptionId': 'string'
            },
            'CacheBehaviors': {
                'Quantity': 123,
                'Items': [
                    {
                        'PathPattern': 'string',
                        'TargetOriginId': 'string',
                        'ForwardedValues': {
                            'QueryString': True|False,
                            'Cookies': {
                                'Forward': 'none'|'whitelist'|'all',
                                'WhitelistedNames': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                }
                            },
                            'Headers': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            },
                            'QueryStringCacheKeys': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                        'TrustedSigners': {
                            'Enabled': True|False,
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        },
                        'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                        'MinTTL': 123,
                        'AllowedMethods': {
                            'Quantity': 123,
                            'Items': [
                                'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                            ],
                            'CachedMethods': {
                                'Quantity': 123,
                                'Items': [
                                    'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                ]
                            }
                        },
                        'SmoothStreaming': True|False,
                        'DefaultTTL': 123,
                        'MaxTTL': 123,
                        'Compress': True|False,
                        'LambdaFunctionAssociations': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'LambdaFunctionARN': 'string',
                                    'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                    'IncludeBody': True|False
                                },
                            ]
                        },
                        'FieldLevelEncryptionId': 'string'
                    },
                ]
            },
            'CustomErrorResponses': {
                'Quantity': 123,
                'Items': [
                    {
                        'ErrorCode': 123,
                        'ResponsePagePath': 'string',
                        'ResponseCode': 'string',
                        'ErrorCachingMinTTL': 123
                    },
                ]
            },
            'Comment': 'string',
            'Logging': {
                'Enabled': True|False,
                'IncludeCookies': True|False,
                'Bucket': 'string',
                'Prefix': 'string'
            },
            'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
            'Enabled': True|False,
            'ViewerCertificate': {
                'CloudFrontDefaultCertificate': True|False,
                'IAMCertificateId': 'string',
                'ACMCertificateArn': 'string',
                'SSLSupportMethod': 'sni-only'|'vip',
                'MinimumProtocolVersion': 'SSLv3'|'TLSv1'|'TLSv1_2016'|'TLSv1.1_2016'|'TLSv1.2_2018',
                'Certificate': 'string',
                'CertificateSource': 'cloudfront'|'iam'|'acm'
            },
            'Restrictions': {
                'GeoRestriction': {
                    'RestrictionType': 'blacklist'|'whitelist'|'none',
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                }
            },
            'WebACLId': 'string',
            'HttpVersion': 'http1.1'|'http2',
            'IsIPV6Enabled': True|False
        },
        'AliasICPRecordals': [
            {
                'CNAME': 'string',
                'ICPRecordalStatus': 'APPROVED'|'SUSPENDED'|'PENDING'
            },
        ]
    },
    'ETag': 'string'
}


Response Structure

(dict) --
The returned result of the corresponding request.

Distribution (dict) --
The distribution\'s information.

Id (string) --
The identifier for the distribution. For example: EDFDVBD632BHDS5 .

ARN (string) --
The ARN (Amazon Resource Name) for the distribution. For example: arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5 , where 123456789012 is your AWS account ID.

Status (string) --
This response element indicates the current status of the distribution. When the status is Deployed , the distribution\'s information is fully propagated to all CloudFront edge locations.

LastModifiedTime (datetime) --
The date and time the distribution was last modified.

InProgressInvalidationBatches (integer) --
The number of invalidation batches currently in progress.

DomainName (string) --
The domain name corresponding to the distribution, for example, d111111abcdef8.cloudfront.net .

ActiveTrustedSigners (dict) --
CloudFront automatically adds this element to the response only if you\'ve set up the distribution to serve private content with signed URLs. The element lists the key pair IDs that CloudFront is aware of for each trusted signer. The Signer child element lists the AWS account number of the trusted signer (or an empty Self element if the signer is you). The Signer element also includes the IDs of any active key pairs associated with the trusted signer\'s AWS account. If no KeyPairId element appears for a Signer , that signer can\'t create working signed URLs.

Enabled (boolean) --
Enabled is true if any of the AWS accounts listed in the TrustedSigners complex type for this distribution have active CloudFront key pairs. If not, Enabled is false .

Quantity (integer) --
The number of trusted signers specified in the TrustedSigners complex type.

Items (list) --
A complex type that contains one Signer complex type for each trusted signer that is specified in the TrustedSigners complex type.

(dict) --
A complex type that lists the AWS accounts that were included in the TrustedSigners complex type, as well as their active CloudFront key pair IDs, if any.

AwsAccountNumber (string) --
An AWS account that is included in the TrustedSigners complex type for this distribution. Valid values include:

self , which is the AWS account used to create the distribution.
An AWS account number.


KeyPairIds (dict) --
A complex type that lists the active CloudFront key pairs, if any, that are associated with AwsAccountNumber .

Quantity (integer) --
The number of active CloudFront key pairs for AwsAccountNumber .
For more information, see ActiveTrustedSigners .

Items (list) --
A complex type that lists the active CloudFront key pairs, if any, that are associated with AwsAccountNumber .
For more information, see ActiveTrustedSigners .

(string) --










DistributionConfig (dict) --
The current configuration information for the distribution. Send a GET request to the /*CloudFront API version* /distribution ID/config resource.

CallerReference (string) --
A unique value (for example, a date-time stamp) that ensures that the request can\'t be replayed.
If the value of CallerReference is new (regardless of the content of the DistributionConfig object), CloudFront creates a new distribution.
If CallerReference is a value that you already sent in a previous request to create a distribution, CloudFront returns a DistributionAlreadyExists error.

Aliases (dict) --
A complex type that contains information about CNAMEs (alternate domain names), if any, for this distribution.

Quantity (integer) --
The number of CNAME aliases, if any, that you want to associate with this distribution.

Items (list) --
A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.

(string) --




DefaultRootObject (string) --
The object that you want CloudFront to request from your origin (for example, index.html ) when a viewer requests the root URL for your distribution (http://www.example.com ) instead of an object in your distribution (http://www.example.com/product-description.html ). Specifying a default root object avoids exposing the contents of your distribution.
Specify only the object name, for example, index.html . Don\'t add a / before the object name.
If you don\'t want to specify a default root object when you create a distribution, include an empty DefaultRootObject element.
To delete the default root object from an existing distribution, update the distribution configuration and include an empty DefaultRootObject element.
To replace the default root object, update the distribution configuration and specify the new object.
For more information about the default root object, see Creating a Default Root Object in the Amazon CloudFront Developer Guide .

Origins (dict) --
A complex type that contains information about origins for this distribution.

Quantity (integer) --
The number of origins or origin groups for this distribution.

Items (list) --
A complex type that contains origins or origin groups for this distribution.

(dict) --
A complex type that describes the Amazon S3 bucket, HTTP server (for example, a web server), Amazon MediaStore, or other server from which CloudFront gets your files. This can also be an origin group, if you\'ve created an origin group. You must specify at least one origin or origin group.
For the current limit on the number of origins or origin groups that you can specify for a distribution, see Amazon CloudFront Limits in the AWS General Reference .

Id (string) --
A unique identifier for the origin or origin group. The value of Id must be unique within the distribution.
When you specify the value of TargetOriginId for the default cache behavior or for another cache behavior, you indicate the origin to which you want the cache behavior to route requests by specifying the value of the Id element for that origin. When a request matches the path pattern for that cache behavior, CloudFront routes the request to the specified origin. For more information, see Cache Behavior Settings in the Amazon CloudFront Developer Guide .

DomainName (string) --

Amazon S3 origins : The DNS name of the Amazon S3 bucket from which you want CloudFront to get objects for this origin, for example, myawsbucket.s3.amazonaws.com . If you set up your bucket to be configured as a website endpoint, enter the Amazon S3 static website hosting endpoint for the bucket.

For more information about specifying this value for different types of origins, see Origin Domain Name in the Amazon CloudFront Developer Guide .
Constraints for Amazon S3 origins:

If you configured Amazon S3 Transfer Acceleration for your bucket, don\'t specify the s3-accelerate endpoint for DomainName .
The bucket name must be between 3 and 63 characters long (inclusive).
The bucket name must contain only lowercase characters, numbers, periods, underscores, and dashes.
The bucket name must not contain adjacent periods.


Custom Origins : The DNS domain name for the HTTP server from which you want CloudFront to get objects for this origin, for example, www.example.com .

Constraints for custom origins:

DomainName must be a valid DNS name that contains only a-z, A-Z, 0-9, dot (.), hyphen (-), or underscore (_) characters.
The name cannot exceed 128 characters.


OriginPath (string) --
An optional element that causes CloudFront to request your content from a directory in your Amazon S3 bucket or your custom origin. When you include the OriginPath element, specify the directory name, beginning with a / . CloudFront appends the directory name to the value of DomainName , for example, example.com/production . Do not include a / at the end of the directory name.
For example, suppose you\'ve specified the following values for your distribution:

DomainName : An Amazon S3 bucket named myawsbucket .
OriginPath : /production
CNAME : example.com

When a user enters example.com/index.html in a browser, CloudFront sends a request to Amazon S3 for myawsbucket/production/index.html .
When a user enters example.com/acme/index.html in a browser, CloudFront sends a request to Amazon S3 for myawsbucket/production/acme/index.html .

CustomHeaders (dict) --
A complex type that contains names and values for the custom headers that you want.

Quantity (integer) --
The number of custom headers, if any, for this distribution.

Items (list) --

Optional : A list that contains one OriginCustomHeader element for each custom header that you want CloudFront to forward to the origin. If Quantity is 0 , omit Items .


(dict) --
A complex type that contains HeaderName and HeaderValue elements, if any, for this distribution.

HeaderName (string) --
The name of a header that you want CloudFront to forward to your origin. For more information, see Forwarding Custom Headers to Your Origin (Web Distributions Only) in the Amazon CloudFront Developer Guide .

HeaderValue (string) --
The value for the header that you specified in the HeaderName field.







S3OriginConfig (dict) --
A complex type that contains information about the Amazon S3 origin. If the origin is a custom origin, use the CustomOriginConfig element instead.

OriginAccessIdentity (string) --
The CloudFront origin access identity to associate with the origin. Use an origin access identity to configure the origin so that viewers can only access objects in an Amazon S3 bucket through CloudFront. The format of the value is:
origin-access-identity/cloudfront/ID-of-origin-access-identity
where `` ID-of-origin-access-identity `` is the value that CloudFront returned in the ID element when you created the origin access identity.
If you want viewers to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty OriginAccessIdentity element.
To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty OriginAccessIdentity element.
To replace the origin access identity, update the distribution configuration and specify the new origin access identity.
For more information about the origin access identity, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .



CustomOriginConfig (dict) --
A complex type that contains information about a custom origin. If the origin is an Amazon S3 bucket, use the S3OriginConfig element instead.

HTTPPort (integer) --
The HTTP port the custom origin listens on.

HTTPSPort (integer) --
The HTTPS port the custom origin listens on.

OriginProtocolPolicy (string) --
The origin protocol policy to apply to your origin.

OriginSslProtocols (dict) --
The SSL/TLS protocols that you want CloudFront to use when communicating with your origin over HTTPS.

Quantity (integer) --
The number of SSL/TLS protocols that you want to allow CloudFront to use when establishing an HTTPS connection with this origin.

Items (list) --
A list that contains allowed SSL/TLS protocols for this distribution.

(string) --




OriginReadTimeout (integer) --
You can create a custom origin read timeout. All timeout units are in seconds. The default origin read timeout is 30 seconds, but you can configure custom timeout lengths using the CloudFront API. The minimum timeout length is 4 seconds; the maximum is 60 seconds.
If you need to increase the maximum time limit, contact the AWS Support Center .

OriginKeepaliveTimeout (integer) --
You can create a custom keep-alive timeout. All timeout units are in seconds. The default keep-alive timeout is 5 seconds, but you can configure custom timeout lengths using the CloudFront API. The minimum timeout length is 1 second; the maximum is 60 seconds.
If you need to increase the maximum time limit, contact the AWS Support Center .









OriginGroups (dict) --
A complex type that contains information about origin groups for this distribution.

Quantity (integer) --
The number of origin groups.

Items (list) --
The items (origin groups) in a distribution.

(dict) --
An origin group includes two origins (a primary origin and a second origin to failover to) and a failover criteria that you specify. You create an origin group to support origin failover in CloudFront. When you create or update a distribution, you can specifiy the origin group instead of a single origin, and CloudFront will failover from the primary origin to the second origin under the failover conditions that you\'ve chosen.

Id (string) --
The origin group\'s ID.

FailoverCriteria (dict) --
A complex type that contains information about the failover criteria for an origin group.

StatusCodes (dict) --
The status codes that, when returned from the primary origin, will trigger CloudFront to failover to the second origin.

Quantity (integer) --
The number of status codes.

Items (list) --
The items (status codes) for an origin group.

(integer) --






Members (dict) --
A complex type that contains information about the origins in an origin group.

Quantity (integer) --
The number of origins in an origin group.

Items (list) --
Items (origins) in an origin group.

(dict) --
An origin in an origin group.

OriginId (string) --
The ID for an origin in an origin group.













DefaultCacheBehavior (dict) --
A complex type that describes the default cache behavior if you don\'t specify a CacheBehavior element or if files don\'t match any of the values of PathPattern in CacheBehavior elements. You must create exactly one default cache behavior.

TargetOriginId (string) --
The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior in your distribution.

ForwardedValues (dict) --
A complex type that specifies how CloudFront handles query strings, cookies, and HTTP headers.

QueryString (boolean) --
Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior and cache based on the query string parameters. CloudFront behavior depends on the value of QueryString and on the values that you specify for QueryStringCacheKeys , if any:
If you specify true for QueryString and you don\'t specify any values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin and caches based on all query string parameters. Depending on how many query string parameters and values you have, this can adversely affect performance because CloudFront must forward more requests to the origin.
If you specify true for QueryString and you specify one or more values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin, but it only caches based on the query string parameters that you specify.
If you specify false for QueryString , CloudFront doesn\'t forward any query string parameters to the origin, and doesn\'t cache based on query string parameters.
For more information, see Configuring CloudFront to Cache Based on Query String Parameters in the Amazon CloudFront Developer Guide .

Cookies (dict) --
A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see How CloudFront Forwards, Caches, and Logs Cookies in the Amazon CloudFront Developer Guide .

Forward (string) --
Specifies which cookies to forward to the origin for this cache behavior: all, none, or the list of cookies specified in the WhitelistedNames complex type.
Amazon S3 doesn\'t process cookies. When the cache behavior is forwarding requests to an Amazon S3 origin, specify none for the Forward element.

WhitelistedNames (dict) --
Required if you specify whitelist for the value of Forward . A complex type that specifies how many different cookies you want CloudFront to forward to the origin for this cache behavior and, if you want to forward selected cookies, the names of those cookies.
If you specify all or none for the value of Forward , omit WhitelistedNames . If you change the value of Forward from whitelist to all or none and you don\'t delete the WhitelistedNames element and its child elements, CloudFront deletes them automatically.
For the current limit on the number of cookie names that you can whitelist for each cache behavior, see CloudFront Limits in the AWS General Reference .

Quantity (integer) --
The number of different cookies that you want CloudFront to forward to the origin for this cache behavior. The value must equal the number of items that are in the Items field.
When you set Forward = whitelist (in the CookiePreferences object), this value must be 1 or higher.

Items (list) --
A complex type that contains one Name element for each cookie that you want CloudFront to forward to the origin for this cache behavior. It must contain the same number of items that is specified in the Quantity field.
When you set Forward = whitelist (in the CookiePreferences object), this field must contain at least one item.

(string) --






Headers (dict) --
A complex type that specifies the Headers , if any, that you want CloudFront to forward to the origin for this cache behavior (whitelisted headers). For the headers that you specify, CloudFront also caches separate versions of a specified object that is based on the header values in viewer requests.
For more information, see Caching Content Based on Request Headers in the Amazon CloudFront Developer Guide .

Quantity (integer) --
The number of different headers that you want CloudFront to base caching on for this cache behavior. You can configure each cache behavior in a web distribution to do one of the following:

Forward all headers to your origin : Specify 1 for Quantity and * for Name .


Warning
CloudFront doesn\'t cache the objects that are associated with this cache behavior. Instead, CloudFront sends every request to the origin.


Forward a whitelist of headers you specify : Specify the number of headers that you want CloudFront to base caching on. Then specify the header names in Name elements. CloudFront caches your objects based on the values in the specified headers.
Forward only the default headers : Specify 0 for Quantity and omit Items . In this configuration, CloudFront doesn\'t cache based on the values in the request headers.

Regardless of which option you choose, CloudFront forwards headers to your origin based on whether the origin is an S3 bucket or a custom origin. See the following documentation:

S3 bucket : See HTTP Request Headers That CloudFront Removes or Updates
Custom origin : See HTTP Request Headers and CloudFront Behavior


Items (list) --
A list that contains one Name element for each header that you want CloudFront to use for caching in this cache behavior. If Quantity is 0 , omit Items .

(string) --




QueryStringCacheKeys (dict) --
A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.

Quantity (integer) --
The number of whitelisted query string parameters for a cache behavior.

Items (list) --
A list that contains the query string parameters that you want CloudFront to use as a basis for caching for a cache behavior. If Quantity is 0, you can omit Items .

(string) --






TrustedSigners (dict) --
A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content.
If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled , and specify the applicable values for Quantity and Items . For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .
If you don\'t want to require signed URLs in requests for objects that match PathPattern , specify false for Enabled and 0 for Quantity . Omit Items .
To add, change, or remove one or more trusted signers, change Enabled to true (if it\'s currently false ), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.

Enabled (boolean) --
Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .

Quantity (integer) --
The number of trusted signers for this cache behavior.

Items (list) --

Optional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .


(string) --




ViewerProtocolPolicy (string) --
The protocol that viewers can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern . You can specify the following options:

allow-all : Viewers can use HTTP or HTTPS.
redirect-to-https : If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.
https-only : If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).

For more information about requiring the HTTPS protocol, see Using an HTTPS Connection to Access Your Objects in the Amazon CloudFront Developer Guide .

Note
The only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects\' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .


MinTTL (integer) --
The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .
You must specify 0 for MinTTL if you configure CloudFront to forward all headers to your origin (under Headers , if you specify 1 for Quantity and * for Name ).

AllowedMethods (dict) --
A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices:

CloudFront forwards only GET and HEAD requests.
CloudFront forwards only GET , HEAD , and OPTIONS requests.
CloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests.

If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can\'t perform operations that you don\'t want them to. For example, you might not want users to have permissions to delete objects from your origin.

Quantity (integer) --
The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET , HEAD , and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests).

Items (list) --
A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.

(string) --


CachedMethods (dict) --
A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices:

CloudFront caches responses to GET and HEAD requests.
CloudFront caches responses to GET , HEAD , and OPTIONS requests.

If you pick the second choice for your Amazon S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers, and Origin headers for the responses to be cached correctly.

Quantity (integer) --
The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET , HEAD , and OPTIONS requests).

Items (list) --
A complex type that contains the HTTP methods that you want CloudFront to cache responses to.

(string) --






SmoothStreaming (boolean) --
Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true ; if not, specify false . If you specify true for SmoothStreaming , you can still distribute other content using this cache behavior if the content matches the value of PathPattern .

DefaultTTL (integer) --
The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .

MaxTTL (integer) --
The maximum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .

Compress (boolean) --
Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify true ; if not, specify false . For more information, see Serving Compressed Files in the Amazon CloudFront Developer Guide .

LambdaFunctionAssociations (dict) --
A complex type that contains zero or more Lambda function associations for a cache behavior.

Quantity (integer) --
The number of Lambda function associations for this cache behavior.

Items (list) --

Optional : A complex type that contains LambdaFunctionAssociation items for this cache behavior. If Quantity is 0 , you can omit Items .


(dict) --
A complex type that contains a Lambda function association.

LambdaFunctionARN (string) --
The ARN of the Lambda function. You must specify the ARN of a function version; you can\'t specify a Lambda alias or $LATEST.

EventType (string) --
Specifies the event type that triggers a Lambda function invocation. You can specify the following values:

viewer-request : The function executes when CloudFront receives a request from a viewer and before it checks to see whether the requested object is in the edge cache.
origin-request : The function executes only when CloudFront forwards a request to your origin. When the requested object is in the edge cache, the function doesn\'t execute.
origin-response : The function executes after CloudFront receives a response from the origin and before it caches the object in the response. When the requested object is in the edge cache, the function doesn\'t execute.
viewer-response : The function executes before CloudFront returns the requested object to the viewer. The function executes regardless of whether the object was already in the edge cache. If the origin returns an HTTP status code other than HTTP 200 (OK), the function doesn\'t execute.


IncludeBody (boolean) --
A flag that allows a Lambda function to have read access to the body content. For more information, see Accessing the Request Body by Choosing the Include Body Option in the Amazon CloudFront Developer Guide.







FieldLevelEncryptionId (string) --
The value of ID for the field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data for a cache behavior or for the default cache behavior in your distribution.



CacheBehaviors (dict) --
A complex type that contains zero or more CacheBehavior elements.

Quantity (integer) --
The number of cache behaviors for this distribution.

Items (list) --
Optional: A complex type that contains cache behaviors for this distribution. If Quantity is 0 , you can omit Items .

(dict) --
A complex type that describes how CloudFront processes requests.
You must create at least as many cache behaviors (including the default cache behavior) as you have origins if you want CloudFront to distribute objects from all of the origins. Each cache behavior specifies the one origin from which you want CloudFront to get objects. If you have two origins and only the default cache behavior, the default cache behavior will cause CloudFront to get objects from one of the origins, but the other origin is never used.
For the current limit on the number of cache behaviors that you can add to a distribution, see Amazon CloudFront Limits in the AWS General Reference .
If you don\'t want to specify any cache behaviors, include only an empty CacheBehaviors element. Don\'t include an empty CacheBehavior element, or CloudFront returns a MalformedXML error.
To delete all cache behaviors in an existing distribution, update the distribution configuration and include only an empty CacheBehaviors element.
To add, change, or remove one or more cache behaviors, update the distribution configuration and specify all of the cache behaviors that you want to include in the updated distribution.
For more information about cache behaviors, see Cache Behaviors in the Amazon CloudFront Developer Guide .

PathPattern (string) --
The pattern (for example, images/*.jpg ) that specifies which requests to apply the behavior to. When CloudFront receives a viewer request, the requested path is compared with path patterns in the order in which cache behaviors are listed in the distribution.

Note
You can optionally include a slash (/ ) at the beginning of the path pattern. For example, /images/*.jpg . CloudFront behavior is the same with or without the leading / .

The path pattern for the default cache behavior is * and cannot be changed. If the request for an object does not match the path pattern for any cache behaviors, CloudFront applies the behavior in the default cache behavior.
For more information, see Path Pattern in the Amazon CloudFront Developer Guide .

TargetOriginId (string) --
The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior in your distribution.

ForwardedValues (dict) --
A complex type that specifies how CloudFront handles query strings, cookies, and HTTP headers.

QueryString (boolean) --
Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior and cache based on the query string parameters. CloudFront behavior depends on the value of QueryString and on the values that you specify for QueryStringCacheKeys , if any:
If you specify true for QueryString and you don\'t specify any values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin and caches based on all query string parameters. Depending on how many query string parameters and values you have, this can adversely affect performance because CloudFront must forward more requests to the origin.
If you specify true for QueryString and you specify one or more values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin, but it only caches based on the query string parameters that you specify.
If you specify false for QueryString , CloudFront doesn\'t forward any query string parameters to the origin, and doesn\'t cache based on query string parameters.
For more information, see Configuring CloudFront to Cache Based on Query String Parameters in the Amazon CloudFront Developer Guide .

Cookies (dict) --
A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see How CloudFront Forwards, Caches, and Logs Cookies in the Amazon CloudFront Developer Guide .

Forward (string) --
Specifies which cookies to forward to the origin for this cache behavior: all, none, or the list of cookies specified in the WhitelistedNames complex type.
Amazon S3 doesn\'t process cookies. When the cache behavior is forwarding requests to an Amazon S3 origin, specify none for the Forward element.

WhitelistedNames (dict) --
Required if you specify whitelist for the value of Forward . A complex type that specifies how many different cookies you want CloudFront to forward to the origin for this cache behavior and, if you want to forward selected cookies, the names of those cookies.
If you specify all or none for the value of Forward , omit WhitelistedNames . If you change the value of Forward from whitelist to all or none and you don\'t delete the WhitelistedNames element and its child elements, CloudFront deletes them automatically.
For the current limit on the number of cookie names that you can whitelist for each cache behavior, see CloudFront Limits in the AWS General Reference .

Quantity (integer) --
The number of different cookies that you want CloudFront to forward to the origin for this cache behavior. The value must equal the number of items that are in the Items field.
When you set Forward = whitelist (in the CookiePreferences object), this value must be 1 or higher.

Items (list) --
A complex type that contains one Name element for each cookie that you want CloudFront to forward to the origin for this cache behavior. It must contain the same number of items that is specified in the Quantity field.
When you set Forward = whitelist (in the CookiePreferences object), this field must contain at least one item.

(string) --






Headers (dict) --
A complex type that specifies the Headers , if any, that you want CloudFront to forward to the origin for this cache behavior (whitelisted headers). For the headers that you specify, CloudFront also caches separate versions of a specified object that is based on the header values in viewer requests.
For more information, see Caching Content Based on Request Headers in the Amazon CloudFront Developer Guide .

Quantity (integer) --
The number of different headers that you want CloudFront to base caching on for this cache behavior. You can configure each cache behavior in a web distribution to do one of the following:

Forward all headers to your origin : Specify 1 for Quantity and * for Name .


Warning
CloudFront doesn\'t cache the objects that are associated with this cache behavior. Instead, CloudFront sends every request to the origin.


Forward a whitelist of headers you specify : Specify the number of headers that you want CloudFront to base caching on. Then specify the header names in Name elements. CloudFront caches your objects based on the values in the specified headers.
Forward only the default headers : Specify 0 for Quantity and omit Items . In this configuration, CloudFront doesn\'t cache based on the values in the request headers.

Regardless of which option you choose, CloudFront forwards headers to your origin based on whether the origin is an S3 bucket or a custom origin. See the following documentation:

S3 bucket : See HTTP Request Headers That CloudFront Removes or Updates
Custom origin : See HTTP Request Headers and CloudFront Behavior


Items (list) --
A list that contains one Name element for each header that you want CloudFront to use for caching in this cache behavior. If Quantity is 0 , omit Items .

(string) --




QueryStringCacheKeys (dict) --
A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.

Quantity (integer) --
The number of whitelisted query string parameters for a cache behavior.

Items (list) --
A list that contains the query string parameters that you want CloudFront to use as a basis for caching for a cache behavior. If Quantity is 0, you can omit Items .

(string) --






TrustedSigners (dict) --
A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content.
If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled , and specify the applicable values for Quantity and Items . For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .
If you don\'t want to require signed URLs in requests for objects that match PathPattern , specify false for Enabled and 0 for Quantity . Omit Items .
To add, change, or remove one or more trusted signers, change Enabled to true (if it\'s currently false ), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.

Enabled (boolean) --
Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .

Quantity (integer) --
The number of trusted signers for this cache behavior.

Items (list) --

Optional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .


(string) --




ViewerProtocolPolicy (string) --
The protocol that viewers can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern . You can specify the following options:

allow-all : Viewers can use HTTP or HTTPS.
redirect-to-https : If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.
https-only : If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).

For more information about requiring the HTTPS protocol, see Using an HTTPS Connection to Access Your Objects in the Amazon CloudFront Developer Guide .

Note
The only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects\' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .


MinTTL (integer) --
The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .
You must specify 0 for MinTTL if you configure CloudFront to forward all headers to your origin (under Headers , if you specify 1 for Quantity and * for Name ).

AllowedMethods (dict) --
A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices:

CloudFront forwards only GET and HEAD requests.
CloudFront forwards only GET , HEAD , and OPTIONS requests.
CloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests.

If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can\'t perform operations that you don\'t want them to. For example, you might not want users to have permissions to delete objects from your origin.

Quantity (integer) --
The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET , HEAD , and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests).

Items (list) --
A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.

(string) --


CachedMethods (dict) --
A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices:

CloudFront caches responses to GET and HEAD requests.
CloudFront caches responses to GET , HEAD , and OPTIONS requests.

If you pick the second choice for your Amazon S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers, and Origin headers for the responses to be cached correctly.

Quantity (integer) --
The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET , HEAD , and OPTIONS requests).

Items (list) --
A complex type that contains the HTTP methods that you want CloudFront to cache responses to.

(string) --






SmoothStreaming (boolean) --
Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true ; if not, specify false . If you specify true for SmoothStreaming , you can still distribute other content using this cache behavior if the content matches the value of PathPattern .

DefaultTTL (integer) --
The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .

MaxTTL (integer) --
The maximum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Managing How Long Content Stays in an Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .

Compress (boolean) --
Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify true; if not, specify false. For more information, see Serving Compressed Files in the Amazon CloudFront Developer Guide .

LambdaFunctionAssociations (dict) --
A complex type that contains zero or more Lambda function associations for a cache behavior.

Quantity (integer) --
The number of Lambda function associations for this cache behavior.

Items (list) --

Optional : A complex type that contains LambdaFunctionAssociation items for this cache behavior. If Quantity is 0 , you can omit Items .


(dict) --
A complex type that contains a Lambda function association.

LambdaFunctionARN (string) --
The ARN of the Lambda function. You must specify the ARN of a function version; you can\'t specify a Lambda alias or $LATEST.

EventType (string) --
Specifies the event type that triggers a Lambda function invocation. You can specify the following values:

viewer-request : The function executes when CloudFront receives a request from a viewer and before it checks to see whether the requested object is in the edge cache.
origin-request : The function executes only when CloudFront forwards a request to your origin. When the requested object is in the edge cache, the function doesn\'t execute.
origin-response : The function executes after CloudFront receives a response from the origin and before it caches the object in the response. When the requested object is in the edge cache, the function doesn\'t execute.
viewer-response : The function executes before CloudFront returns the requested object to the viewer. The function executes regardless of whether the object was already in the edge cache. If the origin returns an HTTP status code other than HTTP 200 (OK), the function doesn\'t execute.


IncludeBody (boolean) --
A flag that allows a Lambda function to have read access to the body content. For more information, see Accessing the Request Body by Choosing the Include Body Option in the Amazon CloudFront Developer Guide.







FieldLevelEncryptionId (string) --
The value of ID for the field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data for a cache behavior or for the default cache behavior in your distribution.







CustomErrorResponses (dict) --
A complex type that controls the following:

Whether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.
How long CloudFront caches HTTP status codes in the 4xx and 5xx range.

For more information about custom error pages, see Customizing Error Responses in the Amazon CloudFront Developer Guide .

Quantity (integer) --
The number of HTTP status codes for which you want to specify a custom error page and/or a caching duration. If Quantity is 0 , you can omit Items .

Items (list) --
A complex type that contains a CustomErrorResponse element for each HTTP status code for which you want to specify a custom error page and/or a caching duration.

(dict) --
A complex type that controls:

Whether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.
How long CloudFront caches HTTP status codes in the 4xx and 5xx range.

For more information about custom error pages, see Customizing Error Responses in the Amazon CloudFront Developer Guide .

ErrorCode (integer) --
The HTTP status code for which you want to specify a custom error page and/or a caching duration.

ResponsePagePath (string) --
The path to the custom error page that you want CloudFront to return to a viewer when your origin returns the HTTP status code specified by ErrorCode , for example, /4xx-errors/403-forbidden.html . If you want to store your objects and your custom error pages in different locations, your distribution must include a cache behavior for which the following is true:

The value of PathPattern matches the path to your custom error messages. For example, suppose you saved custom error pages for 4xx errors in an Amazon S3 bucket in a directory named /4xx-errors . Your distribution must include a cache behavior for which the path pattern routes requests for your custom error pages to that location, for example, /4xx-errors/* .
The value of TargetOriginId specifies the value of the ID element for the origin that contains your custom error pages.

If you specify a value for ResponsePagePath , you must also specify a value for ResponseCode .
We recommend that you store custom error pages in an Amazon S3 bucket. If you store custom error pages on an HTTP server and the server starts to return 5xx errors, CloudFront can\'t get the files that you want to return to viewers because the origin server is unavailable.

ResponseCode (string) --
The HTTP status code that you want CloudFront to return to the viewer along with the custom error page. There are a variety of reasons that you might want CloudFront to return a status code different from the status code that your origin returned to CloudFront, for example:

Some Internet devices (some firewalls and corporate proxies, for example) intercept HTTP 4xx and 5xx and prevent the response from being returned to the viewer. If you substitute 200 , the response typically won\'t be intercepted.
If you don\'t care about distinguishing among different client errors or server errors, you can specify 400 or 500 as the ResponseCode for all 4xx or 5xx errors.
You might want to return a 200 status code (OK) and static website so your customers don\'t know that your website is down.

If you specify a value for ResponseCode , you must also specify a value for ResponsePagePath .

ErrorCachingMinTTL (integer) --
The minimum amount of time, in seconds, that you want CloudFront to cache the HTTP status code specified in ErrorCode . When this time period has elapsed, CloudFront queries your origin to see whether the problem that caused the error has been resolved and the requested object is now available.
For more information, see Customizing Error Responses in the Amazon CloudFront Developer Guide .







Comment (string) --
Any comments you want to include about the distribution.
If you don\'t want to specify a comment, include an empty Comment element.
To delete an existing comment, update the distribution configuration and include an empty Comment element.
To add or change a comment, update the distribution configuration and specify the new comment.

Logging (dict) --
A complex type that controls whether access logs are written for the distribution.
For more information about logging, see Access Logs in the Amazon CloudFront Developer Guide .

Enabled (boolean) --
Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you don\'t want to enable logging when you create a distribution or if you want to disable logging for an existing distribution, specify false for Enabled , and specify empty Bucket and Prefix elements. If you specify false for Enabled but you specify values for Bucket , prefix , and IncludeCookies , the values are automatically deleted.

IncludeCookies (boolean) --
Specifies whether you want CloudFront to include cookies in access logs, specify true for IncludeCookies . If you choose to include cookies in logs, CloudFront logs all cookies regardless of how you configure the cache behaviors for this distribution. If you don\'t want to include cookies when you create a distribution or if you want to disable include cookies for an existing distribution, specify false for IncludeCookies .

Bucket (string) --
The Amazon S3 bucket to store the access logs in, for example, myawslogbucket.s3.amazonaws.com .

Prefix (string) --
An optional string that you want CloudFront to prefix to the access log filenames for this distribution, for example, myprefix/ . If you want to enable logging, but you don\'t want to specify a prefix, you still must include an empty Prefix element in the Logging element.



PriceClass (string) --
The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify PriceClass_All , CloudFront responds to requests for your objects from all CloudFront edge locations.
If you specify a price class other than PriceClass_All , CloudFront serves your objects from the CloudFront edge location that has the lowest latency among the edge locations in your price class. Viewers who are in or near regions that are excluded from your specified price class may encounter slower performance.
For more information about price classes, see Choosing the Price Class for a CloudFront Distribution in the Amazon CloudFront Developer Guide . For information about CloudFront pricing, including how price classes (such as Price Class 100) map to CloudFront regions, see Amazon CloudFront Pricing . For price class information, scroll down to see the table at the bottom of the page.

Enabled (boolean) --
From this field, you can enable or disable the selected distribution.

ViewerCertificate (dict) --
A complex type that determines the distribution\xe2\x80\x99s SSL/TLS configuration for communicating with viewers.

CloudFrontDefaultCertificate (boolean) --
If the distribution uses the CloudFront domain name such as d111111abcdef8.cloudfront.net , set this field to true .
If the distribution uses Aliases (alternate domain names or CNAMEs), set this field to false and specify values for the following fields:

ACMCertificateArn or IAMCertificateId (specify a value for one, not both)
MinimumProtocolVersion
SSLSupportMethod


IAMCertificateId (string) --
If the distribution uses Aliases (alternate domain names or CNAMEs) and the SSL/TLS certificate is stored in AWS Identity and Access Management (AWS IAM) , provide the ID of the IAM certificate.
If you specify an IAM certificate ID, you must also specify values for MinimumProtocolVerison and SSLSupportMethod .

ACMCertificateArn (string) --
If the distribution uses Aliases (alternate domain names or CNAMEs) and the SSL/TLS certificate is stored in AWS Certificate Manager (ACM) , provide the Amazon Resource Name (ARN) of the ACM certificate. CloudFront only supports ACM certificates in the US East (N. Virginia) Region (us-east-1 ).
If you specify an ACM certificate ARN, you must also specify values for MinimumProtocolVerison and SSLSupportMethod .

SSLSupportMethod (string) --
If the distribution uses Aliases (alternate domain names or CNAMEs), specify which viewers the distribution accepts HTTPS connections from.

sni-only \xe2\x80\x93 The distribution accepts HTTPS connections from only viewers that support server name indication (SNI) . This is recommended. Most browsers and clients released after 2010 support SNI.
vip \xe2\x80\x93 The distribution accepts HTTPS connections from all viewers including those that don\xe2\x80\x99t support SNI. This is not recommended, and results in additional monthly charges from CloudFront.

If the distribution uses the CloudFront domain name such as d111111abcdef8.cloudfront.net , don\xe2\x80\x99t set a value for this field.

MinimumProtocolVersion (string) --
If the distribution uses Aliases (alternate domain names or CNAMEs), specify the security policy that you want CloudFront to use for HTTPS connections with viewers. The security policy determines two settings:

The minimum SSL/TLS protocol that CloudFront can use to communicate with viewers.
The ciphers that CloudFront can use to encrypt the content that it returns to viewers.

For more information, see Security Policy and Supported Protocols and Ciphers Between Viewers and CloudFront in the Amazon CloudFront Developer Guide .

Note
On the CloudFront console, this setting is called Security Policy .

We recommend that you specify TLSv1.2_2018 unless your viewers are using browsers or devices that don\xe2\x80\x99t support TLSv1.2.
When you\xe2\x80\x99re using SNI only (you set SSLSupportMethod to sni-only ), you must specify TLSv1 or higher.
If the distribution uses the CloudFront domain name such as d111111abcdef8.cloudfront.net (you set CloudFrontDefaultCertificate to true ), CloudFront automatically sets the security policy to TLSv1 regardless of the value that you set here.

Certificate (string) --
This field is deprecated. Use one of the following fields instead:

ACMCertificateArn
IAMCertificateId
CloudFrontDefaultCertificate


CertificateSource (string) --
This field is deprecated. Use one of the following fields instead:

ACMCertificateArn
IAMCertificateId
CloudFrontDefaultCertificate




Restrictions (dict) --
A complex type that identifies ways in which you want to restrict distribution of your content.

GeoRestriction (dict) --
A complex type that controls the countries in which your content is distributed. CloudFront determines the location of your users using MaxMind GeoIP databases.

RestrictionType (string) --
The method that you want to use to restrict distribution of your content by country:

none : No geo restriction is enabled, meaning access to content is not restricted by client geo location.
blacklist : The Location elements specify the countries in which you don\'t want CloudFront to distribute your content.
whitelist : The Location elements specify the countries in which you want CloudFront to distribute your content.


Quantity (integer) --
When geo restriction is enabled , this is the number of countries in your whitelist or blacklist . Otherwise, when it is not enabled, Quantity is 0 , and you can omit Items .

Items (list) --
A complex type that contains a Location element for each country in which you want CloudFront either to distribute your content (whitelist ) or not distribute your content (blacklist ).
The Location element is a two-letter, uppercase country code for a country that you want to include in your blacklist or whitelist . Include one Location element for each country.
CloudFront and MaxMind both use ISO 3166 country codes. For the current list of countries and the corresponding codes, see ISO 3166-1-alpha-2 code on the International Organization for Standardization website. You can also refer to the country list on the CloudFront console, which includes both country names and codes.

(string) --






WebACLId (string) --
A unique identifier that specifies the AWS WAF web ACL, if any, to associate with this distribution. To specify a web ACL created using the latest version of AWS WAF, use the ACL ARN, for example arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/473e64fd-f30b-4765-81a0-62ad96dd167a . To specify a web ACL created using AWS WAF Classic, use the ACL ID, for example 473e64fd-f30b-4765-81a0-62ad96dd167a .
AWS WAF is a web application firewall that lets you monitor the HTTP and HTTPS requests that are forwarded to CloudFront, and lets you control access to your content. Based on conditions that you specify, such as the IP addresses that requests originate from or the values of query strings, CloudFront responds to requests either with the requested content or with an HTTP 403 status code (Forbidden). You can also configure CloudFront to return a custom error page when a request is blocked. For more information about AWS WAF, see the AWS WAF Developer Guide .

HttpVersion (string) --
(Optional) Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront. The default value for new web distributions is http2. Viewers that don\'t support HTTP/2 automatically use an earlier HTTP version.
For viewers and CloudFront to use HTTP/2, viewers must support TLS 1.2 or later, and must support Server Name Identification (SNI).
In general, configuring CloudFront to communicate with viewers using HTTP/2 reduces latency. You can improve performance by optimizing for HTTP/2. For more information, do an Internet search for "http/2 optimization."

IsIPV6Enabled (boolean) --
If you want CloudFront to respond to IPv6 DNS requests with an IPv6 address for your distribution, specify true . If you specify false , CloudFront responds to IPv6 DNS requests with the DNS response code NOERROR and with no IP addresses. This allows viewers to submit a second request, for an IPv4 address for your distribution.
In general, you should enable IPv6 if you have users on IPv6 networks who want to access your content. However, if you\'re using signed URLs or signed cookies to restrict access to your content, and if you\'re using a custom policy that includes the IpAddress parameter to restrict the IP addresses that can access your content, don\'t enable IPv6. If you want to restrict access to some content by IP address and not restrict access to other content (or restrict access but not by IP address), you can create two distributions. For more information, see Creating a Signed URL Using a Custom Policy in the Amazon CloudFront Developer Guide .
If you\'re using an Amazon Route 53 alias resource record set to route traffic to your CloudFront distribution, you need to create a second alias resource record set when both of the following are true:

You enable IPv6 for the distribution
You\'re using alternate domain names in the URLs for your objects

For more information, see Routing Traffic to an Amazon CloudFront Web Distribution by Using Your Domain Name in the Amazon Route 53 Developer Guide .
If you created a CNAME resource record set, either with Amazon Route 53 or with another DNS service, you don\'t need to make any changes. A CNAME record will route traffic to your distribution regardless of the IP address format of the viewer request.



AliasICPRecordals (list) --
AWS services in China customers must file for an Internet Content Provider (ICP) recordal if they want to serve content publicly on an alternate domain name, also known as a CNAME, that they\'ve added to CloudFront. AliasICPRecordal provides the ICP recordal status for CNAMEs associated with distributions.
For more information about ICP recordals, see Signup, Accounts, and Credentials in Getting Started with AWS services in China .

(dict) --
AWS services in China customers must file for an Internet Content Provider (ICP) recordal if they want to serve content publicly on an alternate domain name, also known as a CNAME, that they\'ve added to CloudFront. AliasICPRecordal provides the ICP recordal status for CNAMEs associated with distributions. The status is returned in the CloudFront response; you can\'t configure it yourself.
For more information about ICP recordals, see Signup, Accounts, and Credentials in Getting Started with AWS services in China .

CNAME (string) --
A domain name associated with a distribution.

ICPRecordalStatus (string) --
The Internet Content Provider (ICP) recordal status for a CNAME. The ICPRecordalStatus is set to APPROVED for all CNAMEs (aliases) in regions outside of China.
The status values returned are the following:

APPROVED indicates that the associated CNAME has a valid ICP recordal number. Multiple CNAMEs can be associated with a distribution, and CNAMEs can correspond to different ICP recordals. To be marked as APPROVED, that is, valid to use with China region, a CNAME must have one ICP recordal number associated with it.
SUSPENDED indicates that the associated CNAME does not have a valid ICP recordal number.
PENDING indicates that CloudFront can\'t determine the ICP recordal status of the CNAME associated with the distribution because there was an error in trying to determine the status. You can try again to see if the error is resolved in which case CloudFront returns an APPROVED or SUSPENDED status.








ETag (string) --
The current version of the configuration. For example: E2QWRUHAPOMQZL .







Exceptions

CloudFront.Client.exceptions.AccessDenied
CloudFront.Client.exceptions.CNAMEAlreadyExists
CloudFront.Client.exceptions.IllegalUpdate
CloudFront.Client.exceptions.InvalidIfMatchVersion
CloudFront.Client.exceptions.MissingBody
CloudFront.Client.exceptions.NoSuchDistribution
CloudFront.Client.exceptions.PreconditionFailed
CloudFront.Client.exceptions.TooManyDistributionCNAMEs
CloudFront.Client.exceptions.InvalidDefaultRootObject
CloudFront.Client.exceptions.InvalidRelativePath
CloudFront.Client.exceptions.InvalidErrorCode
CloudFront.Client.exceptions.InvalidResponseCode
CloudFront.Client.exceptions.InvalidArgument
CloudFront.Client.exceptions.InvalidOriginAccessIdentity
CloudFront.Client.exceptions.TooManyTrustedSigners
CloudFront.Client.exceptions.TrustedSignerDoesNotExist
CloudFront.Client.exceptions.InvalidViewerCertificate
CloudFront.Client.exceptions.InvalidMinimumProtocolVersion
CloudFront.Client.exceptions.InvalidRequiredProtocol
CloudFront.Client.exceptions.NoSuchOrigin
CloudFront.Client.exceptions.TooManyOrigins
CloudFront.Client.exceptions.TooManyOriginGroupsPerDistribution
CloudFront.Client.exceptions.TooManyCacheBehaviors
CloudFront.Client.exceptions.TooManyCookieNamesInWhiteList
CloudFront.Client.exceptions.InvalidForwardCookies
CloudFront.Client.exceptions.TooManyHeadersInForwardedValues
CloudFront.Client.exceptions.InvalidHeadersForS3Origin
CloudFront.Client.exceptions.InconsistentQuantities
CloudFront.Client.exceptions.TooManyCertificates
CloudFront.Client.exceptions.InvalidLocationCode
CloudFront.Client.exceptions.InvalidGeoRestrictionParameter
CloudFront.Client.exceptions.InvalidTTLOrder
CloudFront.Client.exceptions.InvalidWebACLId
CloudFront.Client.exceptions.TooManyOriginCustomHeaders
CloudFront.Client.exceptions.TooManyQueryStringParameters
CloudFront.Client.exceptions.InvalidQueryStringParameters
CloudFront.Client.exceptions.TooManyDistributionsWithLambdaAssociations
CloudFront.Client.exceptions.TooManyLambdaFunctionAssociations
CloudFront.Client.exceptions.InvalidLambdaFunctionAssociation
CloudFront.Client.exceptions.InvalidOriginReadTimeout
CloudFront.Client.exceptions.InvalidOriginKeepaliveTimeout
CloudFront.Client.exceptions.NoSuchFieldLevelEncryptionConfig
CloudFront.Client.exceptions.IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior
CloudFront.Client.exceptions.TooManyDistributionsAssociatedToFieldLevelEncryptionConfig


    :return: {
        'Distribution': {
            'Id': 'string',
            'ARN': 'string',
            'Status': 'string',
            'LastModifiedTime': datetime(2015, 1, 1),
            'InProgressInvalidationBatches': 123,
            'DomainName': 'string',
            'ActiveTrustedSigners': {
                'Enabled': True|False,
                'Quantity': 123,
                'Items': [
                    {
                        'AwsAccountNumber': 'string',
                        'KeyPairIds': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                ]
            },
            'DistributionConfig': {
                'CallerReference': 'string',
                'Aliases': {
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'DefaultRootObject': 'string',
                'Origins': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'Id': 'string',
                            'DomainName': 'string',
                            'OriginPath': 'string',
                            'CustomHeaders': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'HeaderName': 'string',
                                        'HeaderValue': 'string'
                                    },
                                ]
                            },
                            'S3OriginConfig': {
                                'OriginAccessIdentity': 'string'
                            },
                            'CustomOriginConfig': {
                                'HTTPPort': 123,
                                'HTTPSPort': 123,
                                'OriginProtocolPolicy': 'http-only'|'match-viewer'|'https-only',
                                'OriginSslProtocols': {
                                    'Quantity': 123,
                                    'Items': [
                                        'SSLv3'|'TLSv1'|'TLSv1.1'|'TLSv1.2',
                                    ]
                                },
                                'OriginReadTimeout': 123,
                                'OriginKeepaliveTimeout': 123
                            }
                        },
                    ]
                },
                'OriginGroups': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'Id': 'string',
                            'FailoverCriteria': {
                                'StatusCodes': {
                                    'Quantity': 123,
                                    'Items': [
                                        123,
                                    ]
                                }
                            },
                            'Members': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'OriginId': 'string'
                                    },
                                ]
                            }
                        },
                    ]
                },
                'DefaultCacheBehavior': {
                    'TargetOriginId': 'string',
                    'ForwardedValues': {
                        'QueryString': True|False,
                        'Cookies': {
                            'Forward': 'none'|'whitelist'|'all',
                            'WhitelistedNames': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                        'Headers': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        },
                        'QueryStringCacheKeys': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                    'TrustedSigners': {
                        'Enabled': True|False,
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    },
                    'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                    'MinTTL': 123,
                    'AllowedMethods': {
                        'Quantity': 123,
                        'Items': [
                            'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                        ],
                        'CachedMethods': {
                            'Quantity': 123,
                            'Items': [
                                'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                            ]
                        }
                    },
                    'SmoothStreaming': True|False,
                    'DefaultTTL': 123,
                    'MaxTTL': 123,
                    'Compress': True|False,
                    'LambdaFunctionAssociations': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'LambdaFunctionARN': 'string',
                                'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                'IncludeBody': True|False
                            },
                        ]
                    },
                    'FieldLevelEncryptionId': 'string'
                },
                'CacheBehaviors': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'PathPattern': 'string',
                            'TargetOriginId': 'string',
                            'ForwardedValues': {
                                'QueryString': True|False,
                                'Cookies': {
                                    'Forward': 'none'|'whitelist'|'all',
                                    'WhitelistedNames': {
                                        'Quantity': 123,
                                        'Items': [
                                            'string',
                                        ]
                                    }
                                },
                                'Headers': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                },
                                'QueryStringCacheKeys': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                }
                            },
                            'TrustedSigners': {
                                'Enabled': True|False,
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            },
                            'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                            'MinTTL': 123,
                            'AllowedMethods': {
                                'Quantity': 123,
                                'Items': [
                                    'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                ],
                                'CachedMethods': {
                                    'Quantity': 123,
                                    'Items': [
                                        'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                    ]
                                }
                            },
                            'SmoothStreaming': True|False,
                            'DefaultTTL': 123,
                            'MaxTTL': 123,
                            'Compress': True|False,
                            'LambdaFunctionAssociations': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'LambdaFunctionARN': 'string',
                                        'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                        'IncludeBody': True|False
                                    },
                                ]
                            },
                            'FieldLevelEncryptionId': 'string'
                        },
                    ]
                },
                'CustomErrorResponses': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'ErrorCode': 123,
                            'ResponsePagePath': 'string',
                            'ResponseCode': 'string',
                            'ErrorCachingMinTTL': 123
                        },
                    ]
                },
                'Comment': 'string',
                'Logging': {
                    'Enabled': True|False,
                    'IncludeCookies': True|False,
                    'Bucket': 'string',
                    'Prefix': 'string'
                },
                'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
                'Enabled': True|False,
                'ViewerCertificate': {
                    'CloudFrontDefaultCertificate': True|False,
                    'IAMCertificateId': 'string',
                    'ACMCertificateArn': 'string',
                    'SSLSupportMethod': 'sni-only'|'vip',
                    'MinimumProtocolVersion': 'SSLv3'|'TLSv1'|'TLSv1_2016'|'TLSv1.1_2016'|'TLSv1.2_2018',
                    'Certificate': 'string',
                    'CertificateSource': 'cloudfront'|'iam'|'acm'
                },
                'Restrictions': {
                    'GeoRestriction': {
                        'RestrictionType': 'blacklist'|'whitelist'|'none',
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    }
                },
                'WebACLId': 'string',
                'HttpVersion': 'http1.1'|'http2',
                'IsIPV6Enabled': True|False
            },
            'AliasICPRecordals': [
                {
                    'CNAME': 'string',
                    'ICPRecordalStatus': 'APPROVED'|'SUSPENDED'|'PENDING'
                },
            ]
        },
        'ETag': 'string'
    }
    
    
    :returns: 
    Update the XML document that was returned in the response to your GetDistributionConfig request to include your changes.
    
    """
    pass

def update_field_level_encryption_config(FieldLevelEncryptionConfig=None, Id=None, IfMatch=None):
    """
    Update a field-level encryption configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_field_level_encryption_config(
        FieldLevelEncryptionConfig={
            'CallerReference': 'string',
            'Comment': 'string',
            'QueryArgProfileConfig': {
                'ForwardWhenQueryArgProfileIsUnknown': True|False,
                'QueryArgProfiles': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'QueryArg': 'string',
                            'ProfileId': 'string'
                        },
                    ]
                }
            },
            'ContentTypeProfileConfig': {
                'ForwardWhenContentTypeIsUnknown': True|False,
                'ContentTypeProfiles': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'Format': 'URLEncoded',
                            'ProfileId': 'string',
                            'ContentType': 'string'
                        },
                    ]
                }
            }
        },
        Id='string',
        IfMatch='string'
    )
    
    
    :type FieldLevelEncryptionConfig: dict
    :param FieldLevelEncryptionConfig: [REQUIRED]\nRequest to update a field-level encryption configuration.\n\nCallerReference (string) -- [REQUIRED]A unique number that ensures the request can\'t be replayed.\n\nComment (string) --An optional comment about the configuration.\n\nQueryArgProfileConfig (dict) --A complex data type that specifies when to forward content if a profile isn\'t found and the profile that can be provided as a query argument in a request.\n\nForwardWhenQueryArgProfileIsUnknown (boolean) -- [REQUIRED]Flag to set if you want a request to be forwarded to the origin even if the profile specified by the field-level encryption query argument, fle-profile, is unknown.\n\nQueryArgProfiles (dict) --Profiles specified for query argument-profile mapping for field-level encryption.\n\nQuantity (integer) -- [REQUIRED]Number of profiles for query argument-profile mapping for field-level encryption.\n\nItems (list) --Number of items for query argument-profile mapping for field-level encryption.\n\n(dict) --Query argument-profile mapping for field-level encryption.\n\nQueryArg (string) -- [REQUIRED]Query argument for field-level encryption query argument-profile mapping.\n\nProfileId (string) -- [REQUIRED]ID of profile to use for field-level encryption query argument-profile mapping\n\n\n\n\n\n\n\n\n\nContentTypeProfileConfig (dict) --A complex data type that specifies when to forward content if a content type isn\'t recognized and profiles to use as by default in a request if a query argument doesn\'t specify a profile to use.\n\nForwardWhenContentTypeIsUnknown (boolean) -- [REQUIRED]The setting in a field-level encryption content type-profile mapping that specifies what to do when an unknown content type is provided for the profile. If true, content is forwarded without being encrypted when the content type is unknown. If false (the default), an error is returned when the content type is unknown.\n\nContentTypeProfiles (dict) --The configuration for a field-level encryption content type-profile.\n\nQuantity (integer) -- [REQUIRED]The number of field-level encryption content type-profile mappings.\n\nItems (list) --Items in a field-level encryption content type-profile mapping.\n\n(dict) --A field-level encryption content type profile.\n\nFormat (string) -- [REQUIRED]The format for a field-level encryption content type-profile mapping.\n\nProfileId (string) --The profile ID for a field-level encryption content type-profile mapping.\n\nContentType (string) -- [REQUIRED]The content type for a field-level encryption content type-profile mapping.\n\n\n\n\n\n\n\n\n\n\n

    :type Id: string
    :param Id: [REQUIRED]\nThe ID of the configuration you want to update.\n

    :type IfMatch: string
    :param IfMatch: The value of the ETag header that you received when retrieving the configuration identity to update. For example: E2QWRUHAPOMQZL .

    :rtype: dict

ReturnsResponse Syntax
{
    'FieldLevelEncryption': {
        'Id': 'string',
        'LastModifiedTime': datetime(2015, 1, 1),
        'FieldLevelEncryptionConfig': {
            'CallerReference': 'string',
            'Comment': 'string',
            'QueryArgProfileConfig': {
                'ForwardWhenQueryArgProfileIsUnknown': True|False,
                'QueryArgProfiles': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'QueryArg': 'string',
                            'ProfileId': 'string'
                        },
                    ]
                }
            },
            'ContentTypeProfileConfig': {
                'ForwardWhenContentTypeIsUnknown': True|False,
                'ContentTypeProfiles': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'Format': 'URLEncoded',
                            'ProfileId': 'string',
                            'ContentType': 'string'
                        },
                    ]
                }
            }
        }
    },
    'ETag': 'string'
}


Response Structure

(dict) --

FieldLevelEncryption (dict) --
Return the results of updating the configuration.

Id (string) --
The configuration ID for a field-level encryption configuration which includes a set of profiles that specify certain selected data fields to be encrypted by specific public keys.

LastModifiedTime (datetime) --
The last time the field-level encryption configuration was changed.

FieldLevelEncryptionConfig (dict) --
A complex data type that includes the profile configurations specified for field-level encryption.

CallerReference (string) --
A unique number that ensures the request can\'t be replayed.

Comment (string) --
An optional comment about the configuration.

QueryArgProfileConfig (dict) --
A complex data type that specifies when to forward content if a profile isn\'t found and the profile that can be provided as a query argument in a request.

ForwardWhenQueryArgProfileIsUnknown (boolean) --
Flag to set if you want a request to be forwarded to the origin even if the profile specified by the field-level encryption query argument, fle-profile, is unknown.

QueryArgProfiles (dict) --
Profiles specified for query argument-profile mapping for field-level encryption.

Quantity (integer) --
Number of profiles for query argument-profile mapping for field-level encryption.

Items (list) --
Number of items for query argument-profile mapping for field-level encryption.

(dict) --
Query argument-profile mapping for field-level encryption.

QueryArg (string) --
Query argument for field-level encryption query argument-profile mapping.

ProfileId (string) --
ID of profile to use for field-level encryption query argument-profile mapping









ContentTypeProfileConfig (dict) --
A complex data type that specifies when to forward content if a content type isn\'t recognized and profiles to use as by default in a request if a query argument doesn\'t specify a profile to use.

ForwardWhenContentTypeIsUnknown (boolean) --
The setting in a field-level encryption content type-profile mapping that specifies what to do when an unknown content type is provided for the profile. If true, content is forwarded without being encrypted when the content type is unknown. If false (the default), an error is returned when the content type is unknown.

ContentTypeProfiles (dict) --
The configuration for a field-level encryption content type-profile.

Quantity (integer) --
The number of field-level encryption content type-profile mappings.

Items (list) --
Items in a field-level encryption content type-profile mapping.

(dict) --
A field-level encryption content type profile.

Format (string) --
The format for a field-level encryption content type-profile mapping.

ProfileId (string) --
The profile ID for a field-level encryption content type-profile mapping.

ContentType (string) --
The content type for a field-level encryption content type-profile mapping.













ETag (string) --
The value of the ETag header that you received when updating the configuration. For example: E2QWRUHAPOMQZL .







Exceptions

CloudFront.Client.exceptions.AccessDenied
CloudFront.Client.exceptions.IllegalUpdate
CloudFront.Client.exceptions.InconsistentQuantities
CloudFront.Client.exceptions.InvalidArgument
CloudFront.Client.exceptions.InvalidIfMatchVersion
CloudFront.Client.exceptions.NoSuchFieldLevelEncryptionProfile
CloudFront.Client.exceptions.NoSuchFieldLevelEncryptionConfig
CloudFront.Client.exceptions.PreconditionFailed
CloudFront.Client.exceptions.TooManyFieldLevelEncryptionQueryArgProfiles
CloudFront.Client.exceptions.TooManyFieldLevelEncryptionContentTypeProfiles
CloudFront.Client.exceptions.QueryArgProfileEmpty


    :return: {
        'FieldLevelEncryption': {
            'Id': 'string',
            'LastModifiedTime': datetime(2015, 1, 1),
            'FieldLevelEncryptionConfig': {
                'CallerReference': 'string',
                'Comment': 'string',
                'QueryArgProfileConfig': {
                    'ForwardWhenQueryArgProfileIsUnknown': True|False,
                    'QueryArgProfiles': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'QueryArg': 'string',
                                'ProfileId': 'string'
                            },
                        ]
                    }
                },
                'ContentTypeProfileConfig': {
                    'ForwardWhenContentTypeIsUnknown': True|False,
                    'ContentTypeProfiles': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'Format': 'URLEncoded',
                                'ProfileId': 'string',
                                'ContentType': 'string'
                            },
                        ]
                    }
                }
            }
        },
        'ETag': 'string'
    }
    
    
    :returns: 
    CloudFront.Client.exceptions.AccessDenied
    CloudFront.Client.exceptions.IllegalUpdate
    CloudFront.Client.exceptions.InconsistentQuantities
    CloudFront.Client.exceptions.InvalidArgument
    CloudFront.Client.exceptions.InvalidIfMatchVersion
    CloudFront.Client.exceptions.NoSuchFieldLevelEncryptionProfile
    CloudFront.Client.exceptions.NoSuchFieldLevelEncryptionConfig
    CloudFront.Client.exceptions.PreconditionFailed
    CloudFront.Client.exceptions.TooManyFieldLevelEncryptionQueryArgProfiles
    CloudFront.Client.exceptions.TooManyFieldLevelEncryptionContentTypeProfiles
    CloudFront.Client.exceptions.QueryArgProfileEmpty
    
    """
    pass

def update_field_level_encryption_profile(FieldLevelEncryptionProfileConfig=None, Id=None, IfMatch=None):
    """
    Update a field-level encryption profile.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_field_level_encryption_profile(
        FieldLevelEncryptionProfileConfig={
            'Name': 'string',
            'CallerReference': 'string',
            'Comment': 'string',
            'EncryptionEntities': {
                'Quantity': 123,
                'Items': [
                    {
                        'PublicKeyId': 'string',
                        'ProviderId': 'string',
                        'FieldPatterns': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                ]
            }
        },
        Id='string',
        IfMatch='string'
    )
    
    
    :type FieldLevelEncryptionProfileConfig: dict
    :param FieldLevelEncryptionProfileConfig: [REQUIRED]\nRequest to update a field-level encryption profile.\n\nName (string) -- [REQUIRED]Profile name for the field-level encryption profile.\n\nCallerReference (string) -- [REQUIRED]A unique number that ensures that the request can\'t be replayed.\n\nComment (string) --An optional comment for the field-level encryption profile.\n\nEncryptionEntities (dict) -- [REQUIRED]A complex data type of encryption entities for the field-level encryption profile that include the public key ID, provider, and field patterns for specifying which fields to encrypt with this key.\n\nQuantity (integer) -- [REQUIRED]Number of field pattern items in a field-level encryption content type-profile mapping.\n\nItems (list) --An array of field patterns in a field-level encryption content type-profile mapping.\n\n(dict) --Complex data type for field-level encryption profiles that includes the encryption key and field pattern specifications.\n\nPublicKeyId (string) -- [REQUIRED]The public key associated with a set of field-level encryption patterns, to be used when encrypting the fields that match the patterns.\n\nProviderId (string) -- [REQUIRED]The provider associated with the public key being used for encryption. This value must also be provided with the private key for applications to be able to decrypt data.\n\nFieldPatterns (dict) -- [REQUIRED]Field patterns in a field-level encryption content type profile specify the fields that you want to be encrypted. You can provide the full field name, or any beginning characters followed by a wildcard (*). You can\'t overlap field patterns. For example, you can\'t have both ABC* and AB*. Note that field patterns are case-sensitive.\n\nQuantity (integer) -- [REQUIRED]The number of field-level encryption field patterns.\n\nItems (list) --An array of the field-level encryption field patterns.\n\n(string) --\n\n\n\n\n\n\n\n\n\n\n\n

    :type Id: string
    :param Id: [REQUIRED]\nThe ID of the field-level encryption profile request.\n

    :type IfMatch: string
    :param IfMatch: The value of the ETag header that you received when retrieving the profile identity to update. For example: E2QWRUHAPOMQZL .

    :rtype: dict

ReturnsResponse Syntax
{
    'FieldLevelEncryptionProfile': {
        'Id': 'string',
        'LastModifiedTime': datetime(2015, 1, 1),
        'FieldLevelEncryptionProfileConfig': {
            'Name': 'string',
            'CallerReference': 'string',
            'Comment': 'string',
            'EncryptionEntities': {
                'Quantity': 123,
                'Items': [
                    {
                        'PublicKeyId': 'string',
                        'ProviderId': 'string',
                        'FieldPatterns': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                ]
            }
        }
    },
    'ETag': 'string'
}


Response Structure

(dict) --

FieldLevelEncryptionProfile (dict) --
Return the results of updating the profile.

Id (string) --
The ID for a field-level encryption profile configuration which includes a set of profiles that specify certain selected data fields to be encrypted by specific public keys.

LastModifiedTime (datetime) --
The last time the field-level encryption profile was updated.

FieldLevelEncryptionProfileConfig (dict) --
A complex data type that includes the profile name and the encryption entities for the field-level encryption profile.

Name (string) --
Profile name for the field-level encryption profile.

CallerReference (string) --
A unique number that ensures that the request can\'t be replayed.

Comment (string) --
An optional comment for the field-level encryption profile.

EncryptionEntities (dict) --
A complex data type of encryption entities for the field-level encryption profile that include the public key ID, provider, and field patterns for specifying which fields to encrypt with this key.

Quantity (integer) --
Number of field pattern items in a field-level encryption content type-profile mapping.

Items (list) --
An array of field patterns in a field-level encryption content type-profile mapping.

(dict) --
Complex data type for field-level encryption profiles that includes the encryption key and field pattern specifications.

PublicKeyId (string) --
The public key associated with a set of field-level encryption patterns, to be used when encrypting the fields that match the patterns.

ProviderId (string) --
The provider associated with the public key being used for encryption. This value must also be provided with the private key for applications to be able to decrypt data.

FieldPatterns (dict) --
Field patterns in a field-level encryption content type profile specify the fields that you want to be encrypted. You can provide the full field name, or any beginning characters followed by a wildcard (*). You can\'t overlap field patterns. For example, you can\'t have both ABC* and AB*. Note that field patterns are case-sensitive.

Quantity (integer) --
The number of field-level encryption field patterns.

Items (list) --
An array of the field-level encryption field patterns.

(string) --














ETag (string) --
The result of the field-level encryption profile request.







Exceptions

CloudFront.Client.exceptions.AccessDenied
CloudFront.Client.exceptions.FieldLevelEncryptionProfileAlreadyExists
CloudFront.Client.exceptions.IllegalUpdate
CloudFront.Client.exceptions.InconsistentQuantities
CloudFront.Client.exceptions.InvalidArgument
CloudFront.Client.exceptions.InvalidIfMatchVersion
CloudFront.Client.exceptions.NoSuchPublicKey
CloudFront.Client.exceptions.NoSuchFieldLevelEncryptionProfile
CloudFront.Client.exceptions.PreconditionFailed
CloudFront.Client.exceptions.FieldLevelEncryptionProfileSizeExceeded
CloudFront.Client.exceptions.TooManyFieldLevelEncryptionEncryptionEntities
CloudFront.Client.exceptions.TooManyFieldLevelEncryptionFieldPatterns


    :return: {
        'FieldLevelEncryptionProfile': {
            'Id': 'string',
            'LastModifiedTime': datetime(2015, 1, 1),
            'FieldLevelEncryptionProfileConfig': {
                'Name': 'string',
                'CallerReference': 'string',
                'Comment': 'string',
                'EncryptionEntities': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'PublicKeyId': 'string',
                            'ProviderId': 'string',
                            'FieldPatterns': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                    ]
                }
            }
        },
        'ETag': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_public_key(PublicKeyConfig=None, Id=None, IfMatch=None):
    """
    Update public key information. Note that the only value you can change is the comment.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_public_key(
        PublicKeyConfig={
            'CallerReference': 'string',
            'Name': 'string',
            'EncodedKey': 'string',
            'Comment': 'string'
        },
        Id='string',
        IfMatch='string'
    )
    
    
    :type PublicKeyConfig: dict
    :param PublicKeyConfig: [REQUIRED]\nRequest to update public key information.\n\nCallerReference (string) -- [REQUIRED]A unique number that ensures that the request can\'t be replayed.\n\nName (string) -- [REQUIRED]The name for a public key you add to CloudFront to use with features like field-level encryption.\n\nEncodedKey (string) -- [REQUIRED]The encoded public key that you want to add to CloudFront to use with features like field-level encryption.\n\nComment (string) --An optional comment about a public key.\n\n\n

    :type Id: string
    :param Id: [REQUIRED]\nID of the public key to be updated.\n

    :type IfMatch: string
    :param IfMatch: The value of the ETag header that you received when retrieving the public key to update. For example: E2QWRUHAPOMQZL .

    :rtype: dict

ReturnsResponse Syntax
{
    'PublicKey': {
        'Id': 'string',
        'CreatedTime': datetime(2015, 1, 1),
        'PublicKeyConfig': {
            'CallerReference': 'string',
            'Name': 'string',
            'EncodedKey': 'string',
            'Comment': 'string'
        }
    },
    'ETag': 'string'
}


Response Structure

(dict) --

PublicKey (dict) --
Return the results of updating the public key.

Id (string) --
A unique ID assigned to a public key you\'ve added to CloudFront.

CreatedTime (datetime) --
A time you added a public key to CloudFront.

PublicKeyConfig (dict) --
A complex data type for a public key you add to CloudFront to use with features like field-level encryption.

CallerReference (string) --
A unique number that ensures that the request can\'t be replayed.

Name (string) --
The name for a public key you add to CloudFront to use with features like field-level encryption.

EncodedKey (string) --
The encoded public key that you want to add to CloudFront to use with features like field-level encryption.

Comment (string) --
An optional comment about a public key.





ETag (string) --
The current version of the update public key result. For example: E2QWRUHAPOMQZL .







Exceptions

CloudFront.Client.exceptions.AccessDenied
CloudFront.Client.exceptions.CannotChangeImmutablePublicKeyFields
CloudFront.Client.exceptions.InvalidArgument
CloudFront.Client.exceptions.InvalidIfMatchVersion
CloudFront.Client.exceptions.IllegalUpdate
CloudFront.Client.exceptions.NoSuchPublicKey
CloudFront.Client.exceptions.PreconditionFailed


    :return: {
        'PublicKey': {
            'Id': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'PublicKeyConfig': {
                'CallerReference': 'string',
                'Name': 'string',
                'EncodedKey': 'string',
                'Comment': 'string'
            }
        },
        'ETag': 'string'
    }
    
    
    :returns: 
    CloudFront.Client.exceptions.AccessDenied
    CloudFront.Client.exceptions.CannotChangeImmutablePublicKeyFields
    CloudFront.Client.exceptions.InvalidArgument
    CloudFront.Client.exceptions.InvalidIfMatchVersion
    CloudFront.Client.exceptions.IllegalUpdate
    CloudFront.Client.exceptions.NoSuchPublicKey
    CloudFront.Client.exceptions.PreconditionFailed
    
    """
    pass

def update_streaming_distribution(StreamingDistributionConfig=None, Id=None, IfMatch=None):
    """
    Update a streaming distribution.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_streaming_distribution(
        StreamingDistributionConfig={
            'CallerReference': 'string',
            'S3Origin': {
                'DomainName': 'string',
                'OriginAccessIdentity': 'string'
            },
            'Aliases': {
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'Comment': 'string',
            'Logging': {
                'Enabled': True|False,
                'Bucket': 'string',
                'Prefix': 'string'
            },
            'TrustedSigners': {
                'Enabled': True|False,
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
            'Enabled': True|False
        },
        Id='string',
        IfMatch='string'
    )
    
    
    :type StreamingDistributionConfig: dict
    :param StreamingDistributionConfig: [REQUIRED]\nThe streaming distribution\'s configuration information.\n\nCallerReference (string) -- [REQUIRED]A unique value (for example, a date-time stamp) that ensures that the request can\'t be replayed.\nIf the value of CallerReference is new (regardless of the content of the StreamingDistributionConfig object), CloudFront creates a new distribution.\nIf CallerReference is a value that you already sent in a previous request to create a distribution, CloudFront returns a DistributionAlreadyExists error.\n\nS3Origin (dict) -- [REQUIRED]A complex type that contains information about the Amazon S3 bucket from which you want CloudFront to get your media files for distribution.\n\nDomainName (string) -- [REQUIRED]The DNS name of the Amazon S3 origin.\n\nOriginAccessIdentity (string) -- [REQUIRED]The CloudFront origin access identity to associate with the distribution. Use an origin access identity to configure the distribution so that end users can only access objects in an Amazon S3 bucket through CloudFront.\nIf you want end users to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty OriginAccessIdentity element.\nTo delete the origin access identity from an existing distribution, update the distribution configuration and include an empty OriginAccessIdentity element.\nTo replace the origin access identity, update the distribution configuration and specify the new origin access identity.\nFor more information, see Using an Origin Access Identity to Restrict Access to Your Amazon S3 Content in the Amazon CloudFront Developer Guide .\n\n\n\nAliases (dict) --A complex type that contains information about CNAMEs (alternate domain names), if any, for this streaming distribution.\n\nQuantity (integer) -- [REQUIRED]The number of CNAME aliases, if any, that you want to associate with this distribution.\n\nItems (list) --A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.\n\n(string) --\n\n\n\n\nComment (string) -- [REQUIRED]Any comments you want to include about the streaming distribution.\n\nLogging (dict) --A complex type that controls whether access logs are written for the streaming distribution.\n\nEnabled (boolean) -- [REQUIRED]Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you don\'t want to enable logging when you create a streaming distribution or if you want to disable logging for an existing streaming distribution, specify false for Enabled , and specify empty Bucket and Prefix elements. If you specify false for Enabled but you specify values for Bucket and Prefix , the values are automatically deleted.\n\nBucket (string) -- [REQUIRED]The Amazon S3 bucket to store the access logs in, for example, myawslogbucket.s3.amazonaws.com .\n\nPrefix (string) -- [REQUIRED]An optional string that you want CloudFront to prefix to the access log filenames for this streaming distribution, for example, myprefix/ . If you want to enable logging, but you don\'t want to specify a prefix, you still must include an empty Prefix element in the Logging element.\n\n\n\nTrustedSigners (dict) -- [REQUIRED]A complex type that specifies any AWS accounts that you want to permit to create signed URLs for private content. If you want the distribution to use signed URLs, include this element; if you want the distribution to use public URLs, remove this element. For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .\n\nEnabled (boolean) -- [REQUIRED]Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .\n\nQuantity (integer) -- [REQUIRED]The number of trusted signers for this cache behavior.\n\nItems (list) --\nOptional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .\n\n(string) --\n\n\n\n\nPriceClass (string) --A complex type that contains information about price class for this streaming distribution.\n\nEnabled (boolean) -- [REQUIRED]Whether the streaming distribution is enabled to accept user requests for content.\n\n\n

    :type Id: string
    :param Id: [REQUIRED]\nThe streaming distribution\'s id.\n

    :type IfMatch: string
    :param IfMatch: The value of the ETag header that you received when retrieving the streaming distribution\'s configuration. For example: E2QWRUHAPOMQZL .

    :rtype: dict

ReturnsResponse Syntax
{
    'StreamingDistribution': {
        'Id': 'string',
        'ARN': 'string',
        'Status': 'string',
        'LastModifiedTime': datetime(2015, 1, 1),
        'DomainName': 'string',
        'ActiveTrustedSigners': {
            'Enabled': True|False,
            'Quantity': 123,
            'Items': [
                {
                    'AwsAccountNumber': 'string',
                    'KeyPairIds': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    }
                },
            ]
        },
        'StreamingDistributionConfig': {
            'CallerReference': 'string',
            'S3Origin': {
                'DomainName': 'string',
                'OriginAccessIdentity': 'string'
            },
            'Aliases': {
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'Comment': 'string',
            'Logging': {
                'Enabled': True|False,
                'Bucket': 'string',
                'Prefix': 'string'
            },
            'TrustedSigners': {
                'Enabled': True|False,
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
            'Enabled': True|False
        }
    },
    'ETag': 'string'
}


Response Structure

(dict) --
The returned result of the corresponding request.

StreamingDistribution (dict) --
The streaming distribution\'s information.

Id (string) --
The identifier for the RTMP distribution. For example: EGTXBD79EXAMPLE .

ARN (string) --
The ARN (Amazon Resource Name) for the distribution. For example: arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5 , where 123456789012 is your AWS account ID.

Status (string) --
The current status of the RTMP distribution. When the status is Deployed , the distribution\'s information is propagated to all CloudFront edge locations.

LastModifiedTime (datetime) --
The date and time that the distribution was last modified.

DomainName (string) --
The domain name that corresponds to the streaming distribution, for example, s5c39gqb8ow64r.cloudfront.net .

ActiveTrustedSigners (dict) --
A complex type that lists the AWS accounts, if any, that you included in the TrustedSigners complex type for this distribution. These are the accounts that you want to allow to create signed URLs for private content.
The Signer complex type lists the AWS account number of the trusted signer or self if the signer is the AWS account that created the distribution. The Signer element also includes the IDs of any active CloudFront key pairs that are associated with the trusted signer\'s AWS account. If no KeyPairId element appears for a Signer , that signer can\'t create signed URLs.
For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .

Enabled (boolean) --
Enabled is true if any of the AWS accounts listed in the TrustedSigners complex type for this distribution have active CloudFront key pairs. If not, Enabled is false .

Quantity (integer) --
The number of trusted signers specified in the TrustedSigners complex type.

Items (list) --
A complex type that contains one Signer complex type for each trusted signer that is specified in the TrustedSigners complex type.

(dict) --
A complex type that lists the AWS accounts that were included in the TrustedSigners complex type, as well as their active CloudFront key pair IDs, if any.

AwsAccountNumber (string) --
An AWS account that is included in the TrustedSigners complex type for this distribution. Valid values include:

self , which is the AWS account used to create the distribution.
An AWS account number.


KeyPairIds (dict) --
A complex type that lists the active CloudFront key pairs, if any, that are associated with AwsAccountNumber .

Quantity (integer) --
The number of active CloudFront key pairs for AwsAccountNumber .
For more information, see ActiveTrustedSigners .

Items (list) --
A complex type that lists the active CloudFront key pairs, if any, that are associated with AwsAccountNumber .
For more information, see ActiveTrustedSigners .

(string) --










StreamingDistributionConfig (dict) --
The current configuration information for the RTMP distribution.

CallerReference (string) --
A unique value (for example, a date-time stamp) that ensures that the request can\'t be replayed.
If the value of CallerReference is new (regardless of the content of the StreamingDistributionConfig object), CloudFront creates a new distribution.
If CallerReference is a value that you already sent in a previous request to create a distribution, CloudFront returns a DistributionAlreadyExists error.

S3Origin (dict) --
A complex type that contains information about the Amazon S3 bucket from which you want CloudFront to get your media files for distribution.

DomainName (string) --
The DNS name of the Amazon S3 origin.

OriginAccessIdentity (string) --
The CloudFront origin access identity to associate with the distribution. Use an origin access identity to configure the distribution so that end users can only access objects in an Amazon S3 bucket through CloudFront.
If you want end users to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty OriginAccessIdentity element.
To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty OriginAccessIdentity element.
To replace the origin access identity, update the distribution configuration and specify the new origin access identity.
For more information, see Using an Origin Access Identity to Restrict Access to Your Amazon S3 Content in the Amazon CloudFront Developer Guide .



Aliases (dict) --
A complex type that contains information about CNAMEs (alternate domain names), if any, for this streaming distribution.

Quantity (integer) --
The number of CNAME aliases, if any, that you want to associate with this distribution.

Items (list) --
A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.

(string) --




Comment (string) --
Any comments you want to include about the streaming distribution.

Logging (dict) --
A complex type that controls whether access logs are written for the streaming distribution.

Enabled (boolean) --
Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you don\'t want to enable logging when you create a streaming distribution or if you want to disable logging for an existing streaming distribution, specify false for Enabled , and specify empty Bucket and Prefix elements. If you specify false for Enabled but you specify values for Bucket and Prefix , the values are automatically deleted.

Bucket (string) --
The Amazon S3 bucket to store the access logs in, for example, myawslogbucket.s3.amazonaws.com .

Prefix (string) --
An optional string that you want CloudFront to prefix to the access log filenames for this streaming distribution, for example, myprefix/ . If you want to enable logging, but you don\'t want to specify a prefix, you still must include an empty Prefix element in the Logging element.



TrustedSigners (dict) --
A complex type that specifies any AWS accounts that you want to permit to create signed URLs for private content. If you want the distribution to use signed URLs, include this element; if you want the distribution to use public URLs, remove this element. For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .

Enabled (boolean) --
Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .

Quantity (integer) --
The number of trusted signers for this cache behavior.

Items (list) --

Optional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .


(string) --




PriceClass (string) --
A complex type that contains information about price class for this streaming distribution.

Enabled (boolean) --
Whether the streaming distribution is enabled to accept user requests for content.





ETag (string) --
The current version of the configuration. For example: E2QWRUHAPOMQZL .







Exceptions

CloudFront.Client.exceptions.AccessDenied
CloudFront.Client.exceptions.CNAMEAlreadyExists
CloudFront.Client.exceptions.IllegalUpdate
CloudFront.Client.exceptions.InvalidIfMatchVersion
CloudFront.Client.exceptions.MissingBody
CloudFront.Client.exceptions.NoSuchStreamingDistribution
CloudFront.Client.exceptions.PreconditionFailed
CloudFront.Client.exceptions.TooManyStreamingDistributionCNAMEs
CloudFront.Client.exceptions.InvalidArgument
CloudFront.Client.exceptions.InvalidOriginAccessIdentity
CloudFront.Client.exceptions.TooManyTrustedSigners
CloudFront.Client.exceptions.TrustedSignerDoesNotExist
CloudFront.Client.exceptions.InconsistentQuantities


    :return: {
        'StreamingDistribution': {
            'Id': 'string',
            'ARN': 'string',
            'Status': 'string',
            'LastModifiedTime': datetime(2015, 1, 1),
            'DomainName': 'string',
            'ActiveTrustedSigners': {
                'Enabled': True|False,
                'Quantity': 123,
                'Items': [
                    {
                        'AwsAccountNumber': 'string',
                        'KeyPairIds': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                ]
            },
            'StreamingDistributionConfig': {
                'CallerReference': 'string',
                'S3Origin': {
                    'DomainName': 'string',
                    'OriginAccessIdentity': 'string'
                },
                'Aliases': {
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'Comment': 'string',
                'Logging': {
                    'Enabled': True|False,
                    'Bucket': 'string',
                    'Prefix': 'string'
                },
                'TrustedSigners': {
                    'Enabled': True|False,
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
                'Enabled': True|False
            }
        },
        'ETag': 'string'
    }
    
    
    :returns: 
    self , which is the AWS account used to create the distribution.
    An AWS account number.
    
    """
    pass

