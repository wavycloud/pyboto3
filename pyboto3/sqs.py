'''

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

'''

def add_permission(QueueUrl=None, Label=None, AWSAccountIds=None, Actions=None):
    """
    Adds a permission to a queue for a specific principal . This allows for sharing access to the queue.
    When you create a queue, you have full control access rights for the queue. Only you (as owner of the queue) can grant or deny permissions to the queue. For more information about these permissions, see Shared Queues in the Amazon SQS Developer Guide .
    
    
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
            The URL of the Amazon SQS queue to take action on.
            Queue URLs are case-sensitive.
            

    :type Label: string
    :param Label: [REQUIRED]
            The unique identification of the permission you're setting (e.g., AliceSendMessage ). Constraints: Maximum 80 characters; alphanumeric characters, hyphens (-), and underscores (_) are allowed.
            

    :type AWSAccountIds: list
    :param AWSAccountIds: [REQUIRED]
            The AWS account number of the principal who will be given permission. The principal must have an AWS account, but does not need to be signed up for Amazon SQS. For information about locating the AWS account identification, see Your AWS Identifiers in the Amazon SQS Developer Guide .
            (string) --
            

    :type Actions: list
    :param Actions: [REQUIRED]
            The action the client wants to allow for the specified principal. The following are valid values: * | SendMessage | ReceiveMessage | DeleteMessage | ChangeMessageVisibility | GetQueueAttributes | GetQueueUrl . For more information about these actions, see Understanding Permissions in the Amazon SQS Developer Guide .
            Specifying SendMessage , DeleteMessage , or ChangeMessageVisibility for the ActionName.n also grants permissions for the corresponding batch versions of those actions: SendMessageBatch , DeleteMessageBatch , and ChangeMessageVisibilityBatch .
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
    Changes the visibility timeout of a specified message in a queue to a new value. The maximum allowed timeout value you can set the value to is 12 hours. This means you can't extend the timeout of a message in an existing queue to more than a total visibility timeout of 12 hours. (For more information visibility timeout, see Visibility Timeout in the Amazon SQS Developer Guide .)
    For example, let's say you have a message and its default message visibility timeout is 5 minutes. After 3 minutes, you call ChangeMessageVisiblity with a timeout of 10 minutes. At that time, the timeout for the message would be extended by 10 minutes beyond the time of the ChangeMessageVisibility call. This results in a total visibility timeout of 13 minutes. You can continue to call ChangeMessageVisibility to extend the visibility timeout to a maximum of 12 hours. If you try to extend beyond 12 hours, the request will be rejected.
    
    
    :example: response = client.change_message_visibility(
        QueueUrl='string',
        ReceiptHandle='string',
        VisibilityTimeout=123
    )
    
    
    :type QueueUrl: string
    :param QueueUrl: [REQUIRED]
            The URL of the Amazon SQS queue to take action on.
            Queue URLs are case-sensitive.
            

    :type ReceiptHandle: string
    :param ReceiptHandle: [REQUIRED]
            The receipt handle associated with the message whose visibility timeout should be changed. This parameter is returned by the ReceiveMessage action.
            

    :type VisibilityTimeout: integer
    :param VisibilityTimeout: [REQUIRED]
            The new value (in seconds - from 0 to 43200 - maximum 12 hours) for the message's visibility timeout.
            

    """
    pass

