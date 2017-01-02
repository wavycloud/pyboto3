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

def accept_portfolio_share(AcceptLanguage=None, PortfolioId=None):
    """
    Accepts an offer to share a portfolio.
    See also: AWS API Documentation
    
    
    :example: response = client.accept_portfolio_share(
        AcceptLanguage='string',
        PortfolioId='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type PortfolioId: string
    :param PortfolioId: [REQUIRED]
            The portfolio identifier.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def associate_principal_with_portfolio(AcceptLanguage=None, PortfolioId=None, PrincipalARN=None, PrincipalType=None):
    """
    Associates the specified principal ARN with the specified portfolio.
    See also: AWS API Documentation
    
    
    :example: response = client.associate_principal_with_portfolio(
        AcceptLanguage='string',
        PortfolioId='string',
        PrincipalARN='string',
        PrincipalType='IAM'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type PortfolioId: string
    :param PortfolioId: [REQUIRED]
            The portfolio identifier.
            

    :type PrincipalARN: string
    :param PrincipalARN: [REQUIRED]
            The ARN representing the principal (IAM user, role, or group).
            

    :type PrincipalType: string
    :param PrincipalType: [REQUIRED]
            The principal type. Must be IAM
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def associate_product_with_portfolio(AcceptLanguage=None, ProductId=None, PortfolioId=None, SourcePortfolioId=None):
    """
    Associates a product with a portfolio.
    See also: AWS API Documentation
    
    
    :example: response = client.associate_product_with_portfolio(
        AcceptLanguage='string',
        ProductId='string',
        PortfolioId='string',
        SourcePortfolioId='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type ProductId: string
    :param ProductId: [REQUIRED]
            The product identifier.
            

    :type PortfolioId: string
    :param PortfolioId: [REQUIRED]
            The portfolio identifier.
            

    :type SourcePortfolioId: string
    :param SourcePortfolioId: The identifier of the source portfolio to use with this association.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
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

def create_constraint(AcceptLanguage=None, PortfolioId=None, ProductId=None, Parameters=None, Type=None, Description=None, IdempotencyToken=None):
    """
    Creates a new constraint.
    See also: AWS API Documentation
    
    
    :example: response = client.create_constraint(
        AcceptLanguage='string',
        PortfolioId='string',
        ProductId='string',
        Parameters='string',
        Type='string',
        Description='string',
        IdempotencyToken='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type PortfolioId: string
    :param PortfolioId: [REQUIRED]
            The portfolio identifier.
            

    :type ProductId: string
    :param ProductId: [REQUIRED]
            The product identifier.
            

    :type Parameters: string
    :param Parameters: [REQUIRED]
            The constraint parameters.
            

    :type Type: string
    :param Type: [REQUIRED]
            The type of the constraint.
            

    :type Description: string
    :param Description: The text description of the constraint.

    :type IdempotencyToken: string
    :param IdempotencyToken: [REQUIRED]
            A token to disambiguate duplicate requests. You can create multiple resources using the same input in multiple requests, provided that you also specify a different idempotency token for each request.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'ConstraintDetail': {
            'ConstraintId': 'string',
            'Type': 'string',
            'Description': 'string',
            'Owner': 'string'
        },
        'ConstraintParameters': 'string',
        'Status': 'AVAILABLE'|'CREATING'|'FAILED'
    }
    
    
    """
    pass

def create_portfolio(AcceptLanguage=None, DisplayName=None, Description=None, ProviderName=None, Tags=None, IdempotencyToken=None):
    """
    Creates a new portfolio.
    See also: AWS API Documentation
    
    
    :example: response = client.create_portfolio(
        AcceptLanguage='string',
        DisplayName='string',
        Description='string',
        ProviderName='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        IdempotencyToken='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type DisplayName: string
    :param DisplayName: [REQUIRED]
            The name to use for display purposes.
            

    :type Description: string
    :param Description: The text description of the portfolio.

    :type ProviderName: string
    :param ProviderName: [REQUIRED]
            The name of the portfolio provider.
            

    :type Tags: list
    :param Tags: Tags to associate with the new portfolio.
            (dict) --Key/value pairs to associate with this provisioning. These tags are entirely discretionary and are propagated to the resources created in the provisioning.
            Key (string) -- [REQUIRED]The ProvisioningArtifactParameter.TagKey parameter from DescribeProvisioningParameters .
            Value (string) -- [REQUIRED]The esired value for this key.
            
            

    :type IdempotencyToken: string
    :param IdempotencyToken: [REQUIRED]
            A token to disambiguate duplicate requests. You can create multiple resources using the same input in multiple requests, provided that you also specify a different idempotency token for each request.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'PortfolioDetail': {
            'Id': 'string',
            'ARN': 'string',
            'DisplayName': 'string',
            'Description': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'ProviderName': 'string'
        },
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    """
    pass

def create_portfolio_share(AcceptLanguage=None, PortfolioId=None, AccountId=None):
    """
    Creates a new portfolio share.
    See also: AWS API Documentation
    
    
    :example: response = client.create_portfolio_share(
        AcceptLanguage='string',
        PortfolioId='string',
        AccountId='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type PortfolioId: string
    :param PortfolioId: [REQUIRED]
            The portfolio identifier.
            

    :type AccountId: string
    :param AccountId: [REQUIRED]
            The account ID with which to share the portfolio.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def create_product(AcceptLanguage=None, Name=None, Owner=None, Description=None, Distributor=None, SupportDescription=None, SupportEmail=None, SupportUrl=None, ProductType=None, Tags=None, ProvisioningArtifactParameters=None, IdempotencyToken=None):
    """
    Creates a new product.
    See also: AWS API Documentation
    
    
    :example: response = client.create_product(
        AcceptLanguage='string',
        Name='string',
        Owner='string',
        Description='string',
        Distributor='string',
        SupportDescription='string',
        SupportEmail='string',
        SupportUrl='string',
        ProductType='CLOUD_FORMATION_TEMPLATE',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        ProvisioningArtifactParameters={
            'Name': 'string',
            'Description': 'string',
            'Info': {
                'string': 'string'
            },
            'Type': 'CLOUD_FORMATION_TEMPLATE'
        },
        IdempotencyToken='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type Name: string
    :param Name: [REQUIRED]
            The name of the product.
            

    :type Owner: string
    :param Owner: [REQUIRED]
            The owner of the product.
            

    :type Description: string
    :param Description: The text description of the product.

    :type Distributor: string
    :param Distributor: The distributor of the product.

    :type SupportDescription: string
    :param SupportDescription: Support information about the product.

    :type SupportEmail: string
    :param SupportEmail: Contact email for product support.

    :type SupportUrl: string
    :param SupportUrl: Contact URL for product support.

    :type ProductType: string
    :param ProductType: [REQUIRED]
            The type of the product to create.
            

    :type Tags: list
    :param Tags: Tags to associate with the new product.
            (dict) --Key/value pairs to associate with this provisioning. These tags are entirely discretionary and are propagated to the resources created in the provisioning.
            Key (string) -- [REQUIRED]The ProvisioningArtifactParameter.TagKey parameter from DescribeProvisioningParameters .
            Value (string) -- [REQUIRED]The esired value for this key.
            
            

    :type ProvisioningArtifactParameters: dict
    :param ProvisioningArtifactParameters: [REQUIRED]
            Parameters for the provisioning artifact.
            Name (string) --The name assigned to the provisioning artifact properties.
            Description (string) --The text description of the provisioning artifact properties.
            Info (dict) -- [REQUIRED]Additional information about the provisioning artifact properties.
            (string) --
            (string) --
            
            Type (string) --The type of the provisioning artifact properties.
            

    :type IdempotencyToken: string
    :param IdempotencyToken: [REQUIRED]
            A token to disambiguate duplicate requests. You can create multiple resources using the same input in multiple requests, provided that you also specify a different idempotency token for each request.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'ProductViewDetail': {
            'ProductViewSummary': {
                'Id': 'string',
                'ProductId': 'string',
                'Name': 'string',
                'Owner': 'string',
                'ShortDescription': 'string',
                'Type': 'CLOUD_FORMATION_TEMPLATE',
                'Distributor': 'string',
                'HasDefaultPath': True|False,
                'SupportEmail': 'string',
                'SupportDescription': 'string',
                'SupportUrl': 'string'
            },
            'Status': 'AVAILABLE'|'CREATING'|'FAILED',
            'ProductARN': 'string',
            'CreatedTime': datetime(2015, 1, 1)
        },
        'ProvisioningArtifactDetail': {
            'Id': 'string',
            'Name': 'string',
            'Description': 'string',
            'Type': 'CLOUD_FORMATION_TEMPLATE',
            'CreatedTime': datetime(2015, 1, 1)
        },
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    """
    pass

def create_provisioning_artifact(AcceptLanguage=None, ProductId=None, Parameters=None, IdempotencyToken=None):
    """
    Create a new provisioning artifact for the specified product. This operation will not work with a product that has been shared with you.
    See also: AWS API Documentation
    
    
    :example: response = client.create_provisioning_artifact(
        AcceptLanguage='string',
        ProductId='string',
        Parameters={
            'Name': 'string',
            'Description': 'string',
            'Info': {
                'string': 'string'
            },
            'Type': 'CLOUD_FORMATION_TEMPLATE'
        },
        IdempotencyToken='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type ProductId: string
    :param ProductId: [REQUIRED]
            The product identifier.
            

    :type Parameters: dict
    :param Parameters: [REQUIRED]
            The parameters to use when creating the new provisioning artifact.
            Name (string) --The name assigned to the provisioning artifact properties.
            Description (string) --The text description of the provisioning artifact properties.
            Info (dict) -- [REQUIRED]Additional information about the provisioning artifact properties.
            (string) --
            (string) --
            
            Type (string) --The type of the provisioning artifact properties.
            

    :type IdempotencyToken: string
    :param IdempotencyToken: [REQUIRED]
            A token to disambiguate duplicate requests. You can create multiple resources using the same input in multiple requests, provided that you also specify a different idempotency token for each request.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'ProvisioningArtifactDetail': {
            'Id': 'string',
            'Name': 'string',
            'Description': 'string',
            'Type': 'CLOUD_FORMATION_TEMPLATE',
            'CreatedTime': datetime(2015, 1, 1)
        },
        'Info': {
            'string': 'string'
        },
        'Status': 'AVAILABLE'|'CREATING'|'FAILED'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def delete_constraint(AcceptLanguage=None, Id=None):
    """
    Deletes the specified constraint.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_constraint(
        AcceptLanguage='string',
        Id='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type Id: string
    :param Id: [REQUIRED]
            The identifier of the constraint to delete.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_portfolio(AcceptLanguage=None, Id=None):
    """
    Deletes the specified portfolio. This operation will not work with a portfolio that has been shared with you or if it has products, users, constraints, or shared accounts associated with it.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_portfolio(
        AcceptLanguage='string',
        Id='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type Id: string
    :param Id: [REQUIRED]
            The identifier of the portfolio for the delete request.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_portfolio_share(AcceptLanguage=None, PortfolioId=None, AccountId=None):
    """
    Deletes the specified portfolio share.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_portfolio_share(
        AcceptLanguage='string',
        PortfolioId='string',
        AccountId='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type PortfolioId: string
    :param PortfolioId: [REQUIRED]
            The portfolio identifier.
            

    :type AccountId: string
    :param AccountId: [REQUIRED]
            The account ID associated with the share to delete.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_product(AcceptLanguage=None, Id=None):
    """
    Deletes the specified product. This operation will not work with a product that has been shared with you or is associated with a portfolio.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_product(
        AcceptLanguage='string',
        Id='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type Id: string
    :param Id: [REQUIRED]
            The identifier of the product for the delete request.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_provisioning_artifact(AcceptLanguage=None, ProductId=None, ProvisioningArtifactId=None):
    """
    Deletes the specified provisioning artifact. This operation will not work on a provisioning artifact associated with a product that has been shared with you, or on the last provisioning artifact associated with a product (a product must have at least one provisioning artifact).
    See also: AWS API Documentation
    
    
    :example: response = client.delete_provisioning_artifact(
        AcceptLanguage='string',
        ProductId='string',
        ProvisioningArtifactId='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type ProductId: string
    :param ProductId: [REQUIRED]
            The product identifier.
            

    :type ProvisioningArtifactId: string
    :param ProvisioningArtifactId: [REQUIRED]
            The identifier of the provisioning artifact for the delete request.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def describe_constraint(AcceptLanguage=None, Id=None):
    """
    Retrieves detailed information for a specified constraint.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_constraint(
        AcceptLanguage='string',
        Id='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type Id: string
    :param Id: [REQUIRED]
            The identifier of the constraint.
            

    :rtype: dict
    :return: {
        'ConstraintDetail': {
            'ConstraintId': 'string',
            'Type': 'string',
            'Description': 'string',
            'Owner': 'string'
        },
        'ConstraintParameters': 'string',
        'Status': 'AVAILABLE'|'CREATING'|'FAILED'
    }
    
    
    """
    pass

def describe_portfolio(AcceptLanguage=None, Id=None):
    """
    Retrieves detailed information and any tags associated with the specified portfolio.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_portfolio(
        AcceptLanguage='string',
        Id='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type Id: string
    :param Id: [REQUIRED]
            The identifier of the portfolio for which to retrieve information.
            

    :rtype: dict
    :return: {
        'PortfolioDetail': {
            'Id': 'string',
            'ARN': 'string',
            'DisplayName': 'string',
            'Description': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'ProviderName': 'string'
        },
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_product(AcceptLanguage=None, Id=None):
    """
    Retrieves information about a specified product.
    This operation is functionally identical to  DescribeProductView except that it takes as input ProductId instead of ProductViewId .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_product(
        AcceptLanguage='string',
        Id='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type Id: string
    :param Id: [REQUIRED]
            The ProductId of the product to describe.
            

    :rtype: dict
    :return: {
        'ProductViewSummary': {
            'Id': 'string',
            'ProductId': 'string',
            'Name': 'string',
            'Owner': 'string',
            'ShortDescription': 'string',
            'Type': 'CLOUD_FORMATION_TEMPLATE',
            'Distributor': 'string',
            'HasDefaultPath': True|False,
            'SupportEmail': 'string',
            'SupportDescription': 'string',
            'SupportUrl': 'string'
        },
        'ProvisioningArtifacts': [
            {
                'Id': 'string',
                'Name': 'string',
                'Description': 'string',
                'CreatedTime': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    """
    pass

def describe_product_as_admin(AcceptLanguage=None, Id=None):
    """
    Retrieves information about a specified product, run with administrator access.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_product_as_admin(
        AcceptLanguage='string',
        Id='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type Id: string
    :param Id: [REQUIRED]
            The identifier of the product for which to retrieve information.
            

    :rtype: dict
    :return: {
        'ProductViewDetail': {
            'ProductViewSummary': {
                'Id': 'string',
                'ProductId': 'string',
                'Name': 'string',
                'Owner': 'string',
                'ShortDescription': 'string',
                'Type': 'CLOUD_FORMATION_TEMPLATE',
                'Distributor': 'string',
                'HasDefaultPath': True|False,
                'SupportEmail': 'string',
                'SupportDescription': 'string',
                'SupportUrl': 'string'
            },
            'Status': 'AVAILABLE'|'CREATING'|'FAILED',
            'ProductARN': 'string',
            'CreatedTime': datetime(2015, 1, 1)
        },
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_product_view(AcceptLanguage=None, Id=None):
    """
    Retrieves information about a specified product.
    This operation is functionally identical to  DescribeProduct except that it takes as input ProductViewId instead of ProductId .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_product_view(
        AcceptLanguage='string',
        Id='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type Id: string
    :param Id: [REQUIRED]
            The ProductViewId of the product to describe.
            

    :rtype: dict
    :return: {
        'ProductViewSummary': {
            'Id': 'string',
            'ProductId': 'string',
            'Name': 'string',
            'Owner': 'string',
            'ShortDescription': 'string',
            'Type': 'CLOUD_FORMATION_TEMPLATE',
            'Distributor': 'string',
            'HasDefaultPath': True|False,
            'SupportEmail': 'string',
            'SupportDescription': 'string',
            'SupportUrl': 'string'
        },
        'ProvisioningArtifacts': [
            {
                'Id': 'string',
                'Name': 'string',
                'Description': 'string',
                'CreatedTime': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    """
    pass

def describe_provisioning_artifact(AcceptLanguage=None, ProvisioningArtifactId=None, ProductId=None):
    """
    Retrieves detailed information about the specified provisioning artifact.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_provisioning_artifact(
        AcceptLanguage='string',
        ProvisioningArtifactId='string',
        ProductId='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type ProvisioningArtifactId: string
    :param ProvisioningArtifactId: [REQUIRED]
            The identifier of the provisioning artifact.
            

    :type ProductId: string
    :param ProductId: [REQUIRED]
            The product identifier.
            

    :rtype: dict
    :return: {
        'ProvisioningArtifactDetail': {
            'Id': 'string',
            'Name': 'string',
            'Description': 'string',
            'Type': 'CLOUD_FORMATION_TEMPLATE',
            'CreatedTime': datetime(2015, 1, 1)
        },
        'Info': {
            'string': 'string'
        },
        'Status': 'AVAILABLE'|'CREATING'|'FAILED'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def describe_provisioning_parameters(AcceptLanguage=None, ProductId=None, ProvisioningArtifactId=None, PathId=None):
    """
    Provides information about parameters required to provision a specified product in a specified manner. Use this operation to obtain the list of ProvisioningArtifactParameters parameters available to call the  ProvisionProduct operation for the specified product.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_provisioning_parameters(
        AcceptLanguage='string',
        ProductId='string',
        ProvisioningArtifactId='string',
        PathId='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type ProductId: string
    :param ProductId: [REQUIRED]
            The product identifier.
            

    :type ProvisioningArtifactId: string
    :param ProvisioningArtifactId: [REQUIRED]
            The provisioning artifact identifier for this product.
            

    :type PathId: string
    :param PathId: The identifier of the path for this product's provisioning. This value is optional if the product has a default path, and is required if there is more than one path for the specified product.

    :rtype: dict
    :return: {
        'ProvisioningArtifactParameters': [
            {
                'ParameterKey': 'string',
                'DefaultValue': 'string',
                'ParameterType': 'string',
                'IsNoEcho': True|False,
                'Description': 'string',
                'ParameterConstraints': {
                    'AllowedValues': [
                        'string',
                    ]
                }
            },
        ],
        'ConstraintSummaries': [
            {
                'Type': 'string',
                'Description': 'string'
            },
        ],
        'UsageInstructions': [
            {
                'Type': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_record(AcceptLanguage=None, Id=None, PageToken=None, PageSize=None):
    """
    Retrieves a paginated list of the full details of a specific request. Use this operation after calling a request operation ( ProvisionProduct ,  TerminateProvisionedProduct , or  UpdateProvisionedProduct ).
    See also: AWS API Documentation
    
    
    :example: response = client.describe_record(
        AcceptLanguage='string',
        Id='string',
        PageToken='string',
        PageSize=123
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type Id: string
    :param Id: [REQUIRED]
            The record identifier of the ProvisionedProduct object for which to retrieve output information. This is the RecordDetail.RecordId obtained from the request operation's response.
            

    :type PageToken: string
    :param PageToken: The page token of the first page retrieved. If null, this retrieves the first page of size PageSize .

    :type PageSize: integer
    :param PageSize: The maximum number of items to return in the results. If more results exist than fit in the specified PageSize , the value of NextPageToken in the response is non-null.

    :rtype: dict
    :return: {
        'RecordDetail': {
            'RecordId': 'string',
            'ProvisionedProductName': 'string',
            'Status': 'IN_PROGRESS'|'SUCCEEDED'|'ERROR',
            'CreatedTime': datetime(2015, 1, 1),
            'UpdatedTime': datetime(2015, 1, 1),
            'ProvisionedProductType': 'string',
            'RecordType': 'string',
            'ProvisionedProductId': 'string',
            'ProductId': 'string',
            'ProvisioningArtifactId': 'string',
            'PathId': 'string',
            'RecordErrors': [
                {
                    'Code': 'string',
                    'Description': 'string'
                },
            ],
            'RecordTags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        },
        'RecordOutputs': [
            {
                'OutputKey': 'string',
                'OutputValue': 'string',
                'Description': 'string'
            },
        ],
        'NextPageToken': 'string'
    }
    
    
    """
    pass

def disassociate_principal_from_portfolio(AcceptLanguage=None, PortfolioId=None, PrincipalARN=None):
    """
    Disassociates a previously associated principal ARN from a specified portfolio.
    See also: AWS API Documentation
    
    
    :example: response = client.disassociate_principal_from_portfolio(
        AcceptLanguage='string',
        PortfolioId='string',
        PrincipalARN='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type PortfolioId: string
    :param PortfolioId: [REQUIRED]
            The portfolio identifier.
            

    :type PrincipalARN: string
    :param PrincipalARN: [REQUIRED]
            The ARN representing the principal (IAM user, role, or group).
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def disassociate_product_from_portfolio(AcceptLanguage=None, ProductId=None, PortfolioId=None):
    """
    Disassociates the specified product from the specified portfolio.
    See also: AWS API Documentation
    
    
    :example: response = client.disassociate_product_from_portfolio(
        AcceptLanguage='string',
        ProductId='string',
        PortfolioId='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type ProductId: string
    :param ProductId: [REQUIRED]
            The product identifier.
            

    :type PortfolioId: string
    :param PortfolioId: [REQUIRED]
            The portfolio identifier.
            

    :rtype: dict
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

def list_accepted_portfolio_shares(AcceptLanguage=None, PageToken=None, PageSize=None):
    """
    Lists details of all portfolios for which sharing was accepted by this account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_accepted_portfolio_shares(
        AcceptLanguage='string',
        PageToken='string',
        PageSize=123
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type PageToken: string
    :param PageToken: The page token of the first page retrieved. If null, this retrieves the first page of size PageSize .

    :type PageSize: integer
    :param PageSize: The maximum number of items to return in the results. If more results exist than fit in the specified PageSize , the value of NextPageToken in the response is non-null.

    :rtype: dict
    :return: {
        'PortfolioDetails': [
            {
                'Id': 'string',
                'ARN': 'string',
                'DisplayName': 'string',
                'Description': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'ProviderName': 'string'
            },
        ],
        'NextPageToken': 'string'
    }
    
    
    """
    pass

def list_constraints_for_portfolio(AcceptLanguage=None, PortfolioId=None, ProductId=None, PageSize=None, PageToken=None):
    """
    Retrieves detailed constraint information for the specified portfolio and product.
    See also: AWS API Documentation
    
    
    :example: response = client.list_constraints_for_portfolio(
        AcceptLanguage='string',
        PortfolioId='string',
        ProductId='string',
        PageSize=123,
        PageToken='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type PortfolioId: string
    :param PortfolioId: [REQUIRED]
            The portfolio identifier.
            

    :type ProductId: string
    :param ProductId: The product identifier.

    :type PageSize: integer
    :param PageSize: The maximum number of items to return in the results. If more results exist than fit in the specified PageSize , the value of NextPageToken in the response is non-null.

    :type PageToken: string
    :param PageToken: The page token of the first page retrieved. If null, this retrieves the first page of size PageSize .

    :rtype: dict
    :return: {
        'ConstraintDetails': [
            {
                'ConstraintId': 'string',
                'Type': 'string',
                'Description': 'string',
                'Owner': 'string'
            },
        ],
        'NextPageToken': 'string'
    }
    
    
    """
    pass

def list_launch_paths(AcceptLanguage=None, ProductId=None, PageSize=None, PageToken=None):
    """
    Returns a paginated list of all paths to a specified product. A path is how the user has access to a specified product, and is necessary when provisioning a product. A path also determines the constraints put on the product.
    See also: AWS API Documentation
    
    
    :example: response = client.list_launch_paths(
        AcceptLanguage='string',
        ProductId='string',
        PageSize=123,
        PageToken='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type ProductId: string
    :param ProductId: [REQUIRED]
            The product identifier.. Identifies the product for which to retrieve LaunchPathSummaries information.
            

    :type PageSize: integer
    :param PageSize: The maximum number of items to return in the results. If more results exist than fit in the specified PageSize , the value of NextPageToken in the response is non-null.

    :type PageToken: string
    :param PageToken: The page token of the first page retrieved. If null, this retrieves the first page of size PageSize .

    :rtype: dict
    :return: {
        'LaunchPathSummaries': [
            {
                'Id': 'string',
                'ConstraintSummaries': [
                    {
                        'Type': 'string',
                        'Description': 'string'
                    },
                ],
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'Name': 'string'
            },
        ],
        'NextPageToken': 'string'
    }
    
    
    """
    pass

def list_portfolio_access(AcceptLanguage=None, PortfolioId=None):
    """
    Lists the account IDs that have been authorized sharing of the specified portfolio.
    See also: AWS API Documentation
    
    
    :example: response = client.list_portfolio_access(
        AcceptLanguage='string',
        PortfolioId='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type PortfolioId: string
    :param PortfolioId: [REQUIRED]
            The portfolio identifier.
            

    :rtype: dict
    :return: {
        'AccountIds': [
            'string',
        ],
        'NextPageToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_portfolios(AcceptLanguage=None, PageToken=None, PageSize=None):
    """
    Lists all portfolios in the catalog.
    See also: AWS API Documentation
    
    
    :example: response = client.list_portfolios(
        AcceptLanguage='string',
        PageToken='string',
        PageSize=123
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type PageToken: string
    :param PageToken: The page token of the first page retrieved. If null, this retrieves the first page of size PageSize .

    :type PageSize: integer
    :param PageSize: The maximum number of items to return in the results. If more results exist than fit in the specified PageSize , the value of NextPageToken in the response is non-null.

    :rtype: dict
    :return: {
        'PortfolioDetails': [
            {
                'Id': 'string',
                'ARN': 'string',
                'DisplayName': 'string',
                'Description': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'ProviderName': 'string'
            },
        ],
        'NextPageToken': 'string'
    }
    
    
    """
    pass

def list_portfolios_for_product(AcceptLanguage=None, ProductId=None, PageToken=None, PageSize=None):
    """
    Lists all portfolios that the specified product is associated with.
    See also: AWS API Documentation
    
    
    :example: response = client.list_portfolios_for_product(
        AcceptLanguage='string',
        ProductId='string',
        PageToken='string',
        PageSize=123
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type ProductId: string
    :param ProductId: [REQUIRED]
            The product identifier.
            

    :type PageToken: string
    :param PageToken: The page token of the first page retrieved. If null, this retrieves the first page of size PageSize .

    :type PageSize: integer
    :param PageSize: The maximum number of items to return in the results. If more results exist than fit in the specified PageSize , the value of NextPageToken in the response is non-null.

    :rtype: dict
    :return: {
        'PortfolioDetails': [
            {
                'Id': 'string',
                'ARN': 'string',
                'DisplayName': 'string',
                'Description': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'ProviderName': 'string'
            },
        ],
        'NextPageToken': 'string'
    }
    
    
    """
    pass

def list_principals_for_portfolio(AcceptLanguage=None, PortfolioId=None, PageSize=None, PageToken=None):
    """
    Lists all principal ARNs associated with the specified portfolio.
    See also: AWS API Documentation
    
    
    :example: response = client.list_principals_for_portfolio(
        AcceptLanguage='string',
        PortfolioId='string',
        PageSize=123,
        PageToken='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type PortfolioId: string
    :param PortfolioId: [REQUIRED]
            The portfolio identifier.
            

    :type PageSize: integer
    :param PageSize: The maximum number of items to return in the results. If more results exist than fit in the specified PageSize , the value of NextPageToken in the response is non-null.

    :type PageToken: string
    :param PageToken: The page token of the first page retrieved. If null, this retrieves the first page of size PageSize .

    :rtype: dict
    :return: {
        'Principals': [
            {
                'PrincipalARN': 'string',
                'PrincipalType': 'IAM'
            },
        ],
        'NextPageToken': 'string'
    }
    
    
    """
    pass

def list_provisioning_artifacts(AcceptLanguage=None, ProductId=None):
    """
    Lists all provisioning artifacts associated with the specified product.
    See also: AWS API Documentation
    
    
    :example: response = client.list_provisioning_artifacts(
        AcceptLanguage='string',
        ProductId='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type ProductId: string
    :param ProductId: [REQUIRED]
            The product identifier.
            

    :rtype: dict
    :return: {
        'ProvisioningArtifactDetails': [
            {
                'Id': 'string',
                'Name': 'string',
                'Description': 'string',
                'Type': 'CLOUD_FORMATION_TEMPLATE',
                'CreatedTime': datetime(2015, 1, 1)
            },
        ],
        'NextPageToken': 'string'
    }
    
    
    """
    pass

def list_record_history(AcceptLanguage=None, AccessLevelFilter=None, SearchFilter=None, PageSize=None, PageToken=None):
    """
    Returns a paginated list of all performed requests, in the form of RecordDetails objects that are filtered as specified.
    See also: AWS API Documentation
    
    
    :example: response = client.list_record_history(
        AcceptLanguage='string',
        AccessLevelFilter={
            'Key': 'Account'|'Role'|'User',
            'Value': 'string'
        },
        SearchFilter={
            'Key': 'string',
            'Value': 'string'
        },
        PageSize=123,
        PageToken='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type AccessLevelFilter: dict
    :param AccessLevelFilter: The access level for obtaining results. If left unspecified, User level access is used.
            Key (string) --Specifies the access level.
            Account allows results at the account level.Role allows results based on the federated role of the specified user.
            User allows results limited to the specified user.
            Value (string) --Specifies the user to which the access level applies. A value of Self is currently supported.
            

    :type SearchFilter: dict
    :param SearchFilter: The filter to limit search results.
            Key (string) --The filter key.
            Value (string) --The filter value for Key .
            

    :type PageSize: integer
    :param PageSize: The maximum number of items to return in the results. If more results exist than fit in the specified PageSize , the value of NextPageToken in the response is non-null.

    :type PageToken: string
    :param PageToken: The page token of the first page retrieved. If null, this retrieves the first page of size PageSize .

    :rtype: dict
    :return: {
        'RecordDetails': [
            {
                'RecordId': 'string',
                'ProvisionedProductName': 'string',
                'Status': 'IN_PROGRESS'|'SUCCEEDED'|'ERROR',
                'CreatedTime': datetime(2015, 1, 1),
                'UpdatedTime': datetime(2015, 1, 1),
                'ProvisionedProductType': 'string',
                'RecordType': 'string',
                'ProvisionedProductId': 'string',
                'ProductId': 'string',
                'ProvisioningArtifactId': 'string',
                'PathId': 'string',
                'RecordErrors': [
                    {
                        'Code': 'string',
                        'Description': 'string'
                    },
                ],
                'RecordTags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ],
        'NextPageToken': 'string'
    }
    
    
    """
    pass

def provision_product(AcceptLanguage=None, ProductId=None, ProvisioningArtifactId=None, PathId=None, ProvisionedProductName=None, ProvisioningParameters=None, Tags=None, NotificationArns=None, ProvisionToken=None):
    """
    Requests a Provision of a specified product. A ProvisionedProduct is a resourced instance for a product. For example, provisioning a CloudFormation-template-backed product results in launching a CloudFormation stack and all the underlying resources that come with it.
    You can check the status of this request using the  DescribeRecord operation.
    See also: AWS API Documentation
    
    
    :example: response = client.provision_product(
        AcceptLanguage='string',
        ProductId='string',
        ProvisioningArtifactId='string',
        PathId='string',
        ProvisionedProductName='string',
        ProvisioningParameters=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        NotificationArns=[
            'string',
        ],
        ProvisionToken='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type ProductId: string
    :param ProductId: [REQUIRED]
            The product identifier.
            

    :type ProvisioningArtifactId: string
    :param ProvisioningArtifactId: [REQUIRED]
            The provisioning artifact identifier for this product.
            

    :type PathId: string
    :param PathId: The identifier of the path for this product's provisioning. This value is optional if the product has a default path, and is required if there is more than one path for the specified product.

    :type ProvisionedProductName: string
    :param ProvisionedProductName: [REQUIRED]
            A user-friendly name to identify the ProvisionedProduct object. This value must be unique for the AWS account and cannot be updated after the product is provisioned.
            

    :type ProvisioningParameters: list
    :param ProvisioningParameters: Parameters specified by the administrator that are required for provisioning the product.
            (dict) --The arameter key/value pairs used to provision a product.
            Key (string) --The ProvisioningArtifactParameter.ParameterKey parameter from DescribeProvisioningParameters .
            Value (string) --The value to use for provisioning. Any constraints on this value can be found in ProvisioningArtifactParameter for Key .
            
            

    :type Tags: list
    :param Tags: A list of tags to use as provisioning options.
            (dict) --Key/value pairs to associate with this provisioning. These tags are entirely discretionary and are propagated to the resources created in the provisioning.
            Key (string) -- [REQUIRED]The ProvisioningArtifactParameter.TagKey parameter from DescribeProvisioningParameters .
            Value (string) -- [REQUIRED]The esired value for this key.
            
            

    :type NotificationArns: list
    :param NotificationArns: Passed to CloudFormation. The SNS topic ARNs to which to publish stack-related events.
            (string) --
            

    :type ProvisionToken: string
    :param ProvisionToken: [REQUIRED]
            An idempotency token that uniquely identifies the provisioning request.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'RecordDetail': {
            'RecordId': 'string',
            'ProvisionedProductName': 'string',
            'Status': 'IN_PROGRESS'|'SUCCEEDED'|'ERROR',
            'CreatedTime': datetime(2015, 1, 1),
            'UpdatedTime': datetime(2015, 1, 1),
            'ProvisionedProductType': 'string',
            'RecordType': 'string',
            'ProvisionedProductId': 'string',
            'ProductId': 'string',
            'ProvisioningArtifactId': 'string',
            'PathId': 'string',
            'RecordErrors': [
                {
                    'Code': 'string',
                    'Description': 'string'
                },
            ],
            'RecordTags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def reject_portfolio_share(AcceptLanguage=None, PortfolioId=None):
    """
    Rejects an offer to share a portfolio.
    See also: AWS API Documentation
    
    
    :example: response = client.reject_portfolio_share(
        AcceptLanguage='string',
        PortfolioId='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type PortfolioId: string
    :param PortfolioId: [REQUIRED]
            The portfolio identifier.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def scan_provisioned_products(AcceptLanguage=None, AccessLevelFilter=None, PageSize=None, PageToken=None):
    """
    Returns a paginated list of all the ProvisionedProduct objects that are currently available (not terminated).
    See also: AWS API Documentation
    
    
    :example: response = client.scan_provisioned_products(
        AcceptLanguage='string',
        AccessLevelFilter={
            'Key': 'Account'|'Role'|'User',
            'Value': 'string'
        },
        PageSize=123,
        PageToken='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type AccessLevelFilter: dict
    :param AccessLevelFilter: The access level for obtaining results. If left unspecified, User level access is used.
            Key (string) --Specifies the access level.
            Account allows results at the account level.Role allows results based on the federated role of the specified user.
            User allows results limited to the specified user.
            Value (string) --Specifies the user to which the access level applies. A value of Self is currently supported.
            

    :type PageSize: integer
    :param PageSize: The maximum number of items to return in the results. If more results exist than fit in the specified PageSize , the value of NextPageToken in the response is non-null.

    :type PageToken: string
    :param PageToken: The page token of the first page retrieved. If null, this retrieves the first page of size PageSize .

    :rtype: dict
    :return: {
        'ProvisionedProducts': [
            {
                'Name': 'string',
                'Arn': 'string',
                'Type': 'string',
                'Id': 'string',
                'Status': 'IN_PROGRESS'|'SUCCEEDED'|'ERROR',
                'StatusMessage': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'IdempotencyToken': 'string',
                'LastRecordId': 'string'
            },
        ],
        'NextPageToken': 'string'
    }
    
    
    """
    pass

def search_products(AcceptLanguage=None, Filters=None, PageSize=None, SortBy=None, SortOrder=None, PageToken=None):
    """
    Returns a paginated list all of the Products objects to which the caller has access.
    The output of this operation can be used as input for other operations, such as  DescribeProductView .
    See also: AWS API Documentation
    
    
    :example: response = client.search_products(
        AcceptLanguage='string',
        Filters={
            'string': [
                'string',
            ]
        },
        PageSize=123,
        SortBy='Title'|'VersionCount'|'CreationDate',
        SortOrder='ASCENDING'|'DESCENDING',
        PageToken='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type Filters: dict
    :param Filters: The list of filters with which to limit search results. If no search filters are specified, the output is all the products to which the calling user has access.
            (string) --
            (list) --
            (string) --
            
            

    :type PageSize: integer
    :param PageSize: The maximum number of items to return in the results. If more results exist than fit in the specified PageSize , the value of NextPageToken in the response is non-null.

    :type SortBy: string
    :param SortBy: The sort field specifier. If no value is specified, results are not sorted.

    :type SortOrder: string
    :param SortOrder: The sort order specifier. If no value is specified, results are not sorted.

    :type PageToken: string
    :param PageToken: The page token of the first page retrieved. If null, this retrieves the first page of size PageSize .

    :rtype: dict
    :return: {
        'ProductViewSummaries': [
            {
                'Id': 'string',
                'ProductId': 'string',
                'Name': 'string',
                'Owner': 'string',
                'ShortDescription': 'string',
                'Type': 'CLOUD_FORMATION_TEMPLATE',
                'Distributor': 'string',
                'HasDefaultPath': True|False,
                'SupportEmail': 'string',
                'SupportDescription': 'string',
                'SupportUrl': 'string'
            },
        ],
        'ProductViewAggregations': {
            'string': [
                {
                    'Value': 'string',
                    'ApproximateCount': 123
                },
            ]
        },
        'NextPageToken': 'string'
    }
    
    
    """
    pass

def search_products_as_admin(AcceptLanguage=None, PortfolioId=None, Filters=None, SortBy=None, SortOrder=None, PageToken=None, PageSize=None, ProductSource=None):
    """
    Retrieves summary and status information about all products created within the caller's account. If a portfolio ID is provided, this operation retrieves information for only those products that are associated with the specified portfolio.
    See also: AWS API Documentation
    
    
    :example: response = client.search_products_as_admin(
        AcceptLanguage='string',
        PortfolioId='string',
        Filters={
            'string': [
                'string',
            ]
        },
        SortBy='Title'|'VersionCount'|'CreationDate',
        SortOrder='ASCENDING'|'DESCENDING',
        PageToken='string',
        PageSize=123,
        ProductSource='ACCOUNT'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type PortfolioId: string
    :param PortfolioId: The portfolio identifier.

    :type Filters: dict
    :param Filters: The list of filters with which to limit search results. If no search filters are specified, the output is all the products to which the administrator has access.
            (string) --
            (list) --
            (string) --
            
            

    :type SortBy: string
    :param SortBy: The sort field specifier. If no value is specified, results are not sorted.

    :type SortOrder: string
    :param SortOrder: The sort order specifier. If no value is specified, results are not sorted.

    :type PageToken: string
    :param PageToken: The page token of the first page retrieved. If null, this retrieves the first page of size PageSize .

    :type PageSize: integer
    :param PageSize: The maximum number of items to return in the results. If more results exist than fit in the specified PageSize , the value of NextPageToken in the response is non-null.

    :type ProductSource: string
    :param ProductSource: Access level of the source of the product.

    :rtype: dict
    :return: {
        'ProductViewDetails': [
            {
                'ProductViewSummary': {
                    'Id': 'string',
                    'ProductId': 'string',
                    'Name': 'string',
                    'Owner': 'string',
                    'ShortDescription': 'string',
                    'Type': 'CLOUD_FORMATION_TEMPLATE',
                    'Distributor': 'string',
                    'HasDefaultPath': True|False,
                    'SupportEmail': 'string',
                    'SupportDescription': 'string',
                    'SupportUrl': 'string'
                },
                'Status': 'AVAILABLE'|'CREATING'|'FAILED',
                'ProductARN': 'string',
                'CreatedTime': datetime(2015, 1, 1)
            },
        ],
        'NextPageToken': 'string'
    }
    
    
    """
    pass

def terminate_provisioned_product(ProvisionedProductName=None, ProvisionedProductId=None, TerminateToken=None, IgnoreErrors=None, AcceptLanguage=None):
    """
    Requests termination of an existing ProvisionedProduct object. If there are Tags associated with the object, they are terminated when the ProvisionedProduct object is terminated.
    This operation does not delete any records associated with the ProvisionedProduct object.
    You can check the status of this request using the  DescribeRecord operation.
    See also: AWS API Documentation
    
    
    :example: response = client.terminate_provisioned_product(
        ProvisionedProductName='string',
        ProvisionedProductId='string',
        TerminateToken='string',
        IgnoreErrors=True|False,
        AcceptLanguage='string'
    )
    
    
    :type ProvisionedProductName: string
    :param ProvisionedProductName: The name of the ProvisionedProduct object to terminate. You must specify either ProvisionedProductName or ProvisionedProductId , but not both.

    :type ProvisionedProductId: string
    :param ProvisionedProductId: The identifier of the ProvisionedProduct object to terminate. You must specify either ProvisionedProductName or ProvisionedProductId , but not both.

    :type TerminateToken: string
    :param TerminateToken: [REQUIRED]
            An idempotency token that uniquely identifies the termination request. This token is only valid during the termination process. After the ProvisionedProduct object is terminated, further requests to terminate the same ProvisionedProduct object always return ResourceNotFound regardless of the value of TerminateToken .
            This field is autopopulated if not provided.
            

    :type IgnoreErrors: boolean
    :param IgnoreErrors: If set to true, AWS Service Catalog stops managing the specified ProvisionedProduct object even if it cannot delete the underlying resources.

    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :rtype: dict
    :return: {
        'RecordDetail': {
            'RecordId': 'string',
            'ProvisionedProductName': 'string',
            'Status': 'IN_PROGRESS'|'SUCCEEDED'|'ERROR',
            'CreatedTime': datetime(2015, 1, 1),
            'UpdatedTime': datetime(2015, 1, 1),
            'ProvisionedProductType': 'string',
            'RecordType': 'string',
            'ProvisionedProductId': 'string',
            'ProductId': 'string',
            'ProvisioningArtifactId': 'string',
            'PathId': 'string',
            'RecordErrors': [
                {
                    'Code': 'string',
                    'Description': 'string'
                },
            ],
            'RecordTags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def update_constraint(AcceptLanguage=None, Id=None, Description=None):
    """
    Updates an existing constraint.
    See also: AWS API Documentation
    
    
    :example: response = client.update_constraint(
        AcceptLanguage='string',
        Id='string',
        Description='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type Id: string
    :param Id: [REQUIRED]
            The identifier of the constraint to update.
            

    :type Description: string
    :param Description: The updated text description of the constraint.

    :rtype: dict
    :return: {
        'ConstraintDetail': {
            'ConstraintId': 'string',
            'Type': 'string',
            'Description': 'string',
            'Owner': 'string'
        },
        'ConstraintParameters': 'string',
        'Status': 'AVAILABLE'|'CREATING'|'FAILED'
    }
    
    
    """
    pass

def update_portfolio(AcceptLanguage=None, Id=None, DisplayName=None, Description=None, ProviderName=None, AddTags=None, RemoveTags=None):
    """
    Updates the specified portfolio's details. This operation will not work with a product that has been shared with you.
    See also: AWS API Documentation
    
    
    :example: response = client.update_portfolio(
        AcceptLanguage='string',
        Id='string',
        DisplayName='string',
        Description='string',
        ProviderName='string',
        AddTags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        RemoveTags=[
            'string',
        ]
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type Id: string
    :param Id: [REQUIRED]
            The identifier of the portfolio for the update request.
            

    :type DisplayName: string
    :param DisplayName: The name to use for display purposes.

    :type Description: string
    :param Description: The updated text description of the portfolio.

    :type ProviderName: string
    :param ProviderName: The updated name of the portfolio provider.

    :type AddTags: list
    :param AddTags: Tags to add to the existing list of tags associated with the portfolio.
            (dict) --Key/value pairs to associate with this provisioning. These tags are entirely discretionary and are propagated to the resources created in the provisioning.
            Key (string) -- [REQUIRED]The ProvisioningArtifactParameter.TagKey parameter from DescribeProvisioningParameters .
            Value (string) -- [REQUIRED]The esired value for this key.
            
            

    :type RemoveTags: list
    :param RemoveTags: Tags to remove from the existing list of tags associated with the portfolio.
            (string) --
            

    :rtype: dict
    :return: {
        'PortfolioDetail': {
            'Id': 'string',
            'ARN': 'string',
            'DisplayName': 'string',
            'Description': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'ProviderName': 'string'
        },
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    """
    pass

def update_product(AcceptLanguage=None, Id=None, Name=None, Owner=None, Description=None, Distributor=None, SupportDescription=None, SupportEmail=None, SupportUrl=None, AddTags=None, RemoveTags=None):
    """
    Updates an existing product.
    See also: AWS API Documentation
    
    
    :example: response = client.update_product(
        AcceptLanguage='string',
        Id='string',
        Name='string',
        Owner='string',
        Description='string',
        Distributor='string',
        SupportDescription='string',
        SupportEmail='string',
        SupportUrl='string',
        AddTags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        RemoveTags=[
            'string',
        ]
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type Id: string
    :param Id: [REQUIRED]
            The identifier of the product for the update request.
            

    :type Name: string
    :param Name: The updated product name.

    :type Owner: string
    :param Owner: The updated owner of the product.

    :type Description: string
    :param Description: The updated text description of the product.

    :type Distributor: string
    :param Distributor: The updated distributor of the product.

    :type SupportDescription: string
    :param SupportDescription: The updated support description for the product.

    :type SupportEmail: string
    :param SupportEmail: The updated support email for the product.

    :type SupportUrl: string
    :param SupportUrl: The updated support URL for the product.

    :type AddTags: list
    :param AddTags: Tags to add to the existing list of tags associated with the product.
            (dict) --Key/value pairs to associate with this provisioning. These tags are entirely discretionary and are propagated to the resources created in the provisioning.
            Key (string) -- [REQUIRED]The ProvisioningArtifactParameter.TagKey parameter from DescribeProvisioningParameters .
            Value (string) -- [REQUIRED]The esired value for this key.
            
            

    :type RemoveTags: list
    :param RemoveTags: Tags to remove from the existing list of tags associated with the product.
            (string) --
            

    :rtype: dict
    :return: {
        'ProductViewDetail': {
            'ProductViewSummary': {
                'Id': 'string',
                'ProductId': 'string',
                'Name': 'string',
                'Owner': 'string',
                'ShortDescription': 'string',
                'Type': 'CLOUD_FORMATION_TEMPLATE',
                'Distributor': 'string',
                'HasDefaultPath': True|False,
                'SupportEmail': 'string',
                'SupportDescription': 'string',
                'SupportUrl': 'string'
            },
            'Status': 'AVAILABLE'|'CREATING'|'FAILED',
            'ProductARN': 'string',
            'CreatedTime': datetime(2015, 1, 1)
        },
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    """
    pass

def update_provisioned_product(AcceptLanguage=None, ProvisionedProductName=None, ProvisionedProductId=None, ProductId=None, ProvisioningArtifactId=None, PathId=None, ProvisioningParameters=None, UpdateToken=None):
    """
    Requests updates to the configuration of an existing ProvisionedProduct object. If there are tags associated with the object, they cannot be updated or added with this operation. Depending on the specific updates requested, this operation may update with no interruption, with some interruption, or replace the ProvisionedProduct object entirely.
    You can check the status of this request using the  DescribeRecord operation.
    See also: AWS API Documentation
    
    
    :example: response = client.update_provisioned_product(
        AcceptLanguage='string',
        ProvisionedProductName='string',
        ProvisionedProductId='string',
        ProductId='string',
        ProvisioningArtifactId='string',
        PathId='string',
        ProvisioningParameters=[
            {
                'Key': 'string',
                'Value': 'string',
                'UsePreviousValue': True|False
            },
        ],
        UpdateToken='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type ProvisionedProductName: string
    :param ProvisionedProductName: The updated name of the ProvisionedProduct object . You must specify either ProvisionedProductName or ProvisionedProductId , but not both.

    :type ProvisionedProductId: string
    :param ProvisionedProductId: The identifier of the ProvisionedProduct object to update. You must specify either ProvisionedProductName or ProvisionedProductId , but not both.

    :type ProductId: string
    :param ProductId: The identifier of the ProvisionedProduct object.

    :type ProvisioningArtifactId: string
    :param ProvisioningArtifactId: The provisioning artifact identifier for this product.

    :type PathId: string
    :param PathId: The identifier of the path to use in the updated ProvisionedProduct object. This value is optional if the product has a default path, and is required if there is more than one path for the specified product.

    :type ProvisioningParameters: list
    :param ProvisioningParameters: A list of ProvisioningParameter objects used to update the ProvisionedProduct object.
            (dict) --The parameter key/value pair used to update a ProvisionedProduct object. If UsePreviousValue is set to true, Value is ignored and the value for Key is kept as previously set (current value).
            Key (string) --The ProvisioningArtifactParameter.ParameterKey parameter from DescribeProvisioningParameters .
            Value (string) --The value to use for updating the product provisioning. Any constraints on this value can be found in the ProvisioningArtifactParameter parameter for Key .
            UsePreviousValue (boolean) --If true, uses the currently set value for Key , ignoring UpdateProvisioningParameter.Value .
            
            

    :type UpdateToken: string
    :param UpdateToken: [REQUIRED]
            The idempotency token that uniquely identifies the provisioning update request.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'RecordDetail': {
            'RecordId': 'string',
            'ProvisionedProductName': 'string',
            'Status': 'IN_PROGRESS'|'SUCCEEDED'|'ERROR',
            'CreatedTime': datetime(2015, 1, 1),
            'UpdatedTime': datetime(2015, 1, 1),
            'ProvisionedProductType': 'string',
            'RecordType': 'string',
            'ProvisionedProductId': 'string',
            'ProductId': 'string',
            'ProvisioningArtifactId': 'string',
            'PathId': 'string',
            'RecordErrors': [
                {
                    'Code': 'string',
                    'Description': 'string'
                },
            ],
            'RecordTags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def update_provisioning_artifact(AcceptLanguage=None, ProductId=None, ProvisioningArtifactId=None, Name=None, Description=None):
    """
    Updates an existing provisioning artifact's information. This operation will not work on a provisioning artifact associated with a product that has been shared with you.
    See also: AWS API Documentation
    
    
    :example: response = client.update_provisioning_artifact(
        AcceptLanguage='string',
        ProductId='string',
        ProvisioningArtifactId='string',
        Name='string',
        Description='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            

    :type ProductId: string
    :param ProductId: [REQUIRED]
            The product identifier.
            

    :type ProvisioningArtifactId: string
    :param ProvisioningArtifactId: [REQUIRED]
            The identifier of the provisioning artifact for the update request.
            

    :type Name: string
    :param Name: The updated name of the provisioning artifact.

    :type Description: string
    :param Description: The updated text description of the provisioning artifact.

    :rtype: dict
    :return: {
        'ProvisioningArtifactDetail': {
            'Id': 'string',
            'Name': 'string',
            'Description': 'string',
            'Type': 'CLOUD_FORMATION_TEMPLATE',
            'CreatedTime': datetime(2015, 1, 1)
        },
        'Info': {
            'string': 'string'
        },
        'Status': 'AVAILABLE'|'CREATING'|'FAILED'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

