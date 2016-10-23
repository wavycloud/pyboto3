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


def add_permission(QueueUrl=None, Label=None, AWSAccountIds=None, Actions=None):
    """
    :param QueueUrl: [REQUIRED]
            The URL of the Amazon SQS queue to take action on.
            Queue URLs are case-sensitive.
            
    :type QueueUrl: string
    :param Label: [REQUIRED]
            The unique identification of the permission you're setting (e.g., AliceSendMessage ). Constraints: Maximum 80 characters; alphanumeric characters, hyphens (-), and underscores (_) are allowed.
            
    :type Label: string
    :param AWSAccountIds: [REQUIRED]
            The AWS account number of the principal who will be given permission. The principal must have an AWS account, but does not need to be signed up for Amazon SQS. For information about locating the AWS account identification, see Your AWS Identifiers in the Amazon SQS Developer Guide .
            (string) --
            
    :type AWSAccountIds: list
    :param Actions: [REQUIRED]
            The action the client wants to allow for the specified principal. The following are valid values: * | SendMessage | ReceiveMessage | DeleteMessage | ChangeMessageVisibility | GetQueueAttributes | GetQueueUrl . For more information about these actions, see Understanding Permissions in the Amazon SQS Developer Guide .
            Specifying SendMessage , DeleteMessage , or ChangeMessageVisibility for the ActionName.n also grants permissions for the corresponding batch versions of those actions: SendMessageBatch , DeleteMessageBatch , and ChangeMessageVisibilityBatch .
            (string) --
            
    :type Actions: list
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


def change_message_visibility(QueueUrl=None, ReceiptHandle=None, VisibilityTimeout=None):
    """
    :param QueueUrl: [REQUIRED]
            The URL of the Amazon SQS queue to take action on.
            Queue URLs are case-sensitive.
            
    :type QueueUrl: string
    :param ReceiptHandle: [REQUIRED]
            The receipt handle associated with the message whose visibility timeout should be changed. This parameter is returned by the ReceiveMessage action.
            
    :type ReceiptHandle: string
    :param VisibilityTimeout: [REQUIRED]
            The new value (in seconds - from 0 to 43200 - maximum 12 hours) for the message's visibility timeout.
            
    :type VisibilityTimeout: integer
    """
    pass


def change_message_visibility_batch(QueueUrl=None, Entries=None):
    """
    :param QueueUrl: [REQUIRED]
            The URL of the Amazon SQS queue to take action on.
            Queue URLs are case-sensitive.
            
    :type QueueUrl: string
    :param Entries: [REQUIRED]
            A list of receipt handles of the messages for which the visibility timeout must be changed.
            (dict) --Encloses a receipt handle and an entry id for each message in ChangeMessageVisibilityBatch .
            Warning
            All of the following parameters are list parameters that must be prefixed with ChangeMessageVisibilityBatchRequestEntry.n , where n is an integer value starting with 1. For example, a parameter list for this action might look like this:
            Id (string) -- [REQUIRED]An identifier for this particular receipt handle. This is used to communicate the result. Note that the Id s of a batch request need to be unique within the request.
            ReceiptHandle (string) -- [REQUIRED]A receipt handle.
            VisibilityTimeout (integer) --The new value (in seconds) for the message's visibility timeout.
            
            
    :type Entries: list
    """
    pass


def create_queue(QueueName=None, Attributes=None):
    """
    :param QueueName: [REQUIRED]
            The name for the queue to be created.
            Queue names are case-sensitive.
            
    :type QueueName: string
    :param Attributes: A map of attributes with their corresponding values.
            The following lists the names, descriptions, and values of the special request parameters the CreateQueue action uses:
            DelaySeconds - The time in seconds that the delivery of all messages in the queue will be delayed. An integer from 0 to 900 (15 minutes). The default for this attribute is 0 (zero).
            MaximumMessageSize - The limit of how many bytes a message can contain before Amazon SQS rejects it. An integer from 1024 bytes (1 KiB) up to 262144 bytes (256 KiB). The default for this attribute is 262144 (256 KiB).
            MessageRetentionPeriod - The number of seconds Amazon SQS retains a message. Integer representing seconds, from 60 (1 minute) to 1209600 (14 days). The default for this attribute is 345600 (4 days).
            Policy - The queue's policy. A valid AWS policy. For more information about policy structure, see Overview of AWS IAM Policies in the Amazon IAM User Guide .
            ReceiveMessageWaitTimeSeconds - The time for which a ReceiveMessage call will wait for a message to arrive. An integer from 0 to 20 (seconds). The default for this attribute is 0.
            RedrivePolicy - The parameters for dead letter queue functionality of the source queue. For more information about RedrivePolicy and dead letter queues, see Using Amazon SQS Dead Letter Queues in the Amazon SQS Developer Guide .
            VisibilityTimeout - The visibility timeout for the queue. An integer from 0 to 43200 (12 hours). The default for this attribute is 30. For more information about visibility timeout, see Visibility Timeout in the Amazon SQS Developer Guide .
            Any other valid special request parameters that are specified (such as ApproximateNumberOfMessages , ApproximateNumberOfMessagesDelayed , ApproximateNumberOfMessagesNotVisible , CreatedTimestamp , LastModifiedTimestamp , and QueueArn ) will be ignored.
            (string) --
            (string) --
            
    :type Attributes: dict
    """
    pass


def delete_message(QueueUrl=None, ReceiptHandle=None):
    """
    :param QueueUrl: [REQUIRED]
            The URL of the Amazon SQS queue to take action on.
            Queue URLs are case-sensitive.
            
    :type QueueUrl: string
    :param ReceiptHandle: [REQUIRED]
            The receipt handle associated with the message to delete.
            
    :type ReceiptHandle: string
    """
    pass


def delete_message_batch(QueueUrl=None, Entries=None):
    """
    :param QueueUrl: [REQUIRED]
            The URL of the Amazon SQS queue to take action on.
            Queue URLs are case-sensitive.
            
    :type QueueUrl: string
    :param Entries: [REQUIRED]
            A list of receipt handles for the messages to be deleted.
            (dict) --Encloses a receipt handle and an identifier for it.
            Id (string) -- [REQUIRED]An identifier for this particular receipt handle. This is used to communicate the result. Note that the Id s of a batch request need to be unique within the request.
            ReceiptHandle (string) -- [REQUIRED]A receipt handle.
            
            
    :type Entries: list
    """
    pass


def delete_queue(QueueUrl=None):
    """
    :param QueueUrl: [REQUIRED]
            The URL of the Amazon SQS queue to take action on.
            Queue URLs are case-sensitive.
            ReturnsNone
            
    :type QueueUrl: string
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


