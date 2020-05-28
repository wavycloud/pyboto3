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

def associate_domain(FleetArn=None, DomainName=None, DisplayName=None, AcmCertificateArn=None):
    """
    Specifies a domain to be associated to Amazon WorkLink.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_domain(
        FleetArn='string',
        DomainName='string',
        DisplayName='string',
        AcmCertificateArn='string'
    )
    
    
    :type FleetArn: string
    :param FleetArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the fleet.\n

    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe fully qualified domain name (FQDN).\n

    :type DisplayName: string
    :param DisplayName: The name to display.

    :type AcmCertificateArn: string
    :param AcmCertificateArn: [REQUIRED]\nThe ARN of an issued ACM certificate that is valid for the domain being associated.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WorkLink.Client.exceptions.UnauthorizedException
WorkLink.Client.exceptions.InternalServerErrorException
WorkLink.Client.exceptions.InvalidRequestException
WorkLink.Client.exceptions.ResourceNotFoundException
WorkLink.Client.exceptions.ResourceAlreadyExistsException
WorkLink.Client.exceptions.TooManyRequestsException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def associate_website_authorization_provider(FleetArn=None, AuthorizationProviderType=None, DomainName=None):
    """
    Associates a website authorization provider with a specified fleet. This is used to authorize users against associated websites in the company network.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_website_authorization_provider(
        FleetArn='string',
        AuthorizationProviderType='SAML',
        DomainName='string'
    )
    
    
    :type FleetArn: string
    :param FleetArn: [REQUIRED]\nThe ARN of the fleet.\n

    :type AuthorizationProviderType: string
    :param AuthorizationProviderType: [REQUIRED]\nThe authorization provider type.\n

    :type DomainName: string
    :param DomainName: The domain name of the authorization provider. This applies only to SAML-based authorization providers.

    :rtype: dict

ReturnsResponse Syntax
{
    'AuthorizationProviderId': 'string'
}


Response Structure

(dict) --

AuthorizationProviderId (string) --
A unique identifier for the authorization provider.







Exceptions

WorkLink.Client.exceptions.UnauthorizedException
WorkLink.Client.exceptions.InternalServerErrorException
WorkLink.Client.exceptions.InvalidRequestException
WorkLink.Client.exceptions.ResourceNotFoundException
WorkLink.Client.exceptions.ResourceAlreadyExistsException
WorkLink.Client.exceptions.TooManyRequestsException


    :return: {
        'AuthorizationProviderId': 'string'
    }
    
    
    :returns: 
    WorkLink.Client.exceptions.UnauthorizedException
    WorkLink.Client.exceptions.InternalServerErrorException
    WorkLink.Client.exceptions.InvalidRequestException
    WorkLink.Client.exceptions.ResourceNotFoundException
    WorkLink.Client.exceptions.ResourceAlreadyExistsException
    WorkLink.Client.exceptions.TooManyRequestsException
    
    """
    pass

def associate_website_certificate_authority(FleetArn=None, Certificate=None, DisplayName=None):
    """
    Imports the root certificate of a certificate authority (CA) used to obtain TLS certificates used by associated websites within the company network.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_website_certificate_authority(
        FleetArn='string',
        Certificate='string',
        DisplayName='string'
    )
    
    
    :type FleetArn: string
    :param FleetArn: [REQUIRED]\nThe ARN of the fleet.\n

    :type Certificate: string
    :param Certificate: [REQUIRED]\nThe root certificate of the CA.\n

    :type DisplayName: string
    :param DisplayName: The certificate name to display.

    :rtype: dict

ReturnsResponse Syntax
{
    'WebsiteCaId': 'string'
}


Response Structure

(dict) --

WebsiteCaId (string) --
A unique identifier for the CA.







Exceptions

