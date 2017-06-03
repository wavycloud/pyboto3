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

def add_permission(QueueUrl=None, Label=None, AWSAccountIds=None, Actions=None):
    """
    Adds a permission to a queue for a specific principal . This allows sharing access to the queue.
    When you create a queue, you have full control access rights for the queue. Only you, the owner of the queue, can grant or deny permissions to the queue. For more information about these permissions, see Shared Queues in the Amazon SQS Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.add_permission(
        QueueUrl='string',
        Label='string',
        AWSAccountIds=[
            'string',
        ],
        Actions=[
            'string',
        ]
    )
    
    
    :type QueueUrl: string
    :param QueueUrl: [REQUIRED]
            The URL of the Amazon SQS queue to which permissions are added.
            Queue URLs are case-sensitive.
            

    :type Label: string
    :param Label: [REQUIRED]
            The unique identification of the permission you're setting (for example, AliceSendMessage ). Maximum 80 characters. Allowed characters include alphanumeric characters, hyphens (- ), and underscores (_ ).
            

    :type AWSAccountIds: list
    :param AWSAccountIds: [REQUIRED]
            The AWS account number of the principal who is given permission. The principal must have an AWS account, but does not need to be signed up for Amazon SQS. For information about locating the AWS account identification, see Your AWS Identifiers in the Amazon SQS Developer Guide .
            (string) --
            

    :type Actions: list
    :param Actions: [REQUIRED]
            The action the client wants to allow for the specified principal. The following values are valid:
            *
            ChangeMessageVisibility
            DeleteMessage
            GetQueueAttributes
            GetQueueUrl
            ReceiveMessage
            SendMessage
            For more information about these actions, see Understanding Permissions in the Amazon SQS Developer Guide .
            Specifying SendMessage , DeleteMessage , or ChangeMessageVisibility for ActionName.n also grants permissions for the corresponding batch versions of those actions: SendMessageBatch , DeleteMessageBatch , and ChangeMessageVisibilityBatch .
            (string) --
            

    """
    pass

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

def change_message_visibility(QueueUrl=None, ReceiptHandle=None, VisibilityTimeout=None):
    """
    Changes the visibility timeout of a specified message in a queue to a new value. The maximum allowed timeout value is 12 hours. Thus, you can't extend the timeout of a message in an existing queue to more than a total visibility timeout of 12 hours. For more information, see Visibility Timeout in the Amazon SQS Developer Guide .
    For example, you have a message and with the default visibility timeout of 5 minutes. After 3 minutes, you call ChangeMessageVisiblity with a timeout of 10 minutes. At that time, the timeout for the message is extended by 10 minutes beyond the time of the ChangeMessageVisibility action. This results in a total visibility timeout of 13 minutes. You can continue to call the ChangeMessageVisibility to extend the visibility timeout to a maximum of 12 hours. If you try to extend the visibility timeout beyond 12 hours, your request is rejected.
    A message is considered to be in flight after it's received from a queue by a consumer, but not yet deleted from the queue.
    For standard queues, there can be a maximum of 120,000 inflight messages per queue. If you reach this limit, Amazon SQS returns the OverLimit error message. To avoid reaching the limit, you should delete messages from the queue after they're processed. You can also increase the number of queues you use to process your messages.
    For FIFO queues, there can be a maximum of 20,000 inflight messages per queue. If you reach this limit, Amazon SQS returns no error messages.
    See also: AWS API Documentation
    
    
    :example: response = client.change_message_visibility(
        QueueUrl='string',
        ReceiptHandle='string',
        VisibilityTimeout=123
    )
    
    
    :type QueueUrl: string
    :param QueueUrl: [REQUIRED]
            The URL of the Amazon SQS queue whose message's visibility is changed.
            Queue URLs are case-sensitive.
            

    :type ReceiptHandle: string
    :param ReceiptHandle: [REQUIRED]
            The receipt handle associated with the message whose visibility timeout is changed. This parameter is returned by the `` ReceiveMessage `` action.
            

    :type VisibilityTimeout: integer
    :param VisibilityTimeout: [REQUIRED]
            The new value for the message's visibility timeout (in seconds). Values values: 0 to 43200 . Maximum: 12 hours.
            

    """
    pass

def change_message_visibility_batch(QueueUrl=None, Entries=None):
    """
    Changes the visibility timeout of multiple messages. This is a batch version of ``  ChangeMessageVisibility .`` The result of the action on each message is reported individually in the response. You can send up to 10 ``  ChangeMessageVisibility `` requests with each ChangeMessageVisibilityBatch action.
    See also: AWS API Documentation
    
    
    :example: response = client.change_message_visibility_batch(
        QueueUrl='string',
        Entries=[
            {
                'Id': 'string',
                'ReceiptHandle': 'string',
                'VisibilityTimeout': 123
            },
        ]
    )
    
    
    :type QueueUrl: string
    :param QueueUrl: [REQUIRED]
            The URL of the Amazon SQS queue whose messages' visibility is changed.
            Queue URLs are case-sensitive.
            

    :type Entries: list
    :param Entries: [REQUIRED]
            A list of receipt handles of the messages for which the visibility timeout must be changed.
            (dict) --Encloses a receipt handle and an entry id for each message in `` ChangeMessageVisibilityBatch .``
            Warning
            All of the following list parameters must be prefixed with ChangeMessageVisibilityBatchRequestEntry.n , where n is an integer value starting with 1 . For example, a parameter list for this action might look like this:
            amp;ChangeMessageVisibilityBatchRequestEntry.1.Id=change_visibility_msg_2
            amp;ChangeMessageVisibilityBatchRequestEntry.1.ReceiptHandle=replaceableYour_Receipt_Handle/replaceable
            amp;ChangeMessageVisibilityBatchRequestEntry.1.VisibilityTimeout=45
            Id (string) -- [REQUIRED]An identifier for this particular receipt handle used to communicate the result.
            Note
            The Id s of a batch request need to be unique within a request
            ReceiptHandle (string) -- [REQUIRED]A receipt handle.
            VisibilityTimeout (integer) --The new value (in seconds) for the message's visibility timeout.
            
            

    :rtype: dict
    :return: {
        'Successful': [
            {
                'Id': 'string'
            },
        ],
        'Failed': [
            {
                'Id': 'string',
                'SenderFault': True|False,
                'Code': 'string',
                'Message': 'string'
            },
        ]
    }
    
    
    """
    pass

