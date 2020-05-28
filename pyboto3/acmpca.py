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

def create_certificate_authority(CertificateAuthorityConfiguration=None, RevocationConfiguration=None, CertificateAuthorityType=None, IdempotencyToken=None, Tags=None):
    """
    Creates a root or subordinate private certificate authority (CA). You must specify the CA configuration, the certificate revocation list (CRL) configuration, the CA type, and an optional idempotency token to avoid accidental creation of multiple CAs. The CA configuration specifies the name of the algorithm and key size to be used to create the CA private key, the type of signing algorithm that the CA uses, and X.500 subject information. The CRL configuration specifies the CRL expiration period in days (the validity period of the CRL), the Amazon S3 bucket that will contain the CRL, and a CNAME alias for the S3 bucket that is included in certificates issued by the CA. If successful, this action returns the Amazon Resource Name (ARN) of the CA.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_certificate_authority(
        CertificateAuthorityConfiguration={
            'KeyAlgorithm': 'RSA_2048'|'RSA_4096'|'EC_prime256v1'|'EC_secp384r1',
            'SigningAlgorithm': 'SHA256WITHECDSA'|'SHA384WITHECDSA'|'SHA512WITHECDSA'|'SHA256WITHRSA'|'SHA384WITHRSA'|'SHA512WITHRSA',
            'Subject': {
                'Country': 'string',
                'Organization': 'string',
                'OrganizationalUnit': 'string',
                'DistinguishedNameQualifier': 'string',
                'State': 'string',
                'CommonName': 'string',
                'SerialNumber': 'string',
                'Locality': 'string',
                'Title': 'string',
                'Surname': 'string',
                'GivenName': 'string',
                'Initials': 'string',
                'Pseudonym': 'string',
                'GenerationQualifier': 'string'
            }
        },
        RevocationConfiguration={
            'CrlConfiguration': {
                'Enabled': True|False,
                'ExpirationInDays': 123,
                'CustomCname': 'string',
                'S3BucketName': 'string'
            }
        },
        CertificateAuthorityType='ROOT'|'SUBORDINATE',
        IdempotencyToken='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type CertificateAuthorityConfiguration: dict
    :param CertificateAuthorityConfiguration: [REQUIRED]\nName and bit size of the private key algorithm, the name of the signing algorithm, and X.500 certificate subject information.\n\nKeyAlgorithm (string) -- [REQUIRED]Type of the public key algorithm and size, in bits, of the key pair that your CA creates when it issues a certificate. When you create a subordinate CA, you must use a key algorithm supported by the parent CA.\n\nSigningAlgorithm (string) -- [REQUIRED]Name of the algorithm your private CA uses to sign certificate requests.\n\nSubject (dict) -- [REQUIRED]Structure that contains X.500 distinguished name information for your private CA.\n\nCountry (string) --Two-digit code that specifies the country in which the certificate subject located.\n\nOrganization (string) --Legal name of the organization with which the certificate subject is affiliated.\n\nOrganizationalUnit (string) --A subdivision or unit of the organization (such as sales or finance) with which the certificate subject is affiliated.\n\nDistinguishedNameQualifier (string) --Disambiguating information for the certificate subject.\n\nState (string) --State in which the subject of the certificate is located.\n\nCommonName (string) --Fully qualified domain name (FQDN) associated with the certificate subject.\n\nSerialNumber (string) --The certificate serial number.\n\nLocality (string) --The locality (such as a city or town) in which the certificate subject is located.\n\nTitle (string) --A title such as Mr. or Ms., which is pre-pended to the name to refer formally to the certificate subject.\n\nSurname (string) --Family name. In the US and the UK, for example, the surname of an individual is ordered last. In Asian cultures the surname is typically ordered first.\n\nGivenName (string) --First name.\n\nInitials (string) --Concatenation that typically contains the first letter of the GivenName , the first letter of the middle name if one exists, and the first letter of the SurName .\n\nPseudonym (string) --Typically a shortened version of a longer GivenName . For example, Jonathan is often shortened to John. Elizabeth is often shortened to Beth, Liz, or Eliza.\n\nGenerationQualifier (string) --Typically a qualifier appended to the name of an individual. Examples include Jr. for junior, Sr. for senior, and III for third.\n\n\n\n\n

    :type RevocationConfiguration: dict
    :param RevocationConfiguration: Contains a Boolean value that you can use to enable a certification revocation list (CRL) for the CA, the name of the S3 bucket to which ACM Private CA will write the CRL, and an optional CNAME alias that you can use to hide the name of your bucket in the CRL Distribution Points extension of your CA certificate. For more information, see the CrlConfiguration structure.\n\nCrlConfiguration (dict) --Configuration of the certificate revocation list (CRL), if any, maintained by your private CA.\n\nEnabled (boolean) -- [REQUIRED]Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. You can use this value to enable certificate revocation for a new CA when you call the CreateCertificateAuthority action or for an existing CA when you call the UpdateCertificateAuthority action.\n\nExpirationInDays (integer) --Number of days until a certificate expires.\n\nCustomCname (string) --Name inserted into the certificate CRL Distribution Points extension that enables the use of an alias for the CRL distribution point. Use this value if you don\'t want the name of your S3 bucket to be public.\n\nS3BucketName (string) --Name of the S3 bucket that contains the CRL. If you do not provide a value for the CustomCname argument, the name of your S3 bucket is placed into the CRL Distribution Points extension of the issued certificate. You can change the name of your bucket by calling the UpdateCertificateAuthority action. You must specify a bucket policy that allows ACM Private CA to write the CRL to your bucket.\n\n\n\n\n

    :type CertificateAuthorityType: string
    :param CertificateAuthorityType: [REQUIRED]\nThe type of the certificate authority.\n

    :type IdempotencyToken: string
    :param IdempotencyToken: Alphanumeric string that can be used to distinguish between calls to CreateCertificateAuthority . Idempotency tokens time out after five minutes. Therefore, if you call CreateCertificateAuthority multiple times with the same idempotency token within a five minute period, ACM Private CA recognizes that you are requesting only one certificate. As a result, ACM Private CA issues only one. If you change the idempotency token for each call, however, ACM Private CA recognizes that you are requesting multiple certificates.

    :type Tags: list
    :param Tags: Key-value pairs that will be attached to the new private CA. You can associate up to 50 tags with a private CA. For information using tags with\nIAM to manage permissions, see Controlling Access Using IAM Tags .\n\n(dict) --Tags are labels that you can use to identify and organize your private CAs. Each tag consists of a key and an optional value. You can associate up to 50 tags with a private CA. To add one or more tags to a private CA, call the TagCertificateAuthority action. To remove a tag, call the UntagCertificateAuthority action.\n\nKey (string) -- [REQUIRED]Key (name) of the tag.\n\nValue (string) --Value of the tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CertificateAuthorityArn': 'string'
}


Response Structure

(dict) --

CertificateAuthorityArn (string) --
If successful, the Amazon Resource Name (ARN) of the certificate authority (CA). This is of the form:

``arn:aws:acm-pca:region :account :certificate-authority/12345678-1234-1234-1234-123456789012 `` .








Exceptions

ACMPCA.Client.exceptions.InvalidArgsException
ACMPCA.Client.exceptions.InvalidPolicyException
ACMPCA.Client.exceptions.InvalidTagException
ACMPCA.Client.exceptions.LimitExceededException


    :return: {
        'CertificateAuthorityArn': 'string'
    }
    
    
    :returns: 
    ACMPCA.Client.exceptions.InvalidArgsException
    ACMPCA.Client.exceptions.InvalidPolicyException
    ACMPCA.Client.exceptions.InvalidTagException
    ACMPCA.Client.exceptions.LimitExceededException
    
    """
    pass

