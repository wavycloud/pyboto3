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

def create_license_configuration(Name=None, Description=None, LicenseCountingType=None, LicenseCount=None, LicenseCountHardLimit=None, LicenseRules=None, Tags=None, ProductInformationList=None):
    """
    Creates a license configuration.
    A license configuration is an abstraction of a customer license agreement that can be consumed and enforced by License Manager. Components include specifications for the license type (licensing by instance, socket, CPU, or vCPU), allowed tenancy (shared tenancy, Dedicated Instance, Dedicated Host, or all of these), host affinity (how long a VM must be associated with a host), and the number of licenses purchased and used.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_license_configuration(
        Name='string',
        Description='string',
        LicenseCountingType='vCPU'|'Instance'|'Core'|'Socket',
        LicenseCount=123,
        LicenseCountHardLimit=True|False,
        LicenseRules=[
            'string',
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        ProductInformationList=[
            {
                'ResourceType': 'string',
                'ProductInformationFilterList': [
                    {
                        'ProductInformationFilterName': 'string',
                        'ProductInformationFilterValue': [
                            'string',
                        ],
                        'ProductInformationFilterComparator': 'string'
                    },
                ]
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nName of the license configuration.\n

    :type Description: string
    :param Description: Description of the license configuration.

    :type LicenseCountingType: string
    :param LicenseCountingType: [REQUIRED]\nDimension used to track the license inventory.\n

    :type LicenseCount: integer
    :param LicenseCount: Number of licenses managed by the license configuration.

    :type LicenseCountHardLimit: boolean
    :param LicenseCountHardLimit: Indicates whether hard or soft license enforcement is used. Exceeding a hard limit blocks the launch of new instances.

    :type LicenseRules: list
    :param LicenseRules: License rules. The syntax is #name=value (for example, #allowedTenancy=EC2-DedicatedHost). Available rules vary by dimension.\n\nCores dimension: allowedTenancy | maximumCores | minimumCores\nInstances dimension: allowedTenancy | maximumCores | minimumCores | maximumSockets | minimumSockets | maximumVcpus | minimumVcpus\nSockets dimension: allowedTenancy | maximumSockets | minimumSockets\nvCPUs dimension: allowedTenancy | honorVcpuOptimization | maximumVcpus | minimumVcpus\n\n\n(string) --\n\n

    :type Tags: list
    :param Tags: Tags to add to the license configuration.\n\n(dict) --Details about a tag for a license configuration.\n\nKey (string) --Tag key.\n\nValue (string) --Tag value.\n\n\n\n\n

    :type ProductInformationList: list
    :param ProductInformationList: Product information.\n\n(dict) --Describes product information for a license configuration.\n\nResourceType (string) -- [REQUIRED]Resource type. The value is SSM_MANAGED .\n\nProductInformationFilterList (list) -- [REQUIRED]Product information filters. The following filters and logical operators are supported:\n\nApplication Name - The name of the application. Logical operator is EQUALS .\nApplication Publisher - The publisher of the application. Logical operator is EQUALS .\nApplication Version - The version of the application. Logical operator is EQUALS .\nPlatform Name - The name of the platform. Logical operator is EQUALS .\nPlatform Type - The platform type. Logical operator is EQUALS .\nLicense Included - The type of license included. Logical operators are EQUALS and NOT_EQUALS . Possible values are sql-server-enterprise | sql-server-standard | sql-server-web | windows-server-datacenter .\n\n\n(dict) --Describes product information filters.\n\nProductInformationFilterName (string) -- [REQUIRED]Filter name.\n\nProductInformationFilterValue (list) -- [REQUIRED]Filter value.\n\n(string) --\n\n\nProductInformationFilterComparator (string) -- [REQUIRED]Logical operator.\n\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'LicenseConfigurationArn': 'string'
}


Response Structure

(dict) --

LicenseConfigurationArn (string) --
Amazon Resource Name (ARN) of the license configuration.







Exceptions

LicenseManager.Client.exceptions.InvalidParameterValueException
LicenseManager.Client.exceptions.ServerInternalException
LicenseManager.Client.exceptions.ResourceLimitExceededException
LicenseManager.Client.exceptions.AuthorizationException
LicenseManager.Client.exceptions.AccessDeniedException
LicenseManager.Client.exceptions.RateLimitExceededException


    :return: {
        'LicenseConfigurationArn': 'string'
    }
    
    
    :returns: 
    LicenseManager.Client.exceptions.InvalidParameterValueException
    LicenseManager.Client.exceptions.ServerInternalException
    LicenseManager.Client.exceptions.ResourceLimitExceededException
    LicenseManager.Client.exceptions.AuthorizationException
    LicenseManager.Client.exceptions.AccessDeniedException
    LicenseManager.Client.exceptions.RateLimitExceededException
    
    """
    pass

