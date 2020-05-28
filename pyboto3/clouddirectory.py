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
    Adds a new  Facet to an object. An object can have more than one facet applied on it.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param DirectoryArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that is associated with the Directory where the object resides. For more information, see arns .\n

    :type SchemaFacet: dict
    :param SchemaFacet: [REQUIRED]\nIdentifiers for the facet that you are adding to the object. See SchemaFacet for details.\n\nSchemaArn (string) --The ARN of the schema that contains the facet with no minor component. See arns and In-Place Schema Upgrade for a description of when to provide minor versions.\n\nFacetName (string) --The name of the facet.\n\n\n

    :type ObjectAttributeList: list
    :param ObjectAttributeList: Attributes on the facet that you are adding to the object.\n\n(dict) --The combination of an attribute key and an attribute value.\n\nKey (dict) -- [REQUIRED]The key of the attribute.\n\nSchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.\n\nFacetName (string) -- [REQUIRED]The name of the facet that the attribute exists within.\n\nName (string) -- [REQUIRED]The name of the attribute.\n\n\n\nValue (dict) -- [REQUIRED]The value of the attribute.\n\nStringValue (string) --A string data value.\n\nBinaryValue (bytes) --A binary data value.\n\nBooleanValue (boolean) --A Boolean data value.\n\nNumberValue (string) --A number data value.\n\nDatetimeValue (datetime) --A date and time value.\n\n\n\n\n\n\n

    :type ObjectReference: dict
    :param ObjectReference: [REQUIRED]\nA reference to the object you are adding the specified facet to.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.DirectoryNotEnabledException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.FacetValidationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def apply_schema(PublishedSchemaArn=None, DirectoryArn=None):
    """
    Copies the input published schema, at the specified version, into the  Directory with the same name and version as that of the published schema.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.apply_schema(
        PublishedSchemaArn='string',
        DirectoryArn='string'
    )
    
    
    :type PublishedSchemaArn: string
    :param PublishedSchemaArn: [REQUIRED]\nPublished schema Amazon Resource Name (ARN) that needs to be copied. For more information, see arns .\n

    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that is associated with the Directory into which the schema is copied. For more information, see arns .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AppliedSchemaArn': 'string',
    'DirectoryArn': 'string'
}


Response Structure

(dict) --

AppliedSchemaArn (string) --
The applied schema ARN that is associated with the copied schema in the  Directory . You can use this ARN to describe the schema information applied on this directory. For more information, see  arns .

DirectoryArn (string) --
The ARN that is associated with the  Directory . For more information, see  arns .







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.SchemaAlreadyExistsException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.InvalidAttachmentException


    :return: {
        'AppliedSchemaArn': 'string',
        'DirectoryArn': 'string'
    }
    
    
    :returns: 
    CloudDirectory.Client.exceptions.InternalServiceException
    CloudDirectory.Client.exceptions.InvalidArnException
    CloudDirectory.Client.exceptions.RetryableConflictException
    CloudDirectory.Client.exceptions.ValidationException
    CloudDirectory.Client.exceptions.LimitExceededException
    CloudDirectory.Client.exceptions.AccessDeniedException
    CloudDirectory.Client.exceptions.SchemaAlreadyExistsException
    CloudDirectory.Client.exceptions.ResourceNotFoundException
    CloudDirectory.Client.exceptions.InvalidAttachmentException
    
    """
    pass

def attach_object(DirectoryArn=None, ParentReference=None, ChildReference=None, LinkName=None):
    """
    Attaches an existing object to another object. An object can be accessed in two ways:
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param DirectoryArn: [REQUIRED]\nAmazon Resource Name (ARN) that is associated with the Directory where both objects reside. For more information, see arns .\n

    :type ParentReference: dict
    :param ParentReference: [REQUIRED]\nThe parent object reference.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n

    :type ChildReference: dict
    :param ChildReference: [REQUIRED]\nThe child object reference to be attached to the object.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n

    :type LinkName: string
    :param LinkName: [REQUIRED]\nThe link name with which the child object is attached to the parent.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AttachedObjectIdentifier': 'string'
}


Response Structure

(dict) --

AttachedObjectIdentifier (string) --
The attached ObjectIdentifier , which is the child ObjectIdentifier .







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.DirectoryNotEnabledException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.LinkNameAlreadyInUseException
CloudDirectory.Client.exceptions.InvalidAttachmentException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.FacetValidationException


    :return: {
        'AttachedObjectIdentifier': 'string'
    }
    
    
    :returns: 
    DirectoryArn (string) -- [REQUIRED]
    Amazon Resource Name (ARN) that is associated with the  Directory where both objects reside. For more information, see  arns .
    
    ParentReference (dict) -- [REQUIRED]
    The parent object reference.
    
    Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:
    
    $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier
    /some/path - Identifies the object based on path
    #SomeBatchReference - Identifies the object in a batch call
    
    
    
    
    ChildReference (dict) -- [REQUIRED]
    The child object reference to be attached to the object.
    
    Selector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:
    
    $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier
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
    
    Exceptions
    
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
    :param DirectoryArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that is associated with the Directory where both objects reside. For more information, see arns .\n

    :type PolicyReference: dict
    :param PolicyReference: [REQUIRED]\nThe reference that is associated with the policy object.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n

    :type ObjectReference: dict
    :param ObjectReference: [REQUIRED]\nThe reference that identifies the object to which the policy will be attached.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.DirectoryNotEnabledException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.NotPolicyException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def attach_to_index(DirectoryArn=None, IndexReference=None, TargetReference=None):
    """
    Attaches the specified object to the specified index.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param DirectoryArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the directory where the object and index exist.\n

    :type IndexReference: dict
    :param IndexReference: [REQUIRED]\nA reference to the index that you are attaching the object to.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n

    :type TargetReference: dict
    :param TargetReference: [REQUIRED]\nA reference to the object that you are attaching to the index.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AttachedObjectIdentifier': 'string'
}


Response Structure

(dict) --

AttachedObjectIdentifier (string) --
The ObjectIdentifier of the object that was attached to the index.







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.DirectoryNotEnabledException
CloudDirectory.Client.exceptions.InvalidAttachmentException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.LinkNameAlreadyInUseException
CloudDirectory.Client.exceptions.IndexedAttributeMissingException
CloudDirectory.Client.exceptions.NotIndexException


    :return: {
        'AttachedObjectIdentifier': 'string'
    }
    
    
    :returns: 
    CloudDirectory.Client.exceptions.InternalServiceException
    CloudDirectory.Client.exceptions.InvalidArnException
    CloudDirectory.Client.exceptions.RetryableConflictException
    CloudDirectory.Client.exceptions.ValidationException
    CloudDirectory.Client.exceptions.LimitExceededException
    CloudDirectory.Client.exceptions.AccessDeniedException
    CloudDirectory.Client.exceptions.DirectoryNotEnabledException
    CloudDirectory.Client.exceptions.InvalidAttachmentException
    CloudDirectory.Client.exceptions.ResourceNotFoundException
    CloudDirectory.Client.exceptions.LinkNameAlreadyInUseException
    CloudDirectory.Client.exceptions.IndexedAttributeMissingException
    CloudDirectory.Client.exceptions.NotIndexException
    
    """
    pass

def attach_typed_link(DirectoryArn=None, SourceObjectReference=None, TargetObjectReference=None, TypedLinkFacet=None, Attributes=None):
    """
    Attaches a typed link to a specified source and target object. For more information, see Typed Links .
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param DirectoryArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the directory where you want to attach the typed link.\n

    :type SourceObjectReference: dict
    :param SourceObjectReference: [REQUIRED]\nIdentifies the source object that the typed link will attach to.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n

    :type TargetObjectReference: dict
    :param TargetObjectReference: [REQUIRED]\nIdentifies the target object that the typed link will attach to.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n

    :type TypedLinkFacet: dict
    :param TypedLinkFacet: [REQUIRED]\nIdentifies the typed link facet that is associated with the typed link.\n\nSchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) that is associated with the schema. For more information, see arns .\n\nTypedLinkName (string) -- [REQUIRED]The unique name of the typed link facet.\n\n\n

    :type Attributes: list
    :param Attributes: [REQUIRED]\nA set of attributes that are associated with the typed link.\n\n(dict) --Identifies the attribute name and value for a typed link.\n\nAttributeName (string) -- [REQUIRED]The attribute name of the typed link.\n\nValue (dict) -- [REQUIRED]The value for the typed link.\n\nStringValue (string) --A string data value.\n\nBinaryValue (bytes) --A binary data value.\n\nBooleanValue (boolean) --A Boolean data value.\n\nNumberValue (string) --A number data value.\n\nDatetimeValue (datetime) --A date and time value.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

TypedLinkSpecifier (dict) --
Returns a typed link specifier as output.

TypedLinkFacet (dict) --
Identifies the typed link facet that is associated with the typed link.

SchemaArn (string) --
The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .

TypedLinkName (string) --
The unique name of the typed link facet.



SourceObjectReference (dict) --
Identifies the source object that the typed link will attach to.

Selector (string) --
A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call




TargetObjectReference (dict) --
Identifies the target object that the typed link will attach to.

Selector (string) --
A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call




IdentityAttributeValues (list) --
Identifies the attribute value to update.

(dict) --
Identifies the attribute name and value for a typed link.

AttributeName (string) --
The attribute name of the typed link.

Value (dict) --
The value for the typed link.

StringValue (string) --
A string data value.

BinaryValue (bytes) --
A binary data value.

BooleanValue (boolean) --
A Boolean data value.

NumberValue (string) --
A number data value.

DatetimeValue (datetime) --
A date and time value.















Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.DirectoryNotEnabledException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.InvalidAttachmentException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.FacetValidationException


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
    $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier
    /some/path - Identifies the object based on path
    #SomeBatchReference - Identifies the object in a batch call
    
    """
    pass

def batch_read(DirectoryArn=None, Operations=None, ConsistencyLevel=None):
    """
    Performs all the read operations in a batch.
    See also: AWS API Documentation
    
    Exceptions
    
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
                },
                'ListAttachedIndices': {
                    'TargetReference': {
                        'Selector': 'string'
                    },
                    'NextToken': 'string',
                    'MaxResults': 123
                },
                'ListObjectParentPaths': {
                    'ObjectReference': {
                        'Selector': 'string'
                    },
                    'NextToken': 'string',
                    'MaxResults': 123
                },
                'GetObjectInformation': {
                    'ObjectReference': {
                        'Selector': 'string'
                    }
                },
                'GetObjectAttributes': {
                    'ObjectReference': {
                        'Selector': 'string'
                    },
                    'SchemaFacet': {
                        'SchemaArn': 'string',
                        'FacetName': 'string'
                    },
                    'AttributeNames': [
                        'string',
                    ]
                },
                'ListObjectParents': {
                    'ObjectReference': {
                        'Selector': 'string'
                    },
                    'NextToken': 'string',
                    'MaxResults': 123
                },
                'ListObjectPolicies': {
                    'ObjectReference': {
                        'Selector': 'string'
                    },
                    'NextToken': 'string',
                    'MaxResults': 123
                },
                'ListPolicyAttachments': {
                    'PolicyReference': {
                        'Selector': 'string'
                    },
                    'NextToken': 'string',
                    'MaxResults': 123
                },
                'LookupPolicy': {
                    'ObjectReference': {
                        'Selector': 'string'
                    },
                    'NextToken': 'string',
                    'MaxResults': 123
                },
                'ListIndex': {
                    'RangesOnIndexedValues': [
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
                    'IndexReference': {
                        'Selector': 'string'
                    },
                    'MaxResults': 123,
                    'NextToken': 'string'
                },
                'ListOutgoingTypedLinks': {
                    'ObjectReference': {
                        'Selector': 'string'
                    },
                    'FilterAttributeRanges': [
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
                    'FilterTypedLink': {
                        'SchemaArn': 'string',
                        'TypedLinkName': 'string'
                    },
                    'NextToken': 'string',
                    'MaxResults': 123
                },
                'ListIncomingTypedLinks': {
                    'ObjectReference': {
                        'Selector': 'string'
                    },
                    'FilterAttributeRanges': [
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
                    'FilterTypedLink': {
                        'SchemaArn': 'string',
                        'TypedLinkName': 'string'
                    },
                    'NextToken': 'string',
                    'MaxResults': 123
                },
                'GetLinkAttributes': {
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
                    },
                    'AttributeNames': [
                        'string',
                    ]
                }
            },
        ],
        ConsistencyLevel='SERIALIZABLE'|'EVENTUAL'
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that is associated with the Directory . For more information, see arns .\n

    :type Operations: list
    :param Operations: [REQUIRED]\nA list of operations that are part of the batch.\n\n(dict) --Represents the output of a BatchRead operation.\n\nListObjectAttributes (dict) --Lists all attributes that are associated with an object.\n\nObjectReference (dict) -- [REQUIRED]Reference of the object whose attributes need to be listed.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nNextToken (string) --The pagination token.\n\nMaxResults (integer) --The maximum number of items to be retrieved in a single call. This is an approximate number.\n\nFacetFilter (dict) --Used to filter the list of object attributes that are associated with a certain facet.\n\nSchemaArn (string) --The ARN of the schema that contains the facet with no minor component. See arns and In-Place Schema Upgrade for a description of when to provide minor versions.\n\nFacetName (string) --The name of the facet.\n\n\n\n\n\nListObjectChildren (dict) --Returns a paginated list of child objects that are associated with a given object.\n\nObjectReference (dict) -- [REQUIRED]Reference of the object for which child objects are being listed.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nNextToken (string) --The pagination token.\n\nMaxResults (integer) --Maximum number of items to be retrieved in a single call. This is an approximate number.\n\n\n\nListAttachedIndices (dict) --Lists indices attached to an object.\n\nTargetReference (dict) -- [REQUIRED]A reference to the object that has indices attached.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nNextToken (string) --The pagination token.\n\nMaxResults (integer) --The maximum number of results to retrieve.\n\n\n\nListObjectParentPaths (dict) --Retrieves all available parent paths for any object type such as node, leaf node, policy node, and index node objects. For more information about objects, see Directory Structure .\n\nObjectReference (dict) -- [REQUIRED]The reference that identifies the object whose attributes will be listed.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nNextToken (string) --The pagination token.\n\nMaxResults (integer) --The maximum number of results to retrieve.\n\n\n\nGetObjectInformation (dict) --Retrieves metadata about an object.\n\nObjectReference (dict) -- [REQUIRED]A reference to the object.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\n\n\nGetObjectAttributes (dict) --Retrieves attributes within a facet that are associated with an object.\n\nObjectReference (dict) -- [REQUIRED]Reference that identifies the object whose attributes will be retrieved.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nSchemaFacet (dict) -- [REQUIRED]Identifier for the facet whose attributes will be retrieved. See SchemaFacet for details.\n\nSchemaArn (string) --The ARN of the schema that contains the facet with no minor component. See arns and In-Place Schema Upgrade for a description of when to provide minor versions.\n\nFacetName (string) --The name of the facet.\n\n\n\nAttributeNames (list) -- [REQUIRED]List of attribute names whose values will be retrieved.\n\n(string) --\n\n\n\n\nListObjectParents (dict) --\nObjectReference (dict) -- [REQUIRED]The reference that identifies an object.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nNextToken (string) --\nMaxResults (integer) --\n\n\nListObjectPolicies (dict) --Returns policies attached to an object in pagination fashion.\n\nObjectReference (dict) -- [REQUIRED]The reference that identifies the object whose attributes will be listed.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nNextToken (string) --The pagination token.\n\nMaxResults (integer) --The maximum number of results to retrieve.\n\n\n\nListPolicyAttachments (dict) --Returns all of the ObjectIdentifiers to which a given policy is attached.\n\nPolicyReference (dict) -- [REQUIRED]The reference that identifies the policy object.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nNextToken (string) --The pagination token.\n\nMaxResults (integer) --The maximum number of results to retrieve.\n\n\n\nLookupPolicy (dict) --Lists all policies from the root of the Directory to the object specified. If there are no policies present, an empty list is returned. If policies are present, and if some objects don\'t have the policies attached, it returns the ObjectIdentifier for such objects. If policies are present, it returns ObjectIdentifier , policyId , and policyType . Paths that don\'t lead to the root from the target object are ignored. For more information, see Policies .\n\nObjectReference (dict) -- [REQUIRED]Reference that identifies the object whose policies will be looked up.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nNextToken (string) --The pagination token.\n\nMaxResults (integer) --The maximum number of results to retrieve.\n\n\n\nListIndex (dict) --Lists objects attached to the specified index.\n\nRangesOnIndexedValues (list) --Specifies the ranges of indexed values that you want to query.\n\n(dict) --A range of attributes.\n\nAttributeKey (dict) --The key of the attribute that the attribute range covers.\n\nSchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.\n\nFacetName (string) -- [REQUIRED]The name of the facet that the attribute exists within.\n\nName (string) -- [REQUIRED]The name of the attribute.\n\n\n\nRange (dict) --The range of attribute values being selected.\n\nStartMode (string) -- [REQUIRED]The inclusive or exclusive range start.\n\nStartValue (dict) --The value to start the range at.\n\nStringValue (string) --A string data value.\n\nBinaryValue (bytes) --A binary data value.\n\nBooleanValue (boolean) --A Boolean data value.\n\nNumberValue (string) --A number data value.\n\nDatetimeValue (datetime) --A date and time value.\n\n\n\nEndMode (string) -- [REQUIRED]The inclusive or exclusive range end.\n\nEndValue (dict) --The attribute value to terminate the range at.\n\nStringValue (string) --A string data value.\n\nBinaryValue (bytes) --A binary data value.\n\nBooleanValue (boolean) --A Boolean data value.\n\nNumberValue (string) --A number data value.\n\nDatetimeValue (datetime) --A date and time value.\n\n\n\n\n\n\n\n\n\nIndexReference (dict) -- [REQUIRED]The reference to the index to list.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nMaxResults (integer) --The maximum number of results to retrieve.\n\nNextToken (string) --The pagination token.\n\n\n\nListOutgoingTypedLinks (dict) --Returns a paginated list of all the outgoing TypedLinkSpecifier information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see Typed Links .\n\nObjectReference (dict) -- [REQUIRED]The reference that identifies the object whose attributes will be listed.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nFilterAttributeRanges (list) --Provides range filters for multiple attributes. When providing ranges to typed link selection, any inexact ranges must be specified at the end. Any attributes that do not have a range specified are presumed to match the entire range.\n\n(dict) --Identifies the range of attributes that are used by a specified filter.\n\nAttributeName (string) --The unique name of the typed link attribute.\n\nRange (dict) -- [REQUIRED]The range of attribute values that are being selected.\n\nStartMode (string) -- [REQUIRED]The inclusive or exclusive range start.\n\nStartValue (dict) --The value to start the range at.\n\nStringValue (string) --A string data value.\n\nBinaryValue (bytes) --A binary data value.\n\nBooleanValue (boolean) --A Boolean data value.\n\nNumberValue (string) --A number data value.\n\nDatetimeValue (datetime) --A date and time value.\n\n\n\nEndMode (string) -- [REQUIRED]The inclusive or exclusive range end.\n\nEndValue (dict) --The attribute value to terminate the range at.\n\nStringValue (string) --A string data value.\n\nBinaryValue (bytes) --A binary data value.\n\nBooleanValue (boolean) --A Boolean data value.\n\nNumberValue (string) --A number data value.\n\nDatetimeValue (datetime) --A date and time value.\n\n\n\n\n\n\n\n\n\nFilterTypedLink (dict) --Filters are interpreted in the order of the attributes defined on the typed link facet, not the order they are supplied to any API calls.\n\nSchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) that is associated with the schema. For more information, see arns .\n\nTypedLinkName (string) -- [REQUIRED]The unique name of the typed link facet.\n\n\n\nNextToken (string) --The pagination token.\n\nMaxResults (integer) --The maximum number of results to retrieve.\n\n\n\nListIncomingTypedLinks (dict) --Returns a paginated list of all the incoming TypedLinkSpecifier information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see Typed Links .\n\nObjectReference (dict) -- [REQUIRED]The reference that identifies the object whose attributes will be listed.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nFilterAttributeRanges (list) --Provides range filters for multiple attributes. When providing ranges to typed link selection, any inexact ranges must be specified at the end. Any attributes that do not have a range specified are presumed to match the entire range.\n\n(dict) --Identifies the range of attributes that are used by a specified filter.\n\nAttributeName (string) --The unique name of the typed link attribute.\n\nRange (dict) -- [REQUIRED]The range of attribute values that are being selected.\n\nStartMode (string) -- [REQUIRED]The inclusive or exclusive range start.\n\nStartValue (dict) --The value to start the range at.\n\nStringValue (string) --A string data value.\n\nBinaryValue (bytes) --A binary data value.\n\nBooleanValue (boolean) --A Boolean data value.\n\nNumberValue (string) --A number data value.\n\nDatetimeValue (datetime) --A date and time value.\n\n\n\nEndMode (string) -- [REQUIRED]The inclusive or exclusive range end.\n\nEndValue (dict) --The attribute value to terminate the range at.\n\nStringValue (string) --A string data value.\n\nBinaryValue (bytes) --A binary data value.\n\nBooleanValue (boolean) --A Boolean data value.\n\nNumberValue (string) --A number data value.\n\nDatetimeValue (datetime) --A date and time value.\n\n\n\n\n\n\n\n\n\nFilterTypedLink (dict) --Filters are interpreted in the order of the attributes on the typed link facet, not the order in which they are supplied to any API calls.\n\nSchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) that is associated with the schema. For more information, see arns .\n\nTypedLinkName (string) -- [REQUIRED]The unique name of the typed link facet.\n\n\n\nNextToken (string) --The pagination token.\n\nMaxResults (integer) --The maximum number of results to retrieve.\n\n\n\nGetLinkAttributes (dict) --Retrieves attributes that are associated with a typed link.\n\nTypedLinkSpecifier (dict) -- [REQUIRED]Allows a typed link specifier to be accepted as input.\n\nTypedLinkFacet (dict) -- [REQUIRED]Identifies the typed link facet that is associated with the typed link.\n\nSchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) that is associated with the schema. For more information, see arns .\n\nTypedLinkName (string) -- [REQUIRED]The unique name of the typed link facet.\n\n\n\nSourceObjectReference (dict) -- [REQUIRED]Identifies the source object that the typed link will attach to.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nTargetObjectReference (dict) -- [REQUIRED]Identifies the target object that the typed link will attach to.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nIdentityAttributeValues (list) -- [REQUIRED]Identifies the attribute value to update.\n\n(dict) --Identifies the attribute name and value for a typed link.\n\nAttributeName (string) -- [REQUIRED]The attribute name of the typed link.\n\nValue (dict) -- [REQUIRED]The value for the typed link.\n\nStringValue (string) --A string data value.\n\nBinaryValue (bytes) --A binary data value.\n\nBooleanValue (boolean) --A Boolean data value.\n\nNumberValue (string) --A number data value.\n\nDatetimeValue (datetime) --A date and time value.\n\n\n\n\n\n\n\n\n\nAttributeNames (list) -- [REQUIRED]A list of attribute names whose values will be retrieved.\n\n(string) --\n\n\n\n\n\n\n\n

    :type ConsistencyLevel: string
    :param ConsistencyLevel: Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.

    :rtype: dict

