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


def add_permission(FunctionName=None, StatementId=None, Action=None, Principal=None, SourceArn=None, SourceAccount=None,
                   EventSourceToken=None, Qualifier=None):
    """
    :param FunctionName: [REQUIRED]
            Name of the Lambda function whose resource policy you are updating by adding a new permission.
            You can specify a function name (for example, Thumbnail ) or you can specify Amazon Resource Name (ARN) of the function (for example, arn:aws:lambda:us-west-2:account-id:function:ThumbNail ). AWS Lambda also allows you to specify partial ARN (for example, account-id:Thumbnail ). Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 character in length.
            
    :type FunctionName: string
    :param StatementId: [REQUIRED]
            A unique statement identifier.
            
    :type StatementId: string
    :param Action: [REQUIRED]
            The AWS Lambda action you want to allow in this statement. Each Lambda action is a string starting with lambda: followed by the API name . For example, lambda:CreateFunction . You can use wildcard (lambda:* ) to grant permission for all AWS Lambda actions.
            
    :type Action: string
    :param Principal: [REQUIRED]
            The principal who is getting this permission. It can be Amazon S3 service Principal (s3.amazonaws.com ) if you want Amazon S3 to invoke the function, an AWS account ID if you are granting cross-account permission, or any valid AWS service principal such as sns.amazonaws.com . For example, you might want to allow a custom application in another AWS account to push events to AWS Lambda by invoking your function.
            
    :type Principal: string
    :param SourceArn: This is optional; however, when granting Amazon S3 permission to invoke your function, you should specify this field with the Amazon Resource Name (ARN) as its value. This ensures that only events generated from the specified source can invoke the function.
            Warning
            If you add a permission for the Amazon S3 principal without providing the source ARN, any AWS account that creates a mapping to your function ARN can send events to invoke your Lambda function from Amazon S3.
            
    :type SourceArn: string
    :param SourceAccount: This parameter is used for S3 and SES only. The AWS account ID (without a hyphen) of the source owner. For example, if the SourceArn identifies a bucket, then this is the bucket owner's account ID. You can use this additional condition to ensure the bucket you specify is owned by a specific account (it is possible the bucket owner deleted the bucket and some other AWS account created the bucket). You can also use this condition to specify all sources (that is, you don't specify the SourceArn ) owned by a specific account.
    :type SourceAccount: string
    :param EventSourceToken: A unique token that must be supplied by the principal invoking the function. This is currently only used for Alexa Smart Home functions.
    :type EventSourceToken: string
    :param Qualifier: You can use this optional query parameter to describe a qualified ARN using a function version or an alias name. The permission will then apply to the specific qualified ARN. For example, if you specify function version 2 as the qualifier, then permission applies only when request is made using qualified function ARN:
            arn:aws:lambda:aws-region:acct-id:function:function-name:2
            If you specify an alias name, for example PROD , then the permission is valid only for requests made using the alias ARN:
            arn:aws:lambda:aws-region:acct-id:function:function-name:PROD
            If the qualifier is not specified, the permission is valid only when requests is made using unqualified function ARN.
            arn:aws:lambda:aws-region:acct-id:function:function-name
            
    :type Qualifier: string
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


def create_alias(FunctionName=None, Name=None, FunctionVersion=None, Description=None):
    """
    :param FunctionName: [REQUIRED]
            Name of the Lambda function for which you want to create an alias.
            
    :type FunctionName: string
    :param Name: [REQUIRED]
            Name for the alias you are creating.
            
    :type Name: string
    :param FunctionVersion: [REQUIRED]
            Lambda function version for which you are creating the alias.
            
    :type FunctionVersion: string
    :param Description: Description of the alias.
    :type Description: string
    """
    pass


def create_event_source_mapping(EventSourceArn=None, FunctionName=None, Enabled=None, BatchSize=None,
                                StartingPosition=None):
    """
    :param EventSourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the Amazon Kinesis or the Amazon DynamoDB stream that is the event source. Any record added to this stream could cause AWS Lambda to invoke your Lambda function, it depends on the BatchSize . AWS Lambda POSTs the Amazon Kinesis event, containing records, to your Lambda function as JSON.
            
    :type EventSourceArn: string
    :param FunctionName: [REQUIRED]
            The Lambda function to invoke when AWS Lambda detects an event on the stream.
            You can specify the function name (for example, Thumbnail ) or you can specify Amazon Resource Name (ARN) of the function (for example, arn:aws:lambda:us-west-2:account-id:function:ThumbNail ).
            If you are using versioning, you can also provide a qualified function ARN (ARN that is qualified with function version or alias name as suffix). For more information about versioning, see AWS Lambda Function Versioning and Aliases
            AWS Lambda also allows you to specify only the function name with the account ID qualifier (for example, account-id:Thumbnail ).
            Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 character in length.
            
    :type FunctionName: string
    :param Enabled: Indicates whether AWS Lambda should begin polling the event source. By default, Enabled is true.
    :type Enabled: boolean
    :param BatchSize: The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function. Your function receives an event with all the retrieved records. The default is 100 records.
    :type BatchSize: integer
    :param StartingPosition: [REQUIRED]
            The position in the stream where AWS Lambda should start reading. For more information, go to ShardIteratorType in the Amazon Kinesis API Reference .
            
    :type StartingPosition: string
    """
    pass


def create_function(FunctionName=None, Runtime=None, Role=None, Handler=None, Code=None, Description=None, Timeout=None,
                    MemorySize=None, Publish=None, VpcConfig=None):
    """
    :param FunctionName: [REQUIRED]
            The name you want to assign to the function you are uploading. The function names appear in the console and are returned in the ListFunctions API. Function names are used to specify functions to other AWS Lambda APIs, such as Invoke .
            
    :type FunctionName: string
    :param Runtime: [REQUIRED]
            The runtime environment for the Lambda function you are uploading.
            To use the Node.js runtime v4.3, set the value to 'nodejs4.3'. To use earlier runtime (v0.10.42), set the value to 'nodejs'.
            
    :type Runtime: string
    :param Role: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM role that Lambda assumes when it executes your function to access any other Amazon Web Services (AWS) resources. For more information, see AWS Lambda: How it Works .
            
    :type Role: string
    :param Handler: [REQUIRED]
            The function within your code that Lambda calls to begin execution. For Node.js, it is the module-name .*export* value in your function. For Java, it can be package.class-name::handler or package.class-name . For more information, see Lambda Function Handler (Java) .
            
    :type Handler: string
    :param Code: [REQUIRED]
            The code for the Lambda function.
            ZipFile (bytes) --The contents of your zip file containing your deployment package. If you are using the web API directly, the contents of the zip file must be base64-encoded. If you are using the AWS SDKs or the AWS CLI, the SDKs or CLI will do the encoding for you. For more information about creating a .zip file, go to Execution Permissions in the AWS Lambda Developer Guide .
            S3Bucket (string) --Amazon S3 bucket name where the .zip file containing your deployment package is stored. This bucket must reside in the same AWS region where you are creating the Lambda function.
            S3Key (string) --The Amazon S3 object (the deployment package) key name you want to upload.
            S3ObjectVersion (string) --The Amazon S3 object (the deployment package) version you want to upload.
            
    :type Code: dict
    :param Description: A short, user-defined function description. Lambda does not use this value. Assign a meaningful description as you see fit.
    :type Description: string
    :param Timeout: The function execution time at which Lambda should terminate the function. Because the execution time has cost implications, we recommend you set this value based on your expected execution time. The default is 3 seconds.
    :type Timeout: integer
    :param MemorySize: The amount of memory, in MB, your Lambda function is given. Lambda uses this memory size to infer the amount of CPU and memory allocated to your function. Your function use-case determines your CPU and memory requirements. For example, a database operation might need less memory compared to an image processing function. The default value is 128 MB. The value must be a multiple of 64 MB.
    :type MemorySize: integer
    :param Publish: This boolean parameter can be used to request AWS Lambda to create the Lambda function and publish a version as an atomic operation.
    :type Publish: boolean
    :param VpcConfig: If your Lambda function accesses resources in a VPC, you provide this parameter identifying the list of security group IDs and subnet IDs. These must belong to the same VPC. You must provide at least one security group and one subnet ID.
            SubnetIds (list) --A list of one or more subnet IDs in your VPC.
            (string) --
            SecurityGroupIds (list) --A list of one or more security groups IDs in your VPC.
            (string) --
            
    :type VpcConfig: dict
    """
    pass


def delete_alias(FunctionName=None, Name=None):
    """
    :param FunctionName: [REQUIRED]
            The Lambda function name for which the alias is created. Deleting an alias does not delete the function version to which it is pointing.
            
    :type FunctionName: string
    :param Name: [REQUIRED]
            Name of the alias to delete.
            
    :type Name: string
    """
    pass


def delete_event_source_mapping(UUID=None):
    """
    :param UUID: [REQUIRED]
            The event source mapping ID.
            Return typedict
            ReturnsResponse Syntax{
              'UUID': 'string',
              'BatchSize': 123,
              'EventSourceArn': 'string',
              'FunctionArn': 'string',
              'LastModified': datetime(2015, 1, 1),
              'LastProcessingResult': 'string',
              'State': 'string',
              'StateTransitionReason': 'string'
            }
            Response Structure
            (dict) --Describes mapping between an Amazon Kinesis stream and a Lambda function.
            UUID (string) --The AWS Lambda assigned opaque identifier for the mapping.
            BatchSize (integer) --The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function. Your function receives an event with all the retrieved records.
            EventSourceArn (string) --The Amazon Resource Name (ARN) of the Amazon Kinesis stream that is the source of events.
            FunctionArn (string) --The Lambda function to invoke when AWS Lambda detects an event on the stream.
            LastModified (datetime) --The UTC time string indicating the last time the event mapping was updated.
            LastProcessingResult (string) --The result of the last AWS Lambda invocation of your Lambda function.
            State (string) --The state of the event source mapping. It can be Creating , Enabled , Disabled , Enabling , Disabling , Updating , or Deleting .
            StateTransitionReason (string) --The reason the event source mapping is in its current state. It is either user-requested or an AWS Lambda-initiated state transition.
            
            
    :type UUID: string
    """
    pass


def delete_function(FunctionName=None, Qualifier=None):
    """
    :param FunctionName: [REQUIRED]
            The Lambda function to delete.
            You can specify the function name (for example, Thumbnail ) or you can specify Amazon Resource Name (ARN) of the function (for example, arn:aws:lambda:us-west-2:account-id:function:ThumbNail ). If you are using versioning, you can also provide a qualified function ARN (ARN that is qualified with function version or alias name as suffix). AWS Lambda also allows you to specify only the function name with the account ID qualifier (for example, account-id:Thumbnail ). Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 character in length.
            
    :type FunctionName: string
    :param Qualifier: Using this optional parameter you can specify a function version (but not the $LATEST version) to direct AWS Lambda to delete a specific function version. If the function version has one or more aliases pointing to it, you will get an error because you cannot have aliases pointing to it. You can delete any function version but not the $LATEST , that is, you cannot specify $LATEST as the value of this parameter. The $LATEST version can be deleted only when you want to delete all the function versions and aliases.
            You can only specify a function version, not an alias name, using this parameter. You cannot delete a function version using its alias.
            If you don't specify this parameter, AWS Lambda will delete the function, including all of its versions and aliases.
            
    :type Qualifier: string
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