def create_certificate_authority_audit_report(CertificateAuthorityArn=None, S3BucketName=None, AuditReportResponseFormat=None):
    """
    Creates an audit report that lists every time that your CA private key is used. The report is saved in the Amazon S3 bucket that you specify on input. The  IssueCertificate and  RevokeCertificate actions use the private key.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_certificate_authority_audit_report(
        CertificateAuthorityArn='string',
        S3BucketName='string',
        AuditReportResponseFormat='JSON'|'CSV'
    )
    
    
    :type CertificateAuthorityArn: string
    :param CertificateAuthorityArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the CA to be audited. This is of the form:\n\n``arn:aws:acm-pca:region :account :certificate-authority/12345678-1234-1234-1234-123456789012 `` .\n

    :type S3BucketName: string
    :param S3BucketName: [REQUIRED]\nThe name of the S3 bucket that will contain the audit report.\n

    :type AuditReportResponseFormat: string
    :param AuditReportResponseFormat: [REQUIRED]\nThe format in which to create the report. This can be either JSON or CSV .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AuditReportId': 'string',
    'S3Key': 'string'
}


Response Structure

(dict) --

AuditReportId (string) --
An alphanumeric string that contains a report identifier.

S3Key (string) --
The key that uniquely identifies the report file in your S3 bucket.







Exceptions

ACMPCA.Client.exceptions.RequestInProgressException
ACMPCA.Client.exceptions.RequestFailedException
ACMPCA.Client.exceptions.ResourceNotFoundException
ACMPCA.Client.exceptions.InvalidArnException
ACMPCA.Client.exceptions.InvalidArgsException
ACMPCA.Client.exceptions.InvalidStateException


    :return: {
        'AuditReportId': 'string',
        'S3Key': 'string'
    }
    
    
    :returns: 
    ACMPCA.Client.exceptions.RequestInProgressException
    ACMPCA.Client.exceptions.RequestFailedException
    ACMPCA.Client.exceptions.ResourceNotFoundException
    ACMPCA.Client.exceptions.InvalidArnException
    ACMPCA.Client.exceptions.InvalidArgsException
    ACMPCA.Client.exceptions.InvalidStateException
    
    """
    pass

def create_permission(CertificateAuthorityArn=None, Principal=None, SourceAccount=None, Actions=None):
    """
    Assigns permissions from a private CA to a designated AWS service. Services are specified by their service principals and can be given permission to create and retrieve certificates on a private CA. Services can also be given permission to list the active permissions that the private CA has granted. For ACM to automatically renew your private CA\'s certificates, you must assign all possible permissions from the CA to the ACM service principal.
    At this time, you can only assign permissions to ACM (acm.amazonaws.com ). Permissions can be revoked with the  DeletePermission action and listed with the  ListPermissions action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_permission(
        CertificateAuthorityArn='string',
        Principal='string',
        SourceAccount='string',
        Actions=[
            'IssueCertificate'|'GetCertificate'|'ListPermissions',
        ]
    )
    
    
    :type CertificateAuthorityArn: string
    :param CertificateAuthorityArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the CA that grants the permissions. You can find the ARN by calling the ListCertificateAuthorities action. This must have the following form:\n\n``arn:aws:acm-pca:region :account :certificate-authority/12345678-1234-1234-1234-123456789012 `` .\n

    :type Principal: string
    :param Principal: [REQUIRED]\nThe AWS service or identity that receives the permission. At this time, the only valid principal is acm.amazonaws.com .\n

    :type SourceAccount: string
    :param SourceAccount: The ID of the calling account.

    :type Actions: list
    :param Actions: [REQUIRED]\nThe actions that the specified AWS service principal can use. These include IssueCertificate , GetCertificate , and ListPermissions .\n\n(string) --\n\n

    :returns: 
    ACMPCA.Client.exceptions.ResourceNotFoundException
    ACMPCA.Client.exceptions.InvalidArnException
    ACMPCA.Client.exceptions.PermissionAlreadyExistsException
    ACMPCA.Client.exceptions.LimitExceededException
    ACMPCA.Client.exceptions.InvalidStateException
    ACMPCA.Client.exceptions.RequestFailedException
    
    """
    pass

def delete_certificate_authority(CertificateAuthorityArn=None, PermanentDeletionTimeInDays=None):
    """
    Deletes a private certificate authority (CA). You must provide the Amazon Resource Name (ARN) of the private CA that you want to delete. You can find the ARN by calling the  ListCertificateAuthorities action.
    Before you can delete a CA that you have created and activated, you must disable it. To do this, call the  UpdateCertificateAuthority action and set the CertificateAuthorityStatus parameter to DISABLED .
    Additionally, you can delete a CA if you are waiting for it to be created (that is, the status of the CA is CREATING ). You can also delete it if the CA has been created but you haven\'t yet imported the signed certificate into ACM Private CA (that is, the status of the CA is PENDING_CERTIFICATE ).
    When you successfully call  DeleteCertificateAuthority , the CA\'s status changes to DELETED . However, the CA won\'t be permanently deleted until the restoration period has passed. By default, if you do not set the PermanentDeletionTimeInDays parameter, the CA remains restorable for 30 days. You can set the parameter from 7 to 30 days. The  DescribeCertificateAuthority action returns the time remaining in the restoration window of a private CA in the DELETED state. To restore an eligible CA, call the  RestoreCertificateAuthority action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_certificate_authority(
        CertificateAuthorityArn='string',
        PermanentDeletionTimeInDays=123
    )
    
    
    :type CertificateAuthorityArn: string
    :param CertificateAuthorityArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that was returned when you called CreateCertificateAuthority . This must have the following form:\n\n``arn:aws:acm-pca:region :account :certificate-authority/12345678-1234-1234-1234-123456789012 `` .\n

    :type PermanentDeletionTimeInDays: integer
    :param PermanentDeletionTimeInDays: The number of days to make a CA restorable after it has been deleted. This can be anywhere from 7 to 30 days, with 30 being the default.

    :returns: 
    ACMPCA.Client.exceptions.ConcurrentModificationException
    ACMPCA.Client.exceptions.ResourceNotFoundException
    ACMPCA.Client.exceptions.InvalidArnException
    ACMPCA.Client.exceptions.InvalidStateException
    
    """
    pass

def delete_permission(CertificateAuthorityArn=None, Principal=None, SourceAccount=None):
    """
    Revokes permissions that a private CA assigned to a designated AWS service. Permissions can be created with the  CreatePermission action and listed with the  ListPermissions action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_permission(
        CertificateAuthorityArn='string',
        Principal='string',
        SourceAccount='string'
    )
    
    
    :type CertificateAuthorityArn: string
    :param CertificateAuthorityArn: [REQUIRED]\nThe Amazon Resource Number (ARN) of the private CA that issued the permissions. You can find the CA\'s ARN by calling the ListCertificateAuthorities action. This must have the following form:\n\n``arn:aws:acm-pca:region :account :certificate-authority/12345678-1234-1234-1234-123456789012 `` .\n

    :type Principal: string
    :param Principal: [REQUIRED]\nThe AWS service or identity that will have its CA permissions revoked. At this time, the only valid service principal is acm.amazonaws.com\n

    :type SourceAccount: string
    :param SourceAccount: The AWS account that calls this action.

    :returns: 
    ACMPCA.Client.exceptions.ResourceNotFoundException
    ACMPCA.Client.exceptions.InvalidArnException
    ACMPCA.Client.exceptions.InvalidStateException
    ACMPCA.Client.exceptions.RequestFailedException
    
    """
    pass