WorkLink.Client.exceptions.UnauthorizedException
WorkLink.Client.exceptions.InternalServerErrorException
WorkLink.Client.exceptions.InvalidRequestException
WorkLink.Client.exceptions.ResourceNotFoundException
WorkLink.Client.exceptions.ResourceAlreadyExistsException
WorkLink.Client.exceptions.TooManyRequestsException


    :return: {
        'WebsiteCaId': 'string'
    }
    
    
    :returns: 
    WorkLink.Client.exceptions.UnauthorizedException
    WorkLink.Client.exceptions.InternalServerErrorException
    WorkLink.Client.exceptions.InvalidRequestException
    WorkLink.Client.exceptions.ResourceNotFoundException
    WorkLink.Client.exceptions.ResourceAlreadyExistsException
    WorkLink.Client.exceptions.TooManyRequestsException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_fleet(FleetName=None, DisplayName=None, OptimizeForEndUserLocation=None):
    """
    Creates a fleet. A fleet consists of resources and the configuration that delivers associated websites to authorized users who download and set up the Amazon WorkLink app.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_fleet(
        FleetName='string',
        DisplayName='string',
        OptimizeForEndUserLocation=True|False
    )
    
    
    :type FleetName: string
    :param FleetName: [REQUIRED]\nA unique name for the fleet.\n

    :type DisplayName: string
    :param DisplayName: The fleet name to display.

    :type OptimizeForEndUserLocation: boolean
    :param OptimizeForEndUserLocation: The option to optimize for better performance by routing traffic through the closest AWS Region to users, which may be outside of your home Region.

    :rtype: dict

ReturnsResponse Syntax
{
    'FleetArn': 'string'
}


Response Structure

(dict) --

FleetArn (string) --
The ARN of the fleet.







Exceptions

WorkLink.Client.exceptions.UnauthorizedException
WorkLink.Client.exceptions.InternalServerErrorException
WorkLink.Client.exceptions.InvalidRequestException
WorkLink.Client.exceptions.ResourceNotFoundException
WorkLink.Client.exceptions.ResourceAlreadyExistsException
WorkLink.Client.exceptions.TooManyRequestsException


    :return: {
        'FleetArn': 'string'
    }
    
    
    :returns: 
    WorkLink.Client.exceptions.UnauthorizedException
    WorkLink.Client.exceptions.InternalServerErrorException
    WorkLink.Client.exceptions.InvalidRequestException
    WorkLink.Client.exceptions.ResourceNotFoundException
    WorkLink.Client.exceptions.ResourceAlreadyExistsException
    WorkLink.Client.exceptions.TooManyRequestsException
    
    """
    pass

def delete_fleet(FleetArn=None):
    """
    Deletes a fleet. Prevents users from accessing previously associated websites.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_fleet(
        FleetArn='string'
    )
    
    
    :type FleetArn: string
    :param FleetArn: [REQUIRED]\nThe ARN of the fleet.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

WorkLink.Client.exceptions.UnauthorizedException
WorkLink.Client.exceptions.InternalServerErrorException
WorkLink.Client.exceptions.InvalidRequestException
WorkLink.Client.exceptions.ResourceNotFoundException
WorkLink.Client.exceptions.TooManyRequestsException


    :return: {}
    
    
    :returns: 
    WorkLink.Client.exceptions.UnauthorizedException
    WorkLink.Client.exceptions.InternalServerErrorException
    WorkLink.Client.exceptions.InvalidRequestException
    WorkLink.Client.exceptions.ResourceNotFoundException
    WorkLink.Client.exceptions.TooManyRequestsException
    
    """
    pass

def describe_audit_stream_configuration(FleetArn=None):
    """
    Describes the configuration for delivering audit streams to the customer account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_audit_stream_configuration(
        FleetArn='string'
    )
    
    
    :type FleetArn: string
    :param FleetArn: [REQUIRED]\nThe ARN of the fleet.\n

    :rtype: dict
ReturnsResponse Syntax{
    'AuditStreamArn': 'string'
}


Response Structure

(dict) --
AuditStreamArn (string) --The ARN of the Amazon Kinesis data stream that will receive the audit events.






Exceptions

WorkLink.Client.exceptions.UnauthorizedException
WorkLink.Client.exceptions.InternalServerErrorException
WorkLink.Client.exceptions.InvalidRequestException
WorkLink.Client.exceptions.ResourceNotFoundException
WorkLink.Client.exceptions.TooManyRequestsException


    :return: {
        'AuditStreamArn': 'string'
    }
    
    
    """
    pass

def describe_company_network_configuration(FleetArn=None):
    """
    Describes the networking configuration to access the internal websites associated with the specified fleet.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_company_network_configuration(
        FleetArn='string'
    )
    
    
    :type FleetArn: string
    :param FleetArn: [REQUIRED]\nThe ARN of the fleet.\n

    :rtype: dict
ReturnsResponse Syntax{
    'VpcId': 'string',
    'SubnetIds': [
        'string',
    ],
    'SecurityGroupIds': [
        'string',
    ]
}


Response Structure

(dict) --
VpcId (string) --The VPC with connectivity to associated websites.

SubnetIds (list) --The subnets used for X-ENI connections from Amazon WorkLink rendering containers.

(string) --


SecurityGroupIds (list) --The security groups associated with access to the provided subnets.

(string) --







Exceptions

WorkLink.Client.exceptions.UnauthorizedException
WorkLink.Client.exceptions.InternalServerErrorException
WorkLink.Client.exceptions.InvalidRequestException
WorkLink.Client.exceptions.ResourceNotFoundException
WorkLink.Client.exceptions.TooManyRequestsException


    :return: {
        'VpcId': 'string',
        'SubnetIds': [
            'string',
        ],
        'SecurityGroupIds': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_device(FleetArn=None, DeviceId=None):
    """
    Provides information about a user\'s device.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_device(
        FleetArn='string',
        DeviceId='string'
    )
    
    
    :type FleetArn: string
    :param FleetArn: [REQUIRED]\nThe ARN of the fleet.\n

    :type DeviceId: string
    :param DeviceId: [REQUIRED]\nA unique identifier for a registered user\'s device.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Status': 'ACTIVE'|'SIGNED_OUT',
    'Model': 'string',
    'Manufacturer': 'string',
    'OperatingSystem': 'string',
    'OperatingSystemVersion': 'string',
    'PatchLevel': 'string',
    'FirstAccessedTime': datetime(2015, 1, 1),
    'LastAccessedTime': datetime(2015, 1, 1),
    'Username': 'string'
}


