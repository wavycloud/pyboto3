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

def associate_customer_gateway(CustomerGatewayArn=None, GlobalNetworkId=None, DeviceId=None, LinkId=None):
    """
    Associates a customer gateway with a device and optionally, with a link. If you specify a link, it must be associated with the specified device.
    You can only associate customer gateways that are connected to a VPN attachment on a transit gateway. The transit gateway must be registered in your global network. When you register a transit gateway, customer gateways that are connected to the transit gateway are automatically included in the global network. To list customer gateways that are connected to a transit gateway, use the DescribeVpnConnections EC2 API and filter by transit-gateway-id .
    You cannot associate a customer gateway with more than one device and link.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_customer_gateway(
        CustomerGatewayArn='string',
        GlobalNetworkId='string',
        DeviceId='string',
        LinkId='string'
    )
    
    
    :type CustomerGatewayArn: string
    :param CustomerGatewayArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the customer gateway. For more information, see Resources Defined by Amazon EC2 .\n

    :type GlobalNetworkId: string
    :param GlobalNetworkId: [REQUIRED]\nThe ID of the global network.\n

    :type DeviceId: string
    :param DeviceId: [REQUIRED]\nThe ID of the device.\n

    :type LinkId: string
    :param LinkId: The ID of the link.

    :rtype: dict

ReturnsResponse Syntax
{
    'CustomerGatewayAssociation': {
        'CustomerGatewayArn': 'string',
        'GlobalNetworkId': 'string',
        'DeviceId': 'string',
        'LinkId': 'string',
        'State': 'PENDING'|'AVAILABLE'|'DELETING'|'DELETED'
    }
}


Response Structure

(dict) --

CustomerGatewayAssociation (dict) --
The customer gateway association.

CustomerGatewayArn (string) --
The Amazon Resource Name (ARN) of the customer gateway.

GlobalNetworkId (string) --
The ID of the global network.

DeviceId (string) --
The ID of the device.

LinkId (string) --
The ID of the link.

State (string) --
The association state.









Exceptions

NetworkManager.Client.exceptions.ValidationException
NetworkManager.Client.exceptions.ServiceQuotaExceededException
NetworkManager.Client.exceptions.AccessDeniedException
NetworkManager.Client.exceptions.ResourceNotFoundException
NetworkManager.Client.exceptions.ConflictException
NetworkManager.Client.exceptions.ThrottlingException
NetworkManager.Client.exceptions.InternalServerException


    :return: {
        'CustomerGatewayAssociation': {
            'CustomerGatewayArn': 'string',
            'GlobalNetworkId': 'string',
            'DeviceId': 'string',
            'LinkId': 'string',
            'State': 'PENDING'|'AVAILABLE'|'DELETING'|'DELETED'
        }
    }
    
    
    :returns: 
    NetworkManager.Client.exceptions.ValidationException
    NetworkManager.Client.exceptions.ServiceQuotaExceededException
    NetworkManager.Client.exceptions.AccessDeniedException
    NetworkManager.Client.exceptions.ResourceNotFoundException
    NetworkManager.Client.exceptions.ConflictException
    NetworkManager.Client.exceptions.ThrottlingException
    NetworkManager.Client.exceptions.InternalServerException
    
    """
    pass

