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

def describe_report_creation():
    """
    Describes the status of the StartReportCreation operation.
    You can call this operation only from the organization\'s master account and from the us-east-1 Region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_report_creation()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'Status': 'string',
    'S3Location': 'string',
    'ErrorMessage': 'string'
}


Response Structure

(dict) --
Status (string) --Reports the status of the operation.
The operation status can be one of the following:

RUNNING - Report creation is in progress.
SUCCEEDED - Report creation is complete. You can open the report from the Amazon S3 bucket that you specified when you ran StartReportCreation .
FAILED - Report creation timed out or the Amazon S3 bucket is not accessible.
NO REPORT - No report was generated in the last 90 days.


S3Location (string) --The path to the Amazon S3 bucket where the report was stored on creation.

ErrorMessage (string) --Details of the common errors that all operations return.






Exceptions

ResourceGroupsTaggingAPI.Client.exceptions.ConstraintViolationException
ResourceGroupsTaggingAPI.Client.exceptions.InternalServiceException
ResourceGroupsTaggingAPI.Client.exceptions.InvalidParameterException
ResourceGroupsTaggingAPI.Client.exceptions.ThrottledException


    :return: {
        'Status': 'string',
        'S3Location': 'string',
        'ErrorMessage': 'string'
    }
    
    
    :returns: 
    ResourceGroupsTaggingAPI.Client.exceptions.ConstraintViolationException
    ResourceGroupsTaggingAPI.Client.exceptions.InternalServiceException
    ResourceGroupsTaggingAPI.Client.exceptions.InvalidParameterException
    ResourceGroupsTaggingAPI.Client.exceptions.ThrottledException
    
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

def get_compliance_summary(TargetIdFilters=None, RegionFilters=None, ResourceTypeFilters=None, TagKeyFilters=None, GroupBy=None, MaxResults=None, PaginationToken=None):
    """
    Returns a table that shows counts of resources that are noncompliant with their tag policies.
    For more information on tag policies, see Tag Policies in the AWS Organizations User Guide.
    You can call this operation only from the organization\'s master account and from the us-east-1 Region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_compliance_summary(
        TargetIdFilters=[
            'string',
        ],
        RegionFilters=[
            'string',
        ],
        ResourceTypeFilters=[
            'string',
        ],
        TagKeyFilters=[
            'string',
        ],
        GroupBy=[
            'TARGET_ID'|'REGION'|'RESOURCE_TYPE',
        ],
        MaxResults=123,
        PaginationToken='string'
    )
    
    
    :type TargetIdFilters: list
    :param TargetIdFilters: The target identifiers (usually, specific account IDs) to limit the output by. If you use this parameter, the count of returned noncompliant resources includes only resources with the specified target IDs.\n\n(string) --\n\n

    :type RegionFilters: list
    :param RegionFilters: A list of Regions to limit the output by. If you use this parameter, the count of returned noncompliant resources includes only resources in the specified Regions.\n\n(string) --\n\n

    :type ResourceTypeFilters: list
    :param ResourceTypeFilters: The constraints on the resources that you want returned. The format of each resource type is service[:resourceType] . For example, specifying a resource type of ec2 returns all Amazon EC2 resources (which includes EC2 instances). Specifying a resource type of ec2:instance returns only EC2 instances.\nThe string for each service name and resource type is the same as that embedded in a resource\'s Amazon Resource Name (ARN). Consult the AWS General Reference for the following:\n\nFor a list of service name strings, see AWS Service Namespaces .\nFor resource type strings, see Example ARNs .\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nYou can specify multiple resource types by using an array. The array can include up to 100 items. Note that the length constraint requirement applies to each resource type filter.\n\n(string) --\n\n

    :type TagKeyFilters: list
    :param TagKeyFilters: A list of tag keys to limit the output by. If you use this parameter, the count of returned noncompliant resources includes only resources that have the specified tag keys.\n\n(string) --\n\n

    :type GroupBy: list
    :param GroupBy: A list of attributes to group the counts of noncompliant resources by. If supplied, the counts are sorted by those attributes.\n\n(string) --\n\n

    :type MaxResults: integer
    :param MaxResults: A limit that restricts the number of results that are returned per page.

    :type PaginationToken: string
    :param PaginationToken: A string that indicates that additional data is available. Leave this value empty for your initial request. If the response includes a PaginationToken , use that string for this value to request an additional page of data.

    :rtype: dict