def change_message_visibility_batch(QueueUrl=None, Entries=None):
    """
    Changes the visibility timeout of multiple messages. This is a batch version of  ChangeMessageVisibility . The result of the action on each message is reported individually in the response. You can send up to 10  ChangeMessageVisibility requests with each ChangeMessageVisibilityBatch action.
    
    
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
            The URL of the Amazon SQS queue to take action on.
            Queue URLs are case-sensitive.
            

    :type Entries: list
    :param Entries: [REQUIRED]
            A list of receipt handles of the messages for which the visibility timeout must be changed.
            (dict) --Encloses a receipt handle and an entry id for each message in ChangeMessageVisibilityBatch .
            Warning
            All of the following parameters are list parameters that must be prefixed with ChangeMessageVisibilityBatchRequestEntry.n , where n is an integer value starting with 1. For example, a parameter list for this action might look like this:
            Id (string) -- [REQUIRED]An identifier for this particular receipt handle. This is used to communicate the result. Note that the Id s of a batch request need to be unique within the request.
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
    Creates a new queue, or returns the URL of an existing one. When you request CreateQueue , you provide a name for the queue. To successfully create a new queue, you must provide a name that is unique within the scope of your own queues.
    You may pass one or more attributes in the request. If you do not provide a value for any attribute, the queue will have the default value for that attribute.
    If you provide the name of an existing queue, along with the exact names and values of all the queue's attributes, CreateQueue returns the queue URL for the existing queue. If the queue name, attribute names, or attribute values do not match an existing queue, CreateQueue returns an error.
    
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
            The name for the queue to be created.
            Queue names are case-sensitive.
            

    :type Attributes: dict
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
            

    :rtype: dict
    :return: {
        'QueueUrl': 'string'
    }
    
    
    """
    pass

def delete_message(QueueUrl=None, ReceiptHandle=None):
    """
    Deletes the specified message from the specified queue. You specify the message by using the message's receipt handle and not the message ID you received when you sent the message. Even if the message is locked by another reader due to the visibility timeout setting, it is still deleted from the queue. If you leave a message in the queue for longer than the queue's configured retention period, Amazon SQS automatically deletes it.
    
    
    :example: response = client.delete_message(
        QueueUrl='string',
        ReceiptHandle='string'
    )
    
    
    :type QueueUrl: string
    :param QueueUrl: [REQUIRED]
            The URL of the Amazon SQS queue to take action on.
            Queue URLs are case-sensitive.
            

    :type ReceiptHandle: string
    :param ReceiptHandle: [REQUIRED]
            The receipt handle associated with the message to delete.
            

    """
    pass

def delete_message_batch(QueueUrl=None, Entries=None):
    """
    Deletes up to ten messages from the specified queue. This is a batch version of  DeleteMessage . The result of the delete action on each message is reported individually in the response.
    
    
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
            The URL of the Amazon SQS queue to take action on.
            Queue URLs are case-sensitive.
            

    :type Entries: list
    :param Entries: [REQUIRED]
            A list of receipt handles for the messages to be deleted.
            (dict) --Encloses a receipt handle and an identifier for it.
            Id (string) -- [REQUIRED]An identifier for this particular receipt handle. This is used to communicate the result. Note that the Id s of a batch request need to be unique within the request.
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
    Deletes the queue specified by the queue URL , regardless of whether the queue is empty. If the specified queue does not exist, Amazon SQS returns a successful response.
    When you delete a queue, the deletion process takes up to 60 seconds. Requests you send involving that queue during the 60 seconds might succeed. For example, a  SendMessage request might succeed, but after the 60 seconds, the queue and that message you sent no longer exist. Also, when you delete a queue, you must wait at least 60 seconds before creating a queue with the same name.
    We reserve the right to delete queues that have had no activity for more than 30 days. For more information, see How Amazon SQS Queues Work in the Amazon SQS Developer Guide .
    
    
    :example: response = client.delete_queue(
        QueueUrl='string'
    )
    
    
    :type QueueUrl: string
    :param QueueUrl: [REQUIRED]
            The URL of the Amazon SQS queue to take action on.
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
    
    
    :example: response = client.get_queue_attributes(
        QueueUrl='string',
        AttributeNames=[
            'Policy'|'VisibilityTimeout'|'MaximumMessageSize'|'MessageRetentionPeriod'|'ApproximateNumberOfMessages'|'ApproximateNumberOfMessagesNotVisible'|'CreatedTimestamp'|'LastModifiedTimestamp'|'QueueArn'|'ApproximateNumberOfMessagesDelayed'|'DelaySeconds'|'ReceiveMessageWaitTimeSeconds'|'RedrivePolicy',
        ]
    )
    
    
    :type QueueUrl: string
    :param QueueUrl: [REQUIRED]
            The URL of the Amazon SQS queue to take action on.
            Queue URLs are case-sensitive.
            

    :type AttributeNames: list
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
    To access a queue that belongs to another AWS account, use the QueueOwnerAWSAccountId parameter to specify the account ID of the queue's owner. The queue's owner must grant you permission to access the queue. For more information about shared queue access, see  AddPermission or go to Shared Queues in the Amazon SQS Developer Guide .
    
    Examples
    The following example retrieves the queue ARN.
    Expected Output:
    
    :example: response = client.get_queue_url(
        QueueName='string',
        QueueOwnerAWSAccountId='string'
    )
    
    
    :type QueueName: string
    :param QueueName: [REQUIRED]
            The name of the queue whose URL must be fetched. Maximum 80 characters; alphanumeric characters, hyphens (-), and underscores (_) are allowed.
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
    For more information about using dead letter queues, see Using Amazon SQS Dead Letter Queues .
    
    
    :example: response = client.list_dead_letter_source_queues(
        QueueUrl='string'
    )
    
    
    :type QueueUrl: string
    :param QueueUrl: [REQUIRED]
            The queue URL of a dead letter queue.
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
    Returns a list of your queues. The maximum number of queues that can be returned is 1000. If you specify a value for the optional QueueNamePrefix parameter, only queues with a name beginning with the specified value are returned.
    
    
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
    Deletes the messages in a queue specified by the queue URL .
    When you purge a queue, the message deletion process takes up to 60 seconds. All messages sent to the queue before calling PurgeQueue will be deleted; messages sent to the queue while it is being purged may be deleted. While the queue is being purged, messages sent to the queue before PurgeQueue was called may be received, but will be deleted within the next minute.
    
    
    :example: response = client.purge_queue(
        QueueUrl='string'
    )
    
    
    :type QueueUrl: string
    :param QueueUrl: [REQUIRED]
            The queue URL of the queue to delete the messages from when using the PurgeQueue API.
            Queue URLs are case-sensitive.
            

    """
    pass

