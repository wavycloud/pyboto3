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

def describe_accelerator_offerings(locationType=None, acceleratorTypes=None):
    """
    Describes the locations in which a given accelerator type or set of types is present in a given region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_accelerator_offerings(
        locationType='region'|'availability-zone'|'availability-zone-id',
        acceleratorTypes=[
            'string',
        ]
    )
    
    
    :type locationType: string
    :param locationType: [REQUIRED]\nThe location type that you want to describe accelerator type offerings for. It can assume the following values: region: will return the accelerator type offering at the regional level. availability-zone: will return the accelerator type offering at the availability zone level. availability-zone-id: will return the accelerator type offering at the availability zone level returning the availability zone id.\n

    :type acceleratorTypes: list
    :param acceleratorTypes: The list of accelerator types to describe.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'acceleratorTypeOfferings': [
        {
            'acceleratorType': 'string',
            'locationType': 'region'|'availability-zone'|'availability-zone-id',
            'location': 'string'
        },
    ]
}


Response Structure

(dict) --

acceleratorTypeOfferings (list) --
The list of accelerator type offerings for a specific location.

(dict) --
The offering for an Elastic Inference Accelerator type.

acceleratorType (string) --
The name of the Elastic Inference Accelerator type.

locationType (string) --
The location type for the offering. It can assume the following values: region: defines that the offering is at the regional level. availability-zone: defines that the offering is at the availability zone level. availability-zone-id: defines that the offering is at the availability zone level, defined by the availability zone id.

location (string) --
The location for the offering. It will return either the region, availability zone or availability zone id for the offering depending on the locationType value.











Exceptions

ElasticInference.Client.exceptions.BadRequestException
ElasticInference.Client.exceptions.ResourceNotFoundException
ElasticInference.Client.exceptions.InternalServerException


    :return: {
        'acceleratorTypeOfferings': [
            {
                'acceleratorType': 'string',
                'locationType': 'region'|'availability-zone'|'availability-zone-id',
                'location': 'string'
            },
        ]
    }
    
    
    :returns: 
    ElasticInference.Client.exceptions.BadRequestException
    ElasticInference.Client.exceptions.ResourceNotFoundException
    ElasticInference.Client.exceptions.InternalServerException
    
    """
    pass

