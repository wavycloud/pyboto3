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

def accept_portfolio_share(AcceptLanguage=None, PortfolioId=None, PortfolioShareType=None):
    """
    Accepts an offer to share the specified portfolio.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.accept_portfolio_share(
        AcceptLanguage='string',
        PortfolioId='string',
        PortfolioShareType='IMPORTED'|'AWS_SERVICECATALOG'|'AWS_ORGANIZATIONS'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type PortfolioId: string
    :param PortfolioId: [REQUIRED]\nThe portfolio identifier.\n

    :type PortfolioShareType: string
    :param PortfolioShareType: The type of shared portfolios to accept. The default is to accept imported portfolios.\n\nAWS_ORGANIZATIONS - Accept portfolios shared by the master account of your organization.\nIMPORTED - Accept imported portfolios.\nAWS_SERVICECATALOG - Not supported. (Throws ResourceNotFoundException.)\n\nFor example, aws servicecatalog accept-portfolio-share --portfolio-id 'port-2qwzkwxt3y5fk' --portfolio-share-type AWS_ORGANIZATIONS\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ServiceCatalog.Client.exceptions.InvalidParametersException
ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.LimitExceededException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def associate_budget_with_resource(BudgetName=None, ResourceId=None):
    """
    Associates the specified budget with the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_budget_with_resource(
        BudgetName='string',
        ResourceId='string'
    )
    
    
    :type BudgetName: string
    :param BudgetName: [REQUIRED]\nThe name of the budget you want to associate.\n

    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe resource identifier. Either a portfolio-id or a product-id.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ServiceCatalog.Client.exceptions.InvalidParametersException
ServiceCatalog.Client.exceptions.DuplicateResourceException
ServiceCatalog.Client.exceptions.LimitExceededException
ServiceCatalog.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def associate_principal_with_portfolio(AcceptLanguage=None, PortfolioId=None, PrincipalARN=None, PrincipalType=None):
    """
    Associates the specified principal ARN with the specified portfolio.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_principal_with_portfolio(
        AcceptLanguage='string',
        PortfolioId='string',
        PrincipalARN='string',
        PrincipalType='IAM'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type PortfolioId: string
    :param PortfolioId: [REQUIRED]\nThe portfolio identifier.\n

    :type PrincipalARN: string
    :param PrincipalARN: [REQUIRED]\nThe ARN of the principal (IAM user, role, or group).\n

    :type PrincipalType: string
    :param PrincipalType: [REQUIRED]\nThe principal type. The supported value is IAM .\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ServiceCatalog.Client.exceptions.InvalidParametersException
ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.LimitExceededException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def associate_product_with_portfolio(AcceptLanguage=None, ProductId=None, PortfolioId=None, SourcePortfolioId=None):
    """
    Associates the specified product with the specified portfolio.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_product_with_portfolio(
        AcceptLanguage='string',
        ProductId='string',
        PortfolioId='string',
        SourcePortfolioId='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type ProductId: string
    :param ProductId: [REQUIRED]\nThe product identifier.\n

    :type PortfolioId: string
    :param PortfolioId: [REQUIRED]\nThe portfolio identifier.\n

    :type SourcePortfolioId: string
    :param SourcePortfolioId: The identifier of the source portfolio.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ServiceCatalog.Client.exceptions.InvalidParametersException
ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.LimitExceededException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def associate_service_action_with_provisioning_artifact(ProductId=None, ProvisioningArtifactId=None, ServiceActionId=None, AcceptLanguage=None):
    """
    Associates a self-service action with a provisioning artifact.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_service_action_with_provisioning_artifact(
        ProductId='string',
        ProvisioningArtifactId='string',
        ServiceActionId='string',
        AcceptLanguage='string'
    )
    
    
    :type ProductId: string
    :param ProductId: [REQUIRED]\nThe product identifier. For example, prod-abcdzk7xy33qa .\n

    :type ProvisioningArtifactId: string
    :param ProvisioningArtifactId: [REQUIRED]\nThe identifier of the provisioning artifact. For example, pa-4abcdjnxjj6ne .\n

    :type ServiceActionId: string
    :param ServiceActionId: [REQUIRED]\nThe self-service action identifier. For example, act-fs7abcd89wxyz .\n

    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.DuplicateResourceException
ServiceCatalog.Client.exceptions.LimitExceededException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def associate_tag_option_with_resource(ResourceId=None, TagOptionId=None):
    """
    Associate the specified TagOption with the specified portfolio or product.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_tag_option_with_resource(
        ResourceId='string',
        TagOptionId='string'
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe resource identifier.\n

    :type TagOptionId: string
    :param TagOptionId: [REQUIRED]\nThe TagOption identifier.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ServiceCatalog.Client.exceptions.TagOptionNotMigratedException
ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.InvalidParametersException
ServiceCatalog.Client.exceptions.LimitExceededException
ServiceCatalog.Client.exceptions.DuplicateResourceException
ServiceCatalog.Client.exceptions.InvalidStateException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def batch_associate_service_action_with_provisioning_artifact(ServiceActionAssociations=None, AcceptLanguage=None):
    """
    Associates multiple self-service actions with provisioning artifacts.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_associate_service_action_with_provisioning_artifact(
        ServiceActionAssociations=[
            {
                'ServiceActionId': 'string',
                'ProductId': 'string',
                'ProvisioningArtifactId': 'string'
            },
        ],
        AcceptLanguage='string'
    )
    
    
    :type ServiceActionAssociations: list
    :param ServiceActionAssociations: [REQUIRED]\nOne or more associations, each consisting of the Action ID, the Product ID, and the Provisioning Artifact ID.\n\n(dict) --A self-service action association consisting of the Action ID, the Product ID, and the Provisioning Artifact ID.\n\nServiceActionId (string) -- [REQUIRED]The self-service action identifier. For example, act-fs7abcd89wxyz .\n\nProductId (string) -- [REQUIRED]The product identifier. For example, prod-abcdzk7xy33qa .\n\nProvisioningArtifactId (string) -- [REQUIRED]The identifier of the provisioning artifact. For example, pa-4abcdjnxjj6ne .\n\n\n\n\n

    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'FailedServiceActionAssociations': [
        {
            'ServiceActionId': 'string',
            'ProductId': 'string',
            'ProvisioningArtifactId': 'string',
            'ErrorCode': 'DUPLICATE_RESOURCE'|'INTERNAL_FAILURE'|'LIMIT_EXCEEDED'|'RESOURCE_NOT_FOUND'|'THROTTLING',
            'ErrorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --

FailedServiceActionAssociations (list) --
An object that contains a list of errors, along with information to help you identify the self-service action.

(dict) --
An object containing information about the error, along with identifying information about the self-service action and its associations.

ServiceActionId (string) --
The self-service action identifier. For example, act-fs7abcd89wxyz .

ProductId (string) --
The product identifier. For example, prod-abcdzk7xy33qa .

ProvisioningArtifactId (string) --
The identifier of the provisioning artifact. For example, pa-4abcdjnxjj6ne .

ErrorCode (string) --
The error code. Valid values are listed below.

ErrorMessage (string) --
A text description of the error.











Exceptions

ServiceCatalog.Client.exceptions.InvalidParametersException


    :return: {
        'FailedServiceActionAssociations': [
            {
                'ServiceActionId': 'string',
                'ProductId': 'string',
                'ProvisioningArtifactId': 'string',
                'ErrorCode': 'DUPLICATE_RESOURCE'|'INTERNAL_FAILURE'|'LIMIT_EXCEEDED'|'RESOURCE_NOT_FOUND'|'THROTTLING',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    ServiceCatalog.Client.exceptions.InvalidParametersException
    
    """
    pass

def batch_disassociate_service_action_from_provisioning_artifact(ServiceActionAssociations=None, AcceptLanguage=None):
    """
    Disassociates a batch of self-service actions from the specified provisioning artifact.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_disassociate_service_action_from_provisioning_artifact(
        ServiceActionAssociations=[
            {
                'ServiceActionId': 'string',
                'ProductId': 'string',
                'ProvisioningArtifactId': 'string'
            },
        ],
        AcceptLanguage='string'
    )
    
    
    :type ServiceActionAssociations: list
    :param ServiceActionAssociations: [REQUIRED]\nOne or more associations, each consisting of the Action ID, the Product ID, and the Provisioning Artifact ID.\n\n(dict) --A self-service action association consisting of the Action ID, the Product ID, and the Provisioning Artifact ID.\n\nServiceActionId (string) -- [REQUIRED]The self-service action identifier. For example, act-fs7abcd89wxyz .\n\nProductId (string) -- [REQUIRED]The product identifier. For example, prod-abcdzk7xy33qa .\n\nProvisioningArtifactId (string) -- [REQUIRED]The identifier of the provisioning artifact. For example, pa-4abcdjnxjj6ne .\n\n\n\n\n

    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'FailedServiceActionAssociations': [
        {
            'ServiceActionId': 'string',
            'ProductId': 'string',
            'ProvisioningArtifactId': 'string',
            'ErrorCode': 'DUPLICATE_RESOURCE'|'INTERNAL_FAILURE'|'LIMIT_EXCEEDED'|'RESOURCE_NOT_FOUND'|'THROTTLING',
            'ErrorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --

FailedServiceActionAssociations (list) --
An object that contains a list of errors, along with information to help you identify the self-service action.

(dict) --
An object containing information about the error, along with identifying information about the self-service action and its associations.

ServiceActionId (string) --
The self-service action identifier. For example, act-fs7abcd89wxyz .

ProductId (string) --
The product identifier. For example, prod-abcdzk7xy33qa .

ProvisioningArtifactId (string) --
The identifier of the provisioning artifact. For example, pa-4abcdjnxjj6ne .

ErrorCode (string) --
The error code. Valid values are listed below.

ErrorMessage (string) --
A text description of the error.











Exceptions

ServiceCatalog.Client.exceptions.InvalidParametersException


    :return: {
        'FailedServiceActionAssociations': [
            {
                'ServiceActionId': 'string',
                'ProductId': 'string',
                'ProvisioningArtifactId': 'string',
                'ErrorCode': 'DUPLICATE_RESOURCE'|'INTERNAL_FAILURE'|'LIMIT_EXCEEDED'|'RESOURCE_NOT_FOUND'|'THROTTLING',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    ServiceCatalog.Client.exceptions.InvalidParametersException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def copy_product(AcceptLanguage=None, SourceProductArn=None, TargetProductId=None, TargetProductName=None, SourceProvisioningArtifactIdentifiers=None, CopyOptions=None, IdempotencyToken=None):
    """
    Copies the specified source product to the specified target product or a new product.
    You can copy a product to the same account or another account. You can copy a product to the same region or another region.
    This operation is performed asynchronously. To track the progress of the operation, use  DescribeCopyProductStatus .
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type SourceProductArn: string
    :param SourceProductArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the source product.\n

    :type TargetProductId: string
    :param TargetProductId: The identifier of the target product. By default, a new product is created.

    :type TargetProductName: string
    :param TargetProductName: A name for the target product. The default is the name of the source product.

    :type SourceProvisioningArtifactIdentifiers: list
    :param SourceProvisioningArtifactIdentifiers: The identifiers of the provisioning artifacts (also known as versions) of the product to copy. By default, all provisioning artifacts are copied.\n\n(dict) --\n(string) --\n(string) --\n\n\n\n\n\n

    :type CopyOptions: list
    :param CopyOptions: The copy options. If the value is CopyTags , the tags from the source product are copied to the target product.\n\n(string) --\n\n

    :type IdempotencyToken: string
    :param IdempotencyToken: [REQUIRED]\nA unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CopyProductToken': 'string'
}


Response Structure

(dict) --

CopyProductToken (string) --
The token to use to track the progress of the operation.







Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.InvalidParametersException


    :return: {
        'CopyProductToken': 'string'
    }
    
    
    :returns: 
    ServiceCatalog.Client.exceptions.ResourceNotFoundException
    ServiceCatalog.Client.exceptions.InvalidParametersException
    
    """
    pass

def create_constraint(AcceptLanguage=None, PortfolioId=None, ProductId=None, Parameters=None, Type=None, Description=None, IdempotencyToken=None):
    """
    Creates a constraint.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type PortfolioId: string
    :param PortfolioId: [REQUIRED]\nThe portfolio identifier.\n

    :type ProductId: string
    :param ProductId: [REQUIRED]\nThe product identifier.\n

    :type Parameters: string
    :param Parameters: [REQUIRED]\nThe constraint parameters, in JSON format. The syntax depends on the constraint type as follows:\n\nLAUNCH\nYou are required to specify either the RoleArn or the LocalRoleName but can\'t use both.\nSpecify the RoleArn property as follows:\n\n{'RoleArn' : 'arn:aws:iam::123456789012:role/LaunchRole'}\nSpecify the LocalRoleName property as follows:\n\n{'LocalRoleName': 'SCBasicLaunchRole'}\nIf you specify the LocalRoleName property, when an account uses the launch constraint, the IAM role with that name in the account will be used. This allows launch-role constraints to be account-agnostic so the administrator can create fewer resources per shared account.\n\nNote\nThe given role name must exist in the account used to create the launch constraint and the account of the user who launches a product with this launch constraint.\n\nYou cannot have both a LAUNCH and a STACKSET constraint.\nYou also cannot have more than one LAUNCH constraint on a product and portfolio.\n\nNOTIFICATION\nSpecify the NotificationArns property as follows:\n\n{'NotificationArns' : ['arn:aws:sns:us-east-1:123456789012:Topic']}\nRESOURCE_UPDATE\n\nSpecify the TagUpdatesOnProvisionedProduct property as follows:\n\n{'Version':'2.0','Properties':{'TagUpdateOnProvisionedProduct':'String'}}\nThe TagUpdatesOnProvisionedProduct property accepts a string value of ALLOWED or NOT_ALLOWED .\n\nSTACKSET\nSpecify the Parameters property as follows:\n\n{'Version': 'String', 'Properties': {'AccountList': [ 'String' ], 'RegionList': [ 'String' ], 'AdminRole': 'String', 'ExecutionRole': 'String'}}\nYou cannot have both a LAUNCH and a STACKSET constraint.\nYou also cannot have more than one STACKSET constraint on a product and portfolio.\nProducts with a STACKSET constraint will launch an AWS CloudFormation stack set.\n\nTEMPLATE\nSpecify the Rules property. For more information, see Template Constraint Rules .\n

    :type Type: string
    :param Type: [REQUIRED]\nThe type of constraint.\n\nLAUNCH\nNOTIFICATION\nRESOURCE_UPDATE\nSTACKSET\nTEMPLATE\n\n

    :type Description: string
    :param Description: The description of the constraint.

    :type IdempotencyToken: string
    :param IdempotencyToken: [REQUIRED]\nA unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ConstraintDetail': {
        'ConstraintId': 'string',
        'Type': 'string',
        'Description': 'string',
        'Owner': 'string',
        'ProductId': 'string',
        'PortfolioId': 'string'
    },
    'ConstraintParameters': 'string',
    'Status': 'AVAILABLE'|'CREATING'|'FAILED'
}


Response Structure

(dict) --

ConstraintDetail (dict) --
Information about the constraint.

ConstraintId (string) --
The identifier of the constraint.

Type (string) --
The type of constraint.

LAUNCH
NOTIFICATION
STACKSET
TEMPLATE


Description (string) --
The description of the constraint.

Owner (string) --
The owner of the constraint.

ProductId (string) --
The identifier of the product the constraint applies to. Note that a constraint applies to a specific instance of a product within a certain portfolio.

PortfolioId (string) --
The identifier of the portfolio the product resides in. The constraint applies only to the instance of the product that lives within this portfolio.



ConstraintParameters (string) --
The constraint parameters.

Status (string) --
The status of the current request.







Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.InvalidParametersException
ServiceCatalog.Client.exceptions.LimitExceededException
ServiceCatalog.Client.exceptions.DuplicateResourceException


    :return: {
        'ConstraintDetail': {
            'ConstraintId': 'string',
            'Type': 'string',
            'Description': 'string',
            'Owner': 'string',
            'ProductId': 'string',
            'PortfolioId': 'string'
        },
        'ConstraintParameters': 'string',
        'Status': 'AVAILABLE'|'CREATING'|'FAILED'
    }
    
    
    :returns: 
    LAUNCH
    NOTIFICATION
    STACKSET
    TEMPLATE
    
    """
    pass

def create_portfolio(AcceptLanguage=None, DisplayName=None, Description=None, ProviderName=None, Tags=None, IdempotencyToken=None):
    """
    Creates a portfolio.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type DisplayName: string
    :param DisplayName: [REQUIRED]\nThe name to use for display purposes.\n

    :type Description: string
    :param Description: The description of the portfolio.

    :type ProviderName: string
    :param ProviderName: [REQUIRED]\nThe name of the portfolio provider.\n

    :type Tags: list
    :param Tags: One or more tags.\n\n(dict) --Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.\n\nKey (string) -- [REQUIRED]The tag key.\n\nValue (string) -- [REQUIRED]The value for this key.\n\n\n\n\n

    :type IdempotencyToken: string
    :param IdempotencyToken: [REQUIRED]\nA unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

PortfolioDetail (dict) --
Information about the portfolio.

Id (string) --
The portfolio identifier.

ARN (string) --
The ARN assigned to the portfolio.

DisplayName (string) --
The name to use for display purposes.

Description (string) --
The description of the portfolio.

CreatedTime (datetime) --
The UTC time stamp of the creation time.

ProviderName (string) --
The name of the portfolio provider.



Tags (list) --
Information about the tags associated with the portfolio.

(dict) --
Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.

Key (string) --
The tag key.

Value (string) --
The value for this key.











Exceptions

ServiceCatalog.Client.exceptions.InvalidParametersException
ServiceCatalog.Client.exceptions.LimitExceededException
ServiceCatalog.Client.exceptions.TagOptionNotMigratedException


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
    
    
    :returns: 
    ServiceCatalog.Client.exceptions.InvalidParametersException
    ServiceCatalog.Client.exceptions.LimitExceededException
    ServiceCatalog.Client.exceptions.TagOptionNotMigratedException
    
    """
    pass

def create_portfolio_share(AcceptLanguage=None, PortfolioId=None, AccountId=None, OrganizationNode=None):
    """
    Shares the specified portfolio with the specified account or organization node. Shares to an organization node can only be created by the master account of an Organization. AWSOrganizationsAccess must be enabled in order to create a portfolio share to an organization node.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_portfolio_share(
        AcceptLanguage='string',
        PortfolioId='string',
        AccountId='string',
        OrganizationNode={
            'Type': 'ORGANIZATION'|'ORGANIZATIONAL_UNIT'|'ACCOUNT',
            'Value': 'string'
        }
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type PortfolioId: string
    :param PortfolioId: [REQUIRED]\nThe portfolio identifier.\n

    :type AccountId: string
    :param AccountId: The AWS account ID. For example, 123456789012 .

    :type OrganizationNode: dict
    :param OrganizationNode: The organization node to whom you are going to share. If OrganizationNode is passed in, PortfolioShare will be created for the node and its children (when applies), and a PortfolioShareToken will be returned in the output in order for the administrator to monitor the status of the PortfolioShare creation process.\n\nType (string) --The organization node type.\n\nValue (string) --The identifier of the organization node.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'PortfolioShareToken': 'string'
}


Response Structure

(dict) --

