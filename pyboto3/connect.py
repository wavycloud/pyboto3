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
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').

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

def get_waiter(waiter_name=None):
    """
    
    :type waiter_name: 
    :param waiter_name: 

    """
    pass

def start_outbound_voice_contact(DestinationPhoneNumber=None, ContactFlowId=None, InstanceId=None, ClientToken=None, SourcePhoneNumber=None, QueueId=None, Attributes=None):
    """
    The StartOutboundVoiceContact operation initiates a contact flow to place an outbound call to a customer.
    There is a throttling limit placed on usage of the API that includes a RateLimit of 2 per second, and a BurstLimit of 5 per second.
    If you are using an IAM account, it must have permissions to the connect:StartOutboundVoiceContact action.
    See also: AWS API Documentation
    
    
    :example: response = client.start_outbound_voice_contact(
        DestinationPhoneNumber='string',
        ContactFlowId='string',
        InstanceId='string',
        ClientToken='string',
        SourcePhoneNumber='string',
        QueueId='string',
        Attributes={
            'string': 'string'
        }
    )
    
    
    :type DestinationPhoneNumber: string
    :param DestinationPhoneNumber: [REQUIRED]
            The phone number, in E.164 format, of the customer to call with the outbound contact.
            

    :type ContactFlowId: string
    :param ContactFlowId: [REQUIRED]
            The identifier for the contact flow to execute for the outbound call. This is a GUID value only. Amazon Resource Name (ARN) values are not supported.
            To find the ContactFlowId , open the contact flow to use in the Amazon Connect contact flow designer. The ID for the contact flow is displayed in the address bar as part of the URL. For example, an address displayed when you open a contact flow is similar to the following: https://myconnectinstance.awsapps.com/connect/contact-flows/edit?id=arn:aws:connect:us-east-1:361814831152:instance/2fb42df9-78a2-4b99-b484-f5cf80dc300c/contact-flow/*b0b8f2dd-ed1b-4c44-af36-ce189a178181* `` . At the end of the URL, you see ``contact-flow/b0b8f2dd-ed1b-4c44-af36-ce189a178181 . The ContactFlowID for this contact flow is `` b0b8f2dd-ed1b-4c44-af36-ce189a178181 `` . Make sure to include only the GUID after the 'contact-flow/' in your requests.
            

    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The identifier for your Amazon Connect instance. To find the InstanceId value for your Amazon Connect instance, open the Amazon Connect console . Select the instance alias of the instance and view the instance ID in the Overview section. For example, the instance ID is the set of characters at the end of the instance ARN, after 'instance/', such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
            

    :type ClientToken: string
    :param ClientToken: A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. The token is valid for 7 days after creation. If a contact is already started, the contact ID is returned. If the contact is disconnected, a new contact is started.
            This field is autopopulated if not provided.
            

    :type SourcePhoneNumber: string
    :param SourcePhoneNumber: The phone number, in E.164 format, associated with your Amazon Connect instance to use to place the outbound call.

    :type QueueId: string
    :param QueueId: The queue to which to add the call. If you specify a queue, the phone displayed for caller ID is the phone number defined for the queue. If you do not specify a queue, the queue used is the queue defined in the contact flow specified by ContactFlowId .
            To find the QueueId , open the queue to use in the Amazon Connect queue editor. The ID for the queue is displayed in the address bar as part of the URL. For example, the QueueId value is the set of characters at the end of the URL, after 'queue/', such as aeg40574-2d01-51c3-73d6-bf8624d2168c .
            

    :type Attributes: dict
    :param Attributes: Specify a custom key-value pair using an attribute map. The attributes are standard Amazon Connect attributes, and can be accessed in contact flows just like any other contact attributes.
            There can be up to 32,768 UTF-8 bytes across all key-value pairs. Attribute keys can include only alphanumeric, dash, and underscore characters.
            For example, to play a greeting when the customer answers the call, you can pass the customer name in attributes similar to the following:
            (string) -- Key for the key value pair to be used for additional attributes.
            (string) -- Value for the key value pair to be used for additional attributes.
            

    :rtype: dict
    :return: {
        'ContactId': 'string'
    }
    
    
    """
    pass

def stop_contact(ContactId=None, InstanceId=None):
    """
    Ends the contact initiated by the StartOutboundVoiceContact operation.
    If you are using an IAM account, it must have permissions to the connect:StopContact operation.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_contact(
        ContactId='string',
        InstanceId='string'
    )
    
    
    :type ContactId: string
    :param ContactId: [REQUIRED]
            The unique identifier of the contact to end. This is the ContactId value returned from the StartOutboundVoiceContact operation.
            

    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The identifier of the Amazon Connect instance in which the contact is active.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

