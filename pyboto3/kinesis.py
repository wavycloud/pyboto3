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

def add_tags_to_stream(StreamName=None, Tags=None):
    """
    Adds or updates tags for the specified Kinesis data stream. Each time you invoke this operation, you can specify up to 10 tags. If you want to add more than 10 tags to your stream, you can invoke this operation multiple times. In total, each stream can have up to 50 tags.
    If tags have already been assigned to the stream, AddTagsToStream overwrites any existing tags that correspond to the specified tag keys.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.add_tags_to_stream(
        StreamName='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]\nThe name of the stream.\n

    :type Tags: dict
    :param Tags: [REQUIRED]\nA set of up to 10 key-value pairs to use to create the tags.\n\n(string) --\n(string) --\n\n\n\n

    :returns: 
    Kinesis.Client.exceptions.ResourceNotFoundException
    Kinesis.Client.exceptions.ResourceInUseException
    Kinesis.Client.exceptions.InvalidArgumentException
    Kinesis.Client.exceptions.LimitExceededException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_stream(StreamName=None, ShardCount=None):
    """
    Creates a Kinesis data stream. A stream captures and transports data records that are continuously emitted from different data sources or producers . Scale-out within a stream is explicitly supported by means of shards, which are uniquely identified groups of data records in a stream.
    You specify and control the number of shards that a stream is composed of. Each shard can support reads up to five transactions per second, up to a maximum data read total of 2 MB per second. Each shard can support writes up to 1,000 records per second, up to a maximum data write total of 1 MB per second. If the amount of data input increases or decreases, you can add or remove shards.
    The stream name identifies the stream. The name is scoped to the AWS account used by the application. It is also scoped by AWS Region. That is, two streams in two different accounts can have the same name, and two streams in the same account, but in two different Regions, can have the same name.
    You receive a LimitExceededException when making a CreateStream request when you try to do one of the following:
    For the default shard limit for an AWS account, see Amazon Kinesis Data Streams Limits in the Amazon Kinesis Data Streams Developer Guide . To increase this limit, contact AWS Support .
    You can use DescribeStream to check the stream status, which is returned in StreamStatus .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_stream(
        StreamName='string',
        ShardCount=123
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]\nA name to identify the stream. The stream name is scoped to the AWS account used by the application that creates the stream. It is also scoped by AWS Region. That is, two streams in two different AWS accounts can have the same name. Two streams in the same AWS account but in two different Regions can also have the same name.\n

    :type ShardCount: integer
    :param ShardCount: [REQUIRED]\nThe number of shards that the stream will use. The throughput of the stream is a function of the number of shards; more shards are required for greater provisioned throughput.\nDefaultShardLimit;\n

    :returns: 
    StreamName (string) -- [REQUIRED]
    A name to identify the stream. The stream name is scoped to the AWS account used by the application that creates the stream. It is also scoped by AWS Region. That is, two streams in two different AWS accounts can have the same name. Two streams in the same AWS account but in two different Regions can also have the same name.
    
    ShardCount (integer) -- [REQUIRED]
    The number of shards that the stream will use. The throughput of the stream is a function of the number of shards; more shards are required for greater provisioned throughput.
    DefaultShardLimit;
    
    
    """
    pass

def decrease_stream_retention_period(StreamName=None, RetentionPeriodHours=None):
    """
    Decreases the Kinesis data stream\'s retention period, which is the length of time data records are accessible after they are added to the stream. The minimum value of a stream\'s retention period is 24 hours.
    This operation may result in lost data. For example, if the stream\'s retention period is 48 hours and is decreased to 24 hours, any data already in the stream that is older than 24 hours is inaccessible.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.decrease_stream_retention_period(
        StreamName='string',
        RetentionPeriodHours=123
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]\nThe name of the stream to modify.\n

    :type RetentionPeriodHours: integer
    :param RetentionPeriodHours: [REQUIRED]\nThe new retention period of the stream, in hours. Must be less than the current retention period.\n

    :returns: 
    Kinesis.Client.exceptions.ResourceInUseException
    Kinesis.Client.exceptions.ResourceNotFoundException
    Kinesis.Client.exceptions.LimitExceededException
    Kinesis.Client.exceptions.InvalidArgumentException
    
    """
    pass

def delete_stream(StreamName=None, EnforceConsumerDeletion=None):
    """
    Deletes a Kinesis data stream and all its shards and data. You must shut down any applications that are operating on the stream before you delete the stream. If an application attempts to operate on a deleted stream, it receives the exception ResourceNotFoundException .
    If the stream is in the ACTIVE state, you can delete it. After a DeleteStream request, the specified stream is in the DELETING state until Kinesis Data Streams completes the deletion.
    When you delete a stream, any shards in that stream are also deleted, and any tags are dissociated from the stream.
    You can use the  DescribeStream operation to check the state of the stream, which is returned in StreamStatus .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_stream(
        StreamName='string',
        EnforceConsumerDeletion=True|False
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]\nThe name of the stream to delete.\n

    :type EnforceConsumerDeletion: boolean
    :param EnforceConsumerDeletion: If this parameter is unset (null ) or if you set it to false , and the stream has registered consumers, the call to DeleteStream fails with a ResourceInUseException .

    :returns: 
    Kinesis.Client.exceptions.ResourceNotFoundException
    Kinesis.Client.exceptions.LimitExceededException
    Kinesis.Client.exceptions.ResourceInUseException
    
    """
    pass

def deregister_stream_consumer(StreamARN=None, ConsumerName=None, ConsumerARN=None):
    """
    To deregister a consumer, provide its ARN. Alternatively, you can provide the ARN of the data stream and the name you gave the consumer when you registered it. You may also provide all three parameters, as long as they don\'t conflict with each other. If you don\'t know the name or ARN of the consumer that you want to deregister, you can use the  ListStreamConsumers operation to get a list of the descriptions of all the consumers that are currently registered with a given data stream. The description of a consumer contains its name and ARN.
    This operation has a limit of five transactions per second per account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.deregister_stream_consumer(
        StreamARN='string',
        ConsumerName='string',
        ConsumerARN='string'
    )
    
    
    :type StreamARN: string
    :param StreamARN: The ARN of the Kinesis data stream that the consumer is registered with. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .

    :type ConsumerName: string
    :param ConsumerName: The name that you gave to the consumer.

    :type ConsumerARN: string
    :param ConsumerARN: The ARN returned by Kinesis Data Streams when you registered the consumer. If you don\'t know the ARN of the consumer that you want to deregister, you can use the ListStreamConsumers operation to get a list of the descriptions of all the consumers that are currently registered with a given data stream. The description of a consumer contains its ARN.

    :returns: 
    Kinesis.Client.exceptions.LimitExceededException
    Kinesis.Client.exceptions.ResourceNotFoundException
    Kinesis.Client.exceptions.InvalidArgumentException
    
    """
    pass

def describe_limits():
    """
    Describes the shard limits and usage for the account.
    If you update your account limits, the old limits might be returned for a few minutes.
    This operation has a limit of one transaction per second per account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_limits()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'ShardLimit': 123,
    'OpenShardCount': 123
}


Response Structure

(dict) --
ShardLimit (integer) --The maximum number of shards.

OpenShardCount (integer) --The number of open shards.






Exceptions

Kinesis.Client.exceptions.LimitExceededException


    :return: {
        'ShardLimit': 123,
        'OpenShardCount': 123
    }
    
    
    """
    pass

def describe_stream(StreamName=None, Limit=None, ExclusiveStartShardId=None):
    """
    Describes the specified Kinesis data stream.
    The information returned includes the stream name, Amazon Resource Name (ARN), creation time, enhanced metric configuration, and shard map. The shard map is an array of shard objects. For each shard object, there is the hash key and sequence number ranges that the shard spans, and the IDs of any earlier shards that played in a role in creating the shard. Every record ingested in the stream is identified by a sequence number, which is assigned when the record is put into the stream.
    You can limit the number of shards returned by each call. For more information, see Retrieving Shards from a Stream in the Amazon Kinesis Data Streams Developer Guide .
    There are no guarantees about the chronological order shards returned. To process shards in chronological order, use the ID of the parent shard to track the lineage to the oldest shard.
    This operation has a limit of 10 transactions per second per account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_stream(
        StreamName='string',
        Limit=123,
        ExclusiveStartShardId='string'
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]\nThe name of the stream to describe.\n

    :type Limit: integer
    :param Limit: The maximum number of shards to return in a single call. The default value is 100. If you specify a value greater than 100, at most 100 shards are returned.

    :type ExclusiveStartShardId: string
    :param ExclusiveStartShardId: The shard ID of the shard to start with.

    :rtype: dict

ReturnsResponse Syntax
{
    'StreamDescription': {
        'StreamName': 'string',
        'StreamARN': 'string',
        'StreamStatus': 'CREATING'|'DELETING'|'ACTIVE'|'UPDATING',
        'Shards': [
            {
                'ShardId': 'string',
                'ParentShardId': 'string',
                'AdjacentParentShardId': 'string',
                'HashKeyRange': {
                    'StartingHashKey': 'string',
                    'EndingHashKey': 'string'
                },
                'SequenceNumberRange': {
                    'StartingSequenceNumber': 'string',
                    'EndingSequenceNumber': 'string'
                }
            },
        ],
        'HasMoreShards': True|False,
        'RetentionPeriodHours': 123,
        'StreamCreationTimestamp': datetime(2015, 1, 1),
        'EnhancedMonitoring': [
            {
                'ShardLevelMetrics': [
                    'IncomingBytes'|'IncomingRecords'|'OutgoingBytes'|'OutgoingRecords'|'WriteProvisionedThroughputExceeded'|'ReadProvisionedThroughputExceeded'|'IteratorAgeMilliseconds'|'ALL',
                ]
            },
        ],
        'EncryptionType': 'NONE'|'KMS',
        'KeyId': 'string'
    }
}


Response Structure

(dict) --
Represents the output for DescribeStream .

StreamDescription (dict) --
The current status of the stream, the stream Amazon Resource Name (ARN), an array of shard objects that comprise the stream, and whether there are more shards available.

StreamName (string) --
The name of the stream being described.

StreamARN (string) --
The Amazon Resource Name (ARN) for the stream being described.

StreamStatus (string) --
The current status of the stream being described. The stream status is one of the following states:

CREATING - The stream is being created. Kinesis Data Streams immediately returns and sets StreamStatus to CREATING .
DELETING - The stream is being deleted. The specified stream is in the DELETING state until Kinesis Data Streams completes the deletion.
ACTIVE - The stream exists and is ready for read and write operations or deletion. You should perform read and write operations only on an ACTIVE stream.
UPDATING - Shards in the stream are being merged or split. Read and write operations continue to work while the stream is in the UPDATING state.


Shards (list) --
The shards that comprise the stream.

(dict) --
A uniquely identified group of data records in a Kinesis data stream.

ShardId (string) --
The unique identifier of the shard within the stream.