ReturnsResponse Syntax
{
    'SummaryList': [
        {
            'LastUpdated': 'string',
            'TargetId': 'string',
            'TargetIdType': 'ACCOUNT'|'OU'|'ROOT',
            'Region': 'string',
            'ResourceType': 'string',
            'NonCompliantResources': 123
        },
    ],
    'PaginationToken': 'string'
}


Response Structure

(dict) --

SummaryList (list) --
A table that shows counts of noncompliant resources.

(dict) --
A count of noncompliant resources.

LastUpdated (string) --
The timestamp that shows when this summary was generated in this Region.

TargetId (string) --
The account identifier or the root identifier of the organization. If you don\'t know the root ID, you can call the AWS Organizations ListRoots API.

TargetIdType (string) --
Whether the target is an account, an OU, or the organization root.

Region (string) --
The AWS Region that the summary applies to.

ResourceType (string) --
The AWS resource type.

NonCompliantResources (integer) --
The count of noncompliant resources.





PaginationToken (string) --
A string that indicates that the response contains more data than can be returned in a single response. To receive additional data, specify this string for the PaginationToken value in a subsequent request.







Exceptions

ResourceGroupsTaggingAPI.Client.exceptions.ConstraintViolationException
ResourceGroupsTaggingAPI.Client.exceptions.InternalServiceException
ResourceGroupsTaggingAPI.Client.exceptions.InvalidParameterException
ResourceGroupsTaggingAPI.Client.exceptions.ThrottledException


    :return: {
        'SummaryList': [
            {
                'LastUpdated': 'string',
                'TargetId': 'string',
                'TargetIdType': 'ACCOUNT'|'OU'|'ROOT',
                'Region': 'string',
                'ResourceType': 'string',
                'NonCompliantResources': 123
            },
        ],
        'PaginationToken': 'string'
    }
    
    
    :returns: 
    ResourceGroupsTaggingAPI.Client.exceptions.ConstraintViolationException
    ResourceGroupsTaggingAPI.Client.exceptions.InternalServiceException
    ResourceGroupsTaggingAPI.Client.exceptions.InvalidParameterException
    ResourceGroupsTaggingAPI.Client.exceptions.ThrottledException
    
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

