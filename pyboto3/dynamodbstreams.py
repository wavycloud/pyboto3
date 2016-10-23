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


def describe_stream(StreamArn=None, Limit=None, ExclusiveStartShardId=None):
    """
    :param StreamArn: [REQUIRED]
            The Amazon Resource Name (ARN) for the stream.
            
    :type StreamArn: string
    :param Limit: The maximum number of shard objects to return. The upper limit is 100.
    :type Limit: integer
    :param ExclusiveStartShardId: The shard ID of the first item that this operation will evaluate. Use the value that was returned for LastEvaluatedShardId in the previous operation.
    :type ExclusiveStartShardId: string
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


def get_records(ShardIterator=None, Limit=None):
    """
    :param ShardIterator: [REQUIRED]
            A shard iterator that was retrieved from a previous GetShardIterator operation. This iterator can be used to access the stream records in this shard.
            
    :type ShardIterator: string
    :param Limit: The maximum number of records to return from the shard. The upper limit is 1000.
    :type Limit: integer
    """
    pass


def get_shard_iterator(StreamArn=None, ShardId=None, ShardIteratorType=None, SequenceNumber=None):
    """
    :param StreamArn: [REQUIRED]
            The Amazon Resource Name (ARN) for the stream.
            
    :type StreamArn: string
    :param ShardId: [REQUIRED]
            The identifier of the shard. The iterator will be returned for this shard ID.
            
    :type ShardId: string
    :param ShardIteratorType: [REQUIRED]
            Determines how the shard iterator is used to start reading stream records from the shard:
            AT_SEQUENCE_NUMBER - Start reading exactly from the position denoted by a specific sequence number.
            AFTER_SEQUENCE_NUMBER - Start reading right after the position denoted by a specific sequence number.
            TRIM_HORIZON - Start reading at the last (untrimmed) stream record, which is the oldest record in the shard. In DynamoDB Streams, there is a 24 hour limit on data retention. Stream records whose age exceeds this limit are subject to removal (trimming) from the stream.
            LATEST - Start reading just after the most recent stream record in the shard, so that you always read the most recent data in the shard.
            
    :type ShardIteratorType: string
    :param SequenceNumber: The sequence number of a stream record in the shard from which to start reading.
    :type SequenceNumber: string
    """
    pass


def get_waiter():
    """
    """
    pass


def list_streams(TableName=None, Limit=None, ExclusiveStartStreamArn=None):
    """
    :param TableName: If this parameter is provided, then only the streams associated with this table name are returned.
    :type TableName: string
    :param Limit: The maximum number of streams to return. The upper limit is 100.
    :type Limit: integer
    :param ExclusiveStartStreamArn: The ARN (Amazon Resource Name) of the first item that this operation will evaluate. Use the value that was returned for LastEvaluatedStreamArn in the previous operation.
    :type ExclusiveStartStreamArn: string
    """
    pass