ReturnsResponse Syntax
{
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
                },
                'GetObjectInformation': {
                    'SchemaFacets': [
                        {
                            'SchemaArn': 'string',
                            'FacetName': 'string'
                        },
                    ],
                    'ObjectIdentifier': 'string'
                },
                'GetObjectAttributes': {
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
                    ]
                },
                'ListAttachedIndices': {
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
                },
                'ListObjectParentPaths': {
                    'PathToObjectIdentifiersList': [
                        {
                            'Path': 'string',
                            'ObjectIdentifiers': [
                                'string',
                            ]
                        },
                    ],
                    'NextToken': 'string'
                },
                'ListObjectPolicies': {
                    'AttachedPolicyIds': [
                        'string',
                    ],
                    'NextToken': 'string'
                },
                'ListPolicyAttachments': {
                    'ObjectIdentifiers': [
                        'string',
                    ],
                    'NextToken': 'string'
                },
                'LookupPolicy': {
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
                },
                'ListIndex': {
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
                },
                'ListOutgoingTypedLinks': {
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
                },
                'ListIncomingTypedLinks': {
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
                },
                'GetLinkAttributes': {
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
                    ]
                },
                'ListObjectParents': {
                    'ParentLinks': [
                        {
                            'ObjectIdentifier': 'string',
                            'LinkName': 'string'
                        },
                    ],
                    'NextToken': 'string'
                }
            },
            'ExceptionResponse': {
                'Type': 'ValidationException'|'InvalidArnException'|'ResourceNotFoundException'|'InvalidNextTokenException'|'AccessDeniedException'|'NotNodeException'|'FacetValidationException'|'CannotListParentOfRootException'|'NotIndexException'|'NotPolicyException'|'DirectoryNotEnabledException'|'LimitExceededException'|'InternalServiceException',
                'Message': 'string'
            }
        },
    ]
}


Response Structure

(dict) --

Responses (list) --
A list of all the responses for each batch read.

(dict) --
Represents the output of a BatchRead response operation.

SuccessfulResponse (dict) --
Identifies which operation in a batch has succeeded.

ListObjectAttributes (dict) --
Lists all attributes that are associated with an object.

Attributes (list) --
The attributes map that is associated with the object. AttributeArn is the key; attribute value is the value.

(dict) --
The combination of an attribute key and an attribute value.

Key (dict) --
The key of the attribute.

SchemaArn (string) --
The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

FacetName (string) --
The name of the facet that the attribute exists within.

Name (string) --
The name of the attribute.



Value (dict) --
The value of the attribute.

StringValue (string) --
A string data value.

BinaryValue (bytes) --
A binary data value.

BooleanValue (boolean) --
A Boolean data value.

NumberValue (string) --
A number data value.

DatetimeValue (datetime) --
A date and time value.







NextToken (string) --
The pagination token.



ListObjectChildren (dict) --
Returns a paginated list of child objects that are associated with a given object.

Children (dict) --
The children structure, which is a map with the key as the LinkName and ObjectIdentifier as the value.

(string) --
(string) --




NextToken (string) --
The pagination token.



GetObjectInformation (dict) --
Retrieves metadata about an object.

SchemaFacets (list) --
The facets attached to the specified object.

(dict) --
A facet.

SchemaArn (string) --
The ARN of the schema that contains the facet with no minor component. See  arns and In-Place Schema Upgrade for a description of when to provide minor versions.

FacetName (string) --
The name of the facet.





ObjectIdentifier (string) --
The ObjectIdentifier of the specified object.



GetObjectAttributes (dict) --
Retrieves attributes within a facet that are associated with an object.

Attributes (list) --
The attribute values that are associated with an object.

(dict) --
The combination of an attribute key and an attribute value.

Key (dict) --
The key of the attribute.

SchemaArn (string) --
The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

FacetName (string) --
The name of the facet that the attribute exists within.

Name (string) --
The name of the attribute.



Value (dict) --
The value of the attribute.

StringValue (string) --
A string data value.

BinaryValue (bytes) --
A binary data value.

BooleanValue (boolean) --
A Boolean data value.

NumberValue (string) --
A number data value.

DatetimeValue (datetime) --
A date and time value.









ListAttachedIndices (dict) --
Lists indices attached to an object.

IndexAttachments (list) --
The indices attached to the specified object.

(dict) --
Represents an index and an attached object.

IndexedAttributes (list) --
The indexed attribute values.

(dict) --
The combination of an attribute key and an attribute value.

Key (dict) --
The key of the attribute.

SchemaArn (string) --
The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

FacetName (string) --
The name of the facet that the attribute exists within.

Name (string) --
The name of the attribute.



Value (dict) --
The value of the attribute.

StringValue (string) --
A string data value.

BinaryValue (bytes) --
A binary data value.

BooleanValue (boolean) --
A Boolean data value.

NumberValue (string) --
A number data value.

DatetimeValue (datetime) --
A date and time value.







ObjectIdentifier (string) --
In response to  ListIndex , the ObjectIdentifier of the object attached to the index. In response to  ListAttachedIndices , the ObjectIdentifier of the index attached to the object. This field will always contain the ObjectIdentifier of the object on the opposite side of the attachment specified in the query.





NextToken (string) --
The pagination token.



ListObjectParentPaths (dict) --
Retrieves all available parent paths for any object type such as node, leaf node, policy node, and index node objects. For more information about objects, see Directory Structure .

PathToObjectIdentifiersList (list) --
Returns the path to the ObjectIdentifiers that are associated with the directory.

(dict) --
Returns the path to the ObjectIdentifiers that is associated with the directory.

Path (string) --
The path that is used to identify the object starting from directory root.

ObjectIdentifiers (list) --
Lists ObjectIdentifiers starting from directory root to the object in the request.

(string) --






NextToken (string) --
The pagination token.



ListObjectPolicies (dict) --
Returns policies attached to an object in pagination fashion.

AttachedPolicyIds (list) --
A list of policy ObjectIdentifiers , that are attached to the object.

(string) --


NextToken (string) --
The pagination token.



ListPolicyAttachments (dict) --
Returns all of the ObjectIdentifiers to which a given policy is attached.

ObjectIdentifiers (list) --
A list of ObjectIdentifiers to which the policy is attached.

(string) --


NextToken (string) --
The pagination token.



LookupPolicy (dict) --
Lists all policies from the root of the  Directory to the object specified. If there are no policies present, an empty list is returned. If policies are present, and if some objects don\'t have the policies attached, it returns the ObjectIdentifier for such objects. If policies are present, it returns ObjectIdentifier , policyId , and policyType . Paths that don\'t lead to the root from the target object are ignored. For more information, see Policies .

PolicyToPathList (list) --
Provides list of path to policies. Policies contain PolicyId , ObjectIdentifier , and PolicyType . For more information, see Policies .

(dict) --
Used when a regular object exists in a  Directory and you want to find all of the policies that are associated with that object and the parent to that object.

Path (string) --
The path that is referenced from the root.

Policies (list) --
List of policy objects.

(dict) --
Contains the PolicyType , PolicyId , and the ObjectIdentifier to which it is attached. For more information, see Policies .

PolicyId (string) --
The ID of PolicyAttachment .

ObjectIdentifier (string) --
The ObjectIdentifier that is associated with PolicyAttachment .

PolicyType (string) --
The type of policy that can be associated with PolicyAttachment .









NextToken (string) --
The pagination token.



ListIndex (dict) --
Lists objects attached to the specified index.

IndexAttachments (list) --
The objects and indexed values attached to the index.

(dict) --
Represents an index and an attached object.

IndexedAttributes (list) --
The indexed attribute values.

(dict) --
The combination of an attribute key and an attribute value.

Key (dict) --
The key of the attribute.

SchemaArn (string) --
The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

FacetName (string) --
The name of the facet that the attribute exists within.

Name (string) --
The name of the attribute.



Value (dict) --
The value of the attribute.

StringValue (string) --
A string data value.

BinaryValue (bytes) --
A binary data value.

BooleanValue (boolean) --
A Boolean data value.

NumberValue (string) --
A number data value.

DatetimeValue (datetime) --
A date and time value.







ObjectIdentifier (string) --
In response to  ListIndex , the ObjectIdentifier of the object attached to the index. In response to  ListAttachedIndices , the ObjectIdentifier of the index attached to the object. This field will always contain the ObjectIdentifier of the object on the opposite side of the attachment specified in the query.





NextToken (string) --
The pagination token.



ListOutgoingTypedLinks (dict) --
Returns a paginated list of all the outgoing  TypedLinkSpecifier information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see Typed Links .

TypedLinkSpecifiers (list) --
Returns a typed link specifier as output.

(dict) --
Contains all the information that is used to uniquely identify a typed link. The parameters discussed in this topic are used to uniquely specify the typed link being operated on. The  AttachTypedLink API returns a typed link specifier while the  DetachTypedLink API accepts one as input. Similarly, the  ListIncomingTypedLinks and  ListOutgoingTypedLinks API operations provide typed link specifiers as output. You can also construct a typed link specifier from scratch.

TypedLinkFacet (dict) --
Identifies the typed link facet that is associated with the typed link.

SchemaArn (string) --
The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .

TypedLinkName (string) --
The unique name of the typed link facet.



SourceObjectReference (dict) --
Identifies the source object that the typed link will attach to.

Selector (string) --
A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call




TargetObjectReference (dict) --
Identifies the target object that the typed link will attach to.

Selector (string) --
A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call




IdentityAttributeValues (list) --
Identifies the attribute value to update.

(dict) --
Identifies the attribute name and value for a typed link.

AttributeName (string) --
The attribute name of the typed link.

Value (dict) --
The value for the typed link.

StringValue (string) --
A string data value.

BinaryValue (bytes) --
A binary data value.

BooleanValue (boolean) --
A Boolean data value.

NumberValue (string) --
A number data value.

DatetimeValue (datetime) --
A date and time value.











NextToken (string) --
The pagination token.



ListIncomingTypedLinks (dict) --
Returns a paginated list of all the incoming  TypedLinkSpecifier information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see Typed Links .

LinkSpecifiers (list) --
Returns one or more typed link specifiers as output.

(dict) --
Contains all the information that is used to uniquely identify a typed link. The parameters discussed in this topic are used to uniquely specify the typed link being operated on. The  AttachTypedLink API returns a typed link specifier while the  DetachTypedLink API accepts one as input. Similarly, the  ListIncomingTypedLinks and  ListOutgoingTypedLinks API operations provide typed link specifiers as output. You can also construct a typed link specifier from scratch.

TypedLinkFacet (dict) --
Identifies the typed link facet that is associated with the typed link.

SchemaArn (string) --
The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .

TypedLinkName (string) --
The unique name of the typed link facet.



SourceObjectReference (dict) --
Identifies the source object that the typed link will attach to.

Selector (string) --
A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call




TargetObjectReference (dict) --
Identifies the target object that the typed link will attach to.

Selector (string) --
A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call




IdentityAttributeValues (list) --
Identifies the attribute value to update.

(dict) --
Identifies the attribute name and value for a typed link.

AttributeName (string) --
The attribute name of the typed link.

Value (dict) --
The value for the typed link.

StringValue (string) --
A string data value.

BinaryValue (bytes) --
A binary data value.

BooleanValue (boolean) --
A Boolean data value.

NumberValue (string) --
A number data value.

DatetimeValue (datetime) --
A date and time value.











NextToken (string) --
The pagination token.



GetLinkAttributes (dict) --
The list of attributes to retrieve from the typed link.

Attributes (list) --
The attributes that are associated with the typed link.

(dict) --
The combination of an attribute key and an attribute value.

Key (dict) --
The key of the attribute.

SchemaArn (string) --
The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

FacetName (string) --
The name of the facet that the attribute exists within.

Name (string) --
The name of the attribute.



Value (dict) --
The value of the attribute.

StringValue (string) --
A string data value.

BinaryValue (bytes) --
A binary data value.

BooleanValue (boolean) --
A Boolean data value.

NumberValue (string) --
A number data value.

DatetimeValue (datetime) --
A date and time value.









ListObjectParents (dict) --

ParentLinks (list) --

(dict) --
A pair of ObjectIdentifier and LinkName.

ObjectIdentifier (string) --
The ID that is associated with the object.

LinkName (string) --
The name of the link between the parent and the child object.





NextToken (string) --





ExceptionResponse (dict) --
Identifies which operation in a batch has failed.

Type (string) --
A type of exception, such as InvalidArnException .