def get_resources(PaginationToken=None, TagFilters=None, ResourcesPerPage=None, TagsPerPage=None, ResourceTypeFilters=None, IncludeComplianceDetails=None, ExcludeCompliantResources=None):
    """
    Returns all the tagged or previously tagged resources that are located in the specified Region for the AWS account.
    Depending on what information you want returned, you can also specify the following:
    See also: AWS API Documentation
    
    Exceptions
    
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
        ],
        IncludeComplianceDetails=True|False,
        ExcludeCompliantResources=True|False
    )
    
    
    :type PaginationToken: string
    :param PaginationToken: A string that indicates that additional data is available. Leave this value empty for your initial request. If the response includes a PaginationToken , use that string for this value to request an additional page of data.

    :type TagFilters: list
    :param TagFilters: A list of TagFilters (keys and values). Each TagFilter specified must contain a key with values as optional. A request can include up to 50 keys, and each key can include up to 20 values.\nNote the following when deciding how to use TagFilters:\n\nIf you do specify a TagFilter, the response returns only those resources that are currently associated with the specified tag.\nIf you don\'t specify a TagFilter, the response includes all resources that were ever associated with tags. Resources that currently don\'t have associated tags are shown with an empty tag set, like this: 'Tags': [] .\nIf you specify more than one filter in a single request, the response returns only those resources that satisfy all specified filters.\nIf you specify a filter that contains more than one value for a key, the response returns resources that match any of the specified values for that key.\nIf you don\'t specify any values for a key, the response returns resources that are tagged with that key irrespective of the value. For example, for filters: filter1 = {key1, {value1}}, filter2 = {key2, {value2,value3,value4}} , filter3 = {key3}:\nGetResources( {filter1} ) returns resources tagged with key1=value1\nGetResources( {filter2} ) returns resources tagged with key2=value2 or key2=value3 or key2=value4\nGetResources( {filter3} ) returns resources tagged with any tag containing key3 as its tag key, irrespective of its value\nGetResources( {filter1,filter2,filter3} ) returns resources tagged with ( key1=value1) and ( key2=value2 or key2=value3 or key2=value4) and (key3, irrespective of the value)\n\n\n\n\n(dict) --A list of tags (keys and values) that are used to specify the associated resources.\n\nKey (string) --One part of a key-value pair that makes up a tag. A key is a general label that acts like a category for more specific tag values.\n\nValues (list) --One part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key). The value can be empty or null.\n\n(string) --\n\n\n\n\n\n

    :type ResourcesPerPage: integer
    :param ResourcesPerPage: A limit that restricts the number of resources returned by GetResources in paginated output. You can set ResourcesPerPage to a minimum of 1 item and the maximum of 100 items.

    :type TagsPerPage: integer
    :param TagsPerPage: AWS recommends using ResourcesPerPage instead of this parameter.\nA limit that restricts the number of tags (key and value pairs) returned by GetResources in paginated output. A resource with no tags is counted as having one tag (one key and value pair).\n\nGetResources does not split a resource and its associated tags across pages. If the specified TagsPerPage would cause such a break, a PaginationToken is returned in place of the affected resource and its tags. Use that token in another request to get the remaining data. For example, if you specify a TagsPerPage of 100 and the account has 22 resources with 10 tags each (meaning that each resource has 10 key and value pairs), the output will consist of three pages. The first page displays the first 10 resources, each with its 10 tags. The second page displays the next 10 resources, each with its 10 tags. The third page displays the remaining 2 resources, each with its 10 tags.\nYou can set TagsPerPage to a minimum of 100 items and the maximum of 500 items.\n

    :type ResourceTypeFilters: list
    :param ResourceTypeFilters: The constraints on the resources that you want returned. The format of each resource type is service[:resourceType] . For example, specifying a resource type of ec2 returns all Amazon EC2 resources (which includes EC2 instances). Specifying a resource type of ec2:instance returns only EC2 instances.\nThe string for each service name and resource type is the same as that embedded in a resource\'s Amazon Resource Name (ARN). Consult the AWS General Reference for the following:\n\nFor a list of service name strings, see AWS Service Namespaces .\nFor resource type strings, see Example ARNs .\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nYou can specify multiple resource types by using an array. The array can include up to 100 items. Note that the length constraint requirement applies to each resource type filter.\n\n(string) --\n\n

    :type IncludeComplianceDetails: boolean
    :param IncludeComplianceDetails: Specifies whether to include details regarding the compliance with the effective tag policy. Set this to true to determine whether resources are compliant with the tag policy and to get details.

    :type ExcludeCompliantResources: boolean
    :param ExcludeCompliantResources: Specifies whether to exclude resources that are compliant with the tag policy. Set this to true if you are interested in retrieving information on noncompliant resources only.\nYou can use this parameter only if the IncludeComplianceDetails parameter is also set to true .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'PaginationToken': 'string',
    'ResourceTagMappingList': [
        {
            'ResourceARN': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'ComplianceDetails': {
                'NoncompliantKeys': [
                    'string',
                ],
                'KeysWithNoncompliantValues': [
                    'string',
                ],
                'ComplianceStatus': True|False
            }
        },
    ]
}


Response Structure

(dict) --

PaginationToken (string) --
A string that indicates that the response contains more data than can be returned in a single response. To receive additional data, specify this string for the PaginationToken value in a subsequent request.

ResourceTagMappingList (list) --
A list of resource ARNs and the tags (keys and values) associated with each.

(dict) --
A list of resource ARNs and the tags (keys and values) that are associated with each.

ResourceARN (string) --
The ARN of the resource.

Tags (list) --
The tags that have been applied to one or more AWS resources.

(dict) --
The metadata that you apply to AWS resources to help you categorize and organize them. Each tag consists of a key and a value, both of which you define. For more information, see Tagging AWS Resources in the AWS General Reference .

Key (string) --
One part of a key-value pair that makes up a tag. A key is a general label that acts like a category for more specific tag values.

Value (string) --
One part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key). The value can be empty or null.





ComplianceDetails (dict) --
Information that shows whether a resource is compliant with the effective tag policy, including details on any noncompliant tag keys.

NoncompliantKeys (list) --
These tag keys on the resource are noncompliant with the effective tag policy.

(string) --


KeysWithNoncompliantValues (list) --
These are keys defined in the effective policy that are on the resource with either incorrect case treatment or noncompliant values.

(string) --


ComplianceStatus (boolean) --
Whether a resource is compliant with the effective tag policy.













Exceptions

ResourceGroupsTaggingAPI.Client.exceptions.InvalidParameterException
ResourceGroupsTaggingAPI.Client.exceptions.ThrottledException
ResourceGroupsTaggingAPI.Client.exceptions.InternalServiceException
ResourceGroupsTaggingAPI.Client.exceptions.PaginationTokenExpiredException


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
                ],
                'ComplianceDetails': {
                    'NoncompliantKeys': [
                        'string',
                    ],
                    'KeysWithNoncompliantValues': [
                        'string',
                    ],
                    'ComplianceStatus': True|False
                }
            },
        ]
    }
    
    
    :returns: 
    PaginationToken (string) -- A string that indicates that additional data is available. Leave this value empty for your initial request. If the response includes a PaginationToken , use that string for this value to request an additional page of data.
    TagFilters (list) -- A list of TagFilters (keys and values). Each TagFilter specified must contain a key with values as optional. A request can include up to 50 keys, and each key can include up to 20 values.
    Note the following when deciding how to use TagFilters:
    
    If you do specify a TagFilter, the response returns only those resources that are currently associated with the specified tag.
    If you don\'t specify a TagFilter, the response includes all resources that were ever associated with tags. Resources that currently don\'t have associated tags are shown with an empty tag set, like this: "Tags": [] .
    If you specify more than one filter in a single request, the response returns only those resources that satisfy all specified filters.
    If you specify a filter that contains more than one value for a key, the response returns resources that match any of the specified values for that key.
    If you don\'t specify any values for a key, the response returns resources that are tagged with that key irrespective of the value. For example, for filters: filter1 = {key1, {value1}}, filter2 = {key2, {value2,value3,value4}} , filter3 = {key3}:
    GetResources( {filter1} ) returns resources tagged with key1=value1
    GetResources( {filter2} ) returns resources tagged with key2=value2 or key2=value3 or key2=value4
    GetResources( {filter3} ) returns resources tagged with any tag containing key3 as its tag key, irrespective of its value
    GetResources( {filter1,filter2,filter3} ) returns resources tagged with ( key1=value1) and ( key2=value2 or key2=value3 or key2=value4) and (key3, irrespective of the value)
    
    
    
    
    (dict) --A list of tags (keys and values) that are used to specify the associated resources.
    
    Key (string) --One part of a key-value pair that makes up a tag. A key is a general label that acts like a category for more specific tag values.
    
    Values (list) --One part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key). The value can be empty or null.
    
    (string) --
    
    
    
    
    
    
    ResourcesPerPage (integer) -- A limit that restricts the number of resources returned by GetResources in paginated output. You can set ResourcesPerPage to a minimum of 1 item and the maximum of 100 items.
    TagsPerPage (integer) -- AWS recommends using ResourcesPerPage instead of this parameter.
    A limit that restricts the number of tags (key and value pairs) returned by GetResources in paginated output. A resource with no tags is counted as having one tag (one key and value pair).
    
    GetResources does not split a resource and its associated tags across pages. If the specified TagsPerPage would cause such a break, a PaginationToken is returned in place of the affected resource and its tags. Use that token in another request to get the remaining data. For example, if you specify a TagsPerPage of 100 and the account has 22 resources with 10 tags each (meaning that each resource has 10 key and value pairs), the output will consist of three pages. The first page displays the first 10 resources, each with its 10 tags. The second page displays the next 10 resources, each with its 10 tags. The third page displays the remaining 2 resources, each with its 10 tags.
    You can set TagsPerPage to a minimum of 100 items and the maximum of 500 items.
    
    ResourceTypeFilters (list) -- The constraints on the resources that you want returned. The format of each resource type is service[:resourceType] . For example, specifying a resource type of ec2 returns all Amazon EC2 resources (which includes EC2 instances). Specifying a resource type of ec2:instance returns only EC2 instances.
    The string for each service name and resource type is the same as that embedded in a resource\'s Amazon Resource Name (ARN). Consult the AWS General Reference for the following:
    
    For a list of service name strings, see AWS Service Namespaces .
    For resource type strings, see Example ARNs .
    For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
    
    You can specify multiple resource types by using an array. The array can include up to 100 items. Note that the length constraint requirement applies to each resource type filter.
    
    (string) --
    
    
    IncludeComplianceDetails (boolean) -- Specifies whether to include details regarding the compliance with the effective tag policy. Set this to true to determine whether resources are compliant with the tag policy and to get details.
    ExcludeCompliantResources (boolean) -- Specifies whether to exclude resources that are compliant with the tag policy. Set this to true if you are interested in retrieving information on noncompliant resources only.
    You can use this parameter only if the IncludeComplianceDetails parameter is also set to true .
    
    
    """
    pass

