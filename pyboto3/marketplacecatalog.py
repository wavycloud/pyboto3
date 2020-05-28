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

def cancel_change_set(Catalog=None, ChangeSetId=None):
    """
    Used to cancel an open change request. Must be sent before the status of the request changes to APPLYING , the final stage of completing your change request. You can describe a change during the 60-day request history retention period for API calls.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.cancel_change_set(
        Catalog='string',
        ChangeSetId='string'
    )
    
    
    :type Catalog: string
    :param Catalog: [REQUIRED]\nRequired. The catalog related to the request. Fixed value: AWSMarketplace .\n

    :type ChangeSetId: string
    :param ChangeSetId: [REQUIRED]\nRequired. The unique identifier of the StartChangeSet request that you want to cancel.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChangeSetId': 'string',
    'ChangeSetArn': 'string'
}


Response Structure

(dict) --

ChangeSetId (string) --
The unique identifier for the change set referenced in this request.

ChangeSetArn (string) --
The ARN associated with the change set referenced in this request.







Exceptions

MarketplaceCatalog.Client.exceptions.InternalServiceException
MarketplaceCatalog.Client.exceptions.AccessDeniedException
MarketplaceCatalog.Client.exceptions.ValidationException
MarketplaceCatalog.Client.exceptions.ResourceNotFoundException
MarketplaceCatalog.Client.exceptions.ResourceInUseException
MarketplaceCatalog.Client.exceptions.ThrottlingException


    :return: {
        'ChangeSetId': 'string',
        'ChangeSetArn': 'string'
    }
    
    
    :returns: 
    MarketplaceCatalog.Client.exceptions.InternalServiceException
    MarketplaceCatalog.Client.exceptions.AccessDeniedException
    MarketplaceCatalog.Client.exceptions.ValidationException
    MarketplaceCatalog.Client.exceptions.ResourceNotFoundException
    MarketplaceCatalog.Client.exceptions.ResourceInUseException
    MarketplaceCatalog.Client.exceptions.ThrottlingException
    
    """
    pass

def describe_change_set(Catalog=None, ChangeSetId=None):
    """
    Provides information about a given change set.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_change_set(
        Catalog='string',
        ChangeSetId='string'
    )
    
    
    :type Catalog: string
    :param Catalog: [REQUIRED]\nRequired. The catalog related to the request. Fixed value: AWSMarketplace\n

    :type ChangeSetId: string
    :param ChangeSetId: [REQUIRED]\nRequired. The unique identifier for the StartChangeSet request that you want to describe the details for.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChangeSetId': 'string',
    'ChangeSetArn': 'string',
    'ChangeSetName': 'string',
    'StartTime': 'string',
    'EndTime': 'string',
    'Status': 'PREPARING'|'APPLYING'|'SUCCEEDED'|'CANCELLED'|'FAILED',
    'FailureDescription': 'string',
    'ChangeSet': [
        {
            'ChangeType': 'string',
            'Entity': {
                'Type': 'string',
                'Identifier': 'string'
            },
            'ErrorDetailList': [
                {
                    'ErrorCode': 'string',
                    'ErrorMessage': 'string'
                },
            ]
        },
    ]
}


Response Structure

(dict) --

ChangeSetId (string) --
Required. The unique identifier for the change set referenced in this request.

ChangeSetArn (string) --
The ARN associated with the unique identifier for the change set referenced in this request.

ChangeSetName (string) --
The optional name provided in the StartChangeSet request. If you do not provide a name, one is set by default.

StartTime (string) --
The date and time, in ISO 8601 format (2018-02-27T13:45:22Z), the request started.

EndTime (string) --
The date and time, in ISO 8601 format (2018-02-27T13:45:22Z), the request transitioned to a terminal state. The change cannot transition to a different state. Null if the request is not in a terminal state.

Status (string) --
The status of the change request.

FailureDescription (string) --
Returned if there is a failure on the change set, but that failure is not related to any of the changes in the request.

ChangeSet (list) --
An array of ChangeSummary objects.

(dict) --
This object is a container for common summary information about the change. The summary doesn\'t contain the whole change structure.

ChangeType (string) --
The type of the change.

Entity (dict) --
The entity to be changed.

Type (string) --
The type of entity.

Identifier (string) --
The identifier for the entity.



ErrorDetailList (list) --
An array of ErrorDetail objects associated with the change.

(dict) --
Details about the error.

ErrorCode (string) --
The error code that identifies the type of error.

ErrorMessage (string) --
The message for the error.















Exceptions

MarketplaceCatalog.Client.exceptions.InternalServiceException
MarketplaceCatalog.Client.exceptions.AccessDeniedException
MarketplaceCatalog.Client.exceptions.ValidationException
MarketplaceCatalog.Client.exceptions.ResourceNotFoundException
MarketplaceCatalog.Client.exceptions.ThrottlingException


    :return: {
        'ChangeSetId': 'string',
        'ChangeSetArn': 'string',
        'ChangeSetName': 'string',
        'StartTime': 'string',
        'EndTime': 'string',
        'Status': 'PREPARING'|'APPLYING'|'SUCCEEDED'|'CANCELLED'|'FAILED',
        'FailureDescription': 'string',
        'ChangeSet': [
            {
                'ChangeType': 'string',
                'Entity': {
                    'Type': 'string',
                    'Identifier': 'string'
                },
                'ErrorDetailList': [
                    {
                        'ErrorCode': 'string',
                        'ErrorMessage': 'string'
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    MarketplaceCatalog.Client.exceptions.InternalServiceException
    MarketplaceCatalog.Client.exceptions.AccessDeniedException
    MarketplaceCatalog.Client.exceptions.ValidationException
    MarketplaceCatalog.Client.exceptions.ResourceNotFoundException
    MarketplaceCatalog.Client.exceptions.ThrottlingException
    
    """
    pass

