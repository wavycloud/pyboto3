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
    Accepts an offer to share the specified portfolio.
    See also: AWS API Documentation
    
    
    :example: response = client.accept_portfolio_share(
        AcceptLanguage='string',
        PortfolioId='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

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
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type PortfolioId: string
    :param PortfolioId: [REQUIRED]
            The portfolio identifier.
            

    :type PrincipalARN: string
    :param PrincipalARN: [REQUIRED]
            The ARN of the principal (IAM user, role, or group).
            

    :type PrincipalType: string
    :param PrincipalType: [REQUIRED]
            The principal type. The supported value is IAM .
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def associate_product_with_portfolio(AcceptLanguage=None, ProductId=None, PortfolioId=None, SourcePortfolioId=None):
    """
    Associates the specified product with the specified portfolio.
    See also: AWS API Documentation
    
    
    :example: response = client.associate_product_with_portfolio(
        AcceptLanguage='string',
        ProductId='string',
        PortfolioId='string',
        SourcePortfolioId='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type ProductId: string
    :param ProductId: [REQUIRED]
            The product identifier.
            

    :type PortfolioId: string
    :param PortfolioId: [REQUIRED]
            The portfolio identifier.
            

    :type SourcePortfolioId: string
    :param SourcePortfolioId: The identifier of the source portfolio.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def associate_tag_option_with_resource(ResourceId=None, TagOptionId=None):
    """
    Associate the specified TagOption with the specified portfolio or product.
    See also: AWS API Documentation
    
    
    :example: response = client.associate_tag_option_with_resource(
        ResourceId='string',
        TagOptionId='string'
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The resource identifier.
            

    :type TagOptionId: string
    :param TagOptionId: [REQUIRED]
            The TagOption identifier.
            

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

def copy_product(AcceptLanguage=None, SourceProductArn=None, TargetProductId=None, TargetProductName=None, SourceProvisioningArtifactIdentifiers=None, CopyOptions=None, IdempotencyToken=None):
    """
    Copies the specified source product to the specified target product or a new product.
    You can copy a product to the same account or another account. You can copy a product to the same region or another region.
    This operation is performed asynchronously. To track the progress of the operation, use  DescribeCopyProductStatus .
    See also: AWS API Documentation
    
    
    :example: response = client.copy_product(
        AcceptLanguage='string',
        SourceProductArn='string',
        TargetProductId='string',
        TargetProductName='string',
        SourceProvisioningArtifactIdentifiers=[
            {
                'string': 'string'
            },
        ],
        CopyOptions=[
            'CopyTags',
        ],
        IdempotencyToken='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type SourceProductArn: string
    :param SourceProductArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the source product.
            

    :type TargetProductId: string
    :param TargetProductId: The identifier of the target product. By default, a new product is created.

    :type TargetProductName: string
    :param TargetProductName: A name for the target product. The default is the name of the source product.

    :type SourceProvisioningArtifactIdentifiers: list
    :param SourceProvisioningArtifactIdentifiers: The identifiers of the provisioning artifacts (also known as versions) of the product to copy. By default, all provisioning artifacts are copied.
            (dict) --
            (string) --
            (string) --
            
            

    :type CopyOptions: list
    :param CopyOptions: The copy options. If the value is CopyTags , the tags from the source product are copied to the target product.
            (string) --
            

    :type IdempotencyToken: string
    :param IdempotencyToken: [REQUIRED]
            A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'CopyProductToken': 'string'
    }
    
    
    """
    pass

def create_constraint(AcceptLanguage=None, PortfolioId=None, ProductId=None, Parameters=None, Type=None, Description=None, IdempotencyToken=None):
    """
    Creates a constraint.
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
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type PortfolioId: string
    :param PortfolioId: [REQUIRED]
            The portfolio identifier.
            

    :type ProductId: string
    :param ProductId: [REQUIRED]
            The product identifier.
            

    :type Parameters: string
    :param Parameters: [REQUIRED]
            The constraint parameters, in JSON format. The syntax depends on the constraint type as follows:
            LAUNCH
            Specify the RoleArn property as follows:
            'RoleArn' : 'arn:aws:iam::123456789012:role/LaunchRole'
            NOTIFICATION
            Specify the NotificationArns property as follows:
            'NotificationArns' : ['arn:aws:sns:us-east-1:123456789012:Topic']
            TEMPLATE
            Specify the Rules property. For more information, see Template Constraint Rules .
            

    :type Type: string
    :param Type: [REQUIRED]
            The type of constraint.
            LAUNCH
            NOTIFICATION
            TEMPLATE
            

    :type Description: string
    :param Description: The description of the constraint.

    :type IdempotencyToken: string
    :param IdempotencyToken: [REQUIRED]
            A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.
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
    
    
    :returns: 
    LAUNCH
    NOTIFICATION
    TEMPLATE
    
    """
    pass

def create_portfolio(AcceptLanguage=None, DisplayName=None, Description=None, ProviderName=None, Tags=None, IdempotencyToken=None):
    """
    Creates a portfolio.
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
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type DisplayName: string
    :param DisplayName: [REQUIRED]
            The name to use for display purposes.
            

    :type Description: string
    :param Description: The description of the portfolio.

    :type ProviderName: string
    :param ProviderName: [REQUIRED]
            The name of the portfolio provider.
            

    :type Tags: list
    :param Tags: One or more tags.
            (dict) --Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.
            Key (string) -- [REQUIRED]The tag key.
            Value (string) -- [REQUIRED]The value for this key.
            
            

    :type IdempotencyToken: string
    :param IdempotencyToken: [REQUIRED]
            A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.
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
    Shares the specified portfolio with the specified account.
    See also: AWS API Documentation
    
    
    :example: response = client.create_portfolio_share(
        AcceptLanguage='string',
        PortfolioId='string',
        AccountId='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type PortfolioId: string
    :param PortfolioId: [REQUIRED]
            The portfolio identifier.
            

    :type AccountId: string
    :param AccountId: [REQUIRED]
            The AWS account ID.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def create_product(AcceptLanguage=None, Name=None, Owner=None, Description=None, Distributor=None, SupportDescription=None, SupportEmail=None, SupportUrl=None, ProductType=None, Tags=None, ProvisioningArtifactParameters=None, IdempotencyToken=None):
    """
    Creates a product.
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
        ProductType='CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE',
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
            'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE_AMI'|'MARKETPLACE_CAR'
        },
        IdempotencyToken='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type Name: string
    :param Name: [REQUIRED]
            The name of the product.
            

    :type Owner: string
    :param Owner: [REQUIRED]
            The owner of the product.
            

    :type Description: string
    :param Description: The description of the product.

    :type Distributor: string
    :param Distributor: The distributor of the product.

    :type SupportDescription: string
    :param SupportDescription: The support information about the product.

    :type SupportEmail: string
    :param SupportEmail: The contact email for product support.

    :type SupportUrl: string
    :param SupportUrl: The contact URL for product support.

    :type ProductType: string
    :param ProductType: [REQUIRED]
            The type of product.
            

    :type Tags: list
    :param Tags: One or more tags.
            (dict) --Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.
            Key (string) -- [REQUIRED]The tag key.
            Value (string) -- [REQUIRED]The value for this key.
            
            

    :type ProvisioningArtifactParameters: dict
    :param ProvisioningArtifactParameters: [REQUIRED]
            The configuration of the provisioning artifact.
            Name (string) --The name of the provisioning artifact (for example, v1 v2beta). No spaces are allowed.
            Description (string) --The description of the provisioning artifact, including how it differs from the previous provisioning artifact.
            Info (dict) -- [REQUIRED]The URL of the CloudFormation template in Amazon S3. Specify the URL in JSON format as follows:
            'LoadTemplateFromURL': 'https://s3.amazonaws.com/cf-templates-ozkq9d3hgiq2-us-east-1/...'
            (string) --
            (string) --
            
            Type (string) --The type of provisioning artifact.
            CLOUD_FORMATION_TEMPLATE - AWS CloudFormation template
            MARKETPLACE_AMI - AWS Marketplace AMI
            MARKETPLACE_CAR - AWS Marketplace Clusters and AWS Resources
            

    :type IdempotencyToken: string
    :param IdempotencyToken: [REQUIRED]
            A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.
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
                'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE',
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
            'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE_AMI'|'MARKETPLACE_CAR',
            'CreatedTime': datetime(2015, 1, 1),
            'Active': True|False
        },
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    :returns: 
    AVAILABLE - The product is ready for use.
    CREATING - Product creation has started; the product is not ready for use.
    FAILED - An action failed.
    
    """
    pass

def create_provisioned_product_plan(AcceptLanguage=None, PlanName=None, PlanType=None, NotificationArns=None, PathId=None, ProductId=None, ProvisionedProductName=None, ProvisioningArtifactId=None, ProvisioningParameters=None, IdempotencyToken=None, Tags=None):
    """
    Creates a plan. A plan includes the list of resources to be created (when provisioning a new product) or modified (when updating a provisioned product) when the plan is executed.
    You can create one plan per provisioned product. To create a plan for an existing provisioned product, the product status must be AVAILBLE or TAINTED.
    To view the resource changes in the change set, use  DescribeProvisionedProductPlan . To create or modify the provisioned product, use  ExecuteProvisionedProductPlan .
    See also: AWS API Documentation
    
    
    :example: response = client.create_provisioned_product_plan(
        AcceptLanguage='string',
        PlanName='string',
        PlanType='CLOUDFORMATION',
        NotificationArns=[
            'string',
        ],
        PathId='string',
        ProductId='string',
        ProvisionedProductName='string',
        ProvisioningArtifactId='string',
        ProvisioningParameters=[
            {
                'Key': 'string',
                'Value': 'string',
                'UsePreviousValue': True|False
            },
        ],
        IdempotencyToken='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type PlanName: string
    :param PlanName: [REQUIRED]
            The name of the plan.
            

    :type PlanType: string
    :param PlanType: [REQUIRED]
            The plan type.
            

    :type NotificationArns: list
    :param NotificationArns: Passed to CloudFormation. The SNS topic ARNs to which to publish stack-related events.
            (string) --
            

    :type PathId: string
    :param PathId: The path identifier of the product. This value is optional if the product has a default path, and required if the product has more than one path. To list the paths for a product, use ListLaunchPaths .

    :type ProductId: string
    :param ProductId: [REQUIRED]
            The product identifier.
            

    :type ProvisionedProductName: string
    :param ProvisionedProductName: [REQUIRED]
            A user-friendly name for the provisioned product. This value must be unique for the AWS account and cannot be updated after the product is provisioned.
            

    :type ProvisioningArtifactId: string
    :param ProvisioningArtifactId: [REQUIRED]
            The identifier of the provisioning artifact.
            

    :type ProvisioningParameters: list
    :param ProvisioningParameters: Parameters specified by the administrator that are required for provisioning the product.
            (dict) --The parameter key-value pair used to update a provisioned product.
            Key (string) --The parameter key.
            Value (string) --The parameter value.
            UsePreviousValue (boolean) --If set to true, Value is ignored and the previous parameter value is kept.
            
            

    :type IdempotencyToken: string
    :param IdempotencyToken: [REQUIRED]
            A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.
            This field is autopopulated if not provided.
            

    :type Tags: list
    :param Tags: One or more tags.
            (dict) --Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.
            Key (string) -- [REQUIRED]The tag key.
            Value (string) -- [REQUIRED]The value for this key.
            
            

    :rtype: dict
    :return: {
        'PlanName': 'string',
        'PlanId': 'string',
        'ProvisionProductId': 'string',
        'ProvisionedProductName': 'string',
        'ProvisioningArtifactId': 'string'
    }
    
    
    """
    pass

def create_provisioning_artifact(AcceptLanguage=None, ProductId=None, Parameters=None, IdempotencyToken=None):
    """
    Creates a provisioning artifact (also known as a version) for the specified product.
    You cannot create a provisioning artifact for a product that was shared with you.
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
            'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE_AMI'|'MARKETPLACE_CAR'
        },
        IdempotencyToken='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type ProductId: string
    :param ProductId: [REQUIRED]
            The product identifier.
            

    :type Parameters: dict
    :param Parameters: [REQUIRED]
            The configuration for the provisioning artifact.
            Name (string) --The name of the provisioning artifact (for example, v1 v2beta). No spaces are allowed.
            Description (string) --The description of the provisioning artifact, including how it differs from the previous provisioning artifact.
            Info (dict) -- [REQUIRED]The URL of the CloudFormation template in Amazon S3. Specify the URL in JSON format as follows:
            'LoadTemplateFromURL': 'https://s3.amazonaws.com/cf-templates-ozkq9d3hgiq2-us-east-1/...'
            (string) --
            (string) --
            
            Type (string) --The type of provisioning artifact.
            CLOUD_FORMATION_TEMPLATE - AWS CloudFormation template
            MARKETPLACE_AMI - AWS Marketplace AMI
            MARKETPLACE_CAR - AWS Marketplace Clusters and AWS Resources
            

    :type IdempotencyToken: string
    :param IdempotencyToken: [REQUIRED]
            A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'ProvisioningArtifactDetail': {
            'Id': 'string',
            'Name': 'string',
            'Description': 'string',
            'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE_AMI'|'MARKETPLACE_CAR',
            'CreatedTime': datetime(2015, 1, 1),
            'Active': True|False
        },
        'Info': {
            'string': 'string'
        },
        'Status': 'AVAILABLE'|'CREATING'|'FAILED'
    }
    
    
    :returns: 
    CLOUD_FORMATION_TEMPLATE - AWS CloudFormation template
    MARKETPLACE_AMI - AWS Marketplace AMI
    MARKETPLACE_CAR - AWS Marketplace Clusters and AWS Resources
    
    """
    pass

def create_tag_option(Key=None, Value=None):
    """
    Creates a TagOption.
    See also: AWS API Documentation
    
    
    :example: response = client.create_tag_option(
        Key='string',
        Value='string'
    )
    
    
    :type Key: string
    :param Key: [REQUIRED]
            The TagOption key.
            

    :type Value: string
    :param Value: [REQUIRED]
            The TagOption value.
            

    :rtype: dict
    :return: {
        'TagOptionDetail': {
            'Key': 'string',
            'Value': 'string',
            'Active': True|False,
            'Id': 'string'
        }
    }
    
    
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
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type Id: string
    :param Id: [REQUIRED]
            The identifier of the constraint.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_portfolio(AcceptLanguage=None, Id=None):
    """
    Deletes the specified portfolio.
    You cannot delete a portfolio if it was shared with you or if it has associated products, users, constraints, or shared accounts.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_portfolio(
        AcceptLanguage='string',
        Id='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type Id: string
    :param Id: [REQUIRED]
            The portfolio identifier.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_portfolio_share(AcceptLanguage=None, PortfolioId=None, AccountId=None):
    """
    Stops sharing the specified portfolio with the specified account.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_portfolio_share(
        AcceptLanguage='string',
        PortfolioId='string',
        AccountId='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type PortfolioId: string
    :param PortfolioId: [REQUIRED]
            The portfolio identifier.
            

    :type AccountId: string
    :param AccountId: [REQUIRED]
            The AWS account ID.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_product(AcceptLanguage=None, Id=None):
    """
    Deletes the specified product.
    You cannot delete a product if it was shared with you or is associated with a portfolio.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_product(
        AcceptLanguage='string',
        Id='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type Id: string
    :param Id: [REQUIRED]
            The product identifier.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_provisioned_product_plan(AcceptLanguage=None, PlanId=None, IgnoreErrors=None):
    """
    Deletes the specified plan.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_provisioned_product_plan(
        AcceptLanguage='string',
        PlanId='string',
        IgnoreErrors=True|False
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type PlanId: string
    :param PlanId: [REQUIRED]
            The plan identifier.
            

    :type IgnoreErrors: boolean
    :param IgnoreErrors: If set to true, AWS Service Catalog stops managing the specified provisioned product even if it cannot delete the underlying resources.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_provisioning_artifact(AcceptLanguage=None, ProductId=None, ProvisioningArtifactId=None):
    """
    Deletes the specified provisioning artifact (also known as a version) for the specified product.
    You cannot delete a provisioning artifact associated with a product that was shared with you. You cannot delete the last provisioning artifact for a product, because a product must have at least one provisioning artifact.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_provisioning_artifact(
        AcceptLanguage='string',
        ProductId='string',
        ProvisioningArtifactId='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type ProductId: string
    :param ProductId: [REQUIRED]
            The product identifier.
            

    :type ProvisioningArtifactId: string
    :param ProvisioningArtifactId: [REQUIRED]
            The identifier of the provisioning artifact.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_tag_option(Id=None):
    """
    Deletes the specified TagOption.
    You cannot delete a TagOption if it is associated with a product or portfolio.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_tag_option(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The TagOption identifier.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def describe_constraint(AcceptLanguage=None, Id=None):
    """
    Gets information about the specified constraint.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_constraint(
        AcceptLanguage='string',
        Id='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

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
    
    
    :returns: 
    LAUNCH
    NOTIFICATION
    TEMPLATE
    
    """
    pass

def describe_copy_product_status(AcceptLanguage=None, CopyProductToken=None):
    """
    Gets the status of the specified copy product operation.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_copy_product_status(
        AcceptLanguage='string',
        CopyProductToken='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type CopyProductToken: string
    :param CopyProductToken: [REQUIRED]
            The token for the copy product operation. This token is returned by CopyProduct .
            

    :rtype: dict
    :return: {
        'CopyProductStatus': 'SUCCEEDED'|'IN_PROGRESS'|'FAILED',
        'TargetProductId': 'string',
        'StatusDetail': 'string'
    }
    
    
    """
    pass

def describe_portfolio(AcceptLanguage=None, Id=None):
    """
    Gets information about the specified portfolio.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_portfolio(
        AcceptLanguage='string',
        Id='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type Id: string
    :param Id: [REQUIRED]
            The portfolio identifier.
            

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
        ],
        'TagOptions': [
            {
                'Key': 'string',
                'Value': 'string',
                'Active': True|False,
                'Id': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_product(AcceptLanguage=None, Id=None):
    """
    Gets information about the specified product.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_product(
        AcceptLanguage='string',
        Id='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type Id: string
    :param Id: [REQUIRED]
            The product identifier.
            

    :rtype: dict
    :return: {
        'ProductViewSummary': {
            'Id': 'string',
            'ProductId': 'string',
            'Name': 'string',
            'Owner': 'string',
            'ShortDescription': 'string',
            'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE',
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
    Gets information about the specified product. This operation is run with administrator access.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_product_as_admin(
        AcceptLanguage='string',
        Id='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type Id: string
    :param Id: [REQUIRED]
            The product identifier.
            

    :rtype: dict
    :return: {
        'ProductViewDetail': {
            'ProductViewSummary': {
                'Id': 'string',
                'ProductId': 'string',
                'Name': 'string',
                'Owner': 'string',
                'ShortDescription': 'string',
                'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE',
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
        'ProvisioningArtifactSummaries': [
            {
                'Id': 'string',
                'Name': 'string',
                'Description': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'ProvisioningArtifactMetadata': {
                    'string': 'string'
                }
            },
        ],
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'TagOptions': [
            {
                'Key': 'string',
                'Value': 'string',
                'Active': True|False,
                'Id': 'string'
            },
        ]
    }
    
    
    :returns: 
    AVAILABLE - The product is ready for use.
    CREATING - Product creation has started; the product is not ready for use.
    FAILED - An action failed.
    
    """
    pass

def describe_product_view(AcceptLanguage=None, Id=None):
    """
    Gets information about the specified product.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_product_view(
        AcceptLanguage='string',
        Id='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type Id: string
    :param Id: [REQUIRED]
            The product view identifier.
            

    :rtype: dict
    :return: {
        'ProductViewSummary': {
            'Id': 'string',
            'ProductId': 'string',
            'Name': 'string',
            'Owner': 'string',
            'ShortDescription': 'string',
            'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE',
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

def describe_provisioned_product(AcceptLanguage=None, Id=None):
    """
    Gets information about the specified provisioned product.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_provisioned_product(
        AcceptLanguage='string',
        Id='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type Id: string
    :param Id: [REQUIRED]
            The provisioned product identifier.
            

    :rtype: dict
    :return: {
        'ProvisionedProductDetail': {
            'Name': 'string',
            'Arn': 'string',
            'Type': 'string',
            'Id': 'string',
            'Status': 'AVAILABLE'|'UNDER_CHANGE'|'TAINTED'|'ERROR'|'PLAN_IN_PROGRESS',
            'StatusMessage': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'IdempotencyToken': 'string',
            'LastRecordId': 'string'
        },
        'CloudWatchDashboards': [
            {
                'Name': 'string'
            },
        ]
    }
    
    
    :returns: 
    AVAILABLE - Stable state, ready to perform any operation. The most recent operation succeeded and completed.
    UNDER_CHANGE - Transitive state, operations performed might not have valid results. Wait for an AVAILABLE status before performing operations.
    TAINTED - Stable state, ready to perform any operation. The stack has completed the requested operation but is not exactly what was requested. For example, a request to update to a new version failed and the stack rolled back to the current version.
    ERROR - An unexpected error occurred, the provisioned product exists but the stack is not running. For example, CloudFormation received a parameter value that was not valid and could not launch the stack.
    
    """
    pass

def describe_provisioned_product_plan(AcceptLanguage=None, PlanId=None, PageSize=None, PageToken=None):
    """
    Gets information about the resource changes for the specified plan.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_provisioned_product_plan(
        AcceptLanguage='string',
        PlanId='string',
        PageSize=123,
        PageToken='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type PlanId: string
    :param PlanId: [REQUIRED]
            The plan identifier.
            

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :rtype: dict
    :return: {
        'ProvisionedProductPlanDetails': {
            'CreatedTime': datetime(2015, 1, 1),
            'PathId': 'string',
            'ProductId': 'string',
            'PlanName': 'string',
            'PlanId': 'string',
            'ProvisionProductId': 'string',
            'ProvisionProductName': 'string',
            'PlanType': 'CLOUDFORMATION',
            'ProvisioningArtifactId': 'string',
            'Status': 'CREATE_IN_PROGRESS'|'CREATE_SUCCESS'|'CREATE_FAILED'|'EXECUTE_IN_PROGRESS'|'EXECUTE_SUCCESS'|'EXECUTE_FAILED',
            'UpdatedTime': datetime(2015, 1, 1),
            'NotificationArns': [
                'string',
            ],
            'ProvisioningParameters': [
                {
                    'Key': 'string',
                    'Value': 'string',
                    'UsePreviousValue': True|False
                },
            ],
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'StatusMessage': 'string'
        },
        'ResourceChanges': [
            {
                'Action': 'ADD'|'MODIFY'|'REMOVE',
                'LogicalResourceId': 'string',
                'PhysicalResourceId': 'string',
                'ResourceType': 'string',
                'Replacement': 'TRUE'|'FALSE'|'CONDITIONAL',
                'Scope': [
                    'PROPERTIES'|'METADATA'|'CREATIONPOLICY'|'UPDATEPOLICY'|'DELETIONPOLICY'|'TAGS',
                ],
                'Details': [
                    {
                        'Target': {
                            'Attribute': 'PROPERTIES'|'METADATA'|'CREATIONPOLICY'|'UPDATEPOLICY'|'DELETIONPOLICY'|'TAGS',
                            'Name': 'string',
                            'RequiresRecreation': 'NEVER'|'CONDITIONALLY'|'ALWAYS'
                        },
                        'Evaluation': 'STATIC'|'DYNAMIC',
                        'CausingEntity': 'string'
                    },
                ]
            },
        ],
        'NextPageToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_provisioning_artifact(AcceptLanguage=None, ProvisioningArtifactId=None, ProductId=None, Verbose=None):
    """
    Gets information about the specified provisioning artifact (also known as a version) for the specified product.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_provisioning_artifact(
        AcceptLanguage='string',
        ProvisioningArtifactId='string',
        ProductId='string',
        Verbose=True|False
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type ProvisioningArtifactId: string
    :param ProvisioningArtifactId: [REQUIRED]
            The identifier of the provisioning artifact.
            

    :type ProductId: string
    :param ProductId: [REQUIRED]
            The product identifier.
            

    :type Verbose: boolean
    :param Verbose: Indicates whether a verbose level of detail is enabled.

    :rtype: dict
    :return: {
        'ProvisioningArtifactDetail': {
            'Id': 'string',
            'Name': 'string',
            'Description': 'string',
            'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE_AMI'|'MARKETPLACE_CAR',
            'CreatedTime': datetime(2015, 1, 1),
            'Active': True|False
        },
        'Info': {
            'string': 'string'
        },
        'Status': 'AVAILABLE'|'CREATING'|'FAILED'
    }
    
    
    :returns: 
    CLOUD_FORMATION_TEMPLATE - AWS CloudFormation template
    MARKETPLACE_AMI - AWS Marketplace AMI
    MARKETPLACE_CAR - AWS Marketplace Clusters and AWS Resources
    
    """
    pass

def describe_provisioning_parameters(AcceptLanguage=None, ProductId=None, ProvisioningArtifactId=None, PathId=None):
    """
    Gets information about the configuration required to provision the specified product using the specified provisioning artifact.
    If the output contains a TagOption key with an empty list of values, there is a TagOption conflict for that key. The end user cannot take action to fix the conflict, and launch is not blocked. In subsequent calls to  ProvisionProduct , do not include conflicted TagOption keys as tags, or this causes the error "Parameter validation failed: Missing required parameter in Tags[N ]:Value ". Tag the provisioned product with the value sc-tagoption-conflict-portfolioId-productId .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_provisioning_parameters(
        AcceptLanguage='string',
        ProductId='string',
        ProvisioningArtifactId='string',
        PathId='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type ProductId: string
    :param ProductId: [REQUIRED]
            The product identifier.
            

    :type ProvisioningArtifactId: string
    :param ProvisioningArtifactId: [REQUIRED]
            The identifier of the provisioning artifact.
            

    :type PathId: string
    :param PathId: The path identifier of the product. This value is optional if the product has a default path, and required if the product has more than one path. To list the paths for a product, use ListLaunchPaths .

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
        ],
        'TagOptions': [
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_record(AcceptLanguage=None, Id=None, PageToken=None, PageSize=None):
    """
    Gets information about the specified request operation.
    Use this operation after calling a request operation (for example,  ProvisionProduct ,  TerminateProvisionedProduct , or  UpdateProvisionedProduct ).
    See also: AWS API Documentation
    
    
    :example: response = client.describe_record(
        AcceptLanguage='string',
        Id='string',
        PageToken='string',
        PageSize=123
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type Id: string
    :param Id: [REQUIRED]
            The record identifier of the provisioned product. This identifier is returned by the request operation.
            

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :rtype: dict
    :return: {
        'RecordDetail': {
            'RecordId': 'string',
            'ProvisionedProductName': 'string',
            'Status': 'CREATED'|'IN_PROGRESS'|'IN_PROGRESS_IN_ERROR'|'SUCCEEDED'|'FAILED',
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
    
    
    :returns: 
    CREATED - The request was created but the operation has not started.
    IN_PROGRESS - The requested operation is in progress.
    IN_PROGRESS_IN_ERROR - The provisioned product is under change but the requested operation failed and some remediation is occurring. For example, a rollback.
    SUCCEEDED - The requested operation has successfully completed.
    FAILED - The requested operation has unsuccessfully completed. Investigate using the error messages returned.
    
    """
    pass

def describe_tag_option(Id=None):
    """
    Gets information about the specified TagOption.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_tag_option(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The TagOption identifier.
            

    :rtype: dict
    :return: {
        'TagOptionDetail': {
            'Key': 'string',
            'Value': 'string',
            'Active': True|False,
            'Id': 'string'
        }
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
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type PortfolioId: string
    :param PortfolioId: [REQUIRED]
            The portfolio identifier.
            

    :type PrincipalARN: string
    :param PrincipalARN: [REQUIRED]
            The ARN of the principal (IAM user, role, or group).
            

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
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

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

def disassociate_tag_option_from_resource(ResourceId=None, TagOptionId=None):
    """
    Disassociates the specified TagOption from the specified resource.
    See also: AWS API Documentation
    
    
    :example: response = client.disassociate_tag_option_from_resource(
        ResourceId='string',
        TagOptionId='string'
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The resource identifier.
            

    :type TagOptionId: string
    :param TagOptionId: [REQUIRED]
            The TagOption identifier.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def execute_provisioned_product_plan(AcceptLanguage=None, PlanId=None, IdempotencyToken=None):
    """
    Provisions or modifies a product based on the resource changes for the specified plan.
    See also: AWS API Documentation
    
    
    :example: response = client.execute_provisioned_product_plan(
        AcceptLanguage='string',
        PlanId='string',
        IdempotencyToken='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type PlanId: string
    :param PlanId: [REQUIRED]
            The plan identifier.
            

    :type IdempotencyToken: string
    :param IdempotencyToken: [REQUIRED]
            A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'RecordDetail': {
            'RecordId': 'string',
            'ProvisionedProductName': 'string',
            'Status': 'CREATED'|'IN_PROGRESS'|'IN_PROGRESS_IN_ERROR'|'SUCCEEDED'|'FAILED',
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
    
    
    :returns: 
    CREATED - The request was created but the operation has not started.
    IN_PROGRESS - The requested operation is in progress.
    IN_PROGRESS_IN_ERROR - The provisioned product is under change but the requested operation failed and some remediation is occurring. For example, a rollback.
    SUCCEEDED - The requested operation has successfully completed.
    FAILED - The requested operation has unsuccessfully completed. Investigate using the error messages returned.
    
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
    Lists all portfolios for which sharing was accepted by this account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_accepted_portfolio_shares(
        AcceptLanguage='string',
        PageToken='string',
        PageSize=123
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

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
    Lists the constraints for the specified portfolio and product.
    See also: AWS API Documentation
    
    
    :example: response = client.list_constraints_for_portfolio(
        AcceptLanguage='string',
        PortfolioId='string',
        ProductId='string',
        PageSize=123,
        PageToken='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type PortfolioId: string
    :param PortfolioId: [REQUIRED]
            The portfolio identifier.
            

    :type ProductId: string
    :param ProductId: The product identifier.

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

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
    
    
    :returns: 
    LAUNCH
    NOTIFICATION
    TEMPLATE
    
    """
    pass

def list_launch_paths(AcceptLanguage=None, ProductId=None, PageSize=None, PageToken=None):
    """
    Lists the paths to the specified product. A path is how the user has access to a specified product, and is necessary when provisioning a product. A path also determines the constraints put on the product.
    See also: AWS API Documentation
    
    
    :example: response = client.list_launch_paths(
        AcceptLanguage='string',
        ProductId='string',
        PageSize=123,
        PageToken='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type ProductId: string
    :param ProductId: [REQUIRED]
            The product identifier.
            

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

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
    
    
    :returns: 
    LAUNCH
    NOTIFICATION
    TEMPLATE
    
    """
    pass

def list_portfolio_access(AcceptLanguage=None, PortfolioId=None):
    """
    Lists the account IDs that have access to the specified portfolio.
    See also: AWS API Documentation
    
    
    :example: response = client.list_portfolio_access(
        AcceptLanguage='string',
        PortfolioId='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

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
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

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
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type ProductId: string
    :param ProductId: [REQUIRED]
            The product identifier.
            

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

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
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type PortfolioId: string
    :param PortfolioId: [REQUIRED]
            The portfolio identifier.
            

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

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

def list_provisioned_product_plans(AcceptLanguage=None, ProvisionProductId=None, PageSize=None, PageToken=None, AccessLevelFilter=None):
    """
    Lists the plans for the specified provisioned product or all plans to which the user has access.
    See also: AWS API Documentation
    
    
    :example: response = client.list_provisioned_product_plans(
        AcceptLanguage='string',
        ProvisionProductId='string',
        PageSize=123,
        PageToken='string',
        AccessLevelFilter={
            'Key': 'Account'|'Role'|'User',
            'Value': 'string'
        }
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type ProvisionProductId: string
    :param ProvisionProductId: The product identifier.

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :type AccessLevelFilter: dict
    :param AccessLevelFilter: The access level to use to obtain results. The default is User .
            Key (string) --The access level.
            Account - Filter results based on the account.
            Role - Filter results based on the federated role of the specified user.
            User - Filter results based on the specified user.
            Value (string) --The user to which the access level applies. The only supported value is Self .
            

    :rtype: dict
    :return: {
        'ProvisionedProductPlans': [
            {
                'PlanName': 'string',
                'PlanId': 'string',
                'ProvisionProductId': 'string',
                'ProvisionProductName': 'string',
                'PlanType': 'CLOUDFORMATION',
                'ProvisioningArtifactId': 'string'
            },
        ],
        'NextPageToken': 'string'
    }
    
    
    """
    pass

def list_provisioning_artifacts(AcceptLanguage=None, ProductId=None):
    """
    Lists all provisioning artifacts (also known as versions) for the specified product.
    See also: AWS API Documentation
    
    
    :example: response = client.list_provisioning_artifacts(
        AcceptLanguage='string',
        ProductId='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

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
                'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE_AMI'|'MARKETPLACE_CAR',
                'CreatedTime': datetime(2015, 1, 1),
                'Active': True|False
            },
        ],
        'NextPageToken': 'string'
    }
    
    
    :returns: 
    CLOUD_FORMATION_TEMPLATE - AWS CloudFormation template
    MARKETPLACE_AMI - AWS Marketplace AMI
    MARKETPLACE_CAR - AWS Marketplace Clusters and AWS Resources
    
    """
    pass

def list_record_history(AcceptLanguage=None, AccessLevelFilter=None, SearchFilter=None, PageSize=None, PageToken=None):
    """
    Lists the specified requests or all performed requests.
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
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type AccessLevelFilter: dict
    :param AccessLevelFilter: The access level to use to obtain results. The default is User .
            Key (string) --The access level.
            Account - Filter results based on the account.
            Role - Filter results based on the federated role of the specified user.
            User - Filter results based on the specified user.
            Value (string) --The user to which the access level applies. The only supported value is Self .
            

    :type SearchFilter: dict
    :param SearchFilter: The search filter to scope the results.
            Key (string) --The filter key.
            product - Filter results based on the specified product identifier.
            provisionedproduct - Filter results based on the provisioned product identifier.
            Value (string) --The filter value.
            

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :rtype: dict
    :return: {
        'RecordDetails': [
            {
                'RecordId': 'string',
                'ProvisionedProductName': 'string',
                'Status': 'CREATED'|'IN_PROGRESS'|'IN_PROGRESS_IN_ERROR'|'SUCCEEDED'|'FAILED',
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
    
    
    :returns: 
    CREATED - The request was created but the operation has not started.
    IN_PROGRESS - The requested operation is in progress.
    IN_PROGRESS_IN_ERROR - The provisioned product is under change but the requested operation failed and some remediation is occurring. For example, a rollback.
    SUCCEEDED - The requested operation has successfully completed.
    FAILED - The requested operation has unsuccessfully completed. Investigate using the error messages returned.
    
    """
    pass

def list_resources_for_tag_option(TagOptionId=None, ResourceType=None, PageSize=None, PageToken=None):
    """
    Lists the resources associated with the specified TagOption.
    See also: AWS API Documentation
    
    
    :example: response = client.list_resources_for_tag_option(
        TagOptionId='string',
        ResourceType='string',
        PageSize=123,
        PageToken='string'
    )
    
    
    :type TagOptionId: string
    :param TagOptionId: [REQUIRED]
            The TagOption identifier.
            

    :type ResourceType: string
    :param ResourceType: The resource type.
            Portfolio
            Product
            

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :rtype: dict
    :return: {
        'ResourceDetails': [
            {
                'Id': 'string',
                'ARN': 'string',
                'Name': 'string',
                'Description': 'string',
                'CreatedTime': datetime(2015, 1, 1)
            },
        ],
        'PageToken': 'string'
    }
    
    
    """
    pass

def list_tag_options(Filters=None, PageSize=None, PageToken=None):
    """
    Lists the specified TagOptions or all TagOptions.
    See also: AWS API Documentation
    
    
    :example: response = client.list_tag_options(
        Filters={
            'Key': 'string',
            'Value': 'string',
            'Active': True|False
        },
        PageSize=123,
        PageToken='string'
    )
    
    
    :type Filters: dict
    :param Filters: The search filters. If no search filters are specified, the output includes all TagOptions.
            Key (string) --The TagOption key.
            Value (string) --The TagOption value.
            Active (boolean) --The active state.
            

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :rtype: dict
    :return: {
        'TagOptionDetails': [
            {
                'Key': 'string',
                'Value': 'string',
                'Active': True|False,
                'Id': 'string'
            },
        ],
        'PageToken': 'string'
    }
    
    
    """
    pass

def provision_product(AcceptLanguage=None, ProductId=None, ProvisioningArtifactId=None, PathId=None, ProvisionedProductName=None, ProvisioningParameters=None, Tags=None, NotificationArns=None, ProvisionToken=None):
    """
    Provisions the specified product.
    A provisioned product is a resourced instance of a product. For example, provisioning a product based on a CloudFormation template launches a CloudFormation stack and its underlying resources. You can check the status of this request using  DescribeRecord .
    If the request contains a tag key with an empty list of values, there is a tag conflict for that key. Do not include conflicted keys as tags, or this causes the error "Parameter validation failed: Missing required parameter in Tags[N ]:Value ".
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
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type ProductId: string
    :param ProductId: [REQUIRED]
            The product identifier.
            

    :type ProvisioningArtifactId: string
    :param ProvisioningArtifactId: [REQUIRED]
            The identifier of the provisioning artifact.
            

    :type PathId: string
    :param PathId: The path identifier of the product. This value is optional if the product has a default path, and required if the product has more than one path. To list the paths for a product, use ListLaunchPaths .

    :type ProvisionedProductName: string
    :param ProvisionedProductName: [REQUIRED]
            A user-friendly name for the provisioned product. This value must be unique for the AWS account and cannot be updated after the product is provisioned.
            

    :type ProvisioningParameters: list
    :param ProvisioningParameters: Parameters specified by the administrator that are required for provisioning the product.
            (dict) --Information about a parameter used to provision a product.
            Key (string) --The parameter key.
            Value (string) --The parameter value.
            
            

    :type Tags: list
    :param Tags: One or more tags.
            (dict) --Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.
            Key (string) -- [REQUIRED]The tag key.
            Value (string) -- [REQUIRED]The value for this key.
            
            

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
            'Status': 'CREATED'|'IN_PROGRESS'|'IN_PROGRESS_IN_ERROR'|'SUCCEEDED'|'FAILED',
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
    
    
    :returns: 
    CREATED - The request was created but the operation has not started.
    IN_PROGRESS - The requested operation is in progress.
    IN_PROGRESS_IN_ERROR - The provisioned product is under change but the requested operation failed and some remediation is occurring. For example, a rollback.
    SUCCEEDED - The requested operation has successfully completed.
    FAILED - The requested operation has unsuccessfully completed. Investigate using the error messages returned.
    
    """
    pass

def reject_portfolio_share(AcceptLanguage=None, PortfolioId=None):
    """
    Rejects an offer to share the specified portfolio.
    See also: AWS API Documentation
    
    
    :example: response = client.reject_portfolio_share(
        AcceptLanguage='string',
        PortfolioId='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

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
    Lists the provisioned products that are available (not terminated).
    To use additional filtering, see  SearchProvisionedProducts .
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
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type AccessLevelFilter: dict
    :param AccessLevelFilter: The access level to use to obtain results. The default is User .
            Key (string) --The access level.
            Account - Filter results based on the account.
            Role - Filter results based on the federated role of the specified user.
            User - Filter results based on the specified user.
            Value (string) --The user to which the access level applies. The only supported value is Self .
            

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :rtype: dict
    :return: {
        'ProvisionedProducts': [
            {
                'Name': 'string',
                'Arn': 'string',
                'Type': 'string',
                'Id': 'string',
                'Status': 'AVAILABLE'|'UNDER_CHANGE'|'TAINTED'|'ERROR'|'PLAN_IN_PROGRESS',
                'StatusMessage': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'IdempotencyToken': 'string',
                'LastRecordId': 'string'
            },
        ],
        'NextPageToken': 'string'
    }
    
    
    :returns: 
    AVAILABLE - Stable state, ready to perform any operation. The most recent operation succeeded and completed.
    UNDER_CHANGE - Transitive state, operations performed might not have valid results. Wait for an AVAILABLE status before performing operations.
    TAINTED - Stable state, ready to perform any operation. The stack has completed the requested operation but is not exactly what was requested. For example, a request to update to a new version failed and the stack rolled back to the current version.
    ERROR - An unexpected error occurred, the provisioned product exists but the stack is not running. For example, CloudFormation received a parameter value that was not valid and could not launch the stack.
    
    """
    pass

def search_products(AcceptLanguage=None, Filters=None, PageSize=None, SortBy=None, SortOrder=None, PageToken=None):
    """
    Gets information about the products to which the caller has access.
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
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type Filters: dict
    :param Filters: The search filters. If no search filters are specified, the output includes all products to which the caller has access.
            (string) --
            (list) --
            (string) --
            
            

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :type SortBy: string
    :param SortBy: The sort field. If no value is specified, the results are not sorted.

    :type SortOrder: string
    :param SortOrder: The sort order. If no value is specified, the results are not sorted.

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :rtype: dict
    :return: {
        'ProductViewSummaries': [
            {
                'Id': 'string',
                'ProductId': 'string',
                'Name': 'string',
                'Owner': 'string',
                'ShortDescription': 'string',
                'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE',
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
    Gets information about the products for the specified portfolio or all products.
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
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type PortfolioId: string
    :param PortfolioId: The portfolio identifier.

    :type Filters: dict
    :param Filters: The search filters. If no search filters are specified, the output includes all products to which the administrator has access.
            (string) --
            (list) --
            (string) --
            
            

    :type SortBy: string
    :param SortBy: The sort field. If no value is specified, the results are not sorted.

    :type SortOrder: string
    :param SortOrder: The sort order. If no value is specified, the results are not sorted.

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

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
                    'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE',
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
    
    
    :returns: 
    AVAILABLE - The product is ready for use.
    CREATING - Product creation has started; the product is not ready for use.
    FAILED - An action failed.
    
    """
    pass

def search_provisioned_products(AcceptLanguage=None, AccessLevelFilter=None, Filters=None, SortBy=None, SortOrder=None, PageSize=None, PageToken=None):
    """
    Gets information about the provisioned products that meet the specified criteria.
    See also: AWS API Documentation
    
    
    :example: response = client.search_provisioned_products(
        AcceptLanguage='string',
        AccessLevelFilter={
            'Key': 'Account'|'Role'|'User',
            'Value': 'string'
        },
        Filters={
            'string': [
                'string',
            ]
        },
        SortBy='string',
        SortOrder='ASCENDING'|'DESCENDING',
        PageSize=123,
        PageToken='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type AccessLevelFilter: dict
    :param AccessLevelFilter: The access level to use to obtain results. The default is User .
            Key (string) --The access level.
            Account - Filter results based on the account.
            Role - Filter results based on the federated role of the specified user.
            User - Filter results based on the specified user.
            Value (string) --The user to which the access level applies. The only supported value is Self .
            

    :type Filters: dict
    :param Filters: The search filters.
            When the key is SearchQuery , the searchable fields are arn , createdTime , id , lastRecordId , idempotencyToken , name , physicalId , productId , provisioningArtifact , type , status , tags , userArn , and userArnSession .
            Example: 'SearchQuery':['status:AVAILABLE']
            (string) --
            (list) --
            (string) --
            
            

    :type SortBy: string
    :param SortBy: The sort field. If no value is specified, the results are not sorted. The valid values are arn , id , name , and lastRecordId .

    :type SortOrder: string
    :param SortOrder: The sort order. If no value is specified, the results are not sorted.

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :rtype: dict
    :return: {
        'ProvisionedProducts': [
            {
                'Name': 'string',
                'Arn': 'string',
                'Type': 'string',
                'Id': 'string',
                'Status': 'AVAILABLE'|'UNDER_CHANGE'|'TAINTED'|'ERROR'|'PLAN_IN_PROGRESS',
                'StatusMessage': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'IdempotencyToken': 'string',
                'LastRecordId': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'PhysicalId': 'string',
                'ProductId': 'string',
                'ProvisioningArtifactId': 'string',
                'UserArn': 'string',
                'UserArnSession': 'string'
            },
        ],
        'TotalResultsCount': 123,
        'NextPageToken': 'string'
    }
    
    
    :returns: 
    AVAILABLE - Stable state, ready to perform any operation. The most recent operation succeeded and completed.
    UNDER_CHANGE - Transitive state, operations performed might not have valid results. Wait for an AVAILABLE status before performing operations.
    TAINTED - Stable state, ready to perform any operation. The stack has completed the requested operation but is not exactly what was requested. For example, a request to update to a new version failed and the stack rolled back to the current version.
    ERROR - An unexpected error occurred, the provisioned product exists but the stack is not running. For example, CloudFormation received a parameter value that was not valid and could not launch the stack.
    
    """
    pass

def terminate_provisioned_product(ProvisionedProductName=None, ProvisionedProductId=None, TerminateToken=None, IgnoreErrors=None, AcceptLanguage=None):
    """
    Terminates the specified provisioned product.
    This operation does not delete any records associated with the provisioned product.
    You can check the status of this request using  DescribeRecord .
    See also: AWS API Documentation
    
    
    :example: response = client.terminate_provisioned_product(
        ProvisionedProductName='string',
        ProvisionedProductId='string',
        TerminateToken='string',
        IgnoreErrors=True|False,
        AcceptLanguage='string'
    )
    
    
    :type ProvisionedProductName: string
    :param ProvisionedProductName: The name of the provisioned product. You cannot specify both ProvisionedProductName and ProvisionedProductId .

    :type ProvisionedProductId: string
    :param ProvisionedProductId: The identifier of the provisioned product. You cannot specify both ProvisionedProductName and ProvisionedProductId .

    :type TerminateToken: string
    :param TerminateToken: [REQUIRED]
            An idempotency token that uniquely identifies the termination request. This token is only valid during the termination process. After the provisioned product is terminated, subsequent requests to terminate the same provisioned product always return ResourceNotFound .
            This field is autopopulated if not provided.
            

    :type IgnoreErrors: boolean
    :param IgnoreErrors: If set to true, AWS Service Catalog stops managing the specified provisioned product even if it cannot delete the underlying resources.

    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :rtype: dict
    :return: {
        'RecordDetail': {
            'RecordId': 'string',
            'ProvisionedProductName': 'string',
            'Status': 'CREATED'|'IN_PROGRESS'|'IN_PROGRESS_IN_ERROR'|'SUCCEEDED'|'FAILED',
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
    
    
    :returns: 
    CREATED - The request was created but the operation has not started.
    IN_PROGRESS - The requested operation is in progress.
    IN_PROGRESS_IN_ERROR - The provisioned product is under change but the requested operation failed and some remediation is occurring. For example, a rollback.
    SUCCEEDED - The requested operation has successfully completed.
    FAILED - The requested operation has unsuccessfully completed. Investigate using the error messages returned.
    
    """
    pass

def update_constraint(AcceptLanguage=None, Id=None, Description=None):
    """
    Updates the specified constraint.
    See also: AWS API Documentation
    
    
    :example: response = client.update_constraint(
        AcceptLanguage='string',
        Id='string',
        Description='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type Id: string
    :param Id: [REQUIRED]
            The identifier of the constraint.
            

    :type Description: string
    :param Description: The updated description of the constraint.

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
    
    
    :returns: 
    LAUNCH
    NOTIFICATION
    TEMPLATE
    
    """
    pass

def update_portfolio(AcceptLanguage=None, Id=None, DisplayName=None, Description=None, ProviderName=None, AddTags=None, RemoveTags=None):
    """
    Updates the specified portfolio.
    You cannot update a product that was shared with you.
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
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type Id: string
    :param Id: [REQUIRED]
            The portfolio identifier.
            

    :type DisplayName: string
    :param DisplayName: The name to use for display purposes.

    :type Description: string
    :param Description: The updated description of the portfolio.

    :type ProviderName: string
    :param ProviderName: The updated name of the portfolio provider.

    :type AddTags: list
    :param AddTags: The tags to add.
            (dict) --Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.
            Key (string) -- [REQUIRED]The tag key.
            Value (string) -- [REQUIRED]The value for this key.
            
            

    :type RemoveTags: list
    :param RemoveTags: The tags to remove.
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
    Updates the specified product.
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
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type Id: string
    :param Id: [REQUIRED]
            The product identifier.
            

    :type Name: string
    :param Name: The updated product name.

    :type Owner: string
    :param Owner: The updated owner of the product.

    :type Description: string
    :param Description: The updated description of the product.

    :type Distributor: string
    :param Distributor: The updated distributor of the product.

    :type SupportDescription: string
    :param SupportDescription: The updated support description for the product.

    :type SupportEmail: string
    :param SupportEmail: The updated support email for the product.

    :type SupportUrl: string
    :param SupportUrl: The updated support URL for the product.

    :type AddTags: list
    :param AddTags: The tags to add to the product.
            (dict) --Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.
            Key (string) -- [REQUIRED]The tag key.
            Value (string) -- [REQUIRED]The value for this key.
            
            

    :type RemoveTags: list
    :param RemoveTags: The tags to remove from the product.
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
                'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE',
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
    
    
    :returns: 
    AVAILABLE - The product is ready for use.
    CREATING - Product creation has started; the product is not ready for use.
    FAILED - An action failed.
    
    """
    pass

def update_provisioned_product(AcceptLanguage=None, ProvisionedProductName=None, ProvisionedProductId=None, ProductId=None, ProvisioningArtifactId=None, PathId=None, ProvisioningParameters=None, UpdateToken=None):
    """
    Requests updates to the configuration of the specified provisioned product.
    If there are tags associated with the object, they cannot be updated or added. Depending on the specific updates requested, this operation can update with no interruption, with some interruption, or replace the provisioned product entirely.
    You can check the status of this request using  DescribeRecord .
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
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type ProvisionedProductName: string
    :param ProvisionedProductName: The updated name of the provisioned product. You cannot specify both ProvisionedProductName and ProvisionedProductId .

    :type ProvisionedProductId: string
    :param ProvisionedProductId: The identifier of the provisioned product. You cannot specify both ProvisionedProductName and ProvisionedProductId .

    :type ProductId: string
    :param ProductId: The identifier of the provisioned product.

    :type ProvisioningArtifactId: string
    :param ProvisioningArtifactId: The identifier of the provisioning artifact.

    :type PathId: string
    :param PathId: The new path identifier. This value is optional if the product has a default path, and required if the product has more than one path.

    :type ProvisioningParameters: list
    :param ProvisioningParameters: The new parameters.
            (dict) --The parameter key-value pair used to update a provisioned product.
            Key (string) --The parameter key.
            Value (string) --The parameter value.
            UsePreviousValue (boolean) --If set to true, Value is ignored and the previous parameter value is kept.
            
            

    :type UpdateToken: string
    :param UpdateToken: [REQUIRED]
            The idempotency token that uniquely identifies the provisioning update request.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'RecordDetail': {
            'RecordId': 'string',
            'ProvisionedProductName': 'string',
            'Status': 'CREATED'|'IN_PROGRESS'|'IN_PROGRESS_IN_ERROR'|'SUCCEEDED'|'FAILED',
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
    
    
    :returns: 
    CREATED - The request was created but the operation has not started.
    IN_PROGRESS - The requested operation is in progress.
    IN_PROGRESS_IN_ERROR - The provisioned product is under change but the requested operation failed and some remediation is occurring. For example, a rollback.
    SUCCEEDED - The requested operation has successfully completed.
    FAILED - The requested operation has unsuccessfully completed. Investigate using the error messages returned.
    
    """
    pass

def update_provisioning_artifact(AcceptLanguage=None, ProductId=None, ProvisioningArtifactId=None, Name=None, Description=None, Active=None):
    """
    Updates the specified provisioning artifact (also known as a version) for the specified product.
    You cannot update a provisioning artifact for a product that was shared with you.
    See also: AWS API Documentation
    
    
    :example: response = client.update_provisioning_artifact(
        AcceptLanguage='string',
        ProductId='string',
        ProvisioningArtifactId='string',
        Name='string',
        Description='string',
        Active=True|False
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.
            en - English (default)
            jp - Japanese
            zh - Chinese
            

    :type ProductId: string
    :param ProductId: [REQUIRED]
            The product identifier.
            

    :type ProvisioningArtifactId: string
    :param ProvisioningArtifactId: [REQUIRED]
            The identifier of the provisioning artifact.
            

    :type Name: string
    :param Name: The updated name of the provisioning artifact.

    :type Description: string
    :param Description: The updated description of the provisioning artifact.

    :type Active: boolean
    :param Active: Indicates whether the product version is active.

    :rtype: dict
    :return: {
        'ProvisioningArtifactDetail': {
            'Id': 'string',
            'Name': 'string',
            'Description': 'string',
            'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE_AMI'|'MARKETPLACE_CAR',
            'CreatedTime': datetime(2015, 1, 1),
            'Active': True|False
        },
        'Info': {
            'string': 'string'
        },
        'Status': 'AVAILABLE'|'CREATING'|'FAILED'
    }
    
    
    :returns: 
    CLOUD_FORMATION_TEMPLATE - AWS CloudFormation template
    MARKETPLACE_AMI - AWS Marketplace AMI
    MARKETPLACE_CAR - AWS Marketplace Clusters and AWS Resources
    
    """
    pass

def update_tag_option(Id=None, Value=None, Active=None):
    """
    Updates the specified TagOption.
    See also: AWS API Documentation
    
    
    :example: response = client.update_tag_option(
        Id='string',
        Value='string',
        Active=True|False
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The TagOption identifier.
            

    :type Value: string
    :param Value: The updated value.

    :type Active: boolean
    :param Active: The updated active state.

    :rtype: dict
    :return: {
        'TagOptionDetail': {
            'Key': 'string',
            'Value': 'string',
            'Active': True|False,
            'Id': 'string'
        }
    }
    
    
    """
    pass