def create_queue(QueueName=None, Attributes=None):
    """
    Creates a new standard or FIFO queue. You can pass one or more attributes in the request. Keep the following caveats in mind:
    To successfully create a new queue, you must provide a queue name that adheres to the limits related to queues and is unique within the scope of your queues.
    To get the queue URL, use the ``  GetQueueUrl `` action. ``  GetQueueUrl `` requires only the QueueName parameter. be aware of existing queue names:
    See also: AWS API Documentation
    
    Examples
    The following operation creates an SQS queue named MyQueue.
    Expected Output:
    
    :example: response = client.create_queue(
        QueueName='string',
        Attributes={
            'string': 'string'
        }
    )
    
    
    :type QueueName: string
    :param QueueName: [REQUIRED]
            The name of the new queue. The following limits apply to this name:
            A queue name can have up to 80 characters.
            Valid values: alphanumeric characters, hyphens (- ), and underscores (_ ).
            A FIFO queue name must end with the .fifo suffix.
            Queue names are case-sensitive.
            

    :type Attributes: dict
    :param Attributes: A map of attributes with their corresponding values.
            The following lists the names, descriptions, and values of the special request parameters that the CreateQueue action uses:
            DelaySeconds - The length of time, in seconds, for which the delivery of all messages in the queue is delayed. Valid values: An integer from 0 to 900 seconds (15 minutes). The default is 0 (zero).
            MaximumMessageSize - The limit of how many bytes a message can contain before Amazon SQS rejects it. Valid values: An integer from 1,024 bytes (1 KiB) to 262,144 bytes (256 KiB). The default is 262,144 (256 KiB).
            MessageRetentionPeriod - The length of time, in seconds, for which Amazon SQS retains a message. Valid values: An integer from 60 seconds (1 minute) to 1,209,600 seconds (14 days). The default is 345,600 (4 days).
            Policy - The queue's policy. A valid AWS policy. For more information about policy structure, see Overview of AWS IAM Policies in the Amazon IAM User Guide .
            ReceiveMessageWaitTimeSeconds - The length of time, in seconds, for which a `` ReceiveMessage `` action waits for a message to arrive. Valid values: An integer from 0 to 20 (seconds). The default is 0 (zero).
            RedrivePolicy - The parameters for the dead letter queue functionality of the source queue. For more information about the redrive policy and dead letter queues, see Using Amazon SQS Dead Letter Queues in the Amazon SQS Developer Guide .
            Note
            The dead letter queue of a FIFO queue must also be a FIFO queue. Similarly, the dead letter queue of a standard queue must also be a standard queue.
            VisibilityTimeout - The visibility timeout for the queue. Valid values: An integer from 0 to 43,200 (12 hours). The default is 30. For more information about the visibility timeout, see Visibility Timeout in the Amazon SQS Developer Guide .
            The following attributes apply only to server-side-encryption :
            KmsMasterKeyId - The ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK. For more information, see Key Terms . While the alias of the AWS-managed CMK for Amazon SQS is always alias/aws/sqs , the alias of a custom CMK can, for example, be alias/aws/sqs . For more examples, see KeyId in the AWS Key Management Service API Reference .
            KmsDataKeyReusePeriodSeconds - The length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. An integer representing seconds, between 60 seconds (1 minute) and 86,400 seconds (24 hours). The default is 300 (5 minutes). A shorter time period provides better security but results in more calls to KMS which incur charges after Free Tier. For more information, see How Does the Data Key Reuse Period Work? .
            The following attributes apply only to FIFO (first-in-first-out) queues :
            FifoQueue - Designates a queue as FIFO. Valid values: true , false . You can provide this attribute only during queue creation. You can't change it for an existing queue. When you set this attribute, you must also provide the MessageGroupId for your messages explicitly. For more information, see FIFO Queue Logic in the Amazon SQS Developer Guide .
            ContentBasedDeduplication - Enables content-based deduplication. Valid values: true , false . For more information, see Exactly-Once Processing in the Amazon SQS Developer Guide .
            Every message must have a unique MessageDeduplicationId ,
            You may provide a MessageDeduplicationId explicitly.
            If you aren't able to provide a MessageDeduplicationId and you enable ContentBasedDeduplication for your queue, Amazon SQS uses a SHA-256 hash to generate the MessageDeduplicationId using the body of the message (but not the attributes of the message).
            If you don't provide a MessageDeduplicationId and the queue doesn't have ContentBasedDeduplication set, the action fails with an error.
            If the queue has ContentBasedDeduplication set, your MessageDeduplicationId overrides the generated one.
            When ContentBasedDeduplication is in effect, messages with identical content sent within the deduplication interval are treated as duplicates and only one copy of the message is delivered.
            If you send one message with ContentBasedDeduplication enabled and then another message with a MessageDeduplicationId that is the same as the one generated for the first MessageDeduplicationId , the two messages are treated as duplicates and only one copy of the message is delivered.
            Any other valid special request parameters (such as the following) are ignored:
            ApproximateNumberOfMessages
            ApproximateNumberOfMessagesDelayed
            ApproximateNumberOfMessagesNotVisible
            CreatedTimestamp
            LastModifiedTimestamp
            QueueArn
            (string) --
            (string) --
            

    :rtype: dict
    :return: {
        'QueueUrl': 'string'
    }
    
    
    :returns: 
    If you don't provide a value for an attribute, the queue is created with the default value for the attribute.
    If you delete a queue, you must wait at least 60 seconds before creating a queue with the same name.
    
    """
    pass

def delete_message(QueueUrl=None, ReceiptHandle=None):
    """
    Deletes the specified message from the specified queue. You specify the message by using the message's receipt handle and not the MessageId you receive when you send the message. Even if the message is locked by another reader due to the visibility timeout setting, it is still deleted from the queue. If you leave a message in the queue for longer than the queue's configured retention period, Amazon SQS automatically deletes the message.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_message(
        QueueUrl='string',
        ReceiptHandle='string'
    )
    
    
    :type QueueUrl: string
    :param QueueUrl: [REQUIRED]
            The URL of the Amazon SQS queue from which messages are deleted.
            Queue URLs are case-sensitive.
            

    :type ReceiptHandle: string
    :param ReceiptHandle: [REQUIRED]
            The receipt handle associated with the message to delete.
            

    """
    pass

def delete_message_batch(QueueUrl=None, Entries=None):
    """
    Deletes up to ten messages from the specified queue. This is a batch version of ``  DeleteMessage .`` The result of the action on each message is reported individually in the response.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_message_batch(
        QueueUrl='string',
        Entries=[
            {
                'Id': 'string',
                'ReceiptHandle': 'string'
            },
        ]
    )
    
    
    :type QueueUrl: string
    :param QueueUrl: [REQUIRED]
            The URL of the Amazon SQS queue from which messages are deleted.
            Queue URLs are case-sensitive.
            

    :type Entries: list
    :param Entries: [REQUIRED]
            A list of receipt handles for the messages to be deleted.
            (dict) --Encloses a receipt handle and an identifier for it.
            Id (string) -- [REQUIRED]An identifier for this particular receipt handle. This is used to communicate the result.
            Note
            The Id s of a batch request need to be unique within a request
            ReceiptHandle (string) -- [REQUIRED]A receipt handle.
            
            

    :rtype: dict
    :return: {
        'Successful': [
            {
                'Id': 'string'
            },
        ],
        'Failed': [
            {
                'Id': 'string',
                'SenderFault': True|False,
                'Code': 'string',
                'Message': 'string'
            },
        ]
    }
    
    
    """
    pass