def delete_license_configuration(LicenseConfigurationArn=None):
    """
    Deletes the specified license configuration.
    You cannot delete a license configuration that is in use.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_license_configuration(
        LicenseConfigurationArn='string'
    )
    
    
    :type LicenseConfigurationArn: string
    :param LicenseConfigurationArn: [REQUIRED]\nID of the license configuration.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

LicenseManager.Client.exceptions.InvalidParameterValueException
LicenseManager.Client.exceptions.ServerInternalException
LicenseManager.Client.exceptions.AuthorizationException
LicenseManager.Client.exceptions.AccessDeniedException
LicenseManager.Client.exceptions.RateLimitExceededException


    :return: {}
    
    
    :returns: 
    LicenseManager.Client.exceptions.InvalidParameterValueException
    LicenseManager.Client.exceptions.ServerInternalException
    LicenseManager.Client.exceptions.AuthorizationException
    LicenseManager.Client.exceptions.AccessDeniedException
    LicenseManager.Client.exceptions.RateLimitExceededException
    
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

def get_license_configuration(LicenseConfigurationArn=None):
    """
    Gets detailed information about the specified license configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_license_configuration(
        LicenseConfigurationArn='string'
    )
    
    
    :type LicenseConfigurationArn: string
    :param LicenseConfigurationArn: [REQUIRED]\nAmazon Resource Name (ARN) of the license configuration.\n

    :rtype: dict
