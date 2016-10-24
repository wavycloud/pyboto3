'''

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

'''

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

def describe_product(AcceptLanguage=None, Id=None):
    """
    Retrieves information about a specified product.
    This operation is functionally identical to  DescribeProductView except that it takes as input ProductId instead of ProductViewId .
    
    
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
            'Type': 'string',
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

def describe_product_view(AcceptLanguage=None, Id=None):
    """
    Retrieves information about a specified product.
    This operation is functionally identical to  DescribeProduct except that it takes as input ProductViewId instead of ProductId .
    
    
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
            'Type': 'string',
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

def describe_provisioning_parameters(AcceptLanguage=None, ProductId=None, ProvisioningArtifactId=None, PathId=None):
    """
    Provides information about parameters required to provision a specified product in a specified manner. Use this operation to obtain the list of ProvisioningArtifactParameters parameters available to call the  ProvisionProduct operation for the specified product.
    
    
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
            The identifier of the product.
            

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

def list_launch_paths(AcceptLanguage=None, ProductId=None, PageSize=None, PageToken=None):
    """
    Returns a paginated list of all paths to a specified product. A path is how the user has access to a specified product, and is necessary when provisioning a product. A path also determines the constraints put on the product.
    
    
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
            Identifies the product for which to retrieve LaunchPathSummaries information.
            

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

def list_record_history(AcceptLanguage=None, AccessLevelFilter=None, SearchFilter=None, PageSize=None, PageToken=None):
    """
    Returns a paginated list of all performed requests, in the form of RecordDetails objects that are filtered as specified.
    
    
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
            The identifier of the product.
            

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
            Key (string) --The ProvisioningArtifactParameter.TagKey parameter from DescribeProvisioningParameters .
            Value (string) --The esired value for this key.
            
            

    :type NotificationArns: list
    :param NotificationArns: Passed to CloudFormation. The SNS topic ARNs to which to publish stack-related events.
            (string) --
            

    :type ProvisionToken: string
    :param ProvisionToken: [REQUIRED]
            An idempotency token that uniquely identifies the provisioning request.
            

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

def scan_provisioned_products(AcceptLanguage=None, AccessLevelFilter=None, PageSize=None, PageToken=None):
    """
    Returns a paginated list of all the ProvisionedProduct objects that are currently available (not terminated).
    
    
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
                'Type': 'string',
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

def terminate_provisioned_product(ProvisionedProductName=None, ProvisionedProductId=None, TerminateToken=None, IgnoreErrors=None, AcceptLanguage=None):
    """
    Requests termination of an existing ProvisionedProduct object. If there are Tags associated with the object, they are terminated when the ProvisionedProduct object is terminated.
    This operation does not delete any records associated with the ProvisionedProduct object.
    You can check the status of this request using the  DescribeRecord operation.
    
    
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

def update_provisioned_product(AcceptLanguage=None, ProvisionedProductName=None, ProvisionedProductId=None, ProductId=None, ProvisioningArtifactId=None, PathId=None, ProvisioningParameters=None, UpdateToken=None):
    """
    Requests updates to the configuration of an existing ProvisionedProduct object. If there are tags associated with the object, they cannot be updated or added with this operation. Depending on the specific updates requested, this operation may update with no interruption, with some interruption, or replace the ProvisionedProduct object entirely.
    You can check the status of this request using the  DescribeRecord operation.
    
    
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

