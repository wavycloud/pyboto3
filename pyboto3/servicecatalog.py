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


def describe_product(AcceptLanguage=None, Id=None):
    """
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            
    :type AcceptLanguage: string
    :param Id: [REQUIRED]
            The ProductId of the product to describe.
            
    :type Id: string
    """
    pass


def describe_product_view(AcceptLanguage=None, Id=None):
    """
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            
    :type AcceptLanguage: string
    :param Id: [REQUIRED]
            The ProductViewId of the product to describe.
            
    :type Id: string
    """
    pass


def describe_provisioning_parameters(AcceptLanguage=None, ProductId=None, ProvisioningArtifactId=None, PathId=None):
    """
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            
    :type AcceptLanguage: string
    :param ProductId: [REQUIRED]
            The identifier of the product.
            
    :type ProductId: string
    :param ProvisioningArtifactId: [REQUIRED]
            The provisioning artifact identifier for this product.
            
    :type ProvisioningArtifactId: string
    :param PathId: The identifier of the path for this product's provisioning. This value is optional if the product has a default path, and is required if there is more than one path for the specified product.
    :type PathId: string
    """
    pass


def describe_record(AcceptLanguage=None, Id=None, PageToken=None, PageSize=None):
    """
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            
    :type AcceptLanguage: string
    :param Id: [REQUIRED]
            The record identifier of the ProvisionedProduct object for which to retrieve output information. This is the RecordDetail.RecordId obtained from the request operation's response.
            
    :type Id: string
    :param PageToken: The page token of the first page retrieved. If null, this retrieves the first page of size PageSize .
    :type PageToken: string
    :param PageSize: The maximum number of items to return in the results. If more results exist than fit in the specified PageSize , the value of NextPageToken in the response is non-null.
    :type PageSize: integer
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


def list_launch_paths(AcceptLanguage=None, ProductId=None, PageSize=None, PageToken=None):
    """
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            
    :type AcceptLanguage: string
    :param ProductId: [REQUIRED]
            Identifies the product for which to retrieve LaunchPathSummaries information.
            
    :type ProductId: string
    :param PageSize: The maximum number of items to return in the results. If more results exist than fit in the specified PageSize , the value of NextPageToken in the response is non-null.
    :type PageSize: integer
    :param PageToken: The page token of the first page retrieved. If null, this retrieves the first page of size PageSize .
    :type PageToken: string
    """
    pass


def list_record_history(AcceptLanguage=None, AccessLevelFilter=None, SearchFilter=None, PageSize=None, PageToken=None):
    """
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            
    :type AcceptLanguage: string
    :param AccessLevelFilter: The access level for obtaining results. If left unspecified, User level access is used.
            Key (string) --Specifies the access level.
            Account allows results at the account level.Role allows results based on the federated role of the specified user.
            User allows results limited to the specified user.
            Value (string) --Specifies the user to which the access level applies. A value of Self is currently supported.
            
    :type AccessLevelFilter: dict
    :param SearchFilter: The filter to limit search results.
            Key (string) --The filter key.
            Value (string) --The filter value for Key .
            
    :type SearchFilter: dict
    :param PageSize: The maximum number of items to return in the results. If more results exist than fit in the specified PageSize , the value of NextPageToken in the response is non-null.
    :type PageSize: integer
    :param PageToken: The page token of the first page retrieved. If null, this retrieves the first page of size PageSize .
    :type PageToken: string
    """
    pass


def provision_product(AcceptLanguage=None, ProductId=None, ProvisioningArtifactId=None, PathId=None,
                      ProvisionedProductName=None, ProvisioningParameters=None, Tags=None, NotificationArns=None,
                      ProvisionToken=None):
    """
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            
    :type AcceptLanguage: string
    :param ProductId: [REQUIRED]
            The identifier of the product.
            
    :type ProductId: string
    :param ProvisioningArtifactId: [REQUIRED]
            The provisioning artifact identifier for this product.
            
    :type ProvisioningArtifactId: string
    :param PathId: The identifier of the path for this product's provisioning. This value is optional if the product has a default path, and is required if there is more than one path for the specified product.
    :type PathId: string
    :param ProvisionedProductName: [REQUIRED]
            A user-friendly name to identify the ProvisionedProduct object. This value must be unique for the AWS account and cannot be updated after the product is provisioned.
            
    :type ProvisionedProductName: string
    :param ProvisioningParameters: Parameters specified by the administrator that are required for provisioning the product.
            (dict) --The arameter key/value pairs used to provision a product.
            Key (string) --The ProvisioningArtifactParameter.ParameterKey parameter from DescribeProvisioningParameters .
            Value (string) --The value to use for provisioning. Any constraints on this value can be found in ProvisioningArtifactParameter for Key .
            
            
    :type ProvisioningParameters: list
    :param Tags: A list of tags to use as provisioning options.
            (dict) --Key/value pairs to associate with this provisioning. These tags are entirely discretionary and are propagated to the resources created in the provisioning.
            Key (string) --The ProvisioningArtifactParameter.TagKey parameter from DescribeProvisioningParameters .
            Value (string) --The esired value for this key.
            
            
    :type Tags: list
    :param NotificationArns: Passed to CloudFormation. The SNS topic ARNs to which to publish stack-related events.
            (string) --
            
    :type NotificationArns: list
    :param ProvisionToken: [REQUIRED]
            An idempotency token that uniquely identifies the provisioning request.
            
    :type ProvisionToken: string
    """
    pass


def scan_provisioned_products(AcceptLanguage=None, AccessLevelFilter=None, PageSize=None, PageToken=None):
    """
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            
    :type AcceptLanguage: string
    :param AccessLevelFilter: The access level for obtaining results. If left unspecified, User level access is used.
            Key (string) --Specifies the access level.
            Account allows results at the account level.Role allows results based on the federated role of the specified user.
            User allows results limited to the specified user.
            Value (string) --Specifies the user to which the access level applies. A value of Self is currently supported.
            
    :type AccessLevelFilter: dict
    :param PageSize: The maximum number of items to return in the results. If more results exist than fit in the specified PageSize , the value of NextPageToken in the response is non-null.
    :type PageSize: integer
    :param PageToken: The page token of the first page retrieved. If null, this retrieves the first page of size PageSize .
    :type PageToken: string
    """
    pass


def search_products(AcceptLanguage=None, Filters=None, PageSize=None, SortBy=None, SortOrder=None, PageToken=None):
    """
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            
    :type AcceptLanguage: string
    :param Filters: The list of filters with which to limit search results. If no search filters are specified, the output is all the products to which the calling user has access.
            (string) --
            (list) --
            (string) --
            
            
    :type Filters: dict
    :param PageSize: The maximum number of items to return in the results. If more results exist than fit in the specified PageSize , the value of NextPageToken in the response is non-null.
    :type PageSize: integer
    :param SortBy: The sort field specifier. If no value is specified, results are not sorted.
    :type SortBy: string
    :param SortOrder: The sort order specifier. If no value is specified, results are not sorted.
    :type SortOrder: string
    :param PageToken: The page token of the first page retrieved. If null, this retrieves the first page of size PageSize .
    :type PageToken: string
    """
    pass


def terminate_provisioned_product(ProvisionedProductName=None, ProvisionedProductId=None, TerminateToken=None,
                                  IgnoreErrors=None, AcceptLanguage=None):
    """
    :param ProvisionedProductName: The name of the ProvisionedProduct object to terminate. You must specify either ProvisionedProductName or ProvisionedProductId , but not both.
    :type ProvisionedProductName: string
    :param ProvisionedProductId: The identifier of the ProvisionedProduct object to terminate. You must specify either ProvisionedProductName or ProvisionedProductId , but not both.
    :type ProvisionedProductId: string
    :param TerminateToken: [REQUIRED]
            An idempotency token that uniquely identifies the termination request. This token is only valid during the termination process. After the ProvisionedProduct object is terminated, further requests to terminate the same ProvisionedProduct object always return ResourceNotFound regardless of the value of TerminateToken .
            
    :type TerminateToken: string
    :param IgnoreErrors: If set to true, AWS Service Catalog stops managing the specified ProvisionedProduct object even if it cannot delete the underlying resources.
    :type IgnoreErrors: boolean
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            
    :type AcceptLanguage: string
    """
    pass


def update_provisioned_product(AcceptLanguage=None, ProvisionedProductName=None, ProvisionedProductId=None,
                               ProductId=None, ProvisioningArtifactId=None, PathId=None, ProvisioningParameters=None,
                               UpdateToken=None):
    """
    :param AcceptLanguage: The language code to use for this operation. Supported language codes are as follows:
            'en' (English)
            'jp' (Japanese)
            'zh' (Chinese)
            If no code is specified, 'en' is used as the default.
            
    :type AcceptLanguage: string
    :param ProvisionedProductName: The updated name of the ProvisionedProduct object . You must specify either ProvisionedProductName or ProvisionedProductId , but not both.
    :type ProvisionedProductName: string
    :param ProvisionedProductId: The identifier of the ProvisionedProduct object to update. You must specify either ProvisionedProductName or ProvisionedProductId , but not both.
    :type ProvisionedProductId: string
    :param ProductId: The identifier of the ProvisionedProduct object.
    :type ProductId: string
    :param ProvisioningArtifactId: The provisioning artifact identifier for this product.
    :type ProvisioningArtifactId: string
    :param PathId: The identifier of the path to use in the updated ProvisionedProduct object. This value is optional if the product has a default path, and is required if there is more than one path for the specified product.
    :type PathId: string
    :param ProvisioningParameters: A list of ProvisioningParameter objects used to update the ProvisionedProduct object.
            (dict) --The parameter key/value pair used to update a ProvisionedProduct object. If UsePreviousValue is set to true, Value is ignored and the value for Key is kept as previously set (current value).
            Key (string) --The ProvisioningArtifactParameter.ParameterKey parameter from DescribeProvisioningParameters .
            Value (string) --The value to use for updating the product provisioning. Any constraints on this value can be found in the ProvisioningArtifactParameter parameter for Key .
            UsePreviousValue (boolean) --If true, uses the currently set value for Key , ignoring UpdateProvisioningParameter.Value .
            
            
    :type ProvisioningParameters: list
    :param UpdateToken: [REQUIRED]
            The idempotency token that uniquely identifies the provisioning update request.
            
    :type UpdateToken: string
    """
    pass