PortfolioShareToken (string) --
The portfolio share unique identifier. This will only be returned if portfolio is shared to an organization node.







Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.LimitExceededException
ServiceCatalog.Client.exceptions.InvalidParametersException
ServiceCatalog.Client.exceptions.OperationNotSupportedException
ServiceCatalog.Client.exceptions.InvalidStateException


    :return: {
        'PortfolioShareToken': 'string'
    }
    
    
    :returns: 
    ServiceCatalog.Client.exceptions.ResourceNotFoundException
    ServiceCatalog.Client.exceptions.LimitExceededException
    ServiceCatalog.Client.exceptions.InvalidParametersException
    ServiceCatalog.Client.exceptions.OperationNotSupportedException
    ServiceCatalog.Client.exceptions.InvalidStateException
    
    """
    pass

def create_product(AcceptLanguage=None, Name=None, Owner=None, Description=None, Distributor=None, SupportDescription=None, SupportEmail=None, SupportUrl=None, ProductType=None, Tags=None, ProvisioningArtifactParameters=None, IdempotencyToken=None):
    """
    Creates a product.
    See also: AWS API Documentation
    
    Exceptions
    
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
            'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE_AMI'|'MARKETPLACE_CAR',
            'DisableTemplateValidation': True|False
        },
        IdempotencyToken='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the product.\n

    :type Owner: string
    :param Owner: [REQUIRED]\nThe owner of the product.\n

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
    :param ProductType: [REQUIRED]\nThe type of product.\n

    :type Tags: list
    :param Tags: One or more tags.\n\n(dict) --Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.\n\nKey (string) -- [REQUIRED]The tag key.\n\nValue (string) -- [REQUIRED]The value for this key.\n\n\n\n\n

    :type ProvisioningArtifactParameters: dict
    :param ProvisioningArtifactParameters: [REQUIRED]\nThe configuration of the provisioning artifact.\n\nName (string) --The name of the provisioning artifact (for example, v1 v2beta). No spaces are allowed.\n\nDescription (string) --The description of the provisioning artifact, including how it differs from the previous provisioning artifact.\n\nInfo (dict) -- [REQUIRED]The URL of the CloudFormation template in Amazon S3. Specify the URL in JSON format as follows:\n\n'LoadTemplateFromURL': 'https://s3.amazonaws.com/cf-templates-ozkq9d3hgiq2-us-east-1/...'\n\n(string) --\n(string) --\n\n\n\n\nType (string) --The type of provisioning artifact.\n\nCLOUD_FORMATION_TEMPLATE - AWS CloudFormation template\nMARKETPLACE_AMI - AWS Marketplace AMI\nMARKETPLACE_CAR - AWS Marketplace Clusters and AWS Resources\n\n\nDisableTemplateValidation (boolean) --If set to true, AWS Service Catalog stops validating the specified provisioning artifact even if it is invalid.\n\n\n

    :type IdempotencyToken: string
    :param IdempotencyToken: [REQUIRED]\nA unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
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
        'Active': True|False,
        'Guidance': 'DEFAULT'|'DEPRECATED'
    },
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --

ProductViewDetail (dict) --
Information about the product view.

ProductViewSummary (dict) --
Summary information about the product view.

Id (string) --
The product view identifier.

ProductId (string) --
The product identifier.

Name (string) --
The name of the product.

Owner (string) --
The owner of the product. Contact the product administrator for the significance of this value.

ShortDescription (string) --
Short description of the product.

Type (string) --
The product type. Contact the product administrator for the significance of this value. If this value is MARKETPLACE , the product was created by AWS Marketplace.

Distributor (string) --
The distributor of the product. Contact the product administrator for the significance of this value.

HasDefaultPath (boolean) --
Indicates whether the product has a default path. If the product does not have a default path, call  ListLaunchPaths to disambiguate between paths. Otherwise,  ListLaunchPaths is not required, and the output of  ProductViewSummary can be used directly with  DescribeProvisioningParameters .

SupportEmail (string) --
The email contact information to obtain support for this Product.

SupportDescription (string) --
The description of the support for this Product.

SupportUrl (string) --
The URL information to obtain support for this Product.



Status (string) --
The status of the product.

AVAILABLE - The product is ready for use.
CREATING - Product creation has started; the product is not ready for use.
FAILED - An action failed.


ProductARN (string) --
The ARN of the product.

CreatedTime (datetime) --
The UTC time stamp of the creation time.



ProvisioningArtifactDetail (dict) --
Information about the provisioning artifact.

Id (string) --
The identifier of the provisioning artifact.

Name (string) --
The name of the provisioning artifact.

Description (string) --
The description of the provisioning artifact.

Type (string) --
The type of provisioning artifact.

CLOUD_FORMATION_TEMPLATE - AWS CloudFormation template
MARKETPLACE_AMI - AWS Marketplace AMI
MARKETPLACE_CAR - AWS Marketplace Clusters and AWS Resources


CreatedTime (datetime) --
The UTC time stamp of the creation time.

Active (boolean) --
Indicates whether the product version is active.

Guidance (string) --
Information set by the administrator to provide guidance to end users about which provisioning artifacts to use.



Tags (list) --
Information about the tags associated with the product.

(dict) --
Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.

Key (string) --
The tag key.

Value (string) --
The value for this key.











Exceptions

ServiceCatalog.Client.exceptions.InvalidParametersException
ServiceCatalog.Client.exceptions.LimitExceededException
ServiceCatalog.Client.exceptions.TagOptionNotMigratedException


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
            'Active': True|False,
            'Guidance': 'DEFAULT'|'DEPRECATED'
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
    
    Exceptions
    
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
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type PlanName: string
    :param PlanName: [REQUIRED]\nThe name of the plan.\n

    :type PlanType: string
    :param PlanType: [REQUIRED]\nThe plan type.\n

    :type NotificationArns: list
    :param NotificationArns: Passed to CloudFormation. The SNS topic ARNs to which to publish stack-related events.\n\n(string) --\n\n

    :type PathId: string
    :param PathId: The path identifier of the product. This value is optional if the product has a default path, and required if the product has more than one path. To list the paths for a product, use ListLaunchPaths .

    :type ProductId: string
    :param ProductId: [REQUIRED]\nThe product identifier.\n

    :type ProvisionedProductName: string
    :param ProvisionedProductName: [REQUIRED]\nA user-friendly name for the provisioned product. This value must be unique for the AWS account and cannot be updated after the product is provisioned.\n

    :type ProvisioningArtifactId: string
    :param ProvisioningArtifactId: [REQUIRED]\nThe identifier of the provisioning artifact.\n

    :type ProvisioningParameters: list
    :param ProvisioningParameters: Parameters specified by the administrator that are required for provisioning the product.\n\n(dict) --The parameter key-value pair used to update a provisioned product.\n\nKey (string) --The parameter key.\n\nValue (string) --The parameter value.\n\nUsePreviousValue (boolean) --If set to true, Value is ignored and the previous parameter value is kept.\n\n\n\n\n

    :type IdempotencyToken: string
    :param IdempotencyToken: [REQUIRED]\nA unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.\nThis field is autopopulated if not provided.\n

    :type Tags: list
    :param Tags: One or more tags.\nIf the plan is for an existing provisioned product, the product must have a RESOURCE_UPDATE constraint with TagUpdatesOnProvisionedProduct set to ALLOWED to allow tag updates.\n\n(dict) --Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.\n\nKey (string) -- [REQUIRED]The tag key.\n\nValue (string) -- [REQUIRED]The value for this key.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'PlanName': 'string',
    'PlanId': 'string',
    'ProvisionProductId': 'string',
    'ProvisionedProductName': 'string',
    'ProvisioningArtifactId': 'string'
}


Response Structure

(dict) --

PlanName (string) --
The name of the plan.

PlanId (string) --
The plan identifier.

ProvisionProductId (string) --
The product identifier.

ProvisionedProductName (string) --
The user-friendly name of the provisioned product.

ProvisioningArtifactId (string) --
The identifier of the provisioning artifact.







Exceptions

ServiceCatalog.Client.exceptions.InvalidParametersException
ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.InvalidStateException


    :return: {
        'PlanName': 'string',
        'PlanId': 'string',
        'ProvisionProductId': 'string',
        'ProvisionedProductName': 'string',
        'ProvisioningArtifactId': 'string'
    }
    
    
    :returns: 
    ServiceCatalog.Client.exceptions.InvalidParametersException
    ServiceCatalog.Client.exceptions.ResourceNotFoundException
    ServiceCatalog.Client.exceptions.InvalidStateException
    
    """
    pass

def create_provisioning_artifact(AcceptLanguage=None, ProductId=None, Parameters=None, IdempotencyToken=None):
    """
    Creates a provisioning artifact (also known as a version) for the specified product.
    You cannot create a provisioning artifact for a product that was shared with you.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_provisioning_artifact(
        AcceptLanguage='string',
        ProductId='string',
        Parameters={
            'Name': 'string',
            'Description': 'string',
            'Info': {
                'string': 'string'
            },
            'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE_AMI'|'MARKETPLACE_CAR',
            'DisableTemplateValidation': True|False
        },
        IdempotencyToken='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type ProductId: string
    :param ProductId: [REQUIRED]\nThe product identifier.\n

    :type Parameters: dict
    :param Parameters: [REQUIRED]\nThe configuration for the provisioning artifact.\n\nName (string) --The name of the provisioning artifact (for example, v1 v2beta). No spaces are allowed.\n\nDescription (string) --The description of the provisioning artifact, including how it differs from the previous provisioning artifact.\n\nInfo (dict) -- [REQUIRED]The URL of the CloudFormation template in Amazon S3. Specify the URL in JSON format as follows:\n\n'LoadTemplateFromURL': 'https://s3.amazonaws.com/cf-templates-ozkq9d3hgiq2-us-east-1/...'\n\n(string) --\n(string) --\n\n\n\n\nType (string) --The type of provisioning artifact.\n\nCLOUD_FORMATION_TEMPLATE - AWS CloudFormation template\nMARKETPLACE_AMI - AWS Marketplace AMI\nMARKETPLACE_CAR - AWS Marketplace Clusters and AWS Resources\n\n\nDisableTemplateValidation (boolean) --If set to true, AWS Service Catalog stops validating the specified provisioning artifact even if it is invalid.\n\n\n

    :type IdempotencyToken: string
    :param IdempotencyToken: [REQUIRED]\nA unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ProvisioningArtifactDetail': {
        'Id': 'string',
        'Name': 'string',
        'Description': 'string',
        'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE_AMI'|'MARKETPLACE_CAR',
        'CreatedTime': datetime(2015, 1, 1),
        'Active': True|False,
        'Guidance': 'DEFAULT'|'DEPRECATED'
    },
    'Info': {
        'string': 'string'
    },
    'Status': 'AVAILABLE'|'CREATING'|'FAILED'
}


Response Structure

(dict) --

ProvisioningArtifactDetail (dict) --
Information about the provisioning artifact.

Id (string) --
The identifier of the provisioning artifact.

Name (string) --
The name of the provisioning artifact.

Description (string) --
The description of the provisioning artifact.

Type (string) --
The type of provisioning artifact.

CLOUD_FORMATION_TEMPLATE - AWS CloudFormation template
MARKETPLACE_AMI - AWS Marketplace AMI
MARKETPLACE_CAR - AWS Marketplace Clusters and AWS Resources


CreatedTime (datetime) --
The UTC time stamp of the creation time.

Active (boolean) --
Indicates whether the product version is active.

Guidance (string) --
Information set by the administrator to provide guidance to end users about which provisioning artifacts to use.



Info (dict) --
The URL of the CloudFormation template in Amazon S3, in JSON format.

(string) --
(string) --




Status (string) --
The status of the current request.







Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.InvalidParametersException
ServiceCatalog.Client.exceptions.LimitExceededException


    :return: {
        'ProvisioningArtifactDetail': {
            'Id': 'string',
            'Name': 'string',
            'Description': 'string',
            'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE_AMI'|'MARKETPLACE_CAR',
            'CreatedTime': datetime(2015, 1, 1),
            'Active': True|False,
            'Guidance': 'DEFAULT'|'DEPRECATED'
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

def create_service_action(Name=None, DefinitionType=None, Definition=None, Description=None, AcceptLanguage=None, IdempotencyToken=None):
    """
    Creates a self-service action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_service_action(
        Name='string',
        DefinitionType='SSM_AUTOMATION',
        Definition={
            'string': 'string'
        },
        Description='string',
        AcceptLanguage='string',
        IdempotencyToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe self-service action name.\n

    :type DefinitionType: string
    :param DefinitionType: [REQUIRED]\nThe service action definition type. For example, SSM_AUTOMATION .\n

    :type Definition: dict
    :param Definition: [REQUIRED]\nThe self-service action definition. Can be one of the following:\n\nName\nThe name of the AWS Systems Manager Document. For example, AWS-RestartEC2Instance .\n\nVersion\nThe AWS Systems Manager automation document version. For example, 'Version': '1'\n\nAssumeRole\nThe Amazon Resource Name (ARN) of the role that performs the self-service actions on your behalf. For example, 'AssumeRole': 'arn:aws:iam::12345678910:role/ActionRole' .\nTo reuse the provisioned product launch role, set to 'AssumeRole': 'LAUNCH_ROLE' .\n\nParameters\nThe list of parameters in JSON format.\nFor example: [{\\'Name\\':\\'InstanceId\\',\\'Type\\':\\'TARGET\\'}] or [{\\'Name\\':\\'InstanceId\\',\\'Type\\':\\'TEXT_VALUE\\'}] .\n\n(string) --\n(string) --\n\n\n\n

    :type Description: string
    :param Description: The self-service action description.

    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type IdempotencyToken: string
    :param IdempotencyToken: [REQUIRED]\nA unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ServiceActionDetail': {
        'ServiceActionSummary': {
            'Id': 'string',
            'Name': 'string',
            'Description': 'string',
            'DefinitionType': 'SSM_AUTOMATION'
        },
        'Definition': {
            'string': 'string'
        }
    }
}


Response Structure

(dict) --

ServiceActionDetail (dict) --
An object containing information about the self-service action.

ServiceActionSummary (dict) --
Summary information about the self-service action.

Id (string) --
The self-service action identifier.

Name (string) --
The self-service action name.

Description (string) --
The self-service action description.

DefinitionType (string) --
The self-service action definition type. For example, SSM_AUTOMATION .



Definition (dict) --
A map that defines the self-service action.

(string) --
(string) --












Exceptions

ServiceCatalog.Client.exceptions.InvalidParametersException
ServiceCatalog.Client.exceptions.LimitExceededException


    :return: {
        'ServiceActionDetail': {
            'ServiceActionSummary': {
                'Id': 'string',
                'Name': 'string',
                'Description': 'string',
                'DefinitionType': 'SSM_AUTOMATION'
            },
            'Definition': {
                'string': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def create_tag_option(Key=None, Value=None):
    """
    Creates a TagOption.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_tag_option(
        Key='string',
        Value='string'
    )
    
    
    :type Key: string
    :param Key: [REQUIRED]\nThe TagOption key.\n

    :type Value: string
    :param Value: [REQUIRED]\nThe TagOption value.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TagOptionDetail': {
        'Key': 'string',
        'Value': 'string',
        'Active': True|False,
        'Id': 'string'
    }
}


Response Structure

(dict) --

TagOptionDetail (dict) --
Information about the TagOption.

Key (string) --
The TagOption key.

Value (string) --
The TagOption value.

Active (boolean) --
The TagOption active state.

Id (string) --
The TagOption identifier.









Exceptions

