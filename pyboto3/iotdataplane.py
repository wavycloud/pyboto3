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

def delete_thing_shadow(thingName=None):
    """
    Deletes the thing shadow for the specified thing.
    For more information, see DeleteThingShadow in the AWS IoT Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_thing_shadow(
        thingName='string'
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]\nThe name of the thing.\n

    :rtype: dict
ReturnsResponse Syntax{
    'payload': StreamingBody()
}


Response Structure

(dict) --The output from the DeleteThingShadow operation.

payload (StreamingBody) --The state information, in JSON format.






Exceptions

IoTDataPlane.Client.exceptions.ResourceNotFoundException
IoTDataPlane.Client.exceptions.InvalidRequestException
IoTDataPlane.Client.exceptions.ThrottlingException
IoTDataPlane.Client.exceptions.UnauthorizedException
IoTDataPlane.Client.exceptions.ServiceUnavailableException
IoTDataPlane.Client.exceptions.InternalFailureException
IoTDataPlane.Client.exceptions.MethodNotAllowedException
IoTDataPlane.Client.exceptions.UnsupportedDocumentEncodingException


    :return: {
        'payload': StreamingBody()
    }
    
    
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

def get_thing_shadow(thingName=None):
    """
    Gets the thing shadow for the specified thing.
    For more information, see GetThingShadow in the AWS IoT Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_thing_shadow(
        thingName='string'
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]\nThe name of the thing.\n

    :rtype: dict
ReturnsResponse Syntax{
    'payload': StreamingBody()
}


Response Structure

(dict) --The output from the GetThingShadow operation.

payload (StreamingBody) --The state information, in JSON format.






Exceptions

IoTDataPlane.Client.exceptions.InvalidRequestException
IoTDataPlane.Client.exceptions.ResourceNotFoundException
IoTDataPlane.Client.exceptions.ThrottlingException
IoTDataPlane.Client.exceptions.UnauthorizedException
IoTDataPlane.Client.exceptions.ServiceUnavailableException
IoTDataPlane.Client.exceptions.InternalFailureException
IoTDataPlane.Client.exceptions.MethodNotAllowedException
IoTDataPlane.Client.exceptions.UnsupportedDocumentEncodingException


    :return: {
        'payload': StreamingBody()
    }
    
    
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

def publish(topic=None, qos=None, payload=None):
    """
    Publishes state information.
    For more information, see HTTP Protocol in the AWS IoT Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.publish(
        topic='string',
        qos=123,
        payload=b'bytes'|file
    )
    
    
    :type topic: string
    :param topic: [REQUIRED]\nThe name of the MQTT topic.\n

    :type qos: integer
    :param qos: The Quality of Service (QoS) level.

    :type payload: bytes or seekable file-like object
    :param payload: The state information, in JSON format.

    :returns: 
    IoTDataPlane.Client.exceptions.InternalFailureException
    IoTDataPlane.Client.exceptions.InvalidRequestException
    IoTDataPlane.Client.exceptions.UnauthorizedException
    IoTDataPlane.Client.exceptions.MethodNotAllowedException
    
    """
    pass

def update_thing_shadow(thingName=None, payload=None):
    """
    Updates the thing shadow for the specified thing.
    For more information, see UpdateThingShadow in the AWS IoT Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_thing_shadow(
        thingName='string',
        payload=b'bytes'|file
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]\nThe name of the thing.\n

    :type payload: bytes or seekable file-like object
    :param payload: [REQUIRED]\nThe state information, in JSON format.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'payload': StreamingBody()
}


Response Structure

(dict) --
The output from the UpdateThingShadow operation.

payload (StreamingBody) --
The state information, in JSON format.







Exceptions

IoTDataPlane.Client.exceptions.ConflictException
IoTDataPlane.Client.exceptions.RequestEntityTooLargeException
IoTDataPlane.Client.exceptions.InvalidRequestException
IoTDataPlane.Client.exceptions.ThrottlingException
IoTDataPlane.Client.exceptions.UnauthorizedException
IoTDataPlane.Client.exceptions.ServiceUnavailableException
IoTDataPlane.Client.exceptions.InternalFailureException
IoTDataPlane.Client.exceptions.MethodNotAllowedException
IoTDataPlane.Client.exceptions.UnsupportedDocumentEncodingException


    :return: {
        'payload': StreamingBody()
    }
    
    
    :returns: 
    IoTDataPlane.Client.exceptions.ConflictException
    IoTDataPlane.Client.exceptions.RequestEntityTooLargeException
    IoTDataPlane.Client.exceptions.InvalidRequestException
    IoTDataPlane.Client.exceptions.ThrottlingException
    IoTDataPlane.Client.exceptions.UnauthorizedException
    IoTDataPlane.Client.exceptions.ServiceUnavailableException
    IoTDataPlane.Client.exceptions.InternalFailureException
    IoTDataPlane.Client.exceptions.MethodNotAllowedException
    IoTDataPlane.Client.exceptions.UnsupportedDocumentEncodingException
    
    """
    pass