Message (string) --
An exception message that is associated with the failure.













Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.DirectoryNotEnabledException


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
                    },
                    'GetObjectInformation': {
                        'SchemaFacets': [
                            {
                                'SchemaArn': 'string',
                                'FacetName': 'string'
                            },
                        ],
                        'ObjectIdentifier': 'string'
                    },
                    'GetObjectAttributes': {
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
                        ]
                    },
                    'ListAttachedIndices': {
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
                    },
                    'ListObjectParentPaths': {
                        'PathToObjectIdentifiersList': [
                            {
                                'Path': 'string',
                                'ObjectIdentifiers': [
                                    'string',
                                ]
                            },
                        ],
                        'NextToken': 'string'
                    },
                    'ListObjectPolicies': {
                        'AttachedPolicyIds': [
                            'string',
                        ],
                        'NextToken': 'string'
                    },
                    'ListPolicyAttachments': {
                        'ObjectIdentifiers': [
                            'string',
                        ],
                        'NextToken': 'string'
                    },
                    'LookupPolicy': {
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
                    },
                    'ListIndex': {
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
                    },
                    'ListOutgoingTypedLinks': {
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
                    },
                    'ListIncomingTypedLinks': {
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
                    },
                    'GetLinkAttributes': {
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
                        ]
                    },
                    'ListObjectParents': {
                        'ParentLinks': [
                            {
                                'ObjectIdentifier': 'string',
                                'LinkName': 'string'
                            },
                        ],
                        'NextToken': 'string'
                    }
                },
                'ExceptionResponse': {
                    'Type': 'ValidationException'|'InvalidArnException'|'ResourceNotFoundException'|'InvalidNextTokenException'|'AccessDeniedException'|'NotNodeException'|'FacetValidationException'|'CannotListParentOfRootException'|'NotIndexException'|'NotPolicyException'|'DirectoryNotEnabledException'|'LimitExceededException'|'InternalServiceException',
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
    Performs all the write operations in a batch. Either all the operations succeed or none.
    See also: AWS API Documentation
    
    Exceptions
    
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
                },
                'AttachPolicy': {
                    'PolicyReference': {
                        'Selector': 'string'
                    },
                    'ObjectReference': {
                        'Selector': 'string'
                    }
                },
                'DetachPolicy': {
                    'PolicyReference': {
                        'Selector': 'string'
                    },
                    'ObjectReference': {
                        'Selector': 'string'
                    }
                },
                'CreateIndex': {
                    'OrderedIndexedAttributeList': [
                        {
                            'SchemaArn': 'string',
                            'FacetName': 'string',
                            'Name': 'string'
                        },
                    ],
                    'IsUnique': True|False,
                    'ParentReference': {
                        'Selector': 'string'
                    },
                    'LinkName': 'string',
                    'BatchReferenceName': 'string'
                },
                'AttachToIndex': {
                    'IndexReference': {
                        'Selector': 'string'
                    },
                    'TargetReference': {
                        'Selector': 'string'
                    }
                },
                'DetachFromIndex': {
                    'IndexReference': {
                        'Selector': 'string'
                    },
                    'TargetReference': {
                        'Selector': 'string'
                    }
                },
                'AttachTypedLink': {
                    'SourceObjectReference': {
                        'Selector': 'string'
                    },
                    'TargetObjectReference': {
                        'Selector': 'string'
                    },
                    'TypedLinkFacet': {
                        'SchemaArn': 'string',
                        'TypedLinkName': 'string'
                    },
                    'Attributes': [
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
                'DetachTypedLink': {
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
                },
                'UpdateLinkAttributes': {
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
                    },
                    'AttributeUpdates': [
                        {
                            'AttributeKey': {
                                'SchemaArn': 'string',
                                'FacetName': 'string',
                                'Name': 'string'
                            },
                            'AttributeAction': {
                                'AttributeActionType': 'CREATE_OR_UPDATE'|'DELETE',
                                'AttributeUpdateValue': {
                                    'StringValue': 'string',
                                    'BinaryValue': b'bytes',
                                    'BooleanValue': True|False,
                                    'NumberValue': 'string',
                                    'DatetimeValue': datetime(2015, 1, 1)
                                }
                            }
                        },
                    ]
                }
            },
        ]
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that is associated with the Directory . For more information, see arns .\n

    :type Operations: list
    :param Operations: [REQUIRED]\nA list of operations that are part of the batch.\n\n(dict) --Represents the output of a BatchWrite operation.\n\nCreateObject (dict) --Creates an object.\n\nSchemaFacet (list) -- [REQUIRED]A list of FacetArns that will be associated with the object. For more information, see arns .\n\n(dict) --A facet.\n\nSchemaArn (string) --The ARN of the schema that contains the facet with no minor component. See arns and In-Place Schema Upgrade for a description of when to provide minor versions.\n\nFacetName (string) --The name of the facet.\n\n\n\n\n\nObjectAttributeList (list) -- [REQUIRED]An attribute map, which contains an attribute ARN as the key and attribute value as the map value.\n\n(dict) --The combination of an attribute key and an attribute value.\n\nKey (dict) -- [REQUIRED]The key of the attribute.\n\nSchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.\n\nFacetName (string) -- [REQUIRED]The name of the facet that the attribute exists within.\n\nName (string) -- [REQUIRED]The name of the attribute.\n\n\n\nValue (dict) -- [REQUIRED]The value of the attribute.\n\nStringValue (string) --A string data value.\n\nBinaryValue (bytes) --A binary data value.\n\nBooleanValue (boolean) --A Boolean data value.\n\nNumberValue (string) --A number data value.\n\nDatetimeValue (datetime) --A date and time value.\n\n\n\n\n\n\n\nParentReference (dict) --If specified, the parent reference to which this object will be attached.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nLinkName (string) --The name of the link.\n\nBatchReferenceName (string) --The batch reference name. See Transaction Support for more information.\n\n\n\nAttachObject (dict) --Attaches an object to a Directory .\n\nParentReference (dict) -- [REQUIRED]The parent object reference.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nChildReference (dict) -- [REQUIRED]The child object reference that is to be attached to the object.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nLinkName (string) -- [REQUIRED]The name of the link.\n\n\n\nDetachObject (dict) --Detaches an object from a Directory .\n\nParentReference (dict) -- [REQUIRED]Parent reference from which the object with the specified link name is detached.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nLinkName (string) -- [REQUIRED]The name of the link.\n\nBatchReferenceName (string) --The batch reference name. See Transaction Support for more information.\n\n\n\nUpdateObjectAttributes (dict) --Updates a given object\'s attributes.\n\nObjectReference (dict) -- [REQUIRED]Reference that identifies the object.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nAttributeUpdates (list) -- [REQUIRED]Attributes update structure.\n\n(dict) --Structure that contains attribute update information.\n\nObjectAttributeKey (dict) --The key of the attribute being updated.\n\nSchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.\n\nFacetName (string) -- [REQUIRED]The name of the facet that the attribute exists within.\n\nName (string) -- [REQUIRED]The name of the attribute.\n\n\n\nObjectAttributeAction (dict) --The action to perform as part of the attribute update.\n\nObjectAttributeActionType (string) --A type that can be either Update or Delete .\n\nObjectAttributeUpdateValue (dict) --The value that you want to update to.\n\nStringValue (string) --A string data value.\n\nBinaryValue (bytes) --A binary data value.\n\nBooleanValue (boolean) --A Boolean data value.\n\nNumberValue (string) --A number data value.\n\nDatetimeValue (datetime) --A date and time value.\n\n\n\n\n\n\n\n\n\n\n\nDeleteObject (dict) --Deletes an object in a Directory .\n\nObjectReference (dict) -- [REQUIRED]The reference that identifies the object.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\n\n\nAddFacetToObject (dict) --A batch operation that adds a facet to an object.\n\nSchemaFacet (dict) -- [REQUIRED]Represents the facet being added to the object.\n\nSchemaArn (string) --The ARN of the schema that contains the facet with no minor component. See arns and In-Place Schema Upgrade for a description of when to provide minor versions.\n\nFacetName (string) --The name of the facet.\n\n\n\nObjectAttributeList (list) -- [REQUIRED]The attributes to set on the object.\n\n(dict) --The combination of an attribute key and an attribute value.\n\nKey (dict) -- [REQUIRED]The key of the attribute.\n\nSchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.\n\nFacetName (string) -- [REQUIRED]The name of the facet that the attribute exists within.\n\nName (string) -- [REQUIRED]The name of the attribute.\n\n\n\nValue (dict) -- [REQUIRED]The value of the attribute.\n\nStringValue (string) --A string data value.\n\nBinaryValue (bytes) --A binary data value.\n\nBooleanValue (boolean) --A Boolean data value.\n\nNumberValue (string) --A number data value.\n\nDatetimeValue (datetime) --A date and time value.\n\n\n\n\n\n\n\nObjectReference (dict) -- [REQUIRED]A reference to the object being mutated.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\n\n\nRemoveFacetFromObject (dict) --A batch operation that removes a facet from an object.\n\nSchemaFacet (dict) -- [REQUIRED]The facet to remove from the object.\n\nSchemaArn (string) --The ARN of the schema that contains the facet with no minor component. See arns and In-Place Schema Upgrade for a description of when to provide minor versions.\n\nFacetName (string) --The name of the facet.\n\n\n\nObjectReference (dict) -- [REQUIRED]A reference to the object whose facet will be removed.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\n\n\nAttachPolicy (dict) --Attaches a policy object to a regular object. An object can have a limited number of attached policies.\n\nPolicyReference (dict) -- [REQUIRED]The reference that is associated with the policy object.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nObjectReference (dict) -- [REQUIRED]The reference that identifies the object to which the policy will be attached.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\n\n\nDetachPolicy (dict) --Detaches a policy from a Directory .\n\nPolicyReference (dict) -- [REQUIRED]Reference that identifies the policy object.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nObjectReference (dict) -- [REQUIRED]Reference that identifies the object whose policy object will be detached.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\n\n\nCreateIndex (dict) --Creates an index object. See Indexing and search for more information.\n\nOrderedIndexedAttributeList (list) -- [REQUIRED]Specifies the attributes that should be indexed on. Currently only a single attribute is supported.\n\n(dict) --A unique identifier for an attribute.\n\nSchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.\n\nFacetName (string) -- [REQUIRED]The name of the facet that the attribute exists within.\n\nName (string) -- [REQUIRED]The name of the attribute.\n\n\n\n\n\nIsUnique (boolean) -- [REQUIRED]Indicates whether the attribute that is being indexed has unique values or not.\n\nParentReference (dict) --A reference to the parent object that contains the index object.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nLinkName (string) --The name of the link between the parent object and the index object.\n\nBatchReferenceName (string) --The batch reference name. See Transaction Support for more information.\n\n\n\nAttachToIndex (dict) --Attaches the specified object to the specified index.\n\nIndexReference (dict) -- [REQUIRED]A reference to the index that you are attaching the object to.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nTargetReference (dict) -- [REQUIRED]A reference to the object that you are attaching to the index.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\n\n\nDetachFromIndex (dict) --Detaches the specified object from the specified index.\n\nIndexReference (dict) -- [REQUIRED]A reference to the index object.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nTargetReference (dict) -- [REQUIRED]A reference to the object being detached from the index.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\n\n\nAttachTypedLink (dict) --Attaches a typed link to a specified source and target object. For more information, see Typed Links .\n\nSourceObjectReference (dict) -- [REQUIRED]Identifies the source object that the typed link will attach to.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nTargetObjectReference (dict) -- [REQUIRED]Identifies the target object that the typed link will attach to.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nTypedLinkFacet (dict) -- [REQUIRED]Identifies the typed link facet that is associated with the typed link.\n\nSchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) that is associated with the schema. For more information, see arns .\n\nTypedLinkName (string) -- [REQUIRED]The unique name of the typed link facet.\n\n\n\nAttributes (list) -- [REQUIRED]A set of attributes that are associated with the typed link.\n\n(dict) --Identifies the attribute name and value for a typed link.\n\nAttributeName (string) -- [REQUIRED]The attribute name of the typed link.\n\nValue (dict) -- [REQUIRED]The value for the typed link.\n\nStringValue (string) --A string data value.\n\nBinaryValue (bytes) --A binary data value.\n\nBooleanValue (boolean) --A Boolean data value.\n\nNumberValue (string) --A number data value.\n\nDatetimeValue (datetime) --A date and time value.\n\n\n\n\n\n\n\n\n\nDetachTypedLink (dict) --Detaches a typed link from a specified source and target object. For more information, see Typed Links .\n\nTypedLinkSpecifier (dict) -- [REQUIRED]Used to accept a typed link specifier as input.\n\nTypedLinkFacet (dict) -- [REQUIRED]Identifies the typed link facet that is associated with the typed link.\n\nSchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) that is associated with the schema. For more information, see arns .\n\nTypedLinkName (string) -- [REQUIRED]The unique name of the typed link facet.\n\n\n\nSourceObjectReference (dict) -- [REQUIRED]Identifies the source object that the typed link will attach to.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nTargetObjectReference (dict) -- [REQUIRED]Identifies the target object that the typed link will attach to.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nIdentityAttributeValues (list) -- [REQUIRED]Identifies the attribute value to update.\n\n(dict) --Identifies the attribute name and value for a typed link.\n\nAttributeName (string) -- [REQUIRED]The attribute name of the typed link.\n\nValue (dict) -- [REQUIRED]The value for the typed link.\n\nStringValue (string) --A string data value.\n\nBinaryValue (bytes) --A binary data value.\n\nBooleanValue (boolean) --A Boolean data value.\n\nNumberValue (string) --A number data value.\n\nDatetimeValue (datetime) --A date and time value.\n\n\n\n\n\n\n\n\n\n\n\nUpdateLinkAttributes (dict) --Updates a given object\'s attributes.\n\nTypedLinkSpecifier (dict) -- [REQUIRED]Allows a typed link specifier to be accepted as input.\n\nTypedLinkFacet (dict) -- [REQUIRED]Identifies the typed link facet that is associated with the typed link.\n\nSchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) that is associated with the schema. For more information, see arns .\n\nTypedLinkName (string) -- [REQUIRED]The unique name of the typed link facet.\n\n\n\nSourceObjectReference (dict) -- [REQUIRED]Identifies the source object that the typed link will attach to.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nTargetObjectReference (dict) -- [REQUIRED]Identifies the target object that the typed link will attach to.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nIdentityAttributeValues (list) -- [REQUIRED]Identifies the attribute value to update.\n\n(dict) --Identifies the attribute name and value for a typed link.\n\nAttributeName (string) -- [REQUIRED]The attribute name of the typed link.\n\nValue (dict) -- [REQUIRED]The value for the typed link.\n\nStringValue (string) --A string data value.\n\nBinaryValue (bytes) --A binary data value.\n\nBooleanValue (boolean) --A Boolean data value.\n\nNumberValue (string) --A number data value.\n\nDatetimeValue (datetime) --A date and time value.\n\n\n\n\n\n\n\n\n\nAttributeUpdates (list) -- [REQUIRED]The attributes update structure.\n\n(dict) --Structure that contains attribute update information.\n\nAttributeKey (dict) --The key of the attribute being updated.\n\nSchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.\n\nFacetName (string) -- [REQUIRED]The name of the facet that the attribute exists within.\n\nName (string) -- [REQUIRED]The name of the attribute.\n\n\n\nAttributeAction (dict) --The action to perform as part of the attribute update.\n\nAttributeActionType (string) --A type that can be either UPDATE_OR_CREATE or DELETE .\n\nAttributeUpdateValue (dict) --The value that you want to update to.\n\nStringValue (string) --A string data value.\n\nBinaryValue (bytes) --A binary data value.\n\nBooleanValue (boolean) --A Boolean data value.\n\nNumberValue (string) --A number data value.\n\nDatetimeValue (datetime) --A date and time value.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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
            'DeleteObject': {},
            'AddFacetToObject': {},
            'RemoveFacetFromObject': {},
            'AttachPolicy': {},
            'DetachPolicy': {},
            'CreateIndex': {
                'ObjectIdentifier': 'string'
            },
            'AttachToIndex': {
                'AttachedObjectIdentifier': 'string'
            },
            'DetachFromIndex': {
                'DetachedObjectIdentifier': 'string'
            },
            'AttachTypedLink': {
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
            },
            'DetachTypedLink': {},
            'UpdateLinkAttributes': {}
        },
    ]
}


Response Structure

(dict) --

Responses (list) --
A list of all the responses for each batch write.

(dict) --
Represents the output of a BatchWrite response operation.

CreateObject (dict) --
Creates an object in a  Directory .

ObjectIdentifier (string) --
The ID that is associated with the object.



AttachObject (dict) --
Attaches an object to a  Directory .

attachedObjectIdentifier (string) --
The ObjectIdentifier of the object that has been attached.



DetachObject (dict) --
Detaches an object from a  Directory .

detachedObjectIdentifier (string) --
The ObjectIdentifier of the detached object.



UpdateObjectAttributes (dict) --
Updates a given object\xe2\x80\x99s attributes.

ObjectIdentifier (string) --
ID that is associated with the object.



DeleteObject (dict) --
Deletes an object in a  Directory .

AddFacetToObject (dict) --
The result of an add facet to object batch operation.

RemoveFacetFromObject (dict) --
The result of a batch remove facet from object operation.

AttachPolicy (dict) --
Attaches a policy object to a regular object. An object can have a limited number of attached policies.

DetachPolicy (dict) --
Detaches a policy from a  Directory .

CreateIndex (dict) --
Creates an index object. See Indexing and search for more information.

ObjectIdentifier (string) --
The ObjectIdentifier of the index created by this operation.



AttachToIndex (dict) --
Attaches the specified object to the specified index.

AttachedObjectIdentifier (string) --
The ObjectIdentifier of the object that was attached to the index.



DetachFromIndex (dict) --
Detaches the specified object from the specified index.

DetachedObjectIdentifier (string) --
The ObjectIdentifier of the object that was detached from the index.



AttachTypedLink (dict) --
Attaches a typed link to a specified source and target object. For more information, see Typed Links .

TypedLinkSpecifier (dict) --
Returns a typed link specifier as output.

TypedLinkFacet (dict) --
Identifies the typed link facet that is associated with the typed link.

SchemaArn (string) --
The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .

TypedLinkName (string) --
The unique name of the typed link facet.



SourceObjectReference (dict) --
Identifies the source object that the typed link will attach to.

Selector (string) --
A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call




TargetObjectReference (dict) --
Identifies the target object that the typed link will attach to.

Selector (string) --
A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call




IdentityAttributeValues (list) --
Identifies the attribute value to update.

(dict) --
Identifies the attribute name and value for a typed link.

AttributeName (string) --
The attribute name of the typed link.

Value (dict) --
The value for the typed link.

StringValue (string) --
A string data value.

BinaryValue (bytes) --
A binary data value.

BooleanValue (boolean) --
A Boolean data value.

NumberValue (string) --
A number data value.

DatetimeValue (datetime) --
A date and time value.











DetachTypedLink (dict) --
Detaches a typed link from a specified source and target object. For more information, see Typed Links .