def receive_message(QueueUrl=None, AttributeNames=None, MessageAttributeNames=None, MaxNumberOfMessages=None, VisibilityTimeout=None, WaitTimeSeconds=None):
    """
    Retrieves one or more messages, with a maximum limit of 10 messages, from the specified queue. Long poll support is enabled by using the WaitTimeSeconds parameter. For more information, see Amazon SQS Long Poll in the Amazon SQS Developer Guide .
    Short poll is the default behavior where a weighted random set of machines is sampled on a ReceiveMessage call. This means only the messages on the sampled machines are returned. If the number of messages in the queue is small (less than 1000), it is likely you will get fewer messages than you requested per ReceiveMessage call. If the number of messages in the queue is extremely small, you might not receive any messages in a particular ReceiveMessage response; in which case you should repeat the request.
    For each message returned, the response includes the following:
    The receipt handle is the identifier you must provide when deleting the message. For more information, see Queue and Message Identifiers in the Amazon SQS Developer Guide .
    You can provide the VisibilityTimeout parameter in your request, which will be applied to the messages that Amazon SQS returns in the response. If you do not include the parameter, the overall visibility timeout for the queue is used for the returned messages. For more information, see Visibility Timeout in the Amazon SQS Developer Guide .
    
    
    :example: response = client.receive_message(
        QueueUrl='string',
        AttributeNames=[
            'Policy'|'VisibilityTimeout'|'MaximumMessageSize'|'MessageRetentionPeriod'|'ApproximateNumberOfMessages'|'ApproximateNumberOfMessagesNotVisible'|'CreatedTimestamp'|'LastModifiedTimestamp'|'QueueArn'|'ApproximateNumberOfMessagesDelayed'|'DelaySeconds'|'ReceiveMessageWaitTimeSeconds'|'RedrivePolicy',
        ],
        MessageAttributeNames=[
            'string',
        ],
        MaxNumberOfMessages=123,
        VisibilityTimeout=123,
        WaitTimeSeconds=123
    )
    
    
    :type QueueUrl: string
    :param QueueUrl: [REQUIRED]
            The URL of the Amazon SQS queue to take action on.
            Queue URLs are case-sensitive.
            

    :type AttributeNames: list
    :param AttributeNames: A list of attributes that need to be returned along with each message. These attributes include:
            All - returns all values.
            ApproximateFirstReceiveTimestamp - returns the time when the message was first received from the queue (epoch time in milliseconds).
            ApproximateReceiveCount - returns the number of times a message has been received from the queue but not deleted.
            SenderId - returns the AWS account number (or the IP address, if anonymous access is allowed) of the sender.
            SentTimestamp - returns the time when the message was sent to the queue (epoch time in milliseconds).
            Any other valid special request parameters that are specified (such as ApproximateNumberOfMessages , ApproximateNumberOfMessagesDelayed , ApproximateNumberOfMessagesNotVisible , CreatedTimestamp , DelaySeconds , LastModifiedTimestamp , MaximumMessageSize , MessageRetentionPeriod , Policy , QueueArn , ReceiveMessageWaitTimeSeconds , RedrivePolicy , and VisibilityTimeout ) will be ignored.
            (string) --
            

    :type MessageAttributeNames: list
    :param MessageAttributeNames: The name of the message attribute, where N is the index. The message attribute name can contain the following characters: A-Z, a-z, 0-9, underscore (_), hyphen (-), and period (.). The name must not start or end with a period, and it should not have successive periods. The name is case sensitive and must be unique among all attribute names for the message. The name can be up to 256 characters long. The name cannot start with 'AWS.' or 'Amazon.' (or any variations in casing), because these prefixes are reserved for use by Amazon Web Services.
            When using ReceiveMessage , you can send a list of attribute names to receive, or you can return all of the attributes by specifying 'All' or '.*' in your request. You can also use 'bar.*' to return all message attributes starting with the 'bar' prefix.
            (string) --
            

    :type MaxNumberOfMessages: integer
    :param MaxNumberOfMessages: The maximum number of messages to return. Amazon SQS never returns more messages than this value but may return fewer. Values can be from 1 to 10. Default is 1.
            All of the messages are not necessarily returned.
            

    :type VisibilityTimeout: integer
    :param VisibilityTimeout: The duration (in seconds) that the received messages are hidden from subsequent retrieve requests after being retrieved by a ReceiveMessage request.

    :type WaitTimeSeconds: integer
    :param WaitTimeSeconds: The duration (in seconds) for which the call will wait for a message to arrive in the queue before returning. If a message is available, the call will return sooner than WaitTimeSeconds.

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
    The URL of the Amazon SQS queue to take action on.
    Queue URLs are case-sensitive.
    
    AttributeNames (list) -- A list of attributes that need to be returned along with each message. These attributes include:
    
    All - returns all values.
    ApproximateFirstReceiveTimestamp - returns the time when the message was first received from the queue (epoch time in milliseconds).
    ApproximateReceiveCount - returns the number of times a message has been received from the queue but not deleted.
    SenderId - returns the AWS account number (or the IP address, if anonymous access is allowed) of the sender.
    SentTimestamp - returns the time when the message was sent to the queue (epoch time in milliseconds).
    
    Any other valid special request parameters that are specified (such as ApproximateNumberOfMessages , ApproximateNumberOfMessagesDelayed , ApproximateNumberOfMessagesNotVisible , CreatedTimestamp , DelaySeconds , LastModifiedTimestamp , MaximumMessageSize , MessageRetentionPeriod , Policy , QueueArn , ReceiveMessageWaitTimeSeconds , RedrivePolicy , and VisibilityTimeout ) will be ignored.
    
    (string) --
    
    
    MessageAttributeNames (list) -- The name of the message attribute, where N is the index. The message attribute name can contain the following characters: A-Z, a-z, 0-9, underscore (_), hyphen (-), and period (.). The name must not start or end with a period, and it should not have successive periods. The name is case sensitive and must be unique among all attribute names for the message. The name can be up to 256 characters long. The name cannot start with "AWS." or "Amazon." (or any variations in casing), because these prefixes are reserved for use by Amazon Web Services.
    When using ReceiveMessage , you can send a list of attribute names to receive, or you can return all of the attributes by specifying "All" or ".*" in your request. You can also use "bar.*" to return all message attributes starting with the "bar" prefix.
    
    (string) --
    
    
    MaxNumberOfMessages (integer) -- The maximum number of messages to return. Amazon SQS never returns more messages than this value but may return fewer. Values can be from 1 to 10. Default is 1.
    All of the messages are not necessarily returned.
    
    VisibilityTimeout (integer) -- The duration (in seconds) that the received messages are hidden from subsequent retrieve requests after being retrieved by a ReceiveMessage request.
    WaitTimeSeconds (integer) -- The duration (in seconds) for which the call will wait for a message to arrive in the queue before returning. If a message is available, the call will return sooner than WaitTimeSeconds.
    
    """
    pass