ParentShardId (string) --
The shard ID of the shard\'s parent.

AdjacentParentShardId (string) --
The shard ID of the shard adjacent to the shard\'s parent.

HashKeyRange (dict) --
The range of possible hash key values for the shard, which is a set of ordered contiguous positive integers.

StartingHashKey (string) --
The starting hash key of the hash key range.

EndingHashKey (string) --
The ending hash key of the hash key range.



SequenceNumberRange (dict) --
The range of possible sequence numbers for the shard.

StartingSequenceNumber (string) --
The starting sequence number for the range.

EndingSequenceNumber (string) --
The ending sequence number for the range. Shards that are in the OPEN state have an ending sequence number of null .







HasMoreShards (boolean) --
If set to true , more shards in the stream are available to describe.

RetentionPeriodHours (integer) --
The current retention period, in hours.

StreamCreationTimestamp (datetime) --
The approximate time that the stream was created.

EnhancedMonitoring (list) --
Represents the current enhanced monitoring settings of the stream.

(dict) --
Represents enhanced metrics types.

ShardLevelMetrics (list) --
List of shard-level metrics.
The following are the valid shard-level metrics. The value "ALL " enhances every metric.

IncomingBytes
IncomingRecords
OutgoingBytes
OutgoingRecords
WriteProvisionedThroughputExceeded
ReadProvisionedThroughputExceeded
IteratorAgeMilliseconds
ALL

For more information, see Monitoring the Amazon Kinesis Data Streams Service with Amazon CloudWatch in the Amazon Kinesis Data Streams Developer Guide .

(string) --






EncryptionType (string) --
The server-side encryption type used on the stream. This parameter can be one of the following values:

NONE : Do not encrypt the records in the stream.
KMS : Use server-side encryption on the records in the stream using a customer-managed AWS KMS key.


KeyId (string) --
The GUID for the customer-managed AWS KMS key to use for encryption. This value can be a globally unique identifier, a fully specified ARN to either an alias or a key, or an alias name prefixed by "alias/".You can also use a master key owned by Kinesis Data Streams by specifying the alias aws/kinesis .

Key ARN example: arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
Alias ARN example: arn:aws:kms:us-east-1:123456789012:alias/MyAliasName
Globally unique key ID example: 12345678-1234-1234-1234-123456789012
Alias name example: alias/MyAliasName
Master key owned by Kinesis Data Streams: alias/aws/kinesis










Exceptions

Kinesis.Client.exceptions.ResourceNotFoundException
Kinesis.Client.exceptions.LimitExceededException


    :return: {
        'StreamDescription': {
            'StreamName': 'string',
            'StreamARN': 'string',
            'StreamStatus': 'CREATING'|'DELETING'|'ACTIVE'|'UPDATING',
            'Shards': [
                {
                    'ShardId': 'string',
                    'ParentShardId': 'string',
                    'AdjacentParentShardId': 'string',
                    'HashKeyRange': {
                        'StartingHashKey': 'string',
                        'EndingHashKey': 'string'
                    },
                    'SequenceNumberRange': {
                        'StartingSequenceNumber': 'string',
                        'EndingSequenceNumber': 'string'
                    }
                },
            ],
            'HasMoreShards': True|False,
            'RetentionPeriodHours': 123,
            'StreamCreationTimestamp': datetime(2015, 1, 1),
            'EnhancedMonitoring': [
                {
                    'ShardLevelMetrics': [
                        'IncomingBytes'|'IncomingRecords'|'OutgoingBytes'|'OutgoingRecords'|'WriteProvisionedThroughputExceeded'|'ReadProvisionedThroughputExceeded'|'IteratorAgeMilliseconds'|'ALL',
                    ]
                },
            ],
            'EncryptionType': 'NONE'|'KMS',
            'KeyId': 'string'
        }
    }
    
    
    :returns: 
    CREATING - The stream is being created. Kinesis Data Streams immediately returns and sets StreamStatus to CREATING .
    DELETING - The stream is being deleted. The specified stream is in the DELETING state until Kinesis Data Streams completes the deletion.
    ACTIVE - The stream exists and is ready for read and write operations or deletion. You should perform read and write operations only on an ACTIVE stream.
    UPDATING - Shards in the stream are being merged or split. Read and write operations continue to work while the stream is in the UPDATING state.
    
    """
    pass

def describe_stream_consumer(StreamARN=None, ConsumerName=None, ConsumerARN=None):
    """
    To get the description of a registered consumer, provide the ARN of the consumer. Alternatively, you can provide the ARN of the data stream and the name you gave the consumer when you registered it. You may also provide all three parameters, as long as they don\'t conflict with each other. If you don\'t know the name or ARN of the consumer that you want to describe, you can use the  ListStreamConsumers operation to get a list of the descriptions of all the consumers that are currently registered with a given data stream.
    This operation has a limit of 20 transactions per second per account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_stream_consumer(
        StreamARN='string',
        ConsumerName='string',
        ConsumerARN='string'
    )
    
    
    :type StreamARN: string
    :param StreamARN: The ARN of the Kinesis data stream that the consumer is registered with. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .

    :type ConsumerName: string
    :param ConsumerName: The name that you gave to the consumer.

    :type ConsumerARN: string
    :param ConsumerARN: The ARN returned by Kinesis Data Streams when you registered the consumer.

    :rtype: dict

ReturnsResponse Syntax
{
    'ConsumerDescription': {
        'ConsumerName': 'string',
        'ConsumerARN': 'string',
        'ConsumerStatus': 'CREATING'|'DELETING'|'ACTIVE',
        'ConsumerCreationTimestamp': datetime(2015, 1, 1),
        'StreamARN': 'string'
    }
}


Response Structure

(dict) --

ConsumerDescription (dict) --
An object that represents the details of the consumer.

ConsumerName (string) --
The name of the consumer is something you choose when you register the consumer.

ConsumerARN (string) --
When you register a consumer, Kinesis Data Streams generates an ARN for it. You need this ARN to be able to call  SubscribeToShard .
If you delete a consumer and then create a new one with the same name, it won\'t have the same ARN. That\'s because consumer ARNs contain the creation timestamp. This is important to keep in mind if you have IAM policies that reference consumer ARNs.

ConsumerStatus (string) --
A consumer can\'t read data while in the CREATING or DELETING states.

ConsumerCreationTimestamp (datetime) --

StreamARN (string) --
The ARN of the stream with which you registered the consumer.









Exceptions

Kinesis.Client.exceptions.LimitExceededException
Kinesis.Client.exceptions.ResourceNotFoundException
Kinesis.Client.exceptions.InvalidArgumentException


    :return: {
        'ConsumerDescription': {
            'ConsumerName': 'string',
            'ConsumerARN': 'string',
            'ConsumerStatus': 'CREATING'|'DELETING'|'ACTIVE',
            'ConsumerCreationTimestamp': datetime(2015, 1, 1),
            'StreamARN': 'string'
        }
    }
    
    
    :returns: 
    Kinesis.Client.exceptions.LimitExceededException
    Kinesis.Client.exceptions.ResourceNotFoundException
    Kinesis.Client.exceptions.InvalidArgumentException
    
    """
    pass

def describe_stream_summary(StreamName=None):
    """
    Provides a summarized description of the specified Kinesis data stream without the shard list.
    The information returned includes the stream name, Amazon Resource Name (ARN), status, record retention period, approximate creation time, monitoring, encryption details, and open shard count.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_stream_summary(
        StreamName='string'
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]\nThe name of the stream to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'StreamDescriptionSummary': {
        'StreamName': 'string',
        'StreamARN': 'string',
        'StreamStatus': 'CREATING'|'DELETING'|'ACTIVE'|'UPDATING',
        'RetentionPeriodHours': 123,
        'StreamCreationTimestamp': datetime(2015, 1, 1),
        'EnhancedMonitoring': [
            {
                'ShardLevelMetrics': [
                    'IncomingBytes'|'IncomingRecords'|'OutgoingBytes'|'OutgoingRecords'|'WriteProvisionedThroughputExceeded'|'ReadProvisionedThroughputExceeded'|'IteratorAgeMilliseconds'|'ALL',
                ]
            },
        ],
        'EncryptionType': 'NONE'|'KMS',
        'KeyId': 'string',
        'OpenShardCount': 123,
        'ConsumerCount': 123
    }
}


Response Structure

(dict) --
StreamDescriptionSummary (dict) --A  StreamDescriptionSummary containing information about the stream.

StreamName (string) --The name of the stream being described.

StreamARN (string) --The Amazon Resource Name (ARN) for the stream being described.

StreamStatus (string) --The current status of the stream being described. The stream status is one of the following states:

CREATING - The stream is being created. Kinesis Data Streams immediately returns and sets StreamStatus to CREATING .
DELETING - The stream is being deleted. The specified stream is in the DELETING state until Kinesis Data Streams completes the deletion.
ACTIVE - The stream exists and is ready for read and write operations or deletion. You should perform read and write operations only on an ACTIVE stream.
UPDATING - Shards in the stream are being merged or split. Read and write operations continue to work while the stream is in the UPDATING state.


RetentionPeriodHours (integer) --The current retention period, in hours.

StreamCreationTimestamp (datetime) --The approximate time that the stream was created.

EnhancedMonitoring (list) --Represents the current enhanced monitoring settings of the stream.

(dict) --Represents enhanced metrics types.

ShardLevelMetrics (list) --List of shard-level metrics.
The following are the valid shard-level metrics. The value "ALL " enhances every metric.

IncomingBytes
IncomingRecords
OutgoingBytes
OutgoingRecords
WriteProvisionedThroughputExceeded
ReadProvisionedThroughputExceeded
IteratorAgeMilliseconds
ALL

For more information, see Monitoring the Amazon Kinesis Data Streams Service with Amazon CloudWatch in the Amazon Kinesis Data Streams Developer Guide .

(string) --






EncryptionType (string) --The encryption type used. This value is one of the following:

KMS
NONE


KeyId (string) --The GUID for the customer-managed AWS KMS key to use for encryption. This value can be a globally unique identifier, a fully specified ARN to either an alias or a key, or an alias name prefixed by "alias/".You can also use a master key owned by Kinesis Data Streams by specifying the alias aws/kinesis .

Key ARN example: arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
Alias ARN example: arn:aws:kms:us-east-1:123456789012:alias/MyAliasName
Globally unique key ID example: 12345678-1234-1234-1234-123456789012
Alias name example: alias/MyAliasName
Master key owned by Kinesis Data Streams: alias/aws/kinesis


OpenShardCount (integer) --The number of open shards in the stream.

ConsumerCount (integer) --The number of enhanced fan-out consumers registered with the stream.








Exceptions

