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

def add_tags_to_certificate(CertificateArn=None, Tags=None):
    """
    Adds one or more tags to an ACM Certificate. Tags are labels that you can use to identify and organize your AWS resources. Each tag consists of a key and an optional value . You specify the certificate on input by its Amazon Resource Name (ARN). You specify the tag by using a key-value pair.
    You can apply a tag to just one certificate if you want to identify a specific characteristic of that certificate, or you can apply the same tag to multiple certificates if you want to filter for a common relationship among those certificates. Similarly, you can apply the same tag to multiple resources if you want to specify a relationship among those resources. For example, you can add the same tag to an ACM Certificate and an Elastic Load Balancing load balancer to indicate that they are both used by the same website. For more information, see Tagging ACM Certificates .
    To remove one or more tags, use the  RemoveTagsFromCertificate action. To view all of the tags that have been applied to the certificate, use the  ListTagsForCertificate action.
    See also: AWS API Documentation
    
    
    :example: response = client.add_tags_to_certificate(
        CertificateArn='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type CertificateArn: string
    :param CertificateArn: [REQUIRED]
            String that contains the ARN of the ACM Certificate to which the tag is to be applied. This must be of the form:
            arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
            

    :type Tags: list
    :param Tags: [REQUIRED]
            The key-value pair that defines the tag. The tag value is optional.
            (dict) --A key-value pair that identifies or specifies metadata about an ACM resource.
            Key (string) -- [REQUIRED]The key of the tag.
            Value (string) --The value of the tag.
            
            

    """
    pass

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

def delete_certificate(CertificateArn=None):
    """
    Deletes an ACM Certificate and its associated private key. If this action succeeds, the certificate no longer appears in the list of ACM Certificates that can be displayed by calling the  ListCertificates action or be retrieved by calling the  GetCertificate action. The certificate will not be available for use by other AWS services.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_certificate(
        CertificateArn='string'
    )
    
    
    :type CertificateArn: string
    :param CertificateArn: [REQUIRED]
            String that contains the ARN of the ACM Certificate to be deleted. This must be of the form:
            arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
            

    """
    pass