def get_alias(FunctionName=None, Name=None):
    """
    :param FunctionName: [REQUIRED]
            Function name for which the alias is created. An alias is a subresource that exists only in the context of an existing Lambda function so you must specify the function name.
            
    :type FunctionName: string
    :param Name: [REQUIRED]
            Name of the alias for which you want to retrieve information.
            
    :type Name: string
    """
    pass


def get_event_source_mapping(UUID=None):
    """
    :param UUID: [REQUIRED]
            The AWS Lambda assigned ID of the event source mapping.
            Return typedict
            ReturnsResponse Syntax{
              'UUID': 'string',
              'BatchSize': 123,
              'EventSourceArn': 'string',
              'FunctionArn': 'string',
              'LastModified': datetime(2015, 1, 1),
              'LastProcessingResult': 'string',
              'State': 'string',
              'StateTransitionReason': 'string'
            }
            Response Structure
            (dict) --Describes mapping between an Amazon Kinesis stream and a Lambda function.
            UUID (string) --The AWS Lambda assigned opaque identifier for the mapping.
            BatchSize (integer) --The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function. Your function receives an event with all the retrieved records.
            EventSourceArn (string) --The Amazon Resource Name (ARN) of the Amazon Kinesis stream that is the source of events.
            FunctionArn (string) --The Lambda function to invoke when AWS Lambda detects an event on the stream.
            LastModified (datetime) --The UTC time string indicating the last time the event mapping was updated.
            LastProcessingResult (string) --The result of the last AWS Lambda invocation of your Lambda function.
            State (string) --The state of the event source mapping. It can be Creating , Enabled , Disabled , Enabling , Disabling , Updating , or Deleting .
            StateTransitionReason (string) --The reason the event source mapping is in its current state. It is either user-requested or an AWS Lambda-initiated state transition.
            
            
    :type UUID: string
    """
    pass