Kinesis.Client.exceptions.ResourceNotFoundException
Kinesis.Client.exceptions.LimitExceededException


    :return: {
        'StreamDescriptionSummary': {
            'StreamName': 'string',
            'StreamARN': 'string',
            'StreamStatus': 'CREATING'|'DELETING'|'ACTIVE'|'UPDATING',
            'RetentionPeriodHours': 123,
            'StreamCreationTimestamp': datetime(2015, 1, 1),
            'EnhancedMonitoring': [
                {
                    'ShardLevelMetrics': [
                        'IncomingBytes'|'IncomingRecords'|'OutgoingBytes'|'OutgoingRecords'|'WriteProvisionedThroughputExceeded'|'ReadProvisionedThroughputExceeded'|'IteratorAgeMilliseconds'|'ALL',
                    ]
                },
            ],
            'EncryptionType': 'NONE'|'KMS',
            'KeyId': 'string',
            'OpenShardCount': 123,
            'ConsumerCount': 123
        }
    }
    
    
    :returns: 
    IncomingBytes
    IncomingRecords
    OutgoingBytes
    OutgoingRecords
    WriteProvisionedThroughputExceeded
    ReadProvisionedThroughputExceeded
    IteratorAgeMilliseconds
    ALL
    
    """
    pass

def disable_enhanced_monitoring(StreamName=None, ShardLevelMetrics=None):
    """
    Disables enhanced monitoring.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disable_enhanced_monitoring(
        StreamName='string',
        ShardLevelMetrics=[
            'IncomingBytes'|'IncomingRecords'|'OutgoingBytes'|'OutgoingRecords'|'WriteProvisionedThroughputExceeded'|'ReadProvisionedThroughputExceeded'|'IteratorAgeMilliseconds'|'ALL',
        ]
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]\nThe name of the Kinesis data stream for which to disable enhanced monitoring.\n

    :type ShardLevelMetrics: list
    :param ShardLevelMetrics: [REQUIRED]\nList of shard-level metrics to disable.\nThe following are the valid shard-level metrics. The value 'ALL ' disables every metric.\n\nIncomingBytes\nIncomingRecords\nOutgoingBytes\nOutgoingRecords\nWriteProvisionedThroughputExceeded\nReadProvisionedThroughputExceeded\nIteratorAgeMilliseconds\nALL\n\nFor more information, see Monitoring the Amazon Kinesis Data Streams Service with Amazon CloudWatch in the Amazon Kinesis Data Streams Developer Guide .\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'StreamName': 'string',
    'CurrentShardLevelMetrics': [
        'IncomingBytes'|'IncomingRecords'|'OutgoingBytes'|'OutgoingRecords'|'WriteProvisionedThroughputExceeded'|'ReadProvisionedThroughputExceeded'|'IteratorAgeMilliseconds'|'ALL',
    ],
    'DesiredShardLevelMetrics': [
        'IncomingBytes'|'IncomingRecords'|'OutgoingBytes'|'OutgoingRecords'|'WriteProvisionedThroughputExceeded'|'ReadProvisionedThroughputExceeded'|'IteratorAgeMilliseconds'|'ALL',
    ]
}


Response Structure

(dict) --
Represents the output for  EnableEnhancedMonitoring and  DisableEnhancedMonitoring .

StreamName (string) --
The name of the Kinesis data stream.

CurrentShardLevelMetrics (list) --
Represents the current state of the metrics that are in the enhanced state before the operation.

(string) --


DesiredShardLevelMetrics (list) --
Represents the list of all the metrics that would be in the enhanced state after the operation.

(string) --








Exceptions