def get_queue_attributes(QueueUrl=None, AttributeNames=None):
    """
    :param QueueUrl: [REQUIRED]
            The URL of the Amazon SQS queue to take action on.
            Queue URLs are case-sensitive.
            
    :type QueueUrl: string
    :param AttributeNames: A list of attributes to retrieve information for. The following attributes are supported:
            All - returns all values.
            ApproximateNumberOfMessages - returns the approximate number of visible messages in a queue. For more information, see Resources Required to Process Messages in the Amazon SQS Developer Guide .
            ApproximateNumberOfMessagesNotVisible - returns the approximate number of messages that are not timed-out and not deleted. For more information, see Resources Required to Process Messages in the Amazon SQS Developer Guide .
            VisibilityTimeout - returns the visibility timeout for the queue. For more information about visibility timeout, see Visibility Timeout in the Amazon SQS Developer Guide .
            CreatedTimestamp - returns the time when the queue was created (epoch time in seconds).
            LastModifiedTimestamp - returns the time when the queue was last changed (epoch time in seconds).
            Policy - returns the queue's policy.
            MaximumMessageSize - returns the limit of how many bytes a message can contain before Amazon SQS rejects it.
            MessageRetentionPeriod - returns the number of seconds Amazon SQS retains a message.
            QueueArn - returns the queue's Amazon resource name (ARN).
            ApproximateNumberOfMessagesDelayed - returns the approximate number of messages that are pending to be added to the queue.
            DelaySeconds - returns the default delay on the queue in seconds.
            ReceiveMessageWaitTimeSeconds - returns the time for which a ReceiveMessage call will wait for a message to arrive.
            RedrivePolicy - returns the parameters for dead letter queue functionality of the source queue. For more information about RedrivePolicy and dead letter queues, see Using Amazon SQS Dead Letter Queues in the Amazon SQS Developer Guide .
            Note
            Going forward, new attributes might be added. If you are writing code that calls this action, we recommend that you structure your code so that it can handle new attributes gracefully.
            (string) --
            
    :type AttributeNames: list
    """
    pass


