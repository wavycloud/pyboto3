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

def describe_stream(StreamArn=None, Limit=None, ExclusiveStartShardId=None):
    """
    Returns information about a stream, including the current status of the stream, its Amazon Resource Name (ARN), the composition of its shards, and its corresponding DynamoDB table.
    Each shard in the stream has a SequenceNumberRange associated with it. If the SequenceNumberRange has a StartingSequenceNumber but no EndingSequenceNumber , then the shard is still open (able to receive more stream records). If both StartingSequenceNumber and EndingSequenceNumber are present, then that shard is closed and can no longer receive more data.
    See also: AWS API Documentation
    
    Examples
    The following example describes a stream with a given stream ARN.
    Expected Output:
    
    :example: response = client.describe_stream(
        StreamArn='string',
        Limit=123,
        ExclusiveStartShardId='string'
    )
    
    
    :type StreamArn: string
    :param StreamArn: [REQUIRED]
            The Amazon Resource Name (ARN) for the stream.
            

    :type Limit: integer
    :param Limit: The maximum number of shard objects to return. The upper limit is 100.

    :type ExclusiveStartShardId: string
    :param ExclusiveStartShardId: The shard ID of the first item that this operation will evaluate. Use the value that was returned for LastEvaluatedShardId in the previous operation.

    :rtype: dict
    :return: {
        'StreamDescription': {
            'StreamArn': 'string',
            'StreamLabel': 'string',
            'StreamStatus': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED',
            'StreamViewType': 'NEW_IMAGE'|'OLD_IMAGE'|'NEW_AND_OLD_IMAGES'|'KEYS_ONLY',
            'CreationRequestDateTime': datetime(2015, 1, 1),
            'TableName': 'string',
            'KeySchema': [
                {
                    'AttributeName': 'string',
                    'KeyType': 'HASH'|'RANGE'
                },
            ],
            'Shards': [
                {
                    'ShardId': 'string',
                    'SequenceNumberRange': {
                        'StartingSequenceNumber': 'string',
                        'EndingSequenceNumber': 'string'
                    },
                    'ParentShardId': 'string'
                },
            ],
            'LastEvaluatedShardId': 'string'
        }
    }
    
    
    :returns: 
    the AWS customer ID.
    the table name
    the StreamLabel
    
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

def get_records(ShardIterator=None, Limit=None):
    """
    Retrieves the stream records from a given shard.
    Specify a shard iterator using the ShardIterator parameter. The shard iterator specifies the position in the shard from which you want to start reading stream records sequentially. If there are no stream records available in the portion of the shard that the iterator points to, GetRecords returns an empty list. Note that it might take multiple calls to get to a portion of the shard that contains stream records.
    See also: AWS API Documentation
    
    Examples
    The following example retrieves all the stream records from a shard.
    Expected Output:
    
    :example: response = client.get_records(
        ShardIterator='string',
        Limit=123
    )
    
    
    :type ShardIterator: string
    :param ShardIterator: [REQUIRED]
            A shard iterator that was retrieved from a previous GetShardIterator operation. This iterator can be used to access the stream records in this shard.
            

    :type Limit: integer
    :param Limit: The maximum number of records to return from the shard. The upper limit is 1000.

    :rtype: dict
    :return: {
        'Records': [
            {
                'eventID': 'string',
                'eventName': 'INSERT'|'MODIFY'|'REMOVE',
                'eventVersion': 'string',
                'eventSource': 'string',
                'awsRegion': 'string',
                'dynamodb': {
                    'ApproximateCreationDateTime': datetime(2015, 1, 1),
                    'Keys': {
                        'string': {
                            'S': 'string',
                            'N': 'string',
                            'B': b'bytes',
                            'SS': [
                                'string',
                            ],
                            'NS': [
                                'string',
                            ],
                            'BS': [
                                b'bytes',
                            ],
                            'M': {
                                'string': {'... recursive ...'}
                            },
                            'L': [
                                {'... recursive ...'},
                            ],
                            'NULL': True|False,
                            'BOOL': True|False
                        }
                    },
                    'NewImage': {
                        'string': {
                            'S': 'string',
                            'N': 'string',
                            'B': b'bytes',
                            'SS': [
                                'string',
                            ],
                            'NS': [
                                'string',
                            ],
                            'BS': [
                                b'bytes',
                            ],
                            'M': {
                                'string': {'... recursive ...'}
                            },
                            'L': [
                                {'... recursive ...'},
                            ],
                            'NULL': True|False,
                            'BOOL': True|False
                        }
                    },
                    'OldImage': {
                        'string': {
                            'S': 'string',
                            'N': 'string',
                            'B': b'bytes',
                            'SS': [
                                'string',
                            ],
                            'NS': [
                                'string',
                            ],
                            'BS': [
                                b'bytes',
                            ],
                            'M': {
                                'string': {'... recursive ...'}
                            },
                            'L': [
                                {'... recursive ...'},
                            ],
                            'NULL': True|False,
                            'BOOL': True|False
                        }
                    },
                    'SequenceNumber': 'string',
                    'SizeBytes': 123,
                    'StreamViewType': 'NEW_IMAGE'|'OLD_IMAGE'|'NEW_AND_OLD_IMAGES'|'KEYS_ONLY'
                },
                'userIdentity': {
                    'PrincipalId': 'string',
                    'Type': 'string'
                }
            },
        ],
        'NextShardIterator': 'string'
    }
    
    
    :returns: 
    INSERT - a new item was added to the table.
    MODIFY - one or more of an existing item's attributes were modified.
    REMOVE - the item was deleted from the table
    
    """
    pass

def get_shard_iterator(StreamArn=None, ShardId=None, ShardIteratorType=None, SequenceNumber=None):
    """
    Returns a shard iterator. A shard iterator provides information about how to retrieve the stream records from within a shard. Use the shard iterator in a subsequent GetRecords request to read the stream records from the shard.
    See also: AWS API Documentation
    
    Examples
    The following example returns a shard iterator for the provided stream ARN and shard ID.
    Expected Output:
    
    :example: response = client.get_shard_iterator(
        StreamArn='string',
        ShardId='string',
        ShardIteratorType='TRIM_HORIZON'|'LATEST'|'AT_SEQUENCE_NUMBER'|'AFTER_SEQUENCE_NUMBER',
        SequenceNumber='string'
    )
    
    
    :type StreamArn: string
    :param StreamArn: [REQUIRED]
            The Amazon Resource Name (ARN) for the stream.
            

    :type ShardId: string
    :param ShardId: [REQUIRED]
            The identifier of the shard. The iterator will be returned for this shard ID.
            

    :type ShardIteratorType: string
    :param ShardIteratorType: [REQUIRED]
            Determines how the shard iterator is used to start reading stream records from the shard:
            AT_SEQUENCE_NUMBER - Start reading exactly from the position denoted by a specific sequence number.
            AFTER_SEQUENCE_NUMBER - Start reading right after the position denoted by a specific sequence number.
            TRIM_HORIZON - Start reading at the last (untrimmed) stream record, which is the oldest record in the shard. In DynamoDB Streams, there is a 24 hour limit on data retention. Stream records whose age exceeds this limit are subject to removal (trimming) from the stream.
            LATEST - Start reading just after the most recent stream record in the shard, so that you always read the most recent data in the shard.
            

    :type SequenceNumber: string
    :param SequenceNumber: The sequence number of a stream record in the shard from which to start reading.

    :rtype: dict
    :return: {
        'ShardIterator': 'string'
    }
    
    
    """
    pass

def get_waiter():
    """
    
    """
    pass

def list_streams(TableName=None, Limit=None, ExclusiveStartStreamArn=None):
    """
    Returns an array of stream ARNs associated with the current account and endpoint. If the TableName parameter is present, then ListStreams will return only the streams ARNs for that table.
    See also: AWS API Documentation
    
    Examples
    The following example lists all of the stream ARNs.
    Expected Output:
    
    :example: response = client.list_streams(
        TableName='string',
        Limit=123,
        ExclusiveStartStreamArn='string'
    )
    
    
    :type TableName: string
    :param TableName: If this parameter is provided, then only the streams associated with this table name are returned.

    :type Limit: integer
    :param Limit: The maximum number of streams to return. The upper limit is 100.

    :type ExclusiveStartStreamArn: string
    :param ExclusiveStartStreamArn: The ARN (Amazon Resource Name) of the first item that this operation will evaluate. Use the value that was returned for LastEvaluatedStreamArn in the previous operation.

    :rtype: dict
    :return: {
        'Streams': [
            {
                'StreamArn': 'string',
                'TableName': 'string',
                'StreamLabel': 'string'
            },
        ],
        'LastEvaluatedStreamArn': 'string'
    }
    
    
    :returns: 
    the AWS customer ID.
    the table name
    the StreamLabel
    
    """
    pass