Kinesis.Client.exceptions.InvalidArgumentException
Kinesis.Client.exceptions.LimitExceededException
Kinesis.Client.exceptions.ResourceInUseException
Kinesis.Client.exceptions.ResourceNotFoundException


    :return: {
        'StreamName': 'string',
        'CurrentShardLevelMetrics': [
            'IncomingBytes'|'IncomingRecords'|'OutgoingBytes'|'OutgoingRecords'|'WriteProvisionedThroughputExceeded'|'ReadProvisionedThroughputExceeded'|'IteratorAgeMilliseconds'|'ALL',
        ],
        'DesiredShardLevelMetrics': [
            'IncomingBytes'|'IncomingRecords'|'OutgoingBytes'|'OutgoingRecords'|'WriteProvisionedThroughputExceeded'|'ReadProvisionedThroughputExceeded'|'IteratorAgeMilliseconds'|'ALL',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def enable_enhanced_monitoring(StreamName=None, ShardLevelMetrics=None):
    """
    Enables enhanced Kinesis data stream monitoring for shard-level metrics.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.enable_enhanced_monitoring(
        StreamName='string',
        ShardLevelMetrics=[
            'IncomingBytes'|'IncomingRecords'|'OutgoingBytes'|'OutgoingRecords'|'WriteProvisionedThroughputExceeded'|'ReadProvisionedThroughputExceeded'|'IteratorAgeMilliseconds'|'ALL',
        ]
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]\nThe name of the stream for which to enable enhanced monitoring.\n

    :type ShardLevelMetrics: list
    :param ShardLevelMetrics: [REQUIRED]\nList of shard-level metrics to enable.\nThe following are the valid shard-level metrics. The value 'ALL ' enables every metric.\n\nIncomingBytes\nIncomingRecords\nOutgoingBytes\nOutgoingRecords\nWriteProvisionedThroughputExceeded\nReadProvisionedThroughputExceeded\nIteratorAgeMilliseconds\nALL\n\nFor more information, see Monitoring the Amazon Kinesis Data Streams Service with Amazon CloudWatch in the Amazon Kinesis Data Streams Developer Guide .\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'StreamName': 'string',
    'CurrentShardLevelMetrics': [
        'IncomingBytes'|'IncomingRecords'|'OutgoingBytes'|'OutgoingRecords'|'WriteProvisionedThroughputExceeded'|'ReadProvisionedThroughputExceeded'|'IteratorAgeMilliseconds'|'ALL',
    ],
    'DesiredShardLevelMetrics': [
        'IncomingBytes'|'IncomingRecords'|'OutgoingBytes'|'OutgoingRecords'|'WriteProvisionedThroughputExceeded'|'ReadProvisionedThroughputExceeded'|'IteratorAgeMilliseconds'|'ALL',
    ]
}


Response Structure

(dict) --
Represents the output for  EnableEnhancedMonitoring and  DisableEnhancedMonitoring .

StreamName (string) --
The name of the Kinesis data stream.

CurrentShardLevelMetrics (list) --
Represents the current state of the metrics that are in the enhanced state before the operation.

(string) --


DesiredShardLevelMetrics (list) --
Represents the list of all the metrics that would be in the enhanced state after the operation.

(string) --








Exceptions

Kinesis.Client.exceptions.InvalidArgumentException
Kinesis.Client.exceptions.LimitExceededException
Kinesis.Client.exceptions.ResourceInUseException
Kinesis.Client.exceptions.ResourceNotFoundException


    :return: {
        'StreamName': 'string',
        'CurrentShardLevelMetrics': [
            'IncomingBytes'|'IncomingRecords'|'OutgoingBytes'|'OutgoingRecords'|'WriteProvisionedThroughputExceeded'|'ReadProvisionedThroughputExceeded'|'IteratorAgeMilliseconds'|'ALL',
        ],
        'DesiredShardLevelMetrics': [
            'IncomingBytes'|'IncomingRecords'|'OutgoingBytes'|'OutgoingRecords'|'WriteProvisionedThroughputExceeded'|'ReadProvisionedThroughputExceeded'|'IteratorAgeMilliseconds'|'ALL',
        ]
    }
    
    
    :returns: 
    (string) --
    
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

def get_records(ShardIterator=None, Limit=None):
    """
    Gets data records from a Kinesis data stream\'s shard.
    Specify a shard iterator using the ShardIterator parameter. The shard iterator specifies the position in the shard from which you want to start reading data records sequentially. If there are no records available in the portion of the shard that the iterator points to,  GetRecords returns an empty list. It might take multiple calls to get to a portion of the shard that contains records.
    You can scale by provisioning multiple shards per stream while considering service limits (for more information, see Amazon Kinesis Data Streams Limits in the Amazon Kinesis Data Streams Developer Guide ). Your application should have one thread per shard, each reading continuously from its stream. To read from a stream continually, call  GetRecords in a loop. Use  GetShardIterator to get the shard iterator to specify in the first  GetRecords call.  GetRecords returns a new shard iterator in NextShardIterator . Specify the shard iterator returned in NextShardIterator in subsequent calls to  GetRecords . If the shard has been closed, the shard iterator can\'t return more data and  GetRecords returns null in NextShardIterator . You can terminate the loop when the shard is closed, or when the shard iterator reaches the record with the sequence number or other attribute that marks it as the last record to process.
    Each data record can be up to 1 MiB in size, and each shard can read up to 2 MiB per second. You can ensure that your calls don\'t exceed the maximum supported size or throughput by using the Limit parameter to specify the maximum number of records that  GetRecords can return. Consider your average record size when determining this limit. The maximum number of records that can be returned per call is 10,000.
    The size of the data returned by  GetRecords varies depending on the utilization of the shard. The maximum size of data that  GetRecords can return is 10 MiB. If a call returns this amount of data, subsequent calls made within the next 5 seconds throw ProvisionedThroughputExceededException . If there is insufficient provisioned throughput on the stream, subsequent calls made within the next 1 second throw ProvisionedThroughputExceededException .  GetRecords doesn\'t return any data when it throws an exception. For this reason, we recommend that you wait 1 second between calls to  GetRecords . However, it\'s possible that the application will get exceptions for longer than 1 second.
    To detect whether the application is falling behind in processing, you can use the MillisBehindLatest response attribute. You can also monitor the stream using CloudWatch metrics and other mechanisms (see Monitoring in the Amazon Kinesis Data Streams Developer Guide ).
    Each Amazon Kinesis record includes a value, ApproximateArrivalTimestamp , that is set when a stream successfully receives and stores a record. This is commonly referred to as a server-side time stamp, whereas a client-side time stamp is set when a data producer creates or sends the record to a stream (a data producer is any data source putting data records into a stream, for example with  PutRecords ). The time stamp has millisecond precision. There are no guarantees about the time stamp accuracy, or that the time stamp is always increasing. For example, records in a shard or across a stream might have time stamps that are out of order.
    This operation has a limit of five transactions per second per account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_records(
        ShardIterator='string',
        Limit=123
    )
    
    
    :type ShardIterator: string
    :param ShardIterator: [REQUIRED]\nThe position in the shard from which you want to start sequentially reading data records. A shard iterator specifies this position using the sequence number of a data record in the shard.\n

    :type Limit: integer
    :param Limit: The maximum number of records to return. Specify a value of up to 10,000. If you specify a value that is greater than 10,000, GetRecords throws InvalidArgumentException .

    :rtype: dict

ReturnsResponse Syntax
{
    'Records': [
        {
            'SequenceNumber': 'string',
            'ApproximateArrivalTimestamp': datetime(2015, 1, 1),
            'Data': b'bytes',
            'PartitionKey': 'string',
            'EncryptionType': 'NONE'|'KMS'
        },
    ],
    'NextShardIterator': 'string',
    'MillisBehindLatest': 123
}


Response Structure

(dict) --
Represents the output for  GetRecords .

Records (list) --
The data records retrieved from the shard.

(dict) --
The unit of data of the Kinesis data stream, which is composed of a sequence number, a partition key, and a data blob.

SequenceNumber (string) --
The unique identifier of the record within its shard.

ApproximateArrivalTimestamp (datetime) --
The approximate time that the record was inserted into the stream.

Data (bytes) --
The data blob. The data in the blob is both opaque and immutable to Kinesis Data Streams, which does not inspect, interpret, or change the data in the blob in any way. When the data blob (the payload before base64-encoding) is added to the partition key size, the total size must not exceed the maximum record size (1 MB).

PartitionKey (string) --
Identifies which shard in the stream the data record is assigned to.

EncryptionType (string) --
The encryption type used on the record. This parameter can be one of the following values:

NONE : Do not encrypt the records in the stream.
KMS : Use server-side encryption on the records in the stream using a customer-managed AWS KMS key.






NextShardIterator (string) --
The next position in the shard from which to start sequentially reading data records. If set to null , the shard has been closed and the requested iterator does not return any more data.

MillisBehindLatest (integer) --
The number of milliseconds the  GetRecords response is from the tip of the stream, indicating how far behind current time the consumer is. A value of zero indicates that record processing is caught up, and there are no new records to process at this moment.







Exceptions

Kinesis.Client.exceptions.ResourceNotFoundException
Kinesis.Client.exceptions.InvalidArgumentException
Kinesis.Client.exceptions.ProvisionedThroughputExceededException
Kinesis.Client.exceptions.ExpiredIteratorException
Kinesis.Client.exceptions.KMSDisabledException
Kinesis.Client.exceptions.KMSInvalidStateException
Kinesis.Client.exceptions.KMSAccessDeniedException
Kinesis.Client.exceptions.KMSNotFoundException
Kinesis.Client.exceptions.KMSOptInRequired
Kinesis.Client.exceptions.KMSThrottlingException


    :return: {
        'Records': [
            {
                'SequenceNumber': 'string',
                'ApproximateArrivalTimestamp': datetime(2015, 1, 1),
                'Data': b'bytes',
                'PartitionKey': 'string',
                'EncryptionType': 'NONE'|'KMS'
            },
        ],
        'NextShardIterator': 'string',
        'MillisBehindLatest': 123
    }
    
    
    :returns: 
    NONE : Do not encrypt the records in the stream.
    KMS : Use server-side encryption on the records in the stream using a customer-managed AWS KMS key.
    
    """
    pass

def get_shard_iterator(StreamName=None, ShardId=None, ShardIteratorType=None, StartingSequenceNumber=None, Timestamp=None):
    """
    Gets an Amazon Kinesis shard iterator. A shard iterator expires 5 minutes after it is returned to the requester.
    A shard iterator specifies the shard position from which to start reading data records sequentially. The position is specified using the sequence number of a data record in a shard. A sequence number is the identifier associated with every record ingested in the stream, and is assigned when a record is put into the stream. Each stream has one or more shards.
    You must specify the shard iterator type. For example, you can set the ShardIteratorType parameter to read exactly from the position denoted by a specific sequence number by using the AT_SEQUENCE_NUMBER shard iterator type. Alternatively, the parameter can read right after the sequence number by using the AFTER_SEQUENCE_NUMBER shard iterator type, using sequence numbers returned by earlier calls to  PutRecord ,  PutRecords ,  GetRecords , or  DescribeStream . In the request, you can specify the shard iterator type AT_TIMESTAMP to read records from an arbitrary point in time, TRIM_HORIZON to cause ShardIterator to point to the last untrimmed record in the shard in the system (the oldest data record in the shard), or LATEST so that you always read the most recent data in the shard.
    When you read repeatedly from a stream, use a  GetShardIterator request to get the first shard iterator for use in your first  GetRecords request and for subsequent reads use the shard iterator returned by the  GetRecords request in NextShardIterator . A new shard iterator is returned by every  GetRecords request in NextShardIterator , which you use in the ShardIterator parameter of the next  GetRecords request.
    If a  GetShardIterator request is made too often, you receive a ProvisionedThroughputExceededException . For more information about throughput limits, see  GetRecords , and Streams Limits in the Amazon Kinesis Data Streams Developer Guide .
    If the shard is closed,  GetShardIterator returns a valid iterator for the last sequence number of the shard. A shard can be closed as a result of using  SplitShard or  MergeShards .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_shard_iterator(
        StreamName='string',
        ShardId='string',
        ShardIteratorType='AT_SEQUENCE_NUMBER'|'AFTER_SEQUENCE_NUMBER'|'TRIM_HORIZON'|'LATEST'|'AT_TIMESTAMP',
        StartingSequenceNumber='string',
        Timestamp=datetime(2015, 1, 1)
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]\nThe name of the Amazon Kinesis data stream.\n

    :type ShardId: string
    :param ShardId: [REQUIRED]\nThe shard ID of the Kinesis Data Streams shard to get the iterator for.\n

    :type ShardIteratorType: string
    :param ShardIteratorType: [REQUIRED]\nDetermines how the shard iterator is used to start reading data records from the shard.\nThe following are the valid Amazon Kinesis shard iterator types:\n\nAT_SEQUENCE_NUMBER - Start reading from the position denoted by a specific sequence number, provided in the value StartingSequenceNumber .\nAFTER_SEQUENCE_NUMBER - Start reading right after the position denoted by a specific sequence number, provided in the value StartingSequenceNumber .\nAT_TIMESTAMP - Start reading from the position denoted by a specific time stamp, provided in the value Timestamp .\nTRIM_HORIZON - Start reading at the last untrimmed record in the shard in the system, which is the oldest data record in the shard.\nLATEST - Start reading just after the most recent record in the shard, so that you always read the most recent data in the shard.\n\n

    :type StartingSequenceNumber: string
    :param StartingSequenceNumber: The sequence number of the data record in the shard from which to start reading. Used with shard iterator type AT_SEQUENCE_NUMBER and AFTER_SEQUENCE_NUMBER.

    :type Timestamp: datetime
    :param Timestamp: The time stamp of the data record from which to start reading. Used with shard iterator type AT_TIMESTAMP. A time stamp is the Unix epoch date with precision in milliseconds. For example, 2016-04-04T19:58:46.480-00:00 or 1459799926.480 . If a record with this exact time stamp does not exist, the iterator returned is for the next (later) record. If the time stamp is older than the current trim horizon, the iterator returned is for the oldest untrimmed data record (TRIM_HORIZON).

    :rtype: dict

ReturnsResponse Syntax
{
    'ShardIterator': 'string'
}


Response Structure

(dict) --
Represents the output for GetShardIterator .

ShardIterator (string) --
The position in the shard from which to start reading data records sequentially. A shard iterator specifies this position using the sequence number of a data record in a shard.







Exceptions

Kinesis.Client.exceptions.ResourceNotFoundException
Kinesis.Client.exceptions.InvalidArgumentException
Kinesis.Client.exceptions.ProvisionedThroughputExceededException


    :return: {
        'ShardIterator': 'string'
    }
    
    
    :returns: 
    Kinesis.Client.exceptions.ResourceNotFoundException
    Kinesis.Client.exceptions.InvalidArgumentException
    Kinesis.Client.exceptions.ProvisionedThroughputExceededException
    
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

def increase_stream_retention_period(StreamName=None, RetentionPeriodHours=None):
    """
    Increases the Kinesis data stream\'s retention period, which is the length of time data records are accessible after they are added to the stream. The maximum value of a stream\'s retention period is 168 hours (7 days).
    If you choose a longer stream retention period, this operation increases the time period during which records that have not yet expired are accessible. However, it does not make previous, expired data (older than the stream\'s previous retention period) accessible after the operation has been called. For example, if a stream\'s retention period is set to 24 hours and is increased to 168 hours, any data that is older than 24 hours remains inaccessible to consumer applications.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.increase_stream_retention_period(
        StreamName='string',
        RetentionPeriodHours=123
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]\nThe name of the stream to modify.\n

    :type RetentionPeriodHours: integer
    :param RetentionPeriodHours: [REQUIRED]\nThe new retention period of the stream, in hours. Must be more than the current retention period.\n

    :returns: 
    Kinesis.Client.exceptions.ResourceInUseException
    Kinesis.Client.exceptions.ResourceNotFoundException
    Kinesis.Client.exceptions.LimitExceededException
    Kinesis.Client.exceptions.InvalidArgumentException
    
    """
    pass

def list_shards(StreamName=None, NextToken=None, ExclusiveStartShardId=None, MaxResults=None, StreamCreationTimestamp=None):
    """
    Lists the shards in a stream and provides information about each shard. This operation has a limit of 100 transactions per second per data stream.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_shards(
        StreamName='string',
        NextToken='string',
        ExclusiveStartShardId='string',
        MaxResults=123,
        StreamCreationTimestamp=datetime(2015, 1, 1)
    )
    
    
    :type StreamName: string
    :param StreamName: The name of the data stream whose shards you want to list.\nYou cannot specify this parameter if you specify the NextToken parameter.\n

    :type NextToken: string
    :param NextToken: When the number of shards in the data stream is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of shards in the data stream, the response includes a pagination token named NextToken . You can specify this NextToken value in a subsequent call to ListShards to list the next set of shards.\nDon\'t specify StreamName or StreamCreationTimestamp if you specify NextToken because the latter unambiguously identifies the stream.\nYou can optionally specify a value for the MaxResults parameter when you specify NextToken . If you specify a MaxResults value that is less than the number of shards that the operation returns if you don\'t specify MaxResults , the response will contain a new NextToken value. You can use the new NextToken value in a subsequent call to the ListShards operation.\n\nWarning\nTokens expire after 300 seconds. When you obtain a value for NextToken in the response to a call to ListShards , you have 300 seconds to use that value. If you specify an expired token in a call to ListShards , you get ExpiredNextTokenException .\n\n

    :type ExclusiveStartShardId: string
    :param ExclusiveStartShardId: Specify this parameter to indicate that you want to list the shards starting with the shard whose ID immediately follows ExclusiveStartShardId .\nIf you don\'t specify this parameter, the default behavior is for ListShards to list the shards starting with the first one in the stream.\nYou cannot specify this parameter if you specify NextToken .\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of shards to return in a single call to ListShards . The minimum value you can specify for this parameter is 1, and the maximum is 1,000, which is also the default.\nWhen the number of shards to be listed is greater than the value of MaxResults , the response contains a NextToken value that you can use in a subsequent call to ListShards to list the next set of shards.\n

    :type StreamCreationTimestamp: datetime
    :param StreamCreationTimestamp: Specify this input parameter to distinguish data streams that have the same name. For example, if you create a data stream and then delete it, and you later create another data stream with the same name, you can use this input parameter to specify which of the two streams you want to list the shards for.\nYou cannot specify this parameter if you specify the NextToken parameter.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Shards': [
        {
            'ShardId': 'string',
            'ParentShardId': 'string',
            'AdjacentParentShardId': 'string',
            'HashKeyRange': {
                'StartingHashKey': 'string',
                'EndingHashKey': 'string'
            },
            'SequenceNumberRange': {
                'StartingSequenceNumber': 'string',
                'EndingSequenceNumber': 'string'
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Shards (list) --
An array of JSON objects. Each object represents one shard and specifies the IDs of the shard, the shard\'s parent, and the shard that\'s adjacent to the shard\'s parent. Each object also contains the starting and ending hash keys and the starting and ending sequence numbers for the shard.

(dict) --
A uniquely identified group of data records in a Kinesis data stream.

ShardId (string) --
The unique identifier of the shard within the stream.

ParentShardId (string) --
The shard ID of the shard\'s parent.

AdjacentParentShardId (string) --
The shard ID of the shard adjacent to the shard\'s parent.

HashKeyRange (dict) --
The range of possible hash key values for the shard, which is a set of ordered contiguous positive integers.

StartingHashKey (string) --
The starting hash key of the hash key range.

EndingHashKey (string) --
The ending hash key of the hash key range.



SequenceNumberRange (dict) --
The range of possible sequence numbers for the shard.

StartingSequenceNumber (string) --
The starting sequence number for the range.

EndingSequenceNumber (string) --
The ending sequence number for the range. Shards that are in the OPEN state have an ending sequence number of null .







NextToken (string) --
When the number of shards in the data stream is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of shards in the data stream, the response includes a pagination token named NextToken . You can specify this NextToken value in a subsequent call to ListShards to list the next set of shards. For more information about the use of this pagination token when calling the ListShards operation, see  ListShardsInput$NextToken .

Warning
Tokens expire after 300 seconds. When you obtain a value for NextToken in the response to a call to ListShards , you have 300 seconds to use that value. If you specify an expired token in a call to ListShards , you get ExpiredNextTokenException .








Exceptions

Kinesis.Client.exceptions.ResourceNotFoundException
Kinesis.Client.exceptions.InvalidArgumentException
Kinesis.Client.exceptions.LimitExceededException
Kinesis.Client.exceptions.ExpiredNextTokenException
Kinesis.Client.exceptions.ResourceInUseException


    :return: {
        'Shards': [
            {
                'ShardId': 'string',
                'ParentShardId': 'string',
                'AdjacentParentShardId': 'string',
                'HashKeyRange': {
                    'StartingHashKey': 'string',
                    'EndingHashKey': 'string'
                },
                'SequenceNumberRange': {
                    'StartingSequenceNumber': 'string',
                    'EndingSequenceNumber': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Kinesis.Client.exceptions.ResourceNotFoundException
    Kinesis.Client.exceptions.InvalidArgumentException
    Kinesis.Client.exceptions.LimitExceededException
    Kinesis.Client.exceptions.ExpiredNextTokenException
    Kinesis.Client.exceptions.ResourceInUseException
    
    """
    pass

def list_stream_consumers(StreamARN=None, NextToken=None, MaxResults=None, StreamCreationTimestamp=None):
    """
    Lists the consumers registered to receive data from a stream using enhanced fan-out, and provides information about each consumer.
    This operation has a limit of 10 transactions per second per account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_stream_consumers(
        StreamARN='string',
        NextToken='string',
        MaxResults=123,
        StreamCreationTimestamp=datetime(2015, 1, 1)
    )
    
    
    :type StreamARN: string
    :param StreamARN: [REQUIRED]\nThe ARN of the Kinesis data stream for which you want to list the registered consumers. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n

    :type NextToken: string
    :param NextToken: When the number of consumers that are registered with the data stream is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of consumers that are registered with the data stream, the response includes a pagination token named NextToken . You can specify this NextToken value in a subsequent call to ListStreamConsumers to list the next set of registered consumers.\nDon\'t specify StreamName or StreamCreationTimestamp if you specify NextToken because the latter unambiguously identifies the stream.\nYou can optionally specify a value for the MaxResults parameter when you specify NextToken . If you specify a MaxResults value that is less than the number of consumers that the operation returns if you don\'t specify MaxResults , the response will contain a new NextToken value. You can use the new NextToken value in a subsequent call to the ListStreamConsumers operation to list the next set of consumers.\n\nWarning\nTokens expire after 300 seconds. When you obtain a value for NextToken in the response to a call to ListStreamConsumers , you have 300 seconds to use that value. If you specify an expired token in a call to ListStreamConsumers , you get ExpiredNextTokenException .\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of consumers that you want a single call of ListStreamConsumers to return.

    :type StreamCreationTimestamp: datetime
    :param StreamCreationTimestamp: Specify this input parameter to distinguish data streams that have the same name. For example, if you create a data stream and then delete it, and you later create another data stream with the same name, you can use this input parameter to specify which of the two streams you want to list the consumers for.\nYou can\'t specify this parameter if you specify the NextToken parameter.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Consumers': [
        {
            'ConsumerName': 'string',
            'ConsumerARN': 'string',
            'ConsumerStatus': 'CREATING'|'DELETING'|'ACTIVE',
            'ConsumerCreationTimestamp': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Consumers (list) --
An array of JSON objects. Each object represents one registered consumer.

(dict) --
An object that represents the details of the consumer you registered.

ConsumerName (string) --
The name of the consumer is something you choose when you register the consumer.

ConsumerARN (string) --
When you register a consumer, Kinesis Data Streams generates an ARN for it. You need this ARN to be able to call  SubscribeToShard .
If you delete a consumer and then create a new one with the same name, it won\'t have the same ARN. That\'s because consumer ARNs contain the creation timestamp. This is important to keep in mind if you have IAM policies that reference consumer ARNs.

ConsumerStatus (string) --
A consumer can\'t read data while in the CREATING or DELETING states.

ConsumerCreationTimestamp (datetime) --





NextToken (string) --
When the number of consumers that are registered with the data stream is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of registered consumers, the response includes a pagination token named NextToken . You can specify this NextToken value in a subsequent call to ListStreamConsumers to list the next set of registered consumers. For more information about the use of this pagination token when calling the ListStreamConsumers operation, see  ListStreamConsumersInput$NextToken .

Warning
Tokens expire after 300 seconds. When you obtain a value for NextToken in the response to a call to ListStreamConsumers , you have 300 seconds to use that value. If you specify an expired token in a call to ListStreamConsumers , you get ExpiredNextTokenException .








Exceptions

Kinesis.Client.exceptions.ResourceNotFoundException
Kinesis.Client.exceptions.InvalidArgumentException
Kinesis.Client.exceptions.LimitExceededException
Kinesis.Client.exceptions.ExpiredNextTokenException
Kinesis.Client.exceptions.ResourceInUseException


    :return: {
        'Consumers': [
            {
                'ConsumerName': 'string',
                'ConsumerARN': 'string',
                'ConsumerStatus': 'CREATING'|'DELETING'|'ACTIVE',
                'ConsumerCreationTimestamp': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Kinesis.Client.exceptions.ResourceNotFoundException
    Kinesis.Client.exceptions.InvalidArgumentException
    Kinesis.Client.exceptions.LimitExceededException
    Kinesis.Client.exceptions.ExpiredNextTokenException
    Kinesis.Client.exceptions.ResourceInUseException
    
    """
    pass

def list_streams(Limit=None, ExclusiveStartStreamName=None):
    """
    Lists your Kinesis data streams.
    The number of streams may be too large to return from a single call to ListStreams . You can limit the number of returned streams using the Limit parameter. If you do not specify a value for the Limit parameter, Kinesis Data Streams uses the default limit, which is currently 10.
    You can detect if there are more streams available to list by using the HasMoreStreams flag from the returned output. If there are more streams available, you can request more streams by using the name of the last stream returned by the ListStreams request in the ExclusiveStartStreamName parameter in a subsequent request to ListStreams . The group of stream names returned by the subsequent request is then added to the list. You can continue this process until all the stream names have been collected in the list.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_streams(
        Limit=123,
        ExclusiveStartStreamName='string'
    )
    
    
    :type Limit: integer
    :param Limit: The maximum number of streams to list.

    :type ExclusiveStartStreamName: string
    :param ExclusiveStartStreamName: The name of the stream to start the list with.

    :rtype: dict

ReturnsResponse Syntax
{
    'StreamNames': [
        'string',
    ],
    'HasMoreStreams': True|False
}


Response Structure

(dict) --
Represents the output for ListStreams .

StreamNames (list) --
The names of the streams that are associated with the AWS account making the ListStreams request.

(string) --


HasMoreStreams (boolean) --
If set to true , there are more streams available to list.







Exceptions

Kinesis.Client.exceptions.LimitExceededException


    :return: {
        'StreamNames': [
            'string',
        ],
        'HasMoreStreams': True|False
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_tags_for_stream(StreamName=None, ExclusiveStartTagKey=None, Limit=None):
    """
    Lists the tags for the specified Kinesis data stream. This operation has a limit of five transactions per second per account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_stream(
        StreamName='string',
        ExclusiveStartTagKey='string',
        Limit=123
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]\nThe name of the stream.\n

    :type ExclusiveStartTagKey: string
    :param ExclusiveStartTagKey: The key to use as the starting point for the list of tags. If this parameter is set, ListTagsForStream gets all tags that occur after ExclusiveStartTagKey .

    :type Limit: integer
    :param Limit: The number of tags to return. If this number is less than the total number of tags associated with the stream, HasMoreTags is set to true . To list additional tags, set ExclusiveStartTagKey to the last key in the response.

    :rtype: dict

ReturnsResponse Syntax
{
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ],
    'HasMoreTags': True|False
}


Response Structure

(dict) --
Represents the output for ListTagsForStream .

Tags (list) --
A list of tags associated with StreamName , starting with the first tag after ExclusiveStartTagKey and up to the specified Limit .

(dict) --
Metadata assigned to the stream, consisting of a key-value pair.

Key (string) --
A unique identifier for the tag. Maximum length: 128 characters. Valid characters: Unicode letters, digits, white space, _ . / = + - % @

Value (string) --
An optional string, typically used to describe or define the tag. Maximum length: 256 characters. Valid characters: Unicode letters, digits, white space, _ . / = + - % @





HasMoreTags (boolean) --
If set to true , more tags are available. To request additional tags, set ExclusiveStartTagKey to the key of the last tag returned.







Exceptions

Kinesis.Client.exceptions.ResourceNotFoundException
Kinesis.Client.exceptions.InvalidArgumentException
Kinesis.Client.exceptions.LimitExceededException


    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'HasMoreTags': True|False
    }
    
    
    :returns: 
    Kinesis.Client.exceptions.ResourceNotFoundException
    Kinesis.Client.exceptions.InvalidArgumentException
    Kinesis.Client.exceptions.LimitExceededException
    
    """
    pass

def merge_shards(StreamName=None, ShardToMerge=None, AdjacentShardToMerge=None):
    """
    Merges two adjacent shards in a Kinesis data stream and combines them into a single shard to reduce the stream\'s capacity to ingest and transport data. Two shards are considered adjacent if the union of the hash key ranges for the two shards form a contiguous set with no gaps. For example, if you have two shards, one with a hash key range of 276...381 and the other with a hash key range of 382...454, then you could merge these two shards into a single shard that would have a hash key range of 276...454. After the merge, the single child shard receives data for all hash key values covered by the two parent shards.
    If the stream is in the ACTIVE state, you can call MergeShards . If a stream is in the CREATING , UPDATING , or DELETING state, MergeShards returns a ResourceInUseException . If the specified stream does not exist, MergeShards returns a ResourceNotFoundException .
    You can use  DescribeStream to check the state of the stream, which is returned in StreamStatus .
    You use  DescribeStream to determine the shard IDs that are specified in the MergeShards request.
    If you try to operate on too many streams in parallel using  CreateStream ,  DeleteStream , MergeShards , or  SplitShard , you receive a LimitExceededException .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.merge_shards(
        StreamName='string',
        ShardToMerge='string',
        AdjacentShardToMerge='string'
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]\nThe name of the stream for the merge.\n

    :type ShardToMerge: string
    :param ShardToMerge: [REQUIRED]\nThe shard ID of the shard to combine with the adjacent shard for the merge.\n

    :type AdjacentShardToMerge: string
    :param AdjacentShardToMerge: [REQUIRED]\nThe shard ID of the adjacent shard for the merge.\n

    :returns: 
    Kinesis.Client.exceptions.ResourceNotFoundException
    Kinesis.Client.exceptions.ResourceInUseException
    Kinesis.Client.exceptions.InvalidArgumentException
    Kinesis.Client.exceptions.LimitExceededException
    
    """
    pass

def put_record(StreamName=None, Data=None, PartitionKey=None, ExplicitHashKey=None, SequenceNumberForOrdering=None):
    """
    Writes a single data record into an Amazon Kinesis data stream. Call PutRecord to send data into the stream for real-time ingestion and subsequent processing, one record at a time. Each shard can support writes up to 1,000 records per second, up to a maximum data write total of 1 MB per second.
    You must specify the name of the stream that captures, stores, and transports the data; a partition key; and the data blob itself.
    The data blob can be any type of data; for example, a segment from a log file, geographic/location data, website clickstream data, and so on.
    The partition key is used by Kinesis Data Streams to distribute data across shards. Kinesis Data Streams segregates the data records that belong to a stream into multiple shards, using the partition key associated with each data record to determine the shard to which a given data record belongs.
    Partition keys are Unicode strings, with a maximum length limit of 256 characters for each key. An MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards using the hash key ranges of the shards. You can override hashing the partition key to determine the shard by explicitly specifying a hash value using the ExplicitHashKey parameter. For more information, see Adding Data to a Stream in the Amazon Kinesis Data Streams Developer Guide .
    Sequence numbers increase over time and are specific to a shard within a stream, not across all shards within a stream. To guarantee strictly increasing ordering, write serially to a shard and use the SequenceNumberForOrdering parameter. For more information, see Adding Data to a Stream in the Amazon Kinesis Data Streams Developer Guide .
    If a PutRecord request cannot be processed because of insufficient provisioned throughput on the shard involved in the request, PutRecord throws ProvisionedThroughputExceededException .
    By default, data records are accessible for 24 hours from the time that they are added to a stream. You can use  IncreaseStreamRetentionPeriod or  DecreaseStreamRetentionPeriod to modify this retention period.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_record(
        StreamName='string',
        Data=b'bytes',
        PartitionKey='string',
        ExplicitHashKey='string',
        SequenceNumberForOrdering='string'
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]\nThe name of the stream to put the data record into.\n

    :type Data: bytes
    :param Data: [REQUIRED]\nThe data blob to put into the record, which is base64-encoded when the blob is serialized. When the data blob (the payload before base64-encoding) is added to the partition key size, the total size must not exceed the maximum record size (1 MB).\n

    :type PartitionKey: string
    :param PartitionKey: [REQUIRED]\nDetermines which shard in the stream the data record is assigned to. Partition keys are Unicode strings with a maximum length limit of 256 characters for each key. Amazon Kinesis Data Streams uses the partition key as input to a hash function that maps the partition key and associated data to a specific shard. Specifically, an MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards. As a result of this hashing mechanism, all data records with the same partition key map to the same shard within the stream.\n

    :type ExplicitHashKey: string
    :param ExplicitHashKey: The hash value used to explicitly determine the shard the data record is assigned to by overriding the partition key hash.

    :type SequenceNumberForOrdering: string
    :param SequenceNumberForOrdering: Guarantees strictly increasing sequence numbers, for puts from the same client and to the same partition key. Usage: set the SequenceNumberForOrdering of record n to the sequence number of record n-1 (as returned in the result when putting record n-1 ). If this parameter is not set, records are coarsely ordered based on arrival time.

    :rtype: dict