def get_queue_url(QueueName=None, QueueOwnerAWSAccountId=None):
    """
    :param QueueName: [REQUIRED]
            The name of the queue whose URL must be fetched. Maximum 80 characters; alphanumeric characters, hyphens (-), and underscores (_) are allowed.
            Queue names are case-sensitive.
            
    :type QueueName: string
    :param QueueOwnerAWSAccountId: The AWS account ID of the account that created the queue.
    :type QueueOwnerAWSAccountId: string
    """
    pass


def get_waiter():
    """
    """
    pass


def list_dead_letter_source_queues(QueueUrl=None):
    """
    :param QueueUrl: [REQUIRED]
            The queue URL of a dead letter queue.
            Queue URLs are case-sensitive.
            Return typedict
            ReturnsResponse Syntax{
              'queueUrls': [
                'string',
              ]
            }
            Response Structure
            (dict) --A list of your dead letter source queues.
            queueUrls (list) --A list of source queue URLs that have the RedrivePolicy queue attribute configured with a dead letter queue.
            (string) --
            
            
    :type QueueUrl: string
    """
    pass


def list_queues(QueueNamePrefix=None):
    """
    :param QueueNamePrefix: A string to use for filtering the list results. Only those queues whose name begins with the specified string are returned.
            Queue names are case-sensitive.
            Return typedict
            ReturnsResponse Syntax{
              'QueueUrls': [
                'string',
              ]
            }
            Response Structure
            (dict) --A list of your queues.
            QueueUrls (list) --A list of queue URLs, up to 1000 entries.
            (string) --
            
            
    :type QueueNamePrefix: string
    """
    pass


def purge_queue(QueueUrl=None):
    """
    :param QueueUrl: [REQUIRED]
            The queue URL of the queue to delete the messages from when using the PurgeQueue API.
            Queue URLs are case-sensitive.
            ReturnsNone
            
    :type QueueUrl: string
    """
    pass


