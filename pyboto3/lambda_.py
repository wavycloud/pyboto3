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

def add_layer_version_permission(LayerName=None, VersionNumber=None, StatementId=None, Action=None, Principal=None, OrganizationId=None, RevisionId=None):
    """
    Adds permissions to the resource-based policy of a version of an AWS Lambda layer . Use this action to grant layer usage permission to other accounts. You can grant permission to a single account, all AWS accounts, or all accounts in an organization.
    To revoke permission, call  RemoveLayerVersionPermission with the statement ID that you specified when you added it.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example grants permission for the account 223456789012 to use version 1 of a layer named my-layer.
    Expected Output:
    
    :example: response = client.add_layer_version_permission(
        LayerName='string',
        VersionNumber=123,
        StatementId='string',
        Action='string',
        Principal='string',
        OrganizationId='string',
        RevisionId='string'
    )
    
    
    :type LayerName: string
    :param LayerName: [REQUIRED]\nThe name or Amazon Resource Name (ARN) of the layer.\n

    :type VersionNumber: integer
    :param VersionNumber: [REQUIRED]\nThe version number.\n

    :type StatementId: string
    :param StatementId: [REQUIRED]\nAn identifier that distinguishes the policy from others on the same layer version.\n

    :type Action: string
    :param Action: [REQUIRED]\nThe API action that grants access to the layer. For example, lambda:GetLayerVersion .\n

    :type Principal: string
    :param Principal: [REQUIRED]\nAn account ID, or * to grant permission to all AWS accounts.\n

    :type OrganizationId: string
    :param OrganizationId: With the principal set to * , grant permission to all accounts in the specified organization.

    :type RevisionId: string
    :param RevisionId: Only update the policy if the revision ID matches the ID specified. Use this option to avoid modifying a policy that has changed since you last read it.

    :rtype: dict

ReturnsResponse Syntax
{
    'Statement': 'string',
    'RevisionId': 'string'
}


Response Structure

(dict) --

Statement (string) --
The permission statement.

RevisionId (string) --
A unique identifier for the current revision of the policy.







Exceptions

Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.ResourceNotFoundException
Lambda.Client.exceptions.ResourceConflictException
Lambda.Client.exceptions.TooManyRequestsException
Lambda.Client.exceptions.InvalidParameterValueException
Lambda.Client.exceptions.PolicyLengthExceededException
Lambda.Client.exceptions.PreconditionFailedException

Examples
The following example grants permission for the account 223456789012 to use version 1 of a layer named my-layer.
response = client.add_layer_version_permission(
    Action='lambda:GetLayerVersion',
    LayerName='my-layer',
    Principal='223456789012',
    StatementId='xaccount',
    VersionNumber=1,
)

print(response)


Expected Output:
{
    'RevisionId': '35d87451-f796-4a3f-a618-95a3671b0a0c',
    'Statement': '{"Sid":"xaccount","Effect":"Allow","Principal":{"AWS":"arn:aws:iam::223456789012:root"},"Action":"lambda:GetLayerVersion","Resource":"arn:aws:lambda:us-east-2:123456789012:layer:my-layer:1"}',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Statement': 'string',
        'RevisionId': 'string'
    }
    
    
    :returns: 
    Lambda.Client.exceptions.ServiceException
    Lambda.Client.exceptions.ResourceNotFoundException
    Lambda.Client.exceptions.ResourceConflictException
    Lambda.Client.exceptions.TooManyRequestsException
    Lambda.Client.exceptions.InvalidParameterValueException
    Lambda.Client.exceptions.PolicyLengthExceededException
    Lambda.Client.exceptions.PreconditionFailedException
    
    """
    pass

def add_permission(FunctionName=None, StatementId=None, Action=None, Principal=None, SourceArn=None, SourceAccount=None, EventSourceToken=None, Qualifier=None, RevisionId=None):
    """
    Grants an AWS service or another account permission to use a function. You can apply the policy at the function level, or specify a qualifier to restrict access to a single version or alias. If you use a qualifier, the invoker must use the full Amazon Resource Name (ARN) of that version or alias to invoke the function.
    To grant permission to another account, specify the account ID as the Principal . For AWS services, the principal is a domain-style identifier defined by the service, like s3.amazonaws.com or sns.amazonaws.com . For AWS services, you can also specify the ARN of the associated resource as the SourceArn . If you grant permission to a service principal without specifying the source, other accounts could potentially configure resources in their account to invoke your Lambda function.
    This action adds a statement to a resource-based permissions policy for the function. For more information about function policies, see Lambda Function Policies .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example adds permission for Amazon S3 to invoke a Lambda function named my-function for notifications from a bucket named my-bucket-1xpuxmplzrlbh in account 123456789012.
    Expected Output:
    The following example adds permission for account 223456789012 invoke a Lambda function named my-function.
    Expected Output:
    
    :example: response = client.add_permission(
        FunctionName='string',
        StatementId='string',
        Action='string',
        Principal='string',
        SourceArn='string',
        SourceAccount='string',
        EventSourceToken='string',
        Qualifier='string',
        RevisionId='string'
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the Lambda function, version, or alias.\n\nName formats\n\nFunction name - my-function (name-only), my-function:v1 (with alias).\nFunction ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function .\nPartial ARN - 123456789012:function:my-function .\n\nYou can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.\n

    :type StatementId: string
    :param StatementId: [REQUIRED]\nA statement identifier that differentiates the statement from others in the same policy.\n

    :type Action: string
    :param Action: [REQUIRED]\nThe action that the principal can use on the function. For example, lambda:InvokeFunction or lambda:GetFunction .\n

    :type Principal: string
    :param Principal: [REQUIRED]\nThe AWS service or account that invokes the function. If you specify a service, use SourceArn or SourceAccount to limit who can invoke the function through that service.\n

    :type SourceArn: string
    :param SourceArn: For AWS services, the ARN of the AWS resource that invokes the function. For example, an Amazon S3 bucket or Amazon SNS topic.

    :type SourceAccount: string
    :param SourceAccount: For Amazon S3, the ID of the account that owns the resource. Use this together with SourceArn to ensure that the resource is owned by the specified account. It is possible for an Amazon S3 bucket to be deleted by its owner and recreated by another account.

    :type EventSourceToken: string
    :param EventSourceToken: For Alexa Smart Home functions, a token that must be supplied by the invoker.

    :type Qualifier: string
    :param Qualifier: Specify a version or alias to add permissions to a published version of the function.

    :type RevisionId: string
    :param RevisionId: Only update the policy if the revision ID matches the ID that\'s specified. Use this option to avoid modifying a policy that has changed since you last read it.

    :rtype: dict

ReturnsResponse Syntax
{
    'Statement': 'string'
}


Response Structure

(dict) --

Statement (string) --
The permission statement that\'s added to the function policy.







Exceptions

Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.ResourceNotFoundException
Lambda.Client.exceptions.ResourceConflictException
Lambda.Client.exceptions.InvalidParameterValueException
Lambda.Client.exceptions.PolicyLengthExceededException
Lambda.Client.exceptions.TooManyRequestsException
Lambda.Client.exceptions.PreconditionFailedException

Examples
The following example adds permission for Amazon S3 to invoke a Lambda function named my-function for notifications from a bucket named my-bucket-1xpuxmplzrlbh in account 123456789012.
response = client.add_permission(
    Action='lambda:InvokeFunction',
    FunctionName='my-function',
    Principal='s3.amazonaws.com',
    SourceAccount='123456789012',
    SourceArn='arn:aws:s3:::my-bucket-1xpuxmplzrlbh/*',
    StatementId='s3',
)

print(response)


Expected Output:
{
    'Statement': '{"Sid":"s3","Effect":"Allow","Principal":{"Service":"s3.amazonaws.com"},"Action":"lambda:InvokeFunction","Resource":"arn:aws:lambda:us-east-2:123456789012:function:my-function","Condition":{"StringEquals":{"AWS:SourceAccount":"123456789012"},"ArnLike":{"AWS:SourceArn":"arn:aws:s3:::my-bucket-1xpuxmplzrlbh"}}}',
    'ResponseMetadata': {
        '...': '...',
    },
}


The following example adds permission for account 223456789012 invoke a Lambda function named my-function.
response = client.add_permission(
    Action='lambda:InvokeFunction',
    FunctionName='my-function',
    Principal='223456789012',
    StatementId='xaccount',
)

print(response)


Expected Output:
{
    'Statement': '{"Sid":"xaccount","Effect":"Allow","Principal":{"AWS":"arn:aws:iam::223456789012:root"},"Action":"lambda:InvokeFunction","Resource":"arn:aws:lambda:us-east-2:123456789012:function:my-function"}',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Statement': 'string'
    }
    
    
    :returns: 
    Lambda.Client.exceptions.ServiceException
    Lambda.Client.exceptions.ResourceNotFoundException
    Lambda.Client.exceptions.ResourceConflictException
    Lambda.Client.exceptions.InvalidParameterValueException
    Lambda.Client.exceptions.PolicyLengthExceededException
    Lambda.Client.exceptions.TooManyRequestsException
    Lambda.Client.exceptions.PreconditionFailedException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_alias(FunctionName=None, Name=None, FunctionVersion=None, Description=None, RoutingConfig=None):
    """
    Creates an alias for a Lambda function version. Use aliases to provide clients with a function identifier that you can update to invoke a different version.
    You can also map an alias to split invocation requests between two versions. Use the RoutingConfig parameter to specify a second version and the percentage of invocation requests that it receives.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example creates an alias named LIVE that points to version 1 of the my-function Lambda function.
    Expected Output:
    
    :example: response = client.create_alias(
        FunctionName='string',
        Name='string',
        FunctionVersion='string',
        Description='string',
        RoutingConfig={
            'AdditionalVersionWeights': {
                'string': 123.0
            }
        }
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the Lambda function.\n\nName formats\n\nFunction name - MyFunction .\nFunction ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .\nPartial ARN - 123456789012:function:MyFunction .\n\nThe length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.\n

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the alias.\n

    :type FunctionVersion: string
    :param FunctionVersion: [REQUIRED]\nThe function version that the alias invokes.\n

    :type Description: string
    :param Description: A description of the alias.

    :type RoutingConfig: dict
    :param RoutingConfig: The routing configuration of the alias.\n\nAdditionalVersionWeights (dict) --The name of the second alias, and the percentage of traffic that\'s routed to it.\n\n(string) --\n(float) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AliasArn': 'string',
    'Name': 'string',
    'FunctionVersion': 'string',
    'Description': 'string',
    'RoutingConfig': {
        'AdditionalVersionWeights': {
            'string': 123.0
        }
    },
    'RevisionId': 'string'
}


Response Structure

(dict) --
Provides configuration information about a Lambda function alias .

AliasArn (string) --
The Amazon Resource Name (ARN) of the alias.

Name (string) --
The name of the alias.

FunctionVersion (string) --
The function version that the alias invokes.

Description (string) --
A description of the alias.

RoutingConfig (dict) --
The routing configuration of the alias.

AdditionalVersionWeights (dict) --
The name of the second alias, and the percentage of traffic that\'s routed to it.

(string) --
(float) --






RevisionId (string) --
A unique identifier that changes when you update the alias.







Exceptions

Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.ResourceNotFoundException
Lambda.Client.exceptions.ResourceConflictException
Lambda.Client.exceptions.InvalidParameterValueException
Lambda.Client.exceptions.TooManyRequestsException

Examples
The following example creates an alias named LIVE that points to version 1 of the my-function Lambda function.
response = client.create_alias(
    Description='alias for live version of function',
    FunctionName='my-function',
    FunctionVersion='1',
    Name='LIVE',
)

print(response)


Expected Output:
{
    'AliasArn': 'arn:aws:lambda:us-east-2:123456789012:function:my-function:LIVE',
    'Description': 'alias for live version of function',
    'FunctionVersion': '1',
    'Name': 'LIVE',
    'RevisionId': '873282ed-xmpl-4dc8-a069-d0c647e470c6',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'AliasArn': 'string',
        'Name': 'string',
        'FunctionVersion': 'string',
        'Description': 'string',
        'RoutingConfig': {
            'AdditionalVersionWeights': {
                'string': 123.0
            }
        },
        'RevisionId': 'string'
    }
    
    
    :returns: 
    (string) --
    (float) --
    
    
    
    """
    pass

def create_event_source_mapping(EventSourceArn=None, FunctionName=None, Enabled=None, BatchSize=None, MaximumBatchingWindowInSeconds=None, ParallelizationFactor=None, StartingPosition=None, StartingPositionTimestamp=None, DestinationConfig=None, MaximumRecordAgeInSeconds=None, BisectBatchOnFunctionError=None, MaximumRetryAttempts=None):
    """
    Creates a mapping between an event source and an AWS Lambda function. Lambda reads items from the event source and triggers the function.
    For details about each event source type, see the following topics.
    The following error handling options are only available for stream sources (DynamoDB and Kinesis):
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example creates a mapping between an SQS queue and the my-function Lambda function.
    Expected Output:
    
    :example: response = client.create_event_source_mapping(
        EventSourceArn='string',
        FunctionName='string',
        Enabled=True|False,
        BatchSize=123,
        MaximumBatchingWindowInSeconds=123,
        ParallelizationFactor=123,
        StartingPosition='TRIM_HORIZON'|'LATEST'|'AT_TIMESTAMP',
        StartingPositionTimestamp=datetime(2015, 1, 1),
        DestinationConfig={
            'OnSuccess': {
                'Destination': 'string'
            },
            'OnFailure': {
                'Destination': 'string'
            }
        },
        MaximumRecordAgeInSeconds=123,
        BisectBatchOnFunctionError=True|False,
        MaximumRetryAttempts=123
    )
    
    
    :type EventSourceArn: string
    :param EventSourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the event source.\n\nAmazon Kinesis - The ARN of the data stream or a stream consumer.\nAmazon DynamoDB Streams - The ARN of the stream.\nAmazon Simple Queue Service - The ARN of the queue.\n\n

    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the Lambda function.\n\nName formats\n\nFunction name - MyFunction .\nFunction ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .\nVersion or Alias ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD .\nPartial ARN - 123456789012:function:MyFunction .\n\nThe length constraint applies only to the full ARN. If you specify only the function name, it\'s limited to 64 characters in length.\n

    :type Enabled: boolean
    :param Enabled: Disables the event source mapping to pause polling and invocation.

    :type BatchSize: integer
    :param BatchSize: The maximum number of items to retrieve in a single batch.\n\nAmazon Kinesis - Default 100. Max 10,000.\nAmazon DynamoDB Streams - Default 100. Max 1,000.\nAmazon Simple Queue Service - Default 10. Max 10.\n\n

    :type MaximumBatchingWindowInSeconds: integer
    :param MaximumBatchingWindowInSeconds: (Streams) The maximum amount of time to gather records before invoking the function, in seconds.

    :type ParallelizationFactor: integer
    :param ParallelizationFactor: (Streams) The number of batches to process from each shard concurrently.

    :type StartingPosition: string
    :param StartingPosition: The position in a stream from which to start reading. Required for Amazon Kinesis and Amazon DynamoDB Streams sources. AT_TIMESTAMP is only supported for Amazon Kinesis streams.

    :type StartingPositionTimestamp: datetime
    :param StartingPositionTimestamp: With StartingPosition set to AT_TIMESTAMP , the time from which to start reading.

    :type DestinationConfig: dict
    :param DestinationConfig: (Streams) An Amazon SQS queue or Amazon SNS topic destination for discarded records.\n\nOnSuccess (dict) --The destination configuration for successful invocations.\n\nDestination (string) --The Amazon Resource Name (ARN) of the destination resource.\n\n\n\nOnFailure (dict) --The destination configuration for failed invocations.\n\nDestination (string) --The Amazon Resource Name (ARN) of the destination resource.\n\n\n\n\n

    :type MaximumRecordAgeInSeconds: integer
    :param MaximumRecordAgeInSeconds: (Streams) The maximum age of a record that Lambda sends to a function for processing.

    :type BisectBatchOnFunctionError: boolean
    :param BisectBatchOnFunctionError: (Streams) If the function returns an error, split the batch in two and retry.

    :type MaximumRetryAttempts: integer
    :param MaximumRetryAttempts: (Streams) The maximum number of times to retry when the function returns an error.

    :rtype: dict

ReturnsResponse Syntax
{
    'UUID': 'string',
    'BatchSize': 123,
    'MaximumBatchingWindowInSeconds': 123,
    'ParallelizationFactor': 123,
    'EventSourceArn': 'string',
    'FunctionArn': 'string',
    'LastModified': datetime(2015, 1, 1),
    'LastProcessingResult': 'string',
    'State': 'string',
    'StateTransitionReason': 'string',
    'DestinationConfig': {
        'OnSuccess': {
            'Destination': 'string'
        },
        'OnFailure': {
            'Destination': 'string'
        }
    },
    'MaximumRecordAgeInSeconds': 123,
    'BisectBatchOnFunctionError': True|False,
    'MaximumRetryAttempts': 123
}


Response Structure

(dict) --
A mapping between an AWS resource and an AWS Lambda function. See  CreateEventSourceMapping for details.

UUID (string) --
The identifier of the event source mapping.

BatchSize (integer) --
The maximum number of items to retrieve in a single batch.

MaximumBatchingWindowInSeconds (integer) --
(Streams) The maximum amount of time to gather records before invoking the function, in seconds.

ParallelizationFactor (integer) --
(Streams) The number of batches to process from each shard concurrently.

EventSourceArn (string) --
The Amazon Resource Name (ARN) of the event source.

FunctionArn (string) --
The ARN of the Lambda function.

LastModified (datetime) --
The date that the event source mapping was last updated, or its state changed.

LastProcessingResult (string) --
The result of the last AWS Lambda invocation of your Lambda function.

State (string) --
The state of the event source mapping. It can be one of the following: Creating , Enabling , Enabled , Disabling , Disabled , Updating , or Deleting .

StateTransitionReason (string) --
Indicates whether the last change to the event source mapping was made by a user, or by the Lambda service.

DestinationConfig (dict) --
(Streams) An Amazon SQS queue or Amazon SNS topic destination for discarded records.

OnSuccess (dict) --
The destination configuration for successful invocations.

Destination (string) --
The Amazon Resource Name (ARN) of the destination resource.



OnFailure (dict) --
The destination configuration for failed invocations.

Destination (string) --
The Amazon Resource Name (ARN) of the destination resource.





MaximumRecordAgeInSeconds (integer) --
(Streams) The maximum age of a record that Lambda sends to a function for processing.

BisectBatchOnFunctionError (boolean) --
(Streams) If the function returns an error, split the batch in two and retry.

MaximumRetryAttempts (integer) --
(Streams) The maximum number of times to retry when the function returns an error.







Exceptions

Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.InvalidParameterValueException
Lambda.Client.exceptions.ResourceConflictException
Lambda.Client.exceptions.TooManyRequestsException
Lambda.Client.exceptions.ResourceNotFoundException

Examples
The following example creates a mapping between an SQS queue and the my-function Lambda function.
response = client.create_event_source_mapping(
    BatchSize=5,
    EventSourceArn='arn:aws:sqs:us-west-2:123456789012:my-queue',
    FunctionName='my-function',
)

print(response)


Expected Output:
{
    'BatchSize': 5,
    'EventSourceArn': 'arn:aws:sqs:us-west-2:123456789012:my-queue',
    'FunctionArn': 'arn:aws:lambda:us-west-2:123456789012:function:my-function',
    'LastModified': 1569284520.333,
    'State': 'Creating',
    'StateTransitionReason': 'USER_INITIATED',
    'UUID': 'a1b2c3d4-5678-90ab-cdef-11111EXAMPLE',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'UUID': 'string',
        'BatchSize': 123,
        'MaximumBatchingWindowInSeconds': 123,
        'ParallelizationFactor': 123,
        'EventSourceArn': 'string',
        'FunctionArn': 'string',
        'LastModified': datetime(2015, 1, 1),
        'LastProcessingResult': 'string',
        'State': 'string',
        'StateTransitionReason': 'string',
        'DestinationConfig': {
            'OnSuccess': {
                'Destination': 'string'
            },
            'OnFailure': {
                'Destination': 'string'
            }
        },
        'MaximumRecordAgeInSeconds': 123,
        'BisectBatchOnFunctionError': True|False,
        'MaximumRetryAttempts': 123
    }
    
    
    :returns: 
    BisectBatchOnFunctionError - If the function returns an error, split the batch in two and retry.
    DestinationConfig - Send discarded records to an Amazon SQS queue or Amazon SNS topic.
    MaximumRecordAgeInSeconds - Discard records older than the specified age.
    MaximumRetryAttempts - Discard records after the specified number of retries.
    ParallelizationFactor - Process multiple batches from each shard concurrently.
    
    """
    pass

def create_function(FunctionName=None, Runtime=None, Role=None, Handler=None, Code=None, Description=None, Timeout=None, MemorySize=None, Publish=None, VpcConfig=None, DeadLetterConfig=None, Environment=None, KMSKeyArn=None, TracingConfig=None, Tags=None, Layers=None):
    """
    Creates a Lambda function. To create a function, you need a deployment package and an execution role . The deployment package contains your function code. The execution role grants the function permission to use AWS services, such as Amazon CloudWatch Logs for log streaming and AWS X-Ray for request tracing.
    When you create a function, Lambda provisions an instance of the function and its supporting resources. If your function connects to a VPC, this process can take a minute or so. During this time, you can\'t invoke or modify the function. The State , StateReason , and StateReasonCode fields in the response from  GetFunctionConfiguration indicate when the function is ready to invoke. For more information, see Function States .
    A function has an unpublished version, and can have published versions and aliases. The unpublished version changes when you update your function\'s code and configuration. A published version is a snapshot of your function code and configuration that can\'t be changed. An alias is a named resource that maps to a version, and can be changed to map to a different version. Use the Publish parameter to create version 1 of your function from its initial configuration.
    The other parameters let you configure version-specific and function-level settings. You can modify version-specific settings later with  UpdateFunctionConfiguration . Function-level settings apply to both the unpublished and published versions of the function, and include tags ( TagResource ) and per-function concurrency limits ( PutFunctionConcurrency ).
    If another account or an AWS service invokes your function, use  AddPermission to grant permission by creating a resource-based IAM policy. You can grant permissions at the function level, on a version, or on an alias.
    To invoke your function directly, use  Invoke . To invoke your function in response to events in other AWS services, create an event source mapping ( CreateEventSourceMapping ), or configure a function trigger in the other service. For more information, see Invoking Functions .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example creates a function with a deployment package in Amazon S3 and enables X-Ray tracing and environment variable encryption.
    Expected Output:
    
    :example: response = client.create_function(
        FunctionName='string',
        Runtime='nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'dotnetcore3.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'ruby2.7'|'provided',
        Role='string',
        Handler='string',
        Code={
            'ZipFile': b'bytes',
            'S3Bucket': 'string',
            'S3Key': 'string',
            'S3ObjectVersion': 'string'
        },
        Description='string',
        Timeout=123,
        MemorySize=123,
        Publish=True|False,
        VpcConfig={
            'SubnetIds': [
                'string',
            ],
            'SecurityGroupIds': [
                'string',
            ]
        },
        DeadLetterConfig={
            'TargetArn': 'string'
        },
        Environment={
            'Variables': {
                'string': 'string'
            }
        },
        KMSKeyArn='string',
        TracingConfig={
            'Mode': 'Active'|'PassThrough'
        },
        Tags={
            'string': 'string'
        },
        Layers=[
            'string',
        ]
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the Lambda function.\n\nName formats\n\nFunction name - my-function .\nFunction ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function .\nPartial ARN - 123456789012:function:my-function .\n\nThe length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.\n

    :type Runtime: string
    :param Runtime: [REQUIRED]\nThe identifier of the function\'s runtime .\n

    :type Role: string
    :param Role: [REQUIRED]\nThe Amazon Resource Name (ARN) of the function\'s execution role.\n

    :type Handler: string
    :param Handler: [REQUIRED]\nThe name of the method within your code that Lambda calls to execute your function. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime. For more information, see Programming Model .\n

    :type Code: dict
    :param Code: [REQUIRED]\nThe code for the function.\n\nZipFile (bytes) --The base64-encoded contents of the deployment package. AWS SDK and AWS CLI clients handle the encoding for you.\n\nS3Bucket (string) --An Amazon S3 bucket in the same AWS Region as your function. The bucket can be in a different AWS account.\n\nS3Key (string) --The Amazon S3 key of the deployment package.\n\nS3ObjectVersion (string) --For versioned objects, the version of the deployment package object to use.\n\n\n

    :type Description: string
    :param Description: A description of the function.

    :type Timeout: integer
    :param Timeout: The amount of time that Lambda allows a function to run before stopping it. The default is 3 seconds. The maximum allowed value is 900 seconds.

    :type MemorySize: integer
    :param MemorySize: The amount of memory that your function has access to. Increasing the function\'s memory also increases its CPU allocation. The default value is 128 MB. The value must be a multiple of 64 MB.

    :type Publish: boolean
    :param Publish: Set to true to publish the first version of the function during creation.

    :type VpcConfig: dict
    :param VpcConfig: For network connectivity to AWS resources in a VPC, specify a list of security groups and subnets in the VPC. When you connect a function to a VPC, it can only access resources and the internet through that VPC. For more information, see VPC Settings .\n\nSubnetIds (list) --A list of VPC subnet IDs.\n\n(string) --\n\n\nSecurityGroupIds (list) --A list of VPC security groups IDs.\n\n(string) --\n\n\n\n

    :type DeadLetterConfig: dict
    :param DeadLetterConfig: A dead letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing. For more information, see Dead Letter Queues .\n\nTargetArn (string) --The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.\n\n\n

    :type Environment: dict
    :param Environment: Environment variables that are accessible from function code during execution.\n\nVariables (dict) --Environment variable key-value pairs.\n\n(string) --\n(string) --\n\n\n\n\n\n

    :type KMSKeyArn: string
    :param KMSKeyArn: The ARN of the AWS Key Management Service (AWS KMS) key that\'s used to encrypt your function\'s environment variables. If it\'s not provided, AWS Lambda uses a default service key.

    :type TracingConfig: dict
    :param TracingConfig: Set Mode to Active to sample and trace a subset of incoming requests with AWS X-Ray.\n\nMode (string) --The tracing mode.\n\n\n

    :type Tags: dict
    :param Tags: A list of tags to apply to the function.\n\n(string) --\n(string) --\n\n\n\n

    :type Layers: list
    :param Layers: A list of function layers to add to the function\'s execution environment. Specify each layer by its ARN, including the version.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'FunctionName': 'string',
    'FunctionArn': 'string',
    'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'dotnetcore3.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'ruby2.7'|'provided',
    'Role': 'string',
    'Handler': 'string',
    'CodeSize': 123,
    'Description': 'string',
    'Timeout': 123,
    'MemorySize': 123,
    'LastModified': 'string',
    'CodeSha256': 'string',
    'Version': 'string',
    'VpcConfig': {
        'SubnetIds': [
            'string',
        ],
        'SecurityGroupIds': [
            'string',
        ],
        'VpcId': 'string'
    },
    'DeadLetterConfig': {
        'TargetArn': 'string'
    },
    'Environment': {
        'Variables': {
            'string': 'string'
        },
        'Error': {
            'ErrorCode': 'string',
            'Message': 'string'
        }
    },
    'KMSKeyArn': 'string',
    'TracingConfig': {
        'Mode': 'Active'|'PassThrough'
    },
    'MasterArn': 'string',
    'RevisionId': 'string',
    'Layers': [
        {
            'Arn': 'string',
            'CodeSize': 123
        },
    ],
    'State': 'Pending'|'Active'|'Inactive'|'Failed',
    'StateReason': 'string',
    'StateReasonCode': 'Idle'|'Creating'|'Restoring'|'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'|'SubnetOutOfIPAddresses'|'InvalidSubnet'|'InvalidSecurityGroup',
    'LastUpdateStatus': 'Successful'|'Failed'|'InProgress',
    'LastUpdateStatusReason': 'string',
    'LastUpdateStatusReasonCode': 'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'|'SubnetOutOfIPAddresses'|'InvalidSubnet'|'InvalidSecurityGroup'
}


