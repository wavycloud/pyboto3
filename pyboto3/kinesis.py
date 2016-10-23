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


def add_tags_to_stream(StreamName=None, Tags=None):
    """
    :param StreamName: [REQUIRED]
            The name of the stream.
            
    :type StreamName: string
    :param Tags: [REQUIRED]
            The set of key-value pairs to use to create the tags.
            (string) --
            (string) --
            
    :type Tags: dict
    """
    pass


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


def create_stream(StreamName=None, ShardCount=None):
    """
    :param StreamName: [REQUIRED]
            A name to identify the stream. The stream name is scoped to the AWS account used by the application that creates the stream. It is also scoped by region. That is, two streams in two different AWS accounts can have the same name, and two streams in the same AWS account but in two different regions can have the same name.
            
    :type StreamName: string
    :param ShardCount: [REQUIRED]
            The number of shards that the stream will use. The throughput of the stream is a function of the number of shards; more shards are required for greater provisioned throughput.
            DefaultShardLimit;
            
    :type ShardCount: integer
    """
    pass


def decrease_stream_retention_period(StreamName=None, RetentionPeriodHours=None):
    """
    :param StreamName: [REQUIRED]
            The name of the stream to modify.
            
    :type StreamName: string
    :param RetentionPeriodHours: [REQUIRED]
            The new retention period of the stream, in hours. Must be less than the current retention period.
            
    :type RetentionPeriodHours: integer
    """
    pass


def delete_stream(StreamName=None):
    """
    :param StreamName: [REQUIRED]
            The name of the stream to delete.
            ReturnsNone
            
    :type StreamName: string
    """
    pass


def describe_stream(StreamName=None, Limit=None, ExclusiveStartShardId=None):
    """
    :param StreamName: [REQUIRED]
            The name of the stream to describe.
            
    :type StreamName: string
    :param Limit: The maximum number of shards to return.
    :type Limit: integer
    :param ExclusiveStartShardId: The shard ID of the shard to start with.
    :type ExclusiveStartShardId: string
    """
    pass


def disable_enhanced_monitoring(StreamName=None, ShardLevelMetrics=None):
    """
    :param StreamName: [REQUIRED]
            The name of the Amazon Kinesis stream for which to disable enhanced monitoring.
            
    :type StreamName: string
    :param ShardLevelMetrics: [REQUIRED]
            List of shard-level metrics to disable.
            The following are the valid shard-level metrics. The value 'ALL ' disables every metric.
            IncomingBytes
            IncomingRecords
            OutgoingBytes
            OutgoingRecords
            WriteProvisionedThroughputExceeded
            ReadProvisionedThroughputExceeded
            IteratorAgeMilliseconds
            ALL
            For more information, see Monitoring the Amazon Kinesis Streams Service with Amazon CloudWatch in the Amazon Kinesis Streams Developer Guide .
            (string) --
            
    :type ShardLevelMetrics: list
    """
    pass


def enable_enhanced_monitoring(StreamName=None, ShardLevelMetrics=None):
    """
    :param StreamName: [REQUIRED]
            The name of the stream for which to enable enhanced monitoring.
            
    :type StreamName: string
    :param ShardLevelMetrics: [REQUIRED]
            List of shard-level metrics to enable.
            The following are the valid shard-level metrics. The value 'ALL ' enables every metric.
            IncomingBytes
            IncomingRecords
            OutgoingBytes
            OutgoingRecords
            WriteProvisionedThroughputExceeded
            ReadProvisionedThroughputExceeded
            IteratorAgeMilliseconds
            ALL
            For more information, see Monitoring the Amazon Kinesis Streams Service with Amazon CloudWatch in the Amazon Kinesis Streams Developer Guide .
            (string) --
            
    :type ShardLevelMetrics: list
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
            The position in the shard from which you want to start sequentially reading data records. A shard iterator specifies this position using the sequence number of a data record in the shard.
            
    :type ShardIterator: string
    :param Limit: The maximum number of records to return. Specify a value of up to 10,000. If you specify a value that is greater than 10,000, GetRecords throws InvalidArgumentException .
    :type Limit: integer
    """
    pass