UpdateLinkAttributes (dict) --
Represents the output of a BatchWrite response operation.











Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.DirectoryNotEnabledException
CloudDirectory.Client.exceptions.BatchWriteException


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
                'DeleteObject': {},
                'AddFacetToObject': {},
                'RemoveFacetFromObject': {},
                'AttachPolicy': {},
                'DetachPolicy': {},
                'CreateIndex': {
                    'ObjectIdentifier': 'string'
                },
                'AttachToIndex': {
                    'AttachedObjectIdentifier': 'string'
                },
                'DetachFromIndex': {
                    'DetachedObjectIdentifier': 'string'
                },
                'AttachTypedLink': {
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
                },
                'DetachTypedLink': {},
                'UpdateLinkAttributes': {}
            },
        ]
    }
    
    
    :returns: 
    $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier
    /some/path - Identifies the object based on path
    #SomeBatchReference - Identifies the object in a batch call
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_directory(Name=None, SchemaArn=None):
    """
    Creates a  Directory by copying the published schema into the directory. A directory cannot be created without a schema.
    You can also quickly create a directory using a managed schema, called the QuickStartSchema . For more information, see Managed Schema in the Amazon Cloud Directory Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_directory(
        Name='string',
        SchemaArn='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the Directory . Should be unique per account, per region.\n

    :type SchemaArn: string
    :param SchemaArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the published schema that will be copied into the data Directory . For more information, see arns .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DirectoryArn': 'string',
    'Name': 'string',
    'ObjectIdentifier': 'string',
    'AppliedSchemaArn': 'string'
}


Response Structure

(dict) --

DirectoryArn (string) --
The ARN that is associated with the  Directory . For more information, see  arns .

Name (string) --
The name of the  Directory .

ObjectIdentifier (string) --
The root object node of the created directory.

AppliedSchemaArn (string) --
The ARN of the published schema in the  Directory . Once a published schema is copied into the directory, it has its own ARN, which is referred to applied schema ARN. For more information, see  arns .







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.DirectoryAlreadyExistsException
CloudDirectory.Client.exceptions.ResourceNotFoundException


    :return: {
        'DirectoryArn': 'string',
        'Name': 'string',
        'ObjectIdentifier': 'string',
        'AppliedSchemaArn': 'string'
    }
    
    
    :returns: 
    CloudDirectory.Client.exceptions.InternalServiceException
    CloudDirectory.Client.exceptions.InvalidArnException
    CloudDirectory.Client.exceptions.RetryableConflictException
    CloudDirectory.Client.exceptions.ValidationException
    CloudDirectory.Client.exceptions.LimitExceededException
    CloudDirectory.Client.exceptions.AccessDeniedException
    CloudDirectory.Client.exceptions.DirectoryAlreadyExistsException
    CloudDirectory.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def create_facet(SchemaArn=None, Name=None, Attributes=None, ObjectType=None, FacetStyle=None):
    """
    Creates a new  Facet in a schema. Facet creation is allowed only in development or applied schemas.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_facet(
        SchemaArn='string',
        Name='string',
        Attributes=[
            {
                'Name': 'string',
                'AttributeDefinition': {
                    'Type': 'STRING'|'BINARY'|'BOOLEAN'|'NUMBER'|'DATETIME'|'VARIANT',
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
        ObjectType='NODE'|'LEAF_NODE'|'POLICY'|'INDEX',
        FacetStyle='STATIC'|'DYNAMIC'
    )
    
    
    :type SchemaArn: string
    :param SchemaArn: [REQUIRED]\nThe schema ARN in which the new Facet will be created. For more information, see arns .\n

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the Facet , which is unique for a given schema.\n

    :type Attributes: list
    :param Attributes: The attributes that are associated with the Facet .\n\n(dict) --An attribute that is associated with the Facet .\n\nName (string) -- [REQUIRED]The name of the facet attribute.\n\nAttributeDefinition (dict) --A facet attribute consists of either a definition or a reference. This structure contains the attribute definition. See Attribute References for more information.\n\nType (string) -- [REQUIRED]The type of the attribute.\n\nDefaultValue (dict) --The default value of the attribute (if configured).\n\nStringValue (string) --A string data value.\n\nBinaryValue (bytes) --A binary data value.\n\nBooleanValue (boolean) --A Boolean data value.\n\nNumberValue (string) --A number data value.\n\nDatetimeValue (datetime) --A date and time value.\n\n\n\nIsImmutable (boolean) --Whether the attribute is mutable or not.\n\nRules (dict) --Validation rules attached to the attribute definition.\n\n(string) --\n(dict) --Contains an Amazon Resource Name (ARN) and parameters that are associated with the rule.\n\nType (string) --The type of attribute validation rule.\n\nParameters (dict) --The minimum and maximum parameters that are associated with the rule.\n\n(string) --\n(string) --\n\n\n\n\n\n\n\n\n\n\n\n\nAttributeReference (dict) --An attribute reference that is associated with the attribute. See Attribute References for more information.\n\nTargetFacetName (string) -- [REQUIRED]The target facet name that is associated with the facet reference. See Attribute References for more information.\n\nTargetAttributeName (string) -- [REQUIRED]The target attribute name that is associated with the facet reference. See Attribute References for more information.\n\n\n\nRequiredBehavior (string) --The required behavior of the FacetAttribute .\n\n\n\n\n

    :type ObjectType: string
    :param ObjectType: Specifies whether a given object created from this facet is of type node, leaf node, policy or index.\n\nNode: Can have multiple children but one parent.\nLeaf node: Cannot have children but can have multiple parents.\nPolicy: Allows you to store a policy document and policy type. For more information, see Policies .\nIndex: Can be created with the Index API.\n\n

    :type FacetStyle: string
    :param FacetStyle: There are two different styles that you can define on any given facet, Static and Dynamic . For static facets, all attributes must be defined in the schema. For dynamic facets, attributes can be defined during data plane operations.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.FacetAlreadyExistsException
CloudDirectory.Client.exceptions.InvalidRuleException
CloudDirectory.Client.exceptions.FacetValidationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def create_index(DirectoryArn=None, OrderedIndexedAttributeList=None, IsUnique=None, ParentReference=None, LinkName=None):
    """
    Creates an index object. See Indexing and search for more information.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param DirectoryArn: [REQUIRED]\nThe ARN of the directory where the index should be created.\n

    :type OrderedIndexedAttributeList: list
    :param OrderedIndexedAttributeList: [REQUIRED]\nSpecifies the attributes that should be indexed on. Currently only a single attribute is supported.\n\n(dict) --A unique identifier for an attribute.\n\nSchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.\n\nFacetName (string) -- [REQUIRED]The name of the facet that the attribute exists within.\n\nName (string) -- [REQUIRED]The name of the attribute.\n\n\n\n\n

    :type IsUnique: boolean
    :param IsUnique: [REQUIRED]\nIndicates whether the attribute that is being indexed has unique values or not.\n

    :type ParentReference: dict
    :param ParentReference: A reference to the parent object that contains the index object.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n

    :type LinkName: string
    :param LinkName: The name of the link between the parent object and the index object.

    :rtype: dict

ReturnsResponse Syntax
{
    'ObjectIdentifier': 'string'
}


Response Structure

(dict) --

ObjectIdentifier (string) --
The ObjectIdentifier of the index created by this operation.







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.DirectoryNotEnabledException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.FacetValidationException
CloudDirectory.Client.exceptions.LinkNameAlreadyInUseException
CloudDirectory.Client.exceptions.UnsupportedIndexTypeException


    :return: {
        'ObjectIdentifier': 'string'
    }
    
    
    :returns: 
    CloudDirectory.Client.exceptions.InternalServiceException
    CloudDirectory.Client.exceptions.InvalidArnException
    CloudDirectory.Client.exceptions.RetryableConflictException
    CloudDirectory.Client.exceptions.ValidationException
    CloudDirectory.Client.exceptions.LimitExceededException
    CloudDirectory.Client.exceptions.AccessDeniedException
    CloudDirectory.Client.exceptions.DirectoryNotEnabledException
    CloudDirectory.Client.exceptions.ResourceNotFoundException
    CloudDirectory.Client.exceptions.FacetValidationException
    CloudDirectory.Client.exceptions.LinkNameAlreadyInUseException
    CloudDirectory.Client.exceptions.UnsupportedIndexTypeException
    
    """
    pass

def create_object(DirectoryArn=None, SchemaFacets=None, ObjectAttributeList=None, ParentReference=None, LinkName=None):
    """
    Creates an object in a  Directory . Additionally attaches the object to a parent, if a parent reference and LinkName is specified. An object is simply a collection of  Facet attributes. You can also use this API call to create a policy object, if the facet from which you create the object is a policy facet.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param DirectoryArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that is associated with the Directory in which the object will be created. For more information, see arns .\n

    :type SchemaFacets: list
    :param SchemaFacets: [REQUIRED]\nA list of schema facets to be associated with the object. Do not provide minor version components. See SchemaFacet for details.\n\n(dict) --A facet.\n\nSchemaArn (string) --The ARN of the schema that contains the facet with no minor component. See arns and In-Place Schema Upgrade for a description of when to provide minor versions.\n\nFacetName (string) --The name of the facet.\n\n\n\n\n

    :type ObjectAttributeList: list
    :param ObjectAttributeList: The attribute map whose attribute ARN contains the key and attribute value as the map value.\n\n(dict) --The combination of an attribute key and an attribute value.\n\nKey (dict) -- [REQUIRED]The key of the attribute.\n\nSchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.\n\nFacetName (string) -- [REQUIRED]The name of the facet that the attribute exists within.\n\nName (string) -- [REQUIRED]The name of the attribute.\n\n\n\nValue (dict) -- [REQUIRED]The value of the attribute.\n\nStringValue (string) --A string data value.\n\nBinaryValue (bytes) --A binary data value.\n\nBooleanValue (boolean) --A Boolean data value.\n\nNumberValue (string) --A number data value.\n\nDatetimeValue (datetime) --A date and time value.\n\n\n\n\n\n\n

    :type ParentReference: dict
    :param ParentReference: If specified, the parent reference to which this object will be attached.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n

    :type LinkName: string
    :param LinkName: The name of link that is used to attach this object to a parent.

    :rtype: dict

ReturnsResponse Syntax
{
    'ObjectIdentifier': 'string'
}


Response Structure

(dict) --

ObjectIdentifier (string) --
The identifier that is associated with the object.







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.DirectoryNotEnabledException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.FacetValidationException
CloudDirectory.Client.exceptions.LinkNameAlreadyInUseException
CloudDirectory.Client.exceptions.UnsupportedIndexTypeException


    :return: {
        'ObjectIdentifier': 'string'
    }
    
    
    :returns: 
    CloudDirectory.Client.exceptions.InternalServiceException
    CloudDirectory.Client.exceptions.InvalidArnException
    CloudDirectory.Client.exceptions.RetryableConflictException
    CloudDirectory.Client.exceptions.ValidationException
    CloudDirectory.Client.exceptions.LimitExceededException
    CloudDirectory.Client.exceptions.AccessDeniedException
    CloudDirectory.Client.exceptions.DirectoryNotEnabledException
    CloudDirectory.Client.exceptions.ResourceNotFoundException
    CloudDirectory.Client.exceptions.FacetValidationException
    CloudDirectory.Client.exceptions.LinkNameAlreadyInUseException
    CloudDirectory.Client.exceptions.UnsupportedIndexTypeException
    
    """
    pass

def create_schema(Name=None):
    """
    Creates a new schema in a development state. A schema can exist in three phases:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_schema(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name that is associated with the schema. This is unique to each account and in each region.\n

    :rtype: dict
ReturnsResponse Syntax{
    'SchemaArn': 'string'
}


Response Structure

(dict) --
SchemaArn (string) --The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .






Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.SchemaAlreadyExistsException
CloudDirectory.Client.exceptions.AccessDeniedException


    :return: {
        'SchemaArn': 'string'
    }
    
    
    :returns: 
    CloudDirectory.Client.exceptions.InternalServiceException
    CloudDirectory.Client.exceptions.InvalidArnException
    CloudDirectory.Client.exceptions.RetryableConflictException
    CloudDirectory.Client.exceptions.ValidationException
    CloudDirectory.Client.exceptions.LimitExceededException
    CloudDirectory.Client.exceptions.AccessDeniedException
    CloudDirectory.Client.exceptions.SchemaAlreadyExistsException
    CloudDirectory.Client.exceptions.AccessDeniedException
    
    """
    pass

def create_typed_link_facet(SchemaArn=None, Facet=None):
    """
    Creates a  TypedLinkFacet . For more information, see Typed Links .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_typed_link_facet(
        SchemaArn='string',
        Facet={
            'Name': 'string',
            'Attributes': [
                {
                    'Name': 'string',
                    'Type': 'STRING'|'BINARY'|'BOOLEAN'|'NUMBER'|'DATETIME'|'VARIANT',
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
    :param SchemaArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that is associated with the schema. For more information, see arns .\n

    :type Facet: dict
    :param Facet: [REQUIRED]\n\nFacet structure that is associated with the typed link facet.\n\nName (string) -- [REQUIRED]The unique name of the typed link facet.\n\nAttributes (list) -- [REQUIRED]A set of key-value pairs associated with the typed link. Typed link attributes are used when you have data values that are related to the link itself, and not to one of the two objects being linked. Identity attributes also serve to distinguish the link from others of the same type between the same objects.\n\n(dict) --A typed link attribute definition.\n\nName (string) -- [REQUIRED]The unique name of the typed link attribute.\n\nType (string) -- [REQUIRED]The type of the attribute.\n\nDefaultValue (dict) --The default value of the attribute (if configured).\n\nStringValue (string) --A string data value.\n\nBinaryValue (bytes) --A binary data value.\n\nBooleanValue (boolean) --A Boolean data value.\n\nNumberValue (string) --A number data value.\n\nDatetimeValue (datetime) --A date and time value.\n\n\n\nIsImmutable (boolean) --Whether the attribute is mutable or not.\n\nRules (dict) --Validation rules that are attached to the attribute definition.\n\n(string) --\n(dict) --Contains an Amazon Resource Name (ARN) and parameters that are associated with the rule.\n\nType (string) --The type of attribute validation rule.\n\nParameters (dict) --The minimum and maximum parameters that are associated with the rule.\n\n(string) --\n(string) --\n\n\n\n\n\n\n\n\n\n\nRequiredBehavior (string) -- [REQUIRED]The required behavior of the TypedLinkAttributeDefinition .\n\n\n\n\n\nIdentityAttributeOrder (list) -- [REQUIRED]The set of attributes that distinguish links made from this facet from each other, in the order of significance. Listing typed links can filter on the values of these attributes. See ListOutgoingTypedLinks and ListIncomingTypedLinks for details.\n\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.FacetAlreadyExistsException
CloudDirectory.Client.exceptions.InvalidRuleException
CloudDirectory.Client.exceptions.FacetValidationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_directory(DirectoryArn=None):
    """
    Deletes a directory. Only disabled directories can be deleted. A deleted directory cannot be undone. Exercise extreme caution when deleting directories.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_directory(
        DirectoryArn='string'
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]\nThe ARN of the directory to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'DirectoryArn': 'string'
}


Response Structure

(dict) --
DirectoryArn (string) --The ARN of the deleted directory.






Exceptions

CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.DirectoryNotDisabledException
CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.DirectoryDeletedException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.InvalidArnException


    :return: {
        'DirectoryArn': 'string'
    }
    
    
    """
    pass

def delete_facet(SchemaArn=None, Name=None):
    """
    Deletes a given  Facet . All attributes and  Rule s that are associated with the facet will be deleted. Only development schema facets are allowed deletion.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_facet(
        SchemaArn='string',
        Name='string'
    )
    
    
    :type SchemaArn: string
    :param SchemaArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that is associated with the Facet . For more information, see arns .\n

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the facet to delete.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.FacetNotFoundException
CloudDirectory.Client.exceptions.FacetInUseException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_object(DirectoryArn=None, ObjectReference=None):
    """
    Deletes an object and its associated attributes. Only objects with no children and no parents can be deleted. The maximum number of attributes that can be deleted during an object deletion is 30. For more information, see Amazon Cloud Directory Limits .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_object(
        DirectoryArn='string',
        ObjectReference={
            'Selector': 'string'
        }
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that is associated with the Directory where the object resides. For more information, see arns .\n

    :type ObjectReference: dict
    :param ObjectReference: [REQUIRED]\nA reference that identifies the object.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.DirectoryNotEnabledException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.ObjectNotDetachedException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_schema(SchemaArn=None):
    """
    Deletes a given schema. Schemas in a development and published state can only be deleted.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_schema(
        SchemaArn='string'
    )
    
    
    :type SchemaArn: string
    :param SchemaArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the development schema. For more information, see arns .\n

    :rtype: dict
ReturnsResponse Syntax{
    'SchemaArn': 'string'
}


Response Structure

(dict) --
SchemaArn (string) --The input ARN that is returned as part of the response. For more information, see  arns .






Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.StillContainsLinksException


    :return: {
        'SchemaArn': 'string'
    }
    
    
    """
    pass

def delete_typed_link_facet(SchemaArn=None, Name=None):
    """
    Deletes a  TypedLinkFacet . For more information, see Typed Links .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_typed_link_facet(
        SchemaArn='string',
        Name='string'
    )
    
    
    :type SchemaArn: string
    :param SchemaArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that is associated with the schema. For more information, see arns .\n

    :type Name: string
    :param Name: [REQUIRED]\nThe unique name of the typed link facet.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.FacetNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def detach_from_index(DirectoryArn=None, IndexReference=None, TargetReference=None):
    """
    Detaches the specified object from the specified index.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param DirectoryArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the directory the index and object exist in.\n

    :type IndexReference: dict
    :param IndexReference: [REQUIRED]\nA reference to the index object.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n

    :type TargetReference: dict
    :param TargetReference: [REQUIRED]\nA reference to the object being detached from the index.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DetachedObjectIdentifier': 'string'
}


Response Structure

(dict) --

DetachedObjectIdentifier (string) --
The ObjectIdentifier of the object that was detached from the index.







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.DirectoryNotEnabledException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.ObjectAlreadyDetachedException
CloudDirectory.Client.exceptions.NotIndexException


    :return: {
        'DetachedObjectIdentifier': 'string'
    }
    
    
    :returns: 
    CloudDirectory.Client.exceptions.InternalServiceException
    CloudDirectory.Client.exceptions.InvalidArnException
    CloudDirectory.Client.exceptions.RetryableConflictException
    CloudDirectory.Client.exceptions.ValidationException
    CloudDirectory.Client.exceptions.LimitExceededException
    CloudDirectory.Client.exceptions.AccessDeniedException
    CloudDirectory.Client.exceptions.DirectoryNotEnabledException
    CloudDirectory.Client.exceptions.ResourceNotFoundException
    CloudDirectory.Client.exceptions.ObjectAlreadyDetachedException
    CloudDirectory.Client.exceptions.NotIndexException
    
    """
    pass

def detach_object(DirectoryArn=None, ParentReference=None, LinkName=None):
    """
    Detaches a given object from the parent object. The object that is to be detached from the parent is specified by the link name.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.detach_object(
        DirectoryArn='string',
        ParentReference={
            'Selector': 'string'
        },
        LinkName='string'
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that is associated with the Directory where objects reside. For more information, see arns .\n

    :type ParentReference: dict
    :param ParentReference: [REQUIRED]\nThe parent reference from which the object with the specified link name is detached.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n

    :type LinkName: string
    :param LinkName: [REQUIRED]\nThe link name associated with the object that needs to be detached.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DetachedObjectIdentifier': 'string'
}


Response Structure

(dict) --

DetachedObjectIdentifier (string) --
The ObjectIdentifier that was detached from the object.







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.DirectoryNotEnabledException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.NotNodeException


    :return: {
        'DetachedObjectIdentifier': 'string'
    }
    
    
    :returns: 
    CloudDirectory.Client.exceptions.InternalServiceException
    CloudDirectory.Client.exceptions.InvalidArnException
    CloudDirectory.Client.exceptions.RetryableConflictException
    CloudDirectory.Client.exceptions.ValidationException
    CloudDirectory.Client.exceptions.LimitExceededException
    CloudDirectory.Client.exceptions.AccessDeniedException
    CloudDirectory.Client.exceptions.DirectoryNotEnabledException
    CloudDirectory.Client.exceptions.ResourceNotFoundException
    CloudDirectory.Client.exceptions.NotNodeException
    
    """
    pass

def detach_policy(DirectoryArn=None, PolicyReference=None, ObjectReference=None):
    """
    Detaches a policy from an object.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param DirectoryArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that is associated with the Directory where both objects reside. For more information, see arns .\n

    :type PolicyReference: dict
    :param PolicyReference: [REQUIRED]\nReference that identifies the policy object.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n

    :type ObjectReference: dict
    :param ObjectReference: [REQUIRED]\nReference that identifies the object whose policy object will be detached.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.DirectoryNotEnabledException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.NotPolicyException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def detach_typed_link(DirectoryArn=None, TypedLinkSpecifier=None):
    """
    Detaches a typed link from a specified source and target object. For more information, see Typed Links .
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param DirectoryArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the directory where you want to detach the typed link.\n

    :type TypedLinkSpecifier: dict
    :param TypedLinkSpecifier: [REQUIRED]\nUsed to accept a typed link specifier as input.\n\nTypedLinkFacet (dict) -- [REQUIRED]Identifies the typed link facet that is associated with the typed link.\n\nSchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) that is associated with the schema. For more information, see arns .\n\nTypedLinkName (string) -- [REQUIRED]The unique name of the typed link facet.\n\n\n\nSourceObjectReference (dict) -- [REQUIRED]Identifies the source object that the typed link will attach to.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nTargetObjectReference (dict) -- [REQUIRED]Identifies the target object that the typed link will attach to.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nIdentityAttributeValues (list) -- [REQUIRED]Identifies the attribute value to update.\n\n(dict) --Identifies the attribute name and value for a typed link.\n\nAttributeName (string) -- [REQUIRED]The attribute name of the typed link.\n\nValue (dict) -- [REQUIRED]The value for the typed link.\n\nStringValue (string) --A string data value.\n\nBinaryValue (bytes) --A binary data value.\n\nBooleanValue (boolean) --A Boolean data value.\n\nNumberValue (string) --A number data value.\n\nDatetimeValue (datetime) --A date and time value.\n\n\n\n\n\n\n\n\n

    :returns: 
    CloudDirectory.Client.exceptions.InternalServiceException
    CloudDirectory.Client.exceptions.InvalidArnException
    CloudDirectory.Client.exceptions.RetryableConflictException
    CloudDirectory.Client.exceptions.ValidationException
    CloudDirectory.Client.exceptions.LimitExceededException
    CloudDirectory.Client.exceptions.AccessDeniedException
    CloudDirectory.Client.exceptions.DirectoryNotEnabledException
    CloudDirectory.Client.exceptions.ResourceNotFoundException
    CloudDirectory.Client.exceptions.FacetValidationException
    
    """
    pass

def disable_directory(DirectoryArn=None):
    """
    Disables the specified directory. Disabled directories cannot be read or written to. Only enabled directories can be disabled. Disabled directories may be reenabled.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disable_directory(
        DirectoryArn='string'
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]\nThe ARN of the directory to disable.\n

    :rtype: dict
ReturnsResponse Syntax{
    'DirectoryArn': 'string'
}


Response Structure

(dict) --
DirectoryArn (string) --The ARN of the directory that has been disabled.






Exceptions

CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.DirectoryDeletedException
CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.InvalidArnException


    :return: {
        'DirectoryArn': 'string'
    }
    
    
    """
    pass

def enable_directory(DirectoryArn=None):
    """
    Enables the specified directory. Only disabled directories can be enabled. Once enabled, the directory can then be read and written to.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.enable_directory(
        DirectoryArn='string'
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]\nThe ARN of the directory to enable.\n

    :rtype: dict
ReturnsResponse Syntax{
    'DirectoryArn': 'string'
}


Response Structure

(dict) --
DirectoryArn (string) --The ARN of the enabled directory.






Exceptions

CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.DirectoryDeletedException
CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.InvalidArnException


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
    :param Params: The parameters normally passed to\nClientMethod.

    :type ExpiresIn: int
    :param ExpiresIn: The number of seconds the presigned url is valid\nfor. By default it expires in an hour (3600 seconds)

    :type HttpMethod: string
    :param HttpMethod: The http method to use on the generated url. By\ndefault, the http method is whatever is used in the method\'s model.

    """
    pass

def get_applied_schema_version(SchemaArn=None):
    """
    Returns current applied schema version ARN, including the minor version in use.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_applied_schema_version(
        SchemaArn='string'
    )
    
    
    :type SchemaArn: string
    :param SchemaArn: [REQUIRED]\nThe ARN of the applied schema.\n

    :rtype: dict
ReturnsResponse Syntax{
    'AppliedSchemaArn': 'string'
}


Response Structure

(dict) --
AppliedSchemaArn (string) --Current applied schema ARN, including the minor version in use if one was provided.






Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.ResourceNotFoundException


    :return: {
        'AppliedSchemaArn': 'string'
    }
    
    
    """
    pass

def get_directory(DirectoryArn=None):
    """
    Retrieves metadata about a directory.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_directory(
        DirectoryArn='string'
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]\nThe ARN of the directory.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Directory': {
        'Name': 'string',
        'DirectoryArn': 'string',
        'State': 'ENABLED'|'DISABLED'|'DELETED',
        'CreationDateTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
Directory (dict) --Metadata about the directory.

Name (string) --The name of the directory.

DirectoryArn (string) --The Amazon Resource Name (ARN) that is associated with the directory. For more information, see  arns .

State (string) --The state of the directory. Can be either Enabled , Disabled , or Deleted .

CreationDateTime (datetime) --The date and time when the directory was created.








Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException


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
    
    Exceptions
    
    :example: response = client.get_facet(
        SchemaArn='string',
        Name='string'
    )
    
    
    :type SchemaArn: string
    :param SchemaArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that is associated with the Facet . For more information, see arns .\n

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the facet to retrieve.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Facet': {
        'Name': 'string',
        'ObjectType': 'NODE'|'LEAF_NODE'|'POLICY'|'INDEX',
        'FacetStyle': 'STATIC'|'DYNAMIC'
    }
}