def get_function(FunctionName=None, Qualifier=None):
    """
    :param FunctionName: [REQUIRED]
            The Lambda function name.
            You can specify a function name (for example, Thumbnail ) or you can specify Amazon Resource Name (ARN) of the function (for example, arn:aws:lambda:us-west-2:account-id:function:ThumbNail ). AWS Lambda also allows you to specify a partial ARN (for example, account-id:Thumbnail ). Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 character in length.
            
    :type FunctionName: string
    :param Qualifier: Using this optional parameter to specify a function version or an alias name. If you specify function version, the API uses qualified function ARN for the request and returns information about the specific Lambda function version. If you specify an alias name, the API uses the alias ARN and returns information about the function version to which the alias points. If you don't provide this parameter, the API uses unqualified function ARN and returns information about the $LATEST version of the Lambda function.
    :type Qualifier: string
    """
    pass


def get_function_configuration(FunctionName=None, Qualifier=None):
    """
    :param FunctionName: [REQUIRED]
            The name of the Lambda function for which you want to retrieve the configuration information.
            You can specify a function name (for example, Thumbnail ) or you can specify Amazon Resource Name (ARN) of the function (for example, arn:aws:lambda:us-west-2:account-id:function:ThumbNail ). AWS Lambda also allows you to specify a partial ARN (for example, account-id:Thumbnail ). Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 character in length.
            
    :type FunctionName: string
    :param Qualifier: Using this optional parameter you can specify a function version or an alias name. If you specify function version, the API uses qualified function ARN and returns information about the specific function version. If you specify an alias name, the API uses the alias ARN and returns information about the function version to which the alias points.
            If you don't specify this parameter, the API uses unqualified function ARN, and returns information about the $LATEST function version.
            
    :type Qualifier: string
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


def get_policy(FunctionName=None, Qualifier=None):
    """
    :param FunctionName: [REQUIRED]
            Function name whose resource policy you want to retrieve.
            You can specify the function name (for example, Thumbnail ) or you can specify Amazon Resource Name (ARN) of the function (for example, arn:aws:lambda:us-west-2:account-id:function:ThumbNail ). If you are using versioning, you can also provide a qualified function ARN (ARN that is qualified with function version or alias name as suffix). AWS Lambda also allows you to specify only the function name with the account ID qualifier (for example, account-id:Thumbnail ). Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 character in length.
            
    :type FunctionName: string
    :param Qualifier: You can specify this optional query parameter to specify a function version or an alias name in which case this API will return all permissions associated with the specific qualified ARN. If you don't provide this parameter, the API will return permissions that apply to the unqualified function ARN.
    :type Qualifier: string
    """
    pass


def get_waiter():
    """
    """
    pass


def invoke(FunctionName=None, InvocationType=None, LogType=None, ClientContext=None, Payload=None, Qualifier=None):
    """
    :param FunctionName: [REQUIRED]
            The Lambda function name.
            You can specify a function name (for example, Thumbnail ) or you can specify Amazon Resource Name (ARN) of the function (for example, arn:aws:lambda:us-west-2:account-id:function:ThumbNail ). AWS Lambda also allows you to specify a partial ARN (for example, account-id:Thumbnail ). Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 character in length.
            
    :type FunctionName: string
    :param InvocationType: By default, the Invoke API assumes RequestResponse invocation type. You can optionally request asynchronous execution by specifying Event as the InvocationType . You can also use this parameter to request AWS Lambda to not execute the function but do some verification, such as if the caller is authorized to invoke the function and if the inputs are valid. You request this by specifying DryRun as the InvocationType . This is useful in a cross-account scenario when you want to verify access to a function without running it.
    :type InvocationType: string
    :param LogType: You can set this optional parameter to Tail in the request only if you specify the InvocationType parameter with value RequestResponse . In this case, AWS Lambda returns the base64-encoded last 4 KB of log data produced by your Lambda function in the x-amz-log-result header.
    :type LogType: string
    :param ClientContext: Using the ClientContext you can pass client-specific information to the Lambda function you are invoking. You can then process the client information in your Lambda function as you choose through the context variable. For an example of a ClientContext JSON, see PutEvents in the Amazon Mobile Analytics API Reference and User Guide .
            The ClientContext JSON must be base64-encoded.
            
    :type ClientContext: string
    :param Payload: JSON that you want to provide to your Lambda function as input.
    :type Payload: bytes or seekable file-like object
    :param Qualifier: You can use this optional parameter to specify a Lambda function version or alias name. If you specify a function version, the API uses the qualified function ARN to invoke a specific Lambda function. If you specify an alias name, the API uses the alias ARN to invoke the Lambda function version to which the alias points.
            If you don't provide this parameter, then the API uses unqualified function ARN which results in invocation of the $LATEST version.
            
    :type Qualifier: string
    """
    pass


def invoke_async(FunctionName=None, InvokeArgs=None):
    """
    :param FunctionName: [REQUIRED]
            The Lambda function name.
            
    :type FunctionName: string
    :param InvokeArgs: [REQUIRED]
            JSON that you want to provide to your Lambda function as input.
            
    :type InvokeArgs: bytes or seekable file-like object
    """
    pass


def list_aliases(FunctionName=None, FunctionVersion=None, Marker=None, MaxItems=None):
    """
    :param FunctionName: [REQUIRED]
            Lambda function name for which the alias is created.
            
    :type FunctionName: string
    :param FunctionVersion: If you specify this optional parameter, the API returns only the aliases that are pointing to the specific Lambda function version, otherwise the API returns all of the aliases created for the Lambda function.
    :type FunctionVersion: string
    :param Marker: Optional string. An opaque pagination token returned from a previous ListAliases operation. If present, indicates where to continue the listing.
    :type Marker: string
    :param MaxItems: Optional integer. Specifies the maximum number of aliases to return in response. This parameter value must be greater than 0.
    :type MaxItems: integer
    """
    pass


def list_event_source_mappings(EventSourceArn=None, FunctionName=None, Marker=None, MaxItems=None):
    """
    :param EventSourceArn: The Amazon Resource Name (ARN) of the Amazon Kinesis stream. (This parameter is optional.)
    :type EventSourceArn: string
    :param FunctionName: The name of the Lambda function.
            You can specify the function name (for example, Thumbnail ) or you can specify Amazon Resource Name (ARN) of the function (for example, arn:aws:lambda:us-west-2:account-id:function:ThumbNail ). If you are using versioning, you can also provide a qualified function ARN (ARN that is qualified with function version or alias name as suffix). AWS Lambda also allows you to specify only the function name with the account ID qualifier (for example, account-id:Thumbnail ). Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 character in length.
            
    :type FunctionName: string
    :param Marker: Optional string. An opaque pagination token returned from a previous ListEventSourceMappings operation. If present, specifies to continue the list from where the returning call left off.
    :type Marker: string
    :param MaxItems: Optional integer. Specifies the maximum number of event sources to return in response. This value must be greater than 0.
    :type MaxItems: integer
    """
    pass


def list_functions(Marker=None, MaxItems=None):
    """
    :param Marker: Optional string. An opaque pagination token returned from a previous ListFunctions operation. If present, indicates where to continue the listing.
    :type Marker: string
    :param MaxItems: Optional integer. Specifies the maximum number of AWS Lambda functions to return in response. This parameter value must be greater than 0.
    :type MaxItems: integer
    """
    pass


def list_versions_by_function(FunctionName=None, Marker=None, MaxItems=None):
    """
    :param FunctionName: [REQUIRED]
            Function name whose versions to list. You can specify a function name (for example, Thumbnail ) or you can specify Amazon Resource Name (ARN) of the function (for example, arn:aws:lambda:us-west-2:account-id:function:ThumbNail ). AWS Lambda also allows you to specify a partial ARN (for example, account-id:Thumbnail ). Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 character in length.
            
    :type FunctionName: string
    :param Marker: Optional string. An opaque pagination token returned from a previous ListVersionsByFunction operation. If present, indicates where to continue the listing.
    :type Marker: string
    :param MaxItems: Optional integer. Specifies the maximum number of AWS Lambda function versions to return in response. This parameter value must be greater than 0.
    :type MaxItems: integer
    """
    pass


def publish_version(FunctionName=None, CodeSha256=None, Description=None):
    """
    :param FunctionName: [REQUIRED]
            The Lambda function name. You can specify a function name (for example, Thumbnail ) or you can specify Amazon Resource Name (ARN) of the function (for example, arn:aws:lambda:us-west-2:account-id:function:ThumbNail ). AWS Lambda also allows you to specify a partial ARN (for example, account-id:Thumbnail ). Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 character in length.
            
    :type FunctionName: string
    :param CodeSha256: The SHA256 hash of the deployment package you want to publish. This provides validation on the code you are publishing. If you provide this parameter value must match the SHA256 of the $LATEST version for the publication to succeed.
    :type CodeSha256: string
    :param Description: The description for the version you are publishing. If not provided, AWS Lambda copies the description from the $LATEST version.
    :type Description: string
    """
    pass


def remove_permission(FunctionName=None, StatementId=None, Qualifier=None):
    """
    :param FunctionName: [REQUIRED]
            Lambda function whose resource policy you want to remove a permission from.
            You can specify a function name (for example, Thumbnail ) or you can specify Amazon Resource Name (ARN) of the function (for example, arn:aws:lambda:us-west-2:account-id:function:ThumbNail ). AWS Lambda also allows you to specify a partial ARN (for example, account-id:Thumbnail ). Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 character in length.
            
    :type FunctionName: string
    :param StatementId: [REQUIRED]
            Statement ID of the permission to remove.
            
    :type StatementId: string
    :param Qualifier: You can specify this optional parameter to remove permission associated with a specific function version or function alias. If you don't specify this parameter, the API removes permission associated with the unqualified function ARN.
    :type Qualifier: string
    """
    pass


def update_alias(FunctionName=None, Name=None, FunctionVersion=None, Description=None):
    """
    :param FunctionName: [REQUIRED]
            The function name for which the alias is created.
            
    :type FunctionName: string
    :param Name: [REQUIRED]
            The alias name.
            
    :type Name: string
    :param FunctionVersion: Using this parameter you can change the Lambda function version to which the alias points.
    :type FunctionVersion: string
    :param Description: You can change the description of the alias using this parameter.
    :type Description: string
    """
    pass


def update_event_source_mapping(UUID=None, FunctionName=None, Enabled=None, BatchSize=None):
    """
    :param UUID: [REQUIRED]
            The event source mapping identifier.
            
    :type UUID: string
    :param FunctionName: The Lambda function to which you want the stream records sent.
            You can specify a function name (for example, Thumbnail ) or you can specify Amazon Resource Name (ARN) of the function (for example, arn:aws:lambda:us-west-2:account-id:function:ThumbNail ). AWS Lambda also allows you to specify a partial ARN (for example, account-id:Thumbnail ).
            If you are using versioning, you can also provide a qualified function ARN (ARN that is qualified with function version or alias name as suffix). For more information about versioning, see AWS Lambda Function Versioning and Aliases
            Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 character in length.
            
    :type FunctionName: string
    :param Enabled: Specifies whether AWS Lambda should actively poll the stream or not. If disabled, AWS Lambda will not poll the stream.
    :type Enabled: boolean
    :param BatchSize: The maximum number of stream records that can be sent to your Lambda function for a single invocation.
    :type BatchSize: integer
    """
    pass


def update_function_code(FunctionName=None, ZipFile=None, S3Bucket=None, S3Key=None, S3ObjectVersion=None,
                         Publish=None):
    """
    :param FunctionName: [REQUIRED]
            The existing Lambda function name whose code you want to replace.
            You can specify a function name (for example, Thumbnail ) or you can specify Amazon Resource Name (ARN) of the function (for example, arn:aws:lambda:us-west-2:account-id:function:ThumbNail ). AWS Lambda also allows you to specify a partial ARN (for example, account-id:Thumbnail ). Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 character in length.
            
    :type FunctionName: string
    :param ZipFile: The contents of your zip file containing your deployment package. If you are using the web API directly, the contents of the zip file must be base64-encoded. If you are using the AWS SDKs or the AWS CLI, the SDKs or CLI will do the encoding for you. For more information about creating a .zip file, go to Execution Permissions in the AWS Lambda Developer Guide .
            This value will be base64 encoded automatically. Do not base64 encode this value prior to performing the operation.
            
    :type ZipFile: bytes
    :param S3Bucket: Amazon S3 bucket name where the .zip file containing your deployment package is stored. This bucket must reside in the same AWS region where you are creating the Lambda function.
    :type S3Bucket: string
    :param S3Key: The Amazon S3 object (the deployment package) key name you want to upload.
    :type S3Key: string
    :param S3ObjectVersion: The Amazon S3 object (the deployment package) version you want to upload.
    :type S3ObjectVersion: string
    :param Publish: This boolean parameter can be used to request AWS Lambda to update the Lambda function and publish a version as an atomic operation.
    :type Publish: boolean
    """
    pass


def update_function_configuration(FunctionName=None, Role=None, Handler=None, Description=None, Timeout=None,
                                  MemorySize=None, VpcConfig=None, Runtime=None):
    """
    :param FunctionName: [REQUIRED]
            The name of the Lambda function.
            You can specify a function name (for example, Thumbnail ) or you can specify Amazon Resource Name (ARN) of the function (for example, arn:aws:lambda:us-west-2:account-id:function:ThumbNail ). AWS Lambda also allows you to specify a partial ARN (for example, account-id:Thumbnail ). Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 character in length.
            
    :type FunctionName: string
    :param Role: The Amazon Resource Name (ARN) of the IAM role that Lambda will assume when it executes your function.
    :type Role: string
    :param Handler: The function that Lambda calls to begin executing your function. For Node.js, it is the module-name.export value in your function.
    :type Handler: string
    :param Description: A short user-defined function description. AWS Lambda does not use this value. Assign a meaningful description as you see fit.
    :type Description: string
    :param Timeout: The function execution time at which AWS Lambda should terminate the function. Because the execution time has cost implications, we recommend you set this value based on your expected execution time. The default is 3 seconds.
    :type Timeout: integer
    :param MemorySize: The amount of memory, in MB, your Lambda function is given. AWS Lambda uses this memory size to infer the amount of CPU allocated to your function. Your function use-case determines your CPU and memory requirements. For example, a database operation might need less memory compared to an image processing function. The default value is 128 MB. The value must be a multiple of 64 MB.
    :type MemorySize: integer
    :param VpcConfig: If your Lambda function accesses resources in a VPC, you provide this parameter identifying the list of security group IDs and subnet IDs. These must belong to the same VPC. You must provide at least one security group and one subnet ID.
            SubnetIds (list) --A list of one or more subnet IDs in your VPC.
            (string) --
            SecurityGroupIds (list) --A list of one or more security groups IDs in your VPC.
            (string) --
            
    :type VpcConfig: dict
    :param Runtime: The runtime environment for the Lambda function.
            To use the Node.js runtime v4.3, set the value to 'nodejs4.3'. To use earlier runtime (v0.10.42), set the value to 'nodejs'.
            
    :type Runtime: string
    """
    pass