def get_shard_iterator(StreamName=None, ShardId=None, ShardIteratorType=None, StartingSequenceNumber=None,
                       Timestamp=None):
    """
    :param StreamName: [REQUIRED]
            The name of the Amazon Kinesis stream.
            
    :type StreamName: string
    :param ShardId: [REQUIRED]
            The shard ID of the Amazon Kinesis shard to get the iterator for.
            
    :type ShardId: string
    :param ShardIteratorType: [REQUIRED]
            Determines how the shard iterator is used to start reading data records from the shard.
            The following are the valid Amazon Kinesis shard iterator types:
            AT_SEQUENCE_NUMBER - Start reading from the position denoted by a specific sequence number, provided in the value StartingSequenceNumber .
            AFTER_SEQUENCE_NUMBER - Start reading right after the position denoted by a specific sequence number, provided in the value StartingSequenceNumber .
            AT_TIMESTAMP - Start reading from the position denoted by a specific timestamp, provided in the value Timestamp .
            TRIM_HORIZON - Start reading at the last untrimmed record in the shard in the system, which is the oldest data record in the shard.
            LATEST - Start reading just after the most recent record in the shard, so that you always read the most recent data in the shard.
            
    :type ShardIteratorType: string
    :param StartingSequenceNumber: The sequence number of the data record in the shard from which to start reading. Used with shard iterator type AT_SEQUENCE_NUMBER and AFTER_SEQUENCE_NUMBER.
    :type StartingSequenceNumber: string
    :param Timestamp: The timestamp of the data record from which to start reading. Used with shard iterator type AT_TIMESTAMP. A timestamp is the Unix epoch date with precision in milliseconds. For example, 2016-04-04T19:58:46.480-00:00 or 1459799926.480 . If a record with this exact timestamp does not exist, the iterator returned is for the next (later) record. If the timestamp is older than the current trim horizon, the iterator returned is for the oldest untrimmed data record (TRIM_HORIZON).
    :type Timestamp: datetime
    """
    pass


def get_waiter():
    """
    """
    pass


def increase_stream_retention_period(StreamName=None, RetentionPeriodHours=None):
    """
    :param StreamName: [REQUIRED]
            The name of the stream to modify.
            
    :type StreamName: string
    :param RetentionPeriodHours: [REQUIRED]
            The new retention period of the stream, in hours. Must be more than the current retention period.
            
    :type RetentionPeriodHours: integer
    """
    pass


def list_streams(Limit=None, ExclusiveStartStreamName=None):
    """
    :param Limit: The maximum number of streams to list.
    :type Limit: integer
    :param ExclusiveStartStreamName: The name of the stream to start the list with.
    :type ExclusiveStartStreamName: string
    """
    pass


def list_tags_for_stream(StreamName=None, ExclusiveStartTagKey=None, Limit=None):
    """
    :param StreamName: [REQUIRED]
            The name of the stream.
            
    :type StreamName: string
    :param ExclusiveStartTagKey: The key to use as the starting point for the list of tags. If this parameter is set, ListTagsForStream gets all tags that occur after ExclusiveStartTagKey .
    :type ExclusiveStartTagKey: string
    :param Limit: The number of tags to return. If this number is less than the total number of tags associated with the stream, HasMoreTags is set to true . To list additional tags, set ExclusiveStartTagKey to the last key in the response.
    :type Limit: integer
    """
    pass


def merge_shards(StreamName=None, ShardToMerge=None, AdjacentShardToMerge=None):
    """
    :param StreamName: [REQUIRED]
            The name of the stream for the merge.
            
    :type StreamName: string
    :param ShardToMerge: [REQUIRED]
            The shard ID of the shard to combine with the adjacent shard for the merge.
            
    :type ShardToMerge: string
    :param AdjacentShardToMerge: [REQUIRED]
            The shard ID of the adjacent shard for the merge.
            
    :type AdjacentShardToMerge: string
    """
    pass