def describe_certificate_authority(CertificateAuthorityArn=None):
    """
    Lists information about your private certificate authority (CA). You specify the private CA on input by its ARN (Amazon Resource Name). The output contains the status of your CA. This can be any of the following:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_certificate_authority(
        CertificateAuthorityArn='string'
    )
    
    
    :type CertificateAuthorityArn: string
    :param CertificateAuthorityArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that was returned when you called CreateCertificateAuthority . This must be of the form:\n\n``arn:aws:acm-pca:region :account :certificate-authority/12345678-1234-1234-1234-123456789012 `` .\n

    :rtype: dict
ReturnsResponse Syntax{
    'CertificateAuthority': {
        'Arn': 'string',
        'CreatedAt': datetime(2015, 1, 1),
        'LastStateChangeAt': datetime(2015, 1, 1),
        'Type': 'ROOT'|'SUBORDINATE',
        'Serial': 'string',
        'Status': 'CREATING'|'PENDING_CERTIFICATE'|'ACTIVE'|'DELETED'|'DISABLED'|'EXPIRED'|'FAILED',
        'NotBefore': datetime(2015, 1, 1),
        'NotAfter': datetime(2015, 1, 1),
        'FailureReason': 'REQUEST_TIMED_OUT'|'UNSUPPORTED_ALGORITHM'|'OTHER',
        'CertificateAuthorityConfiguration': {
            'KeyAlgorithm': 'RSA_2048'|'RSA_4096'|'EC_prime256v1'|'EC_secp384r1',
            'SigningAlgorithm': 'SHA256WITHECDSA'|'SHA384WITHECDSA'|'SHA512WITHECDSA'|'SHA256WITHRSA'|'SHA384WITHRSA'|'SHA512WITHRSA',
            'Subject': {
                'Country': 'string',
                'Organization': 'string',
                'OrganizationalUnit': 'string',
                'DistinguishedNameQualifier': 'string',
                'State': 'string',
                'CommonName': 'string',
                'SerialNumber': 'string',
                'Locality': 'string',
                'Title': 'string',
                'Surname': 'string',
                'GivenName': 'string',
                'Initials': 'string',
                'Pseudonym': 'string',
                'GenerationQualifier': 'string'
            }
        },
        'RevocationConfiguration': {
            'CrlConfiguration': {
                'Enabled': True|False,
                'ExpirationInDays': 123,
                'CustomCname': 'string',
                'S3BucketName': 'string'
            }
        },
        'RestorableUntil': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
CertificateAuthority (dict) --A  CertificateAuthority structure that contains information about your private CA.

Arn (string) --Amazon Resource Name (ARN) for your private certificate authority (CA). The format is `` 12345678-1234-1234-1234-123456789012 `` .

CreatedAt (datetime) --Date and time at which your private CA was created.

LastStateChangeAt (datetime) --Date and time at which your private CA was last updated.

Type (string) --Type of your private CA.

Serial (string) --Serial number of your private CA.

Status (string) --Status of your private CA.

NotBefore (datetime) --Date and time before which your private CA certificate is not valid.

NotAfter (datetime) --Date and time after which your private CA certificate is not valid.

FailureReason (string) --Reason the request to create your private CA failed.

CertificateAuthorityConfiguration (dict) --Your private CA configuration.

KeyAlgorithm (string) --Type of the public key algorithm and size, in bits, of the key pair that your CA creates when it issues a certificate. When you create a subordinate CA, you must use a key algorithm supported by the parent CA.

SigningAlgorithm (string) --Name of the algorithm your private CA uses to sign certificate requests.

Subject (dict) --Structure that contains X.500 distinguished name information for your private CA.

Country (string) --Two-digit code that specifies the country in which the certificate subject located.

Organization (string) --Legal name of the organization with which the certificate subject is affiliated.

OrganizationalUnit (string) --A subdivision or unit of the organization (such as sales or finance) with which the certificate subject is affiliated.

DistinguishedNameQualifier (string) --Disambiguating information for the certificate subject.

State (string) --State in which the subject of the certificate is located.

CommonName (string) --Fully qualified domain name (FQDN) associated with the certificate subject.

SerialNumber (string) --The certificate serial number.

Locality (string) --The locality (such as a city or town) in which the certificate subject is located.

Title (string) --A title such as Mr. or Ms., which is pre-pended to the name to refer formally to the certificate subject.

Surname (string) --Family name. In the US and the UK, for example, the surname of an individual is ordered last. In Asian cultures the surname is typically ordered first.

GivenName (string) --First name.

Initials (string) --Concatenation that typically contains the first letter of the GivenName , the first letter of the middle name if one exists, and the first letter of the SurName .

Pseudonym (string) --Typically a shortened version of a longer GivenName . For example, Jonathan is often shortened to John. Elizabeth is often shortened to Beth, Liz, or Eliza.

GenerationQualifier (string) --Typically a qualifier appended to the name of an individual. Examples include Jr. for junior, Sr. for senior, and III for third.





RevocationConfiguration (dict) --Information about the certificate revocation list (CRL) created and maintained by your private CA.

CrlConfiguration (dict) --Configuration of the certificate revocation list (CRL), if any, maintained by your private CA.

Enabled (boolean) --Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. You can use this value to enable certificate revocation for a new CA when you call the  CreateCertificateAuthority action or for an existing CA when you call the  UpdateCertificateAuthority action.

ExpirationInDays (integer) --Number of days until a certificate expires.

CustomCname (string) --Name inserted into the certificate CRL Distribution Points extension that enables the use of an alias for the CRL distribution point. Use this value if you don\'t want the name of your S3 bucket to be public.

S3BucketName (string) --Name of the S3 bucket that contains the CRL. If you do not provide a value for the CustomCname argument, the name of your S3 bucket is placed into the CRL Distribution Points extension of the issued certificate. You can change the name of your bucket by calling the  UpdateCertificateAuthority action. You must specify a bucket policy that allows ACM Private CA to write the CRL to your bucket.





RestorableUntil (datetime) --The period during which a deleted CA can be restored. For more information, see the PermanentDeletionTimeInDays parameter of the  DeleteCertificateAuthorityRequest action.








Exceptions

ACMPCA.Client.exceptions.ResourceNotFoundException
ACMPCA.Client.exceptions.InvalidArnException


    :return: {
        'CertificateAuthority': {
            'Arn': 'string',
            'CreatedAt': datetime(2015, 1, 1),
            'LastStateChangeAt': datetime(2015, 1, 1),
            'Type': 'ROOT'|'SUBORDINATE',
            'Serial': 'string',
            'Status': 'CREATING'|'PENDING_CERTIFICATE'|'ACTIVE'|'DELETED'|'DISABLED'|'EXPIRED'|'FAILED',
            'NotBefore': datetime(2015, 1, 1),
            'NotAfter': datetime(2015, 1, 1),
            'FailureReason': 'REQUEST_TIMED_OUT'|'UNSUPPORTED_ALGORITHM'|'OTHER',
            'CertificateAuthorityConfiguration': {
                'KeyAlgorithm': 'RSA_2048'|'RSA_4096'|'EC_prime256v1'|'EC_secp384r1',
                'SigningAlgorithm': 'SHA256WITHECDSA'|'SHA384WITHECDSA'|'SHA512WITHECDSA'|'SHA256WITHRSA'|'SHA384WITHRSA'|'SHA512WITHRSA',
                'Subject': {
                    'Country': 'string',
                    'Organization': 'string',
                    'OrganizationalUnit': 'string',
                    'DistinguishedNameQualifier': 'string',
                    'State': 'string',
                    'CommonName': 'string',
                    'SerialNumber': 'string',
                    'Locality': 'string',
                    'Title': 'string',
                    'Surname': 'string',
                    'GivenName': 'string',
                    'Initials': 'string',
                    'Pseudonym': 'string',
                    'GenerationQualifier': 'string'
                }
            },
            'RevocationConfiguration': {
                'CrlConfiguration': {
                    'Enabled': True|False,
                    'ExpirationInDays': 123,
                    'CustomCname': 'string',
                    'S3BucketName': 'string'
                }
            },
            'RestorableUntil': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    ACMPCA.Client.exceptions.ResourceNotFoundException
    ACMPCA.Client.exceptions.InvalidArnException
    
    """
    pass

