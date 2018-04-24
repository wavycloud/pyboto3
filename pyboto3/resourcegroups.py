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

def create_group(Name=None, Description=None, ResourceQuery=None, Tags=None):
    """
    Creates a group with a specified name, description, and resource query.
    See also: AWS API Documentation
    
    
    :example: response = client.create_group(
        Name='string',
        Description='string',
        ResourceQuery={
            'Type': 'TAG_FILTERS_1_0',
            'Query': 'string'
        },
        Tags={
            'string': 'string'
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the group, which is the identifier of the group in other operations. A resource group name cannot be updated after it is created. A resource group name can have a maximum of 127 characters, including letters, numbers, hyphens, dots, and underscores. The name cannot start with AWS or aws ; these are reserved. A resource group name must be unique within your account.
            

    :type Description: string
    :param Description: The description of the resource group. Descriptions can have a maximum of 511 characters, including letters, numbers, hyphens, underscores, punctuation, and spaces.

    :type ResourceQuery: dict
    :param ResourceQuery: [REQUIRED]
            The resource query that determines which AWS resources are members of this group.
            Type (string) -- [REQUIRED]The type of the query. The valid value in this release is TAG_FILTERS_1_0 .
            TAG_FILTERS_1_0: * A JSON syntax that lets you specify a collection of simple tag filters for resource types and tags, as supported by the AWS Tagging API GetResources operation. When more than one element is present, only resources that match all filters are part of the result. If a filter specifies more than one value for a key, a resource matches the filter if its tag value matches any of the specified values.
            Query (string) -- [REQUIRED]The query that defines a group or a search.
            

    :type Tags: dict
    :param Tags: The tags to add to the group. A tag is a string-to-string map of key-value pairs. Tag keys can have a maximum character length of 127 characters, and tag values can have a maximum length of 255 characters.
            (string) --
            (string) --
            

    :rtype: dict
    :return: {
        'Group': {
            'GroupArn': 'string',
            'Name': 'string',
            'Description': 'string'
        },
        'ResourceQuery': {
            'Type': 'TAG_FILTERS_1_0',
            'Query': 'string'
        },
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    TAG_FILTERS_1_0: * A JSON syntax that lets you specify a collection of simple tag filters for resource types and tags, as supported by the AWS Tagging API GetResources operation. When more than one element is present, only resources that match all filters are part of the result. If a filter specifies more than one value for a key, a resource matches the filter if its tag value matches any of the specified values.
    
    """
    pass