ReturnsResponse Syntax{
    'LicenseConfigurationId': 'string',
    'LicenseConfigurationArn': 'string',
    'Name': 'string',
    'Description': 'string',
    'LicenseCountingType': 'vCPU'|'Instance'|'Core'|'Socket',
    'LicenseRules': [
        'string',
    ],
    'LicenseCount': 123,
    'LicenseCountHardLimit': True|False,
    'ConsumedLicenses': 123,
    'Status': 'string',
    'OwnerAccountId': 'string',
    'ConsumedLicenseSummaryList': [
        {
            'ResourceType': 'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI'|'RDS'|'SYSTEMS_MANAGER_MANAGED_INSTANCE',
            'ConsumedLicenses': 123
        },
    ],
    'ManagedResourceSummaryList': [
        {
            'ResourceType': 'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI'|'RDS'|'SYSTEMS_MANAGER_MANAGED_INSTANCE',
            'AssociationCount': 123
        },
    ],
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ],
    'ProductInformationList': [
        {
            'ResourceType': 'string',
            'ProductInformationFilterList': [
                {
                    'ProductInformationFilterName': 'string',
                    'ProductInformationFilterValue': [
                        'string',
                    ],
                    'ProductInformationFilterComparator': 'string'
                },
            ]
        },
    ],
    'AutomatedDiscoveryInformation': {
        'LastRunTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
LicenseConfigurationId (string) --Unique ID for the license configuration.

LicenseConfigurationArn (string) --Amazon Resource Name (ARN) of the license configuration.

Name (string) --Name of the license configuration.

Description (string) --Description of the license configuration.

LicenseCountingType (string) --Dimension on which the licenses are counted.

LicenseRules (list) --License rules.

(string) --


LicenseCount (integer) --Number of available licenses.

LicenseCountHardLimit (boolean) --Sets the number of available licenses as a hard limit.

ConsumedLicenses (integer) --Number of licenses assigned to resources.

Status (string) --License configuration status.

OwnerAccountId (string) --Account ID of the owner of the license configuration.

ConsumedLicenseSummaryList (list) --Summaries of the licenses consumed by resources.

(dict) --Details about license consumption.

ResourceType (string) --Resource type of the resource consuming a license.

ConsumedLicenses (integer) --Number of licenses consumed by the resource.





ManagedResourceSummaryList (list) --Summaries of the managed resources.

(dict) --Summary information about a managed resource.

ResourceType (string) --Type of resource associated with a license.

AssociationCount (integer) --Number of resources associated with licenses.





Tags (list) --Tags for the license configuration.

(dict) --Details about a tag for a license configuration.

Key (string) --Tag key.

Value (string) --Tag value.





ProductInformationList (list) --Product information.

(dict) --Describes product information for a license configuration.

ResourceType (string) --Resource type. The value is SSM_MANAGED .

ProductInformationFilterList (list) --Product information filters. The following filters and logical operators are supported:

Application Name - The name of the application. Logical operator is EQUALS .
Application Publisher - The publisher of the application. Logical operator is EQUALS .
Application Version - The version of the application. Logical operator is EQUALS .
Platform Name - The name of the platform. Logical operator is EQUALS .
Platform Type - The platform type. Logical operator is EQUALS .
License Included - The type of license included. Logical operators are EQUALS and NOT_EQUALS . Possible values are sql-server-enterprise | sql-server-standard | sql-server-web | windows-server-datacenter .


(dict) --Describes product information filters.

ProductInformationFilterName (string) --Filter name.

ProductInformationFilterValue (list) --Filter value.

(string) --


ProductInformationFilterComparator (string) --Logical operator.









AutomatedDiscoveryInformation (dict) --Automated discovery information.

LastRunTime (datetime) --Time that automated discovery last ran.








Exceptions

LicenseManager.Client.exceptions.InvalidParameterValueException
LicenseManager.Client.exceptions.ServerInternalException
LicenseManager.Client.exceptions.AuthorizationException
LicenseManager.Client.exceptions.AccessDeniedException
LicenseManager.Client.exceptions.RateLimitExceededException


    :return: {
        'LicenseConfigurationId': 'string',
        'LicenseConfigurationArn': 'string',
        'Name': 'string',
        'Description': 'string',
        'LicenseCountingType': 'vCPU'|'Instance'|'Core'|'Socket',
        'LicenseRules': [
            'string',
        ],
        'LicenseCount': 123,
        'LicenseCountHardLimit': True|False,
        'ConsumedLicenses': 123,
        'Status': 'string',
        'OwnerAccountId': 'string',
        'ConsumedLicenseSummaryList': [
            {
                'ResourceType': 'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI'|'RDS'|'SYSTEMS_MANAGER_MANAGED_INSTANCE',
                'ConsumedLicenses': 123
            },
        ],
        'ManagedResourceSummaryList': [
            {
                'ResourceType': 'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI'|'RDS'|'SYSTEMS_MANAGER_MANAGED_INSTANCE',
                'AssociationCount': 123
            },
        ],
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'ProductInformationList': [
            {
                'ResourceType': 'string',
                'ProductInformationFilterList': [
                    {
                        'ProductInformationFilterName': 'string',
                        'ProductInformationFilterValue': [
                            'string',
                        ],
                        'ProductInformationFilterComparator': 'string'
                    },
                ]
            },
        ],
        'AutomatedDiscoveryInformation': {
            'LastRunTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    Application Name - The name of the application. Logical operator is EQUALS .
    Application Publisher - The publisher of the application. Logical operator is EQUALS .
    Application Version - The version of the application. Logical operator is EQUALS .
    Platform Name - The name of the platform. Logical operator is EQUALS .
    Platform Type - The platform type. Logical operator is EQUALS .
    License Included - The type of license included. Logical operators are EQUALS and NOT_EQUALS . Possible values are sql-server-enterprise | sql-server-standard | sql-server-web | windows-server-datacenter .
    
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

def get_service_settings():
    """
    Gets the License Manager settings for the current Region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_service_settings()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'S3BucketArn': 'string',
    'SnsTopicArn': 'string',
    'OrganizationConfiguration': {
        'EnableIntegration': True|False
    },
    'EnableCrossAccountsDiscovery': True|False,
    'LicenseManagerResourceShareArn': 'string'
}


Response Structure

(dict) --
S3BucketArn (string) --Regional S3 bucket path for storing reports, license trail event data, discovery data, and so on.

SnsTopicArn (string) --SNS topic configured to receive notifications from License Manager.

OrganizationConfiguration (dict) --Indicates whether AWS Organizations has been integrated with License Manager for cross-account discovery.

EnableIntegration (boolean) --Enables AWS Organization integration.



EnableCrossAccountsDiscovery (boolean) --Indicates whether cross-account discovery has been enabled.

LicenseManagerResourceShareArn (string) --Amazon Resource Name (ARN) of the AWS resource share. The License Manager master account will provide member accounts with access to this share.






Exceptions

LicenseManager.Client.exceptions.ServerInternalException
LicenseManager.Client.exceptions.AuthorizationException
LicenseManager.Client.exceptions.AccessDeniedException
LicenseManager.Client.exceptions.RateLimitExceededException


    :return: {
        'S3BucketArn': 'string',
        'SnsTopicArn': 'string',
        'OrganizationConfiguration': {
            'EnableIntegration': True|False
        },
        'EnableCrossAccountsDiscovery': True|False,
        'LicenseManagerResourceShareArn': 'string'
    }
    
    
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

def list_associations_for_license_configuration(LicenseConfigurationArn=None, MaxResults=None, NextToken=None):
    """
    Lists the resource associations for the specified license configuration.
    Resource associations need not consume licenses from a license configuration. For example, an AMI or a stopped instance might not consume a license (depending on the license rules).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_associations_for_license_configuration(
        LicenseConfigurationArn='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type LicenseConfigurationArn: string
    :param LicenseConfigurationArn: [REQUIRED]\nAmazon Resource Name (ARN) of a license configuration.\n

    :type MaxResults: integer
    :param MaxResults: Maximum number of results to return in a single call.

    :type NextToken: string
    :param NextToken: Token for the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'LicenseConfigurationAssociations': [
        {
            'ResourceArn': 'string',
            'ResourceType': 'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI'|'RDS'|'SYSTEMS_MANAGER_MANAGED_INSTANCE',
            'ResourceOwnerId': 'string',
            'AssociationTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

LicenseConfigurationAssociations (list) --
Information about the associations for the license configuration.

(dict) --
Describes an association with a license configuration.

ResourceArn (string) --
Amazon Resource Name (ARN) of the resource.

ResourceType (string) --
Type of server resource.

ResourceOwnerId (string) --
ID of the AWS account that owns the resource consuming licenses.

AssociationTime (datetime) --
Time when the license configuration was associated with the resource.





NextToken (string) --
Token for the next set of results.







Exceptions

LicenseManager.Client.exceptions.InvalidParameterValueException
LicenseManager.Client.exceptions.FilterLimitExceededException
LicenseManager.Client.exceptions.ServerInternalException
LicenseManager.Client.exceptions.AuthorizationException
LicenseManager.Client.exceptions.AccessDeniedException
LicenseManager.Client.exceptions.RateLimitExceededException


    :return: {
        'LicenseConfigurationAssociations': [
            {
                'ResourceArn': 'string',
                'ResourceType': 'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI'|'RDS'|'SYSTEMS_MANAGER_MANAGED_INSTANCE',
                'ResourceOwnerId': 'string',
                'AssociationTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    LicenseManager.Client.exceptions.InvalidParameterValueException
    LicenseManager.Client.exceptions.FilterLimitExceededException
    LicenseManager.Client.exceptions.ServerInternalException
    LicenseManager.Client.exceptions.AuthorizationException
    LicenseManager.Client.exceptions.AccessDeniedException
    LicenseManager.Client.exceptions.RateLimitExceededException
    
    """
    pass

def list_failures_for_license_configuration_operations(LicenseConfigurationArn=None, MaxResults=None, NextToken=None):
    """
    Lists the license configuration operations that failed.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_failures_for_license_configuration_operations(
        LicenseConfigurationArn='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type LicenseConfigurationArn: string
    :param LicenseConfigurationArn: [REQUIRED]\nAmazon Resource Name of the license configuration.\n

    :type MaxResults: integer
    :param MaxResults: Maximum number of results to return in a single call.

    :type NextToken: string
    :param NextToken: Token for the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'LicenseOperationFailureList': [
        {
            'ResourceArn': 'string',
            'ResourceType': 'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI'|'RDS'|'SYSTEMS_MANAGER_MANAGED_INSTANCE',
            'ErrorMessage': 'string',
            'FailureTime': datetime(2015, 1, 1),
            'OperationName': 'string',
            'ResourceOwnerId': 'string',
            'OperationRequestedBy': 'string',
            'MetadataList': [
                {
                    'Name': 'string',
                    'Value': 'string'
                },
            ]
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

LicenseOperationFailureList (list) --
License configuration operations that failed.

(dict) --
Describes the failure of a license operation.

ResourceArn (string) --
Amazon Resource Name (ARN) of the resource.

ResourceType (string) --
Resource type.

ErrorMessage (string) --
Error message.

FailureTime (datetime) --
Failure time.

OperationName (string) --
Name of the operation.

ResourceOwnerId (string) --
ID of the AWS account that owns the resource.

OperationRequestedBy (string) --
The requester is "License Manager Automated Discovery".

MetadataList (list) --
Reserved.

(dict) --
Reserved.

Name (string) --
Reserved.

Value (string) --
Reserved.









NextToken (string) --
Token for the next set of results.







Exceptions

LicenseManager.Client.exceptions.InvalidParameterValueException
LicenseManager.Client.exceptions.ServerInternalException
LicenseManager.Client.exceptions.AuthorizationException
LicenseManager.Client.exceptions.AccessDeniedException
LicenseManager.Client.exceptions.RateLimitExceededException


    :return: {
        'LicenseOperationFailureList': [
            {
                'ResourceArn': 'string',
                'ResourceType': 'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI'|'RDS'|'SYSTEMS_MANAGER_MANAGED_INSTANCE',
                'ErrorMessage': 'string',
                'FailureTime': datetime(2015, 1, 1),
                'OperationName': 'string',
                'ResourceOwnerId': 'string',
                'OperationRequestedBy': 'string',
                'MetadataList': [
                    {
                        'Name': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    LicenseManager.Client.exceptions.InvalidParameterValueException
    LicenseManager.Client.exceptions.ServerInternalException
    LicenseManager.Client.exceptions.AuthorizationException
    LicenseManager.Client.exceptions.AccessDeniedException
    LicenseManager.Client.exceptions.RateLimitExceededException
    
    """
    pass

def list_license_configurations(LicenseConfigurationArns=None, MaxResults=None, NextToken=None, Filters=None):
    """
    Lists the license configurations for your account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_license_configurations(
        LicenseConfigurationArns=[
            'string',
        ],
        MaxResults=123,
        NextToken='string',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type LicenseConfigurationArns: list
    :param LicenseConfigurationArns: Amazon Resource Names (ARN) of the license configurations.\n\n(string) --\n\n

    :type MaxResults: integer
    :param MaxResults: Maximum number of results to return in a single call.

    :type NextToken: string
    :param NextToken: Token for the next set of results.

    :type Filters: list
    :param Filters: Filters to scope the results. The following filters and logical operators are supported:\n\nlicenseCountingType - The dimension on which licenses are counted (vCPU). Logical operators are EQUALS | NOT_EQUALS .\nenforceLicenseCount - A Boolean value that indicates whether hard license enforcement is used. Logical operators are EQUALS | NOT_EQUALS .\nusagelimitExceeded - A Boolean value that indicates whether the available licenses have been exceeded. Logical operators are EQUALS | NOT_EQUALS .\n\n\n(dict) --A filter name and value pair that is used to return more specific results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs.\n\nName (string) --Name of the filter. Filter names are case-sensitive.\n\nValues (list) --Filter values. Filter values are case-sensitive.\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'LicenseConfigurations': [
        {
            'LicenseConfigurationId': 'string',
            'LicenseConfigurationArn': 'string',
            'Name': 'string',
            'Description': 'string',
            'LicenseCountingType': 'vCPU'|'Instance'|'Core'|'Socket',
            'LicenseRules': [
                'string',
            ],
            'LicenseCount': 123,
            'LicenseCountHardLimit': True|False,
            'ConsumedLicenses': 123,
            'Status': 'string',
            'OwnerAccountId': 'string',
            'ConsumedLicenseSummaryList': [
                {
                    'ResourceType': 'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI'|'RDS'|'SYSTEMS_MANAGER_MANAGED_INSTANCE',
                    'ConsumedLicenses': 123
                },
            ],
            'ManagedResourceSummaryList': [
                {
                    'ResourceType': 'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI'|'RDS'|'SYSTEMS_MANAGER_MANAGED_INSTANCE',
                    'AssociationCount': 123
                },
            ],
            'ProductInformationList': [
                {
                    'ResourceType': 'string',
                    'ProductInformationFilterList': [
                        {
                            'ProductInformationFilterName': 'string',
                            'ProductInformationFilterValue': [
                                'string',
                            ],
                            'ProductInformationFilterComparator': 'string'
                        },
                    ]
                },
            ],
            'AutomatedDiscoveryInformation': {
                'LastRunTime': datetime(2015, 1, 1)
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

LicenseConfigurations (list) --
Information about the license configurations.

(dict) --
A license configuration is an abstraction of a customer license agreement that can be consumed and enforced by License Manager. Components include specifications for the license type (licensing by instance, socket, CPU, or vCPU), allowed tenancy (shared tenancy, Dedicated Instance, Dedicated Host, or all of these), host affinity (how long a VM must be associated with a host), and the number of licenses purchased and used.

LicenseConfigurationId (string) --
Unique ID of the license configuration.

LicenseConfigurationArn (string) --
Amazon Resource Name (ARN) of the license configuration.

Name (string) --
Name of the license configuration.

Description (string) --
Description of the license configuration.

LicenseCountingType (string) --
Dimension to use to track the license inventory.

LicenseRules (list) --
License rules.

(string) --


LicenseCount (integer) --
Number of licenses managed by the license configuration.

LicenseCountHardLimit (boolean) --
Number of available licenses as a hard limit.

ConsumedLicenses (integer) --
Number of licenses consumed.

Status (string) --
Status of the license configuration.

OwnerAccountId (string) --
Account ID of the license configuration\'s owner.

ConsumedLicenseSummaryList (list) --
Summaries for licenses consumed by various resources.

(dict) --
Details about license consumption.

ResourceType (string) --
Resource type of the resource consuming a license.

ConsumedLicenses (integer) --
Number of licenses consumed by the resource.





ManagedResourceSummaryList (list) --
Summaries for managed resources.

(dict) --
Summary information about a managed resource.

ResourceType (string) --
Type of resource associated with a license.

AssociationCount (integer) --
Number of resources associated with licenses.





ProductInformationList (list) --
Product information.

(dict) --
Describes product information for a license configuration.

ResourceType (string) --
Resource type. The value is SSM_MANAGED .

ProductInformationFilterList (list) --
Product information filters. The following filters and logical operators are supported:

Application Name - The name of the application. Logical operator is EQUALS .
Application Publisher - The publisher of the application. Logical operator is EQUALS .
Application Version - The version of the application. Logical operator is EQUALS .
Platform Name - The name of the platform. Logical operator is EQUALS .
Platform Type - The platform type. Logical operator is EQUALS .
License Included - The type of license included. Logical operators are EQUALS and NOT_EQUALS . Possible values are sql-server-enterprise | sql-server-standard | sql-server-web | windows-server-datacenter .


(dict) --
Describes product information filters.

ProductInformationFilterName (string) --
Filter name.

ProductInformationFilterValue (list) --
Filter value.

(string) --


ProductInformationFilterComparator (string) --
Logical operator.









AutomatedDiscoveryInformation (dict) --
Automated discovery information.

LastRunTime (datetime) --
Time that automated discovery last ran.







NextToken (string) --
Token for the next set of results.







Exceptions

LicenseManager.Client.exceptions.InvalidParameterValueException
LicenseManager.Client.exceptions.ServerInternalException
LicenseManager.Client.exceptions.FilterLimitExceededException
LicenseManager.Client.exceptions.AuthorizationException
LicenseManager.Client.exceptions.AccessDeniedException
LicenseManager.Client.exceptions.RateLimitExceededException


    :return: {
        'LicenseConfigurations': [
            {
                'LicenseConfigurationId': 'string',
                'LicenseConfigurationArn': 'string',
                'Name': 'string',
                'Description': 'string',
                'LicenseCountingType': 'vCPU'|'Instance'|'Core'|'Socket',
                'LicenseRules': [
                    'string',
                ],
                'LicenseCount': 123,
                'LicenseCountHardLimit': True|False,
                'ConsumedLicenses': 123,
                'Status': 'string',
                'OwnerAccountId': 'string',
                'ConsumedLicenseSummaryList': [
                    {
                        'ResourceType': 'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI'|'RDS'|'SYSTEMS_MANAGER_MANAGED_INSTANCE',
                        'ConsumedLicenses': 123
                    },
                ],
                'ManagedResourceSummaryList': [
                    {
                        'ResourceType': 'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI'|'RDS'|'SYSTEMS_MANAGER_MANAGED_INSTANCE',
                        'AssociationCount': 123
                    },
                ],
                'ProductInformationList': [
                    {
                        'ResourceType': 'string',
                        'ProductInformationFilterList': [
                            {
                                'ProductInformationFilterName': 'string',
                                'ProductInformationFilterValue': [
                                    'string',
                                ],
                                'ProductInformationFilterComparator': 'string'
                            },
                        ]
                    },
                ],
                'AutomatedDiscoveryInformation': {
                    'LastRunTime': datetime(2015, 1, 1)
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_license_specifications_for_resource(ResourceArn=None, MaxResults=None, NextToken=None):
    """
    Describes the license configurations for the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_license_specifications_for_resource(
        ResourceArn='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nAmazon Resource Name (ARN) of a resource that has an associated license configuration.\n

    :type MaxResults: integer
    :param MaxResults: Maximum number of results to return in a single call.

    :type NextToken: string
    :param NextToken: Token for the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'LicenseSpecifications': [
        {
            'LicenseConfigurationArn': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

LicenseSpecifications (list) --
License configurations associated with a resource.

(dict) --
Details for associating a license configuration with a resource.

LicenseConfigurationArn (string) --
Amazon Resource Name (ARN) of the license configuration.





NextToken (string) --
Token for the next set of results.







Exceptions

LicenseManager.Client.exceptions.InvalidParameterValueException
LicenseManager.Client.exceptions.ServerInternalException
LicenseManager.Client.exceptions.AuthorizationException
LicenseManager.Client.exceptions.AccessDeniedException
LicenseManager.Client.exceptions.RateLimitExceededException


    :return: {
        'LicenseSpecifications': [
            {
                'LicenseConfigurationArn': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    LicenseManager.Client.exceptions.InvalidParameterValueException
    LicenseManager.Client.exceptions.ServerInternalException
    LicenseManager.Client.exceptions.AuthorizationException
    LicenseManager.Client.exceptions.AccessDeniedException
    LicenseManager.Client.exceptions.RateLimitExceededException
    
    """
    pass

def list_resource_inventory(MaxResults=None, NextToken=None, Filters=None):
    """
    Lists resources managed using Systems Manager inventory.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_resource_inventory(
        MaxResults=123,
        NextToken='string',
        Filters=[
            {
                'Name': 'string',
                'Condition': 'EQUALS'|'NOT_EQUALS'|'BEGINS_WITH'|'CONTAINS',
                'Value': 'string'
            },
        ]
    )
    
    
    :type MaxResults: integer
    :param MaxResults: Maximum number of results to return in a single call.

    :type NextToken: string
    :param NextToken: Token for the next set of results.

    :type Filters: list
    :param Filters: Filters to scope the results. The following filters and logical operators are supported:\n\naccount_id - The ID of the AWS account that owns the resource. Logical operators are EQUALS | NOT_EQUALS .\napplication_name - The name of the application. Logical operators are EQUALS | BEGINS_WITH .\nlicense_included - The type of license included. Logical operators are EQUALS | NOT_EQUALS . Possible values are sql-server-enterprise | sql-server-standard | sql-server-web | windows-server-datacenter .\nplatform - The platform of the resource. Logical operators are EQUALS | BEGINS_WITH .\nresource_id - The ID of the resource. Logical operators are EQUALS | NOT_EQUALS .\n\n\n(dict) --An inventory filter.\n\nName (string) -- [REQUIRED]Name of the filter.\n\nCondition (string) -- [REQUIRED]Condition of the filter.\n\nValue (string) --Value of the filter.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ResourceInventoryList': [
        {
            'ResourceId': 'string',
            'ResourceType': 'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI'|'RDS'|'SYSTEMS_MANAGER_MANAGED_INSTANCE',
            'ResourceArn': 'string',
            'Platform': 'string',
            'PlatformVersion': 'string',
            'ResourceOwningAccountId': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ResourceInventoryList (list) --
Information about the resources.

(dict) --
Details about a resource.

ResourceId (string) --
ID of the resource.

ResourceType (string) --
Type of resource.

ResourceArn (string) --
Amazon Resource Name (ARN) of the resource.

Platform (string) --
Platform of the resource.

PlatformVersion (string) --
Platform version of the resource in the inventory.

ResourceOwningAccountId (string) --
ID of the account that owns the resource.





NextToken (string) --
Token for the next set of results.







Exceptions

LicenseManager.Client.exceptions.InvalidParameterValueException
LicenseManager.Client.exceptions.ServerInternalException
LicenseManager.Client.exceptions.FilterLimitExceededException
LicenseManager.Client.exceptions.FailedDependencyException
LicenseManager.Client.exceptions.AuthorizationException
LicenseManager.Client.exceptions.AccessDeniedException
LicenseManager.Client.exceptions.RateLimitExceededException


    :return: {
        'ResourceInventoryList': [
            {
                'ResourceId': 'string',
                'ResourceType': 'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI'|'RDS'|'SYSTEMS_MANAGER_MANAGED_INSTANCE',
                'ResourceArn': 'string',
                'Platform': 'string',
                'PlatformVersion': 'string',
                'ResourceOwningAccountId': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    LicenseManager.Client.exceptions.InvalidParameterValueException
    LicenseManager.Client.exceptions.ServerInternalException
    LicenseManager.Client.exceptions.FilterLimitExceededException
    LicenseManager.Client.exceptions.FailedDependencyException
    LicenseManager.Client.exceptions.AuthorizationException
    LicenseManager.Client.exceptions.AccessDeniedException
    LicenseManager.Client.exceptions.RateLimitExceededException
    
    """
    pass

def list_tags_for_resource(ResourceArn=None):
    """
    Lists the tags for the specified license configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nAmazon Resource Name (ARN) of the license configuration.\n

    :rtype: dict
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
Tags (list) --Information about the tags.

(dict) --Details about a tag for a license configuration.

Key (string) --Tag key.

Value (string) --Tag value.










Exceptions

LicenseManager.Client.exceptions.InvalidParameterValueException
LicenseManager.Client.exceptions.ServerInternalException
LicenseManager.Client.exceptions.AuthorizationException
LicenseManager.Client.exceptions.AccessDeniedException
LicenseManager.Client.exceptions.RateLimitExceededException


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

def list_usage_for_license_configuration(LicenseConfigurationArn=None, MaxResults=None, NextToken=None, Filters=None):
    """
    Lists all license usage records for a license configuration, displaying license consumption details by resource at a selected point in time. Use this action to audit the current license consumption for any license inventory and configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_usage_for_license_configuration(
        LicenseConfigurationArn='string',
        MaxResults=123,
        NextToken='string',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type LicenseConfigurationArn: string
    :param LicenseConfigurationArn: [REQUIRED]\nAmazon Resource Name (ARN) of the license configuration.\n

    :type MaxResults: integer
    :param MaxResults: Maximum number of results to return in a single call.

    :type NextToken: string
    :param NextToken: Token for the next set of results.

    :type Filters: list
    :param Filters: Filters to scope the results. The following filters and logical operators are supported:\n\nresourceArn - The ARN of the license configuration resource. Logical operators are EQUALS | NOT_EQUALS .\nresourceType - The resource type (EC2_INSTANCE | EC2_HOST | EC2_AMI | SYSTEMS_MANAGER_MANAGED_INSTANCE). Logical operators are EQUALS | NOT_EQUALS .\nresourceAccount - The ID of the account that owns the resource. Logical operators are EQUALS | NOT_EQUALS .\n\n\n(dict) --A filter name and value pair that is used to return more specific results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs.\n\nName (string) --Name of the filter. Filter names are case-sensitive.\n\nValues (list) --Filter values. Filter values are case-sensitive.\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'LicenseConfigurationUsageList': [
        {
            'ResourceArn': 'string',
            'ResourceType': 'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI'|'RDS'|'SYSTEMS_MANAGER_MANAGED_INSTANCE',
            'ResourceStatus': 'string',
            'ResourceOwnerId': 'string',
            'AssociationTime': datetime(2015, 1, 1),
            'ConsumedLicenses': 123
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

LicenseConfigurationUsageList (list) --
Information about the license configurations.

(dict) --
Details about the usage of a resource associated with a license configuration.

ResourceArn (string) --
Amazon Resource Name (ARN) of the resource.

ResourceType (string) --
Type of resource.

ResourceStatus (string) --
Status of the resource.

ResourceOwnerId (string) --
ID of the account that owns the resource.

AssociationTime (datetime) --
Time when the license configuration was initially associated with the resource.

ConsumedLicenses (integer) --
Number of licenses consumed by the resource.





NextToken (string) --
Token for the next set of results.







Exceptions

LicenseManager.Client.exceptions.InvalidParameterValueException
LicenseManager.Client.exceptions.FilterLimitExceededException
LicenseManager.Client.exceptions.ServerInternalException
LicenseManager.Client.exceptions.AuthorizationException
LicenseManager.Client.exceptions.AccessDeniedException
LicenseManager.Client.exceptions.RateLimitExceededException


    :return: {
        'LicenseConfigurationUsageList': [
            {
                'ResourceArn': 'string',
                'ResourceType': 'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI'|'RDS'|'SYSTEMS_MANAGER_MANAGED_INSTANCE',
                'ResourceStatus': 'string',
                'ResourceOwnerId': 'string',
                'AssociationTime': datetime(2015, 1, 1),
                'ConsumedLicenses': 123
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    LicenseManager.Client.exceptions.InvalidParameterValueException
    LicenseManager.Client.exceptions.FilterLimitExceededException
    LicenseManager.Client.exceptions.ServerInternalException
    LicenseManager.Client.exceptions.AuthorizationException
    LicenseManager.Client.exceptions.AccessDeniedException
    LicenseManager.Client.exceptions.RateLimitExceededException
    
    """
    pass

def tag_resource(ResourceArn=None, Tags=None):
    """
    Adds the specified tags to the specified license configuration.
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
    :param ResourceArn: [REQUIRED]\nAmazon Resource Name (ARN) of the license configuration.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nOne or more tags.\n\n(dict) --Details about a tag for a license configuration.\n\nKey (string) --Tag key.\n\nValue (string) --Tag value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

LicenseManager.Client.exceptions.InvalidParameterValueException
LicenseManager.Client.exceptions.ServerInternalException
LicenseManager.Client.exceptions.AuthorizationException
LicenseManager.Client.exceptions.AccessDeniedException
LicenseManager.Client.exceptions.RateLimitExceededException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceArn=None, TagKeys=None):
    """
    Removes the specified tags from the specified license configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nAmazon Resource Name (ARN) of the license configuration.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nKeys identifying the tags to remove.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

LicenseManager.Client.exceptions.InvalidParameterValueException
LicenseManager.Client.exceptions.ServerInternalException
LicenseManager.Client.exceptions.AuthorizationException
LicenseManager.Client.exceptions.AccessDeniedException
LicenseManager.Client.exceptions.RateLimitExceededException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_license_configuration(LicenseConfigurationArn=None, LicenseConfigurationStatus=None, LicenseRules=None, LicenseCount=None, LicenseCountHardLimit=None, Name=None, Description=None, ProductInformationList=None):
    """
    Modifies the attributes of an existing license configuration.
    A license configuration is an abstraction of a customer license agreement that can be consumed and enforced by License Manager. Components include specifications for the license type (licensing by instance, socket, CPU, or vCPU), allowed tenancy (shared tenancy, Dedicated Instance, Dedicated Host, or all of these), host affinity (how long a VM must be associated with a host), and the number of licenses purchased and used.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_license_configuration(
        LicenseConfigurationArn='string',
        LicenseConfigurationStatus='AVAILABLE'|'DISABLED',
        LicenseRules=[
            'string',
        ],
        LicenseCount=123,
        LicenseCountHardLimit=True|False,
        Name='string',
        Description='string',
        ProductInformationList=[
            {
                'ResourceType': 'string',
                'ProductInformationFilterList': [
                    {
                        'ProductInformationFilterName': 'string',
                        'ProductInformationFilterValue': [
                            'string',
                        ],
                        'ProductInformationFilterComparator': 'string'
                    },
                ]
            },
        ]
    )
    
    
    :type LicenseConfigurationArn: string
    :param LicenseConfigurationArn: [REQUIRED]\nAmazon Resource Name (ARN) of the license configuration.\n

    :type LicenseConfigurationStatus: string
    :param LicenseConfigurationStatus: New status of the license configuration.

    :type LicenseRules: list
    :param LicenseRules: New license rules.\n\n(string) --\n\n

    :type LicenseCount: integer
    :param LicenseCount: New number of licenses managed by the license configuration.

    :type LicenseCountHardLimit: boolean
    :param LicenseCountHardLimit: New hard limit of the number of available licenses.

    :type Name: string
    :param Name: New name of the license configuration.

    :type Description: string
    :param Description: New description of the license configuration.

    :type ProductInformationList: list
    :param ProductInformationList: New product information.\n\n(dict) --Describes product information for a license configuration.\n\nResourceType (string) -- [REQUIRED]Resource type. The value is SSM_MANAGED .\n\nProductInformationFilterList (list) -- [REQUIRED]Product information filters. The following filters and logical operators are supported:\n\nApplication Name - The name of the application. Logical operator is EQUALS .\nApplication Publisher - The publisher of the application. Logical operator is EQUALS .\nApplication Version - The version of the application. Logical operator is EQUALS .\nPlatform Name - The name of the platform. Logical operator is EQUALS .\nPlatform Type - The platform type. Logical operator is EQUALS .\nLicense Included - The type of license included. Logical operators are EQUALS and NOT_EQUALS . Possible values are sql-server-enterprise | sql-server-standard | sql-server-web | windows-server-datacenter .\n\n\n(dict) --Describes product information filters.\n\nProductInformationFilterName (string) -- [REQUIRED]Filter name.\n\nProductInformationFilterValue (list) -- [REQUIRED]Filter value.\n\n(string) --\n\n\nProductInformationFilterComparator (string) -- [REQUIRED]Logical operator.\n\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

LicenseManager.Client.exceptions.InvalidParameterValueException
LicenseManager.Client.exceptions.ServerInternalException
LicenseManager.Client.exceptions.AuthorizationException
LicenseManager.Client.exceptions.AccessDeniedException
LicenseManager.Client.exceptions.RateLimitExceededException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_license_specifications_for_resource(ResourceArn=None, AddLicenseSpecifications=None, RemoveLicenseSpecifications=None):
    """
    Adds or removes the specified license configurations for the specified AWS resource.
    You can update the license specifications of AMIs, instances, and hosts. You cannot update the license specifications for launch templates and AWS CloudFormation templates, as they send license configurations to the operation that creates the resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_license_specifications_for_resource(
        ResourceArn='string',
        AddLicenseSpecifications=[
            {
                'LicenseConfigurationArn': 'string'
            },
        ],
        RemoveLicenseSpecifications=[
            {
                'LicenseConfigurationArn': 'string'
            },
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nAmazon Resource Name (ARN) of the AWS resource.\n

    :type AddLicenseSpecifications: list
    :param AddLicenseSpecifications: ARNs of the license configurations to add.\n\n(dict) --Details for associating a license configuration with a resource.\n\nLicenseConfigurationArn (string) -- [REQUIRED]Amazon Resource Name (ARN) of the license configuration.\n\n\n\n\n

    :type RemoveLicenseSpecifications: list
    :param RemoveLicenseSpecifications: ARNs of the license configurations to remove.\n\n(dict) --Details for associating a license configuration with a resource.\n\nLicenseConfigurationArn (string) -- [REQUIRED]Amazon Resource Name (ARN) of the license configuration.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

LicenseManager.Client.exceptions.InvalidParameterValueException
LicenseManager.Client.exceptions.InvalidResourceStateException
LicenseManager.Client.exceptions.LicenseUsageException
LicenseManager.Client.exceptions.ServerInternalException
LicenseManager.Client.exceptions.AuthorizationException
LicenseManager.Client.exceptions.AccessDeniedException
LicenseManager.Client.exceptions.RateLimitExceededException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_service_settings(S3BucketArn=None, SnsTopicArn=None, OrganizationConfiguration=None, EnableCrossAccountsDiscovery=None):
    """
    Updates License Manager settings for the current Region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_service_settings(
        S3BucketArn='string',
        SnsTopicArn='string',
        OrganizationConfiguration={
            'EnableIntegration': True|False
        },
        EnableCrossAccountsDiscovery=True|False
    )
    
    
    :type S3BucketArn: string
    :param S3BucketArn: Amazon Resource Name (ARN) of the Amazon S3 bucket where the License Manager information is stored.

    :type SnsTopicArn: string
    :param SnsTopicArn: Amazon Resource Name (ARN) of the Amazon SNS topic used for License Manager alerts.

    :type OrganizationConfiguration: dict
    :param OrganizationConfiguration: Enables integration with AWS Organizations for cross-account discovery.\n\nEnableIntegration (boolean) -- [REQUIRED]Enables AWS Organization integration.\n\n\n

    :type EnableCrossAccountsDiscovery: boolean
    :param EnableCrossAccountsDiscovery: Activates cross-account discovery.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

LicenseManager.Client.exceptions.InvalidParameterValueException
LicenseManager.Client.exceptions.ServerInternalException
LicenseManager.Client.exceptions.AuthorizationException
LicenseManager.Client.exceptions.AccessDeniedException
LicenseManager.Client.exceptions.RateLimitExceededException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

