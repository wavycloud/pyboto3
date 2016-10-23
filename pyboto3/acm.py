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


def add_tags_to_certificate(CertificateArn=None, Tags=None):
    """
    :param CertificateArn: [REQUIRED]
            String that contains the ARN of the ACM Certificate to which the tag is to be applied. This must be of the form:
            arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
            
    :type CertificateArn: string
    :param Tags: [REQUIRED]
            The key-value pair that defines the tag. The tag value is optional.
            (dict) --A key-value pair that identifies or specifies metadata about an ACM resource.
            Key (string) -- [REQUIRED]The key of the tag.
            Value (string) --The value of the tag.
            
            
    :type Tags: list
    """
    pass


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


def delete_certificate(CertificateArn=None):
    """
    :param CertificateArn: [REQUIRED]
            String that contains the ARN of the ACM Certificate to be deleted. This must be of the form:
            arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
            ReturnsNone
            
    :type CertificateArn: string
    """
    pass


def describe_certificate(CertificateArn=None):
    """
    :param CertificateArn: [REQUIRED]
            String that contains an ACM Certificate ARN. The ARN must be of the form:
            arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
            Return typedict
            ReturnsResponse Syntax{
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
                    'ValidationDomain': 'string'
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
                'Type': 'IMPORTED'|'AMAZON_ISSUED'
              }
            }
            Response Structure
            (dict) --
            Certificate (dict) --Contains a CertificateDetail structure that lists the fields of an ACM Certificate.
            CertificateArn (string) --The Amazon Resource Name (ARN) of the certificate. For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            DomainName (string) --The fully qualified domain name for the certificate, such as www.example.com or example.com.
            SubjectAlternativeNames (list) --One or more domain names (subject alternative names) included in the certificate. This list contains the domain names that are bound to the public key that is contained in the certificate. The subject alternative names include the canonical domain name (CN) of the certificate and additional domain names that can be used to connect to the website.
            (string) --
            DomainValidationOptions (list) --Contains information about the email address or addresses used for domain validation. This field exists only when the certificate type is AMAZON_ISSUED .
            (dict) --Structure that contains the domain name, the base validation domain to which validation email is sent, and the email addresses used to validate the domain identity.
            DomainName (string) --Fully Qualified Domain Name (FQDN) of the form www.example.com or example.com .
            ValidationEmails (list) --A list of contact address for the domain registrant.
            (string) --
            ValidationDomain (string) --The base validation domain that acts as the suffix of the email addresses that are used to send the emails.
            
            Serial (string) --The serial number of the certificate.
            Subject (string) --The name of the entity that is associated with the public key contained in the certificate.
            Issuer (string) --The name of the certificate authority that issued and signed the certificate.
            CreatedAt (datetime) --The time at which the certificate was requested. This value exists only when the certificate type is AMAZON_ISSUED .
            IssuedAt (datetime) --The time at which the certificate was issued. This value exists only when the certificate type is AMAZON_ISSUED .
            ImportedAt (datetime) --The date and time at which the certificate was imported. This value exists only when the certificate type is IMPORTED .
            Status (string) --The status of the certificate.
            RevokedAt (datetime) --The time at which the certificate was revoked. This value exists only when the certificate status is REVOKED .
            RevocationReason (string) --The reason the certificate was revoked. This value exists only when the certificate status is REVOKED .
            NotBefore (datetime) --The time before which the certificate is not valid.
            NotAfter (datetime) --The time after which the certificate is not valid.
            KeyAlgorithm (string) --The algorithm that was used to generate the key pair (the public and private key).
            SignatureAlgorithm (string) --The algorithm that was used to sign the certificate.
            InUseBy (list) --A list of ARNs for the AWS resources that are using the certificate. A certificate can be used by multiple AWS resources.
            (string) --
            FailureReason (string) --The reason the certificate request failed. This value exists only when the certificate status is FAILED . For more information, see Certificate Request Failed in the AWS Certificate Manager User Guide .
            Type (string) --The source of the certificate. For certificates provided by ACM, this value is AMAZON_ISSUED . For certificates that you imported with ImportCertificate , this value is IMPORTED . ACM does not provide managed renewal for imported certificates. For more information about the differences between certificates that you import and those that ACM provides, see Importing Certificates in the AWS Certificate Manager User Guide .
            
            
            
    :type CertificateArn: string
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


def get_certificate(CertificateArn=None):
    """
    :param CertificateArn: [REQUIRED]
            String that contains a certificate ARN in the following format:
            arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
            Return typedict
            ReturnsResponse Syntax{
              'Certificate': 'string',
              'CertificateChain': 'string'
            }
            Response Structure
            (dict) --
            Certificate (string) --String that contains the ACM Certificate represented by the ARN specified at input.
            CertificateChain (string) --The certificate chain that contains the root certificate issued by the certificate authority (CA).
            
            
    :type CertificateArn: string
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