Response Structure

(dict) --

Status (string) --
The current state of the device.

Model (string) --
The model of the device.

Manufacturer (string) --
The manufacturer of the device.

OperatingSystem (string) --
The operating system of the device.

OperatingSystemVersion (string) --
The operating system version of the device.

PatchLevel (string) --
The operating system patch level of the device.

FirstAccessedTime (datetime) --
The date that the device first signed in to Amazon WorkLink.

LastAccessedTime (datetime) --
The date that the device last accessed Amazon WorkLink.

Username (string) --
The user name associated with the device.







Exceptions

WorkLink.Client.exceptions.UnauthorizedException
WorkLink.Client.exceptions.InternalServerErrorException
WorkLink.Client.exceptions.InvalidRequestException
WorkLink.Client.exceptions.ResourceNotFoundException
WorkLink.Client.exceptions.TooManyRequestsException


    :return: {
        'Status': 'ACTIVE'|'SIGNED_OUT',
        'Model': 'string',
        'Manufacturer': 'string',
        'OperatingSystem': 'string',
        'OperatingSystemVersion': 'string',
        'PatchLevel': 'string',
        'FirstAccessedTime': datetime(2015, 1, 1),
        'LastAccessedTime': datetime(2015, 1, 1),
        'Username': 'string'
    }
    
    
    :returns: 
    WorkLink.Client.exceptions.UnauthorizedException
    WorkLink.Client.exceptions.InternalServerErrorException
    WorkLink.Client.exceptions.InvalidRequestException
    WorkLink.Client.exceptions.ResourceNotFoundException
    WorkLink.Client.exceptions.TooManyRequestsException
    
    """
    pass

def describe_device_policy_configuration(FleetArn=None):
    """
    Describes the device policy configuration for the specified fleet.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_device_policy_configuration(
        FleetArn='string'
    )
    
    
    :type FleetArn: string
    :param FleetArn: [REQUIRED]\nThe ARN of the fleet.\n

    :rtype: dict
ReturnsResponse Syntax{
    'DeviceCaCertificate': 'string'
}


Response Structure

(dict) --
DeviceCaCertificate (string) --The certificate chain, including intermediate certificates and the root certificate authority certificate used to issue device certificates.






Exceptions

WorkLink.Client.exceptions.UnauthorizedException
WorkLink.Client.exceptions.InternalServerErrorException
WorkLink.Client.exceptions.InvalidRequestException
WorkLink.Client.exceptions.ResourceNotFoundException
WorkLink.Client.exceptions.TooManyRequestsException


    :return: {
        'DeviceCaCertificate': 'string'
    }
    
    
    """
    pass

def describe_domain(FleetArn=None, DomainName=None):
    """
    Provides information about the domain.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_domain(
        FleetArn='string',
        DomainName='string'
    )
    
    
    :type FleetArn: string
    :param FleetArn: [REQUIRED]\nThe ARN of the fleet.\n

    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe name of the domain.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DomainName': 'string',
    'DisplayName': 'string',
    'CreatedTime': datetime(2015, 1, 1),
    'DomainStatus': 'PENDING_VALIDATION'|'ASSOCIATING'|'ACTIVE'|'INACTIVE'|'DISASSOCIATING'|'DISASSOCIATED'|'FAILED_TO_ASSOCIATE'|'FAILED_TO_DISASSOCIATE',
    'AcmCertificateArn': 'string'
}


Response Structure

(dict) --

DomainName (string) --
The name of the domain.

DisplayName (string) --
The name to display.

CreatedTime (datetime) --
The time that the domain was added.

DomainStatus (string) --
The current state for the domain.

AcmCertificateArn (string) --
The ARN of an issued ACM certificate that is valid for the domain being associated.







Exceptions

WorkLink.Client.exceptions.UnauthorizedException
WorkLink.Client.exceptions.InternalServerErrorException
WorkLink.Client.exceptions.InvalidRequestException
WorkLink.Client.exceptions.ResourceNotFoundException
WorkLink.Client.exceptions.TooManyRequestsException


    :return: {
        'DomainName': 'string',
        'DisplayName': 'string',
        'CreatedTime': datetime(2015, 1, 1),
        'DomainStatus': 'PENDING_VALIDATION'|'ASSOCIATING'|'ACTIVE'|'INACTIVE'|'DISASSOCIATING'|'DISASSOCIATED'|'FAILED_TO_ASSOCIATE'|'FAILED_TO_DISASSOCIATE',
        'AcmCertificateArn': 'string'
    }
    
    
    :returns: 
    WorkLink.Client.exceptions.UnauthorizedException
    WorkLink.Client.exceptions.InternalServerErrorException
    WorkLink.Client.exceptions.InvalidRequestException
    WorkLink.Client.exceptions.ResourceNotFoundException
    WorkLink.Client.exceptions.TooManyRequestsException
    
    """
    pass

def describe_fleet_metadata(FleetArn=None):
    """
    Provides basic information for the specified fleet, excluding identity provider, networking, and device configuration details.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_fleet_metadata(
        FleetArn='string'
    )
    
    
    :type FleetArn: string
    :param FleetArn: [REQUIRED]\nThe ARN of the fleet.\n

    :rtype: dict
