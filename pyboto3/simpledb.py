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


def batch_delete_attributes(DomainName=None, Items=None):
    """
    :param DomainName: [REQUIRED] The name of the domain in which the attributes are being deleted.
    :type DomainName: string
    :param Items: [REQUIRED] A list of items on which to perform the operation.
            (dict) --
            Name (string) -- [REQUIRED]
            Attributes (list) --
            (dict) --
            Name (string) -- [REQUIRED] The name of the attribute.
            AlternateNameEncoding (string) --
            Value (string) -- [REQUIRED] The value of the attribute.
            AlternateValueEncoding (string) --
            
            
    :type Items: list
    """
    pass


def batch_put_attributes(DomainName=None, Items=None):
    """
    :param DomainName: [REQUIRED] The name of the domain in which the attributes are being stored.
    :type DomainName: string
    :param Items: [REQUIRED] A list of items on which to perform the operation.
            (dict) --
            Name (string) -- [REQUIRED] The name of the replaceable item.
            Attributes (list) -- [REQUIRED] The list of attributes for a replaceable item.
            (dict) --
            Name (string) -- [REQUIRED] The name of the replaceable attribute.
            Value (string) -- [REQUIRED] The value of the replaceable attribute.
            Replace (boolean) -- A flag specifying whether or not to replace the attribute/value pair or to add a new attribute/value pair. The default setting is false .
            
            
    :type Items: list
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


def create_domain(DomainName=None):
    """
    :param DomainName: [REQUIRED] The name of the domain to create. The name can range between 3 and 255 characters and can contain the following characters: a-z, A-Z, 0-9, '_', '-', and '.'.
            ReturnsNone
            
    :type DomainName: string
    """
    pass


def delete_attributes(DomainName=None, ItemName=None, Attributes=None, Expected=None):
    """
    :param DomainName: [REQUIRED] The name of the domain in which to perform the operation.
    :type DomainName: string
    :param ItemName: [REQUIRED] The name of the item. Similar to rows on a spreadsheet, items represent individual objects that contain one or more value-attribute pairs.
    :type ItemName: string
    :param Attributes: A list of Attributes. Similar to columns on a spreadsheet, attributes represent categories of data that can be assigned to items.
            (dict) --
            Name (string) -- [REQUIRED] The name of the attribute.
            AlternateNameEncoding (string) --
            Value (string) -- [REQUIRED] The value of the attribute.
            AlternateValueEncoding (string) --
            
    :type Attributes: list
    :param Expected: The update condition which, if specified, determines whether the specified attributes will be deleted or not. The update condition must be satisfied in order for this request to be processed and the attributes to be deleted.
            Name (string) --The name of the attribute involved in the condition.
            Value (string) --The value of an attribute. This value can only be specified when the Exists parameter is equal to true .
            Exists (boolean) --A value specifying whether or not the specified attribute must exist with the specified value in order for the update condition to be satisfied. Specify true if the attribute must exist for the update condition to be satisfied. Specify false if the attribute should not exist in order for the update condition to be satisfied.
            
    :type Expected: dict
    """
    pass


def delete_domain(DomainName=None):
    """
    :param DomainName: [REQUIRED] The name of the domain to delete.
            ReturnsNone
            
    :type DomainName: string
    """
    pass


def domain_metadata(DomainName=None):
    """
    :param DomainName: [REQUIRED] The name of the domain for which to display the metadata of.
            Return typedict
            ReturnsResponse Syntax{
              'ItemCount': 123,
              'ItemNamesSizeBytes': 123,
              'AttributeNameCount': 123,
              'AttributeNamesSizeBytes': 123,
              'AttributeValueCount': 123,
              'AttributeValuesSizeBytes': 123,
              'Timestamp': 123
            }
            Response Structure
            (dict) --
            ItemCount (integer) -- The number of all items in the domain.
            ItemNamesSizeBytes (integer) -- The total size of all item names in the domain, in bytes.
            AttributeNameCount (integer) -- The number of unique attribute names in the domain.
            AttributeNamesSizeBytes (integer) -- The total size of all unique attribute names in the domain, in bytes.
            AttributeValueCount (integer) -- The number of all attribute name/value pairs in the domain.
            AttributeValuesSizeBytes (integer) -- The total size of all attribute values in the domain, in bytes.
            Timestamp (integer) -- The data and time when metadata was calculated, in Epoch (UNIX) seconds.
            
            
    :type DomainName: string
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


def get_attributes(DomainName=None, ItemName=None, AttributeNames=None, ConsistentRead=None):
    """
    :param DomainName: [REQUIRED] The name of the domain in which to perform the operation.
    :type DomainName: string
    :param ItemName: [REQUIRED] The name of the item.
    :type ItemName: string
    :param AttributeNames: The names of the attributes.
            (string) --
            
    :type AttributeNames: list
    :param ConsistentRead: Determines whether or not strong consistency should be enforced when data is read from SimpleDB. If true , any data previously written to SimpleDB will be returned. Otherwise, results will be consistent eventually, and the client may not see data that was written immediately before your read.
    :type ConsistentRead: boolean
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


def get_waiter():
    """
    """
    pass


def list_domains(MaxNumberOfDomains=None, NextToken=None):
    """
    :param MaxNumberOfDomains: The maximum number of domain names you want returned. The range is 1 to 100. The default setting is 100.
    :type MaxNumberOfDomains: integer
    :param NextToken: A string informing Amazon SimpleDB where to start the next list of domain names.
    :type NextToken: string
    """
    pass


def put_attributes(DomainName=None, ItemName=None, Attributes=None, Expected=None):
    """
    :param DomainName: [REQUIRED] The name of the domain in which to perform the operation.
    :type DomainName: string
    :param ItemName: [REQUIRED] The name of the item.
    :type ItemName: string
    :param Attributes: [REQUIRED] The list of attributes.
            (dict) --
            Name (string) -- [REQUIRED] The name of the replaceable attribute.
            Value (string) -- [REQUIRED] The value of the replaceable attribute.
            Replace (boolean) -- A flag specifying whether or not to replace the attribute/value pair or to add a new attribute/value pair. The default setting is false .
            
    :type Attributes: list
    :param Expected: The update condition which, if specified, determines whether the specified attributes will be updated or not. The update condition must be satisfied in order for this request to be processed and the attributes to be updated.
            Name (string) --The name of the attribute involved in the condition.
            Value (string) --The value of an attribute. This value can only be specified when the Exists parameter is equal to true .
            Exists (boolean) --A value specifying whether or not the specified attribute must exist with the specified value in order for the update condition to be satisfied. Specify true if the attribute must exist for the update condition to be satisfied. Specify false if the attribute should not exist in order for the update condition to be satisfied.
            
    :type Expected: dict
    """
    pass


def select(SelectExpression=None, NextToken=None, ConsistentRead=None):
    """
    :param SelectExpression: [REQUIRED] The expression used to query the domain.
    :type SelectExpression: string
    :param NextToken: A string informing Amazon SimpleDB where to start the next list of ItemNames .
    :type NextToken: string
    :param ConsistentRead: Determines whether or not strong consistency should be enforced when data is read from SimpleDB. If true , any data previously written to SimpleDB will be returned. Otherwise, results will be consistent eventually, and the client may not see data that was written immediately before your read.
    :type ConsistentRead: boolean
    """
    pass