ReturnsResponse Syntax
{
    'ShardId': 'string',
    'SequenceNumber': 'string',
    'EncryptionType': 'NONE'|'KMS'
}


Response Structure

(dict) --
Represents the output for PutRecord .

ShardId (string) --
The shard ID of the shard where the data record was placed.

SequenceNumber (string) --
The sequence number identifier that was assigned to the put data record. The sequence number for the record is unique across all records in the stream. A sequence number is the identifier associated with every record put into the stream.

EncryptionType (string) --
The encryption type to use on the record. This parameter can be one of the following values:

NONE : Do not encrypt the records in the stream.
KMS : Use server-side encryption on the records in the stream using a customer-managed AWS KMS key.








Exceptions

Kinesis.Client.exceptions.ResourceNotFoundException
Kinesis.Client.exceptions.InvalidArgumentException
Kinesis.Client.exceptions.ProvisionedThroughputExceededException
Kinesis.Client.exceptions.KMSDisabledException
Kinesis.Client.exceptions.KMSInvalidStateException
Kinesis.Client.exceptions.KMSAccessDeniedException
Kinesis.Client.exceptions.KMSNotFoundException
Kinesis.Client.exceptions.KMSOptInRequired
Kinesis.Client.exceptions.KMSThrottlingException


    :return: {
        'ShardId': 'string',
        'SequenceNumber': 'string',
        'EncryptionType': 'NONE'|'KMS'
    }
    
    
    :returns: 
    NONE : Do not encrypt the records in the stream.
    KMS : Use server-side encryption on the records in the stream using a customer-managed AWS KMS key.
    
    """
    pass

def put_records(Records=None, StreamName=None):
    """
    Writes multiple data records into a Kinesis data stream in a single call (also referred to as a PutRecords request). Use this operation to send data into the stream for data ingestion and processing.
    Each PutRecords request can support up to 500 records. Each record in the request can be as large as 1 MB, up to a limit of 5 MB for the entire request, including partition keys. Each shard can support writes up to 1,000 records per second, up to a maximum data write total of 1 MB per second.
    You must specify the name of the stream that captures, stores, and transports the data; and an array of request Records , with each record in the array requiring a partition key and data blob. The record size limit applies to the total size of the partition key and data blob.
    The data blob can be any type of data; for example, a segment from a log file, geographic/location data, website clickstream data, and so on.
    The partition key is used by Kinesis Data Streams as input to a hash function that maps the partition key and associated data to a specific shard. An MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards. As a result of this hashing mechanism, all data records with the same partition key map to the same shard within the stream. For more information, see Adding Data to a Stream in the Amazon Kinesis Data Streams Developer Guide .
    Each record in the Records array may include an optional parameter, ExplicitHashKey , which overrides the partition key to shard mapping. This parameter allows a data producer to determine explicitly the shard where the record is stored. For more information, see Adding Multiple Records with PutRecords in the Amazon Kinesis Data Streams Developer Guide .
    The PutRecords response includes an array of response Records . Each record in the response array directly correlates with a record in the request array using natural ordering, from the top to the bottom of the request and response. The response Records array always includes the same number of records as the request array.
    The response Records array includes both successfully and unsuccessfully processed records. Kinesis Data Streams attempts to process all records in each PutRecords request. A single record failure does not stop the processing of subsequent records.
    A successfully processed record includes ShardId and SequenceNumber values. The ShardId parameter identifies the shard in the stream where the record is stored. The SequenceNumber parameter is an identifier assigned to the put record, unique to all records in the stream.
    An unsuccessfully processed record includes ErrorCode and ErrorMessage values. ErrorCode reflects the type of error and can be one of the following values: ProvisionedThroughputExceededException or InternalFailure . ErrorMessage provides more detailed information about the ProvisionedThroughputExceededException exception including the account ID, stream name, and shard ID of the record that was throttled. For more information about partially successful responses, see Adding Multiple Records with PutRecords in the Amazon Kinesis Data Streams Developer Guide .
    By default, data records are accessible for 24 hours from the time that they are added to a stream. You can use  IncreaseStreamRetentionPeriod or  DecreaseStreamRetentionPeriod to modify this retention period.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_records(
        Records=[
            {
                'Data': b'bytes',
                'ExplicitHashKey': 'string',
                'PartitionKey': 'string'
            },
        ],
        StreamName='string'
    )
    
    
    :type Records: list
    :param Records: [REQUIRED]\nThe records associated with the request.\n\n(dict) --Represents the output for PutRecords .\n\nData (bytes) -- [REQUIRED]The data blob to put into the record, which is base64-encoded when the blob is serialized. When the data blob (the payload before base64-encoding) is added to the partition key size, the total size must not exceed the maximum record size (1 MB).\n\nExplicitHashKey (string) --The hash value used to determine explicitly the shard that the data record is assigned to by overriding the partition key hash.\n\nPartitionKey (string) -- [REQUIRED]Determines which shard in the stream the data record is assigned to. Partition keys are Unicode strings with a maximum length limit of 256 characters for each key. Amazon Kinesis Data Streams uses the partition key as input to a hash function that maps the partition key and associated data to a specific shard. Specifically, an MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards. As a result of this hashing mechanism, all data records with the same partition key map to the same shard within the stream.\n\n\n\n\n

    :type StreamName: string
    :param StreamName: [REQUIRED]\nThe stream name associated with the request.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'FailedRecordCount': 123,
    'Records': [
        {
            'SequenceNumber': 'string',
            'ShardId': 'string',
            'ErrorCode': 'string',
            'ErrorMessage': 'string'
        },
    ],
    'EncryptionType': 'NONE'|'KMS'
}