ReturnsResponse Syntax{
    'CreatedTime': datetime(2015, 1, 1),
    'LastUpdatedTime': datetime(2015, 1, 1),
    'FleetName': 'string',
    'DisplayName': 'string',
    'OptimizeForEndUserLocation': True|False,
    'CompanyCode': 'string',
    'FleetStatus': 'CREATING'|'ACTIVE'|'DELETING'|'DELETED'|'FAILED_TO_CREATE'|'FAILED_TO_DELETE'
}


Response Structure

(dict) --
CreatedTime (datetime) --The time that the fleet was created.

LastUpdatedTime (datetime) --The time that the fleet was last updated.

FleetName (string) --The name of the fleet.

DisplayName (string) --The name to display.

OptimizeForEndUserLocation (boolean) --The option to optimize for better performance by routing traffic through the closest AWS Region to users, which may be outside of your home Region.

CompanyCode (string) --The identifier used by users to sign in to the Amazon WorkLink app.

FleetStatus (string) --The current state of the fleet.






Exceptions

WorkLink.Client.exceptions.UnauthorizedException
WorkLink.Client.exceptions.InternalServerErrorException
WorkLink.Client.exceptions.InvalidRequestException
WorkLink.Client.exceptions.ResourceNotFoundException
WorkLink.Client.exceptions.TooManyRequestsException


    :return: {
        'CreatedTime': datetime(2015, 1, 1),
        'LastUpdatedTime': datetime(2015, 1, 1),
        'FleetName': 'string',
        'DisplayName': 'string',
        'OptimizeForEndUserLocation': True|False,
        'CompanyCode': 'string',
        'FleetStatus': 'CREATING'|'ACTIVE'|'DELETING'|'DELETED'|'FAILED_TO_CREATE'|'FAILED_TO_DELETE'
    }
    
    
    """
    pass

def describe_identity_provider_configuration(FleetArn=None):
    """
    Describes the identity provider configuration of the specified fleet.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_identity_provider_configuration(
        FleetArn='string'
    )
    
    
    :type FleetArn: string
    :param FleetArn: [REQUIRED]\nThe ARN of the fleet.\n

    :rtype: dict
ReturnsResponse Syntax{
    'IdentityProviderType': 'SAML',
    'ServiceProviderSamlMetadata': 'string',
    'IdentityProviderSamlMetadata': 'string'
}


Response Structure

(dict) --
IdentityProviderType (string) --The type of identity provider.

ServiceProviderSamlMetadata (string) --The SAML metadata document uploaded to the user\xe2\x80\x99s identity provider.

IdentityProviderSamlMetadata (string) --The SAML metadata document provided by the user\xe2\x80\x99s identity provider.






Exceptions

WorkLink.Client.exceptions.UnauthorizedException
WorkLink.Client.exceptions.InternalServerErrorException
WorkLink.Client.exceptions.InvalidRequestException
WorkLink.Client.exceptions.ResourceNotFoundException
WorkLink.Client.exceptions.TooManyRequestsException


    :return: {
        'IdentityProviderType': 'SAML',
        'ServiceProviderSamlMetadata': 'string',
        'IdentityProviderSamlMetadata': 'string'
    }
    
    
    """
    pass

def describe_website_certificate_authority(FleetArn=None, WebsiteCaId=None):
    """
    Provides information about the certificate authority.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_website_certificate_authority(
        FleetArn='string',
        WebsiteCaId='string'
    )
    
    
    :type FleetArn: string
    :param FleetArn: [REQUIRED]\nThe ARN of the fleet.\n

    :type WebsiteCaId: string
    :param WebsiteCaId: [REQUIRED]\nA unique identifier for the certificate authority.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Certificate': 'string',
    'CreatedTime': datetime(2015, 1, 1),
    'DisplayName': 'string'
}


Response Structure

(dict) --

Certificate (string) --
The root certificate of the certificate authority.

CreatedTime (datetime) --
The time that the certificate authority was added.

DisplayName (string) --
The certificate name to display.







Exceptions