def delete_group(GroupName=None):
    """
    Deletes a specified resource group. Deleting a resource group does not delete resources that are members of the group; it only deletes the group structure.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_group(
        GroupName='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]
            The name of the resource group to delete.
            

    :rtype: dict
    :return: {
        'Group': {
            'GroupArn': 'string',
            'Name': 'string',
            'Description': 'string'
        }
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

def get_group(GroupName=None):
    """
    Returns information about a specified resource group.
    See also: AWS API Documentation
    
    
    :example: response = client.get_group(
        GroupName='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]
            The name of the resource group.
            

    :rtype: dict
    :return: {
        'Group': {
            'GroupArn': 'string',
            'Name': 'string',
            'Description': 'string'
        }
    }
    
    
    """
    pass

def get_group_query(GroupName=None):
    """
    Returns the resource query associated with the specified resource group.
    See also: AWS API Documentation
    
    
    :example: response = client.get_group_query(
        GroupName='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]
            The name of the resource group.
            

    :rtype: dict
    :return: {
        'GroupQuery': {
            'GroupName': 'string',
            'ResourceQuery': {
                'Type': 'TAG_FILTERS_1_0',
                'Query': 'string'
            }
        }
    }
    
    
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

def get_tags(Arn=None):
    """
    Returns a list of tags that are associated with a resource, specified by an ARN.
    See also: AWS API Documentation
    
    
    :example: response = client.get_tags(
        Arn='string'
    )
    
    
    :type Arn: string
    :param Arn: [REQUIRED]
            The ARN of the resource for which you want a list of tags. The resource must exist within the account you are using.
            

    :rtype: dict
    :return: {
        'Arn': 'string',
        'Tags': {
            'string': 'string'
        }
    }
    
    
    """
    pass

def get_waiter(waiter_name=None):
    """
    
    :type waiter_name: 
    :param waiter_name: 

    """
    pass

def list_group_resources(GroupName=None, MaxResults=None, NextToken=None):
    """
    Returns a list of ARNs of resources that are members of a specified resource group.
    See also: AWS API Documentation
    
    
    :example: response = client.list_group_resources(
        GroupName='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]
            The name of the resource group.
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of group member ARNs that are returned in a single call by ListGroupResources, in paginated output. By default, this number is 50.

    :type NextToken: string
    :param NextToken: The NextToken value that is returned in a paginated ListGroupResources request. To get the next page of results, run the call again, add the NextToken parameter, and specify the NextToken value.

    :rtype: dict
    :return: {
        'ResourceIdentifiers': [
            {
                'ResourceArn': 'string',
                'ResourceType': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_groups(MaxResults=None, NextToken=None):
    """
    Returns a list of existing resource groups in your account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_groups(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of resource group results that are returned by ListGroups in paginated output. By default, this number is 50.

    :type NextToken: string
    :param NextToken: The NextToken value that is returned in a paginated ListGroups request. To get the next page of results, run the call again, add the NextToken parameter, and specify the NextToken value.

    :rtype: dict
    :return: {
        'Groups': [
            {
                'GroupArn': 'string',
                'Name': 'string',
                'Description': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def search_resources(ResourceQuery=None, MaxResults=None, NextToken=None):
    """
    Returns a list of AWS resource identifiers that matches a specified query. The query uses the same format as a resource query in a CreateGroup or UpdateGroupQuery operation.
    See also: AWS API Documentation
    
    
    :example: response = client.search_resources(
        ResourceQuery={
            'Type': 'TAG_FILTERS_1_0',
            'Query': 'string'
        },
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ResourceQuery: dict
    :param ResourceQuery: [REQUIRED]
            The search query, using the same formats that are supported for resource group definition.
            Type (string) -- [REQUIRED]The type of the query. The valid value in this release is TAG_FILTERS_1_0 .
            TAG_FILTERS_1_0: * A JSON syntax that lets you specify a collection of simple tag filters for resource types and tags, as supported by the AWS Tagging API GetResources operation. When more than one element is present, only resources that match all filters are part of the result. If a filter specifies more than one value for a key, a resource matches the filter if its tag value matches any of the specified values.
            Query (string) -- [REQUIRED]The query that defines a group or a search.
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of group member ARNs returned by SearchResources in paginated output. By default, this number is 50.

    :type NextToken: string
    :param NextToken: The NextToken value that is returned in a paginated SearchResources request. To get the next page of results, run the call again, add the NextToken parameter, and specify the NextToken value.

    :rtype: dict
    :return: {
        'ResourceIdentifiers': [
            {
                'ResourceArn': 'string',
                'ResourceType': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def tag(Arn=None, Tags=None):
    """
    Adds specified tags to a resource with the specified ARN. Existing tags on a resource are not changed if they are not specified in the request parameters.
    See also: AWS API Documentation
    
    
    :example: response = client.tag(
        Arn='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type Arn: string
    :param Arn: [REQUIRED]
            The ARN of the resource to which to add tags.
            

    :type Tags: dict
    :param Tags: [REQUIRED]
            The tags to add to the specified resource. A tag is a string-to-string map of key-value pairs. Tag keys can have a maximum character length of 127 characters, and tag values can have a maximum length of 255 characters.
            (string) --
            (string) --
            

    :rtype: dict
    :return: {
        'Arn': 'string',
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def untag(Arn=None, Keys=None):
    """
    Deletes specified tags from a specified resource.
    See also: AWS API Documentation
    
    
    :example: response = client.untag(
        Arn='string',
        Keys=[
            'string',
        ]
    )
    
    
    :type Arn: string
    :param Arn: [REQUIRED]
            The ARN of the resource from which to remove tags.
            

    :type Keys: list
    :param Keys: [REQUIRED]
            The keys of the tags to be removed.
            (string) --
            

    :rtype: dict
    :return: {
        'Arn': 'string',
        'Keys': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_group(GroupName=None, Description=None):
    """
    Updates an existing group with a new or changed description. You cannot update the name of a resource group.
    See also: AWS API Documentation
    
    
    :example: response = client.update_group(
        GroupName='string',
        Description='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]
            The name of the resource group for which you want to update its description.
            

    :type Description: string
    :param Description: The description of the resource group. Descriptions can have a maximum of 511 characters, including letters, numbers, hyphens, underscores, punctuation, and spaces.

    :rtype: dict
    :return: {
        'Group': {
            'GroupArn': 'string',
            'Name': 'string',
            'Description': 'string'
        }
    }
    
    
    """
    pass

def update_group_query(GroupName=None, ResourceQuery=None):
    """
    Updates the resource query of a group.
    See also: AWS API Documentation
    
    
    :example: response = client.update_group_query(
        GroupName='string',
        ResourceQuery={
            'Type': 'TAG_FILTERS_1_0',
            'Query': 'string'
        }
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]
            The name of the resource group for which you want to edit the query.
            

    :type ResourceQuery: dict
    :param ResourceQuery: [REQUIRED]
            The resource query that determines which AWS resources are members of the resource group.
            Type (string) -- [REQUIRED]The type of the query. The valid value in this release is TAG_FILTERS_1_0 .
            TAG_FILTERS_1_0: * A JSON syntax that lets you specify a collection of simple tag filters for resource types and tags, as supported by the AWS Tagging API GetResources operation. When more than one element is present, only resources that match all filters are part of the result. If a filter specifies more than one value for a key, a resource matches the filter if its tag value matches any of the specified values.
            Query (string) -- [REQUIRED]The query that defines a group or a search.
            

    :rtype: dict
    :return: {
        'GroupQuery': {
            'GroupName': 'string',
            'ResourceQuery': {
                'Type': 'TAG_FILTERS_1_0',
                'Query': 'string'
            }
        }
    }
    
    
    :returns: 
    TAG_FILTERS_1_0: * A JSON syntax that lets you specify a collection of simple tag filters for resource types and tags, as supported by the AWS Tagging API GetResources operation. When more than one element is present, only resources that match all filters are part of the result. If a filter specifies more than one value for a key, a resource matches the filter if its tag value matches any of the specified values.
    
    """
    pass