Response Structure

(dict) --

PutRecords results.


FailedRecordCount (integer) --
The number of unsuccessfully processed records in a PutRecords request.

Records (list) --
An array of successfully and unsuccessfully processed record results, correlated with the request by natural ordering. A record that is successfully added to a stream includes SequenceNumber and ShardId in the result. A record that fails to be added to a stream includes ErrorCode and ErrorMessage in the result.

(dict) --
Represents the result of an individual record from a PutRecords request. A record that is successfully added to a stream includes SequenceNumber and ShardId in the result. A record that fails to be added to the stream includes ErrorCode and ErrorMessage in the result.

SequenceNumber (string) --
The sequence number for an individual record result.

ShardId (string) --
The shard ID for an individual record result.

ErrorCode (string) --
The error code for an individual record result. ErrorCodes can be either ProvisionedThroughputExceededException or InternalFailure .

ErrorMessage (string) --
The error message for an individual record result. An ErrorCode value of ProvisionedThroughputExceededException has an error message that includes the account ID, stream name, and shard ID. An ErrorCode value of InternalFailure has the error message "Internal Service Failure" .





EncryptionType (string) --
The encryption type used on the records. This parameter can be one of the following values:

NONE : Do not encrypt the records.
KMS : Use server-side encryption on the records using a customer-managed AWS KMS key.