WorkLink.Client.exceptions.UnauthorizedException
WorkLink.Client.exceptions.InternalServerErrorException
WorkLink.Client.exceptions.InvalidRequestException
WorkLink.Client.exceptions.ResourceNotFoundException
WorkLink.Client.exceptions.TooManyRequestsException


    :return: {
        'Certificate': 'string',
        'CreatedTime': datetime(2015, 1, 1),
        'DisplayName': 'string'
    }
    
    
    :returns: 
    WorkLink.Client.exceptions.UnauthorizedException
    WorkLink.Client.exceptions.InternalServerErrorException
    WorkLink.Client.exceptions.InvalidRequestException
    WorkLink.Client.exceptions.ResourceNotFoundException
    WorkLink.Client.exceptions.TooManyRequestsException
    
    """
    pass

def disassociate_domain(FleetArn=None, DomainName=None):
    """
    Disassociates a domain from Amazon WorkLink. End users lose the ability to access the domain with Amazon WorkLink.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_domain(
        FleetArn='string',
        DomainName='string'
    )
    
    
    :type FleetArn: string
    :param FleetArn: [REQUIRED]\nThe ARN of the fleet.\n

    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe name of the domain.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WorkLink.Client.exceptions.UnauthorizedException
WorkLink.Client.exceptions.InternalServerErrorException
WorkLink.Client.exceptions.InvalidRequestException
WorkLink.Client.exceptions.ResourceNotFoundException
WorkLink.Client.exceptions.TooManyRequestsException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def disassociate_website_authorization_provider(FleetArn=None, AuthorizationProviderId=None):
    """
    Disassociates a website authorization provider from a specified fleet. After the disassociation, users can\'t load any associated websites that require this authorization provider.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_website_authorization_provider(
        FleetArn='string',
        AuthorizationProviderId='string'
    )
    
    
    :type FleetArn: string
    :param FleetArn: [REQUIRED]\nThe ARN of the fleet.\n

    :type AuthorizationProviderId: string
    :param AuthorizationProviderId: [REQUIRED]\nA unique identifier for the authorization provider.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WorkLink.Client.exceptions.UnauthorizedException
WorkLink.Client.exceptions.InternalServerErrorException
WorkLink.Client.exceptions.InvalidRequestException
WorkLink.Client.exceptions.ResourceNotFoundException
WorkLink.Client.exceptions.ResourceAlreadyExistsException
WorkLink.Client.exceptions.TooManyRequestsException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def disassociate_website_certificate_authority(FleetArn=None, WebsiteCaId=None):
    """
    Removes a certificate authority (CA).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_website_certificate_authority(
        FleetArn='string',
        WebsiteCaId='string'
    )
    
    
    :type FleetArn: string
    :param FleetArn: [REQUIRED]\nThe ARN of the fleet.\n

    :type WebsiteCaId: string
    :param WebsiteCaId: [REQUIRED]\nA unique identifier for the CA.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WorkLink.Client.exceptions.UnauthorizedException
WorkLink.Client.exceptions.InternalServerErrorException
WorkLink.Client.exceptions.InvalidRequestException
WorkLink.Client.exceptions.ResourceNotFoundException
WorkLink.Client.exceptions.TooManyRequestsException


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

def list_devices(FleetArn=None, NextToken=None, MaxResults=None):
    """
    Retrieves a list of devices registered with the specified fleet.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_devices(
        FleetArn='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type FleetArn: string
    :param FleetArn: [REQUIRED]\nThe ARN of the fleet.\n

    :type NextToken: string
    :param NextToken: The pagination token used to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be included in the next page.

    :rtype: dict

ReturnsResponse Syntax
{
    'Devices': [
        {
            'DeviceId': 'string',
            'DeviceStatus': 'ACTIVE'|'SIGNED_OUT'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Devices (list) --
Information about the devices.

(dict) --
The summary of devices.

DeviceId (string) --
The ID of the device.

DeviceStatus (string) --
The status of the device.





NextToken (string) --
The pagination token used to retrieve the next page of results for this operation. If there are no more pages, this value is null.







Exceptions

WorkLink.Client.exceptions.UnauthorizedException
WorkLink.Client.exceptions.InternalServerErrorException
WorkLink.Client.exceptions.InvalidRequestException
WorkLink.Client.exceptions.ResourceNotFoundException
WorkLink.Client.exceptions.TooManyRequestsException


    :return: {
        'Devices': [
            {
                'DeviceId': 'string',
                'DeviceStatus': 'ACTIVE'|'SIGNED_OUT'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    WorkLink.Client.exceptions.UnauthorizedException
    WorkLink.Client.exceptions.InternalServerErrorException
    WorkLink.Client.exceptions.InvalidRequestException
    WorkLink.Client.exceptions.ResourceNotFoundException
    WorkLink.Client.exceptions.TooManyRequestsException
    
    """
    pass

