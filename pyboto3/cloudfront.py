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

import boto3


class Cloudfront(object):
    def __init__(self):
        self.client = boto3.client('Cloudfront')

    def can_paginate(self, operation_name=None):
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
        self.client.can_paginate(operation_name=operation_name)

    def create_cloud_front_origin_access_identity(self, CloudFrontOriginAccessIdentityConfig=None):
        """
        :param CloudFrontOriginAccessIdentityConfig: [REQUIRED] The origin access identity's configuration information.
            CallerReference (string) -- [REQUIRED] A unique number that ensures the request can't be replayed. If the CallerReference is new (no matter the content of the CloudFrontOriginAccessIdentityConfig object), a new origin access identity is created. If the CallerReference is a value you already sent in a previous request to create an identity, and the content of the CloudFrontOriginAccessIdentityConfig is identical to the original request (ignoring white space), the response includes the same information returned to the original request. If the CallerReference is a value you already sent in a previous request to create an identity but the content of the CloudFrontOriginAccessIdentityConfig is different from the original request, CloudFront returns a CloudFrontOriginAccessIdentityAlreadyExists error.
            Comment (string) -- [REQUIRED] Any comments you want to include about the origin access identity.
            Return typedict
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
            (dict) -- The returned result of the corresponding request.
            CloudFrontOriginAccessIdentity (dict) -- The origin access identity's information.
            Id (string) -- The ID for the origin access identity. For example: E74FTE3AJFJ256A.
            S3CanonicalUserId (string) -- The Amazon S3 canonical user ID for the origin access identity, which you use when giving the origin access identity read permission to an object in Amazon S3.
            CloudFrontOriginAccessIdentityConfig (dict) -- The current configuration information for the identity.
            CallerReference (string) -- A unique number that ensures the request can't be replayed. If the CallerReference is new (no matter the content of the CloudFrontOriginAccessIdentityConfig object), a new origin access identity is created. If the CallerReference is a value you already sent in a previous request to create an identity, and the content of the CloudFrontOriginAccessIdentityConfig is identical to the original request (ignoring white space), the response includes the same information returned to the original request. If the CallerReference is a value you already sent in a previous request to create an identity but the content of the CloudFrontOriginAccessIdentityConfig is different from the original request, CloudFront returns a CloudFrontOriginAccessIdentityAlreadyExists error.
            Comment (string) -- Any comments you want to include about the origin access identity.
            
            Location (string) -- The fully qualified URI of the new origin access identity just created. For example: https://cloudfront.amazonaws.com/2010-11-01/origin-access-identity/cloudfront/E74FTE3AJFJ256A.
            ETag (string) -- The current version of the origin access identity created.
            
            
        :type CloudFrontOriginAccessIdentityConfig: dict
        """
        self.client.create_cloud_front_origin_access_identity(
            CloudFrontOriginAccessIdentityConfig=CloudFrontOriginAccessIdentityConfig)

    def create_distribution(self, DistributionConfig=None):
        """
        :param DistributionConfig: [REQUIRED] The distribution's configuration information.
            CallerReference (string) -- [REQUIRED] A unique number that ensures the request can't be replayed. If the CallerReference is new (no matter the content of the DistributionConfig object), a new distribution is created. If the CallerReference is a value you already sent in a previous request to create a distribution, and the content of the DistributionConfig is identical to the original request (ignoring white space), the response includes the same information returned to the original request. If the CallerReference is a value you already sent in a previous request to create a distribution but the content of the DistributionConfig is different from the original request, CloudFront returns a DistributionAlreadyExists error.
            Aliases (dict) -- A complex type that contains information about CNAMEs (alternate domain names), if any, for this distribution.
            Quantity (integer) -- [REQUIRED] The number of CNAMEs, if any, for this distribution.
            Items (list) -- Optional: A complex type that contains CNAME elements, if any, for this distribution. If Quantity is 0, you can omit Items.
            (string) --
            
            DefaultRootObject (string) -- The object that you want CloudFront to return (for example, index.html) when an end user requests the root URL for your distribution (http://www.example.com) instead of an object in your distribution (http://www.example.com/index.html). Specifying a default root object avoids exposing the contents of your distribution. If you don't want to specify a default root object when you create a distribution, include an empty DefaultRootObject element. To delete the default root object from an existing distribution, update the distribution configuration and include an empty DefaultRootObject element. To replace the default root object, update the distribution configuration and specify the new object.
            Origins (dict) -- [REQUIRED] A complex type that contains information about origins for this distribution.
            Quantity (integer) -- [REQUIRED] The number of origins for this distribution.
            Items (list) -- A complex type that contains origins for this distribution.
            (dict) -- A complex type that describes the Amazon S3 bucket or the HTTP server (for example, a web server) from which CloudFront gets your files.You must create at least one origin.
            Id (string) -- [REQUIRED] A unique identifier for the origin. The value of Id must be unique within the distribution. You use the value of Id when you create a cache behavior. The Id identifies the origin that CloudFront routes a request to when the request matches the path pattern for that cache behavior.
            DomainName (string) -- [REQUIRED] Amazon S3 origins: The DNS name of the Amazon S3 bucket from which you want CloudFront to get objects for this origin, for example, myawsbucket.s3.amazonaws.com. Custom origins: The DNS domain name for the HTTP server from which you want CloudFront to get objects for this origin, for example, www.example.com.
            OriginPath (string) -- An optional element that causes CloudFront to request your content from a directory in your Amazon S3 bucket or your custom origin. When you include the OriginPath element, specify the directory name, beginning with a /. CloudFront appends the directory name to the value of DomainName.
            CustomHeaders (dict) -- A complex type that contains information about the custom headers associated with this Origin.
            Quantity (integer) -- [REQUIRED] The number of custom headers for this origin.
            Items (list) -- A complex type that contains the custom headers for this Origin.
            (dict) -- A complex type that contains information related to a Header
            HeaderName (string) -- [REQUIRED] The header's name.
            HeaderValue (string) -- [REQUIRED] The header's value.
            
            S3OriginConfig (dict) -- A complex type that contains information about the Amazon S3 origin. If the origin is a custom origin, use the CustomOriginConfig element instead.
            OriginAccessIdentity (string) -- [REQUIRED] The CloudFront origin access identity to associate with the origin. Use an origin access identity to configure the origin so that end users can only access objects in an Amazon S3 bucket through CloudFront. If you want end users to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty OriginAccessIdentity element. To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty OriginAccessIdentity element. To replace the origin access identity, update the distribution configuration and specify the new origin access identity. Use the format origin-access-identity/cloudfront/Id where Id is the value that CloudFront returned in the Id element when you created the origin access identity.
            CustomOriginConfig (dict) -- A complex type that contains information about a custom origin. If the origin is an Amazon S3 bucket, use the S3OriginConfig element instead.
            HTTPPort (integer) -- [REQUIRED] The HTTP port the custom origin listens on.
            HTTPSPort (integer) -- [REQUIRED] The HTTPS port the custom origin listens on.
            OriginProtocolPolicy (string) -- [REQUIRED] The origin protocol policy to apply to your origin.
            OriginSslProtocols (dict) -- The SSL/TLS protocols that you want CloudFront to use when communicating with your origin over HTTPS.
            Quantity (integer) -- [REQUIRED] The number of SSL/TLS protocols that you want to allow CloudFront to use when establishing an HTTPS connection with this origin.
            Items (list) -- [REQUIRED] A complex type that contains one SslProtocol element for each SSL/TLS protocol that you want to allow CloudFront to use when establishing an HTTPS connection with this origin.
            (string) --
            
            
            
            DefaultCacheBehavior (dict) -- [REQUIRED] A complex type that describes the default cache behavior if you do not specify a CacheBehavior element or if files don't match any of the values of PathPattern in CacheBehavior elements.You must create exactly one default cache behavior.
            TargetOriginId (string) -- [REQUIRED] The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior.
            ForwardedValues (dict) -- [REQUIRED] A complex type that specifies how CloudFront handles query strings, cookies and headers.
            QueryString (boolean) -- [REQUIRED] Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior. If so, specify true; if not, specify false.
            Cookies (dict) -- [REQUIRED] A complex type that specifies how CloudFront handles cookies.
            Forward (string) -- [REQUIRED] Use this element to specify whether you want CloudFront to forward cookies to the origin that is associated with this cache behavior. You can specify all, none or whitelist. If you choose All, CloudFront forwards all cookies regardless of how many your application uses.
            WhitelistedNames (dict) -- A complex type that specifies the whitelisted cookies, if any, that you want CloudFront to forward to your origin that is associated with this cache behavior.
            Quantity (integer) -- [REQUIRED] The number of whitelisted cookies for this cache behavior.
            Items (list) -- Optional: A complex type that contains whitelisted cookies for this cache behavior. If Quantity is 0, you can omit Items.
            (string) --
            
            Headers (dict) -- A complex type that specifies the Headers, if any, that you want CloudFront to vary upon for this cache behavior.
            Quantity (integer) -- [REQUIRED] The number of different headers that you want CloudFront to forward to the origin and to vary on for this cache behavior. The maximum number of headers that you can specify by name is 10. If you want CloudFront to forward all headers to the origin and vary on all of them, specify 1 for Quantity and * for Name. If you don't want CloudFront to forward any additional headers to the origin or to vary on any headers, specify 0 for Quantity and omit Items.
            Items (list) -- Optional: A complex type that contains a Name element for each header that you want CloudFront to forward to the origin and to vary on for this cache behavior. If Quantity is 0, omit Items.
            (string) --
            
            TrustedSigners (dict) -- [REQUIRED] A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content. If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled, and specify the applicable values for Quantity and Items. For more information, go to Using a Signed URL to Serve Private Content in the Amazon CloudFront Developer Guide. If you don't want to require signed URLs in requests for objects that match PathPattern, specify false for Enabled and 0 for Quantity. Omit Items. To add, change, or remove one or more trusted signers, change Enabled to true (if it's currently false), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.
            Enabled (boolean) -- [REQUIRED] Specifies whether you want to require end users to use signed URLs to access the files specified by PathPattern and TargetOriginId.
            Quantity (integer) -- [REQUIRED] The number of trusted signers for this cache behavior.
            Items (list) -- Optional: A complex type that contains trusted signers for this cache behavior. If Quantity is 0, you can omit Items.
            (string) --
            
            ViewerProtocolPolicy (string) -- [REQUIRED] Use this element to specify the protocol that users can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern. If you want CloudFront to allow end users to use any available protocol, specify allow-all. If you want CloudFront to require HTTPS, specify https. If you want CloudFront to respond to an HTTP request with an HTTP status code of 301 (Moved Permanently) and the HTTPS URL, specify redirect-to-https. The viewer then resubmits the request using the HTTPS URL.
            MinTTL (integer) -- [REQUIRED] The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront queries your origin to see whether the object has been updated.You can specify a value from 0 to 3,153,600,000 seconds (100 years).
            AllowedMethods (dict) -- A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices: - CloudFront forwards only GET and HEAD requests. - CloudFront forwards only GET, HEAD and OPTIONS requests. - CloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST, and DELETE requests. If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can't perform operations that you don't want them to. For example, you may not want users to have permission to delete objects from your origin.
            Quantity (integer) -- [REQUIRED] The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET, HEAD and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST, and DELETE requests).
            Items (list) -- [REQUIRED] A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.
            (string) --
            CachedMethods (dict) -- A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices: - CloudFront caches responses to GET and HEAD requests. - CloudFront caches responses to GET, HEAD, and OPTIONS requests. If you pick the second choice for your S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers and Origin headers for the responses to be cached correctly.
            Quantity (integer) -- [REQUIRED] The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET, HEAD, and OPTIONS requests).
            Items (list) -- [REQUIRED] A complex type that contains the HTTP methods that you want CloudFront to cache responses to.
            (string) --
            
            SmoothStreaming (boolean) -- Indicates whether you want to distribute media files in Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true; if not, specify false.
            DefaultTTL (integer) -- If you don't configure your origin to add a Cache-Control max-age directive or an Expires header, DefaultTTL is the default amount of time (in seconds) that an object is in a CloudFront cache before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age, Cache-Control s-maxage, and Expires to objects. You can specify a value from 0 to 3,153,600,000 seconds (100 years).
            MaxTTL (integer) -- The maximum amount of time (in seconds) that an object is in a CloudFront cache before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as Cache-Control max-age, Cache-Control s-maxage, and Expires to objects. You can specify a value from 0 to 3,153,600,000 seconds (100 years).
            Compress (boolean) -- Whether you want CloudFront to automatically compress content for web requests that include Accept-Encoding: gzip in the request header. If so, specify true; if not, specify false. CloudFront compresses files larger than 1000 bytes and less than 1 megabyte for both Amazon S3 and custom origins. When a CloudFront edge location is unusually busy, some files might not be compressed. The value of the Content-Type header must be on the list of file types that CloudFront will compress. For the current list, see Serving Compressed Content in the Amazon CloudFront Developer Guide. If you configure CloudFront to compress content, CloudFront removes the ETag response header from the objects that it compresses. The ETag header indicates that the version in a CloudFront edge cache is identical to the version on the origin server, but after compression the two versions are no longer identical. As a result, for compressed objects, CloudFront can't use the ETag header to determine whether an expired object in the CloudFront edge cache is still the latest version.
            CacheBehaviors (dict) -- A complex type that contains zero or more CacheBehavior elements.
            Quantity (integer) -- [REQUIRED] The number of cache behaviors for this distribution.
            Items (list) -- Optional: A complex type that contains cache behaviors for this distribution. If Quantity is 0, you can omit Items.
            (dict) -- A complex type that describes how CloudFront processes requests. You can create up to 10 cache behaviors.You must create at least as many cache behaviors (including the default cache behavior) as you have origins if you want CloudFront to distribute objects from all of the origins. Each cache behavior specifies the one origin from which you want CloudFront to get objects. If you have two origins and only the default cache behavior, the default cache behavior will cause CloudFront to get objects from one of the origins, but the other origin will never be used. If you don't want to specify any cache behaviors, include only an empty CacheBehaviors element. Don't include an empty CacheBehavior element, or CloudFront returns a MalformedXML error. To delete all cache behaviors in an existing distribution, update the distribution configuration and include only an empty CacheBehaviors element. To add, change, or remove one or more cache behaviors, update the distribution configuration and specify all of the cache behaviors that you want to include in the updated distribution.
            PathPattern (string) -- [REQUIRED] The pattern (for example, images/*.jpg) that specifies which requests you want this cache behavior to apply to. When CloudFront receives an end-user request, the requested path is compared with path patterns in the order in which cache behaviors are listed in the distribution. The path pattern for the default cache behavior is * and cannot be changed. If the request for an object does not match the path pattern for any cache behaviors, CloudFront applies the behavior in the default cache behavior.
            TargetOriginId (string) -- [REQUIRED] The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior.
            ForwardedValues (dict) -- [REQUIRED] A complex type that specifies how CloudFront handles query strings, cookies and headers.
            QueryString (boolean) -- [REQUIRED] Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior. If so, specify true; if not, specify false.
            Cookies (dict) -- [REQUIRED] A complex type that specifies how CloudFront handles cookies.
            Forward (string) -- [REQUIRED] Use this element to specify whether you want CloudFront to forward cookies to the origin that is associated with this cache behavior. You can specify all, none or whitelist. If you choose All, CloudFront forwards all cookies regardless of how many your application uses.
            WhitelistedNames (dict) -- A complex type that specifies the whitelisted cookies, if any, that you want CloudFront to forward to your origin that is associated with this cache behavior.
            Quantity (integer) -- [REQUIRED] The number of whitelisted cookies for this cache behavior.
            Items (list) -- Optional: A complex type that contains whitelisted cookies for this cache behavior. If Quantity is 0, you can omit Items.
            (string) --
            
            Headers (dict) -- A complex type that specifies the Headers, if any, that you want CloudFront to vary upon for this cache behavior.
            Quantity (integer) -- [REQUIRED] The number of different headers that you want CloudFront to forward to the origin and to vary on for this cache behavior. The maximum number of headers that you can specify by name is 10. If you want CloudFront to forward all headers to the origin and vary on all of them, specify 1 for Quantity and * for Name. If you don't want CloudFront to forward any additional headers to the origin or to vary on any headers, specify 0 for Quantity and omit Items.
            Items (list) -- Optional: A complex type that contains a Name element for each header that you want CloudFront to forward to the origin and to vary on for this cache behavior. If Quantity is 0, omit Items.
            (string) --
            
            TrustedSigners (dict) -- [REQUIRED] A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content. If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled, and specify the applicable values for Quantity and Items. For more information, go to Using a Signed URL to Serve Private Content in the Amazon CloudFront Developer Guide. If you don't want to require signed URLs in requests for objects that match PathPattern, specify false for Enabled and 0 for Quantity. Omit Items. To add, change, or remove one or more trusted signers, change Enabled to true (if it's currently false), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.
            Enabled (boolean) -- [REQUIRED] Specifies whether you want to require end users to use signed URLs to access the files specified by PathPattern and TargetOriginId.
            Quantity (integer) -- [REQUIRED] The number of trusted signers for this cache behavior.
            Items (list) -- Optional: A complex type that contains trusted signers for this cache behavior. If Quantity is 0, you can omit Items.
            (string) --
            
            ViewerProtocolPolicy (string) -- [REQUIRED] Use this element to specify the protocol that users can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern. If you want CloudFront to allow end users to use any available protocol, specify allow-all. If you want CloudFront to require HTTPS, specify https. If you want CloudFront to respond to an HTTP request with an HTTP status code of 301 (Moved Permanently) and the HTTPS URL, specify redirect-to-https. The viewer then resubmits the request using the HTTPS URL.
            MinTTL (integer) -- [REQUIRED] The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront queries your origin to see whether the object has been updated.You can specify a value from 0 to 3,153,600,000 seconds (100 years).
            AllowedMethods (dict) -- A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices: - CloudFront forwards only GET and HEAD requests. - CloudFront forwards only GET, HEAD and OPTIONS requests. - CloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST, and DELETE requests. If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can't perform operations that you don't want them to. For example, you may not want users to have permission to delete objects from your origin.
            Quantity (integer) -- [REQUIRED] The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET, HEAD and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST, and DELETE requests).
            Items (list) -- [REQUIRED] A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.
            (string) --
            CachedMethods (dict) -- A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices: - CloudFront caches responses to GET and HEAD requests. - CloudFront caches responses to GET, HEAD, and OPTIONS requests. If you pick the second choice for your S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers and Origin headers for the responses to be cached correctly.
            Quantity (integer) -- [REQUIRED] The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET, HEAD, and OPTIONS requests).
            Items (list) -- [REQUIRED] A complex type that contains the HTTP methods that you want CloudFront to cache responses to.
            (string) --
            
            SmoothStreaming (boolean) -- Indicates whether you want to distribute media files in Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true; if not, specify false.
            DefaultTTL (integer) -- If you don't configure your origin to add a Cache-Control max-age directive or an Expires header, DefaultTTL is the default amount of time (in seconds) that an object is in a CloudFront cache before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age, Cache-Control s-maxage, and Expires to objects. You can specify a value from 0 to 3,153,600,000 seconds (100 years).
            MaxTTL (integer) -- The maximum amount of time (in seconds) that an object is in a CloudFront cache before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as Cache-Control max-age, Cache-Control s-maxage, and Expires to objects. You can specify a value from 0 to 3,153,600,000 seconds (100 years).
            Compress (boolean) -- Whether you want CloudFront to automatically compress content for web requests that include Accept-Encoding: gzip in the request header. If so, specify true; if not, specify false. CloudFront compresses files larger than 1000 bytes and less than 1 megabyte for both Amazon S3 and custom origins. When a CloudFront edge location is unusually busy, some files might not be compressed. The value of the Content-Type header must be on the list of file types that CloudFront will compress. For the current list, see Serving Compressed Content in the Amazon CloudFront Developer Guide. If you configure CloudFront to compress content, CloudFront removes the ETag response header from the objects that it compresses. The ETag header indicates that the version in a CloudFront edge cache is identical to the version on the origin server, but after compression the two versions are no longer identical. As a result, for compressed objects, CloudFront can't use the ETag header to determine whether an expired object in the CloudFront edge cache is still the latest version.
            
            CustomErrorResponses (dict) -- A complex type that contains zero or more CustomErrorResponse elements.
            Quantity (integer) -- [REQUIRED] The number of custom error responses for this distribution.
            Items (list) -- Optional: A complex type that contains custom error responses for this distribution. If Quantity is 0, you can omit Items.
            (dict) -- A complex type that describes how you'd prefer CloudFront to respond to requests that result in either a 4xx or 5xx response. You can control whether a custom error page should be displayed, what the desired response code should be for this error page and how long should the error response be cached by CloudFront. If you don't want to specify any custom error responses, include only an empty CustomErrorResponses element. To delete all custom error responses in an existing distribution, update the distribution configuration and include only an empty CustomErrorResponses element. To add, change, or remove one or more custom error responses, update the distribution configuration and specify all of the custom error responses that you want to include in the updated distribution.
            ErrorCode (integer) -- [REQUIRED] The 4xx or 5xx HTTP status code that you want to customize. For a list of HTTP status codes that you can customize, see CloudFront documentation.
            ResponsePagePath (string) -- The path of the custom error page (for example, /custom_404.html). The path is relative to the distribution and must begin with a slash (/). If the path includes any non-ASCII characters or unsafe characters as defined in RFC 1783 (http://www.ietf.org/rfc/rfc1738.txt), URL encode those characters. Do not URL encode any other characters in the path, or CloudFront will not return the custom error page to the viewer.
            ResponseCode (string) -- The HTTP status code that you want CloudFront to return with the custom error page to the viewer. For a list of HTTP status codes that you can replace, see CloudFront Documentation.
            ErrorCachingMinTTL (integer) -- The minimum amount of time you want HTTP error codes to stay in CloudFront caches before CloudFront queries your origin to see whether the object has been updated. You can specify a value from 0 to 31,536,000.
            
            Comment (string) -- [REQUIRED] Any comments you want to include about the distribution.
            Logging (dict) -- A complex type that controls whether access logs are written for the distribution.
            Enabled (boolean) -- [REQUIRED] Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you do not want to enable logging when you create a distribution or if you want to disable logging for an existing distribution, specify false for Enabled, and specify empty Bucket and Prefix elements. If you specify false for Enabled but you specify values for Bucket, prefix and IncludeCookies, the values are automatically deleted.
            IncludeCookies (boolean) -- [REQUIRED] Specifies whether you want CloudFront to include cookies in access logs, specify true for IncludeCookies. If you choose to include cookies in logs, CloudFront logs all cookies regardless of how you configure the cache behaviors for this distribution. If you do not want to include cookies when you create a distribution or if you want to disable include cookies for an existing distribution, specify false for IncludeCookies.
            Bucket (string) -- [REQUIRED] The Amazon S3 bucket to store the access logs in, for example, myawslogbucket.s3.amazonaws.com.
            Prefix (string) -- [REQUIRED] An optional string that you want CloudFront to prefix to the access log filenames for this distribution, for example, myprefix/. If you want to enable logging, but you do not want to specify a prefix, you still must include an empty Prefix element in the Logging element.
            PriceClass (string) -- A complex type that contains information about price class for this distribution.
            Enabled (boolean) -- [REQUIRED] Whether the distribution is enabled to accept end user requests for content.
            ViewerCertificate (dict) -- A complex type that contains information about viewer certificates for this distribution.
            CloudFrontDefaultCertificate (boolean) -- If you want viewers to use HTTPS to request your objects and you're using the CloudFront domain name of your distribution in your object URLs (for example, https://d111111abcdef8.cloudfront.net/logo.jpg), set to true. Omit this value if you are setting an ACMCertificateArn or IAMCertificateId.
            IAMCertificateId (string) -- If you want viewers to use HTTPS to request your objects and you're using an alternate domain name in your object URLs (for example, https://example.com/logo.jpg), specify the IAM certificate identifier of the custom viewer certificate for this distribution. Specify either this value, ACMCertificateArn, or CloudFrontDefaultCertificate.
            ACMCertificateArn (string) -- If you want viewers to use HTTPS to request your objects and you're using an alternate domain name in your object URLs (for example, https://example.com/logo.jpg), specify the ACM certificate ARN of the custom viewer certificate for this distribution. Specify either this value, IAMCertificateId, or CloudFrontDefaultCertificate.
            SSLSupportMethod (string) -- If you specify a value for IAMCertificateId, you must also specify how you want CloudFront to serve HTTPS requests. Valid values are vip and sni-only. If you specify vip, CloudFront uses dedicated IP addresses for your content and can respond to HTTPS requests from any viewer. However, you must request permission to use this feature, and you incur additional monthly charges. If you specify sni-only, CloudFront can only respond to HTTPS requests from viewers that support Server Name Indication (SNI). All modern browsers support SNI, but some browsers still in use don't support SNI. Do not specify a value for SSLSupportMethod if you specified true for CloudFrontDefaultCertificate.
            MinimumProtocolVersion (string) -- Specify the minimum version of the SSL protocol that you want CloudFront to use, SSLv3 or TLSv1, for HTTPS connections. CloudFront will serve your objects only to browsers or devices that support at least the SSL version that you specify. The TLSv1 protocol is more secure, so we recommend that you specify SSLv3 only if your users are using browsers or devices that don't support TLSv1. If you're using a custom certificate (if you specify a value for IAMCertificateId) and if you're using dedicated IP (if you specify vip for SSLSupportMethod), you can choose SSLv3 or TLSv1 as the MinimumProtocolVersion. If you're using a custom certificate (if you specify a value for IAMCertificateId) and if you're using SNI (if you specify sni-only for SSLSupportMethod), you must specify TLSv1 for MinimumProtocolVersion.
            Certificate (string) -- Note: this field is deprecated. Please use one of [ACMCertificateArn, IAMCertificateId, CloudFrontDefaultCertificate].
            CertificateSource (string) -- Note: this field is deprecated. Please use one of [ACMCertificateArn, IAMCertificateId, CloudFrontDefaultCertificate].
            Restrictions (dict) -- A complex type that identifies ways in which you want to restrict distribution of your content.
            GeoRestriction (dict) -- [REQUIRED] A complex type that controls the countries in which your content is distributed. For more information about geo restriction, go to Customizing Error Responses in the Amazon CloudFront Developer Guide. CloudFront determines the location of your users using MaxMind GeoIP databases. For information about the accuracy of these databases, see How accurate are your GeoIP databases? on the MaxMind website.
            RestrictionType (string) -- [REQUIRED] The method that you want to use to restrict distribution of your content by country: - none: No geo restriction is enabled, meaning access to content is not restricted by client geo location. - blacklist: The Location elements specify the countries in which you do not want CloudFront to distribute your content. - whitelist: The Location elements specify the countries in which you want CloudFront to distribute your content.
            Quantity (integer) -- [REQUIRED] When geo restriction is enabled, this is the number of countries in your whitelist or blacklist. Otherwise, when it is not enabled, Quantity is 0, and you can omit Items.
            Items (list) -- A complex type that contains a Location element for each country in which you want CloudFront either to distribute your content (whitelist) or not distribute your content (blacklist). The Location element is a two-letter, uppercase country code for a country that you want to include in your blacklist or whitelist. Include one Location element for each country. CloudFront and MaxMind both use ISO 3166 country codes. For the current list of countries and the corresponding codes, see ISO 3166-1-alpha-2 code on the International Organization for Standardization website. You can also refer to the country list in the CloudFront console, which includes both country names and codes.
            (string) --
            
            WebACLId (string) -- (Optional) If you're using AWS WAF to filter CloudFront requests, the Id of the AWS WAF web ACL that is associated with the distribution.
            Return typedict
            ReturnsResponse Syntax{
              'Distribution': {
                'Id': 'string',
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
                          }
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
                    'Compress': True|False
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
                        'Compress': True|False
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
                    'MinimumProtocolVersion': 'SSLv3'|'TLSv1',
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
                  'WebACLId': 'string'
                }
              },
              'Location': 'string',
              'ETag': 'string'
            }
            Response Structure
            (dict) -- The returned result of the corresponding request.
            Distribution (dict) -- The distribution's information.
            Id (string) -- The identifier for the distribution. For example: EDFDVBD632BHDS5.
            Status (string) -- This response element indicates the current status of the distribution. When the status is Deployed, the distribution's information is fully propagated throughout the Amazon CloudFront system.
            LastModifiedTime (datetime) -- The date and time the distribution was last modified.
            InProgressInvalidationBatches (integer) -- The number of invalidation batches currently in progress.
            DomainName (string) -- The domain name corresponding to the distribution. For example: d604721fxaaqy9.cloudfront.net.
            ActiveTrustedSigners (dict) -- CloudFront automatically adds this element to the response only if you've set up the distribution to serve private content with signed URLs. The element lists the key pair IDs that CloudFront is aware of for each trusted signer. The Signer child element lists the AWS account number of the trusted signer (or an empty Self element if the signer is you). The Signer element also includes the IDs of any active key pairs associated with the trusted signer's AWS account. If no KeyPairId element appears for a Signer, that signer can't create working signed URLs.
            Enabled (boolean) -- Each active trusted signer.
            Quantity (integer) -- The number of unique trusted signers included in all cache behaviors. For example, if three cache behaviors all list the same three AWS accounts, the value of Quantity for ActiveTrustedSigners will be 3.
            Items (list) -- A complex type that contains one Signer complex type for each unique trusted signer that is specified in the TrustedSigners complex type, including trusted signers in the default cache behavior and in all of the other cache behaviors.
            (dict) -- A complex type that lists the AWS accounts that were included in the TrustedSigners complex type, as well as their active CloudFront key pair IDs, if any.
            AwsAccountNumber (string) -- Specifies an AWS account that can create signed URLs. Values: self, which indicates that the AWS account that was used to create the distribution can created signed URLs, or an AWS account number. Omit the dashes in the account number.
            KeyPairIds (dict) -- A complex type that lists the active CloudFront key pairs, if any, that are associated with AwsAccountNumber.
            Quantity (integer) -- The number of active CloudFront key pairs for AwsAccountNumber.
            Items (list) -- A complex type that lists the active CloudFront key pairs, if any, that are associated with AwsAccountNumber.
            (string) --
            
            
            DistributionConfig (dict) -- The current configuration information for the distribution.
            CallerReference (string) -- A unique number that ensures the request can't be replayed. If the CallerReference is new (no matter the content of the DistributionConfig object), a new distribution is created. If the CallerReference is a value you already sent in a previous request to create a distribution, and the content of the DistributionConfig is identical to the original request (ignoring white space), the response includes the same information returned to the original request. If the CallerReference is a value you already sent in a previous request to create a distribution but the content of the DistributionConfig is different from the original request, CloudFront returns a DistributionAlreadyExists error.
            Aliases (dict) -- A complex type that contains information about CNAMEs (alternate domain names), if any, for this distribution.
            Quantity (integer) -- The number of CNAMEs, if any, for this distribution.
            Items (list) -- Optional: A complex type that contains CNAME elements, if any, for this distribution. If Quantity is 0, you can omit Items.
            (string) --
            
            DefaultRootObject (string) -- The object that you want CloudFront to return (for example, index.html) when an end user requests the root URL for your distribution (http://www.example.com) instead of an object in your distribution (http://www.example.com/index.html). Specifying a default root object avoids exposing the contents of your distribution. If you don't want to specify a default root object when you create a distribution, include an empty DefaultRootObject element. To delete the default root object from an existing distribution, update the distribution configuration and include an empty DefaultRootObject element. To replace the default root object, update the distribution configuration and specify the new object.
            Origins (dict) -- A complex type that contains information about origins for this distribution.
            Quantity (integer) -- The number of origins for this distribution.
            Items (list) -- A complex type that contains origins for this distribution.
            (dict) -- A complex type that describes the Amazon S3 bucket or the HTTP server (for example, a web server) from which CloudFront gets your files.You must create at least one origin.
            Id (string) -- A unique identifier for the origin. The value of Id must be unique within the distribution. You use the value of Id when you create a cache behavior. The Id identifies the origin that CloudFront routes a request to when the request matches the path pattern for that cache behavior.
            DomainName (string) -- Amazon S3 origins: The DNS name of the Amazon S3 bucket from which you want CloudFront to get objects for this origin, for example, myawsbucket.s3.amazonaws.com. Custom origins: The DNS domain name for the HTTP server from which you want CloudFront to get objects for this origin, for example, www.example.com.
            OriginPath (string) -- An optional element that causes CloudFront to request your content from a directory in your Amazon S3 bucket or your custom origin. When you include the OriginPath element, specify the directory name, beginning with a /. CloudFront appends the directory name to the value of DomainName.
            CustomHeaders (dict) -- A complex type that contains information about the custom headers associated with this Origin.
            Quantity (integer) -- The number of custom headers for this origin.
            Items (list) -- A complex type that contains the custom headers for this Origin.
            (dict) -- A complex type that contains information related to a Header
            HeaderName (string) -- The header's name.
            HeaderValue (string) -- The header's value.
            
            S3OriginConfig (dict) -- A complex type that contains information about the Amazon S3 origin. If the origin is a custom origin, use the CustomOriginConfig element instead.
            OriginAccessIdentity (string) -- The CloudFront origin access identity to associate with the origin. Use an origin access identity to configure the origin so that end users can only access objects in an Amazon S3 bucket through CloudFront. If you want end users to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty OriginAccessIdentity element. To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty OriginAccessIdentity element. To replace the origin access identity, update the distribution configuration and specify the new origin access identity. Use the format origin-access-identity/cloudfront/Id where Id is the value that CloudFront returned in the Id element when you created the origin access identity.
            CustomOriginConfig (dict) -- A complex type that contains information about a custom origin. If the origin is an Amazon S3 bucket, use the S3OriginConfig element instead.
            HTTPPort (integer) -- The HTTP port the custom origin listens on.
            HTTPSPort (integer) -- The HTTPS port the custom origin listens on.
            OriginProtocolPolicy (string) -- The origin protocol policy to apply to your origin.
            OriginSslProtocols (dict) -- The SSL/TLS protocols that you want CloudFront to use when communicating with your origin over HTTPS.
            Quantity (integer) -- The number of SSL/TLS protocols that you want to allow CloudFront to use when establishing an HTTPS connection with this origin.
            Items (list) -- A complex type that contains one SslProtocol element for each SSL/TLS protocol that you want to allow CloudFront to use when establishing an HTTPS connection with this origin.
            (string) --
            
            
            
            DefaultCacheBehavior (dict) -- A complex type that describes the default cache behavior if you do not specify a CacheBehavior element or if files don't match any of the values of PathPattern in CacheBehavior elements.You must create exactly one default cache behavior.
            TargetOriginId (string) -- The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior.
            ForwardedValues (dict) -- A complex type that specifies how CloudFront handles query strings, cookies and headers.
            QueryString (boolean) -- Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior. If so, specify true; if not, specify false.
            Cookies (dict) -- A complex type that specifies how CloudFront handles cookies.
            Forward (string) -- Use this element to specify whether you want CloudFront to forward cookies to the origin that is associated with this cache behavior. You can specify all, none or whitelist. If you choose All, CloudFront forwards all cookies regardless of how many your application uses.
            WhitelistedNames (dict) -- A complex type that specifies the whitelisted cookies, if any, that you want CloudFront to forward to your origin that is associated with this cache behavior.
            Quantity (integer) -- The number of whitelisted cookies for this cache behavior.
            Items (list) -- Optional: A complex type that contains whitelisted cookies for this cache behavior. If Quantity is 0, you can omit Items.
            (string) --
            
            Headers (dict) -- A complex type that specifies the Headers, if any, that you want CloudFront to vary upon for this cache behavior.
            Quantity (integer) -- The number of different headers that you want CloudFront to forward to the origin and to vary on for this cache behavior. The maximum number of headers that you can specify by name is 10. If you want CloudFront to forward all headers to the origin and vary on all of them, specify 1 for Quantity and * for Name. If you don't want CloudFront to forward any additional headers to the origin or to vary on any headers, specify 0 for Quantity and omit Items.
            Items (list) -- Optional: A complex type that contains a Name element for each header that you want CloudFront to forward to the origin and to vary on for this cache behavior. If Quantity is 0, omit Items.
            (string) --
            
            TrustedSigners (dict) -- A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content. If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled, and specify the applicable values for Quantity and Items. For more information, go to Using a Signed URL to Serve Private Content in the Amazon CloudFront Developer Guide. If you don't want to require signed URLs in requests for objects that match PathPattern, specify false for Enabled and 0 for Quantity. Omit Items. To add, change, or remove one or more trusted signers, change Enabled to true (if it's currently false), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.
            Enabled (boolean) -- Specifies whether you want to require end users to use signed URLs to access the files specified by PathPattern and TargetOriginId.
            Quantity (integer) -- The number of trusted signers for this cache behavior.
            Items (list) -- Optional: A complex type that contains trusted signers for this cache behavior. If Quantity is 0, you can omit Items.
            (string) --
            
            ViewerProtocolPolicy (string) -- Use this element to specify the protocol that users can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern. If you want CloudFront to allow end users to use any available protocol, specify allow-all. If you want CloudFront to require HTTPS, specify https. If you want CloudFront to respond to an HTTP request with an HTTP status code of 301 (Moved Permanently) and the HTTPS URL, specify redirect-to-https. The viewer then resubmits the request using the HTTPS URL.
            MinTTL (integer) -- The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront queries your origin to see whether the object has been updated.You can specify a value from 0 to 3,153,600,000 seconds (100 years).
            AllowedMethods (dict) -- A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices: - CloudFront forwards only GET and HEAD requests. - CloudFront forwards only GET, HEAD and OPTIONS requests. - CloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST, and DELETE requests. If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can't perform operations that you don't want them to. For example, you may not want users to have permission to delete objects from your origin.
            Quantity (integer) -- The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET, HEAD and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST, and DELETE requests).
            Items (list) -- A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.
            (string) --
            CachedMethods (dict) -- A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices: - CloudFront caches responses to GET and HEAD requests. - CloudFront caches responses to GET, HEAD, and OPTIONS requests. If you pick the second choice for your S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers and Origin headers for the responses to be cached correctly.
            Quantity (integer) -- The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET, HEAD, and OPTIONS requests).
            Items (list) -- A complex type that contains the HTTP methods that you want CloudFront to cache responses to.
            (string) --
            
            SmoothStreaming (boolean) -- Indicates whether you want to distribute media files in Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true; if not, specify false.
            DefaultTTL (integer) -- If you don't configure your origin to add a Cache-Control max-age directive or an Expires header, DefaultTTL is the default amount of time (in seconds) that an object is in a CloudFront cache before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age, Cache-Control s-maxage, and Expires to objects. You can specify a value from 0 to 3,153,600,000 seconds (100 years).
            MaxTTL (integer) -- The maximum amount of time (in seconds) that an object is in a CloudFront cache before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as Cache-Control max-age, Cache-Control s-maxage, and Expires to objects. You can specify a value from 0 to 3,153,600,000 seconds (100 years).
            Compress (boolean) -- Whether you want CloudFront to automatically compress content for web requests that include Accept-Encoding: gzip in the request header. If so, specify true; if not, specify false. CloudFront compresses files larger than 1000 bytes and less than 1 megabyte for both Amazon S3 and custom origins. When a CloudFront edge location is unusually busy, some files might not be compressed. The value of the Content-Type header must be on the list of file types that CloudFront will compress. For the current list, see Serving Compressed Content in the Amazon CloudFront Developer Guide. If you configure CloudFront to compress content, CloudFront removes the ETag response header from the objects that it compresses. The ETag header indicates that the version in a CloudFront edge cache is identical to the version on the origin server, but after compression the two versions are no longer identical. As a result, for compressed objects, CloudFront can't use the ETag header to determine whether an expired object in the CloudFront edge cache is still the latest version.
            CacheBehaviors (dict) -- A complex type that contains zero or more CacheBehavior elements.
            Quantity (integer) -- The number of cache behaviors for this distribution.
            Items (list) -- Optional: A complex type that contains cache behaviors for this distribution. If Quantity is 0, you can omit Items.
            (dict) -- A complex type that describes how CloudFront processes requests. You can create up to 10 cache behaviors.You must create at least as many cache behaviors (including the default cache behavior) as you have origins if you want CloudFront to distribute objects from all of the origins. Each cache behavior specifies the one origin from which you want CloudFront to get objects. If you have two origins and only the default cache behavior, the default cache behavior will cause CloudFront to get objects from one of the origins, but the other origin will never be used. If you don't want to specify any cache behaviors, include only an empty CacheBehaviors element. Don't include an empty CacheBehavior element, or CloudFront returns a MalformedXML error. To delete all cache behaviors in an existing distribution, update the distribution configuration and include only an empty CacheBehaviors element. To add, change, or remove one or more cache behaviors, update the distribution configuration and specify all of the cache behaviors that you want to include in the updated distribution.
            PathPattern (string) -- The pattern (for example, images/*.jpg) that specifies which requests you want this cache behavior to apply to. When CloudFront receives an end-user request, the requested path is compared with path patterns in the order in which cache behaviors are listed in the distribution. The path pattern for the default cache behavior is * and cannot be changed. If the request for an object does not match the path pattern for any cache behaviors, CloudFront applies the behavior in the default cache behavior.
            TargetOriginId (string) -- The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior.
            ForwardedValues (dict) -- A complex type that specifies how CloudFront handles query strings, cookies and headers.
            QueryString (boolean) -- Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior. If so, specify true; if not, specify false.
            Cookies (dict) -- A complex type that specifies how CloudFront handles cookies.
            Forward (string) -- Use this element to specify whether you want CloudFront to forward cookies to the origin that is associated with this cache behavior. You can specify all, none or whitelist. If you choose All, CloudFront forwards all cookies regardless of how many your application uses.
            WhitelistedNames (dict) -- A complex type that specifies the whitelisted cookies, if any, that you want CloudFront to forward to your origin that is associated with this cache behavior.
            Quantity (integer) -- The number of whitelisted cookies for this cache behavior.
            Items (list) -- Optional: A complex type that contains whitelisted cookies for this cache behavior. If Quantity is 0, you can omit Items.
            (string) --
            
            Headers (dict) -- A complex type that specifies the Headers, if any, that you want CloudFront to vary upon for this cache behavior.
            Quantity (integer) -- The number of different headers that you want CloudFront to forward to the origin and to vary on for this cache behavior. The maximum number of headers that you can specify by name is 10. If you want CloudFront to forward all headers to the origin and vary on all of them, specify 1 for Quantity and * for Name. If you don't want CloudFront to forward any additional headers to the origin or to vary on any headers, specify 0 for Quantity and omit Items.
            Items (list) -- Optional: A complex type that contains a Name element for each header that you want CloudFront to forward to the origin and to vary on for this cache behavior. If Quantity is 0, omit Items.
            (string) --
            
            TrustedSigners (dict) -- A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content. If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled, and specify the applicable values for Quantity and Items. For more information, go to Using a Signed URL to Serve Private Content in the Amazon CloudFront Developer Guide. If you don't want to require signed URLs in requests for objects that match PathPattern, specify false for Enabled and 0 for Quantity. Omit Items. To add, change, or remove one or more trusted signers, change Enabled to true (if it's currently false), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.
            Enabled (boolean) -- Specifies whether you want to require end users to use signed URLs to access the files specified by PathPattern and TargetOriginId.
            Quantity (integer) -- The number of trusted signers for this cache behavior.
            Items (list) -- Optional: A complex type that contains trusted signers for this cache behavior. If Quantity is 0, you can omit Items.
            (string) --
            
            ViewerProtocolPolicy (string) -- Use this element to specify the protocol that users can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern. If you want CloudFront to allow end users to use any available protocol, specify allow-all. If you want CloudFront to require HTTPS, specify https. If you want CloudFront to respond to an HTTP request with an HTTP status code of 301 (Moved Permanently) and the HTTPS URL, specify redirect-to-https. The viewer then resubmits the request using the HTTPS URL.
            MinTTL (integer) -- The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront queries your origin to see whether the object has been updated.You can specify a value from 0 to 3,153,600,000 seconds (100 years).
            AllowedMethods (dict) -- A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices: - CloudFront forwards only GET and HEAD requests. - CloudFront forwards only GET, HEAD and OPTIONS requests. - CloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST, and DELETE requests. If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can't perform operations that you don't want them to. For example, you may not want users to have permission to delete objects from your origin.
            Quantity (integer) -- The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET, HEAD and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST, and DELETE requests).
            Items (list) -- A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.
            (string) --
            CachedMethods (dict) -- A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices: - CloudFront caches responses to GET and HEAD requests. - CloudFront caches responses to GET, HEAD, and OPTIONS requests. If you pick the second choice for your S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers and Origin headers for the responses to be cached correctly.
            Quantity (integer) -- The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET, HEAD, and OPTIONS requests).
            Items (list) -- A complex type that contains the HTTP methods that you want CloudFront to cache responses to.
            (string) --
            
            SmoothStreaming (boolean) -- Indicates whether you want to distribute media files in Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true; if not, specify false.
            DefaultTTL (integer) -- If you don't configure your origin to add a Cache-Control max-age directive or an Expires header, DefaultTTL is the default amount of time (in seconds) that an object is in a CloudFront cache before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age, Cache-Control s-maxage, and Expires to objects. You can specify a value from 0 to 3,153,600,000 seconds (100 years).
            MaxTTL (integer) -- The maximum amount of time (in seconds) that an object is in a CloudFront cache before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as Cache-Control max-age, Cache-Control s-maxage, and Expires to objects. You can specify a value from 0 to 3,153,600,000 seconds (100 years).
            Compress (boolean) -- Whether you want CloudFront to automatically compress content for web requests that include Accept-Encoding: gzip in the request header. If so, specify true; if not, specify false. CloudFront compresses files larger than 1000 bytes and less than 1 megabyte for both Amazon S3 and custom origins. When a CloudFront edge location is unusually busy, some files might not be compressed. The value of the Content-Type header must be on the list of file types that CloudFront will compress. For the current list, see Serving Compressed Content in the Amazon CloudFront Developer Guide. If you configure CloudFront to compress content, CloudFront removes the ETag response header from the objects that it compresses. The ETag header indicates that the version in a CloudFront edge cache is identical to the version on the origin server, but after compression the two versions are no longer identical. As a result, for compressed objects, CloudFront can't use the ETag header to determine whether an expired object in the CloudFront edge cache is still the latest version.
            
            CustomErrorResponses (dict) -- A complex type that contains zero or more CustomErrorResponse elements.
            Quantity (integer) -- The number of custom error responses for this distribution.
            Items (list) -- Optional: A complex type that contains custom error responses for this distribution. If Quantity is 0, you can omit Items.
            (dict) -- A complex type that describes how you'd prefer CloudFront to respond to requests that result in either a 4xx or 5xx response. You can control whether a custom error page should be displayed, what the desired response code should be for this error page and how long should the error response be cached by CloudFront. If you don't want to specify any custom error responses, include only an empty CustomErrorResponses element. To delete all custom error responses in an existing distribution, update the distribution configuration and include only an empty CustomErrorResponses element. To add, change, or remove one or more custom error responses, update the distribution configuration and specify all of the custom error responses that you want to include in the updated distribution.
            ErrorCode (integer) -- The 4xx or 5xx HTTP status code that you want to customize. For a list of HTTP status codes that you can customize, see CloudFront documentation.
            ResponsePagePath (string) -- The path of the custom error page (for example, /custom_404.html). The path is relative to the distribution and must begin with a slash (/). If the path includes any non-ASCII characters or unsafe characters as defined in RFC 1783 (http://www.ietf.org/rfc/rfc1738.txt), URL encode those characters. Do not URL encode any other characters in the path, or CloudFront will not return the custom error page to the viewer.
            ResponseCode (string) -- The HTTP status code that you want CloudFront to return with the custom error page to the viewer. For a list of HTTP status codes that you can replace, see CloudFront Documentation.
            ErrorCachingMinTTL (integer) -- The minimum amount of time you want HTTP error codes to stay in CloudFront caches before CloudFront queries your origin to see whether the object has been updated. You can specify a value from 0 to 31,536,000.
            
            Comment (string) -- Any comments you want to include about the distribution.
            Logging (dict) -- A complex type that controls whether access logs are written for the distribution.
            Enabled (boolean) -- Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you do not want to enable logging when you create a distribution or if you want to disable logging for an existing distribution, specify false for Enabled, and specify empty Bucket and Prefix elements. If you specify false for Enabled but you specify values for Bucket, prefix and IncludeCookies, the values are automatically deleted.
            IncludeCookies (boolean) -- Specifies whether you want CloudFront to include cookies in access logs, specify true for IncludeCookies. If you choose to include cookies in logs, CloudFront logs all cookies regardless of how you configure the cache behaviors for this distribution. If you do not want to include cookies when you create a distribution or if you want to disable include cookies for an existing distribution, specify false for IncludeCookies.
            Bucket (string) -- The Amazon S3 bucket to store the access logs in, for example, myawslogbucket.s3.amazonaws.com.
            Prefix (string) -- An optional string that you want CloudFront to prefix to the access log filenames for this distribution, for example, myprefix/. If you want to enable logging, but you do not want to specify a prefix, you still must include an empty Prefix element in the Logging element.
            PriceClass (string) -- A complex type that contains information about price class for this distribution.
            Enabled (boolean) -- Whether the distribution is enabled to accept end user requests for content.
            ViewerCertificate (dict) -- A complex type that contains information about viewer certificates for this distribution.
            CloudFrontDefaultCertificate (boolean) -- If you want viewers to use HTTPS to request your objects and you're using the CloudFront domain name of your distribution in your object URLs (for example, https://d111111abcdef8.cloudfront.net/logo.jpg), set to true. Omit this value if you are setting an ACMCertificateArn or IAMCertificateId.
            IAMCertificateId (string) -- If you want viewers to use HTTPS to request your objects and you're using an alternate domain name in your object URLs (for example, https://example.com/logo.jpg), specify the IAM certificate identifier of the custom viewer certificate for this distribution. Specify either this value, ACMCertificateArn, or CloudFrontDefaultCertificate.
            ACMCertificateArn (string) -- If you want viewers to use HTTPS to request your objects and you're using an alternate domain name in your object URLs (for example, https://example.com/logo.jpg), specify the ACM certificate ARN of the custom viewer certificate for this distribution. Specify either this value, IAMCertificateId, or CloudFrontDefaultCertificate.
            SSLSupportMethod (string) -- If you specify a value for IAMCertificateId, you must also specify how you want CloudFront to serve HTTPS requests. Valid values are vip and sni-only. If you specify vip, CloudFront uses dedicated IP addresses for your content and can respond to HTTPS requests from any viewer. However, you must request permission to use this feature, and you incur additional monthly charges. If you specify sni-only, CloudFront can only respond to HTTPS requests from viewers that support Server Name Indication (SNI). All modern browsers support SNI, but some browsers still in use don't support SNI. Do not specify a value for SSLSupportMethod if you specified true for CloudFrontDefaultCertificate.
            MinimumProtocolVersion (string) -- Specify the minimum version of the SSL protocol that you want CloudFront to use, SSLv3 or TLSv1, for HTTPS connections. CloudFront will serve your objects only to browsers or devices that support at least the SSL version that you specify. The TLSv1 protocol is more secure, so we recommend that you specify SSLv3 only if your users are using browsers or devices that don't support TLSv1. If you're using a custom certificate (if you specify a value for IAMCertificateId) and if you're using dedicated IP (if you specify vip for SSLSupportMethod), you can choose SSLv3 or TLSv1 as the MinimumProtocolVersion. If you're using a custom certificate (if you specify a value for IAMCertificateId) and if you're using SNI (if you specify sni-only for SSLSupportMethod), you must specify TLSv1 for MinimumProtocolVersion.
            Certificate (string) -- Note: this field is deprecated. Please use one of [ACMCertificateArn, IAMCertificateId, CloudFrontDefaultCertificate].
            CertificateSource (string) -- Note: this field is deprecated. Please use one of [ACMCertificateArn, IAMCertificateId, CloudFrontDefaultCertificate].
            Restrictions (dict) -- A complex type that identifies ways in which you want to restrict distribution of your content.
            GeoRestriction (dict) -- A complex type that controls the countries in which your content is distributed. For more information about geo restriction, go to Customizing Error Responses in the Amazon CloudFront Developer Guide. CloudFront determines the location of your users using MaxMind GeoIP databases. For information about the accuracy of these databases, see How accurate are your GeoIP databases? on the MaxMind website.
            RestrictionType (string) -- The method that you want to use to restrict distribution of your content by country: - none: No geo restriction is enabled, meaning access to content is not restricted by client geo location. - blacklist: The Location elements specify the countries in which you do not want CloudFront to distribute your content. - whitelist: The Location elements specify the countries in which you want CloudFront to distribute your content.
            Quantity (integer) -- When geo restriction is enabled, this is the number of countries in your whitelist or blacklist. Otherwise, when it is not enabled, Quantity is 0, and you can omit Items.
            Items (list) -- A complex type that contains a Location element for each country in which you want CloudFront either to distribute your content (whitelist) or not distribute your content (blacklist). The Location element is a two-letter, uppercase country code for a country that you want to include in your blacklist or whitelist. Include one Location element for each country. CloudFront and MaxMind both use ISO 3166 country codes. For the current list of countries and the corresponding codes, see ISO 3166-1-alpha-2 code on the International Organization for Standardization website. You can also refer to the country list in the CloudFront console, which includes both country names and codes.
            (string) --
            
            WebACLId (string) -- (Optional) If you're using AWS WAF to filter CloudFront requests, the Id of the AWS WAF web ACL that is associated with the distribution.
            
            Location (string) -- The fully qualified URI of the new distribution resource just created. For example: https://cloudfront.amazonaws.com/2010-11-01/distribution/EDFDVBD632BHDS5.
            ETag (string) -- The current version of the distribution created.
            
            
        :type DistributionConfig: dict
        """
        self.client.create_distribution(DistributionConfig=DistributionConfig)

    def create_invalidation(self, DistributionId=None, InvalidationBatch=None):
        """
        :param DistributionId: [REQUIRED] The distribution's id.
        :type DistributionId: string
        :param InvalidationBatch: [REQUIRED] The batch information for the invalidation.
            Paths (dict) -- [REQUIRED] The path of the object to invalidate. The path is relative to the distribution and must begin with a slash (/). You must enclose each invalidation object with the Path element tags. If the path includes non-ASCII characters or unsafe characters as defined in RFC 1783 (http://www.ietf.org/rfc/rfc1738.txt), URL encode those characters. Do not URL encode any other characters in the path, or CloudFront will not invalidate the old version of the updated object.
            Quantity (integer) -- [REQUIRED] The number of objects that you want to invalidate.
            Items (list) -- A complex type that contains a list of the objects that you want to invalidate.
            (string) --
            
            CallerReference (string) -- [REQUIRED] A unique name that ensures the request can't be replayed. If the CallerReference is new (no matter the content of the Path object), a new distribution is created. If the CallerReference is a value you already sent in a previous request to create an invalidation batch, and the content of each Path element is identical to the original request, the response includes the same information returned to the original request. If the CallerReference is a value you already sent in a previous request to create a distribution but the content of any Path is different from the original request, CloudFront returns an InvalidationBatchAlreadyExists error.
            
        :type InvalidationBatch: dict
        """
        self.client.create_invalidation(DistributionId=DistributionId, InvalidationBatch=InvalidationBatch)

    def create_streaming_distribution(self, StreamingDistributionConfig=None):
        """
        :param StreamingDistributionConfig: [REQUIRED] The streaming distribution's configuration information.
            CallerReference (string) -- [REQUIRED] A unique number that ensures the request can't be replayed. If the CallerReference is new (no matter the content of the StreamingDistributionConfig object), a new streaming distribution is created. If the CallerReference is a value you already sent in a previous request to create a streaming distribution, and the content of the StreamingDistributionConfig is identical to the original request (ignoring white space), the response includes the same information returned to the original request. If the CallerReference is a value you already sent in a previous request to create a streaming distribution but the content of the StreamingDistributionConfig is different from the original request, CloudFront returns a DistributionAlreadyExists error.
            S3Origin (dict) -- [REQUIRED] A complex type that contains information about the Amazon S3 bucket from which you want CloudFront to get your media files for distribution.
            DomainName (string) -- [REQUIRED] The DNS name of the S3 origin.
            OriginAccessIdentity (string) -- [REQUIRED] Your S3 origin's origin access identity.
            Aliases (dict) -- A complex type that contains information about CNAMEs (alternate domain names), if any, for this streaming distribution.
            Quantity (integer) -- [REQUIRED] The number of CNAMEs, if any, for this distribution.
            Items (list) -- Optional: A complex type that contains CNAME elements, if any, for this distribution. If Quantity is 0, you can omit Items.
            (string) --
            
            Comment (string) -- [REQUIRED] Any comments you want to include about the streaming distribution.
            Logging (dict) -- A complex type that controls whether access logs are written for the streaming distribution.
            Enabled (boolean) -- [REQUIRED] Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you do not want to enable logging when you create a streaming distribution or if you want to disable logging for an existing streaming distribution, specify false for Enabled, and specify empty Bucket and Prefix elements. If you specify false for Enabled but you specify values for Bucket and Prefix, the values are automatically deleted.
            Bucket (string) -- [REQUIRED] The Amazon S3 bucket to store the access logs in, for example, myawslogbucket.s3.amazonaws.com.
            Prefix (string) -- [REQUIRED] An optional string that you want CloudFront to prefix to the access log filenames for this streaming distribution, for example, myprefix/. If you want to enable logging, but you do not want to specify a prefix, you still must include an empty Prefix element in the Logging element.
            TrustedSigners (dict) -- [REQUIRED] A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content. If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled, and specify the applicable values for Quantity and Items. For more information, go to Using a Signed URL to Serve Private Content in the Amazon CloudFront Developer Guide. If you don't want to require signed URLs in requests for objects that match PathPattern, specify false for Enabled and 0 for Quantity. Omit Items. To add, change, or remove one or more trusted signers, change Enabled to true (if it's currently false), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.
            Enabled (boolean) -- [REQUIRED] Specifies whether you want to require end users to use signed URLs to access the files specified by PathPattern and TargetOriginId.
            Quantity (integer) -- [REQUIRED] The number of trusted signers for this cache behavior.
            Items (list) -- Optional: A complex type that contains trusted signers for this cache behavior. If Quantity is 0, you can omit Items.
            (string) --
            
            PriceClass (string) -- A complex type that contains information about price class for this streaming distribution.
            Enabled (boolean) -- [REQUIRED] Whether the streaming distribution is enabled to accept end user requests for content.
            Return typedict
            ReturnsResponse Syntax{
              'StreamingDistribution': {
                'Id': 'string',
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
            (dict) -- The returned result of the corresponding request.
            StreamingDistribution (dict) -- The streaming distribution's information.
            Id (string) -- The identifier for the streaming distribution. For example: EGTXBD79H29TRA8.
            Status (string) -- The current status of the streaming distribution. When the status is Deployed, the distribution's information is fully propagated throughout the Amazon CloudFront system.
            LastModifiedTime (datetime) -- The date and time the distribution was last modified.
            DomainName (string) -- The domain name corresponding to the streaming distribution. For example: s5c39gqb8ow64r.cloudfront.net.
            ActiveTrustedSigners (dict) -- CloudFront automatically adds this element to the response only if you've set up the distribution to serve private content with signed URLs. The element lists the key pair IDs that CloudFront is aware of for each trusted signer. The Signer child element lists the AWS account number of the trusted signer (or an empty Self element if the signer is you). The Signer element also includes the IDs of any active key pairs associated with the trusted signer's AWS account. If no KeyPairId element appears for a Signer, that signer can't create working signed URLs.
            Enabled (boolean) -- Each active trusted signer.
            Quantity (integer) -- The number of unique trusted signers included in all cache behaviors. For example, if three cache behaviors all list the same three AWS accounts, the value of Quantity for ActiveTrustedSigners will be 3.
            Items (list) -- A complex type that contains one Signer complex type for each unique trusted signer that is specified in the TrustedSigners complex type, including trusted signers in the default cache behavior and in all of the other cache behaviors.
            (dict) -- A complex type that lists the AWS accounts that were included in the TrustedSigners complex type, as well as their active CloudFront key pair IDs, if any.
            AwsAccountNumber (string) -- Specifies an AWS account that can create signed URLs. Values: self, which indicates that the AWS account that was used to create the distribution can created signed URLs, or an AWS account number. Omit the dashes in the account number.
            KeyPairIds (dict) -- A complex type that lists the active CloudFront key pairs, if any, that are associated with AwsAccountNumber.
            Quantity (integer) -- The number of active CloudFront key pairs for AwsAccountNumber.
            Items (list) -- A complex type that lists the active CloudFront key pairs, if any, that are associated with AwsAccountNumber.
            (string) --
            
            
            StreamingDistributionConfig (dict) -- The current configuration information for the streaming distribution.
            CallerReference (string) -- A unique number that ensures the request can't be replayed. If the CallerReference is new (no matter the content of the StreamingDistributionConfig object), a new streaming distribution is created. If the CallerReference is a value you already sent in a previous request to create a streaming distribution, and the content of the StreamingDistributionConfig is identical to the original request (ignoring white space), the response includes the same information returned to the original request. If the CallerReference is a value you already sent in a previous request to create a streaming distribution but the content of the StreamingDistributionConfig is different from the original request, CloudFront returns a DistributionAlreadyExists error.
            S3Origin (dict) -- A complex type that contains information about the Amazon S3 bucket from which you want CloudFront to get your media files for distribution.
            DomainName (string) -- The DNS name of the S3 origin.
            OriginAccessIdentity (string) -- Your S3 origin's origin access identity.
            Aliases (dict) -- A complex type that contains information about CNAMEs (alternate domain names), if any, for this streaming distribution.
            Quantity (integer) -- The number of CNAMEs, if any, for this distribution.
            Items (list) -- Optional: A complex type that contains CNAME elements, if any, for this distribution. If Quantity is 0, you can omit Items.
            (string) --
            
            Comment (string) -- Any comments you want to include about the streaming distribution.
            Logging (dict) -- A complex type that controls whether access logs are written for the streaming distribution.
            Enabled (boolean) -- Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you do not want to enable logging when you create a streaming distribution or if you want to disable logging for an existing streaming distribution, specify false for Enabled, and specify empty Bucket and Prefix elements. If you specify false for Enabled but you specify values for Bucket and Prefix, the values are automatically deleted.
            Bucket (string) -- The Amazon S3 bucket to store the access logs in, for example, myawslogbucket.s3.amazonaws.com.
            Prefix (string) -- An optional string that you want CloudFront to prefix to the access log filenames for this streaming distribution, for example, myprefix/. If you want to enable logging, but you do not want to specify a prefix, you still must include an empty Prefix element in the Logging element.
            TrustedSigners (dict) -- A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content. If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled, and specify the applicable values for Quantity and Items. For more information, go to Using a Signed URL to Serve Private Content in the Amazon CloudFront Developer Guide. If you don't want to require signed URLs in requests for objects that match PathPattern, specify false for Enabled and 0 for Quantity. Omit Items. To add, change, or remove one or more trusted signers, change Enabled to true (if it's currently false), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.
            Enabled (boolean) -- Specifies whether you want to require end users to use signed URLs to access the files specified by PathPattern and TargetOriginId.
            Quantity (integer) -- The number of trusted signers for this cache behavior.
            Items (list) -- Optional: A complex type that contains trusted signers for this cache behavior. If Quantity is 0, you can omit Items.
            (string) --
            
            PriceClass (string) -- A complex type that contains information about price class for this streaming distribution.
            Enabled (boolean) -- Whether the streaming distribution is enabled to accept end user requests for content.
            
            Location (string) -- The fully qualified URI of the new streaming distribution resource just created. For example: https://cloudfront.amazonaws.com/2010-11-01/streaming-distribution/EGTXBD79H29TRA8.
            ETag (string) -- The current version of the streaming distribution created.
            
            
        :type StreamingDistributionConfig: dict
        """
        self.client.create_streaming_distribution(StreamingDistributionConfig=StreamingDistributionConfig)

    def delete_cloud_front_origin_access_identity(self, Id=None, IfMatch=None):
        """
        :param Id: [REQUIRED] The origin access identity's id.
        :type Id: string
        :param IfMatch: The value of the ETag header you received from a previous GET or PUT request. For example: E2QWRUHAPOMQZL.
        :type IfMatch: string
        """
        self.client.delete_cloud_front_origin_access_identity(Id=Id, IfMatch=IfMatch)

    def delete_distribution(self, Id=None, IfMatch=None):
        """
        :param Id: [REQUIRED] The distribution id.
        :type Id: string
        :param IfMatch: The value of the ETag header you received when you disabled the distribution. For example: E2QWRUHAPOMQZL.
        :type IfMatch: string
        """
        self.client.delete_distribution(Id=Id, IfMatch=IfMatch)

    def delete_streaming_distribution(self, Id=None, IfMatch=None):
        """
        :param Id: [REQUIRED] The distribution id.
        :type Id: string
        :param IfMatch: The value of the ETag header you received when you disabled the streaming distribution. For example: E2QWRUHAPOMQZL.
        :type IfMatch: string
        """
        self.client.delete_streaming_distribution(Id=Id, IfMatch=IfMatch)

    def generate_presigned_url(self, ClientMethod=None, Params=None, ExpiresIn=None, HttpMethod=None):
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
        self.client.generate_presigned_url(ClientMethod=ClientMethod, Params=Params, ExpiresIn=ExpiresIn,
                                           HttpMethod=HttpMethod)

    def get_cloud_front_origin_access_identity(self, Id=None):
        """
        :param Id: [REQUIRED] The identity's id.
            Return typedict
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
            (dict) -- The returned result of the corresponding request.
            CloudFrontOriginAccessIdentity (dict) -- The origin access identity's information.
            Id (string) -- The ID for the origin access identity. For example: E74FTE3AJFJ256A.
            S3CanonicalUserId (string) -- The Amazon S3 canonical user ID for the origin access identity, which you use when giving the origin access identity read permission to an object in Amazon S3.
            CloudFrontOriginAccessIdentityConfig (dict) -- The current configuration information for the identity.
            CallerReference (string) -- A unique number that ensures the request can't be replayed. If the CallerReference is new (no matter the content of the CloudFrontOriginAccessIdentityConfig object), a new origin access identity is created. If the CallerReference is a value you already sent in a previous request to create an identity, and the content of the CloudFrontOriginAccessIdentityConfig is identical to the original request (ignoring white space), the response includes the same information returned to the original request. If the CallerReference is a value you already sent in a previous request to create an identity but the content of the CloudFrontOriginAccessIdentityConfig is different from the original request, CloudFront returns a CloudFrontOriginAccessIdentityAlreadyExists error.
            Comment (string) -- Any comments you want to include about the origin access identity.
            
            ETag (string) -- The current version of the origin access identity's information. For example: E2QWRUHAPOMQZL.
            
            
        :type Id: string
        """
        self.client.get_cloud_front_origin_access_identity(Id=Id)

    def get_cloud_front_origin_access_identity_config(self, Id=None):
        """
        :param Id: [REQUIRED] The identity's id.
            Return typedict
            ReturnsResponse Syntax{
              'CloudFrontOriginAccessIdentityConfig': {
                'CallerReference': 'string',
                'Comment': 'string'
              },
              'ETag': 'string'
            }
            Response Structure
            (dict) -- The returned result of the corresponding request.
            CloudFrontOriginAccessIdentityConfig (dict) -- The origin access identity's configuration information.
            CallerReference (string) -- A unique number that ensures the request can't be replayed. If the CallerReference is new (no matter the content of the CloudFrontOriginAccessIdentityConfig object), a new origin access identity is created. If the CallerReference is a value you already sent in a previous request to create an identity, and the content of the CloudFrontOriginAccessIdentityConfig is identical to the original request (ignoring white space), the response includes the same information returned to the original request. If the CallerReference is a value you already sent in a previous request to create an identity but the content of the CloudFrontOriginAccessIdentityConfig is different from the original request, CloudFront returns a CloudFrontOriginAccessIdentityAlreadyExists error.
            Comment (string) -- Any comments you want to include about the origin access identity.
            ETag (string) -- The current version of the configuration. For example: E2QWRUHAPOMQZL.
            
            
        :type Id: string
        """
        self.client.get_cloud_front_origin_access_identity_config(Id=Id)

    def get_distribution(self, Id=None):
        """
        :param Id: [REQUIRED] The distribution's id.
            Return typedict
            ReturnsResponse Syntax{
              'Distribution': {
                'Id': 'string',
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
                          }
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
                    'Compress': True|False
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
                        'Compress': True|False
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
                    'MinimumProtocolVersion': 'SSLv3'|'TLSv1',
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
                  'WebACLId': 'string'
                }
              },
              'ETag': 'string'
            }
            Response Structure
            (dict) -- The returned result of the corresponding request.
            Distribution (dict) -- The distribution's information.
            Id (string) -- The identifier for the distribution. For example: EDFDVBD632BHDS5.
            Status (string) -- This response element indicates the current status of the distribution. When the status is Deployed, the distribution's information is fully propagated throughout the Amazon CloudFront system.
            LastModifiedTime (datetime) -- The date and time the distribution was last modified.
            InProgressInvalidationBatches (integer) -- The number of invalidation batches currently in progress.
            DomainName (string) -- The domain name corresponding to the distribution. For example: d604721fxaaqy9.cloudfront.net.
            ActiveTrustedSigners (dict) -- CloudFront automatically adds this element to the response only if you've set up the distribution to serve private content with signed URLs. The element lists the key pair IDs that CloudFront is aware of for each trusted signer. The Signer child element lists the AWS account number of the trusted signer (or an empty Self element if the signer is you). The Signer element also includes the IDs of any active key pairs associated with the trusted signer's AWS account. If no KeyPairId element appears for a Signer, that signer can't create working signed URLs.
            Enabled (boolean) -- Each active trusted signer.
            Quantity (integer) -- The number of unique trusted signers included in all cache behaviors. For example, if three cache behaviors all list the same three AWS accounts, the value of Quantity for ActiveTrustedSigners will be 3.
            Items (list) -- A complex type that contains one Signer complex type for each unique trusted signer that is specified in the TrustedSigners complex type, including trusted signers in the default cache behavior and in all of the other cache behaviors.
            (dict) -- A complex type that lists the AWS accounts that were included in the TrustedSigners complex type, as well as their active CloudFront key pair IDs, if any.
            AwsAccountNumber (string) -- Specifies an AWS account that can create signed URLs. Values: self, which indicates that the AWS account that was used to create the distribution can created signed URLs, or an AWS account number. Omit the dashes in the account number.
            KeyPairIds (dict) -- A complex type that lists the active CloudFront key pairs, if any, that are associated with AwsAccountNumber.
            Quantity (integer) -- The number of active CloudFront key pairs for AwsAccountNumber.
            Items (list) -- A complex type that lists the active CloudFront key pairs, if any, that are associated with AwsAccountNumber.
            (string) --
            
            
            DistributionConfig (dict) -- The current configuration information for the distribution.
            CallerReference (string) -- A unique number that ensures the request can't be replayed. If the CallerReference is new (no matter the content of the DistributionConfig object), a new distribution is created. If the CallerReference is a value you already sent in a previous request to create a distribution, and the content of the DistributionConfig is identical to the original request (ignoring white space), the response includes the same information returned to the original request. If the CallerReference is a value you already sent in a previous request to create a distribution but the content of the DistributionConfig is different from the original request, CloudFront returns a DistributionAlreadyExists error.
            Aliases (dict) -- A complex type that contains information about CNAMEs (alternate domain names), if any, for this distribution.
            Quantity (integer) -- The number of CNAMEs, if any, for this distribution.
            Items (list) -- Optional: A complex type that contains CNAME elements, if any, for this distribution. If Quantity is 0, you can omit Items.
            (string) --
            
            DefaultRootObject (string) -- The object that you want CloudFront to return (for example, index.html) when an end user requests the root URL for your distribution (http://www.example.com) instead of an object in your distribution (http://www.example.com/index.html). Specifying a default root object avoids exposing the contents of your distribution. If you don't want to specify a default root object when you create a distribution, include an empty DefaultRootObject element. To delete the default root object from an existing distribution, update the distribution configuration and include an empty DefaultRootObject element. To replace the default root object, update the distribution configuration and specify the new object.
            Origins (dict) -- A complex type that contains information about origins for this distribution.
            Quantity (integer) -- The number of origins for this distribution.
            Items (list) -- A complex type that contains origins for this distribution.
            (dict) -- A complex type that describes the Amazon S3 bucket or the HTTP server (for example, a web server) from which CloudFront gets your files.You must create at least one origin.
            Id (string) -- A unique identifier for the origin. The value of Id must be unique within the distribution. You use the value of Id when you create a cache behavior. The Id identifies the origin that CloudFront routes a request to when the request matches the path pattern for that cache behavior.
            DomainName (string) -- Amazon S3 origins: The DNS name of the Amazon S3 bucket from which you want CloudFront to get objects for this origin, for example, myawsbucket.s3.amazonaws.com. Custom origins: The DNS domain name for the HTTP server from which you want CloudFront to get objects for this origin, for example, www.example.com.
            OriginPath (string) -- An optional element that causes CloudFront to request your content from a directory in your Amazon S3 bucket or your custom origin. When you include the OriginPath element, specify the directory name, beginning with a /. CloudFront appends the directory name to the value of DomainName.
            CustomHeaders (dict) -- A complex type that contains information about the custom headers associated with this Origin.
            Quantity (integer) -- The number of custom headers for this origin.
            Items (list) -- A complex type that contains the custom headers for this Origin.
            (dict) -- A complex type that contains information related to a Header
            HeaderName (string) -- The header's name.
            HeaderValue (string) -- The header's value.
            
            S3OriginConfig (dict) -- A complex type that contains information about the Amazon S3 origin. If the origin is a custom origin, use the CustomOriginConfig element instead.
            OriginAccessIdentity (string) -- The CloudFront origin access identity to associate with the origin. Use an origin access identity to configure the origin so that end users can only access objects in an Amazon S3 bucket through CloudFront. If you want end users to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty OriginAccessIdentity element. To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty OriginAccessIdentity element. To replace the origin access identity, update the distribution configuration and specify the new origin access identity. Use the format origin-access-identity/cloudfront/Id where Id is the value that CloudFront returned in the Id element when you created the origin access identity.
            CustomOriginConfig (dict) -- A complex type that contains information about a custom origin. If the origin is an Amazon S3 bucket, use the S3OriginConfig element instead.
            HTTPPort (integer) -- The HTTP port the custom origin listens on.
            HTTPSPort (integer) -- The HTTPS port the custom origin listens on.
            OriginProtocolPolicy (string) -- The origin protocol policy to apply to your origin.
            OriginSslProtocols (dict) -- The SSL/TLS protocols that you want CloudFront to use when communicating with your origin over HTTPS.
            Quantity (integer) -- The number of SSL/TLS protocols that you want to allow CloudFront to use when establishing an HTTPS connection with this origin.
            Items (list) -- A complex type that contains one SslProtocol element for each SSL/TLS protocol that you want to allow CloudFront to use when establishing an HTTPS connection with this origin.
            (string) --
            
            
            
            DefaultCacheBehavior (dict) -- A complex type that describes the default cache behavior if you do not specify a CacheBehavior element or if files don't match any of the values of PathPattern in CacheBehavior elements.You must create exactly one default cache behavior.
            TargetOriginId (string) -- The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior.
            ForwardedValues (dict) -- A complex type that specifies how CloudFront handles query strings, cookies and headers.
            QueryString (boolean) -- Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior. If so, specify true; if not, specify false.
            Cookies (dict) -- A complex type that specifies how CloudFront handles cookies.
            Forward (string) -- Use this element to specify whether you want CloudFront to forward cookies to the origin that is associated with this cache behavior. You can specify all, none or whitelist. If you choose All, CloudFront forwards all cookies regardless of how many your application uses.
            WhitelistedNames (dict) -- A complex type that specifies the whitelisted cookies, if any, that you want CloudFront to forward to your origin that is associated with this cache behavior.
            Quantity (integer) -- The number of whitelisted cookies for this cache behavior.
            Items (list) -- Optional: A complex type that contains whitelisted cookies for this cache behavior. If Quantity is 0, you can omit Items.
            (string) --
            
            Headers (dict) -- A complex type that specifies the Headers, if any, that you want CloudFront to vary upon for this cache behavior.
            Quantity (integer) -- The number of different headers that you want CloudFront to forward to the origin and to vary on for this cache behavior. The maximum number of headers that you can specify by name is 10. If you want CloudFront to forward all headers to the origin and vary on all of them, specify 1 for Quantity and * for Name. If you don't want CloudFront to forward any additional headers to the origin or to vary on any headers, specify 0 for Quantity and omit Items.
            Items (list) -- Optional: A complex type that contains a Name element for each header that you want CloudFront to forward to the origin and to vary on for this cache behavior. If Quantity is 0, omit Items.
            (string) --
            
            TrustedSigners (dict) -- A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content. If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled, and specify the applicable values for Quantity and Items. For more information, go to Using a Signed URL to Serve Private Content in the Amazon CloudFront Developer Guide. If you don't want to require signed URLs in requests for objects that match PathPattern, specify false for Enabled and 0 for Quantity. Omit Items. To add, change, or remove one or more trusted signers, change Enabled to true (if it's currently false), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.
            Enabled (boolean) -- Specifies whether you want to require end users to use signed URLs to access the files specified by PathPattern and TargetOriginId.
            Quantity (integer) -- The number of trusted signers for this cache behavior.
            Items (list) -- Optional: A complex type that contains trusted signers for this cache behavior. If Quantity is 0, you can omit Items.
            (string) --
            
            ViewerProtocolPolicy (string) -- Use this element to specify the protocol that users can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern. If you want CloudFront to allow end users to use any available protocol, specify allow-all. If you want CloudFront to require HTTPS, specify https. If you want CloudFront to respond to an HTTP request with an HTTP status code of 301 (Moved Permanently) and the HTTPS URL, specify redirect-to-https. The viewer then resubmits the request using the HTTPS URL.
            MinTTL (integer) -- The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront queries your origin to see whether the object has been updated.You can specify a value from 0 to 3,153,600,000 seconds (100 years).
            AllowedMethods (dict) -- A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices: - CloudFront forwards only GET and HEAD requests. - CloudFront forwards only GET, HEAD and OPTIONS requests. - CloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST, and DELETE requests. If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can't perform operations that you don't want them to. For example, you may not want users to have permission to delete objects from your origin.
            Quantity (integer) -- The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET, HEAD and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST, and DELETE requests).
            Items (list) -- A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.
            (string) --
            CachedMethods (dict) -- A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices: - CloudFront caches responses to GET and HEAD requests. - CloudFront caches responses to GET, HEAD, and OPTIONS requests. If you pick the second choice for your S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers and Origin headers for the responses to be cached correctly.
            Quantity (integer) -- The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET, HEAD, and OPTIONS requests).
            Items (list) -- A complex type that contains the HTTP methods that you want CloudFront to cache responses to.
            (string) --
            
            SmoothStreaming (boolean) -- Indicates whether you want to distribute media files in Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true; if not, specify false.
            DefaultTTL (integer) -- If you don't configure your origin to add a Cache-Control max-age directive or an Expires header, DefaultTTL is the default amount of time (in seconds) that an object is in a CloudFront cache before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age, Cache-Control s-maxage, and Expires to objects. You can specify a value from 0 to 3,153,600,000 seconds (100 years).
            MaxTTL (integer) -- The maximum amount of time (in seconds) that an object is in a CloudFront cache before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as Cache-Control max-age, Cache-Control s-maxage, and Expires to objects. You can specify a value from 0 to 3,153,600,000 seconds (100 years).
            Compress (boolean) -- Whether you want CloudFront to automatically compress content for web requests that include Accept-Encoding: gzip in the request header. If so, specify true; if not, specify false. CloudFront compresses files larger than 1000 bytes and less than 1 megabyte for both Amazon S3 and custom origins. When a CloudFront edge location is unusually busy, some files might not be compressed. The value of the Content-Type header must be on the list of file types that CloudFront will compress. For the current list, see Serving Compressed Content in the Amazon CloudFront Developer Guide. If you configure CloudFront to compress content, CloudFront removes the ETag response header from the objects that it compresses. The ETag header indicates that the version in a CloudFront edge cache is identical to the version on the origin server, but after compression the two versions are no longer identical. As a result, for compressed objects, CloudFront can't use the ETag header to determine whether an expired object in the CloudFront edge cache is still the latest version.
            CacheBehaviors (dict) -- A complex type that contains zero or more CacheBehavior elements.
            Quantity (integer) -- The number of cache behaviors for this distribution.
            Items (list) -- Optional: A complex type that contains cache behaviors for this distribution. If Quantity is 0, you can omit Items.
            (dict) -- A complex type that describes how CloudFront processes requests. You can create up to 10 cache behaviors.You must create at least as many cache behaviors (including the default cache behavior) as you have origins if you want CloudFront to distribute objects from all of the origins. Each cache behavior specifies the one origin from which you want CloudFront to get objects. If you have two origins and only the default cache behavior, the default cache behavior will cause CloudFront to get objects from one of the origins, but the other origin will never be used. If you don't want to specify any cache behaviors, include only an empty CacheBehaviors element. Don't include an empty CacheBehavior element, or CloudFront returns a MalformedXML error. To delete all cache behaviors in an existing distribution, update the distribution configuration and include only an empty CacheBehaviors element. To add, change, or remove one or more cache behaviors, update the distribution configuration and specify all of the cache behaviors that you want to include in the updated distribution.
            PathPattern (string) -- The pattern (for example, images/*.jpg) that specifies which requests you want this cache behavior to apply to. When CloudFront receives an end-user request, the requested path is compared with path patterns in the order in which cache behaviors are listed in the distribution. The path pattern for the default cache behavior is * and cannot be changed. If the request for an object does not match the path pattern for any cache behaviors, CloudFront applies the behavior in the default cache behavior.
            TargetOriginId (string) -- The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior.
            ForwardedValues (dict) -- A complex type that specifies how CloudFront handles query strings, cookies and headers.
            QueryString (boolean) -- Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior. If so, specify true; if not, specify false.
            Cookies (dict) -- A complex type that specifies how CloudFront handles cookies.
            Forward (string) -- Use this element to specify whether you want CloudFront to forward cookies to the origin that is associated with this cache behavior. You can specify all, none or whitelist. If you choose All, CloudFront forwards all cookies regardless of how many your application uses.
            WhitelistedNames (dict) -- A complex type that specifies the whitelisted cookies, if any, that you want CloudFront to forward to your origin that is associated with this cache behavior.
            Quantity (integer) -- The number of whitelisted cookies for this cache behavior.
            Items (list) -- Optional: A complex type that contains whitelisted cookies for this cache behavior. If Quantity is 0, you can omit Items.
            (string) --
            
            Headers (dict) -- A complex type that specifies the Headers, if any, that you want CloudFront to vary upon for this cache behavior.
            Quantity (integer) -- The number of different headers that you want CloudFront to forward to the origin and to vary on for this cache behavior. The maximum number of headers that you can specify by name is 10. If you want CloudFront to forward all headers to the origin and vary on all of them, specify 1 for Quantity and * for Name. If you don't want CloudFront to forward any additional headers to the origin or to vary on any headers, specify 0 for Quantity and omit Items.
            Items (list) -- Optional: A complex type that contains a Name element for each header that you want CloudFront to forward to the origin and to vary on for this cache behavior. If Quantity is 0, omit Items.
            (string) --
            
            TrustedSigners (dict) -- A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content. If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled, and specify the applicable values for Quantity and Items. For more information, go to Using a Signed URL to Serve Private Content in the Amazon CloudFront Developer Guide. If you don't want to require signed URLs in requests for objects that match PathPattern, specify false for Enabled and 0 for Quantity. Omit Items. To add, change, or remove one or more trusted signers, change Enabled to true (if it's currently false), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.
            Enabled (boolean) -- Specifies whether you want to require end users to use signed URLs to access the files specified by PathPattern and TargetOriginId.
            Quantity (integer) -- The number of trusted signers for this cache behavior.
            Items (list) -- Optional: A complex type that contains trusted signers for this cache behavior. If Quantity is 0, you can omit Items.
            (string) --
            
            ViewerProtocolPolicy (string) -- Use this element to specify the protocol that users can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern. If you want CloudFront to allow end users to use any available protocol, specify allow-all. If you want CloudFront to require HTTPS, specify https. If you want CloudFront to respond to an HTTP request with an HTTP status code of 301 (Moved Permanently) and the HTTPS URL, specify redirect-to-https. The viewer then resubmits the request using the HTTPS URL.
            MinTTL (integer) -- The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront queries your origin to see whether the object has been updated.You can specify a value from 0 to 3,153,600,000 seconds (100 years).
            AllowedMethods (dict) -- A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices: - CloudFront forwards only GET and HEAD requests. - CloudFront forwards only GET, HEAD and OPTIONS requests. - CloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST, and DELETE requests. If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can't perform operations that you don't want them to. For example, you may not want users to have permission to delete objects from your origin.
            Quantity (integer) -- The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET, HEAD and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST, and DELETE requests).
            Items (list) -- A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.
            (string) --
            CachedMethods (dict) -- A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices: - CloudFront caches responses to GET and HEAD requests. - CloudFront caches responses to GET, HEAD, and OPTIONS requests. If you pick the second choice for your S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers and Origin headers for the responses to be cached correctly.
            Quantity (integer) -- The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET, HEAD, and OPTIONS requests).
            Items (list) -- A complex type that contains the HTTP methods that you want CloudFront to cache responses to.
            (string) --
            
            SmoothStreaming (boolean) -- Indicates whether you want to distribute media files in Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true; if not, specify false.
            DefaultTTL (integer) -- If you don't configure your origin to add a Cache-Control max-age directive or an Expires header, DefaultTTL is the default amount of time (in seconds) that an object is in a CloudFront cache before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age, Cache-Control s-maxage, and Expires to objects. You can specify a value from 0 to 3,153,600,000 seconds (100 years).
            MaxTTL (integer) -- The maximum amount of time (in seconds) that an object is in a CloudFront cache before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as Cache-Control max-age, Cache-Control s-maxage, and Expires to objects. You can specify a value from 0 to 3,153,600,000 seconds (100 years).
            Compress (boolean) -- Whether you want CloudFront to automatically compress content for web requests that include Accept-Encoding: gzip in the request header. If so, specify true; if not, specify false. CloudFront compresses files larger than 1000 bytes and less than 1 megabyte for both Amazon S3 and custom origins. When a CloudFront edge location is unusually busy, some files might not be compressed. The value of the Content-Type header must be on the list of file types that CloudFront will compress. For the current list, see Serving Compressed Content in the Amazon CloudFront Developer Guide. If you configure CloudFront to compress content, CloudFront removes the ETag response header from the objects that it compresses. The ETag header indicates that the version in a CloudFront edge cache is identical to the version on the origin server, but after compression the two versions are no longer identical. As a result, for compressed objects, CloudFront can't use the ETag header to determine whether an expired object in the CloudFront edge cache is still the latest version.
            
            CustomErrorResponses (dict) -- A complex type that contains zero or more CustomErrorResponse elements.
            Quantity (integer) -- The number of custom error responses for this distribution.
            Items (list) -- Optional: A complex type that contains custom error responses for this distribution. If Quantity is 0, you can omit Items.
            (dict) -- A complex type that describes how you'd prefer CloudFront to respond to requests that result in either a 4xx or 5xx response. You can control whether a custom error page should be displayed, what the desired response code should be for this error page and how long should the error response be cached by CloudFront. If you don't want to specify any custom error responses, include only an empty CustomErrorResponses element. To delete all custom error responses in an existing distribution, update the distribution configuration and include only an empty CustomErrorResponses element. To add, change, or remove one or more custom error responses, update the distribution configuration and specify all of the custom error responses that you want to include in the updated distribution.
            ErrorCode (integer) -- The 4xx or 5xx HTTP status code that you want to customize. For a list of HTTP status codes that you can customize, see CloudFront documentation.
            ResponsePagePath (string) -- The path of the custom error page (for example, /custom_404.html). The path is relative to the distribution and must begin with a slash (/). If the path includes any non-ASCII characters or unsafe characters as defined in RFC 1783 (http://www.ietf.org/rfc/rfc1738.txt), URL encode those characters. Do not URL encode any other characters in the path, or CloudFront will not return the custom error page to the viewer.
            ResponseCode (string) -- The HTTP status code that you want CloudFront to return with the custom error page to the viewer. For a list of HTTP status codes that you can replace, see CloudFront Documentation.
            ErrorCachingMinTTL (integer) -- The minimum amount of time you want HTTP error codes to stay in CloudFront caches before CloudFront queries your origin to see whether the object has been updated. You can specify a value from 0 to 31,536,000.
            
            Comment (string) -- Any comments you want to include about the distribution.
            Logging (dict) -- A complex type that controls whether access logs are written for the distribution.
            Enabled (boolean) -- Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you do not want to enable logging when you create a distribution or if you want to disable logging for an existing distribution, specify false for Enabled, and specify empty Bucket and Prefix elements. If you specify false for Enabled but you specify values for Bucket, prefix and IncludeCookies, the values are automatically deleted.
            IncludeCookies (boolean) -- Specifies whether you want CloudFront to include cookies in access logs, specify true for IncludeCookies. If you choose to include cookies in logs, CloudFront logs all cookies regardless of how you configure the cache behaviors for this distribution. If you do not want to include cookies when you create a distribution or if you want to disable include cookies for an existing distribution, specify false for IncludeCookies.
            Bucket (string) -- The Amazon S3 bucket to store the access logs in, for example, myawslogbucket.s3.amazonaws.com.
            Prefix (string) -- An optional string that you want CloudFront to prefix to the access log filenames for this distribution, for example, myprefix/. If you want to enable logging, but you do not want to specify a prefix, you still must include an empty Prefix element in the Logging element.
            PriceClass (string) -- A complex type that contains information about price class for this distribution.
            Enabled (boolean) -- Whether the distribution is enabled to accept end user requests for content.
            ViewerCertificate (dict) -- A complex type that contains information about viewer certificates for this distribution.
            CloudFrontDefaultCertificate (boolean) -- If you want viewers to use HTTPS to request your objects and you're using the CloudFront domain name of your distribution in your object URLs (for example, https://d111111abcdef8.cloudfront.net/logo.jpg), set to true. Omit this value if you are setting an ACMCertificateArn or IAMCertificateId.
            IAMCertificateId (string) -- If you want viewers to use HTTPS to request your objects and you're using an alternate domain name in your object URLs (for example, https://example.com/logo.jpg), specify the IAM certificate identifier of the custom viewer certificate for this distribution. Specify either this value, ACMCertificateArn, or CloudFrontDefaultCertificate.
            ACMCertificateArn (string) -- If you want viewers to use HTTPS to request your objects and you're using an alternate domain name in your object URLs (for example, https://example.com/logo.jpg), specify the ACM certificate ARN of the custom viewer certificate for this distribution. Specify either this value, IAMCertificateId, or CloudFrontDefaultCertificate.
            SSLSupportMethod (string) -- If you specify a value for IAMCertificateId, you must also specify how you want CloudFront to serve HTTPS requests. Valid values are vip and sni-only. If you specify vip, CloudFront uses dedicated IP addresses for your content and can respond to HTTPS requests from any viewer. However, you must request permission to use this feature, and you incur additional monthly charges. If you specify sni-only, CloudFront can only respond to HTTPS requests from viewers that support Server Name Indication (SNI). All modern browsers support SNI, but some browsers still in use don't support SNI. Do not specify a value for SSLSupportMethod if you specified true for CloudFrontDefaultCertificate.
            MinimumProtocolVersion (string) -- Specify the minimum version of the SSL protocol that you want CloudFront to use, SSLv3 or TLSv1, for HTTPS connections. CloudFront will serve your objects only to browsers or devices that support at least the SSL version that you specify. The TLSv1 protocol is more secure, so we recommend that you specify SSLv3 only if your users are using browsers or devices that don't support TLSv1. If you're using a custom certificate (if you specify a value for IAMCertificateId) and if you're using dedicated IP (if you specify vip for SSLSupportMethod), you can choose SSLv3 or TLSv1 as the MinimumProtocolVersion. If you're using a custom certificate (if you specify a value for IAMCertificateId) and if you're using SNI (if you specify sni-only for SSLSupportMethod), you must specify TLSv1 for MinimumProtocolVersion.
            Certificate (string) -- Note: this field is deprecated. Please use one of [ACMCertificateArn, IAMCertificateId, CloudFrontDefaultCertificate].
            CertificateSource (string) -- Note: this field is deprecated. Please use one of [ACMCertificateArn, IAMCertificateId, CloudFrontDefaultCertificate].
            Restrictions (dict) -- A complex type that identifies ways in which you want to restrict distribution of your content.
            GeoRestriction (dict) -- A complex type that controls the countries in which your content is distributed. For more information about geo restriction, go to Customizing Error Responses in the Amazon CloudFront Developer Guide. CloudFront determines the location of your users using MaxMind GeoIP databases. For information about the accuracy of these databases, see How accurate are your GeoIP databases? on the MaxMind website.
            RestrictionType (string) -- The method that you want to use to restrict distribution of your content by country: - none: No geo restriction is enabled, meaning access to content is not restricted by client geo location. - blacklist: The Location elements specify the countries in which you do not want CloudFront to distribute your content. - whitelist: The Location elements specify the countries in which you want CloudFront to distribute your content.
            Quantity (integer) -- When geo restriction is enabled, this is the number of countries in your whitelist or blacklist. Otherwise, when it is not enabled, Quantity is 0, and you can omit Items.
            Items (list) -- A complex type that contains a Location element for each country in which you want CloudFront either to distribute your content (whitelist) or not distribute your content (blacklist). The Location element is a two-letter, uppercase country code for a country that you want to include in your blacklist or whitelist. Include one Location element for each country. CloudFront and MaxMind both use ISO 3166 country codes. For the current list of countries and the corresponding codes, see ISO 3166-1-alpha-2 code on the International Organization for Standardization website. You can also refer to the country list in the CloudFront console, which includes both country names and codes.
            (string) --
            
            WebACLId (string) -- (Optional) If you're using AWS WAF to filter CloudFront requests, the Id of the AWS WAF web ACL that is associated with the distribution.
            
            ETag (string) -- The current version of the distribution's information. For example: E2QWRUHAPOMQZL.
            
            
        :type Id: string
        """
        self.client.get_distribution(Id=Id)

    def get_distribution_config(self, Id=None):
        """
        :param Id: [REQUIRED] The distribution's id.
            Return typedict
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
                        }
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
                  'Compress': True|False
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
                      'Compress': True|False
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
                  'MinimumProtocolVersion': 'SSLv3'|'TLSv1',
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
                'WebACLId': 'string'
              },
              'ETag': 'string'
            }
            Response Structure
            (dict) -- The returned result of the corresponding request.
            DistributionConfig (dict) -- The distribution's configuration information.
            CallerReference (string) -- A unique number that ensures the request can't be replayed. If the CallerReference is new (no matter the content of the DistributionConfig object), a new distribution is created. If the CallerReference is a value you already sent in a previous request to create a distribution, and the content of the DistributionConfig is identical to the original request (ignoring white space), the response includes the same information returned to the original request. If the CallerReference is a value you already sent in a previous request to create a distribution but the content of the DistributionConfig is different from the original request, CloudFront returns a DistributionAlreadyExists error.
            Aliases (dict) -- A complex type that contains information about CNAMEs (alternate domain names), if any, for this distribution.
            Quantity (integer) -- The number of CNAMEs, if any, for this distribution.
            Items (list) -- Optional: A complex type that contains CNAME elements, if any, for this distribution. If Quantity is 0, you can omit Items.
            (string) --
            
            DefaultRootObject (string) -- The object that you want CloudFront to return (for example, index.html) when an end user requests the root URL for your distribution (http://www.example.com) instead of an object in your distribution (http://www.example.com/index.html). Specifying a default root object avoids exposing the contents of your distribution. If you don't want to specify a default root object when you create a distribution, include an empty DefaultRootObject element. To delete the default root object from an existing distribution, update the distribution configuration and include an empty DefaultRootObject element. To replace the default root object, update the distribution configuration and specify the new object.
            Origins (dict) -- A complex type that contains information about origins for this distribution.
            Quantity (integer) -- The number of origins for this distribution.
            Items (list) -- A complex type that contains origins for this distribution.
            (dict) -- A complex type that describes the Amazon S3 bucket or the HTTP server (for example, a web server) from which CloudFront gets your files.You must create at least one origin.
            Id (string) -- A unique identifier for the origin. The value of Id must be unique within the distribution. You use the value of Id when you create a cache behavior. The Id identifies the origin that CloudFront routes a request to when the request matches the path pattern for that cache behavior.
            DomainName (string) -- Amazon S3 origins: The DNS name of the Amazon S3 bucket from which you want CloudFront to get objects for this origin, for example, myawsbucket.s3.amazonaws.com. Custom origins: The DNS domain name for the HTTP server from which you want CloudFront to get objects for this origin, for example, www.example.com.
            OriginPath (string) -- An optional element that causes CloudFront to request your content from a directory in your Amazon S3 bucket or your custom origin. When you include the OriginPath element, specify the directory name, beginning with a /. CloudFront appends the directory name to the value of DomainName.
            CustomHeaders (dict) -- A complex type that contains information about the custom headers associated with this Origin.
            Quantity (integer) -- The number of custom headers for this origin.
            Items (list) -- A complex type that contains the custom headers for this Origin.
            (dict) -- A complex type that contains information related to a Header
            HeaderName (string) -- The header's name.
            HeaderValue (string) -- The header's value.
            
            S3OriginConfig (dict) -- A complex type that contains information about the Amazon S3 origin. If the origin is a custom origin, use the CustomOriginConfig element instead.
            OriginAccessIdentity (string) -- The CloudFront origin access identity to associate with the origin. Use an origin access identity to configure the origin so that end users can only access objects in an Amazon S3 bucket through CloudFront. If you want end users to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty OriginAccessIdentity element. To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty OriginAccessIdentity element. To replace the origin access identity, update the distribution configuration and specify the new origin access identity. Use the format origin-access-identity/cloudfront/Id where Id is the value that CloudFront returned in the Id element when you created the origin access identity.
            CustomOriginConfig (dict) -- A complex type that contains information about a custom origin. If the origin is an Amazon S3 bucket, use the S3OriginConfig element instead.
            HTTPPort (integer) -- The HTTP port the custom origin listens on.
            HTTPSPort (integer) -- The HTTPS port the custom origin listens on.
            OriginProtocolPolicy (string) -- The origin protocol policy to apply to your origin.
            OriginSslProtocols (dict) -- The SSL/TLS protocols that you want CloudFront to use when communicating with your origin over HTTPS.
            Quantity (integer) -- The number of SSL/TLS protocols that you want to allow CloudFront to use when establishing an HTTPS connection with this origin.
            Items (list) -- A complex type that contains one SslProtocol element for each SSL/TLS protocol that you want to allow CloudFront to use when establishing an HTTPS connection with this origin.
            (string) --
            
            
            
            DefaultCacheBehavior (dict) -- A complex type that describes the default cache behavior if you do not specify a CacheBehavior element or if files don't match any of the values of PathPattern in CacheBehavior elements.You must create exactly one default cache behavior.
            TargetOriginId (string) -- The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior.
            ForwardedValues (dict) -- A complex type that specifies how CloudFront handles query strings, cookies and headers.
            QueryString (boolean) -- Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior. If so, specify true; if not, specify false.
            Cookies (dict) -- A complex type that specifies how CloudFront handles cookies.
            Forward (string) -- Use this element to specify whether you want CloudFront to forward cookies to the origin that is associated with this cache behavior. You can specify all, none or whitelist. If you choose All, CloudFront forwards all cookies regardless of how many your application uses.
            WhitelistedNames (dict) -- A complex type that specifies the whitelisted cookies, if any, that you want CloudFront to forward to your origin that is associated with this cache behavior.
            Quantity (integer) -- The number of whitelisted cookies for this cache behavior.
            Items (list) -- Optional: A complex type that contains whitelisted cookies for this cache behavior. If Quantity is 0, you can omit Items.
            (string) --
            
            Headers (dict) -- A complex type that specifies the Headers, if any, that you want CloudFront to vary upon for this cache behavior.
            Quantity (integer) -- The number of different headers that you want CloudFront to forward to the origin and to vary on for this cache behavior. The maximum number of headers that you can specify by name is 10. If you want CloudFront to forward all headers to the origin and vary on all of them, specify 1 for Quantity and * for Name. If you don't want CloudFront to forward any additional headers to the origin or to vary on any headers, specify 0 for Quantity and omit Items.
            Items (list) -- Optional: A complex type that contains a Name element for each header that you want CloudFront to forward to the origin and to vary on for this cache behavior. If Quantity is 0, omit Items.
            (string) --
            
            TrustedSigners (dict) -- A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content. If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled, and specify the applicable values for Quantity and Items. For more information, go to Using a Signed URL to Serve Private Content in the Amazon CloudFront Developer Guide. If you don't want to require signed URLs in requests for objects that match PathPattern, specify false for Enabled and 0 for Quantity. Omit Items. To add, change, or remove one or more trusted signers, change Enabled to true (if it's currently false), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.
            Enabled (boolean) -- Specifies whether you want to require end users to use signed URLs to access the files specified by PathPattern and TargetOriginId.
            Quantity (integer) -- The number of trusted signers for this cache behavior.
            Items (list) -- Optional: A complex type that contains trusted signers for this cache behavior. If Quantity is 0, you can omit Items.
            (string) --
            
            ViewerProtocolPolicy (string) -- Use this element to specify the protocol that users can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern. If you want CloudFront to allow end users to use any available protocol, specify allow-all. If you want CloudFront to require HTTPS, specify https. If you want CloudFront to respond to an HTTP request with an HTTP status code of 301 (Moved Permanently) and the HTTPS URL, specify redirect-to-https. The viewer then resubmits the request using the HTTPS URL.
            MinTTL (integer) -- The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront queries your origin to see whether the object has been updated.You can specify a value from 0 to 3,153,600,000 seconds (100 years).
            AllowedMethods (dict) -- A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices: - CloudFront forwards only GET and HEAD requests. - CloudFront forwards only GET, HEAD and OPTIONS requests. - CloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST, and DELETE requests. If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can't perform operations that you don't want them to. For example, you may not want users to have permission to delete objects from your origin.
            Quantity (integer) -- The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET, HEAD and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST, and DELETE requests).
            Items (list) -- A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.
            (string) --
            CachedMethods (dict) -- A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices: - CloudFront caches responses to GET and HEAD requests. - CloudFront caches responses to GET, HEAD, and OPTIONS requests. If you pick the second choice for your S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers and Origin headers for the responses to be cached correctly.
            Quantity (integer) -- The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET, HEAD, and OPTIONS requests).
            Items (list) -- A complex type that contains the HTTP methods that you want CloudFront to cache responses to.
            (string) --
            
            SmoothStreaming (boolean) -- Indicates whether you want to distribute media files in Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true; if not, specify false.
            DefaultTTL (integer) -- If you don't configure your origin to add a Cache-Control max-age directive or an Expires header, DefaultTTL is the default amount of time (in seconds) that an object is in a CloudFront cache before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age, Cache-Control s-maxage, and Expires to objects. You can specify a value from 0 to 3,153,600,000 seconds (100 years).
            MaxTTL (integer) -- The maximum amount of time (in seconds) that an object is in a CloudFront cache before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as Cache-Control max-age, Cache-Control s-maxage, and Expires to objects. You can specify a value from 0 to 3,153,600,000 seconds (100 years).
            Compress (boolean) -- Whether you want CloudFront to automatically compress content for web requests that include Accept-Encoding: gzip in the request header. If so, specify true; if not, specify false. CloudFront compresses files larger than 1000 bytes and less than 1 megabyte for both Amazon S3 and custom origins. When a CloudFront edge location is unusually busy, some files might not be compressed. The value of the Content-Type header must be on the list of file types that CloudFront will compress. For the current list, see Serving Compressed Content in the Amazon CloudFront Developer Guide. If you configure CloudFront to compress content, CloudFront removes the ETag response header from the objects that it compresses. The ETag header indicates that the version in a CloudFront edge cache is identical to the version on the origin server, but after compression the two versions are no longer identical. As a result, for compressed objects, CloudFront can't use the ETag header to determine whether an expired object in the CloudFront edge cache is still the latest version.
            CacheBehaviors (dict) -- A complex type that contains zero or more CacheBehavior elements.
            Quantity (integer) -- The number of cache behaviors for this distribution.
            Items (list) -- Optional: A complex type that contains cache behaviors for this distribution. If Quantity is 0, you can omit Items.
            (dict) -- A complex type that describes how CloudFront processes requests. You can create up to 10 cache behaviors.You must create at least as many cache behaviors (including the default cache behavior) as you have origins if you want CloudFront to distribute objects from all of the origins. Each cache behavior specifies the one origin from which you want CloudFront to get objects. If you have two origins and only the default cache behavior, the default cache behavior will cause CloudFront to get objects from one of the origins, but the other origin will never be used. If you don't want to specify any cache behaviors, include only an empty CacheBehaviors element. Don't include an empty CacheBehavior element, or CloudFront returns a MalformedXML error. To delete all cache behaviors in an existing distribution, update the distribution configuration and include only an empty CacheBehaviors element. To add, change, or remove one or more cache behaviors, update the distribution configuration and specify all of the cache behaviors that you want to include in the updated distribution.
            PathPattern (string) -- The pattern (for example, images/*.jpg) that specifies which requests you want this cache behavior to apply to. When CloudFront receives an end-user request, the requested path is compared with path patterns in the order in which cache behaviors are listed in the distribution. The path pattern for the default cache behavior is * and cannot be changed. If the request for an object does not match the path pattern for any cache behaviors, CloudFront applies the behavior in the default cache behavior.
            TargetOriginId (string) -- The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior.
            ForwardedValues (dict) -- A complex type that specifies how CloudFront handles query strings, cookies and headers.
            QueryString (boolean) -- Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior. If so, specify true; if not, specify false.
            Cookies (dict) -- A complex type that specifies how CloudFront handles cookies.
            Forward (string) -- Use this element to specify whether you want CloudFront to forward cookies to the origin that is associated with this cache behavior. You can specify all, none or whitelist. If you choose All, CloudFront forwards all cookies regardless of how many your application uses.
            WhitelistedNames (dict) -- A complex type that specifies the whitelisted cookies, if any, that you want CloudFront to forward to your origin that is associated with this cache behavior.
            Quantity (integer) -- The number of whitelisted cookies for this cache behavior.
            Items (list) -- Optional: A complex type that contains whitelisted cookies for this cache behavior. If Quantity is 0, you can omit Items.
            (string) --
            
            Headers (dict) -- A complex type that specifies the Headers, if any, that you want CloudFront to vary upon for this cache behavior.
            Quantity (integer) -- The number of different headers that you want CloudFront to forward to the origin and to vary on for this cache behavior. The maximum number of headers that you can specify by name is 10. If you want CloudFront to forward all headers to the origin and vary on all of them, specify 1 for Quantity and * for Name. If you don't want CloudFront to forward any additional headers to the origin or to vary on any headers, specify 0 for Quantity and omit Items.
            Items (list) -- Optional: A complex type that contains a Name element for each header that you want CloudFront to forward to the origin and to vary on for this cache behavior. If Quantity is 0, omit Items.
            (string) --
            
            TrustedSigners (dict) -- A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content. If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled, and specify the applicable values for Quantity and Items. For more information, go to Using a Signed URL to Serve Private Content in the Amazon CloudFront Developer Guide. If you don't want to require signed URLs in requests for objects that match PathPattern, specify false for Enabled and 0 for Quantity. Omit Items. To add, change, or remove one or more trusted signers, change Enabled to true (if it's currently false), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.
            Enabled (boolean) -- Specifies whether you want to require end users to use signed URLs to access the files specified by PathPattern and TargetOriginId.
            Quantity (integer) -- The number of trusted signers for this cache behavior.
            Items (list) -- Optional: A complex type that contains trusted signers for this cache behavior. If Quantity is 0, you can omit Items.
            (string) --
            
            ViewerProtocolPolicy (string) -- Use this element to specify the protocol that users can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern. If you want CloudFront to allow end users to use any available protocol, specify allow-all. If you want CloudFront to require HTTPS, specify https. If you want CloudFront to respond to an HTTP request with an HTTP status code of 301 (Moved Permanently) and the HTTPS URL, specify redirect-to-https. The viewer then resubmits the request using the HTTPS URL.
            MinTTL (integer) -- The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront queries your origin to see whether the object has been updated.You can specify a value from 0 to 3,153,600,000 seconds (100 years).
            AllowedMethods (dict) -- A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices: - CloudFront forwards only GET and HEAD requests. - CloudFront forwards only GET, HEAD and OPTIONS requests. - CloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST, and DELETE requests. If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can't perform operations that you don't want them to. For example, you may not want users to have permission to delete objects from your origin.
            Quantity (integer) -- The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET, HEAD and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST, and DELETE requests).
            Items (list) -- A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.
            (string) --
            CachedMethods (dict) -- A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices: - CloudFront caches responses to GET and HEAD requests. - CloudFront caches responses to GET, HEAD, and OPTIONS requests. If you pick the second choice for your S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers and Origin headers for the responses to be cached correctly.
            Quantity (integer) -- The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET, HEAD, and OPTIONS requests).
            Items (list) -- A complex type that contains the HTTP methods that you want CloudFront to cache responses to.
            (string) --
            
            SmoothStreaming (boolean) -- Indicates whether you want to distribute media files in Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true; if not, specify false.
            DefaultTTL (integer) -- If you don't configure your origin to add a Cache-Control max-age directive or an Expires header, DefaultTTL is the default amount of time (in seconds) that an object is in a CloudFront cache before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age, Cache-Control s-maxage, and Expires to objects. You can specify a value from 0 to 3,153,600,000 seconds (100 years).
            MaxTTL (integer) -- The maximum amount of time (in seconds) that an object is in a CloudFront cache before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as Cache-Control max-age, Cache-Control s-maxage, and Expires to objects. You can specify a value from 0 to 3,153,600,000 seconds (100 years).
            Compress (boolean) -- Whether you want CloudFront to automatically compress content for web requests that include Accept-Encoding: gzip in the request header. If so, specify true; if not, specify false. CloudFront compresses files larger than 1000 bytes and less than 1 megabyte for both Amazon S3 and custom origins. When a CloudFront edge location is unusually busy, some files might not be compressed. The value of the Content-Type header must be on the list of file types that CloudFront will compress. For the current list, see Serving Compressed Content in the Amazon CloudFront Developer Guide. If you configure CloudFront to compress content, CloudFront removes the ETag response header from the objects that it compresses. The ETag header indicates that the version in a CloudFront edge cache is identical to the version on the origin server, but after compression the two versions are no longer identical. As a result, for compressed objects, CloudFront can't use the ETag header to determine whether an expired object in the CloudFront edge cache is still the latest version.
            
            CustomErrorResponses (dict) -- A complex type that contains zero or more CustomErrorResponse elements.
            Quantity (integer) -- The number of custom error responses for this distribution.
            Items (list) -- Optional: A complex type that contains custom error responses for this distribution. If Quantity is 0, you can omit Items.
            (dict) -- A complex type that describes how you'd prefer CloudFront to respond to requests that result in either a 4xx or 5xx response. You can control whether a custom error page should be displayed, what the desired response code should be for this error page and how long should the error response be cached by CloudFront. If you don't want to specify any custom error responses, include only an empty CustomErrorResponses element. To delete all custom error responses in an existing distribution, update the distribution configuration and include only an empty CustomErrorResponses element. To add, change, or remove one or more custom error responses, update the distribution configuration and specify all of the custom error responses that you want to include in the updated distribution.
            ErrorCode (integer) -- The 4xx or 5xx HTTP status code that you want to customize. For a list of HTTP status codes that you can customize, see CloudFront documentation.
            ResponsePagePath (string) -- The path of the custom error page (for example, /custom_404.html). The path is relative to the distribution and must begin with a slash (/). If the path includes any non-ASCII characters or unsafe characters as defined in RFC 1783 (http://www.ietf.org/rfc/rfc1738.txt), URL encode those characters. Do not URL encode any other characters in the path, or CloudFront will not return the custom error page to the viewer.
            ResponseCode (string) -- The HTTP status code that you want CloudFront to return with the custom error page to the viewer. For a list of HTTP status codes that you can replace, see CloudFront Documentation.
            ErrorCachingMinTTL (integer) -- The minimum amount of time you want HTTP error codes to stay in CloudFront caches before CloudFront queries your origin to see whether the object has been updated. You can specify a value from 0 to 31,536,000.
            
            Comment (string) -- Any comments you want to include about the distribution.
            Logging (dict) -- A complex type that controls whether access logs are written for the distribution.
            Enabled (boolean) -- Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you do not want to enable logging when you create a distribution or if you want to disable logging for an existing distribution, specify false for Enabled, and specify empty Bucket and Prefix elements. If you specify false for Enabled but you specify values for Bucket, prefix and IncludeCookies, the values are automatically deleted.
            IncludeCookies (boolean) -- Specifies whether you want CloudFront to include cookies in access logs, specify true for IncludeCookies. If you choose to include cookies in logs, CloudFront logs all cookies regardless of how you configure the cache behaviors for this distribution. If you do not want to include cookies when you create a distribution or if you want to disable include cookies for an existing distribution, specify false for IncludeCookies.
            Bucket (string) -- The Amazon S3 bucket to store the access logs in, for example, myawslogbucket.s3.amazonaws.com.
            Prefix (string) -- An optional string that you want CloudFront to prefix to the access log filenames for this distribution, for example, myprefix/. If you want to enable logging, but you do not want to specify a prefix, you still must include an empty Prefix element in the Logging element.
            PriceClass (string) -- A complex type that contains information about price class for this distribution.
            Enabled (boolean) -- Whether the distribution is enabled to accept end user requests for content.
            ViewerCertificate (dict) -- A complex type that contains information about viewer certificates for this distribution.
            CloudFrontDefaultCertificate (boolean) -- If you want viewers to use HTTPS to request your objects and you're using the CloudFront domain name of your distribution in your object URLs (for example, https://d111111abcdef8.cloudfront.net/logo.jpg), set to true. Omit this value if you are setting an ACMCertificateArn or IAMCertificateId.
            IAMCertificateId (string) -- If you want viewers to use HTTPS to request your objects and you're using an alternate domain name in your object URLs (for example, https://example.com/logo.jpg), specify the IAM certificate identifier of the custom viewer certificate for this distribution. Specify either this value, ACMCertificateArn, or CloudFrontDefaultCertificate.
            ACMCertificateArn (string) -- If you want viewers to use HTTPS to request your objects and you're using an alternate domain name in your object URLs (for example, https://example.com/logo.jpg), specify the ACM certificate ARN of the custom viewer certificate for this distribution. Specify either this value, IAMCertificateId, or CloudFrontDefaultCertificate.
            SSLSupportMethod (string) -- If you specify a value for IAMCertificateId, you must also specify how you want CloudFront to serve HTTPS requests. Valid values are vip and sni-only. If you specify vip, CloudFront uses dedicated IP addresses for your content and can respond to HTTPS requests from any viewer. However, you must request permission to use this feature, and you incur additional monthly charges. If you specify sni-only, CloudFront can only respond to HTTPS requests from viewers that support Server Name Indication (SNI). All modern browsers support SNI, but some browsers still in use don't support SNI. Do not specify a value for SSLSupportMethod if you specified true for CloudFrontDefaultCertificate.
            MinimumProtocolVersion (string) -- Specify the minimum version of the SSL protocol that you want CloudFront to use, SSLv3 or TLSv1, for HTTPS connections. CloudFront will serve your objects only to browsers or devices that support at least the SSL version that you specify. The TLSv1 protocol is more secure, so we recommend that you specify SSLv3 only if your users are using browsers or devices that don't support TLSv1. If you're using a custom certificate (if you specify a value for IAMCertificateId) and if you're using dedicated IP (if you specify vip for SSLSupportMethod), you can choose SSLv3 or TLSv1 as the MinimumProtocolVersion. If you're using a custom certificate (if you specify a value for IAMCertificateId) and if you're using SNI (if you specify sni-only for SSLSupportMethod), you must specify TLSv1 for MinimumProtocolVersion.
            Certificate (string) -- Note: this field is deprecated. Please use one of [ACMCertificateArn, IAMCertificateId, CloudFrontDefaultCertificate].
            CertificateSource (string) -- Note: this field is deprecated. Please use one of [ACMCertificateArn, IAMCertificateId, CloudFrontDefaultCertificate].
            Restrictions (dict) -- A complex type that identifies ways in which you want to restrict distribution of your content.
            GeoRestriction (dict) -- A complex type that controls the countries in which your content is distributed. For more information about geo restriction, go to Customizing Error Responses in the Amazon CloudFront Developer Guide. CloudFront determines the location of your users using MaxMind GeoIP databases. For information about the accuracy of these databases, see How accurate are your GeoIP databases? on the MaxMind website.
            RestrictionType (string) -- The method that you want to use to restrict distribution of your content by country: - none: No geo restriction is enabled, meaning access to content is not restricted by client geo location. - blacklist: The Location elements specify the countries in which you do not want CloudFront to distribute your content. - whitelist: The Location elements specify the countries in which you want CloudFront to distribute your content.
            Quantity (integer) -- When geo restriction is enabled, this is the number of countries in your whitelist or blacklist. Otherwise, when it is not enabled, Quantity is 0, and you can omit Items.
            Items (list) -- A complex type that contains a Location element for each country in which you want CloudFront either to distribute your content (whitelist) or not distribute your content (blacklist). The Location element is a two-letter, uppercase country code for a country that you want to include in your blacklist or whitelist. Include one Location element for each country. CloudFront and MaxMind both use ISO 3166 country codes. For the current list of countries and the corresponding codes, see ISO 3166-1-alpha-2 code on the International Organization for Standardization website. You can also refer to the country list in the CloudFront console, which includes both country names and codes.
            (string) --
            
            WebACLId (string) -- (Optional) If you're using AWS WAF to filter CloudFront requests, the Id of the AWS WAF web ACL that is associated with the distribution.
            ETag (string) -- The current version of the configuration. For example: E2QWRUHAPOMQZL.
            
            
        :type Id: string
        """
        self.client.get_distribution_config(Id=Id)

    def get_invalidation(self, DistributionId=None, Id=None):
        """
        :param DistributionId: [REQUIRED] The distribution's id.
        :type DistributionId: string
        :param Id: [REQUIRED] The invalidation's id.
        :type Id: string
        """
        self.client.get_invalidation(DistributionId=DistributionId, Id=Id)

    def get_paginator(self, operation_name=None):
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
        self.client.get_paginator(operation_name=operation_name)

    def get_streaming_distribution(self, Id=None):
        """
        :param Id: [REQUIRED] The streaming distribution's id.
            Return typedict
            ReturnsResponse Syntax{
              'StreamingDistribution': {
                'Id': 'string',
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
            (dict) -- The returned result of the corresponding request.
            StreamingDistribution (dict) -- The streaming distribution's information.
            Id (string) -- The identifier for the streaming distribution. For example: EGTXBD79H29TRA8.
            Status (string) -- The current status of the streaming distribution. When the status is Deployed, the distribution's information is fully propagated throughout the Amazon CloudFront system.
            LastModifiedTime (datetime) -- The date and time the distribution was last modified.
            DomainName (string) -- The domain name corresponding to the streaming distribution. For example: s5c39gqb8ow64r.cloudfront.net.
            ActiveTrustedSigners (dict) -- CloudFront automatically adds this element to the response only if you've set up the distribution to serve private content with signed URLs. The element lists the key pair IDs that CloudFront is aware of for each trusted signer. The Signer child element lists the AWS account number of the trusted signer (or an empty Self element if the signer is you). The Signer element also includes the IDs of any active key pairs associated with the trusted signer's AWS account. If no KeyPairId element appears for a Signer, that signer can't create working signed URLs.
            Enabled (boolean) -- Each active trusted signer.
            Quantity (integer) -- The number of unique trusted signers included in all cache behaviors. For example, if three cache behaviors all list the same three AWS accounts, the value of Quantity for ActiveTrustedSigners will be 3.
            Items (list) -- A complex type that contains one Signer complex type for each unique trusted signer that is specified in the TrustedSigners complex type, including trusted signers in the default cache behavior and in all of the other cache behaviors.
            (dict) -- A complex type that lists the AWS accounts that were included in the TrustedSigners complex type, as well as their active CloudFront key pair IDs, if any.
            AwsAccountNumber (string) -- Specifies an AWS account that can create signed URLs. Values: self, which indicates that the AWS account that was used to create the distribution can created signed URLs, or an AWS account number. Omit the dashes in the account number.
            KeyPairIds (dict) -- A complex type that lists the active CloudFront key pairs, if any, that are associated with AwsAccountNumber.
            Quantity (integer) -- The number of active CloudFront key pairs for AwsAccountNumber.
            Items (list) -- A complex type that lists the active CloudFront key pairs, if any, that are associated with AwsAccountNumber.
            (string) --
            
            
            StreamingDistributionConfig (dict) -- The current configuration information for the streaming distribution.
            CallerReference (string) -- A unique number that ensures the request can't be replayed. If the CallerReference is new (no matter the content of the StreamingDistributionConfig object), a new streaming distribution is created. If the CallerReference is a value you already sent in a previous request to create a streaming distribution, and the content of the StreamingDistributionConfig is identical to the original request (ignoring white space), the response includes the same information returned to the original request. If the CallerReference is a value you already sent in a previous request to create a streaming distribution but the content of the StreamingDistributionConfig is different from the original request, CloudFront returns a DistributionAlreadyExists error.
            S3Origin (dict) -- A complex type that contains information about the Amazon S3 bucket from which you want CloudFront to get your media files for distribution.
            DomainName (string) -- The DNS name of the S3 origin.
            OriginAccessIdentity (string) -- Your S3 origin's origin access identity.
            Aliases (dict) -- A complex type that contains information about CNAMEs (alternate domain names), if any, for this streaming distribution.
            Quantity (integer) -- The number of CNAMEs, if any, for this distribution.
            Items (list) -- Optional: A complex type that contains CNAME elements, if any, for this distribution. If Quantity is 0, you can omit Items.
            (string) --
            
            Comment (string) -- Any comments you want to include about the streaming distribution.
            Logging (dict) -- A complex type that controls whether access logs are written for the streaming distribution.
            Enabled (boolean) -- Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you do not want to enable logging when you create a streaming distribution or if you want to disable logging for an existing streaming distribution, specify false for Enabled, and specify empty Bucket and Prefix elements. If you specify false for Enabled but you specify values for Bucket and Prefix, the values are automatically deleted.
            Bucket (string) -- The Amazon S3 bucket to store the access logs in, for example, myawslogbucket.s3.amazonaws.com.
            Prefix (string) -- An optional string that you want CloudFront to prefix to the access log filenames for this streaming distribution, for example, myprefix/. If you want to enable logging, but you do not want to specify a prefix, you still must include an empty Prefix element in the Logging element.
            TrustedSigners (dict) -- A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content. If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled, and specify the applicable values for Quantity and Items. For more information, go to Using a Signed URL to Serve Private Content in the Amazon CloudFront Developer Guide. If you don't want to require signed URLs in requests for objects that match PathPattern, specify false for Enabled and 0 for Quantity. Omit Items. To add, change, or remove one or more trusted signers, change Enabled to true (if it's currently false), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.
            Enabled (boolean) -- Specifies whether you want to require end users to use signed URLs to access the files specified by PathPattern and TargetOriginId.
            Quantity (integer) -- The number of trusted signers for this cache behavior.
            Items (list) -- Optional: A complex type that contains trusted signers for this cache behavior. If Quantity is 0, you can omit Items.
            (string) --
            
            PriceClass (string) -- A complex type that contains information about price class for this streaming distribution.
            Enabled (boolean) -- Whether the streaming distribution is enabled to accept end user requests for content.
            
            ETag (string) -- The current version of the streaming distribution's information. For example: E2QWRUHAPOMQZL.
            
            
        :type Id: string
        """
        self.client.get_streaming_distribution(Id=Id)

    def get_streaming_distribution_config(self, Id=None):
        """
        :param Id: [REQUIRED] The streaming distribution's id.
            Return typedict
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
            (dict) -- The returned result of the corresponding request.
            StreamingDistributionConfig (dict) -- The streaming distribution's configuration information.
            CallerReference (string) -- A unique number that ensures the request can't be replayed. If the CallerReference is new (no matter the content of the StreamingDistributionConfig object), a new streaming distribution is created. If the CallerReference is a value you already sent in a previous request to create a streaming distribution, and the content of the StreamingDistributionConfig is identical to the original request (ignoring white space), the response includes the same information returned to the original request. If the CallerReference is a value you already sent in a previous request to create a streaming distribution but the content of the StreamingDistributionConfig is different from the original request, CloudFront returns a DistributionAlreadyExists error.
            S3Origin (dict) -- A complex type that contains information about the Amazon S3 bucket from which you want CloudFront to get your media files for distribution.
            DomainName (string) -- The DNS name of the S3 origin.
            OriginAccessIdentity (string) -- Your S3 origin's origin access identity.
            Aliases (dict) -- A complex type that contains information about CNAMEs (alternate domain names), if any, for this streaming distribution.
            Quantity (integer) -- The number of CNAMEs, if any, for this distribution.
            Items (list) -- Optional: A complex type that contains CNAME elements, if any, for this distribution. If Quantity is 0, you can omit Items.
            (string) --
            
            Comment (string) -- Any comments you want to include about the streaming distribution.
            Logging (dict) -- A complex type that controls whether access logs are written for the streaming distribution.
            Enabled (boolean) -- Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you do not want to enable logging when you create a streaming distribution or if you want to disable logging for an existing streaming distribution, specify false for Enabled, and specify empty Bucket and Prefix elements. If you specify false for Enabled but you specify values for Bucket and Prefix, the values are automatically deleted.
            Bucket (string) -- The Amazon S3 bucket to store the access logs in, for example, myawslogbucket.s3.amazonaws.com.
            Prefix (string) -- An optional string that you want CloudFront to prefix to the access log filenames for this streaming distribution, for example, myprefix/. If you want to enable logging, but you do not want to specify a prefix, you still must include an empty Prefix element in the Logging element.
            TrustedSigners (dict) -- A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content. If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled, and specify the applicable values for Quantity and Items. For more information, go to Using a Signed URL to Serve Private Content in the Amazon CloudFront Developer Guide. If you don't want to require signed URLs in requests for objects that match PathPattern, specify false for Enabled and 0 for Quantity. Omit Items. To add, change, or remove one or more trusted signers, change Enabled to true (if it's currently false), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.
            Enabled (boolean) -- Specifies whether you want to require end users to use signed URLs to access the files specified by PathPattern and TargetOriginId.
            Quantity (integer) -- The number of trusted signers for this cache behavior.
            Items (list) -- Optional: A complex type that contains trusted signers for this cache behavior. If Quantity is 0, you can omit Items.
            (string) --
            
            PriceClass (string) -- A complex type that contains information about price class for this streaming distribution.
            Enabled (boolean) -- Whether the streaming distribution is enabled to accept end user requests for content.
            ETag (string) -- The current version of the configuration. For example: E2QWRUHAPOMQZL.
            
            
        :type Id: string
        """
        self.client.get_streaming_distribution_config(Id=Id)

    def get_waiter(self):
        """
        """
        self.client.get_waiter()

    def list_cloud_front_origin_access_identities(self, Marker=None, MaxItems=None):
        """
        :param Marker: Use this when paginating results to indicate where to begin in your list of origin access identities. The results include identities in the list that occur after the marker. To get the next page of results, set the Marker to the value of the NextMarker from the current page's response (which is also the ID of the last identity on that page).
        :type Marker: string
        :param MaxItems: The maximum number of origin access identities you want in the response body.
        :type MaxItems: string
        """
        self.client.list_cloud_front_origin_access_identities(Marker=Marker, MaxItems=MaxItems)

    def list_distributions(self, Marker=None, MaxItems=None):
        """
        :param Marker: Use Marker and MaxItems to control pagination of results. If you have more than MaxItems distributions that satisfy the request, the response includes a NextMarker element. To get the next page of results, submit another request. For the value of Marker, specify the value of NextMarker from the last response. (For the first request, omit Marker.)
        :type Marker: string
        :param MaxItems: The maximum number of distributions that you want CloudFront to return in the response body. The maximum and default values are both 100.
        :type MaxItems: string
        """
        self.client.list_distributions(Marker=Marker, MaxItems=MaxItems)

    def list_distributions_by_web_acl_id(self, Marker=None, MaxItems=None, WebACLId=None):
        """
        :param Marker: Use Marker and MaxItems to control pagination of results. If you have more than MaxItems distributions that satisfy the request, the response includes a NextMarker element. To get the next page of results, submit another request. For the value of Marker, specify the value of NextMarker from the last response. (For the first request, omit Marker.)
        :type Marker: string
        :param MaxItems: The maximum number of distributions that you want CloudFront to return in the response body. The maximum and default values are both 100.
        :type MaxItems: string
        :param WebACLId: [REQUIRED] The Id of the AWS WAF web ACL for which you want to list the associated distributions. If you specify 'null' for the Id, the request returns a list of the distributions that aren't associated with a web ACL.
        :type WebACLId: string
        """
        self.client.list_distributions_by_web_acl_id(Marker=Marker, MaxItems=MaxItems, WebACLId=WebACLId)

    def list_invalidations(self, DistributionId=None, Marker=None, MaxItems=None):
        """
        :param DistributionId: [REQUIRED] The distribution's id.
        :type DistributionId: string
        :param Marker: Use this parameter when paginating results to indicate where to begin in your list of invalidation batches. Because the results are returned in decreasing order from most recent to oldest, the most recent results are on the first page, the second page will contain earlier results, and so on. To get the next page of results, set the Marker to the value of the NextMarker from the current page's response. This value is the same as the ID of the last invalidation batch on that page.
        :type Marker: string
        :param MaxItems: The maximum number of invalidation batches you want in the response body.
        :type MaxItems: string
        """
        self.client.list_invalidations(DistributionId=DistributionId, Marker=Marker, MaxItems=MaxItems)

    def list_streaming_distributions(self, Marker=None, MaxItems=None):
        """
        :param Marker: Use this when paginating results to indicate where to begin in your list of streaming distributions. The results include distributions in the list that occur after the marker. To get the next page of results, set the Marker to the value of the NextMarker from the current page's response (which is also the ID of the last distribution on that page).
        :type Marker: string
        :param MaxItems: The maximum number of streaming distributions you want in the response body.
        :type MaxItems: string
        """
        self.client.list_streaming_distributions(Marker=Marker, MaxItems=MaxItems)

    def update_cloud_front_origin_access_identity(self, CloudFrontOriginAccessIdentityConfig=None, Id=None,
                                                  IfMatch=None):
        """
        :param CloudFrontOriginAccessIdentityConfig: [REQUIRED] The identity's configuration information.
            CallerReference (string) -- [REQUIRED] A unique number that ensures the request can't be replayed. If the CallerReference is new (no matter the content of the CloudFrontOriginAccessIdentityConfig object), a new origin access identity is created. If the CallerReference is a value you already sent in a previous request to create an identity, and the content of the CloudFrontOriginAccessIdentityConfig is identical to the original request (ignoring white space), the response includes the same information returned to the original request. If the CallerReference is a value you already sent in a previous request to create an identity but the content of the CloudFrontOriginAccessIdentityConfig is different from the original request, CloudFront returns a CloudFrontOriginAccessIdentityAlreadyExists error.
            Comment (string) -- [REQUIRED] Any comments you want to include about the origin access identity.
            
        :type CloudFrontOriginAccessIdentityConfig: dict
        :param Id: [REQUIRED] The identity's id.
        :type Id: string
        :param IfMatch: The value of the ETag header you received when retrieving the identity's configuration. For example: E2QWRUHAPOMQZL.
        :type IfMatch: string
        """
        self.client.update_cloud_front_origin_access_identity(
            CloudFrontOriginAccessIdentityConfig=CloudFrontOriginAccessIdentityConfig, Id=Id, IfMatch=IfMatch)

    def update_distribution(self, DistributionConfig=None, Id=None, IfMatch=None):
        """
        :param DistributionConfig: [REQUIRED] The distribution's configuration information.
            CallerReference (string) -- [REQUIRED] A unique number that ensures the request can't be replayed. If the CallerReference is new (no matter the content of the DistributionConfig object), a new distribution is created. If the CallerReference is a value you already sent in a previous request to create a distribution, and the content of the DistributionConfig is identical to the original request (ignoring white space), the response includes the same information returned to the original request. If the CallerReference is a value you already sent in a previous request to create a distribution but the content of the DistributionConfig is different from the original request, CloudFront returns a DistributionAlreadyExists error.
            Aliases (dict) -- A complex type that contains information about CNAMEs (alternate domain names), if any, for this distribution.
            Quantity (integer) -- [REQUIRED] The number of CNAMEs, if any, for this distribution.
            Items (list) -- Optional: A complex type that contains CNAME elements, if any, for this distribution. If Quantity is 0, you can omit Items.
            (string) --
            
            DefaultRootObject (string) -- The object that you want CloudFront to return (for example, index.html) when an end user requests the root URL for your distribution (http://www.example.com) instead of an object in your distribution (http://www.example.com/index.html). Specifying a default root object avoids exposing the contents of your distribution. If you don't want to specify a default root object when you create a distribution, include an empty DefaultRootObject element. To delete the default root object from an existing distribution, update the distribution configuration and include an empty DefaultRootObject element. To replace the default root object, update the distribution configuration and specify the new object.
            Origins (dict) -- [REQUIRED] A complex type that contains information about origins for this distribution.
            Quantity (integer) -- [REQUIRED] The number of origins for this distribution.
            Items (list) -- A complex type that contains origins for this distribution.
            (dict) -- A complex type that describes the Amazon S3 bucket or the HTTP server (for example, a web server) from which CloudFront gets your files.You must create at least one origin.
            Id (string) -- [REQUIRED] A unique identifier for the origin. The value of Id must be unique within the distribution. You use the value of Id when you create a cache behavior. The Id identifies the origin that CloudFront routes a request to when the request matches the path pattern for that cache behavior.
            DomainName (string) -- [REQUIRED] Amazon S3 origins: The DNS name of the Amazon S3 bucket from which you want CloudFront to get objects for this origin, for example, myawsbucket.s3.amazonaws.com. Custom origins: The DNS domain name for the HTTP server from which you want CloudFront to get objects for this origin, for example, www.example.com.
            OriginPath (string) -- An optional element that causes CloudFront to request your content from a directory in your Amazon S3 bucket or your custom origin. When you include the OriginPath element, specify the directory name, beginning with a /. CloudFront appends the directory name to the value of DomainName.
            CustomHeaders (dict) -- A complex type that contains information about the custom headers associated with this Origin.
            Quantity (integer) -- [REQUIRED] The number of custom headers for this origin.
            Items (list) -- A complex type that contains the custom headers for this Origin.
            (dict) -- A complex type that contains information related to a Header
            HeaderName (string) -- [REQUIRED] The header's name.
            HeaderValue (string) -- [REQUIRED] The header's value.
            
            S3OriginConfig (dict) -- A complex type that contains information about the Amazon S3 origin. If the origin is a custom origin, use the CustomOriginConfig element instead.
            OriginAccessIdentity (string) -- [REQUIRED] The CloudFront origin access identity to associate with the origin. Use an origin access identity to configure the origin so that end users can only access objects in an Amazon S3 bucket through CloudFront. If you want end users to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty OriginAccessIdentity element. To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty OriginAccessIdentity element. To replace the origin access identity, update the distribution configuration and specify the new origin access identity. Use the format origin-access-identity/cloudfront/Id where Id is the value that CloudFront returned in the Id element when you created the origin access identity.
            CustomOriginConfig (dict) -- A complex type that contains information about a custom origin. If the origin is an Amazon S3 bucket, use the S3OriginConfig element instead.
            HTTPPort (integer) -- [REQUIRED] The HTTP port the custom origin listens on.
            HTTPSPort (integer) -- [REQUIRED] The HTTPS port the custom origin listens on.
            OriginProtocolPolicy (string) -- [REQUIRED] The origin protocol policy to apply to your origin.
            OriginSslProtocols (dict) -- The SSL/TLS protocols that you want CloudFront to use when communicating with your origin over HTTPS.
            Quantity (integer) -- [REQUIRED] The number of SSL/TLS protocols that you want to allow CloudFront to use when establishing an HTTPS connection with this origin.
            Items (list) -- [REQUIRED] A complex type that contains one SslProtocol element for each SSL/TLS protocol that you want to allow CloudFront to use when establishing an HTTPS connection with this origin.
            (string) --
            
            
            
            DefaultCacheBehavior (dict) -- [REQUIRED] A complex type that describes the default cache behavior if you do not specify a CacheBehavior element or if files don't match any of the values of PathPattern in CacheBehavior elements.You must create exactly one default cache behavior.
            TargetOriginId (string) -- [REQUIRED] The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior.
            ForwardedValues (dict) -- [REQUIRED] A complex type that specifies how CloudFront handles query strings, cookies and headers.
            QueryString (boolean) -- [REQUIRED] Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior. If so, specify true; if not, specify false.
            Cookies (dict) -- [REQUIRED] A complex type that specifies how CloudFront handles cookies.
            Forward (string) -- [REQUIRED] Use this element to specify whether you want CloudFront to forward cookies to the origin that is associated with this cache behavior. You can specify all, none or whitelist. If you choose All, CloudFront forwards all cookies regardless of how many your application uses.
            WhitelistedNames (dict) -- A complex type that specifies the whitelisted cookies, if any, that you want CloudFront to forward to your origin that is associated with this cache behavior.
            Quantity (integer) -- [REQUIRED] The number of whitelisted cookies for this cache behavior.
            Items (list) -- Optional: A complex type that contains whitelisted cookies for this cache behavior. If Quantity is 0, you can omit Items.
            (string) --
            
            Headers (dict) -- A complex type that specifies the Headers, if any, that you want CloudFront to vary upon for this cache behavior.
            Quantity (integer) -- [REQUIRED] The number of different headers that you want CloudFront to forward to the origin and to vary on for this cache behavior. The maximum number of headers that you can specify by name is 10. If you want CloudFront to forward all headers to the origin and vary on all of them, specify 1 for Quantity and * for Name. If you don't want CloudFront to forward any additional headers to the origin or to vary on any headers, specify 0 for Quantity and omit Items.
            Items (list) -- Optional: A complex type that contains a Name element for each header that you want CloudFront to forward to the origin and to vary on for this cache behavior. If Quantity is 0, omit Items.
            (string) --
            
            TrustedSigners (dict) -- [REQUIRED] A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content. If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled, and specify the applicable values for Quantity and Items. For more information, go to Using a Signed URL to Serve Private Content in the Amazon CloudFront Developer Guide. If you don't want to require signed URLs in requests for objects that match PathPattern, specify false for Enabled and 0 for Quantity. Omit Items. To add, change, or remove one or more trusted signers, change Enabled to true (if it's currently false), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.
            Enabled (boolean) -- [REQUIRED] Specifies whether you want to require end users to use signed URLs to access the files specified by PathPattern and TargetOriginId.
            Quantity (integer) -- [REQUIRED] The number of trusted signers for this cache behavior.
            Items (list) -- Optional: A complex type that contains trusted signers for this cache behavior. If Quantity is 0, you can omit Items.
            (string) --
            
            ViewerProtocolPolicy (string) -- [REQUIRED] Use this element to specify the protocol that users can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern. If you want CloudFront to allow end users to use any available protocol, specify allow-all. If you want CloudFront to require HTTPS, specify https. If you want CloudFront to respond to an HTTP request with an HTTP status code of 301 (Moved Permanently) and the HTTPS URL, specify redirect-to-https. The viewer then resubmits the request using the HTTPS URL.
            MinTTL (integer) -- [REQUIRED] The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront queries your origin to see whether the object has been updated.You can specify a value from 0 to 3,153,600,000 seconds (100 years).
            AllowedMethods (dict) -- A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices: - CloudFront forwards only GET and HEAD requests. - CloudFront forwards only GET, HEAD and OPTIONS requests. - CloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST, and DELETE requests. If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can't perform operations that you don't want them to. For example, you may not want users to have permission to delete objects from your origin.
            Quantity (integer) -- [REQUIRED] The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET, HEAD and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST, and DELETE requests).
            Items (list) -- [REQUIRED] A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.
            (string) --
            CachedMethods (dict) -- A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices: - CloudFront caches responses to GET and HEAD requests. - CloudFront caches responses to GET, HEAD, and OPTIONS requests. If you pick the second choice for your S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers and Origin headers for the responses to be cached correctly.
            Quantity (integer) -- [REQUIRED] The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET, HEAD, and OPTIONS requests).
            Items (list) -- [REQUIRED] A complex type that contains the HTTP methods that you want CloudFront to cache responses to.
            (string) --
            
            SmoothStreaming (boolean) -- Indicates whether you want to distribute media files in Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true; if not, specify false.
            DefaultTTL (integer) -- If you don't configure your origin to add a Cache-Control max-age directive or an Expires header, DefaultTTL is the default amount of time (in seconds) that an object is in a CloudFront cache before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age, Cache-Control s-maxage, and Expires to objects. You can specify a value from 0 to 3,153,600,000 seconds (100 years).
            MaxTTL (integer) -- The maximum amount of time (in seconds) that an object is in a CloudFront cache before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as Cache-Control max-age, Cache-Control s-maxage, and Expires to objects. You can specify a value from 0 to 3,153,600,000 seconds (100 years).
            Compress (boolean) -- Whether you want CloudFront to automatically compress content for web requests that include Accept-Encoding: gzip in the request header. If so, specify true; if not, specify false. CloudFront compresses files larger than 1000 bytes and less than 1 megabyte for both Amazon S3 and custom origins. When a CloudFront edge location is unusually busy, some files might not be compressed. The value of the Content-Type header must be on the list of file types that CloudFront will compress. For the current list, see Serving Compressed Content in the Amazon CloudFront Developer Guide. If you configure CloudFront to compress content, CloudFront removes the ETag response header from the objects that it compresses. The ETag header indicates that the version in a CloudFront edge cache is identical to the version on the origin server, but after compression the two versions are no longer identical. As a result, for compressed objects, CloudFront can't use the ETag header to determine whether an expired object in the CloudFront edge cache is still the latest version.
            CacheBehaviors (dict) -- A complex type that contains zero or more CacheBehavior elements.
            Quantity (integer) -- [REQUIRED] The number of cache behaviors for this distribution.
            Items (list) -- Optional: A complex type that contains cache behaviors for this distribution. If Quantity is 0, you can omit Items.
            (dict) -- A complex type that describes how CloudFront processes requests. You can create up to 10 cache behaviors.You must create at least as many cache behaviors (including the default cache behavior) as you have origins if you want CloudFront to distribute objects from all of the origins. Each cache behavior specifies the one origin from which you want CloudFront to get objects. If you have two origins and only the default cache behavior, the default cache behavior will cause CloudFront to get objects from one of the origins, but the other origin will never be used. If you don't want to specify any cache behaviors, include only an empty CacheBehaviors element. Don't include an empty CacheBehavior element, or CloudFront returns a MalformedXML error. To delete all cache behaviors in an existing distribution, update the distribution configuration and include only an empty CacheBehaviors element. To add, change, or remove one or more cache behaviors, update the distribution configuration and specify all of the cache behaviors that you want to include in the updated distribution.
            PathPattern (string) -- [REQUIRED] The pattern (for example, images/*.jpg) that specifies which requests you want this cache behavior to apply to. When CloudFront receives an end-user request, the requested path is compared with path patterns in the order in which cache behaviors are listed in the distribution. The path pattern for the default cache behavior is * and cannot be changed. If the request for an object does not match the path pattern for any cache behaviors, CloudFront applies the behavior in the default cache behavior.
            TargetOriginId (string) -- [REQUIRED] The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior.
            ForwardedValues (dict) -- [REQUIRED] A complex type that specifies how CloudFront handles query strings, cookies and headers.
            QueryString (boolean) -- [REQUIRED] Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior. If so, specify true; if not, specify false.
            Cookies (dict) -- [REQUIRED] A complex type that specifies how CloudFront handles cookies.
            Forward (string) -- [REQUIRED] Use this element to specify whether you want CloudFront to forward cookies to the origin that is associated with this cache behavior. You can specify all, none or whitelist. If you choose All, CloudFront forwards all cookies regardless of how many your application uses.
            WhitelistedNames (dict) -- A complex type that specifies the whitelisted cookies, if any, that you want CloudFront to forward to your origin that is associated with this cache behavior.
            Quantity (integer) -- [REQUIRED] The number of whitelisted cookies for this cache behavior.
            Items (list) -- Optional: A complex type that contains whitelisted cookies for this cache behavior. If Quantity is 0, you can omit Items.
            (string) --
            
            Headers (dict) -- A complex type that specifies the Headers, if any, that you want CloudFront to vary upon for this cache behavior.
            Quantity (integer) -- [REQUIRED] The number of different headers that you want CloudFront to forward to the origin and to vary on for this cache behavior. The maximum number of headers that you can specify by name is 10. If you want CloudFront to forward all headers to the origin and vary on all of them, specify 1 for Quantity and * for Name. If you don't want CloudFront to forward any additional headers to the origin or to vary on any headers, specify 0 for Quantity and omit Items.
            Items (list) -- Optional: A complex type that contains a Name element for each header that you want CloudFront to forward to the origin and to vary on for this cache behavior. If Quantity is 0, omit Items.
            (string) --
            
            TrustedSigners (dict) -- [REQUIRED] A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content. If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled, and specify the applicable values for Quantity and Items. For more information, go to Using a Signed URL to Serve Private Content in the Amazon CloudFront Developer Guide. If you don't want to require signed URLs in requests for objects that match PathPattern, specify false for Enabled and 0 for Quantity. Omit Items. To add, change, or remove one or more trusted signers, change Enabled to true (if it's currently false), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.
            Enabled (boolean) -- [REQUIRED] Specifies whether you want to require end users to use signed URLs to access the files specified by PathPattern and TargetOriginId.
            Quantity (integer) -- [REQUIRED] The number of trusted signers for this cache behavior.
            Items (list) -- Optional: A complex type that contains trusted signers for this cache behavior. If Quantity is 0, you can omit Items.
            (string) --
            
            ViewerProtocolPolicy (string) -- [REQUIRED] Use this element to specify the protocol that users can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern. If you want CloudFront to allow end users to use any available protocol, specify allow-all. If you want CloudFront to require HTTPS, specify https. If you want CloudFront to respond to an HTTP request with an HTTP status code of 301 (Moved Permanently) and the HTTPS URL, specify redirect-to-https. The viewer then resubmits the request using the HTTPS URL.
            MinTTL (integer) -- [REQUIRED] The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront queries your origin to see whether the object has been updated.You can specify a value from 0 to 3,153,600,000 seconds (100 years).
            AllowedMethods (dict) -- A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices: - CloudFront forwards only GET and HEAD requests. - CloudFront forwards only GET, HEAD and OPTIONS requests. - CloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST, and DELETE requests. If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can't perform operations that you don't want them to. For example, you may not want users to have permission to delete objects from your origin.
            Quantity (integer) -- [REQUIRED] The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET, HEAD and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST, and DELETE requests).
            Items (list) -- [REQUIRED] A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.
            (string) --
            CachedMethods (dict) -- A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices: - CloudFront caches responses to GET and HEAD requests. - CloudFront caches responses to GET, HEAD, and OPTIONS requests. If you pick the second choice for your S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers and Origin headers for the responses to be cached correctly.
            Quantity (integer) -- [REQUIRED] The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET, HEAD, and OPTIONS requests).
            Items (list) -- [REQUIRED] A complex type that contains the HTTP methods that you want CloudFront to cache responses to.
            (string) --
            
            SmoothStreaming (boolean) -- Indicates whether you want to distribute media files in Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true; if not, specify false.
            DefaultTTL (integer) -- If you don't configure your origin to add a Cache-Control max-age directive or an Expires header, DefaultTTL is the default amount of time (in seconds) that an object is in a CloudFront cache before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age, Cache-Control s-maxage, and Expires to objects. You can specify a value from 0 to 3,153,600,000 seconds (100 years).
            MaxTTL (integer) -- The maximum amount of time (in seconds) that an object is in a CloudFront cache before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as Cache-Control max-age, Cache-Control s-maxage, and Expires to objects. You can specify a value from 0 to 3,153,600,000 seconds (100 years).
            Compress (boolean) -- Whether you want CloudFront to automatically compress content for web requests that include Accept-Encoding: gzip in the request header. If so, specify true; if not, specify false. CloudFront compresses files larger than 1000 bytes and less than 1 megabyte for both Amazon S3 and custom origins. When a CloudFront edge location is unusually busy, some files might not be compressed. The value of the Content-Type header must be on the list of file types that CloudFront will compress. For the current list, see Serving Compressed Content in the Amazon CloudFront Developer Guide. If you configure CloudFront to compress content, CloudFront removes the ETag response header from the objects that it compresses. The ETag header indicates that the version in a CloudFront edge cache is identical to the version on the origin server, but after compression the two versions are no longer identical. As a result, for compressed objects, CloudFront can't use the ETag header to determine whether an expired object in the CloudFront edge cache is still the latest version.
            
            CustomErrorResponses (dict) -- A complex type that contains zero or more CustomErrorResponse elements.
            Quantity (integer) -- [REQUIRED] The number of custom error responses for this distribution.
            Items (list) -- Optional: A complex type that contains custom error responses for this distribution. If Quantity is 0, you can omit Items.
            (dict) -- A complex type that describes how you'd prefer CloudFront to respond to requests that result in either a 4xx or 5xx response. You can control whether a custom error page should be displayed, what the desired response code should be for this error page and how long should the error response be cached by CloudFront. If you don't want to specify any custom error responses, include only an empty CustomErrorResponses element. To delete all custom error responses in an existing distribution, update the distribution configuration and include only an empty CustomErrorResponses element. To add, change, or remove one or more custom error responses, update the distribution configuration and specify all of the custom error responses that you want to include in the updated distribution.
            ErrorCode (integer) -- [REQUIRED] The 4xx or 5xx HTTP status code that you want to customize. For a list of HTTP status codes that you can customize, see CloudFront documentation.
            ResponsePagePath (string) -- The path of the custom error page (for example, /custom_404.html). The path is relative to the distribution and must begin with a slash (/). If the path includes any non-ASCII characters or unsafe characters as defined in RFC 1783 (http://www.ietf.org/rfc/rfc1738.txt), URL encode those characters. Do not URL encode any other characters in the path, or CloudFront will not return the custom error page to the viewer.
            ResponseCode (string) -- The HTTP status code that you want CloudFront to return with the custom error page to the viewer. For a list of HTTP status codes that you can replace, see CloudFront Documentation.
            ErrorCachingMinTTL (integer) -- The minimum amount of time you want HTTP error codes to stay in CloudFront caches before CloudFront queries your origin to see whether the object has been updated. You can specify a value from 0 to 31,536,000.
            
            Comment (string) -- [REQUIRED] Any comments you want to include about the distribution.
            Logging (dict) -- A complex type that controls whether access logs are written for the distribution.
            Enabled (boolean) -- [REQUIRED] Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you do not want to enable logging when you create a distribution or if you want to disable logging for an existing distribution, specify false for Enabled, and specify empty Bucket and Prefix elements. If you specify false for Enabled but you specify values for Bucket, prefix and IncludeCookies, the values are automatically deleted.
            IncludeCookies (boolean) -- [REQUIRED] Specifies whether you want CloudFront to include cookies in access logs, specify true for IncludeCookies. If you choose to include cookies in logs, CloudFront logs all cookies regardless of how you configure the cache behaviors for this distribution. If you do not want to include cookies when you create a distribution or if you want to disable include cookies for an existing distribution, specify false for IncludeCookies.
            Bucket (string) -- [REQUIRED] The Amazon S3 bucket to store the access logs in, for example, myawslogbucket.s3.amazonaws.com.
            Prefix (string) -- [REQUIRED] An optional string that you want CloudFront to prefix to the access log filenames for this distribution, for example, myprefix/. If you want to enable logging, but you do not want to specify a prefix, you still must include an empty Prefix element in the Logging element.
            PriceClass (string) -- A complex type that contains information about price class for this distribution.
            Enabled (boolean) -- [REQUIRED] Whether the distribution is enabled to accept end user requests for content.
            ViewerCertificate (dict) -- A complex type that contains information about viewer certificates for this distribution.
            CloudFrontDefaultCertificate (boolean) -- If you want viewers to use HTTPS to request your objects and you're using the CloudFront domain name of your distribution in your object URLs (for example, https://d111111abcdef8.cloudfront.net/logo.jpg), set to true. Omit this value if you are setting an ACMCertificateArn or IAMCertificateId.
            IAMCertificateId (string) -- If you want viewers to use HTTPS to request your objects and you're using an alternate domain name in your object URLs (for example, https://example.com/logo.jpg), specify the IAM certificate identifier of the custom viewer certificate for this distribution. Specify either this value, ACMCertificateArn, or CloudFrontDefaultCertificate.
            ACMCertificateArn (string) -- If you want viewers to use HTTPS to request your objects and you're using an alternate domain name in your object URLs (for example, https://example.com/logo.jpg), specify the ACM certificate ARN of the custom viewer certificate for this distribution. Specify either this value, IAMCertificateId, or CloudFrontDefaultCertificate.
            SSLSupportMethod (string) -- If you specify a value for IAMCertificateId, you must also specify how you want CloudFront to serve HTTPS requests. Valid values are vip and sni-only. If you specify vip, CloudFront uses dedicated IP addresses for your content and can respond to HTTPS requests from any viewer. However, you must request permission to use this feature, and you incur additional monthly charges. If you specify sni-only, CloudFront can only respond to HTTPS requests from viewers that support Server Name Indication (SNI). All modern browsers support SNI, but some browsers still in use don't support SNI. Do not specify a value for SSLSupportMethod if you specified true for CloudFrontDefaultCertificate.
            MinimumProtocolVersion (string) -- Specify the minimum version of the SSL protocol that you want CloudFront to use, SSLv3 or TLSv1, for HTTPS connections. CloudFront will serve your objects only to browsers or devices that support at least the SSL version that you specify. The TLSv1 protocol is more secure, so we recommend that you specify SSLv3 only if your users are using browsers or devices that don't support TLSv1. If you're using a custom certificate (if you specify a value for IAMCertificateId) and if you're using dedicated IP (if you specify vip for SSLSupportMethod), you can choose SSLv3 or TLSv1 as the MinimumProtocolVersion. If you're using a custom certificate (if you specify a value for IAMCertificateId) and if you're using SNI (if you specify sni-only for SSLSupportMethod), you must specify TLSv1 for MinimumProtocolVersion.
            Certificate (string) -- Note: this field is deprecated. Please use one of [ACMCertificateArn, IAMCertificateId, CloudFrontDefaultCertificate].
            CertificateSource (string) -- Note: this field is deprecated. Please use one of [ACMCertificateArn, IAMCertificateId, CloudFrontDefaultCertificate].
            Restrictions (dict) -- A complex type that identifies ways in which you want to restrict distribution of your content.
            GeoRestriction (dict) -- [REQUIRED] A complex type that controls the countries in which your content is distributed. For more information about geo restriction, go to Customizing Error Responses in the Amazon CloudFront Developer Guide. CloudFront determines the location of your users using MaxMind GeoIP databases. For information about the accuracy of these databases, see How accurate are your GeoIP databases? on the MaxMind website.
            RestrictionType (string) -- [REQUIRED] The method that you want to use to restrict distribution of your content by country: - none: No geo restriction is enabled, meaning access to content is not restricted by client geo location. - blacklist: The Location elements specify the countries in which you do not want CloudFront to distribute your content. - whitelist: The Location elements specify the countries in which you want CloudFront to distribute your content.
            Quantity (integer) -- [REQUIRED] When geo restriction is enabled, this is the number of countries in your whitelist or blacklist. Otherwise, when it is not enabled, Quantity is 0, and you can omit Items.
            Items (list) -- A complex type that contains a Location element for each country in which you want CloudFront either to distribute your content (whitelist) or not distribute your content (blacklist). The Location element is a two-letter, uppercase country code for a country that you want to include in your blacklist or whitelist. Include one Location element for each country. CloudFront and MaxMind both use ISO 3166 country codes. For the current list of countries and the corresponding codes, see ISO 3166-1-alpha-2 code on the International Organization for Standardization website. You can also refer to the country list in the CloudFront console, which includes both country names and codes.
            (string) --
            
            WebACLId (string) -- (Optional) If you're using AWS WAF to filter CloudFront requests, the Id of the AWS WAF web ACL that is associated with the distribution.
            
        :type DistributionConfig: dict
        :param Id: [REQUIRED] The distribution's id.
        :type Id: string
        :param IfMatch: The value of the ETag header you received when retrieving the distribution's configuration. For example: E2QWRUHAPOMQZL.
        :type IfMatch: string
        """
        self.client.update_distribution(DistributionConfig=DistributionConfig, Id=Id, IfMatch=IfMatch)

    def update_streaming_distribution(self, StreamingDistributionConfig=None, Id=None, IfMatch=None):
        """
        :param StreamingDistributionConfig: [REQUIRED] The streaming distribution's configuration information.
            CallerReference (string) -- [REQUIRED] A unique number that ensures the request can't be replayed. If the CallerReference is new (no matter the content of the StreamingDistributionConfig object), a new streaming distribution is created. If the CallerReference is a value you already sent in a previous request to create a streaming distribution, and the content of the StreamingDistributionConfig is identical to the original request (ignoring white space), the response includes the same information returned to the original request. If the CallerReference is a value you already sent in a previous request to create a streaming distribution but the content of the StreamingDistributionConfig is different from the original request, CloudFront returns a DistributionAlreadyExists error.
            S3Origin (dict) -- [REQUIRED] A complex type that contains information about the Amazon S3 bucket from which you want CloudFront to get your media files for distribution.
            DomainName (string) -- [REQUIRED] The DNS name of the S3 origin.
            OriginAccessIdentity (string) -- [REQUIRED] Your S3 origin's origin access identity.
            Aliases (dict) -- A complex type that contains information about CNAMEs (alternate domain names), if any, for this streaming distribution.
            Quantity (integer) -- [REQUIRED] The number of CNAMEs, if any, for this distribution.
            Items (list) -- Optional: A complex type that contains CNAME elements, if any, for this distribution. If Quantity is 0, you can omit Items.
            (string) --
            
            Comment (string) -- [REQUIRED] Any comments you want to include about the streaming distribution.
            Logging (dict) -- A complex type that controls whether access logs are written for the streaming distribution.
            Enabled (boolean) -- [REQUIRED] Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you do not want to enable logging when you create a streaming distribution or if you want to disable logging for an existing streaming distribution, specify false for Enabled, and specify empty Bucket and Prefix elements. If you specify false for Enabled but you specify values for Bucket and Prefix, the values are automatically deleted.
            Bucket (string) -- [REQUIRED] The Amazon S3 bucket to store the access logs in, for example, myawslogbucket.s3.amazonaws.com.
            Prefix (string) -- [REQUIRED] An optional string that you want CloudFront to prefix to the access log filenames for this streaming distribution, for example, myprefix/. If you want to enable logging, but you do not want to specify a prefix, you still must include an empty Prefix element in the Logging element.
            TrustedSigners (dict) -- [REQUIRED] A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content. If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled, and specify the applicable values for Quantity and Items. For more information, go to Using a Signed URL to Serve Private Content in the Amazon CloudFront Developer Guide. If you don't want to require signed URLs in requests for objects that match PathPattern, specify false for Enabled and 0 for Quantity. Omit Items. To add, change, or remove one or more trusted signers, change Enabled to true (if it's currently false), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.
            Enabled (boolean) -- [REQUIRED] Specifies whether you want to require end users to use signed URLs to access the files specified by PathPattern and TargetOriginId.
            Quantity (integer) -- [REQUIRED] The number of trusted signers for this cache behavior.
            Items (list) -- Optional: A complex type that contains trusted signers for this cache behavior. If Quantity is 0, you can omit Items.
            (string) --
            
            PriceClass (string) -- A complex type that contains information about price class for this streaming distribution.
            Enabled (boolean) -- [REQUIRED] Whether the streaming distribution is enabled to accept end user requests for content.
            
        :type StreamingDistributionConfig: dict
        :param Id: [REQUIRED] The streaming distribution's id.
        :type Id: string
        :param IfMatch: The value of the ETag header you received when retrieving the streaming distribution's configuration. For example: E2QWRUHAPOMQZL.
        :type IfMatch: string
        """
        self.client.update_streaming_distribution(StreamingDistributionConfig=StreamingDistributionConfig, Id=Id,
                                                  IfMatch=IfMatch)