Response Structure

(dict) --

Facet (dict) --
The  Facet structure that is associated with the facet.

Name (string) --
The name of the  Facet .

ObjectType (string) --
The object type that is associated with the facet. See  CreateFacetRequest$ObjectType for more details.

FacetStyle (string) --
There are two different styles that you can define on any given facet, Static and Dynamic . For static facets, all attributes must be defined in the schema. For dynamic facets, attributes can be defined during data plane operations.









Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.FacetNotFoundException


    :return: {
        'Facet': {
            'Name': 'string',
            'ObjectType': 'NODE'|'LEAF_NODE'|'POLICY'|'INDEX',
            'FacetStyle': 'STATIC'|'DYNAMIC'
        }
    }
    
    
    :returns: 
    CloudDirectory.Client.exceptions.InternalServiceException
    CloudDirectory.Client.exceptions.InvalidArnException
    CloudDirectory.Client.exceptions.RetryableConflictException
    CloudDirectory.Client.exceptions.ValidationException
    CloudDirectory.Client.exceptions.LimitExceededException
    CloudDirectory.Client.exceptions.AccessDeniedException
    CloudDirectory.Client.exceptions.ResourceNotFoundException
    CloudDirectory.Client.exceptions.FacetNotFoundException
    
    """
    pass

def get_link_attributes(DirectoryArn=None, TypedLinkSpecifier=None, AttributeNames=None, ConsistencyLevel=None):
    """
    Retrieves attributes that are associated with a typed link.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_link_attributes(
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
        },
        AttributeNames=[
            'string',
        ],
        ConsistencyLevel='SERIALIZABLE'|'EVENTUAL'
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that is associated with the Directory where the typed link resides. For more information, see arns or Typed Links .\n

    :type TypedLinkSpecifier: dict
    :param TypedLinkSpecifier: [REQUIRED]\nAllows a typed link specifier to be accepted as input.\n\nTypedLinkFacet (dict) -- [REQUIRED]Identifies the typed link facet that is associated with the typed link.\n\nSchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) that is associated with the schema. For more information, see arns .\n\nTypedLinkName (string) -- [REQUIRED]The unique name of the typed link facet.\n\n\n\nSourceObjectReference (dict) -- [REQUIRED]Identifies the source object that the typed link will attach to.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nTargetObjectReference (dict) -- [REQUIRED]Identifies the target object that the typed link will attach to.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nIdentityAttributeValues (list) -- [REQUIRED]Identifies the attribute value to update.\n\n(dict) --Identifies the attribute name and value for a typed link.\n\nAttributeName (string) -- [REQUIRED]The attribute name of the typed link.\n\nValue (dict) -- [REQUIRED]The value for the typed link.\n\nStringValue (string) --A string data value.\n\nBinaryValue (bytes) --A binary data value.\n\nBooleanValue (boolean) --A Boolean data value.\n\nNumberValue (string) --A number data value.\n\nDatetimeValue (datetime) --A date and time value.\n\n\n\n\n\n\n\n\n

    :type AttributeNames: list
    :param AttributeNames: [REQUIRED]\nA list of attribute names whose values will be retrieved.\n\n(string) --\n\n

    :type ConsistencyLevel: string
    :param ConsistencyLevel: The consistency level at which to retrieve the attributes on a typed link.

    :rtype: dict

ReturnsResponse Syntax
{
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
    ]
}


Response Structure

(dict) --

Attributes (list) --
The attributes that are associated with the typed link.

(dict) --
The combination of an attribute key and an attribute value.

Key (dict) --
The key of the attribute.

SchemaArn (string) --
The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

FacetName (string) --
The name of the facet that the attribute exists within.

Name (string) --
The name of the attribute.



Value (dict) --
The value of the attribute.

StringValue (string) --
A string data value.

BinaryValue (bytes) --
A binary data value.

BooleanValue (boolean) --
A Boolean data value.

NumberValue (string) --
A number data value.

DatetimeValue (datetime) --
A date and time value.













Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.DirectoryNotEnabledException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.FacetValidationException


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
        ]
    }
    
    
    :returns: 
    CloudDirectory.Client.exceptions.InternalServiceException
    CloudDirectory.Client.exceptions.InvalidArnException
    CloudDirectory.Client.exceptions.RetryableConflictException
    CloudDirectory.Client.exceptions.ValidationException
    CloudDirectory.Client.exceptions.LimitExceededException
    CloudDirectory.Client.exceptions.AccessDeniedException
    CloudDirectory.Client.exceptions.DirectoryNotEnabledException
    CloudDirectory.Client.exceptions.ResourceNotFoundException
    CloudDirectory.Client.exceptions.FacetValidationException
    
    """
    pass

def get_object_attributes(DirectoryArn=None, ObjectReference=None, ConsistencyLevel=None, SchemaFacet=None, AttributeNames=None):
    """
    Retrieves attributes within a facet that are associated with an object.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_object_attributes(
        DirectoryArn='string',
        ObjectReference={
            'Selector': 'string'
        },
        ConsistencyLevel='SERIALIZABLE'|'EVENTUAL',
        SchemaFacet={
            'SchemaArn': 'string',
            'FacetName': 'string'
        },
        AttributeNames=[
            'string',
        ]
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that is associated with the Directory where the object resides.\n

    :type ObjectReference: dict
    :param ObjectReference: [REQUIRED]\nReference that identifies the object whose attributes will be retrieved.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n

    :type ConsistencyLevel: string
    :param ConsistencyLevel: The consistency level at which to retrieve the attributes on an object.

    :type SchemaFacet: dict
    :param SchemaFacet: [REQUIRED]\nIdentifier for the facet whose attributes will be retrieved. See SchemaFacet for details.\n\nSchemaArn (string) --The ARN of the schema that contains the facet with no minor component. See arns and In-Place Schema Upgrade for a description of when to provide minor versions.\n\nFacetName (string) --The name of the facet.\n\n\n

    :type AttributeNames: list
    :param AttributeNames: [REQUIRED]\nList of attribute names whose values will be retrieved.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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
    ]
}


Response Structure

(dict) --

Attributes (list) --
The attributes that are associated with the object.

(dict) --
The combination of an attribute key and an attribute value.

Key (dict) --
The key of the attribute.

SchemaArn (string) --
The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

FacetName (string) --
The name of the facet that the attribute exists within.

Name (string) --
The name of the attribute.



Value (dict) --
The value of the attribute.

StringValue (string) --
A string data value.

BinaryValue (bytes) --
A binary data value.

BooleanValue (boolean) --
A Boolean data value.

NumberValue (string) --
A number data value.

DatetimeValue (datetime) --
A date and time value.













Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.DirectoryNotEnabledException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.FacetValidationException


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
        ]
    }
    
    
    :returns: 
    CloudDirectory.Client.exceptions.InternalServiceException
    CloudDirectory.Client.exceptions.InvalidArnException
    CloudDirectory.Client.exceptions.RetryableConflictException
    CloudDirectory.Client.exceptions.ValidationException
    CloudDirectory.Client.exceptions.LimitExceededException
    CloudDirectory.Client.exceptions.AccessDeniedException
    CloudDirectory.Client.exceptions.DirectoryNotEnabledException
    CloudDirectory.Client.exceptions.ResourceNotFoundException
    CloudDirectory.Client.exceptions.FacetValidationException
    
    """
    pass

def get_object_information(DirectoryArn=None, ObjectReference=None, ConsistencyLevel=None):
    """
    Retrieves metadata about an object.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_object_information(
        DirectoryArn='string',
        ObjectReference={
            'Selector': 'string'
        },
        ConsistencyLevel='SERIALIZABLE'|'EVENTUAL'
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]\nThe ARN of the directory being retrieved.\n

    :type ObjectReference: dict
    :param ObjectReference: [REQUIRED]\nA reference to the object.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n

    :type ConsistencyLevel: string
    :param ConsistencyLevel: The consistency level at which to retrieve the object information.

    :rtype: dict

ReturnsResponse Syntax
{
    'SchemaFacets': [
        {
            'SchemaArn': 'string',
            'FacetName': 'string'
        },
    ],
    'ObjectIdentifier': 'string'
}


Response Structure

(dict) --

SchemaFacets (list) --
The facets attached to the specified object. Although the response does not include minor version information, the most recently applied minor version of each Facet is in effect. See  GetAppliedSchemaVersion for details.

(dict) --
A facet.

SchemaArn (string) --
The ARN of the schema that contains the facet with no minor component. See  arns and In-Place Schema Upgrade for a description of when to provide minor versions.

FacetName (string) --
The name of the facet.





ObjectIdentifier (string) --
The ObjectIdentifier of the specified object.







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.DirectoryNotEnabledException
CloudDirectory.Client.exceptions.ResourceNotFoundException


    :return: {
        'SchemaFacets': [
            {
                'SchemaArn': 'string',
                'FacetName': 'string'
            },
        ],
        'ObjectIdentifier': 'string'
    }
    
    
    :returns: 
    CloudDirectory.Client.exceptions.InternalServiceException
    CloudDirectory.Client.exceptions.InvalidArnException
    CloudDirectory.Client.exceptions.RetryableConflictException
    CloudDirectory.Client.exceptions.ValidationException
    CloudDirectory.Client.exceptions.LimitExceededException
    CloudDirectory.Client.exceptions.AccessDeniedException
    CloudDirectory.Client.exceptions.DirectoryNotEnabledException
    CloudDirectory.Client.exceptions.ResourceNotFoundException
    
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

def get_schema_as_json(SchemaArn=None):
    """
    Retrieves a JSON representation of the schema. See JSON Schema Format for more information.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_schema_as_json(
        SchemaArn='string'
    )
    
    
    :type SchemaArn: string
    :param SchemaArn: [REQUIRED]\nThe ARN of the schema to retrieve.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Name': 'string',
    'Document': 'string'
}


Response Structure

(dict) --
Name (string) --The name of the retrieved schema.

Document (string) --The JSON representation of the schema document.






Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.ValidationException


    :return: {
        'Name': 'string',
        'Document': 'string'
    }
    
    
    """
    pass