Response Structure

(dict) --
Details about a function\'s configuration.

FunctionName (string) --
The name of the function.

FunctionArn (string) --
The function\'s Amazon Resource Name (ARN).

Runtime (string) --
The runtime environment for the Lambda function.

Role (string) --
The function\'s execution role.

Handler (string) --
The function that Lambda calls to begin executing your function.

CodeSize (integer) --
The size of the function\'s deployment package, in bytes.

Description (string) --
The function\'s description.

Timeout (integer) --
The amount of time in seconds that Lambda allows a function to run before stopping it.

MemorySize (integer) --
The memory that\'s allocated to the function.

LastModified (string) --
The date and time that the function was last updated, in ISO-8601 format (YYYY-MM-DDThh:mm:ss.sTZD).

CodeSha256 (string) --
The SHA256 hash of the function\'s deployment package.

Version (string) --
The version of the Lambda function.

VpcConfig (dict) --
The function\'s networking configuration.

SubnetIds (list) --
A list of VPC subnet IDs.

(string) --


SecurityGroupIds (list) --
A list of VPC security groups IDs.

(string) --


VpcId (string) --
The ID of the VPC.



DeadLetterConfig (dict) --
The function\'s dead letter queue.

TargetArn (string) --
The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.



Environment (dict) --
The function\'s environment variables.

Variables (dict) --
Environment variable key-value pairs.

(string) --
(string) --




Error (dict) --
Error messages for environment variables that couldn\'t be applied.

ErrorCode (string) --
The error code.

Message (string) --
The error message.





KMSKeyArn (string) --
The KMS key that\'s used to encrypt the function\'s environment variables. This key is only returned if you\'ve configured a customer managed CMK.

TracingConfig (dict) --
The function\'s AWS X-Ray tracing configuration.

Mode (string) --
The tracing mode.



MasterArn (string) --
For Lambda@Edge functions, the ARN of the master function.

RevisionId (string) --
The latest updated revision of the function or alias.

Layers (list) --
The function\'s layers .

(dict) --
An AWS Lambda layer .

Arn (string) --
The Amazon Resource Name (ARN) of the function layer.

CodeSize (integer) --
The size of the layer archive in bytes.





State (string) --
The current state of the function. When the state is Inactive , you can reactivate the function by invoking it.

StateReason (string) --
The reason for the function\'s current state.

StateReasonCode (string) --
The reason code for the function\'s current state. When the code is Creating , you can\'t invoke or modify the function.

LastUpdateStatus (string) --
The status of the last update that was performed on the function. This is first set to Successful after function creation completes.

LastUpdateStatusReason (string) --
The reason for the last update that was performed on the function.

LastUpdateStatusReasonCode (string) --
The reason code for the last update that was performed on the function.







Exceptions

Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.InvalidParameterValueException
Lambda.Client.exceptions.ResourceNotFoundException
Lambda.Client.exceptions.ResourceConflictException
Lambda.Client.exceptions.TooManyRequestsException
Lambda.Client.exceptions.CodeStorageExceededException

Examples
The following example creates a function with a deployment package in Amazon S3 and enables X-Ray tracing and environment variable encryption.
response = client.create_function(
    Code={
        'S3Bucket': 'my-bucket-1xpuxmplzrlbh',
        'S3Key': 'function.zip',
    },
    Description='Process image objects from Amazon S3.',
    Environment={
        'Variables': {
            'BUCKET': 'my-bucket-1xpuxmplzrlbh',
            'PREFIX': 'inbound',
        },
    },
    FunctionName='my-function',
    Handler='index.handler',
    KMSKeyArn='arn:aws:kms:us-west-2:123456789012:key/b0844d6c-xmpl-4463-97a4-d49f50839966',
    MemorySize=256,
    Publish=True,
    Role='arn:aws:iam::123456789012:role/lambda-role',
    Runtime='nodejs12.x',
    Tags={
        'DEPARTMENT': 'Assets',
    },
    Timeout=15,
    TracingConfig={
        'Mode': 'Active',
    },
)

print(response)


Expected Output:
{
    'CodeSha256': 'YFgDgEKG3ugvF1+pX64gV6tu9qNuIYNUdgJm8nCxsm4=',
    'CodeSize': 5797206,
    'Description': 'Process image objects from Amazon S3.',
    'Environment': {
        'Variables': {
            'BUCKET': 'my-bucket-1xpuxmplzrlbh',
            'PREFIX': 'inbound',
        },
    },
    'FunctionArn': 'arn:aws:lambda:us-west-2:123456789012:function:my-function',
    'FunctionName': 'my-function',
    'Handler': 'index.handler',
    'KMSKeyArn': 'arn:aws:kms:us-west-2:123456789012:key/b0844d6c-xmpl-4463-97a4-d49f50839966',
    'LastModified': '2020-04-10T19:06:32.563+0000',
    'LastUpdateStatus': 'Successful',
    'MemorySize': 256,
    'RevisionId': 'b75dcd81-xmpl-48a8-a75a-93ba8b5b9727',
    'Role': 'arn:aws:iam::123456789012:role/lambda-role',
    'Runtime': 'nodejs12.x',
    'State': 'Active',
    'Timeout': 15,
    'TracingConfig': {
        'Mode': 'Active',
    },
    'Version': '1',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'FunctionName': 'string',
        'FunctionArn': 'string',
        'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'dotnetcore3.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'ruby2.7'|'provided',
        'Role': 'string',
        'Handler': 'string',
        'CodeSize': 123,
        'Description': 'string',
        'Timeout': 123,
        'MemorySize': 123,
        'LastModified': 'string',
        'CodeSha256': 'string',
        'Version': 'string',
        'VpcConfig': {
            'SubnetIds': [
                'string',
            ],
            'SecurityGroupIds': [
                'string',
            ],
            'VpcId': 'string'
        },
        'DeadLetterConfig': {
            'TargetArn': 'string'
        },
        'Environment': {
            'Variables': {
                'string': 'string'
            },
            'Error': {
                'ErrorCode': 'string',
                'Message': 'string'
            }
        },
        'KMSKeyArn': 'string',
        'TracingConfig': {
            'Mode': 'Active'|'PassThrough'
        },
        'MasterArn': 'string',
        'RevisionId': 'string',
        'Layers': [
            {
                'Arn': 'string',
                'CodeSize': 123
            },
        ],
        'State': 'Pending'|'Active'|'Inactive'|'Failed',
        'StateReason': 'string',
        'StateReasonCode': 'Idle'|'Creating'|'Restoring'|'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'|'SubnetOutOfIPAddresses'|'InvalidSubnet'|'InvalidSecurityGroup',
        'LastUpdateStatus': 'Successful'|'Failed'|'InProgress',
        'LastUpdateStatusReason': 'string',
        'LastUpdateStatusReasonCode': 'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'|'SubnetOutOfIPAddresses'|'InvalidSubnet'|'InvalidSecurityGroup'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_alias(FunctionName=None, Name=None):
    """
    Deletes a Lambda function alias .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example deletes an alias named BLUE from a function named my-function
    Expected Output:
    
    :example: response = client.delete_alias(
        FunctionName='string',
        Name='string'
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the Lambda function.\n\nName formats\n\nFunction name - MyFunction .\nFunction ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .\nPartial ARN - 123456789012:function:MyFunction .\n\nThe length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.\n

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the alias.\n

    :return: response = client.delete_alias(
        FunctionName='my-function',
        Name='BLUE',
    )
    
    print(response)
    
    
    :returns: 
    Lambda.Client.exceptions.ServiceException
    Lambda.Client.exceptions.InvalidParameterValueException
    Lambda.Client.exceptions.ResourceConflictException
    Lambda.Client.exceptions.TooManyRequestsException
    
    """
    pass

def delete_event_source_mapping(UUID=None):
    """
    Deletes an event source mapping . You can get the identifier of a mapping from the output of  ListEventSourceMappings .
    When you delete an event source mapping, it enters a Deleting state and might not be completely deleted for several seconds.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example deletes an event source mapping. To get a mapping\'s UUID, use ListEventSourceMappings.
    Expected Output:
    
    :example: response = client.delete_event_source_mapping(
        UUID='string'
    )
    
    
    :type UUID: string
    :param UUID: [REQUIRED]\nThe identifier of the event source mapping.\n

    :rtype: dict
ReturnsResponse Syntax{
    'UUID': 'string',
    'BatchSize': 123,
    'MaximumBatchingWindowInSeconds': 123,
    'ParallelizationFactor': 123,
    'EventSourceArn': 'string',
    'FunctionArn': 'string',
    'LastModified': datetime(2015, 1, 1),
    'LastProcessingResult': 'string',
    'State': 'string',
    'StateTransitionReason': 'string',
    'DestinationConfig': {
        'OnSuccess': {
            'Destination': 'string'
        },
        'OnFailure': {
            'Destination': 'string'
        }
    },
    'MaximumRecordAgeInSeconds': 123,
    'BisectBatchOnFunctionError': True|False,
    'MaximumRetryAttempts': 123
}


Response Structure

(dict) --A mapping between an AWS resource and an AWS Lambda function. See  CreateEventSourceMapping for details.

UUID (string) --The identifier of the event source mapping.

BatchSize (integer) --The maximum number of items to retrieve in a single batch.

MaximumBatchingWindowInSeconds (integer) --(Streams) The maximum amount of time to gather records before invoking the function, in seconds.

ParallelizationFactor (integer) --(Streams) The number of batches to process from each shard concurrently.

EventSourceArn (string) --The Amazon Resource Name (ARN) of the event source.

FunctionArn (string) --The ARN of the Lambda function.

LastModified (datetime) --The date that the event source mapping was last updated, or its state changed.

LastProcessingResult (string) --The result of the last AWS Lambda invocation of your Lambda function.

State (string) --The state of the event source mapping. It can be one of the following: Creating , Enabling , Enabled , Disabling , Disabled , Updating , or Deleting .

StateTransitionReason (string) --Indicates whether the last change to the event source mapping was made by a user, or by the Lambda service.

DestinationConfig (dict) --(Streams) An Amazon SQS queue or Amazon SNS topic destination for discarded records.

OnSuccess (dict) --The destination configuration for successful invocations.

Destination (string) --The Amazon Resource Name (ARN) of the destination resource.



OnFailure (dict) --The destination configuration for failed invocations.

Destination (string) --The Amazon Resource Name (ARN) of the destination resource.





MaximumRecordAgeInSeconds (integer) --(Streams) The maximum age of a record that Lambda sends to a function for processing.

BisectBatchOnFunctionError (boolean) --(Streams) If the function returns an error, split the batch in two and retry.

MaximumRetryAttempts (integer) --(Streams) The maximum number of times to retry when the function returns an error.






Exceptions

Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.ResourceNotFoundException
Lambda.Client.exceptions.InvalidParameterValueException
Lambda.Client.exceptions.TooManyRequestsException
Lambda.Client.exceptions.ResourceInUseException

Examples
The following example deletes an event source mapping. To get a mapping\'s UUID, use ListEventSourceMappings.
response = client.delete_event_source_mapping(
    UUID='14e0db71-xmpl-4eb5-b481-8945cf9d10c2',
)

print(response)


Expected Output:
{
    'BatchSize': 5,
    'EventSourceArn': 'arn:aws:sqs:us-west-2:123456789012:my-queue',
    'FunctionArn': 'arn:aws:lambda:us-east-2:123456789012:function:my-function',
    'LastModified': datetime(2016, 11, 21, 19, 49, 20, 0, 326, 0),
    'State': 'Enabled',
    'StateTransitionReason': 'USER_INITIATED',
    'UUID': '14e0db71-xmpl-4eb5-b481-8945cf9d10c2',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'UUID': 'string',
        'BatchSize': 123,
        'MaximumBatchingWindowInSeconds': 123,
        'ParallelizationFactor': 123,
        'EventSourceArn': 'string',
        'FunctionArn': 'string',
        'LastModified': datetime(2015, 1, 1),
        'LastProcessingResult': 'string',
        'State': 'string',
        'StateTransitionReason': 'string',
        'DestinationConfig': {
            'OnSuccess': {
                'Destination': 'string'
            },
            'OnFailure': {
                'Destination': 'string'
            }
        },
        'MaximumRecordAgeInSeconds': 123,
        'BisectBatchOnFunctionError': True|False,
        'MaximumRetryAttempts': 123
    }
    
    
    """
    pass

def delete_function(FunctionName=None, Qualifier=None):
    """
    Deletes a Lambda function. To delete a specific function version, use the Qualifier parameter. Otherwise, all versions and aliases are deleted.
    To delete Lambda event source mappings that invoke a function, use  DeleteEventSourceMapping . For AWS services and resources that invoke your function directly, delete the trigger in the service where you originally configured it.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example deletes version 1 of a Lambda function named my-function.
    Expected Output:
    
    :example: response = client.delete_function(
        FunctionName='string',
        Qualifier='string'
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the Lambda function or version.\n\nName formats\n\nFunction name - my-function (name-only), my-function:1 (with version).\nFunction ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function .\nPartial ARN - 123456789012:function:my-function .\n\nYou can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.\n

    :type Qualifier: string
    :param Qualifier: Specify a version to delete. You can\'t delete a version that\'s referenced by an alias.

    :return: response = client.delete_function(
        FunctionName='my-function',
        Qualifier='1',
    )
    
    print(response)
    
    
    :returns: 
    Lambda.Client.exceptions.ServiceException
    Lambda.Client.exceptions.ResourceNotFoundException
    Lambda.Client.exceptions.TooManyRequestsException
    Lambda.Client.exceptions.InvalidParameterValueException
    Lambda.Client.exceptions.ResourceConflictException
    
    """
    pass

def delete_function_concurrency(FunctionName=None):
    """
    Removes a concurrent execution limit from a function.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example deletes the reserved concurrent execution limit from a function named my-function.
    Expected Output:
    
    :example: response = client.delete_function_concurrency(
        FunctionName='string'
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the Lambda function.\n\nName formats\n\nFunction name - my-function .\nFunction ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function .\nPartial ARN - 123456789012:function:my-function .\n\nThe length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.\n

    :return: response = client.delete_function_concurrency(
        FunctionName='my-function',
    )
    
    print(response)
    
    
    :returns: 
    Lambda.Client.exceptions.ServiceException
    Lambda.Client.exceptions.ResourceNotFoundException
    Lambda.Client.exceptions.TooManyRequestsException
    Lambda.Client.exceptions.InvalidParameterValueException
    Lambda.Client.exceptions.ResourceConflictException
    
    """
    pass

def delete_function_event_invoke_config(FunctionName=None, Qualifier=None):
    """
    Deletes the configuration for asynchronous invocation for a function, version, or alias.
    To configure options for asynchronous invocation, use  PutFunctionEventInvokeConfig .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example deletes the asynchronous invocation configuration for the GREEN alias of a function named my-function.
    Expected Output:
    
    :example: response = client.delete_function_event_invoke_config(
        FunctionName='string',
        Qualifier='string'
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the Lambda function, version, or alias.\n\nName formats\n\nFunction name - my-function (name-only), my-function:v1 (with alias).\nFunction ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function .\nPartial ARN - 123456789012:function:my-function .\n\nYou can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.\n

    :type Qualifier: string
    :param Qualifier: A version number or alias name.

    :return: response = client.delete_function_event_invoke_config(
        FunctionName='my-function',
        Qualifier='GREEN',
    )
    
    print(response)
    
    
    :returns: 
    Lambda.Client.exceptions.ServiceException
    Lambda.Client.exceptions.ResourceNotFoundException
    Lambda.Client.exceptions.InvalidParameterValueException
    Lambda.Client.exceptions.TooManyRequestsException
    
    """
    pass

def delete_layer_version(LayerName=None, VersionNumber=None):
    """
    Deletes a version of an AWS Lambda layer . Deleted versions can no longer be viewed or added to functions. To avoid breaking functions, a copy of the version remains in Lambda until no functions refer to it.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example deletes version 2 of a layer named my-layer.
    Expected Output:
    
    :example: response = client.delete_layer_version(
        LayerName='string',
        VersionNumber=123
    )
    
    
    :type LayerName: string
    :param LayerName: [REQUIRED]\nThe name or Amazon Resource Name (ARN) of the layer.\n

    :type VersionNumber: integer
    :param VersionNumber: [REQUIRED]\nThe version number.\n

    :return: response = client.delete_layer_version(
        LayerName='my-layer',
        VersionNumber=2,
    )
    
    print(response)
    
    
    :returns: 
    Lambda.Client.exceptions.ServiceException
    Lambda.Client.exceptions.TooManyRequestsException
    
    """
    pass

def delete_provisioned_concurrency_config(FunctionName=None, Qualifier=None):
    """
    Deletes the provisioned concurrency configuration for a function.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example deletes the provisioned concurrency configuration for the GREEN alias of a function named my-function.
    Expected Output:
    
    :example: response = client.delete_provisioned_concurrency_config(
        FunctionName='string',
        Qualifier='string'
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the Lambda function.\n\nName formats\n\nFunction name - my-function .\nFunction ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function .\nPartial ARN - 123456789012:function:my-function .\n\nThe length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.\n

    :type Qualifier: string
    :param Qualifier: [REQUIRED]\nThe version number or alias name.\n

    :return: response = client.delete_provisioned_concurrency_config(
        FunctionName='my-function',
        Qualifier='GREEN',
    )
    
    print(response)
    
    
    :returns: 
    Lambda.Client.exceptions.InvalidParameterValueException
    Lambda.Client.exceptions.ResourceConflictException
    Lambda.Client.exceptions.ResourceNotFoundException
    Lambda.Client.exceptions.TooManyRequestsException
    Lambda.Client.exceptions.ServiceException
    
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

def get_account_settings():
    """
    Retrieves details about your account\'s limits and usage in an AWS Region.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This operation takes no parameters and returns details about storage and concurrency quotas in the current Region.
    Expected Output:
    
    :example: response = client.get_account_settings()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'AccountLimit': {
        'TotalCodeSize': 123,
        'CodeSizeUnzipped': 123,
        'CodeSizeZipped': 123,
        'ConcurrentExecutions': 123,
        'UnreservedConcurrentExecutions': 123
    },
    'AccountUsage': {
        'TotalCodeSize': 123,
        'FunctionCount': 123
    }
}


Response Structure

(dict) --
AccountLimit (dict) --Limits that are related to concurrency and code storage.

TotalCodeSize (integer) --The amount of storage space that you can use for all deployment packages and layer archives.

CodeSizeUnzipped (integer) --The maximum size of a function\'s deployment package and layers when they\'re extracted.

CodeSizeZipped (integer) --The maximum size of a deployment package when it\'s uploaded directly to AWS Lambda. Use Amazon S3 for larger files.

ConcurrentExecutions (integer) --The maximum number of simultaneous function executions.

UnreservedConcurrentExecutions (integer) --The maximum number of simultaneous function executions, minus the capacity that\'s reserved for individual functions with  PutFunctionConcurrency .



AccountUsage (dict) --The number of functions and amount of storage in use.

TotalCodeSize (integer) --The amount of storage space, in bytes, that\'s being used by deployment packages and layer archives.

FunctionCount (integer) --The number of Lambda functions.








Exceptions

Lambda.Client.exceptions.TooManyRequestsException
Lambda.Client.exceptions.ServiceException

Examples
This operation takes no parameters and returns details about storage and concurrency quotas in the current Region.
response = client.get_account_settings(
)

print(response)