def describe_certificate_authority_audit_report(CertificateAuthorityArn=None, AuditReportId=None):
    """
    Lists information about a specific audit report created by calling the  CreateCertificateAuthorityAuditReport action. Audit information is created every time the certificate authority (CA) private key is used. The private key is used when you call the  IssueCertificate action or the  RevokeCertificate action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_certificate_authority_audit_report(
        CertificateAuthorityArn='string',
        AuditReportId='string'
    )
    
    
    :type CertificateAuthorityArn: string
    :param CertificateAuthorityArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the private CA. This must be of the form:\n\n``arn:aws:acm-pca:region :account :certificate-authority/12345678-1234-1234-1234-123456789012 `` .\n

    :type AuditReportId: string
    :param AuditReportId: [REQUIRED]\nThe report ID returned by calling the CreateCertificateAuthorityAuditReport action.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AuditReportStatus': 'CREATING'|'SUCCESS'|'FAILED',
    'S3BucketName': 'string',
    'S3Key': 'string',
    'CreatedAt': datetime(2015, 1, 1)
}


Response Structure

(dict) --

AuditReportStatus (string) --
Specifies whether report creation is in progress, has succeeded, or has failed.

S3BucketName (string) --
Name of the S3 bucket that contains the report.

S3Key (string) --
S3 key that uniquely identifies the report file in your S3 bucket.

CreatedAt (datetime) --
The date and time at which the report was created.







Exceptions

ACMPCA.Client.exceptions.ResourceNotFoundException
ACMPCA.Client.exceptions.InvalidArnException
ACMPCA.Client.exceptions.InvalidArgsException


    :return: {
        'AuditReportStatus': 'CREATING'|'SUCCESS'|'FAILED',
        'S3BucketName': 'string',
        'S3Key': 'string',
        'CreatedAt': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    ACMPCA.Client.exceptions.ResourceNotFoundException
    ACMPCA.Client.exceptions.InvalidArnException
    ACMPCA.Client.exceptions.InvalidArgsException
    
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

def get_certificate(CertificateAuthorityArn=None, CertificateArn=None):
    """
    Retrieves a certificate from your private CA. The ARN of the certificate is returned when you call the  IssueCertificate action. You must specify both the ARN of your private CA and the ARN of the issued certificate when calling the GetCertificate action. You can retrieve the certificate if it is in the ISSUED state. You can call the  CreateCertificateAuthorityAuditReport action to create a report that contains information about all of the certificates issued and revoked by your private CA.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_certificate(
        CertificateAuthorityArn='string',
        CertificateArn='string'
    )
    
    
    :type CertificateAuthorityArn: string
    :param CertificateAuthorityArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that was returned when you called CreateCertificateAuthority . This must be of the form:\n\n``arn:aws:acm-pca:region :account :certificate-authority/12345678-1234-1234-1234-123456789012 `` .\n

    :type CertificateArn: string
    :param CertificateArn: [REQUIRED]\nThe ARN of the issued certificate. The ARN contains the certificate serial number and must be in the following form:\n\n``arn:aws:acm-pca:region :account :certificate-authority/12345678-1234-1234-1234-123456789012 /certificate/286535153982981100925020015808220737245 ``\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Certificate': 'string',
    'CertificateChain': 'string'
}


Response Structure

(dict) --

Certificate (string) --
The base64 PEM-encoded certificate specified by the CertificateArn parameter.

CertificateChain (string) --
The base64 PEM-encoded certificate chain that chains up to the on-premises root CA certificate that you used to sign your private CA certificate.







Exceptions

ACMPCA.Client.exceptions.RequestInProgressException
ACMPCA.Client.exceptions.RequestFailedException
ACMPCA.Client.exceptions.ResourceNotFoundException
ACMPCA.Client.exceptions.InvalidArnException
ACMPCA.Client.exceptions.InvalidStateException


    :return: {
        'Certificate': 'string',
        'CertificateChain': 'string'
    }
    
    
    :returns: 
    ACMPCA.Client.exceptions.RequestInProgressException
    ACMPCA.Client.exceptions.RequestFailedException
    ACMPCA.Client.exceptions.ResourceNotFoundException
    ACMPCA.Client.exceptions.InvalidArnException
    ACMPCA.Client.exceptions.InvalidStateException
    
    """
    pass

def get_certificate_authority_certificate(CertificateAuthorityArn=None):
    """
    Retrieves the certificate and certificate chain for your private certificate authority (CA). Both the certificate and the chain are base64 PEM-encoded. The chain does not include the CA certificate. Each certificate in the chain signs the one before it.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_certificate_authority_certificate(
        CertificateAuthorityArn='string'
    )
    
    
    :type CertificateAuthorityArn: string
    :param CertificateAuthorityArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of your private CA. This is of the form:\n\n``arn:aws:acm-pca:region :account :certificate-authority/12345678-1234-1234-1234-123456789012 `` .\n

    :rtype: dict
ReturnsResponse Syntax{
    'Certificate': 'string',
    'CertificateChain': 'string'
}


Response Structure

(dict) --
Certificate (string) --Base64-encoded certificate authority (CA) certificate.

CertificateChain (string) --Base64-encoded certificate chain that includes any intermediate certificates and chains up to root on-premises certificate that you used to sign your private CA certificate. The chain does not include your private CA certificate. If this is a root CA, the value will be null.






Exceptions

ACMPCA.Client.exceptions.ResourceNotFoundException
ACMPCA.Client.exceptions.InvalidStateException
ACMPCA.Client.exceptions.InvalidArnException


    :return: {
        'Certificate': 'string',
        'CertificateChain': 'string'
    }
    
    
    """
    pass

def get_certificate_authority_csr(CertificateAuthorityArn=None):
    """
    Retrieves the certificate signing request (CSR) for your private certificate authority (CA). The CSR is created when you call the  CreateCertificateAuthority action. Sign the CSR with your ACM Private CA-hosted or on-premises root or subordinate CA. Then import the signed certificate back into ACM Private CA by calling the  ImportCertificateAuthorityCertificate action. The CSR is returned as a base64 PEM-encoded string.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_certificate_authority_csr(
        CertificateAuthorityArn='string'
    )
    
    
    :type CertificateAuthorityArn: string
    :param CertificateAuthorityArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that was returned when you called the CreateCertificateAuthority action. This must be of the form:\n\n``arn:aws:acm-pca:region :account :certificate-authority/12345678-1234-1234-1234-123456789012 ``\n

    :rtype: dict
ReturnsResponse Syntax{
    'Csr': 'string'
}


Response Structure

(dict) --
Csr (string) --The base64 PEM-encoded certificate signing request (CSR) for your private CA certificate.






Exceptions

ACMPCA.Client.exceptions.RequestInProgressException
ACMPCA.Client.exceptions.RequestFailedException
ACMPCA.Client.exceptions.ResourceNotFoundException
ACMPCA.Client.exceptions.InvalidArnException
ACMPCA.Client.exceptions.InvalidStateException


    :return: {
        'Csr': 'string'
    }
    
    
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