def list_domains(FleetArn=None, NextToken=None, MaxResults=None):
    """
    Retrieves a list of domains associated to a specified fleet.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_domains(
        FleetArn='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type FleetArn: string
    :param FleetArn: [REQUIRED]\nThe ARN of the fleet.\n

    :type NextToken: string
    :param NextToken: The pagination token used to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be included in the next page.

    :rtype: dict

ReturnsResponse Syntax
{
    'Domains': [
        {
            'DomainName': 'string',
            'DisplayName': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'DomainStatus': 'PENDING_VALIDATION'|'ASSOCIATING'|'ACTIVE'|'INACTIVE'|'DISASSOCIATING'|'DISASSOCIATED'|'FAILED_TO_ASSOCIATE'|'FAILED_TO_DISASSOCIATE'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Domains (list) --
Information about the domains.

(dict) --
The summary of the domain.

DomainName (string) --
The name of the domain.

DisplayName (string) --
The name to display.

CreatedTime (datetime) --
The time that the domain was created.

DomainStatus (string) --
The status of the domain.





NextToken (string) --
The pagination token used to retrieve the next page of results for this operation. If there are no more pages, this value is null.







Exceptions

WorkLink.Client.exceptions.UnauthorizedException
WorkLink.Client.exceptions.InternalServerErrorException
WorkLink.Client.exceptions.InvalidRequestException
WorkLink.Client.exceptions.TooManyRequestsException


    :return: {
        'Domains': [
            {
                'DomainName': 'string',
                'DisplayName': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'DomainStatus': 'PENDING_VALIDATION'|'ASSOCIATING'|'ACTIVE'|'INACTIVE'|'DISASSOCIATING'|'DISASSOCIATED'|'FAILED_TO_ASSOCIATE'|'FAILED_TO_DISASSOCIATE'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    WorkLink.Client.exceptions.UnauthorizedException
    WorkLink.Client.exceptions.InternalServerErrorException
    WorkLink.Client.exceptions.InvalidRequestException
    WorkLink.Client.exceptions.TooManyRequestsException
    
    """
    pass

def list_fleets(NextToken=None, MaxResults=None):
    """
    Retrieves a list of fleets for the current account and Region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_fleets(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: The pagination token used to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be included in the next page.

    :rtype: dict

ReturnsResponse Syntax
{
    'FleetSummaryList': [
        {
            'FleetArn': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'LastUpdatedTime': datetime(2015, 1, 1),
            'FleetName': 'string',
            'DisplayName': 'string',
            'CompanyCode': 'string',
            'FleetStatus': 'CREATING'|'ACTIVE'|'DELETING'|'DELETED'|'FAILED_TO_CREATE'|'FAILED_TO_DELETE'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

FleetSummaryList (list) --
The summary list of the fleets.

(dict) --
The summary of the fleet.

FleetArn (string) --
The ARN of the fleet.

CreatedTime (datetime) --
The time when the fleet was created.

LastUpdatedTime (datetime) --
The time when the fleet was last updated.

FleetName (string) --
The name of the fleet.

DisplayName (string) --
The name to display.

CompanyCode (string) --
The identifier used by users to sign into the Amazon WorkLink app.

FleetStatus (string) --
The status of the fleet.





NextToken (string) --
The pagination token used to retrieve the next page of results for this operation. If there are no more pages, this value is null.







Exceptions

WorkLink.Client.exceptions.UnauthorizedException
WorkLink.Client.exceptions.InternalServerErrorException
WorkLink.Client.exceptions.InvalidRequestException
WorkLink.Client.exceptions.TooManyRequestsException


    :return: {
        'FleetSummaryList': [
            {
                'FleetArn': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'LastUpdatedTime': datetime(2015, 1, 1),
                'FleetName': 'string',
                'DisplayName': 'string',
                'CompanyCode': 'string',
                'FleetStatus': 'CREATING'|'ACTIVE'|'DELETING'|'DELETED'|'FAILED_TO_CREATE'|'FAILED_TO_DELETE'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    WorkLink.Client.exceptions.UnauthorizedException
    WorkLink.Client.exceptions.InternalServerErrorException
    WorkLink.Client.exceptions.InvalidRequestException
    WorkLink.Client.exceptions.TooManyRequestsException
    
    """
    pass

def list_website_authorization_providers(FleetArn=None, NextToken=None, MaxResults=None):
    """
    Retrieves a list of website authorization providers associated with a specified fleet.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_website_authorization_providers(
        FleetArn='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type FleetArn: string
    :param FleetArn: [REQUIRED]\nThe ARN of the fleet.\n

    :type NextToken: string
    :param NextToken: The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be included in the next page.

    :rtype: dict

ReturnsResponse Syntax
{
    'WebsiteAuthorizationProviders': [
        {
            'AuthorizationProviderId': 'string',
            'AuthorizationProviderType': 'SAML',
            'DomainName': 'string',
            'CreatedTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

WebsiteAuthorizationProviders (list) --
The website authorization providers.

(dict) --
The summary of the website authorization provider.

AuthorizationProviderId (string) --
A unique identifier for the authorization provider.

AuthorizationProviderType (string) --
The authorization provider type.

DomainName (string) --
The domain name of the authorization provider. This applies only to SAML-based authorization providers.

CreatedTime (datetime) --
The time of creation.





NextToken (string) --
The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.







Exceptions

WorkLink.Client.exceptions.UnauthorizedException
WorkLink.Client.exceptions.InternalServerErrorException
WorkLink.Client.exceptions.InvalidRequestException
WorkLink.Client.exceptions.ResourceNotFoundException
WorkLink.Client.exceptions.TooManyRequestsException


    :return: {
        'WebsiteAuthorizationProviders': [
            {
                'AuthorizationProviderId': 'string',
                'AuthorizationProviderType': 'SAML',
                'DomainName': 'string',
                'CreatedTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    WorkLink.Client.exceptions.UnauthorizedException
    WorkLink.Client.exceptions.InternalServerErrorException
    WorkLink.Client.exceptions.InvalidRequestException
    WorkLink.Client.exceptions.ResourceNotFoundException
    WorkLink.Client.exceptions.TooManyRequestsException
    
    """
    pass