def delete_queue(QueueUrl=None):
    """
    Deletes the queue specified by the QueueUrl , even if the queue is empty. If the specified queue doesn't exist, Amazon SQS returns a successful response.
    When you delete a queue, the deletion process takes up to 60 seconds. Requests you send involving that queue during the 60 seconds might succeed. For example, a ``  SendMessage `` request might succeed, but after 60 seconds the queue and the message you sent no longer exist.
    When you delete a queue, you must wait at least 60 seconds before creating a queue with the same name.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_queue(
        QueueUrl='string'
    )
    
    
    :type QueueUrl: string
    :param QueueUrl: [REQUIRED]
            The URL of the Amazon SQS queue to delete.
            Queue URLs are case-sensitive.
            

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

def get_queue_attributes(QueueUrl=None, AttributeNames=None):
    """
    Gets attributes for the specified queue.
    See also: AWS API Documentation
    
    
    :example: response = client.get_queue_attributes(
        QueueUrl='string',
        AttributeNames=[
            'All'|'Policy'|'VisibilityTimeout'|'MaximumMessageSize'|'MessageRetentionPeriod'|'ApproximateNumberOfMessages'|'ApproximateNumberOfMessagesNotVisible'|'CreatedTimestamp'|'LastModifiedTimestamp'|'QueueArn'|'ApproximateNumberOfMessagesDelayed'|'DelaySeconds'|'ReceiveMessageWaitTimeSeconds'|'RedrivePolicy'|'FifoQueue'|'ContentBasedDeduplication'|'KmsMasterKeyId'|'KmsDataKeyReusePeriodSeconds',
        ]
    )
    
    
    :type QueueUrl: string
    :param QueueUrl: [REQUIRED]
            The URL of the Amazon SQS queue whose attribute information is retrieved.
            Queue URLs are case-sensitive.
            

    :type AttributeNames: list
    :param AttributeNames: A list of attributes for which to retrieve information.
            Note
            In the future, new attributes might be added. If you write code that calls this action, we recommend that you structure your code so that it can handle new attributes gracefully.
            The following attributes are supported:
            All - Returns all values.
            ApproximateNumberOfMessages - Returns the approximate number of visible messages in a queue. For more information, see Resources Required to Process Messages in the Amazon SQS Developer Guide .
            ApproximateNumberOfMessagesDelayed - Returns the approximate number of messages that are waiting to be added to the queue.
            ApproximateNumberOfMessagesNotVisible - Returns the approximate number of messages that have not timed-out and aren't deleted. For more information, see Resources Required to Process Messages in the Amazon SQS Developer Guide .
            CreatedTimestamp - Returns the time when the queue was created in seconds (epoch time ).
            DelaySeconds - Returns the default delay on the queue in seconds.
            LastModifiedTimestamp - Returns the time when the queue was last changed in seconds (epoch time ).
            MaximumMessageSize - Returns the limit of how many bytes a message can contain before Amazon SQS rejects it.
            MessageRetentionPeriod - Returns the length of time, in seconds, for which Amazon SQS retains a message.
            Policy - Returns the policy of the queue.
            QueueArn - Returns the Amazon resource name (ARN) of the queue.
            ReceiveMessageWaitTimeSeconds - Returns the length of time, in seconds, for which the ReceiveMessage action waits for a message to arrive.
            RedrivePolicy - Returns the parameters for dead letter queue functionality of the source queue. For more information about the redrive policy and dead letter queues, see Using Amazon SQS Dead Letter Queues in the Amazon SQS Developer Guide .
            VisibilityTimeout - Returns the visibility timeout for the queue. For more information about the visibility timeout, see Visibility Timeout in the Amazon SQS Developer Guide .
            The following attributes apply only to server-side-encryption :
            KmsMasterKeyId - Returns the ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK. For more information, see Key Terms .
            KmsDataKeyReusePeriodSeconds - Returns the length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again.
            The following attributes apply only to FIFO (first-in-first-out) queues :
            FifoQueue - Returns whether the queue is FIFO. For more information, see FIFO Queue Logic in the Amazon SQS Developer Guide .
            Note
            To determine whether a queue is FIFO , you can check whether QueueName ends with the .fifo suffix.
            ContentBasedDeduplication - Returns whether content-based deduplication is enabled for the queue. For more information, see Exactly-Once Processing in the Amazon SQS Developer Guide .
            (string) --
            

    :rtype: dict
    :return: {
        'Attributes': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_queue_url(QueueName=None, QueueOwnerAWSAccountId=None):
    """
    Returns the URL of an existing queue. This action provides a simple way to retrieve the URL of an Amazon SQS queue.
    To access a queue that belongs to another AWS account, use the QueueOwnerAWSAccountId parameter to specify the account ID of the queue's owner. The queue's owner must grant you permission to access the queue. For more information about shared queue access, see ``  AddPermission `` or see Shared Queues in the Amazon SQS Developer Guide .
    See also: AWS API Documentation
    
    Examples
    The following example retrieves the queue ARN.
    Expected Output:
    
    :example: response = client.get_queue_url(
        QueueName='string',
        QueueOwnerAWSAccountId='string'
    )
    
    
    :type QueueName: string
    :param QueueName: [REQUIRED]
            The name of the queue whose URL must be fetched. Maximum 80 characters. Valid values: alphanumeric characters, hyphens (- ), and underscores (_ ).
            Queue names are case-sensitive.
            

    :type QueueOwnerAWSAccountId: string
    :param QueueOwnerAWSAccountId: The AWS account ID of the account that created the queue.

    :rtype: dict
    :return: {
        'QueueUrl': 'string'
    }
    
    
    """
    pass

def get_waiter():
    """
    
    """
    pass

def list_dead_letter_source_queues(QueueUrl=None):
    """
    Returns a list of your queues that have the RedrivePolicy queue attribute configured with a dead letter queue.
    For more information about using dead letter queues, see Using Amazon SQS Dead Letter Queues in the Amazon SQS Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.list_dead_letter_source_queues(
        QueueUrl='string'
    )
    
    
    :type QueueUrl: string
    :param QueueUrl: [REQUIRED]
            The URL of a dead letter queue.
            Queue URLs are case-sensitive.
            

    :rtype: dict
    :return: {
        'queueUrls': [
            'string',
        ]
    }
    
    
    """
    pass

def list_queues(QueueNamePrefix=None):
    """
    Returns a list of your queues. The maximum number of queues that can be returned is 1,000. If you specify a value for the optional QueueNamePrefix parameter, only queues with a name that begins with the specified value are returned.
    See also: AWS API Documentation
    
    
    :example: response = client.list_queues(
        QueueNamePrefix='string'
    )
    
    
    :type QueueNamePrefix: string
    :param QueueNamePrefix: A string to use for filtering the list results. Only those queues whose name begins with the specified string are returned.
            Queue names are case-sensitive.
            

    :rtype: dict
    :return: {
        'QueueUrls': [
            'string',
        ]
    }
    
    
    """
    pass

def purge_queue(QueueUrl=None):
    """
    Deletes the messages in a queue specified by the QueueURL parameter.
    When you purge a queue, the message deletion process takes up to 60 seconds. All messages sent to the queue before calling the PurgeQueue action are deleted. Messages sent to the queue while it is being purged might be deleted. While the queue is being purged, messages sent to the queue before PurgeQueue is called might be received, but are deleted within the next minute.
    See also: AWS API Documentation
    
    
    :example: response = client.purge_queue(
        QueueUrl='string'
    )
    
    
    :type QueueUrl: string
    :param QueueUrl: [REQUIRED]
            The URL of the queue from which the PurgeQueue action deletes messages.
            Queue URLs are case-sensitive.
            

    """
    pass

def receive_message(QueueUrl=None, AttributeNames=None, MessageAttributeNames=None, MaxNumberOfMessages=None, VisibilityTimeout=None, WaitTimeSeconds=None, ReceiveRequestAttemptId=None):
    """
    Retrieves one or more messages (up to 10), from the specified queue. Using the WaitTimeSeconds parameter enables long-poll support. For more information, see Amazon SQS Long Polling in the Amazon SQS Developer Guide .
    Short poll is the default behavior where a weighted random set of machines is sampled on a ReceiveMessage call. Thus, only the messages on the sampled machines are returned. If the number of messages in the queue is small (fewer than 1,000), you most likely get fewer messages than you requested per ReceiveMessage call. If the number of messages in the queue is extremely small, you might not receive any messages in a particular ReceiveMessage response. If this happens, repeat the request.
    For each message returned, the response includes the following:
    The receipt handle is the identifier you must provide when deleting the message. For more information, see Queue and Message Identifiers in the Amazon SQS Developer Guide .
    You can provide the VisibilityTimeout parameter in your request. The parameter is applied to the messages that Amazon SQS returns in the response. If you don't include the parameter, the overall visibility timeout for the queue is used for the returned messages. For more information, see Visibility Timeout in the Amazon SQS Developer Guide .
    A message that isn't deleted or a message whose visibility isn't extended before the visibility timeout expires counts as a failed receive. Depending on the configuration of the queue, the message might be sent to the dead letter queue.
    See also: AWS API Documentation
    
    
    :example: response = client.receive_message(
        QueueUrl='string',
        AttributeNames=[
            'All'|'Policy'|'VisibilityTimeout'|'MaximumMessageSize'|'MessageRetentionPeriod'|'ApproximateNumberOfMessages'|'ApproximateNumberOfMessagesNotVisible'|'CreatedTimestamp'|'LastModifiedTimestamp'|'QueueArn'|'ApproximateNumberOfMessagesDelayed'|'DelaySeconds'|'ReceiveMessageWaitTimeSeconds'|'RedrivePolicy'|'FifoQueue'|'ContentBasedDeduplication'|'KmsMasterKeyId'|'KmsDataKeyReusePeriodSeconds',
        ],
        MessageAttributeNames=[
            'string',
        ],
        MaxNumberOfMessages=123,
        VisibilityTimeout=123,
        WaitTimeSeconds=123,
        ReceiveRequestAttemptId='string'
    )
    
    
    :type QueueUrl: string
    :param QueueUrl: [REQUIRED]
            The URL of the Amazon SQS queue from which messages are received.
            Queue URLs are case-sensitive.
            

    :type AttributeNames: list
    :param AttributeNames: A list of attributes that need to be returned along with each message. These attributes include:
            All - Returns all values.
            ApproximateFirstReceiveTimestamp - Returns the time the message was first received from the queue (epoch time in milliseconds).
            ApproximateReceiveCount - Returns the number of times a message has been received from the queue but not deleted.
            SenderId
            For an IAM user, returns the IAM user ID, for example ABCDEFGHI1JKLMNOPQ23R .
            For an IAM role, returns the IAM role ID, for example ABCDE1F2GH3I4JK5LMNOP:i-a123b456 .
            SentTimestamp - Returns the time the message was sent to the queue (epoch time in milliseconds).
            MessageDeduplicationId - Returns the value provided by the sender that calls the `` SendMessage `` action.
            MessageGroupId - Returns the value provided by the sender that calls the `` SendMessage `` action. Messages with the same MessageGroupId are returned in sequence.
            SequenceNumber - Returns the value provided by Amazon SQS.
            Any other valid special request parameters (such as the following) are ignored:
            ApproximateNumberOfMessages
            ApproximateNumberOfMessagesDelayed
            ApproximateNumberOfMessagesNotVisible
            CreatedTimestamp
            ContentBasedDeduplication
            DelaySeconds
            FifoQueue
            LastModifiedTimestamp
            MaximumMessageSize
            MessageRetentionPeriod
            Policy
            QueueArn ,
            ReceiveMessageWaitTimeSeconds
            RedrivePolicy
            VisibilityTimeout
            (string) --
            

    :type MessageAttributeNames: list
    :param MessageAttributeNames: The name of the message attribute, where N is the index.
            The name can contain alphanumeric characters and the underscore (_ ), hyphen (- ), and period (. ).
            The name is case-sensitive and must be unique among all attribute names for the message.
            The name must not start with AWS-reserved prefixes such as AWS. or Amazon. (or any casing variants).
            The name must not start or end with a period (. ), and it should not have periods in succession (.. ).
            The name can be up to 256 characters long.
            When using ReceiveMessage , you can send a list of attribute names to receive, or you can return all of the attributes by specifying All or .* in your request. You can also use all message attributes starting with a prefix, for example bar.* .
            (string) --
            

    :type MaxNumberOfMessages: integer
    :param MaxNumberOfMessages: The maximum number of messages to return. Amazon SQS never returns more messages than this value (however, fewer messages might be returned). Valid values are 1 to 10. Default is 1.

    :type VisibilityTimeout: integer
    :param VisibilityTimeout: The duration (in seconds) that the received messages are hidden from subsequent retrieve requests after being retrieved by a ReceiveMessage request.

    :type WaitTimeSeconds: integer
    :param WaitTimeSeconds: The duration (in seconds) for which the call waits for a message to arrive in the queue before returning. If a message is available, the call returns sooner than WaitTimeSeconds .

    :type ReceiveRequestAttemptId: string
    :param ReceiveRequestAttemptId: This parameter applies only to FIFO (first-in-first-out) queues.
            The token used for deduplication of ReceiveMessage calls. If a networking issue occurs after a ReceiveMessage action, and instead of a response you receive a generic error, you can retry the same action with an identical ReceiveRequestAttemptId to retrieve the same set of messages, even if their visibility timeout has not yet expired.
            You can use ReceiveRequestAttemptId only for 5 minutes after a ReceiveMessage action.
            When you set FifoQueue , a caller of the ReceiveMessage action can provide a ReceiveRequestAttemptId explicitly.
            If a caller of the ReceiveMessage action doesn't provide a ReceiveRequestAttemptId , Amazon SQS generates a ReceiveRequestAttemptId .
            You can retry the ReceiveMessage action with the same ReceiveRequestAttemptId if none of the messages have been modified (deleted or had their visibility changes).
            During a visibility timeout, subsequent calls with the same ReceiveRequestAttemptId return the same messages and receipt handles. If a retry occurs within the deduplication interval, it resets the visibility timeout. For more information, see Visibility Timeout in the Amazon Simple Queue Service Developer Guide .
            Warning
            If a caller of the ReceiveMessage action is still processing messages when the visibility timeout expires and messages become visible, another worker reading from the same queue can receive the same messages and therefore process duplicates. Also, if a reader whose message processing time is longer than the visibility timeout tries to delete the processed messages, the action fails with an error. To mitigate this effect, ensure that your application observes a safe threshold before the visibility timeout expires and extend the visibility timeout as necessary.
            While messages with a particular MessageGroupId are invisible, no more messages belonging to the same MessageGroupId are returned until the visibility timeout expires. You can still receive messages with another MessageGroupId as long as it is also visible.
            If a caller of ReceiveMessage can't track the ReceiveRequestAttemptId , no retries work until the original visibility timeout expires. As a result, delays might occur but the messages in the queue remain in a strict order.
            The length of ReceiveRequestAttemptId is 128 characters. ReceiveRequestAttemptId can contain alphanumeric characters (a-z , A-Z , 0-9 ) and punctuation (!'#$%'()*+,-./:;=?@[\]^_`{|}~ ).
            For best practices of using ReceiveRequestAttemptId , see Using the ReceiveRequestAttemptId Request Parameter in the Amazon Simple Queue Service Developer Guide .
            

    :rtype: dict
    :return: {
        'Messages': [
            {
                'MessageId': 'string',
                'ReceiptHandle': 'string',
                'MD5OfBody': 'string',
                'Body': 'string',
                'Attributes': {
                    'string': 'string'
                },
                'MD5OfMessageAttributes': 'string',
                'MessageAttributes': {
                    'string': {
                        'StringValue': 'string',
                        'BinaryValue': b'bytes',
                        'StringListValues': [
                            'string',
                        ],
                        'BinaryListValues': [
                            b'bytes',
                        ],
                        'DataType': 'string'
                    }
                }
            },
        ]
    }
    
    
    :returns: 
    QueueUrl (string) -- [REQUIRED]
    The URL of the Amazon SQS queue from which messages are received.
    Queue URLs are case-sensitive.
    
    AttributeNames (list) -- A list of attributes that need to be returned along with each message. These attributes include:
    
    All - Returns all values.
    ApproximateFirstReceiveTimestamp - Returns the time the message was first received from the queue (epoch time in milliseconds).
    ApproximateReceiveCount - Returns the number of times a message has been received from the queue but not deleted.
    SenderId
    For an IAM user, returns the IAM user ID, for example ABCDEFGHI1JKLMNOPQ23R .
    For an IAM role, returns the IAM role ID, for example ABCDE1F2GH3I4JK5LMNOP:i-a123b456 .
    
    
    SentTimestamp - Returns the time the message was sent to the queue (epoch time in milliseconds).
    MessageDeduplicationId - Returns the value provided by the sender that calls the ``  SendMessage `` action.
    MessageGroupId - Returns the value provided by the sender that calls the ``  SendMessage `` action. Messages with the same MessageGroupId are returned in sequence.
    SequenceNumber - Returns the value provided by Amazon SQS.
    
    Any other valid special request parameters (such as the following) are ignored:
    
    ApproximateNumberOfMessages
    ApproximateNumberOfMessagesDelayed
    ApproximateNumberOfMessagesNotVisible
    CreatedTimestamp
    ContentBasedDeduplication
    DelaySeconds
    FifoQueue
    LastModifiedTimestamp
    MaximumMessageSize
    MessageRetentionPeriod
    Policy
    QueueArn ,
    ReceiveMessageWaitTimeSeconds
    RedrivePolicy
    VisibilityTimeout
    
    
    (string) --
    
    
    MessageAttributeNames (list) -- The name of the message attribute, where N is the index.
    
    The name can contain alphanumeric characters and the underscore (_ ), hyphen (- ), and period (. ).
    The name is case-sensitive and must be unique among all attribute names for the message.
    The name must not start with AWS-reserved prefixes such as AWS. or Amazon. (or any casing variants).
    The name must not start or end with a period (. ), and it should not have periods in succession (.. ).
    The name can be up to 256 characters long.
    
    When using ReceiveMessage , you can send a list of attribute names to receive, or you can return all of the attributes by specifying All or .* in your request. You can also use all message attributes starting with a prefix, for example bar.* .
    
    (string) --
    
    
    MaxNumberOfMessages (integer) -- The maximum number of messages to return. Amazon SQS never returns more messages than this value (however, fewer messages might be returned). Valid values are 1 to 10. Default is 1.
    VisibilityTimeout (integer) -- The duration (in seconds) that the received messages are hidden from subsequent retrieve requests after being retrieved by a ReceiveMessage request.
    WaitTimeSeconds (integer) -- The duration (in seconds) for which the call waits for a message to arrive in the queue before returning. If a message is available, the call returns sooner than WaitTimeSeconds .
    ReceiveRequestAttemptId (string) -- This parameter applies only to FIFO (first-in-first-out) queues.
    The token used for deduplication of ReceiveMessage calls. If a networking issue occurs after a ReceiveMessage action, and instead of a response you receive a generic error, you can retry the same action with an identical ReceiveRequestAttemptId to retrieve the same set of messages, even if their visibility timeout has not yet expired.
    
    You can use ReceiveRequestAttemptId only for 5 minutes after a ReceiveMessage action.
    When you set FifoQueue , a caller of the ReceiveMessage action can provide a ReceiveRequestAttemptId explicitly.
    If a caller of the ReceiveMessage action doesn't provide a ReceiveRequestAttemptId , Amazon SQS generates a ReceiveRequestAttemptId .
    You can retry the ReceiveMessage action with the same ReceiveRequestAttemptId if none of the messages have been modified (deleted or had their visibility changes).
    During a visibility timeout, subsequent calls with the same ReceiveRequestAttemptId return the same messages and receipt handles. If a retry occurs within the deduplication interval, it resets the visibility timeout. For more information, see Visibility Timeout in the Amazon Simple Queue Service Developer Guide .
    
    
    Warning
    If a caller of the ReceiveMessage action is still processing messages when the visibility timeout expires and messages become visible, another worker reading from the same queue can receive the same messages and therefore process duplicates. Also, if a reader whose message processing time is longer than the visibility timeout tries to delete the processed messages, the action fails with an error. To mitigate this effect, ensure that your application observes a safe threshold before the visibility timeout expires and extend the visibility timeout as necessary.
    
    
    While messages with a particular MessageGroupId are invisible, no more messages belonging to the same MessageGroupId are returned until the visibility timeout expires. You can still receive messages with another MessageGroupId as long as it is also visible.
    If a caller of ReceiveMessage can't track the ReceiveRequestAttemptId , no retries work until the original visibility timeout expires. As a result, delays might occur but the messages in the queue remain in a strict order.
    
    The length of ReceiveRequestAttemptId is 128 characters. ReceiveRequestAttemptId can contain alphanumeric characters (a-z , A-Z , 0-9 ) and punctuation (!"#$%'()*+,-./:;=?@[\]^_`{|}~ ).
    For best practices of using ReceiveRequestAttemptId , see Using the ReceiveRequestAttemptId Request Parameter in the Amazon Simple Queue Service Developer Guide .
    
    
    """
    pass

def remove_permission(QueueUrl=None, Label=None):
    """
    Revokes any permissions in the queue policy that matches the specified Label parameter. Only the owner of the queue can remove permissions.
    See also: AWS API Documentation
    
    
    :example: response = client.remove_permission(
        QueueUrl='string',
        Label='string'
    )
    
    
    :type QueueUrl: string
    :param QueueUrl: [REQUIRED]
            The URL of the Amazon SQS queue from which permissions are removed.
            Queue URLs are case-sensitive.
            

    :type Label: string
    :param Label: [REQUIRED]
            The identification of the permission to remove. This is the label added using the `` AddPermission `` action.
            

    """
    pass

def send_message(QueueUrl=None, MessageBody=None, DelaySeconds=None, MessageAttributes=None, MessageDeduplicationId=None, MessageGroupId=None):
    """
    Delivers a message to the specified queue.
    See also: AWS API Documentation
    
    
    :example: response = client.send_message(
        QueueUrl='string',
        MessageBody='string',
        DelaySeconds=123,
        MessageAttributes={
            'string': {
                'StringValue': 'string',
                'BinaryValue': b'bytes',
                'StringListValues': [
                    'string',
                ],
                'BinaryListValues': [
                    b'bytes',
                ],
                'DataType': 'string'
            }
        },
        MessageDeduplicationId='string',
        MessageGroupId='string'
    )
    
    
    :type QueueUrl: string
    :param QueueUrl: [REQUIRED]
            The URL of the Amazon SQS queue to which a message is sent.
            Queue URLs are case-sensitive.
            

    :type MessageBody: string
    :param MessageBody: [REQUIRED]
            The message to send. The maximum string size is 256 KB.
            Warning
            A message can include only XML, JSON, and unformatted text. The following Unicode characters are allowed:
            #x9 | #xA | #xD | #x20 to #xD7FF | #xE000 to #xFFFD | #x10000 to #x10FFFF
            Any characters not included in this list will be rejected. For more information, see the W3C specification for characters .
            

    :type DelaySeconds: integer
    :param DelaySeconds: The length of time, in seconds, for which to delay a specific message. Valid values: 0 to 900. Maximum: 15 minutes. Messages with a positive DelaySeconds value become available for processing after the delay period is finished. If you don't specify a value, the default value for the queue applies.
            Note
            When you set FifoQueue , you can't set DelaySeconds per message. You can set this parameter only on a queue level.
            

    :type MessageAttributes: dict
    :param MessageAttributes: Each message attribute consists of a Name , Type , and Value . For more information, see Message Attribute Items and Validation in the Amazon SQS Developer Guide .
            (string) --
            (dict) --The user-specified message attribute value. For string data types, the Value attribute has the same restrictions on the content as the message body. For more information, see `` SendMessage .``
            Name , type , value and the message body must not be empty or null. All parts of the message attribute, including Name , Type , and Value , are part of the message size restriction (256 KB or 262,144 bytes).
            StringValue (string) --Strings are Unicode with UTF-8 binary encoding. For a list of code values, see ASCII Printable Characters .
            BinaryValue (bytes) --Binary type attributes can store any binary data, such as compressed data, encrypted data, or images.
            StringListValues (list) --Not implemented. Reserved for future use.
            (string) --
            BinaryListValues (list) --Not implemented. Reserved for future use.
            (bytes) --
            DataType (string) -- [REQUIRED]Amazon SQS supports the following logical data types: String , Number , and Binary . For the Number data type, you must use StringValue .
            You can also append custom labels. For more information, see Message Attribute Data Types and Validation in the Amazon SQS Developer Guide .
            
            

    :type MessageDeduplicationId: string
    :param MessageDeduplicationId: This parameter applies only to FIFO (first-in-first-out) queues.
            The token used for deduplication of sent messages. If a message with a particular MessageDeduplicationId is sent successfully, any messages sent with the same MessageDeduplicationId are accepted successfully but aren't delivered during the 5-minute deduplication interval. For more information, see Exactly-Once Processing in the Amazon SQS Developer Guide .
            Every message must have a unique MessageDeduplicationId ,
            You may provide a MessageDeduplicationId explicitly.
            If you aren't able to provide a MessageDeduplicationId and you enable ContentBasedDeduplication for your queue, Amazon SQS uses a SHA-256 hash to generate the MessageDeduplicationId using the body of the message (but not the attributes of the message).
            If you don't provide a MessageDeduplicationId and the queue doesn't have ContentBasedDeduplication set, the action fails with an error.
            If the queue has ContentBasedDeduplication set, your MessageDeduplicationId overrides the generated one.
            When ContentBasedDeduplication is in effect, messages with identical content sent within the deduplication interval are treated as duplicates and only one copy of the message is delivered.
            If you send one message with ContentBasedDeduplication enabled and then another message with a MessageDeduplicationId that is the same as the one generated for the first MessageDeduplicationId , the two messages are treated as duplicates and only one copy of the message is delivered.
            Note
            The MessageDeduplicationId is available to the recipient of the message (this can be useful for troubleshooting delivery issues).
            If a message is sent successfully but the acknowledgement is lost and the message is resent with the same MessageDeduplicationId after the deduplication interval, Amazon SQS can't detect duplicate messages.
            The length of MessageDeduplicationId is 128 characters. MessageDeduplicationId can contain alphanumeric characters (a-z , A-Z , 0-9 ) and punctuation (!'#$%'()*+,-./:;=?@[\]^_`{|}~ ).
            For best practices of using MessageDeduplicationId , see Using the MessageDeduplicationId Property in the Amazon Simple Queue Service Developer Guide .
            

    :type MessageGroupId: string
    :param MessageGroupId: This parameter applies only to FIFO (first-in-first-out) queues.
            The tag that specifies that a message belongs to a specific message group. Messages that belong to the same message group are processed in a FIFO manner (however, messages in different message groups might be processed out of order). To interleave multiple ordered streams within a single queue, use MessageGroupId values (for example, session data for multiple users). In this scenario, multiple readers can process the queue, but the session data of each user is processed in a FIFO fashion.
            You must associate a non-empty MessageGroupId with a message. If you don't provide a MessageGroupId , the action fails.
            ReceiveMessage might return messages with multiple MessageGroupId values. For each MessageGroupId , the messages are sorted by time sent. The caller can't specify a MessageGroupId .
            The length of MessageGroupId is 128 characters. Valid values are alphanumeric characters and punctuation (!'#$%'()*+,-./:;=?@[\]^_`{|}~) .
            For best practices of using MessageGroupId , see Using the MessageGroupId Property in the Amazon Simple Queue Service Developer Guide .
            Warning
            MessageGroupId is required for FIFO queues. You can't use it for Standard queues.
            

    :rtype: dict
    :return: {
        'MD5OfMessageBody': 'string',
        'MD5OfMessageAttributes': 'string',
        'MessageId': 'string',
        'SequenceNumber': 'string'
    }
    
    
    """
    pass

def send_message_batch(QueueUrl=None, Entries=None):
    """
    Delivers up to ten messages to the specified queue. This is a batch version of ``  SendMessage .`` For a FIFO queue, multiple messages within a single batch are enqueued in the order they are sent.
    The result of sending each message is reported individually in the response. Because the batch request can result in a combination of successful and unsuccessful actions, you should check for batch errors even when the call returns an HTTP status code of 200 .
    The maximum allowed individual message size and the maximum total payload size (the sum of the individual lengths of all of the batched messages) are both 256 KB (262,144 bytes).
    If you don't specify the DelaySeconds parameter for an entry, Amazon SQS uses the default value for the queue.
    See also: AWS API Documentation
    
    
    :example: response = client.send_message_batch(
        QueueUrl='string',
        Entries=[
            {
                'Id': 'string',
                'MessageBody': 'string',
                'DelaySeconds': 123,
                'MessageAttributes': {
                    'string': {
                        'StringValue': 'string',
                        'BinaryValue': b'bytes',
                        'StringListValues': [
                            'string',
                        ],
                        'BinaryListValues': [
                            b'bytes',
                        ],
                        'DataType': 'string'
                    }
                },
                'MessageDeduplicationId': 'string',
                'MessageGroupId': 'string'
            },
        ]
    )
    
    
    :type QueueUrl: string
    :param QueueUrl: [REQUIRED]
            The URL of the Amazon SQS queue to which batched messages are sent.
            Queue URLs are case-sensitive.
            

    :type Entries: list
    :param Entries: [REQUIRED]
            A list of `` SendMessageBatchRequestEntry `` items.
            (dict) --Contains the details of a single Amazon SQS message along with an Id .
            Id (string) -- [REQUIRED]An identifier for a message in this batch used to communicate the result.
            Note
            The Id s of a batch request need to be unique within a request
            MessageBody (string) -- [REQUIRED]The body of the message.
            DelaySeconds (integer) --The length of time, in seconds, for which a specific message is delayed. Valid values: 0 to 900. Maximum: 15 minutes. Messages with a positive DelaySeconds value become available for processing after the delay period is finished. If you don't specify a value, the default value for the queue is applied.
            Note
            When you set FifoQueue , you can't set DelaySeconds per message. You can set this parameter only on a queue level.
            MessageAttributes (dict) --Each message attribute consists of a Name , Type , and Value . For more information, see Message Attribute Items and Validation in the Amazon SQS Developer Guide .
            (string) --
            (dict) --The user-specified message attribute value. For string data types, the Value attribute has the same restrictions on the content as the message body. For more information, see `` SendMessage .``
            Name , type , value and the message body must not be empty or null. All parts of the message attribute, including Name , Type , and Value , are part of the message size restriction (256 KB or 262,144 bytes).
            StringValue (string) --Strings are Unicode with UTF-8 binary encoding. For a list of code values, see ASCII Printable Characters .
            BinaryValue (bytes) --Binary type attributes can store any binary data, such as compressed data, encrypted data, or images.
            StringListValues (list) --Not implemented. Reserved for future use.
            (string) --
            BinaryListValues (list) --Not implemented. Reserved for future use.
            (bytes) --
            DataType (string) -- [REQUIRED]Amazon SQS supports the following logical data types: String , Number , and Binary . For the Number data type, you must use StringValue .
            You can also append custom labels. For more information, see Message Attribute Data Types and Validation in the Amazon SQS Developer Guide .
            
            MessageDeduplicationId (string) --This parameter applies only to FIFO (first-in-first-out) queues.
            The token used for deduplication of messages within a 5-minute minimum deduplication interval. If a message with a particular MessageDeduplicationId is sent successfully, subsequent messages with the same MessageDeduplicationId are accepted successfully but aren't delivered. For more information, see Exactly-Once Processing in the Amazon SQS Developer Guide .
            Every message must have a unique MessageDeduplicationId ,
            You may provide a MessageDeduplicationId explicitly.
            If you aren't able to provide a MessageDeduplicationId and you enable ContentBasedDeduplication for your queue, Amazon SQS uses a SHA-256 hash to generate the MessageDeduplicationId using the body of the message (but not the attributes of the message).
            If you don't provide a MessageDeduplicationId and the queue doesn't have ContentBasedDeduplication set, the action fails with an error.
            If the queue has ContentBasedDeduplication set, your MessageDeduplicationId overrides the generated one.
            When ContentBasedDeduplication is in effect, messages with identical content sent within the deduplication interval are treated as duplicates and only one copy of the message is delivered.
            If you send one message with ContentBasedDeduplication enabled and then another message with a MessageDeduplicationId that is the same as the one generated for the first MessageDeduplicationId , the two messages are treated as duplicates and only one copy of the message is delivered.
            Note
            The MessageDeduplicationId is available to the recipient of the message (this can be useful for troubleshooting delivery issues).
            If a message is sent successfully but the acknowledgement is lost and the message is resent with the same MessageDeduplicationId after the deduplication interval, Amazon SQS can't detect duplicate messages.
            The length of MessageDeduplicationId is 128 characters. MessageDeduplicationId can contain alphanumeric characters (a-z , A-Z , 0-9 ) and punctuation (!'#$%'()*+,-./:;=?@[\]^_`{|}~ ).
            For best practices of using MessageDeduplicationId , see Using the MessageDeduplicationId Property in the Amazon Simple Queue Service Developer Guide .
            MessageGroupId (string) --This parameter applies only to FIFO (first-in-first-out) queues.
            The tag that specifies that a message belongs to a specific message group. Messages that belong to the same message group are processed in a FIFO manner (however, messages in different message groups might be processed out of order). To interleave multiple ordered streams within a single queue, use MessageGroupId values (for example, session data for multiple users). In this scenario, multiple readers can process the queue, but the session data of each user is processed in a FIFO fashion.
            You must associate a non-empty MessageGroupId with a message. If you don't provide a MessageGroupId , the action fails.
            ReceiveMessage might return messages with multiple MessageGroupId values. For each MessageGroupId , the messages are sorted by time sent. The caller can't specify a MessageGroupId .
            The length of MessageGroupId is 128 characters. Valid values are alphanumeric characters and punctuation (!'#$%'()*+,-./:;=?@[\]^_`{|}~) .
            For best practices of using MessageGroupId , see Using the MessageGroupId Property in the Amazon Simple Queue Service Developer Guide .
            Warning
            MessageGroupId is required for FIFO queues. You can't use it for Standard queues.
            
            

    :rtype: dict
    :return: {
        'Successful': [
            {
                'Id': 'string',
                'MessageId': 'string',
                'MD5OfMessageBody': 'string',
                'MD5OfMessageAttributes': 'string',
                'SequenceNumber': 'string'
            },
        ],
        'Failed': [
            {
                'Id': 'string',
                'SenderFault': True|False,
                'Code': 'string',
                'Message': 'string'
            },
        ]
    }
    
    
    """
    pass

def set_queue_attributes(QueueUrl=None, Attributes=None):
    """
    Sets the value of one or more queue attributes. When you change a queue's attributes, the change can take up to 60 seconds for most of the attributes to propagate throughout the Amazon SQS system. Changes made to the MessageRetentionPeriod attribute can take up to 15 minutes.
    See also: AWS API Documentation
    
    
    :example: response = client.set_queue_attributes(
        QueueUrl='string',
        Attributes={
            'string': 'string'
        }
    )
    
    
    :type QueueUrl: string
    :param QueueUrl: [REQUIRED]
            The URL of the Amazon SQS queue whose attributes are set.
            Queue URLs are case-sensitive.
            

    :type Attributes: dict
    :param Attributes: [REQUIRED]
            A map of attributes to set.
            The following lists the names, descriptions, and values of the special request parameters that the SetQueueAttributes action uses:
            DelaySeconds - The length of time, in seconds, for which the delivery of all messages in the queue is delayed. Valid values: An integer from 0 to 900 (15 minutes). The default is 0 (zero).
            MaximumMessageSize - The limit of how many bytes a message can contain before Amazon SQS rejects it. Valid values: An integer from 1,024 bytes (1 KiB) up to 262,144 bytes (256 KiB). The default is 262,144 (256 KiB).
            MessageRetentionPeriod - The length of time, in seconds, for which Amazon SQS retains a message. Valid values: An integer representing seconds, from 60 (1 minute) to 1,209,600 (14 days). The default is 345,600 (4 days).
            Policy - The queue's policy. A valid AWS policy. For more information about policy structure, see Overview of AWS IAM Policies in the Amazon IAM User Guide .
            ReceiveMessageWaitTimeSeconds - The length of time, in seconds, for which a `` ReceiveMessage `` action waits for a message to arrive. Valid values: an integer from 0 to 20 (seconds). The default is 0.
            RedrivePolicy - The parameters for the dead letter queue functionality of the source queue. For more information about the redrive policy and dead letter queues, see Using Amazon SQS Dead Letter Queues in the Amazon SQS Developer Guide .
            Note
            The dead letter queue of a FIFO queue must also be a FIFO queue. Similarly, the dead letter queue of a standard queue must also be a standard queue.
            VisibilityTimeout - The visibility timeout for the queue. Valid values: an integer from 0 to 43,200 (12 hours). The default is 30. For more information about the visibility timeout, see Visibility Timeout in the Amazon SQS Developer Guide .
            The following attributes apply only to server-side-encryption :
            KmsMasterKeyId - The ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK. For more information, see Key Terms . While the alias of the AWS-managed CMK for Amazon SQS is always alias/aws/sqs , the alias of a custom CMK can, for example, be alias/aws/sqs . For more examples, see KeyId in the AWS Key Management Service API Reference .
            KmsDataKeyReusePeriodSeconds - The length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. An integer representing seconds, between 60 seconds (1 minute) and 86,400 seconds (24 hours). The default is 300 (5 minutes). A shorter time period provides better security but results in more calls to KMS which incur charges after Free Tier. For more information, see How Does the Data Key Reuse Period Work? .
            The following attribute applies only to FIFO (first-in-first-out) queues :
            ContentBasedDeduplication - Enables content-based deduplication. For more information, see Exactly-Once Processing in the Amazon SQS Developer Guide .
            Every message must have a unique MessageDeduplicationId ,
            You may provide a MessageDeduplicationId explicitly.
            If you aren't able to provide a MessageDeduplicationId and you enable ContentBasedDeduplication for your queue, Amazon SQS uses a SHA-256 hash to generate the MessageDeduplicationId using the body of the message (but not the attributes of the message).
            If you don't provide a MessageDeduplicationId and the queue doesn't have ContentBasedDeduplication set, the action fails with an error.
            If the queue has ContentBasedDeduplication set, your MessageDeduplicationId overrides the generated one.
            When ContentBasedDeduplication is in effect, messages with identical content sent within the deduplication interval are treated as duplicates and only one copy of the message is delivered.
            If you send one message with ContentBasedDeduplication enabled and then another message with a MessageDeduplicationId that is the same as the one generated for the first MessageDeduplicationId , the two messages are treated as duplicates and only one copy of the message is delivered.
            Any other valid special request parameters (such as the following) are ignored:
            ApproximateNumberOfMessages
            ApproximateNumberOfMessagesDelayed
            ApproximateNumberOfMessagesNotVisible
            CreatedTimestamp
            LastModifiedTimestamp
            QueueArn
            (string) --
            (string) --
            

    """
    pass