def import_certificate(CertificateArn=None, Certificate=None, PrivateKey=None, CertificateChain=None):
    """
    :param CertificateArn: The Amazon Resource Name (ARN) of an imported certificate to replace. To import a new certificate, omit this field.
    :type CertificateArn: string
    :param Certificate: [REQUIRED]
            The certificate to import. It must meet the following requirements:
            Must be PEM-encoded.
            Must contain a 1024-bit or 2048-bit RSA public key.
            Must be valid at the time of import. You cannot import a certificate before its validity period begins (the certificate's NotBefore date) or after it expires (the certificate's NotAfter date).
            
    :type Certificate: bytes
    :param PrivateKey: [REQUIRED]
            The private key that matches the public key in the certificate. It must meet the following requirements:
            Must be PEM-encoded.
            Must be unencrypted. You cannot import a private key that is protected by a password or passphrase.
            
    :type PrivateKey: bytes
    :param CertificateChain: The certificate chain. It must be PEM-encoded.
    :type CertificateChain: bytes
    """
    pass


def list_certificates(CertificateStatuses=None, NextToken=None, MaxItems=None):
    """
    :param CertificateStatuses: The status or statuses on which to filter the list of ACM Certificates.
            (string) --
            
    :type CertificateStatuses: list
    :param NextToken: Use this parameter only when paginating results and only in a subsequent request after you receive a response with truncated results. Set it to the value of NextToken from the response you just received.
    :type NextToken: string
    :param MaxItems: Use this parameter when paginating results to specify the maximum number of items to return in the response. If additional items exist beyond the number you specify, the NextToken element is sent in the response. Use this NextToken value in a subsequent request to retrieve additional items.
    :type MaxItems: integer
    """
    pass


def list_tags_for_certificate(CertificateArn=None):
    """
    :param CertificateArn: [REQUIRED]
            String that contains the ARN of the ACM Certificate for which you want to list the tags. This must be of the form:
            arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
            Return typedict
            ReturnsResponse Syntax{
              'Tags': [
                {
                  'Key': 'string',
                  'Value': 'string'
                },
              ]
            }
            Response Structure
            (dict) --
            Tags (list) --The key-value pairs that define the applied tags.
            (dict) --A key-value pair that identifies or specifies metadata about an ACM resource.
            Key (string) --The key of the tag.
            Value (string) --The value of the tag.
            
            
            
    :type CertificateArn: string
    """
    pass


def remove_tags_from_certificate(CertificateArn=None, Tags=None):
    """
    :param CertificateArn: [REQUIRED]
            String that contains the ARN of the ACM Certificate with one or more tags that you want to remove. This must be of the form:
            arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
            
    :type CertificateArn: string
    :param Tags: [REQUIRED]
            The key-value pair that defines the tag to remove.
            (dict) --A key-value pair that identifies or specifies metadata about an ACM resource.
            Key (string) -- [REQUIRED]The key of the tag.
            Value (string) --The value of the tag.
            
            
    :type Tags: list
    """
    pass