def remove_permission(QueueUrl=None, Label=None):
    """
    Revokes any permissions in the queue policy that matches the specified Label parameter. Only the owner of the queue can remove permissions.
    
    
    :example: response = client.remove_permission(
        QueueUrl='string',
        Label='string'
    )
    
    
    :type QueueUrl: string
    :param QueueUrl: [REQUIRED]
            The URL of the Amazon SQS queue to take action on.
            Queue URLs are case-sensitive.
            

    :type Label: string
    :param Label: [REQUIRED]
            The identification of the permission to remove. This is the label added with the AddPermission action.
            

    """
    pass

def send_message(QueueUrl=None, MessageBody=None, DelaySeconds=None, MessageAttributes=None):
    """
    Delivers a message to the specified queue. With Amazon SQS, you now have the ability to send large payload messages that are up to 256KB (262,144 bytes) in size. To send large payloads, you must use an AWS SDK that supports SigV4 signing. To verify whether SigV4 is supported for an AWS SDK, check the SDK release notes.
    
    
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
        }
    )
    
    
    :type QueueUrl: string
    :param QueueUrl: [REQUIRED]
            The URL of the Amazon SQS queue to take action on.
            Queue URLs are case-sensitive.
            

    :type MessageBody: string
    :param MessageBody: [REQUIRED]
            The message to send. String maximum 256 KB in size. For a list of allowed characters, see the preceding important note.
            

    :type DelaySeconds: integer
    :param DelaySeconds: The number of seconds (0 to 900 - 15 minutes) to delay a specific message. Messages with a positive DelaySeconds value become available for processing after the delay time is finished. If you don't specify a value, the default value for the queue applies.

    :type MessageAttributes: dict
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
            
            

    :rtype: dict
    :return: {
        'MD5OfMessageBody': 'string',
        'MD5OfMessageAttributes': 'string',
        'MessageId': 'string'
    }
    
    
    """
    pass