def associate_link(GlobalNetworkId=None, DeviceId=None, LinkId=None):
    """
    Associates a link to a device. A device can be associated to multiple links and a link can be associated to multiple devices. The device and link must be in the same global network and the same site.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_link(
        GlobalNetworkId='string',
        DeviceId='string',
        LinkId='string'
    )
    
    
    :type GlobalNetworkId: string
    :param GlobalNetworkId: [REQUIRED]\nThe ID of the global network.\n

    :type DeviceId: string
    :param DeviceId: [REQUIRED]\nThe ID of the device.\n

    :type LinkId: string
    :param LinkId: [REQUIRED]\nThe ID of the link.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'LinkAssociation': {
        'GlobalNetworkId': 'string',
        'DeviceId': 'string',
        'LinkId': 'string',
        'LinkAssociationState': 'PENDING'|'AVAILABLE'|'DELETING'|'DELETED'
    }
}


Response Structure

(dict) --

LinkAssociation (dict) --
The link association.

GlobalNetworkId (string) --
The ID of the global network.

DeviceId (string) --
The device ID for the link association.

LinkId (string) --
The ID of the link.

LinkAssociationState (string) --
The state of the association.









Exceptions

NetworkManager.Client.exceptions.ValidationException
NetworkManager.Client.exceptions.ServiceQuotaExceededException
NetworkManager.Client.exceptions.AccessDeniedException
NetworkManager.Client.exceptions.ResourceNotFoundException
NetworkManager.Client.exceptions.ConflictException
NetworkManager.Client.exceptions.ThrottlingException
NetworkManager.Client.exceptions.InternalServerException


    :return: {
        'LinkAssociation': {
            'GlobalNetworkId': 'string',
            'DeviceId': 'string',
            'LinkId': 'string',
            'LinkAssociationState': 'PENDING'|'AVAILABLE'|'DELETING'|'DELETED'
        }
    }
    
    
    :returns: 
    NetworkManager.Client.exceptions.ValidationException
    NetworkManager.Client.exceptions.ServiceQuotaExceededException
    NetworkManager.Client.exceptions.AccessDeniedException
    NetworkManager.Client.exceptions.ResourceNotFoundException
    NetworkManager.Client.exceptions.ConflictException
    NetworkManager.Client.exceptions.ThrottlingException
    NetworkManager.Client.exceptions.InternalServerException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_device(GlobalNetworkId=None, Description=None, Type=None, Vendor=None, Model=None, SerialNumber=None, Location=None, SiteId=None, Tags=None):
    """
    Creates a new device in a global network. If you specify both a site ID and a location, the location of the site is used for visualization in the Network Manager console.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_device(
        GlobalNetworkId='string',
        Description='string',
        Type='string',
        Vendor='string',
        Model='string',
        SerialNumber='string',
        Location={
            'Address': 'string',
            'Latitude': 'string',
            'Longitude': 'string'
        },
        SiteId='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type GlobalNetworkId: string
    :param GlobalNetworkId: [REQUIRED]\nThe ID of the global network.\n

    :type Description: string
    :param Description: A description of the device.\nLength Constraints: Maximum length of 256 characters.\n

    :type Type: string
    :param Type: The type of the device.

    :type Vendor: string
    :param Vendor: The vendor of the device.\nLength Constraints: Maximum length of 128 characters.\n

    :type Model: string
    :param Model: The model of the device.\nLength Constraints: Maximum length of 128 characters.\n

    :type SerialNumber: string
    :param SerialNumber: The serial number of the device.\nLength Constraints: Maximum length of 128 characters.\n

    :type Location: dict
    :param Location: The location of the device.\n\nAddress (string) --The physical address.\n\nLatitude (string) --The latitude.\n\nLongitude (string) --The longitude.\n\n\n

    :type SiteId: string
    :param SiteId: The ID of the site.

    :type Tags: list
    :param Tags: The tags to apply to the resource during creation.\n\n(dict) --Describes a tag.\n\nKey (string) --The tag key.\nLength Constraints: Maximum length of 128 characters.\n\nValue (string) --The tag value.\nLength Constraints: Maximum length of 256 characters.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Device': {
        'DeviceId': 'string',
        'DeviceArn': 'string',
        'GlobalNetworkId': 'string',
        'Description': 'string',
        'Type': 'string',
        'Vendor': 'string',
        'Model': 'string',
        'SerialNumber': 'string',
        'Location': {
            'Address': 'string',
            'Latitude': 'string',
            'Longitude': 'string'
        },
        'SiteId': 'string',
        'CreatedAt': datetime(2015, 1, 1),
        'State': 'PENDING'|'AVAILABLE'|'DELETING'|'UPDATING',
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

Device (dict) --
Information about the device.

DeviceId (string) --
The ID of the device.

DeviceArn (string) --
The Amazon Resource Name (ARN) of the device.

GlobalNetworkId (string) --
The ID of the global network.

Description (string) --
The description of the device.

Type (string) --
The device type.

Vendor (string) --
The device vendor.

Model (string) --
The device model.

SerialNumber (string) --
The device serial number.

Location (dict) --
The site location.

Address (string) --
The physical address.

Latitude (string) --
The latitude.

Longitude (string) --
The longitude.



SiteId (string) --
The site ID.

CreatedAt (datetime) --
The date and time that the site was created.

State (string) --
The device state.

Tags (list) --
The tags for the device.

(dict) --
Describes a tag.

Key (string) --
The tag key.
Length Constraints: Maximum length of 128 characters.

Value (string) --
The tag value.
Length Constraints: Maximum length of 256 characters.













Exceptions

NetworkManager.Client.exceptions.ValidationException
NetworkManager.Client.exceptions.ServiceQuotaExceededException
NetworkManager.Client.exceptions.AccessDeniedException
NetworkManager.Client.exceptions.ResourceNotFoundException
NetworkManager.Client.exceptions.ConflictException
NetworkManager.Client.exceptions.ThrottlingException
NetworkManager.Client.exceptions.InternalServerException


    :return: {
        'Device': {
            'DeviceId': 'string',
            'DeviceArn': 'string',
            'GlobalNetworkId': 'string',
            'Description': 'string',
            'Type': 'string',
            'Vendor': 'string',
            'Model': 'string',
            'SerialNumber': 'string',
            'Location': {
                'Address': 'string',
                'Latitude': 'string',
                'Longitude': 'string'
            },
            'SiteId': 'string',
            'CreatedAt': datetime(2015, 1, 1),
            'State': 'PENDING'|'AVAILABLE'|'DELETING'|'UPDATING',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    NetworkManager.Client.exceptions.ValidationException
    NetworkManager.Client.exceptions.ServiceQuotaExceededException
    NetworkManager.Client.exceptions.AccessDeniedException
    NetworkManager.Client.exceptions.ResourceNotFoundException
    NetworkManager.Client.exceptions.ConflictException
    NetworkManager.Client.exceptions.ThrottlingException
    NetworkManager.Client.exceptions.InternalServerException
    
    """
    pass

def create_global_network(Description=None, Tags=None):
    """
    Creates a new, empty global network.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_global_network(
        Description='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Description: string
    :param Description: A description of the global network.\nLength Constraints: Maximum length of 256 characters.\n

    :type Tags: list
    :param Tags: The tags to apply to the resource during creation.\n\n(dict) --Describes a tag.\n\nKey (string) --The tag key.\nLength Constraints: Maximum length of 128 characters.\n\nValue (string) --The tag value.\nLength Constraints: Maximum length of 256 characters.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GlobalNetwork': {
        'GlobalNetworkId': 'string',
        'GlobalNetworkArn': 'string',
        'Description': 'string',
        'CreatedAt': datetime(2015, 1, 1),
        'State': 'PENDING'|'AVAILABLE'|'DELETING'|'UPDATING',
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

GlobalNetwork (dict) --
Information about the global network object.

GlobalNetworkId (string) --
The ID of the global network.

GlobalNetworkArn (string) --
The Amazon Resource Name (ARN) of the global network.

Description (string) --
The description of the global network.

CreatedAt (datetime) --
The date and time that the global network was created.

State (string) --
The state of the global network.

Tags (list) --
The tags for the global network.

(dict) --
Describes a tag.

Key (string) --
The tag key.
Length Constraints: Maximum length of 128 characters.

Value (string) --
The tag value.
Length Constraints: Maximum length of 256 characters.













Exceptions

NetworkManager.Client.exceptions.ValidationException
NetworkManager.Client.exceptions.ServiceQuotaExceededException
NetworkManager.Client.exceptions.AccessDeniedException
NetworkManager.Client.exceptions.ConflictException
NetworkManager.Client.exceptions.ThrottlingException
NetworkManager.Client.exceptions.InternalServerException


    :return: {
        'GlobalNetwork': {
            'GlobalNetworkId': 'string',
            'GlobalNetworkArn': 'string',
            'Description': 'string',
            'CreatedAt': datetime(2015, 1, 1),
            'State': 'PENDING'|'AVAILABLE'|'DELETING'|'UPDATING',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    NetworkManager.Client.exceptions.ValidationException
    NetworkManager.Client.exceptions.ServiceQuotaExceededException
    NetworkManager.Client.exceptions.AccessDeniedException
    NetworkManager.Client.exceptions.ConflictException
    NetworkManager.Client.exceptions.ThrottlingException
    NetworkManager.Client.exceptions.InternalServerException
    
    """
    pass

def create_link(GlobalNetworkId=None, Description=None, Type=None, Bandwidth=None, Provider=None, SiteId=None, Tags=None):
    """
    Creates a new link for a specified site.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_link(
        GlobalNetworkId='string',
        Description='string',
        Type='string',
        Bandwidth={
            'UploadSpeed': 123,
            'DownloadSpeed': 123
        },
        Provider='string',
        SiteId='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type GlobalNetworkId: string
    :param GlobalNetworkId: [REQUIRED]\nThe ID of the global network.\n

    :type Description: string
    :param Description: A description of the link.\nLength Constraints: Maximum length of 256 characters.\n

    :type Type: string
    :param Type: The type of the link.\nConstraints: Cannot include the following characters: | ^\nLength Constraints: Maximum length of 128 characters.\n

    :type Bandwidth: dict
    :param Bandwidth: [REQUIRED]\nThe upload speed and download speed in Mbps.\n\nUploadSpeed (integer) --Upload speed in Mbps.\n\nDownloadSpeed (integer) --Download speed in Mbps.\n\n\n

    :type Provider: string
    :param Provider: The provider of the link.\nConstraints: Cannot include the following characters: | ^\nLength Constraints: Maximum length of 128 characters.\n

    :type SiteId: string
    :param SiteId: [REQUIRED]\nThe ID of the site.\n

    :type Tags: list
    :param Tags: The tags to apply to the resource during creation.\n\n(dict) --Describes a tag.\n\nKey (string) --The tag key.\nLength Constraints: Maximum length of 128 characters.\n\nValue (string) --The tag value.\nLength Constraints: Maximum length of 256 characters.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Link': {
        'LinkId': 'string',
        'LinkArn': 'string',
        'GlobalNetworkId': 'string',
        'SiteId': 'string',
        'Description': 'string',
        'Type': 'string',
        'Bandwidth': {
            'UploadSpeed': 123,
            'DownloadSpeed': 123
        },
        'Provider': 'string',
        'CreatedAt': datetime(2015, 1, 1),
        'State': 'PENDING'|'AVAILABLE'|'DELETING'|'UPDATING',
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

Link (dict) --
Information about the link.

LinkId (string) --
The ID of the link.

LinkArn (string) --
The Amazon Resource Name (ARN) of the link.

GlobalNetworkId (string) --
The ID of the global network.

SiteId (string) --
The ID of the site.

Description (string) --
The description of the link.

Type (string) --
The type of the link.

Bandwidth (dict) --
The bandwidth for the link.

UploadSpeed (integer) --
Upload speed in Mbps.

DownloadSpeed (integer) --
Download speed in Mbps.



Provider (string) --
The provider of the link.

CreatedAt (datetime) --
The date and time that the link was created.

State (string) --
The state of the link.

Tags (list) --
The tags for the link.

(dict) --
Describes a tag.

Key (string) --
The tag key.
Length Constraints: Maximum length of 128 characters.

Value (string) --
The tag value.
Length Constraints: Maximum length of 256 characters.













Exceptions

NetworkManager.Client.exceptions.ValidationException
NetworkManager.Client.exceptions.ServiceQuotaExceededException
NetworkManager.Client.exceptions.AccessDeniedException
NetworkManager.Client.exceptions.ResourceNotFoundException
NetworkManager.Client.exceptions.ConflictException
NetworkManager.Client.exceptions.ThrottlingException
NetworkManager.Client.exceptions.InternalServerException


    :return: {
        'Link': {
            'LinkId': 'string',
            'LinkArn': 'string',
            'GlobalNetworkId': 'string',
            'SiteId': 'string',
            'Description': 'string',
            'Type': 'string',
            'Bandwidth': {
                'UploadSpeed': 123,
                'DownloadSpeed': 123
            },
            'Provider': 'string',
            'CreatedAt': datetime(2015, 1, 1),
            'State': 'PENDING'|'AVAILABLE'|'DELETING'|'UPDATING',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    NetworkManager.Client.exceptions.ValidationException
    NetworkManager.Client.exceptions.ServiceQuotaExceededException
    NetworkManager.Client.exceptions.AccessDeniedException
    NetworkManager.Client.exceptions.ResourceNotFoundException
    NetworkManager.Client.exceptions.ConflictException
    NetworkManager.Client.exceptions.ThrottlingException
    NetworkManager.Client.exceptions.InternalServerException
    
    """
    pass

def create_site(GlobalNetworkId=None, Description=None, Location=None, Tags=None):
    """
    Creates a new site in a global network.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_site(
        GlobalNetworkId='string',
        Description='string',
        Location={
            'Address': 'string',
            'Latitude': 'string',
            'Longitude': 'string'
        },
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type GlobalNetworkId: string
    :param GlobalNetworkId: [REQUIRED]\nThe ID of the global network.\n

    :type Description: string
    :param Description: A description of your site.\nLength Constraints: Maximum length of 256 characters.\n

    :type Location: dict
    :param Location: The site location. This information is used for visualization in the Network Manager console. If you specify the address, the latitude and longitude are automatically calculated.\n\nAddress : The physical address of the site.\nLatitude : The latitude of the site.\nLongitude : The longitude of the site.\n\n\nAddress (string) --The physical address.\n\nLatitude (string) --The latitude.\n\nLongitude (string) --The longitude.\n\n\n

    :type Tags: list
    :param Tags: The tags to apply to the resource during creation.\n\n(dict) --Describes a tag.\n\nKey (string) --The tag key.\nLength Constraints: Maximum length of 128 characters.\n\nValue (string) --The tag value.\nLength Constraints: Maximum length of 256 characters.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Site': {
        'SiteId': 'string',
        'SiteArn': 'string',
        'GlobalNetworkId': 'string',
        'Description': 'string',
        'Location': {
            'Address': 'string',
            'Latitude': 'string',
            'Longitude': 'string'
        },
        'CreatedAt': datetime(2015, 1, 1),
        'State': 'PENDING'|'AVAILABLE'|'DELETING'|'UPDATING',
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

Site (dict) --
Information about the site.

SiteId (string) --
The ID of the site.

SiteArn (string) --
The Amazon Resource Name (ARN) of the site.

GlobalNetworkId (string) --
The ID of the global network.

Description (string) --
The description of the site.

Location (dict) --
The location of the site.

Address (string) --
The physical address.

Latitude (string) --
The latitude.

Longitude (string) --
The longitude.



CreatedAt (datetime) --
The date and time that the site was created.

State (string) --
The state of the site.

Tags (list) --
The tags for the site.

(dict) --
Describes a tag.

Key (string) --
The tag key.
Length Constraints: Maximum length of 128 characters.

Value (string) --
The tag value.
Length Constraints: Maximum length of 256 characters.













Exceptions

NetworkManager.Client.exceptions.ValidationException
NetworkManager.Client.exceptions.ServiceQuotaExceededException
NetworkManager.Client.exceptions.AccessDeniedException
NetworkManager.Client.exceptions.ResourceNotFoundException
NetworkManager.Client.exceptions.ConflictException
NetworkManager.Client.exceptions.ThrottlingException
NetworkManager.Client.exceptions.InternalServerException


    :return: {
        'Site': {
            'SiteId': 'string',
            'SiteArn': 'string',
            'GlobalNetworkId': 'string',
            'Description': 'string',
            'Location': {
                'Address': 'string',
                'Latitude': 'string',
                'Longitude': 'string'
            },
            'CreatedAt': datetime(2015, 1, 1),
            'State': 'PENDING'|'AVAILABLE'|'DELETING'|'UPDATING',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    NetworkManager.Client.exceptions.ValidationException
    NetworkManager.Client.exceptions.ServiceQuotaExceededException
    NetworkManager.Client.exceptions.AccessDeniedException
    NetworkManager.Client.exceptions.ResourceNotFoundException
    NetworkManager.Client.exceptions.ConflictException
    NetworkManager.Client.exceptions.ThrottlingException
    NetworkManager.Client.exceptions.InternalServerException
    
    """
    pass

def delete_device(GlobalNetworkId=None, DeviceId=None):
    """
    Deletes an existing device. You must first disassociate the device from any links and customer gateways.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_device(
        GlobalNetworkId='string',
        DeviceId='string'
    )
    
    
    :type GlobalNetworkId: string
    :param GlobalNetworkId: [REQUIRED]\nThe ID of the global network.\n

    :type DeviceId: string
    :param DeviceId: [REQUIRED]\nThe ID of the device.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Device': {
        'DeviceId': 'string',
        'DeviceArn': 'string',
        'GlobalNetworkId': 'string',
        'Description': 'string',
        'Type': 'string',
        'Vendor': 'string',
        'Model': 'string',
        'SerialNumber': 'string',
        'Location': {
            'Address': 'string',
            'Latitude': 'string',
            'Longitude': 'string'
        },
        'SiteId': 'string',
        'CreatedAt': datetime(2015, 1, 1),
        'State': 'PENDING'|'AVAILABLE'|'DELETING'|'UPDATING',
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

Device (dict) --
Information about the device.

DeviceId (string) --
The ID of the device.

DeviceArn (string) --
The Amazon Resource Name (ARN) of the device.

GlobalNetworkId (string) --
The ID of the global network.

Description (string) --
The description of the device.

Type (string) --
The device type.

Vendor (string) --
The device vendor.

Model (string) --
The device model.

SerialNumber (string) --
The device serial number.

Location (dict) --
The site location.

Address (string) --
The physical address.

Latitude (string) --
The latitude.

Longitude (string) --
The longitude.



SiteId (string) --
The site ID.

CreatedAt (datetime) --
The date and time that the site was created.

State (string) --
The device state.

Tags (list) --
The tags for the device.

(dict) --
Describes a tag.

Key (string) --
The tag key.
Length Constraints: Maximum length of 128 characters.

Value (string) --
The tag value.
Length Constraints: Maximum length of 256 characters.













Exceptions

NetworkManager.Client.exceptions.ValidationException
NetworkManager.Client.exceptions.AccessDeniedException
NetworkManager.Client.exceptions.ResourceNotFoundException
NetworkManager.Client.exceptions.ConflictException
NetworkManager.Client.exceptions.ThrottlingException
NetworkManager.Client.exceptions.InternalServerException


    :return: {
        'Device': {
            'DeviceId': 'string',
            'DeviceArn': 'string',
            'GlobalNetworkId': 'string',
            'Description': 'string',
            'Type': 'string',
            'Vendor': 'string',
            'Model': 'string',
            'SerialNumber': 'string',
            'Location': {
                'Address': 'string',
                'Latitude': 'string',
                'Longitude': 'string'
            },
            'SiteId': 'string',
            'CreatedAt': datetime(2015, 1, 1),
            'State': 'PENDING'|'AVAILABLE'|'DELETING'|'UPDATING',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    NetworkManager.Client.exceptions.ValidationException
    NetworkManager.Client.exceptions.AccessDeniedException
    NetworkManager.Client.exceptions.ResourceNotFoundException
    NetworkManager.Client.exceptions.ConflictException
    NetworkManager.Client.exceptions.ThrottlingException
    NetworkManager.Client.exceptions.InternalServerException
    
    """
    pass

def delete_global_network(GlobalNetworkId=None):
    """
    Deletes an existing global network. You must first delete all global network objects (devices, links, and sites) and deregister all transit gateways.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_global_network(
        GlobalNetworkId='string'
    )
    
    
    :type GlobalNetworkId: string
    :param GlobalNetworkId: [REQUIRED]\nThe ID of the global network.\n

    :rtype: dict
ReturnsResponse Syntax{
    'GlobalNetwork': {
        'GlobalNetworkId': 'string',
        'GlobalNetworkArn': 'string',
        'Description': 'string',
        'CreatedAt': datetime(2015, 1, 1),
        'State': 'PENDING'|'AVAILABLE'|'DELETING'|'UPDATING',
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --
GlobalNetwork (dict) --Information about the global network.

GlobalNetworkId (string) --The ID of the global network.

GlobalNetworkArn (string) --The Amazon Resource Name (ARN) of the global network.

Description (string) --The description of the global network.

CreatedAt (datetime) --The date and time that the global network was created.

State (string) --The state of the global network.

Tags (list) --The tags for the global network.

(dict) --Describes a tag.

Key (string) --The tag key.
Length Constraints: Maximum length of 128 characters.

Value (string) --The tag value.
Length Constraints: Maximum length of 256 characters.












Exceptions

NetworkManager.Client.exceptions.ValidationException
NetworkManager.Client.exceptions.AccessDeniedException
NetworkManager.Client.exceptions.ResourceNotFoundException
NetworkManager.Client.exceptions.ConflictException
NetworkManager.Client.exceptions.ThrottlingException
NetworkManager.Client.exceptions.InternalServerException


    :return: {
        'GlobalNetwork': {
            'GlobalNetworkId': 'string',
            'GlobalNetworkArn': 'string',
            'Description': 'string',
            'CreatedAt': datetime(2015, 1, 1),
            'State': 'PENDING'|'AVAILABLE'|'DELETING'|'UPDATING',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def delete_link(GlobalNetworkId=None, LinkId=None):
    """
    Deletes an existing link. You must first disassociate the link from any devices and customer gateways.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_link(
        GlobalNetworkId='string',
        LinkId='string'
    )
    
    
    :type GlobalNetworkId: string
    :param GlobalNetworkId: [REQUIRED]\nThe ID of the global network.\n

    :type LinkId: string
    :param LinkId: [REQUIRED]\nThe ID of the link.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Link': {
        'LinkId': 'string',
        'LinkArn': 'string',
        'GlobalNetworkId': 'string',
        'SiteId': 'string',
        'Description': 'string',
        'Type': 'string',
        'Bandwidth': {
            'UploadSpeed': 123,
            'DownloadSpeed': 123
        },
        'Provider': 'string',
        'CreatedAt': datetime(2015, 1, 1),
        'State': 'PENDING'|'AVAILABLE'|'DELETING'|'UPDATING',
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

Link (dict) --
Information about the link.

LinkId (string) --
The ID of the link.

LinkArn (string) --
The Amazon Resource Name (ARN) of the link.

GlobalNetworkId (string) --
The ID of the global network.

SiteId (string) --
The ID of the site.

Description (string) --
The description of the link.

Type (string) --
The type of the link.

Bandwidth (dict) --
The bandwidth for the link.

UploadSpeed (integer) --
Upload speed in Mbps.

DownloadSpeed (integer) --
Download speed in Mbps.



Provider (string) --
The provider of the link.

CreatedAt (datetime) --
The date and time that the link was created.

State (string) --
The state of the link.

Tags (list) --
The tags for the link.

(dict) --
Describes a tag.

Key (string) --
The tag key.
Length Constraints: Maximum length of 128 characters.

Value (string) --
The tag value.
Length Constraints: Maximum length of 256 characters.













Exceptions

NetworkManager.Client.exceptions.ValidationException
NetworkManager.Client.exceptions.AccessDeniedException
NetworkManager.Client.exceptions.ResourceNotFoundException
NetworkManager.Client.exceptions.ConflictException
NetworkManager.Client.exceptions.ThrottlingException
NetworkManager.Client.exceptions.InternalServerException


    :return: {
        'Link': {
            'LinkId': 'string',
            'LinkArn': 'string',
            'GlobalNetworkId': 'string',
            'SiteId': 'string',
            'Description': 'string',
            'Type': 'string',
            'Bandwidth': {
                'UploadSpeed': 123,
                'DownloadSpeed': 123
            },
            'Provider': 'string',
            'CreatedAt': datetime(2015, 1, 1),
            'State': 'PENDING'|'AVAILABLE'|'DELETING'|'UPDATING',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    NetworkManager.Client.exceptions.ValidationException
    NetworkManager.Client.exceptions.AccessDeniedException
    NetworkManager.Client.exceptions.ResourceNotFoundException
    NetworkManager.Client.exceptions.ConflictException
    NetworkManager.Client.exceptions.ThrottlingException
    NetworkManager.Client.exceptions.InternalServerException
    
    """
    pass

def delete_site(GlobalNetworkId=None, SiteId=None):
    """
    Deletes an existing site. The site cannot be associated with any device or link.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_site(
        GlobalNetworkId='string',
        SiteId='string'
    )
    
    
    :type GlobalNetworkId: string
    :param GlobalNetworkId: [REQUIRED]\nThe ID of the global network.\n

    :type SiteId: string
    :param SiteId: [REQUIRED]\nThe ID of the site.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Site': {
        'SiteId': 'string',
        'SiteArn': 'string',
        'GlobalNetworkId': 'string',
        'Description': 'string',
        'Location': {
            'Address': 'string',
            'Latitude': 'string',
            'Longitude': 'string'
        },
        'CreatedAt': datetime(2015, 1, 1),
        'State': 'PENDING'|'AVAILABLE'|'DELETING'|'UPDATING',
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

Site (dict) --
Information about the site.

SiteId (string) --
The ID of the site.

SiteArn (string) --
The Amazon Resource Name (ARN) of the site.

GlobalNetworkId (string) --
The ID of the global network.

Description (string) --
The description of the site.

Location (dict) --
The location of the site.

Address (string) --
The physical address.

Latitude (string) --
The latitude.

Longitude (string) --
The longitude.



CreatedAt (datetime) --
The date and time that the site was created.

State (string) --
The state of the site.

Tags (list) --
The tags for the site.

(dict) --
Describes a tag.

Key (string) --
The tag key.
Length Constraints: Maximum length of 128 characters.

Value (string) --
The tag value.
Length Constraints: Maximum length of 256 characters.













Exceptions

NetworkManager.Client.exceptions.ValidationException
NetworkManager.Client.exceptions.AccessDeniedException
NetworkManager.Client.exceptions.ResourceNotFoundException
NetworkManager.Client.exceptions.ConflictException
NetworkManager.Client.exceptions.ThrottlingException
NetworkManager.Client.exceptions.InternalServerException


    :return: {
        'Site': {
            'SiteId': 'string',
            'SiteArn': 'string',
            'GlobalNetworkId': 'string',
            'Description': 'string',
            'Location': {
                'Address': 'string',
                'Latitude': 'string',
                'Longitude': 'string'
            },
            'CreatedAt': datetime(2015, 1, 1),
            'State': 'PENDING'|'AVAILABLE'|'DELETING'|'UPDATING',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    NetworkManager.Client.exceptions.ValidationException
    NetworkManager.Client.exceptions.AccessDeniedException
    NetworkManager.Client.exceptions.ResourceNotFoundException
    NetworkManager.Client.exceptions.ConflictException
    NetworkManager.Client.exceptions.ThrottlingException
    NetworkManager.Client.exceptions.InternalServerException
    
    """
    pass

def deregister_transit_gateway(GlobalNetworkId=None, TransitGatewayArn=None):
    """
    Deregisters a transit gateway from your global network. This action does not delete your transit gateway, or modify any of its attachments. This action removes any customer gateway associations.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.deregister_transit_gateway(
        GlobalNetworkId='string',
        TransitGatewayArn='string'
    )
    
    
    :type GlobalNetworkId: string
    :param GlobalNetworkId: [REQUIRED]\nThe ID of the global network.\n

    :type TransitGatewayArn: string
    :param TransitGatewayArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the transit gateway.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TransitGatewayRegistration': {
        'GlobalNetworkId': 'string',
        'TransitGatewayArn': 'string',
        'State': {
            'Code': 'PENDING'|'AVAILABLE'|'DELETING'|'DELETED'|'FAILED',
            'Message': 'string'
        }
    }
}


Response Structure

(dict) --

TransitGatewayRegistration (dict) --
The transit gateway registration information.

GlobalNetworkId (string) --
The ID of the global network.

TransitGatewayArn (string) --
The Amazon Resource Name (ARN) of the transit gateway.

State (dict) --
The state of the transit gateway registration.

Code (string) --
The code for the state reason.

Message (string) --
The message for the state reason.











Exceptions

NetworkManager.Client.exceptions.ValidationException
NetworkManager.Client.exceptions.AccessDeniedException
NetworkManager.Client.exceptions.ResourceNotFoundException
NetworkManager.Client.exceptions.ConflictException
NetworkManager.Client.exceptions.ThrottlingException
NetworkManager.Client.exceptions.InternalServerException


    :return: {
        'TransitGatewayRegistration': {
            'GlobalNetworkId': 'string',
            'TransitGatewayArn': 'string',
            'State': {
                'Code': 'PENDING'|'AVAILABLE'|'DELETING'|'DELETED'|'FAILED',
                'Message': 'string'
            }
        }
    }
    
    
    :returns: 
    NetworkManager.Client.exceptions.ValidationException
    NetworkManager.Client.exceptions.AccessDeniedException
    NetworkManager.Client.exceptions.ResourceNotFoundException
    NetworkManager.Client.exceptions.ConflictException
    NetworkManager.Client.exceptions.ThrottlingException
    NetworkManager.Client.exceptions.InternalServerException
    
    """
    pass

def describe_global_networks(GlobalNetworkIds=None, MaxResults=None, NextToken=None):
    """
    Describes one or more global networks. By default, all global networks are described. To describe the objects in your global network, you must use the appropriate Get* action. For example, to list the transit gateways in your global network, use  GetTransitGatewayRegistrations .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_global_networks(
        GlobalNetworkIds=[
            'string',
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type GlobalNetworkIds: list
    :param GlobalNetworkIds: The IDs of one or more global networks. The maximum is 10.\n\n(string) --\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return.

    :type NextToken: string
    :param NextToken: The token for the next page of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'GlobalNetworks': [
        {
            'GlobalNetworkId': 'string',
            'GlobalNetworkArn': 'string',
            'Description': 'string',
            'CreatedAt': datetime(2015, 1, 1),
            'State': 'PENDING'|'AVAILABLE'|'DELETING'|'UPDATING',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

GlobalNetworks (list) --
Information about the global networks.

(dict) --
Describes a global network.

GlobalNetworkId (string) --
The ID of the global network.

GlobalNetworkArn (string) --
The Amazon Resource Name (ARN) of the global network.

Description (string) --
The description of the global network.

CreatedAt (datetime) --
The date and time that the global network was created.

State (string) --
The state of the global network.

Tags (list) --
The tags for the global network.

(dict) --
Describes a tag.

Key (string) --
The tag key.
Length Constraints: Maximum length of 128 characters.

Value (string) --
The tag value.
Length Constraints: Maximum length of 256 characters.









NextToken (string) --
The token for the next page of results.







Exceptions

NetworkManager.Client.exceptions.ValidationException
NetworkManager.Client.exceptions.AccessDeniedException
NetworkManager.Client.exceptions.ResourceNotFoundException
NetworkManager.Client.exceptions.ThrottlingException
NetworkManager.Client.exceptions.InternalServerException


    :return: {
        'GlobalNetworks': [
            {
                'GlobalNetworkId': 'string',
                'GlobalNetworkArn': 'string',
                'Description': 'string',
                'CreatedAt': datetime(2015, 1, 1),
                'State': 'PENDING'|'AVAILABLE'|'DELETING'|'UPDATING',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    NetworkManager.Client.exceptions.ValidationException
    NetworkManager.Client.exceptions.AccessDeniedException
    NetworkManager.Client.exceptions.ResourceNotFoundException
    NetworkManager.Client.exceptions.ThrottlingException
    NetworkManager.Client.exceptions.InternalServerException
    
    """
    pass

def disassociate_customer_gateway(GlobalNetworkId=None, CustomerGatewayArn=None):
    """
    Disassociates a customer gateway from a device and a link.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_customer_gateway(
        GlobalNetworkId='string',
        CustomerGatewayArn='string'
    )
    
    
    :type GlobalNetworkId: string
    :param GlobalNetworkId: [REQUIRED]\nThe ID of the global network.\n

    :type CustomerGatewayArn: string
    :param CustomerGatewayArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the customer gateway. For more information, see Resources Defined by Amazon EC2 .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CustomerGatewayAssociation': {
        'CustomerGatewayArn': 'string',
        'GlobalNetworkId': 'string',
        'DeviceId': 'string',
        'LinkId': 'string',
        'State': 'PENDING'|'AVAILABLE'|'DELETING'|'DELETED'
    }
}


Response Structure

(dict) --

CustomerGatewayAssociation (dict) --
Information about the customer gateway association.

CustomerGatewayArn (string) --
The Amazon Resource Name (ARN) of the customer gateway.

GlobalNetworkId (string) --
The ID of the global network.

DeviceId (string) --
The ID of the device.

LinkId (string) --
The ID of the link.

State (string) --
The association state.









Exceptions

NetworkManager.Client.exceptions.ValidationException
NetworkManager.Client.exceptions.AccessDeniedException
NetworkManager.Client.exceptions.ResourceNotFoundException
NetworkManager.Client.exceptions.ConflictException
NetworkManager.Client.exceptions.ThrottlingException
NetworkManager.Client.exceptions.InternalServerException


    :return: {
        'CustomerGatewayAssociation': {
            'CustomerGatewayArn': 'string',
            'GlobalNetworkId': 'string',
            'DeviceId': 'string',
            'LinkId': 'string',
            'State': 'PENDING'|'AVAILABLE'|'DELETING'|'DELETED'
        }
    }
    
    
    :returns: 
    NetworkManager.Client.exceptions.ValidationException
    NetworkManager.Client.exceptions.AccessDeniedException
    NetworkManager.Client.exceptions.ResourceNotFoundException
    NetworkManager.Client.exceptions.ConflictException
    NetworkManager.Client.exceptions.ThrottlingException
    NetworkManager.Client.exceptions.InternalServerException
    
    """
    pass

def disassociate_link(GlobalNetworkId=None, DeviceId=None, LinkId=None):
    """
    Disassociates an existing device from a link. You must first disassociate any customer gateways that are associated with the link.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_link(
        GlobalNetworkId='string',
        DeviceId='string',
        LinkId='string'
    )
    
    
    :type GlobalNetworkId: string
    :param GlobalNetworkId: [REQUIRED]\nThe ID of the global network.\n

    :type DeviceId: string
    :param DeviceId: [REQUIRED]\nThe ID of the device.\n

    :type LinkId: string
    :param LinkId: [REQUIRED]\nThe ID of the link.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'LinkAssociation': {
        'GlobalNetworkId': 'string',
        'DeviceId': 'string',
        'LinkId': 'string',
        'LinkAssociationState': 'PENDING'|'AVAILABLE'|'DELETING'|'DELETED'
    }
}


Response Structure

(dict) --

LinkAssociation (dict) --
Information about the link association.

GlobalNetworkId (string) --
The ID of the global network.

DeviceId (string) --
The device ID for the link association.

LinkId (string) --
The ID of the link.

LinkAssociationState (string) --
The state of the association.









Exceptions

NetworkManager.Client.exceptions.ValidationException
NetworkManager.Client.exceptions.AccessDeniedException
NetworkManager.Client.exceptions.ResourceNotFoundException
NetworkManager.Client.exceptions.ConflictException
NetworkManager.Client.exceptions.ThrottlingException
NetworkManager.Client.exceptions.InternalServerException


    :return: {
        'LinkAssociation': {
            'GlobalNetworkId': 'string',
            'DeviceId': 'string',
            'LinkId': 'string',
            'LinkAssociationState': 'PENDING'|'AVAILABLE'|'DELETING'|'DELETED'
        }
    }
    
    
    :returns: 
    NetworkManager.Client.exceptions.ValidationException
    NetworkManager.Client.exceptions.AccessDeniedException
    NetworkManager.Client.exceptions.ResourceNotFoundException
    NetworkManager.Client.exceptions.ConflictException
    NetworkManager.Client.exceptions.ThrottlingException
    NetworkManager.Client.exceptions.InternalServerException
    
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

def get_customer_gateway_associations(GlobalNetworkId=None, CustomerGatewayArns=None, MaxResults=None, NextToken=None):
    """
    Gets the association information for customer gateways that are associated with devices and links in your global network.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_customer_gateway_associations(
        GlobalNetworkId='string',
        CustomerGatewayArns=[
            'string',
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type GlobalNetworkId: string
    :param GlobalNetworkId: [REQUIRED]\nThe ID of the global network.\n

    :type CustomerGatewayArns: list
    :param CustomerGatewayArns: One or more customer gateway Amazon Resource Names (ARNs). For more information, see Resources Defined by Amazon EC2 . The maximum is 10.\n\n(string) --\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return.

    :type NextToken: string
    :param NextToken: The token for the next page of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'CustomerGatewayAssociations': [
        {
            'CustomerGatewayArn': 'string',
            'GlobalNetworkId': 'string',
            'DeviceId': 'string',
            'LinkId': 'string',
            'State': 'PENDING'|'AVAILABLE'|'DELETING'|'DELETED'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

CustomerGatewayAssociations (list) --
The customer gateway associations.

(dict) --
Describes the association between a customer gateway, a device, and a link.

CustomerGatewayArn (string) --
The Amazon Resource Name (ARN) of the customer gateway.

GlobalNetworkId (string) --
The ID of the global network.

DeviceId (string) --
The ID of the device.

LinkId (string) --
The ID of the link.

State (string) --
The association state.





NextToken (string) --
The token for the next page of results.







Exceptions

NetworkManager.Client.exceptions.ValidationException
NetworkManager.Client.exceptions.AccessDeniedException
NetworkManager.Client.exceptions.ResourceNotFoundException
NetworkManager.Client.exceptions.ConflictException
NetworkManager.Client.exceptions.ThrottlingException
NetworkManager.Client.exceptions.InternalServerException


    :return: {
        'CustomerGatewayAssociations': [
            {
                'CustomerGatewayArn': 'string',
                'GlobalNetworkId': 'string',
                'DeviceId': 'string',
                'LinkId': 'string',
                'State': 'PENDING'|'AVAILABLE'|'DELETING'|'DELETED'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    NetworkManager.Client.exceptions.ValidationException
    NetworkManager.Client.exceptions.AccessDeniedException
    NetworkManager.Client.exceptions.ResourceNotFoundException
    NetworkManager.Client.exceptions.ConflictException
    NetworkManager.Client.exceptions.ThrottlingException
    NetworkManager.Client.exceptions.InternalServerException
    
    """
    pass

def get_devices(GlobalNetworkId=None, DeviceIds=None, SiteId=None, MaxResults=None, NextToken=None):
    """
    Gets information about one or more of your devices in a global network.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_devices(
        GlobalNetworkId='string',
        DeviceIds=[
            'string',
        ],
        SiteId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type GlobalNetworkId: string
    :param GlobalNetworkId: [REQUIRED]\nThe ID of the global network.\n

    :type DeviceIds: list
    :param DeviceIds: One or more device IDs. The maximum is 10.\n\n(string) --\n\n

    :type SiteId: string
    :param SiteId: The ID of the site.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return.

    :type NextToken: string
    :param NextToken: The token for the next page of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'Devices': [
        {
            'DeviceId': 'string',
            'DeviceArn': 'string',
            'GlobalNetworkId': 'string',
            'Description': 'string',
            'Type': 'string',
            'Vendor': 'string',
            'Model': 'string',
            'SerialNumber': 'string',
            'Location': {
                'Address': 'string',
                'Latitude': 'string',
                'Longitude': 'string'
            },
            'SiteId': 'string',
            'CreatedAt': datetime(2015, 1, 1),
            'State': 'PENDING'|'AVAILABLE'|'DELETING'|'UPDATING',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Devices (list) --
The devices.

(dict) --
Describes a device.

DeviceId (string) --
The ID of the device.

DeviceArn (string) --
The Amazon Resource Name (ARN) of the device.

GlobalNetworkId (string) --
The ID of the global network.

Description (string) --
The description of the device.

Type (string) --
The device type.

Vendor (string) --
The device vendor.

Model (string) --
The device model.

SerialNumber (string) --
The device serial number.

Location (dict) --
The site location.

Address (string) --
The physical address.

Latitude (string) --
The latitude.

Longitude (string) --
The longitude.



SiteId (string) --
The site ID.

CreatedAt (datetime) --
The date and time that the site was created.

State (string) --
The device state.

Tags (list) --
The tags for the device.

(dict) --
Describes a tag.

Key (string) --
The tag key.
Length Constraints: Maximum length of 128 characters.

Value (string) --
The tag value.
Length Constraints: Maximum length of 256 characters.









NextToken (string) --
The token for the next page of results.







Exceptions

NetworkManager.Client.exceptions.ValidationException
NetworkManager.Client.exceptions.AccessDeniedException
NetworkManager.Client.exceptions.ResourceNotFoundException
NetworkManager.Client.exceptions.ThrottlingException
NetworkManager.Client.exceptions.InternalServerException


    :return: {
        'Devices': [
            {
                'DeviceId': 'string',
                'DeviceArn': 'string',
                'GlobalNetworkId': 'string',
                'Description': 'string',
                'Type': 'string',
                'Vendor': 'string',
                'Model': 'string',
                'SerialNumber': 'string',
                'Location': {
                    'Address': 'string',
                    'Latitude': 'string',
                    'Longitude': 'string'
                },
                'SiteId': 'string',
                'CreatedAt': datetime(2015, 1, 1),
                'State': 'PENDING'|'AVAILABLE'|'DELETING'|'UPDATING',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    NetworkManager.Client.exceptions.ValidationException
    NetworkManager.Client.exceptions.AccessDeniedException
    NetworkManager.Client.exceptions.ResourceNotFoundException
    NetworkManager.Client.exceptions.ThrottlingException
    NetworkManager.Client.exceptions.InternalServerException
    
    """
    pass

def get_link_associations(GlobalNetworkId=None, DeviceId=None, LinkId=None, MaxResults=None, NextToken=None):
    """
    Gets the link associations for a device or a link. Either the device ID or the link ID must be specified.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_link_associations(
        GlobalNetworkId='string',
        DeviceId='string',
        LinkId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type GlobalNetworkId: string
    :param GlobalNetworkId: [REQUIRED]\nThe ID of the global network.\n

    :type DeviceId: string
    :param DeviceId: The ID of the device.

    :type LinkId: string
    :param LinkId: The ID of the link.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return.

    :type NextToken: string
    :param NextToken: The token for the next page of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'LinkAssociations': [
        {
            'GlobalNetworkId': 'string',
            'DeviceId': 'string',
            'LinkId': 'string',
            'LinkAssociationState': 'PENDING'|'AVAILABLE'|'DELETING'|'DELETED'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

LinkAssociations (list) --
The link associations.

(dict) --
Describes the association between a device and a link.

GlobalNetworkId (string) --
The ID of the global network.

DeviceId (string) --
The device ID for the link association.

LinkId (string) --
The ID of the link.

LinkAssociationState (string) --
The state of the association.





NextToken (string) --
The token for the next page of results.







Exceptions

NetworkManager.Client.exceptions.ValidationException
NetworkManager.Client.exceptions.AccessDeniedException
NetworkManager.Client.exceptions.ResourceNotFoundException
NetworkManager.Client.exceptions.ThrottlingException
NetworkManager.Client.exceptions.InternalServerException


    :return: {
        'LinkAssociations': [
            {
                'GlobalNetworkId': 'string',
                'DeviceId': 'string',
                'LinkId': 'string',
                'LinkAssociationState': 'PENDING'|'AVAILABLE'|'DELETING'|'DELETED'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    NetworkManager.Client.exceptions.ValidationException
    NetworkManager.Client.exceptions.AccessDeniedException
    NetworkManager.Client.exceptions.ResourceNotFoundException
    NetworkManager.Client.exceptions.ThrottlingException
    NetworkManager.Client.exceptions.InternalServerException
    
    """
    pass

def get_links(GlobalNetworkId=None, LinkIds=None, SiteId=None, Type=None, Provider=None, MaxResults=None, NextToken=None):
    """
    Gets information about one or more links in a specified global network.
    If you specify the site ID, you cannot specify the type or provider in the same request. You can specify the type and provider in the same request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_links(
        GlobalNetworkId='string',
        LinkIds=[
            'string',
        ],
        SiteId='string',
        Type='string',
        Provider='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type GlobalNetworkId: string
    :param GlobalNetworkId: [REQUIRED]\nThe ID of the global network.\n

    :type LinkIds: list
    :param LinkIds: One or more link IDs. The maximum is 10.\n\n(string) --\n\n

    :type SiteId: string
    :param SiteId: The ID of the site.

    :type Type: string
    :param Type: The link type.

    :type Provider: string
    :param Provider: The link provider.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return.

    :type NextToken: string
    :param NextToken: The token for the next page of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'Links': [
        {
            'LinkId': 'string',
            'LinkArn': 'string',
            'GlobalNetworkId': 'string',
            'SiteId': 'string',
            'Description': 'string',
            'Type': 'string',
            'Bandwidth': {
                'UploadSpeed': 123,
                'DownloadSpeed': 123
            },
            'Provider': 'string',
            'CreatedAt': datetime(2015, 1, 1),
            'State': 'PENDING'|'AVAILABLE'|'DELETING'|'UPDATING',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Links (list) --
The links.

(dict) --
Describes a link.

LinkId (string) --
The ID of the link.

LinkArn (string) --
The Amazon Resource Name (ARN) of the link.

GlobalNetworkId (string) --
The ID of the global network.

SiteId (string) --
The ID of the site.

Description (string) --
The description of the link.

Type (string) --
The type of the link.

Bandwidth (dict) --
The bandwidth for the link.

UploadSpeed (integer) --
Upload speed in Mbps.

DownloadSpeed (integer) --
Download speed in Mbps.



Provider (string) --
The provider of the link.

CreatedAt (datetime) --
The date and time that the link was created.

State (string) --
The state of the link.

Tags (list) --
The tags for the link.

(dict) --
Describes a tag.

Key (string) --
The tag key.
Length Constraints: Maximum length of 128 characters.

Value (string) --
The tag value.
Length Constraints: Maximum length of 256 characters.









NextToken (string) --
The token for the next page of results.







Exceptions

NetworkManager.Client.exceptions.ValidationException
NetworkManager.Client.exceptions.AccessDeniedException
NetworkManager.Client.exceptions.ResourceNotFoundException
NetworkManager.Client.exceptions.ThrottlingException
NetworkManager.Client.exceptions.InternalServerException


    :return: {
        'Links': [
            {
                'LinkId': 'string',
                'LinkArn': 'string',
                'GlobalNetworkId': 'string',
                'SiteId': 'string',
                'Description': 'string',
                'Type': 'string',
                'Bandwidth': {
                    'UploadSpeed': 123,
                    'DownloadSpeed': 123
                },
                'Provider': 'string',
                'CreatedAt': datetime(2015, 1, 1),
                'State': 'PENDING'|'AVAILABLE'|'DELETING'|'UPDATING',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    NetworkManager.Client.exceptions.ValidationException
    NetworkManager.Client.exceptions.AccessDeniedException
    NetworkManager.Client.exceptions.ResourceNotFoundException
    NetworkManager.Client.exceptions.ThrottlingException
    NetworkManager.Client.exceptions.InternalServerException
    
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

def get_sites(GlobalNetworkId=None, SiteIds=None, MaxResults=None, NextToken=None):
    """
    Gets information about one or more of your sites in a global network.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_sites(
        GlobalNetworkId='string',
        SiteIds=[
            'string',
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type GlobalNetworkId: string
    :param GlobalNetworkId: [REQUIRED]\nThe ID of the global network.\n

    :type SiteIds: list
    :param SiteIds: One or more site IDs. The maximum is 10.\n\n(string) --\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return.

    :type NextToken: string
    :param NextToken: The token for the next page of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'Sites': [
        {
            'SiteId': 'string',
            'SiteArn': 'string',
            'GlobalNetworkId': 'string',
            'Description': 'string',
            'Location': {
                'Address': 'string',
                'Latitude': 'string',
                'Longitude': 'string'
            },
            'CreatedAt': datetime(2015, 1, 1),
            'State': 'PENDING'|'AVAILABLE'|'DELETING'|'UPDATING',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Sites (list) --
The sites.

(dict) --
Describes a site.

SiteId (string) --
The ID of the site.

SiteArn (string) --
The Amazon Resource Name (ARN) of the site.

GlobalNetworkId (string) --
The ID of the global network.

Description (string) --
The description of the site.

Location (dict) --
The location of the site.

Address (string) --
The physical address.

Latitude (string) --
The latitude.

Longitude (string) --
The longitude.



CreatedAt (datetime) --
The date and time that the site was created.

State (string) --
The state of the site.

Tags (list) --
The tags for the site.

(dict) --
Describes a tag.

Key (string) --
The tag key.
Length Constraints: Maximum length of 128 characters.

Value (string) --
The tag value.
Length Constraints: Maximum length of 256 characters.









NextToken (string) --
The token for the next page of results.







Exceptions

NetworkManager.Client.exceptions.ValidationException
NetworkManager.Client.exceptions.AccessDeniedException
NetworkManager.Client.exceptions.ResourceNotFoundException
NetworkManager.Client.exceptions.ThrottlingException
NetworkManager.Client.exceptions.InternalServerException


    :return: {
        'Sites': [
            {
                'SiteId': 'string',
                'SiteArn': 'string',
                'GlobalNetworkId': 'string',
                'Description': 'string',
                'Location': {
                    'Address': 'string',
                    'Latitude': 'string',
                    'Longitude': 'string'
                },
                'CreatedAt': datetime(2015, 1, 1),
                'State': 'PENDING'|'AVAILABLE'|'DELETING'|'UPDATING',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    NetworkManager.Client.exceptions.ValidationException
    NetworkManager.Client.exceptions.AccessDeniedException
    NetworkManager.Client.exceptions.ResourceNotFoundException
    NetworkManager.Client.exceptions.ThrottlingException
    NetworkManager.Client.exceptions.InternalServerException
    
    """
    pass

def get_transit_gateway_registrations(GlobalNetworkId=None, TransitGatewayArns=None, MaxResults=None, NextToken=None):
    """
    Gets information about the transit gateway registrations in a specified global network.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_transit_gateway_registrations(
        GlobalNetworkId='string',
        TransitGatewayArns=[
            'string',
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type GlobalNetworkId: string
    :param GlobalNetworkId: [REQUIRED]\nThe ID of the global network.\n

    :type TransitGatewayArns: list
    :param TransitGatewayArns: The Amazon Resource Names (ARNs) of one or more transit gateways. The maximum is 10.\n\n(string) --\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return.

    :type NextToken: string
    :param NextToken: The token for the next page of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'TransitGatewayRegistrations': [
        {
            'GlobalNetworkId': 'string',
            'TransitGatewayArn': 'string',
            'State': {
                'Code': 'PENDING'|'AVAILABLE'|'DELETING'|'DELETED'|'FAILED',
                'Message': 'string'
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

TransitGatewayRegistrations (list) --
The transit gateway registrations.

(dict) --
Describes the registration of a transit gateway to a global network.

GlobalNetworkId (string) --
The ID of the global network.

TransitGatewayArn (string) --
The Amazon Resource Name (ARN) of the transit gateway.

State (dict) --
The state of the transit gateway registration.

Code (string) --
The code for the state reason.

Message (string) --
The message for the state reason.







NextToken (string) --
The token for the next page of results.







Exceptions

NetworkManager.Client.exceptions.ValidationException
NetworkManager.Client.exceptions.AccessDeniedException
NetworkManager.Client.exceptions.ResourceNotFoundException
NetworkManager.Client.exceptions.ThrottlingException
NetworkManager.Client.exceptions.InternalServerException


    :return: {
        'TransitGatewayRegistrations': [
            {
                'GlobalNetworkId': 'string',
                'TransitGatewayArn': 'string',
                'State': {
                    'Code': 'PENDING'|'AVAILABLE'|'DELETING'|'DELETED'|'FAILED',
                    'Message': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    NetworkManager.Client.exceptions.ValidationException
    NetworkManager.Client.exceptions.AccessDeniedException
    NetworkManager.Client.exceptions.ResourceNotFoundException
    NetworkManager.Client.exceptions.ThrottlingException
    NetworkManager.Client.exceptions.InternalServerException
    
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

def list_tags_for_resource(ResourceArn=None):
    """
    Lists the tags for a specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource.\n

    :rtype: dict
ReturnsResponse Syntax{
    'TagList': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --
TagList (list) --The list of tags.

(dict) --Describes a tag.

Key (string) --The tag key.
Length Constraints: Maximum length of 128 characters.

Value (string) --The tag value.
Length Constraints: Maximum length of 256 characters.










Exceptions

NetworkManager.Client.exceptions.ValidationException
NetworkManager.Client.exceptions.AccessDeniedException
NetworkManager.Client.exceptions.ResourceNotFoundException
NetworkManager.Client.exceptions.ThrottlingException
NetworkManager.Client.exceptions.InternalServerException


    :return: {
        'TagList': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    """
    pass

def register_transit_gateway(GlobalNetworkId=None, TransitGatewayArn=None):
    """
    Registers a transit gateway in your global network. The transit gateway can be in any AWS Region, but it must be owned by the same AWS account that owns the global network. You cannot register a transit gateway in more than one global network.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_transit_gateway(
        GlobalNetworkId='string',
        TransitGatewayArn='string'
    )
    
    
    :type GlobalNetworkId: string
    :param GlobalNetworkId: [REQUIRED]\nThe ID of the global network.\n

    :type TransitGatewayArn: string
    :param TransitGatewayArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the transit gateway. For more information, see Resources Defined by Amazon EC2 .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TransitGatewayRegistration': {
        'GlobalNetworkId': 'string',
        'TransitGatewayArn': 'string',
        'State': {
            'Code': 'PENDING'|'AVAILABLE'|'DELETING'|'DELETED'|'FAILED',
            'Message': 'string'
        }
    }
}


Response Structure

(dict) --

TransitGatewayRegistration (dict) --
Information about the transit gateway registration.

GlobalNetworkId (string) --
The ID of the global network.

TransitGatewayArn (string) --
The Amazon Resource Name (ARN) of the transit gateway.

State (dict) --
The state of the transit gateway registration.

Code (string) --
The code for the state reason.

Message (string) --
The message for the state reason.











Exceptions

NetworkManager.Client.exceptions.ValidationException
NetworkManager.Client.exceptions.AccessDeniedException
NetworkManager.Client.exceptions.ResourceNotFoundException
NetworkManager.Client.exceptions.ConflictException
NetworkManager.Client.exceptions.ThrottlingException
NetworkManager.Client.exceptions.InternalServerException


    :return: {
        'TransitGatewayRegistration': {
            'GlobalNetworkId': 'string',
            'TransitGatewayArn': 'string',
            'State': {
                'Code': 'PENDING'|'AVAILABLE'|'DELETING'|'DELETED'|'FAILED',
                'Message': 'string'
            }
        }
    }
    
    
    :returns: 
    NetworkManager.Client.exceptions.ValidationException
    NetworkManager.Client.exceptions.AccessDeniedException
    NetworkManager.Client.exceptions.ResourceNotFoundException
    NetworkManager.Client.exceptions.ConflictException
    NetworkManager.Client.exceptions.ThrottlingException
    NetworkManager.Client.exceptions.InternalServerException
    
    """
    pass

def tag_resource(ResourceArn=None, Tags=None):
    """
    Tags a specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceArn='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nThe tags to apply to the specified resource.\n\n(dict) --Describes a tag.\n\nKey (string) --The tag key.\nLength Constraints: Maximum length of 128 characters.\n\nValue (string) --The tag value.\nLength Constraints: Maximum length of 256 characters.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

NetworkManager.Client.exceptions.ValidationException
NetworkManager.Client.exceptions.ServiceQuotaExceededException
NetworkManager.Client.exceptions.AccessDeniedException
NetworkManager.Client.exceptions.ResourceNotFoundException
NetworkManager.Client.exceptions.ConflictException
NetworkManager.Client.exceptions.ThrottlingException
NetworkManager.Client.exceptions.InternalServerException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceArn=None, TagKeys=None):
    """
    Removes tags from a specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe tag keys to remove from the specified resource.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

NetworkManager.Client.exceptions.ValidationException
NetworkManager.Client.exceptions.AccessDeniedException
NetworkManager.Client.exceptions.ResourceNotFoundException
NetworkManager.Client.exceptions.ConflictException
NetworkManager.Client.exceptions.ThrottlingException
NetworkManager.Client.exceptions.InternalServerException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_device(GlobalNetworkId=None, DeviceId=None, Description=None, Type=None, Vendor=None, Model=None, SerialNumber=None, Location=None, SiteId=None):
    """
    Updates the details for an existing device. To remove information for any of the parameters, specify an empty string.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_device(
        GlobalNetworkId='string',
        DeviceId='string',
        Description='string',
        Type='string',
        Vendor='string',
        Model='string',
        SerialNumber='string',
        Location={
            'Address': 'string',
            'Latitude': 'string',
            'Longitude': 'string'
        },
        SiteId='string'
    )
    
    
    :type GlobalNetworkId: string
    :param GlobalNetworkId: [REQUIRED]\nThe ID of the global network.\n

    :type DeviceId: string
    :param DeviceId: [REQUIRED]\nThe ID of the device.\n

    :type Description: string
    :param Description: A description of the device.\nLength Constraints: Maximum length of 256 characters.\n

    :type Type: string
    :param Type: The type of the device.

    :type Vendor: string
    :param Vendor: The vendor of the device.\nLength Constraints: Maximum length of 128 characters.\n

    :type Model: string
    :param Model: The model of the device.\nLength Constraints: Maximum length of 128 characters.\n

    :type SerialNumber: string
    :param SerialNumber: The serial number of the device.\nLength Constraints: Maximum length of 128 characters.\n

    :type Location: dict
    :param Location: Describes a location.\n\nAddress (string) --The physical address.\n\nLatitude (string) --The latitude.\n\nLongitude (string) --The longitude.\n\n\n

    :type SiteId: string
    :param SiteId: The ID of the site.

    :rtype: dict

ReturnsResponse Syntax
{
    'Device': {
        'DeviceId': 'string',
        'DeviceArn': 'string',
        'GlobalNetworkId': 'string',
        'Description': 'string',
        'Type': 'string',
        'Vendor': 'string',
        'Model': 'string',
        'SerialNumber': 'string',
        'Location': {
            'Address': 'string',
            'Latitude': 'string',
            'Longitude': 'string'
        },
        'SiteId': 'string',
        'CreatedAt': datetime(2015, 1, 1),
        'State': 'PENDING'|'AVAILABLE'|'DELETING'|'UPDATING',
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

Device (dict) --
Information about the device.

DeviceId (string) --
The ID of the device.

DeviceArn (string) --
The Amazon Resource Name (ARN) of the device.

GlobalNetworkId (string) --
The ID of the global network.

Description (string) --
The description of the device.

Type (string) --
The device type.

Vendor (string) --
The device vendor.

Model (string) --
The device model.

SerialNumber (string) --
The device serial number.

Location (dict) --
The site location.

Address (string) --
The physical address.

Latitude (string) --
The latitude.

Longitude (string) --
The longitude.



SiteId (string) --
The site ID.

CreatedAt (datetime) --
The date and time that the site was created.

State (string) --
The device state.

Tags (list) --
The tags for the device.

(dict) --
Describes a tag.

Key (string) --
The tag key.
Length Constraints: Maximum length of 128 characters.

Value (string) --
The tag value.
Length Constraints: Maximum length of 256 characters.













Exceptions

NetworkManager.Client.exceptions.ValidationException
NetworkManager.Client.exceptions.AccessDeniedException
NetworkManager.Client.exceptions.ResourceNotFoundException
NetworkManager.Client.exceptions.ConflictException
NetworkManager.Client.exceptions.ThrottlingException
NetworkManager.Client.exceptions.InternalServerException


    :return: {
        'Device': {
            'DeviceId': 'string',
            'DeviceArn': 'string',
            'GlobalNetworkId': 'string',
            'Description': 'string',
            'Type': 'string',
            'Vendor': 'string',
            'Model': 'string',
            'SerialNumber': 'string',
            'Location': {
                'Address': 'string',
                'Latitude': 'string',
                'Longitude': 'string'
            },
            'SiteId': 'string',
            'CreatedAt': datetime(2015, 1, 1),
            'State': 'PENDING'|'AVAILABLE'|'DELETING'|'UPDATING',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    NetworkManager.Client.exceptions.ValidationException
    NetworkManager.Client.exceptions.AccessDeniedException
    NetworkManager.Client.exceptions.ResourceNotFoundException
    NetworkManager.Client.exceptions.ConflictException
    NetworkManager.Client.exceptions.ThrottlingException
    NetworkManager.Client.exceptions.InternalServerException
    
    """
    pass

def update_global_network(GlobalNetworkId=None, Description=None):
    """
    Updates an existing global network. To remove information for any of the parameters, specify an empty string.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_global_network(
        GlobalNetworkId='string',
        Description='string'
    )
    
    
    :type GlobalNetworkId: string
    :param GlobalNetworkId: [REQUIRED]\nThe ID of your global network.\n

    :type Description: string
    :param Description: A description of the global network.\nLength Constraints: Maximum length of 256 characters.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GlobalNetwork': {
        'GlobalNetworkId': 'string',
        'GlobalNetworkArn': 'string',
        'Description': 'string',
        'CreatedAt': datetime(2015, 1, 1),
        'State': 'PENDING'|'AVAILABLE'|'DELETING'|'UPDATING',
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

GlobalNetwork (dict) --
Information about the global network object.

GlobalNetworkId (string) --
The ID of the global network.

GlobalNetworkArn (string) --
The Amazon Resource Name (ARN) of the global network.

Description (string) --
The description of the global network.

CreatedAt (datetime) --
The date and time that the global network was created.

State (string) --
The state of the global network.

Tags (list) --
The tags for the global network.

(dict) --
Describes a tag.

Key (string) --
The tag key.
Length Constraints: Maximum length of 128 characters.

Value (string) --
The tag value.
Length Constraints: Maximum length of 256 characters.













Exceptions

NetworkManager.Client.exceptions.ValidationException
NetworkManager.Client.exceptions.AccessDeniedException
NetworkManager.Client.exceptions.ResourceNotFoundException
NetworkManager.Client.exceptions.ConflictException
NetworkManager.Client.exceptions.ThrottlingException
NetworkManager.Client.exceptions.InternalServerException


    :return: {
        'GlobalNetwork': {
            'GlobalNetworkId': 'string',
            'GlobalNetworkArn': 'string',
            'Description': 'string',
            'CreatedAt': datetime(2015, 1, 1),
            'State': 'PENDING'|'AVAILABLE'|'DELETING'|'UPDATING',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    NetworkManager.Client.exceptions.ValidationException
    NetworkManager.Client.exceptions.AccessDeniedException
    NetworkManager.Client.exceptions.ResourceNotFoundException
    NetworkManager.Client.exceptions.ConflictException
    NetworkManager.Client.exceptions.ThrottlingException
    NetworkManager.Client.exceptions.InternalServerException
    
    """
    pass

def update_link(GlobalNetworkId=None, LinkId=None, Description=None, Type=None, Bandwidth=None, Provider=None):
    """
    Updates the details for an existing link. To remove information for any of the parameters, specify an empty string.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_link(
        GlobalNetworkId='string',
        LinkId='string',
        Description='string',
        Type='string',
        Bandwidth={
            'UploadSpeed': 123,
            'DownloadSpeed': 123
        },
        Provider='string'
    )
    
    
    :type GlobalNetworkId: string
    :param GlobalNetworkId: [REQUIRED]\nThe ID of the global network.\n

    :type LinkId: string
    :param LinkId: [REQUIRED]\nThe ID of the link.\n

    :type Description: string
    :param Description: A description of the link.\nLength Constraints: Maximum length of 256 characters.\n

    :type Type: string
    :param Type: The type of the link.\nLength Constraints: Maximum length of 128 characters.\n

    :type Bandwidth: dict
    :param Bandwidth: The upload and download speed in Mbps.\n\nUploadSpeed (integer) --Upload speed in Mbps.\n\nDownloadSpeed (integer) --Download speed in Mbps.\n\n\n

    :type Provider: string
    :param Provider: The provider of the link.\nLength Constraints: Maximum length of 128 characters.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Link': {
        'LinkId': 'string',
        'LinkArn': 'string',
        'GlobalNetworkId': 'string',
        'SiteId': 'string',
        'Description': 'string',
        'Type': 'string',
        'Bandwidth': {
            'UploadSpeed': 123,
            'DownloadSpeed': 123
        },
        'Provider': 'string',
        'CreatedAt': datetime(2015, 1, 1),
        'State': 'PENDING'|'AVAILABLE'|'DELETING'|'UPDATING',
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

Link (dict) --
Information about the link.

LinkId (string) --
The ID of the link.

LinkArn (string) --
The Amazon Resource Name (ARN) of the link.

GlobalNetworkId (string) --
The ID of the global network.

SiteId (string) --
The ID of the site.

Description (string) --
The description of the link.

Type (string) --
The type of the link.

Bandwidth (dict) --
The bandwidth for the link.

UploadSpeed (integer) --
Upload speed in Mbps.

DownloadSpeed (integer) --
Download speed in Mbps.



Provider (string) --
The provider of the link.

CreatedAt (datetime) --
The date and time that the link was created.

State (string) --
The state of the link.

Tags (list) --
The tags for the link.

(dict) --
Describes a tag.

Key (string) --
The tag key.
Length Constraints: Maximum length of 128 characters.

Value (string) --
The tag value.
Length Constraints: Maximum length of 256 characters.













Exceptions

NetworkManager.Client.exceptions.ValidationException
NetworkManager.Client.exceptions.ServiceQuotaExceededException
NetworkManager.Client.exceptions.AccessDeniedException
NetworkManager.Client.exceptions.ResourceNotFoundException
NetworkManager.Client.exceptions.ConflictException
NetworkManager.Client.exceptions.ThrottlingException
NetworkManager.Client.exceptions.InternalServerException


    :return: {
        'Link': {
            'LinkId': 'string',
            'LinkArn': 'string',
            'GlobalNetworkId': 'string',
            'SiteId': 'string',
            'Description': 'string',
            'Type': 'string',
            'Bandwidth': {
                'UploadSpeed': 123,
                'DownloadSpeed': 123
            },
            'Provider': 'string',
            'CreatedAt': datetime(2015, 1, 1),
            'State': 'PENDING'|'AVAILABLE'|'DELETING'|'UPDATING',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    NetworkManager.Client.exceptions.ValidationException
    NetworkManager.Client.exceptions.ServiceQuotaExceededException
    NetworkManager.Client.exceptions.AccessDeniedException
    NetworkManager.Client.exceptions.ResourceNotFoundException
    NetworkManager.Client.exceptions.ConflictException
    NetworkManager.Client.exceptions.ThrottlingException
    NetworkManager.Client.exceptions.InternalServerException
    
    """
    pass

def update_site(GlobalNetworkId=None, SiteId=None, Description=None, Location=None):
    """
    Updates the information for an existing site. To remove information for any of the parameters, specify an empty string.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_site(
        GlobalNetworkId='string',
        SiteId='string',
        Description='string',
        Location={
            'Address': 'string',
            'Latitude': 'string',
            'Longitude': 'string'
        }
    )
    
    
    :type GlobalNetworkId: string
    :param GlobalNetworkId: [REQUIRED]\nThe ID of the global network.\n

    :type SiteId: string
    :param SiteId: [REQUIRED]\nThe ID of your site.\n

    :type Description: string
    :param Description: A description of your site.\nLength Constraints: Maximum length of 256 characters.\n

    :type Location: dict
    :param Location: The site location:\n\nAddress : The physical address of the site.\nLatitude : The latitude of the site.\nLongitude : The longitude of the site.\n\n\nAddress (string) --The physical address.\n\nLatitude (string) --The latitude.\n\nLongitude (string) --The longitude.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Site': {
        'SiteId': 'string',
        'SiteArn': 'string',
        'GlobalNetworkId': 'string',
        'Description': 'string',
        'Location': {
            'Address': 'string',
            'Latitude': 'string',
            'Longitude': 'string'
        },
        'CreatedAt': datetime(2015, 1, 1),
        'State': 'PENDING'|'AVAILABLE'|'DELETING'|'UPDATING',
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

Site (dict) --
Information about the site.

SiteId (string) --
The ID of the site.

SiteArn (string) --
The Amazon Resource Name (ARN) of the site.

GlobalNetworkId (string) --
The ID of the global network.

Description (string) --
The description of the site.

Location (dict) --
The location of the site.

Address (string) --
The physical address.

Latitude (string) --
The latitude.

Longitude (string) --
The longitude.



CreatedAt (datetime) --
The date and time that the site was created.

State (string) --
The state of the site.

Tags (list) --
The tags for the site.

(dict) --
Describes a tag.

Key (string) --
The tag key.
Length Constraints: Maximum length of 128 characters.

Value (string) --
The tag value.
Length Constraints: Maximum length of 256 characters.













Exceptions

NetworkManager.Client.exceptions.ValidationException
NetworkManager.Client.exceptions.AccessDeniedException
NetworkManager.Client.exceptions.ResourceNotFoundException
NetworkManager.Client.exceptions.ConflictException
NetworkManager.Client.exceptions.ThrottlingException
NetworkManager.Client.exceptions.InternalServerException


    :return: {
        'Site': {
            'SiteId': 'string',
            'SiteArn': 'string',
            'GlobalNetworkId': 'string',
            'Description': 'string',
            'Location': {
                'Address': 'string',
                'Latitude': 'string',
                'Longitude': 'string'
            },
            'CreatedAt': datetime(2015, 1, 1),
            'State': 'PENDING'|'AVAILABLE'|'DELETING'|'UPDATING',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    NetworkManager.Client.exceptions.ValidationException
    NetworkManager.Client.exceptions.AccessDeniedException
    NetworkManager.Client.exceptions.ResourceNotFoundException
    NetworkManager.Client.exceptions.ConflictException
    NetworkManager.Client.exceptions.ThrottlingException
    NetworkManager.Client.exceptions.InternalServerException
    
    """
    pass