def describe_accelerator_types():
    """
    Describes the accelerator types available in a given region, as well as their characteristics, such as memory and throughput.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_accelerator_types()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'acceleratorTypes': [
        {
            'acceleratorTypeName': 'string',
            'memoryInfo': {
                'sizeInMiB': 123
            },
            'throughputInfo': [
                {
                    'key': 'string',
                    'value': 123
                },
            ]
        },
    ]
}


Response Structure

(dict) --
acceleratorTypes (list) --The available accelerator types.

(dict) --The details of an Elastic Inference Accelerator type.

acceleratorTypeName (string) --The name of the Elastic Inference Accelerator type.

memoryInfo (dict) --The memory information of the Elastic Inference Accelerator type.

sizeInMiB (integer) --The size in mebibytes of the Elastic Inference Accelerator type.



throughputInfo (list) --The throughput information of the Elastic Inference Accelerator type.

(dict) --A throughput entry for an Elastic Inference Accelerator type.

key (string) --The throughput value of the Elastic Inference Accelerator type. It can assume the following values: TFLOPS16bit: the throughput expressed in 16bit TeraFLOPS. TFLOPS32bit: the throughput expressed in 32bit TeraFLOPS.

value (integer) --The throughput value of the Elastic Inference Accelerator type.














Exceptions

ElasticInference.Client.exceptions.InternalServerException


    :return: {
        'acceleratorTypes': [
            {
                'acceleratorTypeName': 'string',
                'memoryInfo': {
                    'sizeInMiB': 123
                },
                'throughputInfo': [
                    {
                        'key': 'string',
                        'value': 123
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def describe_accelerators(acceleratorIds=None, filters=None, maxResults=None, nextToken=None):
    """
    Describes information over a provided set of accelerators belonging to an account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_accelerators(
        acceleratorIds=[
            'string',
        ],
        filters=[
            {
                'name': 'string',
                'values': [
                    'string',
                ]
            },
        ],
        maxResults=123,
        nextToken='string'
    )
    
    
    :type acceleratorIds: list
    :param acceleratorIds: The IDs of the accelerators to describe.\n\n(string) --\n\n

    :type filters: list
    :param filters: One or more filters. Filter names and values are case-sensitive. Valid filter names are: accelerator-types: can provide a list of accelerator type names to filter for. instance-id: can provide a list of EC2 instance ids to filter for.\n\n(dict) --A filter expression for the Elastic Inference Accelerator list.\n\nname (string) --The filter name for the Elastic Inference Accelerator list. It can assume the following values: accelerator-type: the type of Elastic Inference Accelerator to filter for. instance-id: an EC2 instance id to filter for.\n\nvalues (list) --The values for the filter of the Elastic Inference Accelerator list.\n\n(string) --\n\n\n\n\n\n

    :type maxResults: integer
    :param maxResults: The total number of items to return in the command\'s output. If the total number of items available is more than the value specified, a NextToken is provided in the command\'s output. To resume pagination, provide the NextToken value in the starting-token argument of a subsequent command. Do not use the NextToken response element directly outside of the AWS CLI.

    :type nextToken: string
    :param nextToken: A token to specify where to start paginating. This is the NextToken from a previously truncated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'acceleratorSet': [
        {
            'acceleratorHealth': {
                'status': 'string'
            },
            'acceleratorType': 'string',
            'acceleratorId': 'string',
            'availabilityZone': 'string',
            'attachedResource': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

acceleratorSet (list) --
The details of the Elastic Inference Accelerators.

(dict) --
The details of an Elastic Inference Accelerator.

acceleratorHealth (dict) --
The health of the Elastic Inference Accelerator.

status (string) --
The health status of the Elastic Inference Accelerator.



acceleratorType (string) --
The type of the Elastic Inference Accelerator.

acceleratorId (string) --
The ID of the Elastic Inference Accelerator.

availabilityZone (string) --
The availability zone where the Elastic Inference Accelerator is present.

attachedResource (string) --
The ARN of the resource that the Elastic Inference Accelerator is attached to.





nextToken (string) --
A token to specify where to start paginating. This is the NextToken from a previously truncated response.







Exceptions

ElasticInference.Client.exceptions.BadRequestException
ElasticInference.Client.exceptions.ResourceNotFoundException
ElasticInference.Client.exceptions.InternalServerException


    :return: {
        'acceleratorSet': [
            {
                'acceleratorHealth': {
                    'status': 'string'
                },
                'acceleratorType': 'string',
                'acceleratorId': 'string',
                'availabilityZone': 'string',
                'attachedResource': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    ElasticInference.Client.exceptions.BadRequestException
    ElasticInference.Client.exceptions.ResourceNotFoundException
    ElasticInference.Client.exceptions.InternalServerException
    
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

def list_tags_for_resource(resourceArn=None):
    """
    Returns all tags of an Elastic Inference Accelerator.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        resourceArn='string'
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe ARN of the Elastic Inference Accelerator to list the tags for.\n

    :rtype: dict
ReturnsResponse Syntax{
    'tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
tags (dict) --The tags of the Elastic Inference Accelerator.

(string) --
(string) --









Exceptions

ElasticInference.Client.exceptions.BadRequestException
ElasticInference.Client.exceptions.ResourceNotFoundException
ElasticInference.Client.exceptions.InternalServerException


    :return: {
        'tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    ElasticInference.Client.exceptions.BadRequestException
    ElasticInference.Client.exceptions.ResourceNotFoundException
    ElasticInference.Client.exceptions.InternalServerException
    
    """
    pass

def tag_resource(resourceArn=None, tags=None):
    """
    Adds the specified tags to an Elastic Inference Accelerator.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        resourceArn='string',
        tags={
            'string': 'string'
        }
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe ARN of the Elastic Inference Accelerator to tag.\n

    :type tags: dict
    :param tags: [REQUIRED]\nThe tags to add to the Elastic Inference Accelerator.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ElasticInference.Client.exceptions.BadRequestException
ElasticInference.Client.exceptions.ResourceNotFoundException
ElasticInference.Client.exceptions.InternalServerException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(resourceArn=None, tagKeys=None):
    """
    Removes the specified tags from an Elastic Inference Accelerator.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        resourceArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe ARN of the Elastic Inference Accelerator to untag.\n

    :type tagKeys: list
    :param tagKeys: [REQUIRED]\nThe list of tags to remove from the Elastic Inference Accelerator.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ElasticInference.Client.exceptions.BadRequestException
ElasticInference.Client.exceptions.ResourceNotFoundException
ElasticInference.Client.exceptions.InternalServerException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

