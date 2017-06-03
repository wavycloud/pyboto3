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

def add_facet_to_object(DirectoryArn=None, SchemaFacet=None, ObjectAttributeList=None, ObjectReference=None):
    """
    Adds a new  Facet to an object.
    See also: AWS API Documentation
    
    
    :example: response = client.add_facet_to_object(
        DirectoryArn='string',
        SchemaFacet={
            'SchemaArn': 'string',
            'FacetName': 'string'
        },
        ObjectAttributeList=[
            {
                'Key': {
                    'SchemaArn': 'string',
                    'FacetName': 'string',
                    'Name': 'string'
                },
                'Value': {
                    'StringValue': 'string',
                    'BinaryValue': b'bytes',
                    'BooleanValue': True|False,
                    'NumberValue': 'string',
                    'DatetimeValue': datetime(2015, 1, 1)
                }
            },
        ],
        ObjectReference={
            'Selector': 'string'
        }
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]
            The Amazon Resource Name (ARN) that is associated with the Directory where the object resides. For more information, see arns .
            

    :type SchemaFacet: dict
    :param SchemaFacet: [REQUIRED]
            Identifiers for the facet that you are adding to the object.
            SchemaArn (string) --The ARN of the schema that contains the facet.
            FacetName (string) --The name of the facet.
            

    :type ObjectAttributeList: list
    :param ObjectAttributeList: Attributes on the facet that you are adding to the object.
            (dict) --The combination of an attribute key and an attribute value.
            Key (dict) -- [REQUIRED]The key of the attribute.
            SchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
            FacetName (string) -- [REQUIRED]The name of the facet that the attribute exists within.
            Name (string) -- [REQUIRED]The name of the attribute.
            Value (dict) -- [REQUIRED]The value of the attribute.
            StringValue (string) --A string data value.
            BinaryValue (bytes) --A binary data value.
            BooleanValue (boolean) --A Boolean data value.
            NumberValue (string) --A number data value.
            DatetimeValue (datetime) --A date and time value.
            
            

    :type ObjectReference: dict
    :param ObjectReference: [REQUIRED]
            A reference to the object you are adding the specified facet to.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def apply_schema(PublishedSchemaArn=None, DirectoryArn=None):
    """
    Copies the input published schema into the  Directory with the same name and version as that of the published schema .
    See also: AWS API Documentation
    
    
    :example: response = client.apply_schema(
        PublishedSchemaArn='string',
        DirectoryArn='string'
    )
    
    
    :type PublishedSchemaArn: string
    :param PublishedSchemaArn: [REQUIRED]
            Published schema Amazon Resource Name (ARN) that needs to be copied. For more information, see arns .
            

    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]
            The Amazon Resource Name (ARN) that is associated with the Directory into which the schema is copied. For more information, see arns .
            

    :rtype: dict
    :return: {
        'AppliedSchemaArn': 'string',
        'DirectoryArn': 'string'
    }
    
    
    """
    pass

def attach_object(DirectoryArn=None, ParentReference=None, ChildReference=None, LinkName=None):
    """
    Attaches an existing object to another object. An object can be accessed in two ways:
    See also: AWS API Documentation
    
    
    :example: response = client.attach_object(
        DirectoryArn='string',
        ParentReference={
            'Selector': 'string'
        },
        ChildReference={
            'Selector': 'string'
        },
        LinkName='string'
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]
            Amazon Resource Name (ARN) that is associated with the Directory where both objects reside. For more information, see arns .
            

    :type ParentReference: dict
    :param ParentReference: [REQUIRED]
            The parent object reference.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            

    :type ChildReference: dict
    :param ChildReference: [REQUIRED]
            The child object reference to be attached to the object.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            

    :type LinkName: string
    :param LinkName: [REQUIRED]
            The link name with which the child object is attached to the parent.
            

    :rtype: dict
    :return: {
        'AttachedObjectIdentifier': 'string'
    }
    
    
    :returns: 
    DirectoryArn (string) -- [REQUIRED]
    Amazon Resource Name (ARN) that is associated with the  Directory where both objects reside. For more information, see  arns .
    
    ParentReference (dict) -- [REQUIRED]
    The parent object reference.
    
    Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
    
    $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objects identifier is immutable and no two objects will ever share the same object identifier
    /some/path - Identifies the object based on path
    #SomeBatchReference - Identifies the object in a batch call
    
    
    
    
    ChildReference (dict) -- [REQUIRED]
    The child object reference to be attached to the object.
    
    Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
    
    $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objects identifier is immutable and no two objects will ever share the same object identifier
    /some/path - Identifies the object based on path
    #SomeBatchReference - Identifies the object in a batch call
    
    
    
    
    LinkName (string) -- [REQUIRED]
    The link name with which the child object is attached to the parent.
    
    
    """
    pass

def attach_policy(DirectoryArn=None, PolicyReference=None, ObjectReference=None):
    """
    Attaches a policy object to a regular object. An object can have a limited number of attached policies.
    See also: AWS API Documentation
    
    
    :example: response = client.attach_policy(
        DirectoryArn='string',
        PolicyReference={
            'Selector': 'string'
        },
        ObjectReference={
            'Selector': 'string'
        }
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: The Amazon Resource Name (ARN) that is associated with the Directory where both objects reside. For more information, see arns .

    :type PolicyReference: dict
    :param PolicyReference: [REQUIRED]
            The reference that is associated with the policy object.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            

    :type ObjectReference: dict
    :param ObjectReference: [REQUIRED]
            The reference that identifies the object to which the policy will be attached.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def attach_to_index(DirectoryArn=None, IndexReference=None, TargetReference=None):
    """
    Attaches the specified object to the specified index.
    See also: AWS API Documentation
    
    
    :example: response = client.attach_to_index(
        DirectoryArn='string',
        IndexReference={
            'Selector': 'string'
        },
        TargetReference={
            'Selector': 'string'
        }
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the directory where the object and index exist.
            

    :type IndexReference: dict
    :param IndexReference: [REQUIRED]
            A reference to the index that you are attaching the object to.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            

    :type TargetReference: dict
    :param TargetReference: [REQUIRED]
            A reference to the object that you are attaching to the index.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            

    :rtype: dict
    :return: {
        'AttachedObjectIdentifier': 'string'
    }
    
    
    """
    pass

def attach_typed_link(DirectoryArn=None, SourceObjectReference=None, TargetObjectReference=None, TypedLinkFacet=None, Attributes=None):
    """
    Attaches a typed link to a specified source and target object. For more information, see Typed link .
    See also: AWS API Documentation
    
    
    :example: response = client.attach_typed_link(
        DirectoryArn='string',
        SourceObjectReference={
            'Selector': 'string'
        },
        TargetObjectReference={
            'Selector': 'string'
        },
        TypedLinkFacet={
            'SchemaArn': 'string',
            'TypedLinkName': 'string'
        },
        Attributes=[
            {
                'AttributeName': 'string',
                'Value': {
                    'StringValue': 'string',
                    'BinaryValue': b'bytes',
                    'BooleanValue': True|False,
                    'NumberValue': 'string',
                    'DatetimeValue': datetime(2015, 1, 1)
                }
            },
        ]
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the directory where you want to attach the typed link.
            

    :type SourceObjectReference: dict
    :param SourceObjectReference: [REQUIRED]
            Identifies the source object that the typed link will attach to.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            

    :type TargetObjectReference: dict
    :param TargetObjectReference: [REQUIRED]
            Identifies the target object that the typed link will attach to.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            

    :type TypedLinkFacet: dict
    :param TypedLinkFacet: [REQUIRED]
            Identifies the typed link facet that is associated with the typed link.
            SchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) that is associated with the schema. For more information, see arns .
            TypedLinkName (string) -- [REQUIRED]The unique name of the typed link facet.
            

    :type Attributes: list
    :param Attributes: [REQUIRED]
            An ordered set of attributes that are associated with the typed link.
            (dict) --Identifies the attribute name and value for a typed link.
            AttributeName (string) -- [REQUIRED]The attribute name of the typed link.
            Value (dict) -- [REQUIRED]The value for the typed link.
            StringValue (string) --A string data value.
            BinaryValue (bytes) --A binary data value.
            BooleanValue (boolean) --A Boolean data value.
            NumberValue (string) --A number data value.
            DatetimeValue (datetime) --A date and time value.
            
            

    :rtype: dict
    :return: {
        'TypedLinkSpecifier': {
            'TypedLinkFacet': {
                'SchemaArn': 'string',
                'TypedLinkName': 'string'
            },
            'SourceObjectReference': {
                'Selector': 'string'
            },
            'TargetObjectReference': {
                'Selector': 'string'
            },
            'IdentityAttributeValues': [
                {
                    'AttributeName': 'string',
                    'Value': {
                        'StringValue': 'string',
                        'BinaryValue': b'bytes',
                        'BooleanValue': True|False,
                        'NumberValue': 'string',
                        'DatetimeValue': datetime(2015, 1, 1)
                    }
                },
            ]
        }
    }
    
    
    :returns: 
    $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objects identifier is immutable and no two objects will ever share the same object identifier
    /some/path - Identifies the object based on path
    #SomeBatchReference - Identifies the object in a batch call
    
    """
    pass

def batch_read(DirectoryArn=None, Operations=None, ConsistencyLevel=None):
    """
    Performs all the read operations in a batch.
    See also: AWS API Documentation
    
    
    :example: response = client.batch_read(
        DirectoryArn='string',
        Operations=[
            {
                'ListObjectAttributes': {
                    'ObjectReference': {
                        'Selector': 'string'
                    },
                    'NextToken': 'string',
                    'MaxResults': 123,
                    'FacetFilter': {
                        'SchemaArn': 'string',
                        'FacetName': 'string'
                    }
                },
                'ListObjectChildren': {
                    'ObjectReference': {
                        'Selector': 'string'
                    },
                    'NextToken': 'string',
                    'MaxResults': 123
                }
            },
        ],
        ConsistencyLevel='SERIALIZABLE'|'EVENTUAL'
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]
            The Amazon Resource Name (ARN) that is associated with the Directory . For more information, see arns .
            

    :type Operations: list
    :param Operations: [REQUIRED]
            A list of operations that are part of the batch.
            (dict) --Represents the output of a BatchRead operation.
            ListObjectAttributes (dict) --Lists all attributes that are associated with an object.
            ObjectReference (dict) -- [REQUIRED]Reference of the object whose attributes need to be listed.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            
            NextToken (string) --The pagination token.
            MaxResults (integer) --The maximum number of items to be retrieved in a single call. This is an approximate number.
            FacetFilter (dict) --Used to filter the list of object attributes that are associated with a certain facet.
            SchemaArn (string) --The ARN of the schema that contains the facet.
            FacetName (string) --The name of the facet.
            
            ListObjectChildren (dict) --Returns a paginated list of child objects that are associated with a given object.
            ObjectReference (dict) -- [REQUIRED]Reference of the object for which child objects are being listed.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            
            NextToken (string) --The pagination token.
            MaxResults (integer) --Maximum number of items to be retrieved in a single call. This is an approximate number.
            
            

    :type ConsistencyLevel: string
    :param ConsistencyLevel: Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.

    :rtype: dict
    :return: {
        'Responses': [
            {
                'SuccessfulResponse': {
                    'ListObjectAttributes': {
                        'Attributes': [
                            {
                                'Key': {
                                    'SchemaArn': 'string',
                                    'FacetName': 'string',
                                    'Name': 'string'
                                },
                                'Value': {
                                    'StringValue': 'string',
                                    'BinaryValue': b'bytes',
                                    'BooleanValue': True|False,
                                    'NumberValue': 'string',
                                    'DatetimeValue': datetime(2015, 1, 1)
                                }
                            },
                        ],
                        'NextToken': 'string'
                    },
                    'ListObjectChildren': {
                        'Children': {
                            'string': 'string'
                        },
                        'NextToken': 'string'
                    }
                },
                'ExceptionResponse': {
                    'Type': 'ValidationException'|'InvalidArnException'|'ResourceNotFoundException'|'InvalidNextTokenException'|'AccessDeniedException'|'NotNodeException',
                    'Message': 'string'
                }
            },
        ]
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def batch_write(DirectoryArn=None, Operations=None):
    """
    Performs all the write operations in a batch. Either all the operations succeed or none. Batch writes supports only object-related operations.
    See also: AWS API Documentation
    
    
    :example: response = client.batch_write(
        DirectoryArn='string',
        Operations=[
            {
                'CreateObject': {
                    'SchemaFacet': [
                        {
                            'SchemaArn': 'string',
                            'FacetName': 'string'
                        },
                    ],
                    'ObjectAttributeList': [
                        {
                            'Key': {
                                'SchemaArn': 'string',
                                'FacetName': 'string',
                                'Name': 'string'
                            },
                            'Value': {
                                'StringValue': 'string',
                                'BinaryValue': b'bytes',
                                'BooleanValue': True|False,
                                'NumberValue': 'string',
                                'DatetimeValue': datetime(2015, 1, 1)
                            }
                        },
                    ],
                    'ParentReference': {
                        'Selector': 'string'
                    },
                    'LinkName': 'string',
                    'BatchReferenceName': 'string'
                },
                'AttachObject': {
                    'ParentReference': {
                        'Selector': 'string'
                    },
                    'ChildReference': {
                        'Selector': 'string'
                    },
                    'LinkName': 'string'
                },
                'DetachObject': {
                    'ParentReference': {
                        'Selector': 'string'
                    },
                    'LinkName': 'string',
                    'BatchReferenceName': 'string'
                },
                'UpdateObjectAttributes': {
                    'ObjectReference': {
                        'Selector': 'string'
                    },
                    'AttributeUpdates': [
                        {
                            'ObjectAttributeKey': {
                                'SchemaArn': 'string',
                                'FacetName': 'string',
                                'Name': 'string'
                            },
                            'ObjectAttributeAction': {
                                'ObjectAttributeActionType': 'CREATE_OR_UPDATE'|'DELETE',
                                'ObjectAttributeUpdateValue': {
                                    'StringValue': 'string',
                                    'BinaryValue': b'bytes',
                                    'BooleanValue': True|False,
                                    'NumberValue': 'string',
                                    'DatetimeValue': datetime(2015, 1, 1)
                                }
                            }
                        },
                    ]
                },
                'DeleteObject': {
                    'ObjectReference': {
                        'Selector': 'string'
                    }
                },
                'AddFacetToObject': {
                    'SchemaFacet': {
                        'SchemaArn': 'string',
                        'FacetName': 'string'
                    },
                    'ObjectAttributeList': [
                        {
                            'Key': {
                                'SchemaArn': 'string',
                                'FacetName': 'string',
                                'Name': 'string'
                            },
                            'Value': {
                                'StringValue': 'string',
                                'BinaryValue': b'bytes',
                                'BooleanValue': True|False,
                                'NumberValue': 'string',
                                'DatetimeValue': datetime(2015, 1, 1)
                            }
                        },
                    ],
                    'ObjectReference': {
                        'Selector': 'string'
                    }
                },
                'RemoveFacetFromObject': {
                    'SchemaFacet': {
                        'SchemaArn': 'string',
                        'FacetName': 'string'
                    },
                    'ObjectReference': {
                        'Selector': 'string'
                    }
                }
            },
        ]
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]
            The Amazon Resource Name (ARN) that is associated with the Directory . For more information, see arns .
            

    :type Operations: list
    :param Operations: [REQUIRED]
            A list of operations that are part of the batch.
            (dict) --Represents the output of a BatchWrite operation.
            CreateObject (dict) --Creates an object.
            SchemaFacet (list) -- [REQUIRED]A list of FacetArns that will be associated with the object. For more information, see arns .
            (dict) --A facet.
            SchemaArn (string) --The ARN of the schema that contains the facet.
            FacetName (string) --The name of the facet.
            
            ObjectAttributeList (list) -- [REQUIRED]An attribute map, which contains an attribute ARN as the key and attribute value as the map value.
            (dict) --The combination of an attribute key and an attribute value.
            Key (dict) -- [REQUIRED]The key of the attribute.
            SchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
            FacetName (string) -- [REQUIRED]The name of the facet that the attribute exists within.
            Name (string) -- [REQUIRED]The name of the attribute.
            Value (dict) -- [REQUIRED]The value of the attribute.
            StringValue (string) --A string data value.
            BinaryValue (bytes) --A binary data value.
            BooleanValue (boolean) --A Boolean data value.
            NumberValue (string) --A number data value.
            DatetimeValue (datetime) --A date and time value.
            
            ParentReference (dict) -- [REQUIRED]If specified, the parent reference to which this object will be attached.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            
            LinkName (string) -- [REQUIRED]The name of the link.
            BatchReferenceName (string) -- [REQUIRED]The batch reference name. See Batches for more information.
            AttachObject (dict) --Attaches an object to a Directory .
            ParentReference (dict) -- [REQUIRED]The parent object reference.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            
            ChildReference (dict) -- [REQUIRED]The child object reference that is to be attached to the object.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            
            LinkName (string) -- [REQUIRED]The name of the link.
            DetachObject (dict) --Detaches an object from a Directory .
            ParentReference (dict) -- [REQUIRED]Parent reference from which the object with the specified link name is detached.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            
            LinkName (string) -- [REQUIRED]The name of the link.
            BatchReferenceName (string) -- [REQUIRED]The batch reference name. See Batches for more information.
            UpdateObjectAttributes (dict) --Updates a given object's attributes.
            ObjectReference (dict) -- [REQUIRED]Reference that identifies the object.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            
            AttributeUpdates (list) -- [REQUIRED]Attributes update structure.
            (dict) --Structure that contains attribute update information.
            ObjectAttributeKey (dict) --The key of the attribute being updated.
            SchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
            FacetName (string) -- [REQUIRED]The name of the facet that the attribute exists within.
            Name (string) -- [REQUIRED]The name of the attribute.
            ObjectAttributeAction (dict) --The action to perform as part of the attribute update.
            ObjectAttributeActionType (string) --A type that can be either Update or Delete .
            ObjectAttributeUpdateValue (dict) --The value that you want to update to.
            StringValue (string) --A string data value.
            BinaryValue (bytes) --A binary data value.
            BooleanValue (boolean) --A Boolean data value.
            NumberValue (string) --A number data value.
            DatetimeValue (datetime) --A date and time value.
            
            
            DeleteObject (dict) --Deletes an object in a Directory .
            ObjectReference (dict) -- [REQUIRED]The reference that identifies the object.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            
            AddFacetToObject (dict) --A batch operation that adds a facet to an object.
            SchemaFacet (dict) -- [REQUIRED]Represents the facet being added to the object.
            SchemaArn (string) --The ARN of the schema that contains the facet.
            FacetName (string) --The name of the facet.
            ObjectAttributeList (list) -- [REQUIRED]The attributes to set on the object.
            (dict) --The combination of an attribute key and an attribute value.
            Key (dict) -- [REQUIRED]The key of the attribute.
            SchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
            FacetName (string) -- [REQUIRED]The name of the facet that the attribute exists within.
            Name (string) -- [REQUIRED]The name of the attribute.
            Value (dict) -- [REQUIRED]The value of the attribute.
            StringValue (string) --A string data value.
            BinaryValue (bytes) --A binary data value.
            BooleanValue (boolean) --A Boolean data value.
            NumberValue (string) --A number data value.
            DatetimeValue (datetime) --A date and time value.
            
            ObjectReference (dict) -- [REQUIRED]A reference to the object being mutated.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            
            RemoveFacetFromObject (dict) --A batch operation that removes a facet from an object.
            SchemaFacet (dict) -- [REQUIRED]The facet to remove from the object.
            SchemaArn (string) --The ARN of the schema that contains the facet.
            FacetName (string) --The name of the facet.
            ObjectReference (dict) -- [REQUIRED]A reference to the object whose facet will be removed.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            
            
            

    :rtype: dict
    :return: {
        'Responses': [
            {
                'CreateObject': {
                    'ObjectIdentifier': 'string'
                },
                'AttachObject': {
                    'attachedObjectIdentifier': 'string'
                },
                'DetachObject': {
                    'detachedObjectIdentifier': 'string'
                },
                'UpdateObjectAttributes': {
                    'ObjectIdentifier': 'string'
                },
                'DeleteObject': {}
                ,
                'AddFacetToObject': {}
                ,
                'RemoveFacetFromObject': {}
    
            },
        ]
    }
    
    
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

def create_directory(Name=None, SchemaArn=None):
    """
    Creates a  Directory by copying the published schema into the directory. A directory cannot be created without a schema.
    See also: AWS API Documentation
    
    
    :example: response = client.create_directory(
        Name='string',
        SchemaArn='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the Directory . Should be unique per account, per region.
            

    :type SchemaArn: string
    :param SchemaArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the published schema that will be copied into the data Directory . For more information, see arns .
            

    :rtype: dict
    :return: {
        'DirectoryArn': 'string',
        'Name': 'string',
        'ObjectIdentifier': 'string',
        'AppliedSchemaArn': 'string'
    }
    
    
    """
    pass

def create_facet(SchemaArn=None, Name=None, Attributes=None, ObjectType=None):
    """
    Creates a new  Facet in a schema. Facet creation is allowed only in development or applied schemas.
    See also: AWS API Documentation
    
    
    :example: response = client.create_facet(
        SchemaArn='string',
        Name='string',
        Attributes=[
            {
                'Name': 'string',
                'AttributeDefinition': {
                    'Type': 'STRING'|'BINARY'|'BOOLEAN'|'NUMBER'|'DATETIME',
                    'DefaultValue': {
                        'StringValue': 'string',
                        'BinaryValue': b'bytes',
                        'BooleanValue': True|False,
                        'NumberValue': 'string',
                        'DatetimeValue': datetime(2015, 1, 1)
                    },
                    'IsImmutable': True|False,
                    'Rules': {
                        'string': {
                            'Type': 'BINARY_LENGTH'|'NUMBER_COMPARISON'|'STRING_FROM_SET'|'STRING_LENGTH',
                            'Parameters': {
                                'string': 'string'
                            }
                        }
                    }
                },
                'AttributeReference': {
                    'TargetFacetName': 'string',
                    'TargetAttributeName': 'string'
                },
                'RequiredBehavior': 'REQUIRED_ALWAYS'|'NOT_REQUIRED'
            },
        ],
        ObjectType='NODE'|'LEAF_NODE'|'POLICY'|'INDEX'
    )
    
    
    :type SchemaArn: string
    :param SchemaArn: [REQUIRED]
            The schema ARN in which the new Facet will be created. For more information, see arns .
            

    :type Name: string
    :param Name: [REQUIRED]
            The name of the Facet , which is unique for a given schema.
            

    :type Attributes: list
    :param Attributes: The attributes that are associated with the Facet .
            (dict) --An attribute that is associated with the Facet .
            Name (string) -- [REQUIRED]The name of the facet attribute.
            AttributeDefinition (dict) --A facet attribute consists of either a definition or a reference. This structure contains the attribute definition. See Attribute References for more information.
            Type (string) -- [REQUIRED]The type of the attribute.
            DefaultValue (dict) --The default value of the attribute (if configured).
            StringValue (string) --A string data value.
            BinaryValue (bytes) --A binary data value.
            BooleanValue (boolean) --A Boolean data value.
            NumberValue (string) --A number data value.
            DatetimeValue (datetime) --A date and time value.
            IsImmutable (boolean) --Whether the attribute is mutable or not.
            Rules (dict) --Validation rules attached to the attribute definition.
            (string) --
            (dict) --Contains an Amazon Resource Name (ARN) and parameters that are associated with the rule.
            Type (string) --The type of attribute validation rule.
            Parameters (dict) --The minimum and maximum parameters that are associated with the rule.
            (string) --
            (string) --
            
            
            
            AttributeReference (dict) --An attribute reference that is associated with the attribute. See Attribute References for more information.
            TargetFacetName (string) -- [REQUIRED]The target facet name that is associated with the facet reference. See Attribute References for more information.
            TargetAttributeName (string) -- [REQUIRED]The target attribute name that is associated with the facet reference. See Attribute References for more information.
            RequiredBehavior (string) --The required behavior of the FacetAttribute .
            
            

    :type ObjectType: string
    :param ObjectType: [REQUIRED]
            Specifies whether a given object created from this facet is of type node, leaf node, policy or index.
            Node: Can have multiple children but one parent.
            Leaf node: Cannot have children but can have multiple parents.
            Policy: Allows you to store a policy document and policy type. For more information, see Policies .
            Index: Can be created with the Index API.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def create_index(DirectoryArn=None, OrderedIndexedAttributeList=None, IsUnique=None, ParentReference=None, LinkName=None):
    """
    Creates an index object. See Indexing for more information.
    See also: AWS API Documentation
    
    
    :example: response = client.create_index(
        DirectoryArn='string',
        OrderedIndexedAttributeList=[
            {
                'SchemaArn': 'string',
                'FacetName': 'string',
                'Name': 'string'
            },
        ],
        IsUnique=True|False,
        ParentReference={
            'Selector': 'string'
        },
        LinkName='string'
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]
            The ARN of the directory where the index should be created.
            

    :type OrderedIndexedAttributeList: list
    :param OrderedIndexedAttributeList: [REQUIRED]
            Specifies the attributes that should be indexed on. Currently only a single attribute is supported.
            (dict) --A unique identifier for an attribute.
            SchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
            FacetName (string) -- [REQUIRED]The name of the facet that the attribute exists within.
            Name (string) -- [REQUIRED]The name of the attribute.
            
            

    :type IsUnique: boolean
    :param IsUnique: [REQUIRED]
            Indicates whether the attribute that is being indexed has unique values or not.
            

    :type ParentReference: dict
    :param ParentReference: A reference to the parent object that contains the index object.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            

    :type LinkName: string
    :param LinkName: The name of the link between the parent object and the index object.

    :rtype: dict
    :return: {
        'ObjectIdentifier': 'string'
    }
    
    
    """
    pass

def create_object(DirectoryArn=None, SchemaFacets=None, ObjectAttributeList=None, ParentReference=None, LinkName=None):
    """
    Creates an object in a  Directory . Additionally attaches the object to a parent, if a parent reference and LinkName is specified. An object is simply a collection of  Facet attributes. You can also use this API call to create a policy object, if the facet from which you create the object is a policy facet.
    See also: AWS API Documentation
    
    
    :example: response = client.create_object(
        DirectoryArn='string',
        SchemaFacets=[
            {
                'SchemaArn': 'string',
                'FacetName': 'string'
            },
        ],
        ObjectAttributeList=[
            {
                'Key': {
                    'SchemaArn': 'string',
                    'FacetName': 'string',
                    'Name': 'string'
                },
                'Value': {
                    'StringValue': 'string',
                    'BinaryValue': b'bytes',
                    'BooleanValue': True|False,
                    'NumberValue': 'string',
                    'DatetimeValue': datetime(2015, 1, 1)
                }
            },
        ],
        ParentReference={
            'Selector': 'string'
        },
        LinkName='string'
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]
            The Amazon Resource Name (ARN) that is associated with the Directory in which the object will be created. For more information, see arns .
            

    :type SchemaFacets: list
    :param SchemaFacets: [REQUIRED]
            A list of schema facets to be associated with the object that contains SchemaArn and facet name. For more information, see arns .
            (dict) --A facet.
            SchemaArn (string) --The ARN of the schema that contains the facet.
            FacetName (string) --The name of the facet.
            
            

    :type ObjectAttributeList: list
    :param ObjectAttributeList: The attribute map whose attribute ARN contains the key and attribute value as the map value.
            (dict) --The combination of an attribute key and an attribute value.
            Key (dict) -- [REQUIRED]The key of the attribute.
            SchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
            FacetName (string) -- [REQUIRED]The name of the facet that the attribute exists within.
            Name (string) -- [REQUIRED]The name of the attribute.
            Value (dict) -- [REQUIRED]The value of the attribute.
            StringValue (string) --A string data value.
            BinaryValue (bytes) --A binary data value.
            BooleanValue (boolean) --A Boolean data value.
            NumberValue (string) --A number data value.
            DatetimeValue (datetime) --A date and time value.
            
            

    :type ParentReference: dict
    :param ParentReference: If specified, the parent reference to which this object will be attached.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            

    :type LinkName: string
    :param LinkName: The name of link that is used to attach this object to a parent.

    :rtype: dict
    :return: {
        'ObjectIdentifier': 'string'
    }
    
    
    """
    pass

def create_schema(Name=None):
    """
    Creates a new schema in a development state. A schema can exist in three phases:
    See also: AWS API Documentation
    
    
    :example: response = client.create_schema(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name that is associated with the schema. This is unique to each account and in each region.
            

    :rtype: dict
    :return: {
        'SchemaArn': 'string'
    }
    
    
    """
    pass

def create_typed_link_facet(SchemaArn=None, Facet=None):
    """
    Creates a  TypedLinkFacet . For more information, see Typed link .
    See also: AWS API Documentation
    
    
    :example: response = client.create_typed_link_facet(
        SchemaArn='string',
        Facet={
            'Name': 'string',
            'Attributes': [
                {
                    'Name': 'string',
                    'Type': 'STRING'|'BINARY'|'BOOLEAN'|'NUMBER'|'DATETIME',
                    'DefaultValue': {
                        'StringValue': 'string',
                        'BinaryValue': b'bytes',
                        'BooleanValue': True|False,
                        'NumberValue': 'string',
                        'DatetimeValue': datetime(2015, 1, 1)
                    },
                    'IsImmutable': True|False,
                    'Rules': {
                        'string': {
                            'Type': 'BINARY_LENGTH'|'NUMBER_COMPARISON'|'STRING_FROM_SET'|'STRING_LENGTH',
                            'Parameters': {
                                'string': 'string'
                            }
                        }
                    },
                    'RequiredBehavior': 'REQUIRED_ALWAYS'|'NOT_REQUIRED'
                },
            ],
            'IdentityAttributeOrder': [
                'string',
            ]
        }
    )
    
    
    :type SchemaArn: string
    :param SchemaArn: [REQUIRED]
            The Amazon Resource Name (ARN) that is associated with the schema. For more information, see arns .
            

    :type Facet: dict
    :param Facet: [REQUIRED]
            Facet structure that is associated with the typed link facet.
            Name (string) -- [REQUIRED]The unique name of the typed link facet.
            Attributes (list) -- [REQUIRED]An ordered set of attributes that are associate with the typed link. You can use typed link attributes when you need to represent the relationship between two objects or allow for quick filtering of incoming or outgoing typed links.
            (dict) --A typed link attribute definition.
            Name (string) -- [REQUIRED]The unique name of the typed link attribute.
            Type (string) -- [REQUIRED]The type of the attribute.
            DefaultValue (dict) --The default value of the attribute (if configured).
            StringValue (string) --A string data value.
            BinaryValue (bytes) --A binary data value.
            BooleanValue (boolean) --A Boolean data value.
            NumberValue (string) --A number data value.
            DatetimeValue (datetime) --A date and time value.
            IsImmutable (boolean) --Whether the attribute is mutable or not.
            Rules (dict) --Validation rules that are attached to the attribute definition.
            (string) --
            (dict) --Contains an Amazon Resource Name (ARN) and parameters that are associated with the rule.
            Type (string) --The type of attribute validation rule.
            Parameters (dict) --The minimum and maximum parameters that are associated with the rule.
            (string) --
            (string) --
            
            
            RequiredBehavior (string) -- [REQUIRED]The required behavior of the TypedLinkAttributeDefinition .
            
            IdentityAttributeOrder (list) -- [REQUIRED]A range filter that you provide for multiple attributes. The ability to filter typed links considers the order that the attributes are defined on the typed link facet. When providing ranges to typed link selection, any inexact ranges must be specified at the end. Any attributes that do not have a range specified are presumed to match the entire range. Filters are interpreted in the order of the attributes on the typed link facet, not the order in which they are supplied to any API calls.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_directory(DirectoryArn=None):
    """
    Deletes a directory. Only disabled directories can be deleted. A deleted directory cannot be undone. Exercise extreme caution when deleting directories.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_directory(
        DirectoryArn='string'
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]
            The ARN of the directory to delete.
            

    :rtype: dict
    :return: {
        'DirectoryArn': 'string'
    }
    
    
    """
    pass

def delete_facet(SchemaArn=None, Name=None):
    """
    Deletes a given  Facet . All attributes and  Rule s that are associated with the facet will be deleted. Only development schema facets are allowed deletion.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_facet(
        SchemaArn='string',
        Name='string'
    )
    
    
    :type SchemaArn: string
    :param SchemaArn: [REQUIRED]
            The Amazon Resource Name (ARN) that is associated with the Facet . For more information, see arns .
            

    :type Name: string
    :param Name: [REQUIRED]
            The name of the facet to delete.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_object(DirectoryArn=None, ObjectReference=None):
    """
    Deletes an object and its associated attributes. Only objects with no children and no parents can be deleted.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_object(
        DirectoryArn='string',
        ObjectReference={
            'Selector': 'string'
        }
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]
            The Amazon Resource Name (ARN) that is associated with the Directory where the object resides. For more information, see arns .
            

    :type ObjectReference: dict
    :param ObjectReference: [REQUIRED]
            A reference that identifies the object.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_schema(SchemaArn=None):
    """
    Deletes a given schema. Schemas in a development and published state can only be deleted.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_schema(
        SchemaArn='string'
    )
    
    
    :type SchemaArn: string
    :param SchemaArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the development schema. For more information, see arns .
            

    :rtype: dict
    :return: {
        'SchemaArn': 'string'
    }
    
    
    """
    pass

def delete_typed_link_facet(SchemaArn=None, Name=None):
    """
    Deletes a  TypedLinkFacet . For more information, see Typed link .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_typed_link_facet(
        SchemaArn='string',
        Name='string'
    )
    
    
    :type SchemaArn: string
    :param SchemaArn: [REQUIRED]
            The Amazon Resource Name (ARN) that is associated with the schema. For more information, see arns .
            

    :type Name: string
    :param Name: [REQUIRED]
            The unique name of the typed link facet.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def detach_from_index(DirectoryArn=None, IndexReference=None, TargetReference=None):
    """
    Detaches the specified object from the specified index.
    See also: AWS API Documentation
    
    
    :example: response = client.detach_from_index(
        DirectoryArn='string',
        IndexReference={
            'Selector': 'string'
        },
        TargetReference={
            'Selector': 'string'
        }
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the directory the index and object exist in.
            

    :type IndexReference: dict
    :param IndexReference: [REQUIRED]
            A reference to the index object.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            

    :type TargetReference: dict
    :param TargetReference: [REQUIRED]
            A reference to the object being detached from the index.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            

    :rtype: dict
    :return: {
        'DetachedObjectIdentifier': 'string'
    }
    
    
    """
    pass

def detach_object(DirectoryArn=None, ParentReference=None, LinkName=None):
    """
    Detaches a given object from the parent object. The object that is to be detached from the parent is specified by the link name.
    See also: AWS API Documentation
    
    
    :example: response = client.detach_object(
        DirectoryArn='string',
        ParentReference={
            'Selector': 'string'
        },
        LinkName='string'
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]
            The Amazon Resource Name (ARN) that is associated with the Directory where objects reside. For more information, see arns .
            

    :type ParentReference: dict
    :param ParentReference: [REQUIRED]
            The parent reference from which the object with the specified link name is detached.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            

    :type LinkName: string
    :param LinkName: [REQUIRED]
            The link name associated with the object that needs to be detached.
            

    :rtype: dict
    :return: {
        'DetachedObjectIdentifier': 'string'
    }
    
    
    """
    pass

def detach_policy(DirectoryArn=None, PolicyReference=None, ObjectReference=None):
    """
    Detaches a policy from an object.
    See also: AWS API Documentation
    
    
    :example: response = client.detach_policy(
        DirectoryArn='string',
        PolicyReference={
            'Selector': 'string'
        },
        ObjectReference={
            'Selector': 'string'
        }
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]
            The Amazon Resource Name (ARN) that is associated with the Directory where both objects reside. For more information, see arns .
            

    :type PolicyReference: dict
    :param PolicyReference: [REQUIRED]
            Reference that identifies the policy object.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            

    :type ObjectReference: dict
    :param ObjectReference: [REQUIRED]
            Reference that identifies the object whose policy object will be detached.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def detach_typed_link(DirectoryArn=None, TypedLinkSpecifier=None):
    """
    Detaches a typed link from a specified source and target object. For more information, see Typed link .
    See also: AWS API Documentation
    
    
    :example: response = client.detach_typed_link(
        DirectoryArn='string',
        TypedLinkSpecifier={
            'TypedLinkFacet': {
                'SchemaArn': 'string',
                'TypedLinkName': 'string'
            },
            'SourceObjectReference': {
                'Selector': 'string'
            },
            'TargetObjectReference': {
                'Selector': 'string'
            },
            'IdentityAttributeValues': [
                {
                    'AttributeName': 'string',
                    'Value': {
                        'StringValue': 'string',
                        'BinaryValue': b'bytes',
                        'BooleanValue': True|False,
                        'NumberValue': 'string',
                        'DatetimeValue': datetime(2015, 1, 1)
                    }
                },
            ]
        }
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the directory where you want to detach the typed link.
            

    :type TypedLinkSpecifier: dict
    :param TypedLinkSpecifier: [REQUIRED]
            Used to accept a typed link specifier as input.
            TypedLinkFacet (dict) -- [REQUIRED]Identifies the typed link facet that is associated with the typed link.
            SchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) that is associated with the schema. For more information, see arns .
            TypedLinkName (string) -- [REQUIRED]The unique name of the typed link facet.
            SourceObjectReference (dict) -- [REQUIRED]Identifies the source object that the typed link will attach to.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            
            TargetObjectReference (dict) -- [REQUIRED]Identifies the target object that the typed link will attach to.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            
            IdentityAttributeValues (list) -- [REQUIRED]Identifies the attribute value to update.
            (dict) --Identifies the attribute name and value for a typed link.
            AttributeName (string) -- [REQUIRED]The attribute name of the typed link.
            Value (dict) -- [REQUIRED]The value for the typed link.
            StringValue (string) --A string data value.
            BinaryValue (bytes) --A binary data value.
            BooleanValue (boolean) --A Boolean data value.
            NumberValue (string) --A number data value.
            DatetimeValue (datetime) --A date and time value.
            
            
            

    """
    pass

def disable_directory(DirectoryArn=None):
    """
    Disables the specified directory. Disabled directories cannot be read or written to. Only enabled directories can be disabled. Disabled directories may be reenabled.
    See also: AWS API Documentation
    
    
    :example: response = client.disable_directory(
        DirectoryArn='string'
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]
            The ARN of the directory to disable.
            

    :rtype: dict
    :return: {
        'DirectoryArn': 'string'
    }
    
    
    """
    pass

def enable_directory(DirectoryArn=None):
    """
    Enables the specified directory. Only disabled directories can be enabled. Once enabled, the directory can then be read and written to.
    See also: AWS API Documentation
    
    
    :example: response = client.enable_directory(
        DirectoryArn='string'
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]
            The ARN of the directory to enable.
            

    :rtype: dict
    :return: {
        'DirectoryArn': 'string'
    }
    
    
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

def get_directory(DirectoryArn=None):
    """
    Retrieves metadata about a directory.
    See also: AWS API Documentation
    
    
    :example: response = client.get_directory(
        DirectoryArn='string'
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]
            The ARN of the directory.
            

    :rtype: dict
    :return: {
        'Directory': {
            'Name': 'string',
            'DirectoryArn': 'string',
            'State': 'ENABLED'|'DISABLED'|'DELETED',
            'CreationDateTime': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def get_facet(SchemaArn=None, Name=None):
    """
    Gets details of the  Facet , such as facet name, attributes,  Rule s, or ObjectType . You can call this on all kinds of schema facets -- published, development, or applied.
    See also: AWS API Documentation
    
    
    :example: response = client.get_facet(
        SchemaArn='string',
        Name='string'
    )
    
    
    :type SchemaArn: string
    :param SchemaArn: [REQUIRED]
            The Amazon Resource Name (ARN) that is associated with the Facet . For more information, see arns .
            

    :type Name: string
    :param Name: [REQUIRED]
            The name of the facet to retrieve.
            

    :rtype: dict
    :return: {
        'Facet': {
            'Name': 'string',
            'ObjectType': 'NODE'|'LEAF_NODE'|'POLICY'|'INDEX'
        }
    }
    
    
    """
    pass

def get_object_information(DirectoryArn=None, ObjectReference=None, ConsistencyLevel=None):
    """
    Retrieves metadata about an object.
    See also: AWS API Documentation
    
    
    :example: response = client.get_object_information(
        DirectoryArn='string',
        ObjectReference={
            'Selector': 'string'
        },
        ConsistencyLevel='SERIALIZABLE'|'EVENTUAL'
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]
            The ARN of the directory being retrieved.
            

    :type ObjectReference: dict
    :param ObjectReference: [REQUIRED]
            A reference to the object.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            

    :type ConsistencyLevel: string
    :param ConsistencyLevel: The consistency level at which to retrieve the object information.

    :rtype: dict
    :return: {
        'SchemaFacets': [
            {
                'SchemaArn': 'string',
                'FacetName': 'string'
            },
        ],
        'ObjectIdentifier': 'string'
    }
    
    
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

def get_schema_as_json(SchemaArn=None):
    """
    Retrieves a JSON representation of the schema. See JSON Schema Format for more information.
    See also: AWS API Documentation
    
    
    :example: response = client.get_schema_as_json(
        SchemaArn='string'
    )
    
    
    :type SchemaArn: string
    :param SchemaArn: [REQUIRED]
            The ARN of the schema to retrieve.
            

    :rtype: dict
    :return: {
        'Name': 'string',
        'Document': 'string'
    }
    
    
    """
    pass

def get_typed_link_facet_information(SchemaArn=None, Name=None):
    """
    Returns the identity attribute order for a specific  TypedLinkFacet . For more information, see Typed link .
    See also: AWS API Documentation
    
    
    :example: response = client.get_typed_link_facet_information(
        SchemaArn='string',
        Name='string'
    )
    
    
    :type SchemaArn: string
    :param SchemaArn: [REQUIRED]
            The Amazon Resource Name (ARN) that is associated with the schema. For more information, see arns .
            

    :type Name: string
    :param Name: [REQUIRED]
            The unique name of the typed link facet.
            

    :rtype: dict
    :return: {
        'IdentityAttributeOrder': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_waiter():
    """
    
    """
    pass

def list_applied_schema_arns(DirectoryArn=None, NextToken=None, MaxResults=None):
    """
    Lists schemas applied to a directory.
    See also: AWS API Documentation
    
    
    :example: response = client.list_applied_schema_arns(
        DirectoryArn='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]
            The ARN of the directory you are listing.
            

    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to retrieve.

    :rtype: dict
    :return: {
        'SchemaArns': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_attached_indices(DirectoryArn=None, TargetReference=None, NextToken=None, MaxResults=None, ConsistencyLevel=None):
    """
    Lists indices attached to an object.
    See also: AWS API Documentation
    
    
    :example: response = client.list_attached_indices(
        DirectoryArn='string',
        TargetReference={
            'Selector': 'string'
        },
        NextToken='string',
        MaxResults=123,
        ConsistencyLevel='SERIALIZABLE'|'EVENTUAL'
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]
            The ARN of the directory.
            

    :type TargetReference: dict
    :param TargetReference: [REQUIRED]
            A reference to the object to that has indices attached.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            

    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to retrieve.

    :type ConsistencyLevel: string
    :param ConsistencyLevel: The consistency level to use for this operation.

    :rtype: dict
    :return: {
        'IndexAttachments': [
            {
                'IndexedAttributes': [
                    {
                        'Key': {
                            'SchemaArn': 'string',
                            'FacetName': 'string',
                            'Name': 'string'
                        },
                        'Value': {
                            'StringValue': 'string',
                            'BinaryValue': b'bytes',
                            'BooleanValue': True|False,
                            'NumberValue': 'string',
                            'DatetimeValue': datetime(2015, 1, 1)
                        }
                    },
                ],
                'ObjectIdentifier': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_development_schema_arns(NextToken=None, MaxResults=None):
    """
    Retrieves each Amazon Resource Name (ARN) of schemas in the development state.
    See also: AWS API Documentation
    
    
    :example: response = client.list_development_schema_arns(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to retrieve.

    :rtype: dict
    :return: {
        'SchemaArns': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_directories(NextToken=None, MaxResults=None, state=None):
    """
    Lists directories created within an account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_directories(
        NextToken='string',
        MaxResults=123,
        state='ENABLED'|'DISABLED'|'DELETED'
    )
    
    
    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to retrieve.

    :type state: string
    :param state: The state of the directories in the list. Can be either Enabled, Disabled, or Deleted.

    :rtype: dict
    :return: {
        'Directories': [
            {
                'Name': 'string',
                'DirectoryArn': 'string',
                'State': 'ENABLED'|'DISABLED'|'DELETED',
                'CreationDateTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_facet_attributes(SchemaArn=None, Name=None, NextToken=None, MaxResults=None):
    """
    Retrieves attributes attached to the facet.
    See also: AWS API Documentation
    
    
    :example: response = client.list_facet_attributes(
        SchemaArn='string',
        Name='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type SchemaArn: string
    :param SchemaArn: [REQUIRED]
            The ARN of the schema where the facet resides.
            

    :type Name: string
    :param Name: [REQUIRED]
            The name of the facet whose attributes will be retrieved.
            

    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to retrieve.

    :rtype: dict
    :return: {
        'Attributes': [
            {
                'Name': 'string',
                'AttributeDefinition': {
                    'Type': 'STRING'|'BINARY'|'BOOLEAN'|'NUMBER'|'DATETIME',
                    'DefaultValue': {
                        'StringValue': 'string',
                        'BinaryValue': b'bytes',
                        'BooleanValue': True|False,
                        'NumberValue': 'string',
                        'DatetimeValue': datetime(2015, 1, 1)
                    },
                    'IsImmutable': True|False,
                    'Rules': {
                        'string': {
                            'Type': 'BINARY_LENGTH'|'NUMBER_COMPARISON'|'STRING_FROM_SET'|'STRING_LENGTH',
                            'Parameters': {
                                'string': 'string'
                            }
                        }
                    }
                },
                'AttributeReference': {
                    'TargetFacetName': 'string',
                    'TargetAttributeName': 'string'
                },
                'RequiredBehavior': 'REQUIRED_ALWAYS'|'NOT_REQUIRED'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_facet_names(SchemaArn=None, NextToken=None, MaxResults=None):
    """
    Retrieves the names of facets that exist in a schema.
    See also: AWS API Documentation
    
    
    :example: response = client.list_facet_names(
        SchemaArn='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type SchemaArn: string
    :param SchemaArn: [REQUIRED]
            The Amazon Resource Name (ARN) to retrieve facet names from.
            

    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to retrieve.

    :rtype: dict
    :return: {
        'FacetNames': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_incoming_typed_links(DirectoryArn=None, ObjectReference=None, FilterAttributeRanges=None, FilterTypedLink=None, NextToken=None, MaxResults=None, ConsistencyLevel=None):
    """
    Returns a paginated list of all the incoming  TypedLinkSpecifier information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see Typed link .
    See also: AWS API Documentation
    
    
    :example: response = client.list_incoming_typed_links(
        DirectoryArn='string',
        ObjectReference={
            'Selector': 'string'
        },
        FilterAttributeRanges=[
            {
                'AttributeName': 'string',
                'Range': {
                    'StartMode': 'FIRST'|'LAST'|'LAST_BEFORE_MISSING_VALUES'|'INCLUSIVE'|'EXCLUSIVE',
                    'StartValue': {
                        'StringValue': 'string',
                        'BinaryValue': b'bytes',
                        'BooleanValue': True|False,
                        'NumberValue': 'string',
                        'DatetimeValue': datetime(2015, 1, 1)
                    },
                    'EndMode': 'FIRST'|'LAST'|'LAST_BEFORE_MISSING_VALUES'|'INCLUSIVE'|'EXCLUSIVE',
                    'EndValue': {
                        'StringValue': 'string',
                        'BinaryValue': b'bytes',
                        'BooleanValue': True|False,
                        'NumberValue': 'string',
                        'DatetimeValue': datetime(2015, 1, 1)
                    }
                }
            },
        ],
        FilterTypedLink={
            'SchemaArn': 'string',
            'TypedLinkName': 'string'
        },
        NextToken='string',
        MaxResults=123,
        ConsistencyLevel='SERIALIZABLE'|'EVENTUAL'
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the directory where you want to list the typed links.
            

    :type ObjectReference: dict
    :param ObjectReference: [REQUIRED]
            Reference that identifies the object whose attributes will be listed.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            

    :type FilterAttributeRanges: list
    :param FilterAttributeRanges: Provides range filters for multiple attributes. When providing ranges to typed link selection, any inexact ranges must be specified at the end. Any attributes that do not have a range specified are presumed to match the entire range.
            (dict) --Identifies the range of attributes that are used by a specified filter.
            AttributeName (string) --The unique name of the typed link attribute.
            Range (dict) -- [REQUIRED]The range of attribute values that are being selected.
            StartMode (string) -- [REQUIRED]The inclusive or exclusive range start.
            StartValue (dict) --The value to start the range at.
            StringValue (string) --A string data value.
            BinaryValue (bytes) --A binary data value.
            BooleanValue (boolean) --A Boolean data value.
            NumberValue (string) --A number data value.
            DatetimeValue (datetime) --A date and time value.
            EndMode (string) -- [REQUIRED]The inclusive or exclusive range end.
            EndValue (dict) --The attribute value to terminate the range at.
            StringValue (string) --A string data value.
            BinaryValue (bytes) --A binary data value.
            BooleanValue (boolean) --A Boolean data value.
            NumberValue (string) --A number data value.
            DatetimeValue (datetime) --A date and time value.
            
            
            

    :type FilterTypedLink: dict
    :param FilterTypedLink: Filters are interpreted in the order of the attributes on the typed link facet, not the order in which they are supplied to any API calls.
            SchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) that is associated with the schema. For more information, see arns .
            TypedLinkName (string) -- [REQUIRED]The unique name of the typed link facet.
            

    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to retrieve.

    :type ConsistencyLevel: string
    :param ConsistencyLevel: The consistency level to execute the request at.

    :rtype: dict
    :return: {
        'LinkSpecifiers': [
            {
                'TypedLinkFacet': {
                    'SchemaArn': 'string',
                    'TypedLinkName': 'string'
                },
                'SourceObjectReference': {
                    'Selector': 'string'
                },
                'TargetObjectReference': {
                    'Selector': 'string'
                },
                'IdentityAttributeValues': [
                    {
                        'AttributeName': 'string',
                        'Value': {
                            'StringValue': 'string',
                            'BinaryValue': b'bytes',
                            'BooleanValue': True|False,
                            'NumberValue': 'string',
                            'DatetimeValue': datetime(2015, 1, 1)
                        }
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objects identifier is immutable and no two objects will ever share the same object identifier
    /some/path - Identifies the object based on path
    #SomeBatchReference - Identifies the object in a batch call
    
    """
    pass

def list_index(DirectoryArn=None, RangesOnIndexedValues=None, IndexReference=None, MaxResults=None, NextToken=None, ConsistencyLevel=None):
    """
    Lists objects attached to the specified index.
    See also: AWS API Documentation
    
    
    :example: response = client.list_index(
        DirectoryArn='string',
        RangesOnIndexedValues=[
            {
                'AttributeKey': {
                    'SchemaArn': 'string',
                    'FacetName': 'string',
                    'Name': 'string'
                },
                'Range': {
                    'StartMode': 'FIRST'|'LAST'|'LAST_BEFORE_MISSING_VALUES'|'INCLUSIVE'|'EXCLUSIVE',
                    'StartValue': {
                        'StringValue': 'string',
                        'BinaryValue': b'bytes',
                        'BooleanValue': True|False,
                        'NumberValue': 'string',
                        'DatetimeValue': datetime(2015, 1, 1)
                    },
                    'EndMode': 'FIRST'|'LAST'|'LAST_BEFORE_MISSING_VALUES'|'INCLUSIVE'|'EXCLUSIVE',
                    'EndValue': {
                        'StringValue': 'string',
                        'BinaryValue': b'bytes',
                        'BooleanValue': True|False,
                        'NumberValue': 'string',
                        'DatetimeValue': datetime(2015, 1, 1)
                    }
                }
            },
        ],
        IndexReference={
            'Selector': 'string'
        },
        MaxResults=123,
        NextToken='string',
        ConsistencyLevel='SERIALIZABLE'|'EVENTUAL'
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]
            The ARN of the directory that the index exists in.
            

    :type RangesOnIndexedValues: list
    :param RangesOnIndexedValues: Specifies the ranges of indexed values that you want to query.
            (dict) --A range of attributes.
            AttributeKey (dict) --The key of the attribute that the attribute range covers.
            SchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
            FacetName (string) -- [REQUIRED]The name of the facet that the attribute exists within.
            Name (string) -- [REQUIRED]The name of the attribute.
            Range (dict) --The range of attribute values being selected.
            StartMode (string) -- [REQUIRED]The inclusive or exclusive range start.
            StartValue (dict) --The value to start the range at.
            StringValue (string) --A string data value.
            BinaryValue (bytes) --A binary data value.
            BooleanValue (boolean) --A Boolean data value.
            NumberValue (string) --A number data value.
            DatetimeValue (datetime) --A date and time value.
            EndMode (string) -- [REQUIRED]The inclusive or exclusive range end.
            EndValue (dict) --The attribute value to terminate the range at.
            StringValue (string) --A string data value.
            BinaryValue (bytes) --A binary data value.
            BooleanValue (boolean) --A Boolean data value.
            NumberValue (string) --A number data value.
            DatetimeValue (datetime) --A date and time value.
            
            
            

    :type IndexReference: dict
    :param IndexReference: [REQUIRED]
            The reference to the index to list.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to retrieve from the index.

    :type NextToken: string
    :param NextToken: The pagination token.

    :type ConsistencyLevel: string
    :param ConsistencyLevel: The consistency level to execute the request at.

    :rtype: dict
    :return: {
        'IndexAttachments': [
            {
                'IndexedAttributes': [
                    {
                        'Key': {
                            'SchemaArn': 'string',
                            'FacetName': 'string',
                            'Name': 'string'
                        },
                        'Value': {
                            'StringValue': 'string',
                            'BinaryValue': b'bytes',
                            'BooleanValue': True|False,
                            'NumberValue': 'string',
                            'DatetimeValue': datetime(2015, 1, 1)
                        }
                    },
                ],
                'ObjectIdentifier': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_object_attributes(DirectoryArn=None, ObjectReference=None, NextToken=None, MaxResults=None, ConsistencyLevel=None, FacetFilter=None):
    """
    Lists all attributes that are associated with an object.
    See also: AWS API Documentation
    
    
    :example: response = client.list_object_attributes(
        DirectoryArn='string',
        ObjectReference={
            'Selector': 'string'
        },
        NextToken='string',
        MaxResults=123,
        ConsistencyLevel='SERIALIZABLE'|'EVENTUAL',
        FacetFilter={
            'SchemaArn': 'string',
            'FacetName': 'string'
        }
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]
            The Amazon Resource Name (ARN) that is associated with the Directory where the object resides. For more information, see arns .
            

    :type ObjectReference: dict
    :param ObjectReference: [REQUIRED]
            The reference that identifies the object whose attributes will be listed.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            

    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to be retrieved in a single call. This is an approximate number.

    :type ConsistencyLevel: string
    :param ConsistencyLevel: Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.

    :type FacetFilter: dict
    :param FacetFilter: Used to filter the list of object attributes that are associated with a certain facet.
            SchemaArn (string) --The ARN of the schema that contains the facet.
            FacetName (string) --The name of the facet.
            

    :rtype: dict
    :return: {
        'Attributes': [
            {
                'Key': {
                    'SchemaArn': 'string',
                    'FacetName': 'string',
                    'Name': 'string'
                },
                'Value': {
                    'StringValue': 'string',
                    'BinaryValue': b'bytes',
                    'BooleanValue': True|False,
                    'NumberValue': 'string',
                    'DatetimeValue': datetime(2015, 1, 1)
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_object_children(DirectoryArn=None, ObjectReference=None, NextToken=None, MaxResults=None, ConsistencyLevel=None):
    """
    Returns a paginated list of child objects that are associated with a given object.
    See also: AWS API Documentation
    
    
    :example: response = client.list_object_children(
        DirectoryArn='string',
        ObjectReference={
            'Selector': 'string'
        },
        NextToken='string',
        MaxResults=123,
        ConsistencyLevel='SERIALIZABLE'|'EVENTUAL'
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]
            The Amazon Resource Name (ARN) that is associated with the Directory where the object resides. For more information, see arns .
            

    :type ObjectReference: dict
    :param ObjectReference: [REQUIRED]
            The reference that identifies the object for which child objects are being listed.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            

    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to be retrieved in a single call. This is an approximate number.

    :type ConsistencyLevel: string
    :param ConsistencyLevel: Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.

    :rtype: dict
    :return: {
        'Children': {
            'string': 'string'
        },
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_object_parent_paths(DirectoryArn=None, ObjectReference=None, NextToken=None, MaxResults=None):
    """
    Retrieves all available parent paths for any object type such as node, leaf node, policy node, and index node objects. For more information about objects, see Directory Structure .
    Use this API to evaluate all parents for an object. The call returns all objects from the root of the directory up to the requested object. The API returns the number of paths based on user-defined MaxResults , in case there are multiple paths to the parent. The order of the paths and nodes returned is consistent among multiple API calls unless the objects are deleted or moved. Paths not leading to the directory root are ignored from the target object.
    See also: AWS API Documentation
    
    
    :example: response = client.list_object_parent_paths(
        DirectoryArn='string',
        ObjectReference={
            'Selector': 'string'
        },
        NextToken='string',
        MaxResults=123
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]
            The ARN of the directory to which the parent path applies.
            

    :type ObjectReference: dict
    :param ObjectReference: [REQUIRED]
            The reference that identifies the object whose parent paths are listed.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            

    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to be retrieved in a single call. This is an approximate number.

    :rtype: dict
    :return: {
        'PathToObjectIdentifiersList': [
            {
                'Path': 'string',
                'ObjectIdentifiers': [
                    'string',
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_object_parents(DirectoryArn=None, ObjectReference=None, NextToken=None, MaxResults=None, ConsistencyLevel=None):
    """
    Lists parent objects that are associated with a given object in pagination fashion.
    See also: AWS API Documentation
    
    
    :example: response = client.list_object_parents(
        DirectoryArn='string',
        ObjectReference={
            'Selector': 'string'
        },
        NextToken='string',
        MaxResults=123,
        ConsistencyLevel='SERIALIZABLE'|'EVENTUAL'
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]
            The Amazon Resource Name (ARN) that is associated with the Directory where the object resides. For more information, see arns .
            

    :type ObjectReference: dict
    :param ObjectReference: [REQUIRED]
            The reference that identifies the object for which parent objects are being listed.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            

    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to be retrieved in a single call. This is an approximate number.

    :type ConsistencyLevel: string
    :param ConsistencyLevel: Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.

    :rtype: dict
    :return: {
        'Parents': {
            'string': 'string'
        },
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_object_policies(DirectoryArn=None, ObjectReference=None, NextToken=None, MaxResults=None, ConsistencyLevel=None):
    """
    Returns policies attached to an object in pagination fashion.
    See also: AWS API Documentation
    
    
    :example: response = client.list_object_policies(
        DirectoryArn='string',
        ObjectReference={
            'Selector': 'string'
        },
        NextToken='string',
        MaxResults=123,
        ConsistencyLevel='SERIALIZABLE'|'EVENTUAL'
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]
            The Amazon Resource Name (ARN) that is associated with the Directory where objects reside. For more information, see arns .
            

    :type ObjectReference: dict
    :param ObjectReference: [REQUIRED]
            Reference that identifies the object for which policies will be listed.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            

    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to be retrieved in a single call. This is an approximate number.

    :type ConsistencyLevel: string
    :param ConsistencyLevel: Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.

    :rtype: dict
    :return: {
        'AttachedPolicyIds': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_outgoing_typed_links(DirectoryArn=None, ObjectReference=None, FilterAttributeRanges=None, FilterTypedLink=None, NextToken=None, MaxResults=None, ConsistencyLevel=None):
    """
    Returns a paginated list of all the outgoing  TypedLinkSpecifier information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see Typed link .
    See also: AWS API Documentation
    
    
    :example: response = client.list_outgoing_typed_links(
        DirectoryArn='string',
        ObjectReference={
            'Selector': 'string'
        },
        FilterAttributeRanges=[
            {
                'AttributeName': 'string',
                'Range': {
                    'StartMode': 'FIRST'|'LAST'|'LAST_BEFORE_MISSING_VALUES'|'INCLUSIVE'|'EXCLUSIVE',
                    'StartValue': {
                        'StringValue': 'string',
                        'BinaryValue': b'bytes',
                        'BooleanValue': True|False,
                        'NumberValue': 'string',
                        'DatetimeValue': datetime(2015, 1, 1)
                    },
                    'EndMode': 'FIRST'|'LAST'|'LAST_BEFORE_MISSING_VALUES'|'INCLUSIVE'|'EXCLUSIVE',
                    'EndValue': {
                        'StringValue': 'string',
                        'BinaryValue': b'bytes',
                        'BooleanValue': True|False,
                        'NumberValue': 'string',
                        'DatetimeValue': datetime(2015, 1, 1)
                    }
                }
            },
        ],
        FilterTypedLink={
            'SchemaArn': 'string',
            'TypedLinkName': 'string'
        },
        NextToken='string',
        MaxResults=123,
        ConsistencyLevel='SERIALIZABLE'|'EVENTUAL'
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the directory where you want to list the typed links.
            

    :type ObjectReference: dict
    :param ObjectReference: [REQUIRED]
            A reference that identifies the object whose attributes will be listed.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            

    :type FilterAttributeRanges: list
    :param FilterAttributeRanges: Provides range filters for multiple attributes. When providing ranges to typed link selection, any inexact ranges must be specified at the end. Any attributes that do not have a range specified are presumed to match the entire range.
            (dict) --Identifies the range of attributes that are used by a specified filter.
            AttributeName (string) --The unique name of the typed link attribute.
            Range (dict) -- [REQUIRED]The range of attribute values that are being selected.
            StartMode (string) -- [REQUIRED]The inclusive or exclusive range start.
            StartValue (dict) --The value to start the range at.
            StringValue (string) --A string data value.
            BinaryValue (bytes) --A binary data value.
            BooleanValue (boolean) --A Boolean data value.
            NumberValue (string) --A number data value.
            DatetimeValue (datetime) --A date and time value.
            EndMode (string) -- [REQUIRED]The inclusive or exclusive range end.
            EndValue (dict) --The attribute value to terminate the range at.
            StringValue (string) --A string data value.
            BinaryValue (bytes) --A binary data value.
            BooleanValue (boolean) --A Boolean data value.
            NumberValue (string) --A number data value.
            DatetimeValue (datetime) --A date and time value.
            
            
            

    :type FilterTypedLink: dict
    :param FilterTypedLink: Filters are interpreted in the order of the attributes defined on the typed link facet, not the order they are supplied to any API calls.
            SchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) that is associated with the schema. For more information, see arns .
            TypedLinkName (string) -- [REQUIRED]The unique name of the typed link facet.
            

    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to retrieve.

    :type ConsistencyLevel: string
    :param ConsistencyLevel: The consistency level to execute the request at.

    :rtype: dict
    :return: {
        'TypedLinkSpecifiers': [
            {
                'TypedLinkFacet': {
                    'SchemaArn': 'string',
                    'TypedLinkName': 'string'
                },
                'SourceObjectReference': {
                    'Selector': 'string'
                },
                'TargetObjectReference': {
                    'Selector': 'string'
                },
                'IdentityAttributeValues': [
                    {
                        'AttributeName': 'string',
                        'Value': {
                            'StringValue': 'string',
                            'BinaryValue': b'bytes',
                            'BooleanValue': True|False,
                            'NumberValue': 'string',
                            'DatetimeValue': datetime(2015, 1, 1)
                        }
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objects identifier is immutable and no two objects will ever share the same object identifier
    /some/path - Identifies the object based on path
    #SomeBatchReference - Identifies the object in a batch call
    
    """
    pass

def list_policy_attachments(DirectoryArn=None, PolicyReference=None, NextToken=None, MaxResults=None, ConsistencyLevel=None):
    """
    Returns all of the ObjectIdentifiers to which a given policy is attached.
    See also: AWS API Documentation
    
    
    :example: response = client.list_policy_attachments(
        DirectoryArn='string',
        PolicyReference={
            'Selector': 'string'
        },
        NextToken='string',
        MaxResults=123,
        ConsistencyLevel='SERIALIZABLE'|'EVENTUAL'
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]
            The Amazon Resource Name (ARN) that is associated with the Directory where objects reside. For more information, see arns .
            

    :type PolicyReference: dict
    :param PolicyReference: [REQUIRED]
            The reference that identifies the policy object.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            

    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to be retrieved in a single call. This is an approximate number.

    :type ConsistencyLevel: string
    :param ConsistencyLevel: Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.

    :rtype: dict
    :return: {
        'ObjectIdentifiers': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_published_schema_arns(NextToken=None, MaxResults=None):
    """
    Retrieves each published schema Amazon Resource Name (ARN).
    See also: AWS API Documentation
    
    
    :example: response = client.list_published_schema_arns(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to retrieve.

    :rtype: dict
    :return: {
        'SchemaArns': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_tags_for_resource(ResourceArn=None, NextToken=None, MaxResults=None):
    """
    Returns tags for a resource. Tagging is currently supported only for directories with a limit of 50 tags per directory. All 50 tags are returned for a given directory with this API call.
    See also: AWS API Documentation
    
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource. Tagging is only supported for directories.
            

    :type NextToken: string
    :param NextToken: The pagination token. This is for future use. Currently pagination is not supported for tagging.

    :type MaxResults: integer
    :param MaxResults: The MaxResults parameter sets the maximum number of results returned in a single page. This is for future use and is not supported currently.

    :rtype: dict
    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_typed_link_facet_attributes(SchemaArn=None, Name=None, NextToken=None, MaxResults=None):
    """
    Returns a paginated list of all attribute definitions for a particular  TypedLinkFacet . For more information, see Typed link .
    See also: AWS API Documentation
    
    
    :example: response = client.list_typed_link_facet_attributes(
        SchemaArn='string',
        Name='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type SchemaArn: string
    :param SchemaArn: [REQUIRED]
            The Amazon Resource Name (ARN) that is associated with the schema. For more information, see arns .
            

    :type Name: string
    :param Name: [REQUIRED]
            The unique name of the typed link facet.
            

    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to retrieve.

    :rtype: dict
    :return: {
        'Attributes': [
            {
                'Name': 'string',
                'Type': 'STRING'|'BINARY'|'BOOLEAN'|'NUMBER'|'DATETIME',
                'DefaultValue': {
                    'StringValue': 'string',
                    'BinaryValue': b'bytes',
                    'BooleanValue': True|False,
                    'NumberValue': 'string',
                    'DatetimeValue': datetime(2015, 1, 1)
                },
                'IsImmutable': True|False,
                'Rules': {
                    'string': {
                        'Type': 'BINARY_LENGTH'|'NUMBER_COMPARISON'|'STRING_FROM_SET'|'STRING_LENGTH',
                        'Parameters': {
                            'string': 'string'
                        }
                    }
                },
                'RequiredBehavior': 'REQUIRED_ALWAYS'|'NOT_REQUIRED'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_typed_link_facet_names(SchemaArn=None, NextToken=None, MaxResults=None):
    """
    Returns a paginated list of TypedLink facet names for a particular schema. For more information, see Typed link .
    See also: AWS API Documentation
    
    
    :example: response = client.list_typed_link_facet_names(
        SchemaArn='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type SchemaArn: string
    :param SchemaArn: [REQUIRED]
            The Amazon Resource Name (ARN) that is associated with the schema. For more information, see arns .
            

    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to retrieve.

    :rtype: dict
    :return: {
        'FacetNames': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def lookup_policy(DirectoryArn=None, ObjectReference=None, NextToken=None, MaxResults=None):
    """
    Lists all policies from the root of the  Directory to the object specified. If there are no policies present, an empty list is returned. If policies are present, and if some objects don't have the policies attached, it returns the ObjectIdentifier for such objects. If policies are present, it returns ObjectIdentifier , policyId , and policyType . Paths that don't lead to the root from the target object are ignored. For more information, see Policies .
    See also: AWS API Documentation
    
    
    :example: response = client.lookup_policy(
        DirectoryArn='string',
        ObjectReference={
            'Selector': 'string'
        },
        NextToken='string',
        MaxResults=123
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]
            The Amazon Resource Name (ARN) that is associated with the Directory . For more information, see arns .
            

    :type ObjectReference: dict
    :param ObjectReference: [REQUIRED]
            Reference that identifies the object whose policies will be looked up.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            

    :type NextToken: string
    :param NextToken: The token to request the next page of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to be retrieved in a single call. This is an approximate number.

    :rtype: dict
    :return: {
        'PolicyToPathList': [
            {
                'Path': 'string',
                'Policies': [
                    {
                        'PolicyId': 'string',
                        'ObjectIdentifier': 'string',
                        'PolicyType': 'string'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def publish_schema(DevelopmentSchemaArn=None, Version=None, Name=None):
    """
    Publishes a development schema with a version. If description and attributes are specified, PublishSchema overrides the development schema description and attributes. If not, the development schema description and attributes are used.
    See also: AWS API Documentation
    
    
    :example: response = client.publish_schema(
        DevelopmentSchemaArn='string',
        Version='string',
        Name='string'
    )
    
    
    :type DevelopmentSchemaArn: string
    :param DevelopmentSchemaArn: [REQUIRED]
            The Amazon Resource Name (ARN) that is associated with the development schema. For more information, see arns .
            

    :type Version: string
    :param Version: [REQUIRED]
            The version under which the schema will be published.
            

    :type Name: string
    :param Name: The new name under which the schema will be published. If this is not provided, the development schema is considered.

    :rtype: dict
    :return: {
        'PublishedSchemaArn': 'string'
    }
    
    
    """
    pass

def put_schema_from_json(SchemaArn=None, Document=None):
    """
    Allows a schema to be updated using JSON upload. Only available for development schemas. See JSON Schema Format for more information.
    See also: AWS API Documentation
    
    
    :example: response = client.put_schema_from_json(
        SchemaArn='string',
        Document='string'
    )
    
    
    :type SchemaArn: string
    :param SchemaArn: [REQUIRED]
            The ARN of the schema to update.
            

    :type Document: string
    :param Document: [REQUIRED]
            The replacement JSON schema.
            

    :rtype: dict
    :return: {
        'Arn': 'string'
    }
    
    
    """
    pass

def remove_facet_from_object(DirectoryArn=None, SchemaFacet=None, ObjectReference=None):
    """
    Removes the specified facet from the specified object.
    See also: AWS API Documentation
    
    
    :example: response = client.remove_facet_from_object(
        DirectoryArn='string',
        SchemaFacet={
            'SchemaArn': 'string',
            'FacetName': 'string'
        },
        ObjectReference={
            'Selector': 'string'
        }
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]
            The ARN of the directory in which the object resides.
            

    :type SchemaFacet: dict
    :param SchemaFacet: [REQUIRED]
            The facet to remove.
            SchemaArn (string) --The ARN of the schema that contains the facet.
            FacetName (string) --The name of the facet.
            

    :type ObjectReference: dict
    :param ObjectReference: [REQUIRED]
            A reference to the object to remove the facet from.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def tag_resource(ResourceArn=None, Tags=None):
    """
    An API operation for adding tags to a resource.
    See also: AWS API Documentation
    
    
    :example: response = client.tag_resource(
        ResourceArn='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource. Tagging is only supported for directories.
            

    :type Tags: list
    :param Tags: [REQUIRED]
            A list of tag key-value pairs.
            (dict) --The tag structure that contains a tag key and value.
            Key (string) --The key that is associated with the tag.
            Value (string) --The value that is associated with the tag.
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceArn=None, TagKeys=None):
    """
    An API operation for removing tags from a resource.
    See also: AWS API Documentation
    
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource. Tagging is only supported for directories.
            

    :type TagKeys: list
    :param TagKeys: [REQUIRED]
            Keys of the tag that need to be removed from the resource.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_facet(SchemaArn=None, Name=None, AttributeUpdates=None, ObjectType=None):
    """
    Does the following:
    See also: AWS API Documentation
    
    
    :example: response = client.update_facet(
        SchemaArn='string',
        Name='string',
        AttributeUpdates=[
            {
                'Attribute': {
                    'Name': 'string',
                    'AttributeDefinition': {
                        'Type': 'STRING'|'BINARY'|'BOOLEAN'|'NUMBER'|'DATETIME',
                        'DefaultValue': {
                            'StringValue': 'string',
                            'BinaryValue': b'bytes',
                            'BooleanValue': True|False,
                            'NumberValue': 'string',
                            'DatetimeValue': datetime(2015, 1, 1)
                        },
                        'IsImmutable': True|False,
                        'Rules': {
                            'string': {
                                'Type': 'BINARY_LENGTH'|'NUMBER_COMPARISON'|'STRING_FROM_SET'|'STRING_LENGTH',
                                'Parameters': {
                                    'string': 'string'
                                }
                            }
                        }
                    },
                    'AttributeReference': {
                        'TargetFacetName': 'string',
                        'TargetAttributeName': 'string'
                    },
                    'RequiredBehavior': 'REQUIRED_ALWAYS'|'NOT_REQUIRED'
                },
                'Action': 'CREATE_OR_UPDATE'|'DELETE'
            },
        ],
        ObjectType='NODE'|'LEAF_NODE'|'POLICY'|'INDEX'
    )
    
    
    :type SchemaArn: string
    :param SchemaArn: [REQUIRED]
            The Amazon Resource Name (ARN) that is associated with the Facet . For more information, see arns .
            

    :type Name: string
    :param Name: [REQUIRED]
            The name of the facet.
            

    :type AttributeUpdates: list
    :param AttributeUpdates: List of attributes that need to be updated in a given schema Facet . Each attribute is followed by AttributeAction , which specifies the type of update operation to perform.
            (dict) --A structure that contains information used to update an attribute.
            Attribute (dict) --The attribute to update.
            Name (string) -- [REQUIRED]The name of the facet attribute.
            AttributeDefinition (dict) --A facet attribute consists of either a definition or a reference. This structure contains the attribute definition. See Attribute References for more information.
            Type (string) -- [REQUIRED]The type of the attribute.
            DefaultValue (dict) --The default value of the attribute (if configured).
            StringValue (string) --A string data value.
            BinaryValue (bytes) --A binary data value.
            BooleanValue (boolean) --A Boolean data value.
            NumberValue (string) --A number data value.
            DatetimeValue (datetime) --A date and time value.
            IsImmutable (boolean) --Whether the attribute is mutable or not.
            Rules (dict) --Validation rules attached to the attribute definition.
            (string) --
            (dict) --Contains an Amazon Resource Name (ARN) and parameters that are associated with the rule.
            Type (string) --The type of attribute validation rule.
            Parameters (dict) --The minimum and maximum parameters that are associated with the rule.
            (string) --
            (string) --
            
            
            
            AttributeReference (dict) --An attribute reference that is associated with the attribute. See Attribute References for more information.
            TargetFacetName (string) -- [REQUIRED]The target facet name that is associated with the facet reference. See Attribute References for more information.
            TargetAttributeName (string) -- [REQUIRED]The target attribute name that is associated with the facet reference. See Attribute References for more information.
            RequiredBehavior (string) --The required behavior of the FacetAttribute .
            Action (string) --The action to perform when updating the attribute.
            
            

    :type ObjectType: string
    :param ObjectType: The object type that is associated with the facet. See CreateFacetRequest$ObjectType for more details.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    SchemaArn (string) -- [REQUIRED]
    The Amazon Resource Name (ARN) that is associated with the  Facet . For more information, see  arns .
    
    Name (string) -- [REQUIRED]
    The name of the facet.
    
    AttributeUpdates (list) -- List of attributes that need to be updated in a given schema  Facet . Each attribute is followed by AttributeAction , which specifies the type of update operation to perform.
    
    (dict) --A structure that contains information used to update an attribute.
    
    Attribute (dict) --The attribute to update.
    
    Name (string) -- [REQUIRED]The name of the facet attribute.
    
    AttributeDefinition (dict) --A facet attribute consists of either a definition or a reference. This structure contains the attribute definition. See Attribute References for more information.
    
    Type (string) -- [REQUIRED]The type of the attribute.
    
    DefaultValue (dict) --The default value of the attribute (if configured).
    
    StringValue (string) --A string data value.
    
    BinaryValue (bytes) --A binary data value.
    
    BooleanValue (boolean) --A Boolean data value.
    
    NumberValue (string) --A number data value.
    
    DatetimeValue (datetime) --A date and time value.
    
    
    
    IsImmutable (boolean) --Whether the attribute is mutable or not.
    
    Rules (dict) --Validation rules attached to the attribute definition.
    
    (string) --
    (dict) --Contains an Amazon Resource Name (ARN) and parameters that are associated with the rule.
    
    Type (string) --The type of attribute validation rule.
    
    Parameters (dict) --The minimum and maximum parameters that are associated with the rule.
    
    (string) --
    (string) --
    
    
    
    
    
    
    
    
    
    
    
    
    AttributeReference (dict) --An attribute reference that is associated with the attribute. See Attribute References for more information.
    
    TargetFacetName (string) -- [REQUIRED]The target facet name that is associated with the facet reference. See Attribute References for more information.
    
    TargetAttributeName (string) -- [REQUIRED]The target attribute name that is associated with the facet reference. See Attribute References for more information.
    
    
    
    RequiredBehavior (string) --The required behavior of the FacetAttribute .
    
    
    
    Action (string) --The action to perform when updating the attribute.
    
    
    
    
    
    ObjectType (string) -- The object type that is associated with the facet. See  CreateFacetRequest$ObjectType for more details.
    
    """
    pass

def update_object_attributes(DirectoryArn=None, ObjectReference=None, AttributeUpdates=None):
    """
    Updates a given object's attributes.
    See also: AWS API Documentation
    
    
    :example: response = client.update_object_attributes(
        DirectoryArn='string',
        ObjectReference={
            'Selector': 'string'
        },
        AttributeUpdates=[
            {
                'ObjectAttributeKey': {
                    'SchemaArn': 'string',
                    'FacetName': 'string',
                    'Name': 'string'
                },
                'ObjectAttributeAction': {
                    'ObjectAttributeActionType': 'CREATE_OR_UPDATE'|'DELETE',
                    'ObjectAttributeUpdateValue': {
                        'StringValue': 'string',
                        'BinaryValue': b'bytes',
                        'BooleanValue': True|False,
                        'NumberValue': 'string',
                        'DatetimeValue': datetime(2015, 1, 1)
                    }
                }
            },
        ]
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]
            The Amazon Resource Name (ARN) that is associated with the Directory where the object resides. For more information, see arns .
            

    :type ObjectReference: dict
    :param ObjectReference: [REQUIRED]
            The reference that identifies the object.
            Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Accessing Objects . You can identify an object in one of the following ways:
            $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object s identifier is immutable and no two objects will ever share the same object identifier
            /some/path - Identifies the object based on path
            #SomeBatchReference - Identifies the object in a batch call
            

    :type AttributeUpdates: list
    :param AttributeUpdates: [REQUIRED]
            The attributes update structure.
            (dict) --Structure that contains attribute update information.
            ObjectAttributeKey (dict) --The key of the attribute being updated.
            SchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
            FacetName (string) -- [REQUIRED]The name of the facet that the attribute exists within.
            Name (string) -- [REQUIRED]The name of the attribute.
            ObjectAttributeAction (dict) --The action to perform as part of the attribute update.
            ObjectAttributeActionType (string) --A type that can be either Update or Delete .
            ObjectAttributeUpdateValue (dict) --The value that you want to update to.
            StringValue (string) --A string data value.
            BinaryValue (bytes) --A binary data value.
            BooleanValue (boolean) --A Boolean data value.
            NumberValue (string) --A number data value.
            DatetimeValue (datetime) --A date and time value.
            
            
            

    :rtype: dict
    :return: {
        'ObjectIdentifier': 'string'
    }
    
    
    """
    pass

def update_schema(SchemaArn=None, Name=None):
    """
    Updates the schema name with a new name. Only development schema names can be updated.
    See also: AWS API Documentation
    
    
    :example: response = client.update_schema(
        SchemaArn='string',
        Name='string'
    )
    
    
    :type SchemaArn: string
    :param SchemaArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the development schema. For more information, see arns .
            

    :type Name: string
    :param Name: [REQUIRED]
            The name of the schema.
            

    :rtype: dict
    :return: {
        'SchemaArn': 'string'
    }
    
    
    """
    pass

def update_typed_link_facet(SchemaArn=None, Name=None, AttributeUpdates=None, IdentityAttributeOrder=None):
    """
    Updates a  TypedLinkFacet . For more information, see Typed link .
    See also: AWS API Documentation
    
    
    :example: response = client.update_typed_link_facet(
        SchemaArn='string',
        Name='string',
        AttributeUpdates=[
            {
                'Attribute': {
                    'Name': 'string',
                    'Type': 'STRING'|'BINARY'|'BOOLEAN'|'NUMBER'|'DATETIME',
                    'DefaultValue': {
                        'StringValue': 'string',
                        'BinaryValue': b'bytes',
                        'BooleanValue': True|False,
                        'NumberValue': 'string',
                        'DatetimeValue': datetime(2015, 1, 1)
                    },
                    'IsImmutable': True|False,
                    'Rules': {
                        'string': {
                            'Type': 'BINARY_LENGTH'|'NUMBER_COMPARISON'|'STRING_FROM_SET'|'STRING_LENGTH',
                            'Parameters': {
                                'string': 'string'
                            }
                        }
                    },
                    'RequiredBehavior': 'REQUIRED_ALWAYS'|'NOT_REQUIRED'
                },
                'Action': 'CREATE_OR_UPDATE'|'DELETE'
            },
        ],
        IdentityAttributeOrder=[
            'string',
        ]
    )
    
    
    :type SchemaArn: string
    :param SchemaArn: [REQUIRED]
            The Amazon Resource Name (ARN) that is associated with the schema. For more information, see arns .
            

    :type Name: string
    :param Name: [REQUIRED]
            The unique name of the typed link facet.
            

    :type AttributeUpdates: list
    :param AttributeUpdates: [REQUIRED]
            Attributes update structure.
            (dict) --A typed link facet attribute update.
            Attribute (dict) -- [REQUIRED]The attribute to update.
            Name (string) -- [REQUIRED]The unique name of the typed link attribute.
            Type (string) -- [REQUIRED]The type of the attribute.
            DefaultValue (dict) --The default value of the attribute (if configured).
            StringValue (string) --A string data value.
            BinaryValue (bytes) --A binary data value.
            BooleanValue (boolean) --A Boolean data value.
            NumberValue (string) --A number data value.
            DatetimeValue (datetime) --A date and time value.
            IsImmutable (boolean) --Whether the attribute is mutable or not.
            Rules (dict) --Validation rules that are attached to the attribute definition.
            (string) --
            (dict) --Contains an Amazon Resource Name (ARN) and parameters that are associated with the rule.
            Type (string) --The type of attribute validation rule.
            Parameters (dict) --The minimum and maximum parameters that are associated with the rule.
            (string) --
            (string) --
            
            
            RequiredBehavior (string) -- [REQUIRED]The required behavior of the TypedLinkAttributeDefinition .
            Action (string) -- [REQUIRED]The action to perform when updating the attribute.
            
            

    :type IdentityAttributeOrder: list
    :param IdentityAttributeOrder: [REQUIRED]
            A range filter that you provide for multiple attributes. The ability to filter typed links considers the order that the attributes are defined on the typed link facet. When providing ranges to a typed link selection, any inexact ranges must be specified at the end. Any attributes that do not have a range specified are presumed to match the entire range. Filters are interpreted in the order of the attributes on the typed link facet, not the order in which they are supplied to any API calls.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