def import_certificate_authority_certificate(CertificateAuthorityArn=None, Certificate=None, CertificateChain=None):
    """
    Imports a signed private CA certificate into ACM Private CA. This action is used when you are using a chain of trust whose root is located outside ACM Private CA. Before you can call this action, the following preparations must in place:
    The following requirements apply when you import a CA certificate.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.import_certificate_authority_certificate(
        CertificateAuthorityArn='string',
        Certificate=b'bytes',
        CertificateChain=b'bytes'
    )
    
    
    :type CertificateAuthorityArn: string
    :param CertificateAuthorityArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that was returned when you called CreateCertificateAuthority . This must be of the form:\n\n``arn:aws:acm-pca:region :account :certificate-authority/12345678-1234-1234-1234-123456789012 ``\n

    :type Certificate: bytes
    :param Certificate: [REQUIRED]\nThe PEM-encoded certificate for a private CA. This may be a self-signed certificate in the case of a root CA, or it may be signed by another CA that you control.\n

    :type CertificateChain: bytes
    :param CertificateChain: A PEM-encoded file that contains all of your certificates, other than the certificate you\'re importing, chaining up to your root CA. Your ACM Private CA-hosted or on-premises root certificate is the last in the chain, and each certificate in the chain signs the one preceding.\nThis parameter must be supplied when you import a subordinate CA. When you import a root CA, there is no chain.\n

    :returns: 
    You cannot import a non-self-signed certificate for use as a root CA.
    You cannot import a self-signed certificate for use as a subordinate CA.
    Your certificate chain must not include the private CA certificate that you are importing.
    Your ACM Private CA-hosted or on-premises CA certificate must be the last certificate in your chain. The subordinate certificate, if any, that your root CA signed must be next to last. The subordinate certificate signed by the preceding subordinate CA must come next, and so on until your chain is built.
    The chain must be PEM-encoded.
    
    """
    pass

def issue_certificate(CertificateAuthorityArn=None, Csr=None, SigningAlgorithm=None, TemplateArn=None, Validity=None, IdempotencyToken=None):
    """
    Uses your private certificate authority (CA) to issue a client certificate. This action returns the Amazon Resource Name (ARN) of the certificate. You can retrieve the certificate by calling the  GetCertificate action and specifying the ARN.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.issue_certificate(
        CertificateAuthorityArn='string',
        Csr=b'bytes',
        SigningAlgorithm='SHA256WITHECDSA'|'SHA384WITHECDSA'|'SHA512WITHECDSA'|'SHA256WITHRSA'|'SHA384WITHRSA'|'SHA512WITHRSA',
        TemplateArn='string',
        Validity={
            'Value': 123,
            'Type': 'END_DATE'|'ABSOLUTE'|'DAYS'|'MONTHS'|'YEARS'
        },
        IdempotencyToken='string'
    )
    
    
    :type CertificateAuthorityArn: string
    :param CertificateAuthorityArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that was returned when you called CreateCertificateAuthority . This must be of the form:\n\n``arn:aws:acm-pca:region :account :certificate-authority/12345678-1234-1234-1234-123456789012 ``\n

    :type Csr: bytes
    :param Csr: [REQUIRED]\nThe certificate signing request (CSR) for the certificate you want to issue. You can use the following OpenSSL command to create the CSR and a 2048 bit RSA private key.\n\nopenssl req -new -newkey rsa:2048 -days 365 -keyout private/test_cert_priv_key.pem -out csr/test_cert_.csr\nIf you have a configuration file, you can use the following OpenSSL command. The usr_cert block in the configuration file contains your X509 version 3 extensions.\n\nopenssl req -new -config openssl_rsa.cnf -extensions usr_cert -newkey rsa:2048 -days -365 -keyout private/test_cert_priv_key.pem -out csr/test_cert_.csr\n

    :type SigningAlgorithm: string
    :param SigningAlgorithm: [REQUIRED]\nThe name of the algorithm that will be used to sign the certificate to be issued.\n

    :type TemplateArn: string
    :param TemplateArn: Specifies a custom configuration template to use when issuing a certificate. If this parameter is not provided, ACM Private CA defaults to the EndEntityCertificate/V1 template.\nThe following service-owned TemplateArn values are supported by ACM Private CA:\n\narn:aws:acm-pca:::template/EndEntityCertificate/V1\narn:aws:acm-pca:::template/SubordinateCACertificate_PathLen0/V1\narn:aws:acm-pca:::template/SubordinateCACertificate_PathLen1/V1\narn:aws:acm-pca:::template/SubordinateCACertificate_PathLen2/V1\narn:aws:acm-pca:::template/SubordinateCACertificate_PathLen3/V1\narn:aws:acm-pca:::template/RootCACertificate/V1\n\nFor more information, see Using Templates .\n

    :type Validity: dict
    :param Validity: [REQUIRED]\nThe type of the validity period.\n\nValue (integer) -- [REQUIRED]Time period.\n\nType (string) -- [REQUIRED]Specifies whether the Value parameter represents days, months, or years.\n\n\n

    :type IdempotencyToken: string
    :param IdempotencyToken: Custom string that can be used to distinguish between calls to the IssueCertificate action. Idempotency tokens time out after one hour. Therefore, if you call IssueCertificate multiple times with the same idempotency token within 5 minutes, ACM Private CA recognizes that you are requesting only one certificate and will issue only one. If you change the idempotency token for each call, PCA recognizes that you are requesting multiple certificates.

    :rtype: dict

ReturnsResponse Syntax
{
    'CertificateArn': 'string'
}


Response Structure

(dict) --

CertificateArn (string) --
The Amazon Resource Name (ARN) of the issued certificate and the certificate serial number. This is of the form:

``arn:aws:acm-pca:region :account :certificate-authority/12345678-1234-1234-1234-123456789012 /certificate/286535153982981100925020015808220737245 ``








Exceptions

ACMPCA.Client.exceptions.LimitExceededException
ACMPCA.Client.exceptions.ResourceNotFoundException
ACMPCA.Client.exceptions.InvalidStateException
ACMPCA.Client.exceptions.InvalidArnException
ACMPCA.Client.exceptions.InvalidArgsException
ACMPCA.Client.exceptions.MalformedCSRException


    :return: {
        'CertificateArn': 'string'
    }
    
    
    :returns: 
    ACMPCA.Client.exceptions.LimitExceededException
    ACMPCA.Client.exceptions.ResourceNotFoundException
    ACMPCA.Client.exceptions.InvalidStateException
    ACMPCA.Client.exceptions.InvalidArnException
    ACMPCA.Client.exceptions.InvalidArgsException
    ACMPCA.Client.exceptions.MalformedCSRException
    
    """
    pass