def list_website_certificate_authorities(FleetArn=None, MaxResults=None, NextToken=None):
    """
    Retrieves a list of certificate authorities added for the current account and Region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_website_certificate_authorities(
        FleetArn='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type FleetArn: string
    :param FleetArn: [REQUIRED]\nThe ARN of the fleet.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be included in the next page.

    :type NextToken: string
    :param NextToken: The pagination token used to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

    :rtype: dict

ReturnsResponse Syntax
{
    'WebsiteCertificateAuthorities': [
        {
            'WebsiteCaId': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'DisplayName': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

WebsiteCertificateAuthorities (list) --
Information about the certificates.

(dict) --
The summary of the certificate authority (CA).

WebsiteCaId (string) --
A unique identifier for the CA.

CreatedTime (datetime) --
The time when the CA was added.

DisplayName (string) --
The name to display.





NextToken (string) --
The pagination token used to retrieve the next page of results for this operation. If there are no more pages, this value is null.







Exceptions

WorkLink.Client.exceptions.UnauthorizedException
WorkLink.Client.exceptions.InternalServerErrorException
WorkLink.Client.exceptions.InvalidRequestException
WorkLink.Client.exceptions.TooManyRequestsException


    :return: {
        'WebsiteCertificateAuthorities': [
            {
                'WebsiteCaId': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'DisplayName': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    WorkLink.Client.exceptions.UnauthorizedException
    WorkLink.Client.exceptions.InternalServerErrorException
    WorkLink.Client.exceptions.InvalidRequestException
    WorkLink.Client.exceptions.TooManyRequestsException
    
    """
    pass

def restore_domain_access(FleetArn=None, DomainName=None):
    """
    Moves a domain to ACTIVE status if it was in the INACTIVE status.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.restore_domain_access(
        FleetArn='string',
        DomainName='string'
    )
    
    
    :type FleetArn: string
    :param FleetArn: [REQUIRED]\nThe ARN of the fleet.\n

    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe name of the domain.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WorkLink.Client.exceptions.UnauthorizedException
WorkLink.Client.exceptions.InternalServerErrorException
WorkLink.Client.exceptions.InvalidRequestException
WorkLink.Client.exceptions.ResourceNotFoundException
WorkLink.Client.exceptions.TooManyRequestsException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def revoke_domain_access(FleetArn=None, DomainName=None):
    """
    Moves a domain to INACTIVE status if it was in the ACTIVE status.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.revoke_domain_access(
        FleetArn='string',
        DomainName='string'
    )
    
    
    :type FleetArn: string
    :param FleetArn: [REQUIRED]\nThe ARN of the fleet.\n

    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe name of the domain.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WorkLink.Client.exceptions.UnauthorizedException
WorkLink.Client.exceptions.InternalServerErrorException
WorkLink.Client.exceptions.InvalidRequestException
WorkLink.Client.exceptions.ResourceNotFoundException
WorkLink.Client.exceptions.TooManyRequestsException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def sign_out_user(FleetArn=None, Username=None):
    """
    Signs the user out from all of their devices. The user can sign in again if they have valid credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.sign_out_user(
        FleetArn='string',
        Username='string'
    )
    
    
    :type FleetArn: string
    :param FleetArn: [REQUIRED]\nThe ARN of the fleet.\n

    :type Username: string
    :param Username: [REQUIRED]\nThe name of the user.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WorkLink.Client.exceptions.UnauthorizedException
WorkLink.Client.exceptions.InternalServerErrorException
WorkLink.Client.exceptions.InvalidRequestException
WorkLink.Client.exceptions.ResourceNotFoundException
WorkLink.Client.exceptions.TooManyRequestsException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_audit_stream_configuration(FleetArn=None, AuditStreamArn=None):
    """
    Updates the audit stream configuration for the fleet.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_audit_stream_configuration(
        FleetArn='string',
        AuditStreamArn='string'
    )
    
    
    :type FleetArn: string
    :param FleetArn: [REQUIRED]\nThe ARN of the fleet.\n

    :type AuditStreamArn: string
    :param AuditStreamArn: The ARN of the Amazon Kinesis data stream that receives the audit events.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WorkLink.Client.exceptions.UnauthorizedException