def describe_entity(Catalog=None, EntityId=None):
    """
    Returns the metadata and content of the entity.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_entity(
        Catalog='string',
        EntityId='string'
    )
    
    
    :type Catalog: string
    :param Catalog: [REQUIRED]\nRequired. The catalog related to the request. Fixed value: AWSMarketplace\n

    :type EntityId: string
    :param EntityId: [REQUIRED]\nRequired. The unique ID of the entity to describe.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'EntityType': 'string',
    'EntityIdentifier': 'string',
    'EntityArn': 'string',
    'LastModifiedDate': 'string',
    'Details': 'string'
}


Response Structure

(dict) --

EntityType (string) --
The named type of the entity, in the format of EntityType@Version .

EntityIdentifier (string) --
The identifier of the entity, in the format of EntityId@RevisionId .

EntityArn (string) --
The ARN associated to the unique identifier for the change set referenced in this request.

LastModifiedDate (string) --
The last modified date of the entity, in ISO 8601 format (2018-02-27T13:45:22Z).

Details (string) --
This stringified JSON object includes the details of the entity.







Exceptions

MarketplaceCatalog.Client.exceptions.InternalServiceException
MarketplaceCatalog.Client.exceptions.AccessDeniedException
MarketplaceCatalog.Client.exceptions.ValidationException
MarketplaceCatalog.Client.exceptions.ResourceNotSupportedException
MarketplaceCatalog.Client.exceptions.ResourceNotFoundException
MarketplaceCatalog.Client.exceptions.ThrottlingException


    :return: {
        'EntityType': 'string',
        'EntityIdentifier': 'string',
        'EntityArn': 'string',
        'LastModifiedDate': 'string',
        'Details': 'string'
    }
    
    
    :returns: 
    MarketplaceCatalog.Client.exceptions.InternalServiceException
    MarketplaceCatalog.Client.exceptions.AccessDeniedException
    MarketplaceCatalog.Client.exceptions.ValidationException
    MarketplaceCatalog.Client.exceptions.ResourceNotSupportedException
    MarketplaceCatalog.Client.exceptions.ResourceNotFoundException
    MarketplaceCatalog.Client.exceptions.ThrottlingException
    
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

def list_change_sets(Catalog=None, FilterList=None, Sort=None, MaxResults=None, NextToken=None):
    """
    Returns the list of change sets owned by the account being used to make the call. You can filter this list by providing any combination of entityId , ChangeSetName , and status. If you provide more than one filter, the API operation applies a logical AND between the filters.
    You can describe a change during the 60-day request history retention period for API calls.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_change_sets(
        Catalog='string',
        FilterList=[
            {
                'Name': 'string',
                'ValueList': [
                    'string',
                ]
            },
        ],
        Sort={
            'SortBy': 'string',
            'SortOrder': 'ASCENDING'|'DESCENDING'
        },
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type Catalog: string
    :param Catalog: [REQUIRED]\nThe catalog related to the request. Fixed value: AWSMarketplace\n

    :type FilterList: list
    :param FilterList: An array of filter objects.\n\n(dict) --A filter object, used to optionally filter results from calls to the ListEntities and ListChangeSets actions.\n\nName (string) --For ListEntities , the supported value for this is an EntityId .\nFor ListChangeSets , the supported values are as follows:\n\nValueList (list) --\nListEntities - This is a list of unique EntityId s.ListChangeSets - The supported filter names and associated ValueList s is as follows:\n\n\nChangeSetName - The supported ValueList is a list of non-unique ChangeSetName s. These are defined when you call the StartChangeSet action.\nStatus - The supported ValueList is a list of statuses for all change set requests.\nEntityId - The supported ValueList is a list of unique EntityId s.\nBeforeStartTime - The supported ValueList is a list of all change sets that started before the filter value.\nAfterStartTime - The supported ValueList is a list of all change sets that started after the filter value.\nBeforeEndTime - The supported ValueList is a list of all change sets that ended before the filter value.\nAfterEndTime - The supported ValueList is a list of all change sets that ended after the filter value.\n\n\n(string) --\n\n\n\n\n\n

    :type Sort: dict
    :param Sort: An object that contains two attributes, sortBy and sortOrder .\n\nSortBy (string) --For ListEntities , supported attributes include LastModifiedDate (default), Visibility , EntityId , and Name .\nFor ListChangeSets , supported attributes include StartTime and EndTime .\n\nSortOrder (string) --The sorting order. Can be ASCENDING or DESCENDING . The default value is DESCENDING .\n\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of results returned by a single call. This value must be provided in the next call to retrieve the next set of results. By default, this value is 20.

    :type NextToken: string
    :param NextToken: The token value retrieved from a previous call to access the next page of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'ChangeSetSummaryList': [
        {
            'ChangeSetId': 'string',
            'ChangeSetArn': 'string',
            'ChangeSetName': 'string',
            'StartTime': 'string',
            'EndTime': 'string',
            'Status': 'PREPARING'|'APPLYING'|'SUCCEEDED'|'CANCELLED'|'FAILED',
            'EntityIdList': [
                'string',
            ]
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ChangeSetSummaryList (list) --
Array of ChangeSetSummaryListItem objects.

(dict) --
A summary of a change set returned in a list of change sets when the ListChangeSets action is called.

ChangeSetId (string) --
The unique identifier for a change set.

ChangeSetArn (string) --
The ARN associated with the unique identifier for the change set referenced in this request.

ChangeSetName (string) --
The non-unique name for the change set.

StartTime (string) --
The time, in ISO 8601 format (2018-02-27T13:45:22Z), when the change set was started.

EndTime (string) --
The time, in ISO 8601 format (2018-02-27T13:45:22Z), when the change set was finished.

Status (string) --
The current status of the change set.

EntityIdList (list) --
This object is a list of entity IDs (string) that are a part of a change set. The entity ID list is a maximum of 20 entities. It must contain at least one entity.

(string) --






NextToken (string) --
The value of the next token, if it exists. Null if there are no more results.







Exceptions

MarketplaceCatalog.Client.exceptions.InternalServiceException
MarketplaceCatalog.Client.exceptions.AccessDeniedException
MarketplaceCatalog.Client.exceptions.ValidationException
MarketplaceCatalog.Client.exceptions.ThrottlingException


    :return: {
        'ChangeSetSummaryList': [
            {
                'ChangeSetId': 'string',
                'ChangeSetArn': 'string',
                'ChangeSetName': 'string',
                'StartTime': 'string',
                'EndTime': 'string',
                'Status': 'PREPARING'|'APPLYING'|'SUCCEEDED'|'CANCELLED'|'FAILED',
                'EntityIdList': [
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

def list_entities(Catalog=None, EntityType=None, FilterList=None, Sort=None, NextToken=None, MaxResults=None):
    """
    Provides the list of entities of a given type.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_entities(
        Catalog='string',
        EntityType='string',
        FilterList=[
            {
                'Name': 'string',
                'ValueList': [
                    'string',
                ]
            },
        ],
        Sort={
            'SortBy': 'string',
            'SortOrder': 'ASCENDING'|'DESCENDING'
        },
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Catalog: string
    :param Catalog: [REQUIRED]\nThe catalog related to the request. Fixed value: AWSMarketplace\n

    :type EntityType: string
    :param EntityType: [REQUIRED]\nThe type of entities to retrieve.\n

    :type FilterList: list
    :param FilterList: An array of filter objects. Each filter object contains two attributes, filterName and filterValues .\n\n(dict) --A filter object, used to optionally filter results from calls to the ListEntities and ListChangeSets actions.\n\nName (string) --For ListEntities , the supported value for this is an EntityId .\nFor ListChangeSets , the supported values are as follows:\n\nValueList (list) --\nListEntities - This is a list of unique EntityId s.ListChangeSets - The supported filter names and associated ValueList s is as follows:\n\n\nChangeSetName - The supported ValueList is a list of non-unique ChangeSetName s. These are defined when you call the StartChangeSet action.\nStatus - The supported ValueList is a list of statuses for all change set requests.\nEntityId - The supported ValueList is a list of unique EntityId s.\nBeforeStartTime - The supported ValueList is a list of all change sets that started before the filter value.\nAfterStartTime - The supported ValueList is a list of all change sets that started after the filter value.\nBeforeEndTime - The supported ValueList is a list of all change sets that ended before the filter value.\nAfterEndTime - The supported ValueList is a list of all change sets that ended after the filter value.\n\n\n(string) --\n\n\n\n\n\n

    :type Sort: dict
    :param Sort: An object that contains two attributes, sortBy and sortOrder .\n\nSortBy (string) --For ListEntities , supported attributes include LastModifiedDate (default), Visibility , EntityId , and Name .\nFor ListChangeSets , supported attributes include StartTime and EndTime .\n\nSortOrder (string) --The sorting order. Can be ASCENDING or DESCENDING . The default value is DESCENDING .\n\n\n

    :type NextToken: string
    :param NextToken: The value of the next token, if it exists. Null if there are no more results.

    :type MaxResults: integer
    :param MaxResults: Specifies the upper limit of the elements on a single page. If a value isn\'t provided, the default value is 20.

    :rtype: dict

ReturnsResponse Syntax
{
    'EntitySummaryList': [
        {
            'Name': 'string',
            'EntityType': 'string',
            'EntityId': 'string',
            'EntityArn': 'string',
            'LastModifiedDate': 'string',
            'Visibility': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

EntitySummaryList (list) --
Array of EntitySummary object.

(dict) --
This object is a container for common summary information about the entity. The summary doesn\'t contain the whole entity structure, but it does contain information common across all entities.

Name (string) --
The name for the entity. This value is not unique. It is defined by the provider.

EntityType (string) --
The type of the entity.

EntityId (string) --
The unique identifier for the entity.

EntityArn (string) --
The ARN associated with the unique identifier for the entity.

LastModifiedDate (string) --
The last time the entity was published, using ISO 8601 format (2018-02-27T13:45:22Z).

Visibility (string) --
The visibility status of the entity to subscribers. This value can be Public (everyone can view the entity), Limited (the entity is visible to limited accounts only), or Restricted (the entity was published and then unpublished and only existing subscribers can view it).





NextToken (string) --
The value of the next token if it exists. Null if there is no more result.







Exceptions

MarketplaceCatalog.Client.exceptions.InternalServiceException
MarketplaceCatalog.Client.exceptions.AccessDeniedException
MarketplaceCatalog.Client.exceptions.ValidationException
MarketplaceCatalog.Client.exceptions.ResourceNotFoundException
MarketplaceCatalog.Client.exceptions.ThrottlingException


    :return: {
        'EntitySummaryList': [
            {
                'Name': 'string',
                'EntityType': 'string',
                'EntityId': 'string',
                'EntityArn': 'string',
                'LastModifiedDate': 'string',
                'Visibility': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    MarketplaceCatalog.Client.exceptions.InternalServiceException
    MarketplaceCatalog.Client.exceptions.AccessDeniedException
    MarketplaceCatalog.Client.exceptions.ValidationException
    MarketplaceCatalog.Client.exceptions.ResourceNotFoundException
    MarketplaceCatalog.Client.exceptions.ThrottlingException
    
    """
    pass

def start_change_set(Catalog=None, ChangeSet=None, ChangeSetName=None, ClientRequestToken=None):
    """
    This operation allows you to request changes in your entities.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_change_set(
        Catalog='string',
        ChangeSet=[
            {
                'ChangeType': 'string',
                'Entity': {
                    'Type': 'string',
                    'Identifier': 'string'
                },
                'Details': 'string'
            },
        ],
        ChangeSetName='string',
        ClientRequestToken='string'
    )
    
    
    :type Catalog: string
    :param Catalog: [REQUIRED]\nThe catalog related to the request. Fixed value: AWSMarketplace\n

    :type ChangeSet: list
    :param ChangeSet: [REQUIRED]\nArray of change object.\n\n(dict) --An object that contains the ChangeType , Details , and Entity .\n\nChangeType (string) -- [REQUIRED]Change types are single string values that describe your intention for the change. Each change type is unique for each EntityType provided in the change\'s scope.\n\nEntity (dict) -- [REQUIRED]The entity to be changed.\n\nType (string) -- [REQUIRED]The type of entity.\n\nIdentifier (string) --The identifier for the entity.\n\n\n\nDetails (string) -- [REQUIRED]This object contains details specific to the change type of the requested change.\n\n\n\n\n

    :type ChangeSetName: string
    :param ChangeSetName: Optional case sensitive string of up to 100 ASCII characters. The change set name can be used to filter the list of change sets.

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique token to identify the request to ensure idempotency.

    :rtype: dict

ReturnsResponse Syntax
{
    'ChangeSetId': 'string',
    'ChangeSetArn': 'string'
}


Response Structure

(dict) --

ChangeSetId (string) --
Unique identifier generated for the request.

ChangeSetArn (string) --
The ARN associated to the unique identifier generated for the request.







Exceptions

MarketplaceCatalog.Client.exceptions.InternalServiceException
MarketplaceCatalog.Client.exceptions.AccessDeniedException
MarketplaceCatalog.Client.exceptions.ValidationException
MarketplaceCatalog.Client.exceptions.ResourceNotFoundException
MarketplaceCatalog.Client.exceptions.ResourceInUseException
MarketplaceCatalog.Client.exceptions.ThrottlingException
MarketplaceCatalog.Client.exceptions.ServiceQuotaExceededException


    :return: {
        'ChangeSetId': 'string',
        'ChangeSetArn': 'string'
    }
    
    
    :returns: 
    MarketplaceCatalog.Client.exceptions.InternalServiceException
    MarketplaceCatalog.Client.exceptions.AccessDeniedException
    MarketplaceCatalog.Client.exceptions.ValidationException
    MarketplaceCatalog.Client.exceptions.ResourceNotFoundException
    MarketplaceCatalog.Client.exceptions.ResourceInUseException
    MarketplaceCatalog.Client.exceptions.ThrottlingException
    MarketplaceCatalog.Client.exceptions.ServiceQuotaExceededException
    
    """
    pass