Expected Output:
{
    'AccountLimit': {
        'CodeSizeUnzipped': 262144000,
        'CodeSizeZipped': 52428800,
        'ConcurrentExecutions': 1000,
        'TotalCodeSize': 80530636800,
        'UnreservedConcurrentExecutions': 1000,
    },
    'AccountUsage': {
        'FunctionCount': 4,
        'TotalCodeSize': 9426,
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'AccountLimit': {
            'TotalCodeSize': 123,
            'CodeSizeUnzipped': 123,
            'CodeSizeZipped': 123,
            'ConcurrentExecutions': 123,
            'UnreservedConcurrentExecutions': 123
        },
        'AccountUsage': {
            'TotalCodeSize': 123,
            'FunctionCount': 123
        }
    }
    
    
    """
    pass

def get_alias(FunctionName=None, Name=None):
    """
    Returns details about a Lambda function alias .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns details about an alias named BLUE for a function named my-function
    Expected Output:
    
    :example: response = client.get_alias(
        FunctionName='string',
        Name='string'
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the Lambda function.\n\nName formats\n\nFunction name - MyFunction .\nFunction ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .\nPartial ARN - 123456789012:function:MyFunction .\n\nThe length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.\n

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the alias.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AliasArn': 'string',
    'Name': 'string',
    'FunctionVersion': 'string',
    'Description': 'string',
    'RoutingConfig': {
        'AdditionalVersionWeights': {
            'string': 123.0
        }
    },
    'RevisionId': 'string'
}


Response Structure

(dict) --
Provides configuration information about a Lambda function alias .

AliasArn (string) --
The Amazon Resource Name (ARN) of the alias.

Name (string) --
The name of the alias.

FunctionVersion (string) --
The function version that the alias invokes.

Description (string) --
A description of the alias.

RoutingConfig (dict) --
The routing configuration of the alias.

AdditionalVersionWeights (dict) --
The name of the second alias, and the percentage of traffic that\'s routed to it.

(string) --
(float) --






RevisionId (string) --
A unique identifier that changes when you update the alias.







Exceptions

Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.ResourceNotFoundException
Lambda.Client.exceptions.InvalidParameterValueException
Lambda.Client.exceptions.TooManyRequestsException

Examples
The following example returns details about an alias named BLUE for a function named my-function
response = client.get_alias(
    FunctionName='my-function',
    Name='BLUE',
)

print(response)


Expected Output:
{
    'AliasArn': 'arn:aws:lambda:us-west-2:123456789012:function:my-function:BLUE',
    'Description': 'Production environment BLUE.',
    'FunctionVersion': '3',
    'Name': 'BLUE',
    'RevisionId': '594f41fb-xmpl-4c20-95c7-6ca5f2a92c93',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'AliasArn': 'string',
        'Name': 'string',
        'FunctionVersion': 'string',
        'Description': 'string',
        'RoutingConfig': {
            'AdditionalVersionWeights': {
                'string': 123.0
            }
        },
        'RevisionId': 'string'
    }
    
    
    :returns: 
    (string) --
    (float) --
    
    
    
    """
    pass

def get_event_source_mapping(UUID=None):
    """
    Returns details about an event source mapping. You can get the identifier of a mapping from the output of  ListEventSourceMappings .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns details about an event source mapping. To get a mapping\'s UUID, use ListEventSourceMappings.
    Expected Output:
    
    :example: response = client.get_event_source_mapping(
        UUID='string'
    )
    
    
    :type UUID: string
    :param UUID: [REQUIRED]\nThe identifier of the event source mapping.\n

    :rtype: dict
ReturnsResponse Syntax{
    'UUID': 'string',
    'BatchSize': 123,
    'MaximumBatchingWindowInSeconds': 123,
    'ParallelizationFactor': 123,
    'EventSourceArn': 'string',
    'FunctionArn': 'string',
    'LastModified': datetime(2015, 1, 1),
    'LastProcessingResult': 'string',
    'State': 'string',
    'StateTransitionReason': 'string',
    'DestinationConfig': {
        'OnSuccess': {
            'Destination': 'string'
        },
        'OnFailure': {
            'Destination': 'string'
        }
    },
    'MaximumRecordAgeInSeconds': 123,
    'BisectBatchOnFunctionError': True|False,
    'MaximumRetryAttempts': 123
}


Response Structure

(dict) --A mapping between an AWS resource and an AWS Lambda function. See  CreateEventSourceMapping for details.

UUID (string) --The identifier of the event source mapping.

BatchSize (integer) --The maximum number of items to retrieve in a single batch.

MaximumBatchingWindowInSeconds (integer) --(Streams) The maximum amount of time to gather records before invoking the function, in seconds.

ParallelizationFactor (integer) --(Streams) The number of batches to process from each shard concurrently.

EventSourceArn (string) --The Amazon Resource Name (ARN) of the event source.

FunctionArn (string) --The ARN of the Lambda function.

LastModified (datetime) --The date that the event source mapping was last updated, or its state changed.

LastProcessingResult (string) --The result of the last AWS Lambda invocation of your Lambda function.

State (string) --The state of the event source mapping. It can be one of the following: Creating , Enabling , Enabled , Disabling , Disabled , Updating , or Deleting .

StateTransitionReason (string) --Indicates whether the last change to the event source mapping was made by a user, or by the Lambda service.

DestinationConfig (dict) --(Streams) An Amazon SQS queue or Amazon SNS topic destination for discarded records.

OnSuccess (dict) --The destination configuration for successful invocations.

Destination (string) --The Amazon Resource Name (ARN) of the destination resource.



OnFailure (dict) --The destination configuration for failed invocations.

Destination (string) --The Amazon Resource Name (ARN) of the destination resource.





MaximumRecordAgeInSeconds (integer) --(Streams) The maximum age of a record that Lambda sends to a function for processing.

BisectBatchOnFunctionError (boolean) --(Streams) If the function returns an error, split the batch in two and retry.

MaximumRetryAttempts (integer) --(Streams) The maximum number of times to retry when the function returns an error.






Exceptions

Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.ResourceNotFoundException
Lambda.Client.exceptions.InvalidParameterValueException
Lambda.Client.exceptions.TooManyRequestsException

Examples
The following example returns details about an event source mapping. To get a mapping\'s UUID, use ListEventSourceMappings.
response = client.get_event_source_mapping(
    UUID='14e0db71-xmpl-4eb5-b481-8945cf9d10c2',
)

print(response)


Expected Output:
{
    'BatchSize': 500,
    'BisectBatchOnFunctionError': False,
    'DestinationConfig': {
    },
    'EventSourceArn': 'arn:aws:sqs:us-east-2:123456789012:mySQSqueue',
    'FunctionArn': 'arn:aws:lambda:us-east-2:123456789012:function:myFunction',
    'LastModified': datetime(2016, 11, 21, 19, 49, 20, 0, 326, 0),
    'LastProcessingResult': 'No records processed',
    'MaximumRecordAgeInSeconds': 604800,
    'MaximumRetryAttempts': 10000,
    'State': 'Creating',
    'StateTransitionReason': 'User action',
    'UUID': '14e0db71-xmpl-4eb5-b481-8945cf9d10c2',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'UUID': 'string',
        'BatchSize': 123,
        'MaximumBatchingWindowInSeconds': 123,
        'ParallelizationFactor': 123,
        'EventSourceArn': 'string',
        'FunctionArn': 'string',
        'LastModified': datetime(2015, 1, 1),
        'LastProcessingResult': 'string',
        'State': 'string',
        'StateTransitionReason': 'string',
        'DestinationConfig': {
            'OnSuccess': {
                'Destination': 'string'
            },
            'OnFailure': {
                'Destination': 'string'
            }
        },
        'MaximumRecordAgeInSeconds': 123,
        'BisectBatchOnFunctionError': True|False,
        'MaximumRetryAttempts': 123
    }
    
    
    """
    pass

def get_function(FunctionName=None, Qualifier=None):
    """
    Returns information about the function or function version, with a link to download the deployment package that\'s valid for 10 minutes. If you specify a function version, only details that are specific to that version are returned.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns code and configuration details for version 1 of a function named my-function.
    Expected Output:
    
    :example: response = client.get_function(
        FunctionName='string',
        Qualifier='string'
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the Lambda function, version, or alias.\n\nName formats\n\nFunction name - my-function (name-only), my-function:v1 (with alias).\nFunction ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function .\nPartial ARN - 123456789012:function:my-function .\n\nYou can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.\n

    :type Qualifier: string
    :param Qualifier: Specify a version or alias to get details about a published version of the function.

    :rtype: dict

ReturnsResponse Syntax
{
    'Configuration': {
        'FunctionName': 'string',
        'FunctionArn': 'string',
        'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'dotnetcore3.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'ruby2.7'|'provided',
        'Role': 'string',
        'Handler': 'string',
        'CodeSize': 123,
        'Description': 'string',
        'Timeout': 123,
        'MemorySize': 123,
        'LastModified': 'string',
        'CodeSha256': 'string',
        'Version': 'string',
        'VpcConfig': {
            'SubnetIds': [
                'string',
            ],
            'SecurityGroupIds': [
                'string',
            ],
            'VpcId': 'string'
        },
        'DeadLetterConfig': {
            'TargetArn': 'string'
        },
        'Environment': {
            'Variables': {
                'string': 'string'
            },
            'Error': {
                'ErrorCode': 'string',
                'Message': 'string'
            }
        },
        'KMSKeyArn': 'string',
        'TracingConfig': {
            'Mode': 'Active'|'PassThrough'
        },
        'MasterArn': 'string',
        'RevisionId': 'string',
        'Layers': [
            {
                'Arn': 'string',
                'CodeSize': 123
            },
        ],
        'State': 'Pending'|'Active'|'Inactive'|'Failed',
        'StateReason': 'string',
        'StateReasonCode': 'Idle'|'Creating'|'Restoring'|'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'|'SubnetOutOfIPAddresses'|'InvalidSubnet'|'InvalidSecurityGroup',
        'LastUpdateStatus': 'Successful'|'Failed'|'InProgress',
        'LastUpdateStatusReason': 'string',
        'LastUpdateStatusReasonCode': 'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'|'SubnetOutOfIPAddresses'|'InvalidSubnet'|'InvalidSecurityGroup'
    },
    'Code': {
        'RepositoryType': 'string',
        'Location': 'string'
    },
    'Tags': {
        'string': 'string'
    },
    'Concurrency': {
        'ReservedConcurrentExecutions': 123
    }
}


Response Structure

(dict) --

Configuration (dict) --
The configuration of the function or version.

FunctionName (string) --
The name of the function.

FunctionArn (string) --
The function\'s Amazon Resource Name (ARN).

Runtime (string) --
The runtime environment for the Lambda function.

Role (string) --
The function\'s execution role.

Handler (string) --
The function that Lambda calls to begin executing your function.

CodeSize (integer) --
The size of the function\'s deployment package, in bytes.

Description (string) --
The function\'s description.

Timeout (integer) --
The amount of time in seconds that Lambda allows a function to run before stopping it.

MemorySize (integer) --
The memory that\'s allocated to the function.

LastModified (string) --
The date and time that the function was last updated, in ISO-8601 format (YYYY-MM-DDThh:mm:ss.sTZD).

CodeSha256 (string) --
The SHA256 hash of the function\'s deployment package.

Version (string) --
The version of the Lambda function.

VpcConfig (dict) --
The function\'s networking configuration.

SubnetIds (list) --
A list of VPC subnet IDs.

(string) --


SecurityGroupIds (list) --
A list of VPC security groups IDs.

(string) --


VpcId (string) --
The ID of the VPC.



DeadLetterConfig (dict) --
The function\'s dead letter queue.

TargetArn (string) --
The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.



Environment (dict) --
The function\'s environment variables.

Variables (dict) --
Environment variable key-value pairs.

(string) --
(string) --




Error (dict) --
Error messages for environment variables that couldn\'t be applied.

ErrorCode (string) --
The error code.

Message (string) --
The error message.





KMSKeyArn (string) --
The KMS key that\'s used to encrypt the function\'s environment variables. This key is only returned if you\'ve configured a customer managed CMK.

TracingConfig (dict) --
The function\'s AWS X-Ray tracing configuration.

Mode (string) --
The tracing mode.



MasterArn (string) --
For Lambda@Edge functions, the ARN of the master function.

RevisionId (string) --
The latest updated revision of the function or alias.

Layers (list) --
The function\'s layers .

(dict) --
An AWS Lambda layer .

Arn (string) --
The Amazon Resource Name (ARN) of the function layer.

CodeSize (integer) --
The size of the layer archive in bytes.





State (string) --
The current state of the function. When the state is Inactive , you can reactivate the function by invoking it.

StateReason (string) --
The reason for the function\'s current state.

StateReasonCode (string) --
The reason code for the function\'s current state. When the code is Creating , you can\'t invoke or modify the function.

LastUpdateStatus (string) --
The status of the last update that was performed on the function. This is first set to Successful after function creation completes.

LastUpdateStatusReason (string) --
The reason for the last update that was performed on the function.

LastUpdateStatusReasonCode (string) --
The reason code for the last update that was performed on the function.



Code (dict) --
The deployment package of the function or version.

RepositoryType (string) --
The service that\'s hosting the file.

Location (string) --
A presigned URL that you can use to download the deployment package.



Tags (dict) --
The function\'s tags .

(string) --
(string) --




Concurrency (dict) --
The function\'s reserved concurrency .

ReservedConcurrentExecutions (integer) --
The number of concurrent executions that are reserved for this function. For more information, see Managing Concurrency .









Exceptions

Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.ResourceNotFoundException
Lambda.Client.exceptions.TooManyRequestsException
Lambda.Client.exceptions.InvalidParameterValueException

Examples
The following example returns code and configuration details for version 1 of a function named my-function.
response = client.get_function(
    FunctionName='my-function',
    Qualifier='1',
)

print(response)


Expected Output:
{
    'Code': {
        'Location': 'https://awslambda-us-west-2-tasks.s3.us-west-2.amazonaws.com/snapshots/123456789012/my-function-e7d9d1ed-xmpl-4f79-904a-4b87f2681f30?versionId=sH3TQwBOaUy...',
        'RepositoryType': 'S3',
    },
    'Configuration': {
        'CodeSha256': 'YFgDgEKG3ugvF1+pX64gV6tu9qNuIYNUdgJm8nCxsm4=',
        'CodeSize': 5797206,
        'Description': 'Process image objects from Amazon S3.',
        'Environment': {
            'Variables': {
                'BUCKET': 'my-bucket-1xpuxmplzrlbh',
                'PREFIX': 'inbound',
            },
        },
        'FunctionArn': 'arn:aws:lambda:us-west-2:123456789012:function:my-function',
        'FunctionName': 'my-function',
        'Handler': 'index.handler',
        'KMSKeyArn': 'arn:aws:kms:us-west-2:123456789012:key/b0844d6c-xmpl-4463-97a4-d49f50839966',
        'LastModified': '2020-04-10T19:06:32.563+0000',
        'LastUpdateStatus': 'Successful',
        'MemorySize': 256,
        'RevisionId': 'b75dcd81-xmpl-48a8-a75a-93ba8b5b9727',
        'Role': 'arn:aws:iam::123456789012:role/lambda-role',
        'Runtime': 'nodejs12.x',
        'State': 'Active',
        'Timeout': 15,
        'TracingConfig': {
            'Mode': 'Active',
        },
        'Version': '$LATEST',
    },
    'Tags': {
        'DEPARTMENT': 'Assets',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Configuration': {
            'FunctionName': 'string',
            'FunctionArn': 'string',
            'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'dotnetcore3.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'ruby2.7'|'provided',
            'Role': 'string',
            'Handler': 'string',
            'CodeSize': 123,
            'Description': 'string',
            'Timeout': 123,
            'MemorySize': 123,
            'LastModified': 'string',
            'CodeSha256': 'string',
            'Version': 'string',
            'VpcConfig': {
                'SubnetIds': [
                    'string',
                ],
                'SecurityGroupIds': [
                    'string',
                ],
                'VpcId': 'string'
            },
            'DeadLetterConfig': {
                'TargetArn': 'string'
            },
            'Environment': {
                'Variables': {
                    'string': 'string'
                },
                'Error': {
                    'ErrorCode': 'string',
                    'Message': 'string'
                }
            },
            'KMSKeyArn': 'string',
            'TracingConfig': {
                'Mode': 'Active'|'PassThrough'
            },
            'MasterArn': 'string',
            'RevisionId': 'string',
            'Layers': [
                {
                    'Arn': 'string',
                    'CodeSize': 123
                },
            ],
            'State': 'Pending'|'Active'|'Inactive'|'Failed',
            'StateReason': 'string',
            'StateReasonCode': 'Idle'|'Creating'|'Restoring'|'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'|'SubnetOutOfIPAddresses'|'InvalidSubnet'|'InvalidSecurityGroup',
            'LastUpdateStatus': 'Successful'|'Failed'|'InProgress',
            'LastUpdateStatusReason': 'string',
            'LastUpdateStatusReasonCode': 'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'|'SubnetOutOfIPAddresses'|'InvalidSubnet'|'InvalidSecurityGroup'
        },
        'Code': {
            'RepositoryType': 'string',
            'Location': 'string'
        },
        'Tags': {
            'string': 'string'
        },
        'Concurrency': {
            'ReservedConcurrentExecutions': 123
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_function_concurrency(FunctionName=None):
    """
    Returns details about the reserved concurrency configuration for a function. To set a concurrency limit for a function, use  PutFunctionConcurrency .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns the reserved concurrency setting for a function named my-function.
    Expected Output:
    
    :example: response = client.get_function_concurrency(
        FunctionName='string'
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the Lambda function.\n\nName formats\n\nFunction name - my-function .\nFunction ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function .\nPartial ARN - 123456789012:function:my-function .\n\nThe length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ReservedConcurrentExecutions': 123
}


Response Structure

(dict) --
ReservedConcurrentExecutions (integer) --The number of simultaneous executions that are reserved for the function.






Exceptions

Lambda.Client.exceptions.InvalidParameterValueException
Lambda.Client.exceptions.ResourceNotFoundException
Lambda.Client.exceptions.TooManyRequestsException
Lambda.Client.exceptions.ServiceException

Examples
The following example returns the reserved concurrency setting for a function named my-function.
response = client.get_function_concurrency(
    FunctionName='my-function',
)

print(response)


Expected Output:
{
    'ReservedConcurrentExecutions': 250,
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ReservedConcurrentExecutions': 123
    }
    
    
    :returns: 
    Lambda.Client.exceptions.InvalidParameterValueException
    Lambda.Client.exceptions.ResourceNotFoundException
    Lambda.Client.exceptions.TooManyRequestsException
    Lambda.Client.exceptions.ServiceException
    
    """
    pass

def get_function_configuration(FunctionName=None, Qualifier=None):
    """
    Returns the version-specific settings of a Lambda function or version. The output includes only options that can vary between versions of a function. To modify these settings, use  UpdateFunctionConfiguration .
    To get all of a function\'s details, including function-level settings, use  GetFunction .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns and configuration details for version 1 of a function named my-function.
    Expected Output:
    
    :example: response = client.get_function_configuration(
        FunctionName='string',
        Qualifier='string'
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the Lambda function, version, or alias.\n\nName formats\n\nFunction name - my-function (name-only), my-function:v1 (with alias).\nFunction ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function .\nPartial ARN - 123456789012:function:my-function .\n\nYou can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.\n

    :type Qualifier: string
    :param Qualifier: Specify a version or alias to get details about a published version of the function.

    :rtype: dict

ReturnsResponse Syntax
{
    'FunctionName': 'string',
    'FunctionArn': 'string',
    'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'dotnetcore3.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'ruby2.7'|'provided',
    'Role': 'string',
    'Handler': 'string',
    'CodeSize': 123,
    'Description': 'string',
    'Timeout': 123,
    'MemorySize': 123,
    'LastModified': 'string',
    'CodeSha256': 'string',
    'Version': 'string',
    'VpcConfig': {
        'SubnetIds': [
            'string',
        ],
        'SecurityGroupIds': [
            'string',
        ],
        'VpcId': 'string'
    },
    'DeadLetterConfig': {
        'TargetArn': 'string'
    },
    'Environment': {
        'Variables': {
            'string': 'string'
        },
        'Error': {
            'ErrorCode': 'string',
            'Message': 'string'
        }
    },
    'KMSKeyArn': 'string',
    'TracingConfig': {
        'Mode': 'Active'|'PassThrough'
    },
    'MasterArn': 'string',
    'RevisionId': 'string',
    'Layers': [
        {
            'Arn': 'string',
            'CodeSize': 123
        },
    ],
    'State': 'Pending'|'Active'|'Inactive'|'Failed',
    'StateReason': 'string',
    'StateReasonCode': 'Idle'|'Creating'|'Restoring'|'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'|'SubnetOutOfIPAddresses'|'InvalidSubnet'|'InvalidSecurityGroup',
    'LastUpdateStatus': 'Successful'|'Failed'|'InProgress',
    'LastUpdateStatusReason': 'string',
    'LastUpdateStatusReasonCode': 'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'|'SubnetOutOfIPAddresses'|'InvalidSubnet'|'InvalidSecurityGroup'
}


Response Structure

(dict) --
Details about a function\'s configuration.

FunctionName (string) --
The name of the function.

FunctionArn (string) --
The function\'s Amazon Resource Name (ARN).

Runtime (string) --
The runtime environment for the Lambda function.

Role (string) --
The function\'s execution role.

Handler (string) --
The function that Lambda calls to begin executing your function.

CodeSize (integer) --
The size of the function\'s deployment package, in bytes.

Description (string) --
The function\'s description.

Timeout (integer) --
The amount of time in seconds that Lambda allows a function to run before stopping it.

MemorySize (integer) --
The memory that\'s allocated to the function.

LastModified (string) --
The date and time that the function was last updated, in ISO-8601 format (YYYY-MM-DDThh:mm:ss.sTZD).

CodeSha256 (string) --
The SHA256 hash of the function\'s deployment package.

Version (string) --
The version of the Lambda function.

VpcConfig (dict) --
The function\'s networking configuration.

SubnetIds (list) --
A list of VPC subnet IDs.

(string) --


SecurityGroupIds (list) --
A list of VPC security groups IDs.

(string) --


VpcId (string) --
The ID of the VPC.



DeadLetterConfig (dict) --
The function\'s dead letter queue.

TargetArn (string) --
The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.



Environment (dict) --
The function\'s environment variables.

Variables (dict) --
Environment variable key-value pairs.

(string) --
(string) --




Error (dict) --
Error messages for environment variables that couldn\'t be applied.

ErrorCode (string) --
The error code.

Message (string) --
The error message.





KMSKeyArn (string) --
The KMS key that\'s used to encrypt the function\'s environment variables. This key is only returned if you\'ve configured a customer managed CMK.

TracingConfig (dict) --
The function\'s AWS X-Ray tracing configuration.

Mode (string) --
The tracing mode.



MasterArn (string) --
For Lambda@Edge functions, the ARN of the master function.

RevisionId (string) --
The latest updated revision of the function or alias.

Layers (list) --
The function\'s layers .

(dict) --
An AWS Lambda layer .

Arn (string) --
The Amazon Resource Name (ARN) of the function layer.

CodeSize (integer) --
The size of the layer archive in bytes.





State (string) --
The current state of the function. When the state is Inactive , you can reactivate the function by invoking it.

StateReason (string) --
The reason for the function\'s current state.

StateReasonCode (string) --
The reason code for the function\'s current state. When the code is Creating , you can\'t invoke or modify the function.

LastUpdateStatus (string) --
The status of the last update that was performed on the function. This is first set to Successful after function creation completes.

LastUpdateStatusReason (string) --
The reason for the last update that was performed on the function.

LastUpdateStatusReasonCode (string) --
The reason code for the last update that was performed on the function.







Exceptions

Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.ResourceNotFoundException
Lambda.Client.exceptions.TooManyRequestsException
Lambda.Client.exceptions.InvalidParameterValueException

Examples
The following example returns and configuration details for version 1 of a function named my-function.
response = client.get_function_configuration(
    FunctionName='my-function',
    Qualifier='1',
)

print(response)


Expected Output:
{
    'CodeSha256': 'YFgDgEKG3ugvF1+pX64gV6tu9qNuIYNUdgJm8nCxsm4=',
    'CodeSize': 5797206,
    'Description': 'Process image objects from Amazon S3.',
    'Environment': {
        'Variables': {
            'BUCKET': 'my-bucket-1xpuxmplzrlbh',
            'PREFIX': 'inbound',
        },
    },
    'FunctionArn': 'arn:aws:lambda:us-west-2:123456789012:function:my-function',
    'FunctionName': 'my-function',
    'Handler': 'index.handler',
    'KMSKeyArn': 'arn:aws:kms:us-west-2:123456789012:key/b0844d6c-xmpl-4463-97a4-d49f50839966',
    'LastModified': '2020-04-10T19:06:32.563+0000',
    'LastUpdateStatus': 'Successful',
    'MemorySize': 256,
    'RevisionId': 'b75dcd81-xmpl-48a8-a75a-93ba8b5b9727',
    'Role': 'arn:aws:iam::123456789012:role/lambda-role',
    'Runtime': 'nodejs12.x',
    'State': 'Active',
    'Timeout': 15,
    'TracingConfig': {
        'Mode': 'Active',
    },
    'Version': '$LATEST',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'FunctionName': 'string',
        'FunctionArn': 'string',
        'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'dotnetcore3.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'ruby2.7'|'provided',
        'Role': 'string',
        'Handler': 'string',
        'CodeSize': 123,
        'Description': 'string',
        'Timeout': 123,
        'MemorySize': 123,
        'LastModified': 'string',
        'CodeSha256': 'string',
        'Version': 'string',
        'VpcConfig': {
            'SubnetIds': [
                'string',
            ],
            'SecurityGroupIds': [
                'string',
            ],
            'VpcId': 'string'
        },
        'DeadLetterConfig': {
            'TargetArn': 'string'
        },
        'Environment': {
            'Variables': {
                'string': 'string'
            },
            'Error': {
                'ErrorCode': 'string',
                'Message': 'string'
            }
        },
        'KMSKeyArn': 'string',
        'TracingConfig': {
            'Mode': 'Active'|'PassThrough'
        },
        'MasterArn': 'string',
        'RevisionId': 'string',
        'Layers': [
            {
                'Arn': 'string',
                'CodeSize': 123
            },
        ],
        'State': 'Pending'|'Active'|'Inactive'|'Failed',
        'StateReason': 'string',
        'StateReasonCode': 'Idle'|'Creating'|'Restoring'|'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'|'SubnetOutOfIPAddresses'|'InvalidSubnet'|'InvalidSecurityGroup',
        'LastUpdateStatus': 'Successful'|'Failed'|'InProgress',
        'LastUpdateStatusReason': 'string',
        'LastUpdateStatusReasonCode': 'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'|'SubnetOutOfIPAddresses'|'InvalidSubnet'|'InvalidSecurityGroup'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_function_event_invoke_config(FunctionName=None, Qualifier=None):
    """
    Retrieves the configuration for asynchronous invocation for a function, version, or alias.
    To configure options for asynchronous invocation, use  PutFunctionEventInvokeConfig .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns the asynchronous invocation configuration for the BLUE alias of a function named my-function.
    Expected Output:
    
    :example: response = client.get_function_event_invoke_config(
        FunctionName='string',
        Qualifier='string'
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the Lambda function, version, or alias.\n\nName formats\n\nFunction name - my-function (name-only), my-function:v1 (with alias).\nFunction ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function .\nPartial ARN - 123456789012:function:my-function .\n\nYou can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.\n

    :type Qualifier: string
    :param Qualifier: A version number or alias name.

    :rtype: dict

ReturnsResponse Syntax
{
    'LastModified': datetime(2015, 1, 1),
    'FunctionArn': 'string',
    'MaximumRetryAttempts': 123,
    'MaximumEventAgeInSeconds': 123,
    'DestinationConfig': {
        'OnSuccess': {
            'Destination': 'string'
        },
        'OnFailure': {
            'Destination': 'string'
        }
    }
}


Response Structure

(dict) --

LastModified (datetime) --
The date and time that the configuration was last updated.

FunctionArn (string) --
The Amazon Resource Name (ARN) of the function.

MaximumRetryAttempts (integer) --
The maximum number of times to retry when the function returns an error.

MaximumEventAgeInSeconds (integer) --
The maximum age of a request that Lambda sends to a function for processing.

DestinationConfig (dict) --
A destination for events after they have been sent to a function for processing.

Destinations


Function - The Amazon Resource Name (ARN) of a Lambda function.
Queue - The ARN of an SQS queue.
Topic - The ARN of an SNS topic.
Event Bus - The ARN of an Amazon EventBridge event bus.


OnSuccess (dict) --
The destination configuration for successful invocations.

Destination (string) --
The Amazon Resource Name (ARN) of the destination resource.



OnFailure (dict) --
The destination configuration for failed invocations.

Destination (string) --
The Amazon Resource Name (ARN) of the destination resource.











Exceptions

Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.ResourceNotFoundException
Lambda.Client.exceptions.InvalidParameterValueException
Lambda.Client.exceptions.TooManyRequestsException

Examples
The following example returns the asynchronous invocation configuration for the BLUE alias of a function named my-function.
response = client.get_function_event_invoke_config(
    FunctionName='my-function',
    Qualifier='BLUE',
)

print(response)


Expected Output:
{
    'DestinationConfig': {
        'OnFailure': {
            'Destination': 'arn:aws:sqs:us-east-2:123456789012:failed-invocations',
        },
        'OnSuccess': {
        },
    },
    'FunctionArn': 'arn:aws:lambda:us-east-2:123456789012:function:my-function:BLUE',
    'LastModified': datetime(2016, 11, 21, 19, 49, 20, 0, 326, 0),
    'MaximumEventAgeInSeconds': 3600,
    'MaximumRetryAttempts': 0,
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'LastModified': datetime(2015, 1, 1),
        'FunctionArn': 'string',
        'MaximumRetryAttempts': 123,
        'MaximumEventAgeInSeconds': 123,
        'DestinationConfig': {
            'OnSuccess': {
                'Destination': 'string'
            },
            'OnFailure': {
                'Destination': 'string'
            }
        }
    }
    
    
    :returns: 
    Function - The Amazon Resource Name (ARN) of a Lambda function.
    Queue - The ARN of an SQS queue.
    Topic - The ARN of an SNS topic.
    Event Bus - The ARN of an Amazon EventBridge event bus.
    
    """
    pass

def get_layer_version(LayerName=None, VersionNumber=None):
    """
    Returns information about a version of an AWS Lambda layer , with a link to download the layer archive that\'s valid for 10 minutes.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns information for version 1 of a layer named my-layer.
    Expected Output:
    
    :example: response = client.get_layer_version(
        LayerName='string',
        VersionNumber=123
    )
    
    
    :type LayerName: string
    :param LayerName: [REQUIRED]\nThe name or Amazon Resource Name (ARN) of the layer.\n

    :type VersionNumber: integer
    :param VersionNumber: [REQUIRED]\nThe version number.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Content': {
        'Location': 'string',
        'CodeSha256': 'string',
        'CodeSize': 123
    },
    'LayerArn': 'string',
    'LayerVersionArn': 'string',
    'Description': 'string',
    'CreatedDate': 'string',
    'Version': 123,
    'CompatibleRuntimes': [
        'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'dotnetcore3.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'ruby2.7'|'provided',
    ],
    'LicenseInfo': 'string'
}


Response Structure

(dict) --

Content (dict) --
Details about the layer version.

Location (string) --
A link to the layer archive in Amazon S3 that is valid for 10 minutes.

CodeSha256 (string) --
The SHA-256 hash of the layer archive.

CodeSize (integer) --
The size of the layer archive in bytes.



LayerArn (string) --
The ARN of the layer.

LayerVersionArn (string) --
The ARN of the layer version.

Description (string) --
The description of the version.

CreatedDate (string) --
The date that the layer version was created, in ISO-8601 format (YYYY-MM-DDThh:mm:ss.sTZD).

Version (integer) --
The version number.

CompatibleRuntimes (list) --
The layer\'s compatible runtimes.

(string) --


LicenseInfo (string) --
The layer\'s software license.







Exceptions

Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.InvalidParameterValueException
Lambda.Client.exceptions.TooManyRequestsException
Lambda.Client.exceptions.ResourceNotFoundException

Examples
The following example returns information for version 1 of a layer named my-layer.
response = client.get_layer_version(
    LayerName='my-layer',
    VersionNumber=1,
)

print(response)


Expected Output:
{
    'CompatibleRuntimes': [
        'python3.6',
        'python3.7',
    ],
    'Content': {
        'CodeSha256': 'tv9jJO+rPbXUUXuRKi7CwHzKtLDkDRJLB3cC3Z/ouXo=',
        'CodeSize': 169,
        'Location': 'https://awslambda-us-east-2-layers.s3.us-east-2.amazonaws.com/snapshots/123456789012/my-layer-4aaa2fbb-ff77-4b0a-ad92-5b78a716a96a?versionId=27iWyA73cCAYqyH...',
    },
    'CreatedDate': '2018-11-14T23:03:52.894+0000',
    'Description': 'My Python layer',
    'LayerArn': 'arn:aws:lambda:us-east-2:123456789012:layer:my-layer',
    'LayerVersionArn': 'arn:aws:lambda:us-east-2:123456789012:layer:my-layer:1',
    'LicenseInfo': 'MIT',
    'Version': 1,
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Content': {
            'Location': 'string',
            'CodeSha256': 'string',
            'CodeSize': 123
        },
        'LayerArn': 'string',
        'LayerVersionArn': 'string',
        'Description': 'string',
        'CreatedDate': 'string',
        'Version': 123,
        'CompatibleRuntimes': [
            'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'dotnetcore3.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'ruby2.7'|'provided',
        ],
        'LicenseInfo': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_layer_version_by_arn(Arn=None):
    """
    Returns information about a version of an AWS Lambda layer , with a link to download the layer archive that\'s valid for 10 minutes.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns information about the layer version with the specified Amazon Resource Name (ARN).
    Expected Output:
    
    :example: response = client.get_layer_version_by_arn(
        Arn='string'
    )
    
    
    :type Arn: string
    :param Arn: [REQUIRED]\nThe ARN of the layer version.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Content': {
        'Location': 'string',
        'CodeSha256': 'string',
        'CodeSize': 123
    },
    'LayerArn': 'string',
    'LayerVersionArn': 'string',
    'Description': 'string',
    'CreatedDate': 'string',
    'Version': 123,
    'CompatibleRuntimes': [
        'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'dotnetcore3.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'ruby2.7'|'provided',
    ],
    'LicenseInfo': 'string'
}


Response Structure

(dict) --
Content (dict) --Details about the layer version.

Location (string) --A link to the layer archive in Amazon S3 that is valid for 10 minutes.

CodeSha256 (string) --The SHA-256 hash of the layer archive.

CodeSize (integer) --The size of the layer archive in bytes.



LayerArn (string) --The ARN of the layer.

LayerVersionArn (string) --The ARN of the layer version.

Description (string) --The description of the version.

CreatedDate (string) --The date that the layer version was created, in ISO-8601 format (YYYY-MM-DDThh:mm:ss.sTZD).

Version (integer) --The version number.

CompatibleRuntimes (list) --The layer\'s compatible runtimes.

(string) --


LicenseInfo (string) --The layer\'s software license.






Exceptions

Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.InvalidParameterValueException
Lambda.Client.exceptions.TooManyRequestsException
Lambda.Client.exceptions.ResourceNotFoundException

Examples
The following example returns information about the layer version with the specified Amazon Resource Name (ARN).
response = client.get_layer_version_by_arn(
    Arn='arn:aws:lambda:ca-central-1:123456789012:layer:blank-python-lib:3',
)

print(response)


Expected Output:
{
    'CompatibleRuntimes': [
        'python3.8',
    ],
    'Content': {
        'CodeSha256': '6x+xmpl/M3BnQUk7gS9sGmfeFsR/npojXoA3fZUv4eU=',
        'CodeSize': 9529009,
        'Location': 'https://awslambda-us-east-2-layers.s3.us-east-2.amazonaws.com/snapshots/123456789012/blank-python-lib-e5212378-xmpl-44ee-8398-9d8ec5113949?versionId=WbZnvf...',
    },
    'CreatedDate': '2020-03-31T00:35:18.949+0000',
    'Description': 'Dependencies for the blank-python sample app.',
    'LayerArn': 'arn:aws:lambda:us-east-2:123456789012:layer:blank-python-lib',
    'LayerVersionArn': 'arn:aws:lambda:us-east-2:123456789012:layer:blank-python-lib:3',
    'Version': 3,
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Content': {
            'Location': 'string',
            'CodeSha256': 'string',
            'CodeSize': 123
        },
        'LayerArn': 'string',
        'LayerVersionArn': 'string',
        'Description': 'string',
        'CreatedDate': 'string',
        'Version': 123,
        'CompatibleRuntimes': [
            'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'dotnetcore3.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'ruby2.7'|'provided',
        ],
        'LicenseInfo': 'string'
    }
    
    
    :returns: 
    Lambda.Client.exceptions.ServiceException
    Lambda.Client.exceptions.InvalidParameterValueException
    Lambda.Client.exceptions.TooManyRequestsException
    Lambda.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def get_layer_version_policy(LayerName=None, VersionNumber=None):
    """
    Returns the permission policy for a version of an AWS Lambda layer . For more information, see  AddLayerVersionPermission .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_layer_version_policy(
        LayerName='string',
        VersionNumber=123
    )
    
    
    :type LayerName: string
    :param LayerName: [REQUIRED]\nThe name or Amazon Resource Name (ARN) of the layer.\n

    :type VersionNumber: integer
    :param VersionNumber: [REQUIRED]\nThe version number.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Policy': 'string',
    'RevisionId': 'string'
}


Response Structure

(dict) --

Policy (string) --
The policy document.

RevisionId (string) --
A unique identifier for the current revision of the policy.







Exceptions

Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.ResourceNotFoundException
Lambda.Client.exceptions.TooManyRequestsException
Lambda.Client.exceptions.InvalidParameterValueException


    :return: {
        'Policy': 'string',
        'RevisionId': 'string'
    }
    
    
    :returns: 
    Lambda.Client.exceptions.ServiceException
    Lambda.Client.exceptions.ResourceNotFoundException
    Lambda.Client.exceptions.TooManyRequestsException
    Lambda.Client.exceptions.InvalidParameterValueException
    
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

def get_policy(FunctionName=None, Qualifier=None):
    """
    Returns the resource-based IAM policy for a function, version, or alias.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns the resource-based policy for version 1 of a Lambda function named my-function.
    Expected Output:
    
    :example: response = client.get_policy(
        FunctionName='string',
        Qualifier='string'
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the Lambda function, version, or alias.\n\nName formats\n\nFunction name - my-function (name-only), my-function:v1 (with alias).\nFunction ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function .\nPartial ARN - 123456789012:function:my-function .\n\nYou can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.\n

    :type Qualifier: string
    :param Qualifier: Specify a version or alias to get the policy for that resource.

    :rtype: dict

ReturnsResponse Syntax
{
    'Policy': 'string',
    'RevisionId': 'string'
}


Response Structure

(dict) --

Policy (string) --
The resource-based policy.

RevisionId (string) --
A unique identifier for the current revision of the policy.







Exceptions

Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.ResourceNotFoundException
Lambda.Client.exceptions.TooManyRequestsException
Lambda.Client.exceptions.InvalidParameterValueException

Examples
The following example returns the resource-based policy for version 1 of a Lambda function named my-function.
response = client.get_policy(
    FunctionName='my-function',
    Qualifier='1',
)

print(response)


Expected Output:
{
    'Policy': '{"Version":"2012-10-17","Id":"default","Statement":[{"Sid":"xaccount","Effect":"Allow","Principal":{"AWS":"arn:aws:iam::123456789012:root"},"Action":"lambda:InvokeFunction","Resource":"arn:aws:lambda:us-east-2:123456789012:function:my-function:1"}]}',
    'RevisionId': '4843f2f6-7c59-4fda-b484-afd0bc0e22b8',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Policy': 'string',
        'RevisionId': 'string'
    }
    
    
    :returns: 
    Lambda.Client.exceptions.ServiceException
    Lambda.Client.exceptions.ResourceNotFoundException
    Lambda.Client.exceptions.TooManyRequestsException
    Lambda.Client.exceptions.InvalidParameterValueException
    
    """
    pass

def get_provisioned_concurrency_config(FunctionName=None, Qualifier=None):
    """
    Retrieves the provisioned concurrency configuration for a function\'s alias or version.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns details for the provisioned concurrency configuration for the BLUE alias of the specified function.
    Expected Output:
    The following example displays details for the provisioned concurrency configuration for the BLUE alias of the specified function.
    Expected Output:
    
    :example: response = client.get_provisioned_concurrency_config(
        FunctionName='string',
        Qualifier='string'
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the Lambda function.\n\nName formats\n\nFunction name - my-function .\nFunction ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function .\nPartial ARN - 123456789012:function:my-function .\n\nThe length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.\n

    :type Qualifier: string
    :param Qualifier: [REQUIRED]\nThe version number or alias name.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'RequestedProvisionedConcurrentExecutions': 123,
    'AvailableProvisionedConcurrentExecutions': 123,
    'AllocatedProvisionedConcurrentExecutions': 123,
    'Status': 'IN_PROGRESS'|'READY'|'FAILED',
    'StatusReason': 'string',
    'LastModified': 'string'
}


Response Structure

(dict) --

RequestedProvisionedConcurrentExecutions (integer) --
The amount of provisioned concurrency requested.

AvailableProvisionedConcurrentExecutions (integer) --
The amount of provisioned concurrency available.

AllocatedProvisionedConcurrentExecutions (integer) --
The amount of provisioned concurrency allocated.

Status (string) --
The status of the allocation process.

StatusReason (string) --
For failed allocations, the reason that provisioned concurrency could not be allocated.

LastModified (string) --
The date and time that a user last updated the configuration, in ISO 8601 format .







Exceptions

Lambda.Client.exceptions.InvalidParameterValueException
Lambda.Client.exceptions.ResourceNotFoundException
Lambda.Client.exceptions.TooManyRequestsException
Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.ProvisionedConcurrencyConfigNotFoundException

Examples
The following example returns details for the provisioned concurrency configuration for the BLUE alias of the specified function.
response = client.get_provisioned_concurrency_config(
    FunctionName='my-function',
    Qualifier='BLUE',
)

print(response)


Expected Output:
{
    'AllocatedProvisionedConcurrentExecutions': 100,
    'AvailableProvisionedConcurrentExecutions': 100,
    'LastModified': '2019-12-31T20:28:49+0000',
    'RequestedProvisionedConcurrentExecutions': 100,
    'Status': 'READY',
    'ResponseMetadata': {
        '...': '...',
    },
}


The following example displays details for the provisioned concurrency configuration for the BLUE alias of the specified function.
response = client.get_provisioned_concurrency_config(
    FunctionName='my-function',
    Qualifier='BLUE',
)

print(response)


Expected Output:
{
    'AllocatedProvisionedConcurrentExecutions': 100,
    'AvailableProvisionedConcurrentExecutions': 100,
    'LastModified': '2019-12-31T20:28:49+0000',
    'RequestedProvisionedConcurrentExecutions': 100,
    'Status': 'READY',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'RequestedProvisionedConcurrentExecutions': 123,
        'AvailableProvisionedConcurrentExecutions': 123,
        'AllocatedProvisionedConcurrentExecutions': 123,
        'Status': 'IN_PROGRESS'|'READY'|'FAILED',
        'StatusReason': 'string',
        'LastModified': 'string'
    }
    
    
    :returns: 
    Lambda.Client.exceptions.InvalidParameterValueException
    Lambda.Client.exceptions.ResourceNotFoundException
    Lambda.Client.exceptions.TooManyRequestsException
    Lambda.Client.exceptions.ServiceException
    Lambda.Client.exceptions.ProvisionedConcurrencyConfigNotFoundException
    
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

def invoke(FunctionName=None, InvocationType=None, LogType=None, ClientContext=None, Payload=None, Qualifier=None):
    """
    Invokes a Lambda function. You can invoke a function synchronously (and wait for the response), or asynchronously. To invoke a function asynchronously, set InvocationType to Event .
    For synchronous invocation , details about the function response, including errors, are included in the response body and headers. For either invocation type, you can find more information in the execution log and trace .
    When an error occurs, your function may be invoked multiple times. Retry behavior varies by error type, client, event source, and invocation type. For example, if you invoke a function asynchronously and it returns an error, Lambda executes the function up to two more times. For more information, see Retry Behavior .
    For asynchronous invocation , Lambda adds events to a queue before sending them to your function. If your function does not have enough capacity to keep up with the queue, events may be lost. Occasionally, your function may receive the same event multiple times, even if no error occurs. To retain events that were not processed, configure your function with a dead-letter queue .
    The status code in the API response doesn\'t reflect function errors. Error codes are reserved for errors that prevent your function from executing, such as permissions errors, limit errors , or issues with your function\'s code and configuration. For example, Lambda returns TooManyRequestsException if executing the function would cause you to exceed a concurrency limit at either the account level (ConcurrentInvocationLimitExceeded ) or function level (ReservedFunctionConcurrentInvocationLimitExceeded ).
    For functions with a long timeout, your client might be disconnected during synchronous invocation while it waits for a response. Configure your HTTP client, SDK, firewall, proxy, or operating system to allow for long connections with timeout or keep-alive settings.
    This operation requires permission for the lambda:InvokeFunction action.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example invokes version 1 of a function named my-function with an empty event payload.
    Expected Output:
    The following example invokes version 1 of a function named my-function asynchronously.
    Expected Output:
    
    :example: response = client.invoke(
        FunctionName='string',
        InvocationType='Event'|'RequestResponse'|'DryRun',
        LogType='None'|'Tail',
        ClientContext='string',
        Payload=b'bytes'|file,
        Qualifier='string'
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the Lambda function, version, or alias.\n\nName formats\n\nFunction name - my-function (name-only), my-function:v1 (with alias).\nFunction ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function .\nPartial ARN - 123456789012:function:my-function .\n\nYou can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.\n

    :type InvocationType: string
    :param InvocationType: Choose from the following options.\n\nRequestResponse (default) - Invoke the function synchronously. Keep the connection open until the function returns a response or times out. The API response includes the function response and additional data.\nEvent - Invoke the function asynchronously. Send events that fail multiple times to the function\'s dead-letter queue (if it\'s configured). The API response only includes a status code.\nDryRun - Validate parameter values and verify that the user or role has permission to invoke the function.\n\n

    :type LogType: string
    :param LogType: Set to Tail to include the execution log in the response.

    :type ClientContext: string
    :param ClientContext: Up to 3583 bytes of base64-encoded data about the invoking client to pass to the function in the context object.

    :type Payload: bytes or seekable file-like object
    :param Payload: The JSON that you want to provide to your Lambda function as input.

    :type Qualifier: string
    :param Qualifier: Specify a version or alias to invoke a published version of the function.

    :rtype: dict

ReturnsResponse Syntax
{
    'StatusCode': 123,
    'FunctionError': 'string',
    'LogResult': 'string',
    'Payload': StreamingBody(),
    'ExecutedVersion': 'string'
}


Response Structure

(dict) --

StatusCode (integer) --
The HTTP status code is in the 200 range for a successful request. For the RequestResponse invocation type, this status code is 200. For the Event invocation type, this status code is 202. For the DryRun invocation type, the status code is 204.

FunctionError (string) --
If present, indicates that an error occurred during function execution. Details about the error are included in the response payload.

LogResult (string) --
The last 4 KB of the execution log, which is base64 encoded.

Payload (StreamingBody) --
The response from the function, or an error object.

ExecutedVersion (string) --
The version of the function that executed. When you invoke a function with an alias, this indicates which version the alias resolved to.







Exceptions

Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.ResourceNotFoundException
Lambda.Client.exceptions.InvalidRequestContentException
Lambda.Client.exceptions.RequestTooLargeException
Lambda.Client.exceptions.UnsupportedMediaTypeException
Lambda.Client.exceptions.TooManyRequestsException
Lambda.Client.exceptions.InvalidParameterValueException
Lambda.Client.exceptions.EC2UnexpectedException
Lambda.Client.exceptions.SubnetIPAddressLimitReachedException
Lambda.Client.exceptions.ENILimitReachedException
Lambda.Client.exceptions.EC2ThrottledException
Lambda.Client.exceptions.EC2AccessDeniedException
Lambda.Client.exceptions.InvalidSubnetIDException
Lambda.Client.exceptions.InvalidSecurityGroupIDException
Lambda.Client.exceptions.InvalidZipFileException
Lambda.Client.exceptions.KMSDisabledException
Lambda.Client.exceptions.KMSInvalidStateException
Lambda.Client.exceptions.KMSAccessDeniedException
Lambda.Client.exceptions.KMSNotFoundException
Lambda.Client.exceptions.InvalidRuntimeException
Lambda.Client.exceptions.ResourceConflictException
Lambda.Client.exceptions.ResourceNotReadyException

Examples
The following example invokes version 1 of a function named my-function with an empty event payload.
response = client.invoke(
    FunctionName='my-function',
    Payload='{}',
    Qualifier='1',
)

print(response)


Expected Output:
{
    'Payload': '200 SUCCESS',
    'StatusCode': 200,
    'ResponseMetadata': {
        '...': '...',
    },
}


The following example invokes version 1 of a function named my-function asynchronously.
response = client.invoke(
    FunctionName='my-function',
    InvocationType='Event',
    Payload='{}',
    Qualifier='1',
)

print(response)


Expected Output:
{
    'Payload': '',
    'StatusCode': 202,
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'StatusCode': 123,
        'FunctionError': 'string',
        'LogResult': 'string',
        'Payload': StreamingBody(),
        'ExecutedVersion': 'string'
    }
    
    
    :returns: 
    Lambda.Client.exceptions.ServiceException
    Lambda.Client.exceptions.ResourceNotFoundException
    Lambda.Client.exceptions.InvalidRequestContentException
    Lambda.Client.exceptions.RequestTooLargeException
    Lambda.Client.exceptions.UnsupportedMediaTypeException
    Lambda.Client.exceptions.TooManyRequestsException
    Lambda.Client.exceptions.InvalidParameterValueException
    Lambda.Client.exceptions.EC2UnexpectedException
    Lambda.Client.exceptions.SubnetIPAddressLimitReachedException
    Lambda.Client.exceptions.ENILimitReachedException
    Lambda.Client.exceptions.EC2ThrottledException
    Lambda.Client.exceptions.EC2AccessDeniedException
    Lambda.Client.exceptions.InvalidSubnetIDException
    Lambda.Client.exceptions.InvalidSecurityGroupIDException
    Lambda.Client.exceptions.InvalidZipFileException
    Lambda.Client.exceptions.KMSDisabledException
    Lambda.Client.exceptions.KMSInvalidStateException
    Lambda.Client.exceptions.KMSAccessDeniedException
    Lambda.Client.exceptions.KMSNotFoundException
    Lambda.Client.exceptions.InvalidRuntimeException
    Lambda.Client.exceptions.ResourceConflictException
    Lambda.Client.exceptions.ResourceNotReadyException
    
    """
    pass

def invoke_async(FunctionName=None, InvokeArgs=None):
    """
    Invokes a function asynchronously.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example invokes a Lambda function asynchronously
    Expected Output:
    
    :example: response = client.invoke_async(
        FunctionName='string',
        InvokeArgs=b'bytes'|file
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the Lambda function.\n\nName formats\n\nFunction name - my-function .\nFunction ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function .\nPartial ARN - 123456789012:function:my-function .\n\nThe length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.\n

    :type InvokeArgs: bytes or seekable file-like object
    :param InvokeArgs: [REQUIRED]\nThe JSON that you want to provide to your Lambda function as input.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Status': 123
}


Response Structure

(dict) --
A success response (202 Accepted ) indicates that the request is queued for invocation.

Status (integer) --
The status code.







Exceptions

Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.ResourceNotFoundException
Lambda.Client.exceptions.InvalidRequestContentException
Lambda.Client.exceptions.InvalidRuntimeException
Lambda.Client.exceptions.ResourceConflictException

Examples
The following example invokes a Lambda function asynchronously
response = client.invoke_async(
    FunctionName='my-function',
    InvokeArgs='{}',
)

print(response)


Expected Output:
{
    'Status': 202,
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Status': 123
    }
    
    
    :returns: 
    Lambda.Client.exceptions.ServiceException
    Lambda.Client.exceptions.ResourceNotFoundException
    Lambda.Client.exceptions.InvalidRequestContentException
    Lambda.Client.exceptions.InvalidRuntimeException
    Lambda.Client.exceptions.ResourceConflictException
    
    """
    pass

def list_aliases(FunctionName=None, FunctionVersion=None, Marker=None, MaxItems=None):
    """
    Returns a list of aliases for a Lambda function.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns a list of aliases for a function named my-function.
    Expected Output:
    
    :example: response = client.list_aliases(
        FunctionName='string',
        FunctionVersion='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the Lambda function.\n\nName formats\n\nFunction name - MyFunction .\nFunction ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .\nPartial ARN - 123456789012:function:MyFunction .\n\nThe length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.\n

    :type FunctionVersion: string
    :param FunctionVersion: Specify a function version to only list aliases that invoke that version.

    :type Marker: string
    :param Marker: Specify the pagination token that\'s returned by a previous request to retrieve the next page of results.

    :type MaxItems: integer
    :param MaxItems: Limit the number of aliases returned.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextMarker': 'string',
    'Aliases': [
        {
            'AliasArn': 'string',
            'Name': 'string',
            'FunctionVersion': 'string',
            'Description': 'string',
            'RoutingConfig': {
                'AdditionalVersionWeights': {
                    'string': 123.0
                }
            },
            'RevisionId': 'string'
        },
    ]
}


Response Structure

(dict) --

NextMarker (string) --
The pagination token that\'s included if more results are available.

Aliases (list) --
A list of aliases.

(dict) --
Provides configuration information about a Lambda function alias .

AliasArn (string) --
The Amazon Resource Name (ARN) of the alias.

Name (string) --
The name of the alias.

FunctionVersion (string) --
The function version that the alias invokes.

Description (string) --
A description of the alias.

RoutingConfig (dict) --
The routing configuration of the alias.

AdditionalVersionWeights (dict) --
The name of the second alias, and the percentage of traffic that\'s routed to it.

(string) --
(float) --






RevisionId (string) --
A unique identifier that changes when you update the alias.











Exceptions

Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.ResourceNotFoundException
Lambda.Client.exceptions.InvalidParameterValueException
Lambda.Client.exceptions.TooManyRequestsException

Examples
The following example returns a list of aliases for a function named my-function.
response = client.list_aliases(
    FunctionName='my-function',
)

print(response)


Expected Output:
{
    'Aliases': [
        {
            'AliasArn': 'arn:aws:lambda:us-west-2:123456789012:function:my-function:BETA',
            'Description': 'Production environment BLUE.',
            'FunctionVersion': '2',
            'Name': 'BLUE',
            'RevisionId': 'a410117f-xmpl-494e-8035-7e204bb7933b',
            'RoutingConfig': {
                'AdditionalVersionWeights': {
                    '1': 0.7,
                },
            },
        },
        {
            'AliasArn': 'arn:aws:lambda:us-west-2:123456789012:function:my-function:LIVE',
            'Description': 'Production environment GREEN.',
            'FunctionVersion': '1',
            'Name': 'GREEN',
            'RevisionId': '21d40116-xmpl-40ba-9360-3ea284da1bb5',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'NextMarker': 'string',
        'Aliases': [
            {
                'AliasArn': 'string',
                'Name': 'string',
                'FunctionVersion': 'string',
                'Description': 'string',
                'RoutingConfig': {
                    'AdditionalVersionWeights': {
                        'string': 123.0
                    }
                },
                'RevisionId': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    (float) --
    
    
    
    """
    pass

def list_event_source_mappings(EventSourceArn=None, FunctionName=None, Marker=None, MaxItems=None):
    """
    Lists event source mappings. Specify an EventSourceArn to only show event source mappings for a single event source.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns a list of the event source mappings for a function named my-function.
    Expected Output:
    
    :example: response = client.list_event_source_mappings(
        EventSourceArn='string',
        FunctionName='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type EventSourceArn: string
    :param EventSourceArn: The Amazon Resource Name (ARN) of the event source.\n\nAmazon Kinesis - The ARN of the data stream or a stream consumer.\nAmazon DynamoDB Streams - The ARN of the stream.\nAmazon Simple Queue Service - The ARN of the queue.\n\n

    :type FunctionName: string
    :param FunctionName: The name of the Lambda function.\n\nName formats\n\nFunction name - MyFunction .\nFunction ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .\nVersion or Alias ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD .\nPartial ARN - 123456789012:function:MyFunction .\n\nThe length constraint applies only to the full ARN. If you specify only the function name, it\'s limited to 64 characters in length.\n

    :type Marker: string
    :param Marker: A pagination token returned by a previous call.

    :type MaxItems: integer
    :param MaxItems: The maximum number of event source mappings to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextMarker': 'string',
    'EventSourceMappings': [
        {
            'UUID': 'string',
            'BatchSize': 123,
            'MaximumBatchingWindowInSeconds': 123,
            'ParallelizationFactor': 123,
            'EventSourceArn': 'string',
            'FunctionArn': 'string',
            'LastModified': datetime(2015, 1, 1),
            'LastProcessingResult': 'string',
            'State': 'string',
            'StateTransitionReason': 'string',
            'DestinationConfig': {
                'OnSuccess': {
                    'Destination': 'string'
                },
                'OnFailure': {
                    'Destination': 'string'
                }
            },
            'MaximumRecordAgeInSeconds': 123,
            'BisectBatchOnFunctionError': True|False,
            'MaximumRetryAttempts': 123
        },
    ]
}


Response Structure

(dict) --

NextMarker (string) --
A pagination token that\'s returned when the response doesn\'t contain all event source mappings.

EventSourceMappings (list) --
A list of event source mappings.

(dict) --
A mapping between an AWS resource and an AWS Lambda function. See  CreateEventSourceMapping for details.

UUID (string) --
The identifier of the event source mapping.

BatchSize (integer) --
The maximum number of items to retrieve in a single batch.

MaximumBatchingWindowInSeconds (integer) --
(Streams) The maximum amount of time to gather records before invoking the function, in seconds.

ParallelizationFactor (integer) --
(Streams) The number of batches to process from each shard concurrently.

EventSourceArn (string) --
The Amazon Resource Name (ARN) of the event source.

FunctionArn (string) --
The ARN of the Lambda function.

LastModified (datetime) --
The date that the event source mapping was last updated, or its state changed.

LastProcessingResult (string) --
The result of the last AWS Lambda invocation of your Lambda function.

State (string) --
The state of the event source mapping. It can be one of the following: Creating , Enabling , Enabled , Disabling , Disabled , Updating , or Deleting .

StateTransitionReason (string) --
Indicates whether the last change to the event source mapping was made by a user, or by the Lambda service.

DestinationConfig (dict) --
(Streams) An Amazon SQS queue or Amazon SNS topic destination for discarded records.

OnSuccess (dict) --
The destination configuration for successful invocations.

Destination (string) --
The Amazon Resource Name (ARN) of the destination resource.



OnFailure (dict) --
The destination configuration for failed invocations.

Destination (string) --
The Amazon Resource Name (ARN) of the destination resource.





MaximumRecordAgeInSeconds (integer) --
(Streams) The maximum age of a record that Lambda sends to a function for processing.

BisectBatchOnFunctionError (boolean) --
(Streams) If the function returns an error, split the batch in two and retry.

MaximumRetryAttempts (integer) --
(Streams) The maximum number of times to retry when the function returns an error.











Exceptions

Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.ResourceNotFoundException
Lambda.Client.exceptions.InvalidParameterValueException
Lambda.Client.exceptions.TooManyRequestsException

Examples
The following example returns a list of the event source mappings for a function named my-function.
response = client.list_event_source_mappings(
    FunctionName='my-function',
)

print(response)


Expected Output:
{
    'EventSourceMappings': [
        {
            'BatchSize': 5,
            'EventSourceArn': 'arn:aws:sqs:us-west-2:123456789012:mySQSqueue',
            'FunctionArn': 'arn:aws:lambda:us-west-2:123456789012:function:my-function',
            'LastModified': 1569284520.333,
            'State': 'Enabled',
            'StateTransitionReason': 'USER_INITIATED',
            'UUID': 'a1b2c3d4-5678-90ab-cdef-11111EXAMPLE',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'NextMarker': 'string',
        'EventSourceMappings': [
            {
                'UUID': 'string',
                'BatchSize': 123,
                'MaximumBatchingWindowInSeconds': 123,
                'ParallelizationFactor': 123,
                'EventSourceArn': 'string',
                'FunctionArn': 'string',
                'LastModified': datetime(2015, 1, 1),
                'LastProcessingResult': 'string',
                'State': 'string',
                'StateTransitionReason': 'string',
                'DestinationConfig': {
                    'OnSuccess': {
                        'Destination': 'string'
                    },
                    'OnFailure': {
                        'Destination': 'string'
                    }
                },
                'MaximumRecordAgeInSeconds': 123,
                'BisectBatchOnFunctionError': True|False,
                'MaximumRetryAttempts': 123
            },
        ]
    }
    
    
    :returns: 
    Lambda.Client.exceptions.ServiceException
    Lambda.Client.exceptions.ResourceNotFoundException
    Lambda.Client.exceptions.InvalidParameterValueException
    Lambda.Client.exceptions.TooManyRequestsException
    
    """
    pass

def list_function_event_invoke_configs(FunctionName=None, Marker=None, MaxItems=None):
    """
    Retrieves a list of configurations for asynchronous invocation for a function.
    To configure options for asynchronous invocation, use  PutFunctionEventInvokeConfig .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns a list of asynchronous invocation configurations for a function named my-function.
    Expected Output:
    
    :example: response = client.list_function_event_invoke_configs(
        FunctionName='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the Lambda function.\n\nName formats\n\nFunction name - my-function .\nFunction ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function .\nPartial ARN - 123456789012:function:my-function .\n\nThe length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.\n

    :type Marker: string
    :param Marker: Specify the pagination token that\'s returned by a previous request to retrieve the next page of results.

    :type MaxItems: integer
    :param MaxItems: The maximum number of configurations to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'FunctionEventInvokeConfigs': [
        {
            'LastModified': datetime(2015, 1, 1),
            'FunctionArn': 'string',
            'MaximumRetryAttempts': 123,
            'MaximumEventAgeInSeconds': 123,
            'DestinationConfig': {
                'OnSuccess': {
                    'Destination': 'string'
                },
                'OnFailure': {
                    'Destination': 'string'
                }
            }
        },
    ],
    'NextMarker': 'string'
}


Response Structure

(dict) --

FunctionEventInvokeConfigs (list) --
A list of configurations.

(dict) --

LastModified (datetime) --
The date and time that the configuration was last updated.

FunctionArn (string) --
The Amazon Resource Name (ARN) of the function.

MaximumRetryAttempts (integer) --
The maximum number of times to retry when the function returns an error.

MaximumEventAgeInSeconds (integer) --
The maximum age of a request that Lambda sends to a function for processing.

DestinationConfig (dict) --
A destination for events after they have been sent to a function for processing.

Destinations


Function - The Amazon Resource Name (ARN) of a Lambda function.
Queue - The ARN of an SQS queue.
Topic - The ARN of an SNS topic.
Event Bus - The ARN of an Amazon EventBridge event bus.


OnSuccess (dict) --
The destination configuration for successful invocations.

Destination (string) --
The Amazon Resource Name (ARN) of the destination resource.



OnFailure (dict) --
The destination configuration for failed invocations.

Destination (string) --
The Amazon Resource Name (ARN) of the destination resource.









NextMarker (string) --
The pagination token that\'s included if more results are available.







Exceptions

Lambda.Client.exceptions.InvalidParameterValueException
Lambda.Client.exceptions.ResourceNotFoundException
Lambda.Client.exceptions.TooManyRequestsException
Lambda.Client.exceptions.ServiceException

Examples
The following example returns a list of asynchronous invocation configurations for a function named my-function.
response = client.list_function_event_invoke_configs(
    FunctionName='my-function',
)

print(response)


Expected Output:
{
    'FunctionEventInvokeConfigs': [
        {
            'FunctionArn': 'arn:aws:lambda:us-east-2:123456789012:function:my-function:GREEN',
            'LastModified': 1577824406.719,
            'MaximumEventAgeInSeconds': 1800,
            'MaximumRetryAttempts': 2,
        },
        {
            'FunctionArn': 'arn:aws:lambda:us-east-2:123456789012:function:my-function:BLUE',
            'LastModified': 1577824396.653,
            'MaximumEventAgeInSeconds': 3600,
            'MaximumRetryAttempts': 0,
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'FunctionEventInvokeConfigs': [
            {
                'LastModified': datetime(2015, 1, 1),
                'FunctionArn': 'string',
                'MaximumRetryAttempts': 123,
                'MaximumEventAgeInSeconds': 123,
                'DestinationConfig': {
                    'OnSuccess': {
                        'Destination': 'string'
                    },
                    'OnFailure': {
                        'Destination': 'string'
                    }
                }
            },
        ],
        'NextMarker': 'string'
    }
    
    
    :returns: 
    Function - The Amazon Resource Name (ARN) of a Lambda function.
    Queue - The ARN of an SQS queue.
    Topic - The ARN of an SNS topic.
    Event Bus - The ARN of an Amazon EventBridge event bus.
    
    """
    pass

def list_functions(MasterRegion=None, FunctionVersion=None, Marker=None, MaxItems=None):
    """
    Returns a list of Lambda functions, with the version-specific configuration of each. Lambda returns up to 50 functions per call.
    Set FunctionVersion to ALL to include all published versions of each function in addition to the unpublished version. To get more information about a function or version, use  GetFunction .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This operation returns a list of Lambda functions.
    Expected Output:
    
    :example: response = client.list_functions(
        MasterRegion='string',
        FunctionVersion='ALL',
        Marker='string',
        MaxItems=123
    )
    
    
    :type MasterRegion: string
    :param MasterRegion: For Lambda@Edge functions, the AWS Region of the master function. For example, us-east-1 filters the list of functions to only include Lambda@Edge functions replicated from a master function in US East (N. Virginia). If specified, you must set FunctionVersion to ALL .

    :type FunctionVersion: string
    :param FunctionVersion: Set to ALL to include entries for all published versions of each function.

    :type Marker: string
    :param Marker: Specify the pagination token that\'s returned by a previous request to retrieve the next page of results.

    :type MaxItems: integer
    :param MaxItems: The maximum number of functions to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextMarker': 'string',
    'Functions': [
        {
            'FunctionName': 'string',
            'FunctionArn': 'string',
            'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'dotnetcore3.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'ruby2.7'|'provided',
            'Role': 'string',
            'Handler': 'string',
            'CodeSize': 123,
            'Description': 'string',
            'Timeout': 123,
            'MemorySize': 123,
            'LastModified': 'string',
            'CodeSha256': 'string',
            'Version': 'string',
            'VpcConfig': {
                'SubnetIds': [
                    'string',
                ],
                'SecurityGroupIds': [
                    'string',
                ],
                'VpcId': 'string'
            },
            'DeadLetterConfig': {
                'TargetArn': 'string'
            },
            'Environment': {
                'Variables': {
                    'string': 'string'
                },
                'Error': {
                    'ErrorCode': 'string',
                    'Message': 'string'
                }
            },
            'KMSKeyArn': 'string',
            'TracingConfig': {
                'Mode': 'Active'|'PassThrough'
            },
            'MasterArn': 'string',
            'RevisionId': 'string',
            'Layers': [
                {
                    'Arn': 'string',
                    'CodeSize': 123
                },
            ],
            'State': 'Pending'|'Active'|'Inactive'|'Failed',
            'StateReason': 'string',
            'StateReasonCode': 'Idle'|'Creating'|'Restoring'|'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'|'SubnetOutOfIPAddresses'|'InvalidSubnet'|'InvalidSecurityGroup',
            'LastUpdateStatus': 'Successful'|'Failed'|'InProgress',
            'LastUpdateStatusReason': 'string',
            'LastUpdateStatusReasonCode': 'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'|'SubnetOutOfIPAddresses'|'InvalidSubnet'|'InvalidSecurityGroup'
        },
    ]
}


Response Structure

(dict) --
A list of Lambda functions.

NextMarker (string) --
The pagination token that\'s included if more results are available.

Functions (list) --
A list of Lambda functions.

(dict) --
Details about a function\'s configuration.

FunctionName (string) --
The name of the function.

FunctionArn (string) --
The function\'s Amazon Resource Name (ARN).

Runtime (string) --
The runtime environment for the Lambda function.

Role (string) --
The function\'s execution role.

Handler (string) --
The function that Lambda calls to begin executing your function.

CodeSize (integer) --
The size of the function\'s deployment package, in bytes.

Description (string) --
The function\'s description.

Timeout (integer) --
The amount of time in seconds that Lambda allows a function to run before stopping it.

MemorySize (integer) --
The memory that\'s allocated to the function.

LastModified (string) --
The date and time that the function was last updated, in ISO-8601 format (YYYY-MM-DDThh:mm:ss.sTZD).

CodeSha256 (string) --
The SHA256 hash of the function\'s deployment package.

Version (string) --
The version of the Lambda function.

VpcConfig (dict) --
The function\'s networking configuration.

SubnetIds (list) --
A list of VPC subnet IDs.

(string) --


SecurityGroupIds (list) --
A list of VPC security groups IDs.

(string) --


VpcId (string) --
The ID of the VPC.



DeadLetterConfig (dict) --
The function\'s dead letter queue.

TargetArn (string) --
The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.



Environment (dict) --
The function\'s environment variables.

Variables (dict) --
Environment variable key-value pairs.

(string) --
(string) --




Error (dict) --
Error messages for environment variables that couldn\'t be applied.

ErrorCode (string) --
The error code.

Message (string) --
The error message.





KMSKeyArn (string) --
The KMS key that\'s used to encrypt the function\'s environment variables. This key is only returned if you\'ve configured a customer managed CMK.

TracingConfig (dict) --
The function\'s AWS X-Ray tracing configuration.

Mode (string) --
The tracing mode.



MasterArn (string) --
For Lambda@Edge functions, the ARN of the master function.

RevisionId (string) --
The latest updated revision of the function or alias.

Layers (list) --
The function\'s layers .

(dict) --
An AWS Lambda layer .

Arn (string) --
The Amazon Resource Name (ARN) of the function layer.

CodeSize (integer) --
The size of the layer archive in bytes.





State (string) --
The current state of the function. When the state is Inactive , you can reactivate the function by invoking it.

StateReason (string) --
The reason for the function\'s current state.

StateReasonCode (string) --
The reason code for the function\'s current state. When the code is Creating , you can\'t invoke or modify the function.

LastUpdateStatus (string) --
The status of the last update that was performed on the function. This is first set to Successful after function creation completes.

LastUpdateStatusReason (string) --
The reason for the last update that was performed on the function.

LastUpdateStatusReasonCode (string) --
The reason code for the last update that was performed on the function.











Exceptions

Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.TooManyRequestsException
Lambda.Client.exceptions.InvalidParameterValueException

Examples
This operation returns a list of Lambda functions.
response = client.list_functions(
)

print(response)


Expected Output:
{
    'Functions': [
        {
            'CodeSha256': 'dBG9m8SGdmlEjw/JYXlhhvCrAv5TxvXsbL/RMr0fT/I=',
            'CodeSize': 294,
            'Description': '',
            'FunctionArn': 'arn:aws:lambda:us-west-2:123456789012:function:helloworld',
            'FunctionName': 'helloworld',
            'Handler': 'helloworld.handler',
            'LastModified': '2019-09-23T18:32:33.857+0000',
            'MemorySize': 128,
            'RevisionId': '1718e831-badf-4253-9518-d0644210af7b',
            'Role': 'arn:aws:iam::123456789012:role/service-role/MyTestFunction-role-zgur6bf4',
            'Runtime': 'nodejs10.x',
            'Timeout': 3,
            'TracingConfig': {
                'Mode': 'PassThrough',
            },
            'Version': '$LATEST',
        },
        {
            'CodeSha256': 'sU0cJ2/hOZevwV/lTxCuQqK3gDZP3i8gUoqUUVRmY6E=',
            'CodeSize': 266,
            'Description': '',
            'FunctionArn': 'arn:aws:lambda:us-west-2:123456789012:function:my-function',
            'FunctionName': 'my-function',
            'Handler': 'index.handler',
            'LastModified': '2019-10-01T16:47:28.490+0000',
            'MemorySize': 256,
            'RevisionId': '93017fc9-59cb-41dc-901b-4845ce4bf668',
            'Role': 'arn:aws:iam::123456789012:role/service-role/helloWorldPython-role-uy3l9qyq',
            'Runtime': 'nodejs10.x',
            'Timeout': 3,
            'TracingConfig': {
                'Mode': 'PassThrough',
            },
            'Version': '$LATEST',
            'VpcConfig': {
                'SecurityGroupIds': [
                ],
                'SubnetIds': [
                ],
                'VpcId': '',
            },
        },
    ],
    'NextMarker': '',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'NextMarker': 'string',
        'Functions': [
            {
                'FunctionName': 'string',
                'FunctionArn': 'string',
                'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'dotnetcore3.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'ruby2.7'|'provided',
                'Role': 'string',
                'Handler': 'string',
                'CodeSize': 123,
                'Description': 'string',
                'Timeout': 123,
                'MemorySize': 123,
                'LastModified': 'string',
                'CodeSha256': 'string',
                'Version': 'string',
                'VpcConfig': {
                    'SubnetIds': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ],
                    'VpcId': 'string'
                },
                'DeadLetterConfig': {
                    'TargetArn': 'string'
                },
                'Environment': {
                    'Variables': {
                        'string': 'string'
                    },
                    'Error': {
                        'ErrorCode': 'string',
                        'Message': 'string'
                    }
                },
                'KMSKeyArn': 'string',
                'TracingConfig': {
                    'Mode': 'Active'|'PassThrough'
                },
                'MasterArn': 'string',
                'RevisionId': 'string',
                'Layers': [
                    {
                        'Arn': 'string',
                        'CodeSize': 123
                    },
                ],
                'State': 'Pending'|'Active'|'Inactive'|'Failed',
                'StateReason': 'string',
                'StateReasonCode': 'Idle'|'Creating'|'Restoring'|'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'|'SubnetOutOfIPAddresses'|'InvalidSubnet'|'InvalidSecurityGroup',
                'LastUpdateStatus': 'Successful'|'Failed'|'InProgress',
                'LastUpdateStatusReason': 'string',
                'LastUpdateStatusReasonCode': 'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'|'SubnetOutOfIPAddresses'|'InvalidSubnet'|'InvalidSecurityGroup'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_layer_versions(CompatibleRuntime=None, LayerName=None, Marker=None, MaxItems=None):
    """
    Lists the versions of an AWS Lambda layer . Versions that have been deleted aren\'t listed. Specify a runtime identifier to list only versions that indicate that they\'re compatible with that runtime.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example displays information about the versions for the layer named blank-java-lib
    Expected Output:
    
    :example: response = client.list_layer_versions(
        CompatibleRuntime='nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'dotnetcore3.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'ruby2.7'|'provided',
        LayerName='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type CompatibleRuntime: string
    :param CompatibleRuntime: A runtime identifier. For example, go1.x .

    :type LayerName: string
    :param LayerName: [REQUIRED]\nThe name or Amazon Resource Name (ARN) of the layer.\n

    :type Marker: string
    :param Marker: A pagination token returned by a previous call.

    :type MaxItems: integer
    :param MaxItems: The maximum number of versions to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextMarker': 'string',
    'LayerVersions': [
        {
            'LayerVersionArn': 'string',
            'Version': 123,
            'Description': 'string',
            'CreatedDate': 'string',
            'CompatibleRuntimes': [
                'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'dotnetcore3.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'ruby2.7'|'provided',
            ],
            'LicenseInfo': 'string'
        },
    ]
}


Response Structure

(dict) --

NextMarker (string) --
A pagination token returned when the response doesn\'t contain all versions.

LayerVersions (list) --
A list of versions.

(dict) --
Details about a version of an AWS Lambda layer .

LayerVersionArn (string) --
The ARN of the layer version.

Version (integer) --
The version number.

Description (string) --
The description of the version.

CreatedDate (string) --
The date that the version was created, in ISO 8601 format. For example, 2018-11-27T15:10:45.123+0000 .

CompatibleRuntimes (list) --
The layer\'s compatible runtimes.

(string) --


LicenseInfo (string) --
The layer\'s open-source license.











Exceptions

Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.InvalidParameterValueException
Lambda.Client.exceptions.ResourceNotFoundException
Lambda.Client.exceptions.TooManyRequestsException

Examples
The following example displays information about the versions for the layer named blank-java-lib
response = client.list_layer_versions(
    LayerName='blank-java-lib',
)

print(response)


Expected Output:
{
    'LayerVersions': [
        {
            'CompatibleRuntimes': [
                'java8',
            ],
            'CreatedDate': '2020-03-18T23:38:42.284+0000',
            'Description': 'Dependencies for the blank-java sample app.',
            'LayerVersionArn': 'arn:aws:lambda:us-east-2:123456789012:layer:blank-java-lib:7',
            'Version': 7,
        },
        {
            'CompatibleRuntimes': [
                'java8',
            ],
            'CreatedDate': '2020-03-17T07:24:21.960+0000',
            'Description': 'Dependencies for the blank-java sample app.',
            'LayerVersionArn': 'arn:aws:lambda:us-east-2:123456789012:layer:blank-java-lib:6',
            'Version': 6,
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'NextMarker': 'string',
        'LayerVersions': [
            {
                'LayerVersionArn': 'string',
                'Version': 123,
                'Description': 'string',
                'CreatedDate': 'string',
                'CompatibleRuntimes': [
                    'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'dotnetcore3.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'ruby2.7'|'provided',
                ],
                'LicenseInfo': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_layers(CompatibleRuntime=None, Marker=None, MaxItems=None):
    """
    Lists AWS Lambda layers and shows information about the latest version of each. Specify a runtime identifier to list only layers that indicate that they\'re compatible with that runtime.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns information about layers that are compatible with the Python 3.7 runtime.
    Expected Output:
    
    :example: response = client.list_layers(
        CompatibleRuntime='nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'dotnetcore3.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'ruby2.7'|'provided',
        Marker='string',
        MaxItems=123
    )
    
    
    :type CompatibleRuntime: string
    :param CompatibleRuntime: A runtime identifier. For example, go1.x .

    :type Marker: string
    :param Marker: A pagination token returned by a previous call.

    :type MaxItems: integer
    :param MaxItems: The maximum number of layers to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextMarker': 'string',
    'Layers': [
        {
            'LayerName': 'string',
            'LayerArn': 'string',
            'LatestMatchingVersion': {
                'LayerVersionArn': 'string',
                'Version': 123,
                'Description': 'string',
                'CreatedDate': 'string',
                'CompatibleRuntimes': [
                    'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'dotnetcore3.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'ruby2.7'|'provided',
                ],
                'LicenseInfo': 'string'
            }
        },
    ]
}


Response Structure

(dict) --

NextMarker (string) --
A pagination token returned when the response doesn\'t contain all layers.

Layers (list) --
A list of function layers.

(dict) --
Details about an AWS Lambda layer .

LayerName (string) --
The name of the layer.

LayerArn (string) --
The Amazon Resource Name (ARN) of the function layer.

LatestMatchingVersion (dict) --
The newest version of the layer.

LayerVersionArn (string) --
The ARN of the layer version.

Version (integer) --
The version number.

Description (string) --
The description of the version.

CreatedDate (string) --
The date that the version was created, in ISO 8601 format. For example, 2018-11-27T15:10:45.123+0000 .

CompatibleRuntimes (list) --
The layer\'s compatible runtimes.

(string) --


LicenseInfo (string) --
The layer\'s open-source license.













Exceptions

Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.InvalidParameterValueException
Lambda.Client.exceptions.TooManyRequestsException

Examples
The following example returns information about layers that are compatible with the Python 3.7 runtime.
response = client.list_layers(
    CompatibleRuntime='python3.7',
)

print(response)


Expected Output:
{
    'Layers': [
        {
            'LatestMatchingVersion': {
                'CompatibleRuntimes': [
                    'python3.6',
                    'python3.7',
                ],
                'CreatedDate': '2018-11-15T00:37:46.592+0000',
                'Description': 'My layer',
                'LayerVersionArn': 'arn:aws:lambda:us-east-2:123456789012:layer:my-layer:2',
                'Version': 2,
            },
            'LayerArn': 'arn:aws:lambda:us-east-2:123456789012:layer:my-layer',
            'LayerName': 'my-layer',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'NextMarker': 'string',
        'Layers': [
            {
                'LayerName': 'string',
                'LayerArn': 'string',
                'LatestMatchingVersion': {
                    'LayerVersionArn': 'string',
                    'Version': 123,
                    'Description': 'string',
                    'CreatedDate': 'string',
                    'CompatibleRuntimes': [
                        'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'dotnetcore3.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'ruby2.7'|'provided',
                    ],
                    'LicenseInfo': 'string'
                }
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_provisioned_concurrency_configs(FunctionName=None, Marker=None, MaxItems=None):
    """
    Retrieves a list of provisioned concurrency configurations for a function.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns a list of provisioned concurrency configurations for a function named my-function.
    Expected Output:
    
    :example: response = client.list_provisioned_concurrency_configs(
        FunctionName='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the Lambda function.\n\nName formats\n\nFunction name - my-function .\nFunction ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function .\nPartial ARN - 123456789012:function:my-function .\n\nThe length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.\n

    :type Marker: string
    :param Marker: Specify the pagination token that\'s returned by a previous request to retrieve the next page of results.

    :type MaxItems: integer
    :param MaxItems: Specify a number to limit the number of configurations returned.

    :rtype: dict

ReturnsResponse Syntax
{
    'ProvisionedConcurrencyConfigs': [
        {
            'FunctionArn': 'string',
            'RequestedProvisionedConcurrentExecutions': 123,
            'AvailableProvisionedConcurrentExecutions': 123,
            'AllocatedProvisionedConcurrentExecutions': 123,
            'Status': 'IN_PROGRESS'|'READY'|'FAILED',
            'StatusReason': 'string',
            'LastModified': 'string'
        },
    ],
    'NextMarker': 'string'
}


Response Structure

(dict) --

ProvisionedConcurrencyConfigs (list) --
A list of provisioned concurrency configurations.

(dict) --
Details about the provisioned concurrency configuration for a function alias or version.

FunctionArn (string) --
The Amazon Resource Name (ARN) of the alias or version.

RequestedProvisionedConcurrentExecutions (integer) --
The amount of provisioned concurrency requested.

AvailableProvisionedConcurrentExecutions (integer) --
The amount of provisioned concurrency available.

AllocatedProvisionedConcurrentExecutions (integer) --
The amount of provisioned concurrency allocated.

Status (string) --
The status of the allocation process.

StatusReason (string) --
For failed allocations, the reason that provisioned concurrency could not be allocated.

LastModified (string) --
The date and time that a user last updated the configuration, in ISO 8601 format .





NextMarker (string) --
The pagination token that\'s included if more results are available.







Exceptions

Lambda.Client.exceptions.InvalidParameterValueException
Lambda.Client.exceptions.ResourceNotFoundException
Lambda.Client.exceptions.TooManyRequestsException
Lambda.Client.exceptions.ServiceException

Examples
The following example returns a list of provisioned concurrency configurations for a function named my-function.
response = client.list_provisioned_concurrency_configs(
    FunctionName='my-function',
)

print(response)


Expected Output:
{
    'ProvisionedConcurrencyConfigs': [
        {
            'AllocatedProvisionedConcurrentExecutions': 100,
            'AvailableProvisionedConcurrentExecutions': 100,
            'FunctionArn': 'arn:aws:lambda:us-east-2:123456789012:function:my-function:GREEN',
            'LastModified': '2019-12-31T20:29:00+0000',
            'RequestedProvisionedConcurrentExecutions': 100,
            'Status': 'READY',
        },
        {
            'AllocatedProvisionedConcurrentExecutions': 100,
            'AvailableProvisionedConcurrentExecutions': 100,
            'FunctionArn': 'arn:aws:lambda:us-east-2:123456789012:function:my-function:BLUE',
            'LastModified': '2019-12-31T20:28:49+0000',
            'RequestedProvisionedConcurrentExecutions': 100,
            'Status': 'READY',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ProvisionedConcurrencyConfigs': [
            {
                'FunctionArn': 'string',
                'RequestedProvisionedConcurrentExecutions': 123,
                'AvailableProvisionedConcurrentExecutions': 123,
                'AllocatedProvisionedConcurrentExecutions': 123,
                'Status': 'IN_PROGRESS'|'READY'|'FAILED',
                'StatusReason': 'string',
                'LastModified': 'string'
            },
        ],
        'NextMarker': 'string'
    }
    
    
    :returns: 
    Lambda.Client.exceptions.InvalidParameterValueException
    Lambda.Client.exceptions.ResourceNotFoundException
    Lambda.Client.exceptions.TooManyRequestsException
    Lambda.Client.exceptions.ServiceException
    
    """
    pass

def list_tags(Resource=None):
    """
    Returns a function\'s tags . You can also view tags with  GetFunction .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example displays the tags attached to the my-function Lambda function.
    Expected Output:
    
    :example: response = client.list_tags(
        Resource='string'
    )
    
    
    :type Resource: string
    :param Resource: [REQUIRED]\nThe function\'s Amazon Resource Name (ARN).\n

    :rtype: dict
ReturnsResponse Syntax{
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
Tags (dict) --The function\'s tags.

(string) --
(string) --









Exceptions

Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.ResourceNotFoundException
Lambda.Client.exceptions.InvalidParameterValueException
Lambda.Client.exceptions.TooManyRequestsException

Examples
The following example displays the tags attached to the my-function Lambda function.
response = client.list_tags(
    Resource='arn:aws:lambda:us-west-2:123456789012:function:my-function',
)

print(response)


Expected Output:
{
    'Tags': {
        'Category': 'Web Tools',
        'Department': 'Sales',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    Lambda.Client.exceptions.ServiceException
    Lambda.Client.exceptions.ResourceNotFoundException
    Lambda.Client.exceptions.InvalidParameterValueException
    Lambda.Client.exceptions.TooManyRequestsException
    
    """
    pass

def list_versions_by_function(FunctionName=None, Marker=None, MaxItems=None):
    """
    Returns a list of versions , with the version-specific configuration of each. Lambda returns up to 50 versions per call.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns a list of versions of a function named my-function
    Expected Output:
    
    :example: response = client.list_versions_by_function(
        FunctionName='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the Lambda function.\n\nName formats\n\nFunction name - MyFunction .\nFunction ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .\nPartial ARN - 123456789012:function:MyFunction .\n\nThe length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.\n

    :type Marker: string
    :param Marker: Specify the pagination token that\'s returned by a previous request to retrieve the next page of results.

    :type MaxItems: integer
    :param MaxItems: The maximum number of versions to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextMarker': 'string',
    'Versions': [
        {
            'FunctionName': 'string',
            'FunctionArn': 'string',
            'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'dotnetcore3.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'ruby2.7'|'provided',
            'Role': 'string',
            'Handler': 'string',
            'CodeSize': 123,
            'Description': 'string',
            'Timeout': 123,
            'MemorySize': 123,
            'LastModified': 'string',
            'CodeSha256': 'string',
            'Version': 'string',
            'VpcConfig': {
                'SubnetIds': [
                    'string',
                ],
                'SecurityGroupIds': [
                    'string',
                ],
                'VpcId': 'string'
            },
            'DeadLetterConfig': {
                'TargetArn': 'string'
            },
            'Environment': {
                'Variables': {
                    'string': 'string'
                },
                'Error': {
                    'ErrorCode': 'string',
                    'Message': 'string'
                }
            },
            'KMSKeyArn': 'string',
            'TracingConfig': {
                'Mode': 'Active'|'PassThrough'
            },
            'MasterArn': 'string',
            'RevisionId': 'string',
            'Layers': [
                {
                    'Arn': 'string',
                    'CodeSize': 123
                },
            ],
            'State': 'Pending'|'Active'|'Inactive'|'Failed',
            'StateReason': 'string',
            'StateReasonCode': 'Idle'|'Creating'|'Restoring'|'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'|'SubnetOutOfIPAddresses'|'InvalidSubnet'|'InvalidSecurityGroup',
            'LastUpdateStatus': 'Successful'|'Failed'|'InProgress',
            'LastUpdateStatusReason': 'string',
            'LastUpdateStatusReasonCode': 'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'|'SubnetOutOfIPAddresses'|'InvalidSubnet'|'InvalidSecurityGroup'
        },
    ]
}


Response Structure

(dict) --

NextMarker (string) --
The pagination token that\'s included if more results are available.

Versions (list) --
A list of Lambda function versions.

(dict) --
Details about a function\'s configuration.

FunctionName (string) --
The name of the function.

FunctionArn (string) --
The function\'s Amazon Resource Name (ARN).

Runtime (string) --
The runtime environment for the Lambda function.

Role (string) --
The function\'s execution role.

Handler (string) --
The function that Lambda calls to begin executing your function.

CodeSize (integer) --
The size of the function\'s deployment package, in bytes.

Description (string) --
The function\'s description.

Timeout (integer) --
The amount of time in seconds that Lambda allows a function to run before stopping it.

MemorySize (integer) --
The memory that\'s allocated to the function.

LastModified (string) --
The date and time that the function was last updated, in ISO-8601 format (YYYY-MM-DDThh:mm:ss.sTZD).

CodeSha256 (string) --
The SHA256 hash of the function\'s deployment package.

Version (string) --
The version of the Lambda function.

VpcConfig (dict) --
The function\'s networking configuration.

SubnetIds (list) --
A list of VPC subnet IDs.

(string) --


SecurityGroupIds (list) --
A list of VPC security groups IDs.

(string) --


VpcId (string) --
The ID of the VPC.



DeadLetterConfig (dict) --
The function\'s dead letter queue.

TargetArn (string) --
The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.



Environment (dict) --
The function\'s environment variables.

Variables (dict) --
Environment variable key-value pairs.

(string) --
(string) --




Error (dict) --
Error messages for environment variables that couldn\'t be applied.

ErrorCode (string) --
The error code.

Message (string) --
The error message.





KMSKeyArn (string) --
The KMS key that\'s used to encrypt the function\'s environment variables. This key is only returned if you\'ve configured a customer managed CMK.

TracingConfig (dict) --
The function\'s AWS X-Ray tracing configuration.

Mode (string) --
The tracing mode.



MasterArn (string) --
For Lambda@Edge functions, the ARN of the master function.

RevisionId (string) --
The latest updated revision of the function or alias.

Layers (list) --
The function\'s layers .

(dict) --
An AWS Lambda layer .

Arn (string) --
The Amazon Resource Name (ARN) of the function layer.

CodeSize (integer) --
The size of the layer archive in bytes.





State (string) --
The current state of the function. When the state is Inactive , you can reactivate the function by invoking it.

StateReason (string) --
The reason for the function\'s current state.

StateReasonCode (string) --
The reason code for the function\'s current state. When the code is Creating , you can\'t invoke or modify the function.

LastUpdateStatus (string) --
The status of the last update that was performed on the function. This is first set to Successful after function creation completes.

LastUpdateStatusReason (string) --
The reason for the last update that was performed on the function.

LastUpdateStatusReasonCode (string) --
The reason code for the last update that was performed on the function.











Exceptions

Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.ResourceNotFoundException
Lambda.Client.exceptions.InvalidParameterValueException
Lambda.Client.exceptions.TooManyRequestsException

Examples
The following example returns a list of versions of a function named my-function
response = client.list_versions_by_function(
    FunctionName='my-function',
)

print(response)


Expected Output:
{
    'Versions': [
        {
            'CodeSha256': 'YFgDgEKG3ugvF1+pX64gV6tu9qNuIYNUdgJm8nCxsm4=',
            'CodeSize': 5797206,
            'Description': 'Process image objects from Amazon S3.',
            'Environment': {
                'Variables': {
                    'BUCKET': 'my-bucket-1xpuxmplzrlbh',
                    'PREFIX': 'inbound',
                },
            },
            'FunctionArn': 'arn:aws:lambda:us-west-2:123456789012:function:my-function',
            'FunctionName': 'my-function',
            'Handler': 'index.handler',
            'KMSKeyArn': 'arn:aws:kms:us-west-2:123456789012:key/b0844d6c-xmpl-4463-97a4-d49f50839966',
            'LastModified': '2020-04-10T19:06:32.563+0000',
            'MemorySize': 256,
            'RevisionId': '850ca006-2d98-4ff4-86db-8766e9d32fe9',
            'Role': 'arn:aws:iam::123456789012:role/lambda-role',
            'Runtime': 'nodejs12.x',
            'Timeout': 15,
            'TracingConfig': {
                'Mode': 'Active',
            },
            'Version': '$LATEST',
        },
        {
            'CodeSha256': 'YFgDgEKG3ugvF1+pX64gV6tu9qNuIYNUdgJm8nCxsm4=',
            'CodeSize': 5797206,
            'Description': 'Process image objects from Amazon S3.',
            'Environment': {
                'Variables': {
                    'BUCKET': 'my-bucket-1xpuxmplzrlbh',
                    'PREFIX': 'inbound',
                },
            },
            'FunctionArn': 'arn:aws:lambda:us-west-2:123456789012:function:my-function',
            'FunctionName': 'my-function',
            'Handler': 'index.handler',
            'KMSKeyArn': 'arn:aws:kms:us-west-2:123456789012:key/b0844d6c-xmpl-4463-97a4-d49f50839966',
            'LastModified': '2020-04-10T19:06:32.563+0000',
            'MemorySize': 256,
            'RevisionId': 'b75dcd81-xmpl-48a8-a75a-93ba8b5b9727',
            'Role': 'arn:aws:iam::123456789012:role/lambda-role',
            'Runtime': 'nodejs12.x',
            'Timeout': 5,
            'TracingConfig': {
                'Mode': 'Active',
            },
            'Version': '1',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'NextMarker': 'string',
        'Versions': [
            {
                'FunctionName': 'string',
                'FunctionArn': 'string',
                'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'dotnetcore3.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'ruby2.7'|'provided',
                'Role': 'string',
                'Handler': 'string',
                'CodeSize': 123,
                'Description': 'string',
                'Timeout': 123,
                'MemorySize': 123,
                'LastModified': 'string',
                'CodeSha256': 'string',
                'Version': 'string',
                'VpcConfig': {
                    'SubnetIds': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ],
                    'VpcId': 'string'
                },
                'DeadLetterConfig': {
                    'TargetArn': 'string'
                },
                'Environment': {
                    'Variables': {
                        'string': 'string'
                    },
                    'Error': {
                        'ErrorCode': 'string',
                        'Message': 'string'
                    }
                },
                'KMSKeyArn': 'string',
                'TracingConfig': {
                    'Mode': 'Active'|'PassThrough'
                },
                'MasterArn': 'string',
                'RevisionId': 'string',
                'Layers': [
                    {
                        'Arn': 'string',
                        'CodeSize': 123
                    },
                ],
                'State': 'Pending'|'Active'|'Inactive'|'Failed',
                'StateReason': 'string',
                'StateReasonCode': 'Idle'|'Creating'|'Restoring'|'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'|'SubnetOutOfIPAddresses'|'InvalidSubnet'|'InvalidSecurityGroup',
                'LastUpdateStatus': 'Successful'|'Failed'|'InProgress',
                'LastUpdateStatusReason': 'string',
                'LastUpdateStatusReasonCode': 'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'|'SubnetOutOfIPAddresses'|'InvalidSubnet'|'InvalidSecurityGroup'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def publish_layer_version(LayerName=None, Description=None, Content=None, CompatibleRuntimes=None, LicenseInfo=None):
    """
    Creates an AWS Lambda layer from a ZIP archive. Each time you call PublishLayerVersion with the same layer name, a new version is created.
    Add layers to your function with  CreateFunction or  UpdateFunctionConfiguration .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example creates a new Python library layer version. The command retrieves the layer content a file named layer.zip in the specified S3 bucket.
    Expected Output:
    
    :example: response = client.publish_layer_version(
        LayerName='string',
        Description='string',
        Content={
            'S3Bucket': 'string',
            'S3Key': 'string',
            'S3ObjectVersion': 'string',
            'ZipFile': b'bytes'
        },
        CompatibleRuntimes=[
            'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'dotnetcore3.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'ruby2.7'|'provided',
        ],
        LicenseInfo='string'
    )
    
    
    :type LayerName: string
    :param LayerName: [REQUIRED]\nThe name or Amazon Resource Name (ARN) of the layer.\n

    :type Description: string
    :param Description: The description of the version.

    :type Content: dict
    :param Content: [REQUIRED]\nThe function layer archive.\n\nS3Bucket (string) --The Amazon S3 bucket of the layer archive.\n\nS3Key (string) --The Amazon S3 key of the layer archive.\n\nS3ObjectVersion (string) --For versioned objects, the version of the layer archive object to use.\n\nZipFile (bytes) --The base64-encoded contents of the layer archive. AWS SDK and AWS CLI clients handle the encoding for you.\n\n\n

    :type CompatibleRuntimes: list
    :param CompatibleRuntimes: A list of compatible function runtimes . Used for filtering with ListLayers and ListLayerVersions .\n\n(string) --\n\n

    :type LicenseInfo: string
    :param LicenseInfo: The layer\'s software license. It can be any of the following:\n\nAn SPDX license identifier . For example, MIT .\nThe URL of a license hosted on the internet. For example, https://opensource.org/licenses/MIT .\nThe full text of the license.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Content': {
        'Location': 'string',
        'CodeSha256': 'string',
        'CodeSize': 123
    },
    'LayerArn': 'string',
    'LayerVersionArn': 'string',
    'Description': 'string',
    'CreatedDate': 'string',
    'Version': 123,
    'CompatibleRuntimes': [
        'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'dotnetcore3.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'ruby2.7'|'provided',
    ],
    'LicenseInfo': 'string'
}


Response Structure

(dict) --

Content (dict) --
Details about the layer version.

Location (string) --
A link to the layer archive in Amazon S3 that is valid for 10 minutes.

CodeSha256 (string) --
The SHA-256 hash of the layer archive.

CodeSize (integer) --
The size of the layer archive in bytes.



LayerArn (string) --
The ARN of the layer.

LayerVersionArn (string) --
The ARN of the layer version.

Description (string) --
The description of the version.

CreatedDate (string) --
The date that the layer version was created, in ISO-8601 format (YYYY-MM-DDThh:mm:ss.sTZD).

Version (integer) --
The version number.

CompatibleRuntimes (list) --
The layer\'s compatible runtimes.

(string) --


LicenseInfo (string) --
The layer\'s software license.







Exceptions

Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.ResourceNotFoundException
Lambda.Client.exceptions.TooManyRequestsException
Lambda.Client.exceptions.InvalidParameterValueException
Lambda.Client.exceptions.CodeStorageExceededException

Examples
The following example creates a new Python library layer version. The command retrieves the layer content a file named layer.zip in the specified S3 bucket.
response = client.publish_layer_version(
    CompatibleRuntimes=[
        'python3.6',
        'python3.7',
    ],
    Content={
        'S3Bucket': 'lambda-layers-us-west-2-123456789012',
        'S3Key': 'layer.zip',
    },
    Description='My Python layer',
    LayerName='my-layer',
    LicenseInfo='MIT',
)

print(response)


Expected Output:
{
    'CompatibleRuntimes': [
        'python3.6',
        'python3.7',
    ],
    'Content': {
        'CodeSha256': 'tv9jJO+rPbXUUXuRKi7CwHzKtLDkDRJLB3cC3Z/ouXo=',
        'CodeSize': 169,
        'Location': 'https://awslambda-us-west-2-layers.s3.us-west-2.amazonaws.com/snapshots/123456789012/my-layer-4aaa2fbb-ff77-4b0a-ad92-5b78a716a96a?versionId=27iWyA73cCAYqyH...',
    },
    'CreatedDate': '2018-11-14T23:03:52.894+0000',
    'Description': 'My Python layer',
    'LayerArn': 'arn:aws:lambda:us-west-2:123456789012:layer:my-layer',
    'LayerVersionArn': 'arn:aws:lambda:us-west-2:123456789012:layer:my-layer:1',
    'LicenseInfo': 'MIT',
    'Version': 1,
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Content': {
            'Location': 'string',
            'CodeSha256': 'string',
            'CodeSize': 123
        },
        'LayerArn': 'string',
        'LayerVersionArn': 'string',
        'Description': 'string',
        'CreatedDate': 'string',
        'Version': 123,
        'CompatibleRuntimes': [
            'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'dotnetcore3.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'ruby2.7'|'provided',
        ],
        'LicenseInfo': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def publish_version(FunctionName=None, CodeSha256=None, Description=None, RevisionId=None):
    """
    Creates a version from the current code and configuration of a function. Use versions to create a snapshot of your function code and configuration that doesn\'t change.
    AWS Lambda doesn\'t publish a version if the function\'s configuration and code haven\'t changed since the last version. Use  UpdateFunctionCode or  UpdateFunctionConfiguration to update the function before publishing a version.
    Clients can invoke versions directly or with an alias. To create an alias, use  CreateAlias .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This operation publishes a version of a Lambda function
    Expected Output:
    
    :example: response = client.publish_version(
        FunctionName='string',
        CodeSha256='string',
        Description='string',
        RevisionId='string'
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the Lambda function.\n\nName formats\n\nFunction name - MyFunction .\nFunction ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .\nPartial ARN - 123456789012:function:MyFunction .\n\nThe length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.\n

    :type CodeSha256: string
    :param CodeSha256: Only publish a version if the hash value matches the value that\'s specified. Use this option to avoid publishing a version if the function code has changed since you last updated it. You can get the hash for the version that you uploaded from the output of UpdateFunctionCode .

    :type Description: string
    :param Description: A description for the version to override the description in the function configuration.

    :type RevisionId: string
    :param RevisionId: Only update the function if the revision ID matches the ID that\'s specified. Use this option to avoid publishing a version if the function configuration has changed since you last updated it.

    :rtype: dict

ReturnsResponse Syntax
{
    'FunctionName': 'string',
    'FunctionArn': 'string',
    'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'dotnetcore3.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'ruby2.7'|'provided',
    'Role': 'string',
    'Handler': 'string',
    'CodeSize': 123,
    'Description': 'string',
    'Timeout': 123,
    'MemorySize': 123,
    'LastModified': 'string',
    'CodeSha256': 'string',
    'Version': 'string',
    'VpcConfig': {
        'SubnetIds': [
            'string',
        ],
        'SecurityGroupIds': [
            'string',
        ],
        'VpcId': 'string'
    },
    'DeadLetterConfig': {
        'TargetArn': 'string'
    },
    'Environment': {
        'Variables': {
            'string': 'string'
        },
        'Error': {
            'ErrorCode': 'string',
            'Message': 'string'
        }
    },
    'KMSKeyArn': 'string',
    'TracingConfig': {
        'Mode': 'Active'|'PassThrough'
    },
    'MasterArn': 'string',
    'RevisionId': 'string',
    'Layers': [
        {
            'Arn': 'string',
            'CodeSize': 123
        },
    ],
    'State': 'Pending'|'Active'|'Inactive'|'Failed',
    'StateReason': 'string',
    'StateReasonCode': 'Idle'|'Creating'|'Restoring'|'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'|'SubnetOutOfIPAddresses'|'InvalidSubnet'|'InvalidSecurityGroup',
    'LastUpdateStatus': 'Successful'|'Failed'|'InProgress',
    'LastUpdateStatusReason': 'string',
    'LastUpdateStatusReasonCode': 'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'|'SubnetOutOfIPAddresses'|'InvalidSubnet'|'InvalidSecurityGroup'
}


Response Structure

(dict) --
Details about a function\'s configuration.

FunctionName (string) --
The name of the function.

FunctionArn (string) --
The function\'s Amazon Resource Name (ARN).

Runtime (string) --
The runtime environment for the Lambda function.

Role (string) --
The function\'s execution role.

Handler (string) --
The function that Lambda calls to begin executing your function.

CodeSize (integer) --
The size of the function\'s deployment package, in bytes.

Description (string) --
The function\'s description.

Timeout (integer) --
The amount of time in seconds that Lambda allows a function to run before stopping it.

MemorySize (integer) --
The memory that\'s allocated to the function.

LastModified (string) --
The date and time that the function was last updated, in ISO-8601 format (YYYY-MM-DDThh:mm:ss.sTZD).

CodeSha256 (string) --
The SHA256 hash of the function\'s deployment package.

Version (string) --
The version of the Lambda function.

VpcConfig (dict) --
The function\'s networking configuration.

SubnetIds (list) --
A list of VPC subnet IDs.

(string) --


SecurityGroupIds (list) --
A list of VPC security groups IDs.

(string) --


VpcId (string) --
The ID of the VPC.



DeadLetterConfig (dict) --
The function\'s dead letter queue.

TargetArn (string) --
The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.



Environment (dict) --
The function\'s environment variables.

Variables (dict) --
Environment variable key-value pairs.

(string) --
(string) --




Error (dict) --
Error messages for environment variables that couldn\'t be applied.

ErrorCode (string) --
The error code.

Message (string) --
The error message.





KMSKeyArn (string) --
The KMS key that\'s used to encrypt the function\'s environment variables. This key is only returned if you\'ve configured a customer managed CMK.

TracingConfig (dict) --
The function\'s AWS X-Ray tracing configuration.

Mode (string) --
The tracing mode.



MasterArn (string) --
For Lambda@Edge functions, the ARN of the master function.

RevisionId (string) --
The latest updated revision of the function or alias.

Layers (list) --
The function\'s layers .

(dict) --
An AWS Lambda layer .

Arn (string) --
The Amazon Resource Name (ARN) of the function layer.

CodeSize (integer) --
The size of the layer archive in bytes.





State (string) --
The current state of the function. When the state is Inactive , you can reactivate the function by invoking it.

StateReason (string) --
The reason for the function\'s current state.

StateReasonCode (string) --
The reason code for the function\'s current state. When the code is Creating , you can\'t invoke or modify the function.

LastUpdateStatus (string) --
The status of the last update that was performed on the function. This is first set to Successful after function creation completes.

LastUpdateStatusReason (string) --
The reason for the last update that was performed on the function.

LastUpdateStatusReasonCode (string) --
The reason code for the last update that was performed on the function.







Exceptions

Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.ResourceNotFoundException
Lambda.Client.exceptions.InvalidParameterValueException
Lambda.Client.exceptions.TooManyRequestsException
Lambda.Client.exceptions.CodeStorageExceededException
Lambda.Client.exceptions.PreconditionFailedException
Lambda.Client.exceptions.ResourceConflictException

Examples
This operation publishes a version of a Lambda function
response = client.publish_version(
    CodeSha256='',
    Description='',
    FunctionName='myFunction',
)

print(response)


Expected Output:
{
    'CodeSha256': 'YFgDgEKG3ugvF1+pX64gV6tu9qNuIYNUdgJm8nCxsm4=',
    'CodeSize': 5797206,
    'Description': 'Process image objects from Amazon S3.',
    'Environment': {
        'Variables': {
            'BUCKET': 'my-bucket-1xpuxmplzrlbh',
            'PREFIX': 'inbound',
        },
    },
    'FunctionArn': 'arn:aws:lambda:us-west-2:123456789012:function:my-function',
    'FunctionName': 'my-function',
    'Handler': 'index.handler',
    'KMSKeyArn': 'arn:aws:kms:us-west-2:123456789012:key/b0844d6c-xmpl-4463-97a4-d49f50839966',
    'LastModified': '2020-04-10T19:06:32.563+0000',
    'LastUpdateStatus': 'Successful',
    'MemorySize': 256,
    'RevisionId': 'b75dcd81-xmpl-48a8-a75a-93ba8b5b9727',
    'Role': 'arn:aws:iam::123456789012:role/lambda-role',
    'Runtime': 'nodejs12.x',
    'State': 'Active',
    'Timeout': 5,
    'TracingConfig': {
        'Mode': 'Active',
    },
    'Version': '1',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'FunctionName': 'string',
        'FunctionArn': 'string',
        'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'dotnetcore3.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'ruby2.7'|'provided',
        'Role': 'string',
        'Handler': 'string',
        'CodeSize': 123,
        'Description': 'string',
        'Timeout': 123,
        'MemorySize': 123,
        'LastModified': 'string',
        'CodeSha256': 'string',
        'Version': 'string',
        'VpcConfig': {
            'SubnetIds': [
                'string',
            ],
            'SecurityGroupIds': [
                'string',
            ],
            'VpcId': 'string'
        },
        'DeadLetterConfig': {
            'TargetArn': 'string'
        },
        'Environment': {
            'Variables': {
                'string': 'string'
            },
            'Error': {
                'ErrorCode': 'string',
                'Message': 'string'
            }
        },
        'KMSKeyArn': 'string',
        'TracingConfig': {
            'Mode': 'Active'|'PassThrough'
        },
        'MasterArn': 'string',
        'RevisionId': 'string',
        'Layers': [
            {
                'Arn': 'string',
                'CodeSize': 123
            },
        ],
        'State': 'Pending'|'Active'|'Inactive'|'Failed',
        'StateReason': 'string',
        'StateReasonCode': 'Idle'|'Creating'|'Restoring'|'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'|'SubnetOutOfIPAddresses'|'InvalidSubnet'|'InvalidSecurityGroup',
        'LastUpdateStatus': 'Successful'|'Failed'|'InProgress',
        'LastUpdateStatusReason': 'string',
        'LastUpdateStatusReasonCode': 'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'|'SubnetOutOfIPAddresses'|'InvalidSubnet'|'InvalidSecurityGroup'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def put_function_concurrency(FunctionName=None, ReservedConcurrentExecutions=None):
    """
    Sets the maximum number of simultaneous executions for a function, and reserves capacity for that concurrency level.
    Concurrency settings apply to the function as a whole, including all published versions and the unpublished version. Reserving concurrency both ensures that your function has capacity to process the specified number of events simultaneously, and prevents it from scaling beyond that level. Use  GetFunction to see the current setting for a function.
    Use  GetAccountSettings to see your Regional concurrency limit. You can reserve concurrency for as many functions as you like, as long as you leave at least 100 simultaneous executions unreserved for functions that aren\'t configured with a per-function limit. For more information, see Managing Concurrency .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example configures 100 reserved concurrent executions for the my-function function.
    Expected Output:
    
    :example: response = client.put_function_concurrency(
        FunctionName='string',
        ReservedConcurrentExecutions=123
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the Lambda function.\n\nName formats\n\nFunction name - my-function .\nFunction ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function .\nPartial ARN - 123456789012:function:my-function .\n\nThe length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.\n

    :type ReservedConcurrentExecutions: integer
    :param ReservedConcurrentExecutions: [REQUIRED]\nThe number of simultaneous executions to reserve for the function.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ReservedConcurrentExecutions': 123
}


Response Structure

(dict) --

ReservedConcurrentExecutions (integer) --
The number of concurrent executions that are reserved for this function. For more information, see Managing Concurrency .







Exceptions

Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.InvalidParameterValueException
Lambda.Client.exceptions.ResourceNotFoundException
Lambda.Client.exceptions.TooManyRequestsException
Lambda.Client.exceptions.ResourceConflictException

Examples
The following example configures 100 reserved concurrent executions for the my-function function.
response = client.put_function_concurrency(
    FunctionName='my-function',
    ReservedConcurrentExecutions=100,
)

print(response)


Expected Output:
{
    'ReservedConcurrentExecutions': 100,
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ReservedConcurrentExecutions': 123
    }
    
    
    :returns: 
    Lambda.Client.exceptions.ServiceException
    Lambda.Client.exceptions.InvalidParameterValueException
    Lambda.Client.exceptions.ResourceNotFoundException
    Lambda.Client.exceptions.TooManyRequestsException
    Lambda.Client.exceptions.ResourceConflictException
    
    """
    pass

def put_function_event_invoke_config(FunctionName=None, Qualifier=None, MaximumRetryAttempts=None, MaximumEventAgeInSeconds=None, DestinationConfig=None):
    """
    Configures options for asynchronous invocation on a function, version, or alias. If a configuration already exists for a function, version, or alias, this operation overwrites it. If you exclude any settings, they are removed. To set one option without affecting existing settings for other options, use  PutFunctionEventInvokeConfig .
    By default, Lambda retries an asynchronous invocation twice if the function returns an error. It retains events in a queue for up to six hours. When an event fails all processing attempts or stays in the asynchronous invocation queue for too long, Lambda discards it. To retain discarded events, configure a dead-letter queue with  UpdateFunctionConfiguration .
    To send an invocation record to a queue, topic, function, or event bus, specify a destination . You can configure separate destinations for successful invocations (on-success) and events that fail all processing attempts (on-failure). You can configure destinations in addition to or instead of a dead-letter queue.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example sets a maximum event age of one hour and disables retries for the specified function.
    Expected Output:
    
    :example: response = client.put_function_event_invoke_config(
        FunctionName='string',
        Qualifier='string',
        MaximumRetryAttempts=123,
        MaximumEventAgeInSeconds=123,
        DestinationConfig={
            'OnSuccess': {
                'Destination': 'string'
            },
            'OnFailure': {
                'Destination': 'string'
            }
        }
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the Lambda function, version, or alias.\n\nName formats\n\nFunction name - my-function (name-only), my-function:v1 (with alias).\nFunction ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function .\nPartial ARN - 123456789012:function:my-function .\n\nYou can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.\n

    :type Qualifier: string
    :param Qualifier: A version number or alias name.

    :type MaximumRetryAttempts: integer
    :param MaximumRetryAttempts: The maximum number of times to retry when the function returns an error.

    :type MaximumEventAgeInSeconds: integer
    :param MaximumEventAgeInSeconds: The maximum age of a request that Lambda sends to a function for processing.

    :type DestinationConfig: dict
    :param DestinationConfig: A destination for events after they have been sent to a function for processing.\n\nDestinations\n\nFunction - The Amazon Resource Name (ARN) of a Lambda function.\nQueue - The ARN of an SQS queue.\nTopic - The ARN of an SNS topic.\nEvent Bus - The ARN of an Amazon EventBridge event bus.\n\n\nOnSuccess (dict) --The destination configuration for successful invocations.\n\nDestination (string) --The Amazon Resource Name (ARN) of the destination resource.\n\n\n\nOnFailure (dict) --The destination configuration for failed invocations.\n\nDestination (string) --The Amazon Resource Name (ARN) of the destination resource.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'LastModified': datetime(2015, 1, 1),
    'FunctionArn': 'string',
    'MaximumRetryAttempts': 123,
    'MaximumEventAgeInSeconds': 123,
    'DestinationConfig': {
        'OnSuccess': {
            'Destination': 'string'
        },
        'OnFailure': {
            'Destination': 'string'
        }
    }
}


Response Structure

(dict) --

LastModified (datetime) --
The date and time that the configuration was last updated.

FunctionArn (string) --
The Amazon Resource Name (ARN) of the function.

MaximumRetryAttempts (integer) --
The maximum number of times to retry when the function returns an error.

MaximumEventAgeInSeconds (integer) --
The maximum age of a request that Lambda sends to a function for processing.

DestinationConfig (dict) --
A destination for events after they have been sent to a function for processing.

Destinations


Function - The Amazon Resource Name (ARN) of a Lambda function.
Queue - The ARN of an SQS queue.
Topic - The ARN of an SNS topic.
Event Bus - The ARN of an Amazon EventBridge event bus.


OnSuccess (dict) --
The destination configuration for successful invocations.

Destination (string) --
The Amazon Resource Name (ARN) of the destination resource.



OnFailure (dict) --
The destination configuration for failed invocations.

Destination (string) --
The Amazon Resource Name (ARN) of the destination resource.











Exceptions

Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.ResourceNotFoundException
Lambda.Client.exceptions.InvalidParameterValueException
Lambda.Client.exceptions.TooManyRequestsException

Examples
The following example sets a maximum event age of one hour and disables retries for the specified function.
response = client.put_function_event_invoke_config(
    FunctionName='my-function',
    MaximumEventAgeInSeconds=3600,
    MaximumRetryAttempts=0,
)

print(response)


Expected Output:
{
    'DestinationConfig': {
        'OnFailure': {
        },
        'OnSuccess': {
        },
    },
    'FunctionArn': 'arn:aws:lambda:us-east-2:123456789012:function:my-function:$LATEST',
    'LastModified': datetime(2016, 11, 21, 19, 49, 20, 0, 326, 0),
    'MaximumEventAgeInSeconds': 3600,
    'MaximumRetryAttempts': 0,
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'LastModified': datetime(2015, 1, 1),
        'FunctionArn': 'string',
        'MaximumRetryAttempts': 123,
        'MaximumEventAgeInSeconds': 123,
        'DestinationConfig': {
            'OnSuccess': {
                'Destination': 'string'
            },
            'OnFailure': {
                'Destination': 'string'
            }
        }
    }
    
    
    :returns: 
    Function - The Amazon Resource Name (ARN) of a Lambda function.
    Queue - The ARN of an SQS queue.
    Topic - The ARN of an SNS topic.
    Event Bus - The ARN of an Amazon EventBridge event bus.
    
    """
    pass

def put_provisioned_concurrency_config(FunctionName=None, Qualifier=None, ProvisionedConcurrentExecutions=None):
    """
    Adds a provisioned concurrency configuration to a function\'s alias or version.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example allocates 100 provisioned concurrency for the BLUE alias of the specified function.
    Expected Output:
    
    :example: response = client.put_provisioned_concurrency_config(
        FunctionName='string',
        Qualifier='string',
        ProvisionedConcurrentExecutions=123
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the Lambda function.\n\nName formats\n\nFunction name - my-function .\nFunction ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function .\nPartial ARN - 123456789012:function:my-function .\n\nThe length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.\n

    :type Qualifier: string
    :param Qualifier: [REQUIRED]\nThe version number or alias name.\n

    :type ProvisionedConcurrentExecutions: integer
    :param ProvisionedConcurrentExecutions: [REQUIRED]\nThe amount of provisioned concurrency to allocate for the version or alias.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'RequestedProvisionedConcurrentExecutions': 123,
    'AvailableProvisionedConcurrentExecutions': 123,
    'AllocatedProvisionedConcurrentExecutions': 123,
    'Status': 'IN_PROGRESS'|'READY'|'FAILED',
    'StatusReason': 'string',
    'LastModified': 'string'
}


Response Structure

(dict) --

RequestedProvisionedConcurrentExecutions (integer) --
The amount of provisioned concurrency requested.

AvailableProvisionedConcurrentExecutions (integer) --
The amount of provisioned concurrency available.

AllocatedProvisionedConcurrentExecutions (integer) --
The amount of provisioned concurrency allocated.

Status (string) --
The status of the allocation process.

StatusReason (string) --
For failed allocations, the reason that provisioned concurrency could not be allocated.

LastModified (string) --
The date and time that a user last updated the configuration, in ISO 8601 format .







Exceptions

Lambda.Client.exceptions.InvalidParameterValueException
Lambda.Client.exceptions.ResourceNotFoundException
Lambda.Client.exceptions.ResourceConflictException
Lambda.Client.exceptions.TooManyRequestsException
Lambda.Client.exceptions.ServiceException

Examples
The following example allocates 100 provisioned concurrency for the BLUE alias of the specified function.
response = client.put_provisioned_concurrency_config(
    FunctionName='my-function',
    ProvisionedConcurrentExecutions=100,
    Qualifier='BLUE',
)

print(response)


Expected Output:
{
    'AllocatedProvisionedConcurrentExecutions': 0,
    'LastModified': '2019-11-21T19:32:12+0000',
    'RequestedProvisionedConcurrentExecutions': 100,
    'Status': 'IN_PROGRESS',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'RequestedProvisionedConcurrentExecutions': 123,
        'AvailableProvisionedConcurrentExecutions': 123,
        'AllocatedProvisionedConcurrentExecutions': 123,
        'Status': 'IN_PROGRESS'|'READY'|'FAILED',
        'StatusReason': 'string',
        'LastModified': 'string'
    }
    
    
    :returns: 
    Lambda.Client.exceptions.InvalidParameterValueException
    Lambda.Client.exceptions.ResourceNotFoundException
    Lambda.Client.exceptions.ResourceConflictException
    Lambda.Client.exceptions.TooManyRequestsException
    Lambda.Client.exceptions.ServiceException
    
    """
    pass

def remove_layer_version_permission(LayerName=None, VersionNumber=None, StatementId=None, RevisionId=None):
    """
    Removes a statement from the permissions policy for a version of an AWS Lambda layer . For more information, see  AddLayerVersionPermission .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example deletes permission for an account to configure a layer version.
    Expected Output:
    
    :example: response = client.remove_layer_version_permission(
        LayerName='string',
        VersionNumber=123,
        StatementId='string',
        RevisionId='string'
    )
    
    
    :type LayerName: string
    :param LayerName: [REQUIRED]\nThe name or Amazon Resource Name (ARN) of the layer.\n

    :type VersionNumber: integer
    :param VersionNumber: [REQUIRED]\nThe version number.\n

    :type StatementId: string
    :param StatementId: [REQUIRED]\nThe identifier that was specified when the statement was added.\n

    :type RevisionId: string
    :param RevisionId: Only update the policy if the revision ID matches the ID specified. Use this option to avoid modifying a policy that has changed since you last read it.

    :return: response = client.remove_layer_version_permission(
        LayerName='my-layer',
        StatementId='xaccount',
        VersionNumber=1,
    )
    
    print(response)
    
    
    :returns: 
    Lambda.Client.exceptions.ServiceException
    Lambda.Client.exceptions.ResourceNotFoundException
    Lambda.Client.exceptions.InvalidParameterValueException
    Lambda.Client.exceptions.TooManyRequestsException
    Lambda.Client.exceptions.PreconditionFailedException
    
    """
    pass

def remove_permission(FunctionName=None, StatementId=None, Qualifier=None, RevisionId=None):
    """
    Revokes function-use permission from an AWS service or another account. You can get the ID of the statement from the output of  GetPolicy .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example removes a permissions statement named xaccount from the PROD alias of a function named my-function.
    Expected Output:
    
    :example: response = client.remove_permission(
        FunctionName='string',
        StatementId='string',
        Qualifier='string',
        RevisionId='string'
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the Lambda function, version, or alias.\n\nName formats\n\nFunction name - my-function (name-only), my-function:v1 (with alias).\nFunction ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function .\nPartial ARN - 123456789012:function:my-function .\n\nYou can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.\n

    :type StatementId: string
    :param StatementId: [REQUIRED]\nStatement ID of the permission to remove.\n

    :type Qualifier: string
    :param Qualifier: Specify a version or alias to remove permissions from a published version of the function.

    :type RevisionId: string
    :param RevisionId: Only update the policy if the revision ID matches the ID that\'s specified. Use this option to avoid modifying a policy that has changed since you last read it.

    :return: response = client.remove_permission(
        FunctionName='my-function',
        Qualifier='PROD',
        StatementId='xaccount',
    )
    
    print(response)
    
    
    :returns: 
    Lambda.Client.exceptions.ServiceException
    Lambda.Client.exceptions.ResourceNotFoundException
    Lambda.Client.exceptions.InvalidParameterValueException
    Lambda.Client.exceptions.TooManyRequestsException
    Lambda.Client.exceptions.PreconditionFailedException
    
    """
    pass

def tag_resource(Resource=None, Tags=None):
    """
    Adds tags to a function.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example adds a tag with the key name DEPARTMENT and a value of \'Department A\' to the specified Lambda function.
    Expected Output:
    
    :example: response = client.tag_resource(
        Resource='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type Resource: string
    :param Resource: [REQUIRED]\nThe function\'s Amazon Resource Name (ARN).\n

    :type Tags: dict
    :param Tags: [REQUIRED]\nA list of tags to apply to the function.\n\n(string) --\n(string) --\n\n\n\n

    :return: response = client.tag_resource(
        Resource='arn:aws:lambda:us-west-2:123456789012:function:my-function',
        Tags={
            'DEPARTMENT': 'Department A',
        },
    )
    
    print(response)
    
    
    :returns: 
    Lambda.Client.exceptions.ServiceException
    Lambda.Client.exceptions.ResourceNotFoundException
    Lambda.Client.exceptions.InvalidParameterValueException
    Lambda.Client.exceptions.TooManyRequestsException
    Lambda.Client.exceptions.ResourceConflictException
    
    """
    pass

def untag_resource(Resource=None, TagKeys=None):
    """
    Removes tags from a function.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example removes the tag with the key name DEPARTMENT tag from the my-function Lambda function.
    Expected Output:
    
    :example: response = client.untag_resource(
        Resource='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type Resource: string
    :param Resource: [REQUIRED]\nThe function\'s Amazon Resource Name (ARN).\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nA list of tag keys to remove from the function.\n\n(string) --\n\n

    :return: response = client.untag_resource(
        Resource='arn:aws:lambda:us-west-2:123456789012:function:my-function',
        TagKeys=[
            'DEPARTMENT',
        ],
    )
    
    print(response)
    
    
    :returns: 
    Lambda.Client.exceptions.ServiceException
    Lambda.Client.exceptions.ResourceNotFoundException
    Lambda.Client.exceptions.InvalidParameterValueException
    Lambda.Client.exceptions.TooManyRequestsException
    Lambda.Client.exceptions.ResourceConflictException
    
    """
    pass

def update_alias(FunctionName=None, Name=None, FunctionVersion=None, Description=None, RoutingConfig=None, RevisionId=None):
    """
    Updates the configuration of a Lambda function alias .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example updates the alias named BLUE to send 30% of traffic to version 2 and 70% to version 1.
    Expected Output:
    
    :example: response = client.update_alias(
        FunctionName='string',
        Name='string',
        FunctionVersion='string',
        Description='string',
        RoutingConfig={
            'AdditionalVersionWeights': {
                'string': 123.0
            }
        },
        RevisionId='string'
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the Lambda function.\n\nName formats\n\nFunction name - MyFunction .\nFunction ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .\nPartial ARN - 123456789012:function:MyFunction .\n\nThe length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.\n

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the alias.\n

    :type FunctionVersion: string
    :param FunctionVersion: The function version that the alias invokes.

    :type Description: string
    :param Description: A description of the alias.

    :type RoutingConfig: dict
    :param RoutingConfig: The routing configuration of the alias.\n\nAdditionalVersionWeights (dict) --The name of the second alias, and the percentage of traffic that\'s routed to it.\n\n(string) --\n(float) --\n\n\n\n\n\n

    :type RevisionId: string
    :param RevisionId: Only update the alias if the revision ID matches the ID that\'s specified. Use this option to avoid modifying an alias that has changed since you last read it.

    :rtype: dict

ReturnsResponse Syntax
{
    'AliasArn': 'string',
    'Name': 'string',
    'FunctionVersion': 'string',
    'Description': 'string',
    'RoutingConfig': {
        'AdditionalVersionWeights': {
            'string': 123.0
        }
    },
    'RevisionId': 'string'
}


Response Structure

(dict) --
Provides configuration information about a Lambda function alias .

AliasArn (string) --
The Amazon Resource Name (ARN) of the alias.

Name (string) --
The name of the alias.

FunctionVersion (string) --
The function version that the alias invokes.

Description (string) --
A description of the alias.

RoutingConfig (dict) --
The routing configuration of the alias.

AdditionalVersionWeights (dict) --
The name of the second alias, and the percentage of traffic that\'s routed to it.

(string) --
(float) --






RevisionId (string) --
A unique identifier that changes when you update the alias.







Exceptions

Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.ResourceNotFoundException
Lambda.Client.exceptions.InvalidParameterValueException
Lambda.Client.exceptions.TooManyRequestsException
Lambda.Client.exceptions.PreconditionFailedException
Lambda.Client.exceptions.ResourceConflictException

Examples
The following example updates the alias named BLUE to send 30% of traffic to version 2 and 70% to version 1.
response = client.update_alias(
    FunctionName='my-function',
    FunctionVersion='2',
    Name='BLUE',
    RoutingConfig={
        'AdditionalVersionWeights': {
            '1': 0.7,
        },
    },
)

print(response)


Expected Output:
{
    'AliasArn': 'arn:aws:lambda:us-west-2:123456789012:function:my-function:BLUE',
    'Description': 'Production environment BLUE.',
    'FunctionVersion': '2',
    'Name': 'BLUE',
    'RevisionId': '594f41fb-xmpl-4c20-95c7-6ca5f2a92c93',
    'RoutingConfig': {
        'AdditionalVersionWeights': {
            '1': 0.7,
        },
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'AliasArn': 'string',
        'Name': 'string',
        'FunctionVersion': 'string',
        'Description': 'string',
        'RoutingConfig': {
            'AdditionalVersionWeights': {
                'string': 123.0
            }
        },
        'RevisionId': 'string'
    }
    
    
    :returns: 
    (string) --
    (float) --
    
    
    
    """
    pass

def update_event_source_mapping(UUID=None, FunctionName=None, Enabled=None, BatchSize=None, MaximumBatchingWindowInSeconds=None, DestinationConfig=None, MaximumRecordAgeInSeconds=None, BisectBatchOnFunctionError=None, MaximumRetryAttempts=None, ParallelizationFactor=None):
    """
    Updates an event source mapping. You can change the function that AWS Lambda invokes, or pause invocation and resume later from the same location.
    The following error handling options are only available for stream sources (DynamoDB and Kinesis):
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This operation updates a Lambda function event source mapping
    Expected Output:
    
    :example: response = client.update_event_source_mapping(
        UUID='string',
        FunctionName='string',
        Enabled=True|False,
        BatchSize=123,
        MaximumBatchingWindowInSeconds=123,
        DestinationConfig={
            'OnSuccess': {
                'Destination': 'string'
            },
            'OnFailure': {
                'Destination': 'string'
            }
        },
        MaximumRecordAgeInSeconds=123,
        BisectBatchOnFunctionError=True|False,
        MaximumRetryAttempts=123,
        ParallelizationFactor=123
    )
    
    
    :type UUID: string
    :param UUID: [REQUIRED]\nThe identifier of the event source mapping.\n

    :type FunctionName: string
    :param FunctionName: The name of the Lambda function.\n\nName formats\n\nFunction name - MyFunction .\nFunction ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .\nVersion or Alias ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD .\nPartial ARN - 123456789012:function:MyFunction .\n\nThe length constraint applies only to the full ARN. If you specify only the function name, it\'s limited to 64 characters in length.\n

    :type Enabled: boolean
    :param Enabled: Disables the event source mapping to pause polling and invocation.

    :type BatchSize: integer
    :param BatchSize: The maximum number of items to retrieve in a single batch.\n\nAmazon Kinesis - Default 100. Max 10,000.\nAmazon DynamoDB Streams - Default 100. Max 1,000.\nAmazon Simple Queue Service - Default 10. Max 10.\n\n

    :type MaximumBatchingWindowInSeconds: integer
    :param MaximumBatchingWindowInSeconds: (Streams) The maximum amount of time to gather records before invoking the function, in seconds.

    :type DestinationConfig: dict
    :param DestinationConfig: (Streams) An Amazon SQS queue or Amazon SNS topic destination for discarded records.\n\nOnSuccess (dict) --The destination configuration for successful invocations.\n\nDestination (string) --The Amazon Resource Name (ARN) of the destination resource.\n\n\n\nOnFailure (dict) --The destination configuration for failed invocations.\n\nDestination (string) --The Amazon Resource Name (ARN) of the destination resource.\n\n\n\n\n

    :type MaximumRecordAgeInSeconds: integer
    :param MaximumRecordAgeInSeconds: (Streams) The maximum age of a record that Lambda sends to a function for processing.

    :type BisectBatchOnFunctionError: boolean
    :param BisectBatchOnFunctionError: (Streams) If the function returns an error, split the batch in two and retry.

    :type MaximumRetryAttempts: integer
    :param MaximumRetryAttempts: (Streams) The maximum number of times to retry when the function returns an error.

    :type ParallelizationFactor: integer
    :param ParallelizationFactor: (Streams) The number of batches to process from each shard concurrently.

    :rtype: dict

ReturnsResponse Syntax
{
    'UUID': 'string',
    'BatchSize': 123,
    'MaximumBatchingWindowInSeconds': 123,
    'ParallelizationFactor': 123,
    'EventSourceArn': 'string',
    'FunctionArn': 'string',
    'LastModified': datetime(2015, 1, 1),
    'LastProcessingResult': 'string',
    'State': 'string',
    'StateTransitionReason': 'string',
    'DestinationConfig': {
        'OnSuccess': {
            'Destination': 'string'
        },
        'OnFailure': {
            'Destination': 'string'
        }
    },
    'MaximumRecordAgeInSeconds': 123,
    'BisectBatchOnFunctionError': True|False,
    'MaximumRetryAttempts': 123
}


Response Structure

(dict) --
A mapping between an AWS resource and an AWS Lambda function. See  CreateEventSourceMapping for details.

UUID (string) --
The identifier of the event source mapping.

BatchSize (integer) --
The maximum number of items to retrieve in a single batch.

MaximumBatchingWindowInSeconds (integer) --
(Streams) The maximum amount of time to gather records before invoking the function, in seconds.

ParallelizationFactor (integer) --
(Streams) The number of batches to process from each shard concurrently.

EventSourceArn (string) --
The Amazon Resource Name (ARN) of the event source.

FunctionArn (string) --
The ARN of the Lambda function.

LastModified (datetime) --
The date that the event source mapping was last updated, or its state changed.

LastProcessingResult (string) --
The result of the last AWS Lambda invocation of your Lambda function.

State (string) --
The state of the event source mapping. It can be one of the following: Creating , Enabling , Enabled , Disabling , Disabled , Updating , or Deleting .

StateTransitionReason (string) --
Indicates whether the last change to the event source mapping was made by a user, or by the Lambda service.

DestinationConfig (dict) --
(Streams) An Amazon SQS queue or Amazon SNS topic destination for discarded records.

OnSuccess (dict) --
The destination configuration for successful invocations.

Destination (string) --
The Amazon Resource Name (ARN) of the destination resource.



OnFailure (dict) --
The destination configuration for failed invocations.

Destination (string) --
The Amazon Resource Name (ARN) of the destination resource.





MaximumRecordAgeInSeconds (integer) --
(Streams) The maximum age of a record that Lambda sends to a function for processing.

BisectBatchOnFunctionError (boolean) --
(Streams) If the function returns an error, split the batch in two and retry.

MaximumRetryAttempts (integer) --
(Streams) The maximum number of times to retry when the function returns an error.







Exceptions

Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.ResourceNotFoundException
Lambda.Client.exceptions.InvalidParameterValueException
Lambda.Client.exceptions.TooManyRequestsException
Lambda.Client.exceptions.ResourceConflictException
Lambda.Client.exceptions.ResourceInUseException

Examples
This operation updates a Lambda function event source mapping
response = client.update_event_source_mapping(
    BatchSize=123,
    Enabled=True,
    FunctionName='myFunction',
    UUID='1234xCy789012',
)

print(response)


Expected Output:
{
    'BatchSize': 123,
    'EventSourceArn': 'arn:aws:s3:::examplebucket/*',
    'FunctionArn': 'arn:aws:lambda:us-west-2:123456789012:function:myFunction',
    'LastModified': datetime(2016, 11, 21, 19, 49, 20, 0, 326, 0),
    'LastProcessingResult': '',
    'State': '',
    'StateTransitionReason': '',
    'UUID': '1234xCy789012',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'UUID': 'string',
        'BatchSize': 123,
        'MaximumBatchingWindowInSeconds': 123,
        'ParallelizationFactor': 123,
        'EventSourceArn': 'string',
        'FunctionArn': 'string',
        'LastModified': datetime(2015, 1, 1),
        'LastProcessingResult': 'string',
        'State': 'string',
        'StateTransitionReason': 'string',
        'DestinationConfig': {
            'OnSuccess': {
                'Destination': 'string'
            },
            'OnFailure': {
                'Destination': 'string'
            }
        },
        'MaximumRecordAgeInSeconds': 123,
        'BisectBatchOnFunctionError': True|False,
        'MaximumRetryAttempts': 123
    }
    
    
    :returns: 
    UUID (string) -- [REQUIRED]
    The identifier of the event source mapping.
    
    FunctionName (string) -- The name of the Lambda function.
    
    Name formats
    
    Function name - MyFunction .
    Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .
    Version or Alias ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD .
    Partial ARN - 123456789012:function:MyFunction .
    
    The length constraint applies only to the full ARN. If you specify only the function name, it\'s limited to 64 characters in length.
    
    Enabled (boolean) -- Disables the event source mapping to pause polling and invocation.
    BatchSize (integer) -- The maximum number of items to retrieve in a single batch.
    
    Amazon Kinesis - Default 100. Max 10,000.
    Amazon DynamoDB Streams - Default 100. Max 1,000.
    Amazon Simple Queue Service - Default 10. Max 10.
    
    
    MaximumBatchingWindowInSeconds (integer) -- (Streams) The maximum amount of time to gather records before invoking the function, in seconds.
    DestinationConfig (dict) -- (Streams) An Amazon SQS queue or Amazon SNS topic destination for discarded records.
    
    OnSuccess (dict) --The destination configuration for successful invocations.
    
    Destination (string) --The Amazon Resource Name (ARN) of the destination resource.
    
    
    
    OnFailure (dict) --The destination configuration for failed invocations.
    
    Destination (string) --The Amazon Resource Name (ARN) of the destination resource.
    
    
    
    
    
    MaximumRecordAgeInSeconds (integer) -- (Streams) The maximum age of a record that Lambda sends to a function for processing.
    BisectBatchOnFunctionError (boolean) -- (Streams) If the function returns an error, split the batch in two and retry.
    MaximumRetryAttempts (integer) -- (Streams) The maximum number of times to retry when the function returns an error.
    ParallelizationFactor (integer) -- (Streams) The number of batches to process from each shard concurrently.
    
    """
    pass

def update_function_code(FunctionName=None, ZipFile=None, S3Bucket=None, S3Key=None, S3ObjectVersion=None, Publish=None, DryRun=None, RevisionId=None):
    """
    Updates a Lambda function\'s code.
    The function\'s code is locked when you publish a version. You can\'t modify the code of a published version, only the unpublished version.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example replaces the code of the unpublished ($LATEST) version of a function named my-function with the contents of the specified zip file in Amazon S3.
    Expected Output:
    
    :example: response = client.update_function_code(
        FunctionName='string',
        ZipFile=b'bytes',
        S3Bucket='string',
        S3Key='string',
        S3ObjectVersion='string',
        Publish=True|False,
        DryRun=True|False,
        RevisionId='string'
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the Lambda function.\n\nName formats\n\nFunction name - my-function .\nFunction ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function .\nPartial ARN - 123456789012:function:my-function .\n\nThe length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.\n

    :type ZipFile: bytes
    :param ZipFile: The base64-encoded contents of the deployment package. AWS SDK and AWS CLI clients handle the encoding for you.\n\nThis value will be base64 encoded automatically. Do not base64 encode this value prior to performing the operation.\n

    :type S3Bucket: string
    :param S3Bucket: An Amazon S3 bucket in the same AWS Region as your function. The bucket can be in a different AWS account.

    :type S3Key: string
    :param S3Key: The Amazon S3 key of the deployment package.

    :type S3ObjectVersion: string
    :param S3ObjectVersion: For versioned objects, the version of the deployment package object to use.

    :type Publish: boolean
    :param Publish: Set to true to publish a new version of the function after updating the code. This has the same effect as calling PublishVersion separately.

    :type DryRun: boolean
    :param DryRun: Set to true to validate the request parameters and access permissions without modifying the function code.

    :type RevisionId: string
    :param RevisionId: Only update the function if the revision ID matches the ID that\'s specified. Use this option to avoid modifying a function that has changed since you last read it.

    :rtype: dict

ReturnsResponse Syntax
{
    'FunctionName': 'string',
    'FunctionArn': 'string',
    'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'dotnetcore3.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'ruby2.7'|'provided',
    'Role': 'string',
    'Handler': 'string',
    'CodeSize': 123,
    'Description': 'string',
    'Timeout': 123,
    'MemorySize': 123,
    'LastModified': 'string',
    'CodeSha256': 'string',
    'Version': 'string',
    'VpcConfig': {
        'SubnetIds': [
            'string',
        ],
        'SecurityGroupIds': [
            'string',
        ],
        'VpcId': 'string'
    },
    'DeadLetterConfig': {
        'TargetArn': 'string'
    },
    'Environment': {
        'Variables': {
            'string': 'string'
        },
        'Error': {
            'ErrorCode': 'string',
            'Message': 'string'
        }
    },
    'KMSKeyArn': 'string',
    'TracingConfig': {
        'Mode': 'Active'|'PassThrough'
    },
    'MasterArn': 'string',
    'RevisionId': 'string',
    'Layers': [
        {
            'Arn': 'string',
            'CodeSize': 123
        },
    ],
    'State': 'Pending'|'Active'|'Inactive'|'Failed',
    'StateReason': 'string',
    'StateReasonCode': 'Idle'|'Creating'|'Restoring'|'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'|'SubnetOutOfIPAddresses'|'InvalidSubnet'|'InvalidSecurityGroup',
    'LastUpdateStatus': 'Successful'|'Failed'|'InProgress',
    'LastUpdateStatusReason': 'string',
    'LastUpdateStatusReasonCode': 'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'|'SubnetOutOfIPAddresses'|'InvalidSubnet'|'InvalidSecurityGroup'
}


Response Structure

(dict) --
Details about a function\'s configuration.

FunctionName (string) --
The name of the function.

FunctionArn (string) --
The function\'s Amazon Resource Name (ARN).

Runtime (string) --
The runtime environment for the Lambda function.

Role (string) --
The function\'s execution role.

Handler (string) --
The function that Lambda calls to begin executing your function.

CodeSize (integer) --
The size of the function\'s deployment package, in bytes.

Description (string) --
The function\'s description.

Timeout (integer) --
The amount of time in seconds that Lambda allows a function to run before stopping it.

MemorySize (integer) --
The memory that\'s allocated to the function.

LastModified (string) --
The date and time that the function was last updated, in ISO-8601 format (YYYY-MM-DDThh:mm:ss.sTZD).

CodeSha256 (string) --
The SHA256 hash of the function\'s deployment package.

Version (string) --
The version of the Lambda function.

VpcConfig (dict) --
The function\'s networking configuration.

SubnetIds (list) --
A list of VPC subnet IDs.

(string) --


SecurityGroupIds (list) --
A list of VPC security groups IDs.

(string) --


VpcId (string) --
The ID of the VPC.



DeadLetterConfig (dict) --
The function\'s dead letter queue.

TargetArn (string) --
The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.



Environment (dict) --
The function\'s environment variables.

Variables (dict) --
Environment variable key-value pairs.

(string) --
(string) --




Error (dict) --
Error messages for environment variables that couldn\'t be applied.

ErrorCode (string) --
The error code.

Message (string) --
The error message.





KMSKeyArn (string) --
The KMS key that\'s used to encrypt the function\'s environment variables. This key is only returned if you\'ve configured a customer managed CMK.

TracingConfig (dict) --
The function\'s AWS X-Ray tracing configuration.

Mode (string) --
The tracing mode.



MasterArn (string) --
For Lambda@Edge functions, the ARN of the master function.

RevisionId (string) --
The latest updated revision of the function or alias.

Layers (list) --
The function\'s layers .

(dict) --
An AWS Lambda layer .

Arn (string) --
The Amazon Resource Name (ARN) of the function layer.

CodeSize (integer) --
The size of the layer archive in bytes.





State (string) --
The current state of the function. When the state is Inactive , you can reactivate the function by invoking it.

StateReason (string) --
The reason for the function\'s current state.

StateReasonCode (string) --
The reason code for the function\'s current state. When the code is Creating , you can\'t invoke or modify the function.

LastUpdateStatus (string) --
The status of the last update that was performed on the function. This is first set to Successful after function creation completes.

LastUpdateStatusReason (string) --
The reason for the last update that was performed on the function.

LastUpdateStatusReasonCode (string) --
The reason code for the last update that was performed on the function.







Exceptions

Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.ResourceNotFoundException
Lambda.Client.exceptions.InvalidParameterValueException
Lambda.Client.exceptions.TooManyRequestsException
Lambda.Client.exceptions.CodeStorageExceededException
Lambda.Client.exceptions.PreconditionFailedException
Lambda.Client.exceptions.ResourceConflictException

Examples
The following example replaces the code of the unpublished ($LATEST) version of a function named my-function with the contents of the specified zip file in Amazon S3.
response = client.update_function_code(
    FunctionName='my-function',
    S3Bucket='my-bucket-1xpuxmplzrlbh',
    S3Key='function.zip',
)

print(response)


Expected Output:
{
    'CodeSha256': 'PFn4S+er27qk+UuZSTKEQfNKG/XNn7QJs90mJgq6oH8=',
    'CodeSize': 308,
    'Description': '',
    'FunctionArn': 'arn:aws:lambda:us-east-2:123456789012:function:my-function',
    'FunctionName': 'my-function',
    'Handler': 'index.handler',
    'LastModified': '2019-08-14T22:26:11.234+0000',
    'MemorySize': 128,
    'RevisionId': '873282ed-xmpl-4dc8-a069-d0c647e470c6',
    'Role': 'arn:aws:iam::123456789012:role/lambda-role',
    'Runtime': 'nodejs12.x',
    'Timeout': 3,
    'TracingConfig': {
        'Mode': 'PassThrough',
    },
    'Version': '$LATEST',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'FunctionName': 'string',
        'FunctionArn': 'string',
        'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'dotnetcore3.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'ruby2.7'|'provided',
        'Role': 'string',
        'Handler': 'string',
        'CodeSize': 123,
        'Description': 'string',
        'Timeout': 123,
        'MemorySize': 123,
        'LastModified': 'string',
        'CodeSha256': 'string',
        'Version': 'string',
        'VpcConfig': {
            'SubnetIds': [
                'string',
            ],
            'SecurityGroupIds': [
                'string',
            ],
            'VpcId': 'string'
        },
        'DeadLetterConfig': {
            'TargetArn': 'string'
        },
        'Environment': {
            'Variables': {
                'string': 'string'
            },
            'Error': {
                'ErrorCode': 'string',
                'Message': 'string'
            }
        },
        'KMSKeyArn': 'string',
        'TracingConfig': {
            'Mode': 'Active'|'PassThrough'
        },
        'MasterArn': 'string',
        'RevisionId': 'string',
        'Layers': [
            {
                'Arn': 'string',
                'CodeSize': 123
            },
        ],
        'State': 'Pending'|'Active'|'Inactive'|'Failed',
        'StateReason': 'string',
        'StateReasonCode': 'Idle'|'Creating'|'Restoring'|'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'|'SubnetOutOfIPAddresses'|'InvalidSubnet'|'InvalidSecurityGroup',
        'LastUpdateStatus': 'Successful'|'Failed'|'InProgress',
        'LastUpdateStatusReason': 'string',
        'LastUpdateStatusReasonCode': 'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'|'SubnetOutOfIPAddresses'|'InvalidSubnet'|'InvalidSecurityGroup'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_function_configuration(FunctionName=None, Role=None, Handler=None, Description=None, Timeout=None, MemorySize=None, VpcConfig=None, Environment=None, Runtime=None, DeadLetterConfig=None, KMSKeyArn=None, TracingConfig=None, RevisionId=None, Layers=None):
    """
    Modify the version-specific settings of a Lambda function.
    When you update a function, Lambda provisions an instance of the function and its supporting resources. If your function connects to a VPC, this process can take a minute. During this time, you can\'t modify the function, but you can still invoke it. The LastUpdateStatus , LastUpdateStatusReason , and LastUpdateStatusReasonCode fields in the response from  GetFunctionConfiguration indicate when the update is complete and the function is processing events with the new configuration. For more information, see Function States .
    These settings can vary between versions of a function and are locked when you publish a version. You can\'t modify the configuration of a published version, only the unpublished version.
    To configure function concurrency, use  PutFunctionConcurrency . To grant invoke permissions to an account or AWS service, use  AddPermission .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example modifies the memory size to be 256 MB for the unpublished ($LATEST) version of a function named my-function.
    Expected Output:
    
    :example: response = client.update_function_configuration(
        FunctionName='string',
        Role='string',
        Handler='string',
        Description='string',
        Timeout=123,
        MemorySize=123,
        VpcConfig={
            'SubnetIds': [
                'string',
            ],
            'SecurityGroupIds': [
                'string',
            ]
        },
        Environment={
            'Variables': {
                'string': 'string'
            }
        },
        Runtime='nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'dotnetcore3.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'ruby2.7'|'provided',
        DeadLetterConfig={
            'TargetArn': 'string'
        },
        KMSKeyArn='string',
        TracingConfig={
            'Mode': 'Active'|'PassThrough'
        },
        RevisionId='string',
        Layers=[
            'string',
        ]
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the Lambda function.\n\nName formats\n\nFunction name - my-function .\nFunction ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function .\nPartial ARN - 123456789012:function:my-function .\n\nThe length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.\n

    :type Role: string
    :param Role: The Amazon Resource Name (ARN) of the function\'s execution role.

    :type Handler: string
    :param Handler: The name of the method within your code that Lambda calls to execute your function. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime. For more information, see Programming Model .

    :type Description: string
    :param Description: A description of the function.

    :type Timeout: integer
    :param Timeout: The amount of time that Lambda allows a function to run before stopping it. The default is 3 seconds. The maximum allowed value is 900 seconds.

    :type MemorySize: integer
    :param MemorySize: The amount of memory that your function has access to. Increasing the function\'s memory also increases its CPU allocation. The default value is 128 MB. The value must be a multiple of 64 MB.

    :type VpcConfig: dict
    :param VpcConfig: For network connectivity to AWS resources in a VPC, specify a list of security groups and subnets in the VPC. When you connect a function to a VPC, it can only access resources and the internet through that VPC. For more information, see VPC Settings .\n\nSubnetIds (list) --A list of VPC subnet IDs.\n\n(string) --\n\n\nSecurityGroupIds (list) --A list of VPC security groups IDs.\n\n(string) --\n\n\n\n

    :type Environment: dict
    :param Environment: Environment variables that are accessible from function code during execution.\n\nVariables (dict) --Environment variable key-value pairs.\n\n(string) --\n(string) --\n\n\n\n\n\n

    :type Runtime: string
    :param Runtime: The identifier of the function\'s runtime .

    :type DeadLetterConfig: dict
    :param DeadLetterConfig: A dead letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing. For more information, see Dead Letter Queues .\n\nTargetArn (string) --The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.\n\n\n

    :type KMSKeyArn: string
    :param KMSKeyArn: The ARN of the AWS Key Management Service (AWS KMS) key that\'s used to encrypt your function\'s environment variables. If it\'s not provided, AWS Lambda uses a default service key.

    :type TracingConfig: dict
    :param TracingConfig: Set Mode to Active to sample and trace a subset of incoming requests with AWS X-Ray.\n\nMode (string) --The tracing mode.\n\n\n

    :type RevisionId: string
    :param RevisionId: Only update the function if the revision ID matches the ID that\'s specified. Use this option to avoid modifying a function that has changed since you last read it.

    :type Layers: list
    :param Layers: A list of function layers to add to the function\'s execution environment. Specify each layer by its ARN, including the version.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'FunctionName': 'string',
    'FunctionArn': 'string',
    'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'dotnetcore3.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'ruby2.7'|'provided',
    'Role': 'string',
    'Handler': 'string',
    'CodeSize': 123,
    'Description': 'string',
    'Timeout': 123,
    'MemorySize': 123,
    'LastModified': 'string',
    'CodeSha256': 'string',
    'Version': 'string',
    'VpcConfig': {
        'SubnetIds': [
            'string',
        ],
        'SecurityGroupIds': [
            'string',
        ],
        'VpcId': 'string'
    },
    'DeadLetterConfig': {
        'TargetArn': 'string'
    },
    'Environment': {
        'Variables': {
            'string': 'string'
        },
        'Error': {
            'ErrorCode': 'string',
            'Message': 'string'
        }
    },
    'KMSKeyArn': 'string',
    'TracingConfig': {
        'Mode': 'Active'|'PassThrough'
    },
    'MasterArn': 'string',
    'RevisionId': 'string',
    'Layers': [
        {
            'Arn': 'string',
            'CodeSize': 123
        },
    ],
    'State': 'Pending'|'Active'|'Inactive'|'Failed',
    'StateReason': 'string',
    'StateReasonCode': 'Idle'|'Creating'|'Restoring'|'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'|'SubnetOutOfIPAddresses'|'InvalidSubnet'|'InvalidSecurityGroup',
    'LastUpdateStatus': 'Successful'|'Failed'|'InProgress',
    'LastUpdateStatusReason': 'string',
    'LastUpdateStatusReasonCode': 'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'|'SubnetOutOfIPAddresses'|'InvalidSubnet'|'InvalidSecurityGroup'
}


Response Structure

(dict) --
Details about a function\'s configuration.

FunctionName (string) --
The name of the function.

FunctionArn (string) --
The function\'s Amazon Resource Name (ARN).

Runtime (string) --
The runtime environment for the Lambda function.

Role (string) --
The function\'s execution role.

Handler (string) --
The function that Lambda calls to begin executing your function.

CodeSize (integer) --
The size of the function\'s deployment package, in bytes.

Description (string) --
The function\'s description.

Timeout (integer) --
The amount of time in seconds that Lambda allows a function to run before stopping it.

MemorySize (integer) --
The memory that\'s allocated to the function.

LastModified (string) --
The date and time that the function was last updated, in ISO-8601 format (YYYY-MM-DDThh:mm:ss.sTZD).

CodeSha256 (string) --
The SHA256 hash of the function\'s deployment package.

Version (string) --
The version of the Lambda function.

VpcConfig (dict) --
The function\'s networking configuration.

SubnetIds (list) --
A list of VPC subnet IDs.

(string) --


SecurityGroupIds (list) --
A list of VPC security groups IDs.

(string) --


VpcId (string) --
The ID of the VPC.



DeadLetterConfig (dict) --
The function\'s dead letter queue.

TargetArn (string) --
The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.



Environment (dict) --
The function\'s environment variables.

Variables (dict) --
Environment variable key-value pairs.

(string) --
(string) --




Error (dict) --
Error messages for environment variables that couldn\'t be applied.

ErrorCode (string) --
The error code.

Message (string) --
The error message.





KMSKeyArn (string) --
The KMS key that\'s used to encrypt the function\'s environment variables. This key is only returned if you\'ve configured a customer managed CMK.

TracingConfig (dict) --
The function\'s AWS X-Ray tracing configuration.

Mode (string) --
The tracing mode.



MasterArn (string) --
For Lambda@Edge functions, the ARN of the master function.

RevisionId (string) --
The latest updated revision of the function or alias.

Layers (list) --
The function\'s layers .

(dict) --
An AWS Lambda layer .

Arn (string) --
The Amazon Resource Name (ARN) of the function layer.

CodeSize (integer) --
The size of the layer archive in bytes.





State (string) --
The current state of the function. When the state is Inactive , you can reactivate the function by invoking it.

StateReason (string) --
The reason for the function\'s current state.

StateReasonCode (string) --
The reason code for the function\'s current state. When the code is Creating , you can\'t invoke or modify the function.

LastUpdateStatus (string) --
The status of the last update that was performed on the function. This is first set to Successful after function creation completes.

LastUpdateStatusReason (string) --
The reason for the last update that was performed on the function.

LastUpdateStatusReasonCode (string) --
The reason code for the last update that was performed on the function.







Exceptions

Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.ResourceNotFoundException
Lambda.Client.exceptions.InvalidParameterValueException
Lambda.Client.exceptions.TooManyRequestsException
Lambda.Client.exceptions.ResourceConflictException
Lambda.Client.exceptions.PreconditionFailedException

Examples
The following example modifies the memory size to be 256 MB for the unpublished ($LATEST) version of a function named my-function.
response = client.update_function_configuration(
    FunctionName='my-function',
    MemorySize=256,
)

print(response)


Expected Output:
{
    'CodeSha256': 'PFn4S+er27qk+UuZSTKEQfNKG/XNn7QJs90mJgq6oH8=',
    'CodeSize': 308,
    'Description': '',
    'FunctionArn': 'arn:aws:lambda:us-east-2:123456789012:function:my-function',
    'FunctionName': 'my-function',
    'Handler': 'index.handler',
    'LastModified': '2019-08-14T22:26:11.234+0000',
    'MemorySize': 256,
    'RevisionId': '873282ed-xmpl-4dc8-a069-d0c647e470c6',
    'Role': 'arn:aws:iam::123456789012:role/lambda-role',
    'Runtime': 'nodejs12.x',
    'Timeout': 3,
    'TracingConfig': {
        'Mode': 'PassThrough',
    },
    'Version': '$LATEST',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'FunctionName': 'string',
        'FunctionArn': 'string',
        'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'dotnetcore3.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'ruby2.7'|'provided',
        'Role': 'string',
        'Handler': 'string',
        'CodeSize': 123,
        'Description': 'string',
        'Timeout': 123,
        'MemorySize': 123,
        'LastModified': 'string',
        'CodeSha256': 'string',
        'Version': 'string',
        'VpcConfig': {
            'SubnetIds': [
                'string',
            ],
            'SecurityGroupIds': [
                'string',
            ],
            'VpcId': 'string'
        },
        'DeadLetterConfig': {
            'TargetArn': 'string'
        },
        'Environment': {
            'Variables': {
                'string': 'string'
            },
            'Error': {
                'ErrorCode': 'string',
                'Message': 'string'
            }
        },
        'KMSKeyArn': 'string',
        'TracingConfig': {
            'Mode': 'Active'|'PassThrough'
        },
        'MasterArn': 'string',
        'RevisionId': 'string',
        'Layers': [
            {
                'Arn': 'string',
                'CodeSize': 123
            },
        ],
        'State': 'Pending'|'Active'|'Inactive'|'Failed',
        'StateReason': 'string',
        'StateReasonCode': 'Idle'|'Creating'|'Restoring'|'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'|'SubnetOutOfIPAddresses'|'InvalidSubnet'|'InvalidSecurityGroup',
        'LastUpdateStatus': 'Successful'|'Failed'|'InProgress',
        'LastUpdateStatusReason': 'string',
        'LastUpdateStatusReasonCode': 'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'|'SubnetOutOfIPAddresses'|'InvalidSubnet'|'InvalidSecurityGroup'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_function_event_invoke_config(FunctionName=None, Qualifier=None, MaximumRetryAttempts=None, MaximumEventAgeInSeconds=None, DestinationConfig=None):
    """
    Updates the configuration for asynchronous invocation for a function, version, or alias.
    To configure options for asynchronous invocation, use  PutFunctionEventInvokeConfig .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example adds an on-failure destination to the existing asynchronous invocation configuration for a function named my-function.
    Expected Output:
    
    :example: response = client.update_function_event_invoke_config(
        FunctionName='string',
        Qualifier='string',
        MaximumRetryAttempts=123,
        MaximumEventAgeInSeconds=123,
        DestinationConfig={
            'OnSuccess': {
                'Destination': 'string'
            },
            'OnFailure': {
                'Destination': 'string'
            }
        }
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the Lambda function, version, or alias.\n\nName formats\n\nFunction name - my-function (name-only), my-function:v1 (with alias).\nFunction ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function .\nPartial ARN - 123456789012:function:my-function .\n\nYou can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.\n

    :type Qualifier: string
    :param Qualifier: A version number or alias name.

    :type MaximumRetryAttempts: integer
    :param MaximumRetryAttempts: The maximum number of times to retry when the function returns an error.

    :type MaximumEventAgeInSeconds: integer
    :param MaximumEventAgeInSeconds: The maximum age of a request that Lambda sends to a function for processing.

    :type DestinationConfig: dict
    :param DestinationConfig: A destination for events after they have been sent to a function for processing.\n\nDestinations\n\nFunction - The Amazon Resource Name (ARN) of a Lambda function.\nQueue - The ARN of an SQS queue.\nTopic - The ARN of an SNS topic.\nEvent Bus - The ARN of an Amazon EventBridge event bus.\n\n\nOnSuccess (dict) --The destination configuration for successful invocations.\n\nDestination (string) --The Amazon Resource Name (ARN) of the destination resource.\n\n\n\nOnFailure (dict) --The destination configuration for failed invocations.\n\nDestination (string) --The Amazon Resource Name (ARN) of the destination resource.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'LastModified': datetime(2015, 1, 1),
    'FunctionArn': 'string',
    'MaximumRetryAttempts': 123,
    'MaximumEventAgeInSeconds': 123,
    'DestinationConfig': {
        'OnSuccess': {
            'Destination': 'string'
        },
        'OnFailure': {
            'Destination': 'string'
        }
    }
}


Response Structure

(dict) --

LastModified (datetime) --
The date and time that the configuration was last updated.

FunctionArn (string) --
The Amazon Resource Name (ARN) of the function.

MaximumRetryAttempts (integer) --
The maximum number of times to retry when the function returns an error.

MaximumEventAgeInSeconds (integer) --
The maximum age of a request that Lambda sends to a function for processing.

DestinationConfig (dict) --
A destination for events after they have been sent to a function for processing.

Destinations


Function - The Amazon Resource Name (ARN) of a Lambda function.
Queue - The ARN of an SQS queue.
Topic - The ARN of an SNS topic.
Event Bus - The ARN of an Amazon EventBridge event bus.


OnSuccess (dict) --
The destination configuration for successful invocations.

Destination (string) --
The Amazon Resource Name (ARN) of the destination resource.



OnFailure (dict) --
The destination configuration for failed invocations.

Destination (string) --
The Amazon Resource Name (ARN) of the destination resource.











Exceptions

Lambda.Client.exceptions.ServiceException
Lambda.Client.exceptions.ResourceNotFoundException
Lambda.Client.exceptions.InvalidParameterValueException
Lambda.Client.exceptions.TooManyRequestsException

Examples
The following example adds an on-failure destination to the existing asynchronous invocation configuration for a function named my-function.
response = client.update_function_event_invoke_config(
    DestinationConfig={
        'OnFailure': {
            'Destination': 'arn:aws:sqs:us-east-2:123456789012:destination',
        },
    },
    FunctionName='my-function',
)

print(response)


Expected Output:
{
    'DestinationConfig': {
        'OnFailure': {
            'Destination': 'arn:aws:sqs:us-east-2:123456789012:destination',
        },
        'OnSuccess': {
        },
    },
    'FunctionArn': 'arn:aws:lambda:us-east-2:123456789012:function:my-function:$LATEST',
    'LastModified': 1573687896.493,
    'MaximumEventAgeInSeconds': 3600,
    'MaximumRetryAttempts': 0,
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'LastModified': datetime(2015, 1, 1),
        'FunctionArn': 'string',
        'MaximumRetryAttempts': 123,
        'MaximumEventAgeInSeconds': 123,
        'DestinationConfig': {
            'OnSuccess': {
                'Destination': 'string'
            },
            'OnFailure': {
                'Destination': 'string'
            }
        }
    }
    
    
    :returns: 
    Function - The Amazon Resource Name (ARN) of a Lambda function.
    Queue - The ARN of an SQS queue.
    Topic - The ARN of an SNS topic.
    Event Bus - The ARN of an Amazon EventBridge event bus.
    
    """
    pass