def get_tag_keys(PaginationToken=None):
    """
    Returns all tag keys in the specified Region for the AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_tag_keys(
        PaginationToken='string'
    )
    
    
    :type PaginationToken: string
    :param PaginationToken: A string that indicates that additional data is available. Leave this value empty for your initial request. If the response includes a PaginationToken , use that string for this value to request an additional page of data.

    :rtype: dict
ReturnsResponse Syntax{
    'PaginationToken': 'string',
    'TagKeys': [
        'string',
    ]
}


Response Structure

(dict) --
PaginationToken (string) --A string that indicates that the response contains more data than can be returned in a single response. To receive additional data, specify this string for the PaginationToken value in a subsequent request.

TagKeys (list) --A list of all tag keys in the AWS account.

(string) --







Exceptions

ResourceGroupsTaggingAPI.Client.exceptions.InvalidParameterException
ResourceGroupsTaggingAPI.Client.exceptions.ThrottledException
ResourceGroupsTaggingAPI.Client.exceptions.InternalServiceException
ResourceGroupsTaggingAPI.Client.exceptions.PaginationTokenExpiredException


    :return: {
        'PaginationToken': 'string',
        'TagKeys': [
            'string',
        ]
    }
    
    
    :returns: 
    ResourceGroupsTaggingAPI.Client.exceptions.InvalidParameterException
    ResourceGroupsTaggingAPI.Client.exceptions.ThrottledException
    ResourceGroupsTaggingAPI.Client.exceptions.InternalServiceException
    ResourceGroupsTaggingAPI.Client.exceptions.PaginationTokenExpiredException
    
    """
    pass