def receive_message(QueueUrl=None, AttributeNames=None, MessageAttributeNames=None, MaxNumberOfMessages=None,
                    VisibilityTimeout=None, WaitTimeSeconds=None):
    """
    :param QueueUrl: [REQUIRED]
            The URL of the Amazon SQS queue to take action on.
            Queue URLs are case-sensitive.
            
    :type QueueUrl: string
    :param AttributeNames: A list of attributes that need to be returned along with each message. These attributes include:
            All - returns all values.
            ApproximateFirstReceiveTimestamp - returns the time when the message was first received from the queue (epoch time in milliseconds).
            ApproximateReceiveCount - returns the number of times a message has been received from the queue but not deleted.
            SenderId - returns the AWS account number (or the IP address, if anonymous access is allowed) of the sender.
            SentTimestamp - returns the time when the message was sent to the queue (epoch time in milliseconds).
            Any other valid special request parameters that are specified (such as ApproximateNumberOfMessages , ApproximateNumberOfMessagesDelayed , ApproximateNumberOfMessagesNotVisible , CreatedTimestamp , DelaySeconds , LastModifiedTimestamp , MaximumMessageSize , MessageRetentionPeriod , Policy , QueueArn , ReceiveMessageWaitTimeSeconds , RedrivePolicy , and VisibilityTimeout ) will be ignored.
            (string) --
            
    :type AttributeNames: list
    :param MessageAttributeNames: The name of the message attribute, where N is the index. The message attribute name can contain the following characters: A-Z, a-z, 0-9, underscore (_), hyphen (-), and period (.). The name must not start or end with a period, and it should not have successive periods. The name is case sensitive and must be unique among all attribute names for the message. The name can be up to 256 characters long. The name cannot start with 'AWS.' or 'Amazon.' (or any variations in casing), because these prefixes are reserved for use by Amazon Web Services.
            When using ReceiveMessage , you can send a list of attribute names to receive, or you can return all of the attributes by specifying 'All' or '.*' in your request. You can also use 'bar.*' to return all message attributes starting with the 'bar' prefix.
            (string) --
            
    :type MessageAttributeNames: list
    :param MaxNumberOfMessages: The maximum number of messages to return. Amazon SQS never returns more messages than this value but may return fewer. Values can be from 1 to 10. Default is 1.
            All of the messages are not necessarily returned.
            
    :type MaxNumberOfMessages: integer
    :param VisibilityTimeout: The duration (in seconds) that the received messages are hidden from subsequent retrieve requests after being retrieved by a ReceiveMessage request.
    :type VisibilityTimeout: integer
    :param WaitTimeSeconds: The duration (in seconds) for which the call will wait for a message to arrive in the queue before returning. If a message is available, the call will return sooner than WaitTimeSeconds.
    :type WaitTimeSeconds: integer
    """
    pass


def remove_permission(QueueUrl=None, Label=None):
    """
    :param QueueUrl: [REQUIRED]
            The URL of the Amazon SQS queue to take action on.
            Queue URLs are case-sensitive.
            
    :type QueueUrl: string
    :param Label: [REQUIRED]
            The identification of the permission to remove. This is the label added with the AddPermission action.
            
    :type Label: string
    """
    pass


def send_message(QueueUrl=None, MessageBody=None, DelaySeconds=None, MessageAttributes=None):
    """
    :param QueueUrl: [REQUIRED]
            The URL of the Amazon SQS queue to take action on.
            Queue URLs are case-sensitive.
            
    :type QueueUrl: string
    :param MessageBody: [REQUIRED]
            The message to send. String maximum 256 KB in size. For a list of allowed characters, see the preceding important note.
            
    :type MessageBody: string
    :param DelaySeconds: The number of seconds (0 to 900 - 15 minutes) to delay a specific message. Messages with a positive DelaySeconds value become available for processing after the delay time is finished. If you don't specify a value, the default value for the queue applies.
    :type DelaySeconds: integer
    :param MessageAttributes: Each message attribute consists of a Name, Type, and Value. For more information, see Message Attribute Items .
            (string) --
            (dict) --The user-specified message attribute value. For string data types, the value attribute has the same restrictions on the content as the message body. For more information, see SendMessage .
            Name, type, and value must not be empty or null. In addition, the message body should not be empty or null. All parts of the message attribute, including name, type, and value, are included in the message size restriction, which is currently 256 KB (262,144 bytes).
            StringValue (string) --Strings are Unicode with UTF8 binary encoding. For a list of code values, see http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters .
            BinaryValue (bytes) --Binary type attributes can store any binary data, for example, compressed data, encrypted data, or images.
            StringListValues (list) --Not implemented. Reserved for future use.
            (string) --
            BinaryListValues (list) --Not implemented. Reserved for future use.
            (bytes) --
            DataType (string) -- [REQUIRED]Amazon SQS supports the following logical data types: String, Number, and Binary. For the Number data type, you must use StringValue.
            You can also append custom labels. For more information, see Message Attribute Data Types .
            
            
    :type MessageAttributes: dict
    """
    pass