def get_typed_link_facet_information(SchemaArn=None, Name=None):
    """
    Returns the identity attribute order for a specific  TypedLinkFacet . For more information, see Typed Links .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_typed_link_facet_information(
        SchemaArn='string',
        Name='string'
    )
    
    
    :type SchemaArn: string
    :param SchemaArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that is associated with the schema. For more information, see arns .\n

    :type Name: string
    :param Name: [REQUIRED]\nThe unique name of the typed link facet.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'IdentityAttributeOrder': [
        'string',
    ]
}


Response Structure

(dict) --

IdentityAttributeOrder (list) --
The order of identity attributes for the facet, from most significant to least significant. The ability to filter typed links considers the order that the attributes are defined on the typed link facet. When providing ranges to typed link selection, any inexact ranges must be specified at the end. Any attributes that do not have a range specified are presumed to match the entire range. Filters are interpreted in the order of the attributes on the typed link facet, not the order in which they are supplied to any API calls. For more information about identity attributes, see Typed Links .

(string) --








Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.InvalidNextTokenException
CloudDirectory.Client.exceptions.FacetNotFoundException


    :return: {
        'IdentityAttributeOrder': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
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

def list_applied_schema_arns(DirectoryArn=None, SchemaArn=None, NextToken=None, MaxResults=None):
    """
    Lists schema major versions applied to a directory. If SchemaArn is provided, lists the minor version.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_applied_schema_arns(
        DirectoryArn='string',
        SchemaArn='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]\nThe ARN of the directory you are listing.\n

    :type SchemaArn: string
    :param SchemaArn: The response for ListAppliedSchemaArns when this parameter is used will list all minor version ARNs for a major version.

    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to retrieve.

    :rtype: dict

ReturnsResponse Syntax
{
    'SchemaArns': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

SchemaArns (list) --
The ARNs of schemas that are applied to the directory.

(string) --


NextToken (string) --
The pagination token.







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.InvalidNextTokenException


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
    Lists indices attached to the specified object.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param DirectoryArn: [REQUIRED]\nThe ARN of the directory.\n

    :type TargetReference: dict
    :param TargetReference: [REQUIRED]\nA reference to the object that has indices attached.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n

    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to retrieve.

    :type ConsistencyLevel: string
    :param ConsistencyLevel: The consistency level to use for this operation.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

IndexAttachments (list) --
The indices attached to the specified object.

(dict) --
Represents an index and an attached object.

IndexedAttributes (list) --
The indexed attribute values.

(dict) --
The combination of an attribute key and an attribute value.

Key (dict) --
The key of the attribute.

SchemaArn (string) --
The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

FacetName (string) --
The name of the facet that the attribute exists within.

Name (string) --
The name of the attribute.



Value (dict) --
The value of the attribute.

StringValue (string) --
A string data value.

BinaryValue (bytes) --
A binary data value.

BooleanValue (boolean) --
A Boolean data value.

NumberValue (string) --
A number data value.

DatetimeValue (datetime) --
A date and time value.







ObjectIdentifier (string) --
In response to  ListIndex , the ObjectIdentifier of the object attached to the index. In response to  ListAttachedIndices , the ObjectIdentifier of the index attached to the object. This field will always contain the ObjectIdentifier of the object on the opposite side of the attachment specified in the query.





NextToken (string) --
The pagination token.







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.DirectoryNotEnabledException
CloudDirectory.Client.exceptions.ResourceNotFoundException


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
    
    
    :returns: 
    CloudDirectory.Client.exceptions.InternalServiceException
    CloudDirectory.Client.exceptions.InvalidArnException
    CloudDirectory.Client.exceptions.RetryableConflictException
    CloudDirectory.Client.exceptions.ValidationException
    CloudDirectory.Client.exceptions.LimitExceededException
    CloudDirectory.Client.exceptions.AccessDeniedException
    CloudDirectory.Client.exceptions.DirectoryNotEnabledException
    CloudDirectory.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def list_development_schema_arns(NextToken=None, MaxResults=None):
    """
    Retrieves each Amazon Resource Name (ARN) of schemas in the development state.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_development_schema_arns(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to retrieve.

    :rtype: dict

ReturnsResponse Syntax
{
    'SchemaArns': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

SchemaArns (list) --
The ARNs of retrieved development schemas.

(string) --


NextToken (string) --
The pagination token.







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.InvalidNextTokenException


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
    
    Exceptions
    
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

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

Directories (list) --
Lists all directories that are associated with your account in pagination fashion.

(dict) --
Directory structure that includes the directory name and directory ARN.

Name (string) --
The name of the directory.

DirectoryArn (string) --
The Amazon Resource Name (ARN) that is associated with the directory. For more information, see  arns .

State (string) --
The state of the directory. Can be either Enabled , Disabled , or Deleted .

CreationDateTime (datetime) --
The date and time when the directory was created.





NextToken (string) --
The pagination token.







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.InvalidNextTokenException


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
    
    
    :returns: 
    CloudDirectory.Client.exceptions.InternalServiceException
    CloudDirectory.Client.exceptions.InvalidArnException
    CloudDirectory.Client.exceptions.RetryableConflictException
    CloudDirectory.Client.exceptions.ValidationException
    CloudDirectory.Client.exceptions.LimitExceededException
    CloudDirectory.Client.exceptions.AccessDeniedException
    CloudDirectory.Client.exceptions.InvalidNextTokenException
    
    """
    pass

def list_facet_attributes(SchemaArn=None, Name=None, NextToken=None, MaxResults=None):
    """
    Retrieves attributes attached to the facet.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_facet_attributes(
        SchemaArn='string',
        Name='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type SchemaArn: string
    :param SchemaArn: [REQUIRED]\nThe ARN of the schema where the facet resides.\n

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the facet whose attributes will be retrieved.\n

    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to retrieve.

    :rtype: dict

ReturnsResponse Syntax
{
    'Attributes': [
        {
            'Name': 'string',
            'AttributeDefinition': {
                'Type': 'STRING'|'BINARY'|'BOOLEAN'|'NUMBER'|'DATETIME'|'VARIANT',
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


Response Structure

(dict) --

Attributes (list) --
The attributes attached to the facet.

(dict) --
An attribute that is associated with the  Facet .

Name (string) --
The name of the facet attribute.

AttributeDefinition (dict) --
A facet attribute consists of either a definition or a reference. This structure contains the attribute definition. See Attribute References for more information.

Type (string) --
The type of the attribute.

DefaultValue (dict) --
The default value of the attribute (if configured).

StringValue (string) --
A string data value.

BinaryValue (bytes) --
A binary data value.

BooleanValue (boolean) --
A Boolean data value.

NumberValue (string) --
A number data value.

DatetimeValue (datetime) --
A date and time value.



IsImmutable (boolean) --
Whether the attribute is mutable or not.

Rules (dict) --
Validation rules attached to the attribute definition.

(string) --

(dict) --
Contains an Amazon Resource Name (ARN) and parameters that are associated with the rule.

Type (string) --
The type of attribute validation rule.

Parameters (dict) --
The minimum and maximum parameters that are associated with the rule.

(string) --
(string) --












AttributeReference (dict) --
An attribute reference that is associated with the attribute. See Attribute References for more information.

TargetFacetName (string) --
The target facet name that is associated with the facet reference. See Attribute References for more information.

TargetAttributeName (string) --
The target attribute name that is associated with the facet reference. See Attribute References for more information.



RequiredBehavior (string) --
The required behavior of the FacetAttribute .





NextToken (string) --
The pagination token.







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.FacetNotFoundException
CloudDirectory.Client.exceptions.InvalidNextTokenException


    :return: {
        'Attributes': [
            {
                'Name': 'string',
                'AttributeDefinition': {
                    'Type': 'STRING'|'BINARY'|'BOOLEAN'|'NUMBER'|'DATETIME'|'VARIANT',
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
    
    Exceptions
    
    :example: response = client.list_facet_names(
        SchemaArn='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type SchemaArn: string
    :param SchemaArn: [REQUIRED]\nThe Amazon Resource Name (ARN) to retrieve facet names from.\n

    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to retrieve.

    :rtype: dict

ReturnsResponse Syntax
{
    'FacetNames': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

FacetNames (list) --
The names of facets that exist within the schema.

(string) --


NextToken (string) --
The pagination token.







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.InvalidNextTokenException


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
    Returns a paginated list of all the incoming  TypedLinkSpecifier information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see Typed Links .
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param DirectoryArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the directory where you want to list the typed links.\n

    :type ObjectReference: dict
    :param ObjectReference: [REQUIRED]\nReference that identifies the object whose attributes will be listed.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n

    :type FilterAttributeRanges: list
    :param FilterAttributeRanges: Provides range filters for multiple attributes. When providing ranges to typed link selection, any inexact ranges must be specified at the end. Any attributes that do not have a range specified are presumed to match the entire range.\n\n(dict) --Identifies the range of attributes that are used by a specified filter.\n\nAttributeName (string) --The unique name of the typed link attribute.\n\nRange (dict) -- [REQUIRED]The range of attribute values that are being selected.\n\nStartMode (string) -- [REQUIRED]The inclusive or exclusive range start.\n\nStartValue (dict) --The value to start the range at.\n\nStringValue (string) --A string data value.\n\nBinaryValue (bytes) --A binary data value.\n\nBooleanValue (boolean) --A Boolean data value.\n\nNumberValue (string) --A number data value.\n\nDatetimeValue (datetime) --A date and time value.\n\n\n\nEndMode (string) -- [REQUIRED]The inclusive or exclusive range end.\n\nEndValue (dict) --The attribute value to terminate the range at.\n\nStringValue (string) --A string data value.\n\nBinaryValue (bytes) --A binary data value.\n\nBooleanValue (boolean) --A Boolean data value.\n\nNumberValue (string) --A number data value.\n\nDatetimeValue (datetime) --A date and time value.\n\n\n\n\n\n\n\n\n

    :type FilterTypedLink: dict
    :param FilterTypedLink: Filters are interpreted in the order of the attributes on the typed link facet, not the order in which they are supplied to any API calls.\n\nSchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) that is associated with the schema. For more information, see arns .\n\nTypedLinkName (string) -- [REQUIRED]The unique name of the typed link facet.\n\n\n

    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to retrieve.

    :type ConsistencyLevel: string
    :param ConsistencyLevel: The consistency level to execute the request at.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

LinkSpecifiers (list) --
Returns one or more typed link specifiers as output.

(dict) --
Contains all the information that is used to uniquely identify a typed link. The parameters discussed in this topic are used to uniquely specify the typed link being operated on. The  AttachTypedLink API returns a typed link specifier while the  DetachTypedLink API accepts one as input. Similarly, the  ListIncomingTypedLinks and  ListOutgoingTypedLinks API operations provide typed link specifiers as output. You can also construct a typed link specifier from scratch.

TypedLinkFacet (dict) --
Identifies the typed link facet that is associated with the typed link.

SchemaArn (string) --
The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .

TypedLinkName (string) --
The unique name of the typed link facet.



SourceObjectReference (dict) --
Identifies the source object that the typed link will attach to.

Selector (string) --
A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call




TargetObjectReference (dict) --
Identifies the target object that the typed link will attach to.

Selector (string) --
A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call




IdentityAttributeValues (list) --
Identifies the attribute value to update.

(dict) --
Identifies the attribute name and value for a typed link.

AttributeName (string) --
The attribute name of the typed link.

Value (dict) --
The value for the typed link.

StringValue (string) --
A string data value.

BinaryValue (bytes) --
A binary data value.

BooleanValue (boolean) --
A Boolean data value.

NumberValue (string) --
A number data value.

DatetimeValue (datetime) --
A date and time value.











NextToken (string) --
The pagination token.







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.DirectoryNotEnabledException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.InvalidNextTokenException
CloudDirectory.Client.exceptions.FacetValidationException


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
    $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier
    /some/path - Identifies the object based on path
    #SomeBatchReference - Identifies the object in a batch call
    
    """
    pass

def list_index(DirectoryArn=None, RangesOnIndexedValues=None, IndexReference=None, MaxResults=None, NextToken=None, ConsistencyLevel=None):
    """
    Lists objects attached to the specified index.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param DirectoryArn: [REQUIRED]\nThe ARN of the directory that the index exists in.\n

    :type RangesOnIndexedValues: list
    :param RangesOnIndexedValues: Specifies the ranges of indexed values that you want to query.\n\n(dict) --A range of attributes.\n\nAttributeKey (dict) --The key of the attribute that the attribute range covers.\n\nSchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.\n\nFacetName (string) -- [REQUIRED]The name of the facet that the attribute exists within.\n\nName (string) -- [REQUIRED]The name of the attribute.\n\n\n\nRange (dict) --The range of attribute values being selected.\n\nStartMode (string) -- [REQUIRED]The inclusive or exclusive range start.\n\nStartValue (dict) --The value to start the range at.\n\nStringValue (string) --A string data value.\n\nBinaryValue (bytes) --A binary data value.\n\nBooleanValue (boolean) --A Boolean data value.\n\nNumberValue (string) --A number data value.\n\nDatetimeValue (datetime) --A date and time value.\n\n\n\nEndMode (string) -- [REQUIRED]The inclusive or exclusive range end.\n\nEndValue (dict) --The attribute value to terminate the range at.\n\nStringValue (string) --A string data value.\n\nBinaryValue (bytes) --A binary data value.\n\nBooleanValue (boolean) --A Boolean data value.\n\nNumberValue (string) --A number data value.\n\nDatetimeValue (datetime) --A date and time value.\n\n\n\n\n\n\n\n\n

    :type IndexReference: dict
    :param IndexReference: [REQUIRED]\nThe reference to the index to list.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of objects in a single page to retrieve from the index during a request. For more information, see Amazon Cloud Directory Limits .

    :type NextToken: string
    :param NextToken: The pagination token.

    :type ConsistencyLevel: string
    :param ConsistencyLevel: The consistency level to execute the request at.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

IndexAttachments (list) --
The objects and indexed values attached to the index.

(dict) --
Represents an index and an attached object.

IndexedAttributes (list) --
The indexed attribute values.

(dict) --
The combination of an attribute key and an attribute value.

Key (dict) --
The key of the attribute.

SchemaArn (string) --
The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

FacetName (string) --
The name of the facet that the attribute exists within.

Name (string) --
The name of the attribute.



Value (dict) --
The value of the attribute.

StringValue (string) --
A string data value.

BinaryValue (bytes) --
A binary data value.

BooleanValue (boolean) --
A Boolean data value.

NumberValue (string) --
A number data value.

DatetimeValue (datetime) --
A date and time value.







ObjectIdentifier (string) --
In response to  ListIndex , the ObjectIdentifier of the object attached to the index. In response to  ListAttachedIndices , the ObjectIdentifier of the index attached to the object. This field will always contain the ObjectIdentifier of the object on the opposite side of the attachment specified in the query.





NextToken (string) --
The pagination token.







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.FacetValidationException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.DirectoryNotEnabledException
CloudDirectory.Client.exceptions.InvalidNextTokenException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.NotIndexException


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
    
    
    :returns: 
    CloudDirectory.Client.exceptions.InternalServiceException
    CloudDirectory.Client.exceptions.InvalidArnException
    CloudDirectory.Client.exceptions.RetryableConflictException
    CloudDirectory.Client.exceptions.FacetValidationException
    CloudDirectory.Client.exceptions.ValidationException
    CloudDirectory.Client.exceptions.LimitExceededException
    CloudDirectory.Client.exceptions.AccessDeniedException
    CloudDirectory.Client.exceptions.DirectoryNotEnabledException
    CloudDirectory.Client.exceptions.InvalidNextTokenException
    CloudDirectory.Client.exceptions.ResourceNotFoundException
    CloudDirectory.Client.exceptions.NotIndexException
    
    """
    pass

def list_managed_schema_arns(SchemaArn=None, NextToken=None, MaxResults=None):
    """
    Lists the major version families of each managed schema. If a major version ARN is provided as SchemaArn, the minor version revisions in that family are listed instead.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_managed_schema_arns(
        SchemaArn='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type SchemaArn: string
    :param SchemaArn: The response for ListManagedSchemaArns. When this parameter is used, all minor version ARNs for a major version are listed.

    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to retrieve.

    :rtype: dict

ReturnsResponse Syntax
{
    'SchemaArns': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

SchemaArns (list) --
The ARNs for all AWS managed schemas.

(string) --


NextToken (string) --
The pagination token.







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.InvalidNextTokenException


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

def list_object_attributes(DirectoryArn=None, ObjectReference=None, NextToken=None, MaxResults=None, ConsistencyLevel=None, FacetFilter=None):
    """
    Lists all attributes that are associated with an object.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param DirectoryArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that is associated with the Directory where the object resides. For more information, see arns .\n

    :type ObjectReference: dict
    :param ObjectReference: [REQUIRED]\nThe reference that identifies the object whose attributes will be listed.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n

    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to be retrieved in a single call. This is an approximate number.

    :type ConsistencyLevel: string
    :param ConsistencyLevel: Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.

    :type FacetFilter: dict
    :param FacetFilter: Used to filter the list of object attributes that are associated with a certain facet.\n\nSchemaArn (string) --The ARN of the schema that contains the facet with no minor component. See arns and In-Place Schema Upgrade for a description of when to provide minor versions.\n\nFacetName (string) --The name of the facet.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

Attributes (list) --
Attributes map that is associated with the object. AttributeArn is the key, and attribute value is the value.

(dict) --
The combination of an attribute key and an attribute value.

Key (dict) --
The key of the attribute.

SchemaArn (string) --
The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

FacetName (string) --
The name of the facet that the attribute exists within.

Name (string) --
The name of the attribute.



Value (dict) --
The value of the attribute.

StringValue (string) --
A string data value.

BinaryValue (bytes) --
A binary data value.

BooleanValue (boolean) --
A Boolean data value.

NumberValue (string) --
A number data value.

DatetimeValue (datetime) --
A date and time value.







NextToken (string) --
The pagination token.







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.DirectoryNotEnabledException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.InvalidNextTokenException
CloudDirectory.Client.exceptions.FacetValidationException


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
    
    
    :returns: 
    CloudDirectory.Client.exceptions.InternalServiceException
    CloudDirectory.Client.exceptions.InvalidArnException
    CloudDirectory.Client.exceptions.RetryableConflictException
    CloudDirectory.Client.exceptions.ValidationException
    CloudDirectory.Client.exceptions.LimitExceededException
    CloudDirectory.Client.exceptions.AccessDeniedException
    CloudDirectory.Client.exceptions.DirectoryNotEnabledException
    CloudDirectory.Client.exceptions.ResourceNotFoundException
    CloudDirectory.Client.exceptions.InvalidNextTokenException
    CloudDirectory.Client.exceptions.FacetValidationException
    
    """
    pass

def list_object_children(DirectoryArn=None, ObjectReference=None, NextToken=None, MaxResults=None, ConsistencyLevel=None):
    """
    Returns a paginated list of child objects that are associated with a given object.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param DirectoryArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that is associated with the Directory where the object resides. For more information, see arns .\n

    :type ObjectReference: dict
    :param ObjectReference: [REQUIRED]\nThe reference that identifies the object for which child objects are being listed.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n

    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to be retrieved in a single call. This is an approximate number.

    :type ConsistencyLevel: string
    :param ConsistencyLevel: Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.

    :rtype: dict

ReturnsResponse Syntax
{
    'Children': {
        'string': 'string'
    },
    'NextToken': 'string'
}


Response Structure

(dict) --

Children (dict) --
Children structure, which is a map with key as the LinkName and ObjectIdentifier as the value.

(string) --
(string) --




NextToken (string) --
The pagination token.







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.DirectoryNotEnabledException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.InvalidNextTokenException
CloudDirectory.Client.exceptions.NotNodeException


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
    
    Exceptions
    
    :example: response = client.list_object_parent_paths(
        DirectoryArn='string',
        ObjectReference={
            'Selector': 'string'
        },
        NextToken='string',
        MaxResults=123
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]\nThe ARN of the directory to which the parent path applies.\n

    :type ObjectReference: dict
    :param ObjectReference: [REQUIRED]\nThe reference that identifies the object whose parent paths are listed.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n

    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to be retrieved in a single call. This is an approximate number.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

PathToObjectIdentifiersList (list) --
Returns the path to the ObjectIdentifiers that are associated with the directory.

(dict) --
Returns the path to the ObjectIdentifiers that is associated with the directory.

Path (string) --
The path that is used to identify the object starting from directory root.

ObjectIdentifiers (list) --
Lists ObjectIdentifiers starting from directory root to the object in the request.

(string) --






NextToken (string) --
The pagination token.







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.DirectoryNotEnabledException
CloudDirectory.Client.exceptions.InvalidNextTokenException
CloudDirectory.Client.exceptions.ResourceNotFoundException


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

def list_object_parents(DirectoryArn=None, ObjectReference=None, NextToken=None, MaxResults=None, ConsistencyLevel=None, IncludeAllLinksToEachParent=None):
    """
    Lists parent objects that are associated with a given object in pagination fashion.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_object_parents(
        DirectoryArn='string',
        ObjectReference={
            'Selector': 'string'
        },
        NextToken='string',
        MaxResults=123,
        ConsistencyLevel='SERIALIZABLE'|'EVENTUAL',
        IncludeAllLinksToEachParent=True|False
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that is associated with the Directory where the object resides. For more information, see arns .\n

    :type ObjectReference: dict
    :param ObjectReference: [REQUIRED]\nThe reference that identifies the object for which parent objects are being listed.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n

    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to be retrieved in a single call. This is an approximate number.

    :type ConsistencyLevel: string
    :param ConsistencyLevel: Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.

    :type IncludeAllLinksToEachParent: boolean
    :param IncludeAllLinksToEachParent: When set to True, returns all ListObjectParentsResponse$ParentLinks . There could be multiple links between a parent-child pair.

    :rtype: dict

ReturnsResponse Syntax
{
    'Parents': {
        'string': 'string'
    },
    'NextToken': 'string',
    'ParentLinks': [
        {
            'ObjectIdentifier': 'string',
            'LinkName': 'string'
        },
    ]
}


Response Structure

(dict) --

Parents (dict) --
The parent structure, which is a map with key as the ObjectIdentifier and LinkName as the value.

(string) --
(string) --




NextToken (string) --
The pagination token.

ParentLinks (list) --
Returns a list of parent reference and LinkName Tuples.

(dict) --
A pair of ObjectIdentifier and LinkName.

ObjectIdentifier (string) --
The ID that is associated with the object.

LinkName (string) --
The name of the link between the parent and the child object.











Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.DirectoryNotEnabledException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.InvalidNextTokenException
CloudDirectory.Client.exceptions.CannotListParentOfRootException


    :return: {
        'Parents': {
            'string': 'string'
        },
        'NextToken': 'string',
        'ParentLinks': [
            {
                'ObjectIdentifier': 'string',
                'LinkName': 'string'
            },
        ]
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
    
    Exceptions
    
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
    :param DirectoryArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that is associated with the Directory where objects reside. For more information, see arns .\n

    :type ObjectReference: dict
    :param ObjectReference: [REQUIRED]\nReference that identifies the object for which policies will be listed.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n

    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to be retrieved in a single call. This is an approximate number.

    :type ConsistencyLevel: string
    :param ConsistencyLevel: Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.

    :rtype: dict

ReturnsResponse Syntax
{
    'AttachedPolicyIds': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

AttachedPolicyIds (list) --
A list of policy ObjectIdentifiers , that are attached to the object.

(string) --


NextToken (string) --
The pagination token.







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.DirectoryNotEnabledException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.InvalidNextTokenException


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
    Returns a paginated list of all the outgoing  TypedLinkSpecifier information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see Typed Links .
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param DirectoryArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the directory where you want to list the typed links.\n

    :type ObjectReference: dict
    :param ObjectReference: [REQUIRED]\nA reference that identifies the object whose attributes will be listed.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n

    :type FilterAttributeRanges: list
    :param FilterAttributeRanges: Provides range filters for multiple attributes. When providing ranges to typed link selection, any inexact ranges must be specified at the end. Any attributes that do not have a range specified are presumed to match the entire range.\n\n(dict) --Identifies the range of attributes that are used by a specified filter.\n\nAttributeName (string) --The unique name of the typed link attribute.\n\nRange (dict) -- [REQUIRED]The range of attribute values that are being selected.\n\nStartMode (string) -- [REQUIRED]The inclusive or exclusive range start.\n\nStartValue (dict) --The value to start the range at.\n\nStringValue (string) --A string data value.\n\nBinaryValue (bytes) --A binary data value.\n\nBooleanValue (boolean) --A Boolean data value.\n\nNumberValue (string) --A number data value.\n\nDatetimeValue (datetime) --A date and time value.\n\n\n\nEndMode (string) -- [REQUIRED]The inclusive or exclusive range end.\n\nEndValue (dict) --The attribute value to terminate the range at.\n\nStringValue (string) --A string data value.\n\nBinaryValue (bytes) --A binary data value.\n\nBooleanValue (boolean) --A Boolean data value.\n\nNumberValue (string) --A number data value.\n\nDatetimeValue (datetime) --A date and time value.\n\n\n\n\n\n\n\n\n

    :type FilterTypedLink: dict
    :param FilterTypedLink: Filters are interpreted in the order of the attributes defined on the typed link facet, not the order they are supplied to any API calls.\n\nSchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) that is associated with the schema. For more information, see arns .\n\nTypedLinkName (string) -- [REQUIRED]The unique name of the typed link facet.\n\n\n

    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to retrieve.

    :type ConsistencyLevel: string
    :param ConsistencyLevel: The consistency level to execute the request at.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

TypedLinkSpecifiers (list) --
Returns a typed link specifier as output.

(dict) --
Contains all the information that is used to uniquely identify a typed link. The parameters discussed in this topic are used to uniquely specify the typed link being operated on. The  AttachTypedLink API returns a typed link specifier while the  DetachTypedLink API accepts one as input. Similarly, the  ListIncomingTypedLinks and  ListOutgoingTypedLinks API operations provide typed link specifiers as output. You can also construct a typed link specifier from scratch.

TypedLinkFacet (dict) --
Identifies the typed link facet that is associated with the typed link.

SchemaArn (string) --
The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .

TypedLinkName (string) --
The unique name of the typed link facet.



SourceObjectReference (dict) --
Identifies the source object that the typed link will attach to.

Selector (string) --
A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call




TargetObjectReference (dict) --
Identifies the target object that the typed link will attach to.

Selector (string) --
A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call




IdentityAttributeValues (list) --
Identifies the attribute value to update.

(dict) --
Identifies the attribute name and value for a typed link.

AttributeName (string) --
The attribute name of the typed link.

Value (dict) --
The value for the typed link.

StringValue (string) --
A string data value.

BinaryValue (bytes) --
A binary data value.

BooleanValue (boolean) --
A Boolean data value.

NumberValue (string) --
A number data value.

DatetimeValue (datetime) --
A date and time value.











NextToken (string) --
The pagination token.







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.DirectoryNotEnabledException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.InvalidNextTokenException
CloudDirectory.Client.exceptions.FacetValidationException


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
    $ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier
    /some/path - Identifies the object based on path
    #SomeBatchReference - Identifies the object in a batch call
    
    """
    pass

def list_policy_attachments(DirectoryArn=None, PolicyReference=None, NextToken=None, MaxResults=None, ConsistencyLevel=None):
    """
    Returns all of the ObjectIdentifiers to which a given policy is attached.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param DirectoryArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that is associated with the Directory where objects reside. For more information, see arns .\n

    :type PolicyReference: dict
    :param PolicyReference: [REQUIRED]\nThe reference that identifies the policy object.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n

    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to be retrieved in a single call. This is an approximate number.

    :type ConsistencyLevel: string
    :param ConsistencyLevel: Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.

    :rtype: dict

ReturnsResponse Syntax
{
    'ObjectIdentifiers': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ObjectIdentifiers (list) --
A list of ObjectIdentifiers to which the policy is attached.

(string) --


NextToken (string) --
The pagination token.







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.DirectoryNotEnabledException
CloudDirectory.Client.exceptions.InvalidNextTokenException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.NotPolicyException


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

def list_published_schema_arns(SchemaArn=None, NextToken=None, MaxResults=None):
    """
    Lists the major version families of each published schema. If a major version ARN is provided as SchemaArn , the minor version revisions in that family are listed instead.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_published_schema_arns(
        SchemaArn='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type SchemaArn: string
    :param SchemaArn: The response for ListPublishedSchemaArns when this parameter is used will list all minor version ARNs for a major version.

    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to retrieve.

    :rtype: dict

ReturnsResponse Syntax
{
    'SchemaArns': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

SchemaArns (list) --
The ARNs of published schemas.

(string) --


NextToken (string) --
The pagination token.







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.InvalidNextTokenException


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
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource. Tagging is only supported for directories.\n

    :type NextToken: string
    :param NextToken: The pagination token. This is for future use. Currently pagination is not supported for tagging.

    :type MaxResults: integer
    :param MaxResults: The MaxResults parameter sets the maximum number of results returned in a single page. This is for future use and is not supported currently.

    :rtype: dict

ReturnsResponse Syntax
{
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Tags (list) --
A list of tag key value pairs that are associated with the response.

(dict) --
The tag structure that contains a tag key and value.

Key (string) --
The key that is associated with the tag.

Value (string) --
The value that is associated with the tag.





NextToken (string) --
The token to use to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.InvalidTaggingRequestException


    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CloudDirectory.Client.exceptions.InternalServiceException
    CloudDirectory.Client.exceptions.InvalidArnException
    CloudDirectory.Client.exceptions.RetryableConflictException
    CloudDirectory.Client.exceptions.ValidationException
    CloudDirectory.Client.exceptions.LimitExceededException
    CloudDirectory.Client.exceptions.AccessDeniedException
    CloudDirectory.Client.exceptions.ResourceNotFoundException
    CloudDirectory.Client.exceptions.InvalidTaggingRequestException
    
    """
    pass

def list_typed_link_facet_attributes(SchemaArn=None, Name=None, NextToken=None, MaxResults=None):
    """
    Returns a paginated list of all attribute definitions for a particular  TypedLinkFacet . For more information, see Typed Links .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_typed_link_facet_attributes(
        SchemaArn='string',
        Name='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type SchemaArn: string
    :param SchemaArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that is associated with the schema. For more information, see arns .\n

    :type Name: string
    :param Name: [REQUIRED]\nThe unique name of the typed link facet.\n

    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to retrieve.

    :rtype: dict

ReturnsResponse Syntax
{
    'Attributes': [
        {
            'Name': 'string',
            'Type': 'STRING'|'BINARY'|'BOOLEAN'|'NUMBER'|'DATETIME'|'VARIANT',
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


Response Structure

(dict) --

Attributes (list) --
An ordered set of attributes associate with the typed link.

(dict) --
A typed link attribute definition.

Name (string) --
The unique name of the typed link attribute.

Type (string) --
The type of the attribute.

DefaultValue (dict) --
The default value of the attribute (if configured).

StringValue (string) --
A string data value.

BinaryValue (bytes) --
A binary data value.

BooleanValue (boolean) --
A Boolean data value.

NumberValue (string) --
A number data value.

DatetimeValue (datetime) --
A date and time value.



IsImmutable (boolean) --
Whether the attribute is mutable or not.

Rules (dict) --
Validation rules that are attached to the attribute definition.

(string) --

(dict) --
Contains an Amazon Resource Name (ARN) and parameters that are associated with the rule.

Type (string) --
The type of attribute validation rule.

Parameters (dict) --
The minimum and maximum parameters that are associated with the rule.

(string) --
(string) --










RequiredBehavior (string) --
The required behavior of the TypedLinkAttributeDefinition .





NextToken (string) --
The pagination token.







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.FacetNotFoundException
CloudDirectory.Client.exceptions.InvalidNextTokenException


    :return: {
        'Attributes': [
            {
                'Name': 'string',
                'Type': 'STRING'|'BINARY'|'BOOLEAN'|'NUMBER'|'DATETIME'|'VARIANT',
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
    Returns a paginated list of TypedLink facet names for a particular schema. For more information, see Typed Links .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_typed_link_facet_names(
        SchemaArn='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type SchemaArn: string
    :param SchemaArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that is associated with the schema. For more information, see arns .\n

    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to retrieve.

    :rtype: dict

ReturnsResponse Syntax
{
    'FacetNames': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

FacetNames (list) --
The names of typed link facets that exist within the schema.

(string) --


NextToken (string) --
The pagination token.







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.InvalidNextTokenException


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
    Lists all policies from the root of the  Directory to the object specified. If there are no policies present, an empty list is returned. If policies are present, and if some objects don\'t have the policies attached, it returns the ObjectIdentifier for such objects. If policies are present, it returns ObjectIdentifier , policyId , and policyType . Paths that don\'t lead to the root from the target object are ignored. For more information, see Policies .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.lookup_policy(
        DirectoryArn='string',
        ObjectReference={
            'Selector': 'string'
        },
        NextToken='string',
        MaxResults=123
    )
    
    
    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that is associated with the Directory . For more information, see arns .\n

    :type ObjectReference: dict
    :param ObjectReference: [REQUIRED]\nReference that identifies the object whose policies will be looked up.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n

    :type NextToken: string
    :param NextToken: The token to request the next page of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to be retrieved in a single call. This is an approximate number.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

PolicyToPathList (list) --
Provides list of path to policies. Policies contain PolicyId , ObjectIdentifier , and PolicyType . For more information, see Policies .

(dict) --
Used when a regular object exists in a  Directory and you want to find all of the policies that are associated with that object and the parent to that object.

Path (string) --
The path that is referenced from the root.

Policies (list) --
List of policy objects.

(dict) --
Contains the PolicyType , PolicyId , and the ObjectIdentifier to which it is attached. For more information, see Policies .

PolicyId (string) --
The ID of PolicyAttachment .

ObjectIdentifier (string) --
The ObjectIdentifier that is associated with PolicyAttachment .

PolicyType (string) --
The type of policy that can be associated with PolicyAttachment .









NextToken (string) --
The pagination token.







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.DirectoryNotEnabledException
CloudDirectory.Client.exceptions.InvalidNextTokenException
CloudDirectory.Client.exceptions.ResourceNotFoundException


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
    
    
    :returns: 
    CloudDirectory.Client.exceptions.InternalServiceException
    CloudDirectory.Client.exceptions.InvalidArnException
    CloudDirectory.Client.exceptions.RetryableConflictException
    CloudDirectory.Client.exceptions.ValidationException
    CloudDirectory.Client.exceptions.LimitExceededException
    CloudDirectory.Client.exceptions.AccessDeniedException
    CloudDirectory.Client.exceptions.DirectoryNotEnabledException
    CloudDirectory.Client.exceptions.InvalidNextTokenException
    CloudDirectory.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def publish_schema(DevelopmentSchemaArn=None, Version=None, MinorVersion=None, Name=None):
    """
    Publishes a development schema with a major version and a recommended minor version.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.publish_schema(
        DevelopmentSchemaArn='string',
        Version='string',
        MinorVersion='string',
        Name='string'
    )
    
    
    :type DevelopmentSchemaArn: string
    :param DevelopmentSchemaArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that is associated with the development schema. For more information, see arns .\n

    :type Version: string
    :param Version: [REQUIRED]\nThe major version under which the schema will be published. Schemas have both a major and minor version associated with them.\n

    :type MinorVersion: string
    :param MinorVersion: The minor version under which the schema will be published. This parameter is recommended. Schemas have both a major and minor version associated with them.

    :type Name: string
    :param Name: The new name under which the schema will be published. If this is not provided, the development schema is considered.

    :rtype: dict

ReturnsResponse Syntax
{
    'PublishedSchemaArn': 'string'
}


Response Structure

(dict) --

PublishedSchemaArn (string) --
The ARN that is associated with the published schema. For more information, see  arns .







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.SchemaAlreadyPublishedException


    :return: {
        'PublishedSchemaArn': 'string'
    }
    
    
    :returns: 
    CloudDirectory.Client.exceptions.InternalServiceException
    CloudDirectory.Client.exceptions.InvalidArnException
    CloudDirectory.Client.exceptions.RetryableConflictException
    CloudDirectory.Client.exceptions.ValidationException
    CloudDirectory.Client.exceptions.LimitExceededException
    CloudDirectory.Client.exceptions.AccessDeniedException
    CloudDirectory.Client.exceptions.ResourceNotFoundException
    CloudDirectory.Client.exceptions.SchemaAlreadyPublishedException
    
    """
    pass

def put_schema_from_json(SchemaArn=None, Document=None):
    """
    Allows a schema to be updated using JSON upload. Only available for development schemas. See JSON Schema Format for more information.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_schema_from_json(
        SchemaArn='string',
        Document='string'
    )
    
    
    :type SchemaArn: string
    :param SchemaArn: [REQUIRED]\nThe ARN of the schema to update.\n

    :type Document: string
    :param Document: [REQUIRED]\nThe replacement JSON schema.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string'
}


Response Structure

(dict) --

Arn (string) --
The ARN of the schema to update.







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.InvalidSchemaDocException
CloudDirectory.Client.exceptions.InvalidRuleException


    :return: {
        'Arn': 'string'
    }
    
    
    :returns: 
    CloudDirectory.Client.exceptions.InternalServiceException
    CloudDirectory.Client.exceptions.InvalidArnException
    CloudDirectory.Client.exceptions.RetryableConflictException
    CloudDirectory.Client.exceptions.ValidationException
    CloudDirectory.Client.exceptions.LimitExceededException
    CloudDirectory.Client.exceptions.AccessDeniedException
    CloudDirectory.Client.exceptions.InvalidSchemaDocException
    CloudDirectory.Client.exceptions.InvalidRuleException
    
    """
    pass

def remove_facet_from_object(DirectoryArn=None, SchemaFacet=None, ObjectReference=None):
    """
    Removes the specified facet from the specified object.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param DirectoryArn: [REQUIRED]\nThe ARN of the directory in which the object resides.\n

    :type SchemaFacet: dict
    :param SchemaFacet: [REQUIRED]\nThe facet to remove. See SchemaFacet for details.\n\nSchemaArn (string) --The ARN of the schema that contains the facet with no minor component. See arns and In-Place Schema Upgrade for a description of when to provide minor versions.\n\nFacetName (string) --The name of the facet.\n\n\n

    :type ObjectReference: dict
    :param ObjectReference: [REQUIRED]\nA reference to the object to remove the facet from.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.DirectoryNotEnabledException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.FacetValidationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def tag_resource(ResourceArn=None, Tags=None):
    """
    An API operation for adding tags to a resource.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource. Tagging is only supported for directories.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nA list of tag key-value pairs.\n\n(dict) --The tag structure that contains a tag key and value.\n\nKey (string) --The key that is associated with the tag.\n\nValue (string) --The value that is associated with the tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.InvalidTaggingRequestException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceArn=None, TagKeys=None):
    """
    An API operation for removing tags from a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource. Tagging is only supported for directories.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nKeys of the tag that need to be removed from the resource.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.InvalidTaggingRequestException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_facet(SchemaArn=None, Name=None, AttributeUpdates=None, ObjectType=None):
    """
    Does the following:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_facet(
        SchemaArn='string',
        Name='string',
        AttributeUpdates=[
            {
                'Attribute': {
                    'Name': 'string',
                    'AttributeDefinition': {
                        'Type': 'STRING'|'BINARY'|'BOOLEAN'|'NUMBER'|'DATETIME'|'VARIANT',
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
    :param SchemaArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that is associated with the Facet . For more information, see arns .\n

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the facet.\n

    :type AttributeUpdates: list
    :param AttributeUpdates: List of attributes that need to be updated in a given schema Facet . Each attribute is followed by AttributeAction , which specifies the type of update operation to perform.\n\n(dict) --A structure that contains information used to update an attribute.\n\nAttribute (dict) --The attribute to update.\n\nName (string) -- [REQUIRED]The name of the facet attribute.\n\nAttributeDefinition (dict) --A facet attribute consists of either a definition or a reference. This structure contains the attribute definition. See Attribute References for more information.\n\nType (string) -- [REQUIRED]The type of the attribute.\n\nDefaultValue (dict) --The default value of the attribute (if configured).\n\nStringValue (string) --A string data value.\n\nBinaryValue (bytes) --A binary data value.\n\nBooleanValue (boolean) --A Boolean data value.\n\nNumberValue (string) --A number data value.\n\nDatetimeValue (datetime) --A date and time value.\n\n\n\nIsImmutable (boolean) --Whether the attribute is mutable or not.\n\nRules (dict) --Validation rules attached to the attribute definition.\n\n(string) --\n(dict) --Contains an Amazon Resource Name (ARN) and parameters that are associated with the rule.\n\nType (string) --The type of attribute validation rule.\n\nParameters (dict) --The minimum and maximum parameters that are associated with the rule.\n\n(string) --\n(string) --\n\n\n\n\n\n\n\n\n\n\n\n\nAttributeReference (dict) --An attribute reference that is associated with the attribute. See Attribute References for more information.\n\nTargetFacetName (string) -- [REQUIRED]The target facet name that is associated with the facet reference. See Attribute References for more information.\n\nTargetAttributeName (string) -- [REQUIRED]The target attribute name that is associated with the facet reference. See Attribute References for more information.\n\n\n\nRequiredBehavior (string) --The required behavior of the FacetAttribute .\n\n\n\nAction (string) --The action to perform when updating the attribute.\n\n\n\n\n

    :type ObjectType: string
    :param ObjectType: The object type that is associated with the facet. See CreateFacetRequest$ObjectType for more details.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.InvalidFacetUpdateException
CloudDirectory.Client.exceptions.FacetValidationException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.FacetNotFoundException
CloudDirectory.Client.exceptions.InvalidRuleException


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

def update_link_attributes(DirectoryArn=None, TypedLinkSpecifier=None, AttributeUpdates=None):
    """
    Updates a given typed link\xe2\x80\x99s attributes. Attributes to be updated must not contribute to the typed link\xe2\x80\x99s identity, as defined by its IdentityAttributeOrder .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_link_attributes(
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
        },
        AttributeUpdates=[
            {
                'AttributeKey': {
                    'SchemaArn': 'string',
                    'FacetName': 'string',
                    'Name': 'string'
                },
                'AttributeAction': {
                    'AttributeActionType': 'CREATE_OR_UPDATE'|'DELETE',
                    'AttributeUpdateValue': {
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
    :param DirectoryArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that is associated with the Directory where the updated typed link resides. For more information, see arns or Typed Links .\n

    :type TypedLinkSpecifier: dict
    :param TypedLinkSpecifier: [REQUIRED]\nAllows a typed link specifier to be accepted as input.\n\nTypedLinkFacet (dict) -- [REQUIRED]Identifies the typed link facet that is associated with the typed link.\n\nSchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) that is associated with the schema. For more information, see arns .\n\nTypedLinkName (string) -- [REQUIRED]The unique name of the typed link facet.\n\n\n\nSourceObjectReference (dict) -- [REQUIRED]Identifies the source object that the typed link will attach to.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nTargetObjectReference (dict) -- [REQUIRED]Identifies the target object that the typed link will attach to.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n\nIdentityAttributeValues (list) -- [REQUIRED]Identifies the attribute value to update.\n\n(dict) --Identifies the attribute name and value for a typed link.\n\nAttributeName (string) -- [REQUIRED]The attribute name of the typed link.\n\nValue (dict) -- [REQUIRED]The value for the typed link.\n\nStringValue (string) --A string data value.\n\nBinaryValue (bytes) --A binary data value.\n\nBooleanValue (boolean) --A Boolean data value.\n\nNumberValue (string) --A number data value.\n\nDatetimeValue (datetime) --A date and time value.\n\n\n\n\n\n\n\n\n

    :type AttributeUpdates: list
    :param AttributeUpdates: [REQUIRED]\nThe attributes update structure.\n\n(dict) --Structure that contains attribute update information.\n\nAttributeKey (dict) --The key of the attribute being updated.\n\nSchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.\n\nFacetName (string) -- [REQUIRED]The name of the facet that the attribute exists within.\n\nName (string) -- [REQUIRED]The name of the attribute.\n\n\n\nAttributeAction (dict) --The action to perform as part of the attribute update.\n\nAttributeActionType (string) --A type that can be either UPDATE_OR_CREATE or DELETE .\n\nAttributeUpdateValue (dict) --The value that you want to update to.\n\nStringValue (string) --A string data value.\n\nBinaryValue (bytes) --A binary data value.\n\nBooleanValue (boolean) --A Boolean data value.\n\nNumberValue (string) --A number data value.\n\nDatetimeValue (datetime) --A date and time value.\n\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.DirectoryNotEnabledException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.FacetValidationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_object_attributes(DirectoryArn=None, ObjectReference=None, AttributeUpdates=None):
    """
    Updates a given object\'s attributes.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param DirectoryArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that is associated with the Directory where the object resides. For more information, see arns .\n

    :type ObjectReference: dict
    :param ObjectReference: [REQUIRED]\nThe reference that identifies the object.\n\nSelector (string) --A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:\n\n$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object\xe2\x80\x99s identifier is immutable and no two objects will ever share the same object identifier\n/some/path - Identifies the object based on path\n#SomeBatchReference - Identifies the object in a batch call\n\n\n\n

    :type AttributeUpdates: list
    :param AttributeUpdates: [REQUIRED]\nThe attributes update structure.\n\n(dict) --Structure that contains attribute update information.\n\nObjectAttributeKey (dict) --The key of the attribute being updated.\n\nSchemaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.\n\nFacetName (string) -- [REQUIRED]The name of the facet that the attribute exists within.\n\nName (string) -- [REQUIRED]The name of the attribute.\n\n\n\nObjectAttributeAction (dict) --The action to perform as part of the attribute update.\n\nObjectAttributeActionType (string) --A type that can be either Update or Delete .\n\nObjectAttributeUpdateValue (dict) --The value that you want to update to.\n\nStringValue (string) --A string data value.\n\nBinaryValue (bytes) --A binary data value.\n\nBooleanValue (boolean) --A Boolean data value.\n\nNumberValue (string) --A number data value.\n\nDatetimeValue (datetime) --A date and time value.\n\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ObjectIdentifier': 'string'
}


Response Structure

(dict) --

ObjectIdentifier (string) --
The ObjectIdentifier of the updated object.







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.DirectoryNotEnabledException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.LinkNameAlreadyInUseException
CloudDirectory.Client.exceptions.FacetValidationException


    :return: {
        'ObjectIdentifier': 'string'
    }
    
    
    :returns: 
    CloudDirectory.Client.exceptions.InternalServiceException
    CloudDirectory.Client.exceptions.InvalidArnException
    CloudDirectory.Client.exceptions.RetryableConflictException
    CloudDirectory.Client.exceptions.ValidationException
    CloudDirectory.Client.exceptions.LimitExceededException
    CloudDirectory.Client.exceptions.AccessDeniedException
    CloudDirectory.Client.exceptions.DirectoryNotEnabledException
    CloudDirectory.Client.exceptions.ResourceNotFoundException
    CloudDirectory.Client.exceptions.LinkNameAlreadyInUseException
    CloudDirectory.Client.exceptions.FacetValidationException
    
    """
    pass

def update_schema(SchemaArn=None, Name=None):
    """
    Updates the schema name with a new name. Only development schema names can be updated.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_schema(
        SchemaArn='string',
        Name='string'
    )
    
    
    :type SchemaArn: string
    :param SchemaArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the development schema. For more information, see arns .\n

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the schema.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'SchemaArn': 'string'
}


Response Structure

(dict) --

SchemaArn (string) --
The ARN that is associated with the updated schema. For more information, see  arns .







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.ResourceNotFoundException


    :return: {
        'SchemaArn': 'string'
    }
    
    
    :returns: 
    CloudDirectory.Client.exceptions.InternalServiceException
    CloudDirectory.Client.exceptions.InvalidArnException
    CloudDirectory.Client.exceptions.RetryableConflictException
    CloudDirectory.Client.exceptions.ValidationException
    CloudDirectory.Client.exceptions.LimitExceededException
    CloudDirectory.Client.exceptions.AccessDeniedException
    CloudDirectory.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def update_typed_link_facet(SchemaArn=None, Name=None, AttributeUpdates=None, IdentityAttributeOrder=None):
    """
    Updates a  TypedLinkFacet . For more information, see Typed Links .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_typed_link_facet(
        SchemaArn='string',
        Name='string',
        AttributeUpdates=[
            {
                'Attribute': {
                    'Name': 'string',
                    'Type': 'STRING'|'BINARY'|'BOOLEAN'|'NUMBER'|'DATETIME'|'VARIANT',
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
    :param SchemaArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that is associated with the schema. For more information, see arns .\n

    :type Name: string
    :param Name: [REQUIRED]\nThe unique name of the typed link facet.\n

    :type AttributeUpdates: list
    :param AttributeUpdates: [REQUIRED]\nAttributes update structure.\n\n(dict) --A typed link facet attribute update.\n\nAttribute (dict) -- [REQUIRED]The attribute to update.\n\nName (string) -- [REQUIRED]The unique name of the typed link attribute.\n\nType (string) -- [REQUIRED]The type of the attribute.\n\nDefaultValue (dict) --The default value of the attribute (if configured).\n\nStringValue (string) --A string data value.\n\nBinaryValue (bytes) --A binary data value.\n\nBooleanValue (boolean) --A Boolean data value.\n\nNumberValue (string) --A number data value.\n\nDatetimeValue (datetime) --A date and time value.\n\n\n\nIsImmutable (boolean) --Whether the attribute is mutable or not.\n\nRules (dict) --Validation rules that are attached to the attribute definition.\n\n(string) --\n(dict) --Contains an Amazon Resource Name (ARN) and parameters that are associated with the rule.\n\nType (string) --The type of attribute validation rule.\n\nParameters (dict) --The minimum and maximum parameters that are associated with the rule.\n\n(string) --\n(string) --\n\n\n\n\n\n\n\n\n\n\nRequiredBehavior (string) -- [REQUIRED]The required behavior of the TypedLinkAttributeDefinition .\n\n\n\nAction (string) -- [REQUIRED]The action to perform when updating the attribute.\n\n\n\n\n

    :type IdentityAttributeOrder: list
    :param IdentityAttributeOrder: [REQUIRED]\nThe order of identity attributes for the facet, from most significant to least significant. The ability to filter typed links considers the order that the attributes are defined on the typed link facet. When providing ranges to a typed link selection, any inexact ranges must be specified at the end. Any attributes that do not have a range specified are presumed to match the entire range. Filters are interpreted in the order of the attributes on the typed link facet, not the order in which they are supplied to any API calls. For more information about identity attributes, see Typed Links .\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.LimitExceededException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.FacetValidationException
CloudDirectory.Client.exceptions.InvalidFacetUpdateException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.FacetNotFoundException
CloudDirectory.Client.exceptions.InvalidRuleException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def upgrade_applied_schema(PublishedSchemaArn=None, DirectoryArn=None, DryRun=None):
    """
    Upgrades a single directory in-place using the PublishedSchemaArn with schema updates found in MinorVersion . Backwards-compatible minor version upgrades are instantaneously available for readers on all objects in the directory. Note: This is a synchronous API call and upgrades only one schema on a given directory per call. To upgrade multiple directories from one schema, you would need to call this API on each directory.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.upgrade_applied_schema(
        PublishedSchemaArn='string',
        DirectoryArn='string',
        DryRun=True|False
    )
    
    
    :type PublishedSchemaArn: string
    :param PublishedSchemaArn: [REQUIRED]\nThe revision of the published schema to upgrade the directory to.\n

    :type DirectoryArn: string
    :param DirectoryArn: [REQUIRED]\nThe ARN for the directory to which the upgraded schema will be applied.\n

    :type DryRun: boolean
    :param DryRun: Used for testing whether the major version schemas are backward compatible or not. If schema compatibility fails, an exception would be thrown else the call would succeed but no changes will be saved. This parameter is optional.

    :rtype: dict

ReturnsResponse Syntax
{
    'UpgradedSchemaArn': 'string',
    'DirectoryArn': 'string'
}


Response Structure

(dict) --

UpgradedSchemaArn (string) --
The ARN of the upgraded schema that is returned as part of the response.

DirectoryArn (string) --
The ARN of the directory that is returned as part of the response.







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.IncompatibleSchemaException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.InvalidAttachmentException
CloudDirectory.Client.exceptions.SchemaAlreadyExistsException


    :return: {
        'UpgradedSchemaArn': 'string',
        'DirectoryArn': 'string'
    }
    
    
    :returns: 
    CloudDirectory.Client.exceptions.InternalServiceException
    CloudDirectory.Client.exceptions.InvalidArnException
    CloudDirectory.Client.exceptions.RetryableConflictException
    CloudDirectory.Client.exceptions.ValidationException
    CloudDirectory.Client.exceptions.IncompatibleSchemaException
    CloudDirectory.Client.exceptions.AccessDeniedException
    CloudDirectory.Client.exceptions.ResourceNotFoundException
    CloudDirectory.Client.exceptions.InvalidAttachmentException
    CloudDirectory.Client.exceptions.SchemaAlreadyExistsException
    
    """
    pass

def upgrade_published_schema(DevelopmentSchemaArn=None, PublishedSchemaArn=None, MinorVersion=None, DryRun=None):
    """
    Upgrades a published schema under a new minor version revision using the current contents of DevelopmentSchemaArn .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.upgrade_published_schema(
        DevelopmentSchemaArn='string',
        PublishedSchemaArn='string',
        MinorVersion='string',
        DryRun=True|False
    )
    
    
    :type DevelopmentSchemaArn: string
    :param DevelopmentSchemaArn: [REQUIRED]\nThe ARN of the development schema with the changes used for the upgrade.\n

    :type PublishedSchemaArn: string
    :param PublishedSchemaArn: [REQUIRED]\nThe ARN of the published schema to be upgraded.\n

    :type MinorVersion: string
    :param MinorVersion: [REQUIRED]\nIdentifies the minor version of the published schema that will be created. This parameter is NOT optional.\n

    :type DryRun: boolean
    :param DryRun: Used for testing whether the Development schema provided is backwards compatible, or not, with the publish schema provided by the user to be upgraded. If schema compatibility fails, an exception would be thrown else the call would succeed. This parameter is optional and defaults to false.

    :rtype: dict

ReturnsResponse Syntax
{
    'UpgradedSchemaArn': 'string'
}


Response Structure

(dict) --

UpgradedSchemaArn (string) --
The ARN of the upgraded schema that is returned as part of the response.







Exceptions

CloudDirectory.Client.exceptions.InternalServiceException
CloudDirectory.Client.exceptions.InvalidArnException
CloudDirectory.Client.exceptions.RetryableConflictException
CloudDirectory.Client.exceptions.ValidationException
CloudDirectory.Client.exceptions.IncompatibleSchemaException
CloudDirectory.Client.exceptions.AccessDeniedException
CloudDirectory.Client.exceptions.ResourceNotFoundException
CloudDirectory.Client.exceptions.InvalidAttachmentException
CloudDirectory.Client.exceptions.LimitExceededException


    :return: {
        'UpgradedSchemaArn': 'string'
    }
    
    
    :returns: 
    CloudDirectory.Client.exceptions.InternalServiceException
    CloudDirectory.Client.exceptions.InvalidArnException
    CloudDirectory.Client.exceptions.RetryableConflictException
    CloudDirectory.Client.exceptions.ValidationException
    CloudDirectory.Client.exceptions.IncompatibleSchemaException
    CloudDirectory.Client.exceptions.AccessDeniedException
    CloudDirectory.Client.exceptions.ResourceNotFoundException
    CloudDirectory.Client.exceptions.InvalidAttachmentException
    CloudDirectory.Client.exceptions.LimitExceededException
    
    """
    pass