def get_tag_values(PaginationToken=None, Key=None):
    """
    Returns all tag values for the specified key in the specified Region for the AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_tag_values(
        PaginationToken='string',
        Key='string'
    )
    
    
    :type PaginationToken: string
    :param PaginationToken: A string that indicates that additional data is available. Leave this value empty for your initial request. If the response includes a PaginationToken , use that string for this value to request an additional page of data.

    :type Key: string
    :param Key: [REQUIRED]\nThe key for which you want to list all existing values in the specified Region for the AWS account.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'PaginationToken': 'string',
    'TagValues': [
        'string',
    ]
}


Response Structure

(dict) --

PaginationToken (string) --
A string that indicates that the response contains more data than can be returned in a single response. To receive additional data, specify this string for the PaginationToken value in a subsequent request.

TagValues (list) --
A list of all tag values for the specified key in the AWS account.

(string) --








Exceptions

ResourceGroupsTaggingAPI.Client.exceptions.InvalidParameterException
ResourceGroupsTaggingAPI.Client.exceptions.ThrottledException
ResourceGroupsTaggingAPI.Client.exceptions.InternalServiceException
ResourceGroupsTaggingAPI.Client.exceptions.PaginationTokenExpiredException


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

def get_waiter(waiter_name=None):
    """
    Returns an object that can wait for some condition.
    
    :type waiter_name: str
    :param waiter_name: The name of the waiter to get. See the waiters\nsection of the service docs for a list of available waiters.

    :rtype: botocore.waiter.Waiter


    """
    pass

def start_report_creation(S3Bucket=None):
    """
    Generates a report that lists all tagged resources in accounts across your organization and tells whether each resource is compliant with the effective tag policy. Compliance data is refreshed daily.
    The generated report is saved to the following location:
    You can call this operation only from the organization\'s master account and from the us-east-1 Region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_report_creation(
        S3Bucket='string'
    )
    
    
    :type S3Bucket: string
    :param S3Bucket: [REQUIRED]\nThe name of the Amazon S3 bucket where the report will be stored; for example:\n\nawsexamplebucket\nFor more information on S3 bucket requirements, including an example bucket policy, see the example S3 bucket policy on this page.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