ServiceCatalog.Client.exceptions.TagOptionNotMigratedException
ServiceCatalog.Client.exceptions.DuplicateResourceException
ServiceCatalog.Client.exceptions.LimitExceededException


    :return: {
        'TagOptionDetail': {
            'Key': 'string',
            'Value': 'string',
            'Active': True|False,
            'Id': 'string'
        }
    }
    
    
    :returns: 
    ServiceCatalog.Client.exceptions.TagOptionNotMigratedException
    ServiceCatalog.Client.exceptions.DuplicateResourceException
    ServiceCatalog.Client.exceptions.LimitExceededException
    
    """
    pass

def delete_constraint(AcceptLanguage=None, Id=None):
    """
    Deletes the specified constraint.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_constraint(
        AcceptLanguage='string',
        Id='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type Id: string
    :param Id: [REQUIRED]\nThe identifier of the constraint.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.InvalidParametersException


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
    
    Exceptions
    
    :example: response = client.delete_portfolio(
        AcceptLanguage='string',
        Id='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type Id: string
    :param Id: [REQUIRED]\nThe portfolio identifier.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.InvalidParametersException
ServiceCatalog.Client.exceptions.ResourceInUseException
ServiceCatalog.Client.exceptions.TagOptionNotMigratedException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_portfolio_share(AcceptLanguage=None, PortfolioId=None, AccountId=None, OrganizationNode=None):
    """
    Stops sharing the specified portfolio with the specified account or organization node. Shares to an organization node can only be deleted by the master account of an Organization.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_portfolio_share(
        AcceptLanguage='string',
        PortfolioId='string',
        AccountId='string',
        OrganizationNode={
            'Type': 'ORGANIZATION'|'ORGANIZATIONAL_UNIT'|'ACCOUNT',
            'Value': 'string'
        }
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type PortfolioId: string
    :param PortfolioId: [REQUIRED]\nThe portfolio identifier.\n

    :type AccountId: string
    :param AccountId: The AWS account ID.

    :type OrganizationNode: dict
    :param OrganizationNode: The organization node to whom you are going to stop sharing.\n\nType (string) --The organization node type.\n\nValue (string) --The identifier of the organization node.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'PortfolioShareToken': 'string'
}


Response Structure

(dict) --

PortfolioShareToken (string) --
The portfolio share unique identifier. This will only be returned if delete is made to an organization node.







Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.InvalidParametersException
ServiceCatalog.Client.exceptions.OperationNotSupportedException
ServiceCatalog.Client.exceptions.InvalidStateException


    :return: {
        'PortfolioShareToken': 'string'
    }
    
    
    :returns: 
    ServiceCatalog.Client.exceptions.ResourceNotFoundException
    ServiceCatalog.Client.exceptions.InvalidParametersException
    ServiceCatalog.Client.exceptions.OperationNotSupportedException
    ServiceCatalog.Client.exceptions.InvalidStateException
    
    """
    pass

def delete_product(AcceptLanguage=None, Id=None):
    """
    Deletes the specified product.
    You cannot delete a product if it was shared with you or is associated with a portfolio.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_product(
        AcceptLanguage='string',
        Id='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type Id: string
    :param Id: [REQUIRED]\nThe product identifier.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.ResourceInUseException
ServiceCatalog.Client.exceptions.InvalidParametersException
ServiceCatalog.Client.exceptions.TagOptionNotMigratedException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_provisioned_product_plan(AcceptLanguage=None, PlanId=None, IgnoreErrors=None):
    """
    Deletes the specified plan.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_provisioned_product_plan(
        AcceptLanguage='string',
        PlanId='string',
        IgnoreErrors=True|False
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type PlanId: string
    :param PlanId: [REQUIRED]\nThe plan identifier.\n

    :type IgnoreErrors: boolean
    :param IgnoreErrors: If set to true, AWS Service Catalog stops managing the specified provisioned product even if it cannot delete the underlying resources.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ServiceCatalog.Client.exceptions.InvalidParametersException
ServiceCatalog.Client.exceptions.ResourceNotFoundException


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
    
    Exceptions
    
    :example: response = client.delete_provisioning_artifact(
        AcceptLanguage='string',
        ProductId='string',
        ProvisioningArtifactId='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type ProductId: string
    :param ProductId: [REQUIRED]\nThe product identifier.\n

    :type ProvisioningArtifactId: string
    :param ProvisioningArtifactId: [REQUIRED]\nThe identifier of the provisioning artifact.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.ResourceInUseException
ServiceCatalog.Client.exceptions.InvalidParametersException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_service_action(Id=None, AcceptLanguage=None):
    """
    Deletes a self-service action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_service_action(
        Id='string',
        AcceptLanguage='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe self-service action identifier. For example, act-fs7abcd89wxyz .\n

    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.ResourceInUseException


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
    
    Exceptions
    
    :example: response = client.delete_tag_option(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe TagOption identifier.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

ServiceCatalog.Client.exceptions.TagOptionNotMigratedException
ServiceCatalog.Client.exceptions.ResourceInUseException
ServiceCatalog.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    ServiceCatalog.Client.exceptions.TagOptionNotMigratedException
    ServiceCatalog.Client.exceptions.ResourceInUseException
    ServiceCatalog.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def describe_constraint(AcceptLanguage=None, Id=None):
    """
    Gets information about the specified constraint.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_constraint(
        AcceptLanguage='string',
        Id='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type Id: string
    :param Id: [REQUIRED]\nThe identifier of the constraint.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ConstraintDetail': {
        'ConstraintId': 'string',
        'Type': 'string',
        'Description': 'string',
        'Owner': 'string',
        'ProductId': 'string',
        'PortfolioId': 'string'
    },
    'ConstraintParameters': 'string',
    'Status': 'AVAILABLE'|'CREATING'|'FAILED'
}


Response Structure

(dict) --

ConstraintDetail (dict) --
Information about the constraint.

ConstraintId (string) --
The identifier of the constraint.

Type (string) --
The type of constraint.

LAUNCH
NOTIFICATION
STACKSET
TEMPLATE


Description (string) --
The description of the constraint.

Owner (string) --
The owner of the constraint.

ProductId (string) --
The identifier of the product the constraint applies to. Note that a constraint applies to a specific instance of a product within a certain portfolio.

PortfolioId (string) --
The identifier of the portfolio the product resides in. The constraint applies only to the instance of the product that lives within this portfolio.



ConstraintParameters (string) --
The constraint parameters.

Status (string) --
The status of the current request.







Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException


    :return: {
        'ConstraintDetail': {
            'ConstraintId': 'string',
            'Type': 'string',
            'Description': 'string',
            'Owner': 'string',
            'ProductId': 'string',
            'PortfolioId': 'string'
        },
        'ConstraintParameters': 'string',
        'Status': 'AVAILABLE'|'CREATING'|'FAILED'
    }
    
    
    :returns: 
    LAUNCH
    NOTIFICATION
    STACKSET
    TEMPLATE
    
    """
    pass

def describe_copy_product_status(AcceptLanguage=None, CopyProductToken=None):
    """
    Gets the status of the specified copy product operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_copy_product_status(
        AcceptLanguage='string',
        CopyProductToken='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type CopyProductToken: string
    :param CopyProductToken: [REQUIRED]\nThe token for the copy product operation. This token is returned by CopyProduct .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CopyProductStatus': 'SUCCEEDED'|'IN_PROGRESS'|'FAILED',
    'TargetProductId': 'string',
    'StatusDetail': 'string'
}


Response Structure

(dict) --

CopyProductStatus (string) --
The status of the copy product operation.

TargetProductId (string) --
The identifier of the copied product.

StatusDetail (string) --
The status message.







Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException


    :return: {
        'CopyProductStatus': 'SUCCEEDED'|'IN_PROGRESS'|'FAILED',
        'TargetProductId': 'string',
        'StatusDetail': 'string'
    }
    
    
    :returns: 
    ServiceCatalog.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def describe_portfolio(AcceptLanguage=None, Id=None):
    """
    Gets information about the specified portfolio.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_portfolio(
        AcceptLanguage='string',
        Id='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type Id: string
    :param Id: [REQUIRED]\nThe portfolio identifier.\n

    :rtype: dict

ReturnsResponse Syntax
{
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
    ],
    'Budgets': [
        {
            'BudgetName': 'string'
        },
    ]
}


Response Structure

(dict) --

PortfolioDetail (dict) --
Information about the portfolio.

Id (string) --
The portfolio identifier.

ARN (string) --
The ARN assigned to the portfolio.

DisplayName (string) --
The name to use for display purposes.

Description (string) --
The description of the portfolio.

CreatedTime (datetime) --
The UTC time stamp of the creation time.

ProviderName (string) --
The name of the portfolio provider.



Tags (list) --
Information about the tags associated with the portfolio.

(dict) --
Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.

Key (string) --
The tag key.

Value (string) --
The value for this key.





TagOptions (list) --
Information about the TagOptions associated with the portfolio.

(dict) --
Information about a TagOption.

Key (string) --
The TagOption key.

Value (string) --
The TagOption value.

Active (boolean) --
The TagOption active state.

Id (string) --
The TagOption identifier.





Budgets (list) --
Information about the associated budgets.

(dict) --
Information about a budget.

BudgetName (string) --
Name of the associated budget.











Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException


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
        ],
        'Budgets': [
            {
                'BudgetName': 'string'
            },
        ]
    }
    
    
    :returns: 
    ServiceCatalog.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def describe_portfolio_share_status(PortfolioShareToken=None):
    """
    Gets the status of the specified portfolio share operation. This API can only be called by the master account in the organization.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_portfolio_share_status(
        PortfolioShareToken='string'
    )
    
    
    :type PortfolioShareToken: string
    :param PortfolioShareToken: [REQUIRED]\nThe token for the portfolio share operation. This token is returned either by CreatePortfolioShare or by DeletePortfolioShare.\n

    :rtype: dict
ReturnsResponse Syntax{
    'PortfolioShareToken': 'string',
    'PortfolioId': 'string',
    'OrganizationNodeValue': 'string',
    'Status': 'NOT_STARTED'|'IN_PROGRESS'|'COMPLETED'|'COMPLETED_WITH_ERRORS'|'ERROR',
    'ShareDetails': {
        'SuccessfulShares': [
            'string',
        ],
        'ShareErrors': [
            {
                'Accounts': [
                    'string',
                ],
                'Message': 'string',
                'Error': 'string'
            },
        ]
    }
}


Response Structure

(dict) --
PortfolioShareToken (string) --The token for the portfolio share operation. For example, share-6v24abcdefghi .

PortfolioId (string) --The portfolio identifier.

OrganizationNodeValue (string) --Organization node identifier. It can be either account id, organizational unit id or organization id.

Status (string) --Status of the portfolio share operation.

ShareDetails (dict) --Information about the portfolio share operation.

SuccessfulShares (list) --List of accounts for whom the operation succeeded.

(string) --


ShareErrors (list) --List of errors.

(dict) --Errors that occurred during the portfolio share operation.

Accounts (list) --List of accounts impacted by the error.

(string) --


Message (string) --Information about the error.

Error (string) --Error type that happened when processing the operation.












Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.InvalidParametersException
ServiceCatalog.Client.exceptions.OperationNotSupportedException


    :return: {
        'PortfolioShareToken': 'string',
        'PortfolioId': 'string',
        'OrganizationNodeValue': 'string',
        'Status': 'NOT_STARTED'|'IN_PROGRESS'|'COMPLETED'|'COMPLETED_WITH_ERRORS'|'ERROR',
        'ShareDetails': {
            'SuccessfulShares': [
                'string',
            ],
            'ShareErrors': [
                {
                    'Accounts': [
                        'string',
                    ],
                    'Message': 'string',
                    'Error': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_product(AcceptLanguage=None, Id=None):
    """
    Gets information about the specified product.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_product(
        AcceptLanguage='string',
        Id='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type Id: string
    :param Id: [REQUIRED]\nThe product identifier.\n

    :rtype: dict

ReturnsResponse Syntax
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
    'ProvisioningArtifacts': [
        {
            'Id': 'string',
            'Name': 'string',
            'Description': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'Guidance': 'DEFAULT'|'DEPRECATED'
        },
    ],
    'Budgets': [
        {
            'BudgetName': 'string'
        },
    ]
}


Response Structure

(dict) --

ProductViewSummary (dict) --
Summary information about the product view.

Id (string) --
The product view identifier.

ProductId (string) --
The product identifier.

Name (string) --
The name of the product.

Owner (string) --
The owner of the product. Contact the product administrator for the significance of this value.

ShortDescription (string) --
Short description of the product.

Type (string) --
The product type. Contact the product administrator for the significance of this value. If this value is MARKETPLACE , the product was created by AWS Marketplace.

Distributor (string) --
The distributor of the product. Contact the product administrator for the significance of this value.

HasDefaultPath (boolean) --
Indicates whether the product has a default path. If the product does not have a default path, call  ListLaunchPaths to disambiguate between paths. Otherwise,  ListLaunchPaths is not required, and the output of  ProductViewSummary can be used directly with  DescribeProvisioningParameters .

SupportEmail (string) --
The email contact information to obtain support for this Product.

SupportDescription (string) --
The description of the support for this Product.

SupportUrl (string) --
The URL information to obtain support for this Product.



ProvisioningArtifacts (list) --
Information about the provisioning artifacts for the specified product.

(dict) --
Information about a provisioning artifact. A provisioning artifact is also known as a product version.

Id (string) --
The identifier of the provisioning artifact.

Name (string) --
The name of the provisioning artifact.

Description (string) --
The description of the provisioning artifact.

CreatedTime (datetime) --
The UTC time stamp of the creation time.

Guidance (string) --
Information set by the administrator to provide guidance to end users about which provisioning artifacts to use.





Budgets (list) --
Information about the associated budgets.

(dict) --
Information about a budget.

BudgetName (string) --
Name of the associated budget.











Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.InvalidParametersException


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
                'CreatedTime': datetime(2015, 1, 1),
                'Guidance': 'DEFAULT'|'DEPRECATED'
            },
        ],
        'Budgets': [
            {
                'BudgetName': 'string'
            },
        ]
    }
    
    
    :returns: 
    ServiceCatalog.Client.exceptions.ResourceNotFoundException
    ServiceCatalog.Client.exceptions.InvalidParametersException
    
    """
    pass

def describe_product_as_admin(AcceptLanguage=None, Id=None):
    """
    Gets information about the specified product. This operation is run with administrator access.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_product_as_admin(
        AcceptLanguage='string',
        Id='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type Id: string
    :param Id: [REQUIRED]\nThe product identifier.\n

    :rtype: dict

ReturnsResponse Syntax
{
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
    ],
    'Budgets': [
        {
            'BudgetName': 'string'
        },
    ]
}


Response Structure

(dict) --

ProductViewDetail (dict) --
Information about the product view.

ProductViewSummary (dict) --
Summary information about the product view.

Id (string) --
The product view identifier.

ProductId (string) --
The product identifier.

Name (string) --
The name of the product.

Owner (string) --
The owner of the product. Contact the product administrator for the significance of this value.

ShortDescription (string) --
Short description of the product.

Type (string) --
The product type. Contact the product administrator for the significance of this value. If this value is MARKETPLACE , the product was created by AWS Marketplace.

Distributor (string) --
The distributor of the product. Contact the product administrator for the significance of this value.

HasDefaultPath (boolean) --
Indicates whether the product has a default path. If the product does not have a default path, call  ListLaunchPaths to disambiguate between paths. Otherwise,  ListLaunchPaths is not required, and the output of  ProductViewSummary can be used directly with  DescribeProvisioningParameters .

SupportEmail (string) --
The email contact information to obtain support for this Product.

SupportDescription (string) --
The description of the support for this Product.

SupportUrl (string) --
The URL information to obtain support for this Product.



Status (string) --
The status of the product.

AVAILABLE - The product is ready for use.
CREATING - Product creation has started; the product is not ready for use.
FAILED - An action failed.


ProductARN (string) --
The ARN of the product.

CreatedTime (datetime) --
The UTC time stamp of the creation time.



ProvisioningArtifactSummaries (list) --
Information about the provisioning artifacts (also known as versions) for the specified product.

(dict) --
Summary information about a provisioning artifact (also known as a version) for a product.

Id (string) --
The identifier of the provisioning artifact.

Name (string) --
The name of the provisioning artifact.

Description (string) --
The description of the provisioning artifact.

CreatedTime (datetime) --
The UTC time stamp of the creation time.

ProvisioningArtifactMetadata (dict) --
The metadata for the provisioning artifact. This is used with AWS Marketplace products.

(string) --
(string) --








Tags (list) --
Information about the tags associated with the product.

(dict) --
Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.

Key (string) --
The tag key.

Value (string) --
The value for this key.





TagOptions (list) --
Information about the TagOptions associated with the product.

(dict) --
Information about a TagOption.

Key (string) --
The TagOption key.

Value (string) --
The TagOption value.

Active (boolean) --
The TagOption active state.

Id (string) --
The TagOption identifier.





Budgets (list) --
Information about the associated budgets.

(dict) --
Information about a budget.

BudgetName (string) --
Name of the associated budget.











Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException


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
        ],
        'Budgets': [
            {
                'BudgetName': 'string'
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
    
    Exceptions
    
    :example: response = client.describe_product_view(
        AcceptLanguage='string',
        Id='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type Id: string
    :param Id: [REQUIRED]\nThe product view identifier.\n

    :rtype: dict

ReturnsResponse Syntax
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
    'ProvisioningArtifacts': [
        {
            'Id': 'string',
            'Name': 'string',
            'Description': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'Guidance': 'DEFAULT'|'DEPRECATED'
        },
    ]
}


Response Structure

(dict) --

ProductViewSummary (dict) --
Summary information about the product.

Id (string) --
The product view identifier.

ProductId (string) --
The product identifier.

Name (string) --
The name of the product.

Owner (string) --
The owner of the product. Contact the product administrator for the significance of this value.

ShortDescription (string) --
Short description of the product.

Type (string) --
The product type. Contact the product administrator for the significance of this value. If this value is MARKETPLACE , the product was created by AWS Marketplace.

Distributor (string) --
The distributor of the product. Contact the product administrator for the significance of this value.

HasDefaultPath (boolean) --
Indicates whether the product has a default path. If the product does not have a default path, call  ListLaunchPaths to disambiguate between paths. Otherwise,  ListLaunchPaths is not required, and the output of  ProductViewSummary can be used directly with  DescribeProvisioningParameters .

SupportEmail (string) --
The email contact information to obtain support for this Product.

SupportDescription (string) --
The description of the support for this Product.

SupportUrl (string) --
The URL information to obtain support for this Product.



ProvisioningArtifacts (list) --
Information about the provisioning artifacts for the product.

(dict) --
Information about a provisioning artifact. A provisioning artifact is also known as a product version.

Id (string) --
The identifier of the provisioning artifact.

Name (string) --
The name of the provisioning artifact.

Description (string) --
The description of the provisioning artifact.

CreatedTime (datetime) --
The UTC time stamp of the creation time.

Guidance (string) --
Information set by the administrator to provide guidance to end users about which provisioning artifacts to use.











Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.InvalidParametersException


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
                'CreatedTime': datetime(2015, 1, 1),
                'Guidance': 'DEFAULT'|'DEPRECATED'
            },
        ]
    }
    
    
    :returns: 
    ServiceCatalog.Client.exceptions.ResourceNotFoundException
    ServiceCatalog.Client.exceptions.InvalidParametersException
    
    """
    pass

def describe_provisioned_product(AcceptLanguage=None, Id=None):
    """
    Gets information about the specified provisioned product.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_provisioned_product(
        AcceptLanguage='string',
        Id='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type Id: string
    :param Id: [REQUIRED]\nThe provisioned product identifier.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ProvisionedProductDetail': {
        'Name': 'string',
        'Arn': 'string',
        'Type': 'string',
        'Id': 'string',
        'Status': 'AVAILABLE'|'UNDER_CHANGE'|'TAINTED'|'ERROR'|'PLAN_IN_PROGRESS',
        'StatusMessage': 'string',
        'CreatedTime': datetime(2015, 1, 1),
        'IdempotencyToken': 'string',
        'LastRecordId': 'string',
        'ProductId': 'string',
        'ProvisioningArtifactId': 'string'
    },
    'CloudWatchDashboards': [
        {
            'Name': 'string'
        },
    ]
}


Response Structure

(dict) --

ProvisionedProductDetail (dict) --
Information about the provisioned product.

Name (string) --
The user-friendly name of the provisioned product.

Arn (string) --
The ARN of the provisioned product.

Type (string) --
The type of provisioned product. The supported values are CFN_STACK and CFN_STACKSET .

Id (string) --
The identifier of the provisioned product.

Status (string) --
The current status of the provisioned product.

AVAILABLE - Stable state, ready to perform any operation. The most recent operation succeeded and completed.
UNDER_CHANGE - Transitive state. Operations performed might not have valid results. Wait for an AVAILABLE status before performing operations.
TAINTED - Stable state, ready to perform any operation. The stack has completed the requested operation but is not exactly what was requested. For example, a request to update to a new version failed and the stack rolled back to the current version.
ERROR - An unexpected error occurred. The provisioned product exists but the stack is not running. For example, CloudFormation received a parameter value that was not valid and could not launch the stack.
PLAN_IN_PROGRESS - Transitive state. The plan operations were performed to provision a new product, but resources have not yet been created. After reviewing the list of resources to be created, execute the plan. Wait for an AVAILABLE status before performing operations.


StatusMessage (string) --
The current status message of the provisioned product.

CreatedTime (datetime) --
The UTC time stamp of the creation time.

IdempotencyToken (string) --
A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.

LastRecordId (string) --
The record identifier of the last request performed on this provisioned product.

ProductId (string) --
The product identifier. For example, prod-abcdzk7xy33qa .

ProvisioningArtifactId (string) --
The identifier of the provisioning artifact. For example, pa-4abcdjnxjj6ne .



CloudWatchDashboards (list) --
Any CloudWatch dashboards that were created when provisioning the product.

(dict) --
Information about a CloudWatch dashboard.

Name (string) --
The name of the CloudWatch dashboard.











Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException


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
            'LastRecordId': 'string',
            'ProductId': 'string',
            'ProvisioningArtifactId': 'string'
        },
        'CloudWatchDashboards': [
            {
                'Name': 'string'
            },
        ]
    }
    
    
    :returns: 
    AVAILABLE - Stable state, ready to perform any operation. The most recent operation succeeded and completed.
    UNDER_CHANGE - Transitive state. Operations performed might not have valid results. Wait for an AVAILABLE status before performing operations.
    TAINTED - Stable state, ready to perform any operation. The stack has completed the requested operation but is not exactly what was requested. For example, a request to update to a new version failed and the stack rolled back to the current version.
    ERROR - An unexpected error occurred. The provisioned product exists but the stack is not running. For example, CloudFormation received a parameter value that was not valid and could not launch the stack.
    PLAN_IN_PROGRESS - Transitive state. The plan operations were performed to provision a new product, but resources have not yet been created. After reviewing the list of resources to be created, execute the plan. Wait for an AVAILABLE status before performing operations.
    
    """
    pass

def describe_provisioned_product_plan(AcceptLanguage=None, PlanId=None, PageSize=None, PageToken=None):
    """
    Gets information about the resource changes for the specified plan.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_provisioned_product_plan(
        AcceptLanguage='string',
        PlanId='string',
        PageSize=123,
        PageToken='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type PlanId: string
    :param PlanId: [REQUIRED]\nThe plan identifier.\n

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

ProvisionedProductPlanDetails (dict) --
Information about the plan.

CreatedTime (datetime) --
The UTC time stamp of the creation time.

PathId (string) --
The path identifier of the product. This value is optional if the product has a default path, and required if the product has more than one path. To list the paths for a product, use  ListLaunchPaths .

ProductId (string) --
The product identifier.

PlanName (string) --
The name of the plan.

PlanId (string) --
The plan identifier.

ProvisionProductId (string) --
The product identifier.

ProvisionProductName (string) --
The user-friendly name of the provisioned product.

PlanType (string) --
The plan type.

ProvisioningArtifactId (string) --
The identifier of the provisioning artifact.

Status (string) --
The status.

UpdatedTime (datetime) --
The time when the plan was last updated.

NotificationArns (list) --
Passed to CloudFormation. The SNS topic ARNs to which to publish stack-related events.

(string) --


ProvisioningParameters (list) --
Parameters specified by the administrator that are required for provisioning the product.

(dict) --
The parameter key-value pair used to update a provisioned product.

Key (string) --
The parameter key.

Value (string) --
The parameter value.

UsePreviousValue (boolean) --
If set to true, Value is ignored and the previous parameter value is kept.





Tags (list) --
One or more tags.

(dict) --
Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.

Key (string) --
The tag key.

Value (string) --
The value for this key.





StatusMessage (string) --
The status message.



ResourceChanges (list) --
Information about the resource changes that will occur when the plan is executed.

(dict) --
Information about a resource change that will occur when a plan is executed.

Action (string) --
The change action.

LogicalResourceId (string) --
The ID of the resource, as defined in the CloudFormation template.

PhysicalResourceId (string) --
The ID of the resource, if it was already created.

ResourceType (string) --
The type of resource.

Replacement (string) --
If the change type is Modify , indicates whether the existing resource is deleted and replaced with a new one.

Scope (list) --
The change scope.

(string) --


Details (list) --
Information about the resource changes.

(dict) --
Information about a change to a resource attribute.

Target (dict) --
Information about the resource attribute to be modified.

Attribute (string) --
The attribute to be changed.

Name (string) --
If the attribute is Properties , the value is the name of the property. Otherwise, the value is null.

RequiresRecreation (string) --
If the attribute is Properties , indicates whether a change to this property causes the resource to be re-created.



Evaluation (string) --
For static evaluations, the value of the resource attribute will change and the new value is known. For dynamic evaluations, the value might change, and any new value will be determined when the plan is updated.

CausingEntity (string) --
The ID of the entity that caused the change.









NextPageToken (string) --
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.







Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.InvalidParametersException


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
    
    Exceptions
    
    :example: response = client.describe_provisioning_artifact(
        AcceptLanguage='string',
        ProvisioningArtifactId='string',
        ProductId='string',
        Verbose=True|False
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type ProvisioningArtifactId: string
    :param ProvisioningArtifactId: [REQUIRED]\nThe identifier of the provisioning artifact.\n

    :type ProductId: string
    :param ProductId: [REQUIRED]\nThe product identifier.\n

    :type Verbose: boolean
    :param Verbose: Indicates whether a verbose level of detail is enabled.

    :rtype: dict

ReturnsResponse Syntax
{
    'ProvisioningArtifactDetail': {
        'Id': 'string',
        'Name': 'string',
        'Description': 'string',
        'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE_AMI'|'MARKETPLACE_CAR',
        'CreatedTime': datetime(2015, 1, 1),
        'Active': True|False,
        'Guidance': 'DEFAULT'|'DEPRECATED'
    },
    'Info': {
        'string': 'string'
    },
    'Status': 'AVAILABLE'|'CREATING'|'FAILED'
}


Response Structure

(dict) --

ProvisioningArtifactDetail (dict) --
Information about the provisioning artifact.

Id (string) --
The identifier of the provisioning artifact.

Name (string) --
The name of the provisioning artifact.

Description (string) --
The description of the provisioning artifact.

Type (string) --
The type of provisioning artifact.

CLOUD_FORMATION_TEMPLATE - AWS CloudFormation template
MARKETPLACE_AMI - AWS Marketplace AMI
MARKETPLACE_CAR - AWS Marketplace Clusters and AWS Resources


CreatedTime (datetime) --
The UTC time stamp of the creation time.

Active (boolean) --
Indicates whether the product version is active.

Guidance (string) --
Information set by the administrator to provide guidance to end users about which provisioning artifacts to use.



Info (dict) --
The URL of the CloudFormation template in Amazon S3.

(string) --
(string) --




Status (string) --
The status of the current request.







Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException


    :return: {
        'ProvisioningArtifactDetail': {
            'Id': 'string',
            'Name': 'string',
            'Description': 'string',
            'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE_AMI'|'MARKETPLACE_CAR',
            'CreatedTime': datetime(2015, 1, 1),
            'Active': True|False,
            'Guidance': 'DEFAULT'|'DEPRECATED'
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
    
    Exceptions
    
    :example: response = client.describe_provisioning_parameters(
        AcceptLanguage='string',
        ProductId='string',
        ProvisioningArtifactId='string',
        PathId='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type ProductId: string
    :param ProductId: [REQUIRED]\nThe product identifier.\n

    :type ProvisioningArtifactId: string
    :param ProvisioningArtifactId: [REQUIRED]\nThe identifier of the provisioning artifact.\n

    :type PathId: string
    :param PathId: The path identifier of the product. This value is optional if the product has a default path, and required if the product has more than one path. To list the paths for a product, use ListLaunchPaths .

    :rtype: dict

ReturnsResponse Syntax
{
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
    ],
    'ProvisioningArtifactPreferences': {
        'StackSetAccounts': [
            'string',
        ],
        'StackSetRegions': [
            'string',
        ]
    }
}


Response Structure

(dict) --

ProvisioningArtifactParameters (list) --
Information about the parameters used to provision the product.

(dict) --
Information about a parameter used to provision a product.

ParameterKey (string) --
The parameter key.

DefaultValue (string) --
The default value.

ParameterType (string) --
The parameter type.

IsNoEcho (boolean) --
If this value is true, the value for this parameter is obfuscated from view when the parameter is retrieved. This parameter is used to hide sensitive information.

Description (string) --
The description of the parameter.

ParameterConstraints (dict) --
Constraints that the administrator has put on a parameter.

AllowedValues (list) --
The values that the administrator has allowed for the parameter.

(string) --








ConstraintSummaries (list) --
Information about the constraints used to provision the product.

(dict) --
Summary information about a constraint.

Type (string) --
The type of constraint.

LAUNCH
NOTIFICATION
STACKSET
TEMPLATE


Description (string) --
The description of the constraint.





UsageInstructions (list) --
Any additional metadata specifically related to the provisioning of the product. For example, see the Version field of the CloudFormation template.

(dict) --
Additional information provided by the administrator.

Type (string) --
The usage instruction type for the value.

Value (string) --
The usage instruction value for this type.





TagOptions (list) --
Information about the TagOptions associated with the resource.

(dict) --
Summary information about a TagOption.

Key (string) --
The TagOption key.

Values (list) --
The TagOption value.

(string) --






ProvisioningArtifactPreferences (dict) --
An object that contains information about preferences, such as regions and accounts, for the provisioning artifact.

StackSetAccounts (list) --
One or more AWS accounts where stack instances are deployed from the stack set. These accounts can be scoped in ProvisioningPreferences$StackSetAccounts and UpdateProvisioningPreferences$StackSetAccounts .
Applicable only to a CFN_STACKSET provisioned product type.

(string) --


StackSetRegions (list) --
One or more AWS Regions where stack instances are deployed from the stack set. These regions can be scoped in ProvisioningPreferences$StackSetRegions and UpdateProvisioningPreferences$StackSetRegions .
Applicable only to a CFN_STACKSET provisioned product type.

(string) --










Exceptions

ServiceCatalog.Client.exceptions.InvalidParametersException
ServiceCatalog.Client.exceptions.ResourceNotFoundException


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
        ],
        'ProvisioningArtifactPreferences': {
            'StackSetAccounts': [
                'string',
            ],
            'StackSetRegions': [
                'string',
            ]
        }
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
    
    Exceptions
    
    :example: response = client.describe_record(
        AcceptLanguage='string',
        Id='string',
        PageToken='string',
        PageSize=123
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type Id: string
    :param Id: [REQUIRED]\nThe record identifier of the provisioned product. This identifier is returned by the request operation.\n

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

RecordDetail (dict) --
Information about the product.

RecordId (string) --
The identifier of the record.

ProvisionedProductName (string) --
The user-friendly name of the provisioned product.

Status (string) --
The status of the provisioned product.

CREATED - The request was created but the operation has not started.
IN_PROGRESS - The requested operation is in progress.
IN_PROGRESS_IN_ERROR - The provisioned product is under change but the requested operation failed and some remediation is occurring. For example, a rollback.
SUCCEEDED - The requested operation has successfully completed.
FAILED - The requested operation has unsuccessfully completed. Investigate using the error messages returned.


CreatedTime (datetime) --
The UTC time stamp of the creation time.

UpdatedTime (datetime) --
The time when the record was last updated.

ProvisionedProductType (string) --
The type of provisioned product. The supported values are CFN_STACK and CFN_STACKSET .

RecordType (string) --
The record type.

PROVISION_PRODUCT
UPDATE_PROVISIONED_PRODUCT
TERMINATE_PROVISIONED_PRODUCT


ProvisionedProductId (string) --
The identifier of the provisioned product.

ProductId (string) --
The product identifier.

ProvisioningArtifactId (string) --
The identifier of the provisioning artifact.

PathId (string) --
The path identifier.

RecordErrors (list) --
The errors that occurred.

(dict) --
The error code and description resulting from an operation.

Code (string) --
The numeric value of the error.

Description (string) --
The description of the error.





RecordTags (list) --
One or more tags.

(dict) --
Information about a tag, which is a key-value pair.

Key (string) --
The key for this tag.

Value (string) --
The value for this tag.







RecordOutputs (list) --
Information about the product created as the result of a request. For example, the output for a CloudFormation-backed product that creates an S3 bucket would include the S3 bucket URL.

(dict) --
The output for the product created as the result of a request. For example, the output for a CloudFormation-backed product that creates an S3 bucket would include the S3 bucket URL.

OutputKey (string) --
The output key.

OutputValue (string) --
The output value.

Description (string) --
The description of the output.





NextPageToken (string) --
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.







Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException


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

def describe_service_action(Id=None, AcceptLanguage=None):
    """
    Describes a self-service action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_service_action(
        Id='string',
        AcceptLanguage='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe self-service action identifier.\n

    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ServiceActionDetail': {
        'ServiceActionSummary': {
            'Id': 'string',
            'Name': 'string',
            'Description': 'string',
            'DefinitionType': 'SSM_AUTOMATION'
        },
        'Definition': {
            'string': 'string'
        }
    }
}


Response Structure

(dict) --

ServiceActionDetail (dict) --
Detailed information about the self-service action.

ServiceActionSummary (dict) --
Summary information about the self-service action.

Id (string) --
The self-service action identifier.

Name (string) --
The self-service action name.

Description (string) --
The self-service action description.

DefinitionType (string) --
The self-service action definition type. For example, SSM_AUTOMATION .



Definition (dict) --
A map that defines the self-service action.

(string) --
(string) --












Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException


    :return: {
        'ServiceActionDetail': {
            'ServiceActionSummary': {
                'Id': 'string',
                'Name': 'string',
                'Description': 'string',
                'DefinitionType': 'SSM_AUTOMATION'
            },
            'Definition': {
                'string': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def describe_service_action_execution_parameters(ProvisionedProductId=None, ServiceActionId=None, AcceptLanguage=None):
    """
    Finds the default parameters for a specific self-service action on a specific provisioned product and returns a map of the results to the user.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_service_action_execution_parameters(
        ProvisionedProductId='string',
        ServiceActionId='string',
        AcceptLanguage='string'
    )
    
    
    :type ProvisionedProductId: string
    :param ProvisionedProductId: [REQUIRED]\nThe identifier of the provisioned product.\n

    :type ServiceActionId: string
    :param ServiceActionId: [REQUIRED]\nThe self-service action identifier.\n

    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ServiceActionParameters': [
        {
            'Name': 'string',
            'Type': 'string',
            'DefaultValues': [
                'string',
            ]
        },
    ]
}


Response Structure

(dict) --

ServiceActionParameters (list) --
The parameters of the self-service action.

(dict) --
Details of an execution parameter value that is passed to a self-service action when executed on a provisioned product.

Name (string) --
The name of the execution parameter.

Type (string) --
The execution parameter type.

DefaultValues (list) --
The default values for the execution parameter.

(string) --












Exceptions

ServiceCatalog.Client.exceptions.InvalidParametersException
ServiceCatalog.Client.exceptions.ResourceNotFoundException


    :return: {
        'ServiceActionParameters': [
            {
                'Name': 'string',
                'Type': 'string',
                'DefaultValues': [
                    'string',
                ]
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_tag_option(Id=None):
    """
    Gets information about the specified TagOption.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_tag_option(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe TagOption identifier.\n

    :rtype: dict
ReturnsResponse Syntax{
    'TagOptionDetail': {
        'Key': 'string',
        'Value': 'string',
        'Active': True|False,
        'Id': 'string'
    }
}


Response Structure

(dict) --
TagOptionDetail (dict) --Information about the TagOption.

Key (string) --The TagOption key.

Value (string) --The TagOption value.

Active (boolean) --The TagOption active state.

Id (string) --The TagOption identifier.








Exceptions

ServiceCatalog.Client.exceptions.TagOptionNotMigratedException
ServiceCatalog.Client.exceptions.ResourceNotFoundException


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

def disable_aws_organizations_access():
    """
    Disable portfolio sharing through AWS Organizations feature. This feature will not delete your current shares but it will prevent you from creating new shares throughout your organization. Current shares will not be in sync with your organization structure if it changes after calling this API. This API can only be called by the master account in the organization.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disable_aws_organizations_access()
    
    
    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.InvalidStateException
ServiceCatalog.Client.exceptions.OperationNotSupportedException


    :return: {}
    
    
    :returns: 
    ServiceCatalog.Client.exceptions.ResourceNotFoundException
    ServiceCatalog.Client.exceptions.InvalidStateException
    ServiceCatalog.Client.exceptions.OperationNotSupportedException
    
    """
    pass

def disassociate_budget_from_resource(BudgetName=None, ResourceId=None):
    """
    Disassociates the specified budget from the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_budget_from_resource(
        BudgetName='string',
        ResourceId='string'
    )
    
    
    :type BudgetName: string
    :param BudgetName: [REQUIRED]\nThe name of the budget you want to disassociate.\n

    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe resource identifier you want to disassociate from. Either a portfolio-id or a product-id.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def disassociate_principal_from_portfolio(AcceptLanguage=None, PortfolioId=None, PrincipalARN=None):
    """
    Disassociates a previously associated principal ARN from a specified portfolio.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_principal_from_portfolio(
        AcceptLanguage='string',
        PortfolioId='string',
        PrincipalARN='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type PortfolioId: string
    :param PortfolioId: [REQUIRED]\nThe portfolio identifier.\n

    :type PrincipalARN: string
    :param PrincipalARN: [REQUIRED]\nThe ARN of the principal (IAM user, role, or group).\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ServiceCatalog.Client.exceptions.InvalidParametersException
ServiceCatalog.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def disassociate_product_from_portfolio(AcceptLanguage=None, ProductId=None, PortfolioId=None):
    """
    Disassociates the specified product from the specified portfolio.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_product_from_portfolio(
        AcceptLanguage='string',
        ProductId='string',
        PortfolioId='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type ProductId: string
    :param ProductId: [REQUIRED]\nThe product identifier.\n

    :type PortfolioId: string
    :param PortfolioId: [REQUIRED]\nThe portfolio identifier.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.ResourceInUseException
ServiceCatalog.Client.exceptions.InvalidParametersException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def disassociate_service_action_from_provisioning_artifact(ProductId=None, ProvisioningArtifactId=None, ServiceActionId=None, AcceptLanguage=None):
    """
    Disassociates the specified self-service action association from the specified provisioning artifact.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_service_action_from_provisioning_artifact(
        ProductId='string',
        ProvisioningArtifactId='string',
        ServiceActionId='string',
        AcceptLanguage='string'
    )
    
    
    :type ProductId: string
    :param ProductId: [REQUIRED]\nThe product identifier. For example, prod-abcdzk7xy33qa .\n

    :type ProvisioningArtifactId: string
    :param ProvisioningArtifactId: [REQUIRED]\nThe identifier of the provisioning artifact. For example, pa-4abcdjnxjj6ne .\n

    :type ServiceActionId: string
    :param ServiceActionId: [REQUIRED]\nThe self-service action identifier. For example, act-fs7abcd89wxyz .\n

    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def disassociate_tag_option_from_resource(ResourceId=None, TagOptionId=None):
    """
    Disassociates the specified TagOption from the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_tag_option_from_resource(
        ResourceId='string',
        TagOptionId='string'
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe resource identifier.\n

    :type TagOptionId: string
    :param TagOptionId: [REQUIRED]\nThe TagOption identifier.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ServiceCatalog.Client.exceptions.TagOptionNotMigratedException
ServiceCatalog.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def enable_aws_organizations_access():
    """
    Enable portfolio sharing feature through AWS Organizations. This API will allow Service Catalog to receive updates on your organization in order to sync your shares with the current structure. This API can only be called by the master account in the organization.
    By calling this API Service Catalog will make a call to organizations:EnableAWSServiceAccess on your behalf so that your shares can be in sync with any changes in your AWS Organizations structure.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.enable_aws_organizations_access()
    
    
    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.InvalidStateException
ServiceCatalog.Client.exceptions.OperationNotSupportedException


    :return: {}
    
    
    :returns: 
    ServiceCatalog.Client.exceptions.ResourceNotFoundException
    ServiceCatalog.Client.exceptions.InvalidStateException
    ServiceCatalog.Client.exceptions.OperationNotSupportedException
    
    """
    pass

def execute_provisioned_product_plan(AcceptLanguage=None, PlanId=None, IdempotencyToken=None):
    """
    Provisions or modifies a product based on the resource changes for the specified plan.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.execute_provisioned_product_plan(
        AcceptLanguage='string',
        PlanId='string',
        IdempotencyToken='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type PlanId: string
    :param PlanId: [REQUIRED]\nThe plan identifier.\n

    :type IdempotencyToken: string
    :param IdempotencyToken: [REQUIRED]\nA unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

RecordDetail (dict) --
Information about the result of provisioning the product.

RecordId (string) --
The identifier of the record.

ProvisionedProductName (string) --
The user-friendly name of the provisioned product.

Status (string) --
The status of the provisioned product.

CREATED - The request was created but the operation has not started.
IN_PROGRESS - The requested operation is in progress.
IN_PROGRESS_IN_ERROR - The provisioned product is under change but the requested operation failed and some remediation is occurring. For example, a rollback.
SUCCEEDED - The requested operation has successfully completed.
FAILED - The requested operation has unsuccessfully completed. Investigate using the error messages returned.


CreatedTime (datetime) --
The UTC time stamp of the creation time.

UpdatedTime (datetime) --
The time when the record was last updated.

ProvisionedProductType (string) --
The type of provisioned product. The supported values are CFN_STACK and CFN_STACKSET .

RecordType (string) --
The record type.

PROVISION_PRODUCT
UPDATE_PROVISIONED_PRODUCT
TERMINATE_PROVISIONED_PRODUCT


ProvisionedProductId (string) --
The identifier of the provisioned product.

ProductId (string) --
The product identifier.

ProvisioningArtifactId (string) --
The identifier of the provisioning artifact.

PathId (string) --
The path identifier.

RecordErrors (list) --
The errors that occurred.

(dict) --
The error code and description resulting from an operation.

Code (string) --
The numeric value of the error.

Description (string) --
The description of the error.





RecordTags (list) --
One or more tags.

(dict) --
Information about a tag, which is a key-value pair.

Key (string) --
The key for this tag.

Value (string) --
The value for this tag.













Exceptions

ServiceCatalog.Client.exceptions.InvalidParametersException
ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.InvalidStateException


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

def execute_provisioned_product_service_action(ProvisionedProductId=None, ServiceActionId=None, ExecuteToken=None, AcceptLanguage=None, Parameters=None):
    """
    Executes a self-service action against a provisioned product.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.execute_provisioned_product_service_action(
        ProvisionedProductId='string',
        ServiceActionId='string',
        ExecuteToken='string',
        AcceptLanguage='string',
        Parameters={
            'string': [
                'string',
            ]
        }
    )
    
    
    :type ProvisionedProductId: string
    :param ProvisionedProductId: [REQUIRED]\nThe identifier of the provisioned product.\n

    :type ServiceActionId: string
    :param ServiceActionId: [REQUIRED]\nThe self-service action identifier. For example, act-fs7abcd89wxyz .\n

    :type ExecuteToken: string
    :param ExecuteToken: [REQUIRED]\nAn idempotency token that uniquely identifies the execute request.\nThis field is autopopulated if not provided.\n

    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type Parameters: dict
    :param Parameters: A map of all self-service action parameters and their values. If a provided parameter is of a special type, such as TARGET , the provided value will override the default value generated by AWS Service Catalog. If the parameters field is not provided, no additional parameters are passed and default values will be used for any special parameters such as TARGET .\n\n(string) --\n(list) --\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

RecordDetail (dict) --
An object containing detailed information about the result of provisioning the product.

RecordId (string) --
The identifier of the record.

ProvisionedProductName (string) --
The user-friendly name of the provisioned product.

Status (string) --
The status of the provisioned product.

CREATED - The request was created but the operation has not started.
IN_PROGRESS - The requested operation is in progress.
IN_PROGRESS_IN_ERROR - The provisioned product is under change but the requested operation failed and some remediation is occurring. For example, a rollback.
SUCCEEDED - The requested operation has successfully completed.
FAILED - The requested operation has unsuccessfully completed. Investigate using the error messages returned.


CreatedTime (datetime) --
The UTC time stamp of the creation time.

UpdatedTime (datetime) --
The time when the record was last updated.

ProvisionedProductType (string) --
The type of provisioned product. The supported values are CFN_STACK and CFN_STACKSET .

RecordType (string) --
The record type.

PROVISION_PRODUCT
UPDATE_PROVISIONED_PRODUCT
TERMINATE_PROVISIONED_PRODUCT


ProvisionedProductId (string) --
The identifier of the provisioned product.

ProductId (string) --
The product identifier.

ProvisioningArtifactId (string) --
The identifier of the provisioning artifact.

PathId (string) --
The path identifier.

RecordErrors (list) --
The errors that occurred.

(dict) --
The error code and description resulting from an operation.

Code (string) --
The numeric value of the error.

Description (string) --
The description of the error.





RecordTags (list) --
One or more tags.

(dict) --
Information about a tag, which is a key-value pair.

Key (string) --
The key for this tag.

Value (string) --
The value for this tag.













Exceptions

ServiceCatalog.Client.exceptions.InvalidParametersException
ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.InvalidStateException


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
    :param Params: The parameters normally passed to\nClientMethod.

    :type ExpiresIn: int
    :param ExpiresIn: The number of seconds the presigned url is valid\nfor. By default it expires in an hour (3600 seconds)

    :type HttpMethod: string
    :param HttpMethod: The http method to use on the generated url. By\ndefault, the http method is whatever is used in the method\'s model.

    """
    pass

def get_aws_organizations_access_status():
    """
    Get the Access Status for AWS Organization portfolio share feature. This API can only be called by the master account in the organization.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_aws_organizations_access_status()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'AccessStatus': 'ENABLED'|'UNDER_CHANGE'|'DISABLED'
}


Response Structure

(dict) --
AccessStatus (string) --The status of the portfolio share feature.






Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.OperationNotSupportedException


    :return: {
        'AccessStatus': 'ENABLED'|'UNDER_CHANGE'|'DISABLED'
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

def list_accepted_portfolio_shares(AcceptLanguage=None, PageToken=None, PageSize=None, PortfolioShareType=None):
    """
    Lists all portfolios for which sharing was accepted by this account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_accepted_portfolio_shares(
        AcceptLanguage='string',
        PageToken='string',
        PageSize=123,
        PortfolioShareType='IMPORTED'|'AWS_SERVICECATALOG'|'AWS_ORGANIZATIONS'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :type PortfolioShareType: string
    :param PortfolioShareType: The type of shared portfolios to list. The default is to list imported portfolios.\n\nAWS_ORGANIZATIONS - List portfolios shared by the master account of your organization\nAWS_SERVICECATALOG - List default portfolios\nIMPORTED - List imported portfolios\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

PortfolioDetails (list) --
Information about the portfolios.

(dict) --
Information about a portfolio.

Id (string) --
The portfolio identifier.

ARN (string) --
The ARN assigned to the portfolio.

DisplayName (string) --
The name to use for display purposes.

Description (string) --
The description of the portfolio.

CreatedTime (datetime) --
The UTC time stamp of the creation time.

ProviderName (string) --
The name of the portfolio provider.





NextPageToken (string) --
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.







Exceptions

ServiceCatalog.Client.exceptions.InvalidParametersException
ServiceCatalog.Client.exceptions.OperationNotSupportedException


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
    
    
    :returns: 
    ServiceCatalog.Client.exceptions.InvalidParametersException
    ServiceCatalog.Client.exceptions.OperationNotSupportedException
    
    """
    pass

def list_budgets_for_resource(AcceptLanguage=None, ResourceId=None, PageSize=None, PageToken=None):
    """
    Lists all the budgets associated to the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_budgets_for_resource(
        AcceptLanguage='string',
        ResourceId='string',
        PageSize=123,
        PageToken='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe resource identifier.\n

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :rtype: dict

ReturnsResponse Syntax
{
    'Budgets': [
        {
            'BudgetName': 'string'
        },
    ],
    'NextPageToken': 'string'
}


Response Structure

(dict) --

Budgets (list) --
Information about the associated budgets.

(dict) --
Information about a budget.

BudgetName (string) --
Name of the associated budget.





NextPageToken (string) --
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.







Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.InvalidParametersException


    :return: {
        'Budgets': [
            {
                'BudgetName': 'string'
            },
        ],
        'NextPageToken': 'string'
    }
    
    
    :returns: 
    ServiceCatalog.Client.exceptions.ResourceNotFoundException
    ServiceCatalog.Client.exceptions.InvalidParametersException
    
    """
    pass

def list_constraints_for_portfolio(AcceptLanguage=None, PortfolioId=None, ProductId=None, PageSize=None, PageToken=None):
    """
    Lists the constraints for the specified portfolio and product.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_constraints_for_portfolio(
        AcceptLanguage='string',
        PortfolioId='string',
        ProductId='string',
        PageSize=123,
        PageToken='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type PortfolioId: string
    :param PortfolioId: [REQUIRED]\nThe portfolio identifier.\n

    :type ProductId: string
    :param ProductId: The product identifier.

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :rtype: dict

ReturnsResponse Syntax
{
    'ConstraintDetails': [
        {
            'ConstraintId': 'string',
            'Type': 'string',
            'Description': 'string',
            'Owner': 'string',
            'ProductId': 'string',
            'PortfolioId': 'string'
        },
    ],
    'NextPageToken': 'string'
}


Response Structure

(dict) --

ConstraintDetails (list) --
Information about the constraints.

(dict) --
Information about a constraint.

ConstraintId (string) --
The identifier of the constraint.

Type (string) --
The type of constraint.

LAUNCH
NOTIFICATION
STACKSET
TEMPLATE


Description (string) --
The description of the constraint.

Owner (string) --
The owner of the constraint.

ProductId (string) --
The identifier of the product the constraint applies to. Note that a constraint applies to a specific instance of a product within a certain portfolio.

PortfolioId (string) --
The identifier of the portfolio the product resides in. The constraint applies only to the instance of the product that lives within this portfolio.





NextPageToken (string) --
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.







Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.InvalidParametersException


    :return: {
        'ConstraintDetails': [
            {
                'ConstraintId': 'string',
                'Type': 'string',
                'Description': 'string',
                'Owner': 'string',
                'ProductId': 'string',
                'PortfolioId': 'string'
            },
        ],
        'NextPageToken': 'string'
    }
    
    
    :returns: 
    LAUNCH
    NOTIFICATION
    STACKSET
    TEMPLATE
    
    """
    pass

def list_launch_paths(AcceptLanguage=None, ProductId=None, PageSize=None, PageToken=None):
    """
    Lists the paths to the specified product. A path is how the user has access to a specified product, and is necessary when provisioning a product. A path also determines the constraints put on the product.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_launch_paths(
        AcceptLanguage='string',
        ProductId='string',
        PageSize=123,
        PageToken='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type ProductId: string
    :param ProductId: [REQUIRED]\nThe product identifier.\n

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

LaunchPathSummaries (list) --
Information about the launch path.

(dict) --
Summary information about a product path for a user.

Id (string) --
The identifier of the product path.

ConstraintSummaries (list) --
The constraints on the portfolio-product relationship.

(dict) --
Summary information about a constraint.

Type (string) --
The type of constraint.

LAUNCH
NOTIFICATION
STACKSET
TEMPLATE


Description (string) --
The description of the constraint.





Tags (list) --
The tags associated with this product path.

(dict) --
Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.

Key (string) --
The tag key.

Value (string) --
The value for this key.





Name (string) --
The name of the portfolio to which the user was assigned.





NextPageToken (string) --
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.







Exceptions

ServiceCatalog.Client.exceptions.InvalidParametersException
ServiceCatalog.Client.exceptions.ResourceNotFoundException


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
    STACKSET
    TEMPLATE
    
    """
    pass

def list_organization_portfolio_access(AcceptLanguage=None, PortfolioId=None, OrganizationNodeType=None, PageToken=None, PageSize=None):
    """
    Lists the organization nodes that have access to the specified portfolio. This API can only be called by the master account in the organization.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_organization_portfolio_access(
        AcceptLanguage='string',
        PortfolioId='string',
        OrganizationNodeType='ORGANIZATION'|'ORGANIZATIONAL_UNIT'|'ACCOUNT',
        PageToken='string',
        PageSize=123
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type PortfolioId: string
    :param PortfolioId: [REQUIRED]\nThe portfolio identifier. For example, port-2abcdext3y5fk .\n

    :type OrganizationNodeType: string
    :param OrganizationNodeType: [REQUIRED]\nThe organization node type that will be returned in the output.\n\nORGANIZATION - Organization that has access to the portfolio.\nORGANIZATIONAL_UNIT - Organizational unit that has access to the portfolio within your organization.\nACCOUNT - Account that has access to the portfolio within your organization.\n\n

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :rtype: dict

ReturnsResponse Syntax
{
    'OrganizationNodes': [
        {
            'Type': 'ORGANIZATION'|'ORGANIZATIONAL_UNIT'|'ACCOUNT',
            'Value': 'string'
        },
    ],
    'NextPageToken': 'string'
}


Response Structure

(dict) --

OrganizationNodes (list) --
Displays information about the organization nodes.

(dict) --
Information about the organization node.

Type (string) --
The organization node type.

Value (string) --
The identifier of the organization node.





NextPageToken (string) --
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.







Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.InvalidParametersException
ServiceCatalog.Client.exceptions.OperationNotSupportedException


    :return: {
        'OrganizationNodes': [
            {
                'Type': 'ORGANIZATION'|'ORGANIZATIONAL_UNIT'|'ACCOUNT',
                'Value': 'string'
            },
        ],
        'NextPageToken': 'string'
    }
    
    
    :returns: 
    ServiceCatalog.Client.exceptions.ResourceNotFoundException
    ServiceCatalog.Client.exceptions.InvalidParametersException
    ServiceCatalog.Client.exceptions.OperationNotSupportedException
    
    """
    pass

def list_portfolio_access(AcceptLanguage=None, PortfolioId=None, OrganizationParentId=None, PageToken=None, PageSize=None):
    """
    Lists the account IDs that have access to the specified portfolio.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_portfolio_access(
        AcceptLanguage='string',
        PortfolioId='string',
        OrganizationParentId='string',
        PageToken='string',
        PageSize=123
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type PortfolioId: string
    :param PortfolioId: [REQUIRED]\nThe portfolio identifier.\n

    :type OrganizationParentId: string
    :param OrganizationParentId: The ID of an organization node the portfolio is shared with. All children of this node with an inherited portfolio share will be returned.

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :rtype: dict

ReturnsResponse Syntax
{
    'AccountIds': [
        'string',
    ],
    'NextPageToken': 'string'
}


Response Structure

(dict) --

AccountIds (list) --
Information about the AWS accounts with access to the portfolio.

(string) --


NextPageToken (string) --
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.







Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.InvalidParametersException


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
    
    Exceptions
    
    :example: response = client.list_portfolios(
        AcceptLanguage='string',
        PageToken='string',
        PageSize=123
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

PortfolioDetails (list) --
Information about the portfolios.

(dict) --
Information about a portfolio.

Id (string) --
The portfolio identifier.

ARN (string) --
The ARN assigned to the portfolio.

DisplayName (string) --
The name to use for display purposes.

Description (string) --
The description of the portfolio.

CreatedTime (datetime) --
The UTC time stamp of the creation time.

ProviderName (string) --
The name of the portfolio provider.





NextPageToken (string) --
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.







Exceptions

ServiceCatalog.Client.exceptions.InvalidParametersException


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
    
    
    :returns: 
    ServiceCatalog.Client.exceptions.InvalidParametersException
    
    """
    pass

def list_portfolios_for_product(AcceptLanguage=None, ProductId=None, PageToken=None, PageSize=None):
    """
    Lists all portfolios that the specified product is associated with.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_portfolios_for_product(
        AcceptLanguage='string',
        ProductId='string',
        PageToken='string',
        PageSize=123
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type ProductId: string
    :param ProductId: [REQUIRED]\nThe product identifier.\n

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

PortfolioDetails (list) --
Information about the portfolios.

(dict) --
Information about a portfolio.

Id (string) --
The portfolio identifier.

ARN (string) --
The ARN assigned to the portfolio.

DisplayName (string) --
The name to use for display purposes.

Description (string) --
The description of the portfolio.

CreatedTime (datetime) --
The UTC time stamp of the creation time.

ProviderName (string) --
The name of the portfolio provider.





NextPageToken (string) --
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.







Exceptions

ServiceCatalog.Client.exceptions.InvalidParametersException
ServiceCatalog.Client.exceptions.ResourceNotFoundException


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
    
    
    :returns: 
    ServiceCatalog.Client.exceptions.InvalidParametersException
    ServiceCatalog.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def list_principals_for_portfolio(AcceptLanguage=None, PortfolioId=None, PageSize=None, PageToken=None):
    """
    Lists all principal ARNs associated with the specified portfolio.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_principals_for_portfolio(
        AcceptLanguage='string',
        PortfolioId='string',
        PageSize=123,
        PageToken='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type PortfolioId: string
    :param PortfolioId: [REQUIRED]\nThe portfolio identifier.\n

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :rtype: dict

ReturnsResponse Syntax
{
    'Principals': [
        {
            'PrincipalARN': 'string',
            'PrincipalType': 'IAM'
        },
    ],
    'NextPageToken': 'string'
}


Response Structure

(dict) --

Principals (list) --
The IAM principals (users or roles) associated with the portfolio.

(dict) --
Information about a principal.

PrincipalARN (string) --
The ARN of the principal (IAM user, role, or group).

PrincipalType (string) --
The principal type. The supported value is IAM .





NextPageToken (string) --
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.







Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.InvalidParametersException


    :return: {
        'Principals': [
            {
                'PrincipalARN': 'string',
                'PrincipalType': 'IAM'
            },
        ],
        'NextPageToken': 'string'
    }
    
    
    :returns: 
    ServiceCatalog.Client.exceptions.ResourceNotFoundException
    ServiceCatalog.Client.exceptions.InvalidParametersException
    
    """
    pass

def list_provisioned_product_plans(AcceptLanguage=None, ProvisionProductId=None, PageSize=None, PageToken=None, AccessLevelFilter=None):
    """
    Lists the plans for the specified provisioned product or all plans to which the user has access.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type ProvisionProductId: string
    :param ProvisionProductId: The product identifier.

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :type AccessLevelFilter: dict
    :param AccessLevelFilter: The access level to use to obtain results. The default is User .\n\nKey (string) --The access level.\n\nAccount - Filter results based on the account.\nRole - Filter results based on the federated role of the specified user.\nUser - Filter results based on the specified user.\n\n\nValue (string) --The user to which the access level applies. The only supported value is Self .\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

ProvisionedProductPlans (list) --
Information about the plans.

(dict) --
Summary information about a plan.

PlanName (string) --
The name of the plan.

PlanId (string) --
The plan identifier.

ProvisionProductId (string) --
The product identifier.

ProvisionProductName (string) --
The user-friendly name of the provisioned product.

PlanType (string) --
The plan type.

ProvisioningArtifactId (string) --
The identifier of the provisioning artifact.





NextPageToken (string) --
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.







Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.InvalidParametersException


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
    
    
    :returns: 
    ServiceCatalog.Client.exceptions.ResourceNotFoundException
    ServiceCatalog.Client.exceptions.InvalidParametersException
    
    """
    pass

def list_provisioning_artifacts(AcceptLanguage=None, ProductId=None):
    """
    Lists all provisioning artifacts (also known as versions) for the specified product.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_provisioning_artifacts(
        AcceptLanguage='string',
        ProductId='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type ProductId: string
    :param ProductId: [REQUIRED]\nThe product identifier.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ProvisioningArtifactDetails': [
        {
            'Id': 'string',
            'Name': 'string',
            'Description': 'string',
            'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE_AMI'|'MARKETPLACE_CAR',
            'CreatedTime': datetime(2015, 1, 1),
            'Active': True|False,
            'Guidance': 'DEFAULT'|'DEPRECATED'
        },
    ],
    'NextPageToken': 'string'
}


Response Structure

(dict) --

ProvisioningArtifactDetails (list) --
Information about the provisioning artifacts.

(dict) --
Information about a provisioning artifact (also known as a version) for a product.

Id (string) --
The identifier of the provisioning artifact.

Name (string) --
The name of the provisioning artifact.

Description (string) --
The description of the provisioning artifact.

Type (string) --
The type of provisioning artifact.

CLOUD_FORMATION_TEMPLATE - AWS CloudFormation template
MARKETPLACE_AMI - AWS Marketplace AMI
MARKETPLACE_CAR - AWS Marketplace Clusters and AWS Resources


CreatedTime (datetime) --
The UTC time stamp of the creation time.

Active (boolean) --
Indicates whether the product version is active.

Guidance (string) --
Information set by the administrator to provide guidance to end users about which provisioning artifacts to use.





NextPageToken (string) --
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.







Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.InvalidParametersException


    :return: {
        'ProvisioningArtifactDetails': [
            {
                'Id': 'string',
                'Name': 'string',
                'Description': 'string',
                'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE_AMI'|'MARKETPLACE_CAR',
                'CreatedTime': datetime(2015, 1, 1),
                'Active': True|False,
                'Guidance': 'DEFAULT'|'DEPRECATED'
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

def list_provisioning_artifacts_for_service_action(ServiceActionId=None, PageSize=None, PageToken=None, AcceptLanguage=None):
    """
    Lists all provisioning artifacts (also known as versions) for the specified self-service action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_provisioning_artifacts_for_service_action(
        ServiceActionId='string',
        PageSize=123,
        PageToken='string',
        AcceptLanguage='string'
    )
    
    
    :type ServiceActionId: string
    :param ServiceActionId: [REQUIRED]\nThe self-service action identifier. For example, act-fs7abcd89wxyz .\n

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ProvisioningArtifactViews': [
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
            'ProvisioningArtifact': {
                'Id': 'string',
                'Name': 'string',
                'Description': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'Guidance': 'DEFAULT'|'DEPRECATED'
            }
        },
    ],
    'NextPageToken': 'string'
}


Response Structure

(dict) --

ProvisioningArtifactViews (list) --
An array of objects with information about product views and provisioning artifacts.

(dict) --
An object that contains summary information about a product view and a provisioning artifact.

ProductViewSummary (dict) --
Summary information about a product view.

Id (string) --
The product view identifier.

ProductId (string) --
The product identifier.

Name (string) --
The name of the product.

Owner (string) --
The owner of the product. Contact the product administrator for the significance of this value.

ShortDescription (string) --
Short description of the product.

Type (string) --
The product type. Contact the product administrator for the significance of this value. If this value is MARKETPLACE , the product was created by AWS Marketplace.

Distributor (string) --
The distributor of the product. Contact the product administrator for the significance of this value.

HasDefaultPath (boolean) --
Indicates whether the product has a default path. If the product does not have a default path, call  ListLaunchPaths to disambiguate between paths. Otherwise,  ListLaunchPaths is not required, and the output of  ProductViewSummary can be used directly with  DescribeProvisioningParameters .

SupportEmail (string) --
The email contact information to obtain support for this Product.

SupportDescription (string) --
The description of the support for this Product.

SupportUrl (string) --
The URL information to obtain support for this Product.



ProvisioningArtifact (dict) --
Information about a provisioning artifact. A provisioning artifact is also known as a product version.

Id (string) --
The identifier of the provisioning artifact.

Name (string) --
The name of the provisioning artifact.

Description (string) --
The description of the provisioning artifact.

CreatedTime (datetime) --
The UTC time stamp of the creation time.

Guidance (string) --
Information set by the administrator to provide guidance to end users about which provisioning artifacts to use.







NextPageToken (string) --
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.







Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.InvalidParametersException


    :return: {
        'ProvisioningArtifactViews': [
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
                'ProvisioningArtifact': {
                    'Id': 'string',
                    'Name': 'string',
                    'Description': 'string',
                    'CreatedTime': datetime(2015, 1, 1),
                    'Guidance': 'DEFAULT'|'DEPRECATED'
                }
            },
        ],
        'NextPageToken': 'string'
    }
    
    
    :returns: 
    ServiceCatalog.Client.exceptions.ResourceNotFoundException
    ServiceCatalog.Client.exceptions.InvalidParametersException
    
    """
    pass

def list_record_history(AcceptLanguage=None, AccessLevelFilter=None, SearchFilter=None, PageSize=None, PageToken=None):
    """
    Lists the specified requests or all performed requests.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type AccessLevelFilter: dict
    :param AccessLevelFilter: The access level to use to obtain results. The default is User .\n\nKey (string) --The access level.\n\nAccount - Filter results based on the account.\nRole - Filter results based on the federated role of the specified user.\nUser - Filter results based on the specified user.\n\n\nValue (string) --The user to which the access level applies. The only supported value is Self .\n\n\n

    :type SearchFilter: dict
    :param SearchFilter: The search filter to scope the results.\n\nKey (string) --The filter key.\n\nproduct - Filter results based on the specified product identifier.\nprovisionedproduct - Filter results based on the provisioned product identifier.\n\n\nValue (string) --The filter value.\n\n\n

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

RecordDetails (list) --
The records, in reverse chronological order.

(dict) --
Information about a request operation.

RecordId (string) --
The identifier of the record.

ProvisionedProductName (string) --
The user-friendly name of the provisioned product.

Status (string) --
The status of the provisioned product.

CREATED - The request was created but the operation has not started.
IN_PROGRESS - The requested operation is in progress.
IN_PROGRESS_IN_ERROR - The provisioned product is under change but the requested operation failed and some remediation is occurring. For example, a rollback.
SUCCEEDED - The requested operation has successfully completed.
FAILED - The requested operation has unsuccessfully completed. Investigate using the error messages returned.


CreatedTime (datetime) --
The UTC time stamp of the creation time.

UpdatedTime (datetime) --
The time when the record was last updated.

ProvisionedProductType (string) --
The type of provisioned product. The supported values are CFN_STACK and CFN_STACKSET .

RecordType (string) --
The record type.

PROVISION_PRODUCT
UPDATE_PROVISIONED_PRODUCT
TERMINATE_PROVISIONED_PRODUCT


ProvisionedProductId (string) --
The identifier of the provisioned product.

ProductId (string) --
The product identifier.

ProvisioningArtifactId (string) --
The identifier of the provisioning artifact.

PathId (string) --
The path identifier.

RecordErrors (list) --
The errors that occurred.

(dict) --
The error code and description resulting from an operation.

Code (string) --
The numeric value of the error.

Description (string) --
The description of the error.





RecordTags (list) --
One or more tags.

(dict) --
Information about a tag, which is a key-value pair.

Key (string) --
The key for this tag.

Value (string) --
The value for this tag.









NextPageToken (string) --
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.







Exceptions

ServiceCatalog.Client.exceptions.InvalidParametersException


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
    
    Exceptions
    
    :example: response = client.list_resources_for_tag_option(
        TagOptionId='string',
        ResourceType='string',
        PageSize=123,
        PageToken='string'
    )
    
    
    :type TagOptionId: string
    :param TagOptionId: [REQUIRED]\nThe TagOption identifier.\n

    :type ResourceType: string
    :param ResourceType: The resource type.\n\nPortfolio\nProduct\n\n

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

ResourceDetails (list) --
Information about the resources.

(dict) --
Information about a resource.

Id (string) --
The identifier of the resource.

ARN (string) --
The ARN of the resource.

Name (string) --
The name of the resource.

Description (string) --
The description of the resource.

CreatedTime (datetime) --
The creation time of the resource.





PageToken (string) --
The page token for the next set of results. To retrieve the first set of results, use null.







Exceptions

ServiceCatalog.Client.exceptions.TagOptionNotMigratedException
ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.InvalidParametersException


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
    
    
    :returns: 
    ServiceCatalog.Client.exceptions.TagOptionNotMigratedException
    ServiceCatalog.Client.exceptions.ResourceNotFoundException
    ServiceCatalog.Client.exceptions.InvalidParametersException
    
    """
    pass

def list_service_actions(AcceptLanguage=None, PageSize=None, PageToken=None):
    """
    Lists all self-service actions.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_service_actions(
        AcceptLanguage='string',
        PageSize=123,
        PageToken='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :rtype: dict

ReturnsResponse Syntax
{
    'ServiceActionSummaries': [
        {
            'Id': 'string',
            'Name': 'string',
            'Description': 'string',
            'DefinitionType': 'SSM_AUTOMATION'
        },
    ],
    'NextPageToken': 'string'
}


Response Structure

(dict) --

ServiceActionSummaries (list) --
An object containing information about the service actions associated with the provisioning artifact.

(dict) --
Detailed information about the self-service action.

Id (string) --
The self-service action identifier.

Name (string) --
The self-service action name.

Description (string) --
The self-service action description.

DefinitionType (string) --
The self-service action definition type. For example, SSM_AUTOMATION .





NextPageToken (string) --
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.







Exceptions

ServiceCatalog.Client.exceptions.InvalidParametersException


    :return: {
        'ServiceActionSummaries': [
            {
                'Id': 'string',
                'Name': 'string',
                'Description': 'string',
                'DefinitionType': 'SSM_AUTOMATION'
            },
        ],
        'NextPageToken': 'string'
    }
    
    
    :returns: 
    ServiceCatalog.Client.exceptions.InvalidParametersException
    
    """
    pass

def list_service_actions_for_provisioning_artifact(ProductId=None, ProvisioningArtifactId=None, PageSize=None, PageToken=None, AcceptLanguage=None):
    """
    Returns a paginated list of self-service actions associated with the specified Product ID and Provisioning Artifact ID.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_service_actions_for_provisioning_artifact(
        ProductId='string',
        ProvisioningArtifactId='string',
        PageSize=123,
        PageToken='string',
        AcceptLanguage='string'
    )
    
    
    :type ProductId: string
    :param ProductId: [REQUIRED]\nThe product identifier. For example, prod-abcdzk7xy33qa .\n

    :type ProvisioningArtifactId: string
    :param ProvisioningArtifactId: [REQUIRED]\nThe identifier of the provisioning artifact. For example, pa-4abcdjnxjj6ne .\n

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ServiceActionSummaries': [
        {
            'Id': 'string',
            'Name': 'string',
            'Description': 'string',
            'DefinitionType': 'SSM_AUTOMATION'
        },
    ],
    'NextPageToken': 'string'
}


Response Structure

(dict) --

ServiceActionSummaries (list) --
An object containing information about the self-service actions associated with the provisioning artifact.

(dict) --
Detailed information about the self-service action.

Id (string) --
The self-service action identifier.

Name (string) --
The self-service action name.

Description (string) --
The self-service action description.

DefinitionType (string) --
The self-service action definition type. For example, SSM_AUTOMATION .





NextPageToken (string) --
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.







Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.InvalidParametersException


    :return: {
        'ServiceActionSummaries': [
            {
                'Id': 'string',
                'Name': 'string',
                'Description': 'string',
                'DefinitionType': 'SSM_AUTOMATION'
            },
        ],
        'NextPageToken': 'string'
    }
    
    
    :returns: 
    ServiceCatalog.Client.exceptions.ResourceNotFoundException
    ServiceCatalog.Client.exceptions.InvalidParametersException
    
    """
    pass

def list_stack_instances_for_provisioned_product(AcceptLanguage=None, ProvisionedProductId=None, PageToken=None, PageSize=None):
    """
    Returns summary information about stack instances that are associated with the specified CFN_STACKSET type provisioned product. You can filter for stack instances that are associated with a specific AWS account name or region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_stack_instances_for_provisioned_product(
        AcceptLanguage='string',
        ProvisionedProductId='string',
        PageToken='string',
        PageSize=123
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type ProvisionedProductId: string
    :param ProvisionedProductId: [REQUIRED]\nThe identifier of the provisioned product.\n

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :rtype: dict

ReturnsResponse Syntax
{
    'StackInstances': [
        {
            'Account': 'string',
            'Region': 'string',
            'StackInstanceStatus': 'CURRENT'|'OUTDATED'|'INOPERABLE'
        },
    ],
    'NextPageToken': 'string'
}


Response Structure

(dict) --

StackInstances (list) --
List of stack instances.

(dict) --
An AWS CloudFormation stack, in a specific account and region, that\'s part of a stack set operation. A stack instance is a reference to an attempted or actual stack in a given account within a given region. A stack instance can exist without a stack\xe2\x80\x94for example, if the stack couldn\'t be created for some reason. A stack instance is associated with only one stack set. Each stack instance contains the ID of its associated stack set, as well as the ID of the actual stack and the stack status.

Account (string) --
The name of the AWS account that the stack instance is associated with.

Region (string) --
The name of the AWS region that the stack instance is associated with.

StackInstanceStatus (string) --
The status of the stack instance, in terms of its synchronization with its associated stack set.

INOPERABLE : A DeleteStackInstances operation has failed and left the stack in an unstable state. Stacks in this state are excluded from further UpdateStackSet operations. You might need to perform a DeleteStackInstances operation, with RetainStacks set to true, to delete the stack instance, and then delete the stack manually.
OUTDATED : The stack isn\'t currently up to date with the stack set because either the associated stack failed during a CreateStackSet or UpdateStackSet operation, or the stack was part of a CreateStackSet or UpdateStackSet operation that failed or was stopped before the stack was created or updated.
CURRENT : The stack is currently up to date with the stack set.






NextPageToken (string) --
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.







Exceptions

ServiceCatalog.Client.exceptions.InvalidParametersException
ServiceCatalog.Client.exceptions.ResourceNotFoundException


    :return: {
        'StackInstances': [
            {
                'Account': 'string',
                'Region': 'string',
                'StackInstanceStatus': 'CURRENT'|'OUTDATED'|'INOPERABLE'
            },
        ],
        'NextPageToken': 'string'
    }
    
    
    :returns: 
    INOPERABLE : A DeleteStackInstances operation has failed and left the stack in an unstable state. Stacks in this state are excluded from further UpdateStackSet operations. You might need to perform a DeleteStackInstances operation, with RetainStacks set to true, to delete the stack instance, and then delete the stack manually.
    OUTDATED : The stack isn\'t currently up to date with the stack set because either the associated stack failed during a CreateStackSet or UpdateStackSet operation, or the stack was part of a CreateStackSet or UpdateStackSet operation that failed or was stopped before the stack was created or updated.
    CURRENT : The stack is currently up to date with the stack set.
    
    """
    pass

def list_tag_options(Filters=None, PageSize=None, PageToken=None):
    """
    Lists the specified TagOptions or all TagOptions.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param Filters: The search filters. If no search filters are specified, the output includes all TagOptions.\n\nKey (string) --The TagOption key.\n\nValue (string) --The TagOption value.\n\nActive (boolean) --The active state.\n\n\n

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

TagOptionDetails (list) --
Information about the TagOptions.

(dict) --
Information about a TagOption.

Key (string) --
The TagOption key.

Value (string) --
The TagOption value.

Active (boolean) --
The TagOption active state.

Id (string) --
The TagOption identifier.





PageToken (string) --
The page token for the next set of results. To retrieve the first set of results, use null.







Exceptions

ServiceCatalog.Client.exceptions.TagOptionNotMigratedException
ServiceCatalog.Client.exceptions.InvalidParametersException


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
    
    
    :returns: 
    ServiceCatalog.Client.exceptions.TagOptionNotMigratedException
    ServiceCatalog.Client.exceptions.InvalidParametersException
    
    """
    pass

def provision_product(AcceptLanguage=None, ProductId=None, ProvisioningArtifactId=None, PathId=None, ProvisionedProductName=None, ProvisioningParameters=None, ProvisioningPreferences=None, Tags=None, NotificationArns=None, ProvisionToken=None):
    """
    Provisions the specified product.
    A provisioned product is a resourced instance of a product. For example, provisioning a product based on a CloudFormation template launches a CloudFormation stack and its underlying resources. You can check the status of this request using  DescribeRecord .
    If the request contains a tag key with an empty list of values, there is a tag conflict for that key. Do not include conflicted keys as tags, or this causes the error "Parameter validation failed: Missing required parameter in Tags[N ]:Value ".
    See also: AWS API Documentation
    
    Exceptions
    
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
        ProvisioningPreferences={
            'StackSetAccounts': [
                'string',
            ],
            'StackSetRegions': [
                'string',
            ],
            'StackSetFailureToleranceCount': 123,
            'StackSetFailureTolerancePercentage': 123,
            'StackSetMaxConcurrencyCount': 123,
            'StackSetMaxConcurrencyPercentage': 123
        },
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
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type ProductId: string
    :param ProductId: [REQUIRED]\nThe product identifier.\n

    :type ProvisioningArtifactId: string
    :param ProvisioningArtifactId: [REQUIRED]\nThe identifier of the provisioning artifact.\n

    :type PathId: string
    :param PathId: The path identifier of the product. This value is optional if the product has a default path, and required if the product has more than one path. To list the paths for a product, use ListLaunchPaths .

    :type ProvisionedProductName: string
    :param ProvisionedProductName: [REQUIRED]\nA user-friendly name for the provisioned product. This value must be unique for the AWS account and cannot be updated after the product is provisioned.\n

    :type ProvisioningParameters: list
    :param ProvisioningParameters: Parameters specified by the administrator that are required for provisioning the product.\n\n(dict) --Information about a parameter used to provision a product.\n\nKey (string) --The parameter key.\n\nValue (string) --The parameter value.\n\n\n\n\n

    :type ProvisioningPreferences: dict
    :param ProvisioningPreferences: An object that contains information about the provisioning preferences for a stack set.\n\nStackSetAccounts (list) --One or more AWS accounts that will have access to the provisioned product.\nApplicable only to a CFN_STACKSET provisioned product type.\nThe AWS accounts specified should be within the list of accounts in the STACKSET constraint. To get the list of accounts in the STACKSET constraint, use the DescribeProvisioningParameters operation.\nIf no values are specified, the default value is all accounts from the STACKSET constraint.\n\n(string) --\n\n\nStackSetRegions (list) --One or more AWS Regions where the provisioned product will be available.\nApplicable only to a CFN_STACKSET provisioned product type.\nThe specified regions should be within the list of regions from the STACKSET constraint. To get the list of regions in the STACKSET constraint, use the DescribeProvisioningParameters operation.\nIf no values are specified, the default value is all regions from the STACKSET constraint.\n\n(string) --\n\n\nStackSetFailureToleranceCount (integer) --The number of accounts, per region, for which this operation can fail before AWS Service Catalog stops the operation in that region. If the operation is stopped in a region, AWS Service Catalog doesn\'t attempt the operation in any subsequent regions.\nApplicable only to a CFN_STACKSET provisioned product type.\nConditional: You must specify either StackSetFailureToleranceCount or StackSetFailureTolerancePercentage , but not both.\nThe default value is 0 if no value is specified.\n\nStackSetFailureTolerancePercentage (integer) --The percentage of accounts, per region, for which this stack operation can fail before AWS Service Catalog stops the operation in that region. If the operation is stopped in a region, AWS Service Catalog doesn\'t attempt the operation in any subsequent regions.\nWhen calculating the number of accounts based on the specified percentage, AWS Service Catalog rounds down to the next whole number.\nApplicable only to a CFN_STACKSET provisioned product type.\nConditional: You must specify either StackSetFailureToleranceCount or StackSetFailureTolerancePercentage , but not both.\n\nStackSetMaxConcurrencyCount (integer) --The maximum number of accounts in which to perform this operation at one time. This is dependent on the value of StackSetFailureToleranceCount . StackSetMaxConcurrentCount is at most one more than the StackSetFailureToleranceCount .\nNote that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.\nApplicable only to a CFN_STACKSET provisioned product type.\nConditional: You must specify either StackSetMaxConcurrentCount or StackSetMaxConcurrentPercentage , but not both.\n\nStackSetMaxConcurrencyPercentage (integer) --The maximum percentage of accounts in which to perform this operation at one time.\nWhen calculating the number of accounts based on the specified percentage, AWS Service Catalog rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, AWS Service Catalog sets the number as 1 instead.\nNote that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.\nApplicable only to a CFN_STACKSET provisioned product type.\nConditional: You must specify either StackSetMaxConcurrentCount or StackSetMaxConcurrentPercentage , but not both.\n\n\n

    :type Tags: list
    :param Tags: One or more tags.\n\n(dict) --Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.\n\nKey (string) -- [REQUIRED]The tag key.\n\nValue (string) -- [REQUIRED]The value for this key.\n\n\n\n\n

    :type NotificationArns: list
    :param NotificationArns: Passed to CloudFormation. The SNS topic ARNs to which to publish stack-related events.\n\n(string) --\n\n

    :type ProvisionToken: string
    :param ProvisionToken: [REQUIRED]\nAn idempotency token that uniquely identifies the provisioning request.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

RecordDetail (dict) --
Information about the result of provisioning the product.

RecordId (string) --
The identifier of the record.

ProvisionedProductName (string) --
The user-friendly name of the provisioned product.

Status (string) --
The status of the provisioned product.

CREATED - The request was created but the operation has not started.
IN_PROGRESS - The requested operation is in progress.
IN_PROGRESS_IN_ERROR - The provisioned product is under change but the requested operation failed and some remediation is occurring. For example, a rollback.
SUCCEEDED - The requested operation has successfully completed.
FAILED - The requested operation has unsuccessfully completed. Investigate using the error messages returned.


CreatedTime (datetime) --
The UTC time stamp of the creation time.

UpdatedTime (datetime) --
The time when the record was last updated.

ProvisionedProductType (string) --
The type of provisioned product. The supported values are CFN_STACK and CFN_STACKSET .

RecordType (string) --
The record type.

PROVISION_PRODUCT
UPDATE_PROVISIONED_PRODUCT
TERMINATE_PROVISIONED_PRODUCT


ProvisionedProductId (string) --
The identifier of the provisioned product.

ProductId (string) --
The product identifier.

ProvisioningArtifactId (string) --
The identifier of the provisioning artifact.

PathId (string) --
The path identifier.

RecordErrors (list) --
The errors that occurred.

(dict) --
The error code and description resulting from an operation.

Code (string) --
The numeric value of the error.

Description (string) --
The description of the error.





RecordTags (list) --
One or more tags.

(dict) --
Information about a tag, which is a key-value pair.

Key (string) --
The key for this tag.

Value (string) --
The value for this tag.













Exceptions

ServiceCatalog.Client.exceptions.InvalidParametersException
ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.DuplicateResourceException


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

def reject_portfolio_share(AcceptLanguage=None, PortfolioId=None, PortfolioShareType=None):
    """
    Rejects an offer to share the specified portfolio.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.reject_portfolio_share(
        AcceptLanguage='string',
        PortfolioId='string',
        PortfolioShareType='IMPORTED'|'AWS_SERVICECATALOG'|'AWS_ORGANIZATIONS'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type PortfolioId: string
    :param PortfolioId: [REQUIRED]\nThe portfolio identifier.\n

    :type PortfolioShareType: string
    :param PortfolioShareType: The type of shared portfolios to reject. The default is to reject imported portfolios.\n\nAWS_ORGANIZATIONS - Reject portfolios shared by the master account of your organization.\nIMPORTED - Reject imported portfolios.\nAWS_SERVICECATALOG - Not supported. (Throws ResourceNotFoundException.)\n\nFor example, aws servicecatalog reject-portfolio-share --portfolio-id 'port-2qwzkwxt3y5fk' --portfolio-share-type AWS_ORGANIZATIONS\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException


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
    
    Exceptions
    
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
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type AccessLevelFilter: dict
    :param AccessLevelFilter: The access level to use to obtain results. The default is User .\n\nKey (string) --The access level.\n\nAccount - Filter results based on the account.\nRole - Filter results based on the federated role of the specified user.\nUser - Filter results based on the specified user.\n\n\nValue (string) --The user to which the access level applies. The only supported value is Self .\n\n\n

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :rtype: dict

ReturnsResponse Syntax
{
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
            'ProductId': 'string',
            'ProvisioningArtifactId': 'string'
        },
    ],
    'NextPageToken': 'string'
}


Response Structure

(dict) --

ProvisionedProducts (list) --
Information about the provisioned products.

(dict) --
Information about a provisioned product.

Name (string) --
The user-friendly name of the provisioned product.

Arn (string) --
The ARN of the provisioned product.

Type (string) --
The type of provisioned product. The supported values are CFN_STACK and CFN_STACKSET .

Id (string) --
The identifier of the provisioned product.

Status (string) --
The current status of the provisioned product.

AVAILABLE - Stable state, ready to perform any operation. The most recent operation succeeded and completed.
UNDER_CHANGE - Transitive state. Operations performed might not have valid results. Wait for an AVAILABLE status before performing operations.
TAINTED - Stable state, ready to perform any operation. The stack has completed the requested operation but is not exactly what was requested. For example, a request to update to a new version failed and the stack rolled back to the current version.
ERROR - An unexpected error occurred. The provisioned product exists but the stack is not running. For example, CloudFormation received a parameter value that was not valid and could not launch the stack.
PLAN_IN_PROGRESS - Transitive state. The plan operations were performed to provision a new product, but resources have not yet been created. After reviewing the list of resources to be created, execute the plan. Wait for an AVAILABLE status before performing operations.


StatusMessage (string) --
The current status message of the provisioned product.

CreatedTime (datetime) --
The UTC time stamp of the creation time.

IdempotencyToken (string) --
A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.

LastRecordId (string) --
The record identifier of the last request performed on this provisioned product.

ProductId (string) --
The product identifier. For example, prod-abcdzk7xy33qa .

ProvisioningArtifactId (string) --
The identifier of the provisioning artifact. For example, pa-4abcdjnxjj6ne .





NextPageToken (string) --
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.







Exceptions

ServiceCatalog.Client.exceptions.InvalidParametersException


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
                'ProductId': 'string',
                'ProvisioningArtifactId': 'string'
            },
        ],
        'NextPageToken': 'string'
    }
    
    
    :returns: 
    AVAILABLE - Stable state, ready to perform any operation. The most recent operation succeeded and completed.
    UNDER_CHANGE - Transitive state. Operations performed might not have valid results. Wait for an AVAILABLE status before performing operations.
    TAINTED - Stable state, ready to perform any operation. The stack has completed the requested operation but is not exactly what was requested. For example, a request to update to a new version failed and the stack rolled back to the current version.
    ERROR - An unexpected error occurred. The provisioned product exists but the stack is not running. For example, CloudFormation received a parameter value that was not valid and could not launch the stack.
    PLAN_IN_PROGRESS - Transitive state. The plan operations were performed to provision a new product, but resources have not yet been created. After reviewing the list of resources to be created, execute the plan. Wait for an AVAILABLE status before performing operations.
    
    """
    pass

def search_products(AcceptLanguage=None, Filters=None, PageSize=None, SortBy=None, SortOrder=None, PageToken=None):
    """
    Gets information about the products to which the caller has access.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type Filters: dict
    :param Filters: The search filters. If no search filters are specified, the output includes all products to which the caller has access.\n\n(string) --\n(list) --\n(string) --\n\n\n\n\n\n

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :type SortBy: string
    :param SortBy: The sort field. If no value is specified, the results are not sorted.

    :type SortOrder: string
    :param SortOrder: The sort order. If no value is specified, the results are not sorted.

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

ProductViewSummaries (list) --
Information about the product views.

(dict) --
Summary information about a product view.

Id (string) --
The product view identifier.

ProductId (string) --
The product identifier.

Name (string) --
The name of the product.

Owner (string) --
The owner of the product. Contact the product administrator for the significance of this value.

ShortDescription (string) --
Short description of the product.

Type (string) --
The product type. Contact the product administrator for the significance of this value. If this value is MARKETPLACE , the product was created by AWS Marketplace.

Distributor (string) --
The distributor of the product. Contact the product administrator for the significance of this value.

HasDefaultPath (boolean) --
Indicates whether the product has a default path. If the product does not have a default path, call  ListLaunchPaths to disambiguate between paths. Otherwise,  ListLaunchPaths is not required, and the output of  ProductViewSummary can be used directly with  DescribeProvisioningParameters .

SupportEmail (string) --
The email contact information to obtain support for this Product.

SupportDescription (string) --
The description of the support for this Product.

SupportUrl (string) --
The URL information to obtain support for this Product.





ProductViewAggregations (dict) --
The product view aggregations.

(string) --

(list) --

(dict) --
A single product view aggregation value/count pair, containing metadata about each product to which the calling user has access.

Value (string) --
The value of the product view aggregation.

ApproximateCount (integer) --
An approximate count of the products that match the value.









NextPageToken (string) --
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.







Exceptions

ServiceCatalog.Client.exceptions.InvalidParametersException


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
    
    
    :returns: 
    ServiceCatalog.Client.exceptions.InvalidParametersException
    
    """
    pass

def search_products_as_admin(AcceptLanguage=None, PortfolioId=None, Filters=None, SortBy=None, SortOrder=None, PageToken=None, PageSize=None, ProductSource=None):
    """
    Gets information about the products for the specified portfolio or all products.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type PortfolioId: string
    :param PortfolioId: The portfolio identifier.

    :type Filters: dict
    :param Filters: The search filters. If no search filters are specified, the output includes all products to which the administrator has access.\n\n(string) --\n(list) --\n(string) --\n\n\n\n\n\n

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

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

ProductViewDetails (list) --
Information about the product views.

(dict) --
Information about a product view.

ProductViewSummary (dict) --
Summary information about the product view.

Id (string) --
The product view identifier.

ProductId (string) --
The product identifier.

Name (string) --
The name of the product.

Owner (string) --
The owner of the product. Contact the product administrator for the significance of this value.

ShortDescription (string) --
Short description of the product.

Type (string) --
The product type. Contact the product administrator for the significance of this value. If this value is MARKETPLACE , the product was created by AWS Marketplace.

Distributor (string) --
The distributor of the product. Contact the product administrator for the significance of this value.

HasDefaultPath (boolean) --
Indicates whether the product has a default path. If the product does not have a default path, call  ListLaunchPaths to disambiguate between paths. Otherwise,  ListLaunchPaths is not required, and the output of  ProductViewSummary can be used directly with  DescribeProvisioningParameters .

SupportEmail (string) --
The email contact information to obtain support for this Product.

SupportDescription (string) --
The description of the support for this Product.

SupportUrl (string) --
The URL information to obtain support for this Product.



Status (string) --
The status of the product.

AVAILABLE - The product is ready for use.
CREATING - Product creation has started; the product is not ready for use.
FAILED - An action failed.


ProductARN (string) --
The ARN of the product.

CreatedTime (datetime) --
The UTC time stamp of the creation time.





NextPageToken (string) --
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.







Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.InvalidParametersException


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
    
    Exceptions
    
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
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type AccessLevelFilter: dict
    :param AccessLevelFilter: The access level to use to obtain results. The default is User .\n\nKey (string) --The access level.\n\nAccount - Filter results based on the account.\nRole - Filter results based on the federated role of the specified user.\nUser - Filter results based on the specified user.\n\n\nValue (string) --The user to which the access level applies. The only supported value is Self .\n\n\n

    :type Filters: dict
    :param Filters: The search filters.\nWhen the key is SearchQuery , the searchable fields are arn , createdTime , id , lastRecordId , idempotencyToken , name , physicalId , productId , provisioningArtifact , type , status , tags , userArn , and userArnSession .\nExample: 'SearchQuery':['status:AVAILABLE']\n\n(string) --\n(list) --\n(string) --\n\n\n\n\n\n

    :type SortBy: string
    :param SortBy: The sort field. If no value is specified, the results are not sorted. The valid values are arn , id , name , and lastRecordId .

    :type SortOrder: string
    :param SortOrder: The sort order. If no value is specified, the results are not sorted.

    :type PageSize: integer
    :param PageSize: The maximum number of items to return with this call.

    :type PageToken: string
    :param PageToken: The page token for the next set of results. To retrieve the first set of results, use null.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

ProvisionedProducts (list) --
Information about the provisioned products.

(dict) --
Information about a provisioned product.

Name (string) --
The user-friendly name of the provisioned product.

Arn (string) --
The ARN of the provisioned product.

Type (string) --
The type of provisioned product. The supported values are CFN_STACK and CFN_STACKSET .

Id (string) --
The identifier of the provisioned product.

Status (string) --
The current status of the provisioned product.

AVAILABLE - Stable state, ready to perform any operation. The most recent operation succeeded and completed.
UNDER_CHANGE - Transitive state. Operations performed might not have valid results. Wait for an AVAILABLE status before performing operations.
TAINTED - Stable state, ready to perform any operation. The stack has completed the requested operation but is not exactly what was requested. For example, a request to update to a new version failed and the stack rolled back to the current version.
ERROR - An unexpected error occurred. The provisioned product exists but the stack is not running. For example, CloudFormation received a parameter value that was not valid and could not launch the stack.
PLAN_IN_PROGRESS - Transitive state. The plan operations were performed to provision a new product, but resources have not yet been created. After reviewing the list of resources to be created, execute the plan. Wait for an AVAILABLE status before performing operations.


StatusMessage (string) --
The current status message of the provisioned product.

CreatedTime (datetime) --
The UTC time stamp of the creation time.

IdempotencyToken (string) --
A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.

LastRecordId (string) --
The record identifier of the last request performed on this provisioned product.

Tags (list) --
One or more tags.

(dict) --
Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.

Key (string) --
The tag key.

Value (string) --
The value for this key.





PhysicalId (string) --
The assigned identifier for the resource, such as an EC2 instance ID or an S3 bucket name.

ProductId (string) --
The product identifier.

ProvisioningArtifactId (string) --
The identifier of the provisioning artifact.

UserArn (string) --
The Amazon Resource Name (ARN) of the IAM user.

UserArnSession (string) --
The ARN of the IAM user in the session. This ARN might contain a session ID.





TotalResultsCount (integer) --
The number of provisioned products found.

NextPageToken (string) --
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.







Exceptions

ServiceCatalog.Client.exceptions.InvalidParametersException


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
    UNDER_CHANGE - Transitive state. Operations performed might not have valid results. Wait for an AVAILABLE status before performing operations.
    TAINTED - Stable state, ready to perform any operation. The stack has completed the requested operation but is not exactly what was requested. For example, a request to update to a new version failed and the stack rolled back to the current version.
    ERROR - An unexpected error occurred. The provisioned product exists but the stack is not running. For example, CloudFormation received a parameter value that was not valid and could not launch the stack.
    PLAN_IN_PROGRESS - Transitive state. The plan operations were performed to provision a new product, but resources have not yet been created. After reviewing the list of resources to be created, execute the plan. Wait for an AVAILABLE status before performing operations.
    
    """
    pass

def terminate_provisioned_product(ProvisionedProductName=None, ProvisionedProductId=None, TerminateToken=None, IgnoreErrors=None, AcceptLanguage=None):
    """
    Terminates the specified provisioned product.
    This operation does not delete any records associated with the provisioned product.
    You can check the status of this request using  DescribeRecord .
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param TerminateToken: [REQUIRED]\nAn idempotency token that uniquely identifies the termination request. This token is only valid during the termination process. After the provisioned product is terminated, subsequent requests to terminate the same provisioned product always return ResourceNotFound .\nThis field is autopopulated if not provided.\n

    :type IgnoreErrors: boolean
    :param IgnoreErrors: If set to true, AWS Service Catalog stops managing the specified provisioned product even if it cannot delete the underlying resources.

    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

RecordDetail (dict) --
Information about the result of this request.

RecordId (string) --
The identifier of the record.

ProvisionedProductName (string) --
The user-friendly name of the provisioned product.

Status (string) --
The status of the provisioned product.

CREATED - The request was created but the operation has not started.
IN_PROGRESS - The requested operation is in progress.
IN_PROGRESS_IN_ERROR - The provisioned product is under change but the requested operation failed and some remediation is occurring. For example, a rollback.
SUCCEEDED - The requested operation has successfully completed.
FAILED - The requested operation has unsuccessfully completed. Investigate using the error messages returned.


CreatedTime (datetime) --
The UTC time stamp of the creation time.

UpdatedTime (datetime) --
The time when the record was last updated.

ProvisionedProductType (string) --
The type of provisioned product. The supported values are CFN_STACK and CFN_STACKSET .

RecordType (string) --
The record type.

PROVISION_PRODUCT
UPDATE_PROVISIONED_PRODUCT
TERMINATE_PROVISIONED_PRODUCT


ProvisionedProductId (string) --
The identifier of the provisioned product.

ProductId (string) --
The product identifier.

ProvisioningArtifactId (string) --
The identifier of the provisioning artifact.

PathId (string) --
The path identifier.

RecordErrors (list) --
The errors that occurred.

(dict) --
The error code and description resulting from an operation.

Code (string) --
The numeric value of the error.

Description (string) --
The description of the error.





RecordTags (list) --
One or more tags.

(dict) --
Information about a tag, which is a key-value pair.

Key (string) --
The key for this tag.

Value (string) --
The value for this tag.













Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException


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

def update_constraint(AcceptLanguage=None, Id=None, Description=None, Parameters=None):
    """
    Updates the specified constraint.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_constraint(
        AcceptLanguage='string',
        Id='string',
        Description='string',
        Parameters='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type Id: string
    :param Id: [REQUIRED]\nThe identifier of the constraint.\n

    :type Description: string
    :param Description: The updated description of the constraint.

    :type Parameters: string
    :param Parameters: The constraint parameters, in JSON format. The syntax depends on the constraint type as follows:\n\nLAUNCH\nYou are required to specify either the RoleArn or the LocalRoleName but can\'t use both.\nSpecify the RoleArn property as follows:\n\n{'RoleArn' : 'arn:aws:iam::123456789012:role/LaunchRole'}\nSpecify the LocalRoleName property as follows:\n\n{'LocalRoleName': 'SCBasicLaunchRole'}\nIf you specify the LocalRoleName property, when an account uses the launch constraint, the IAM role with that name in the account will be used. This allows launch-role constraints to be account-agnostic so the administrator can create fewer resources per shared account.\n\nNote\nThe given role name must exist in the account used to create the launch constraint and the account of the user who launches a product with this launch constraint.\n\nYou cannot have both a LAUNCH and a STACKSET constraint.\nYou also cannot have more than one LAUNCH constraint on a product and portfolio.\n\nNOTIFICATION\nSpecify the NotificationArns property as follows:\n\n{'NotificationArns' : ['arn:aws:sns:us-east-1:123456789012:Topic']}\nRESOURCE_UPDATE\n\nSpecify the TagUpdatesOnProvisionedProduct property as follows:\n\n{'Version':'2.0','Properties':{'TagUpdateOnProvisionedProduct':'String'}}\nThe TagUpdatesOnProvisionedProduct property accepts a string value of ALLOWED or NOT_ALLOWED .\n\nSTACKSET\nSpecify the Parameters property as follows:\n\n{'Version': 'String', 'Properties': {'AccountList': [ 'String' ], 'RegionList': [ 'String' ], 'AdminRole': 'String', 'ExecutionRole': 'String'}}\nYou cannot have both a LAUNCH and a STACKSET constraint.\nYou also cannot have more than one STACKSET constraint on a product and portfolio.\nProducts with a STACKSET constraint will launch an AWS CloudFormation stack set.\n\nTEMPLATE\nSpecify the Rules property. For more information, see Template Constraint Rules .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ConstraintDetail': {
        'ConstraintId': 'string',
        'Type': 'string',
        'Description': 'string',
        'Owner': 'string',
        'ProductId': 'string',
        'PortfolioId': 'string'
    },
    'ConstraintParameters': 'string',
    'Status': 'AVAILABLE'|'CREATING'|'FAILED'
}


Response Structure

(dict) --

ConstraintDetail (dict) --
Information about the constraint.

ConstraintId (string) --
The identifier of the constraint.

Type (string) --
The type of constraint.

LAUNCH
NOTIFICATION
STACKSET
TEMPLATE


Description (string) --
The description of the constraint.

Owner (string) --
The owner of the constraint.

ProductId (string) --
The identifier of the product the constraint applies to. Note that a constraint applies to a specific instance of a product within a certain portfolio.

PortfolioId (string) --
The identifier of the portfolio the product resides in. The constraint applies only to the instance of the product that lives within this portfolio.



ConstraintParameters (string) --
The constraint parameters.

Status (string) --
The status of the current request.







Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.InvalidParametersException


    :return: {
        'ConstraintDetail': {
            'ConstraintId': 'string',
            'Type': 'string',
            'Description': 'string',
            'Owner': 'string',
            'ProductId': 'string',
            'PortfolioId': 'string'
        },
        'ConstraintParameters': 'string',
        'Status': 'AVAILABLE'|'CREATING'|'FAILED'
    }
    
    
    :returns: 
    LAUNCH
    NOTIFICATION
    STACKSET
    TEMPLATE
    
    """
    pass

def update_portfolio(AcceptLanguage=None, Id=None, DisplayName=None, Description=None, ProviderName=None, AddTags=None, RemoveTags=None):
    """
    Updates the specified portfolio.
    You cannot update a product that was shared with you.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type Id: string
    :param Id: [REQUIRED]\nThe portfolio identifier.\n

    :type DisplayName: string
    :param DisplayName: The name to use for display purposes.

    :type Description: string
    :param Description: The updated description of the portfolio.

    :type ProviderName: string
    :param ProviderName: The updated name of the portfolio provider.

    :type AddTags: list
    :param AddTags: The tags to add.\n\n(dict) --Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.\n\nKey (string) -- [REQUIRED]The tag key.\n\nValue (string) -- [REQUIRED]The value for this key.\n\n\n\n\n

    :type RemoveTags: list
    :param RemoveTags: The tags to remove.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

PortfolioDetail (dict) --
Information about the portfolio.

Id (string) --
The portfolio identifier.

ARN (string) --
The ARN assigned to the portfolio.

DisplayName (string) --
The name to use for display purposes.

Description (string) --
The description of the portfolio.

CreatedTime (datetime) --
The UTC time stamp of the creation time.

ProviderName (string) --
The name of the portfolio provider.



Tags (list) --
Information about the tags associated with the portfolio.

(dict) --
Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.

Key (string) --
The tag key.

Value (string) --
The value for this key.











Exceptions

ServiceCatalog.Client.exceptions.InvalidParametersException
ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.LimitExceededException
ServiceCatalog.Client.exceptions.TagOptionNotMigratedException


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
    
    
    :returns: 
    ServiceCatalog.Client.exceptions.InvalidParametersException
    ServiceCatalog.Client.exceptions.ResourceNotFoundException
    ServiceCatalog.Client.exceptions.LimitExceededException
    ServiceCatalog.Client.exceptions.TagOptionNotMigratedException
    
    """
    pass

def update_product(AcceptLanguage=None, Id=None, Name=None, Owner=None, Description=None, Distributor=None, SupportDescription=None, SupportEmail=None, SupportUrl=None, AddTags=None, RemoveTags=None):
    """
    Updates the specified product.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type Id: string
    :param Id: [REQUIRED]\nThe product identifier.\n

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
    :param AddTags: The tags to add to the product.\n\n(dict) --Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.\n\nKey (string) -- [REQUIRED]The tag key.\n\nValue (string) -- [REQUIRED]The value for this key.\n\n\n\n\n

    :type RemoveTags: list
    :param RemoveTags: The tags to remove from the product.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

ProductViewDetail (dict) --
Information about the product view.

ProductViewSummary (dict) --
Summary information about the product view.

Id (string) --
The product view identifier.

ProductId (string) --
The product identifier.

Name (string) --
The name of the product.

Owner (string) --
The owner of the product. Contact the product administrator for the significance of this value.

ShortDescription (string) --
Short description of the product.

Type (string) --
The product type. Contact the product administrator for the significance of this value. If this value is MARKETPLACE , the product was created by AWS Marketplace.

Distributor (string) --
The distributor of the product. Contact the product administrator for the significance of this value.

HasDefaultPath (boolean) --
Indicates whether the product has a default path. If the product does not have a default path, call  ListLaunchPaths to disambiguate between paths. Otherwise,  ListLaunchPaths is not required, and the output of  ProductViewSummary can be used directly with  DescribeProvisioningParameters .

SupportEmail (string) --
The email contact information to obtain support for this Product.

SupportDescription (string) --
The description of the support for this Product.

SupportUrl (string) --
The URL information to obtain support for this Product.



Status (string) --
The status of the product.

AVAILABLE - The product is ready for use.
CREATING - Product creation has started; the product is not ready for use.
FAILED - An action failed.


ProductARN (string) --
The ARN of the product.

CreatedTime (datetime) --
The UTC time stamp of the creation time.



Tags (list) --
Information about the tags associated with the product.

(dict) --
Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.

Key (string) --
The tag key.

Value (string) --
The value for this key.











Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.InvalidParametersException
ServiceCatalog.Client.exceptions.TagOptionNotMigratedException


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

def update_provisioned_product(AcceptLanguage=None, ProvisionedProductName=None, ProvisionedProductId=None, ProductId=None, ProvisioningArtifactId=None, PathId=None, ProvisioningParameters=None, ProvisioningPreferences=None, Tags=None, UpdateToken=None):
    """
    Requests updates to the configuration of the specified provisioned product.
    If there are tags associated with the object, they cannot be updated or added. Depending on the specific updates requested, this operation can update with no interruption, with some interruption, or replace the provisioned product entirely.
    You can check the status of this request using  DescribeRecord .
    See also: AWS API Documentation
    
    Exceptions
    
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
        ProvisioningPreferences={
            'StackSetAccounts': [
                'string',
            ],
            'StackSetRegions': [
                'string',
            ],
            'StackSetFailureToleranceCount': 123,
            'StackSetFailureTolerancePercentage': 123,
            'StackSetMaxConcurrencyCount': 123,
            'StackSetMaxConcurrencyPercentage': 123,
            'StackSetOperationType': 'CREATE'|'UPDATE'|'DELETE'
        },
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        UpdateToken='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type ProvisionedProductName: string
    :param ProvisionedProductName: The name of the provisioned product. You cannot specify both ProvisionedProductName and ProvisionedProductId .

    :type ProvisionedProductId: string
    :param ProvisionedProductId: The identifier of the provisioned product. You cannot specify both ProvisionedProductName and ProvisionedProductId .

    :type ProductId: string
    :param ProductId: The identifier of the product.

    :type ProvisioningArtifactId: string
    :param ProvisioningArtifactId: The identifier of the provisioning artifact.

    :type PathId: string
    :param PathId: The new path identifier. This value is optional if the product has a default path, and required if the product has more than one path.

    :type ProvisioningParameters: list
    :param ProvisioningParameters: The new parameters.\n\n(dict) --The parameter key-value pair used to update a provisioned product.\n\nKey (string) --The parameter key.\n\nValue (string) --The parameter value.\n\nUsePreviousValue (boolean) --If set to true, Value is ignored and the previous parameter value is kept.\n\n\n\n\n

    :type ProvisioningPreferences: dict
    :param ProvisioningPreferences: An object that contains information about the provisioning preferences for a stack set.\n\nStackSetAccounts (list) --One or more AWS accounts that will have access to the provisioned product.\nApplicable only to a CFN_STACKSET provisioned product type.\nThe AWS accounts specified should be within the list of accounts in the STACKSET constraint. To get the list of accounts in the STACKSET constraint, use the DescribeProvisioningParameters operation.\nIf no values are specified, the default value is all accounts from the STACKSET constraint.\n\n(string) --\n\n\nStackSetRegions (list) --One or more AWS Regions where the provisioned product will be available.\nApplicable only to a CFN_STACKSET provisioned product type.\nThe specified regions should be within the list of regions from the STACKSET constraint. To get the list of regions in the STACKSET constraint, use the DescribeProvisioningParameters operation.\nIf no values are specified, the default value is all regions from the STACKSET constraint.\n\n(string) --\n\n\nStackSetFailureToleranceCount (integer) --The number of accounts, per region, for which this operation can fail before AWS Service Catalog stops the operation in that region. If the operation is stopped in a region, AWS Service Catalog doesn\'t attempt the operation in any subsequent regions.\nApplicable only to a CFN_STACKSET provisioned product type.\nConditional: You must specify either StackSetFailureToleranceCount or StackSetFailureTolerancePercentage , but not both.\nThe default value is 0 if no value is specified.\n\nStackSetFailureTolerancePercentage (integer) --The percentage of accounts, per region, for which this stack operation can fail before AWS Service Catalog stops the operation in that region. If the operation is stopped in a region, AWS Service Catalog doesn\'t attempt the operation in any subsequent regions.\nWhen calculating the number of accounts based on the specified percentage, AWS Service Catalog rounds down to the next whole number.\nApplicable only to a CFN_STACKSET provisioned product type.\nConditional: You must specify either StackSetFailureToleranceCount or StackSetFailureTolerancePercentage , but not both.\n\nStackSetMaxConcurrencyCount (integer) --The maximum number of accounts in which to perform this operation at one time. This is dependent on the value of StackSetFailureToleranceCount . StackSetMaxConcurrentCount is at most one more than the StackSetFailureToleranceCount .\nNote that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.\nApplicable only to a CFN_STACKSET provisioned product type.\nConditional: You must specify either StackSetMaxConcurrentCount or StackSetMaxConcurrentPercentage , but not both.\n\nStackSetMaxConcurrencyPercentage (integer) --The maximum percentage of accounts in which to perform this operation at one time.\nWhen calculating the number of accounts based on the specified percentage, AWS Service Catalog rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, AWS Service Catalog sets the number as 1 instead.\nNote that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.\nApplicable only to a CFN_STACKSET provisioned product type.\nConditional: You must specify either StackSetMaxConcurrentCount or StackSetMaxConcurrentPercentage , but not both.\n\nStackSetOperationType (string) --Determines what action AWS Service Catalog performs to a stack set or a stack instance represented by the provisioned product. The default value is UPDATE if nothing is specified.\nApplicable only to a CFN_STACKSET provisioned product type.\n\nCREATE\nCreates a new stack instance in the stack set represented by the provisioned product. In this case, only new stack instances are created based on accounts and regions; if new ProductId or ProvisioningArtifactID are passed, they will be ignored.\n\nUPDATE\nUpdates the stack set represented by the provisioned product and also its stack instances.\n\nDELETE\nDeletes a stack instance in the stack set represented by the provisioned product.\n\n\n

    :type Tags: list
    :param Tags: One or more tags. Requires the product to have RESOURCE_UPDATE constraint with TagUpdatesOnProvisionedProduct set to ALLOWED to allow tag updates.\n\n(dict) --Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.\n\nKey (string) -- [REQUIRED]The tag key.\n\nValue (string) -- [REQUIRED]The value for this key.\n\n\n\n\n

    :type UpdateToken: string
    :param UpdateToken: [REQUIRED]\nThe idempotency token that uniquely identifies the provisioning update request.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

RecordDetail (dict) --
Information about the result of the request.

RecordId (string) --
The identifier of the record.

ProvisionedProductName (string) --
The user-friendly name of the provisioned product.

Status (string) --
The status of the provisioned product.

CREATED - The request was created but the operation has not started.
IN_PROGRESS - The requested operation is in progress.
IN_PROGRESS_IN_ERROR - The provisioned product is under change but the requested operation failed and some remediation is occurring. For example, a rollback.
SUCCEEDED - The requested operation has successfully completed.
FAILED - The requested operation has unsuccessfully completed. Investigate using the error messages returned.


CreatedTime (datetime) --
The UTC time stamp of the creation time.

UpdatedTime (datetime) --
The time when the record was last updated.

ProvisionedProductType (string) --
The type of provisioned product. The supported values are CFN_STACK and CFN_STACKSET .

RecordType (string) --
The record type.

PROVISION_PRODUCT
UPDATE_PROVISIONED_PRODUCT
TERMINATE_PROVISIONED_PRODUCT


ProvisionedProductId (string) --
The identifier of the provisioned product.

ProductId (string) --
The product identifier.

ProvisioningArtifactId (string) --
The identifier of the provisioning artifact.

PathId (string) --
The path identifier.

RecordErrors (list) --
The errors that occurred.

(dict) --
The error code and description resulting from an operation.

Code (string) --
The numeric value of the error.

Description (string) --
The description of the error.





RecordTags (list) --
One or more tags.

(dict) --
Information about a tag, which is a key-value pair.

Key (string) --
The key for this tag.

Value (string) --
The value for this tag.













Exceptions

ServiceCatalog.Client.exceptions.InvalidParametersException
ServiceCatalog.Client.exceptions.ResourceNotFoundException


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

def update_provisioned_product_properties(AcceptLanguage=None, ProvisionedProductId=None, ProvisionedProductProperties=None, IdempotencyToken=None):
    """
    Requests updates to the properties of the specified provisioned product.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_provisioned_product_properties(
        AcceptLanguage='string',
        ProvisionedProductId='string',
        ProvisionedProductProperties={
            'string': 'string'
        },
        IdempotencyToken='string'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type ProvisionedProductId: string
    :param ProvisionedProductId: [REQUIRED]\nThe identifier of the provisioned product.\n

    :type ProvisionedProductProperties: dict
    :param ProvisionedProductProperties: [REQUIRED]\nA map that contains the provisioned product properties to be updated.\nThe OWNER key only accepts user ARNs. The owner is the user that is allowed to see, update, terminate, and execute service actions in the provisioned product.\nThe administrator can change the owner of a provisioned product to another IAM user within the same account. Both end user owners and administrators can see ownership history of the provisioned product using the ListRecordHistory API. The new owner can describe all past records for the provisioned product using the DescribeRecord API. The previous owner can no longer use DescribeRecord , but can still see the product\'s history from when he was an owner using ListRecordHistory .\nIf a provisioned product ownership is assigned to an end user, they can see and perform any action through the API or Service Catalog console such as update, terminate, and execute service actions. If an end user provisions a product and the owner is updated to someone else, they will no longer be able to see or perform any actions through API or the Service Catalog console on that provisioned product.\n\n(string) --\n(string) --\n\n\n\n

    :type IdempotencyToken: string
    :param IdempotencyToken: [REQUIRED]\nThe idempotency token that uniquely identifies the provisioning product update request.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ProvisionedProductId': 'string',
    'ProvisionedProductProperties': {
        'string': 'string'
    },
    'RecordId': 'string',
    'Status': 'CREATED'|'IN_PROGRESS'|'IN_PROGRESS_IN_ERROR'|'SUCCEEDED'|'FAILED'
}


Response Structure

(dict) --

ProvisionedProductId (string) --
The provisioned product identifier.

ProvisionedProductProperties (dict) --
A map that contains the properties updated.

(string) --
(string) --




RecordId (string) --
The identifier of the record.

Status (string) --
The status of the request.







Exceptions

ServiceCatalog.Client.exceptions.InvalidParametersException
ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.InvalidStateException


    :return: {
        'ProvisionedProductId': 'string',
        'ProvisionedProductProperties': {
            'string': 'string'
        },
        'RecordId': 'string',
        'Status': 'CREATED'|'IN_PROGRESS'|'IN_PROGRESS_IN_ERROR'|'SUCCEEDED'|'FAILED'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def update_provisioning_artifact(AcceptLanguage=None, ProductId=None, ProvisioningArtifactId=None, Name=None, Description=None, Active=None, Guidance=None):
    """
    Updates the specified provisioning artifact (also known as a version) for the specified product.
    You cannot update a provisioning artifact for a product that was shared with you.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_provisioning_artifact(
        AcceptLanguage='string',
        ProductId='string',
        ProvisioningArtifactId='string',
        Name='string',
        Description='string',
        Active=True|False,
        Guidance='DEFAULT'|'DEPRECATED'
    )
    
    
    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :type ProductId: string
    :param ProductId: [REQUIRED]\nThe product identifier.\n

    :type ProvisioningArtifactId: string
    :param ProvisioningArtifactId: [REQUIRED]\nThe identifier of the provisioning artifact.\n

    :type Name: string
    :param Name: The updated name of the provisioning artifact.

    :type Description: string
    :param Description: The updated description of the provisioning artifact.

    :type Active: boolean
    :param Active: Indicates whether the product version is active.\nInactive provisioning artifacts are invisible to end users. End users cannot launch or update a provisioned product from an inactive provisioning artifact.\n

    :type Guidance: string
    :param Guidance: Information set by the administrator to provide guidance to end users about which provisioning artifacts to use.\nThe DEFAULT value indicates that the product version is active.\nThe administrator can set the guidance to DEPRECATED to inform users that the product version is deprecated. Users are able to make updates to a provisioned product of a deprecated version but cannot launch new provisioned products using a deprecated version.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ProvisioningArtifactDetail': {
        'Id': 'string',
        'Name': 'string',
        'Description': 'string',
        'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE_AMI'|'MARKETPLACE_CAR',
        'CreatedTime': datetime(2015, 1, 1),
        'Active': True|False,
        'Guidance': 'DEFAULT'|'DEPRECATED'
    },
    'Info': {
        'string': 'string'
    },
    'Status': 'AVAILABLE'|'CREATING'|'FAILED'
}


Response Structure

(dict) --

ProvisioningArtifactDetail (dict) --
Information about the provisioning artifact.

Id (string) --
The identifier of the provisioning artifact.

Name (string) --
The name of the provisioning artifact.

Description (string) --
The description of the provisioning artifact.

Type (string) --
The type of provisioning artifact.

CLOUD_FORMATION_TEMPLATE - AWS CloudFormation template
MARKETPLACE_AMI - AWS Marketplace AMI
MARKETPLACE_CAR - AWS Marketplace Clusters and AWS Resources


CreatedTime (datetime) --
The UTC time stamp of the creation time.

Active (boolean) --
Indicates whether the product version is active.

Guidance (string) --
Information set by the administrator to provide guidance to end users about which provisioning artifacts to use.



Info (dict) --
The URL of the CloudFormation template in Amazon S3.

(string) --
(string) --




Status (string) --
The status of the current request.







Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.InvalidParametersException


    :return: {
        'ProvisioningArtifactDetail': {
            'Id': 'string',
            'Name': 'string',
            'Description': 'string',
            'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE_AMI'|'MARKETPLACE_CAR',
            'CreatedTime': datetime(2015, 1, 1),
            'Active': True|False,
            'Guidance': 'DEFAULT'|'DEPRECATED'
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

def update_service_action(Id=None, Name=None, Definition=None, Description=None, AcceptLanguage=None):
    """
    Updates a self-service action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_service_action(
        Id='string',
        Name='string',
        Definition={
            'string': 'string'
        },
        Description='string',
        AcceptLanguage='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe self-service action identifier.\n

    :type Name: string
    :param Name: The self-service action name.

    :type Definition: dict
    :param Definition: A map that defines the self-service action.\n\n(string) --\n(string) --\n\n\n\n

    :type Description: string
    :param Description: The self-service action description.

    :type AcceptLanguage: string
    :param AcceptLanguage: The language code.\n\nen - English (default)\njp - Japanese\nzh - Chinese\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ServiceActionDetail': {
        'ServiceActionSummary': {
            'Id': 'string',
            'Name': 'string',
            'Description': 'string',
            'DefinitionType': 'SSM_AUTOMATION'
        },
        'Definition': {
            'string': 'string'
        }
    }
}


Response Structure

(dict) --

ServiceActionDetail (dict) --
Detailed information about the self-service action.

ServiceActionSummary (dict) --
Summary information about the self-service action.

Id (string) --
The self-service action identifier.

Name (string) --
The self-service action name.

Description (string) --
The self-service action description.

DefinitionType (string) --
The self-service action definition type. For example, SSM_AUTOMATION .



Definition (dict) --
A map that defines the self-service action.

(string) --
(string) --












Exceptions

ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.InvalidParametersException


    :return: {
        'ServiceActionDetail': {
            'ServiceActionSummary': {
                'Id': 'string',
                'Name': 'string',
                'Description': 'string',
                'DefinitionType': 'SSM_AUTOMATION'
            },
            'Definition': {
                'string': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def update_tag_option(Id=None, Value=None, Active=None):
    """
    Updates the specified TagOption.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_tag_option(
        Id='string',
        Value='string',
        Active=True|False
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe TagOption identifier.\n

    :type Value: string
    :param Value: The updated value.

    :type Active: boolean
    :param Active: The updated active state.

    :rtype: dict

ReturnsResponse Syntax
{
    'TagOptionDetail': {
        'Key': 'string',
        'Value': 'string',
        'Active': True|False,
        'Id': 'string'
    }
}


Response Structure

(dict) --

TagOptionDetail (dict) --
Information about the TagOption.

Key (string) --
The TagOption key.

Value (string) --
The TagOption value.

Active (boolean) --
The TagOption active state.

Id (string) --
The TagOption identifier.









Exceptions

ServiceCatalog.Client.exceptions.TagOptionNotMigratedException
ServiceCatalog.Client.exceptions.ResourceNotFoundException
ServiceCatalog.Client.exceptions.DuplicateResourceException
ServiceCatalog.Client.exceptions.InvalidParametersException


    :return: {
        'TagOptionDetail': {
            'Key': 'string',
            'Value': 'string',
            'Active': True|False,
            'Id': 'string'
        }
    }
    
    
    :returns: 
    ServiceCatalog.Client.exceptions.TagOptionNotMigratedException
    ServiceCatalog.Client.exceptions.ResourceNotFoundException
    ServiceCatalog.Client.exceptions.DuplicateResourceException
    ServiceCatalog.Client.exceptions.InvalidParametersException
    
    """
    pass

