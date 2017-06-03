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
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').

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

def get_resources(PaginationToken=None, TagFilters=None, ResourcesPerPage=None, TagsPerPage=None, ResourceTypeFilters=None):
    """
    Returns all the tagged resources that are associated with the specified tags (keys and values) located in the specified region for the AWS account. The tags and the resource types that you specify in the request are known as filters . The response includes all tags that are associated with the requested resources. If no filter is provided, this action returns a paginated resource list with the associated tags.
    See also: AWS API Documentation
    
    
    :example: response = client.get_resources(
        PaginationToken='string',
        TagFilters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        ResourcesPerPage=123,
        TagsPerPage=123,
        ResourceTypeFilters=[
            'string',
        ]
    )
    
    
    :type PaginationToken: string
    :param PaginationToken: A string that indicates that additional data is available. Leave this value empty for your initial request. If the response includes a PaginationToken , use that string for this value to request an additional page of data.

    :type TagFilters: list
    :param TagFilters: A list of tags (keys and values). A request can include up to 50 keys, and each key can include up to 20 values.
            If you specify multiple filters connected by an AND operator in a single request, the response returns only those resources that are associated with every specified filter.
            If you specify multiple filters connected by an OR operator in a single request, the response returns all resources that are associated with at least one or possibly more of the specified filters.
            (dict) --A list of tags (keys and values) that are used to specify the associated resources.
            Key (string) --One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.
            Values (list) --The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).
            (string) --
            
            

    :type ResourcesPerPage: integer
    :param ResourcesPerPage: A limit that restricts the number of resources returned by GetResources in paginated output. You can set ResourcesPerPage to a minimum of 1 item and the maximum of 50 items.

    :type TagsPerPage: integer
    :param TagsPerPage: A limit that restricts the number of tags (key and value pairs) returned by GetResources in paginated output. A resource with no tags is counted as having one tag (one key and value pair).
            GetResources does not split a resource and its associated tags across pages. If the specified TagsPerPage would cause such a break, a PaginationToken is returned in place of the affected resource and its tags. Use that token in another request to get the remaining data. For example, if you specify a TagsPerPage of 100 and the account has 22 resources with 10 tags each (meaning that each resource has 10 key and value pairs), the output will consist of 3 pages, with the first page displaying the first 10 resources, each with its 10 tags, the second page displaying the next 10 resources each with its 10 tags, and the third page displaying the remaining 2 resources, each with its 10 tags.
            You can set TagsPerPage to a minimum of 100 items and the maximum of 500 items.
            

    :type ResourceTypeFilters: list
    :param ResourceTypeFilters: The constraints on the resources that you want returned. The format of each resource type is service[:resourceType] . For example, specifying a resource type of ec2 returns all tagged Amazon EC2 resources (which includes tagged EC2 instances). Specifying a resource type of ec2:instance returns only EC2 instances.
            The string for each service name and resource type is the same as that embedded in a resource's Amazon Resource Name (ARN). Consult the AWS General Reference for the following:
            For a list of service name strings, see AWS Service Namespaces .
            For resource type strings, see Example ARNs .
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
            (string) --
            

    :rtype: dict
    :return: {
        'PaginationToken': 'string',
        'ResourceTagMappingList': [
            {
                'ResourceARN': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def get_tag_keys(PaginationToken=None):
    """
    Returns all tag keys in the specified region for the AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.get_tag_keys(
        PaginationToken='string'
    )
    
    
    :type PaginationToken: string
    :param PaginationToken: A string that indicates that additional data is available. Leave this value empty for your initial request. If the response includes a PaginationToken, use that string for this value to request an additional page of data.

    :rtype: dict
    :return: {
        'PaginationToken': 'string',
        'TagKeys': [
            'string',
        ]
    }
    
    
    """
    pass

def get_tag_values(PaginationToken=None, Key=None):
    """
    Returns all tag values for the specified key in the specified region for the AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.get_tag_values(
        PaginationToken='string',
        Key='string'
    )
    
    
    :type PaginationToken: string
    :param PaginationToken: A string that indicates that additional data is available. Leave this value empty for your initial request. If the response includes a PaginationToken, use that string for this value to request an additional page of data.

    :type Key: string
    :param Key: [REQUIRED]
            The key for which you want to list all existing values in the specified region for the AWS account.
            

    :rtype: dict
    :return: {
        'PaginationToken': 'string',
        'TagValues': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_waiter():
    """
    
    """
    pass

def tag_resources(ResourceARNList=None, Tags=None):
    """
    Applies one or more tags to the specified resources. Note the following:
    See also: AWS API Documentation
    
    
    :example: response = client.tag_resources(
        ResourceARNList=[
            'string',
        ],
        Tags={
            'string': 'string'
        }
    )
    
    
    :type ResourceARNList: list
    :param ResourceARNList: [REQUIRED]
            A list of ARNs. An ARN (Amazon Resource Name) uniquely identifies a resource. You can specify a minimum of 1 and a maximum of 20 ARNs (resources) to tag. An ARN can be set to a maximum of 1600 characters. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            (string) --
            

    :type Tags: dict
    :param Tags: [REQUIRED]
            The tags that you want to add to the specified resources. A tag consists of a key and a value that you define.
            (string) --
            (string) --
            

    :rtype: dict
    :return: {
        'FailedResourcesMap': {
            'string': {
                'StatusCode': 123,
                'ErrorCode': 'InternalServiceException'|'InvalidParameterException',
                'ErrorMessage': 'string'
            }
        }
    }
    
    
    :returns: 
    ResourceARNList (list) -- [REQUIRED]
    A list of ARNs. An ARN (Amazon Resource Name) uniquely identifies a resource. You can specify a minimum of 1 and a maximum of 20 ARNs (resources) to tag. An ARN can be set to a maximum of 1600 characters. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
    
    (string) --
    
    
    Tags (dict) -- [REQUIRED]
    The tags that you want to add to the specified resources. A tag consists of a key and a value that you define.
    
    (string) --
    (string) --
    
    
    
    
    
    """
    pass

def untag_resources(ResourceARNList=None, TagKeys=None):
    """
    Removes the specified tags from the specified resources. When you specify a tag key, the action removes both that key and its associated value. The operation succeeds even if you attempt to remove tags from a resource that were already removed. Note the following:
    See also: AWS API Documentation
    
    
    :example: response = client.untag_resources(
        ResourceARNList=[
            'string',
        ],
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceARNList: list
    :param ResourceARNList: [REQUIRED]
            A list of ARNs. An ARN (Amazon Resource Name) uniquely identifies a resource. You can specify a minimum of 1 and a maximum of 20 ARNs (resources) to untag. An ARN can be set to a maximum of 1600 characters. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            (string) --
            

    :type TagKeys: list
    :param TagKeys: [REQUIRED]
            A list of the tag keys that you want to remove from the specified resources.
            (string) --
            

    :rtype: dict
    :return: {
        'FailedResourcesMap': {
            'string': {
                'StatusCode': 123,
                'ErrorCode': 'InternalServiceException'|'InvalidParameterException',
                'ErrorMessage': 'string'
            }
        }
    }
    
    
    :returns: 
    ResourceARNList (list) -- [REQUIRED]
    A list of ARNs. An ARN (Amazon Resource Name) uniquely identifies a resource. You can specify a minimum of 1 and a maximum of 20 ARNs (resources) to untag. An ARN can be set to a maximum of 1600 characters. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
    
    (string) --
    
    
    TagKeys (list) -- [REQUIRED]
    A list of the tag keys that you want to remove from the specified resources.
    
    (string) --
    
    
    
    """
    pass