def send_message_batch(QueueUrl=None, Entries=None):
    """
    Delivers up to ten messages to the specified queue. This is a batch version of  SendMessage . The result of the send action on each message is reported individually in the response. The maximum allowed individual message size is 256 KB (262,144 bytes).
    The maximum total payload size (i.e., the sum of all a batch's individual message lengths) is also 256 KB (262,144 bytes).
    If the DelaySeconds parameter is not specified for an entry, the default for the queue is used.
    
    
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
                }
            },
        ]
    )
    
    
    :type QueueUrl: string
    :param QueueUrl: [REQUIRED]
            The URL of the Amazon SQS queue to take action on.
            Queue URLs are case-sensitive.
            

    :type Entries: list
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
            
            
            

    :rtype: dict
    :return: {
        'Successful': [
            {
                'Id': 'string',
                'MessageId': 'string',
                'MD5OfMessageBody': 'string',
                'MD5OfMessageAttributes': 'string'
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
    Sets the value of one or more queue attributes. When you change a queue's attributes, the change can take up to 60 seconds for most of the attributes to propagate throughout the SQS system. Changes made to the MessageRetentionPeriod attribute can take up to 15 minutes.
    
    
    :example: response = client.set_queue_attributes(
        QueueUrl='string',
        Attributes={
            'string': 'string'
        }
    )
    
    
    :type QueueUrl: string
    :param QueueUrl: [REQUIRED]
            The URL of the Amazon SQS queue to take action on.
            Queue URLs are case-sensitive.
            

    :type Attributes: dict
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
            

    """
    pass

