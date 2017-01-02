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

def create_protection(Name=None, ResourceArn=None):
    """
    Enables AWS Shield Advanced for a specific AWS resource. The resource can be an Amazon CloudFront distribution, Elastic Load Balancing load balancer, or an Amazon Route 53 hosted zone.
    See also: AWS API Documentation
    
    
    :example: response = client.create_protection(
        Name='string',
        ResourceArn='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            Friendly name for the Protection you are creating.
            

    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]
            The ARN (Amazon Resource Name) of the resource to be protected.
            

    :rtype: dict
    :return: {
        'ProtectionId': 'string'
    }
    
    
    """
    pass

def create_subscription():
    """
    Activates AWS Shield Advanced for an account.
    See also: AWS API Documentation
    
    
    :example: response = client.create_subscription()
    
    
    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_protection(ProtectionId=None):
    """
    Deletes an AWS Shield Advanced  Protection .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_protection(
        ProtectionId='string'
    )
    
    
    :type ProtectionId: string
    :param ProtectionId: [REQUIRED]
            The unique identifier (ID) for the Protection object to be deleted.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_subscription():
    """
    Removes AWS Shield Advanced from an account.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_subscription()
    
    
    :rtype: dict
    :return: {}
    
    
    """
    pass

def describe_attack(AttackId=None):
    """
    Describes the details of a DDoS attack.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_attack(
        AttackId='string'
    )
    
    
    :type AttackId: string
    :param AttackId: [REQUIRED]
            The unique identifier (ID) for the attack that to be described.
            

    :rtype: dict
    :return: {
        'Attack': {
            'AttackId': 'string',
            'ResourceArn': 'string',
            'SubResources': [
                {
                    'Type': 'IP'|'URL',
                    'Id': 'string',
                    'AttackVectors': [
                        {
                            'VectorType': 'string',
                            'VectorCounters': [
                                {
                                    'Name': 'string',
                                    'Max': 123.0,
                                    'Average': 123.0,
                                    'Sum': 123.0,
                                    'N': 123,
                                    'Unit': 'string'
                                },
                            ]
                        },
                    ],
                    'Counters': [
                        {
                            'Name': 'string',
                            'Max': 123.0,
                            'Average': 123.0,
                            'Sum': 123.0,
                            'N': 123,
                            'Unit': 'string'
                        },
                    ]
                },
            ],
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'AttackCounters': [
                {
                    'Name': 'string',
                    'Max': 123.0,
                    'Average': 123.0,
                    'Sum': 123.0,
                    'N': 123,
                    'Unit': 'string'
                },
            ],
            'Mitigations': [
                {
                    'MitigationName': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def describe_protection(ProtectionId=None):
    """
    Lists the details of a  Protection object.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_protection(
        ProtectionId='string'
    )
    
    
    :type ProtectionId: string
    :param ProtectionId: [REQUIRED]
            The unique identifier (ID) for the Protection object that is described.
            

    :rtype: dict
    :return: {
        'Protection': {
            'Id': 'string',
            'Name': 'string',
            'ResourceArn': 'string'
        }
    }
    
    
    """
    pass

def describe_subscription():
    """
    Provides details about the AWS Shield Advanced subscription for an account.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_subscription()
    
    
    :rtype: dict
    :return: {
        'Subscription': {
            'StartTime': datetime(2015, 1, 1),
            'TimeCommitmentInSeconds': 123
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

def list_attacks(ResourceArns=None, StartTime=None, EndTime=None, NextToken=None, MaxResults=None):
    """
    Returns all ongoing DDoS attacks or all DDoS attacks during a specified time period.
    See also: AWS API Documentation
    
    
    :example: response = client.list_attacks(
        ResourceArns=[
            'string',
        ],
        StartTime={
            'FromInclusive': datetime(2015, 1, 1),
            'ToExclusive': datetime(2015, 1, 1)
        },
        EndTime={
            'FromInclusive': datetime(2015, 1, 1),
            'ToExclusive': datetime(2015, 1, 1)
        },
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ResourceArns: list
    :param ResourceArns: The ARN (Amazon Resource Name) of the resource that was attacked. If this is left blank, all applicable resources for this account will be included.
            (string) --
            

    :type StartTime: dict
    :param StartTime: The time period for the attacks.
            FromInclusive (datetime) --The start time, in the format 2016-12-16T13:50Z.
            ToExclusive (datetime) --The end time, in the format 2016-12-16T15:50Z.
            

    :type EndTime: dict
    :param EndTime: The end of the time period for the attacks.
            FromInclusive (datetime) --The start time, in the format 2016-12-16T13:50Z.
            ToExclusive (datetime) --The end time, in the format 2016-12-16T15:50Z.
            

    :type NextToken: string
    :param NextToken: The ListAttacksRequest.NextMarker value from a previous call to ListAttacksRequest . Pass null if this is the first call.

    :type MaxResults: integer
    :param MaxResults: The maximum number of AttackSummary objects to be returned. If this is left blank, the first 20 results will be returned.

    :rtype: dict
    :return: {
        'AttackSummaries': [
            {
                'AttackId': 'string',
                'ResourceArn': 'string',
                'StartTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'AttackVectors': [
                    {
                        'VectorType': 'string'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_protections(NextToken=None, MaxResults=None):
    """
    Lists all  Protection objects for the account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_protections(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: The ListProtectionsRequest.NextToken value from a previous call to ListProtections . Pass null if this is the first call.

    :type MaxResults: integer
    :param MaxResults: The maximum number of Protection objects to be returned. If this is left blank the first 20 results will be returned.

    :rtype: dict
    :return: {
        'Protections': [
            {
                'Id': 'string',
                'Name': 'string',
                'ResourceArn': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

