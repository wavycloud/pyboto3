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

def create_discoverer(Description=None, SourceArn=None, Tags=None):
    """
    Creates a discoverer.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_discoverer(
        Description='string',
        SourceArn='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type Description: string
    :param Description: A description for the discoverer.

    :type SourceArn: string
    :param SourceArn: [REQUIRED]\nThe ARN of the event bus.\n

    :type Tags: dict
    :param Tags: Tags associated with the resource.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Description': 'string',
    'DiscovererArn': 'string',
    'DiscovererId': 'string',
    'SourceArn': 'string',
    'State': 'STARTED'|'STOPPED',
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
201 response

Description (string) --
The description of the discoverer.

DiscovererArn (string) --
The ARN of the discoverer.

DiscovererId (string) --
The ID of the discoverer.

SourceArn (string) --
The ARN of the event bus.

State (string) --
The state of the discoverer.

Tags (dict) --
Tags associated with the resource.

(string) --
(string) --










Exceptions

Schemas.Client.exceptions.BadRequestException
Schemas.Client.exceptions.InternalServerErrorException
Schemas.Client.exceptions.UnauthorizedException
Schemas.Client.exceptions.ForbiddenException
Schemas.Client.exceptions.ServiceUnavailableException
Schemas.Client.exceptions.ConflictException


    :return: {
        'Description': 'string',
        'DiscovererArn': 'string',
        'DiscovererId': 'string',
        'SourceArn': 'string',
        'State': 'STARTED'|'STOPPED',
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def create_registry(Description=None, RegistryName=None, Tags=None):
    """
    Creates a registry.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_registry(
        Description='string',
        RegistryName='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type Description: string
    :param Description: A description of the registry to be created.

    :type RegistryName: string
    :param RegistryName: [REQUIRED]\nThe name of the registry.\n

    :type Tags: dict
    :param Tags: Tags to associate with the registry.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Description': 'string',
    'RegistryArn': 'string',
    'RegistryName': 'string',
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
201 response

Description (string) --
The description of the registry.

RegistryArn (string) --
The ARN of the registry.

RegistryName (string) --
The name of the registry.

Tags (dict) --
Tags associated with the registry.

(string) --
(string) --










Exceptions

Schemas.Client.exceptions.BadRequestException
Schemas.Client.exceptions.InternalServerErrorException
Schemas.Client.exceptions.UnauthorizedException
Schemas.Client.exceptions.ForbiddenException
Schemas.Client.exceptions.ServiceUnavailableException
Schemas.Client.exceptions.ConflictException


    :return: {
        'Description': 'string',
        'RegistryArn': 'string',
        'RegistryName': 'string',
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def create_schema(Content=None, Description=None, RegistryName=None, SchemaName=None, Tags=None, Type=None):
    """
    Creates a schema definition.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_schema(
        Content='string',
        Description='string',
        RegistryName='string',
        SchemaName='string',
        Tags={
            'string': 'string'
        },
        Type='OpenApi3'
    )
    
    
    :type Content: string
    :param Content: [REQUIRED]\nThe source of the schema definition.\n

    :type Description: string
    :param Description: A description of the schema.

    :type RegistryName: string
    :param RegistryName: [REQUIRED]\nThe name of the registry.\n

    :type SchemaName: string
    :param SchemaName: [REQUIRED]\nThe name of the schema.\n

    :type Tags: dict
    :param Tags: Tags associated with the schema.\n\n(string) --\n(string) --\n\n\n\n

    :type Type: string
    :param Type: [REQUIRED]\nThe type of schema.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Description': 'string',
    'LastModified': datetime(2015, 1, 1),
    'SchemaArn': 'string',
    'SchemaName': 'string',
    'SchemaVersion': 'string',
    'Tags': {
        'string': 'string'
    },
    'Type': 'string',
    'VersionCreatedDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --
201 response

Description (string) --
The description of the schema.

LastModified (datetime) --
The date and time that schema was modified.

SchemaArn (string) --
The ARN of the schema.

SchemaName (string) --
The name of the schema.

SchemaVersion (string) --
The version number of the schema

Tags (dict) --
Key-value pairs associated with a resource.

(string) --
(string) --




Type (string) --
The type of the schema.

VersionCreatedDate (datetime) --
The date the schema version was created.







Exceptions

Schemas.Client.exceptions.ServiceUnavailableException
Schemas.Client.exceptions.BadRequestException
Schemas.Client.exceptions.InternalServerErrorException
Schemas.Client.exceptions.ForbiddenException


    :return: {
        'Description': 'string',
        'LastModified': datetime(2015, 1, 1),
        'SchemaArn': 'string',
        'SchemaName': 'string',
        'SchemaVersion': 'string',
        'Tags': {
            'string': 'string'
        },
        'Type': 'string',
        'VersionCreatedDate': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def delete_discoverer(DiscovererId=None):
    """
    Deletes a discoverer.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_discoverer(
        DiscovererId='string'
    )
    
    
    :type DiscovererId: string
    :param DiscovererId: [REQUIRED]\nThe ID of the discoverer.\n

    """
    pass

def delete_registry(RegistryName=None):
    """
    Deletes a Registry.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_registry(
        RegistryName='string'
    )
    
    
    :type RegistryName: string
    :param RegistryName: [REQUIRED]\nThe name of the registry.\n

    """
    pass

def delete_resource_policy(RegistryName=None):
    """
    Delete the resource-based policy attached to the specified registry.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_resource_policy(
        RegistryName='string'
    )
    
    
    :type RegistryName: string
    :param RegistryName: The name of the registry.

    """
    pass

def delete_schema(RegistryName=None, SchemaName=None):
    """
    Delete a schema definition.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_schema(
        RegistryName='string',
        SchemaName='string'
    )
    
    
    :type RegistryName: string
    :param RegistryName: [REQUIRED]\nThe name of the registry.\n

    :type SchemaName: string
    :param SchemaName: [REQUIRED]\nThe name of the schema.\n

    :returns: 
    Schemas.Client.exceptions.BadRequestException
    Schemas.Client.exceptions.UnauthorizedException
    Schemas.Client.exceptions.InternalServerErrorException
    Schemas.Client.exceptions.ForbiddenException
    Schemas.Client.exceptions.NotFoundException
    Schemas.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def delete_schema_version(RegistryName=None, SchemaName=None, SchemaVersion=None):
    """
    Delete the schema version definition
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_schema_version(
        RegistryName='string',
        SchemaName='string',
        SchemaVersion='string'
    )
    
    
    :type RegistryName: string
    :param RegistryName: [REQUIRED]\nThe name of the registry.\n

    :type SchemaName: string
    :param SchemaName: [REQUIRED]\nThe name of the schema.\n

    :type SchemaVersion: string
    :param SchemaVersion: [REQUIRED] The version number of the schema

    :returns: 
    Schemas.Client.exceptions.BadRequestException
    Schemas.Client.exceptions.UnauthorizedException
    Schemas.Client.exceptions.InternalServerErrorException
    Schemas.Client.exceptions.ForbiddenException
    Schemas.Client.exceptions.NotFoundException
    Schemas.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def describe_code_binding(Language=None, RegistryName=None, SchemaName=None, SchemaVersion=None):
    """
    Describe the code binding URI.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_code_binding(
        Language='string',
        RegistryName='string',
        SchemaName='string',
        SchemaVersion='string'
    )
    
    
    :type Language: string
    :param Language: [REQUIRED]\nThe language of the code binding.\n

    :type RegistryName: string
    :param RegistryName: [REQUIRED]\nThe name of the registry.\n

    :type SchemaName: string
    :param SchemaName: [REQUIRED]\nThe name of the schema.\n

    :type SchemaVersion: string
    :param SchemaVersion: Specifying this limits the results to only this schema version.

    :rtype: dict

ReturnsResponse Syntax
{
    'CreationDate': datetime(2015, 1, 1),
    'LastModified': datetime(2015, 1, 1),
    'SchemaVersion': 'string',
    'Status': 'CREATE_IN_PROGRESS'|'CREATE_COMPLETE'|'CREATE_FAILED'
}


Response Structure

(dict) --
200 response

CreationDate (datetime) --
The time and date that the code binding was created.

LastModified (datetime) --
The date and time that code bindings were modified.

SchemaVersion (string) --
The version number of the schema.

Status (string) --
The current status of code binding generation.







Exceptions

Schemas.Client.exceptions.BadRequestException
Schemas.Client.exceptions.UnauthorizedException
Schemas.Client.exceptions.InternalServerErrorException
Schemas.Client.exceptions.ForbiddenException
Schemas.Client.exceptions.NotFoundException
Schemas.Client.exceptions.TooManyRequestsException


    :return: {
        'CreationDate': datetime(2015, 1, 1),
        'LastModified': datetime(2015, 1, 1),
        'SchemaVersion': 'string',
        'Status': 'CREATE_IN_PROGRESS'|'CREATE_COMPLETE'|'CREATE_FAILED'
    }
    
    
    :returns: 
    Schemas.Client.exceptions.BadRequestException
    Schemas.Client.exceptions.UnauthorizedException
    Schemas.Client.exceptions.InternalServerErrorException
    Schemas.Client.exceptions.ForbiddenException
    Schemas.Client.exceptions.NotFoundException
    Schemas.Client.exceptions.TooManyRequestsException
    
    """
    pass

def describe_discoverer(DiscovererId=None):
    """
    Describes the discoverer.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_discoverer(
        DiscovererId='string'
    )
    
    
    :type DiscovererId: string
    :param DiscovererId: [REQUIRED]\nThe ID of the discoverer.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Description': 'string',
    'DiscovererArn': 'string',
    'DiscovererId': 'string',
    'SourceArn': 'string',
    'State': 'STARTED'|'STOPPED',
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --200 response

Description (string) --The description of the discoverer.

DiscovererArn (string) --The ARN of the discoverer.

DiscovererId (string) --The ID of the discoverer.

SourceArn (string) --The ARN of the event bus.

State (string) --The state of the discoverer.

Tags (dict) --Tags associated with the resource.

(string) --
(string) --









Exceptions

Schemas.Client.exceptions.BadRequestException
Schemas.Client.exceptions.UnauthorizedException
Schemas.Client.exceptions.InternalServerErrorException
Schemas.Client.exceptions.ForbiddenException
Schemas.Client.exceptions.NotFoundException
Schemas.Client.exceptions.ServiceUnavailableException


    :return: {
        'Description': 'string',
        'DiscovererArn': 'string',
        'DiscovererId': 'string',
        'SourceArn': 'string',
        'State': 'STARTED'|'STOPPED',
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    Schemas.Client.exceptions.BadRequestException
    Schemas.Client.exceptions.UnauthorizedException
    Schemas.Client.exceptions.InternalServerErrorException
    Schemas.Client.exceptions.ForbiddenException
    Schemas.Client.exceptions.NotFoundException
    Schemas.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def describe_registry(RegistryName=None):
    """
    Describes the registry.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_registry(
        RegistryName='string'
    )
    
    
    :type RegistryName: string
    :param RegistryName: [REQUIRED]\nThe name of the registry.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Description': 'string',
    'RegistryArn': 'string',
    'RegistryName': 'string',
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --200 response

Description (string) --The description of the registry.

RegistryArn (string) --The ARN of the registry.

RegistryName (string) --The name of the registry.

Tags (dict) --Tags associated with the registry.

(string) --
(string) --









Exceptions

Schemas.Client.exceptions.BadRequestException
Schemas.Client.exceptions.UnauthorizedException
Schemas.Client.exceptions.InternalServerErrorException
Schemas.Client.exceptions.ForbiddenException
Schemas.Client.exceptions.NotFoundException
Schemas.Client.exceptions.ServiceUnavailableException


    :return: {
        'Description': 'string',
        'RegistryArn': 'string',
        'RegistryName': 'string',
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    Schemas.Client.exceptions.BadRequestException
    Schemas.Client.exceptions.UnauthorizedException
    Schemas.Client.exceptions.InternalServerErrorException
    Schemas.Client.exceptions.ForbiddenException
    Schemas.Client.exceptions.NotFoundException
    Schemas.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def describe_schema(RegistryName=None, SchemaName=None, SchemaVersion=None):
    """
    Retrieve the schema definition.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_schema(
        RegistryName='string',
        SchemaName='string',
        SchemaVersion='string'
    )
    
    
    :type RegistryName: string
    :param RegistryName: [REQUIRED]\nThe name of the registry.\n

    :type SchemaName: string
    :param SchemaName: [REQUIRED]\nThe name of the schema.\n

    :type SchemaVersion: string
    :param SchemaVersion: Specifying this limits the results to only this schema version.

    :rtype: dict

ReturnsResponse Syntax
{
    'Content': 'string',
    'Description': 'string',
    'LastModified': datetime(2015, 1, 1),
    'SchemaArn': 'string',
    'SchemaName': 'string',
    'SchemaVersion': 'string',
    'Tags': {
        'string': 'string'
    },
    'Type': 'string',
    'VersionCreatedDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --
200 response

Content (string) --
The source of the schema definition.

Description (string) --
The description of the schema.

LastModified (datetime) --
The date and time that schema was modified.

SchemaArn (string) --
The ARN of the schema.

SchemaName (string) --
The name of the schema.

SchemaVersion (string) --
The version number of the schema

Tags (dict) --
Tags associated with the resource.

(string) --
(string) --




Type (string) --
The type of the schema.

VersionCreatedDate (datetime) --
The date the schema version was created.







Exceptions

Schemas.Client.exceptions.BadRequestException
Schemas.Client.exceptions.UnauthorizedException
Schemas.Client.exceptions.InternalServerErrorException
Schemas.Client.exceptions.ForbiddenException
Schemas.Client.exceptions.NotFoundException
Schemas.Client.exceptions.ServiceUnavailableException


    :return: {
        'Content': 'string',
        'Description': 'string',
        'LastModified': datetime(2015, 1, 1),
        'SchemaArn': 'string',
        'SchemaName': 'string',
        'SchemaVersion': 'string',
        'Tags': {
            'string': 'string'
        },
        'Type': 'string',
        'VersionCreatedDate': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
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

def get_code_binding_source(Language=None, RegistryName=None, SchemaName=None, SchemaVersion=None):
    """
    Get the code binding source URI.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_code_binding_source(
        Language='string',
        RegistryName='string',
        SchemaName='string',
        SchemaVersion='string'
    )
    
    
    :type Language: string
    :param Language: [REQUIRED]\nThe language of the code binding.\n

    :type RegistryName: string
    :param RegistryName: [REQUIRED]\nThe name of the registry.\n

    :type SchemaName: string
    :param SchemaName: [REQUIRED]\nThe name of the schema.\n

    :type SchemaVersion: string
    :param SchemaVersion: Specifying this limits the results to only this schema version.

    :rtype: dict

ReturnsResponse Syntax
{
    'Body': StreamingBody()
}


Response Structure

(dict) --
200 response

Body (StreamingBody) --






Exceptions

Schemas.Client.exceptions.BadRequestException
Schemas.Client.exceptions.UnauthorizedException
Schemas.Client.exceptions.InternalServerErrorException
Schemas.Client.exceptions.ForbiddenException
Schemas.Client.exceptions.NotFoundException
Schemas.Client.exceptions.TooManyRequestsException


    :return: {
        'Body': StreamingBody()
    }
    
    
    :returns: 
    Body (StreamingBody) --
    
    """
    pass

def get_discovered_schema(Events=None, Type=None):
    """
    Get the discovered schema that was generated based on sampled events.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_discovered_schema(
        Events=[
            'string',
        ],
        Type='OpenApi3'
    )
    
    
    :type Events: list
    :param Events: [REQUIRED]\nAn array of strings where each string is a JSON event. These are the events that were used to generate the schema. The array includes a single type of event and has a maximum size of 10 events.\n\n(string) --\n\n

    :type Type: string
    :param Type: [REQUIRED]\nThe type of event.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Content': 'string'
}


Response Structure

(dict) --
200 response

Content (string) --
The source of the schema definition.







Exceptions

Schemas.Client.exceptions.ServiceUnavailableException
Schemas.Client.exceptions.BadRequestException
Schemas.Client.exceptions.UnauthorizedException
Schemas.Client.exceptions.InternalServerErrorException
Schemas.Client.exceptions.ForbiddenException


    :return: {
        'Content': 'string'
    }
    
    
    :returns: 
    Schemas.Client.exceptions.ServiceUnavailableException
    Schemas.Client.exceptions.BadRequestException
    Schemas.Client.exceptions.UnauthorizedException
    Schemas.Client.exceptions.InternalServerErrorException
    Schemas.Client.exceptions.ForbiddenException
    
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

def get_resource_policy(RegistryName=None):
    """
    Retrieves the resource-based policy attached to a given registry.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_resource_policy(
        RegistryName='string'
    )
    
    
    :type RegistryName: string
    :param RegistryName: The name of the registry.

    :rtype: dict
ReturnsResponse Syntax{
    'Policy': 'string',
    'RevisionId': 'string'
}


Response Structure

(dict) --Get Resource-Based Policy Response

Policy (string) --The resource-based policy.

RevisionId (string) --The revision ID.






Exceptions

Schemas.Client.exceptions.BadRequestException
Schemas.Client.exceptions.UnauthorizedException
Schemas.Client.exceptions.InternalServerErrorException
Schemas.Client.exceptions.ForbiddenException
Schemas.Client.exceptions.NotFoundException
Schemas.Client.exceptions.ServiceUnavailableException


    :return: {
        'Policy': 'string',
        'RevisionId': 'string'
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

def list_discoverers(DiscovererIdPrefix=None, Limit=None, NextToken=None, SourceArnPrefix=None):
    """
    List the discoverers.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_discoverers(
        DiscovererIdPrefix='string',
        Limit=123,
        NextToken='string',
        SourceArnPrefix='string'
    )
    
    
    :type DiscovererIdPrefix: string
    :param DiscovererIdPrefix: Specifying this limits the results to only those discoverer IDs that start with the specified prefix.

    :type Limit: integer
    :param Limit: 

    :type NextToken: string
    :param NextToken: The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts.

    :type SourceArnPrefix: string
    :param SourceArnPrefix: Specifying this limits the results to only those ARNs that start with the specified prefix.

    :rtype: dict

ReturnsResponse Syntax
{
    'Discoverers': [
        {
            'DiscovererArn': 'string',
            'DiscovererId': 'string',
            'SourceArn': 'string',
            'State': 'STARTED'|'STOPPED',
            'Tags': {
                'string': 'string'
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
200 response

Discoverers (list) --
An array of DiscovererSummary information.

(dict) --

DiscovererArn (string) --
The ARN of the discoverer.

DiscovererId (string) --
The ID of the discoverer.

SourceArn (string) --
The ARN of the event bus.

State (string) --
The state of the discoverer.

Tags (dict) --
Tags associated with the resource.

(string) --
(string) --








NextToken (string) --
The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts.







Exceptions

Schemas.Client.exceptions.ServiceUnavailableException
Schemas.Client.exceptions.BadRequestException
Schemas.Client.exceptions.UnauthorizedException
Schemas.Client.exceptions.InternalServerErrorException
Schemas.Client.exceptions.ForbiddenException


    :return: {
        'Discoverers': [
            {
                'DiscovererArn': 'string',
                'DiscovererId': 'string',
                'SourceArn': 'string',
                'State': 'STARTED'|'STOPPED',
                'Tags': {
                    'string': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_registries(Limit=None, NextToken=None, RegistryNamePrefix=None, Scope=None):
    """
    List the registries.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_registries(
        Limit=123,
        NextToken='string',
        RegistryNamePrefix='string',
        Scope='string'
    )
    
    
    :type Limit: integer
    :param Limit: 

    :type NextToken: string
    :param NextToken: The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts.

    :type RegistryNamePrefix: string
    :param RegistryNamePrefix: Specifying this limits the results to only those registry names that start with the specified prefix.

    :type Scope: string
    :param Scope: Can be set to Local or AWS to limit responses to your custom registries, or the ones provided by AWS.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'Registries': [
        {
            'RegistryArn': 'string',
            'RegistryName': 'string',
            'Tags': {
                'string': 'string'
            }
        },
    ]
}


Response Structure

(dict) --
200 response

NextToken (string) --
The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts.

Registries (list) --
An array of registry summaries.

(dict) --

RegistryArn (string) --
The ARN of the registry.

RegistryName (string) --
The name of the registry.

Tags (dict) --
Tags associated with the registry.

(string) --
(string) --














Exceptions

Schemas.Client.exceptions.ServiceUnavailableException
Schemas.Client.exceptions.BadRequestException
Schemas.Client.exceptions.UnauthorizedException
Schemas.Client.exceptions.InternalServerErrorException
Schemas.Client.exceptions.ForbiddenException


    :return: {
        'NextToken': 'string',
        'Registries': [
            {
                'RegistryArn': 'string',
                'RegistryName': 'string',
                'Tags': {
                    'string': 'string'
                }
            },
        ]
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_schema_versions(Limit=None, NextToken=None, RegistryName=None, SchemaName=None):
    """
    Provides a list of the schema versions and related information.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_schema_versions(
        Limit=123,
        NextToken='string',
        RegistryName='string',
        SchemaName='string'
    )
    
    
    :type Limit: integer
    :param Limit: 

    :type NextToken: string
    :param NextToken: The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts.

    :type RegistryName: string
    :param RegistryName: [REQUIRED]\nThe name of the registry.\n

    :type SchemaName: string
    :param SchemaName: [REQUIRED]\nThe name of the schema.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'SchemaVersions': [
        {
            'SchemaArn': 'string',
            'SchemaName': 'string',
            'SchemaVersion': 'string'
        },
    ]
}


Response Structure

(dict) --
200 response

NextToken (string) --
The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts.

SchemaVersions (list) --
An array of schema version summaries.

(dict) --

SchemaArn (string) --
The ARN of the schema version.

SchemaName (string) --
The name of the schema.

SchemaVersion (string) --
The version number of the schema.











Exceptions

Schemas.Client.exceptions.BadRequestException
Schemas.Client.exceptions.UnauthorizedException
Schemas.Client.exceptions.InternalServerErrorException
Schemas.Client.exceptions.ForbiddenException
Schemas.Client.exceptions.NotFoundException
Schemas.Client.exceptions.ServiceUnavailableException


    :return: {
        'NextToken': 'string',
        'SchemaVersions': [
            {
                'SchemaArn': 'string',
                'SchemaName': 'string',
                'SchemaVersion': 'string'
            },
        ]
    }
    
    
    :returns: 
    Schemas.Client.exceptions.BadRequestException
    Schemas.Client.exceptions.UnauthorizedException
    Schemas.Client.exceptions.InternalServerErrorException
    Schemas.Client.exceptions.ForbiddenException
    Schemas.Client.exceptions.NotFoundException
    Schemas.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def list_schemas(Limit=None, NextToken=None, RegistryName=None, SchemaNamePrefix=None):
    """
    List the schemas.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_schemas(
        Limit=123,
        NextToken='string',
        RegistryName='string',
        SchemaNamePrefix='string'
    )
    
    
    :type Limit: integer
    :param Limit: 

    :type NextToken: string
    :param NextToken: The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts.

    :type RegistryName: string
    :param RegistryName: [REQUIRED]\nThe name of the registry.\n

    :type SchemaNamePrefix: string
    :param SchemaNamePrefix: Specifying this limits the results to only those schema names that start with the specified prefix.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'Schemas': [
        {
            'LastModified': datetime(2015, 1, 1),
            'SchemaArn': 'string',
            'SchemaName': 'string',
            'Tags': {
                'string': 'string'
            },
            'VersionCount': 123
        },
    ]
}


Response Structure

(dict) --
200 response

NextToken (string) --
The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts.

Schemas (list) --
An array of schema summaries.

(dict) --
A summary of schema details.

LastModified (datetime) --
The date and time that schema was modified.

SchemaArn (string) --
The ARN of the schema.

SchemaName (string) --
The name of the schema.

Tags (dict) --
Tags associated with the schema.

(string) --
(string) --




VersionCount (integer) --
The number of versions available for the schema.











Exceptions

Schemas.Client.exceptions.ServiceUnavailableException
Schemas.Client.exceptions.BadRequestException
Schemas.Client.exceptions.UnauthorizedException
Schemas.Client.exceptions.InternalServerErrorException
Schemas.Client.exceptions.ForbiddenException


    :return: {
        'NextToken': 'string',
        'Schemas': [
            {
                'LastModified': datetime(2015, 1, 1),
                'SchemaArn': 'string',
                'SchemaName': 'string',
                'Tags': {
                    'string': 'string'
                },
                'VersionCount': 123
            },
        ]
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_tags_for_resource(ResourceArn=None):
    """
    Get tags for resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe ARN of the resource.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --200 response

Tags (dict) --Key-value pairs associated with a resource.

(string) --
(string) --









Exceptions

Schemas.Client.exceptions.NotFoundException
Schemas.Client.exceptions.BadRequestException
Schemas.Client.exceptions.InternalServerErrorException
Schemas.Client.exceptions.ForbiddenException


    :return: {
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    Schemas.Client.exceptions.NotFoundException
    Schemas.Client.exceptions.BadRequestException
    Schemas.Client.exceptions.InternalServerErrorException
    Schemas.Client.exceptions.ForbiddenException
    
    """
    pass

def put_code_binding(Language=None, RegistryName=None, SchemaName=None, SchemaVersion=None):
    """
    Put code binding URI
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_code_binding(
        Language='string',
        RegistryName='string',
        SchemaName='string',
        SchemaVersion='string'
    )
    
    
    :type Language: string
    :param Language: [REQUIRED]\nThe language of the code binding.\n

    :type RegistryName: string
    :param RegistryName: [REQUIRED]\nThe name of the registry.\n

    :type SchemaName: string
    :param SchemaName: [REQUIRED]\nThe name of the schema.\n

    :type SchemaVersion: string
    :param SchemaVersion: Specifying this limits the results to only this schema version.

    :rtype: dict

ReturnsResponse Syntax
{
    'CreationDate': datetime(2015, 1, 1),
    'LastModified': datetime(2015, 1, 1),
    'SchemaVersion': 'string',
    'Status': 'CREATE_IN_PROGRESS'|'CREATE_COMPLETE'|'CREATE_FAILED'
}


Response Structure

(dict) --
202 response

CreationDate (datetime) --
The time and date that the code binding was created.

LastModified (datetime) --
The date and time that code bindings were modified.

SchemaVersion (string) --
The version number of the schema.

Status (string) --
The current status of code binding generation.







Exceptions

Schemas.Client.exceptions.GoneException
Schemas.Client.exceptions.BadRequestException
Schemas.Client.exceptions.UnauthorizedException
Schemas.Client.exceptions.InternalServerErrorException
Schemas.Client.exceptions.ForbiddenException
Schemas.Client.exceptions.NotFoundException
Schemas.Client.exceptions.TooManyRequestsException


    :return: {
        'CreationDate': datetime(2015, 1, 1),
        'LastModified': datetime(2015, 1, 1),
        'SchemaVersion': 'string',
        'Status': 'CREATE_IN_PROGRESS'|'CREATE_COMPLETE'|'CREATE_FAILED'
    }
    
    
    :returns: 
    Schemas.Client.exceptions.GoneException
    Schemas.Client.exceptions.BadRequestException
    Schemas.Client.exceptions.UnauthorizedException
    Schemas.Client.exceptions.InternalServerErrorException
    Schemas.Client.exceptions.ForbiddenException
    Schemas.Client.exceptions.NotFoundException
    Schemas.Client.exceptions.TooManyRequestsException
    
    """
    pass

def put_resource_policy(Policy=None, RegistryName=None, RevisionId=None):
    """
    The name of the policy.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_resource_policy(
        Policy='string',
        RegistryName='string',
        RevisionId='string'
    )
    
    
    :type Policy: string
    :param Policy: [REQUIRED]\nThe resource-based policy.\n

    :type RegistryName: string
    :param RegistryName: The name of the registry.

    :type RevisionId: string
    :param RevisionId: The revision ID of the policy.

    :rtype: dict

ReturnsResponse Syntax
{
    'Policy': 'string',
    'RevisionId': 'string'
}


Response Structure

(dict) --
200 response

Policy (string) --
The resource-based policy.

RevisionId (string) --
The revision ID of the policy.







Exceptions

Schemas.Client.exceptions.BadRequestException
Schemas.Client.exceptions.UnauthorizedException
Schemas.Client.exceptions.PreconditionFailedException
Schemas.Client.exceptions.InternalServerErrorException
Schemas.Client.exceptions.ForbiddenException
Schemas.Client.exceptions.NotFoundException
Schemas.Client.exceptions.ServiceUnavailableException


    :return: {
        'Policy': 'string',
        'RevisionId': 'string'
    }
    
    
    :returns: 
    Schemas.Client.exceptions.BadRequestException
    Schemas.Client.exceptions.UnauthorizedException
    Schemas.Client.exceptions.PreconditionFailedException
    Schemas.Client.exceptions.InternalServerErrorException
    Schemas.Client.exceptions.ForbiddenException
    Schemas.Client.exceptions.NotFoundException
    Schemas.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def search_schemas(Keywords=None, Limit=None, NextToken=None, RegistryName=None):
    """
    Search the schemas
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.search_schemas(
        Keywords='string',
        Limit=123,
        NextToken='string',
        RegistryName='string'
    )
    
    
    :type Keywords: string
    :param Keywords: [REQUIRED]\nSpecifying this limits the results to only schemas that include the provided keywords.\n

    :type Limit: integer
    :param Limit: 

    :type NextToken: string
    :param NextToken: The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts.

    :type RegistryName: string
    :param RegistryName: [REQUIRED]\nThe name of the registry.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'Schemas': [
        {
            'RegistryName': 'string',
            'SchemaArn': 'string',
            'SchemaName': 'string',
            'SchemaVersions': [
                {
                    'CreatedDate': datetime(2015, 1, 1),
                    'SchemaVersion': 'string'
                },
            ]
        },
    ]
}


Response Structure

(dict) --
200 response

NextToken (string) --
The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts.

Schemas (list) --
An array of SearchSchemaSummary information.

(dict) --

RegistryName (string) --
The name of the registry.

SchemaArn (string) --
The ARN of the schema.

SchemaName (string) --
The name of the schema.

SchemaVersions (list) --
An array of schema version summaries.

(dict) --

CreatedDate (datetime) --
The date the schema version was created.

SchemaVersion (string) --
The version number of the schema















Exceptions

Schemas.Client.exceptions.ServiceUnavailableException
Schemas.Client.exceptions.BadRequestException
Schemas.Client.exceptions.UnauthorizedException
Schemas.Client.exceptions.InternalServerErrorException
Schemas.Client.exceptions.ForbiddenException


    :return: {
        'NextToken': 'string',
        'Schemas': [
            {
                'RegistryName': 'string',
                'SchemaArn': 'string',
                'SchemaName': 'string',
                'SchemaVersions': [
                    {
                        'CreatedDate': datetime(2015, 1, 1),
                        'SchemaVersion': 'string'
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    Schemas.Client.exceptions.ServiceUnavailableException
    Schemas.Client.exceptions.BadRequestException
    Schemas.Client.exceptions.UnauthorizedException
    Schemas.Client.exceptions.InternalServerErrorException
    Schemas.Client.exceptions.ForbiddenException
    
    """
    pass

def start_discoverer(DiscovererId=None):
    """
    Starts the discoverer
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_discoverer(
        DiscovererId='string'
    )
    
    
    :type DiscovererId: string
    :param DiscovererId: [REQUIRED]\nThe ID of the discoverer.\n

    :rtype: dict
ReturnsResponse Syntax{
    'DiscovererId': 'string',
    'State': 'STARTED'|'STOPPED'
}


Response Structure

(dict) --200 response

DiscovererId (string) --The ID of the discoverer.

State (string) --The state of the discoverer.






Exceptions

Schemas.Client.exceptions.BadRequestException
Schemas.Client.exceptions.UnauthorizedException
Schemas.Client.exceptions.InternalServerErrorException
Schemas.Client.exceptions.ForbiddenException
Schemas.Client.exceptions.NotFoundException
Schemas.Client.exceptions.ServiceUnavailableException


    :return: {
        'DiscovererId': 'string',
        'State': 'STARTED'|'STOPPED'
    }
    
    
    """
    pass

def stop_discoverer(DiscovererId=None):
    """
    Stops the discoverer
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_discoverer(
        DiscovererId='string'
    )
    
    
    :type DiscovererId: string
    :param DiscovererId: [REQUIRED]\nThe ID of the discoverer.\n

    :rtype: dict
ReturnsResponse Syntax{
    'DiscovererId': 'string',
    'State': 'STARTED'|'STOPPED'
}


Response Structure

(dict) --200 response

DiscovererId (string) --The ID of the discoverer.

State (string) --The state of the discoverer.






Exceptions

Schemas.Client.exceptions.BadRequestException
Schemas.Client.exceptions.UnauthorizedException
Schemas.Client.exceptions.InternalServerErrorException
Schemas.Client.exceptions.ForbiddenException
Schemas.Client.exceptions.NotFoundException
Schemas.Client.exceptions.ServiceUnavailableException


    :return: {
        'DiscovererId': 'string',
        'State': 'STARTED'|'STOPPED'
    }
    
    
    """
    pass

def tag_resource(ResourceArn=None, Tags=None):
    """
    Add tags to a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceArn='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe ARN of the resource.\n

    :type Tags: dict
    :param Tags: [REQUIRED]\nTags associated with the resource.\n\n(string) --\n(string) --\n\n\n\n

    :returns: 
    Schemas.Client.exceptions.NotFoundException
    Schemas.Client.exceptions.BadRequestException
    Schemas.Client.exceptions.InternalServerErrorException
    Schemas.Client.exceptions.ForbiddenException
    
    """
    pass

def untag_resource(ResourceArn=None, TagKeys=None):
    """
    Removes tags from a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe ARN of the resource.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nKeys of key-value pairs.\n\n(string) --\n\n

    :returns: 
    Schemas.Client.exceptions.NotFoundException
    Schemas.Client.exceptions.BadRequestException
    Schemas.Client.exceptions.InternalServerErrorException
    Schemas.Client.exceptions.ForbiddenException
    
    """
    pass

def update_discoverer(Description=None, DiscovererId=None):
    """
    Updates the discoverer
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_discoverer(
        Description='string',
        DiscovererId='string'
    )
    
    
    :type Description: string
    :param Description: The description of the discoverer to update.

    :type DiscovererId: string
    :param DiscovererId: [REQUIRED]\nThe ID of the discoverer.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Description': 'string',
    'DiscovererArn': 'string',
    'DiscovererId': 'string',
    'SourceArn': 'string',
    'State': 'STARTED'|'STOPPED',
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
200 response

Description (string) --
The description of the discoverer.

DiscovererArn (string) --
The ARN of the discoverer.

DiscovererId (string) --
The ID of the discoverer.

SourceArn (string) --
The ARN of the event bus.

State (string) --
The state of the discoverer.

Tags (dict) --
Tags associated with the resource.

(string) --
(string) --










Exceptions

Schemas.Client.exceptions.BadRequestException
Schemas.Client.exceptions.UnauthorizedException
Schemas.Client.exceptions.InternalServerErrorException
Schemas.Client.exceptions.ForbiddenException
Schemas.Client.exceptions.NotFoundException
Schemas.Client.exceptions.ServiceUnavailableException


    :return: {
        'Description': 'string',
        'DiscovererArn': 'string',
        'DiscovererId': 'string',
        'SourceArn': 'string',
        'State': 'STARTED'|'STOPPED',
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def update_registry(Description=None, RegistryName=None):
    """
    Updates a registry.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_registry(
        Description='string',
        RegistryName='string'
    )
    
    
    :type Description: string
    :param Description: The description of the registry to update.

    :type RegistryName: string
    :param RegistryName: [REQUIRED]\nThe name of the registry.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Description': 'string',
    'RegistryArn': 'string',
    'RegistryName': 'string',
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
200 response

Description (string) --
The description of the registry.

RegistryArn (string) --
The ARN of the registry.

RegistryName (string) --
The name of the registry.

Tags (dict) --
Tags associated with the registry.

(string) --
(string) --










Exceptions

Schemas.Client.exceptions.BadRequestException
Schemas.Client.exceptions.UnauthorizedException
Schemas.Client.exceptions.InternalServerErrorException
Schemas.Client.exceptions.ForbiddenException
Schemas.Client.exceptions.NotFoundException
Schemas.Client.exceptions.ServiceUnavailableException


    :return: {
        'Description': 'string',
        'RegistryArn': 'string',
        'RegistryName': 'string',
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def update_schema(ClientTokenId=None, Content=None, Description=None, RegistryName=None, SchemaName=None, Type=None):
    """
    Updates the schema definition
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_schema(
        ClientTokenId='string',
        Content='string',
        Description='string',
        RegistryName='string',
        SchemaName='string',
        Type='OpenApi3'
    )
    
    
    :type ClientTokenId: string
    :param ClientTokenId: The ID of the client token.\nThis field is autopopulated if not provided.\n

    :type Content: string
    :param Content: The source of the schema definition.

    :type Description: string
    :param Description: The description of the schema.

    :type RegistryName: string
    :param RegistryName: [REQUIRED]\nThe name of the registry.\n

    :type SchemaName: string
    :param SchemaName: [REQUIRED]\nThe name of the schema.\n

    :type Type: string
    :param Type: The schema type for the events schema.

    :rtype: dict

ReturnsResponse Syntax
{
    'Description': 'string',
    'LastModified': datetime(2015, 1, 1),
    'SchemaArn': 'string',
    'SchemaName': 'string',
    'SchemaVersion': 'string',
    'Tags': {
        'string': 'string'
    },
    'Type': 'string',
    'VersionCreatedDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --
200 response

Description (string) --
The description of the schema.

LastModified (datetime) --
The date and time that schema was modified.

SchemaArn (string) --
The ARN of the schema.

SchemaName (string) --
The name of the schema.

SchemaVersion (string) --
The version number of the schema

Tags (dict) --
Key-value pairs associated with a resource.

(string) --
(string) --




Type (string) --
The type of the schema.

VersionCreatedDate (datetime) --
The date the schema version was created.







Exceptions

Schemas.Client.exceptions.BadRequestException
Schemas.Client.exceptions.InternalServerErrorException
Schemas.Client.exceptions.ForbiddenException
Schemas.Client.exceptions.NotFoundException
Schemas.Client.exceptions.ServiceUnavailableException


    :return: {
        'Description': 'string',
        'LastModified': datetime(2015, 1, 1),
        'SchemaArn': 'string',
        'SchemaName': 'string',
        'SchemaVersion': 'string',
        'Tags': {
            'string': 'string'
        },
        'Type': 'string',
        'VersionCreatedDate': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

