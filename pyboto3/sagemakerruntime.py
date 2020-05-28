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
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

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

def get_waiter(waiter_name=None):
    """
    Returns an object that can wait for some condition.
    
    :type waiter_name: str
    :param waiter_name: The name of the waiter to get. See the waiters\nsection of the service docs for a list of available waiters.

    :rtype: botocore.waiter.Waiter


    """
    pass

def invoke_endpoint(EndpointName=None, Body=None, ContentType=None, Accept=None, CustomAttributes=None, TargetModel=None):
    """
    After you deploy a model into production using Amazon SageMaker hosting services, your client applications use this API to get inferences from the model hosted at the specified endpoint.
    For an overview of Amazon SageMaker, see How It Works .
    Amazon SageMaker strips all POST headers except those supported by the API. Amazon SageMaker might add additional headers. You should not rely on the behavior of headers outside those enumerated in the request syntax.
    Calls to InvokeEndpoint are authenticated by using AWS Signature Version 4. For information, see Authenticating Requests (AWS Signature Version 4) in the Amazon S3 API Reference .
    A customer\'s model containers must respond to requests within 60 seconds. The model itself can have a maximum processing time of 60 seconds before responding to the /invocations. If your model is going to take 50-60 seconds of processing time, the SDK socket timeout should be set to be 70 seconds.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.invoke_endpoint(
        EndpointName='string',
        Body=b'bytes'|file,
        ContentType='string',
        Accept='string',
        CustomAttributes='string',
        TargetModel='string'
    )
    
    
    :type EndpointName: string
    :param EndpointName: [REQUIRED]\nThe name of the endpoint that you specified when you created the endpoint using the CreateEndpoint API.\n

    :type Body: bytes or seekable file-like object
    :param Body: [REQUIRED]\nProvides input data, in the format specified in the ContentType request header. Amazon SageMaker passes all of the data in the body to the model.\nFor information about the format of the request body, see Common Data Formats\xe2\x80\x94Inference .\n

    :type ContentType: string
    :param ContentType: The MIME type of the input data in the request body.

    :type Accept: string
    :param Accept: The desired MIME type of the inference in the response.

    :type CustomAttributes: string
    :param CustomAttributes: Provides additional information about a request for an inference submitted to a model hosted at an Amazon SageMaker endpoint. The information is an opaque value that is forwarded verbatim. You could use this value, for example, to provide an ID that you can use to track a request or to provide other metadata that a service endpoint was programmed to process. The value must consist of no more than 1024 visible US-ASCII characters as specified in Section 3.3.6. Field Value Components of the Hypertext Transfer Protocol (HTTP/1.1). This feature is currently supported in the AWS SDKs but not in the Amazon SageMaker Python SDK.

    :type TargetModel: string
    :param TargetModel: Specifies the model to be requested for an inference when invoking a multi-model endpoint.

    :rtype: dict

ReturnsResponse Syntax
{
    'Body': StreamingBody(),
    'ContentType': 'string',
    'InvokedProductionVariant': 'string',
    'CustomAttributes': 'string'
}


Response Structure

(dict) --

Body (StreamingBody) --
Includes the inference provided by the model.
For information about the format of the response body, see Common Data Formats\xe2\x80\x94Inference .

ContentType (string) --
The MIME type of the inference returned in the response body.

InvokedProductionVariant (string) --
Identifies the production variant that was invoked.

CustomAttributes (string) --
Provides additional information in the response about the inference returned by a model hosted at an Amazon SageMaker endpoint. The information is an opaque value that is forwarded verbatim. You could use this value, for example, to return an ID received in the CustomAttributes header of a request or other metadata that a service endpoint was programmed to produce. The value must consist of no more than 1024 visible US-ASCII characters as specified in Section 3.3.6. Field Value Components of the Hypertext Transfer Protocol (HTTP/1.1). If the customer wants the custom attribute returned, the model must set the custom attribute to be included on the way back.
This feature is currently supported in the AWS SDKs but not in the Amazon SageMaker Python SDK.







Exceptions

SageMakerRuntime.Client.exceptions.InternalFailure
SageMakerRuntime.Client.exceptions.ServiceUnavailable
SageMakerRuntime.Client.exceptions.ValidationError
SageMakerRuntime.Client.exceptions.ModelError


    :return: {
        'Body': StreamingBody(),
        'ContentType': 'string',
        'InvokedProductionVariant': 'string',
        'CustomAttributes': 'string'
    }
    
    
    :returns: 
    SageMakerRuntime.Client.exceptions.InternalFailure
    SageMakerRuntime.Client.exceptions.ServiceUnavailable
    SageMakerRuntime.Client.exceptions.ValidationError
    SageMakerRuntime.Client.exceptions.ModelError
    
    """
    pass