def list_certificate_authorities(NextToken=None, MaxResults=None):
    """
    Lists the private certificate authorities that you created by using the  CreateCertificateAuthority action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_certificate_authorities(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of the NextToken parameter from the response you just received.

    :type MaxResults: integer
    :param MaxResults: Use this parameter when paginating results to specify the maximum number of items to return in the response on each page. If additional items exist beyond the number you specify, the NextToken element is sent in the response. Use this NextToken value in a subsequent request to retrieve additional items.

    :rtype: dict

ReturnsResponse Syntax
{
    'CertificateAuthorities': [
        {
            'Arn': 'string',
            'CreatedAt': datetime(2015, 1, 1),
            'LastStateChangeAt': datetime(2015, 1, 1),
            'Type': 'ROOT'|'SUBORDINATE',
            'Serial': 'string',
            'Status': 'CREATING'|'PENDING_CERTIFICATE'|'ACTIVE'|'DELETED'|'DISABLED'|'EXPIRED'|'FAILED',
            'NotBefore': datetime(2015, 1, 1),
            'NotAfter': datetime(2015, 1, 1),
            'FailureReason': 'REQUEST_TIMED_OUT'|'UNSUPPORTED_ALGORITHM'|'OTHER',
            'CertificateAuthorityConfiguration': {
                'KeyAlgorithm': 'RSA_2048'|'RSA_4096'|'EC_prime256v1'|'EC_secp384r1',
                'SigningAlgorithm': 'SHA256WITHECDSA'|'SHA384WITHECDSA'|'SHA512WITHECDSA'|'SHA256WITHRSA'|'SHA384WITHRSA'|'SHA512WITHRSA',
                'Subject': {
                    'Country': 'string',
                    'Organization': 'string',
                    'OrganizationalUnit': 'string',
                    'DistinguishedNameQualifier': 'string',
                    'State': 'string',
                    'CommonName': 'string',
                    'SerialNumber': 'string',
                    'Locality': 'string',
                    'Title': 'string',
                    'Surname': 'string',
                    'GivenName': 'string',
                    'Initials': 'string',
                    'Pseudonym': 'string',
                    'GenerationQualifier': 'string'
                }
            },
            'RevocationConfiguration': {
                'CrlConfiguration': {
                    'Enabled': True|False,
                    'ExpirationInDays': 123,
                    'CustomCname': 'string',
                    'S3BucketName': 'string'
                }
            },
            'RestorableUntil': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

CertificateAuthorities (list) --
Summary information about each certificate authority you have created.

(dict) --
Contains information about your private certificate authority (CA). Your private CA can issue and revoke X.509 digital certificates. Digital certificates verify that the entity named in the certificate Subject field owns or controls the public key contained in the Subject Public Key Info field. Call the  CreateCertificateAuthority action to create your private CA. You must then call the  GetCertificateAuthorityCertificate action to retrieve a private CA certificate signing request (CSR). Sign the CSR with your ACM Private CA-hosted or on-premises root or subordinate CA certificate. Call the  ImportCertificateAuthorityCertificate action to import the signed certificate into AWS Certificate Manager (ACM).

Arn (string) --
Amazon Resource Name (ARN) for your private certificate authority (CA). The format is `` 12345678-1234-1234-1234-123456789012 `` .

CreatedAt (datetime) --
Date and time at which your private CA was created.

LastStateChangeAt (datetime) --
Date and time at which your private CA was last updated.

Type (string) --
Type of your private CA.

Serial (string) --
Serial number of your private CA.

Status (string) --
Status of your private CA.

NotBefore (datetime) --
Date and time before which your private CA certificate is not valid.

NotAfter (datetime) --
Date and time after which your private CA certificate is not valid.

FailureReason (string) --
Reason the request to create your private CA failed.

CertificateAuthorityConfiguration (dict) --
Your private CA configuration.

KeyAlgorithm (string) --
Type of the public key algorithm and size, in bits, of the key pair that your CA creates when it issues a certificate. When you create a subordinate CA, you must use a key algorithm supported by the parent CA.

SigningAlgorithm (string) --
Name of the algorithm your private CA uses to sign certificate requests.

Subject (dict) --
Structure that contains X.500 distinguished name information for your private CA.

Country (string) --
Two-digit code that specifies the country in which the certificate subject located.

Organization (string) --
Legal name of the organization with which the certificate subject is affiliated.

OrganizationalUnit (string) --
A subdivision or unit of the organization (such as sales or finance) with which the certificate subject is affiliated.

DistinguishedNameQualifier (string) --
Disambiguating information for the certificate subject.

State (string) --
State in which the subject of the certificate is located.

CommonName (string) --
Fully qualified domain name (FQDN) associated with the certificate subject.

SerialNumber (string) --
The certificate serial number.

Locality (string) --
The locality (such as a city or town) in which the certificate subject is located.

Title (string) --
A title such as Mr. or Ms., which is pre-pended to the name to refer formally to the certificate subject.

Surname (string) --
Family name. In the US and the UK, for example, the surname of an individual is ordered last. In Asian cultures the surname is typically ordered first.

GivenName (string) --
First name.

Initials (string) --
Concatenation that typically contains the first letter of the GivenName , the first letter of the middle name if one exists, and the first letter of the SurName .

Pseudonym (string) --
Typically a shortened version of a longer GivenName . For example, Jonathan is often shortened to John. Elizabeth is often shortened to Beth, Liz, or Eliza.

GenerationQualifier (string) --
Typically a qualifier appended to the name of an individual. Examples include Jr. for junior, Sr. for senior, and III for third.





RevocationConfiguration (dict) --
Information about the certificate revocation list (CRL) created and maintained by your private CA.

CrlConfiguration (dict) --
Configuration of the certificate revocation list (CRL), if any, maintained by your private CA.

Enabled (boolean) --
Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. You can use this value to enable certificate revocation for a new CA when you call the  CreateCertificateAuthority action or for an existing CA when you call the  UpdateCertificateAuthority action.

ExpirationInDays (integer) --
Number of days until a certificate expires.

CustomCname (string) --
Name inserted into the certificate CRL Distribution Points extension that enables the use of an alias for the CRL distribution point. Use this value if you don\'t want the name of your S3 bucket to be public.

S3BucketName (string) --
Name of the S3 bucket that contains the CRL. If you do not provide a value for the CustomCname argument, the name of your S3 bucket is placed into the CRL Distribution Points extension of the issued certificate. You can change the name of your bucket by calling the  UpdateCertificateAuthority action. You must specify a bucket policy that allows ACM Private CA to write the CRL to your bucket.





RestorableUntil (datetime) --
The period during which a deleted CA can be restored. For more information, see the PermanentDeletionTimeInDays parameter of the  DeleteCertificateAuthorityRequest action.





NextToken (string) --
When the list is truncated, this value is present and should be used for the NextToken parameter in a subsequent pagination request.







Exceptions

ACMPCA.Client.exceptions.InvalidNextTokenException


    :return: {
        'CertificateAuthorities': [
            {
                'Arn': 'string',
                'CreatedAt': datetime(2015, 1, 1),
                'LastStateChangeAt': datetime(2015, 1, 1),
                'Type': 'ROOT'|'SUBORDINATE',
                'Serial': 'string',
                'Status': 'CREATING'|'PENDING_CERTIFICATE'|'ACTIVE'|'DELETED'|'DISABLED'|'EXPIRED'|'FAILED',
                'NotBefore': datetime(2015, 1, 1),
                'NotAfter': datetime(2015, 1, 1),
                'FailureReason': 'REQUEST_TIMED_OUT'|'UNSUPPORTED_ALGORITHM'|'OTHER',
                'CertificateAuthorityConfiguration': {
                    'KeyAlgorithm': 'RSA_2048'|'RSA_4096'|'EC_prime256v1'|'EC_secp384r1',
                    'SigningAlgorithm': 'SHA256WITHECDSA'|'SHA384WITHECDSA'|'SHA512WITHECDSA'|'SHA256WITHRSA'|'SHA384WITHRSA'|'SHA512WITHRSA',
                    'Subject': {
                        'Country': 'string',
                        'Organization': 'string',
                        'OrganizationalUnit': 'string',
                        'DistinguishedNameQualifier': 'string',
                        'State': 'string',
                        'CommonName': 'string',
                        'SerialNumber': 'string',
                        'Locality': 'string',
                        'Title': 'string',
                        'Surname': 'string',
                        'GivenName': 'string',
                        'Initials': 'string',
                        'Pseudonym': 'string',
                        'GenerationQualifier': 'string'
                    }
                },
                'RevocationConfiguration': {
                    'CrlConfiguration': {
                        'Enabled': True|False,
                        'ExpirationInDays': 123,
                        'CustomCname': 'string',
                        'S3BucketName': 'string'
                    }
                },
                'RestorableUntil': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ACMPCA.Client.exceptions.InvalidNextTokenException
    
    """
    pass