Exceptions

Kinesis.Client.exceptions.ResourceNotFoundException
Kinesis.Client.exceptions.InvalidArgumentException
Kinesis.Client.exceptions.ProvisionedThroughputExceededException
Kinesis.Client.exceptions.KMSDisabledException
Kinesis.Client.exceptions.KMSInvalidStateException
Kinesis.Client.exceptions.KMSAccessDeniedException
Kinesis.Client.exceptions.KMSNotFoundException
Kinesis.Client.exceptions.KMSOptInRequired
Kinesis.Client.exceptions.KMSThrottlingException


    :return: {
        'FailedRecordCount': 123,
        'Records': [
            {
                'SequenceNumber': 'string',
                'ShardId': 'string',
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ],
        'EncryptionType': 'NONE'|'KMS'
    }
    
    
    :returns: 
    NONE : Do not encrypt the records.
    KMS : Use server-side encryption on the records using a customer-managed AWS KMS key.
    
    """
    pass

def register_stream_consumer(StreamARN=None, ConsumerName=None):
    """
    Registers a consumer with a Kinesis data stream. When you use this operation, the consumer you register can read data from the stream at a rate of up to 2 MiB per second. This rate is unaffected by the total number of consumers that read from the same stream.
    You can register up to 5 consumers per stream. A given consumer can only be registered with one stream.
    This operation has a limit of five transactions per second per account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_stream_consumer(
        StreamARN='string',
        ConsumerName='string'
    )
    
    
    :type StreamARN: string
    :param StreamARN: [REQUIRED]\nThe ARN of the Kinesis data stream that you want to register the consumer with. For more info, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n

    :type ConsumerName: string
    :param ConsumerName: [REQUIRED]\nFor a given Kinesis data stream, each consumer must have a unique name. However, consumer names don\'t have to be unique across data streams.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Consumer': {
        'ConsumerName': 'string',
        'ConsumerARN': 'string',
        'ConsumerStatus': 'CREATING'|'DELETING'|'ACTIVE',
        'ConsumerCreationTimestamp': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

Consumer (dict) --
An object that represents the details of the consumer you registered. When you register a consumer, it gets an ARN that is generated by Kinesis Data Streams.

ConsumerName (string) --
The name of the consumer is something you choose when you register the consumer.

ConsumerARN (string) --
When you register a consumer, Kinesis Data Streams generates an ARN for it. You need this ARN to be able to call  SubscribeToShard .
If you delete a consumer and then create a new one with the same name, it won\'t have the same ARN. That\'s because consumer ARNs contain the creation timestamp. This is important to keep in mind if you have IAM policies that reference consumer ARNs.

ConsumerStatus (string) --
A consumer can\'t read data while in the CREATING or DELETING states.

ConsumerCreationTimestamp (datetime) --









Exceptions

Kinesis.Client.exceptions.InvalidArgumentException
Kinesis.Client.exceptions.LimitExceededException
Kinesis.Client.exceptions.ResourceInUseException
Kinesis.Client.exceptions.ResourceNotFoundException


    :return: {
        'Consumer': {
            'ConsumerName': 'string',
            'ConsumerARN': 'string',
            'ConsumerStatus': 'CREATING'|'DELETING'|'ACTIVE',
            'ConsumerCreationTimestamp': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    Kinesis.Client.exceptions.InvalidArgumentException
    Kinesis.Client.exceptions.LimitExceededException
    Kinesis.Client.exceptions.ResourceInUseException
    Kinesis.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def remove_tags_from_stream(StreamName=None, TagKeys=None):
    """
    Removes tags from the specified Kinesis data stream. Removed tags are deleted and cannot be recovered after this operation successfully completes.
    If you specify a tag that does not exist, it is ignored.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.remove_tags_from_stream(
        StreamName='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]\nThe name of the stream.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nA list of tag keys. Each corresponding tag is removed from the stream.\n\n(string) --\n\n

    :returns: 
    Kinesis.Client.exceptions.ResourceNotFoundException
    Kinesis.Client.exceptions.ResourceInUseException
    Kinesis.Client.exceptions.InvalidArgumentException
    Kinesis.Client.exceptions.LimitExceededException
    
    """
    pass

def split_shard(StreamName=None, ShardToSplit=None, NewStartingHashKey=None):
    """
    Splits a shard into two new shards in the Kinesis data stream, to increase the stream\'s capacity to ingest and transport data. SplitShard is called when there is a need to increase the overall capacity of a stream because of an expected increase in the volume of data records being ingested.
    You can also use SplitShard when a shard appears to be approaching its maximum utilization; for example, the producers sending data into the specific shard are suddenly sending more than previously anticipated. You can also call SplitShard to increase stream capacity, so that more Kinesis Data Streams applications can simultaneously read data from the stream for real-time processing.
    You must specify the shard to be split and the new hash key, which is the position in the shard where the shard gets split in two. In many cases, the new hash key might be the average of the beginning and ending hash key, but it can be any hash key value in the range being mapped into the shard. For more information, see Split a Shard in the Amazon Kinesis Data Streams Developer Guide .
    You can use  DescribeStream to determine the shard ID and hash key values for the ShardToSplit and NewStartingHashKey parameters that are specified in the SplitShard request.
    You can use DescribeStream to check the status of the stream, which is returned in StreamStatus . If the stream is in the ACTIVE state, you can call SplitShard . If a stream is in CREATING or UPDATING or DELETING states, DescribeStream returns a ResourceInUseException .
    If the specified stream does not exist, DescribeStream returns a ResourceNotFoundException . If you try to create more shards than are authorized for your account, you receive a LimitExceededException .
    For the default shard limit for an AWS account, see Kinesis Data Streams Limits in the Amazon Kinesis Data Streams Developer Guide . To increase this limit, contact AWS Support .
    If you try to operate on too many streams simultaneously using  CreateStream ,  DeleteStream ,  MergeShards , and/or  SplitShard , you receive a LimitExceededException .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.split_shard(
        StreamName='string',
        ShardToSplit='string',
        NewStartingHashKey='string'
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]\nThe name of the stream for the shard split.\n

    :type ShardToSplit: string
    :param ShardToSplit: [REQUIRED]\nThe shard ID of the shard to split.\n

    :type NewStartingHashKey: string
    :param NewStartingHashKey: [REQUIRED]\nA hash key value for the starting hash key of one of the child shards created by the split. The hash key range for a given shard constitutes a set of ordered contiguous positive integers. The value for NewStartingHashKey must be in the range of hash keys being mapped into the shard. The NewStartingHashKey hash key value and all higher hash key values in hash key range are distributed to one of the child shards. All the lower hash key values in the range are distributed to the other child shard.\n

    :returns: 
    Kinesis.Client.exceptions.ResourceNotFoundException
    Kinesis.Client.exceptions.ResourceInUseException
    Kinesis.Client.exceptions.InvalidArgumentException
    Kinesis.Client.exceptions.LimitExceededException
    
    """
    pass

def start_stream_encryption(StreamName=None, EncryptionType=None, KeyId=None):
    """
    Enables or updates server-side encryption using an AWS KMS key for a specified stream.
    Starting encryption is an asynchronous operation. Upon receiving the request, Kinesis Data Streams returns immediately and sets the status of the stream to UPDATING . After the update is complete, Kinesis Data Streams sets the status of the stream back to ACTIVE . Updating or applying encryption normally takes a few seconds to complete, but it can take minutes. You can continue to read and write data to your stream while its status is UPDATING . Once the status of the stream is ACTIVE , encryption begins for records written to the stream.
    API Limits: You can successfully apply a new AWS KMS key for server-side encryption 25 times in a rolling 24-hour period.
    Note: It can take up to 5 seconds after the stream is in an ACTIVE status before all records written to the stream are encrypted. After you enable encryption, you can verify that encryption is applied by inspecting the API response from PutRecord or PutRecords .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_stream_encryption(
        StreamName='string',
        EncryptionType='NONE'|'KMS',
        KeyId='string'
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]\nThe name of the stream for which to start encrypting records.\n

    :type EncryptionType: string
    :param EncryptionType: [REQUIRED]\nThe encryption type to use. The only valid value is KMS .\n

    :type KeyId: string
    :param KeyId: [REQUIRED]\nThe GUID for the customer-managed AWS KMS key to use for encryption. This value can be a globally unique identifier, a fully specified Amazon Resource Name (ARN) to either an alias or a key, or an alias name prefixed by 'alias/'.You can also use a master key owned by Kinesis Data Streams by specifying the alias aws/kinesis .\n\nKey ARN example: arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012\nAlias ARN example: arn:aws:kms:us-east-1:123456789012:alias/MyAliasName\nGlobally unique key ID example: 12345678-1234-1234-1234-123456789012\nAlias name example: alias/MyAliasName\nMaster key owned by Kinesis Data Streams: alias/aws/kinesis\n\n

    :returns: 
    Kinesis.Client.exceptions.InvalidArgumentException
    Kinesis.Client.exceptions.LimitExceededException
    Kinesis.Client.exceptions.ResourceInUseException
    Kinesis.Client.exceptions.ResourceNotFoundException
    Kinesis.Client.exceptions.KMSDisabledException
    Kinesis.Client.exceptions.KMSInvalidStateException
    Kinesis.Client.exceptions.KMSAccessDeniedException
    Kinesis.Client.exceptions.KMSNotFoundException
    Kinesis.Client.exceptions.KMSOptInRequired
    Kinesis.Client.exceptions.KMSThrottlingException
    
    """
    pass

def stop_stream_encryption(StreamName=None, EncryptionType=None, KeyId=None):
    """
    Disables server-side encryption for a specified stream.
    Stopping encryption is an asynchronous operation. Upon receiving the request, Kinesis Data Streams returns immediately and sets the status of the stream to UPDATING . After the update is complete, Kinesis Data Streams sets the status of the stream back to ACTIVE . Stopping encryption normally takes a few seconds to complete, but it can take minutes. You can continue to read and write data to your stream while its status is UPDATING . Once the status of the stream is ACTIVE , records written to the stream are no longer encrypted by Kinesis Data Streams.
    API Limits: You can successfully disable server-side encryption 25 times in a rolling 24-hour period.
    Note: It can take up to 5 seconds after the stream is in an ACTIVE status before all records written to the stream are no longer subject to encryption. After you disabled encryption, you can verify that encryption is not applied by inspecting the API response from PutRecord or PutRecords .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_stream_encryption(
        StreamName='string',
        EncryptionType='NONE'|'KMS',
        KeyId='string'
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]\nThe name of the stream on which to stop encrypting records.\n

    :type EncryptionType: string
    :param EncryptionType: [REQUIRED]\nThe encryption type. The only valid value is KMS .\n

    :type KeyId: string
    :param KeyId: [REQUIRED]\nThe GUID for the customer-managed AWS KMS key to use for encryption. This value can be a globally unique identifier, a fully specified Amazon Resource Name (ARN) to either an alias or a key, or an alias name prefixed by 'alias/'.You can also use a master key owned by Kinesis Data Streams by specifying the alias aws/kinesis .\n\nKey ARN example: arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012\nAlias ARN example: arn:aws:kms:us-east-1:123456789012:alias/MyAliasName\nGlobally unique key ID example: 12345678-1234-1234-1234-123456789012\nAlias name example: alias/MyAliasName\nMaster key owned by Kinesis Data Streams: alias/aws/kinesis\n\n

    :returns: 
    Kinesis.Client.exceptions.InvalidArgumentException
    Kinesis.Client.exceptions.LimitExceededException
    Kinesis.Client.exceptions.ResourceInUseException
    Kinesis.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def subscribe_to_shard(ConsumerARN=None, ShardId=None, StartingPosition=None):
    """
    Call this operation from your consumer after you call  RegisterStreamConsumer to register the consumer with Kinesis Data Streams. If the call succeeds, your consumer starts receiving events of type  SubscribeToShardEvent for up to 5 minutes, after which time you need to call SubscribeToShard again to renew the subscription if you want to continue to receive records.
    You can make one call to SubscribeToShard per second per ConsumerARN . If your call succeeds, and then you call the operation again less than 5 seconds later, the second call generates a  ResourceInUseException . If you call the operation a second time more than 5 seconds after the first call succeeds, the second call succeeds and the first connection gets shut down.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.subscribe_to_shard(
        ConsumerARN='string',
        ShardId='string',
        StartingPosition={
            'Type': 'AT_SEQUENCE_NUMBER'|'AFTER_SEQUENCE_NUMBER'|'TRIM_HORIZON'|'LATEST'|'AT_TIMESTAMP',
            'SequenceNumber': 'string',
            'Timestamp': datetime(2015, 1, 1)
        }
    )
    
    
    :type ConsumerARN: string
    :param ConsumerARN: [REQUIRED]\nFor this parameter, use the value you obtained when you called RegisterStreamConsumer .\n

    :type ShardId: string
    :param ShardId: [REQUIRED]\nThe ID of the shard you want to subscribe to. To see a list of all the shards for a given stream, use ListShards .\n

    :type StartingPosition: dict
    :param StartingPosition: [REQUIRED]\n\nType (string) -- [REQUIRED]\nSequenceNumber (string) --\nTimestamp (datetime) --\n\n

    :rtype: dict

ReturnsThe response of this operation contains an EventStream member. When iterated the EventStream will yield events based on the structure below, where only one of the top level keys will be present for any given event.
Response Syntax
{
    'EventStream': EventStream({
        'SubscribeToShardEvent': {
            'Records': [
                {
                    'SequenceNumber': 'string',
                    'ApproximateArrivalTimestamp': datetime(2015, 1, 1),
                    'Data': b'bytes',
                    'PartitionKey': 'string',
                    'EncryptionType': 'NONE'|'KMS'
                },
            ],
            'ContinuationSequenceNumber': 'string',
            'MillisBehindLatest': 123
        },
        'ResourceNotFoundException': {
            'message': 'string'
        },
        'ResourceInUseException': {
            'message': 'string'
        },
        'KMSDisabledException': {
            'message': 'string'
        },
        'KMSInvalidStateException': {
            'message': 'string'
        },
        'KMSAccessDeniedException': {
            'message': 'string'
        },
        'KMSNotFoundException': {
            'message': 'string'
        },
        'KMSOptInRequired': {
            'message': 'string'
        },
        'KMSThrottlingException': {
            'message': 'string'
        },
        'InternalFailureException': {
            'message': 'string'
        }
    })
}


Response Structure

(dict) --

EventStream (EventStream) --
The event stream that your consumer can use to read records from the shard.

SubscribeToShardEvent (dict) --
After you call  SubscribeToShard , Kinesis Data Streams sends events of this type to your consumer.

Records (list) --

(dict) --
The unit of data of the Kinesis data stream, which is composed of a sequence number, a partition key, and a data blob.

SequenceNumber (string) --
The unique identifier of the record within its shard.

ApproximateArrivalTimestamp (datetime) --
The approximate time that the record was inserted into the stream.

Data (bytes) --
The data blob. The data in the blob is both opaque and immutable to Kinesis Data Streams, which does not inspect, interpret, or change the data in the blob in any way. When the data blob (the payload before base64-encoding) is added to the partition key size, the total size must not exceed the maximum record size (1 MB).

PartitionKey (string) --
Identifies which shard in the stream the data record is assigned to.

EncryptionType (string) --
The encryption type used on the record. This parameter can be one of the following values:

NONE : Do not encrypt the records in the stream.
KMS : Use server-side encryption on the records in the stream using a customer-managed AWS KMS key.






ContinuationSequenceNumber (string) --
Use this as StartingSequenceNumber in the next call to  SubscribeToShard .

MillisBehindLatest (integer) --
The number of milliseconds the read records are from the tip of the stream, indicating how far behind current time the consumer is. A value of zero indicates that record processing is caught up, and there are no new records to process at this moment.



ResourceNotFoundException (dict) --
The requested resource could not be found. The stream might not be specified correctly.

message (string) --
A message that provides information about the error.



ResourceInUseException (dict) --
The resource is not available for this operation. For successful operation, the resource must be in the ACTIVE state.

message (string) --
A message that provides information about the error.



KMSDisabledException (dict) --
The request was rejected because the specified customer master key (CMK) isn\'t enabled.

message (string) --
A message that provides information about the error.



KMSInvalidStateException (dict) --
The request was rejected because the state of the specified resource isn\'t valid for this request. For more information, see How Key State Affects Use of a Customer Master Key in the AWS Key Management Service Developer Guide .

message (string) --
A message that provides information about the error.



KMSAccessDeniedException (dict) --
The ciphertext references a key that doesn\'t exist or that you don\'t have access to.

message (string) --
A message that provides information about the error.



KMSNotFoundException (dict) --
The request was rejected because the specified entity or resource can\'t be found.

message (string) --
A message that provides information about the error.



KMSOptInRequired (dict) --
The AWS access key ID needs a subscription for the service.

message (string) --
A message that provides information about the error.



KMSThrottlingException (dict) --
The request was denied due to request throttling. For more information about throttling, see Limits in the AWS Key Management Service Developer Guide .

message (string) --
A message that provides information about the error.



InternalFailureException (dict) --

message (string) --










Exceptions

Kinesis.Client.exceptions.ResourceNotFoundException
Kinesis.Client.exceptions.InvalidArgumentException
Kinesis.Client.exceptions.ResourceInUseException
Kinesis.Client.exceptions.LimitExceededException


    :return: {
        'EventStream': EventStream({
            'SubscribeToShardEvent': {
                'Records': [
                    {
                        'SequenceNumber': 'string',
                        'ApproximateArrivalTimestamp': datetime(2015, 1, 1),
                        'Data': b'bytes',
                        'PartitionKey': 'string',
                        'EncryptionType': 'NONE'|'KMS'
                    },
                ],
                'ContinuationSequenceNumber': 'string',
                'MillisBehindLatest': 123
            },
            'ResourceNotFoundException': {
                'message': 'string'
            },
            'ResourceInUseException': {
                'message': 'string'
            },
            'KMSDisabledException': {
                'message': 'string'
            },
            'KMSInvalidStateException': {
                'message': 'string'
            },
            'KMSAccessDeniedException': {
                'message': 'string'
            },
            'KMSNotFoundException': {
                'message': 'string'
            },
            'KMSOptInRequired': {
                'message': 'string'
            },
            'KMSThrottlingException': {
                'message': 'string'
            },
            'InternalFailureException': {
                'message': 'string'
            }
        })
    }
    
    
    :returns: 
    NONE : Do not encrypt the records in the stream.
    KMS : Use server-side encryption on the records in the stream using a customer-managed AWS KMS key.
    
    """
    pass

def update_shard_count(StreamName=None, TargetShardCount=None, ScalingType=None):
    """
    Updates the shard count of the specified stream to the specified number of shards.
    Updating the shard count is an asynchronous operation. Upon receiving the request, Kinesis Data Streams returns immediately and sets the status of the stream to UPDATING . After the update is complete, Kinesis Data Streams sets the status of the stream back to ACTIVE . Depending on the size of the stream, the scaling action could take a few minutes to complete. You can continue to read and write data to your stream while its status is UPDATING .
    To update the shard count, Kinesis Data Streams performs splits or merges on individual shards. This can cause short-lived shards to be created, in addition to the final shards. We recommend that you double or halve the shard count, as this results in the fewest number of splits or merges.
    This operation has the following default limits. By default, you cannot do the following:
    For the default limits for an AWS account, see Streams Limits in the Amazon Kinesis Data Streams Developer Guide . To request an increase in the call rate limit, the shard limit for this API, or your overall shard limit, use the limits form .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_shard_count(
        StreamName='string',
        TargetShardCount=123,
        ScalingType='UNIFORM_SCALING'
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]\nThe name of the stream.\n

    :type TargetShardCount: integer
    :param TargetShardCount: [REQUIRED]\nThe new number of shards.\n

    :type ScalingType: string
    :param ScalingType: [REQUIRED]\nThe scaling type. Uniform scaling creates shards of equal size.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'StreamName': 'string',
    'CurrentShardCount': 123,
    'TargetShardCount': 123
}


Response Structure

(dict) --

StreamName (string) --
The name of the stream.

CurrentShardCount (integer) --
The current number of shards.

TargetShardCount (integer) --
The updated number of shards.







Exceptions

Kinesis.Client.exceptions.InvalidArgumentException
Kinesis.Client.exceptions.LimitExceededException
Kinesis.Client.exceptions.ResourceInUseException
Kinesis.Client.exceptions.ResourceNotFoundException


    :return: {
        'StreamName': 'string',
        'CurrentShardCount': 123,
        'TargetShardCount': 123
    }
    
    
    :returns: 
    StreamName (string) -- [REQUIRED]
    The name of the stream.
    
    TargetShardCount (integer) -- [REQUIRED]
    The new number of shards.
    
    ScalingType (string) -- [REQUIRED]
    The scaling type. Uniform scaling creates shards of equal size.
    
    
    """
    pass