WorkLink.Client.exceptions.InternalServerErrorException
WorkLink.Client.exceptions.InvalidRequestException
WorkLink.Client.exceptions.ResourceNotFoundException
WorkLink.Client.exceptions.TooManyRequestsException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_company_network_configuration(FleetArn=None, VpcId=None, SubnetIds=None, SecurityGroupIds=None):
    """
    Updates the company network configuration for the fleet.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_company_network_configuration(
        FleetArn='string',
        VpcId='string',
        SubnetIds=[
            'string',
        ],
        SecurityGroupIds=[
            'string',
        ]
    )
    
    
    :type FleetArn: string
    :param FleetArn: [REQUIRED]\nThe ARN of the fleet.\n

    :type VpcId: string
    :param VpcId: [REQUIRED]\nThe VPC with connectivity to associated websites.\n

    :type SubnetIds: list
    :param SubnetIds: [REQUIRED]\nThe subnets used for X-ENI connections from Amazon WorkLink rendering containers.\n\n(string) --\n\n

    :type SecurityGroupIds: list
    :param SecurityGroupIds: [REQUIRED]\nThe security groups associated with access to the provided subnets.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WorkLink.Client.exceptions.UnauthorizedException
WorkLink.Client.exceptions.InternalServerErrorException
WorkLink.Client.exceptions.InvalidRequestException
WorkLink.Client.exceptions.ResourceNotFoundException
WorkLink.Client.exceptions.TooManyRequestsException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_device_policy_configuration(FleetArn=None, DeviceCaCertificate=None):
    """
    Updates the device policy configuration for the fleet.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_device_policy_configuration(
        FleetArn='string',
        DeviceCaCertificate='string'
    )
    
    
    :type FleetArn: string
    :param FleetArn: [REQUIRED]\nThe ARN of the fleet.\n

    :type DeviceCaCertificate: string
    :param DeviceCaCertificate: The certificate chain, including intermediate certificates and the root certificate authority certificate used to issue device certificates.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WorkLink.Client.exceptions.UnauthorizedException
WorkLink.Client.exceptions.InternalServerErrorException
WorkLink.Client.exceptions.InvalidRequestException
WorkLink.Client.exceptions.ResourceNotFoundException
WorkLink.Client.exceptions.TooManyRequestsException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_domain_metadata(FleetArn=None, DomainName=None, DisplayName=None):
    """
    Updates domain metadata, such as DisplayName.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_domain_metadata(
        FleetArn='string',
        DomainName='string',
        DisplayName='string'
    )
    
    
    :type FleetArn: string
    :param FleetArn: [REQUIRED]\nThe ARN of the fleet.\n

    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe name of the domain.\n

    :type DisplayName: string
    :param DisplayName: The name to display.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WorkLink.Client.exceptions.UnauthorizedException
WorkLink.Client.exceptions.InternalServerErrorException
WorkLink.Client.exceptions.InvalidRequestException
WorkLink.Client.exceptions.ResourceNotFoundException
WorkLink.Client.exceptions.TooManyRequestsException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_fleet_metadata(FleetArn=None, DisplayName=None, OptimizeForEndUserLocation=None):
    """
    Updates fleet metadata, such as DisplayName.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_fleet_metadata(
        FleetArn='string',
        DisplayName='string',
        OptimizeForEndUserLocation=True|False
    )
    
    
    :type FleetArn: string
    :param FleetArn: [REQUIRED]\nThe ARN of the fleet.\n

    :type DisplayName: string
    :param DisplayName: The fleet name to display. The existing DisplayName is unset if null is passed.

    :type OptimizeForEndUserLocation: boolean
    :param OptimizeForEndUserLocation: The option to optimize for better performance by routing traffic through the closest AWS Region to users, which may be outside of your home Region.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WorkLink.Client.exceptions.UnauthorizedException
WorkLink.Client.exceptions.InternalServerErrorException
WorkLink.Client.exceptions.InvalidRequestException
WorkLink.Client.exceptions.ResourceNotFoundException
WorkLink.Client.exceptions.TooManyRequestsException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_identity_provider_configuration(FleetArn=None, IdentityProviderType=None, IdentityProviderSamlMetadata=None):
    """
    Updates the identity provider configuration for the fleet.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_identity_provider_configuration(
        FleetArn='string',
        IdentityProviderType='SAML',
        IdentityProviderSamlMetadata='string'
    )
    
    
    :type FleetArn: string
    :param FleetArn: [REQUIRED]\nThe ARN of the fleet.\n

    :type IdentityProviderType: string
    :param IdentityProviderType: [REQUIRED]\nThe type of identity provider.\n

    :type IdentityProviderSamlMetadata: string
    :param IdentityProviderSamlMetadata: The SAML metadata document provided by the customer\xe2\x80\x99s identity provider. The existing IdentityProviderSamlMetadata is unset if null is passed.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WorkLink.Client.exceptions.UnauthorizedException
WorkLink.Client.exceptions.InternalServerErrorException
WorkLink.Client.exceptions.InvalidRequestException
WorkLink.Client.exceptions.ResourceNotFoundException
WorkLink.Client.exceptions.TooManyRequestsException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