def send_message_batch(QueueUrl=None, Entries=None):
    """
    :param QueueUrl: [REQUIRED]
            The URL of the Amazon SQS queue to take action on.
            Queue URLs are case-sensitive.
            
    :type QueueUrl: string
    :param Entries: [REQUIRED]
            A list of SendMessageBatchRequestEntry items.
            (dict) --Contains the details of a single Amazon SQS message along with a Id .
            Id (string) -- [REQUIRED]An identifier for the message in this batch. This is used to communicate the result. Note that the Id s of a batch request need to be unique within the request.
            MessageBody (string) -- [REQUIRED]Body of the message.
            DelaySeconds (integer) --The number of seconds for which the message has to be delayed.
            MessageAttributes (dict) --Each message attribute consists of a Name, Type, and Value. For more information, see Message Attribute Items .
            (string) --
            (dict) --The user-specified message attribute value. For string data types, the value attribute has the same restrictions on the content as the message body. For more information, see SendMessage .
            Name, type, and value must not be empty or null. In addition, the message body should not be empty or null. All parts of the message attribute, including name, type, and value, are included in the message size restriction, which is currently 256 KB (262,144 bytes).
            StringValue (string) --Strings are Unicode with UTF8 binary encoding. For a list of code values, see http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters .
            BinaryValue (bytes) --Binary type attributes can store any binary data, for example, compressed data, encrypted data, or images.
            StringListValues (list) --Not implemented. Reserved for future use.
            (string) --
            BinaryListValues (list) --Not implemented. Reserved for future use.
            (bytes) --
            DataType (string) -- [REQUIRED]Amazon SQS supports the following logical data types: String, Number, and Binary. For the Number data type, you must use StringValue.
            You can also append custom labels. For more information, see Message Attribute Data Types .
            
            
            
    :type Entries: list
    """
    pass


def set_queue_attributes(QueueUrl=None, Attributes=None):
    """
    :param QueueUrl: [REQUIRED]
            The URL of the Amazon SQS queue to take action on.
            Queue URLs are case-sensitive.
            
    :type QueueUrl: string
    :param Attributes: [REQUIRED]
            A map of attributes to set.
            The following lists the names, descriptions, and values of the special request parameters the SetQueueAttributes action uses:
            DelaySeconds - The time in seconds that the delivery of all messages in the queue will be delayed. An integer from 0 to 900 (15 minutes). The default for this attribute is 0 (zero).
            MaximumMessageSize - The limit of how many bytes a message can contain before Amazon SQS rejects it. An integer from 1024 bytes (1 KiB) up to 262144 bytes (256 KiB). The default for this attribute is 262144 (256 KiB).
            MessageRetentionPeriod - The number of seconds Amazon SQS retains a message. Integer representing seconds, from 60 (1 minute) to 1209600 (14 days). The default for this attribute is 345600 (4 days).
            Policy - The queue's policy. A valid AWS policy. For more information about policy structure, see Overview of AWS IAM Policies in the Amazon IAM User Guide .
            ReceiveMessageWaitTimeSeconds - The time for which a ReceiveMessage call will wait for a message to arrive. An integer from 0 to 20 (seconds). The default for this attribute is 0.
            VisibilityTimeout - The visibility timeout for the queue. An integer from 0 to 43200 (12 hours). The default for this attribute is 30. For more information about visibility timeout, see Visibility Timeout in the Amazon SQS Developer Guide .
            RedrivePolicy - The parameters for dead letter queue functionality of the source queue. For more information about RedrivePolicy and dead letter queues, see Using Amazon SQS Dead Letter Queues in the Amazon SQS Developer Guide .
            Any other valid special request parameters that are specified (such as ApproximateNumberOfMessages , ApproximateNumberOfMessagesDelayed , ApproximateNumberOfMessagesNotVisible , CreatedTimestamp , LastModifiedTimestamp , and QueueArn ) will be ignored.
            (string) --
            (string) --
            
    :type Attributes: dict
    """
    pass