def describe_certificate(CertificateArn=None):
    """
    Returns detailed metadata about the specified ACM Certificate.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_certificate(
        CertificateArn='string'
    )
    
    
    :type CertificateArn: string
    :param CertificateArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the ACM Certificate. The ARN must have the following form:
            arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
            

    :rtype: dict
    :return: {
        'Certificate': {
            'CertificateArn': 'string',
            'DomainName': 'string',
            'SubjectAlternativeNames': [
                'string',
            ],
            'DomainValidationOptions': [
                {
                    'DomainName': 'string',
                    'ValidationEmails': [
                        'string',
                    ],
                    'ValidationDomain': 'string',
                    'ValidationStatus': 'PENDING_VALIDATION'|'SUCCESS'|'FAILED'
                },
            ],
            'Serial': 'string',
            'Subject': 'string',
            'Issuer': 'string',
            'CreatedAt': datetime(2015, 1, 1),
            'IssuedAt': datetime(2015, 1, 1),
            'ImportedAt': datetime(2015, 1, 1),
            'Status': 'PENDING_VALIDATION'|'ISSUED'|'INACTIVE'|'EXPIRED'|'VALIDATION_TIMED_OUT'|'REVOKED'|'FAILED',
            'RevokedAt': datetime(2015, 1, 1),
            'RevocationReason': 'UNSPECIFIED'|'KEY_COMPROMISE'|'CA_COMPROMISE'|'AFFILIATION_CHANGED'|'SUPERCEDED'|'CESSATION_OF_OPERATION'|'CERTIFICATE_HOLD'|'REMOVE_FROM_CRL'|'PRIVILEGE_WITHDRAWN'|'A_A_COMPROMISE',
            'NotBefore': datetime(2015, 1, 1),
            'NotAfter': datetime(2015, 1, 1),
            'KeyAlgorithm': 'RSA_2048'|'RSA_1024'|'EC_prime256v1',
            'SignatureAlgorithm': 'string',
            'InUseBy': [
                'string',
            ],
            'FailureReason': 'NO_AVAILABLE_CONTACTS'|'ADDITIONAL_VERIFICATION_REQUIRED'|'DOMAIN_NOT_ALLOWED'|'INVALID_PUBLIC_DOMAIN'|'OTHER',
            'Type': 'IMPORTED'|'AMAZON_ISSUED',
            'RenewalSummary': {
                'RenewalStatus': 'PENDING_AUTO_RENEWAL'|'PENDING_VALIDATION'|'SUCCESS'|'FAILED',
                'DomainValidationOptions': [
                    {
                        'DomainName': 'string',
                        'ValidationEmails': [
                            'string',
                        ],
                        'ValidationDomain': 'string',
                        'ValidationStatus': 'PENDING_VALIDATION'|'SUCCESS'|'FAILED'
                    },
                ]
            }
        }
    }
    
    
    :returns: 
    (string) --
    
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

def get_certificate(CertificateArn=None):
    """
    Retrieves an ACM Certificate and certificate chain for the certificate specified by an ARN. The chain is an ordered list of certificates that contains the root certificate, intermediate certificates of subordinate CAs, and the ACM Certificate. The certificate and certificate chain are base64 encoded. If you want to decode the certificate chain to see the individual certificate fields, you can use OpenSSL.
    See also: AWS API Documentation
    
    
    :example: response = client.get_certificate(
        CertificateArn='string'
    )
    
    
    :type CertificateArn: string
    :param CertificateArn: [REQUIRED]
            String that contains a certificate ARN in the following format:
            arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
            

    :rtype: dict
    :return: {
        'Certificate': 'string',
        'CertificateChain': 'string'
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

def import_certificate(CertificateArn=None, Certificate=None, PrivateKey=None, CertificateChain=None):
    """
    Imports an SSL/TLS certificate into AWS Certificate Manager (ACM) to use with ACM's integrated AWS services .
    For more information about importing certificates into ACM, including the differences between certificates that you import and those that ACM provides, see Importing Certificates in the AWS Certificate Manager User Guide .
    To import a certificate, you must provide the certificate and the matching private key. When the certificate is not self-signed, you must also provide a certificate chain. You can omit the certificate chain when importing a self-signed certificate.
    The certificate, private key, and certificate chain must be PEM-encoded. For more information about converting these items to PEM format, see Importing Certificates Troubleshooting in the AWS Certificate Manager User Guide .
    To import a new certificate, omit the CertificateArn field. Include this field only when you want to replace a previously imported certificate.
    This operation returns the Amazon Resource Name (ARN) of the imported certificate.
    See also: AWS API Documentation
    
    
    :example: response = client.import_certificate(
        CertificateArn='string',
        Certificate=b'bytes',
        PrivateKey=b'bytes',
        CertificateChain=b'bytes'
    )
    
    
    :type CertificateArn: string
    :param CertificateArn: The Amazon Resource Name (ARN) of an imported certificate to replace. To import a new certificate, omit this field.

    :type Certificate: bytes
    :param Certificate: [REQUIRED]
            The certificate to import. It must meet the following requirements:
            Must be PEM-encoded.
            Must contain a 1024-bit or 2048-bit RSA public key.
            Must be valid at the time of import. You cannot import a certificate before its validity period begins (the certificate's NotBefore date) or after it expires (the certificate's NotAfter date).
            

    :type PrivateKey: bytes
    :param PrivateKey: [REQUIRED]
            The private key that matches the public key in the certificate. It must meet the following requirements:
            Must be PEM-encoded.
            Must be unencrypted. You cannot import a private key that is protected by a password or passphrase.
            

    :type CertificateChain: bytes
    :param CertificateChain: The certificate chain. It must be PEM-encoded.

    :rtype: dict
    :return: {
        'CertificateArn': 'string'
    }
    
    
    """
    pass

def list_certificates(CertificateStatuses=None, NextToken=None, MaxItems=None):
    """
    Retrieves a list of ACM Certificates and the domain name for each. You can optionally filter the list to return only the certificates that match the specified status.
    See also: AWS API Documentation
    
    
    :example: response = client.list_certificates(
        CertificateStatuses=[
            'PENDING_VALIDATION'|'ISSUED'|'INACTIVE'|'EXPIRED'|'VALIDATION_TIMED_OUT'|'REVOKED'|'FAILED',
        ],
        NextToken='string',
        MaxItems=123
    )
    
    
    :type CertificateStatuses: list
    :param CertificateStatuses: The status or statuses on which to filter the list of ACM Certificates.
            (string) --
            

    :type NextToken: string
    :param NextToken: Use this parameter only when paginating results and only in a subsequent request after you receive a response with truncated results. Set it to the value of NextToken from the response you just received.

    :type MaxItems: integer
    :param MaxItems: Use this parameter when paginating results to specify the maximum number of items to return in the response. If additional items exist beyond the number you specify, the NextToken element is sent in the response. Use this NextToken value in a subsequent request to retrieve additional items.

    :rtype: dict
    :return: {
        'NextToken': 'string',
        'CertificateSummaryList': [
            {
                'CertificateArn': 'string',
                'DomainName': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_tags_for_certificate(CertificateArn=None):
    """
    Lists the tags that have been applied to the ACM Certificate. Use the certificate's Amazon Resource Name (ARN) to specify the certificate. To add a tag to an ACM Certificate, use the  AddTagsToCertificate action. To delete a tag, use the  RemoveTagsFromCertificate action.
    See also: AWS API Documentation
    
    
    :example: response = client.list_tags_for_certificate(
        CertificateArn='string'
    )
    
    
    :type CertificateArn: string
    :param CertificateArn: [REQUIRED]
            String that contains the ARN of the ACM Certificate for which you want to list the tags. This has the following form:
            arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
            

    :rtype: dict
    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    """
    pass

def remove_tags_from_certificate(CertificateArn=None, Tags=None):
    """
    Remove one or more tags from an ACM Certificate. A tag consists of a key-value pair. If you do not specify the value portion of the tag when calling this function, the tag will be removed regardless of value. If you specify a value, the tag is removed only if it is associated with the specified value.
    To add tags to a certificate, use the  AddTagsToCertificate action. To view all of the tags that have been applied to a specific ACM Certificate, use the  ListTagsForCertificate action.
    See also: AWS API Documentation
    
    
    :example: response = client.remove_tags_from_certificate(
        CertificateArn='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type CertificateArn: string
    :param CertificateArn: [REQUIRED]
            String that contains the ARN of the ACM Certificate with one or more tags that you want to remove. This must be of the form:
            arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
            

    :type Tags: list
    :param Tags: [REQUIRED]
            The key-value pair that defines the tag to remove.
            (dict) --A key-value pair that identifies or specifies metadata about an ACM resource.
            Key (string) -- [REQUIRED]The key of the tag.
            Value (string) --The value of the tag.
            
            

    """
    pass

def request_certificate(DomainName=None, SubjectAlternativeNames=None, IdempotencyToken=None, DomainValidationOptions=None):
    """
    Requests an ACM Certificate for use with other AWS services. To request an ACM Certificate, you must specify the fully qualified domain name (FQDN) for your site. You can also specify additional FQDNs if users can reach your site by using other names. For each domain name you specify, email is sent to the domain owner to request approval to issue the certificate. After receiving approval from the domain owner, the ACM Certificate is issued. For more information, see the AWS Certificate Manager User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.request_certificate(
        DomainName='string',
        SubjectAlternativeNames=[
            'string',
        ],
        IdempotencyToken='string',
        DomainValidationOptions=[
            {
                'DomainName': 'string',
                'ValidationDomain': 'string'
            },
        ]
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            Fully qualified domain name (FQDN), such as www.example.com, of the site that you want to secure with an ACM Certificate. Use an asterisk (*) to create a wildcard certificate that protects several sites in the same domain. For example, *.example.com protects www.example.com, site.example.com, and images.example.com.
            

    :type SubjectAlternativeNames: list
    :param SubjectAlternativeNames: Additional FQDNs to be included in the Subject Alternative Name extension of the ACM Certificate. For example, add the name www.example.net to a certificate for which the DomainName field is www.example.com if users can reach your site by using either name.
            (string) --
            

    :type IdempotencyToken: string
    :param IdempotencyToken: Customer chosen string that can be used to distinguish between calls to RequestCertificate . Idempotency tokens time out after one hour. Therefore, if you call RequestCertificate multiple times with the same idempotency token within one hour, ACM recognizes that you are requesting only one certificate and will issue only one. If you change the idempotency token for each call, ACM recognizes that you are requesting multiple certificates.

    :type DomainValidationOptions: list
    :param DomainValidationOptions: The domain name that you want ACM to use to send you emails to validate your ownership of the domain.
            (dict) --Contains information about the domain names that you want ACM to use to send you emails to validate your ownership of the domain.
            DomainName (string) -- [REQUIRED]A fully qualified domain name (FQDN) in the certificate request.
            ValidationDomain (string) -- [REQUIRED]The domain name that you want ACM to use to send you validation emails. This domain name is the suffix of the email addresses that you want ACM to use. This must be the same as the DomainName value or a superdomain of the DomainName value. For example, if you request a certificate for testing.example.com , you can specify example.com for this value. In that case, ACM sends domain validation emails to the following five addresses:
            admin@example.com
            administrator@example.com
            hostmaster@example.com
            postmaster@example.com
            webmaster@example.com
            
            

    :rtype: dict
    :return: {
        'CertificateArn': 'string'
    }
    
    
    """
    pass

def resend_validation_email(CertificateArn=None, Domain=None, ValidationDomain=None):
    """
    Resends the email that requests domain ownership validation. The domain owner or an authorized representative must approve the ACM Certificate before it can be issued. The certificate can be approved by clicking a link in the mail to navigate to the Amazon certificate approval website and then clicking I Approve . However, the validation email can be blocked by spam filters. Therefore, if you do not receive the original mail, you can request that the mail be resent within 72 hours of requesting the ACM Certificate. If more than 72 hours have elapsed since your original request or since your last attempt to resend validation mail, you must request a new certificate.
    See also: AWS API Documentation
    
    
    :example: response = client.resend_validation_email(
        CertificateArn='string',
        Domain='string',
        ValidationDomain='string'
    )
    
    
    :type CertificateArn: string
    :param CertificateArn: [REQUIRED]
            String that contains the ARN of the requested certificate. The certificate ARN is generated and returned by the RequestCertificate action as soon as the request is made. By default, using this parameter causes email to be sent to all top-level domains you specified in the certificate request.
            The ARN must be of the form:
            arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012
            

    :type Domain: string
    :param Domain: [REQUIRED]
            The fully qualified domain name (FQDN) of the certificate that needs to be validated.
            

    :type ValidationDomain: string
    :param ValidationDomain: [REQUIRED]
            The base validation domain that will act as the suffix of the email addresses that are used to send the emails. This must be the same as the Domain value or a superdomain of the Domain value. For example, if you requested a certificate for site.subdomain.example.com and specify a ValidationDomain of subdomain.example.com , ACM sends email to the domain registrant, technical contact, and administrative contact in WHOIS and the following five addresses:
            admin@subdomain.example.com
            administrator@subdomain.example.com
            hostmaster@subdomain.example.com
            postmaster@subdomain.example.com
            webmaster@subdomain.example.com
            

    """
    pass