def put_record(StreamName=None, Data=None, PartitionKey=None, ExplicitHashKey=None, SequenceNumberForOrdering=None):
    """
    :param StreamName: [REQUIRED]
            The name of the stream to put the data record into.
            
    :type StreamName: string
    :param Data: [REQUIRED]
            The data blob to put into the record, which is base64-encoded when the blob is serialized. When the data blob (the payload before base64-encoding) is added to the partition key size, the total size must not exceed the maximum record size (1 MB).
            
    :type Data: bytes
    :param PartitionKey: [REQUIRED]
            Determines which shard in the stream the data record is assigned to. Partition keys are Unicode strings with a maximum length limit of 256 characters for each key. Amazon Kinesis uses the partition key as input to a hash function that maps the partition key and associated data to a specific shard. Specifically, an MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards. As a result of this hashing mechanism, all data records with the same partition key map to the same shard within the stream.
            
    :type PartitionKey: string
    :param ExplicitHashKey: The hash value used to explicitly determine the shard the data record is assigned to by overriding the partition key hash.
    :type ExplicitHashKey: string
    :param SequenceNumberForOrdering: Guarantees strictly increasing sequence numbers, for puts from the same client and to the same partition key. Usage: set the SequenceNumberForOrdering of record n to the sequence number of record n-1 (as returned in the result when putting record n-1 ). If this parameter is not set, records will be coarsely ordered based on arrival time.
    :type SequenceNumberForOrdering: string
    """
    pass


def put_records(Records=None, StreamName=None):
    """
    :param Records: [REQUIRED]
            The records associated with the request.
            (dict) --Represents the output for PutRecords .
            Data (bytes) -- [REQUIRED]The data blob to put into the record, which is base64-encoded when the blob is serialized. When the data blob (the payload before base64-encoding) is added to the partition key size, the total size must not exceed the maximum record size (1 MB).
            ExplicitHashKey (string) --The hash value used to determine explicitly the shard that the data record is assigned to by overriding the partition key hash.
            PartitionKey (string) -- [REQUIRED]Determines which shard in the stream the data record is assigned to. Partition keys are Unicode strings with a maximum length limit of 256 characters for each key. Amazon Kinesis uses the partition key as input to a hash function that maps the partition key and associated data to a specific shard. Specifically, an MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards. As a result of this hashing mechanism, all data records with the same partition key map to the same shard within the stream.
            
            
    :type Records: list
    :param StreamName: [REQUIRED]
            The stream name associated with the request.
            
    :type StreamName: string
    """
    pass


def remove_tags_from_stream(StreamName=None, TagKeys=None):
    """
    :param StreamName: [REQUIRED]
            The name of the stream.
            
    :type StreamName: string
    :param TagKeys: [REQUIRED]
            A list of tag keys. Each corresponding tag is removed from the stream.
            (string) --
            
    :type TagKeys: list
    """
    pass


def split_shard(StreamName=None, ShardToSplit=None, NewStartingHashKey=None):
    """
    :param StreamName: [REQUIRED]
            The name of the stream for the shard split.
            
    :type StreamName: string
    :param ShardToSplit: [REQUIRED]
            The shard ID of the shard to split.
            
    :type ShardToSplit: string
    :param NewStartingHashKey: [REQUIRED]
            A hash key value for the starting hash key of one of the child shards created by the split. The hash key range for a given shard constitutes a set of ordered contiguous positive integers. The value for NewStartingHashKey must be in the range of hash keys being mapped into the shard. The NewStartingHashKey hash key value and all higher hash key values in hash key range are distributed to one of the child shards. All the lower hash key values in the range are distributed to the other child shard.
            
    :type NewStartingHashKey: string
    """
    pass