def request_certificate(DomainName=None, SubjectAlternativeNames=None, IdempotencyToken=None,
                        DomainValidationOptions=None):
    """
    :param DomainName: [REQUIRED]
            Fully qualified domain name (FQDN), such as www.example.com, of the site you want to secure with an ACM Certificate. Use an asterisk (*) to create a wildcard certificate that protects several sites in the same domain. For example, *.example.com protects www.example.com, site.example.com, and images.example.com.
            
    :type DomainName: string
    :param SubjectAlternativeNames: Additional FQDNs to be included in the Subject Alternative Name extension of the ACM Certificate. For example, add the name www.example.net to a certificate for which the DomainName field is www.example.com if users can reach your site by using either name.
            (string) --
            
    :type SubjectAlternativeNames: list
    :param IdempotencyToken: Customer chosen string that can be used to distinguish between calls to RequestCertificate . Idempotency tokens time out after one hour. Therefore, if you call RequestCertificate multiple times with the same idempotency token within one hour, ACM recognizes that you are requesting only one certificate and will issue only one. If you change the idempotency token for each call, ACM recognizes that you are requesting multiple certificates.
    :type IdempotencyToken: string
    :param DomainValidationOptions: The base validation domain that will act as the suffix of the email addresses that are used to send the emails. This must be the same as the Domain value or a superdomain of the Domain value. For example, if you requested a certificate for test.example.com and specify DomainValidationOptions of example.com , ACM sends email to the domain registrant, technical contact, and administrative contact in WHOIS and the following five addresses:
            admin@example.com
            administrator@example.com
            hostmaster@example.com
            postmaster@example.com
            webmaster@example.com
            (dict) --This structure is used in the request object of the RequestCertificate action.
            DomainName (string) -- [REQUIRED]Fully Qualified Domain Name (FQDN) of the certificate being requested.
            ValidationDomain (string) -- [REQUIRED]The domain to which validation email is sent. This is the base validation domain that will act as the suffix of the email addresses. This must be the same as the DomainName value or a superdomain of the DomainName value. For example, if you requested a certificate for site.subdomain.example.com and specify a ValidationDomain of subdomain.example.com , ACM sends email to the domain registrant, technical contact, and administrative contact in WHOIS for the base domain and the following five addresses:
            admin@subdomain.example.com
            administrator@subdomain.example.com
            hostmaster@subdomain.example.com
            postmaster@subdomain.example.com
            webmaster@subdomain.example.com
            
            
    :type DomainValidationOptions: list
    """
    pass


def resend_validation_email(CertificateArn=None, Domain=None, ValidationDomain=None):
    """
    :param CertificateArn: [REQUIRED]
            String that contains the ARN of the requested certificate. The certificate ARN is generated and returned by the RequestCertificate action as soon as the request is made. By default, using this parameter causes email to be sent to all top-level domains you specified in the certificate request.
            The ARN must be of the form:
            arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012
            
    :type CertificateArn: string
    :param Domain: [REQUIRED]
            The Fully Qualified Domain Name (FQDN) of the certificate that needs to be validated.
            
    :type Domain: string
    :param ValidationDomain: [REQUIRED]
            The base validation domain that will act as the suffix of the email addresses that are used to send the emails. This must be the same as the Domain value or a superdomain of the Domain value. For example, if you requested a certificate for site.subdomain.example.com and specify a ValidationDomain of subdomain.example.com , ACM sends email to the domain registrant, technical contact, and administrative contact in WHOIS and the following five addresses:
            admin@subdomain.example.com
            administrator@subdomain.example.com
            hostmaster@subdomain.example.com
            postmaster@subdomain.example.com
            webmaster@subdomain.example.com
            
    :type ValidationDomain: string
    """
    pass