def list_permissions(CertificateAuthorityArn=None, NextToken=None, MaxResults=None):
    """
    Lists all the permissions, if any, that have been assigned by a private CA. Permissions can be granted with the  CreatePermission action and revoked with the  DeletePermission action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_permissions(
        CertificateAuthorityArn='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type CertificateAuthorityArn: string
    :param CertificateAuthorityArn: [REQUIRED]\nThe Amazon Resource Number (ARN) of the private CA to inspect. You can find the ARN by calling the ListCertificateAuthorities action. This must be of the form: arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012 You can get a private CA\'s ARN by running the ListCertificateAuthorities action.\n

    :type NextToken: string
    :param NextToken: When paginating results, use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of NextToken from the response you just received.

    :type MaxResults: integer
    :param MaxResults: When paginating results, use this parameter to specify the maximum number of items to return in the response. If additional items exist beyond the number you specify, the NextToken element is sent in the response. Use this NextToken value in a subsequent request to retrieve additional items.

    :rtype: dict

ReturnsResponse Syntax
{
    'Permissions': [
        {
            'CertificateAuthorityArn': 'string',
            'CreatedAt': datetime(2015, 1, 1),
            'Principal': 'string',
            'SourceAccount': 'string',
            'Actions': [
                'IssueCertificate'|'GetCertificate'|'ListPermissions',
            ],
            'Policy': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Permissions (list) --
Summary information about each permission assigned by the specified private CA, including the action enabled, the policy provided, and the time of creation.

(dict) --
Permissions designate which private CA actions can be performed by an AWS service or entity. In order for ACM to automatically renew private certificates, you must give the ACM service principal all available permissions (IssueCertificate , GetCertificate , and ListPermissions ). Permissions can be assigned with the  CreatePermission action, removed with the  DeletePermission action, and listed with the  ListPermissions action.

CertificateAuthorityArn (string) --
The Amazon Resource Number (ARN) of the private CA from which the permission was issued.

CreatedAt (datetime) --
The time at which the permission was created.

Principal (string) --
The AWS service or entity that holds the permission. At this time, the only valid principal is acm.amazonaws.com .

SourceAccount (string) --
The ID of the account that assigned the permission.

Actions (list) --
The private CA actions that can be performed by the designated AWS service.

(string) --


Policy (string) --
The name of the policy that is associated with the permission.





NextToken (string) --
When the list is truncated, this value is present and should be used for the NextToken parameter in a subsequent pagination request.







Exceptions

ACMPCA.Client.exceptions.ResourceNotFoundException
ACMPCA.Client.exceptions.InvalidArnException
ACMPCA.Client.exceptions.InvalidNextTokenException
ACMPCA.Client.exceptions.InvalidStateException
ACMPCA.Client.exceptions.RequestFailedException


    :return: {
        'Permissions': [
            {
                'CertificateAuthorityArn': 'string',
                'CreatedAt': datetime(2015, 1, 1),
                'Principal': 'string',
                'SourceAccount': 'string',
                'Actions': [
                    'IssueCertificate'|'GetCertificate'|'ListPermissions',
                ],
                'Policy': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_tags(CertificateAuthorityArn=None, NextToken=None, MaxResults=None):
    """
    Lists the tags, if any, that are associated with your private CA. Tags are labels that you can use to identify and organize your CAs. Each tag consists of a key and an optional value. Call the  TagCertificateAuthority action to add one or more tags to your CA. Call the  UntagCertificateAuthority action to remove tags.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags(
        CertificateAuthorityArn='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type CertificateAuthorityArn: string
    :param CertificateAuthorityArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that was returned when you called the CreateCertificateAuthority action. This must be of the form:\n\n``arn:aws:acm-pca:region :account :certificate-authority/12345678-1234-1234-1234-123456789012 ``\n

    :type NextToken: string
    :param NextToken: Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of NextToken from the response you just received.

    :type MaxResults: integer
    :param MaxResults: Use this parameter when paginating results to specify the maximum number of items to return in the response. If additional items exist beyond the number you specify, the NextToken element is sent in the response. Use this NextToken value in a subsequent request to retrieve additional items.

    :rtype: dict

ReturnsResponse Syntax
{
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Tags (list) --
The tags associated with your private CA.

(dict) --
Tags are labels that you can use to identify and organize your private CAs. Each tag consists of a key and an optional value. You can associate up to 50 tags with a private CA. To add one or more tags to a private CA, call the  TagCertificateAuthority action. To remove a tag, call the  UntagCertificateAuthority action.

Key (string) --
Key (name) of the tag.

Value (string) --
Value of the tag.





NextToken (string) --
When the list is truncated, this value is present and should be used for the NextToken parameter in a subsequent pagination request.







Exceptions

ACMPCA.Client.exceptions.ResourceNotFoundException
ACMPCA.Client.exceptions.InvalidArnException
ACMPCA.Client.exceptions.InvalidStateException


    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ACMPCA.Client.exceptions.ResourceNotFoundException
    ACMPCA.Client.exceptions.InvalidArnException
    ACMPCA.Client.exceptions.InvalidStateException
    
    """
    pass

def restore_certificate_authority(CertificateAuthorityArn=None):
    """
    Restores a certificate authority (CA) that is in the DELETED state. You can restore a CA during the period that you defined in the PermanentDeletionTimeInDays parameter of the  DeleteCertificateAuthority action. Currently, you can specify 7 to 30 days. If you did not specify a PermanentDeletionTimeInDays value, by default you can restore the CA at any time in a 30 day period. You can check the time remaining in the restoration period of a private CA in the DELETED state by calling the  DescribeCertificateAuthority or  ListCertificateAuthorities actions. The status of a restored CA is set to its pre-deletion status when the RestoreCertificateAuthority action returns. To change its status to ACTIVE , call the  UpdateCertificateAuthority action. If the private CA was in the PENDING_CERTIFICATE state at deletion, you must use the  ImportCertificateAuthorityCertificate action to import a certificate authority into the private CA before it can be activated. You cannot restore a CA after the restoration period has ended.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.restore_certificate_authority(
        CertificateAuthorityArn='string'
    )
    
    
    :type CertificateAuthorityArn: string
    :param CertificateAuthorityArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that was returned when you called the CreateCertificateAuthority action. This must be of the form:\n\n``arn:aws:acm-pca:region :account :certificate-authority/12345678-1234-1234-1234-123456789012 ``\n

    """
    pass

def revoke_certificate(CertificateAuthorityArn=None, CertificateSerial=None, RevocationReason=None):
    """
    Revokes a certificate that was issued inside ACM Private CA. If you enable a certificate revocation list (CRL) when you create or update your private CA, information about the revoked certificates will be included in the CRL. ACM Private CA writes the CRL to an S3 bucket that you specify. For more information about revocation, see the  CrlConfiguration structure. ACM Private CA also writes revocation information to the audit report. For more information, see  CreateCertificateAuthorityAuditReport .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.revoke_certificate(
        CertificateAuthorityArn='string',
        CertificateSerial='string',
        RevocationReason='UNSPECIFIED'|'KEY_COMPROMISE'|'CERTIFICATE_AUTHORITY_COMPROMISE'|'AFFILIATION_CHANGED'|'SUPERSEDED'|'CESSATION_OF_OPERATION'|'PRIVILEGE_WITHDRAWN'|'A_A_COMPROMISE'
    )
    
    
    :type CertificateAuthorityArn: string
    :param CertificateAuthorityArn: [REQUIRED]\nAmazon Resource Name (ARN) of the private CA that issued the certificate to be revoked. This must be of the form:\n\n``arn:aws:acm-pca:region :account :certificate-authority/12345678-1234-1234-1234-123456789012 ``\n

    :type CertificateSerial: string
    :param CertificateSerial: [REQUIRED]\nSerial number of the certificate to be revoked. This must be in hexadecimal format. You can retrieve the serial number by calling GetCertificate with the Amazon Resource Name (ARN) of the certificate you want and the ARN of your private CA. The GetCertificate action retrieves the certificate in the PEM format. You can use the following OpenSSL command to list the certificate in text format and copy the hexadecimal serial number.\n\nopenssl x509 -in *file_path* -text -noout\nYou can also copy the serial number from the console or use the DescribeCertificate action in the AWS Certificate Manager API Reference .\n

    :type RevocationReason: string
    :param RevocationReason: [REQUIRED]\nSpecifies why you revoked the certificate.\n

    :returns: 
    ACMPCA.Client.exceptions.ConcurrentModificationException
    ACMPCA.Client.exceptions.InvalidArnException
    ACMPCA.Client.exceptions.InvalidRequestException
    ACMPCA.Client.exceptions.InvalidStateException
    ACMPCA.Client.exceptions.LimitExceededException
    ACMPCA.Client.exceptions.ResourceNotFoundException
    ACMPCA.Client.exceptions.RequestAlreadyProcessedException
    ACMPCA.Client.exceptions.RequestInProgressException
    ACMPCA.Client.exceptions.RequestFailedException
    
    """
    pass

def tag_certificate_authority(CertificateAuthorityArn=None, Tags=None):
    """
    Adds one or more tags to your private CA. Tags are labels that you can use to identify and organize your AWS resources. Each tag consists of a key and an optional value. You specify the private CA on input by its Amazon Resource Name (ARN). You specify the tag by using a key-value pair. You can apply a tag to just one private CA if you want to identify a specific characteristic of that CA, or you can apply the same tag to multiple private CAs if you want to filter for a common relationship among those CAs. To remove one or more tags, use the  UntagCertificateAuthority action. Call the  ListTags action to see what tags are associated with your CA.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_certificate_authority(
        CertificateAuthorityArn='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type CertificateAuthorityArn: string
    :param CertificateAuthorityArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that was returned when you called CreateCertificateAuthority . This must be of the form:\n\n``arn:aws:acm-pca:region :account :certificate-authority/12345678-1234-1234-1234-123456789012 ``\n

    :type Tags: list
    :param Tags: [REQUIRED]\nList of tags to be associated with the CA.\n\n(dict) --Tags are labels that you can use to identify and organize your private CAs. Each tag consists of a key and an optional value. You can associate up to 50 tags with a private CA. To add one or more tags to a private CA, call the TagCertificateAuthority action. To remove a tag, call the UntagCertificateAuthority action.\n\nKey (string) -- [REQUIRED]Key (name) of the tag.\n\nValue (string) --Value of the tag.\n\n\n\n\n

    :returns: 
    ACMPCA.Client.exceptions.ResourceNotFoundException
    ACMPCA.Client.exceptions.InvalidArnException
    ACMPCA.Client.exceptions.InvalidStateException
    ACMPCA.Client.exceptions.InvalidTagException
    ACMPCA.Client.exceptions.TooManyTagsException
    
    """
    pass

def untag_certificate_authority(CertificateAuthorityArn=None, Tags=None):
    """
    Remove one or more tags from your private CA. A tag consists of a key-value pair. If you do not specify the value portion of the tag when calling this action, the tag will be removed regardless of value. If you specify a value, the tag is removed only if it is associated with the specified value. To add tags to a private CA, use the  TagCertificateAuthority . Call the  ListTags action to see what tags are associated with your CA.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_certificate_authority(
        CertificateAuthorityArn='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type CertificateAuthorityArn: string
    :param CertificateAuthorityArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that was returned when you called CreateCertificateAuthority . This must be of the form:\n\n``arn:aws:acm-pca:region :account :certificate-authority/12345678-1234-1234-1234-123456789012 ``\n

    :type Tags: list
    :param Tags: [REQUIRED]\nList of tags to be removed from the CA.\n\n(dict) --Tags are labels that you can use to identify and organize your private CAs. Each tag consists of a key and an optional value. You can associate up to 50 tags with a private CA. To add one or more tags to a private CA, call the TagCertificateAuthority action. To remove a tag, call the UntagCertificateAuthority action.\n\nKey (string) -- [REQUIRED]Key (name) of the tag.\n\nValue (string) --Value of the tag.\n\n\n\n\n

    :returns: 
    ACMPCA.Client.exceptions.ResourceNotFoundException
    ACMPCA.Client.exceptions.InvalidArnException
    ACMPCA.Client.exceptions.InvalidStateException
    ACMPCA.Client.exceptions.InvalidTagException
    
    """
    pass

def update_certificate_authority(CertificateAuthorityArn=None, RevocationConfiguration=None, Status=None):
    """
    Updates the status or configuration of a private certificate authority (CA). Your private CA must be in the ACTIVE or DISABLED state before you can update it. You can disable a private CA that is in the ACTIVE state or make a CA that is in the DISABLED state active again.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_certificate_authority(
        CertificateAuthorityArn='string',
        RevocationConfiguration={
            'CrlConfiguration': {
                'Enabled': True|False,
                'ExpirationInDays': 123,
                'CustomCname': 'string',
                'S3BucketName': 'string'
            }
        },
        Status='CREATING'|'PENDING_CERTIFICATE'|'ACTIVE'|'DELETED'|'DISABLED'|'EXPIRED'|'FAILED'
    )
    
    
    :type CertificateAuthorityArn: string
    :param CertificateAuthorityArn: [REQUIRED]\nAmazon Resource Name (ARN) of the private CA that issued the certificate to be revoked. This must be of the form:\n\n``arn:aws:acm-pca:region :account :certificate-authority/12345678-1234-1234-1234-123456789012 ``\n

    :type RevocationConfiguration: dict
    :param RevocationConfiguration: Revocation information for your private CA.\n\nCrlConfiguration (dict) --Configuration of the certificate revocation list (CRL), if any, maintained by your private CA.\n\nEnabled (boolean) -- [REQUIRED]Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. You can use this value to enable certificate revocation for a new CA when you call the CreateCertificateAuthority action or for an existing CA when you call the UpdateCertificateAuthority action.\n\nExpirationInDays (integer) --Number of days until a certificate expires.\n\nCustomCname (string) --Name inserted into the certificate CRL Distribution Points extension that enables the use of an alias for the CRL distribution point. Use this value if you don\'t want the name of your S3 bucket to be public.\n\nS3BucketName (string) --Name of the S3 bucket that contains the CRL. If you do not provide a value for the CustomCname argument, the name of your S3 bucket is placed into the CRL Distribution Points extension of the issued certificate. You can change the name of your bucket by calling the UpdateCertificateAuthority action. You must specify a bucket policy that allows ACM Private CA to write the CRL to your bucket.\n\n\n\n\n

    :type Status: string
    :param Status: Status of your private CA.

    :returns: 
    ACMPCA.Client.exceptions.ConcurrentModificationException
    ACMPCA.Client.exceptions.ResourceNotFoundException
    ACMPCA.Client.exceptions.InvalidArgsException
    ACMPCA.Client.exceptions.InvalidArnException
    ACMPCA.Client.exceptions.InvalidStateException
    ACMPCA.Client.exceptions.InvalidPolicyException
    
    """
    pass

