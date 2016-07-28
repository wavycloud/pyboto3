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

import boto3


class Iotdata(object):
    def __init__(self):
        self.client = boto3.client('Iotdata')

    def can_paginate(self, operation_name=None):
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
        self.client.can_paginate(operation_name=operation_name)

    def delete_thing_shadow(self, thingName=None):
        """
        :param thingName: [REQUIRED]
            The name of the thing.
            Return typedict
            ReturnsResponse Syntax{
              'payload': StreamingBody()
            }
            Response Structure
            (dict) --The output from the DeleteThingShadow operation.
            payload (StreamingBody) --The state information, in JSON format.
            
            
        :type thingName: string
        """
        self.client.delete_thing_shadow(thingName=thingName)

    def generate_presigned_url(self, ClientMethod=None, Params=None, ExpiresIn=None, HttpMethod=None):
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
        self.client.generate_presigned_url(ClientMethod=ClientMethod, Params=Params, ExpiresIn=ExpiresIn,
                                           HttpMethod=HttpMethod)

    def get_paginator(self, operation_name=None):
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
        self.client.get_paginator(operation_name=operation_name)

    def get_thing_shadow(self, thingName=None):
        """
        :param thingName: [REQUIRED]
            The name of the thing.
            Return typedict
            ReturnsResponse Syntax{
              'payload': StreamingBody()
            }
            Response Structure
            (dict) --The output from the GetThingShadow operation.
            payload (StreamingBody) --The state information, in JSON format.
            
            
        :type thingName: string
        """
        self.client.get_thing_shadow(thingName=thingName)

    def get_waiter(self):
        """
        """
        self.client.get_waiter()

    def publish(self, topic=None, qos=None, payload=None):
        """
        :param topic: [REQUIRED]
            The name of the MQTT topic.
            
        :type topic: string
        :param qos: The Quality of Service (QoS) level.
        :type qos: integer
        :param payload: The state information, in JSON format.
        :type payload: bytes or seekable file-like object
        """
        self.client.publish(topic=topic, qos=qos, payload=payload)

    def update_thing_shadow(self, thingName=None, payload=None):
        """
        :param thingName: [REQUIRED]
            The name of the thing.
            
        :type thingName: string
        :param payload: [REQUIRED]
            The state information, in JSON format.
            
        :type payload: bytes or seekable file-like object
        """
        self.client.update_thing_shadow(thingName=thingName, payload=payload)