ResourceGroupsTaggingAPI.Client.exceptions.ConcurrentModificationException
ResourceGroupsTaggingAPI.Client.exceptions.ConstraintViolationException
ResourceGroupsTaggingAPI.Client.exceptions.InternalServiceException
ResourceGroupsTaggingAPI.Client.exceptions.InvalidParameterException
ResourceGroupsTaggingAPI.Client.exceptions.ThrottledException


    :return: {}
    
    
    :returns: 
    ResourceGroupsTaggingAPI.Client.exceptions.ConcurrentModificationException
    ResourceGroupsTaggingAPI.Client.exceptions.ConstraintViolationException
    ResourceGroupsTaggingAPI.Client.exceptions.InternalServiceException
    ResourceGroupsTaggingAPI.Client.exceptions.InvalidParameterException
    ResourceGroupsTaggingAPI.Client.exceptions.ThrottledException
    
    """
    pass

def tag_resources(ResourceARNList=None, Tags=None):
    """
    Applies one or more tags to the specified resources. Note the following:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resources(
        ResourceARNList=[
            'string',
        ],
        Tags={
            'string': 'string'
        }
    )
    
    
    :type ResourceARNList: list
    :param ResourceARNList: [REQUIRED]\nA list of ARNs. An ARN (Amazon Resource Name) uniquely identifies a resource. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .\n\n(string) --\n\n

    :type Tags: dict
    :param Tags: [REQUIRED]\nThe tags that you want to add to the specified resources. A tag consists of a key and a value that you define.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'FailedResourcesMap': {
        'string': {
            'StatusCode': 123,
            'ErrorCode': 'InternalServiceException'|'InvalidParameterException',
            'ErrorMessage': 'string'
        }
    }
}


Response Structure

(dict) --

FailedResourcesMap (dict) --
A map containing a key-value pair for each failed item that couldn\'t be tagged. The key is the ARN of the failed resource. The value is a FailureInfo object that contains an error code, a status code, and an error message. If there are no errors, the FailedResourcesMap is empty.

(string) --

(dict) --
Information about the errors that are returned for each failed resource. This information can include InternalServiceException and InvalidParameterException errors. It can also include any valid error code returned by the AWS service that hosts the resource that the ARN key represents.
The following are common error codes that you might receive from other AWS services:

InternalServiceException \xe2\x80\x93 This can mean that the Resource Groups Tagging API didn\'t receive a response from another AWS service. It can also mean the the resource type in the request is not supported by the Resource Groups Tagging API. In these cases, it\'s safe to retry the request and then call GetResources to verify the changes.
AccessDeniedException \xe2\x80\x93 This can mean that you need permission to calling tagging operations in the AWS service that contains the resource. For example, to use the Resource Groups Tagging API to tag a CloudWatch alarm resource, you need permission to call ` TagResources http://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_TagResources.html`__  and  ` TagResource http://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_TagResource.html`__ in the CloudWatch API.

For more information on errors that are generated from other AWS services, see the documentation for that service.

StatusCode (integer) --
The HTTP status code of the common error.

ErrorCode (string) --
The code of the common error. Valid values include InternalServiceException , InvalidParameterException , and any valid error code returned by the AWS service that hosts the resource that you want to tag.

ErrorMessage (string) --
The message of the common error.













Exceptions

ResourceGroupsTaggingAPI.Client.exceptions.InvalidParameterException
ResourceGroupsTaggingAPI.Client.exceptions.ThrottledException
ResourceGroupsTaggingAPI.Client.exceptions.InternalServiceException


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
    A list of ARNs. An ARN (Amazon Resource Name) uniquely identifies a resource. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
    
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
    
    Exceptions
    
    :example: response = client.untag_resources(
        ResourceARNList=[
            'string',
        ],
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceARNList: list
    :param ResourceARNList: [REQUIRED]\nA list of ARNs. An ARN (Amazon Resource Name) uniquely identifies a resource. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .\n\n(string) --\n\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nA list of the tag keys that you want to remove from the specified resources.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'FailedResourcesMap': {
        'string': {
            'StatusCode': 123,
            'ErrorCode': 'InternalServiceException'|'InvalidParameterException',
            'ErrorMessage': 'string'
        }
    }
}


Response Structure

(dict) --

FailedResourcesMap (dict) --
Details of resources that could not be untagged. An error code, status code, and error message are returned for each failed item.

(string) --

(dict) --
Information about the errors that are returned for each failed resource. This information can include InternalServiceException and InvalidParameterException errors. It can also include any valid error code returned by the AWS service that hosts the resource that the ARN key represents.
The following are common error codes that you might receive from other AWS services:

InternalServiceException \xe2\x80\x93 This can mean that the Resource Groups Tagging API didn\'t receive a response from another AWS service. It can also mean the the resource type in the request is not supported by the Resource Groups Tagging API. In these cases, it\'s safe to retry the request and then call GetResources to verify the changes.
AccessDeniedException \xe2\x80\x93 This can mean that you need permission to calling tagging operations in the AWS service that contains the resource. For example, to use the Resource Groups Tagging API to tag a CloudWatch alarm resource, you need permission to call ` TagResources http://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_TagResources.html`__  and  ` TagResource http://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_TagResource.html`__ in the CloudWatch API.

For more information on errors that are generated from other AWS services, see the documentation for that service.

StatusCode (integer) --
The HTTP status code of the common error.

ErrorCode (string) --
The code of the common error. Valid values include InternalServiceException , InvalidParameterException , and any valid error code returned by the AWS service that hosts the resource that you want to tag.

ErrorMessage (string) --
The message of the common error.













Exceptions

ResourceGroupsTaggingAPI.Client.exceptions.InvalidParameterException
ResourceGroupsTaggingAPI.Client.exceptions.ThrottledException
ResourceGroupsTaggingAPI.Client.exceptions.InternalServiceException


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
    A list of ARNs. An ARN (Amazon Resource Name) uniquely identifies a resource. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
    
    (string) --
    
    
    TagKeys (list) -- [REQUIRED]
    A list of the tag keys that you want to remove from the specified resources.
    
    (string) --
    
    
    
    """
    pass

